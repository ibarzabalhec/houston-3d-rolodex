# -*- coding: utf-8 -*-
"""Is the name actually on the page the card cites for it?

The audit round found four people published as a firm's construction contact who
were not on the firm's own team page, and one who had been dead for a decade. It
found them by sampling: an agent read a card, opened a page, and noticed. That
catches what it happens to look at.

This does not sample. For every contact on the deck with a non-LinkedIn source,
it fetches the raw HTML of that page and asks one question with a yes or no
answer: does the person's name appear in it? No model reads the page. No
summary is involved. The bytes either contain the surname next to the forename
or they do not.

That matters because a model reading a page is exactly how the worst error in
this repository got made. An audit pass reported a Wan Bridge construction vice
president, a fetch of his bio URL returned a profile saying so, and the URL was a
404 the whole time. A fetch that reads a page is not evidence the page exists,
and a page that renders is not evidence the name is on it.

    python3 probe.py                every contact with a fetchable source
    python3 probe.py --titles       also check the title words, not only the name

MISSING is the finding. REVIEW means the page could not be read and nothing is
claimed either way: a host that refuses scripts, a JavaScript team page that
ships no names in its HTML, a PDF. Those need a human with a browser.
"""
import html as _html
import json, pathlib, re, ssl, sys, urllib.error, urllib.request
import concurrent.futures as cf
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "internal" / "probe.json"

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,*/*"}
CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")

SKIP_HOST = {"linkedin.com", "www.linkedin.com"}
# Common first-name spellings that differ between a bio page and a directory.
NICK = {"mike": "michael", "jim": "james", "bob": "robert", "bill": "william",
        "tom": "thomas", "dan": "daniel", "dave": "david", "chris": "christopher",
        "steve": "stephen", "greg": "gregory", "ed": "edward", "eddie": "edward",
        "rick": "richard", "rich": "richard", "tony": "anthony", "joe": "joseph",
        "matt": "matthew", "nick": "nicholas", "ben": "benjamin", "sam": "samuel",
        "andy": "andrew", "ken": "kenneth", "ron": "ronald", "doug": "douglas",
        "jeff": "jeffrey", "pat": "patrick", "alex": "alexander", "kathy": "katherine"}


def text_of(body):
    """Everything a reader could see, plus the markup's own attribute values.

    A name can live in an alt attribute, a JSON-LD block or a data attribute and
    never appear as visible text. All of it counts as the name being on the page.
    """
    s = body.decode("utf-8", "replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = _html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"[^a-z0-9]+", " ", s.lower())


def raw_of(body):
    """The same bytes with markup kept, for names that sit only in attributes."""
    s = body.decode("utf-8", "replace")
    return re.sub(r"[^a-z0-9]+", " ", _html.unescape(s).lower())


def parts(name):
    w = [p for p in re.sub(r"[^A-Za-z \-']", " ", name).split() if len(p) > 1]
    w = [p.lower().strip("-'") for p in w]
    w = [p for p in w if p not in ("jr", "sr", "ii", "iii", "iv", "p", "e")]
    return w


def hit(name, text, raw):
    """A surname alone is not a hit. A forename alone is not a hit."""
    w = parts(name)
    if not w:
        return None
    first, last = w[0], w[-1]
    cands = {first}
    if first in NICK:
        cands.add(NICK[first])
    for k, v in NICK.items():
        if v == first:
            cands.add(k)
    for blob in (text, raw):
        if (" %s " % last) not in blob:
            continue
        if any((" %s " % c) in blob for c in cands):
            return True
    return False


def fetch(url):
    try:
        with urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=30, context=CTX) as r:
            ct = (r.headers.get("Content-Type") or "").lower()
            if "html" not in ct and "xml" not in ct and "text" not in ct:
                return None, "not html (%s)" % ct.split(";")[0]
            body = r.read(3_000_000)
            # A bot challenge answers 200 or 202 with a stub. Burton Construction
            # returns 182 bytes to a script and a full leadership roster to a
            # browser, and the first version of this probe called a real person
            # missing because of it. Anything this small is not a page.
            if len(body) < 2000:
                return None, "stub of %d bytes, a bot challenge" % len(body)
            return body, None
    except urllib.error.HTTPError as e:
        return None, "http %s" % e.code
    except Exception as e:
        return None, type(e).__name__


def main():
    d = json.load(open(ROOT / "houston-data.json", encoding="utf-8"))
    want_titles = "--titles" in sys.argv

    jobs = {}
    for t in d["targets"]:
        for p in t["principals"]:
            u = p.get("source_url") or t.get("team_url")
            if not u or urlparse(u).netloc.lower() in SKIP_HOST:
                continue
            jobs.setdefault(u, []).append((t["short"], p["name"], p.get("role", ""),
                                           bool(p.get("decider"))))

    print("probing %d pages for %d contacts\n"
          % (len(jobs), sum(len(v) for v in jobs.values())))

    missing, review, ok, title_off = [], [], 0, []

    def run(u):
        body, err = fetch(u)
        return u, body, err

    with cf.ThreadPoolExecutor(16) as ex:
        for u, body, err in ex.map(run, sorted(jobs)):
            if err:
                for firm, nm, role, dec in jobs[u]:
                    review.append((firm, nm, dec, u, err))
                continue
            text, raw = text_of(body), raw_of(body)
            # A page that ships no names at all is a rendering problem, not a
            # finding: say so once rather than accusing everyone on it.
            found = [hit(nm, text, raw) for _f, nm, _r, _d in jobs[u]]
            # A team page that ships its names from JavaScript arrives here as a
            # few hundred words of chrome. DSLD's about page and Smith Douglas's
            # acquisition post both do this, and both looked like findings.
            if len(text.split()) < 400 and not any(found):
                for firm, nm, role, dec in jobs[u]:
                    review.append((firm, nm, dec, u,
                                   "%d words, the page renders from script" % len(text.split())))
                continue
            if len(found) > 1 and not any(found):
                for firm, nm, role, dec in jobs[u]:
                    review.append((firm, nm, dec, u, "no name on the page renders"))
                continue
            for (firm, nm, role, dec), f in zip(jobs[u], found):
                if f:
                    ok += 1
                    if want_titles and role:
                        words = [w for w in re.findall(r"[a-z]{4,}", role.lower())
                                 if w not in ("and", "the", "for", "vice", "homes")]
                        miss = [w for w in words if (" %s " % w) not in text]
                        if words and len(miss) > len(words) / 2:
                            title_off.append((firm, nm, role, u))
                else:
                    missing.append((firm, nm, dec, u))

    print("MISSING, the name is not in the page cited for it: %d" % len(missing))
    for firm, nm, dec, u in sorted(missing, key=lambda x: (not x[2], x[0])):
        print("  %s%-30s %-26s" % ("* " if dec else "  ", firm[:30], nm[:26]))
        print("      %s" % u)
    if want_titles and title_off:
        print("\nTITLE NOT ON THE PAGE, the name is: %d" % len(title_off))
        for firm, nm, role, u in title_off:
            print("  %-28s %-24s %s" % (firm[:28], nm[:24], role[:46]))
            print("      %s" % u)
    print("\nnot claimed either way, the page could not be read: %d" % len(review))
    seen = set()
    for firm, nm, dec, u, why in review:
        if (u, why) in seen:
            continue
        seen.add((u, why))
        print("  %-24s %-34s %s" % (why[:24], firm[:34], u))
    print("\nname found on the cited page: %d" % ok)
    print("* marks a contact flagged as the person who can change a wall spec")

    OUT.parent.mkdir(exist_ok=True)
    json.dump({"missing": missing, "review": [list(r) for r in review], "ok": ok},
              open(OUT, "w"), indent=1)
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
