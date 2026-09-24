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
import audit as AUDIT
import audit2 as AUDIT2
import audit3 as AUDIT3
import audit4 as AUDIT4
from trades2 import (WALL, WALL_IDS, CELL as WALL_CELL, CELL_ORDER,
                     CELL_LABEL, CELL_NOTE)
import supply as SUPPLY
import wall_people as WP
from code import CODE, CODE_LINE, PRECEDENT, QUOTES, BANDS_METHOD, BANDS_SOURCES, METHOD
import phones as PHONES
# Build 65. BUILDER's Local Leaders table for Greater Houston, read against the
# deck: three missing cards, six firms now carrying a published Houston figure,
# and one mark that did not follow its own reason.
import leaders as LEAD
import audit5 as AUDIT5
from urllib.parse import quote

BUILD = 66

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
NATIONAL.update(LEAD.NATIONAL)
for _tid, _sc in AUDIT5.SCORE.items():
    CSCORES.setdefault(_tid, {}).update(_sc)
CLOSINGS.update(AUDIT5.CLOSINGS)
PHONES.ABSENT.update(AUDIT5.PHONE_ABSENT)
for _tid, (_line, _bl) in AUDIT5.CHANNEL.items():
    CHANNEL[_tid] = (_line, _bl if _bl is not None else CHANNEL[_tid][1])
ICON_CLIENT.update(LEAD.ICON_CLIENT)
CLOSINGS.update(LEAD.CLOSINGS)
for _tid, _sc in LEAD.SCORE.items():
    CSCORES.setdefault(_tid, {}).update(_sc)
for _tid in LEAD.HOMEPAGE:
    AUDIT3.NO_WEB.pop(_tid, None)
WP.PEOPLE.update(LEAD.PEOPLE)
WP.PHONE.update(LEAD.PHONE)
WP.MORE.update(LEAD.MORE)
PHONES.ABSENT.update(LEAD.PHONE_ABSENT)
SUPPLY.SUPPLY.extend(LEAD.SUPPLY_ROWS)
for _tid, _ppl in R2.PEOPLE.items():
    NEW_PEOPLE.setdefault(_tid, []).extend(_ppl)
for _tid, _sc in R2.SCORES.items():
    CSCORES.setdefault(_tid, {}).update(_sc)
for _tid, _fl in R2.FLAGS.items():
    CFLAGS.setdefault(_tid, []).extend(_fl)
TODAY = "2026-09-24"

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
        # The number layer. Filled by the phones pass below, after the audit
        # passes have settled which homepage a card actually carries.
        t.setdefault("phone", None)
        t.setdefault("phone_label", None)
        t.setdefault("phone_source", None)
        t.setdefault("phone_rule", None)
        t.setdefault("phone_more", [])
        t.setdefault("phone_note", None)
        t.setdefault("phone_absent", None)

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
        elif t["target_id"] in TRADES or t["target_id"] in WALL_IDS:
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
SHORT.update(LEAD.SHORT)

_all = (A_TIER + REST + MID + expand_tail(TAIL) + expand_builders(BUILDERS)
        + expand_builders(NEW_CREATIVE)
        + expand_builders(NEW_TRADES, "contractor", "wall_trade")
        # Build 62. The wall supply chain: the cells the first contractor pass
        # left empty, because it found its firms through tilt-up project
        # profiles and so found tilt-up.
        + expand_builders(WALL, "contractor", "wall_trade")
        + expand_builders(NEW_METHOD)
        + expand_builders(PRINTED_ADOPTERS, "developer", "vertical_buyer")
        + expand_builders(GAP.GAP)
        + expand_builders(GAP.CHANNEL_ROWS, "mpc_developer", "channel")
        + expand_builders(LEAD.NEW))
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

