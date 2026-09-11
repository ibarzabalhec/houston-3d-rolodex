# -*- coding: utf-8 -*-
"""Build the ICON Greater Houston rolodex: JSON -> HTML card deck + XLSX workbench.

Single source of truth is houston-data.json, generated here from the data modules.
Never hand-edit the generated HTML or XLSX.

Build 2 changes the presentation, not the evidence. The 0-12 composite is gone.
Three screens, each of which either holds or does not. Tier A holds all three.
Capital is shown as a visible qualifier rather than folded into a hidden total.
"""
import json, sys, collections

sys.path.insert(0, '.')
from data_a import A_TIER
from data_b import REST
from data_c import MID, TAIL
from screens import VERDICT, SIGNAL_MERGE
from why import WHY, AXIS_TITLE, VERDICT_WORD
from found import CONFIRMED, PROBABLE, MOVED, REMOVED, REJECTED, ADDED
from corrections import (FLAGS as CFLAGS, VERDICTS as CVERD, COMPETITOR,
                         SCORES as CSCORES, WHY_OVERRIDE as CWHY)
from links import COMPANY, PERSON, NEW_PEOPLE, DECIDERS
from machine import MACHINE, DROPPED, NATIONAL, CHANNEL, ICON_CLIENT
from creative import CREATIVE, NEW_CREATIVE, EXTRA as CEXTRA
from competitors import ICON as ICON_RECORD, COMPETITORS, CONSOLIDATION
from builders import BUILDERS
import research2 as R2
from market import CLOSINGS, BANDS, PRINTED, TIMELINE
from code import CODE, CODE_LINE, PRECEDENT, QUOTES, BANDS_METHOD, BANDS_SOURCES, METHOD
from urllib.parse import quote

BUILD = 32

# The second research pass is folded into the same layers the first one wrote
# to, so every downstream rule (verification, deciders, source links) applies
# to it unchanged.
CONFIRMED.update(R2.LINKEDIN)
PERSON.update(R2.SOURCES)
DECIDERS.update(R2.DECIDERS)
for _tid, _ppl in R2.PEOPLE.items():
    NEW_PEOPLE.setdefault(_tid, []).extend(_ppl)
for _tid, _sc in R2.SCORES.items():
    CSCORES.setdefault(_tid, {}).update(_sc)
for _tid, _fl in R2.FLAGS.items():
    CFLAGS.setdefault(_tid, []).extend(_fl)
TODAY = "2026-09-11"

SCREENS = ["repeatability", "machine_fit", "innovation"]

ROLE_LABELS = {
    "vertical_buyer": "Buys walls",
    "proven_adopter": "Prints today",
    "channel": "Sells lots",
    "capital": "Funds it",
}
SIGNAL_LABELS = {
    "method_risk": "Method risk absorbed",
    "repeatable": "Repeatable volume",
    "resilience": "Resilience positioning",
    "schedule": "Schedule pressure",
}


def expand_tail(rows):
    out = []
    for tid, name, etype, role, region, url, reason, scores, src, flag in rows:
        flags = []
        if flag:
            flags.append(flag)
        out.append({
            "target_id": tid, "entity_name": name, "entity_type": etype, "entity_role": role,
            "region": region, "homepage_url": url, "synopsis": reason, "key_stat": None,
            "principals": [], "key_projects": [], "capital_signals": [],
            "scores": dict(scores), "mvp_screen": reason,
            "sources": [{"url": src, "date": None}] if src else [],
            "audit_flags": flags, "hue_hex": "#63635E", "tail": True,
        })
    return out


