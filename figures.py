# -*- coding: utf-8 -*-
"""Is the number on any page the card cites for it?

probe.py asks that question about names. This asks it about figures, which is
the other place a model invents things and the harder one to catch by reading,
because a wrong number looks exactly like a right one.

Four inventions were found by hand in one audit round, each of which had
survived every earlier read: a build-to-rent operator credited with "156 units
inside a single masterplan" when no source anywhere carries that number, a
builder with a catalogue of "eighty-two plans" that neither cited page states, a
firm with "195 closings in 2022, the latest published" whose only source
publishes no annual figure at all, and a builder selling across "more than twenty
communities" whose own communities page lists fourteen.

This tests all of them at once. For every card, take every figure it prints,
fetch every page it cites, and ask whether the figure is in the bytes. A figure
on none of its own card's pages is one of three things, and all three are
findings:

  invented   nothing published it and the card asserts it
  derived    the card did arithmetic and presented the result as published
  uncited    a real figure whose source is not on the card, so no reader can
             follow it

The script cannot tell those apart. A person reading the card and the page can,
in about thirty seconds, which is the point: it turns an unbounded re-read into
a short list.

    python3 figures.py              every card
    python3 figures.py HOU-011      one card

What it deliberately does not flag: years, ordinals under 13, and anything the
card already labels as an assumption. Years are noise because every page is full
of them. Small integers are noise because "three communities" matches any page
with a three on it.
"""
import html as _html
import json, pathlib, re, ssl, sys, urllib.error, urllib.request
import concurrent.futures as cf