# audit.py runs last, because it is a second look at what every pass above wrote.
# It removes people who cannot be called, corrects figures a source did not carry,
# and moves the counts it found pointing the wrong way.
for t in targets:
    tid = t["target_id"]
    t["principals"] = [p for p in t["principals"]
                       if (tid, p["name"]) not in AUDIT.DROP_PEOPLE]
    for (_tid, _nm), (_role, _url, _ev) in AUDIT.PEOPLE.items():
        if _tid != tid or any(p["name"] == _nm for p in t["principals"]):
            continue
        _p = {"name": _nm, "role": _role, "source_url": _url}
        if _ev:
            _p["source_evidence"] = _ev
        if AUDIT.DECIDER.get((tid, _nm)):
            _p["decider"] = True
        t["principals"].append(_p)
    for _pr in t["principals"]:
        _rt = AUDIT.RETITLE.get((tid, _pr["name"]))
        if _rt:
            _pr["role"] = _rt
    if tid in AUDIT.SYNOPSIS:
        t["synopsis"] = AUDIT.SYNOPSIS[tid]
    if tid in AUDIT.KEY_STAT:
        t["key_stat"] = AUDIT.KEY_STAT[tid]
    if tid in AUDIT.DROP_HOMEPAGE:
        t["homepage_url"] = None
    if tid in AUDIT.SCORE:
        t["scores"].update(AUDIT.SCORE[tid])
        for _k, _v in AUDIT.SCORE[tid].items():
            t["marks"][_k] = mark(_v)
        t["holds"] = sum(1 for _k in SCREENS if t["marks"][_k] != "fail")
        t["clears"] = sum(1 for _k in SCREENS if t["marks"][_k] == "clear")
    if tid in AUDIT.WHY:
        for _w, _txt in zip(t["why"], AUDIT.WHY[tid]):
            _w["text"] = _txt
    for _w in t["why"]:
        _w["mark"] = t["marks"][_w["axis"]]
        _w["verdict"] = VERDICT_WORD[_w["mark"]]
    t["key_projects"] = [k for k in t["key_projects"]
                         if (tid, k["name"]) not in AUDIT.DROP_PROJECTS]
    for _k in t["key_projects"]:
        _nu = AUDIT.EDIT_PROJECT_URL.get((tid, _k["name"]))
        if _nu:
            _k["url"] = _nu
        _nd = AUDIT.EDIT_PROJECT_DETAIL.get((tid, _k["name"]))
        if _nd:
            _k["detail"] = _nd
    for _a, _b, _c, _d, _e in AUDIT.PROJECTS.get(tid, []):
        if not any(k["name"] == _a for k in t["key_projects"]):
            t["key_projects"].append({"name": _a, "detail": _b, "signal_type": _c,
                                      "fit_signal": _d, "url": _e})
    t["sources"] = [x for x in t["sources"]
                    if (tid, x.get("url")) not in AUDIT.DROP_SOURCES]
    for _u in AUDIT.SOURCES.get(tid, []):
        if not any(x.get("url") == _u for x in t["sources"]):
            t["sources"].append({"url": _u, "date": None})

# audit2.py is the second round, and three of its entries correct the first.
for t in targets:
    tid = t["target_id"]
    t["principals"] = [p for p in t["principals"]
                       if (tid, p["name"]) not in AUDIT2.DROP_PEOPLE]
    for _pr in t["principals"]:
        _nn = AUDIT2.RENAME.get((tid, _pr["name"]))
        if _nn:
            _pr["name"] = _nn
    for (_tid, _nm), (_role, _url, _ev) in AUDIT2.PEOPLE.items():
        if _tid != tid or any(p["name"] == _nm for p in t["principals"]):
            continue
        _p = {"name": _nm, "role": _role, "source_url": _url}
        if _ev:
            _p["source_evidence"] = _ev
        if AUDIT2.DECIDER.get((tid, _nm)):
            _p["decider"] = True
        t["principals"].append(_p)
    for _pr in t["principals"]:
        _rt = AUDIT2.RETITLE.get((tid, _pr["name"]))
        if _rt:
            _pr["role"] = _rt
        if (tid, _pr["name"]) in AUDIT2.RESOURCE:
            _rs = AUDIT2.RESOURCE[(tid, _pr["name"])]
            if _rs:
                _pr["source_url"] = _rs
            else:
                _pr.pop("source_url", None)
    if tid in AUDIT2.DROP_TEAM_URL:
        t.pop("team_url", None)
    if tid in AUDIT2.SYNOPSIS:
        t["synopsis"] = AUDIT2.SYNOPSIS[tid]
    if tid in AUDIT2.KEY_STAT:
        t["key_stat"] = AUDIT2.KEY_STAT[tid]
    if tid in AUDIT2.HOMEPAGE:
        t["homepage_url"] = AUDIT2.HOMEPAGE[tid]
    if tid in AUDIT2.DROP_HOMEPAGE:
        t["homepage_url"] = None
    if tid in AUDIT2.SCORE:
        t["scores"].update(AUDIT2.SCORE[tid])
        for _k, _v in AUDIT2.SCORE[tid].items():
            t["marks"][_k] = mark(_v)
        t["holds"] = sum(1 for _k in SCREENS if t["marks"][_k] != "fail")
        t["clears"] = sum(1 for _k in SCREENS if t["marks"][_k] == "clear")
    if tid in AUDIT2.WHY:
        for _w, _txt in zip(t["why"], AUDIT2.WHY[tid]):
            _w["text"] = _txt
    for _w in t["why"]:
        _w["mark"] = t["marks"][_w["axis"]]
        _w["verdict"] = VERDICT_WORD[_w["mark"]]
    t["key_projects"] = [k for k in t["key_projects"]
                         if (tid, k["name"]) not in AUDIT2.DROP_PROJECTS]
    for _k in t["key_projects"]:
        _nu = AUDIT2.EDIT_PROJECT_URL.get((tid, _k["name"]))
        if _nu:
            _k["url"] = _nu
        _nd = AUDIT2.EDIT_PROJECT_DETAIL.get((tid, _k["name"]))
        if _nd:
            _k["detail"] = _nd
    for _a, _b, _c, _d, _e in AUDIT2.PROJECTS.get(tid, []):
        if not any(k["name"] == _a for k in t["key_projects"]):
            t["key_projects"].append({"name": _a, "detail": _b, "signal_type": _c,
                                      "fit_signal": _d, "url": _e})
    t["sources"] = [x for x in t["sources"]
                    if (tid, x.get("url")) not in AUDIT2.DROP_SOURCES]
    for _u in AUDIT2.SOURCES.get(tid, []):
        if not any(x.get("url") == _u for x in t["sources"]):
            t["sources"].append({"url": _u, "date": None})

