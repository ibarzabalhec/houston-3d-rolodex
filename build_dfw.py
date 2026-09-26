# -*- coding: utf-8 -*-
"""Build 68. The Dallas-Fort Worth deck.

The first draft of DFW came as a research pack (internal/inputs/dfw-pack/, written by a separate
research tool): 130 firm records, a supply panel, the field, a market block and
Census permits. It was checked with the same four gates as Houston
(marketcheck.py). Seven readers resolved what failed, and five editors rewrote
every card in the Houston deck's house style (internal/inputs/dfw-edit/cards.json). This file
applies all of it and writes build/dfw-data.json in the shape the page reads.

What it holds to, the same as Houston:
  - a verdict is Yes, Partly or No per count, and the section follows the holds;
  - a LinkedIn link is kept only where a search result showed the URL with the
    person's name and the firm (internal/inputs/dfw-edit/linkedin_verified.json);
  - no aggregator, no encyclopedia, no URL that was not seen;
  - a closings figure says whose figure it is.
The build fails on any of it.
"""
import collections
import copy
import json
import pathlib
import re

import audit7 as AUDIT7
import audit8 as AUDIT8
import audit9 as AUDIT9
import audit12 as AUDIT12
import audit13 as AUDIT13
import policy as POLICY
from version import BUILD, DATE
import jsonio
import paths

AUDIT8.DFW_VERDICT.update(AUDIT9.DFW_VERDICT)
for _k, _v in AUDIT9.DFW_SOURCES.items():
    AUDIT8.DFW_SOURCES.setdefault(_k, []).extend(_v)
ROOT = pathlib.Path(__file__).parent
PACK = jsonio.read(paths.DFW_PACK / "03_dfw-data.json")
EDIT = {c["target_id"]: c for c in jsonio.read(paths.DFW_EDIT / "cards.json")}
LIV = jsonio.read(paths.DFW_EDIT / "linkedin_verified.json")
HOU = jsonio.read(paths.HOU_DATA)
TODAY = DATE

V = {"Yes": "clear", "Partly": "partial", "No": "fail"}
S = {"clear": 3, "partial": 2, "fail": 1}
W = {"clear": "Yes", "partial": "Partly", "fail": "No"}
AXES = ("repeatability", "machine_fit", "innovation")
TITLE = {w["axis"]: w["title"] for w in HOU["targets"][0]["why"]}


def _n(u):
    return (u or "").strip().rstrip("/").lower()


LIVN = {_n(k): (k, v) for k, v in LIV.items()}

# ------------------------------------------------------------------ URLs
# A URL with a note pasted after it, from the pack's phone fields.
def clean_url(u):
    if not isinstance(u, str):
        return u
    u = u.strip()
    m = re.match(r"^(https?://\S+)\s+\(.*\)$", u)
    return m.group(1) if m else (u if u.startswith("http") else None)


# Replacements for links that failed and were found again at a working address.
URL_FIX = {
    "https://www.reuters.com/world/us/worlds-largest-3d-printed-neighborhood-nears-completion-texas-2024-08-08/":
        "https://finance.yahoo.com/news/worlds-largest-3d-printed-neighborhood-060654334.html",
    "https://investors.amh.com/": "https://investors.amh.com/home/default.aspx",
    "https://investors.tripointehomes.com/divisions/": "https://investors.tripointehomes.com/divisions/default.aspx",
    "https://www.avillarailhead.com/": "https://www.avillarailhead.com/mapsanddirections",
    "https://www.energy.gov/sites/default/files/2015/06/f22/DOE_ZEH_CarlFranklin_09-20-14.pdf":
        "https://www.energy.gov/sites/prod/files/2015/06/f22/DOE_ZEH_CarlFranklin_09-20-14.pdf",
    "https://erwss.com/construction-company-texas/kaufman-concrete/":
        "https://erw-sitesolutions.com/construction-company-texas/kaufman-concrete-foundations-texas/",
    "https://daltxrealestate.com/san-antonio-company-finds-a-sweet-spot-with-first-north-texas-project/":
        "https://candysdirt.com/2022/07/10/san-antonio-company-finds-a-sweet-spot-with-first-north-texas-project/",
}
# Links that are gone, banned, or were never seen.
DROP_URL = re.compile(r"buildzoom\.com|zoominfo|rocketreach|theorg\.com|bbb\.org|carlfranklinhomes\.com|sekisuihouse-global\.com/common/pdf/2026_1_6_en\.pdf|"
                      r"star-telegram\.com/news/local/fort-worth/article288851185|erwss\.com/contact")


def fix(u):
    u = clean_url(u)
    if not u:
        return None
    u = URL_FIX.get(u, u)
    return None if DROP_URL.search(u) else u


# ------------------------------------------------------ cross-market parity
# A firm on both decks keeps one track record: paying for a new building method
# is a fact about the firm, not about the metro. Where the DFW draft and the
# Houston card disagree, the Houston card is the one that was audited.
def _hwhy(hid, axis="innovation"):
    t = next(x for x in HOU["targets"] if x["target_id"] == hid)
    w = next(x for x in t["why"] if x["axis"] == axis)
    return w["verdict"], w["text"]