def expand_builders(rows):
    """The builder layer carries its own verdict and reasons inline."""
    out = []
    for (tid, name, region, url, stat, syn, sc, verdict, why3,
         people, projects, srcs, flags) in rows:
        out.append({
            "target_id": tid, "entity_name": name, "entity_type": "homebuilder",
            "entity_role": "vertical_buyer", "region": region, "homepage_url": url,
            "synopsis": syn, "key_stat": stat,
            "principals": [{"name": n, "role": r} for n, r in people],
            "key_projects": [{"name": a, "detail": b, "signal_type": c, "fit_signal": d, "url": e}
                             for a, b, c, d, e in projects],
            "capital_signals": [],
            "scores": {"repeatability": sc[0], "machine_fit": sc[1],
                       "innovation": sc[2], "capital_access": sc[3]},
            "mvp_screen": verdict, "_verdict": verdict, "_why": list(why3),
            "sources": [{"url": u, "date": None} for u in srcs],
            "audit_flags": list(flags), "hue_hex": "#FF4F00", "tail": False,
            "new_layer": True,
        })
    return out


def mark(v):
    """3 clears the screen, 2 is partial, 0-1 fails."""
    return "clear" if v == 3 else ("partial" if v == 2 else "fail")


def finalize(recs):
    for t in recs:
        s = t["scores"]
        if "machine_fit" not in s:
            if t["target_id"] not in MACHINE:
                raise SystemExit("no machine-fit count written for %s (%s)"
                                 % (t["target_id"], t["entity_name"]))
            s["machine_fit"], t["_machine_why"] = MACHINE[t["target_id"]]
        s.update(CSCORES.get(t["target_id"], {}))
        t["marks"] = {k: mark(s[k]) for k in SCREENS}
        t["holds"] = sum(1 for k in SCREENS if s[k] >= 2)
        t["capital_mark"] = mark(s["capital_access"])
        for k in ("audit_flags", "sources", "principals", "key_projects", "capital_signals"):
            t.setdefault(k, [])
        t.setdefault("hue_hex", "#FF4F00")
        t.setdefault("tail", False)

        hard = any("Do not approach" in f for f in t["audit_flags"])
        if t["entity_role"] == "proven_adopter":
            t["group"], t["tier"] = "adopter", "P"
        elif t["target_id"] in ICON_CLIENT:
            t["group"], t["tier"] = "icon", "I"
            if ICON_CLIENT[t["target_id"]] not in t["audit_flags"]:
                t["audit_flags"].append(ICON_CLIENT[t["target_id"]])
        elif t["entity_role"] == "channel":
            t["group"], t["tier"] = "channel", "M"
        elif t["target_id"] in NATIONAL:
            t["group"], t["tier"] = "national", "N"
        elif t["target_id"] in CREATIVE:
            t["group"], t["tier"] = "creative", "X"
        elif hard:
            t["group"], t["tier"] = "out", "D"
        elif t["holds"] == 3:
            t["group"], t["tier"] = "a", "A"
        elif t["holds"] == 2:
            t["group"], t["tier"] = "b", "B"
        else:
            t["group"], t["tier"] = "out", "C" if t["holds"] == 1 else "D"
        t["last_verified"] = TODAY

        if "_verdict" not in t and t["target_id"] not in VERDICT:
            raise SystemExit("no verdict written for %s (%s)" % (t["target_id"], t["entity_name"]))
        t["mvp_screen"] = t.get("_verdict") or CVERD.get(t["target_id"], VERDICT[t["target_id"]])
        if t["target_id"] in R2.VERDICTS:
            t["mvp_screen"] = R2.VERDICTS[t["target_id"]]
        for fl in CEXTRA.get(t["target_id"], []):
            if fl not in t["audit_flags"]:
                t["audit_flags"].append(fl)
        for fl in CFLAGS.get(t["target_id"], []):
            if fl not in t["audit_flags"]:
                t["audit_flags"].append(fl)

        for p in t["key_projects"]:
            p["signal_type"] = SIGNAL_MERGE.get(p["signal_type"], p["signal_type"])

        if t["group"] in ("adopter", "a", "b", "national", "creative", "icon"):
            if "_why" in t:
                texts = t["_why"]
            else:
                if t["target_id"] not in WHY:
                    raise SystemExit("no reasons written for %s (%s)"
                                     % (t["target_id"], t["entity_name"]))
                old = WHY[t["target_id"]]
                # the middle reason used to answer wall share; the machine count replaces it
                texts = [old[0], t.get("_machine_why", ""), old[2]]
            t["why"] = [{"axis": k, "title": AXIS_TITLE[k],
                         "verdict": VERDICT_WORD[t["marks"][k]], "mark": t["marks"][k],
                         "text": CWHY.get(t["target_id"], {}).get(k, texts[i])}
                        for i, k in enumerate(SCREENS)]
        else:
            t["why"] = []

        # apply verified LinkedIn findings before search links are generated
        if t["entity_name"] in {v["firm"] for v in REMOVED.values()}:
            gone = [n for n, v in REMOVED.items() if v["firm"] == t["entity_name"]]
            for n in gone:
                if any(p["name"] == n for p in t["principals"]):
                    t["principals"] = [p for p in t["principals"] if p["name"] != n]
                    t["audit_flags"].append(REMOVED[n]["flag"])
        for p in t["principals"]:
            if p["name"] in CONFIRMED:
                p["linkedin_url"], p["li_evidence"] = CONFIRMED[p["name"]]
            elif p["name"] in PROBABLE and PROBABLE[p["name"]]["firm"] == t["entity_name"]:
                pr = PROBABLE[p["name"]]
                p["linkedin_url"], p["li_evidence"], p["probable"] = pr["url"], pr["evidence"], True
                if pr["flag"] not in t["audit_flags"]:
                    t["audit_flags"].append(pr["flag"])
            elif p["name"] in MOVED and MOVED[p["name"]]["firm"] == t["entity_name"]:
                mv = MOVED[p["name"]]
                p["linkedin_url"], p["role"], p["departed"] = mv["url"], mv["role"], True
                if mv["flag"] not in t["audit_flags"]:
                    t["audit_flags"].append(mv["flag"])
        for n, firm, why in REJECTED:
            if firm == t["entity_name"] and any(p["name"] == n for p in t["principals"]):
                fl = "No LinkedIn profile is held for %s. %s" % (n, why)
                if fl not in t["audit_flags"]:
                    t["audit_flags"].append(fl)

        for extra in ADDED.get(t["entity_name"], []):
            if not any(p["name"] == extra["name"] for p in t["principals"]):
                t["principals"].append(dict(extra))

        for name, role in NEW_PEOPLE.get(t["target_id"], []):
            if not any(p["name"] == name for p in t["principals"]):
                t["principals"].append({"name": name, "role": role})
        for p in t["principals"]:
            nr = R2.TITLES.get((t["target_id"], p["name"]))
            if nr:
                p["role"] = nr
        if t["target_id"] in R2.STATS:
            t["key_stat"] = R2.STATS[t["target_id"]]
        if t["target_id"] in R2.MACHINE_WHY:
            for w in t.get("why", []):
                if w["axis"] == "machine_fit":
                    w["text"] = R2.MACHINE_WHY[t["target_id"]]

        # the company link layer
        c = COMPANY.get(t["target_id"], {})
        t["company_li"] = c.get("li")
        t["company_li_note"] = c.get("li_note")
        t["team_url"] = c.get("team")
        t["team_note"] = c.get("team_note")

        for p in t["principals"]:
            if (t["target_id"], p["name"]) in DECIDERS:
                p["decider"] = True
            # people added from a firm's own page arrive after the first LinkedIn pass,
            # so run it again for them rather than leaving a held URL unattached
            if not p.get("linkedin_url"):
                if p["name"] in CONFIRMED:
                    p["linkedin_url"], p["li_evidence"] = CONFIRMED[p["name"]]
                elif p["name"] in PROBABLE and PROBABLE[p["name"]]["firm"] == t["entity_name"]:
                    pr = PROBABLE[p["name"]]
                    p["linkedin_url"], p["li_evidence"], p["probable"] = pr["url"], pr["evidence"], True
                    if pr["flag"] not in t["audit_flags"]:
                        t["audit_flags"].append(pr["flag"])
            src = PERSON.get((t["target_id"], p["name"]))
            if src:
                p["source_url"], p["source_evidence"] = src
            if not p.get("linkedin_url"):
                p["find_url"] = ("https://www.linkedin.com/search/results/people/?keywords="
                                 + quote(p["name"] + " " + t["entity_name"].split(" / ")[0].split(" (")[0]))
    return recs


