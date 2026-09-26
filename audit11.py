# -*- coding: utf-8 -*-
"""Build 84. Sources a reader can open.

paywall.py fetched every page the deck links and read it for the marks
publishers set on a locked article. It found 34 links behind a subscription on
ten outlets. A citation the reader cannot open is a citation in name only, so
each one was handled by one of three rules, in this order:

  drop   a line in a card's "In the press" list. The list points a reader at
         coverage. It carries no fact, so a locked line is removed.
  swap   a free page on the record carries the same fact. The locked link is
         removed or replaced by that page. Every free page here was read before
         it was used, and every one was already on a card or reached from a
         page that was.
  mark   no free page on the record carries the fact. The fact stays and so
         does the link, and the page labels it "Subscription" beside it.

The marked links are the queue for a session with a search budget. PAID below
is the whole list. emit.py labels them on the page, and stops the build if a
link on a locked outlet reaches the page without a label.
"""
from urllib.parse import urlparse

HOMES = ("https://www.homes.com/news/houstons-3d-printed-housing-push-grows-with-two-new-developments/"
         "647676272/")
ABC13 = "https://abc13.com/post/san-leon-development-aims-sustainability-ground/18943368/"
GALV = ("https://www.galvnews.com/news/printing-the-future-san-leon-project-tests-new-model-for-coastal-"
        "housing/article_e6c622f8-f6cd-47f6-ad36-ed1cac45a3d4.html")
STRIPES = "https://www.stripes.com/branches/army/2026-07-28/fort-bliss-3-d-barracks-opening-22393339.html"

# Outlets that lock their articles. A link on one of these must be in PAID or
# off the page. HousingWire is not here: it locks some articles and not others,
# and the scan read five of its eight pages open, so its three locked pages are
# listed one by one.
LOCKED = ("houstonchronicle.com", "dallasnews.com", "therealdeal.com", "bizjournals.com", "bisnow.com",
          "enr.com", "galvnews.com", "stripes.com", "clpha.org", "wsj.com",
          "bloomberg.com", "ft.com", "costar.com", "star-telegram.com", "nytimes.com", "washingtonpost.com",
          "businessinsider.com", "theinformation.com", "barrons.com", "texasmonthly.com",
          "commercialobserver.com", "globest.com")

# Kept and labelled. The fact on the card is on no free page on the record.
PAID = {
    "https://therealdeal.com/texas/2026/03/12/icon-opens-3d-home-printing-tech-to-outside-builders/":
        "Cole Klein's Titan reservation, and leases before sales",
    "https://therealdeal.com/texas/houston/2025/12/30/brohn-homes-plants-flag-in-houston-with-historymaker-deal/":
        "Clayton Properties Group as part of Berkshire Hathaway",
    "https://www.housingwire.com/articles/century-communities-q2-2026-strategy/":
        "Century's 112-day cycle and 5 percent direct-cost cut",
    "https://therealdeal.com/texas/houston/2024/11/25/long-lake-purchased-100-acre-tract-in-houston-area/":
        "Woodmere's 95 acres, November 2024",
    "https://www.houstonchronicle.com/business/article/Frank-Liu-s-big-bets-on-urban-living-pay-off-15053303.php":
        "InTown's townhome programme",
    "https://therealdeal.com/texas/houston/2023/03/10/live-lone-star-opens-its-first-manufactured-home-development/":
        "Live Lone Star's communities, lots and Pearland figures",
    "https://www.bisnow.com/houston/news/industrial/provident-realty-advisors-hires-christen-vestal-to-lead-forthcoming-houston-office-116393":
        "Christen Vestal's Houston role",
    "https://www.housingwire.com/articles/why-builders-firstsource-bought-icg-and-why-pulte-sold-it/":
        "Builders FirstSource buying Pulte's framing producer",
    "https://www.bisnow.com/houston/news/construction-development/skanska-overcomes-challenges-on-texas-sized-tiltwall-project-131013":
        "Baker's panels at the Harris Health pharmacy",
    "https://www.housingwire.com/articles/partners-building-succession-plan/":
        "The Lemming succession, June 2026",
    "https://therealdeal.com/texas/houston/2025/08/21/radom-capital-asana-partners-secure-houston-multifamily-loan/":
        "The Clock Tower construction loan",
    "https://therealdeal.com/texas/houston/2023/11/13/pagewood-wile-to-convert-eado-houston-warehouses/":
        "Wile as Pagewood's East Blocks partner",
    "https://www.bisnow.com/houston/news/office/modernized-medical-office-building-to-break-ground-in-katy-90935":
        "Katy Green and Medical Plaza West",
    "https://www.houstonchronicle.com/business/real-estate/article/Taylor-Morrison-starts-first-build-to-rent-16757127.php":
        "Taylor Morrison's Cypress build-to-rent community",
    "https://therealdeal.com/texas/2026/03/05/homebound-lines-up-1000-plus-dallas-fort-worth-home-lots/":
        "Homebound's 1,000-plus DFW lots",
    "https://www.bisnow.com/news/dallas-ft-worth/deal-sheet/homebound-closes-on-731m-deal-for-north-texas-expansion-the-dfw-deal-sheet-133470":
        "Homebound's $731 million lot deal",
    "https://www.dallasnews.com/business/real-estate/2023/07/07/chicago-builder-that-left-d-fw-returns-to-area-takes-1500-home-sites/":
        "William Ryan's return and 500-a-year goal",
    "https://www.dallasnews.com/news/2010/02/08/first-texas-homes-moves-from-arlington-to-uptown-dallas/":
        "First Texas Homes' chief executive, 2010",
    "https://www.dallasnews.com/business/real-estate/2025/07/24/list-who-are-the-10-biggest-homebuilders-in-d-fw/":
        "Zonda starts ranks",
    "https://www.houstonchronicle.com/business/real-estate/article/McGuyer-Homebuilders-acquired-by-Florida-builder-16468304.php":
        "Dream Finders buying MHI, and MHI's 2020 closings",
    "https://www.enr.com/articles/46027-pursuit-of-innovation-drives-success":
        "The 80,000 square foot Richardson plant",
    "https://www.dallasnews.com/abode/2026/03/08/new-homes-and-amenities-take-center-stage/":
        "The lazy river opening, November 2025",
}

