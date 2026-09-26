# -*- coding: utf-8 -*-
"""Which cited pages a reader cannot open for free?

A source a reader cannot open is a citation in name only. This fetches every
page the deck links (both markets, LinkedIn aside) and reads the page for the
marks publishers use to lock an article:

  ld        schema.org "isAccessibleForFree": false, the mark Google asks
            paywalled publishers to set
  tier      a content-tier meta set to locked or metered
  text      "subscribe to continue reading" and its relatives
  register  a free-account wall ("register to continue", "create a free account")
  host      a host known to lock its articles, when the page itself could not be read

    python3 paywall.py            scan, write internal/cache/paywall.json, print the report

Run by hand, like linkcheck.py. A finding is a lead: open the page before
acting on it, since metered sites open a few articles free.
"""
import concurrent.futures as cf
import pathlib
import re
import ssl
import sys
import urllib.request
import zlib
from urllib.parse import urlparse

import jsonio
import paths

ROOT = pathlib.Path(__file__).parent
OUT = paths.CACHE / "paywall.json"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124 Safari/537.36", "Accept": "text/html,*/*"}
# The system trust store, or the bundle SSL_CERT_FILE names. A fixed path here
# worked in one container and nowhere else.
CTX = ssl.create_default_context()

# Hosts that lock their articles behind a subscription. Used only when the page
# itself cannot be read; otherwise the page's own marks decide.
LOCKED = {"houstonchronicle.com", "dallasnews.com", "therealdeal.com", "bizjournals.com", "wsj.com",
          "bloomberg.com", "ft.com", "enr.com", "costar.com", "star-telegram.com", "galvnews.com",
          "nytimes.com", "washingtonpost.com", "businessinsider.com", "theinformation.com",
          "barrons.com", "economist.com", "texasmonthly.com", "commercialobserver.com", "globest.com"}

LD = re.compile(r'"isAccessibleForFree"\s*:\s*"?(false|False)"?')
TIER = re.compile(r'content_tier"\s+content="(locked|metered)"|content="(locked|metered)"\s+name="[^"]*content_tier', re.I)
TEXT = re.compile(r"subscribe (?:now )?to (?:continue|keep) reading|this (?:article|story|content) is "
                  r"(?:only )?(?:available )?(?:exclusively )?(?:for|to) (?:paid )?(?:subscribers|members)|"
                  r"already a subscriber\?|subscriber[- ]only|subscribers only|unlock (?:this|the full) "
                  r"(?:article|story)|to read the full (?:article|story),? (?:subscribe|sign)|"
                  r"premium subscribers|become a (?:paid )?(?:subscriber|member) to (?:read|continue)", re.I)
REG = re.compile(r"(?:register|sign up|create a free account|log in|sign in) to (?:continue|read|keep) reading|"
                 r"free account to (?:continue|read)|registration is required", re.I)


def urls():
    out = {}
    def walk(o, where):
        if isinstance(o, dict):
            for k, v in o.items():
                walk(v, where if k != "target_id" else where)
        elif isinstance(o, list):
            for v in o:
                walk(v, where)
        elif isinstance(o, str) and o.startswith("http") and "linkedin.com" not in o:
            out.setdefault(o, set()).add(where)
    for mk, f in (("houston", "docs/houston-data.json"), ("dfw", "docs/dfw-data.json")):
        P = jsonio.read(ROOT / f)
        for t in P["targets"]:
            walk(t, "%s:%s" % (mk, t["target_id"]))
        walk({k: v for k, v in P.items() if k != "targets"}, "%s:page" % mk)
    return out


def fetch(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=25, context=CTX) as r:
            b = r.read(1_500_000)
            if b[:2] == b"\x1f\x8b":
                b = zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(b, 20_000_000)
            return r.status, b.decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return type(e).__name__, ""


def read(u):
    st, body = fetch(u)
    host = urlparse(u).netloc.lower().replace("www.", "")
    marks = []
    if body and len(body) > 2000:
        if LD.search(body):
            marks.append("ld")
        if TIER.search(body):
            marks.append("tier")
        if TEXT.search(body):
            marks.append("text")
        if REG.search(body):
            marks.append("register")
    if not marks and (not body or len(body) <= 2000) and any(host == h or host.endswith("." + h) for h in LOCKED):
        marks.append("host")
    if not marks and any(host == h or host.endswith("." + h) for h in LOCKED):
        marks.append("host-known")
    return u, {"status": st, "host": host, "marks": marks, "bytes": len(body)}


def main():
    U = urls()
    print("scanning %d pages" % len(U), file=sys.stderr)
    res = {}
    with cf.ThreadPoolExecutor(12) as ex:
        for u, r in ex.map(read, sorted(U)):
            r["cited_on"] = sorted(U[u])
            res[u] = r
    OUT.parent.mkdir(exist_ok=True)
    jsonio.write(res, OUT, indent=1)
    locked = {u: r for u, r in res.items() if set(r["marks"]) & {"ld", "tier", "text", "host", "host-known"}}
    reg = {u: r for u, r in res.items() if r["marks"] == ["register"]}
    by = {}
    for u, r in locked.items():
        by.setdefault(r["host"], []).append(u)
    print("pages: %d, locked or likely locked: %d on %d hosts, free-account walls: %d"
          % (len(res), len(locked), len(by), len(reg)))
    for h, us in sorted(by.items(), key=lambda x: -len(x[1])):
        print("  %-28s %3d  %s" % (h, len(us), ",".join(sorted({m for u in us for m in res[u]["marks"]}))))


if __name__ == "__main__":
    main()