SHORT = {
 "HOU-004": "InTown / Lovett", "HOU-002": "Cole Klein", "HOU-016": "Commander Homes",
 "HOU-017": "Elpis 3D", "HOU-010": "Camillo / SimplyHome", "HOU-037": "The Deal Co.",
 "HOU-057": "Hartman / Silver Star", "HOU-051": "Rice Mgmt (Ion)", "HOU-015": "Signorelli",
 "HOU-007": "First America", "HOU-027": "Greystar Summerwell", "HOU-011": "Howard Hughes",
 "HOU-021": "Dinerstein", "HOU-029": "Hanover", "HOU-050": "Finger Companies",
 "HOU-025": "Taylor Morrison", "HOU-020": "Provident", "HOU-054": "StoneLake",
 "HOU-055": "CAF Capital", "HOU-056": "Sarofim", "HOU-049": "StreetLights",
 "HOU-019": "Camden", "HOU-026": "Christopher Todd", "HOU-030": "Fidelis",
 "HOU-018": "NewQuest", "HOU-044": "RSK", "HOU-003": "Houston Housing Authority",
 "HOU-035": "Avenue CDC", "HOU-046": "MetroNational", "HOU-043": "Newland",
 "HOU-042": "Friendswood", "HOU-053": "Wolff", "HOU-041": "Caldwell",
 "HOU-040": "Johnson Development", "HOU-039": "Land Tejas", "HOU-052": "Medistar",
 "HOU-038": "Cameron Mgmt", "HOU-047": "Baker Katz", "HOU-048": "Wulfe & Co.",
 "HOU-028": "Sueba USA", "HOU-022": "CastleRock", "HOU-023": "David Weekley",
 "HOU-024": "Ashton Woods", "HOU-034": "Brightland", "HOU-033": "Coventry",
 "HOU-045": "Chesmar", "HOU-013": "Perry Homes", "HOU-014": "LGI Homes",
 "HOU-009": "Century Communities", "HOU-008": "Meritage", "HOU-012": "M/I Homes",
 "HOU-001": "Wan Bridge", "HOU-005": "Radom Capital", "HOU-006": "Triten",
 "HOU-031": "Read King", "HOU-032": "Urban Living", "HOU-036": "Midway",
}