# Round three, from a review of the shipped deck. It runs after the audit passes
# because two of its entries undo what an earlier round did: the Houston Housing
# Authority's homepage was dropped as dead and had in fact moved.
for t in targets:
    tid = t["target_id"]
    if tid in AUDIT3.NO_WEB:
        t["no_web_presence"] = True
        t["web_absent"] = AUDIT3.NO_WEB[tid]
    if tid in AUDIT3.DROP_HOMEPAGE:
        t["homepage_url"] = None
    if tid in AUDIT3.HOMEPAGE:
        t["homepage_url"] = AUDIT3.HOMEPAGE[tid]
    if tid in AUDIT3.TEAM_URL:
        t["team_url"], t["team_note"] = AUDIT3.TEAM_URL[tid]
    for p in t["principals"]:
        _s = AUDIT3.PERSON_SOURCE.get((tid, p["name"]))
        if _s:
            p["source_url"], p["source_evidence"] = _s
            p.pop("find_url", None)

# Round four. It runs after round three because both write person sources, and
# because the synopsis edits below have to be the last thing that touches the
# prose: an exact-substring replacement is only safe against text nothing else
# is still rewriting.
for t in targets:
    tid = t["target_id"]
    for _u in AUDIT4.SOURCES.get(tid, []):
        if not any(x.get("url") == _u for x in t["sources"]):
            t["sources"].append({"url": _u, "date": None})
    if tid in AUDIT4.TEAM_URL:
        t["team_url"], t["team_note"] = AUDIT4.TEAM_URL[tid]
    # The meta description was wrong for thirty builds because a sentence was
    # typed once and the data moved. A replacement that has to find its own old
    # text, exactly once, cannot go quietly stale: it fails the build instead.
    for _old, _new in AUDIT4.SYNOPSIS.get(tid, []):
        if t["synopsis"].count(_old) != 1:
            raise SystemExit("FAILED: %s synopsis does not carry the text audit4 "
                             "replaces, exactly once: %r" % (tid, _old[:60]))
        t["synopsis"] = t["synopsis"].replace(_old, _new)
    for p in t["principals"]:
        _e = AUDIT4.PERSON.get((tid, p["name"]))
        if _e:
            p["role"], p["source_url"], p["source_evidence"] = _e
            p.pop("find_url", None)

# Every entry in audit4 names a person or a card that has to exist. A typo in a
# key is otherwise a silent no-op, which is how a correction gets written, read,
# reviewed and never applied.
_ids = {t["target_id"] for t in targets}
_pairs = {(t["target_id"], p["name"]) for t in targets for p in t["principals"]}
_miss = ([k for k in AUDIT4.PERSON if k not in _pairs]
         + [(i, "") for i in list(AUDIT4.SOURCES) + list(AUDIT4.TEAM_URL)
            + list(AUDIT4.SYNOPSIS) if i not in _ids])
if _miss:
    for _m in _miss:
        print("   audit4 names %s %s, which is not on the deck" % _m)
    raise SystemExit("FAILED: audit4 has an entry that matches nothing")

# A role string is a role. It is not the place to say where the role came from,
# because a card that names its evidence in prose and carries no link is asking
# a reader to take its word for something it could have shown him. Eighteen did.
_tell = []
for t in targets:
    for p in t["principals"]:
        _r = (p.get("role") or "").lower()
        if any(s in _r for s in ("named on", "named in", "listed under", "quoted in",
                                 "the firm's own", "own team page", "own about page")):
            if not p.get("source_url"):
                _tell.append("%s / %s: %s" % (t["target_id"], p["name"], p["role"][:70]))
if _tell:
    for _s in _tell:
        print("   " + _s)
    raise SystemExit("FAILED: a role string claims a page and the card does not link it")

# Build 63. The contact layer for the 28 records Build 62 added. It shipped
# with 21 people between them, no profile, no source page, no decision-maker and
# no number, and 15 of the 28 named nobody at all. Three names come off here as
# well: a firm published three executives that corroborate nowhere and read as
# website template filler.
for t in targets:
    tid = t["target_id"]
    if tid in WP.PEOPLE:
        t["principals"] = [p for p in t["principals"]
                           if (tid, p["name"]) not in WP.DROP_PEOPLE]
        for _n, _r, _li, _su, _ev, _dec in WP.PEOPLE[tid]:
            _p = next((x for x in t["principals"] if x["name"] == _n), None)
            if _p is None:
                _p = {"name": _n}
                t["principals"].append(_p)
            if _r:
                _p["role"] = _r
            # Texan Pumpers publishes no leadership and the one person its site
            # can be tied to has no title on any page or profile. An empty role
            # is the honest record; inventing one would be worse.
            _p.setdefault("role", "")
            if _li:
                _p["linkedin_url"], _p["li_evidence"] = _li, _ev
            elif _su:
                _p["source_url"], _p["source_evidence"] = _su, _ev
            if _dec:
                _p["decider"] = True
            _p.pop("find_url", None)
    if tid in WP.NO_PEOPLE:
        t["people_absent"] = WP.NO_PEOPLE[tid]
    for _f in WP.FLAGS.get(tid, []):
        t.setdefault("card_notes", []).append(_f)

