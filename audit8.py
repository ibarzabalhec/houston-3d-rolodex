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
