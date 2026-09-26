# -*- coding: utf-8 -*-
"""Build 72. One rubric, one decision-maker rule, one set of facts per firm.

The Build 71 audit left three things open because each moves a headline count.
They are settled here by the deck's own written rules, not by judgement:

  Printer fit    Yes is about 25 to 400 homes a year, concentrated. Partly is
                 400 to 1,500, purchasing at a parent, or no published yearly
                 figure. No is above 1,500 or a national purchasing desk. A
                 project total is not a yearly figure.
  Track record   Yes is paying for a new building method. Partly is above-code
                 performance, published cycle-time discipline, a certification
                 on every home, or a parent that has paid for a method. Paying an
                 architect, adaptive reuse and a certification on some homes are
                 not on the list, and read No.
  Decision-maker Construction, purchasing, or a division president. The owner at
                 a builder of 400 homes a year or fewer that publishes none of
                 those roles. Whoever signs for equipment at a contractor. Not
                 business development, land, finance, engineering, sales or a
                 parent company's chair.

A firm on both decks keeps one reading of a firm-level fact. Printer fit may
differ between markets where the local volume differs; the method record may not.
"""
import re

DIVPRES = re.compile(r"\b(division|area|regional) president\b|\bpresident, (houston|dallas|dfw|fort worth)",
                     re.I)
SPEC = re.compile(r"construction|purchas|procure|(division|area|regional) president|"
                  r"president, .*(houston|dallas|dfw|fort worth)", re.I)
NO_FIG = "On the bands, a firm with no published yearly figure is a Partly."

# ------------------------------------------------------------------ Houston
# (repeatability, machine_fit, innovation): 3 Yes, 2 Partly, 1 No
HOU_SCORE = {
    "HOU-002": {"machine_fit": 2}, "HOU-016": {"machine_fit": 2}, "HOU-001": {"machine_fit": 2},
    "HOU-131": {"machine_fit": 2}, "HOU-028": {"machine_fit": 2, "innovation": 1},
    "HOU-136": {"machine_fit": 2}, "HOU-026": {"machine_fit": 2}, "HOU-035": {"machine_fit": 2},
    "HOU-146": {"machine_fit": 2}, "HOU-164": {"machine_fit": 2}, "HOU-160": {"machine_fit": 1},
    "HOU-004": {"innovation": 1}, "HOU-133": {"innovation": 1}, "HOU-036": {"innovation": 1},
    "HOU-080": {"innovation": 1}, "HOU-062": {"innovation": 2},
}
HOU_WHY = {
    ("HOU-002", "machine_fit"): "Eighty printed homes on one site, and no yearly figure is published. " + NO_FIG,
    ("HOU-016", "machine_fit"): "Twenty-six homes on one site, and no yearly figure is published. " + NO_FIG,
    ("HOU-001", "machine_fit"): "Builds and holds whole build-to-rent communities, and no yearly figure is "
                                "published. " + NO_FIG,
    ("HOU-131", "machine_fit"): "Three communities and a rank of 41st on a 2023 Houston builder list, and no "
                                "yearly figure is published. " + NO_FIG,
    ("HOU-028", "machine_fit"): "346 units on one site, and no yearly figure is published. " + NO_FIG,
    ("HOU-136", "machine_fit"): "465 homes across two communities is a project total above 400, in the 400 to "
                                "1,500 band.",
    ("HOU-026", "machine_fit"): "Project totals of 240 homes in Cypress and 314 in Conroe, and no yearly figure "
                                "is published. " + NO_FIG,
    ("HOU-035", "machine_fit"): "Five affordable developments in one neighbourhood, and no yearly figure is "
                                "published. " + NO_FIG,
    ("HOU-146", "machine_fit"): "One 17,000 square foot plant serving Texas production builders, and no output "
                                "figure is published. " + NO_FIG,
    ("HOU-164", "machine_fit"): "A single-office contractor serving production builders, and no slab count is "
                                "published. " + NO_FIG,
    ("HOU-160", "machine_fit"): "Two Houston yards inside a national pump fleet, bought at a scale beyond one or "
                                "two printers.",
    ("HOU-006", "machine_fit"): "The Landing at Aliana is 294 units of three-storey garden-style housing on one "
                                "Fort Bend site. No yearly figure is published.",
    ("HOU-028", "innovation"): "Nothing on record about a new building method. Its own affiliates act as "
                               "architect and general contractor.",
    ("HOU-004", "innovation"): "Nothing on record about a new building method. The same owner commissioned OMA "
                               "for POST Houston, which is paying an architect.",
    ("HOU-133", "innovation"): "Nothing on record about paying for a construction method. A hundred printed homes "
                               "were built inside one of its own communities, and Lennar paid for the printing.",
    ("HOU-036", "innovation"): "District-scale design, and no construction method on record.",
    ("HOU-080", "innovation"): "They restored an 1890s building to open Axelrad and took on a National Register "
                               "industrial basilica at The Factory. Adaptive reuse is not a new building method.",
    ("HOU-062", "innovation"): "Every home gets internal and third-party energy verification. That is a "
                               "certification on every home, not a method change.",
}
HOU_PERSON = {
    # not a construction, purchasing or division role
    ("HOU-132", "Brad Conlon"): {"decider": False},
    ("HOU-068", "Diane Danilov"): {"decider": False},
    ("HOU-028", "Raymond Gabriele"): {"decider": False},
    ("HOU-129", "Hikmat Zerbe"): {"decider": False},
    # the Dallas-Fort Worth card cites his move to Bluprint Ventures
    ("HOU-168", "Matt McGhee"): {"departed": True, "decider": False},
}