PARITY = {
    "DFW-002": ("HOU-166", ["https://newsroom.lennar.com/2021-10-26-Lennar-To-Build-Worlds-Largest-Neighborhood-Of-3D-Printed-Homes-With-ICON",
                            "https://newsroom.lennar.com/2022-11-10-LENNAR-ANNOUNCES-VISIONARY-COMMUNITY-OF-3D-PRINTED-HOMES-WITH-ICON-IS-NOW-UNDERWAY-IN-GEORGETOWN,-TX"]),
    "DFW-007": ("HOU-167", ["https://www.housingwire.com/articles/why-builders-firstsource-bought-icg-and-why-pulte-sold-it/",
                            "https://www.constructiondive.com/news/construction-robot-ai-florida-pultegroup/740963/"]),
    "DFW-BTR-010": ("HOU-001", ["https://www.businesswire.com/news/home/20250312098923/en/Wan-Bridge-Expands-Texas-Footprint-with-Five-New-Projects",
                                "https://keycrew.co/journal/wan-bridge-groups-ting-qiao-on-elevating-the-build-to-rent-market/"]),
    "DFW-CH-001": ("HOU-133", ["https://www.hillwoodcommunities.com/blog/the-future-of-housing-3d-printed-homes-in-georgetown-texas/"]),
    "DFW-TR-040": ("HOU-156", ["https://www.deebrowncompanies.com/services"]),
    "DFW-TR-030": ("HOU-144", []),
    "DFW-TR-031": ("HOU-141", []),
}
# An editor's move that departs from how Houston reads the same kind of firm: a
# precast or panel plant making its normal product is not a new method.
REVERT = {"DFW-TR-092": ("innovation", "Partly",
                          "Its core product is offsite wall panels, including StoPanel systems. A panel "
                          "shop making its normal product reads Partly, as Builders FirstSource's panel "
                          "plants do.")}

# Build 68 edits to the edited cards: (card, old, new), each found exactly once.
EDITS = [
    ("DFW-TR-002", " BuildZoom shows past contractor licenses in Fort Worth and Dallas.", ""),
    ("DFW-TR-052", ", and BuildZoom lists a Fort Worth address", ""),
    ("DFW-TR-052", ", and BuildZoom lists an address at 3629 Jockey Dr, Fort Worth", ""),
    ("DFW-TR-052", "Fort Worth address, installs across Texas", "Installs across Texas"),
    # Nothing publishes these; each was cut rather than sourced.
    ("DFW-003d", "Green Brick owns 90 percent of it, per SEC summary materials, and supplies",
     "Green Brick supplies"),
    ("DFW-073", " Its site markets luxury homes at about $1.8 million to over $2.6 million.", ""),
    ("DFW-TR-085", " Taft Homes construction manager Dustin Shaffer comments on its Grand Prairie crews.", ""),
    ("DFW-TR-085", " ERW's contact page lists 972-741-8900 for Kaufman Concrete.", ""),
    ("DFW-TR-081", " David Andrews was a master brick mason for 30 years before the firm began.", ""),
    ("DFW-030", " Community sales line 469-438-2466.", ""),
    ("DFW-053", " The Dallas division lists an online sales line, a Customer Care line at 469-252-2200 "
                "and a Frisco office at 6735 Salt Cedar Way.", ""),
]
# A person whose only page is an aggregator is not a contact.
DROP_PEOPLE = {("DFW-TR-001", "Gary Engasser"), ("DFW-TR-083", "Matt Schultheis")}
# A name the cited page spells differently, or gives in full.
NAME_FIX = {("DFW-008", "Randal Van Wolfswinkel"): "Randall Van Wolfswinkel",
            ("DFW-TR-081", "Jacob"): "Jacob Andrews", ("DFW-TR-081", "David"): "David Andrews"}
# The page a figure on the card came from, where the card did not cite it.
SOURCE_ADD = {
    "DFW-020": ["https://www.builderonline.com/firms/historymaker-homes/"],
    "DFW-029": ["https://www.builderonline.com/firms/american-legend-homes/"],
    "DFW-045": ["https://www.builderonline.com/firms/pacesetter-homes/"],
    "DFW-079": ["https://www.builderonline.com/firms/william-ryan-homes/"],
    "DFW-021": ["https://www.builderonline.com/firms/impression-homes/"],
    "DFW-025": ["https://www.builderonline.com/builder-100/builder-100-list/2026/?next=true"],
    "DFW-033": ["https://www.builderonline.com/builder-100/builder-100-list/2026/"],
    "DFW-026": ["https://www.builderonline.com/firms/our-country-homes_o/"],
    "DFW-022": ["https://www.builderonline.com/firms/megatel-homes_o/"],
    "DFW-027": ["https://www.builderonline.com/firms/sandlin-homes_o/"],
    "DFW-030": ["https://www.builderonline.com/firms/stonehollow-homes_o/"],
    "DFW-032": ["https://www.builderonline.com/firms/landon-homes/"],
    "DFW-041": ["https://www.builderonline.com/firms/chesmar-homes/"],
    "DFW-048": ["https://www.builderonline.com/firms/partners-in-building"],
    "DFW-056": ["https://www.builderonline.com/firms/drees-homes/"],
    "DFW-061": ["https://www.builderonline.com/firms/castlerock-communities/"],
    "DFW-040": ["https://www.builderonline.com/firms/brightland-homes_o"],
    "DFW-BTR-010": ["https://www.businesswire.com/news/home/20250429743086/en/Wan-Bridge-and-Centurion-American-Deliver-Newest-Build-to-Rent-Community-Offering-in-North-Texas"],
    "DFW-BTR-001": ["https://www.sec.gov/Archives/edgar/data/1562401/000156240125000063/amh0630258kexhibit992.htm"],
    "DFW-042": ["https://www.houstonchronicle.com/business/real-estate/article/McGuyer-Homebuilders-acquired-by-Florida-builder-16468304.php"],
    "DFW-031": ["https://paultaylorhomes.com/community/lyons-crest-estates/"],
    "DFW-TR-001": ["https://www.strlco.com/wp-content/uploads/2021/11/Tealstone_Brochure.pdf"],
    "DFW-037": ["https://www.cheldanhomes.com/communities/trail-creek"],
    "DFW-TR-030": ["https://wells.build/contact/locations/hillsboro-texas/"],
    "DFW-BTR-005": ["https://fortworthinc.com/real-estate/lancarte-brokers-sale-for-new-315-home-nexmetro-avilla-commu/"],
}
PHONE_FIX = {"DFW-055": ("9726194200", "https://www.mihomes.com/agent/dallas-fort-worth-metroplex/agent-info",
                         "Line for real estate agents")}