_all = (A_TIER + REST + MID + expand_tail(TAIL) + expand_builders(BUILDERS)
        + expand_builders(NEW_CREATIVE))
_all = [t for t in _all if t["target_id"] not in DROPPED or t["target_id"] in CREATIVE]
targets = finalize(_all)
for t in targets:
    t["short"] = SHORT.get(t["target_id"], t["entity_name"])
    t["cell"] = t["marks"]["repeatability"] + "|" + t["marks"]["machine_fit"]
    ch = CHANNEL.get(t["target_id"])
    if ch:
        t["channel_line"], t["channel_builders"] = ch

# Open items carry two different kinds of sentence. One is a finding a reader can
# act on: a purchasing lead changed, a parent owns the land, a figure came from
# inside the company. The other is a caveat on the record itself: a figure that
# does not reconcile, an undated page, a count made against an absent record.
# Both belong on the card. Findings first, because a reader who stops after two
# items should have stopped on the two that matter.
CAVEAT_MARKS = ("not reconciled", "unconfirmed", "unsourced", "absent record",
                "no capital signal", "do not read", "scored as partial",
                "verify before outreach", "possibly stale", "currency")


def _is_caveat(f):
    low = f.lower()
    return any(m in low for m in CAVEAT_MARKS) or low.startswith("no ")


for t in targets:
    flags = t.get("audit_flags", [])
    t["audit_flags"] = ([f for f in flags if not _is_caveat(f)]
                        + [f for f in flags if _is_caveat(f)])