# Press-list lines removed: the list carries no fact.
DROP_PRESS = {
    GALV,
    "https://www.bizjournals.com/houston/news/2026/04/03/hiveasmbld-3d-printed-homes-community-san-leon.html",
    "https://www.houstonchronicle.com/business/article/3d-print-affordable-houston-east-end-22153531.php",
    "https://www.houstonchronicle.com/business/article/houston-build-to-rent-housing-21293194.php",
    "https://www.bizjournals.com/houston/news/2025/03/14/wan-bridge-adjusts-build-to-rent-goal.html",
    "https://www.bisnow.com/news/houston/construction-development/next-stop-apartments-3d-printed-house-lays-foundation-for-bigger-projects-ahead-117549",
    "https://www.enr.com/toplists/2026-Top-400-Contractors-1",
    "https://www.enr.com/articles/56905-harvey-l-harvey-cleary-a-little-bit-of-everything-firm",
    "https://www.dallasnews.com/business/real-estate/2023/07/07/chicago-builder-that-left-d-fw-returns-to-area-takes-1500-home-sites/",
    "https://www.dallasnews.com/business/real-estate/2025/07/24/list-who-are-the-10-biggest-homebuilders-in-d-fw/",
}

# Source entries removed because a free page on the same card carries the fact.
#   HOU-003  the Housing Alliance HTX bio gives the February 2025 appointment
#   HOU-080  Concept Neighborhood's projects page gives Axelrad's 1890s building
#   HOU-016  Homes.com quotes Steve Commander and carries the plan, the prices and
#            the 5 to 7 percent; ABC13 carries construction under way, April 2026
DROP_SOURCE = {
    ("HOU-003", "https://clpha.org/news/2025/houston-housing-authority-names-jamie-bryant-president-ceo"),
    ("HOU-080", "https://www.houstonchronicle.com/business/real-estate/article/Exclusive-Axelrad-developers-East-End-17291259.php"),
    ("HOU-016", GALV),
}
ADD_SOURCE = {"HOU-016": [{"url": ABC13, "date": "2026-04-22"},
                         {"url": "https://realtynewsreport.com/3d-printed-homes-coming-to-galveston-county-coast/",
                          "date": "2026-04-10"}]}
