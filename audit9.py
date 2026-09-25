# -*- coding: utf-8 -*-
"""Build 80. Content.

Three changes, applied last in both builds so they win:

1. A headline that holds a figure. Sixty rows showed a description where the
   List promised a number. Each replacement below was read on the page it cites,
   and the page is added to the card's sources so figures.py can check it.
   Rows with no published figure keep their line. The column is now called
   Headline, which is what it always held.
2. News since 1 March 2026, per firm, for the top sections. Dated, with the
   outlet and a one-line account of what happened. Search results and fetched
   pages only. No aggregator.
3. One rule stated once. "On the bands, a firm with no published figure is a
   Partly" was the last sentence of 23 Houston verdicts. It now sits once, in
   the note under the three counts.
"""
import re

NEWS_SINCE = "2026-03-01"

GRBK_10K = "https://www.sec.gov/Archives/edgar/data/1373670/000162828026037547/a2025annualreport-grbk.pdf"
LL26 = "https://www.builderonline.com/land/local-leaders-list/2026/dallas-fort-worth-arlington-tx/"

# target_id: (headline, page that carries the figure)
HEADLINE = {
    # Greater Houston
    "HOU-126": ("Factory-built ADUs from $99,000 turnkey in Houston",
                "https://www.auradwellings.com/"),
    "HOU-141": ("Serving the Texas market since 1988",
                "https://www.coreslab.com/locations/austin-texas-precast-concrete/"),
    "HOU-105": ("Employee-owned, established in 2017",
                "https://www.encoreconcrete.com/"),
    "HOU-082": ("About 513,000 sq ft in the East Blocks first phase",
                "https://therealdeal.com/texas/houston/2023/11/13/pagewood-wile-to-convert-eado-houston-warehouses/"),
    "HOU-042": ("More than 60 years of masterplans, and Lennar builds",
                "https://friendswooddevelopment.com/about-fdc"),
    # Dallas-Fort Worth
    "DFW-003b": ("11 DFW townhome communities listed on its site", "https://cbjenihomes.com/communities/"),
    "DFW-003d": ("Seven selling communities at the end of 2025, per Green Brick", GRBK_10K),
    "DFW-003c": ("Five selling communities at the end of 2025, per Green Brick", GRBK_10K),
    "DFW-044": ("19 DFW listings now selling and four coming, on its site",
                "https://risewellhomes.com/texas/dallas-fort-worth-new-homes"),
    "DFW-024": ("Six DFW communities listed on its site",
                "https://www.brittonhomestexas.com/new-homes/texas/dallas"),
    "DFW-060": ("New homes in eight DFW cities, per its own site",
                "https://www.centurycommunities.com/find-your-new-home/texas/dallas-fort-worth-metro/"),
    "DFW-063": ("Inside PulteGroup's 1,083 DFW closings in 2025", LL26),
    "DFW-050": ("Eight DFW communities listed on its site", "https://www.kbhome.com/new-homes-dallas-fort-worth"),
    "DFW-054": ("18 DFW communities listed on its site", "https://www.lgihomes.com/texas/dallas-fort-worth"),
    "DFW-CH-021": ("Over 100,000 lots in more than 300 North Texas communities",
                   "https://centurionamerican.com/about/"),
    "DFW-CH-001": ("Nine current DFW masterplans on its site, 13 in Texas",
                   "https://www.hillwoodcommunities.com/current-communities/"),
    "DFW-TR-051": ("ICF contractor serving North Texas for over 25 years", "https://dnrconcrete.com/"),
    "DFW-TR-074": ("17,000 sq ft production space added in New Caney, 2023",
                   "https://communityimpact.com/houston/lake-houston-humble-kingwood/business/2023/07/20/"
                   "future-frame-usa-expands-into-17000-square-foot-space-in-new-caney/"),
    "DFW-TR-050": ("ICF wall shells across DFW, in business since 2005",
                   "https://monsterconstructors.com/about-us/"),
    "DFW-TR-092": ("80,000 sq ft prefabrication plant in Richardson",
                   "https://www.enr.com/articles/46027-pursuit-of-innovation-drives-success"),
    "DFW-TR-091": ("70,000 sq ft Southlake headquarters and prefab plant",
                   "https://obrienarch.com/project/gmi-corporate-headquarters-pre-fab-facility/"),
    "DFW-TR-012": ("60,000 sq ft Dallas door shop, no DFW panel plant",
                   "https://hbsdealer.com/84-lumber-opens-dallas-door-shop"),
    "DFW-TR-010": ("Trussway had six plants and 1,000 staff when bought, 2022",
                   "https://www.bldr.com/who-we-are/in-the-news/builders-firstsource-acquires-trussway"),
    "DFW-TR-031": ("Serving the Texas market since 1988",
                   "https://www.coreslab.com/locations/austin-texas-precast-concrete/"),
    "DFW-TR-085": ("Fifteen to twenty slabs a week, per First Texas Homes",
                   "https://erw-sitesolutions.com/construction-company-texas/kaufman-concrete-foundations-texas/"),
    "DFW-TR-060": ("Over 750 mobile machines in its fleet, company-wide", "https://brundagebone.com/about/"),
    "DFW-TR-011": ("Hillsboro plant, one of 25 UFP Site Built facilities",
                   "https://ufpsitebuilt.com/leadershipteam/"),
}

