# -*- coding: utf-8 -*-
"""The four page gates, for any market's data file.

probe.py, linkcheck.py, phonecheck.py and figures.py were written against the
Houston build and read its modules directly. The Dallas-Fort Worth deck arrives
as one JSON file, so this runs the same four questions against that file with
the same helpers:

  links    does every URL answer
  names    is each contact's name in the bytes of the page cited for them
  phones   are the ten digits in the bytes of the page cited for them
  figures  is every figure a card prints on a page the card cites

    python3 marketcheck.py dfw/dfw-data.json            all four
    python3 marketcheck.py dfw/dfw-data.json names      one

A page a script cannot read is not a finding either way. It resolves against a
dated hand reading in the market's HAND register, which records only what was
seen, or it is reported as unread.
"""
import json, pathlib, re, sys, time
import concurrent.futures as cf
from urllib.parse import urlparse

import linkcheck as LC
import probe as PR
import phonecheck as PC
import figures as FG

ROOT = pathlib.Path(__file__).parent


def _cache(path):
    return ROOT / "internal" / ("mc_" + pathlib.Path(path).stem + ".json")


def _hand(path):
    """The market's hand readings: {url: text seen, dated}."""
    p = pathlib.Path(path).parent / "hand.json"
    h = json.load(open(p, encoding="utf-8")) if p.exists() else {}
    return _Norm({k.rstrip("/").lower(): v for k, v in h.items()})


class _Norm(dict):
    """A hand reading answers for its URL with or without the trailing slash."""
    def _k(self, u):
        return (u or "").rstrip("/").lower()
    def __contains__(self, u):
        return dict.__contains__(self, self._k(u))
    def __getitem__(self, u):
        return dict.__getitem__(self, self._k(u))


def _pages(urls, cache):
    todo = [u for u in urls if u not in cache]
    if todo:
        print("fetching %d pages" % len(todo), file=sys.stderr)
        def get(u):
            body, err = PR.fetch(u)
            if body is None:
                return u, None
            return u, body.decode("utf-8", "replace")
        with cf.ThreadPoolExecutor(12) as ex:
            for u, b in ex.map(get, todo):
                cache[u] = b
    return cache


def links(d, path):
    urls = LC.where(d)
    for s in d.get("supply", []):
        for k in ("url", "phone_source", "company_li"):
            if isinstance(s.get(k), str) and s[k].startswith("http"):
                urls.setdefault(s[k], set()).add("supply: " + s["name"])
    hits = [u for u in urls if any(b in u.lower() for b in LC.BANNED)]
    todo = sorted(urls)
    with cf.ThreadPoolExecutor(16) as ex:
        res = list(ex.map(LC.status, todo))
    bad = [(u, s) for u, s in res if not (isinstance(s, int) and s < 400)]
    again = {}
    for u, s in bad:
        h = urlparse(u).netloc.lower().replace("www.", "")
        if h in LC.BLOCKED or "linkedin.com" in h:
            continue
        time.sleep(1.2)
        again[u] = LC.status(u)[1]
    dead = [(u, again[u]) for u in again if not (isinstance(again[u], int) and again[u] < 400)]
    blocked = [u for u, s in bad if u not in again]
    print("links: %d urls, %d banned, %d dead, %d blocked or LinkedIn"
          % (len(urls), len(hits), len(dead), len(blocked)))
    for u in hits:
        print("  BANNED  %s  on %s" % (u, ", ".join(sorted(urls[u]))))
    for u, s in sorted(dead, key=lambda x: str(x[1])):
        print("  %-14s %s\n%18s %s" % (s, u, "on:", ", ".join(sorted(urls[u]))[:160]))
    return {"dead": [[u, str(s), sorted(urls[u])] for u, s in dead], "banned": hits}


def names(d, path, cache):
    hand = _hand(path)
    jobs = {}
    for t in d["targets"]:
        for p in t.get("principals", []):
            u = p.get("source_url")
            if u and "linkedin.com" not in u:
                jobs.setdefault(u, []).append((t["target_id"], t["short"], p["name"]))
    for s in d.get("supply", []):
        for p in s.get("people", []) or []:
            u = p.get("source_url") or s.get("url")
            if u:
                jobs.setdefault(u, []).append(("supply", s["name"], p["name"]))
    _pages(list(jobs), cache)
    miss, unread, ok = [], [], 0
    for u, rows in jobs.items():
        body = cache.get(u)
        txt = raw = ""
        if body:
            b = body.encode("utf-8")
            txt, raw = PR.text_of(b), PR.raw_of(b)
        if u in hand:
            h = re.sub(r"[^a-z0-9]+", " ", hand[u].lower())
            txt, raw = txt + " " + h + " ", raw + " " + h + " "
        for tid, short, nm in rows:
            if not txt and not raw:
                unread.append((tid, short, nm, u))
            elif PR.hit(nm, " " + txt + " ", " " + raw + " ") or \
                    PR.hit(re.sub(r"[-'’]", " ", nm), " " + txt + " ", " " + raw + " "):
                ok += 1
            else:
                miss.append((tid, short, nm, u))
    print("names: %d found, %d MISSING from the page cited, %d on a page not read"
          % (ok, len(miss), len(unread)))
    for r in miss:
        print("  MISSING %-11s %-24s %-26s %s" % (r[0], r[1][:24], r[2][:26], r[3]))
    for r in unread:
        print("  unread  %-11s %-24s %-26s %s" % (r[0], r[1][:24], r[2][:26], r[3]))
    return {"missing": miss, "unread": unread}