PEOPLE_ABSENT = {
    "DFW-TR-001": "Its own pages name no officer. The one name found elsewhere rests on a contractor "
                  "directory this deck does not cite.",
    "DFW-CH-004": "The community's own site names no officer of its developer.",
}
# A card with no DFW presence on any page it controls.
OFF = {"DFW-TR-052": "No page the firm controls gives a DFW address, and its published phone "
                     "is a Rio Grande Valley number."}
OFF.update(AUDIT12.DFW_OFF)

# ------------------------------------------------------------------ groups
# Section follows the holds, as on Houston. Fixed sections are what a firm is.
# Build-to-rent operators that build their own homes are builders here, as
# Camillo, Clay and RSK are in Houston. Owners that buy from a builder stay with
# the land owners.
# CastleRock is run from Houston and sits in One gap on the Houston deck. A firm
# on both decks reads the same on both, so it leaves the national section here.
GROUP_FIX = {"DFW-002": "icon", "DFW-061": "b"}

# A brand and its parent, or a masterplan and its developer, that print one
# office line. Each group shares a number on purpose; the page says whose it is.
SHARED_PHONE = [
    {"DFW-029", "DFW-036"},                                   # American Legend, Belclaire
    {"DFW-024", "DFW-010"},                                   # Britton, Perry
    {"DFW-003", "DFW-003a", "DFW-003b", "DFW-003c", "DFW-014"},  # Green Brick and its brands
    {"DFW-CH-001", "DFW-CH-020"},                             # Hillwood, Lilyana
    {"DFW-CH-018", "DFW-CH-011", "DFW-CH-019"},               # Huffines, Serenade, Solterra
    {"DFW-073", "DFW-004"},                                   # Huntington, Highland
    {"DFW-CH-014", "DFW-CH-012"},                             # Johnson Development, Trinity Falls
    {"DFW-CH-016", "DFW-CH-017"},                             # Mosaic, Tellus
    {"DFW-031", "DFW-048"},                                   # Paul Taylor, Partners in Building
    {"DFW-CH-002", "DFW-CH-005"},                             # Republic Property, Walsh
]
BY_HOLDS = {"DFW-BTR-001", "DFW-BTR-005", "DFW-BTR-006", "DFW-BTR-007", "DFW-BTR-008",
            "DFW-BTR-009", "DFW-BTR-010"}
TIER = {"adopter": "P", "icon": "I", "channel": "M", "national": "N", "trade": "W",
        "creative": "X", "a": "A", "b": "B", "out": "C"}

# ------------------------------------------------------------------ closings
# (low, high, year, source, what it covers or None for a DFW figure)
LL = "https://www.builderonline.com/land/local-leaders-list/2025/dallas-fort-worth-arlington-tx/"
CLOSINGS = {
    "DFW-001": (8191, 8191, 2024, "BUILDER Local Leaders 2025, DFW", None),
    "DFW-002": (5513, 5513, 2024, "BUILDER Local Leaders 2025, DFW", None),
    "DFW-003": (2899, 2899, 2024, "BUILDER Local Leaders 2025, DFW, all Green Brick brands", None),
    "DFW-004": (2115, 2115, 2024, "BUILDER Local Leaders 2025, DFW", None),
    "DFW-005": (2036, 2036, 2024, "BUILDER Local Leaders 2025, DFW", None),
    "DFW-006": (1589, 1589, 2024, "BUILDER Local Leaders 2025, DFW", None),
    "DFW-007": (1564, 1564, 2024, "BUILDER Local Leaders 2025, DFW", None),
    "DFW-008": (1170, 1170, 2024, "BUILDER Local Leaders 2025, DFW", None),
    "DFW-009": (1155, 1155, 2024, "BUILDER Local Leaders 2025, DFW", None),
    "DFW-010": (1132, 1132, 2024, "BUILDER Local Leaders 2025, DFW", None),
    "DFW-040": (3162, 3162, 2024, "BUILDER firm page", "company-wide"),
    "DFW-056": (2286, 2286, 2025, "BUILDER firm page", "company-wide"),
    "DFW-041": (1779, 1779, 2022, "BUILDER firm page", "company-wide"),
    "DFW-061": (1465, 1465, 2025, "BUILDER firm page", "company-wide, including Tennessee"),
    "DFW-020": (728, 728, 2025, "BUILDER firm page", "company-wide"),
    "DFW-022": (696, 696, 2023, "BUILDER firm page", "company-wide"),
    "DFW-033": (649, 649, 2025, "Builder 100, 2026 list", "company-wide"),
    "DFW-029": (636, 636, 2025, "BUILDER firm page", "company-wide"),
    "DFW-045": (482, 482, 2025, "BUILDER firm page", "company-wide"),
    "DFW-079": (436, 436, 2025, "BUILDER firm page", "company-wide"),
    "DFW-021": (406, 406, 2025, "BUILDER firm page", "company-wide"),
    "DFW-023": (400, 400, 2026, "The firm's own about page: over 400 a year", None),
    "DFW-025": (374, 374, 2025, "BUILDER list, 2026", "company-wide"),
    "DFW-048": (286, 286, 2025, "BUILDER firm page", "company-wide"),
    "DFW-026": (259, 259, 2023, "BUILDER firm page", "company-wide"),
    "DFW-032": (259, 259, 2025, "BUILDER firm page", "company-wide"),
    "DFW-027": (177, 177, 2023, "BUILDER firm page", "company-wide"),
    "DFW-030": (176, 176, 2022, "BUILDER firm page", "company-wide"),
}
# David Weekley's press kit gives a Dallas division figure; the pack cited it
# and no reader checked it, so it is not drawn.
CLOSINGS.update(AUDIT8.DFW_CLOSINGS)
CLOSINGS.update(AUDIT12.DFW_CLOSINGS)
BANDS = HOU["market"]["bands"]


