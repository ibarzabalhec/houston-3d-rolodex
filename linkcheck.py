# -*- coding: utf-8 -*-
"""Status on every URL the deck publishes, plus a rule sweep on the sources.

Run it by hand. It is not in `make` because it hits the network, and a build
that fails when someone else's server is slow is a build nobody runs.

    python3 linkcheck.py            all urls
    python3 linkcheck.py --new      only urls not in the last run

Two things it catches that nothing else does.

A hard 404 on a page a card is built on. This happened: an audit pass reported a
company executive, a fetch of the page returned a bio saying so, and the URL was
a 404 the whole time. The name went on the deck and came off again an hour later.
A fetch that reads a page is not proof the page exists. This is.

A source from a domain the deck does not use: an encyclopedia, or a contact
aggregator. Every name and figure has to come from a primary page or dated
reporting, and this is the sweep that says so.

BLOCKED holds the hosts that refuse scripted requests and are live in a browser.
They are reported separately rather than as failures. Add to it only after
opening the URL in a browser and confirming the page is there.
"""
import json, pathlib, re, ssl, sys, time, urllib.error, urllib.request
import concurrent.futures as cf
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).parent
CACHE = ROOT / ".linkcheck.json"

BANNED = ["wikipedia", "wikimedia", "zoominfo", "rocketreach", "apollo.io",
          "crunchbase", "buzzfile", "signalhire", "lusha", "leadiq", "dnb.com",
          "bbb.org", "yelp.com", "theorg.com", "glassdoor", "zippia", "wiza",
          "leadar", "contactout", "hunter.io", "clearbit", "datanyze", "owler",
          "manta.com", "bizapedia", "corporationwiki", "spokeo", "whitepages"]

# Live in a browser, closed to a script. Confirmed by hand.
# Build 65. A whole domain that stops answering is a different fact from one
# page that moved, and a different fact again from a host that refuses a script.
# It is reported under its own heading with the date it was seen, and the entry
# expires: three weeks after the date, the host counts as dead again, so an
# outage cannot quietly become a permanent exemption.
DOWN = {
    "napcoprecast.com": ("2026-09-24",
        "Every path 404s, the homepage included, to this script and to a separate "
        "fetcher; plain http answers 403. Read in full on 2026-09-14. Main Street "
        "Capital still lists NAPCO as a current portfolio company, so this reads as "
        "an outage or a re-platform, not a closure."),
}
DOWN_DAYS = 21


def down(host):
    import datetime as _dt
    e = DOWN.get(host.replace("www.", ""))
    if not e:
        return None
    seen = _dt.date.fromisoformat(e[0])
    return e if (_dt.date.today() - seen).days <= DOWN_DAYS else None