# Every entry in the contact layer has to name a card and a person that exist.
_wpb = ([k for k in WP.PEOPLE if k not in {t["target_id"] for t in targets}]
        + [k for k in WP.PHONE if k not in {t["target_id"] for t in targets}])
for (_tid, _nm) in WP.DROP_PEOPLE:
    if any(p["name"] == _nm for t in targets if t["target_id"] == _tid
           for p in t["principals"]):
        _wpb.append("%s still carries %s, which was dropped" % (_tid, _nm))
if _wpb:
    for _b in _wpb:
        print("   %s" % _b)
    raise SystemExit("FAILED: the contact layer names something that is not on the deck")

# A roster card with nobody on it has to say why. Build 62 shipped fifteen
# cards with no contact and not one of them said whether the firm publishes no
# leadership or whether nobody had looked. Those are different facts and a
# reader cannot tell them apart from a blank. The website absence has followed
# this rule since Build 59; the contact absence follows it now.
_pa = []
for t in targets:
    if t.get("group") == "out":
        continue
    if not t["principals"] and not t.get("people_absent"):
        _pa.append("%s names nobody and does not say why" % t["target_id"])
    if t["principals"] and t.get("people_absent"):
        _pa.append("%s says it names nobody and names somebody" % t["target_id"])
if _pa:
    for _b in _pa:
        print("   " + _b)
    raise SystemExit("FAILED: a card is silent about why it has no contact")

# A record cannot both carry a website and say it has none, and a record with no
# website has to say why. The three firms that never had a site were flagged and
# three more with the same condition were not, which is how the deck came to
# present one fact two ways.
_web = []
for t in targets:
    if t.get("no_web_presence") and t.get("homepage_url"):
        _web.append("%s says it has no web presence and carries one" % t["target_id"])
    if t.get("group") != "out" and not t.get("homepage_url") and not t.get("no_web_presence"):
        _web.append("%s has no homepage and is not flagged as having none" % t["target_id"])
if _web:
    for _s in _web:
        print("   " + _s)
    raise SystemExit("FAILED: a card is silent about whether the firm has a website")

# Build 65. The Local Leaders pass runs after every other layer has written its
# prose, because it corrects some of that prose, and before the number layer,
# because it sets a homepage the number layer reads. Every replacement has to
# find its own old text exactly once, and every key has to name a card.
_ll = []
for t in targets:
    tid = t["target_id"]
    if tid in LEAD.KEY_STAT:
        t["key_stat"] = LEAD.KEY_STAT[tid]
    if tid in LEAD.HOMEPAGE:
        t["homepage_url"] = LEAD.HOMEPAGE[tid]
        t.pop("no_web_presence", None); t.pop("web_absent", None)
    if tid in LEAD.SCREEN:
        t["mvp_screen"] = LEAD.SCREEN[tid]
    for w in t.get("why", []):
        if (tid, w["axis"]) in LEAD.WHY:
            w["text"] = LEAD.WHY[(tid, w["axis"])]
    for _old, _new in LEAD.SYNOPSIS.get(tid, []):
        if t["synopsis"].count(_old) != 1:
            _ll.append("%s synopsis does not carry %r exactly once" % (tid, _old[:50]))
        t["synopsis"] = t["synopsis"].replace(_old, _new)
    for _u in LEAD.SOURCES.get(tid, []):
        if not any(x.get("url") == _u for x in t["sources"]):
            t["sources"].append({"url": _u, "date": None})
    _e = LEAD.EMAIL.get(tid)
    t["email"], t["email_label"], t["email_source"] = _e if _e else (None, None, None)
_ids = {t["target_id"] for t in targets}
_keys = (list(LEAD.KEY_STAT) + list(LEAD.SCREEN) + list(LEAD.SYNOPSIS) + list(LEAD.SOURCES)
         + list(LEAD.EMAIL) + list(LEAD.HOMEPAGE) + [k for k, _a in LEAD.WHY])
_ll += ["leaders.py names %s, which is not on the deck" % k for k in _keys if k not in _ids]
for (_tid, _ax) in LEAD.WHY:
    if not any(w["axis"] == _ax for t in targets if t["target_id"] == _tid for w in t["why"]):
        _ll.append("%s has no %s reason to replace" % (_tid, _ax))
# An address with no page behind it is the same fault as a number with none.
for t in targets:
    if t.get("email") and (not t.get("email_source") or "@" not in t["email"]):
        _ll.append("%s prints an email with no page cited for it" % t["target_id"])
if _ll:
    for _b in _ll:
        print("   " + _b)
    raise SystemExit("FAILED: the Local Leaders pass did not apply cleanly")