def build_targets():
    out = []
    for t0 in PACK["targets"]:
        tid = t0["target_id"]
        e = EDIT[tid]
        t = {k: t0.get(k) for k in ("target_id", "entity_name", "short", "entity_type", "entity_role",
                                    "homepage_url", "company_li", "team_url", "chain", "last_verified",
                                    "phone", "phone_source", "phone_more", "phone_absent", "press")}
        t["chain"] = {"tilt": "tiltup"}.get(t["chain"], t["chain"])
        for k in ("key_stat", "mvp_screen", "synopsis", "region", "phone_label", "phone_note",
                  "company_li_note", "team_note"):
            t[k] = e.get(k)
        t["capital_signals"] = e.get("capital_signals") or []
        t["email"] = t["email_label"] = t["email_source"] = None
        t["audit_flags"] = []
        t["tail"] = False
        t["capital_mark"] = None
        # the three counts
        why = []
        for ax in AXES:
            v, txt = e["why"][ax]["verdict"], e["why"][ax]["text"]
            if tid in REVERT and REVERT[tid][0] == ax:
                v, txt = REVERT[tid][1], REVERT[tid][2]
            if (tid, ax) in AUDIT8.DFW_VERDICT:
                v, txt = AUDIT8.DFW_VERDICT[(tid, ax)]
            # Build 85. The ICON BD read: the verdict word only.
            v = AUDIT12.DFW_V.get((tid, ax), v)
            why.append({"axis": ax, "title": TITLE[ax], "verdict": v, "mark": V[v], "text": txt})
        if tid in PARITY:
            hid, srcs = PARITY[tid]
            hv, ht = _hwhy(hid)
            for w in why:
                if w["axis"] == "innovation":
                    w["verdict"], w["mark"], w["text"] = hv, V[hv], ht
        t["why"] = why
        t["marks"] = {w["axis"]: w["mark"] for w in why}
        t["scores"] = dict(t0["scores"])
        for w in why:
            t["scores"][w["axis"]] = S[w["mark"]]
        t["holds"] = sum(1 for w in why if w["mark"] != "fail")
        t["clears"] = sum(1 for w in why if w["mark"] == "clear")
        t["cell"] = t["marks"]["repeatability"] + "|" + t["marks"]["machine_fit"]
        # section
        g = GROUP_FIX.get(tid, t0["group"])
        if g in ("a", "b", "out") or tid in BY_HOLDS:
            g = "a" if t["holds"] == 3 else "b" if t["holds"] == 2 else "out"
        if tid in OFF:
            g = "out"
            t["off_reason"] = OFF[tid]
        elif g == "out":
            t["off_reason"] = "Holds %s of the three counts." % ("one" if t["holds"] == 1 else "none")
        t["group"], t["tier"] = g, TIER[g]
        # projects
        t["key_projects"] = [{"name": p.get("name"), "detail": p.get("detail"), "url": fix(p.get("url")),
                              "signal": None} for p in e.get("key_projects", [])]
        # sources
        src = [fix(s.get("url")) for s in t0.get("sources", [])]
        src += [fix(u) for u in e.get("add_sources", [])]
        if tid in PARITY:
            src += PARITY[tid][1]
        src += SOURCE_ADD.get(tid, []) + AUDIT8.DFW_SOURCES.get(tid, [])
        if "Local Leaders" in " ".join(filter(None, [t["key_stat"], t["synopsis"], t["mvp_screen"]]
                                                 + [w["text"] for w in why])):
            src.append(LL)
        drop = {_n(u) for u in e.get("drop_sources", [])}
        seen, S2 = set(), []
        for u in src:
            if u and _n(u) not in drop and _n(u) not in seen:
                seen.add(_n(u))
                S2.append({"url": u, "date": None})
        t["sources"] = S2
        t["homepage_url"] = fix(t["homepage_url"])
        t["team_url"] = fix(t["team_url"])
        # people
        ep = {p["name"]: p for p in e.get("principals", [])}
        people = []
        for p0 in t0.get("principals", []):
            pe = ep.get(p0["name"], {})
            if pe.get("remove") or (tid, p0["name"]) in DROP_PEOPLE:
                continue
            p = {"name": NAME_FIX.get((tid, p0["name"]), p0["name"]), "role": pe.get("role") or p0.get("role"),
                 "source_url": fix(pe.get("source_url") or p0.get("source_url")),
                 "source_evidence": pe.get("source_evidence") or p0.get("source_evidence")}
            if p0.get("decider"):
                p["decider"] = True
            li = pe.get("linkedin") or pe.get("linkedin_url") or p0.get("linkedin_url")
            if pe.get("drop_linkedin"):
                li = None
            if li and _n(li) in LIVN:
                p["linkedin_url"], title = LIVN[_n(li)]
                p["li_evidence"] = "Indexed title reads %s." % title.rstrip(".")
            if not p["source_url"]:
                p["source_evidence"] = None
            people.append(p)
        # a person the editors added from a verified page (Our Country's CEO)
        for name, pe in ep.items():
            orig = {p0["name"] for p0 in t0.get("principals", [])}
            if (not pe.get("remove") and name not in orig and pe.get("source_url")
                    and not any(x["name"] == name for x in people)):
                people.append({"name": name, "role": pe.get("role"), "source_url": fix(pe["source_url"]),
                               "source_evidence": pe.get("source_evidence")})
        t["principals"] = people
        # phone
        ph = e.get("phone")
        t["phone_source"] = fix(t["phone_source"])
        if ph == "REMOVE" or (t["phone"] and not t["phone_source"]):
            t["phone"], t["phone_source"], t["phone_more"] = None, None, []
            t["phone_label"] = None
            t["phone_note"] = t["phone_note"] or "No firm page cited here publishes a main line."
        elif isinstance(ph, dict) and ph.get("number"):
            t["phone"] = re.sub(r"\D", "", ph["number"])[-10:]
            t["phone_source"] = fix(ph.get("source")) or t["phone_source"]
            t["phone_label"] = ph.get("label") or t["phone_label"]
            t["phone_more"] = []
        if tid in PHONE_FIX:
            t["phone"], t["phone_source"], t["phone_label"] = PHONE_FIX[tid]
        t["phone_more"] = [{"digits": re.sub(r"\D", "", m.get("number") or m.get("digits") or "")[-10:],
                            "label": m.get("label"), "source": None}
                           for m in (t["phone_more"] or []) if m.get("number") or m.get("digits")]
        t["phone_rule"] = None
        if t["phone"]:
            t["phone_note"] = None
            t["phone_absent"] = None
        else:
            # Houston states an absence as a sentence in phone_absent.
            t["phone_absent"] = t["phone_note"] or "No firm page cited here publishes a main line."
            t["phone_note"] = None
        # A card with nobody on it says why, in the words its editor wrote.
        if not t["principals"]:
            t["people_absent"] = (PEOPLE_ABSENT.get(tid) or t.get("team_note")
                                  or "No owner or officer is named on a page this deck can cite.")
        t["phone_shared"] = sorted(x for grp in SHARED_PHONE if tid in grp for x in grp if x != tid)
        out.append(t)
    bad = []
    T = {t["target_id"]: t for t in out}
    for tid, old_, new_ in EDITS:
        blob = [x for x in _visible(T[tid])]
        n = sum(x.count(old_) for x in blob)
        if n != 1:
            bad.append("%s: %r found %d times" % (tid, old_[:50], n))
            continue
        for k in ("key_stat", "mvp_screen", "synopsis", "region"):
            if T[tid].get(k) and old_ in T[tid][k]:
                T[tid][k] = T[tid][k].replace(old_, new_)
        for w in T[tid]["why"]:
            w["text"] = w["text"].replace(old_, new_)
        for k in T[tid]["key_projects"]:
            k["detail"] = (k.get("detail") or "").replace(old_, new_)
    if bad:
        raise SystemExit("FAILED: " + "; ".join(bad))
    return out