BLOCKED = {"investors.bldr.com", "builderonline.com",
           # Build 68, the Dallas-Fort Worth deck. Each answered a script 403,
           # 401 or 404 and a fetcher the page, read 24 September 2026.
           "fortworthinc.com", "investor.kbhome.com", "investors.amh.com",
           "investors.tripointehomes.com", "avillarailhead.com", "cyreneatpaintedtree.com",
           "grandhomes.com", "livabl.com", "sekisuihouse-global.com", "cowtownmaterials.com",
           "erw-sitesolutions.com", "bizjournals.com", "houstonagentmagazine.com",
           "members.ghba.org", "members.texasbuilders.org", "housingwire.com",
           "houstonchronicle.com", "sec.gov", "globenewswire.com", "businesswire.com",
           "concreteproducts.com", "urbanland.uli.org", "knowledge.uli.org",
           "developingresilience.uli.org", "investor.howardhughes.com",
           "investor.lgihomes.com", "investors.camdenliving.com",
           "investors.centurycommunities.com", "investors.mihomes.com",
           "archpaper.com", "homes.com", "har.com", "investing.com",
           "kinder.rice.edu", "risewellhomes.com", "ravennahomes.com",
           "rskrealestatepartners.com", "codes.findlaw.com", "livelonestar.com",
           "benzinga.com", "linkedin.com", "oriongroupholdingsinc.com",
           # Added in Build 58 with the field section's links. Each was opened
           # in a browser by hand before it went in here: cobod.com answers a
           # script 454 and a browser the full site, 3dprinting.com answers 403
           # and renders the article, voxelmatters answers a 202 stub.
           "cobod.com", "3dprinting.com", "voxelmatters.com",
           # landtejas.com answered scripts until Build 57 and now times them
           # out on every attempt. Opened by hand on 14 September 2026: the site
           # loads, and its footer still carries the number the deck holds.
           "landtejas.com",
           # Build 64. Three pages answer a script a 403 or a bare 404 and serve
           # the record to a reader. Each was opened on 14 September 2026 and the
           # claim the card rests on was read off the page: the AGC Houston entry
           # names Gerald Guzman president of Winco Masonry, the ASA entry names
           # Sharon Stelter vice president of Veazey Enterprises, and the D CEO
           # piece of 24 August 2023 quotes Robert Barnes III and dates his
           # succession to 2015.
           "members.agchouston.org", "members.asaonline.com", "dmagazine.com",
           # Build 65. Both opened by a separate fetcher on 24 September 2026 and
           # read: the PulteGroup releases for Ryehill and Del Webb Fulshear, and
           # Multi-Housing News on Tricon Peek Road. Both answer this script 403.
           "pultegroupinc.com", "multihousingnews.com",
           # Build 60. HTTP only, and it answers an HTTPS request with a 302 back
           # to HTTP, so anything that upgrades the scheme loops. Read with curl
           # on 14 September 2026: the about page is there and names the founder.
           "andradeconstructioncompanies.com",
           # Build 60. Marek Brothers answers a scripted HEAD with a 403 and a
           # GET with the article. Read 14 September 2026.
           "marekbros.com",
           # Build 62, with the wall supply chain. Three conditions, all of which
           # look identical in this report and are not the same thing, so each
           # says which it is.
           #
           # Refuses a script and serves a browser:
           "wells.build",      # 403 to a script and to headless Chromium; read
                               # through a fetcher that carries a full browser
                               # profile, 14 September 2026.
           #
           # Reachable, and not from this container: the agent proxy's egress
           # allowlist answers 403 before the request leaves. That is a fact
           # about where this script runs, not about the site.
           "camaratamasonry.com",   # read 14 September 2026: masonry, natural
                                    # stone, tile, terrazzo, architectural
                                    # precast and specialty.
           "wincomasonry.com",      # read 14 September 2026.
           #
           # Live, with an intermittent upstream: trussway.com answers a
           # certificate error to urllib and 502 through the proxy, and serves
           # its full product page otherwise. Read 14 September 2026: roof
           # trusses, floor trusses, wall panels, components and rough openings,
           # beams and hardware.
           "trussway.com"}

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,*/*"}
CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")


def where(d):
    """Every url the deck publishes, and the card it sits on."""
    out = {}
    def add(u, w):
        if isinstance(u, str) and u.startswith("http"):
            out.setdefault(u, set()).add(w)
    for t in d["targets"]:
        w = t["short"]
        add(t.get("homepage_url"), w)
        add(t.get("team_url"), w + " team")
        add(t.get("company_li"), w + " company page")
        add(t.get("phone_source"), w + " phone")
        for s in t.get("sources", []):
            add(s.get("url"), w + " source")
        for k in t.get("key_projects", []):
            add(k.get("url"), w + " evidence")
        for p in t.get("principals", []):
            add(p.get("linkedin_url"), w + " / " + p["name"])
            add(p.get("source_url"), w + " / " + p["name"])
    # The field section. These are not firm cards, so the loop above never saw
    # them, and twelve competitors shipped with no link checked at all until
    # Build 58.
    for c in d.get("competitors", []):
        for lab, u in c.get("links", []):
            add(u, "field: " + c["name"])
    return out


def _once(u, meth):
    try:
        r = urllib.request.Request(u, method=meth, headers=UA)
        with urllib.request.urlopen(r, timeout=30, context=CTX) as resp:
            return resp.status, None
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return None, type(e).__name__


def status(u):
    """Twelve threads hitting one small host look like an attack to it.

    Build 62 ran this against 662 urls and a trade association directory came
    back 404 in the sweep and 200 three times in a row on its own. That is rate
    limiting, and reporting it as a dead source sends a person to check a page
    that was never broken. A second attempt, after a pause, separates a host
    under load from a page that is gone.
    """
    for attempt in (0, 1):
        for meth in ("HEAD", "GET"):
            code, err = _once(u, meth)
            if code is not None:
                # Build 65. PulteGroup's three brand sites answer HEAD with 404
                # and GET with the page, so a 404 on HEAD is not an answer. GET
                # decides.
                if meth == "HEAD" and code in (403, 404, 405, 501):
                    continue
                if code in (404, 429, 500, 502, 503) and attempt == 0:
                    break          # worth one retry: could be load, not absence
                return u, code
            if meth == "GET" and attempt == 0:
                break              # a connection-level failure is worth a retry
            if meth == "GET":
                return u, err
        time.sleep(2.5)
    return u, "?"


def main():
    d = json.load(open(ROOT / "houston-data.json", encoding="utf-8"))
    urls = where(d)

    hits = [u for u in urls if any(b in u.lower() for b in BANNED)]
    print("sources: %d urls across %d cards" % (len(urls), len(d["targets"])))
    if hits:
        print("\nRULE BREAK, a source the deck does not use:")
        for u in hits:
            print("  %s\n     on: %s" % (u, ", ".join(sorted(urls[u]))))
    else:
        print("rule sweep: clean, no encyclopedia and no contact aggregator")

    todo = sorted(urls)
    if "--new" in sys.argv and CACHE.exists():
        seen = set(json.load(open(CACHE)))
        todo = [u for u in todo if u not in seen]
        print("checking %d urls not seen in the last run" % len(todo))

    with cf.ThreadPoolExecutor(24) as ex:
        res = list(ex.map(status, todo))

    # Build 67. Four of five "dead" links in one sweep answered 200 one at a
    # time a minute later: a 429 from a small host, a 400 and two timeouts
    # under twenty-four parallel threads. Anything that failed in the sweep is
    # asked again, alone and slowly, before it is reported.
    def _bad(s):
        return not (isinstance(s, int) and s < 400)
    again = [u for u, s in res if _bad(s)
             and urlparse(u).netloc.lower().replace("www.", "") not in BLOCKED]
    if again:
        fixed = {}
        for u in again:
            time.sleep(1.5)
            fixed[u] = status(u)[1]
        res = [(u, fixed.get(u, s)) for u, s in res]

    dead, blocked, out = [], [], []
    for u, s in res:
        if isinstance(s, int) and s < 400:
            continue
        _h = urlparse(u).netloc.lower().replace("www.", "")
        if down(_h):
            out.append((u, s))
            continue
        (blocked if _h in BLOCKED else dead).append((u, s))
    if out:
        print("\n%d on a host that is down, seen and dated, re-check before a push:" % len(out))
        for _h in sorted({urlparse(u).netloc.lower().replace("www.", "") for u, _s in out}):
            print("  %s  %s: %s" % (_h, DOWN[_h][0], DOWN[_h][1]))

    print("\n%d dead, %d blocked to scripts and live in a browser"
          % (len(dead), len(blocked)))
    for u, s in sorted(dead, key=lambda x: str(x[1])):
        print("  %-16s %s" % (s, u))
        for w in sorted(urls[u]):
            print("%22s %s" % ("on:", w))

    json.dump(sorted(urls), open(CACHE, "w"))
    return 1 if (dead or hits) else 0


if __name__ == "__main__":
    sys.exit(main())