# ------------------------------------------------------------------ Dallas-Fort Worth
HOU_CENTURY = "https://www.housingwire.com/articles/century-communities-q2-2026-strategy/"
DFW_VERDICT = {
    ("DFW-042", "innovation"): ("No", "EcoSmart and Energy Star appear on some communities and listings, which is a "
                                      "certification on some homes, not every home. Nothing on record about a new "
                                      "wall method."),
    ("DFW-AD-001", "machine_fit"): ("Partly", "About seven structures by May 2026, per Community Impact, is under "
                                              "the 25 to 400 band."),
    ("DFW-BTR-006", "machine_fit"): ("Partly", "157 homes is the total for its first North Texas project, not a "
                                               "yearly figure. " + NO_FIG),
    # A company-wide figure is the figure when no DFW one is published, as it is for
    # Landon, Our Country, Sandlin and Chesmar. Above 1,500 reads No.
    ("DFW-056", "machine_fit"): ("No", "2,286 closings in 2025, company-wide across several states, is above "
                                       "1,500. No DFW figure is published."),
    ("DFW-048", "machine_fit"): ("Yes", "286 closings in 2025 per BUILDER, company-wide across Texas and "
                                        "Tennessee, sits in the 25 to 400 band."),
    ("DFW-TR-011", "innovation"): ("No", "No record of paying for an unproven method. Manufacturing wall panels is "
                                         "this industry's ordinary business rather than an adoption."),
    ("DFW-060", "innovation"): ("Partly", "Record 112-day cycle and a 5 percent direct-cost cut, per HousingWire on "
                                          "its Q2 2026 results, but no change of method."),
    ("DFW-TR-026", "machine_fit"): ("Partly", "$2 billion in construction volume and more than 700 employees on the "
                                              "firm's own count. One or two printers would be a line inside a "
                                              "business that size rather than the business."),
    ("DFW-TR-032", "innovation"): ("No", "Nothing on record about a new wall method. Its line includes prestressed "
                                         "wall panels, which is its normal product."),
}
DFW_SOURCES = {
    "DFW-060": [HOU_CENTURY],
    "DFW-TR-026": ["https://www.harveycleary.com/about-us/"],
    "DFW-TR-001": ["https://www.tealstonelp.com/who-we-are/"],
    "DFW-TR-074": ["https://futureframeusa.com/meet-our-team/"],
}
DFW_PERSON = {
    ("DFW-TR-040", "Tim Hughes"): {"role": "Senior Vice President, Construction Management"},
    ("DFW-TR-042", "Mark Grzesiak"): {"decider": False, "departed": True},
    ("DFW-TR-031", "Robb Harrington"): {"decider": False},
    ("DFW-TR-086", "Sergio"): {"decider": False},
    ("DFW-048", "Jim Lemming"): {"decider": False},
    ("DFW-024", "Kathy Britton"): {"decider": False},
    ("DFW-073", "Aaron Graham"): {"decider": False},
    ("DFW-BTR-008", "Dan Miller"): {"decider": False},
    ("DFW-BTR-008", "Matt Hansen"): {"decider": False},
    ("DFW-044", "Matthew R. Zaist"): {"decider": False},
    ("DFW-BTR-001", "Brent Landry"): {"decider": False},
}
# The firms' own team pages name these people. The Houston deck carries them.
DFW_ADD = {
    "DFW-TR-001": [
        {"name": "Gary Engasser", "role": "President", "decider": True,
         "source_url": "https://www.tealstonelp.com/who-we-are/",
         "source_evidence": "Named on the firm's own Who We Are page as President."},
        {"name": "Rick Callihan", "role": "Vice President",
         "source_url": "https://www.tealstonelp.com/who-we-are/",
         "source_evidence": "Named on the firm's own Who We Are page as Vice President."},
    ],
    "DFW-TR-074": [
        {"name": "Shane McCullough", "role": "President", "decider": True,
         "source_url": "https://futureframeusa.com/meet-our-team/",
         "source_evidence": "Named on the firm's own Meet Our Team page as President."},
        {"name": "Glen Gilbert", "role": "General Manager", "decider": True,
         "source_url": "https://futureframeusa.com/meet-our-team/",
         "source_evidence": "Named on the firm's own Meet Our Team page as General Manager."},
    ],
}
DFW_FIELDS = {
    ("DFW-TR-001", "people_absent"): None,
    ("DFW-TR-074", "team_note"): "Joe Mazzenga's LinkedIn profile shows him at Future Frame USA only from "
                                 "September 2021 to May 2022.",
}