GROUP_ORDER = {"adopter": 0, "a": 1, "b": 2, "creative": 3, "national": 4, "channel": 5,
               "icon": 6, "out": 7}
for t in targets:
    t["clears"] = sum(1 for k in SCREENS if t["scores"][k] == 3)
targets.sort(key=lambda t: (GROUP_ORDER[t["group"]], -t["clears"], -t["holds"],
                            -t["scores"]["capital_access"], t["entity_name"]))

deck = [t for t in targets if t["group"] != "out"]
n_off = len(targets) - len(deck) + len(DROPPED)
n = len(deck)
g = collections.Counter(t["group"] for t in deck)
role_counts = collections.Counter(t["entity_role"] for t in deck)
n_people = sum(len(t["principals"]) for t in deck)
n_flags = sum(len(t["audit_flags"]) for t in deck)
n_li = sum(1 for t in deck for p in t["principals"] if p.get("linkedin_url"))

# A decider is a vice president or director of construction, or the head of purchasing:
# the person who can change a wall specification rather than execute one.
for t in deck:
    t["deciders"] = [p["name"] for p in t["principals"] if p.get("decider")]
    t["has_decider"] = bool(t["deciders"])
    # A decider who has left, who sits at a different entity, or who is only a
    # probable match is not the same thing as one you can ring today. The count
    # was treating the two as identical.
    _clean = [p for p in t["principals"] if p.get("decider")
              and not p.get("departed") and not p.get("probable") and not p.get("entity_note")]
    t["decider_confirmed"] = bool(_clean)
    t["decider_caveat"] = t["has_decider"] and not _clean
n_dec = sum(1 for t in deck if t["has_decider"])
n_dec_ok = sum(1 for t in deck if t["decider_confirmed"])
n_dec_chk = sum(1 for t in deck if t["decider_caveat"])
n_dec_live = sum(1 for t in deck if t["has_decider"] and t["group"] in ("a", "adopter", "b"))
n_dec_a = sum(1 for t in deck if t["has_decider"] and t["group"] == "a")


def axis_row(key, label, blurb):
    c = sum(1 for t in deck if t["scores"][key] == 3)
    p = sum(1 for t in deck if t["scores"][key] == 2)
    return {"key": key, "label": label, "blurb": blurb,
            "clear": c, "partial": p, "fail": n - c - p, "total": n}


best = [t for t in deck if t["cell"] == "clear|clear"]
best_yes = [t for t in best if t["marks"]["innovation"] == "clear"]
best_printing = [t for t in best_yes if t["group"] == "adopter"]
best_open = [t for t in best_yes if t["group"] != "adopter"]

best_part = [t for t in best if t["marks"]["innovation"] == "partial"]
best_no = [t for t in best if t["marks"]["innovation"] == "fail"]

def _names(rows):
    return " and ".join(t["short"] for t in rows)

_yes = _names(best_open)
if best_printing:
    _yes += (", plus " if best_open else "") + _names(best_printing) + ", who is already printing with a competitor"

_overlap = len([t for t in best if t["group"] == "a"])

def _n(k, one, many):
    return "%d %s" % (k, one if k == 1 else many)

# A description of the cell and of how it differs from the strip. Nothing about
# what the work in Houston is; the reader draws that. Plurals agree at any count.
MATRIX_NOTE = (
    "The top right cell holds <b>%s</b> that repeat a plan set and build at a volume one or two machines "
    "would cover. The cell is placed on two counts and ignores the third, so it is not the same set as the "
    "%d that are in on all three counts in the strip above; %s in both. Of the %d here, <b>%d</b> "
    "%s paid for an unproven method, %s. <b>%d</b> %s partial evidence. The other <b>%d</b> %s no "
    "method record."
    % (_n(len(best), "firm", "firms"), g["a"], _n(_overlap, "firm appears", "firms appear"),
       len(best), len(best_yes), "has" if len(best_yes) == 1 else "have", _yes,
       len(best_part), "shows" if len(best_part) == 1 else "show",
       len(best_no), "has" if len(best_no) == 1 else "have")
)

