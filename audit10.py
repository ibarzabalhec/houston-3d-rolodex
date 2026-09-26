# -*- coding: utf-8 -*-
"""Build 81. Distilling.

Every card's prose was cut to its facts: the screen line, the firm, the three
reasons, the evidence, the line under each contact, the notes. Rules: lead with
the figure, one fact a sentence, no narration about pages, no method talk on a
card, nothing repeated across the fields of one card, and nothing added. A
reason keeps the figure behind its verdict. The line under a contact still
names the page.

The edits sit in distill/hou.json and distill/dfw.json as [path, old, new]. An
edit applies only while the text on the card is still the old one, so a later
change to a card is never overwritten by a stale cut. Each was checked on the
way in: no longer than the original, no number or name the card did not
already carry, no em dash, semicolon or evaluative word.
"""
import pathlib
import re

import jsonio

ROOT = pathlib.Path(__file__).resolve().parent


def _load(mk):
    p = ROOT / "distill" / ("%s.json" % mk)
    return jsonio.read(p) if p.exists() else []


def apply(D, mk):
    """Apply the cuts. Returns (applied, stale) counts and the stale paths."""
    T = {t["target_id"]: t for t in D["targets"]}
    done, stale = 0, []
    for row in _load(mk):
        t = T.get(row["target_id"])
        if not t:
            continue
        for path, old, new in row["edits"]:
            head, _, rest = path.partition(".")
            if head in ("mvp_screen", "synopsis"):
                obj, key = t, head
            elif head == "why":
                obj = next((w for w in t.get("why", []) if w.get("axis") == rest), None)
                key = "text"
            elif head == "key_projects":
                i, key = rest.split(".")
                kp = t.get("key_projects") or []
                obj = kp[int(i)] if int(i) < len(kp) else None
            elif head == "principals":
                name, _, key = rest.rpartition(".")
                obj = next((p for p in t.get("principals", []) if p.get("name") == name), None)
            elif head == "note":
                obj, key = t, rest
            elif head == "card_notes":
                cn = t.get("card_notes") or []
                i = int(rest)
                if i < len(cn) and cn[i] == old:
                    cn[i] = new
                    done += 1
                else:
                    stale.append("%s %s" % (row["target_id"], path))
                continue
            elif head == "capital_signals":
                i, key = rest.split(".")
                cs = t.get("capital_signals") or []
                obj = cs[int(i)] if int(i) < len(cs) else None
            else:
                obj = None
            if obj is None or obj.get(key) != old:
                stale.append("%s %s" % (row["target_id"], path))
                continue
            obj[key] = new
            done += 1
    return done, stale


def _resolve(D, path):
    """The container and key a global path points at, or (None, None)."""
    parts = path.split(".")
    try:
        if parts[0] in ("competitors", "icon_record") and "facts" in parts:
            base = D[parts[0]] if parts[0] == "icon_record" else D[parts[0]][int(parts[1])]
            return base["facts"][int(parts[-1])], 1
        if parts[0] == "competitors":
            return D["competitors"][int(parts[1])], parts[2]
        if parts[0] == "icon_record":
            return D["icon_record"], parts[1]
        if parts[0] in ("supply", "no_site", "chain"):
            return D[parts[0]][int(parts[1])], parts[2]
        if parts[0] == "code" and len(parts) == 2:
            return D["code"], parts[1]
        if parts[0] == "code":
            return D["code"][parts[1]][int(parts[2])], parts[3]
        if parts[0] in ("group_notes", "supply_notes"):
            return D[parts[0]], parts[1]
        if parts[0] == "consolidation":
            return D, "consolidation"
    except (KeyError, IndexError, ValueError, TypeError):
        pass
    return None, None


def apply_global(D, mk):
    """The same cut for the Field, code, supply and section notes."""
    p = ROOT / "distill" / "global.json"
    rows = jsonio.read(p) if p.exists() else []
    done, stale = 0, []
    for r in rows:
        if r["market"] != mk:
            continue
        obj, key = _resolve(D, r["path"])
        if obj is None or obj[key] != r["old"]:
            stale.append(r["path"])
            continue
        obj[key] = r["new"]
        done += 1
    return done, stale