def main():
    targets = build_targets()
    for t in targets:
        c = CLOSINGS.get(t["target_id"])
        t["vol"] = c[1] if c else None
    # deciders, as Houston marks them. The research pack marked most chief
    # executives. Houston's rule: at a builder, the mark goes on construction,
    # purchasing or the division president; at a small builder with none of
    # those published, on the owner; at a contractor, on whoever signs for
    # equipment, which is the owner or president; at a land owner, on nobody
    # unless a construction or purchasing head is published.
    SPEC = re.compile(r"construction|purchas|procure|(division|area|regional) president|"
                      r"president, .*(dallas|dfw|fort worth)", re.I)
    TOP = re.compile(r"chief executive|\bceo\b|owner|founder|president|chair", re.I)
    for t in targets:
        was = [p for p in t["principals"] if p.pop("decider", False)]
        spec = [p for p in t["principals"] if SPEC.search(p.get("role") or "")]
        if t["group"] == "trade":
            pick = was or spec
        elif spec:
            pick = spec
        elif t["group"] in ("a", "b", "creative", "adopter") and (t.get("vol") or 0) <= 1500:
            pick = [p for p in was if TOP.search(p.get("role") or "")][:2]
        else:
            pick = []
        for p in pick:
            p["decider"] = True
    # Build 71. A contact whose own card says they have left, or who is only a
    # probable match, is marked so, as Houston marks them.
    AUDIT8.dfw_people(targets)
    _bad7 = AUDIT7.people({t["target_id"]: t for t in targets}, AUDIT7.DFW_PERSON)
    if _bad7:
        raise SystemExit("FAILED: " + "; ".join(_bad7))
    for t in targets:
        t["deciders"] = [p["name"] for p in t["principals"] if p.get("decider")]
        t["has_decider"] = bool(t["deciders"])
        _clean = [p for p in t["principals"] if p.get("decider")
                  and not p.get("departed") and not p.get("probable") and not p.get("entity_note")]
        t["decider_confirmed"] = bool(_clean)
        t["decider_caveat"] = t["has_decider"] and not _clean
    GO = {"adopter": 0, "a": 1, "b": 2, "trade": 3, "creative": 4, "national": 5, "channel": 6, "icon": 7, "out": 8}
    targets.sort(key=lambda t: (GO[t["group"]], -t["clears"], -t["holds"],
                                -t["scores"].get("capital_access", 0), t["entity_name"]))
    deck = [t for t in targets if t["group"] != "out"]
    n = len(deck)
    g = collections.Counter(t["group"] for t in deck)
    n_people = sum(len(t["principals"]) for t in deck)
    n_li = sum(1 for t in deck for p in t["principals"] if p.get("linkedin_url"))
    n_dec = sum(1 for t in deck if t["has_decider"])
    n_chk = sum(1 for t in deck if t["decider_caveat"])
    _pp = [p for t in deck for p in t["principals"]]
    n_li_p = sum(1 for p in _pp if p.get("linkedin_url"))
    n_src_p = sum(1 for p in _pp if p.get("source_url") and not p.get("linkedin_url"))
    n_none_p = sum(1 for p in _pp if not p.get("linkedin_url") and not p.get("source_url"))

    def axis_row(key, label):
        c = sum(1 for t in deck if t["scores"][key] == 3)
        p = sum(1 for t in deck if t["scores"][key] == 2)
        return {"key": key, "label": label, "blurb": "", "clear": c, "partial": p, "fail": n - c - p, "total": n}

    best = [t for t in deck if t["cell"] == "clear|clear"]
    hold3 = len([t for t in best if t["holds"] == 3])
    def nn(k, a, b):
        return "%d %s" % (k, a if k == 1 else b)
    n_builders = sum(1 for t in deck if t["group"] not in ("trade", "channel"))
    closings = sorted([
        {"id": tid, "name": t["entity_name"], "short": t["short"], "low": lo, "high": hi, "year": yr,
         "source": src, "fit": t["marks"]["machine_fit"], "method": t["marks"]["innovation"],
         "group": t["group"], "wide": wide}
        for tid, (lo, hi, yr, src, wide) in CLOSINGS.items()
        for t in deck if t["target_id"] == tid], key=lambda r: -r["high"])

    # supply, curated: the pack's panel less the firms that already have a card,
    # the out-of-metro entries and anything no page supports.
    SUP = jsonio.read(paths.DFW_EDIT / "supply.json")

    # the field: Houston's audited entries for the same firms, with DFW's own two
    COMP = jsonio.read(paths.DFW_EDIT / "field.json")

    D = {
        "version": "2.0", "build": BUILD, "last_updated": TODAY,
        "byline": HOU["byline"],
        "kicker": "Rolodex · Dallas-Fort Worth · %s" % TODAY,
        "headline": "Dallas-Fort Worth builders and developers, screened for a construction printer.",
        "headline_html": "Dallas-Fort Worth builders and developers,<br><b>screened for a construction printer.</b>",
        "meta_description": ("%d Dallas-Fort Worth builders, developers and wall contractors screened against "
                             "three counts for a construction printer, with named decision-makers, sources, "
                             "a market view and the permitting route. By Héctor Ibarzábal." % n),
        "group_labels": dict(HOU["group_labels"]),
        "group_notes": dict(HOU["group_notes"], **{
            "trade": "DFW builders do not put up their own walls either, so the firm that would run a "
                     "printer is often the one they hire. The three counts are asked of the wall rather "
                     "than of the plan set.",
            "icon": "Lennar's DFW business. LEN X invested in ICON in August 2021, and Lennar built "
                    "Wolf Ranch with ICON."}),
        "stat_strip": [
            [str(n), "firms screened", False, None],
            [str(g["adopter"]), "already buying printed walls", False, {"group": ["adopter"]}],
            [str(g["a"]), "builders and developers hold all three counts", False, {"group": ["a"]}],
            [str(g["trade"]), "contractors and plants", False, {"group": ["trade"]}],
            [str(n_dec), "of %d with a decision-maker named" % n, True, {"dec": "any"}],
        ],
        "sub": HOU["sub"],
        "axes": [axis_row("repeatability", "Repetition"), axis_row("machine_fit", "Printer fit"),
                 axis_row("innovation", "Track record")],
        "matrix": HOU["matrix"], "axis_titles": HOU["axis_titles"],
        "matrix_note": ("<b>%s</b> read Yes on both axes of this grid. The grid leaves out track record. "
                        "<b>%d</b> of the %d %s all three counts."
                        % (nn(len(best), "firm", "firms"), hold3, len(best), "holds" if hold3 == 1 else "hold")),
        "role_labels": HOU["role_labels"], "signal_labels": HOU["signal_labels"],
        "competitor": None,
        "icon_record": COMP["icon_record"],
        "competitors": [dict(c, site=next((u for lab, u in (c.get("links") or [])
                                           if lab.lower().startswith("their site")), None))
                        for c in COMP["competitors"]],
        "consolidation": COMP["consolidation"],
        "chain": [dict(c, n=sum(1 for t in deck if t.get("chain") == c["key"]))
                  for c in HOU["chain"] if any(t.get("chain") == c["key"] for t in deck)],
        "supply": SUP["supply"],
        "supply_labels": HOU["supply_labels"],
        "supply_notes": SUP["notes"],
        "no_site": [], "no_site_note": "",
        "limits": [
            ["How the list was drawn",
             "BUILDER's Local Leaders table for Dallas-Fort Worth, BUILDER firm pages, the builder lists "
             "each master-planned community publishes, trade press and firm websites. A separate research "
             "tool drew the first list. Every name, number and link on it was then checked against the "
             "page it cites, and what no page supports was cut."],
            ["Who decides",
             "The mark goes on a vice president or director of construction, a head of purchasing, or a "
             "division president: those roles can change a wall specification. Construction managers, "
             "superintendents and purchasing agents execute one. At a builder of 400 homes a year or fewer "
             "that publishes none of those roles, it goes on the owner. At a contractor it goes on whoever "
             "signs for equipment.%s" % ((" On %d of the %d the contact carries a caveat: the person has "
             "left, sits at another entity, or is a probable match." % (n_chk, n_dec)) if n_chk else "")],
            ["Sources",
             "Company filings, company pages and trade press. Each contact rests on one of three, and says "
             "which: %d a LinkedIn headline naming the firm, %d the firm's own site or dated reporting, %d a "
             "name with no page to link. A LinkedIn link is kept only where a search result showed it with "
             "the person's name and the firm. No aggregator was used." % (n_li_p, n_src_p, n_none_p)],
            ["Scope",
             "The Dallas-Fort Worth-Arlington metro and its counties. Architects, engineers and permitting "
             "authorities are not covered. Firms whose product is retail shell, mid-rise or one-off "
             "architecture are held out of the deck."],
        ],
        "code": COMP["code"],
        "method": HOU["method"],
        "bands_method": HOU["bands_method"],
        "market": {
            "closings": closings,
            "closings_missing": n_builders - len(closings),
            "closings_base": n_builders,
            "bands": BANDS,
            "by_section": [
                {"group": gk, "label": HOU["group_labels"][gk] if gk != "icon" else "Lennar",
                 "n": sum(1 for t in deck if t["group"] == gk),
                 "yes": sum(1 for t in deck if t["group"] == gk and t["marks"]["innovation"] == "clear"),
                 "partly": sum(1 for t in deck if t["group"] == gk and t["marks"]["innovation"] == "partial"),
                 "no": sum(1 for t in deck if t["group"] == gk and t["marks"]["innovation"] == "fail"),
                 "decider": sum(1 for t in deck if t["group"] == gk and t["decider_confirmed"]),
                 "confirm": sum(1 for t in deck if t["group"] == gk and t["decider_caveat"]),
                 "linked": sum(1 for t in deck if t["group"] == gk
                               and any(p.get("linkedin_url") or p.get("source_url") for p in t["principals"]))}
                for gk in ("adopter", "a", "b", "trade", "creative", "national", "channel", "icon")
                if any(t["group"] == gk for t in deck)],
            "owners": COMP["owners"],
            "printed": COMP["printed"],
            "timeline": COMP["timeline"],
        },
        "permits": permits(),
        "place": {"key": "dfw", "name": "Dallas-Fort Worth", "short": "DFW", "file": "DFW",
                  "outline": "TxDOT", "local": "Fort Worth|Dallas|Allen|Collin"},
        "stats": {"total": n, "adopters": g["adopter"], "tier_a": g["a"], "tier_b": g["b"],
                  "principals": n_people, "linkedin_held": n_li, "audit_flags": 0,
                  "with_decider": n_dec, "with_decider_live": sum(1 for t in deck if t["has_decider"] and t["group"] in ("a", "b", "adopter")),
                  "with_decider_confirmed": sum(1 for t in deck if t["decider_confirmed"]),
                  "with_decider_caveat": sum(1 for t in deck if t["decider_caveat"])},
        "targets": targets,
        "_derived": {},
    }
    D["group_labels"]["icon"] = "Lennar"
    # owners: every builder id must be a card on the deck, or None
    ids = {t["target_id"] for t in deck}
    held = {t["target_id"] for t in targets if t["group"] == "out"}
    held_names = {t["entity_name"]: t["target_id"] for t in targets if t["group"] == "out"}
    for o in D["market"]["owners"]:
        for b in o["builders"]:
            # Build 71. A builder that has a card held off the deck is screened,
            # and says so, rather than reading "not screened".
            if b.get("id") in held or b.get("name") in held_names:
                b["off"] = True
            if b.get("id") not in ids:
                b["id"] = None
    D["market"]["owners"] = [o for o in D["market"]["owners"] if o["id"] in ids]
    # Build 71. The pre-publication audit (audit7.py).
    AUDIT7.strip_working(D)
    AUDIT7.fix_market(D)
    _bad7 = AUDIT7.apply(D, "dfw")
    AUDIT7.dfw(D)
    AUDIT8.dates(D)
    AUDIT7.tidy(D)
    _bad7 += AUDIT9.finish(D)
    import audit10 as AUDIT10
    _d10, _s10 = AUDIT10.apply(D, "dfw")
    _g10, _gs10 = AUDIT10.apply_global(D, "dfw")
    _d10 += _g10
    _s10 += _gs10
    _bad10 = AUDIT10.final_copy(D, "dfw")
    if _bad10:
        raise SystemExit("FAILED: " + "; ".join(_bad10))
    print("distilled         %d edits, %d stale" % (_d10, len(_s10)))
    for _x in _s10[:20]:
        print("   stale " + _x)
    if _bad7:
        for b in _bad7:
            print("   " + b)
        raise SystemExit("FAILED: an audit7 edit did not land")
    # Build 84. Sources a reader can open (audit11.py).
    import audit11 as AUDIT11
    _bad11 = AUDIT11.apply(D, "dfw")
    if _bad11:
        raise SystemExit("FAILED: " + "; ".join(_bad11))
    # Build 85. The ICON BD read (audit12.py): text, the Field, code and market.
    _bad12 = AUDIT12.final(D, "dfw")
    if _bad12:
        raise SystemExit("FAILED: " + "; ".join(_bad12))
    # Build 87. Screen lines in fact form, and each card's role and kind (audit13.py).
    _bad13 = AUDIT13.final(D, "dfw")
    if _bad13:
        raise SystemExit("FAILED: " + "; ".join(_bad13))
    gate(D)
    jsonio.write(D, paths.out(paths.DFW_DATA), ensure_ascii=False, indent=1)
    print("dfw entities      %d  (off deck %d)" % (n, len(targets) - n))
    print("sections          %s" % dict(g))
    for a in D["axes"]:
        print("  %-16s clear %2d  partial %2d  fail %2d" % (a["label"], a["clear"], a["partial"], a["fail"]))
    print("principals        %d  (linkedin held %d)" % (n_people, n_li))
    print("closings drawn    %d of %d builders and developers" % (len(closings), n_builders))