# The number layer, last, because it is keyed on target_id and reads nothing the
# passes above write. Rule 5 records cases where the page publishes several
# numbers and designates none of them the main line: those carry a directory and
# no main line, and the card says so rather than picking one.
_RULE = {
    1: "the page publishes one number",
    2: "a tel: link in the site header or footer, so on every page",
    3: "the page labels it",
    4: "the only Houston-area line among several",
    5: "the page publishes several and designates none",
}
for t in targets:
    tid = t["target_id"]
    # Build 63. The wall supply chain shipped with no numbers at all, so the
    # 28 records added in Build 62 read the same tables from their own pass.
    _pn = dict(PHONES.PHONE); _pn.update(WP.PHONE)
    _mo = dict(PHONES.MORE); _mo.update(WP.MORE)
    _nt = dict(PHONES.NOTE); _nt.update(WP.NOTE)
    if tid in _pn:
        _d, _lab, _src, _rule = _pn[tid]
        t["phone"], t["phone_label"] = _d, _lab
        t["phone_source"], t["phone_rule"] = _src, _RULE[_rule]
    elif tid in PHONES.NO_MAIN:
        t["phone_source"], t["phone_rule"] = PHONES.NO_MAIN[tid], _RULE[5]
    # A second number may be published on a different page from the main line,
    # so an entry can carry its own source. Without it the deck cites a number
    # to a page that does not have it, which is the error this layer exists to
    # stop, one level down.
    t["phone_more"] = [{"digits": _e[0], "label": _e[1],
                        "source": _e[2] if len(_e) > 2 else None}
                       for _e in _mo.get(tid, [])]
    t["phone_note"] = _nt.get(tid)
    t["phone_absent"] = PHONES.ABSENT.get(tid)

# A number with no page behind it is the thing this whole layer exists to
# prevent. phonecheck.py tests the digits against the bytes; this tests that a
# page was named at all, and that nothing claims both a number and an absence.
_nofix = []
for t in targets:
    if (t["phone"] or t["phone_more"]) and not t["phone_source"]:
        _nofix.append("%s prints a number with no page cited for it" % t["target_id"])
    if t["phone"] and t["phone_absent"]:
        _nofix.append("%s carries a number and a stated absence" % t["target_id"])
    if t["phone"] and len(t["phone"]) != 10:
        _nofix.append("%s: %r is not ten digits" % (t["target_id"], t["phone"]))
    for _m in t["phone_more"]:
        if len(_m["digits"]) != 10:
            _nofix.append("%s: %r is not ten digits" % (t["target_id"], _m["digits"]))
if _nofix:
    for _s in _nofix:
        print("   " + _s)
    raise SystemExit("FAILED: the number layer is inconsistent")

# A corrected figure that is still printed somewhere else on the same card.
# Build 53 rewrote eleven synopses and touched nothing else on those cards, and
# five of them went out contradicting themselves. Correcting a number now means
# declaring the number it replaces, and this refuses to build while the old one
# survives anywhere the reader can see it.
_stale = []
for t in targets:
    for _old, _why in AUDIT2.SUPERSEDED.get(t["target_id"], []):
        _where = []
        if _old in (t.get("synopsis") or ""):
            _where.append("synopsis")
        if _old in (t.get("key_stat") or ""):
            _where.append("headline figure")
        for _w in t["why"]:
            if _old in _w["text"]:
                _where.append("the %s reason" % _w["axis"])
        for _k in t["key_projects"]:
            if _old in (_k["name"] + " " + _k["detail"] + " " + (_k.get("fit_signal") or "")):
                _where.append("evidence: %s" % _k["name"])
        for _p in t["principals"]:
            if _old in (_p.get("role") or ""):
                _where.append("a title")
        if _where:
            _stale.append("%s %s: %r still on the card in %s. It was superseded: %s"
                          % (t["target_id"], t["entity_name"], _old,
                             ", ".join(sorted(set(_where))), _why))
if _stale:
    for _s in _stale:
        print("   " + _s)
    raise SystemExit("FAILED: a superseded figure is still printed on its card")

# A count that moves can move a record between sections, and the section was
# assigned before the audit ran. Only the plain tiers are re-derived: adopter,
# icon, channel, national, trade and creative are assigned by what the firm is,
# not by how it scored.
for t in targets:
    if t["group"] not in ("a", "b", "out") or t["tier"] == "D":
        continue
    t["group"], t["tier"] = (("a", "A") if t["holds"] == 3 else
                             ("b", "B") if t["holds"] == 2 else
                             ("out", "C" if t["holds"] == 1 else "D"))

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
    # Build 62. Where a contractor sits in the wall value chain. The first
    # contractor pass returned 22 firms that were all one link of it and looked
    # like a market, so the section now reads in chain order and says which link
    # each firm is. Builders have no position in it: they buy the finished wall.
    if t["group"] == "trade":
        t["chain"] = WALL_CELL.get(t["target_id"])
        if not t["chain"]:
            raise SystemExit("FAILED: %s is a contractor with no place in the "
                             "wall chain" % t["target_id"])
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