# ------------------------------------------------------------ the page's rules
# The four limits and the method notes, cut the same way. The counts inside
# them are read from the text they replace, so they stay whatever the build
# computed.
DRAWN = {
    "hou": "Trade press, masterplan builder lists, the Builder 100, BUILDER's Local Leaders table and the "
           "Greater Houston Builders Association directory. Directory: 190 companies, five on this deck. "
           "Local Leaders added Lennar, PulteGroup and Highland Homes.",
    "dfw": "BUILDER's Local Leaders table, BUILDER firm pages, masterplan builder lists, trade press and firm "
           "websites. A research tool drew the first list. Every name, number and link was then checked "
           "against its page. What no page supports was cut.",
}
SCOPE = {
    "hou": "Greater Houston and its suburban counties. Not covered: architects, engineers, permitting "
           "authorities. One-off and retail work: the Custom and hybrid section. Held out, kept in the "
           "workbook: mid-rise multifamily, and a builder whose chief executive says it left the metro.",
    "dfw": "The Dallas-Fort Worth-Arlington metro. Not covered: architects, engineers, permitting authorities. "
           "Held out: retail shell, mid-rise and one-off architecture.",
}
METHOD = {
    "Counts on the page": "Every count is a count of the records behind the page, at build time. None is "
                          "estimated or rounded.",
    "Yes, Partly, No": "Each verdict carries its reason and sources. Partly: partial evidence. No: no record, "
                       "not a finding against the firm. Yes and Partly hold a count. No does not.",
    "Annual closings": "Published figures only: Builder 100 firm pages, HousingWire, or the firm's own site. A "
                       "range is the firm's own. Dated figures show the year. Contractors close no homes and "
                       "are not drawn.",
    "Printed units": "As reported by the developer or the printer, outlet named. Announced and unbuilt: drawn "
                     "at zero.",
    "Contacts": "A LinkedIn URL is held only where a retrieved page shows the name and the firm together. The "
                "line under each name says which page. No aggregator. No URL constructed.",
}
BANDS = ("An assumption, not a published figure. Yes: 25 to 400 homes a year, one or two printers, at up to "
         "about 200 houses a year per Titan. Published rates are slower. Wolf Ranch: one Vulcan and crew, about "
         "three weeks a home by August 2024, about seventeen a year (Engadget, 8 August 2024). Zuri Gardens: "
         "a home shell in about two weeks, per the cement supplier (Eco Material). ICON has published no Titan "
         "rate: $20 a square foot for walls, a $5,000 deposit, training from the third quarter of 2026, "
         "deliveries from early 2027 (ICON newsroom, 11 March 2026). The bands will be redrawn when ICON "
         "publishes a rate.")


# Build 83. ICON's record reads in the order a buyer asks: what is for sale,
# who has reserved it, what it has built, what it has here, then the rest of
# the business. The limits open with what the deck covers.
ICON_ORDER = ["Titan, on the record", "The first reservations", "Wolf Ranch, Georgetown",
              "Austin and the Hill Country", "Lennar in Houston", "Lennar in DFW", "Houston",
              "Dallas-Fort Worth", "The Army", "ICON Prime", "The company"]
LIMITS_ORDER = ["Scope", "How the list was drawn", "Who decides", "Sources"]


def final_copy(D, mk):
    """Returns a list of problems; empty when every block was found."""
    bad = []
    ir = D.get("icon_record") or {}
    if ir.get("facts"):
        rank = {k: i for i, k in enumerate(ICON_ORDER)}
        ir["facts"].sort(key=lambda f: rank.get(f[0], 99))
    if D.get("limits"):
        rank = {k: i for i, k in enumerate(LIMITS_ORDER)}
        D["limits"].sort(key=lambda lim: rank.get(lim[0], 99))
    for lim in D.get("limits", []):
        head, text = lim[0], lim[1]
        if head == "How the list was drawn":
            lim[1] = DRAWN[mk]
        elif head == "Scope":
            lim[1] = SCOPE[mk]
        elif head == "Who decides":
            m = re.search(r"On (\d+) of the (\d+)", text)
            lim[1] = ("Marked: a vice president or director of construction, a head of purchasing, or a "
                      "division president. These roles can change a wall specification. At a builder of 400 "
                      "homes a year or fewer that names none, the owner. At a contractor, whoever signs for "
                      "equipment." + (" Caveat on %s of %s: left, related entity, or probable match."
                                      % m.groups() if m else ""))
        elif head == "Sources":
            m = re.search(r"(\d+) a LinkedIn headline naming the firm, (\d+) the firm's own site or dated "
                          r"reporting, (\d+) a name", text)
            if not m:
                bad.append("limits/Sources: counts not found")
                continue
            lim[1] = ("Company filings, company pages, trade press. Each contact names its page: %s LinkedIn "
                      "headlines naming the firm, %s firm sites or dated reports, %s names with no page to "
                      "link. No aggregator. Nothing inferred." % m.groups())
            if mk == "dfw":
                lim[1] += " A LinkedIn link is kept only where a search result showed the name and the firm."
    for m in D.get("method", []):
        if m.get("title") == "Annual closings" and mk == "dfw":
            m["text"] = ("Published figures only: BUILDER's Local Leaders table for DFW figures, BUILDER firm "
                         "pages and the Builder 100 for company-wide figures, or the firm's own site. A range "
                         "is the firm's own. Dated figures show the year. Contractors close no homes and are "
                         "not drawn.")
        elif m.get("title") in METHOD:
            m["text"] = METHOD[m["title"]]
        elif m.get("title") == "Printer-fit bands":
            m["text"] = BANDS
    if isinstance(D.get("bands_method"), dict):
        D["bands_method"]["text"] = BANDS
    return bad