def _principal(tid, name, T):
    ps = [p for p in T[tid]["principals"] if p.get("name") == name]
    if len(ps) != 1:
        raise SystemExit("audit8: %s has %d principals named %s" % (tid, len(ps), name))
    return ps[0]


def divisions(targets):
    """A division president at a builder is a decision-maker, on both decks."""
    for t in targets:
        if t.get("group") in ("trade", "out"):
            continue
        for p in t["principals"]:
            if DIVPRES.search(p.get("role") or "") and not p.get("departed") \
                    and not re.search(r"formerly|ex-", p.get("role") or "", re.I):
                p["decider"] = True


def houston_late(targets):
    T = {t["target_id"]: t for t in targets}
    for (tid, name), f in HOU_PERSON.items():
        _principal(tid, name, T).update(f)
    divisions(targets)


def houston_why(targets):
    """Reasons for the verdicts the rubric moved. Run after every text edit."""
    T = {t["target_id"]: t for t in targets}
    V = {3: "Yes", 2: "Partly", 1: "No"}
    for (tid, ax), txt in HOU_WHY.items():
        w = [x for x in T[tid]["why"] if x["axis"] == ax]
        if len(w) != 1:
            raise SystemExit("audit8: %s has no %s reason" % (tid, ax))
        want = HOU_SCORE.get(tid, {}).get(ax)
        if want and w[0]["verdict"] != V[want]:
            raise SystemExit("audit8: %s %s reads %s, not %s" % (tid, ax, w[0]["verdict"], V[want]))
        w[0]["text"] = txt


