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
from why import WHY, AXIS_TITLE, TRADE_AXIS_TITLE, VERDICT_WORD
from found import CONFIRMED, PROBABLE, MOVED, REMOVED, REJECTED, ADDED
from corrections import (FLAGS as CFLAGS, VERDICTS as CVERD, COMPETITOR,
                         SCORES as CSCORES, WHY_OVERRIDE as CWHY)
from links import COMPANY, PERSON, NEW_PEOPLE, DECIDERS
from machine import MACHINE, DROPPED, NATIONAL, CHANNEL, ICON_CLIENT
from creative import CREATIVE, NEW_CREATIVE, EXTRA as CEXTRA
from competitors import ICON as ICON_RECORD, COMPETITORS, CONSOLIDATION
from builders import BUILDERS
from press import PRESS
from resolved import FIRM_NOTES, PERSON_NOTES, SCREEN_NOTES
from trades import (TRADES, NEW_TRADES, NEW_METHOD, PRINTED_ADOPTERS,
                    TRADE_DECIDERS, TRADE_DECIDER_NOTES,
                    TRADE_PEOPLE, TRADE_PEOPLE_FLAGS,
                    DECIDER_PROFILES, LATE_PEOPLE, NO_PROFILE)
import research2 as R2
from market import CLOSINGS, BANDS, PRINTED, TIMELINE
import permits as PM
import focus as FOCUS
import gap as GAP
from code import CODE, CODE_LINE, PRECEDENT, QUOTES, BANDS_METHOD, BANDS_SOURCES, METHOD
from urllib.parse import quote

BUILD = 51

# The second research pass is folded into the same layers the first one wrote
# to, so every downstream rule (verification, deciders, source links) applies
# to it unchanged.
CONFIRMED.update(R2.LINKEDIN)
PERSON.update(R2.SOURCES)
DECIDERS.update(R2.DECIDERS)
DECIDERS.update(TRADE_DECIDERS)
DECIDERS.update(GAP.DECIDERS)
NATIONAL.update(GAP.NATIONAL)
CHANNEL.update(GAP.CHANNEL)
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
    "wall_trade": "Builds the wall",
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