ROOT = pathlib.Path(__file__).parent
CACHE = ROOT / "internal" / "figures_pages.json"

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,*/*"}
CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")

SKIP_HOST = ("linkedin.com",)

# A figure this size is in every page on the web. Below the floor it is noise.
FLOOR = 13
# Years are on every page ever published.
YEAR = re.compile(r"^(19|20)\d\d$")

NUM = re.compile(r"""
    \$?                          # optional currency
    \d{1,3}(?:,\d{3})+           # 1,234 or 1,234,567
  | \$?\d+(?:\.\d+)?\s*(?:million|billion|percent|%)   # 4.7 million, 17 percent
  | \$?\d{2,}                    # bare integer of two digits or more
""", re.X | re.I)

# Numbers the deck writes as words, which a page may write as digits.
WORDS = {
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "twenty-one": 21, "twenty-two": 22, "twenty-three": 23, "twenty-four": 24,
    "twenty-five": 25, "twenty-six": 26, "twenty-eight": 28, "thirty": 30,
    "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "seventy-five": 75,
    "eighty": 80, "eighty-two": 82, "ninety": 90, "hundred": 100,
}


def flatten(body):
    s = body.decode("utf-8", "replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = _html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"\s+", " ", s)


# Pages that answer a script 403 and a browser the full page, read by hand, with
# the figures that were on them. Without this the five Builder firm pages added
# in Build 60 read as unfetchable, so every closing figure on those cards kept
# counting as unsourced after it had been sourced. A page here is treated as read
# and its text is the text below, which is deliberately only the figures: this is
# a record of what was checked, not a cache of the page.
BYHAND = {
    "https://www.builderonline.com/firms/westin-homes/":
        "2026-09-14: Westin Homes, Sugar Land TX. 2025 closings 1,062, revenue "
        "$621 M, Builder 100 rank 60. 2024 closings 1,016, revenue $625 M, rank 67.",
    "https://www.builderonline.com/firms/colina-homes/":
        "2026-09-14: Colina Homes, Houston TX. 2025 closings 540, revenue $84 M, "
        "rank 96. 2024 closings 552, revenue $129 M, rank 97.",
    "https://www.builderonline.com/firms/sitterle-homes/":
        "2026-09-14: Sitterle Homes, San Antonio TX. 2022 closings 372, revenue "
        "$210 M. 2021 closings 323, revenue $185 M. 2022 is the last year carried, "
        "and the page does not mention Houston.",
    "https://www.builderonline.com/builder-100/builder-100-list/2026/":
        "2026-09-14: 2026 The Top 100. First America Homes at rank 75, 750 "
        "closings, $197 million, for 2025.",
    "https://www.builderonline.com/firms/castlerock-communities/":
        "2026-09-14: CastleRock Communities, Houston TX. 2025 closings 1,465, "
        "revenue $617 M, rank 49. 2024 closings 1,465, revenue $645 M, rank 48. "
        "No cumulative homes or communities count on the page.",
}


def fetch(url):
    if url in BYHAND:
        return flatten(BYHAND[url].encode("utf-8"))
    try:
        with urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=30, context=CTX) as r:
            ct = (r.headers.get("Content-Type") or "").lower()
            if not any(k in ct for k in ("html", "xml", "text")):
                return None
            body = r.read(3_000_000)
            if len(body) < 2000:
                return None
            return flatten(body)
    except Exception:
        return None


def variants(tok):
    """Every way a page might print the same quantity."""
    t = tok.strip().lower().replace("$", "").replace("%", " percent")
    t = re.sub(r"\s+", " ", t).strip()
    out = {t}
    bare = t.replace(",", "")
    out.add(bare)
    m = re.match(r"^([\d.]+)\s*(million|billion|percent)$", t)
    if m:
        n, unit = float(m.group(1)), m.group(2)
        if unit == "million":
            out |= {"%s million" % m.group(1), "%d,000,000" % int(n * 1e6) if n == int(n) else ""}
            out.add("{:,}".format(int(n * 1e6)) if n == int(n) else "")
            # Build 60. Trade tables abbreviate: Builder prints "$621 M" where the
            # card writes "$621 million". Five real, checked figures on three cards
            # were reported unsourced on that difference alone, which is the kind
            # of false positive that trains a reader to skim the report.
            out |= {"%s m" % m.group(1), "%sm" % m.group(1),
                    "%s mm" % m.group(1), "%s mil" % m.group(1)}
        if unit == "billion":
            out.add("{:,}".format(int(n * 1e9)) if n == int(n) else "")
            out |= {"%s b" % m.group(1), "%sb" % m.group(1), "%s bn" % m.group(1)}
        if unit == "percent":
            out |= {"%s%%" % m.group(1), "%s per cent" % m.group(1)}
    if bare.isdigit():
        out.add("{:,}".format(int(bare)))
        # Marketing counters round to thousands: CastleRock's own about page says
        # "20k+ Homes since 2004" where the card says 20,000.
        if int(bare) >= 1000 and int(bare) % 1000 == 0:
            out |= {"%dk" % (int(bare) // 1000), "%d k" % (int(bare) // 1000)}
    return {v for v in out if v}


def figures_in(text):
    found = []
    for m in NUM.finditer(text or ""):
        tok = m.group(0)
        bare = re.sub(r"[^\d.]", "", tok)
        if not bare:
            continue
        if YEAR.match(bare.split(".")[0]) and "," not in tok and "$" not in tok:
            continue
        try:
            if float(bare.split(".")[0] or 0) < FLOOR and "million" not in tok.lower() \
                    and "billion" not in tok.lower():
                continue
        except ValueError:
            continue
        found.append((tok.strip(), max(0, m.start() - 55), m.end() + 25))
    for w, n in WORDS.items():
        for m in re.finditer(r"\b%s\b" % re.escape(w), text or "", re.I):
            if n >= FLOOR:
                found.append((str(n), max(0, m.start() - 55), m.end() + 25))
    return found


def main():
    d = json.load(open(ROOT / "houston-data.json", encoding="utf-8"))
    only = [a for a in sys.argv[1:] if a.startswith("HOU-")]
    targets = [t for t in d["targets"] if not only or t["target_id"] in only]

    cache = {}
    if CACHE.exists():
        cache = json.load(open(CACHE, encoding="utf-8"))

    want = set()
    for t in targets:
        for u in ([t.get("homepage_url")] + [s.get("url") for s in t.get("sources", [])]
                  + [k.get("url") for k in t.get("key_projects", [])]):
            if u and u.startswith("http") and not any(h in u for h in SKIP_HOST) \
                    and u not in cache:
                want.add(u)

    if want:
        print("fetching %d pages not already cached" % len(want), file=sys.stderr)
        with cf.ThreadPoolExecutor(16) as ex:
            for u, txt in zip(sorted(want), ex.map(fetch, sorted(want))):
                cache[u] = txt or ""
        CACHE.parent.mkdir(exist_ok=True)
        json.dump(cache, open(CACHE, "w"), ensure_ascii=False)

    n_fig = n_off = 0
    off_cards = 0
    for t in targets:
        urls = [u for u in ([t.get("homepage_url")]
                            + [s.get("url") for s in t.get("sources", [])]
                            + [k.get("url") for k in t.get("key_projects", [])])
                if u and u.startswith("http") and not any(h in u for h in SKIP_HOST)]
        readable = [u for u in urls if cache.get(u)]
        blob = " ".join(cache.get(u, "") for u in readable).lower()

        text = " ".join(filter(None, [
            t.get("synopsis"), t.get("key_stat"),
            " ".join(w["text"] for w in t.get("why", [])),
            " ".join(k["detail"] for k in t.get("key_projects", []))]))

        hits = figures_in(text)
        n_fig += len(hits)
        if not readable:
            continue
        miss = []
        for tok, a, b in hits:
            if not any(v in blob for v in variants(tok)):
                miss.append((tok, re.sub(r"\s+", " ", text[a:b]).strip()))
        if miss:
            off_cards += 1
            n_off += len(miss)
            print("\n%-9s %-30s  %d of %d cited pages readable"
                  % (t["target_id"], t["short"][:30], len(readable), len(urls)))
            seen = set()
            for tok, ctx in miss:
                if tok in seen:
                    continue
                seen.add(tok)
                print("   %-14s ...%s..." % (tok, ctx[:88]))

    print("\n%d figures across %d cards. %d on no page the card cites, over %d cards."
          % (n_fig, len(targets), n_off, off_cards))
    print("A figure here is invented, derived, or from a source the card does not "
          "list. Open the card and one page to tell which.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