def dfw_people(targets):
    T = {t["target_id"]: t for t in targets}
    for tid, adds in DFW_ADD.items():
        have = {p["name"] for p in T[tid]["principals"]}
        for p in adds:
            if p["name"] not in have:
                T[tid]["principals"].insert(0, dict(p, linkedin_url=None, li_evidence=None))
    for (tid, name), f in DFW_PERSON.items():
        _principal(tid, name, T).update(f)
    for (tid, k), v in DFW_FIELDS.items():
        T[tid][k] = v
    divisions(targets)
    # The owner is the mark only at a builder of 400 homes a year or fewer.
    for t in targets:
        if t.get("group") in ("trade", "out") or (t.get("vol") or 0) <= 400:
            continue
        for p in t["principals"]:
            if p.get("decider") and not SPEC.search(p.get("role") or ""):
                p["decider"] = False


# ------------------------------------------------------------------ dates
# A date prints beside each source, press item and capital line. Seventeen
# Houston sources carried 2026-09-11, the day they were read, and several carried
# a year with -01-01 standing in for an unknown day. Both read as publication
# dates. A date the source does not give is left off.
DATE_FIX = {
    # CastleRock's own card: the deal was announced on 10 August 2021.
    ("HOU-022", "capital_signals"): ("2021-01-01", "2021-08-10"),
}
RETRIEVED = {"2026-09-11"}


def dates(D):
    n = 0
    for t in D["targets"]:
        for key in ("sources", "press", "capital_signals"):
            for x in t.get(key) or []:
                if not isinstance(x, dict) or not x.get("date"):
                    continue
                fix = DATE_FIX.get((t["target_id"], key))
                if fix and x["date"] == fix[0]:
                    x["date"] = fix[1]
                elif x["date"] in RETRIEVED or x["date"].endswith("-01-01"):
                    x["date"] = None
                    n += 1
    return n


# ------------------------------------------------------------------ Build 73
# BUILDER's 2026 Local Leaders table for Dallas-Fort Worth counts 2025 closings.
# It replaces the 2025 table's 2024 figures for the nine firms on both. Perry is
# not in the 2026 top ten and keeps its 2024 figure from the 2025 table.
LL26 = "https://www.builderonline.com/land/local-leaders-list/2026/dallas-fort-worth-arlington-tx/"
DFW_CLOSINGS = {
    "DFW-001": (7058, 7058, 2025, "BUILDER Local Leaders 2026, DFW", None),
    "DFW-002": (5724, 5724, 2025, "BUILDER Local Leaders 2026, DFW", None),
    "DFW-003": (3196, 3196, 2025, "BUILDER Local Leaders 2026, DFW, all Green Brick brands", None),
    "DFW-004": (1742, 1742, 2025, "BUILDER Local Leaders 2026, DFW", None),
    "DFW-005": (1810, 1810, 2025, "BUILDER Local Leaders 2026, DFW", None),
    "DFW-006": (1833, 1833, 2025, "BUILDER Local Leaders 2026, DFW", None),
    "DFW-007": (1083, 1083, 2025, "BUILDER Local Leaders 2026, DFW", None),
    "DFW-008": (1034, 1034, 2025, "BUILDER Local Leaders 2026, DFW", None),
    "DFW-009": (1289, 1289, 2025, "BUILDER Local Leaders 2026, DFW", None),
    "DFW-055": (889, 889, 2025, "BUILDER Local Leaders 2026, DFW", None),
}
for _tid in DFW_CLOSINGS:
    DFW_SOURCES.setdefault(_tid, []).append(LL26)
for _tid in ("DFW-003a", "DFW-014", "DFW-038"):
    DFW_SOURCES.setdefault(_tid, []).append(LL26)
DFW_SOURCES.setdefault("DFW-003", []).append(
    "https://www.sec.gov/Archives/edgar/data/1373670/000162828026050835/ex99pressrelease-dolsonpro.htm")