def phones(d, path, cache):
    hand = _hand(path)
    jobs = []
    for t in d["targets"]:
        if t.get("phone") and t.get("phone_source"):
            jobs.append((t["target_id"], t["short"], t["phone"], t["phone_source"]))
        for m in t.get("phone_more") or []:
            if m.get("number") and t.get("phone_source"):
                jobs.append((t["target_id"], t["short"], m["number"], t["phone_source"]))
    for s in d.get("supply", []):
        if s.get("phone"):
            jobs.append(("supply", s["name"], s["phone"], s.get("phone_source") or s.get("url")))
    _pages(list({j[3] for j in jobs if j[3]}), cache)
    miss, unread, ok = [], [], 0
    for tid, short, num, u in jobs:
        num = re.sub(r"\D", "", num)[-10:]
        body = cache.get(u) or ""
        vis, raw = PC.haystack(body) if body else ("", "")
        if u in hand:
            vis += " " + hand[u]
        if not vis and not raw:
            unread.append((tid, short, num, u))
        elif PC.found_on(num, vis, raw):
            ok += 1
        elif not PC.ships_numbers(vis, raw) and u not in hand:
            unread.append((tid, short, num, u))
        else:
            miss.append((tid, short, num, u))
    print("phones: %d found, %d MISSING, %d on a page that ships no numbers to a script"
          % (ok, len(miss), len(unread)))
    for r in miss:
        print("  MISSING %-11s %-26s %s  %s" % (r[0], r[1][:26], r[2], r[3]))
    for r in unread:
        print("  unread  %-11s %-26s %s  %s" % (r[0], r[1][:26], r[2], r[3]))
    return {"missing": miss, "unread": unread}


def figures(d, path, cache):
    hand = _hand(path)
    derived = d.get("_derived", {})
    urls = set()
    for t in d["targets"]:
        for u in ([t.get("homepage_url")] + [s.get("url") for s in t.get("sources", [])]
                  + [k.get("url") for k in t.get("key_projects", [])]):
            if u and u.startswith("http") and "linkedin.com" not in u:
                urls.add(u)
    _pages(sorted(urls), cache)
    n_fig = n_off = 0
    out, blind = [], []
    for t in d["targets"]:
        us = [u for u in dict.fromkeys([t.get("homepage_url")] + [s.get("url") for s in t.get("sources", [])]
                                       + [k.get("url") for k in t.get("key_projects", [])])
              if u and u.startswith("http") and "linkedin.com" not in u]
        texts = []
        for u in us:
            x = cache.get(u)
            x = FG.flatten(x.encode("utf-8")) if x else ""
            if x and (FG.CHALLENGE.search(x[:5000]) or FG._noise(x)):
                x = ""
            if u in hand:
                x += " " + hand[u]
            if x.strip():
                texts.append(x)
        blob = " ".join(texts).lower()
        text = " ".join(filter(None, [t.get("synopsis"), t.get("key_stat"), t.get("mvp_screen"),
                                      " ".join(w["text"] for w in t.get("why", [])),
                                      " ".join((k.get("detail") or "") for k in t.get("key_projects", []))]))
        # The band edges are the deck's own rubric, quoted, not a figure about the firm.
        text = re.sub(r"\b(?:above|below|over|under|past|beyond) 1,500\b|\b25 to 400\b|\b400 to 1,500\b|"
                      r"\bthe 1,500\b", lambda m: " " * len(m.group(0)), text)
        hits = FG.figures_in(text)
        n_fig += len(hits)
        if not texts:
            if hits:
                blind.append((t["target_id"], t["short"], [h[0] for h in hits]))
            continue
        der = derived.get(t["target_id"], {})
        miss = []
        for tok, a, b in hits:
            if any(v in blob for v in FG.variants(tok)):
                continue
            if tok in der and all(any(v in blob for v in FG.variants(p)) for p in der[tok]):
                continue
            miss.append((tok, re.sub(r"\s+", " ", text[a:b]).strip()))
        if miss:
            n_off += len(miss)
            out.append((t["target_id"], t["short"], len(texts), len(us), miss))
    print("figures: %d across %d cards, %d on no page the card cites, over %d cards; "
          "%d cards with figures and no readable page" % (n_fig, len(d["targets"]), n_off, len(out), len(blind)))
    for tid, short, r, n, miss in out:
        print("\n%-11s %-28s %d of %d readable" % (tid, short[:28], r, n))
        seen = set()
        for tok, ctx in miss:
            if tok not in seen:
                seen.add(tok)
                print("   %-14s ...%s..." % (tok, ctx[:96]))
    for tid, short, figs in blind:
        print("  blind %-11s %-28s %s" % (tid, short[:28], ", ".join(figs[:8])))
    return {"off": [[a, b, [m[0] for m in e]] for a, b, c, dd, e in out], "blind": blind}


def main():
    path = sys.argv[1]
    which = sys.argv[2:] or ["links", "names", "phones", "figures"]
    d = json.load(open(path, encoding="utf-8"))
    cp = _cache(path)
    cache = json.load(open(cp, encoding="utf-8")) if cp.exists() else {}
    res = {}
    try:
        for w in which:
            print("\n" + "=" * 70)
            res[w] = (links(d, path) if w == "links" else
                      globals()[w](d, path, cache))
    finally:
        cp.parent.mkdir(exist_ok=True)
        json.dump(cache, open(cp, "w", encoding="utf-8"), ensure_ascii=False)
        json.dump(res, open(str(cp).replace(".json", "_report.json"), "w"), ensure_ascii=False,
                  indent=1, default=list)
    bad = sum(len(v.get("dead", [])) + len(v.get("banned", [])) + len(v.get("missing", []))
              + len(v.get("off", [])) for v in res.values())
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