DATA = {
 "version": "2.0",
 "build": BUILD,
 "last_updated": TODAY,
 # The build number is a version-control artefact. It stays in the data for the
 # workbook and the verifier, and off the page a reader sees.
 "byline": "Héctor Ibarzábal · ibarzabalhec@gmail.com · %s" % TODAY,

 "kicker": "Titan · Greater Houston business development screen · %s" % TODAY,

 "headline": "Greater Houston, sized for the Titan. %d firms, three counts each." % n,
 # ICON writes display sentences in two weights: the connective words drop back,
 # the load-bearing ones stay solid. The same device, with the numbers carrying it.
 # A title, not a conclusion. What the document is, and nothing about what to think of it.
 # The counts live in the strip below, where a number belongs.
 "headline_html": ("Greater Houston, sized for the Titan.<br>"
                   "<b>%d firms. Three counts each.</b>" % n),
 # A label is a name, not a sentence. The clause each of these used to carry
 # moved into the group note, where there is room to say it once.
 "group_labels": {"adopter": "Already buying printed walls", "a": "Strong target",
                  "b": "One gap", "national": "National builder",
                  "creative": "Custom and hybrid job",
                  "channel": "Land owner, not the buyer",
                  "icon": "Already working with ICON", "out": ""},
 "group_notes": {"a": "In on all three counts.",
                 "b": "In on two of three counts.",
                 "adopter": "Has printed walls standing or contracted with a competitor.",
                 "national": "Purchasing sits at a national desk.",
                 "creative": "Design-led work that does not repeat a plan set. The printed element "
                             "sits inside a conventional project.",
                 "channel": "Owns the ground. The builders inside buy the wall.",
                 "icon": "Already reachable through an existing ICON relationship."},
 "stat_strip": [
   [str(n), "firms screened", False],
   [str(g["a"]), "in on all three counts", False],
   [str(n_dec), "with a named decision-maker", True],
   [str(g["adopter"]), "already printing, with a competitor", False],
 ],
 "sub": "Three counts per firm. Repetition: builds the same plans, in one place. Printer fit: one or two "
        "printers would cover it. Track record: has paid for a new building method before. The first two "
        "place a firm on the grid; the third is the chip colour. Open a firm for the evidence, add it to a "
        "call list, and export the list to Excel or paper.",

 "axes": [
   axis_row("repeatability", "Repetition", ""),
   axis_row("machine_fit", "Printer fit", ""),
   axis_row("innovation", "Track record", ""),
 ],

 "matrix": {
   "x_label": "Repetition: builds the same plans, in one place",
   "y_label": "Printer fit: one or two printers would cover it",
   "order": ["fail", "partial", "clear"],
   "words": {"clear": "Yes", "partial": "Partly", "fail": "No"},
 },
 "axis_titles": AXIS_TITLE,
 "matrix_note": MATRIX_NOTE,

 "role_labels": ROLE_LABELS,
 "signal_labels": SIGNAL_LABELS,
 "competitor": COMPETITOR,
 "icon_record": ICON_RECORD,
 "competitors": COMPETITORS,
 "consolidation": CONSOLIDATION,

 "limits": [
   ["The three counts",
    "Repetition asks whether a firm builds the same plans in one place. Printer fit asks "
    "whether one or two printers would cover a share of a year's output: roughly 25 to 400 homes "
    "a year in a few communities clears it, 400 to 1,500 or a decision that sits with a parent is "
    "partial, and national purchasing fails. Track record asks whether the firm has ever paid for "
    "a new way of building. Yes and Partly both keep a firm in. Only a No takes it out."],
   ["Who decides",
    "%d of %d firms have a named vice president or director of construction, or head of purchasing, "
    "and %d of those %d can be reached as named without a caveat. The other %d carry a decider who has "
    "left, who is listed at a different entity, or whose match is probable rather than confirmed; the "
    "caveat sits on the contact itself. "
    "That is the bar, because those roles can change a wall specification. Construction managers, "
    "superintendents and purchasing agents are excluded: they execute a specification rather than "
    "choose one."
    % (n_dec, n, n_dec_ok, n_dec, n_dec_chk)],
   ["Sources",
    "Company filings, company pages and trade press. Every contact is either a LinkedIn profile whose "
    "headline names the firm, or a page on the firm's own site that names the person with a title, and "
    "the sentence that identified them sits under the name. Where neither exists the field is empty "
    "with the reason stated. No URL, title or figure here was inferred."],
   ["Where a firm has no contact",
    "Several firms publish nobody. That is recorded on the card rather than left blank, because a "
    "builder closing hundreds of homes a year with no identifiable construction lead is a fact "
    "about the firm."],
   ["Scope",
    "Greater Houston and its suburban counties. Architects, engineers and permitting authorities are "
    "not covered. Firms whose product is retail shell, mid-rise or one-off architecture are held out "
    "of the deck and kept in the workbook."],
   ["Figures",
    "Where two sources disagree, both numbers appear and the disagreement is stated. Where a figure is "
    "an average across years rather than a current run rate, it says so."],
 ],


 "code": {"line": CODE_LINE,
          "items": [{"q": a, "a": t, "url": u, "source": src} for a, t, u, src in CODE],
          "precedent": [{"project": p, "where": w, "what": x, "url": u, "source": src}
                        for p, w, x, u, src in PRECEDENT],
          "quotes": [{"text": q, "who": w, "url": u, "source": src} for q, w, u, src in QUOTES]},
 "method": [{"title": a, "text": t} for a, t in METHOD],
 "bands_method": {"text": BANDS_METHOD, "sources": [{"url": u, "label": l} for u, l in BANDS_SOURCES]},
 "market": (lambda: {
   "closings": sorted([
       {"id": tid, "name": next(t["entity_name"] for t in deck if t["target_id"] == tid),
        "short": next(t["short"] for t in deck if t["target_id"] == tid),
        "low": lo, "high": hi, "year": yr, "source": src,
        "fit": next(t["marks"]["machine_fit"] for t in deck if t["target_id"] == tid),
        "method": next(t["marks"]["innovation"] for t in deck if t["target_id"] == tid),
        "group": next(t["group"] for t in deck if t["target_id"] == tid)}
       for tid, (lo, hi, yr, src) in CLOSINGS.items() if any(t["target_id"] == tid for t in deck)],
       key=lambda r: -r["high"]),
   "closings_missing": n - sum(1 for tid in CLOSINGS if any(t["target_id"] == tid for t in deck)),
   "bands": BANDS,
   "by_section": [
       {"group": gk, "label": lbl,
        "n": sum(1 for t in deck if t["group"] == gk),
        "yes": sum(1 for t in deck if t["group"] == gk and t["marks"]["innovation"] == "clear"),
        "partly": sum(1 for t in deck if t["group"] == gk and t["marks"]["innovation"] == "partial"),
        "no": sum(1 for t in deck if t["group"] == gk and t["marks"]["innovation"] == "fail"),
        "decider": sum(1 for t in deck if t["group"] == gk and t["decider_confirmed"]),
        "confirm": sum(1 for t in deck if t["group"] == gk and t["decider_caveat"]),
        "linked": sum(1 for t in deck if t["group"] == gk
                      and any(p.get("linkedin_url") or p.get("source_url") for p in t["principals"]))}
       for gk, lbl in [("adopter", "Already buying printed walls"), ("a", "Strong target"),
                       ("b", "One gap"), ("creative", "Custom and hybrid job"),
                       ("national", "National builder"), ("channel", "Land owner, not the buyer"),
                       ("icon", "Already working with ICON")]],
   "owners": [
       {"id": t["target_id"], "short": t["short"], "line": t.get("channel_line", ""),
        "builders": [{"name": b,
                      "id": next((x["target_id"] for x in deck if x["entity_name"] == b), None),
                      "off": any(x["entity_name"] == b for x in targets if x["group"] == "out")}
                     for b in t.get("channel_builders", [])]}
       for t in deck if t["group"] == "channel"],
   "printed": [{"project": a, "place": b, "printer": c, "units": d, "status": e}
               for a, b, c, d, e in PRINTED],
   "timeline": [{"year": y, "month": m, "label": l, "kind": k} for y, m, l, k in TIMELINE],
 })(),
 "stats": {"total": n, "adopters": g["adopter"], "tier_a": g["a"], "tier_b": g["b"], "out": g["out"],
           "principals": n_people, "linkedin_held": n_li, "audit_flags": n_flags,
           "with_decider": n_dec, "with_decider_live": n_dec_live,
           "with_decider_confirmed": n_dec_ok, "with_decider_caveat": n_dec_chk},
 "targets": targets,
}