DFW_SOURCES.setdefault("DFW-003a", []).append(
    "https://www.sec.gov/Archives/edgar/data/1373670/000162828026050835/ex99pressrelease-dolsonpro.htm")
DFW_PERSON[("DFW-003", "Jed Dolson")] = {
    "role": "President and Chief Operating Officer. Co-Chief Executive Officer from 15 October 2026",
    "source_evidence": "Named on the leadership page as President and Chief Operating Officer. Green Brick's "
                       "30 July 2026 release, filed with the SEC, names him Co-Chief Executive Officer from "
                       "15 October 2026."}


# ------------------------------------------------------------------ ICON's own record
# Rewritten from ICON's newsroom, NASA, the Army and the trade press, read on
# 25 September 2026. The Build 71 line was cut because it said ICON had built
# nothing outside the Austin area. It has: a NASA habitat in Houston and Army
# barracks in El Paso and Louisiana. Every fact here has a link below it.
ICON_LINE = ("ICON's published record: housing in Central Texas, Army barracks in Texas and Louisiana, a NASA "
             "habitat in Houston, and the terms of the Titan, its first system sold to outside builders.")
ICON_FACTS = [
    ["Titan, on the record",
     "Announced 11 March 2026. ICON states multi-storey wall systems at roughly $20 a square foot, a $5,000 "
     "reservation deposit, training from the third quarter of 2026 and first deliveries in early 2027. Its "
     "reservation page publishes no price. Axios and All3DP report a price from $899,000, and The Real Deal "
     "reports leases first, with sales from the first quarter of 2027. Jason Ballard told Builder the target "
     "is small and mid-sized builders."],
    ["The first reservations",
     "The Real Deal names Ghost Factory, Cole Klein Builders and Moderne Development among the firms that "
     "have reserved a Titan. Cole Klein is the Houston builder of Zuri Gardens, which HiveASMBLD prints."],
    ["Wolf Ranch, Georgetown",
     "100 homes with Lennar, designed by BIG and printed on Vulcan. Lennar announced the community on 26 "
     "October 2021, and printing was under way by November 2022. Eight floor plans of 1,574 to 2,112 square "
     "feet, from the mid $400,000s. ICON calls it its first completed residential community, sold with "
     "Lennar's own mortgage arm (June 2026)."],
    ["Austin and the Hill Country",
     "100 more homes under way at Community First! Village (December 2024). Affordable one-bedroom homes "
     "from $195,000 and about a dozen two- and three-bedroom homes at Mueller, printing from July 2025. Eight "
     "homes at Wimberley Springs from the upper $800,000s (July 2024)."],
    ["The Army",
     "Ten barracks at Fort Bliss, El Paso, 78,000 square feet for up to 560 soldiers, under a $62.8 million "
     "Army contract. ICON announced delivery on 28 July 2026. Stars and Stripes reported two of the ten open "
     "that day and the rest due in September. Both ICON and the Army call it the largest deployment of "
     "robotic construction for the Department of War. A $67.9 million award at Fort Polk, Louisiana followed "
     "in March 2026, with vertical construction scheduled for September 2026."],
    ["ICON Prime",
     "A government division launched on 14 April 2026, with Will Hurd as its president. ICON states more "
     "than $360 million in government contracts."],
    ["The company",
     "More than 245 homes and structures completed, per ICON in March 2026, and its site now counts 263 structures built. It filed to lay off 114 people, "
     "more than a quarter of its staff, in January 2025, and closed a $56 million Series C led by Norwest and "
     "Tiger Global in February 2025, per TechCrunch. Jason Ballard is co-founder and chief executive."],
]
ICON_LOCAL = {
    "Houston": ["Houston",
        "ICON printed Mars Dune Alpha, a 1,700 square foot habitat for NASA at Johnson Space Center, and "
        "delivered it in 2021. NASA's second year-long crew mission inside it runs from 19 October 2025 to 31 "
        "October 2026. ICON has published no housing in Houston: its own site says the homes it has sold are "
        "in Central and West Texas. HiveASMBLD has repeat production work inside Greater Houston, and PERI "
        "printed a house inside the city limits."],
    "Dallas-Fort Worth": ["Dallas-Fort Worth",
        "ICON has published no project in the metro: its own site says the homes it has sold are in Central "
        "and West Texas. Its one Houston structure is Mars Dune Alpha, a 1,700 square foot habitat for NASA at "
        "Johnson Space Center, delivered in 2021. In DFW, Black Buffalo printed a house at 100 W. Bolt St., "
        "Fort Worth, in May 2024, and PRINT3D Technologies of Allen sells printed houses in North Texas."],
}
ICON_LINKS = [
    ["ICON on the Titan launch, 11 March 2026",
     "https://www.iconbuild.com/newsroom/icon-announces-first-commercial-rollout-of-its-3d-printing-construction-technology-for-builders"],
    ["Titan reservations", "https://reservations.iconbuild.com/"],
    ["Axios on the Titan price, 11 March 2026",
     "https://www.axios.com/local/austin/2026/03/11/3d-printing-company-icon-expands-austin"],
    ["All3DP on what the price includes, 13 March 2026",
     "https://all3dp.com/4/icons-899k-titan-construction-printer-puts-multistory-construction-in-your-hands-shipping-2027/"],
    ["The Real Deal on leases and the first reservations, March 2026",
     "https://therealdeal.com/texas/2026/03/12/icon-opens-3d-home-printing-tech-to-outside-builders/"],
    ["Builder on ICON's platform for outside builders, 11 March 2026",
     "https://www.builderonline.com/design/technology/icons-next-phase-building-a-scalable-platform-for-3d-printed-housing/"],
    ["Lennar announces Wolf Ranch, 26 October 2021",
     "https://newsroom.lennar.com/2021-10-26-Lennar-To-Build-Worlds-Largest-Neighborhood-Of-3D-Printed-Homes-With-ICON"],
    ["ICON and Lennar, Wolf Ranch under way, 10 November 2022",
     "https://www.iconbuild.com/newsroom/icon-and-lennar-announce-community-of-3d-printed-homes-is-now-underway-in-georgetown-tx"],
    ["ICON and Wells Fargo, 2 June 2026",
     "https://www.iconbuild.com/newsroom/wells-fargo-named-as-an-icon-preferred-home-mortgage-lender-offering-incentives-to-buyers-of-3d-printed-homes"],
    ["ICON at Community First! Village, 19 December 2024",
     "https://www.iconbuild.com/newsroom/icon-announces-construction-is-underway-for-more-3d-printed-homes-to-serve-the-chronically-homeless-in-texas"],
    ["ICON at Mueller, 31 July 2025",
     "https://www.iconbuild.com/newsroom/icon-releases-affordable-3d-printed-homes-for-sale-and-breaks-ground-in-austins-mueller-community"],
    ["ICON at Wimberley Springs, 16 July 2024",
     "https://www.iconbuild.com/newsroom/new-icon-homes-coming-to-wimberley-texas-and-available-for-sale"],
    ["ICON on Fort Bliss delivery, 28 July 2026",
     "https://www.iconbuild.com/newsroom/icon-delivers-largest-robotic-construction-deployment-in-dow-history-at-fort-bliss"],
    ["U.S. Army on the Fort Bliss barracks, 30 July 2026",
     "https://www.army.mil/article/294240/fort_bliss_unveils_new_3d_printed_barracks"],
    ["Stars and Stripes on the opening, 28 July 2026",
     "https://www.stripes.com/branches/army/2026-07-28/fort-bliss-3-d-barracks-opening-22393339.html"],
    ["ICON at Fort Polk, 29 June 2026", "https://www.iconbuild.com/newsroom/fort-polk-ground-break"],
    ["ICON Prime, 14 April 2026",
     "https://www.iconbuild.com/newsroom/icon-launches-icon-prime-a-dedicated-government-division-focused-on-military-intelligence-and-space-applications-to-accelerate-robotic-construction-for-national-security"],
    ["ICON's sold homes, Central and West Texas", "https://www.iconbuild.com/build-with-us"],
    ["NASA on the second Mars Dune Alpha crew, 5 September 2025",
     "https://www.nasa.gov/missions/analog-field-testing/chapea/nasa-announces-chapea-crew-for-year-long-mars-mission-simulation/"],
    ["ICON on Mars Dune Alpha, 6 August 2021",
     "https://www.iconbuild.com/newsroom/icon-3d-prints-the-first-simulated-mars-surface-habitat-for-nasa-designed-by-renowned-architecture-firm-big-bjarke-ingels-group"],
    ["TechCrunch on the 2025 layoff, 9 January 2025",
     "https://techcrunch.com/2025/01/09/icon-a-builder-of-3d-printed-homes-last-valued-around-2-billion-cuts-about-25-of-staff/"],
    ["TechCrunch on the Series C, 14 February 2025",
     "https://techcrunch.com/2025/02/14/icon-a-pioneer-in-3d-home-printing-raises-56m-led-by-norwest-tiger-global/"],
]