# The figures gate had matched "about 40 miles" to "40 Under 40" in the Daily
# News's navigation. Realty News Report gives 38 miles to downtown Houston.
CARD_TEXT = [("HOU-016", "synopsis", "about 40 miles southeast of downtown Houston",
              "about 38 miles from downtown Houston")]
PRINCIPAL_SOURCE = {("HOU-016", "Steve Commander"): (GALV, HOMES)}

# Page-level text. The Army's own article gives two open on the day and the rest
# due in September, so Stars and Stripes comes off.
ICON_FACT = ("The Army", "Stars and Stripes: two open that day, the rest in September.",
             "The Army: two open that day, the rest in September.")
PRECEDENT = {
    "Avenue J": {"url": HOMES, "source": "Homes.com"},
    "Gulf Shore Estates": {"url": HOMES, "source": "Homes.com",
                           "what": ("26 homes planned, 23 to print. HiveASMBLD with Commander Home Builders. "
                                    "Announced April 2026.")},
}


def host(u):
    return urlparse(u).netloc.lower().replace("www.", "")


def locked(u):
    h = host(u)
    return any(h == x or h.endswith("." + x) for x in LOCKED)


def apply(D, mk):
    """Apply the drops and swaps. Returns a list of failures."""
    bad = []
    T = {t["target_id"]: t for t in D["targets"]}
    for t in D["targets"]:
        if t.get("press"):
            t["press"] = [p for p in t["press"] if p.get("url") not in DROP_PRESS]
    for tid, u in DROP_SOURCE:
        t = T.get(tid)
        if not t:
            continue
        n = len(t.get("sources") or [])
        t["sources"] = [s for s in t["sources"] if s.get("url") != u]
        if len(t["sources"]) == n:
            bad.append("audit11: %s has no source %s" % (tid, u))
    for tid, add in ADD_SOURCE.items():
        t = T.get(tid)
        if t:
            have = {s["url"] for s in t["sources"]}
            t["sources"] += [s for s in add if s["url"] not in have]
    for tid, key, old, new in CARD_TEXT:
        t = T.get(tid)
        if t and old in (t.get(key) or ""):
            t[key] = t[key].replace(old, new)
        elif t:
            bad.append("audit11: %s %s no longer says %r" % (tid, key, old))
    for (tid, name), (old, new) in PRINCIPAL_SOURCE.items():
        t = T.get(tid)
        if not t:
            continue
        p = next((p for p in t.get("principals") or [] if p.get("name") == name), None)
        if not p or p.get("source_url") != old:
            bad.append("audit11: %s %s source is not the one replaced" % (tid, name))
        else:
            p["source_url"] = new
    ir = D.get("icon_record") or {}
    if ir:
        f = next((f for f in ir.get("facts", []) if f[0] == ICON_FACT[0]), None)
        if not f or ICON_FACT[1] not in f[1]:
            bad.append("audit11: the ICON record's Army line changed")
        else:
            f[1] = f[1].replace(ICON_FACT[1], ICON_FACT[2])
        ir["links"] = [l for l in ir.get("links", []) if l[1] != STRIPES]
    if mk == "dfw":
        # The Trinity Falls roster pointed Del Webb at PulteGroup's card. Del Webb
        # has its own card.
        n = 0
        for o in (D.get("market") or {}).get("owners") or []:
            for b in o.get("builders") or []:
                if b.get("name") == "Del Webb" and b.get("id") == "DFW-007":
                    b["id"] = "DFW-064"
                    n += 1
        if not n:
            bad.append("audit11: the Del Webb roster entry changed")
    if mk == "hou":
        prec = (D.get("code") or {}).get("precedent") or []
        for name, new in PRECEDENT.items():
            p = next((p for p in prec if p.get("project") == name), None)
            if not p:
                bad.append("audit11: no precedent %s" % name)
            else:
                p.update(new)
    return bad


def urls(o, out=None):
    out = set() if out is None else out
    if isinstance(o, dict):
        for v in o.values():
            urls(v, out)
    elif isinstance(o, list):
        for v in o:
            urls(v, out)
    elif isinstance(o, str) and o.startswith("http"):
        out.add(o)
    return out


def paid(d):
    """The labelled links on this page, and any locked link without a label."""
    on = urls(d)
    unlabelled = sorted(u for u in on if locked(u) and u not in PAID)
    return sorted(u for u in on if u in PAID), unlabelled