# A brand with nothing on sale is not a prospect this year.
DFW_VERDICT = {
    ("DFW-036", "repeatability"): ("No", "Its own communities page lists no active Belclaire communities and "
                                         "points buyers to American Legend Homes."),
}
DFW_SOURCES = {"DFW-036": ["https://www.belclairehomes.com/communities"]}


def _n(date, outlet, headline, url, what):
    return {"date": date, "outlet": outlet, "headline": headline, "url": url, "what": what}


RNR_CCW = "https://realtynewsreport.com/fulshears-cross-creek-west-expands-into-luxury-homes/"
RNR_GEORGE = "https://realtynewsreport.com/4000-home-community-starts-sales/"
RNR_TRAILS = "https://realtynewsreport.com/rnr-real-estate-briefs-texas-more-113/"
CAMILLO_ACAD = "https://www.camillocompanies.com/camillo-companies-names-sean-mulroony-president-of-academy-development"
CAMILLO_CFO = "https://www.camillocompanies.com/camillo-companies-appoints-jomar-ereso-as-chief-financial-officer"

NEWS = {
    # ---------------------------------------------------------------- Houston
    "HOU-009": [
        _n("2026-05-28", "Century Communities",
           "Century Communities Continues West Houston Growth With New Home Collection in Fulshear, TX",
           "https://investors.centurycommunities.com/news/news-details/2026/Century-Communities-Continues-West-"
           "Houston-Growth-With-New-Home-Collection-in-Fulshear-TX/default.aspx",
           "Opened sales on The Liberty Collection at Fulshear Lakes, 40-foot homes on 50-foot lots."),
        _n("2026-03-18", "PR Newswire",
           "Century Communities Will Debut New Homes in Northwest Houston at Joint Grand Opening",
           "https://www.prnewswire.com/news-releases/century-communities-will-debut-new-homes-in-northwest-"
           "houston-at-joint-grand-opening-302717678.html",
           "Opened Maple Woods in Hockley, homes up to 3,075 square feet, alongside D.R. Horton."),
        _n("2026-03-12", "PR Newswire", "Century Communities Celebrates Grand Opening in West Houston Market",
           "https://www.prnewswire.com/news-releases/century-communities-celebrates-grand-opening-in-west-"
           "houston-market-302712504.html",
           "Opened in Sunterra Lakes, Brookshire, with two home collections."),
    ],
    "HOU-131": [
        _n("2026-07-20", "Houston Agent Magazine",
           "Caldwell Homes debuts Heritage Collection for Chambers Creek active-adult community",
           "https://houstonagentmagazine.com/2026/07/20/caldwell-homes-heritage-collection-chambers-creek-active-adult/",
           "Released six single-story plans at Chambers Creek in Willis, a 55-and-over community it develops itself."),
    ],
    "HOU-007": [
        _n("2026-06-24", "First America Homes",
           "Nationally Ranked Homebuilder First America Homes Launches Austin Division, Expands in San Antonio",
           "https://www.firstamericahomes.com/blog/nationally-ranked-homebuilder-first-america-homes-launches-"
           "austin-division-expands-in-san-antonio/",
           "Opened an Austin division and secured homesites in 3 Austin and 9 San Antonio communities, about 900 homes."),
        _n("2026-05-11", "Community Impact",
           "First America Homes introduces home designs for Azalea District at Valley Ranch",
           "https://communityimpact.com/houston/new-caney-porter/real-estate/2026/05/11/first-america-homes-"
           "introduces-home-designs-for-azalea-district-at-valley-ranch/",
           "Released plans for a 203-acre phase in New Caney, 156 first-phase homesites on 40 and 50-foot lots."),
        _n("2026-04-08", "Community Impact", "First America Homes now building homes in Cielo community in Conroe",
           "https://communityimpact.com/houston/conroe-montgomery/development/2026/04/08/first-america-homes-"
           "now-building-homes-in-cielo-community-in-conroe/",
           "Began building in the 256-acre Cielo community in Conroe with six floor plans."),
    ],
    "HOU-067": [
        _n("2026-08-17", "Houston Agent Magazine", "Kresston MPC debuts 60- and 80-foot homesites",
           "https://houstonagentmagazine.com/2026/08/17/kresston-mpc-60-80-foot-homesites/",
           "Named with Toll Brothers to build on 31 80-foot lots at Kresston in Magnolia, pre-sales in early 2027."),
        _n("2026-05-18", "J. Patrick Homes", "Now Selling: New Homes for Sale in Richmond, Texas at The George",
           "https://www.jpatrickhomes.com/news/now-selling-new-homes-for-sale-in-richmond-texas-at-the-george/",
           "Began sales on 60-foot homesites at The George, a 1,500-acre Richmond community planned for 4,000 homesites."),
    ],
    "HOU-061": [
        _n("2026-07-09", "Conroe News",
           "Local Builder Bets on Willis and Montgomery as Affordability Reshapes Texas Housing",
           "https://www.conroenews.org/article/local-builder-bets-on-willis-and-montgomery-as-affordability-"
           "reshapes-texas-housing",
           "Projects 70 closings in 2026, up from about 45 in 2025. Its founder co-founded the outlet's publisher."),
    ],
    "HOU-010": [
        _n("2026-07-30", "Camillo Companies", "Camillo Companies Names Sean Mulroony President of Academy Development",
           CAMILLO_ACAD, "Promoted Sean Mulroony to lead Academy Development, its land arm, which has developed "
                         "over 25,000 lots."),
        _n("2026-04-29", "Camillo Companies", "Camillo Companies Appoints Jomar Ereso as Chief Financial Officer",
           CAMILLO_CFO, "Hired Jomar Ereso as chief financial officer, based in Houston."),
        _n("2026-03-03", "Camillo Companies", "Legend Homes Names John Devens as Houston Division President",
           "https://www.camillocompanies.com/legend-homes-names-john-devens-as-houston-division-president",
           "Promoted John Devens, corporate vice president of construction and purchasing since 2017, to "
           "Houston division president."),
    ],
    "HOU-004": [
        _n("2026-05-18", "DFW Agent Magazine", "InTown Homes launches coastal-inspired Carrol Crest community in Carrollton",
           "https://dfwagentmagazine.com/2026/05/18/intown-homes-carrol-crest-carrollton/",
           "Opened Carrol Crest, a community in Carrollton."),
        _n("2026-03-28", "Realty News Report", "RNR Real Estate Briefs – Texas & more",
           "https://realtynewsreport.com/rnr-real-estate-briefs-texas-more-108/",
           "Sold the 300th home at Kolbe Farms in Spring Branch and launched its final phase of about 100 lots."),
    ],
    "HOU-068": [
        _n("2026-09-10", "Realty News Report", "Fulshear’s Cross Creek West Expands into Luxury Homes", RNR_CCW,
           "Named a builder on 45 and 55-foot homesites in the Cross Creek West north tract, 250 homesites by year end."),
        _n("2026-06-04", "Realty News Report", "4000 Home Community Starts Sales", RNR_GEORGE,
           "Named a builder at The George in Richmond, planned for 4,000 homes, first phase more than 300."),
        _n("2026-05-04", "Realty News Report", "RNR Real Estate Briefs – Texas & more", RNR_TRAILS,
           "One of four builders at The Trails in New Caney, which opened a second phase of 344 lots."),
    ],
    "HOU-066": [
        _n("2026-03-30", "Sandcastle Homes", "Garden Opening: Discover Garden Homes on 34th in Garden Oaks",
           "https://www.sandcastlehouston.com/garden-opening-discover-garden-homes-on-34th-in-garden-oaks/",
           "Opened Garden Homes on 34th, a 12-home gated community in Garden Oaks with two plans."),
    ],
    "HOU-033": [
        _n("2026-09-10", "Realty News Report", "Fulshear’s Cross Creek West Expands into Luxury Homes", RNR_CCW,
           "Joined Cross Creek West in Fulshear in 2026 and builds on 50-foot lots in the new north tract."),
        _n("2026-07-17", "Coventry Homes", "Four New Communities Coming Soon to DFW",
           "https://www.coventryhomes.com/blog/four-new-communities-coming-soon-to-dfw/",
           "Announced four Dallas-Fort Worth communities: Celina, Lavon, Arlington and Royse City."),
        _n("2026-05-04", "Realty News Report", "RNR Real Estate Briefs – Texas & more", RNR_TRAILS,
           "One of four builders at The Trails in New Caney, which opened a second phase of 344 lots."),
    ],
    "HOU-069": [
        _n("2026-09-10", "Realty News Report", "Fulshear’s Cross Creek West Expands into Luxury Homes", RNR_CCW,
           "Builds on 50 and 70-foot homesites in the Cross Creek West north tract, with new models planned."),
        _n("2026-06-04", "Realty News Report", "4000 Home Community Starts Sales", RNR_GEORGE,
           "Started pre-sales on 40-foot lots at The George in Richmond, planned for 4,000 homes."),
    ],
    "HOU-044": [
        _n("2026-05-21", "Community Impact", "10 Katy and Fulshear area housing developments updates",
           "https://communityimpact.com/katy-fulshear/real-estate/10-katy-and-fulshear-area-housing-developments-updates/",
           "Its 156-duplex build-to-rent community in Katy was due to open near the end of the second "
           "quarter of 2026, and the 210-duplex Landing at Katy Pointe in the third."),
    ],
    "HOU-070": [
        _n("2026-09-10", "Realty News Report", "Fulshear’s Cross Creek West Expands into Luxury Homes", RNR_CCW,
           "Joined Cross Creek West in Fulshear in 2026 and builds on 60-foot lots in the new north tract."),
    ],
    "HOU-028": [
        _n("2026-05-16", "Realty News Report", "RNR Real Estate Briefs – Texas & more",
           "https://realtynewsreport.com/rnr-real-estate-briefs-texas-more-115/",
           "Opened Boardwalk Square in Katy, 353 mid-rise apartments that its own affiliates designed and built."),
    ],
    # ---------------------------------------------------------- Dallas-Fort Worth
    "DFW-BTR-010": [
        _n("2026-04-14", "REBusinessOnline",
           "Wan Bridge, Centurion Deliver 201-Unit Build-to-Rent Project in Lewisville, Texas",
           "https://rebusinessonline.com/wan-bridge-centurion-deliver-201-unit-build-to-rent-project-in-lewisville-texas/",
           "Delivered Frontera Shores, 201 build-to-rent townhomes on 35.8 acres in Lewisville."),
        _n("2026-03-04", "REBusinessOnline",
           "Wan Bridge Nears Completion of 166-Unit Build-to-Rent Project in Red Oak, Texas",
           "https://rebusinessonline.com/wan-bridge-nears-completion-of-166-unit-build-to-rent-project-in-red-oak-texas/",
           "Near completion of The Reserve at Red Oak, 166 build-to-rent homes on 18 acres, leasing begun."),
    ],
    "DFW-003a": [
        _n("2026-07-30", "Green Brick Partners (SEC filing)", "Green Brick Partners Announces the Promotion of Jed Dolson to Co-CEO",
           "https://www.sec.gov/Archives/edgar/data/1373670/000162828026050835/ex99pressrelease-dolsonpro.htm",
           "The parent named Jed Dolson, who led Trophy from 2022 to 2024, co-CEO from 15 October 2026."),
        _n("2026-03-13", "Business Wire", "Trophy Signature Homes Announces New Nicholson Ranch Community in Lavon, TX",
           "https://www.businesswire.com/news/home/20260313162521/en/Trophy-Signature-Homes-Announces-New-"
           "Nicholson-Ranch-Community-in-Lavon-TX",
           "Announced Nicholson Ranch in Lavon, 1,635 lots in eight phases on 40 and 50-foot lots."),
        _n("2026-03-13", "Business Wire", "Lone Oak by Trophy Signature Homes Now Open in Alvarado, Texas",
           "https://www.businesswire.com/news/home/20260313035590/en/Lone-Oak-by-Trophy-Signature-Homes-Now-"
           "Open-in-Alvarado-Texas",
           "Opened sales at Lone Oak in Alvarado, its Victory Series on 50-foot lots."),
    ],
    "DFW-029": [
        _n("2026-04-07", "inForney", "New $1.5 Billion Master-Planned Community Meraki Breaks Ground in Forney",
           "https://www.inforney.com/local-news/new-15-billion-master-planned-community-meraki-b/"
           "article_dd5dd26a-5a69-4e52-bff0-0890c40eeda7.html",
           "Named one of five builders at Meraki in Forney, 1,079 acres with 406 first-phase homesites."),
    ],
    "DFW-043": [
        _n("2026-03-02", "Bisnow", "Homebound Closes On $731M Deal For North Texas Expansion: The DFW Deal Sheet",
           "https://www.bisnow.com/news/dallas-ft-worth/deal-sheet/homebound-closes-on-731m-deal-for-north-"
           "texas-expansion-the-dfw-deal-sheet-133470",
           "Acquired more than 1,000 lots in Dallas, Prosper, Flower Mound and Mansfield, about $731 million."),
    ],
    "DFW-BTR-001": [
        _n("2026-07-30", "PR Newswire", "AMH Reports Second Quarter 2026 Financial and Operating Results",
           "https://www.prnewswire.com/news-releases/amh-reports-second-quarter-2026-financial-and-operating-"
           "results-302839489.html",
           "Delivered 651 newly built homes in the second quarter and kept 2026 guidance of 1,300 to 1,500 "
           "wholly owned deliveries."),
    ],
    "DFW-BTR-005": [
        _n("2026-04-21", "Business Wire", "NexMetro Expands Access to BTR Investment Platform",
           "https://www.businesswire.com/news/home/20260421879966/en/NexMetro-Expands-Access-to-BTR-Investment-Platform",
           "Opened its 2026 development fund to wealth platforms to raise capital for new build-to-rent projects."),
    ],
    "DFW-BTR-008": [
        _n("2026-07-30", "Camillo Companies", "Camillo Companies Names Sean Mulroony President of Academy Development",
           CAMILLO_ACAD, "Promoted Sean Mulroony to lead Academy Development, its land arm, which has developed "
                         "over 25,000 lots."),
        _n("2026-07-30", "Camillo Companies",
           "Camillo Companies Welcomes Jeff Montgomery as Architecture Design Director",
           "https://www.camillocompanies.com/camillo-companies-welcomes-jeff-montgomery-as-architecture-design-director",
           "Hired Jeff Montgomery, formerly of Highland Homes and Beazer Homes, to direct Legend Homes and "
           "SimplyHome design."),
        _n("2026-04-29", "Camillo Companies", "Camillo Companies Appoints Jomar Ereso as Chief Financial Officer",
           CAMILLO_CFO, "Hired Jomar Ereso as chief financial officer, based in Houston."),
    ],
    "DFW-021": [
        _n("2026-08-19", "Impression Homes",
           "A First Look at What's Next: Impression Homes Previews the Parkmont Series",
           "https://www.impressionhomes.net/resources/blog/a-first-look-at-whats-next-impression-homes-previews-"
           "the-parkmont-series/",
           "Showed nine prototype homes of a new 50-foot series in Justin, to extend to Celina and Rockwall."),
    ],
}