def icon_record(D, place, lennar_fact):
    D["icon_record"] = {"line": ICON_LINE,
                        "facts": [list(f) for f in ICON_FACTS[:2]] + [lennar_fact]
                                 + [list(f) for f in ICON_FACTS[2:]] + [list(ICON_LOCAL[place])],
                        "links": [list(link) for link in ICON_LINKS]}


# ------------------------------------------------------------------ competitors, Build 73
TRD = "https://therealdeal.com/texas/2026/03/12/icon-opens-3d-home-printing-tech-to-outside-builders/"
VONPERRY22 = ("https://dallasinnovates.com/dallas-startup-von-perry-looks-to-raise-2m-to-build-more-"
              "3d%E2%80%91printed-homes-across-texas/")


def competitors73(D):
    for c in D.get("competitors", []):
        if c["name"] == "Mighty Buildings":
            c["line"] = "Put itself up for sale in January 2025. LUMUS now owns its technologies."
            c["facts"] = [["What happened",
                           "Headcount cut, then the whole company offered for sale in January 2025, having "
                           "raised over $150 million. Its own site now says it is a brand of LUMUS Inc., which "
                           "acquired its technologies."]]
            c["links"] = [["Their site, now a LUMUS brand", link[1]] if "mightybuildings.com" in link[1] else link
                          for link in c.get("links", [])]
        if c["name"] == "Von Perry":
            c["status"] = "last reported 2022"
            c["facts"] = [["The house",
                           "About 1,700 square feet and three bedrooms near Nevada, in Collin County, begun in "
                           "December 2021 on a Total Kustom printer. Dallas Innovates reported in August 2022 a "
                           "switch to geopolymer concrete for the Texas heat and a target to finish by the end of "
                           "October 2022. No completion has been published."]] + \
                         [f for f in c["facts"] if f[0] != "The house"]
            if not any(link[1] == VONPERRY22 for link in c["links"]):
                c["links"].append(["Dallas Innovates on the geopolymer switch, 31 August 2022", VONPERRY22])

HOU_SOURCES73 = {
    "HOU-002": [TRD],
    "HOU-001": ["https://www.businesswire.com/news/home/20260318639354/en/Wan-Bridge-Launches-Frontera-Shores-Elevating-Build-To-Rent-Living-in-Lewisville",
                "https://wanbridge.com/tx/houston/eldridge-tower/"],
    "HOU-011": ["https://www.globenewswire.com/news-release/2026/08/05/3339652/0/en/howard-hughes-holdings-inc-reports-second-quarter-2026-results.html"],
}
DFW_SOURCES.setdefault("DFW-BTR-010", []).append(
    "https://www.businesswire.com/news/home/20260318639354/en/Wan-Bridge-Launches-Frontera-Shores-Elevating-Build-To-Rent-Living-in-Lewisville")