# How each contact on the deck is actually evidenced. The Sources block prints
# these three numbers rather than a claim about them, because the claim it used
# to make was checkable and wrong for 40 of them.
_pp = [p for t in deck for p in t["principals"]]
n_li_p = sum(1 for p in _pp if p.get("linkedin_url"))
n_src_p = sum(1 for p in _pp if p.get("source_url") and not p.get("linkedin_url"))
n_none_p = sum(1 for p in _pp if not p.get("linkedin_url") and not p.get("source_url"))
# A decider is the stat a reader probes first, so the same split is carried for
# them and marked on the card itself.
_dd = [p for t in deck for p in t["principals"] if p.get("decider")]
n_dec_li = sum(1 for p in _dd if p.get("linkedin_url"))
n_dec_src = sum(1 for p in _dd if p.get("source_url") and not p.get("linkedin_url"))
n_dec_none = sum(1 for p in _dd if not p.get("linkedin_url") and not p.get("source_url"))
for _t in deck:
    for _p in _t["principals"]:
        if _p.get("decider") and not _p.get("linkedin_url") and not _p.get("source_url"):
            _p["unlinked"] = True
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
_hold3 = len([t for t in best if t["holds"] == 3])

def _n(k, one, many):
    return "%d %s" % (k, one if k == 1 else many)

# A description of the cell and of how it differs from the strip. Nothing about
# what the work in Houston is; the reader draws that. Plurals agree at any count.
MATRIX_NOTE = (
    # Build 64. This ran to 106 words and most of them described the grid. The
    # cell header prints its own count and both verdicts, the chips carry the
    # names, and the legend says what the colour means, so the note said all of
    # it a second time. What a reader cannot see is that the grid ignores the
    # third count, which makes this cell look like the strip's headline number
    # when it is a different set. Build 60 also had the corner wrong here for
    # the life of the deck, and naming no corner is one fewer thing to get wrong.
    # Build 66. The note compared the grid with one section and called the
    # section "all three counts", which it is not: adopters and contractors that
    # hold all three sit in their own sections. It now counts holds directly.
    "<b>%s</b> read Yes on both axes of this grid. The grid leaves out track record; "
    "<b>%d</b> of the %d hold all three counts."
    % (_n(len(best), "firm", "firms"), _hold3, len(best))
)

# A contractor closes no homes, so the closings figure is drawn against the
# builders on the deck and nothing else. One number, used everywhere it is said.
# Build 66: land owners sell lots and close no houses either, so they are out
# of the base too. The captions say builders and developers.
_n_builders = sum(1 for t in deck if t["group"] not in ("trade", "channel"))
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