# Sources have to be primary or press. Encyclopaedias and user-edited wikis are
# not citations for a business-development file, and a single one of them in a
# footnote is enough for a reader to discount the rest. The build refuses them
# rather than relying on whoever writes the next record to remember.
BANNED_SOURCES = ("wikipedia.", "wikiwand.", "dbpedia.", "fandom.", ".wiki/", "wiki.",
                  "everipedia.", "infogalactic.")


def _scan_for_banned(obj, path=""):
    found = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            found += _scan_for_banned(v, path + "/" + str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            found += _scan_for_banned(v, path + "/%d" % i)
    elif isinstance(obj, str):
        low = obj.lower()
        for b in BANNED_SOURCES:
            if b in low:
                found.append((path, obj[:140]))
                break
    return found


_banned = _scan_for_banned(DATA)
if _banned:
    for where, what in _banned:
        print("BANNED SOURCE  %s  %s" % (where, what))
    raise SystemExit("%d banned source references. No encyclopaedia or wiki citations." % len(_banned))

with open("houston-data.json", "w", encoding="utf-8") as f:
    json.dump(DATA, f, ensure_ascii=False, indent=1)

blob = json.dumps(DATA, ensure_ascii=False).replace("</script>", "<\\/script>")
html = (open("_template.html", encoding="utf-8").read()
        .replace("__DATA__", blob)
        .replace("__FONTS__", open("_fonts.css", encoding="utf-8").read())
        .replace("__MARKET__", open("_market.js", encoding="utf-8").read()))
open("ICON_Greater_Houston_Rolodex.html", "w", encoding="utf-8").write(html)

# The hosted copy. The claude.ai viewer wraps a page in its own document
# skeleton (charset, viewport, a small reset), so the artifact body is the
# same page with the document wrapper removed and the title kept at the top.
_a = html
_a = _a.split("<style>", 1)[1]          # drop doctype, html, head opening, meta, title
_a = "<title>Rolodex · Greater Houston</title>\n<style>" + _a
_a = _a.replace("</head><body>", "", 1).replace("</body></html>", "", 1)
open("rolodex-artifact.html", "w", encoding="utf-8").write(_a)

# The served copies. GitHub Pages serves /docs, so index.html there is the page.
import os, shutil
os.makedirs("docs", exist_ok=True)
shutil.copy("ICON_Greater_Houston_Rolodex.html", "docs/index.html")
shutil.copy("ICON_Greater_Houston_Rolodex.html", "docs/ICON_Greater_Houston_Rolodex.html")
shutil.copy("houston-data.json", "docs/houston-data.json")

print("entities          %d" % n)
print("already printing  %d" % g["adopter"])
print("clears all three  %d  (%d%% of roster)" % (g["a"], round(100.0 * g["a"] / n)))
print("clears two        %d" % g["b"])
print("off deck          %d" % len([t for t in targets if t["group"] == "out"]))
print("national scale    %d" % g["national"])
print("masterplan owners %d" % g["channel"])
for a in DATA["axes"]:
    print("  %-16s clear %2d  partial %2d  fail %2d" % (a["label"], a["clear"], a["partial"], a["fail"]))
print("principals        %d  (linkedin held %d)" % (n_people, n_li))
print("open items        %d" % n_flags)
print("html bytes        %d" % len(html))