def permits():
    P = copy.deepcopy(PACK["permits"])
    # Build 70. The pack drew the counties from the Census 1:5,000,000 files.
    # These are TxDOT's, the layer Houston's map uses, simplified the same way,
    # with TxDOT's lakes above 1,000 acres. dfw/geo/outline.py makes both.
    geo = ROOT / "dfw" / "geo"
    outl = {g["fips"]: g for g in jsonio.read(geo / "outlines.json")}
    have = {c["fips"] for c in P["counties"]}
    assert set(outl) == have, "the TxDOT outlines and the permit counties differ"
    P["geom"] = [{"fips": f, "name": outl[f]["name"], "rings": outl[f]["rings"]} for f in sorted(outl)]
    P["water"] = [{"name": w["name"], "rings": w["rings"]}
                  for w in jsonio.read(geo / "water.json")]
    P["places"] = [p for p in P.get("places", []) if any(p.get("sf", []))]
    # The pack carries the fifty largest jurisdictions, not every one, so they
    # do not sum to the counties the way Houston's do.
    P["places_complete"] = False
    # The pack listed six, one of them marked as not used. These are the files
    # the figures were read from, each tagged with the figures it serves.
    P["sources"] = [
        {"url": "https://www2.census.gov/econ/bps/County/", "use": ["metro", "county"],
         "label": "Census Building Permits Survey, annual county files"},
        {"url": "https://www2.census.gov/econ/bps/Place/", "use": ["place"],
         "label": "Census Building Permits Survey, annual place files"},
        {"url": "https://www.census.gov/construction/bps/definitions.html", "use": ["metro"],
         "label": "Census Building Permits Survey, definitions"},
        {"url": "https://gis-txdot.opendata.arcgis.com/datasets/texas-county-boundaries/geoservice", "use": ["map"],
         "label": "TxDOT, Texas County Boundaries"},
        {"url": "https://services.arcgis.com/KTcxiTD9dsQw4r7Z/arcgis/rest/services/Texas_Water_Bodies/FeatureServer",
         "use": ["map"], "label": "TxDOT, Texas Water Bodies"},
    ]
    P.pop("retrieval_note", None)
    return P