def expand_builders(rows, etype="homebuilder", role="vertical_buyer"):
    """The builder layer carries its own verdict and reasons inline."""
    out = []
    for (tid, name, region, url, stat, syn, sc, verdict, why3,
         people, projects, srcs, flags) in rows:
        out.append({
            "target_id": tid, "entity_name": name, "entity_type": etype,
            "entity_role": role, "region": region, "homepage_url": url,
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

        for _n, _r, _u, _ev, _dec in (TRADE_PEOPLE.get(t["target_id"], [])
                                      + LATE_PEOPLE.get(t["target_id"], [])):
            if not any(p["name"] == _n for p in t["principals"]):
                _p = {"name": _n, "role": _r, "linkedin_url": _u, "li_evidence": _ev}
                if _dec:
                    _p["decider"] = True
                t["principals"].append(_p)
        for _p in t["principals"]:
            _g = GAP.PEOPLE_LINKS.get((t["target_id"], _p["name"]))
            if _g:
                _li, _su, _ev = _g
                if _li:
                    _p["linkedin_url"] = _li
                if _su:
                    _p["source_url"] = _su
                if _ev:
                    _p["li_evidence" if _li else "source_evidence"] = _ev
        for _p in t["principals"]:
            _hit = DECIDER_PROFILES.get((t["target_id"], _p["name"]))
            if _hit and not _p.get("linkedin_url"):
                _p["linkedin_url"], _p["li_evidence"] = _hit
        if t["target_id"] in NO_PROFILE and NO_PROFILE[t["target_id"]] not in t["audit_flags"]:
            t["audit_flags"].append(NO_PROFILE[t["target_id"]])

        if t["target_id"] in TRADE_PEOPLE_FLAGS:
            _f = TRADE_PEOPLE_FLAGS[t["target_id"]]
            if _f not in t["audit_flags"]:
                t["audit_flags"].append(_f)

        if t["target_id"] in GAP.DECIDER_NOTES:
            _n = GAP.DECIDER_NOTES[t["target_id"]]
            if _n not in t["audit_flags"]:
                t["audit_flags"].append(_n)

        if t["target_id"] in TRADE_DECIDER_NOTES:
            _n = TRADE_DECIDER_NOTES[t["target_id"]]
            if _n not in t["audit_flags"]:
                t["audit_flags"].append(_n)

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
        elif t["target_id"] in TRADES:
            t["group"], t["tier"] = "trade", "W"
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
        for _s in FIRM_NOTES.get(t["target_id"], []):
            if _s not in t["synopsis"]:
                t["synopsis"] = t["synopsis"].rstrip() + " " + _s
        if t["target_id"] in SCREEN_NOTES:
            t["mvp_screen"] = SCREEN_NOTES[t["target_id"]]
        for _p in t["principals"]:
            for _s in PERSON_NOTES.get("%s|%s" % (t["target_id"], _p["name"]), []):
                _p["source_evidence"] = ((_p.get("source_evidence") or "").rstrip()
                                         + " " + _s).strip()
        t["press"] = [{"date": d, "outlet": o, "headline": h, "url": u}
                      for d, o, h, u in PRESS.get(t["target_id"], [])]
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

        if t["group"] in ("adopter", "a", "b", "trade", "national", "creative", "icon",
                          "channel"):
            if t["target_id"] in FOCUS.WHY:
                texts = list(FOCUS.WHY[t["target_id"]])
            elif "_why" in t:
                texts = t["_why"]
            else:
                if t["target_id"] not in WHY:
                    raise SystemExit("no reasons written for %s (%s)"
                                     % (t["target_id"], t["entity_name"]))
                old = WHY[t["target_id"]]
                # the middle reason used to answer wall share; the machine count replaces it
                texts = [old[0], t.get("_machine_why", ""), old[2]]
            titles = TRADE_AXIS_TITLE if t["group"] == "trade" else AXIS_TITLE
            t["why"] = [{"axis": k, "title": titles[k],
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
 "HOU-132": "D.R. Horton", "HOU-133": "Hillwood", "HOU-135": "Tilson Homes",
 "HOU-001": "Wan Bridge", "HOU-005": "Radom Capital", "HOU-006": "Triten",
 "HOU-031": "Read King", "HOU-032": "Urban Living", "HOU-036": "Midway",
}

_all = (A_TIER + REST + MID + expand_tail(TAIL) + expand_builders(BUILDERS)
        + expand_builders(NEW_CREATIVE)
        + expand_builders(NEW_TRADES, "contractor", "wall_trade")
        + expand_builders(NEW_METHOD)
        + expand_builders(PRINTED_ADOPTERS, "developer", "vertical_buyer")
        + expand_builders(GAP.GAP)
        + expand_builders(GAP.CHANNEL_ROWS, "mpc_developer", "channel"))
_all = [t for t in _all if t["target_id"] not in DROPPED or t["target_id"] in CREATIVE]
targets = finalize(_all)

# focus.py runs before anything reads a mark or a section, because it changes one.
# It points each record at the product a printer can serve and drops the portfolio
# that has nothing to do with a wall.
for t in targets:
    tid = t["target_id"]
    if tid in FOCUS.SYNOPSIS:
        t["synopsis"] = FOCUS.SYNOPSIS[tid]
    if tid in FOCUS.SCREEN:
        t["mvp_screen"] = t["_verdict"] = FOCUS.SCREEN[tid]
    if tid in FOCUS.KEY_STAT:
        t["key_stat"] = FOCUS.KEY_STAT[tid]
    if tid in FOCUS.SCORE:
        t["scores"].update(FOCUS.SCORE[tid])
        for _k, _v in FOCUS.SCORE[tid].items():
            t["marks"][_k] = mark(_v)
        t["holds"] = sum(1 for _k in SCREENS if t["marks"][_k] != "fail")
        t["clears"] = sum(1 for _k in SCREENS if t["marks"][_k] == "clear")
    for _pr in t["principals"]:
        _rt = FOCUS.RETITLE.get((tid, _pr["name"]))
        if _rt:
            _pr["role"] = _rt
    for (_tid, _nm), (_role, _url, _ev) in FOCUS.PEOPLE.items():
        if _tid != tid or any(p["name"] == _nm for p in t["principals"]):
            continue
        _p = {"name": _nm, "role": _role, "source_url": _url, "source_evidence": _ev}
        _conf = FOCUS.DECIDER.get((tid, _nm))
        if _conf is not None:
            _p["decider"] = True
            if not _conf:
                _p["probable"] = True
        t["principals"].append(_p)
    for _a, _b, _c, _d, _e in FOCUS.PROJECTS.get(tid, []):
        if not any(k["name"] == _a for k in t["key_projects"]):
            t["key_projects"].append({"name": _a, "detail": _b, "signal_type": _c,
                                      "fit_signal": _d, "url": _e})
    for _u in FOCUS.SOURCES.get(tid, []):
        if not any(x.get("url") == _u for x in t["sources"]):
            t["sources"].append({"url": _u, "date": None})

# An evidence line that only repeats the title, under an icon that is already the
# link, is the same fact three times. focus.restates_title decides.
for t in targets:
    for _p in t["principals"]:
        for _f in ("li_evidence", "source_evidence"):
            if _p.get(_f) and FOCUS.restates_title(_p[_f], _p.get("role", ""),
                                                  _p.get("name", "")):
                _p.pop(_f, None)

# The grid orders chips by size, so each record carries the figure it publishes.
for t in targets:
    _c = CLOSINGS.get(t["target_id"])
    t["vol"] = _c[1] if _c else GAP.SCALE.get(t["target_id"])

for t in targets:
    t["short"] = SHORT.get(t["target_id"], t["entity_name"])
    t["cell"] = t["marks"]["repeatability"] + "|" + t["marks"]["machine_fit"]
    ch = CHANNEL.get(t["target_id"])
    if ch:
        t["channel_line"], t["channel_builders"] = ch
    if t["target_id"] in FOCUS.BUILDERS:
        t["channel_builders"] = FOCUS.BUILDERS[t["target_id"]]
        t["channel_line"] = FOCUS.CHANNEL_LINE.get(t["target_id"], t.get("channel_line", ""))

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


# The Open items list is gone from the page. What carried a fact moved into the
# record in resolved.py; what remained is the internal register in docs.
for t in targets:
    t["audit_flags"] = []

for t in targets:
    flags = t.get("audit_flags", [])
    t["audit_flags"] = ([f for f in flags if not _is_caveat(f)]
                        + [f for f in flags if _is_caveat(f)])

GROUP_ORDER = {"adopter": 0, "a": 1, "b": 2, "trade": 3, "creative": 4, "national": 5,
               "channel": 6, "icon": 7, "out": 8}
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
    "%s paid for a method that was new at the time, %s. <b>%d</b> %s partial evidence. The other <b>%d</b> %s no "
    "method record."
    % (_n(len(best), "firm", "firms"), g["a"], _n(_overlap, "firm appears", "firms appear"),
       len(best), len(best_yes), "has" if len(best_yes) == 1 else "have", _yes,
       len(best_part), "shows" if len(best_part) == 1 else "show",
       len(best_no), "has" if len(best_no) == 1 else "have")
)

# A contractor closes no homes, so the closings figure is drawn against the
# builders on the deck and nothing else. One number, used everywhere it is said.
_n_builders = sum(1 for t in deck if t["group"] != "trade")
_n_nocontact = sum(1 for t in deck if not t["principals"])
_n_press = sum(1 for t in deck if t.get("press"))
_n_nocontact_trade = sum(1 for t in deck if not t["principals"] and t["group"] == "trade")
_n_closings = sum(1 for tid in CLOSINGS if any(t["target_id"] == tid for t in deck))

DATA = {
 "version": "2.0",
 "build": BUILD,
 "last_updated": TODAY,
 # The build number is a version-control artefact. It stays in the data for the
 # workbook and the verifier, and off the page a reader sees.
 "byline": "Héctor Ibarzábal · ibarzabalhec@gmail.com · %s" % TODAY,

 "kicker": "Greater Houston · business development screen for a construction printer · %s" % TODAY,

 "headline": "Who in Greater Houston is ready to print? %d firms, three counts each." % n,
 # ICON writes display sentences in two weights: the connective words drop back,
 # the load-bearing ones stay solid. The same device, with the numbers carrying it.
 # A title, not a conclusion. What the document is, and nothing about what to think of it.
 # The counts live in the strip below, where a number belongs.
 "headline_html": ("Who in Greater Houston is ready to print?<br>"
                   "<b>%d firms. Three counts each.</b>" % n),
 # A label is a name, not a sentence. The clause each of these used to carry
 # moved into the group note, where there is room to say it once.
 "group_labels": {"adopter": "Already buying printed walls", "a": "Strong target",
                  "b": "One gap", "national": "National builder",
                  "trade": "Builds the wall, not the house",
                  "creative": "Custom and hybrid job",
                  "channel": "Land owner, not the buyer",
                  "icon": "Already working with ICON", "out": ""},
 "group_notes": {"a": "In on all three counts.",
                 "b": "In on two of three counts.",
                 "adopter": "Has printed walls standing or contracted with a competitor.",
                 "national": "Purchasing sits at a national desk.",
                 "trade": "Concrete, shell and wall contractors, and the general contractors that "
                          "self-perform concrete. Houston builders do not put up their own walls, so "
                          "the firm that would run a printer is often the one they hire.",
                 "creative": "Design-led work that does not repeat a plan set. The printed element "
                             "sits inside a conventional project.",
                 "channel": "Owns the ground. The builders inside buy the wall.",
                 "icon": "Already reachable through an existing ICON relationship."},
 "stat_strip": [
   [str(n), "firms screened", False],
   [str(g["a"]), "in on all three counts", False],
   [str(n_dec), "with a named decision-maker", True],
   [str(g["adopter"]), "already printing, with a competitor", False],
   [str(g["trade"]), "contractors who build the wall", False],
 ],
 "sub": "Three counts per firm. Repetition: builds the same plans, in one place. Printer fit: one or two "
        "printers would cover it. Track record: has paid for a new building method before. The first two "
        "place a firm on the grid; the third is the chip colour. Both axes run outward from the top left, "
        "so the first cell holds the firms that clear both counts, and inside every cell the largest "
        "published builder is first. Open a firm for the evidence, add it to a call list, and export the "
        "list to Excel or paper.",

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
    "a new way of building. Yes and Partly both count as holding a count. A No does not. A firm in on all three sits in the first section; one gap puts it in the second; the rest are grouped by what they are rather than by what they score."],
   ["The counts, read for a contractor",
    "A contractor does not close houses, so the same three questions are asked of the work rather "
    "than of the plan set. Repetition asks whether the firm puts up the same wall again and again "
    "inside one metro. Printer fit asks whether one or two printers would cover a share of the wall "
    "it puts up in a year, on the same bands, with a firm whose purchasing sits at a corporate desk "
    "scored Partly for the same reason a national builder is. Track record is unchanged."],
   ["Who decides",
    "%d of %d firms have a named vice president or director of construction, or head of purchasing, "
    "and %d of those %d can be reached as named without a caveat. The other %d carry a decider who has "
    "left, who is listed at a different entity, or whose match is probable rather than confirmed; the "
    "caveat sits on the contact itself. "
    "That is the bar, because those roles can change a wall specification. Construction managers, "
    "superintendents and purchasing agents are excluded: they execute a specification rather than "
    "choose one. At a contractor the specification belongs to somebody else, so the person marked "
    "is the one who signs for equipment: the owner, the president or the division head."
    % (n_dec, n, n_dec_ok, n_dec, n_dec_chk)],
   ["Sources",
    "Company filings, company pages and trade press. Every contact is either a LinkedIn profile whose "
    "headline names the firm, or a page on the firm's own site that names the person with a title, and "
    "the sentence that identified them sits under the name. No source URL, title or figure here was "
    "inferred. The only built links are the LinkedIn searches marked search, which run a keyword "
    "query rather than claim a page."],
   ["What is in the contractor section",
    "Concrete, shell and wall contractors, and the general contractors that self-perform concrete. "
    "The scope rule above is a builder rule and does not apply to them: most of this trade in Houston "
    "is commercial and industrial."],
   ["In the press",
    "Each item is a headline a search actually returned, with the outlet, the date the result "
    "carried, and a link read off the result rather than assembled. The headline is the "
    "publisher's."],
   ["How the list was drawn",
    "Trade press, the builder lists each master-planned community publishes, the "
    "Builder 100, and the Greater Houston Builders Association member directory. "
    "The directory carries 190 companies under Builder, Single Family and six "
    "further categories: Build-to-Rent, Build On Your Lot, ICF Homes, 50+ "
    "Communities, Multi-Family and Townhomes, and Developers. Reading all seven "
    "against this deck, and reading the metro permit leaders against it, added five "
    "firms. The rest of what the directory holds is custom and infill work of a few "
    "homes a year, below the volume a printer is bought for."],
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
   "closings_missing": _n_builders - _n_closings,
   "closings_base": _n_builders,
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
                       ("b", "One gap"), ("trade", "Builds the wall, not the house"),
                       ("creative", "Custom and hybrid job"),
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
 "permits": (lambda: {
   "quantity": PM.QUANTITY,
   "geo": PM.GEO,
   "msa": [{"year": y, "sf": PM.MSA[y][0], "all": PM.MSA[y][1], "quantity": PM.QUANTITY}
           for y in sorted(PM.MSA)],
   "counties": [{"fips": f, "name": nm,
                 "years": sorted(sf), "sf": [sf[y] for y in sorted(sf)],
                 "all": [tot[y] for y in sorted(tot)], "quantity": PM.QUANTITY}
                for f, (nm, sf, tot) in PM.COUNTY.items()],
   "place_years": PM.PLACE_YEARS,
   "places": [{"name": nm, "county": ct, "sf": v, "quantity": PM.QUANTITY}
              for nm, ct, v in PM.PLACE if any(v)],
   "geom": PM.GEOM,
   "sources": [{"url": u, "label": l} for u, l in
               [PM.SOURCE[k] for k in ("socds", "defs", "txdot")]],
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
                  "everipedia.", "infogalactic.",
                  # contact-data aggregators. A person's title is held from the firm's own
                  # page or from a LinkedIn headline, never from a resold database.
                  "zoominfo.", "rocketreach.", "apollo.io", "crunchbase.", "buzzfile.",
                  "signalhire.", "lusha.", "leadiq.", "dnb.com", "bbb.org", "yelp.com")


def _strip_trailing(obj):
    """Trailing spaces are invisible on the page and wrong in the workbook."""
    if isinstance(obj, dict):
        return {k: _strip_trailing(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_strip_trailing(v) for v in obj]
    if isinstance(obj, str):
        return obj.rstrip()
    return obj


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


DATA = _strip_trailing(DATA)
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
