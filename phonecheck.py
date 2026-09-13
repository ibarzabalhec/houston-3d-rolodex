# -*- coding: utf-8 -*-
"""Is the number actually on the page the card cites for it?

probe.py asks this about names and figures.py asks it about figures. This asks
it about phone numbers, which is the easiest of the three to get wrong by hand
and the hardest to notice afterwards, because every ten-digit string looks like
every other ten-digit string.

For every number the deck prints, fetch the page it cites and test the digits
against every rendering a page might use:

    7136810446   713-681-0446   713.681.0446   (713) 681-0446   713 681 0446
    +17136810446   1-713-681-0446   tel:+1-713-681-0446

A number on no page it cites is the finding. It is a transposition, a
transcription slip, or a page that has changed since it was read, and all three
are the same kind of wrong.

Pages a script cannot read resolve against PHONES.VERIFIED, which records what a
browser showed and when. Those are reported as read by hand. They are never
reported as confirmed, because this script did not confirm them.

    python3 phonecheck.py
    python3 phonecheck.py HOU-121
"""
import html as _html
import json, pathlib, re, ssl, sys, urllib.error, urllib.request
import concurrent.futures as cf

ROOT = pathlib.Path(__file__).parent

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,*/*"}
CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")


def fetch(url):
    try:
        with urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=30, context=CTX) as r:
            ct = (r.headers.get("Content-Type") or "").lower()
            if not any(k in ct for k in ("html", "xml", "text")):
                return None, "not html (%s)" % ct.split(";")[0]
            body = r.read(3_000_000)
            if len(body) < 2000:
                return None, "stub of %d bytes, a bot challenge" % len(body)
            return body.decode("utf-8", "replace"), None
    except urllib.error.HTTPError as e:
        return None, "http %s" % e.code
    except Exception as e:
        return None, type(e).__name__


def haystack(body):
    """The page's visible words and its raw markup, digits kept together.

    Both are needed. A number can be printed as text, or live only inside a
    tel: href, or sit in a data attribute that never renders. All three count
    as the page publishing it.
    """
    vis = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body, flags=re.S | re.I)
    vis = _html.unescape(re.sub(r"<[^>]+>", " ", vis))
    raw = _html.unescape(body)
    return vis, raw


def renderings(d):
    """Every way a page might print these ten digits."""
    a, b, c = d[:3], d[3:6], d[6:]
    out = set()
    for sep in ("", "-", ".", " ", "&#8209;", "&#45;"):
        out.add(a + sep + b + sep + c)
        out.add("(%s)%s%s%s" % (a, sep, b, sep + c))
        out.add("(%s) %s%s%s" % (a, b, sep, c))
        out.add("1" + sep + a + sep + b + sep + c)
        out.add("+1" + sep + a + sep + b + sep + c)
    out.add("(%s) %s-%s" % (a, b, c))
    out.add("+1 (%s) %s-%s" % (a, b, c))
    out.add("1-%s-%s-%s" % (a, b, c))
    # A page that splits the number across markup: the digits survive when the
    # tags are stripped, which is what the visible-text haystack is for.
    return out


ANY = re.compile(r"(?:\(\d{3}\)|\d{3})[\s.\-]?\d{3}[\s.\-]?\d{4}(?!\d)")


def found_on(d, vis, raw):
    for r in renderings(d):
        if r in vis or r in raw:
            return True
    # Last resort: the digits with every non-digit removed. Catches a number
    # broken up by spans. Run only on the visible text, because collapsing the
    # markup's digits would match half the stylesheet.
    return d in re.sub(r"\D", "", vis)


def ships_numbers(vis, raw):
    """Does this page put any dialable string in front of a script at all?

    Four sites on this deck send a browser a page full of office numbers and
    send a script the same page with every number missing, because the numbers
    are assembled by JavaScript. On those, not finding a number proves nothing,
    exactly as probe.py found for names. A page with no phone-shaped string
    anywhere is unreadable for this purpose and resolves against a browser note
    instead. A page that does ship numbers, but not this one, is a finding.
    """
    return bool(ANY.search(vis)) or bool(re.search(r'href=["\']tel:', raw, re.I))


def main():
    import phones as P
    only = [a for a in sys.argv[1:] if a.startswith("HOU-")]

    # Every number the deck prints, and the page it is cited to. A number in
    # MORE or NO_MAIN is cited to the same page as its record's main line.
    jobs = {}
    def want(tid, digits, label, url):
        if only and tid not in only:
            return
        jobs.setdefault(url, []).append((tid, digits, label))

    for tid, (d, lab, url, _rule) in P.PHONE.items():
        want(tid, d, lab or "main line", url)
    for tid, url in P.NO_MAIN.items():
        for d, lab in P.MORE.get(tid, []):
            want(tid, d, lab or "no label", url)
    for tid, extra in P.MORE.items():
        if tid in P.NO_MAIN:
            continue
        url = P.PHONE[tid][2]
        for d, lab in extra:
            want(tid, d, lab or "no label", url)

    n = sum(len(v) for v in jobs.values())
    print("checking %d numbers across %d pages\n" % (n, len(jobs)))

    missing, byhand, unread, ok = [], [], [], 0

    def run(u):
        return (u,) + fetch(u)

    with cf.ThreadPoolExecutor(16) as ex:
        for url, body, err in ex.map(run, sorted(jobs)):
            if body is None:
                for tid, d, lab in jobs[url]:
                    (byhand if url in P.VERIFIED else unread).append((tid, d, lab, url, err))
                continue
            vis, raw = haystack(body)
            if not ships_numbers(vis, raw):
                for tid, d, lab in jobs[url]:
                    (byhand if url in P.VERIFIED else unread).append(
                        (tid, d, lab, url, "the page ships no number to a script"))
                continue
            for tid, d, lab in jobs[url]:
                if found_on(d, vis, raw):
                    ok += 1
                else:
                    missing.append((tid, d, lab, url))

    print("MISSING, the digits are not in the page cited for them: %d" % len(missing))
    for tid, d, lab, url in sorted(missing):
        print("  %-9s (%s) %s-%s   %s" % (tid, d[:3], d[3:6], d[6:], lab))
        print("      %s" % url)

    if byhand:
        seen = set()
        print("\nread in a browser by hand, not by this script: %d numbers"
              % len(byhand))
        for tid, d, lab, url, err in sorted(byhand):
            print("  %-9s (%s) %s-%s   %s" % (tid, d[:3], d[3:6], d[6:], lab))
            if url not in seen:
                seen.add(url)
                print("      %s\n      %s" % (url, P.VERIFIED[url]))

    if unread:
        print("\nnot claimed either way, the page could not be read and no browser "
              "note stands for it: %d" % len(unread))
        for tid, d, lab, url, err in sorted(unread):
            print("  %-9s (%s) %s-%s   %-22s %s" % (tid, d[:3], d[3:6], d[6:], err, url))

    print("\ndigits found on the page cited: %d" % ok)
    print("records with a main line: %d. no main line designated: %d. "
          "stated absences: %d." % (len(P.PHONE), len(P.NO_MAIN), len(P.ABSENT)))
    return 1 if (missing or unread) else 0


if __name__ == "__main__":
    sys.exit(main())