# ------------------------------------------------------------------ gates
BANNED = POLICY.BANNED
STYLE = [
    (r"—", "an em dash"),
    (r"\s–\s", "a spaced en dash"),
    (r"→|←", "an arrow"),
    (r"~\s?\d", "a tilde before a number"),
    (r"\b(machine_fit|census|this pass|re-?score|fetched|Grok|records/|HOU-\d+|DFW-[A-Z]*-?\d+)\b", "internal vocabulary"),
    (r"\b(the only|one of the few|first call|better candidate|well above|world-class|leading|premier)\b", "rhetoric"),
]


def _visible(t):
    yield t.get("entity_name") or ""
    yield t.get("short") or ""
    yield t["key_stat"] or ""
    yield t["mvp_screen"] or ""
    yield t["synopsis"] or ""
    for w in t["why"]:
        yield w["text"]
    for k in t["key_projects"]:
        yield (k.get("name") or "") + " " + (k.get("detail") or "")
    for p in t["principals"]:
        yield (p.get("role") or "") + " " + (p.get("source_evidence") or "")
    for k in ("phone_label", "phone_note", "company_li_note", "team_note", "region"):
        yield t.get(k) or ""


def gate(D):
    bad = []
    blob = json.dumps(D, ensure_ascii=False).lower()
    for b in BANNED:
        if b in blob:
            bad.append("banned source: %s" % b)
    for t in D["targets"]:
        if t["group"] == "out":
            continue
        for s in _visible(t):
            for rx, what in STYLE:
                if re.search(rx, s, re.I if what != "an em dash" else 0):
                    bad.append("%s: %s in %r" % (t["target_id"], what, s[:90]))
        ks = t["key_stat"] or ""
        if re.search(r"\bclosings\b", ks) and not re.search(r"DFW|company-wide|Texas|Dallas", ks):
            bad.append("%s headline counts closings without saying whose: %r" % (t["target_id"], ks))
        for p in t["principals"]:
            if p.get("linkedin_url") and _n(p["linkedin_url"]) not in LIVN:
                bad.append("%s: unverified LinkedIn for %s" % (t["target_id"], p["name"]))
        for u in [t.get("homepage_url"), t.get("phone_source")] + [s["url"] for s in t["sources"]]:
            if u and not u.startswith("http"):
                bad.append("%s: not a URL %r" % (t["target_id"], u))
    for x in D["supply"] + D["competitors"]:
        for s in [x.get("line"), x.get("why"), x.get("note")] + [f[1] for f in x.get("facts", [])]:
            for rx, what in STYLE:
                if s and re.search(rx, s, re.I if what != "an em dash" else 0):
                    bad.append("%s: %s in %r" % (x["name"], what, s[:90]))
    if bad:
        for b in bad:
            print("   " + b)
        raise SystemExit("FAILED: %d DFW gate findings" % len(bad))


if __name__ == "__main__":
    main()