# Legend Homes' new Houston division president was its vice president of
# construction and purchasing: the role this deck marks as a decision-maker.
HOU_ADD = {
    "HOU-010": [{
        "name": "John Devens",
        "role": "Houston Division President, Legend Homes",
        "linkedin_url": None,
        "source_url": "https://www.camillocompanies.com/legend-homes-names-john-devens-as-houston-division-president",
        "source_evidence": "Named in Camillo Companies' release of 3 March 2026 as Houston Division President "
                           "of Legend Homes, promoted from corporate vice president of construction and "
                           "purchasing, a post he held from 2017.",
    }],
}

# ------------------------------------------------------------------ rule, once
BANDS = re.compile(r"\s*On the bands, a firm with no [^.]*?is a Partly\.")
BANDS_NOTE = "A firm with no published yearly figure reads Partly on printer fit."


def houston_people(targets):
    T = {t["target_id"]: t for t in targets}
    for tid, adds in HOU_ADD.items():
        if tid not in T:
            continue
        have = {p["name"] for p in T[tid]["principals"]}
        for p in adds:
            if p["name"] not in have:
                T[tid]["principals"].insert(0, dict(p))


def finish(D):
    """Headlines, news and the one-rule tidy. Returns a list of problems."""
    bad = []
    T = {t["target_id"]: t for t in D["targets"]}
    for tid, (line, url) in HEADLINE.items():
        t = T.get(tid)
        if not t:
            continue
        if len(line) > 62:
            bad.append("%s headline over 62 characters" % tid)
        t["key_stat"] = line
        if url and url not in {s.get("url") for s in t.get("sources") or []}:
            t.setdefault("sources", []).append({"url": url, "date": None})
    for tid, items in NEWS.items():
        t = T.get(tid)
        if not t:
            continue
        have = {p.get("url") for p in t.get("press") or []}
        keep = [dict(i) for i in items if i["date"] >= NEWS_SINCE and i["url"] not in have]
        for i in keep:
            if "—" in i["what"] or ";" in i["what"]:
                bad.append("%s news line carries an em dash or semicolon" % tid)
        t["news"] = sorted(keep, key=lambda i: i["date"], reverse=True)
    for t in D["targets"]:
        for w in t.get("why") or []:
            if w.get("axis") == "machine_fit":
                w["text"] = BANDS.sub("", w["text"]).strip()
                if not w["text"]:
                    bad.append("%s printer-fit reason empty after the tidy" % t["target_id"])
    return bad