# Build 66. The kicker repeated the headline beneath it word for word:
 # "screen for a construction printer" over "screened for a construction
 # printer". It now carries only what the headline does not.
 "kicker": "Rolodex · Greater Houston · %s" % TODAY,

 # Build 59 made this a statement. It had been a question with the counts inside
 # it, which broke two of this deck's own rules at once: a title says what the
 # document is rather than asking the reader something, and a count belongs in
 # the strip below, where it appears anyway. The counts are four inches down.
 "headline": "Greater Houston builders and developers, screened for a construction printer.",
 # ICON writes display sentences in two weights: the connective words drop back,
 # the load-bearing ones stay solid.
 "headline_html": ("Greater Houston builders and developers,<br>"
                   "<b>screened for a construction printer.</b>"),
 # The social preview. It was written by hand at 61 firms and the roster grew to
 # 96 without it, so a Slack unfurl or a LinkedIn card contradicted the headline
 # of the page it was previewing. It is generated now, and verify.py fails the
 # build if the number in it stops matching the roster.
 "meta_description": ("%d Greater Houston builders, developers and wall contractors screened "
                      "against three counts for a construction printer, with named "
                      "decision-makers, sources, a market view and the permitting route. "
                      "By Héctor Ibarzábal." % n),
 # A label is a name, not a sentence. The clause each of these used to carry
 # moved into the group note, where there is room to say it once.
 "group_labels": {"adopter": "Already buying printed walls", "a": "Holds all three counts",
                  "b": "One gap", "national": "National builder",
                  "trade": "Builds the wall, not the house",
                  "creative": "Custom and hybrid job",
                  "channel": "Land owner, not the buyer",
                  "icon": "Lennar and the firms it owns"},
 "group_notes": {"a": "In on all three counts.",
                 "b": "In on two of three counts.",
                 "adopter": "Has printed walls standing or contracted with a competitor.",
                 "national": "Purchasing sits at a national desk.",
                 # The three counts read differently here, and that used to be a
                 # paragraph in the methodology block at the foot of the page,
                 # four screens away from the firms it governs. It is one clause
                 # now, on the section it applies to.
                 "trade": "Houston builders do not put up their own walls, so the firm that would "
                          "run a printer is often the one they hire. The three counts are asked of "
                          "the wall rather than of the plan set.",
                 "creative": "Design-led work that does not repeat a plan set. The printed element "
                             "sits inside a conventional project.",
                 "channel": "Owns the ground. The builders inside buy the wall.",
                 "icon": "Already reachable through an existing ICON relationship."},
 # Build 61. Every number here was already a filter the reader could set by
 # hand in the bar below, and none of them said so. A figure that describes a
 # subset should hand you the subset. The fourth element is the filter the stat
 # names; null resets. Clicking one opens the List, because a filter that leaves
 # 74 of 96 chips greyed is describing the answer rather than showing it.
 "stat_strip": [
   [str(n), "firms screened", False, None],
   [str(g["a"]), "builders and developers holding all three counts", False, {"group": ["a"]}],
   # 43 here and 42 on the market view are two different things, and until
   # Build 59 both were called a decision-maker. This one counts firms with the
   # mark; the market view counts the firms where nobody on that mark carries a
   # caveat. Each label now says which.
   [str(n_dec), "with a decision-maker named", True, {"dec": "any"}],
   [str(g["adopter"]), "already printing, with a competitor", False, {"group": ["adopter"]}],
   [str(g["trade"]), "contractors who build the wall", False, {"group": ["trade"]}],
 ],
 # Build 63. This ran to five sentences and four of them described what the
 # page already shows. The two grid axes print their own definitions on the
 # grid, so the sub was repeating them verbatim four hundred pixels above. The
 # chip colour is in the legend. The sort order is visible in the chips, which
 # carry the figure they are sorted on. And the last sentence was an instruction
 # manual for three buttons that are on screen. What is left is the only thing a
 # reader cannot get from looking: what this document measures.
 "sub": "Three counts per firm: repetition, printer fit, and a track record of paying for a new "
        "building method.",

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
 # Build 61. The links were added in Build 58 and the competitor's own name sat
 # above them as plain text, so the one thing a reader would click first was the
 # one thing that was not a link. The site is read off the link list rather than
 # assembled: the entry labelled "Their site" or nothing at all. Three firms here
 # are shut or bankrupt and publish nothing, so those headers stay unlinked,
 # which is the same distinction the firm cards draw.
 "competitors": [dict(c, site=next((u for lab, u in (c.get("links") or [])
                                    if lab.lower().startswith("their site")), None))
                 for c in COMPETITORS],
 "consolidation": CONSOLIDATION,

 # Build 62. The wall value chain, in the order a wall gets made, with the count
 # in each link. The contractor section reads in this order instead of one flat
 # list, because the first contractor pass returned 22 firms that were all one
 # link and looked like a market.
 "chain": [{"key": k, "label": CELL_LABEL[k], "note": CELL_NOTE[k],
            "n": sum(1 for t in deck if t.get("chain") == k)}
           for k in CELL_ORDER if any(t.get("chain") == k for t in deck)],

 # Twenty-one firms that are not printer prospects and should be called first.
 # A post-tension plant will never buy a machine, so scoring one against printer
 # fit and putting it on the grid would be a category error dressed as rigour.
 # Nodes hold the volumes this trade does not publish. Crews hold the hands.
 "supply": [{"name": _n, "kind": _k, "chain": _cl, "region": _r, "url": _u,
             "line": _l, "why": _w,
             "people": [{"name": _pn, "role": _pr} for _pn, _pr in _pp],
             "note": _nt}
            for _key, _n, _k, _cl, _r, _u, _l, _w, _pp, _nt in SUPPLY.SUPPLY],
 "supply_labels": {
     "node": "Knows the volumes",
     "crew": "Has the crew",
 },
 "supply_notes": {
     "node": "This trade does not publish its volume. Of 87 firms found, five "
             "published a figure and twenty-four published years in business "
             "instead. Builders publish "
             "closings because the Builder 100 makes them; nothing makes a wall "
             "contractor publish anything. The numbers exist at the supplier "
             "who batches the concrete, fabricates the tendons or sells the "
             "block, and these firms sell to the crews rather than competing "
             "with them.",
     "crew": "A gunite crew already places cementitious material through a hose "
             "onto a vertical surface, to a profile, with no formwork. One of "
             "these firms advertises on its own careers page for nozzlemen, top "
             "finishers, bottom finishers and foremen. None of them has the "
             "balance sheet to buy a machine and every one of them has the "
             "people to run one.",
 },
 # The third finding, and the reason the slab link is thinner than it should be.
 "no_site": [{"name": _n, "chain": _c, "region": _r, "note": _nt}
             for _n, _c, _r, _nt in SUPPLY.NO_SITE],
 "no_site_note":
     "Twenty-one firms that meet the profile on trade association category and "
     "geography and publish no website at all: six in the Greater Houston "
     "Builders Association's foundation and concrete categories, eleven on the "
     "Associated Masonry Contractors of Houston roster, and four more. They are "
     "not small by inference, they are unlisted. This deck cannot screen them.",

 # Build 61. This block ran to nine entries and about nine hundred words, and
 # seven of the nine described something the page already shows: what a Partly
 # means is under the counts on every firm page, what is in the contractor
 # section is the note on the section, what a press item carries is the outlet
 # and date printed on the item. Text that repeats what a card shows is text a
 # reader has to get past to reach the cards. What is left is the four things a
 # card cannot show: how the roster was assembled, where the decision-maker bar
 # sits, what a contact is evidenced by, and what was deliberately left out.
 "limits": [
   ["How the list was drawn",
    "Trade press, the builder lists each master-planned community publishes, the Builder 100, "
    "and the Greater Houston Builders Association member directory. The directory carries 190 "
    "companies across seven categories. Reading all seven against this deck, and reading the "
    "metro permit leaders against it, added five firms. The rest is custom and infill work of a "
    "few homes a year, below the volume a printer is bought for."],
   ["Who decides",
    "The mark goes on a vice president or director of construction, or a head of purchasing: those "
    "roles can change a wall specification. Construction managers, superintendents and purchasing "
    "agents execute one. At a contractor it goes on whoever signs for equipment. On %d of the %d the "
    "contact carries a caveat: the person has left, sits at another entity, or is a probable match."
    % (n_dec_chk, n_dec)],
   ["Sources",
    # The three counts stay because the claim they replaced was falsifiable in
    # four clicks, and verify.py fails the build if they stop matching the data.
    "Company filings, company pages and trade press. Each contact rests on one of three, and "
    "says which: %d a LinkedIn headline naming the firm, %d the firm's own site or dated "
    "reporting, %d a name carried from a page that named them, where no staff page exists to "
    "link. Nothing was inferred. No aggregator was used."
    % (n_li_p, n_src_p, n_none_p)],
   ["Scope",
    "Greater Houston and its suburban counties. Architects, engineers and permitting authorities "
    "are not covered. Firms whose product is retail shell, mid-rise or one-off architecture are "
    "held out of the deck and kept in the workbook."],
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
       for gk, lbl in [("adopter", "Already buying printed walls"), ("a", "Holds all three counts"),
                       ("b", "One gap"), ("trade", "Builds the wall, not the house"),
                       ("creative", "Custom and hybrid job"),
                       ("national", "National builder"), ("channel", "Land owner, not the buyer"),
                       ("icon", "Lennar and the firms it owns")]],
   "owners": [
       {"id": t["target_id"], "short": t["short"], "line": t.get("channel_line", ""),
        "builders": [{"name": b,
                      "id": (AUDIT5.OWNER_ALIAS[b] if b in AUDIT5.OWNER_ALIAS else
                             next((x["target_id"] for x in deck if x["entity_name"] == b), None)),
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
 "stats": {"total": n, "adopters": g["adopter"], "tier_a": g["a"], "tier_b": g["b"],
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


# Build 66. Every correction from the fifth audit round, applied to the finished
# page data. Each has to find its old text exactly once inside the scope it names.
def _strings(obj):
    # Keys that start with an underscore are the build's working copies (the
    # verdict and reasons as first written) and never reach the page, so they
    # do not count toward "exactly once". They are still rewritten below.
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if not str(k).startswith("_"):
                yield from _strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _strings(v)


def _edit_scope(obj, old, new, hits):
    if isinstance(obj, dict):
        for k, v in list(obj.items()):
            if isinstance(v, str) and old in v:
                hits.append(1)
                obj[k] = None if (new is None and v == old) else v.replace(old, new or "")
            else:
                _edit_scope(v, old, new, hits)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            if isinstance(v, str) and old in v:
                hits.append(1)
                obj[i] = None if (new is None and v == old) else v.replace(old, new or "")
            else:
                _edit_scope(v, old, new, hits)
_bad5 = []
for _t in DATA["targets"]:
    if _t["target_id"] in AUDIT5.SCREEN:
        _t["mvp_screen"] = AUDIT5.SCREEN[_t["target_id"]]
_bad5 += ["audit5.SCREEN names %s, not on the deck" % k for k in AUDIT5.SCREEN
          if not any(t["target_id"] == k for t in DATA["targets"])]
for _scope, _old, _new in AUDIT5.EDITS:
    if _scope.startswith("HOU-"):
        _tgt = next((t for t in DATA["targets"] if t["target_id"] == _scope), None)
    else:
        _tgt = DATA.get(_scope)
    if _tgt is None:
        _bad5.append("%s is not in the page data" % _scope); continue
    _occ = sum(_s.count(_old) for _s in _strings(_tgt))
    if _occ != 1:
        _bad5.append("%s: %r found %d times" % (_scope, _old[:60], _occ)); continue
    if isinstance(_tgt, str):
        DATA[_scope] = _tgt.replace(_old, _new or "")
    else:
        _edit_scope(_tgt, _old, _new, [])
if _bad5:
    for _b in _bad5:
        print("   " + _b)
    raise SystemExit("FAILED: an audit5 edit did not find its text exactly once")

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
        .replace("__DESC__", DATA["meta_description"].replace('"', "&quot;"))
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

# The README said Ninety for thirty builds while the deck grew to 124. It is now
# written here, from the same counts the page prints, so it cannot drift again.
_ORDER = ["adopter", "icon", "a", "b", "trade", "national", "creative", "channel"]
_rd = (open("_README.md", encoding="utf-8").read()
       .replace("__N__", "%d" % n)
       .replace("__NP__", "%d" % n_people)
       .replace("__NS__", "%d" % len(DATA.get("supply", [])))
       .replace("__NN__", "%d" % len(DATA.get("no_site", [])))
       .replace("__SECTIONS__", "\n".join(
           "- **%s**, %d" % (DATA["group_labels"][k], g[k]) for k in _ORDER if g.get(k))))
open("README.md", "w", encoding="utf-8").write(_rd)

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
