# -*- coding: utf-8 -*-
"""Check the built deck in a headless browser before shipping.

Fails loudly rather than printing a clean report, so a broken build cannot be
sent by accident.
"""
import asyncio
import json
import os as _os
import pathlib
import re

from playwright.async_api import async_playwright

import audit13 as _A13
import jsonio
import paths

ROOT = pathlib.Path(__file__).parent
# Build 68. One page, two markets. MARKET=dfw runs every check against the
# Dallas-Fort Worth data, opened through the page's own market switch.
MARKET = _os.environ.get("MARKET", "houston")
# The intro reel plays first on a fresh session; ?intro=0 keeps it off for every
# check but its own, at the end.
URL = "file://" + str(paths.PAGE) + "?intro=0" + (
    "#market=dfw" if MARKET == "dfw" else "")
D = jsonio.read(paths.DFW_DATA if MARKET == "dfw" else paths.HOU_DATA)
PROBE_ID = "HOU-045" if MARKET == "houston" else next(
    t["target_id"] for t in D["targets"] if t["group"] in ("a", "b")
    and any(p.get("decider") and p.get("linkedin_url") and p.get("source_url") for p in t["principals"]))

# A reason that argues one way under a mark that says the other. Howard Hughes
# shipped for four builds marked No on the count its own sentence answered Yes,
# and nothing caught it. This does.
_NEG = re.compile(r"^(nothing on record|no method|none on record|no evidence|"
                  r"nothing published|no construction-method|no published method)", re.I)
# Round one's version matched only "is a Partly". T&T Construction wrote "sits
# at a Partly" and HTX wrote nothing at all, and both shipped a Yes over a
# reason that argued the opposite.
_SAYS = re.compile(r"\b(?:is|sits at|reads as|counts as) an? (Yes|Partly|No)\b", re.I)
_NOFIG = re.compile(r"^no [a-z ,]*(figure|volume|count|closings|revenue|headcount)"
                    r"[a-z ,]* is published", re.I)
_W = {"clear": "Yes", "partial": "Partly", "fail": "No"}
_bad = []
for _t in D["targets"]:
    for _w in _t["why"]:
        _said = _W[_w["mark"]]
        if (_NOFIG.search(_w["text"]) and _w["axis"] == "machine_fit"
                and _w["mark"] == "clear"):
            _bad.append("%s machine_fit: Yes over an absent figure" % _t["short"])
        if _NEG.search(_w["text"]) and _w["mark"] != "fail":
            _bad.append("%s %s: a negative reason under %s" % (_t["short"], _w["axis"], _said))
        _m = _SAYS.search(_w["text"])
        if _m and _m.group(1).capitalize() != _said:
            _bad.append("%s %s: the reason says %s, the mark says %s"
                        % (_t["short"], _w["axis"], _m.group(1), _said))
        if _w["verdict"] != _said:
            _bad.append("%s %s: verdict %s against mark %s"
                        % (_t["short"], _w["axis"], _w["verdict"], _said))
if _bad:
    for _b in _bad:
        print("   " + _b)
    raise SystemExit("FAILED: a reason argues against its own mark")
print("reason vs mark  : %d reasons, none contradict"
      % sum(len(t["why"]) for t in D["targets"]))

# Build 64, a rhetoric pass. The deck's rule is that whatever text is there to
# read adds a fact, not a claim about the facts. Fourteen strings had drifted
# into the family below: the nearest thing, the closest analog, the purest
# description, the single most useful line. Each of them tells a reader the
# conclusion instead of showing him the evidence, and none of them is checkable,
# which is the difference between these and "the only Texas plant" or "the
# largest published figure", both of which stay.
_RHET = re.compile(
    r"\b(?:the |a )?(?:nearest thing|closest (?:thing|analog|analogue|business|"
    r"published|existing)|purest|sharpest|strongest signal|single most|"
    r"most useful line|best[- ]fit\b|"
    # Build 66. Nine cards carried an "only" that another card on the deck
    # disproved: the only precast plant, the only masonry firm selling a
    # prefabricated wall, the only residential division. A claim ranked against
    # the rest of this deck is checkable only by reading the whole deck, and nine
    # of them failed that. Ranked against the world, "the only Texas plant", it
    # stays.
    r"the only\b[^.]{0,90}\b(?:screened|on this deck|in this section|in the whole)|"
    r"one of two \w+ screened|which no other|the one documented case|"
    r"the largest single roster)", re.I)
# Evaluative adjectives the deck does not use about its own subjects.
_ADJ = re.compile(r"\b(remarkabl[ey]|impressive(?:ly)?|striking(?:ly)?|compelling|"
                  r"exciting|extraordinar(?:y|ily)|unusually deep|truly|very )", re.I)
_EM = re.compile(r"[\u2013\u2014]")

def _rendered():
    for _t in D["targets"]:
        if _t["group"] == "out":
            continue
        yield _t["short"] + " screen", _t.get("mvp_screen") or ""
        yield _t["short"] + " synopsis", _t.get("synopsis") or ""
        for _w in _t.get("why", []):
            yield _t["short"] + " why/" + _w["axis"], _w["text"]
        for _k in _t.get("key_projects", []):
            yield _t["short"] + " evidence", _k.get("fit_signal") or ""
        for _pp in _t.get("principals", []):
            yield (_t["short"] + " person",
                   _pp.get("li_evidence") or _pp.get("source_evidence") or "")
    for _a, _b in D.get("limits", []):
        yield "limits/" + _a, _b
    for _k, _v in (D.get("group_notes") or {}).items():
        yield "group note/" + _k, _v
    for _c in D.get("chain", []):
        yield "chain/" + _c["key"], _c["note"]
    for _k, _v in (D.get("supply_notes") or {}).items():
        yield "supply note/" + _k, _v
    for _sp in D.get("supply", []):
        yield "supply/" + _sp["name"], _sp.get("why") or ""
    for _k in ("kicker", "headline", "sub", "matrix_note", "consolidation",
               "no_site_note"):
        yield _k, D.get(_k) or ""

# Build 66. The screen line prints directly under the headline figure, and on
# 30 cards its first sentence said the figure again. The first sentence of the
# screen may not carry a number the headline figure already carries.
_rep = []
for _t in D["targets"]:
    if _t["group"] == "out":
        continue
    _nums = set(re.findall(r"\d[\d,]*", _t.get("key_stat") or "")) - {"2024", "2025", "2026"}
    _first = (_t.get("mvp_screen") or "").split(". ")[0]
    if any(re.search(r"(?<![\d,])%s(?![\d,])" % re.escape(x), _first) for x in _nums):
        _rep.append("%s: %r" % (_t["short"], _first[:70]))
if _rep:
    for _b in _rep:
        print("   " + _b)
    raise SystemExit("FAILED: a screen line opens by restating its headline figure")
print("screen lines    : none restates its headline figure")

# Build 87. A screen line states facts: one or two short sentences, none of the
# words that turn a fact into an argument (so, but, would and the rest).
_argue = re.compile(r"\b(%s)\b" % "|".join(_A13.BANNED), re.I)
_sc = []
for _t in D["targets"]:
    if _t["group"] == "out":
        continue
    _s = _t.get("mvp_screen") or ""
    _m = _argue.search(_s)
    if _m:
        _sc.append("%s argues (%r): %s" % (_t["short"], _m.group(0), _s[:80]))
    if len(_s.split()) > 26 or len(re.findall(r"[a-z0-9)]\. [A-Z0-9]", _s)) > 1:
        _sc.append("%s runs long: %s" % (_t["short"], _s[:80]))
    if _t.get("type") not in dict(D.get("types") or []):
        _sc.append("%s has no type" % _t["short"])
    if "role" in _t or "kind" in _t:
        _sc.append("%s still carries a Build 88 role or kind" % _t["short"])
if _sc:
    for _b in _sc[:20]:
        print("   " + _b)
    raise SystemExit("FAILED: a screen line argues instead of stating facts, or a card has no type")
print("screen facts    : %d lines, none argues, each card has a type"
      % sum(1 for t in D["targets"] if t["group"] != "out"))

_rh, _words = [], 0
for _where, _txt in _rendered():
    _words += len(_txt.split())
    for _pat, _what in ((_RHET, "rhetoric"), (_ADJ, "an evaluative adjective"),
                        (_EM, "an em dash")):
        _m = _pat.search(_txt)
        if _m:
            _rh.append("%s carries %s: %r" % (_where, _what, _txt[max(0, _m.start()-30):_m.end()+40]))
if _rh:
    for _b in sorted(set(_rh))[:20]:
        print("   " + _b)
    raise SystemExit("FAILED: the page tells the reader a conclusion instead of showing the evidence")
print("prose           : %d words rendered, no rhetoric, no evaluative adjective, no em dash"
      % _words)

# The number layer, on shape rather than on truth. phonecheck.py tests the
# digits against the bytes of the page; this tests what the deck can check on
# its own every time it builds: that a number has a page behind it, that it is
# ten digits with a dialable area code, and that no two firms print the same
# line. A number appearing twice is either a transcription slip or a shared
# office, and both want a person to look.
_ph, _seen = [], {}
for _t in D["targets"]:
    _all = ([(_t["phone"], "main line")] if _t.get("phone") else []) + \
           [(_m["digits"], _m["label"] or "no label") for _m in _t.get("phone_more") or []]
    if _all and not _t.get("phone_source"):
        _ph.append("%s prints a number with no page cited for it" % _t["short"])
    if _t.get("phone_source") and not _t["phone_source"].startswith("http"):
        _ph.append("%s: the phone source is not a link" % _t["short"])
    if _t.get("phone") and _t.get("phone_absent"):
        _ph.append("%s carries a number and a stated absence" % _t["short"])
    # A main line that the page calls a fax is the specific error the rules in
    # phones.py exist to stop. It got four numbers wrong on the first sweep.
    if _t.get("phone") and "fax" in (_t.get("phone_label") or "").lower():
        _ph.append("%s prints a fax as its main line" % _t["short"])
    for _d, _lab in _all:
        if not (len(_d) == 10 and _d.isdigit()):
            _ph.append("%s: %r is not ten digits" % (_t["short"], _d))
        elif _d[0] in "01" or _d[3] in "01":
            _ph.append("%s: %s cannot be dialled, the area or exchange code "
                       "starts with %s" % (_t["short"], _d, _d[0] if _d[0] in "01" else _d[3]))
        # Build 68. A brand and its parent, or a masterplan and its developer,
        # can print the same office line. The card says so in phone_shared.
        if _d in _seen and _seen[_d][0] != _t["short"] and not (
                _seen[_d][1] in (_t.get("phone_shared") or [])
                or _t["target_id"] in (_seen[_d][2] or [])):
            _ph.append("%s and %s both print %s" % (_seen[_d][0], _t["short"], _d))
        _seen[_d] = (_t["short"], _t["target_id"], _t.get("phone_shared"))
if _ph:
    for _b in sorted(set(_ph)):
        print("   " + _b)
    raise SystemExit("FAILED: the number layer does not hold together")
_withph = [t for t in D["targets"] if t.get("phone")]
_nomain = [t for t in D["targets"] if not t.get("phone") and (t.get("phone_more") or [])]
print("phones          : %d records with a main line, %d with a directory and no "
      "main line, %d stated absences, %d numbers in all"
      % (len(_withph), len(_nomain),
         sum(1 for t in D["targets"] if t.get("phone_absent")), len(_seen)))

# The field section. A competitor a reader cannot look up is a name in a list.
# Every one carries at least one link, and every link is a real one.
_cf = []
for _c in D.get("competitors", []):
    _ls = _c.get("links") or []
    if not _ls:
        _cf.append("%s carries no link" % _c["name"])
    for _lab, _u in _ls:
        if not _u.startswith("http"):
            _cf.append("%s: %r is not a link" % (_c["name"], _u))
        if not _lab or len(_lab) < 4:
            _cf.append("%s: a link with no label" % _c["name"])
if _cf:
    for _b in sorted(set(_cf)):
        print("   " + _b)
    raise SystemExit("FAILED: the field section has a competitor a reader cannot follow")
print("field links     : %d competitors, %d links, none without one"
      % (len(D.get("competitors", [])),
         sum(len(c.get("links") or []) for c in D.get("competitors", []))))

# The document head, which no view renders and nothing read for thirty builds.
# It said sixty-one firms while the page said ninety-six, and it is the line a
# Slack unfurl and a LinkedIn card quote, so the preview of the page contradicted
# the page. The number in it has to be the roster count.
_md = D.get("meta_description") or ""
_mdn = [int(x) for x in re.findall(r"\b\d+\b", _md)]
_head = D.get("headline") or ""
_hb = []
if not _md:
    _hb.append("there is no meta description")
elif D["stats"]["total"] not in _mdn:
    _hb.append("the meta description says %s and the roster is %d"
               % (_mdn or "no number", D["stats"]["total"]))
if len(_md) > 320:
    _hb.append("the meta description is %d characters and will be cut" % len(_md))
# A title states what the document is. It does not ask the reader a question,
# and the counts live in the strip, which is four inches below it.
if _head.rstrip().endswith("?") or "?" in _head:
    _hb.append("the headline is a question")
if re.search(r"\d", _head):
    _hb.append("the headline carries a number, which belongs in the stat strip")
if _hb:
    for _b in _hb:
        print("   " + _b)
    raise SystemExit("FAILED: the headline or the social preview does not match the deck")
print("head and title  : description quotes %d firms, headline states rather than asks"
      % D["stats"]["total"])

# The Sources block prints how each contact is evidenced. Those three numbers
# have to be the three numbers in the data, because the sentence they replaced
# was a claim a reader could falsify in four clicks.
_p = [p for t in D["targets"] if t["group"] != "out" for p in t["principals"]]
_li = sum(1 for p in _p if p.get("linkedin_url"))
_sr = sum(1 for p in _p if p.get("source_url") and not p.get("linkedin_url"))
_nn = sum(1 for p in _p if not p.get("linkedin_url") and not p.get("source_url"))
_srcblk = "".join(b[1] for b in D.get("limits", []) if b[0] == "Sources")
_sb = []
for _v, _w in ((_li, "LinkedIn"), (_sr, "own page"), (_nn, "neither")):
    if str(_v) not in _srcblk:
        _sb.append("the Sources block does not carry %d, the %s count" % (_v, _w))
if _li + _sr + _nn != len(_p):
    _sb.append("the three evidence counts do not add to %d" % len(_p))
# Every contact with neither is marked on its own row, or the reader has to
# infer it from an icon.
for _t in D["targets"]:
    for _q in _t["principals"]:
        _bare = not _q.get("linkedin_url") and not _q.get("source_url")
        if _q.get("decider") and _bare and not _q.get("unlinked"):
            _sb.append("%s: %s is a decider with no link and is not marked"
                       % (_t["short"], _q["name"]))
        if _q.get("unlinked") and not _bare:
            _sb.append("%s: %s is marked unlinked and has a link" % (_t["short"], _q["name"]))
if _sb:
    for _b in sorted(set(_sb)):
        print("   " + _b)
    raise SystemExit("FAILED: the sources claim does not match the contacts")
print("contact evidence: %d linkedin, %d own page, %d neither, all three printed"
      % (_li, _sr, _nn))

# The note under the grid said "the top right cell" for the life of the deck.
# The cell was the top left one. Build 64 stopped naming a corner at all, which
# removes that whole class of error: the cell header prints its own count and
# both verdicts, and the chips carry the names, so the corner never needed
# saying. What the note still carries is the one thing a reader cannot see, that
# the grid ignores the third count and this cell is therefore not the strip's
# headline number. Both figures in that sentence are derived, so both are checked.
_ord = D["matrix"]["order"]
_first = "%s|%s" % (_ord[-1], _ord[-1])
_rows = [t for t in D["targets"] if t.get("cell") == _first]
# Build 66: the note now counts the firms in that cell that hold all three,
# which is the fact the grid hides, rather than comparing it with a section.
_all3 = sum(1 for t in _rows if t.get("holds") == 3)
_note = D.get("matrix_note") or ""
_nb = []
if _first != "clear|clear":
    _nb.append("the first cell drawn is %s, not the one that clears both counts" % _first)
if ("<b>%d " % len(_rows)) not in _note and ("<b>%d</b>" % len(_rows)) not in _note:
    _nb.append("the note does not carry %d, the count in that cell" % len(_rows))
if ("<b>%d</b>" % _all3) not in _note:
    _nb.append("the note does not carry %d, the firms in that cell holding all three" % _all3)
for _bad in ("top right", "top left", "bottom left", "bottom right"):
    if _bad in _note.lower():
        _nb.append("the note names a corner (%s), which is the claim that was "
                   "wrong for the life of the deck and does not need making" % _bad)
if len(_note.split()) > 45:
    _nb.append("the note runs to %d words, and the grid says most of it itself"
               % len(_note.split()))
if _nb:
    for _b in _nb:
        print("   " + _b)
    raise SystemExit("FAILED: the note under the grid does not describe the grid")
print("grid note       : %d firms and %d, both derived, %d words, no corner named"
      % (len(_rows), _all3, len(_note.split())))

# A role string that names a page has to carry that page. Eighteen contacts read
# "named on the firm's own about page" with no link on the row, which is the
# card telling a reader where to check and not letting him.
_rb = []
for _t in D["targets"]:
    for _q in _t["principals"]:
        _rl = (_q.get("role") or "").lower()
        if any(s in _rl for s in ("named on", "named in", "listed under", "quoted in",
                                  "own team page", "own about page", "the firm's own")):
            if not _q.get("source_url"):
                _rb.append("%s: %s claims a page and links none" % (_t["short"], _q["name"]))
if _rb:
    for _b in _rb:
        print("   " + _b)
    raise SystemExit("FAILED: a role string claims a page the card does not link")
print("role strings    : none asserts a page without linking it")

# Build 62. The wall value chain. The first contractor pass returned 22 firms
# that were all one link of it and read as a market, so the section is ordered
# by the chain and every contractor has to have a place in it. A contractor with
# no link is a record nobody classified, which is how 22 tilt-up firms came to
# stand for the whole trade.
_ch = {c["key"]: c for c in D.get("chain", [])}
_cb = []
if not _ch:
    _cb.append("the deck publishes no wall chain")
_tr = [t for t in D["targets"] if t.get("group") == "trade"]
for _t in _tr:
    if not _t.get("chain"):
        _cb.append("%s is a contractor with no link in the chain" % _t["short"])
    elif _t["chain"] not in _ch:
        _cb.append("%s sits in a link the chain does not publish: %s"
                   % (_t["short"], _t["chain"]))
for _k, _c in _ch.items():
    _n = sum(1 for t in _tr if t.get("chain") == _k)
    if _n != _c["n"]:
        _cb.append("the chain says %d in %s and the roster has %d" % (_c["n"], _k, _n))
    if not _c.get("note"):
        _cb.append("%s has no note saying why the link matters" % _k)
if sum(c["n"] for c in _ch.values()) != len(_tr):
    _cb.append("the chain counts do not add to the %d contractors" % len(_tr))
# A single link holding most of the trade is the condition Build 62 was for.
if _ch:
    _big = max(_ch.values(), key=lambda c: c["n"])
    if _big["n"] > len(_tr) * 0.5:
        _cb.append("%d of %d contractors sit in one link, %s, which is the "
                   "shape the first pass had" % (_big["n"], len(_tr), _big["key"]))
if _cb:
    for _b in _cb:
        print("   " + _b)
    raise SystemExit("FAILED: the contractor section does not describe the wall chain")
print("wall chain      : %d contractors across %d links, largest %d"
      % (len(_tr), len(_ch), max(c["n"] for c in _ch.values())))

# The supply panel. These are deliberately not on the grid, so the check is the
# reverse of the roster's: nothing here may also be a scored record, and every
# entry has to say what it is for.
_names = {t["entity_name"] for t in D["targets"]}
_sb = []
for _s in D.get("supply", []):
    if _s["kind"] not in D.get("supply_labels", {}):
        _sb.append("%s carries a kind the deck does not label: %s" % (_s["name"], _s["kind"]))
    if not _s.get("why"):
        _sb.append("%s is in the supply panel and does not say why" % _s["name"])
    if _s["name"] in _names:
        _sb.append("%s is in the supply panel and also a scored record" % _s["name"])
    if not _s.get("url"):
        _sb.append("%s carries no link" % _s["name"])
for _n in D.get("no_site", []):
    if _n["name"] in _names:
        _sb.append("%s is listed as publishing no website and is on the roster" % _n["name"])
if D.get("no_site") and not D.get("no_site_note"):
    _sb.append("the unlisted firms are shown with no explanation")
if _sb:
    for _b in sorted(set(_sb)):
        print("   " + _b)
    raise SystemExit("FAILED: the supply panel overlaps the roster or does not explain itself")
print("supply panel    : %d not on the grid, %d publishing no website at all"
      % (len(D.get("supply", [])), len(D.get("no_site", []))))

# Build 63. A card with nobody on it has to say why. Build 62 added 28 records
# with 21 people between them, no profile, no page, no decision-maker and no
# number, and fifteen named nobody at all without a word about it. A blank meant
# two different things that look identical: the firm publishes no leadership, or
# nobody looked.
# Build 85. An absence is a blank. The sentence that said so is gone from the
# page, so the check is now that no card carries one.
_ab = [_t["short"] for _t in D["targets"] if _t["group"] != "out"
       and (_t.get("people_absent") or _t.get("web_absent"))]
if _ab:
    for _b in _ab:
        print("   " + _b)
    raise SystemExit("FAILED: a card states an absence")
_silent = [t for t in D["targets"] if t["group"] != "out" and not t["principals"]]
print("contact absence : %d cards name nobody, left blank" % len(_silent))

# The decision-maker stat is the one a reader probes first, and it prints an
# absolute where the meaning is a proportion. Build 62 grew the roster by 29
# percent without adding a single decider, so the figure held at 43 while what
# it meant fell from 45 percent of the deck to 35, and nothing on the page or in
# this file noticed. The share is checked now.
_dec = sum(1 for t in D["targets"] if t["group"] != "out" and t.get("has_decider"))
_tot = D["stats"]["total"]
_strip = [s for s in D["stat_strip"] if "decision-maker" in s[1]]
_db = []
if not _strip:
    _db.append("the strip no longer carries the decision-maker count")
elif int(_strip[0][0]) != _dec:
    _db.append("the strip says %s deciders and the roster has %d" % (_strip[0][0], _dec))
if _dec * 100 < _tot * 40:
    _db.append("only %d of %d records name a decision-maker, %.0f percent. Adding "
               "records without contacts makes this deck worse at the one thing it "
               "is for." % (_dec, _tot, _dec / _tot * 100))
if _db:
    for _b in _db:
        print("   " + _b)
    raise SystemExit("FAILED: the decision-maker coverage does not hold")
print("decider share   : %d of %d, %.0f%% of the roster" % (_dec, _tot, _dec / _tot * 100))


async def main():
    problems = []
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1280, "height": 900})
        errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto(URL)
        await pg.wait_for_timeout(400)

        # Build 65. The page opens on the List, which is the working surface, with
        # every section showing: a pre-filtered landing would hide the 50
        # contractors from a reader told they matter. The checks below were
        # written against the Screen, so they switch to it once here.
        opened = await pg.evaluate(
            "(()=>({mode:document.getElementById('vList').getAttribute('aria-pressed'),"
            "rows:document.querySelectorAll('#tb tr:not(.grp):not(.chn)').length,"
            "first:document.querySelector('.seg[aria-label=View] button').id,"
            "head:!document.querySelector('header.top').hidden&&"
            "document.getElementById('hl').getBoundingClientRect().height>0}))()")
        print("opens on        :", "List" if opened["mode"] == "true" else "not the List",
              "with", opened["rows"], "rows, first button", opened["first"])
        if opened["mode"] != "true" or opened["first"] != "vList":
            problems.append("the page does not open on the List")
        if not opened["head"]:
            problems.append("the page opens with no masthead saying what it is")
        if opened["rows"] != D["stats"]["total"]:
            problems.append("the opening List is filtered (%d of %d)"
                            % (opened["rows"], D["stats"]["total"]))
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(300)

        chips = await pg.locator("#matrix .chip").count()
        print("console errors  :", errs or "none")
        print("chips in matrix :", chips, "of", D["stats"]["total"])
        if errs:
            problems.append("console errors")
        if chips != D["stats"]["total"]:
            problems.append("chip count does not match the roster")

        orange = await pg.locator("#matrix .chip.i-clear").count()
        want = sum(1 for t in D["targets"] if t["marks"]["innovation"] == "clear" and t["group"] != "out")
        print("orange chips    :", orange, "of an expected", want)
        if orange != want:
            problems.append("the accent is not tracking the innovation count")

        # One filter state, read by Screen, List and Cover alike. It used to be
        # two: a two-button toggle here and a seventeen-chip rail on Cover that
        # no other view could see.
        await pg.click('.fsel[data-kind="dec"] > button')
        await pg.wait_for_timeout(200)
        await pg.click('#fmenu button[data-f="dec"]')
        await pg.wait_for_timeout(250)
        lit = await pg.locator("#matrix .chip:not(.dim)").count()
        print("decider filter  :", lit, "lit, expected", D["stats"]["with_decider"])
        if lit != D["stats"]["with_decider"]:
            problems.append("decider filter count is wrong")

        # and a reset is present the moment anything is applied
        if not await pg.locator("#freset").count():
            problems.append("no reset appears when a filter is applied")

        await pg.keyboard.press("Escape")
        await pg.wait_for_timeout(120)
        for v, sel in (("vList", "#tb tr:not(.grp):not(.chn)"), ("vScroll", ".cf-card")):
            await pg.evaluate("document.getElementById('%s').click()" % v)
            await pg.wait_for_timeout(450)
            got = await pg.locator(sel).count()
            print("carries to %-7s:" % v, got)
            if got != D["stats"]["with_decider"]:
                problems.append("the filter does not carry to %s" % v)
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(200)
        await pg.click("#freset")
        await pg.wait_for_timeout(200)
        back = await pg.locator("#matrix .chip:not(.dim)").count()
        print("reset restores  :", back)
        if back != D["stats"]["total"]:
            problems.append("reset does not clear every filter")
        await pg.wait_for_timeout(150)

        await pg.eval_on_selector("#matrix .chip", "n => n.focus()")
        before = await pg.evaluate("document.activeElement.textContent")
        await pg.keyboard.press("ArrowRight")
        after = await pg.evaluate("document.activeElement.textContent")
        print("arrow key moves :", before.strip(), "->", after.strip())
        if before == after:
            problems.append("arrow keys do not move focus")

        # a firm page takes over the view rather than opening a panel
        await pg.evaluate("document.querySelector('.chip[data-id=\"%s\"]').click()" % PROBE_ID)
        await pg.wait_for_timeout(250)
        on = await pg.locator("#stageFirm.on").count()
        idx_hidden = await pg.evaluate("document.getElementById('stageIndex').hidden")
        dec = await pg.locator("#firmBody .p1.dec").count()
        ev = await pg.locator("#firmBody .p1 .ev").count()
        li_icons = await pg.locator("#firmBody .ic.li").count()
        # Build 61. The firm's own name reaches the firm's own site. A card with
        # no website keeps a plain name and says so where the pill would be.
        _hb = []
        for _t in [x for x in D["targets"] if x["group"] != "out"][:40]:
            await pg.evaluate("window.rolodex.open(%r)" % _t["target_id"])
            await pg.wait_for_timeout(45)
            _a = await pg.eval_on_selector_all(
                "#firmBody .fhead h1 a.hlink", "e=>e.map(x=>x.getAttribute('href'))")
            if _t.get("homepage_url") and _a[:1] != [_t["homepage_url"]]:
                _hb.append("%s: the name does not link the site" % _t["short"])
            if not _t.get("homepage_url") and _a:
                _hb.append("%s: the name links a site the card does not hold" % _t["short"])
        print("firm headers    : %d cards sampled, name links the site" % 40)
        problems.extend(_hb)
        await pg.evaluate("window.rolodex.open('%s')" % PROBE_ID + "")
        await pg.wait_for_timeout(200)
        print("firm page       :", "full width" if (on and idx_hidden) else "NOT taking over",
              "|", dec, "badged deciders,", ev, "evidence lines,", li_icons, "linkedin marks")
        if not on or not idx_hidden:
            problems.append("the firm view did not replace the index")
        if dec < 1 or ev < 1 or li_icons < 1:
            problems.append("decider badge, evidence line or LinkedIn mark missing")

        # company-level links render
        links = await pg.locator("#firmBody .fhead .lnk").count()
        print("company links   :", links, "on the Chesmar header")
        if links < 1:
            problems.append("no company links on the firm header")

        # every held company LinkedIn reaches the page
        with_li = [t for t in D["targets"] if t.get("company_li")][:6]
        missing = []
        for t in with_li:
            await pg.evaluate("document.getElementById('home').click()")
            await pg.wait_for_timeout(80)
            await pg.evaluate(
                "document.querySelector('.chip[data-id=\"%s\"]').click()" % t["target_id"])
            await pg.wait_for_timeout(120)
            found = await pg.locator('#firmBody a[href="%s"]' % t["company_li"]).count()
            if not found:
                missing.append(t["target_id"])
        print("company page     :", "all rendered" if not missing else "missing on " + ", ".join(missing))
        if missing:
            problems.append("company LinkedIn held but not rendered")

        # Every held number reaches the page as a dialable link, its source
        # link renders beside it, and the directory opens. Sampled across the
        # three shapes a card can take: one number, one number plus a
        # directory, and a directory with no main line.
        _s = [t for t in D["targets"] if t.get("phone") and not t.get("phone_more")][:2] + \
             [t for t in D["targets"] if t.get("phone") and t.get("phone_more")][:2] + \
             [t for t in D["targets"] if not t.get("phone") and t.get("phone_more")][:1] + \
             [t for t in D["targets"] if t.get("phone_absent")][:1]
        ph_bad, ph_dirs = [], 0
        for t in _s:
            await pg.evaluate("document.getElementById('home').click()")
            await pg.wait_for_timeout(80)
            await pg.evaluate(
                "document.querySelector('.chip[data-id=\"%s\"]').click()" % t["target_id"])
            await pg.wait_for_timeout(120)
            body = await pg.locator("#firmBody").inner_html()
            if t.get("phone"):
                if ('tel:+1%s' % t["phone"]) not in body:
                    ph_bad.append("%s: the number does not render" % t["short"])
                # A printed number with no way to check it is the same as no
                # number, so the source link is part of the number.
                if t["phone_source"] not in body:
                    ph_bad.append("%s: the number renders with no source link" % t["short"])
            for m in (t.get("phone_more") or []):
                if ('tel:+1%s' % m["digits"]) not in body:
                    ph_bad.append("%s: %s is held but not in the directory"
                                  % (t["short"], m["digits"]))
            if t.get("phone_more"):
                ph_dirs += await pg.locator("#firmBody details.ftable ul.dial").count()
            if t.get("phone_absent") and t["phone_absent"][:40] not in body:
                ph_bad.append("%s: the stated absence does not render" % t["short"])
        print("phone on card    :", "%d cards sampled, %d directories opened"
              % (len(_s), ph_dirs), "|", "clean" if not ph_bad else "; ".join(ph_bad))
        if ph_bad:
            problems.append("a held number does not reach its card")
        # The sample above can end on a card with no named contact, and the
        # call-sheet check below adds whatever firm is open. Put a firm with
        # people back on screen first.
        await pg.evaluate("document.getElementById('home').click()")
        await pg.wait_for_timeout(80)
        await pg.evaluate(
            "document.querySelector('.chip[data-id=\"%s\"]').click()" % PROBE_ID)
        await pg.wait_for_timeout(150)

        # the call sheet carries the URL in printable text
        await pg.evaluate("document.querySelector('#firmBody [data-add]').click()")
        await pg.wait_for_timeout(150)
        await pg.evaluate("document.getElementById('openCall').click()")
        await pg.wait_for_timeout(200)
        urls = await pg.locator("#firmBody .urlline").count()
        print("call sheet      :", urls, "printable links")
        if urls < 1:
            problems.append("call sheet has no printable links")

        # ---- the audit's own checks, so a regression fails the build ----

        await pg.evaluate("document.getElementById('home').click()")
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(250)

        # The stat strip has to name what it counts. It once said "clear" for a
        # number that counts holds, where a partial still counts. Build 90: the
        # strip is the List's own order and words again, as before Build 88.
        strip = await pg.eval_on_selector_all(".stat", "e=>e.map(x=>x.textContent)")
        want_a = sum(1 for t in D["targets"] if t["group"] == "a")
        lab = [x for x in strip if "all three counts" in x]
        print("stat strip      :", lab)
        # Build 66: the number is the section, builders and developers holding
        # all three. Adopters and contractors holding all three are in their own
        # sections, so the label has to say whose count it is.
        if not lab or (not re.search(r"(holding|hold) all three counts", lab[0])
                       or "builders and developers" not in lab[0]):
            problems.append("the three-count stat does not say whose holds it counts")
        if str(want_a) not in (lab[0] if lab else ""):
            problems.append("the three-count stat does not match the group count")
        if any("printer buyer" in x.lower() for x in strip):
            problems.append("the strip still counts printer buyers")

        # A firm that is both already printing and method-clear kept the black
        # ground and silently lost the accent the legend promises.
        both = [t for t in D["targets"]
                if t["group"] == "adopter" and t["marks"]["innovation"] == "clear"]
        if both:
            bg = await pg.evaluate(
                "getComputedStyle(document.querySelector('.chip.printing.i-clear')).backgroundColor")
            print("printing+clear  :", bg, "on", len(both), "firms")
            acc = await pg.evaluate(
                "(()=>{const e=document.createElement('i');e.style.background='var(--orange)';"
                "document.body.appendChild(e);const c=getComputedStyle(e).backgroundColor;e.remove();return c})()")
            if bg != acc:
                problems.append("the accent is lost where a firm is both printing and method-clear")

        # Every chip has to say what it is, not only who it is.
        al = await pg.evaluate(
            "document.querySelector('#matrix .chip').getAttribute('aria-label')||''")
        if "Repetition" not in al or "track record" not in al:
            problems.append("matrix chips do not carry their counts in the accessible name")

        # Nothing matching must say so rather than dimming every chip.
        await pg.fill("#q", "zzzznotathing")
        await pg.wait_for_timeout(300)
        zero = await pg.evaluate("document.getElementById('mzero').hidden")
        if zero:
            problems.append("the matrix has no empty state")
        await pg.fill("#q", "")
        await pg.wait_for_timeout(250)

        # The list is the view people scan, and it must work without a mouse.
        await pg.evaluate("document.getElementById('vList').click()")
        await pg.wait_for_timeout(250)
        kb = await pg.evaluate(
            "(function(){var b=document.querySelector('.fbtn2');if(!b)return false;"
            "b.focus();return document.activeElement===b;})()")
        print("list keyboard   :", kb)
        if not kb:
            problems.append("list rows are not reachable by keyboard")

        # A filtered slice has to be actionable in one gesture, not forty-five.
        before = await pg.inner_text("#clN")
        await pg.evaluate("document.querySelector('.grpadd').click()")
        await pg.wait_for_timeout(200)
        after = await pg.inner_text("#clN")
        print("bulk add        :", before, "->", after)
        if after == before:
            problems.append("add-all does not reach the call list")
        await pg.evaluate("document.querySelector('.grpadd').click()")
        await pg.wait_for_timeout(200)

        # Build 76. The type scale runs one way: a section heading is larger
        # than a firm name, a firm name is larger than its figure, and the
        # figure reads in the second ink. No label that carries content is set
        # below 10px. Measured at rest, with the pointer off the list.
        await pg.mouse.move(0, 0)
        await pg.evaluate("document.querySelectorAll('.landed').forEach(function(e){e.classList.remove('landed')})")
        await pg.wait_for_timeout(250)
        ts = await pg.evaluate(
            "(function(){function s(q){var e=document.querySelector(q);"
            "return e?parseFloat(getComputedStyle(e).fontSize):0}"
            "function c(q){var e=document.querySelector(q);return e?getComputedStyle(e).color:''}"
            "return {gl:s('#stageList tr.grp .gl'),nm:s('#stageList .fbtn2'),"
            "hf:s('#stageList td.hf'),th:s('#stageList th'),"
            "nmc:c('#stageList .fbtn2'),hfc:c('#stageList td.hf')}})()")
        print("list type scale :", ts)
        if not (ts["gl"] > ts["nm"] > ts["hf"] >= 13):
            problems.append("list type scale inverted: %r" % ts)
        if ts["th"] < 10:
            problems.append("list column labels below 10px: %r" % ts["th"])
        if ts["nmc"] == ts["hfc"]:
            problems.append("list figure reads in the same ink as the firm name")

        # Build 77. The row under the pointer lifts out of the list, and a click
        # anywhere on it, not only on the name, opens the firm.
        await pg.mouse.move(0, 0)
        rest = await pg.evaluate(
            "getComputedStyle(document.querySelector('#stageList tbody tr:not(.grp):not(.chn)')).backgroundColor")
        row = pg.locator('#stageList tbody tr:not(.grp):not(.chn)').first
        await row.locator('td.hf').hover()
        await pg.wait_for_timeout(300)
        hv = await pg.evaluate(
            "(function(){var r=document.querySelector('#stageList tbody tr:not(.grp):not(.chn)');"
            "var cs=getComputedStyle(r),td=getComputedStyle(r.querySelector('td'));"
            "return {bg:cs.backgroundColor,cur:cs.cursor,rail:td.boxShadow}})()")
        await row.locator('td.hf').click()
        await pg.wait_for_timeout(350)
        opened_row = await pg.evaluate("document.getElementById('stageIndex').hidden")
        await pg.evaluate("document.getElementById('back').click()")
        await pg.wait_for_timeout(350)
        await pg.mouse.move(0, 0)
        print("row hover       :", rest, "->", hv, "| row click opens firm", opened_row)
        if hv["bg"] == rest or hv["cur"] != "pointer" or "inset" not in hv["rail"]:
            problems.append("list row hover does not lift the row: %r" % hv)
        if not opened_row:
            problems.append("a click on a list row outside the name does not open the firm")

        # Opening and closing a firm must not drop focus on the body.
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(250)
        await pg.evaluate("document.querySelector('#matrix .chip').focus();"
                          "document.querySelector('#matrix .chip').click()")
        await pg.wait_for_timeout(300)
        foc = await pg.evaluate("document.activeElement.id||document.activeElement.tagName")
        print("focus on open   :", foc)
        if foc == "BODY":
            problems.append("focus is dropped when a firm page opens")
        await pg.keyboard.press("Escape")
        await pg.wait_for_timeout(300)
        foc2 = await pg.evaluate(
            "document.activeElement.className||document.activeElement.id||document.activeElement.tagName")
        print("focus on close  :", foc2)
        if foc2 == "BODY":
            problems.append("focus is dropped when a firm page closes")

        # Cover flow: one tap brings a card forward, it does not open it.
        await pg.evaluate("document.getElementById('vScroll').click()")
        await pg.wait_for_timeout(500)
        box = await pg.evaluate(
            "(function(){var c=document.querySelectorAll('.cf-card')[3];var r=c.getBoundingClientRect();"
            "return {x:r.x+r.width/2,y:r.y+r.height/2};})()")
        await pg.mouse.click(box["x"], box["y"])
        await pg.wait_for_timeout(700)
        on_index = await pg.evaluate(
            "!document.getElementById('stageFirm').classList.contains('on')")
        count = await pg.inner_text("#cfCount")
        print("cover tap       :", count, "| stayed on index:", on_index)
        if not on_index:
            problems.append("a tap on a non-focused card opens it instead of bringing it forward")

        # and the caret stays with the search box while it is there
        await pg.fill("#q", "houston")
        await pg.wait_for_timeout(300)
        await pg.evaluate("(function(){var q=document.getElementById('q');q.focus();"
                          "q.setSelectionRange(7,7);})()")
        await pg.keyboard.press("ArrowLeft")
        caret = await pg.evaluate("document.getElementById('q').selectionStart")
        print("search caret    :", caret)
        if caret != 6:
            problems.append("the carousel takes arrow keys from the search box")
        await pg.fill("#q", "")
        await pg.wait_for_timeout(250)

        # Search must not look live on a view it cannot filter.
        await pg.evaluate("document.getElementById('vField').click()")
        await pg.wait_for_timeout(250)
        dis = await pg.evaluate("document.getElementById('q').disabled")
        if not dis:
            problems.append("search looks live on the field view and does nothing")

        # Every link held for a competitor reaches the page. The data can carry
        # them and the render can still drop them, which is how the section
        # went twelve builds with none.
        # The site link moved onto the name in Build 61, so it is not counted in
        # the list below it. Every other link still has to render.
        _want = sum(len([link for link in (c.get("links") or []) if link[1] != c.get("site")])
                    for c in D.get("competitors", []))
        _got = await pg.locator("#fieldBody .clinks a").count()
        _blocks = await pg.locator("#fieldBody .cmp .clinks").count()
        print("field links     :", "%d of %d rendered across %d competitors"
              % (_got, _want, _blocks))
        if _got < _want or _blocks < len(D.get("competitors", [])):
            problems.append("a competitor link is held but not rendered")

        # Build 61. The name above those links was plain text, so the first thing
        # a reader reaches for was the one thing that was not a link. Every
        # competitor that publishes a site carries it on its own name, and the
        # three that are shut and publish nothing carry a plain name, which is
        # the same distinction the firm cards draw about a missing website.
        _sites = [c["name"] for c in D.get("competitors", []) if c.get("site")]
        _hrefs = await pg.eval_on_selector_all(
            "#fieldBody .cmp h3 a.hlink", "e=>e.map(x=>x.getAttribute('href'))")
        print("field headers   : %d of %d competitors link their own site"
              % (len(_hrefs), len(D.get("competitors", []))))
        if len(_hrefs) != len(_sites):
            problems.append("a competitor publishes a site and its name is not the link")
        for _c in D.get("competitors", []):
            if _c.get("site") and _c["site"] not in _hrefs:
                problems.append("%s: the header does not carry its own site" % _c["name"])

        # The roster is what a person carries into a meeting.
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(250)
        await pg.emulate_media(media="print")
        await pg.wait_for_timeout(300)
        rows = await pg.locator("#printRoster tbody tr").count()
        print("print roster    :", rows, "rows")
        if rows < D["stats"]["total"]:
            problems.append("the roster does not print")
        await pg.emulate_media(media="screen")

        # The workbook is written in the page. It has to be a real xlsx, not a
        # CSV with the wrong extension, and it has to open.
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(200)
        ok = await pg.evaluate("""(async function(){
          try{
            var rows=rolodex.exportRows(rolodex.firms.slice(0,3));
            var blob=rolodex.buildWorkbook(rolodex.firms.slice(0,3));
            var buf=new Uint8Array(await blob.arrayBuffer());
            return {sig:buf[0]===0x50&&buf[1]===0x4B, bytes:buf.length,
                    rows:rows.length, cols:rows[0].length};
          }catch(e){return {err:String(e)};}
        })()""")
        print("workbook        :", ok)
        if not ok.get("sig") or ok.get("rows", 0) < 2:
            problems.append("the in-page workbook does not build")

        # A built call list has to survive a reload.
        await pg.evaluate("rolodex.setCallList(['%s'])" % D["targets"][0]["target_id"])
        await pg.reload()
        await pg.wait_for_timeout(500)
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(200)
        kept = await pg.inner_text("#clN")
        print("call list keeps :", kept)
        if kept != "1":
            problems.append("the call list does not survive a reload")
        await pg.evaluate("rolodex.setCallList([])")

        # Back closes the firm page rather than leaving the tool.
        await pg.evaluate("document.querySelector('#matrix .chip').click()")
        await pg.wait_for_timeout(300)
        await pg.go_back()
        await pg.wait_for_timeout(400)
        on_ix = await pg.evaluate(
            "!document.getElementById('stageFirm').classList.contains('on')")
        print("back closes firm:", on_ix)
        if not on_ix:
            problems.append("browser Back leaves the tool instead of closing the firm page")

        # A decider who has left, sits at another entity, or is a probable match
        # must not read the same as one you can ring today.
        caveat = [t for t in D["targets"] if t.get("decider_caveat")]
        print("decider caveats :", len(caveat),
              "of", sum(1 for t in D["targets"] if t.get("has_decider")))
        await pg.evaluate("document.getElementById('vList').click()")
        await pg.wait_for_timeout(300)
        chk = await pg.locator(".yn.chk").count()
        if chk != len(caveat):
            problems.append("caveated deciders are not marked in the list")

        # The contractor layer. It is a section like any other, so it has to
        # filter, print, export and open like any other, and the counts it
        # carries have to be the ones the data holds.
        # Every press item carries a real link and an outlet, and the section
        # renders for a firm that has one.
        bad_press = []
        for t in D["targets"]:
            for p in t.get("press", []):
                if not str(p.get("url", "")).startswith("http") or not p.get("outlet") \
                        or not p.get("headline"):
                    bad_press.append(t["entity_name"])
        n_press = sum(1 for t in D["targets"] if t.get("press"))
        print("press           :", n_press, "firms |",
              sum(len(t.get("press") or []) for t in D["targets"]), "items")
        if bad_press:
            problems.append("press items missing a link, outlet or headline: %s" % set(bad_press))
        if n_press:
            await pg.evaluate("document.getElementById('home').click()")
            await pg.wait_for_timeout(120)
            pid = next(t["target_id"] for t in D["targets"] if t.get("press"))
            await pg.evaluate(
                "document.querySelector('.chip[data-id=\"%s\"]').click()" % pid)
            await pg.wait_for_timeout(250)
            links = await pg.locator("#firmBody .mini.press a").count()
            want = len([t for t in D["targets"] if t["target_id"] == pid][0]["press"])
            if links != want:
                problems.append("the press section does not render its items")
            await pg.evaluate("document.getElementById('home').click()")
            await pg.wait_for_timeout(120)

        # The Open items list is internal and must not reach a reader. Nothing
        # carries one in the data, nothing renders one on a card, and the
        # register itself stays out of the directory GitHub Pages serves.
        leftover = [t["entity_name"] for t in D["targets"] if t.get("audit_flags") and t["group"] != "out"]
        if leftover:
            problems.append("%d firms still carry open items" % len(leftover))
        if (ROOT / "docs" / "OPEN_ITEMS.md").exists():
            problems.append("the internal register is inside the served docs directory")
        await pg.evaluate("document.getElementById('home').click()")
        await pg.wait_for_timeout(120)
        await pg.evaluate("document.querySelector('.chip').click()")
        await pg.wait_for_timeout(220)
        labs = await pg.eval_on_selector_all("#firmBody .lab", "e=>e.map(x=>x.textContent.trim())")
        print("firm sections   :", labs)
        if any("Open item" in x for x in labs):
            problems.append("the open items section still renders")

        # An absence is a blank, not a sentence. A cell with no value stays
        # empty, and no block on the page announces that a field was checked
        # and came back with nothing. Gap language in a rendered cell or chip
        # fails the build.
        GAP = ("none published", "not disclosed", "no data", "n/a",
               "unknown", "tbd", "not available", "could not be found")
        cells = await pg.eval_on_selector_all(
            "#firmBody td, #firmBody .yn, #listBody td, .chip",
            "e=>e.map(x=>x.textContent.trim().toLowerCase())")
        hit = sorted({c for c in cells if c in GAP})
        print("gap language    :", hit or "none")
        if hit:
            problems.append("a cell narrates an absence: %s" % ", ".join(hit))
        await pg.evaluate("document.getElementById('home').click()")
        await pg.wait_for_timeout(120)

        blank = [t["entity_name"] for t in D["targets"]
                 if t["group"] != "out" and not t.get("key_stat")]
        if blank:
            problems.append("%d records show a blank headline figure" % len(blank))

        # Every record that is on the deck and not a land owner carries three
        # reasons. Twenty-two contractors once shipped with none, because the
        # section was added to the page and not to the block that builds them.
        noreason = [t["entity_name"] for t in D["targets"]
                    if t["group"] != "out" and len(t.get("why") or []) != 3]
        print("reasons missing  :", noreason or "none")
        if noreason:
            problems.append("%d records carry no reasons" % len(noreason))
        rendered = await pg.evaluate(
            "(()=>{const t=window.rolodex.data.targets.find(x=>x.group==='trade');"
            "return t?(t.why||[]).length:0})()")
        if rendered != 3:
            problems.append("a contractor record does not carry its three reasons")

        trade = [t for t in D["targets"] if t["group"] == "trade"]
        if len(trade) < 15:
            problems.append("the contractor section is missing or short")
        await pg.evaluate("document.getElementById('vList').click()")
        await pg.wait_for_timeout(300)
        hdr = await pg.locator("#tb tr.grp", has_text="Contractors and plants").count()
        # Build 62 put a header row on each link of the wall chain inside this
        # section, so a firm row is now anything that is neither a section
        # header nor a link header.
        rows_trade = await pg.evaluate(
            "(()=>{const r=[...document.querySelectorAll('#tb tr')];"
            "let on=false,n=0;for(const x of r){if(x.classList.contains('grp')){"
            "on=x.textContent.indexOf('Contractors and plants')>=0;continue;}"
            "if(x.classList.contains('chn'))continue;if(on)n++;}return n})()")
        print("contractors     :", len(trade), "in data |", rows_trade, "listed")
        if hdr != 1 or rows_trade != len(trade):
            problems.append("the contractor section does not list its firms")
        # the section filter reaches it
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(250)
        await pg.click('.fsel[data-kind="group"] > button')
        await pg.wait_for_timeout(200)
        opt = await pg.locator('#fmenu [data-f="group:trade"]').count()
        if opt != 1:
            problems.append("the contractor section is not offered in the section filter")
        else:
            await pg.click('#fmenu [data-f="group:trade"]')
            await pg.wait_for_timeout(300)
            shown = await pg.evaluate("window.rolodex.shown().length")
            print("filter to trade :", shown)
            if shown != len(trade):
                problems.append("filtering to the contractor section returns the wrong count")
            await pg.evaluate("window.rolodex.reset()")
            await pg.wait_for_timeout(200)
        # Build 61. Every number in the stat strip is now the filter it names, so
        # every number has to select exactly what it says. A stat that prints 22
        # and returns 21 firms is worse than one that returns nothing, because a
        # reader checks the strip against the list and cannot tell which is
        # wrong. Click each one and count what comes back.
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(250)
        strip = await pg.evaluate("window.rolodex.data.stat_strip")
        got = []
        for i, s in enumerate(strip):
            if not (len(s) > 3 and s[3]):
                continue
            await pg.evaluate("document.getElementById('vMatrix').click()")
            await pg.wait_for_timeout(180)
            await pg.click("#stats button.stat >> nth=%d" % i)
            await pg.wait_for_timeout(300)
            shown = await pg.evaluate("window.rolodex.shown().length")
            got.append("%s=%d" % (s[0], shown))
            if shown != int(s[0]):
                problems.append("the stat '%s' prints %s and its filter returns %d"
                                % (s[1], s[0], shown))
            on_list = await pg.evaluate("!document.getElementById('stageList').hidden")
            if not on_list:
                problems.append("the stat '%s' does not open the list" % s[1])
        print("stat strip      : %s, each filter returns what it prints" % ", ".join(got))
        # The first stat is the whole roster, so it has to put everything back.
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(180)
        await pg.click("#stats button.stat >> nth=0")
        await pg.wait_for_timeout(250)
        # The roster count, not len(targets): the file carries ten records held
        # off the deck, and they are in targets and not on the screen.
        if await pg.evaluate("window.rolodex.shown().length") != D["stats"]["total"]:
            problems.append("the roster stat does not clear the filters")
        await pg.evaluate("window.rolodex.reset()")
        await pg.wait_for_timeout(200)

        # Build 87. A filter on the Screen has to show where its firms landed:
        # each matching chip inked and first in its cell, each cell holding one
        # outlined, each cell without one receding, the other chips a trace, and
        # a strip above the grid whose counts add to the slice. Run on the
        # smallest section, so the strip also names its firms.
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(180)
        fr = await pg.evaluate("""(()=>{
          const R=window.rolodex, gs=[...new Set(R.firms.map(t=>t.group))];
          let g=null, n=1e9;
          gs.forEach(x=>{R.setFilters({group:[x]});const k=R.shown().length;if(k>0&&k<n){n=k;g=x;}});
          R.setFilters({group:[g]});
          const mh=document.getElementById('mhits');
          const cells=[...document.querySelectorAll('#matrix .cell')];
          const order=cells.every(c=>{const ch=[...c.querySelectorAll('.chip')];
            const i=ch.findIndex(e=>!e.classList.contains('match'));
            return i<0||ch.slice(i).every(e=>!e.classList.contains('match'));});
          const strip=[...mh.querySelectorAll('.mh-cell b')].reduce((a,b)=>a+(+b.textContent),0);
          const dim=document.querySelector('#matrix .chip.dim');
          return {g:g,shown:n,hidden:mh.hidden,strip:strip,
            match:document.querySelectorAll('#matrix .chip.match').length,
            named:mh.querySelectorAll('.chip[data-id]').length,
            hit:cells.filter(c=>c.classList.contains('hit')).length,
            withMatch:cells.filter(c=>c.querySelector('.chip.match')).length,
            miss:cells.filter(c=>c.classList.contains('miss')).length, cells:cells.length,
            order:order, dimop:dim?+getComputedStyle(dim).opacity:0};
        })()""")
        print("screen filter   : %s, %d firms, strip %d, %d cells outlined, dim %.2f"
              % (fr["g"], fr["shown"], fr["strip"], fr["hit"], fr["dimop"]))
        if fr["hidden"] or fr["strip"] != fr["shown"]:
            problems.append("the Screen strip does not count the filtered firms")
        if fr["match"] != fr["shown"] or not fr["order"]:
            problems.append("filtered firms are not marked, or not first in their cells")
        if fr["hit"] != fr["withMatch"] or fr["hit"] + fr["miss"] != fr["cells"]:
            problems.append("a cell's outline does not follow whether it holds a match")
        if fr["shown"] <= 20 and fr["named"] != fr["shown"]:
            problems.append("the Screen strip does not name the firms of a small slice")
        if fr["dimop"] > 0.3:
            problems.append("chips outside the filter are not dimmed enough to tell apart")
        await pg.evaluate("window.rolodex.reset()")
        await pg.wait_for_timeout(200)
        if not await pg.evaluate("document.getElementById('mhits').hidden"):
            problems.append("the Screen strip stays up with no filter applied")

        # a contractor names the person who signs for equipment, not a specification
        badge = await pg.evaluate(
            "(()=>{const t=window.rolodex.data.targets.find(x=>x.group==='trade'"
            "&&(x.principals||[]).some(p=>p.decider));return t?t.target_id:null})()")
        if not badge:
            problems.append("no contractor carries a decision-maker")

        # The market view: five figures, each with a table, tooltips on marks,
        # and nothing drawn that the data does not hold.
        await pg.evaluate("document.getElementById('vMarket').click()")
        await pg.wait_for_timeout(400)
        figs = await pg.locator(".figs:not(.method)").count()
        # Build 67. The timeline is an ordered list, which is its own table.
        tabs = (await pg.locator(".figs .ftable table").count()
                + await pg.locator(".figs ol.tline").count()
                + await pg.locator(".figs ol.nlist").count())
        bars = await pg.locator("#mkBody .figs .fig .bar").count()
        print("market figures  :", figs, "| tables", tabs, "| closing bars", bars)
        # Build 80: eleven, with ICON's printer test and the news list.
        if figs != 11 or tabs != 11:
            problems.append("the market view does not draw eleven figures with tables (%d, %d)"
                            % (figs, tabs))
        # the market tab explains nothing about its own method any more
        if await pg.locator("#mkBody .figs.method").count():
            problems.append("a method block is back on the market tab")

        # The permit layer is a different quantity from the closings layer and is
        # never mixed with it. Three levels of the same survey must reconcile
        # exactly, every figure must carry a source, and the map must draw ten
        # counties.
        P = D["permits"]
        msa = {r["year"]: r["sf"] for r in P["msa"]}
        for c in P["counties"]:
            if len(c["years"]) != len(c["sf"]):
                problems.append("a county permit series is ragged")
        for y in P["counties"][0]["years"]:
            tot = sum(c["sf"][c["years"].index(y)] for c in P["counties"])
            if tot != msa.get(y):
                problems.append("county permits do not sum to the metro in %d (%d vs %s)"
                                % (y, tot, msa.get(y)))
        pyi = len(P["place_years"]) - 1
        by_cty = {}
        for pl in P["places"]:
            by_cty[pl["county"]] = by_cty.get(pl["county"], 0) + pl["sf"][pyi]
        for c in (P["counties"] if P.get("places_complete", True) else []):
            y = P["place_years"][pyi]
            want = c["sf"][c["years"].index(y)]
            if by_cty.get(c["name"], 0) != want:
                problems.append("jurisdictions do not sum to %s County in %d" % (c["name"], y))
        if any(r.get("quantity") != "authorized" for r in P["msa"]):
            problems.append("a permit figure is not labelled as an authorisation")
        if len(P["geom"]) != len(P["counties"]):
            problems.append("the county map does not carry an outline per county")
        if not P["sources"] or any(not s0["url"].startswith("http") for s0 in P["sources"]):
            problems.append("a permit source is missing its link")
        # The cross-reads live here, not on the page. A reader is owed the number,
        # not the working that established it.
        import permits as _PM
        if MARKET != "houston":
            _PM = type("X", (), {"CROSSREF": [], "REVISIONS": []})
        for lb, _gg, yy, vv, key, _ind in _PM.CROSSREF:
            if "socds" in key:
                ours = msa.get(yy) if "Single family" in lb else None
                if ours is not None and ours != vv:
                    problems.append("the %d figure moved away from its cross-read" % yy)
        nahb = [c for c in _PM.CROSSREF if c[4] == "nahb"]
        if nahb:
            gap = abs(msa.get(nahb[0][2], 0) - nahb[0][3])
            print("cross-read      : %d vs NAHB %d, gap %d"
                  % (msa.get(nahb[0][2], 0), nahb[0][3], gap))
            if gap > 50:
                problems.append("the metro figure no longer agrees with the published cross-read")
        if any(abs(b - a) > 1200 for _y, a, b in _PM.REVISIONS):
            problems.append("an archived Census year now differs by more than 1,200 units")
        if "defs" in P or "crossref" in P or "revisions" in P:
            problems.append("survey method or cross-reads are shipping on the page")
        srcs = await pg.locator("#mkBody .figsrc a").count()
        cty_paths = await pg.locator("#figMap .cty").count()
        cells = await pg.locator("#mtxHost .cell").count()
        jur = await pg.locator("#jurHost .bar").count()
        print("permits         :", len(P["msa"]), "years |", len(P["counties"]), "counties |",
              len(P["places"]), "jurisdictions | source links", srcs)
        if cty_paths != len(P["counties"]):
            problems.append("the county map does not render every county")
        if cells != len(P["counties"]) * len(P["counties"][0]["years"]):
            problems.append("the county matrix does not render every cell")
        if jur != 25:
            problems.append("the jurisdiction chart does not render its top 25")
        if srcs < 5:
            problems.append("permit figures are missing their source links")

        # Build 70. Lakes, where a market carries them: every one drawn, clipped
        # to the metro, credited on the map, and no county label standing in one.
        lakes = await pg.evaluate(
            "(()=>{const w=[...document.querySelectorAll('#figMap .water path')];"
            "const ls=[...document.querySelectorAll('#figMap .ctyl')];"
            "const wet=ls.filter(t=>{const x=+t.getAttribute('x'),y=+t.getAttribute('y')+2;"
            "return w.some(p=>p.isPointInFill(new DOMPoint(x,y)));}).map(t=>t.textContent);"
            "const g=document.querySelector('#figMap .water');"
            "const cap=(document.querySelector('#figMap')||{}).textContent||'';"
            "return {n:w.length,clip:!!(g&&g.getAttribute('clip-path')),wet:wet,"
            "credit:/lakes: TxDOT|lakes are/i.test(cap),src:/Water Bodies/i.test(cap)}})()")
        want = len(P.get("water") or [])
        print("lakes           :", lakes["n"], "drawn of", want, "| clipped", lakes["clip"],
              "| labels in water", len(lakes["wet"]))
        if lakes["n"] != want:
            problems.append("the county map does not draw every lake the data holds")
        if want and not (lakes["clip"] and lakes["credit"] and lakes["src"]):
            problems.append("the lakes are unclipped or uncredited")
        if lakes["wet"]:
            problems.append("a county label sits in a lake: " + ", ".join(lakes["wet"]))

        # the two quantities never share a figure
        mixed = await pg.evaluate(
            "(()=>{const t=[...document.querySelectorAll('#mkBody .figs')];"
            "return t.filter(s=>/units authorised/i.test(s.textContent)"
            "&&/homes a year/i.test(s.textContent)).length})()")
        if mixed:
            problems.append("a figure mixes permits with closings")
        want_bars = (len(D["market"]["closings"])
                     + sum(1 for r in D["market"]["printed"] if r["units"] > 0)
                     + len(D["permits"]["msa"]) + 25)
        if bars != want_bars:
            problems.append("bar count does not match the published figures (%d vs %d)"
                            % (bars, want_bars))
        # Build 65. Both closings figures used to clamp at 1,200 with Math.min,
        # which was harmless while the largest figure was 1,062 and would have
        # drawn Lennar's 6,362 at 1,200 without a word. A bar past the axis now
        # has to carry a break mark, and the hero has to name every firm it
        # leaves off rather than pile them on its right edge.
        brk = await pg.locator("#mkBody .fig .brk").count()
        want_brk = sum(1 for r in D["market"]["closings"] if r["low"] > 2000)
        print("broken bars     :", brk, "of", want_brk, "past the 2,000 axis")
        if brk != want_brk:
            problems.append("a closings bar runs past the axis without a break mark")
        hero = await pg.evaluate(
            "(()=>({dots:document.querySelectorAll('#heroFig .hdot').length,"
            "cap:document.getElementById('heroFig').textContent}))()")
        _over = [r for r in D["market"]["closings"] if r["high"] > 1500]
        if hero["dots"] != len(D["market"]["closings"]) - len(_over):
            problems.append("the hero strip draws a firm outside its bands")
        for r in _over:
            if r["short"] not in hero["cap"]:
                problems.append("the hero strip leaves %s off without naming it" % r["short"])
        print("hero strip      :", hero["dots"], "dots,", len(_over), "named above 1,500")
        # Build 66. The landing said how the bands were set was on this view,
        # and nothing here rendered it.
        band = await pg.evaluate("(()=>{var b=document.querySelector('#mkBody .bandnote');"
                                 "return b?b.textContent:''})()")
        if "assumption" not in band or "200" not in band:
            problems.append("the printer-fit band assumption is not on the Market view")
        print("band note       :", "rendered" if band else "missing")
        # ---- Build 66, the fifth audit round's interaction findings
        await pg.evaluate("rolodex.reset()")
        await pg.evaluate("document.getElementById('vScroll').click()")
        await pg.wait_for_timeout(300)
        await pg.focus("#cfNext")
        await pg.keyboard.press("Enter")
        await pg.wait_for_timeout(250)
        v66 = await pg.evaluate("(()=>({firm:document.getElementById('stageFirm').classList.contains('on'),"
                                "ae:document.activeElement&&document.activeElement.id}))()")
        if v66["firm"]:
            problems.append("Enter on the Cover's Next button opens a firm instead")
            await pg.evaluate("history.back()")
            await pg.wait_for_timeout(250)
        await pg.evaluate("document.getElementById('vList').click()")
        await pg.wait_for_timeout(250)
        await pg.evaluate("document.querySelector('#tb .rowadd').focus()")
        await pg.keyboard.press("Enter")
        await pg.wait_for_timeout(250)
        fk = await pg.evaluate("(()=>{var a=document.activeElement;return a&&a.getAttribute('data-add')})()")
        await pg.evaluate("rolodex.setCallList([])")
        if not fk:
            problems.append("focus leaves the + on a List row after it is pressed")
        _yp = sum(1 for t in D["targets"] if t["group"] != "out"
                  and t["marks"]["machine_fit"] in ("clear", "partial"))
        orn = await pg.evaluate("(()=>{rolodex.reset();rolodex.setFilters({count:"
                                "['machine_fit:clear','machine_fit:partial']});"
                                "return rolodex.shown().length})()")
        await pg.evaluate("rolodex.reset()")
        if orn != _yp:
            problems.append("two choices on one count do not combine as either (%d vs %d)" % (orn, _yp))
        await pg.fill("#q", "zzzzqq")
        await pg.wait_for_timeout(400)
        sup = await pg.evaluate("document.getElementById('supplyBody').textContent.trim().length")
        await pg.fill("#q", "")
        await pg.wait_for_timeout(300)
        if sup:
            problems.append("a search with no match still shows the supply and no-website lists")
        print("audit round 5   : cover keys, row focus, same-count OR (%d), supply search" % orn)
        await pg.evaluate("document.getElementById('vMarket').click()")
        await pg.wait_for_timeout(500)

        # a segment opens the firms it counts, and the list survives an add
        # Build 67. Clicked at its centre: a fixed x of 100 fell off the segment
        # once the section held one firm fewer.
        _sg = pg.locator('.fig .seg[data-seg="a:partial"]')
        await _sg.scroll_into_view_if_needed()
        _bb = await _sg.bounding_box()
        await pg.mouse.click(_bb["x"] + _bb["width"] / 2, _bb["y"] + _bb["height"] / 2)
        await pg.wait_for_timeout(300)
        seg_rows = await pg.locator("#segList .segrow").count()
        want_seg = sum(1 for t in D["targets"] if t["group"] == "a" and t["marks"]["innovation"] == "partial")
        print("segment list    :", seg_rows, "rows, expected", want_seg)
        if seg_rows != want_seg:
            problems.append("a chart segment does not list its firms")
        await pg.click("#segList .rowadd >> nth=0")
        await pg.wait_for_timeout(300)
        if await pg.evaluate("document.getElementById('segList').hidden"):
            problems.append("the segment list closes when a firm is added from it")
        await pg.evaluate("rolodex.setCallList([])")
        await pg.click("#segClose")
        await pg.wait_for_timeout(150)

        await pg.hover(".fig .bar >> nth=0")
        await pg.wait_for_timeout(200)
        tipped = await pg.evaluate("!document.getElementById('tip').hidden")
        if not tipped:
            problems.append("marks carry no tooltip")
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(200)

        # phone widths: the view switcher must be hittable, not a hairline
        for w in (320, 390, 430):
            await pg.set_viewport_size({"width": w, "height": 800})
            await pg.wait_for_timeout(300)
            hits = await pg.evaluate(
                "[...document.querySelectorAll('.navtools .seg button')].map(function(b){"
                "var r=b.getBoundingClientRect();"
                "var e=document.elementFromPoint(r.x+r.width/2,r.y+r.height/2);"
                "return !!(e&&(e===b||b.contains(e)));})")
            over = await pg.evaluate(
                "document.documentElement.scrollWidth - document.documentElement.clientWidth")
            print("at %-4d        : view buttons hittable %s, overflow %s"
                  % (w, all(hits), over))
            if not all(hits):
                problems.append("view buttons are not tappable at %dpx" % w)
            if over > 0:
                problems.append("horizontal overflow at %dpx" % w)

            # Build 66. Firm pages scrolled sideways on a phone, 22 of them,
            # because a long source URL had no break point. Every firm page is
            # opened at this width and measured.
            fw = await pg.evaluate(
                "(()=>{var bad=[];rolodex.firms.forEach(function(t){rolodex.open(t.target_id);"
                "var o=document.documentElement.scrollWidth-document.documentElement.clientWidth;"
                "if(o>0) bad.push(t.short+' '+o);history.back();});return bad;})()")
            await pg.wait_for_timeout(300)
            await pg.evaluate("(()=>{if(document.getElementById('stageFirm').classList.contains('on'))"
                              "document.getElementById('back')&&document.getElementById('back').click();})()")
            await pg.wait_for_timeout(200)
            if fw:
                problems.append("firm pages scroll sideways at %dpx: %s" % (w, ", ".join(fw[:6])))

            # the list stops being a table on a phone. Seven columns inside a
            # 358px column used to mean a sideways swipe past a sticky firm
            # name that covered the counts you were swiping to reach. Every
            # count has to sit inside the viewport, with nothing to scroll.
            if w <= 430:
                await pg.evaluate("document.getElementById('vList').click()")
                await pg.wait_for_timeout(350)
                lst = await pg.evaluate(
                    "(()=>{const s=document.querySelector('#listSwipe .scroll');"
                    "const cw=document.documentElement.clientWidth;"
                    "const cells=[...document.querySelectorAll('#tb tr:not(.grp) td[data-l]')];"
                    "const out=cells.filter(c=>c.getBoundingClientRect().right>cw+1).length;"
                    "const lab=cells.filter(c=>c.offsetParent&&!c.textContent.trim()).length;"
                    "return {h:s.scrollWidth-s.clientWidth,out:out,rows:"
                    "document.querySelectorAll('#tb tr:not(.grp)').length,emptyLabelled:lab}})()")
                print("list at %-4d   : hscroll %s, cells past the edge %s, rows %s"
                      % (w, lst["h"], lst["out"], lst["rows"]))
                if lst["h"] > 0:
                    problems.append("the list scrolls sideways at %dpx" % w)
                if lst["out"]:
                    problems.append("%d list cells sit past the right edge at %dpx"
                                    % (lst["out"], w))
                if lst["emptyLabelled"]:
                    problems.append("a list cell prints its label with nothing under it at %dpx" % w)
                await pg.evaluate("document.getElementById('vMatrix').click()")
                await pg.wait_for_timeout(200)

        # Build 69. The wordmark goes home from anywhere: from the Market view
        # with a filter and a search on, and from a firm page. Home is the page
        # as it opens: the List, unfiltered, no search, at the top.
        async def _home_state():
            return await pg.evaluate(
                "(()=>({list:document.getElementById('vList').getAttribute('aria-pressed'),"
                "rows:document.querySelectorAll('#tb tr:not(.grp):not(.chn)').length,"
                "q:document.getElementById('q').value,y:Math.round(window.scrollY),"
                "firm:document.getElementById('stageFirm').classList.contains('on'),"
                "head:!document.querySelector('header.top').hidden}))()")
        await pg.set_viewport_size({"width": 1280, "height": 900})
        await pg.evaluate("document.getElementById('vList').click()")
        await pg.wait_for_timeout(200)
        await pg.fill("#q", "concrete")
        await pg.wait_for_timeout(300)
        await pg.evaluate("window.rolodex.setFilters({group:['trade']})")
        await pg.evaluate("document.getElementById('vMarket').click()")
        await pg.wait_for_timeout(300)
        await pg.evaluate("window.scrollTo(0,1500)")
        await pg.click("#home")
        await pg.wait_for_timeout(350)
        h1 = await _home_state()
        await pg.evaluate("window.rolodex.open('%s')" % PROBE_ID)
        await pg.wait_for_timeout(250)
        await pg.click("#home")
        await pg.wait_for_timeout(450)
        h2 = await _home_state()
        print("wordmark home   : from Market %s, from a firm page %s"
              % ("home" if h1["list"] == "true" and h1["rows"] == D["stats"]["total"] and not h1["q"]
                 and h1["y"] == 0 else h1,
                 "home" if h2["list"] == "true" and not h2["firm"] and h2["rows"] == D["stats"]["total"]
                 else h2))
        for _h in (h1, h2):
            if (_h["list"] != "true" or _h["rows"] != D["stats"]["total"] or _h["q"] or _h["y"] != 0
                    or _h["firm"] or not _h["head"]):
                problems.append("the wordmark does not return to the home screen: %s" % _h)
                break

        # Build 67. The timeline. Every event has its own row beside its date,
        # rows never overlap, today falls between the right two events, and the
        # Market view does not scroll sideways on a phone.
        for w in (1280, 390):
            await pg.set_viewport_size({"width": w, "height": 900})
            await pg.evaluate("document.getElementById('vMarket').click()")
            await pg.wait_for_timeout(350)
            tl = await pg.evaluate(
                "(()=>{const L=[...document.querySelectorAll('ol.tline li:not(.tnow)')];"
                "let ov=0;const all=[...document.querySelectorAll('ol.tline li')];"
                "for(let i=1;i<all.length;i++){if(all[i].getBoundingClientRect().top<"
                "all[i-1].getBoundingClientRect().bottom-0.5)ov++;}"
                "const n=document.querySelectorAll('ol.tline li.tnow').length;"
                "return {rows:L.length,ov:ov,now:n,sw:document.documentElement.scrollWidth,"
                "cw:document.documentElement.clientWidth}})()")
            print("timeline at %-4d: %d rows, %d overlaps, today marks %d, width %d of %d"
                  % (w, tl["rows"], tl["ov"], tl["now"], tl["sw"], tl["cw"]))
            if tl["rows"] != len(D["market"]["timeline"]):
                problems.append("the timeline drops events")
            if tl["ov"]:
                problems.append("timeline rows overlap at %dpx" % w)
            if tl["now"] != 1:
                problems.append("the timeline does not mark today once")
            if tl["sw"] > tl["cw"] + 1:
                problems.append("the Market view scrolls sideways at %dpx" % w)
        await pg.set_viewport_size({"width": 1280, "height": 900})

        # Build 67. Dark theme. It follows the system setting, the toggle flips
        # it and remembers, and the text that matters keeps its contrast: body
        # ink on paper, grey on paper, dark text on the orange, and the ink
        # button's label. Print is the light theme whatever the screen shows.
        def _lum(rgb):
            import re as _re
            v = [int(x) / 255 for x in _re.findall(r"\d+", rgb)[:3]]
            v = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in v]
            return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]

        def _cr(a, b):
            la, lb = sorted((_lum(a), _lum(b)), reverse=True)
            return (la + 0.05) / (lb + 0.05)

        dctx = await b.new_context(viewport={"width": 1280, "height": 900}, color_scheme="dark")
        dp = await dctx.new_page()
        derr = []
        dp.on("pageerror", lambda e: derr.append(str(e)))
        await dp.goto(URL)
        await dp.wait_for_timeout(500)
        th = await dp.evaluate("document.documentElement.getAttribute('data-theme')")
        col = await dp.evaluate(
            "(()=>{const g=(s,p)=>{const e=document.querySelector(s);return e?getComputedStyle(e)[p]:null};"
            "const cs=getComputedStyle(document.documentElement);"
            "return {bg:getComputedStyle(document.body).backgroundColor,ink:getComputedStyle(document.body).color,"
            "grey:g('.mark span','color'),"
            "onOrange:(()=>{const e=document.querySelector('.yn.innovation.clear, .chip.i-clear, .tag.o');"
            "return e?[getComputedStyle(e).color,getComputedStyle(e).backgroundColor]:null})(),"
            "btn:[g('.seg button[aria-pressed=true]','color'),g('.seg button[aria-pressed=true]','backgroundColor')]}})()")
        pairs = [("body text", col["ink"], col["bg"], 7.0), ("grey label", col["grey"], col["bg"], 4.5),
                 ("pressed button", col["btn"][0], col["btn"][1], 4.5)]
        if col["onOrange"]:
            pairs.append(("text on orange", col["onOrange"][0], col["onOrange"][1], 4.5))
        rep = ", ".join("%s %.1f" % (n, _cr(a, c)) for n, a, c, _m in pairs)
        print("dark theme      : %s from the system; %s" % (th, rep))
        if th != "dark":
            problems.append("the page does not follow a dark system setting")
        for n, a, c, m in pairs:
            if _cr(a, c) < m:
                problems.append("dark theme: %s contrast %.2f is under %.1f" % (n, _cr(a, c), m))
        await dp.click("#thm")
        await dp.wait_for_timeout(200)
        flipped = await dp.evaluate(
            "(()=>{let s=null;try{s=localStorage.getItem('rolodex-theme')}catch(e){}"
            "return [document.documentElement.getAttribute('data-theme'),s,"
            "getComputedStyle(document.body).backgroundColor]})()")
        print("theme toggle    :", flipped[0], "stored", flipped[1])
        if flipped[0] != "light" or _lum(flipped[2]) < 0.9:
            problems.append("the theme toggle does not switch to the light theme")
        await dp.click("#thm")
        await dp.wait_for_timeout(200)
        await dp.evaluate("document.getElementById('vMarket').click()")
        await dp.wait_for_timeout(400)
        cells = await dp.evaluate(
            "(()=>{const t=[...document.querySelectorAll('#mapHost text.ctyl')];"
            "return t.map(e=>[e.getAttribute('fill'),e.getAttribute('stroke')])})()")
        badcell = [c for c in cells if c[1] and _cr("rgb(%d,%d,%d)" % tuple(int(c[0][i:i+2], 16) for i in (1, 3, 5)),
                                                     "rgb(%d,%d,%d)" % tuple(int(c[1][i:i+2], 16) for i in (1, 3, 5))) < 4.5]
        print("dark map labels :", len(cells), "labels,", len(badcell), "under 4.5:1")
        if badcell:
            problems.append("dark theme: %d county labels read under 4.5:1 on their fill" % len(badcell))
        await dp.emulate_media(media="print")
        pbg = await dp.evaluate("getComputedStyle(document.body).backgroundColor")
        if _lum(pbg) < 0.9:
            problems.append("print is not the light theme")
        if derr:
            problems.append("dark theme: page errors %s" % derr[:2])
        await dctx.close()

        # Build 71. The pre-publication audit's page findings, held.
        a7 = await b.new_context(viewport={"width": 390, "height": 844})
        ap = await a7.new_page()
        aerr = []
        ap.on("pageerror", lambda e: aerr.append(str(e)))
        await ap.goto(URL)
        await ap.wait_for_timeout(400)
        mkt = await ap.evaluate("document.documentElement.getAttribute('data-market')")
        ckey = "rolodex.call.v1" if mkt == "houston" else "rolodex.call.%s.v1" % mkt
        good = next(t["target_id"] for t in D["targets"] if t["group"] != "out")
        # a saved call list holding an id this deck does not carry still opens
        await ap.evaluate("localStorage.setItem(%r, JSON.stringify(['X-NOPE-1', %r]))" % (ckey, good))
        await ap.reload()
        await ap.wait_for_timeout(900)
        await ap.click("#openCall")
        await ap.wait_for_timeout(300)
        sheet = await ap.evaluate("(document.getElementById('firmBody')||{}).textContent||''")
        n_call = await ap.evaluate("window.rolodex.callList().length")
        print("stale call id   : list holds %d, sheet %s" % (n_call, "opens" if "Call list" in sheet else "BROKEN"))
        if n_call != 1 or "Call list" not in sheet:
            problems.append("a stale id in the saved call list breaks the call sheet")
        if (D.get("place") or {}).get("name", "") not in sheet:
            problems.append("the call sheet does not name its market")
        await ap.evaluate("window.rolodex.setCallList([])")
        await ap.goto(URL)
        await ap.wait_for_timeout(300)
        # the firm page keeps the market in the address
        await ap.evaluate("window.rolodex.open(%r)" % good)
        await ap.wait_for_timeout(300)
        h = await ap.evaluate("location.hash")
        print("firm address    :", h)
        if "market=%s" % mkt not in h:
            problems.append("opening a firm drops the market from the address")
        await ap.go_back()
        await ap.wait_for_timeout(300)
        # a view button pressed from the keyboard keeps the focus
        await ap.focus("#vMatrix")
        await ap.keyboard.press("Enter")
        await ap.wait_for_timeout(300)
        fid = await ap.evaluate("document.activeElement&&document.activeElement.id")
        print("view key focus  :", fid)
        if fid != "vMatrix":
            problems.append("a view button pressed from the keyboard loses the focus to %s" % fid)
        # text on the accent chip that also carries the printing dot
        chip = await ap.evaluate(
            "(()=>{const e=document.querySelector('.chip.printing.i-clear');"
            "return e?[getComputedStyle(e).color,getComputedStyle(e).backgroundColor]:null})()")
        if chip:
            print("printing chip   : %.1f:1" % _cr(chip[0], chip[1]))
            if _cr(chip[0], chip[1]) < 4.5:
                problems.append("the printing-and-clear chip reads %.1f:1" % _cr(chip[0], chip[1]))
        # every jurisdiction year button sits on the screen, and no held-off
        # builder reads "not screened"
        await ap.evaluate("document.getElementById('vMarket').click()")
        await ap.wait_for_timeout(500)
        yb = await ap.evaluate(
            "(()=>{const b=[...document.querySelectorAll('[data-jyr]')];"
            "return b.filter(x=>{const r=x.getBoundingClientRect();return r.right>innerWidth+1}).length})()")
        held = {t["entity_name"] for t in D["targets"] if t["group"] == "out"}
        wrong = [bb["name"] for o in D["market"].get("owners", []) for bb in o["builders"]
                 if bb["name"] in held and not bb.get("off")]
        print("year buttons    : %d past the edge at 390 | held-off builders read as unscreened: %d" % (yb, len(wrong)))
        if yb:
            problems.append("%d jurisdiction year buttons run off a phone screen" % yb)
        if wrong:
            problems.append("the owners chart calls held-off builders unscreened: %s" % ", ".join(wrong))
        # a capital line always carries its text
        blank = [t["target_id"] for t in D["targets"] for c in t.get("capital_signals") or []
                 if not isinstance(c, dict) or not (c.get("text") or "").strip()]
        if blank:
            problems.append("capital lines render blank on %s" % ", ".join(blank[:5]))
        # working fields and the retired competitor block do not ship
        leak = [k for t in D["targets"] for k in t if k.startswith("_")] + (["competitor"] if D.get("competitor") else [])
        if leak:
            problems.append("working fields ship in the data: %s" % ", ".join(sorted(set(leak))[:5]))
        # Build 74. The opener leaves nothing hidden or clipped once it is over,
        # and plays once per visit.
        await ap.goto(URL)
        await ap.wait_for_timeout(3200)
        rest = await ap.evaluate(
            "(()=>{const h=document.getElementById('hl');"
            "return {clip:h.style.clipPath||'',pre:document.querySelectorAll('.pre').length,"
            "beads:document.querySelectorAll('.pbead').length}})()")
        print("opener at rest  :", rest)
        if rest["clip"] or rest["pre"] or rest["beads"]:
            problems.append("the opener leaves the hero clipped or hidden: %s" % rest)
        if aerr:
            problems.append("audit checks: page errors %s" % aerr[:2])
        # the page and the served copy ship the deck and nothing held off it
        shipped = await ap.evaluate(
            "(()=>{const d=window.rolodex.data;return {out:d.targets.filter(t=>t.group==='out').length,"
            "priv:d.targets.filter(t=>'off_reason' in t||'audit_flags' in t||'phone_rule' in t).length,"
            "under:Object.keys(d).filter(k=>k.startsWith('_')).length}})()")
        served = jsonio.read(ROOT / "docs" / ("dfw-data.json" if MARKET == "dfw" else "houston-data.json"))
        s_out = sum(1 for t in served["targets"] if t["group"] == "out")
        print("public data     : page holds %d held-off firms, %d private fields; served copy %d held off"
              % (shipped["out"], shipped["priv"], s_out))
        if shipped["out"] or shipped["priv"] or shipped["under"] or s_out:
            problems.append("the page or its served data carries firms held off the deck or internal fields")
        extra = sorted(p.name for p in (ROOT / "docs").iterdir()
                       if p.name not in ("index.html", "ICON_Greater_Houston_Rolodex.html", "houston-data.json",
                                         "dfw-data.json", "ICON_Greater_Houston_Rolodex.xlsx", "DFW_Rolodex.xlsx",
                                         ".nojekyll", "CNAME"))
        if extra:
            problems.append("docs/ serves files that are not the tool: %s" % ", ".join(extra))
        await a7.close()

        # Build 78. The phone pass, on a touch device at 390.
        mctx = await b.new_context(viewport={"width": 390, "height": 844}, is_mobile=True,
                                   has_touch=True, device_scale_factor=2)
        mp = await mctx.new_page()
        await mp.add_init_script("try{sessionStorage.setItem('rolodex-opened','1')}catch(e){}")
        await mp.goto(URL)
        await mp.wait_for_timeout(900)
        ph = await mp.evaluate(
            "(()=>{const q=document.getElementById('q');"
            "const adds=[...document.querySelectorAll('#stageList .rowadd')].filter(b=>b.offsetParent);"
            "return {q:parseFloat(getComputedStyle(q).fontSize),"
            "add:Math.min(...adds.map(b=>Math.min(b.offsetWidth,b.offsetHeight))),"
            "hfl:getComputedStyle(document.querySelector('#stageList td.hf'),'::before').display}})()")
        # reading down slides the top of the bar away; a move up brings it back
        await mp.evaluate("window.scrollTo(0,1400)")
        await mp.wait_for_timeout(120)
        await mp.evaluate("window.scrollTo(0,1800)")
        await mp.wait_for_timeout(300)
        down = await mp.evaluate("document.documentElement.classList.contains('navup')")
        vtop = await mp.evaluate("document.querySelector('.navtools .seg.views').getBoundingClientRect().top")
        await mp.evaluate("window.scrollTo(0,1700)")
        await mp.wait_for_timeout(300)
        back = not await mp.evaluate("document.documentElement.classList.contains('navup')")
        print("phone bar       : search %.0fpx, + %dpx, slides away %s (views at %.0fpx), returns %s"
              % (ph["q"], ph["add"], down, vtop, back))
        if ph["q"] < 16:
            problems.append("the search box is under 16px on a phone, so iOS zooms the page")
        if ph["add"] < 40:
            problems.append("a List + is under 40px on a phone")
        if ph["hfl"] != "none":
            problems.append("the List card still labels its headline figure on a phone")
        if not down or vtop < -1 or vtop > 12 or not back:
            problems.append("the phone bar does not slide away and back with the view switcher left on screen")
        # every filter menu opens inside the screen
        await mp.evaluate("window.scrollTo(0,0)")
        offm = []
        for i in range(await mp.locator('.fsel > button').count()):
            bt = mp.locator('.fsel > button').nth(i)
            await bt.scroll_into_view_if_needed()
            await bt.tap()
            await mp.wait_for_timeout(200)
            r = await mp.evaluate("(()=>{const m=document.getElementById('fmenu');if(!m)return null;"
                                  "const r=m.getBoundingClientRect();return [Math.round(r.left),Math.round(r.right),"
                                  "document.documentElement.scrollWidth-document.documentElement.clientWidth]})()")
            if r and (r[0] < 0 or r[1] > 390 or r[2] > 0):
                offm.append((i, r))
            await bt.tap()
            await mp.wait_for_timeout(150)
        print("phone menus     :", "all inside" if not offm else offm)
        if offm:
            problems.append("a filter menu opens past the edge of a phone: %r" % offm)
        # every Market figure fits the column, and the tables start closed
        await mp.evaluate("window.scrollTo(0,0);document.getElementById('vMarket').click()")
        await mp.wait_for_timeout(700)
        figs = await mp.evaluate(
            "[...document.querySelectorAll('.figs .fwrap')].map(w=>[w.closest('.figs').querySelector('h3').textContent.slice(0,30),"
            "w.scrollWidth-w.clientWidth])")
        wide = [f for f in figs if f[1] > 1]
        opened = await mp.evaluate("document.querySelectorAll('.figs details.ftable[open]').length")
        srch = await mp.evaluate("getComputedStyle(document.getElementById('q')).display")
        print("phone market    : %d figures, %d wider than the column, %d tables open, search %s"
              % (len(figs), len(wide), opened, srch))
        if wide:
            problems.append("market figures run past a phone column: %s" % wide)
        if opened:
            problems.append("market tables start open on a phone")
        if srch != "none":
            problems.append("the search box shows on the Market view on a phone")
        # a tap on a mark shows its tip, on screen, and a tap elsewhere hides it
        await mp.locator("#figClosings .bar").first.tap()
        await mp.wait_for_timeout(250)
        tp = await mp.evaluate(
            "(()=>{const t=document.getElementById('tip');const r=t.getBoundingClientRect();"
            "return {shown:!t.hidden,in:r.left>=0&&r.right<=innerWidth&&r.top>=0&&r.bottom<=innerHeight}})()")
        await mp.locator("#figClosings h3").tap()
        await mp.wait_for_timeout(200)
        gone = await mp.evaluate("document.getElementById('tip').hidden")
        print("phone chart tip :", tp, "| hides on a tap elsewhere", gone)
        if not tp["shown"] or not tp["in"] or not gone:
            problems.append("a chart tip does not show on a tap, sits off screen, or stays: %r %r" % (tp, gone))
        # the code tables stack
        await mp.evaluate("document.getElementById('vField').click()")
        await mp.wait_for_timeout(500)
        ct = await mp.evaluate(
            "[...document.querySelectorAll('.ctab')].map(t=>t.parentElement.scrollWidth-t.parentElement.clientWidth)")
        print("phone code table:", ct)
        if any(x > 1 for x in ct):
            problems.append("the code tables scroll sideways on a phone")
        # a firm page carries its two actions at the bottom edge
        await mp.evaluate("document.getElementById('vList').click()")
        await mp.wait_for_timeout(300)
        await mp.evaluate("window.rolodex.open(%r)" % PROBE_ID)
        await mp.wait_for_timeout(500)
        fb = await mp.evaluate(
            "(()=>{const f=document.querySelector('#firmBody .firmbar');if(!f)return null;const r=f.getBoundingClientRect();"
            "return {bottom:Math.round(innerHeight-r.bottom),h:Math.round(r.height),"
            "add:!!f.querySelector('[data-add]'),back:!!f.querySelector('[data-back]')}})()")
        n0 = await mp.inner_text("#clN")
        await mp.evaluate("document.querySelector('#firmBody .firmbar [data-add]').click()")
        await mp.wait_for_timeout(200)
        n1 = await mp.inner_text("#clN")
        await mp.evaluate("document.querySelector('#firmBody .firmbar [data-add]').click()")
        await mp.evaluate("document.querySelector('#firmBody .firmbar [data-back]').click()")
        await mp.wait_for_timeout(400)
        left = await mp.evaluate("!document.getElementById('stageFirm').classList.contains('on')")
        print("phone firm bar  :", fb, "| add", n0, "->", n1, "| back leaves the firm", left)
        if not fb or fb["bottom"] != 0 or not fb["add"] or not fb["back"]:
            problems.append("the firm page has no action bar at the bottom of a phone: %r" % fb)
        if n0 == n1:
            problems.append("the firm bar's add does not reach the call list")
        if not left:
            problems.append("the firm bar's back does not leave the firm page")
        await mctx.close()
        # and none of it shows on a desktop
        await pg.evaluate("window.rolodex.open(%r)" % PROBE_ID)
        await pg.wait_for_timeout(300)
        dsk = await pg.evaluate("getComputedStyle(document.querySelector('#firmBody .firmbar')).display")
        await pg.evaluate("document.getElementById('back').click()")
        if dsk != "none":
            problems.append("the phone firm bar shows on a desktop")

        # Build 84. Related firms. Every tie shows on both cards it joins, a node
        # on the deck opens its card, the section is never empty, and on a phone
        # the chart stays inside the screen. Links behind a subscription carry
        # their label.
        PUB = jsonio.read(ROOT / "docs" / ("dfw-data.json" if MARKET == "dfw" else "houston-data.json"))
        TI = PUB.get("ties") or []
        ondeck = {t["target_id"] for t in PUB["targets"]}
        want_rel = {}
        for e in TI:
            for me, other in ((e["a"], e["b"]), (e["b"], e["a"])):
                if me in ondeck:
                    want_rel.setdefault(me, set()).add(other)
        rel_missing, rel_empty = [], []
        ids = sorted(want_rel)
        for tid in ids[::max(1, len(ids) // 45)]:
            await pg.evaluate("window.rolodex.open(%r)" % tid)
            await pg.wait_for_timeout(120)
            got = await pg.evaluate(
                "(()=>{const r=[...document.querySelectorAll('#firmBody .row')].find(x=>x.querySelector('.lab')"
                "&&x.querySelector('.lab').textContent.trim()==='Related firms');if(!r)return null;"
                "return {ids:[...r.querySelectorAll('.onode[data-id]')].map(x=>x.dataset.id),"
                "txt:[...r.querySelectorAll('.onode')].map(x=>x.querySelector('.onm').textContent),"
                "cur:r.querySelectorAll('.onode.cur').length,n:r.querySelectorAll('.onode').length}})()")
            if not got or not got["n"]:
                rel_empty.append(tid)
                continue
            names = {t["target_id"]: t["short"] for t in PUB["targets"]}
            for o in want_rel[tid]:
                if o not in got["ids"] and names.get(o, o) not in got["txt"]:
                    rel_missing.append("%s lacks %s" % (tid, o))
        without = [t["target_id"] for t in PUB["targets"] if t["target_id"] not in want_rel][:1]
        stray = False
        if without:
            await pg.evaluate("window.rolodex.open(%r)" % without[0])
            await pg.wait_for_timeout(120)
            stray = await pg.evaluate("[...document.querySelectorAll('#firmBody .lab')].some(x=>x.textContent.trim()==='Related firms')")
        # a node opens the card it names, and that card points back
        src = next((e["b"] for e in TI if e["k"] == "owns" and e["a"] in ondeck and e["b"] in ondeck), None)
        hop = None
        if src:
            await pg.evaluate("window.rolodex.open(%r)" % src)
            await pg.wait_for_timeout(150)
            to = await pg.evaluate("(()=>{const b=document.querySelector('#firmBody button.onode[data-id]');"
                                   "if(!b)return null;const i=b.dataset.id;b.click();return i})()")
            await pg.wait_for_timeout(250)
            hop = await pg.evaluate("(()=>{const h=document.querySelector('#firmBody .onode.cur');"
                                    "return {cur:h?h.textContent:'',back:!!document.querySelector("
                                    "'#firmBody .onode[data-id=\"%s\"]')}})()" % src)
            hop["to"] = to
        # phone: the widest chart stays inside the screen
        big = max(want_rel, key=lambda k: len(want_rel[k])) if want_rel else None
        rctxp = await b.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, device_scale_factor=2)
        rpp = await rctxp.new_page()
        await rpp.goto(URL)
        await rpp.wait_for_timeout(500)
        ph_over = None
        if big:
            await rpp.evaluate("window.rolodex.open(%r)" % big)
            await rpp.wait_for_timeout(250)
            ph_over = await rpp.evaluate(
                "(()=>{const o=[...document.querySelectorAll('#firmBody .org')];"
                "return {page:document.documentElement.scrollWidth-document.documentElement.clientWidth,"
                "chart:Math.max(0,...o.map(x=>x.scrollWidth-x.clientWidth)),"
                "out:[...document.querySelectorAll('#firmBody .onode')].filter(x=>x.getBoundingClientRect().right>innerWidth+1).length}})()")
        await rctxp.close()
        # subscription labels
        paid = PUB.get("paid") or []
        lab = None
        if paid:
            # a card that cites both kinds, so the order can be read
            holder = next((t["target_id"] for t in PUB["targets"]
                           if any(s.get("url") in paid for s in t.get("sources") or [])
                           and any(s.get("url") not in paid for s in t.get("sources") or [])), None)
            if holder:
                await pg.evaluate("window.rolodex.open(%r)" % holder)
                await pg.wait_for_timeout(150)
                lab = await pg.evaluate(
                    "(()=>{const a=[...document.querySelectorAll('#firmBody .srcs a')].filter(x=>%s.includes(x.getAttribute('href')));"
                    "return a.map(x=>getComputedStyle(x,'::after').content)})()" % json.dumps(paid))
                order = await pg.evaluate(
                    "(()=>{const P=%s;return ['.srcs','.mini.press','.mini.news'].map(c=>[...document.querySelectorAll('#firmBody '+c+' a')]"
                    ".map(x=>P.includes(x.getAttribute('href'))))})()" % json.dumps(paid))
                if any(o != sorted(o) for o in order):
                    problems.append("%s lists a subscription link before a free one" % holder)
        await pg.evaluate("document.getElementById('home').click()")
        await pg.wait_for_timeout(120)
        print("related firms   : %d ties, %d cards checked, missing %d, empty %d, stray %s, hop %s, phone %s, "
              "paid labels %s" % (len(TI), len(ids[::max(1, len(ids) // 45)]), len(rel_missing), len(rel_empty),
                                  stray, hop, ph_over, lab))
        if rel_missing:
            problems.append("a tie shows on one card and not the other: %s" % rel_missing[:4])
        if rel_empty:
            problems.append("a Related firms section is empty: %s" % rel_empty[:4])
        if stray:
            problems.append("a card with no ties renders a Related firms section")
        if src and not (hop and hop["to"] and hop["back"] and hop["cur"]):
            problems.append("a Related firms node does not open its card, or the card does not point back: %s" % hop)
        if ph_over and (ph_over["page"] > 1 or ph_over["chart"] > 1 or ph_over["out"]):
            problems.append("the Related firms chart runs off a phone screen: %s" % ph_over)
        if paid and (not lab or any("Subscription" not in (c or "") for c in lab)):
            problems.append("a link behind a subscription has no label: %s" % lab)

        # The intro reel plays first. It covers the page on a fresh session, a
        # tap ends it without reaching the page under it, it does not play twice
        # in a session or with reduced motion, it lifts by itself at the end
        # with the headline at rest, and its numbers are the records'.
        base = URL.split("?")[0]
        hsh = "#market=dfw" if MARKET == "dfw" else ""
        rctx = await b.new_context(viewport={"width": 1280, "height": 800})
        rp = await rctx.new_page()
        rerr = []
        rp.on("pageerror", lambda e: rerr.append(str(e)))
        await rp.goto(base + hsh)
        await rp.wait_for_timeout(700)
        r1 = await rp.evaluate(
            "(()=>{const r=document.getElementById('reel'),c=r&&r.querySelector('canvas'),"
            "e=document.elementFromPoint(innerWidth/2,innerHeight/2);"
            "return {on:!!r&&getComputedStyle(r).display!=='none',top:!!(e&&e.closest('#reel')),w:c?c.width:0}})()")
        await rp.mouse.click(640, 400)
        await rp.wait_for_timeout(500)
        r2 = await rp.evaluate(
            "(()=>({gone:!document.getElementById('reel'),firm:document.getElementById('stageFirm').classList.contains('on'),"
            "cls:document.documentElement.classList.contains('reel'),scroll:getComputedStyle(document.body).overflow}))()")
        await rp.reload()
        await rp.wait_for_timeout(400)
        r3 = await rp.evaluate("!document.documentElement.classList.contains('reel')&&!document.getElementById('reel')")
        await rp.goto(base + "?intro=1" + hsh)
        await rp.wait_for_timeout(6600)
        r4 = await rp.evaluate(
            "(()=>({gone:!document.getElementById('reel'),beads:document.querySelectorAll('.pbead').length,"
            "clip:document.getElementById('hl').style.clipPath||'',cls:document.documentElement.classList.contains('reel')}))()")
        rd = await rp.evaluate("window.rolodex.data.reel")
        # Every frame shape lays out and draws. Two dots exactly one step apart
        # once kept the stacking loop running forever at 1280 by 800.
        shapes = [(w, h) for w in (320, 390, 430, 768, 1024, 1280, 1440, 1920) for h in (568, 720, 800, 844, 1080)]
        try:
            laid = await asyncio.wait_for(rp.evaluate("""async (shapes) => {
                const c = document.createElement('canvas'); c.style.cssText = 'position:fixed;left:0;top:0';
                document.body.appendChild(c); let n = 0;
                for (const [w, h] of shapes){ c.style.width = w + 'px'; c.style.height = h + 'px';
                  const R = window.RolodexReel(c, window.rolodex.data.reel, {}); await R.ready;
                  for (const t of [0.5, 1.2, 2.2, 3.2, 3.7, 4.1, 4.8]) R.renderAt(t); n++; }
                c.remove(); return n; }""", shapes), 60)
        except Exception as e:
            laid = "hung (%s)" % type(e).__name__
        print("reel shapes     : %s of %d frame shapes lay out and draw" % (laid, len(shapes)))
        if laid != len(shapes):
            problems.append("the reel does not lay out at every frame shape: %s" % laid)
        await rctx.close()
        # A change of market pours the new market's headline again, every time.
        sctx = await b.new_context(viewport={"width": 1280, "height": 800})
        sp = await sctx.new_page()
        await sp.add_init_script("try{sessionStorage.setItem('rolodex-opened','1');sessionStorage.setItem('rolodex-arrive','1')}catch(e){}")
        await sp.goto(URL)
        await sp.wait_for_timeout(450)
        pour = await sp.evaluate("document.querySelectorAll('.pbead').length>0||!!document.getElementById('hl').style.clipPath")
        await sp.wait_for_timeout(3200)
        pour_rest = await sp.evaluate("!document.querySelectorAll('.pbead').length&&!document.getElementById('hl').style.clipPath")
        await sctx.close()
        print("market switch   : headline pours %s, at rest after %s" % (pour, pour_rest))
        if not pour or not pour_rest:
            problems.append("a change of market does not pour the headline and leave it at rest")
        qctx = await b.new_context(viewport={"width": 1280, "height": 800}, reduced_motion="reduce")
        qp = await qctx.new_page()
        await qp.goto(base + hsh)
        await qp.wait_for_timeout(300)
        r5 = await qp.evaluate("!document.documentElement.classList.contains('reel')&&!document.getElementById('reel')")
        await qctx.close()
        deck = [t for t in D["targets"] if t.get("group") != "out"]
        want = {"n": len(deck), "track": sum(t["marks"]["innovation"] == "clear" for t in deck),
                "dec": sum(bool(t.get("has_decider")) for t in deck)}
        got = {k: (rd or {}).get(k) for k in want}
        print("intro reel      : covers %s, tap ends %s, opens a firm %s, replays %s, ends clean %s, "
              "reduced motion %s | %s" % (r1["on"] and r1["top"], r2["gone"], r2["firm"], not r3,
                                          r4["gone"] and not r4["beads"] and not r4["clip"], "off" if r5 else "ON", got))
        if not (r1["on"] and r1["top"] and r1["w"]):
            problems.append("the intro reel does not cover the page on a fresh session: %s" % r1)
        if not r2["gone"] or r2["firm"] or r2["cls"] or r2["scroll"] == "hidden":
            problems.append("a tap on the reel does not end it cleanly: %s" % r2)
        if not r3:
            problems.append("the intro reel plays twice in one session")
        if not r4["gone"] or r4["beads"] or r4["clip"] or r4["cls"]:
            problems.append("the reel does not lift by itself with the headline at rest: %s" % r4)
        if not r5:
            problems.append("the intro reel plays with reduced motion on")
        if got != want:
            problems.append("the reel's numbers differ from the records: %s against %s" % (got, want))
        if rerr:
            problems.append("the intro reel raises page errors: %s" % rerr[:2])

        # Build 86. The served page carries a policy that allows no request and no
        # script but its own, by hash, and nothing the page did in this run
        # tripped it. The hosted artifact sits under the viewer's own policy and
        # carries none.
        pol = await pg.evaluate(
            "(document.querySelector('meta[http-equiv=\"Content-Security-Policy\"]')||{}).content||''")
        scripts = pol.split("script-src", 1)[1].split(";", 1)[0] if "script-src" in pol else ""
        strict = pol.startswith("default-src 'none'") and "'sha256-" in scripts and "unsafe" not in scripts
        blocked = [e for e in errs if "Content Security Policy" in e]
        in_artifact = "Content-Security-Policy" in paths.ARTIFACT.read_text(encoding="utf-8")
        print("page policy     :", "no requests, %d scripts by hash" % scripts.count("'sha256-") if strict
              else "missing", "| blocked in this run", len(blocked), "| in the artifact copy", in_artifact)
        if not strict:
            problems.append("the page carries no policy limiting it to its own scripts")
        if blocked:
            problems.append("the page policy blocked something the page does: %s" % blocked[:2])
        if in_artifact:
            problems.append("the artifact copy carries the page policy")

        # Build 90. A card opens on what the firm is: its type above the name, then
        # The firm, then The screen. No verdict about who would buy a printer. One
        # card of each type is opened.
        deck = [t for t in D["targets"] if t["group"] != "out"]
        TL = dict(D["types"])
        firsts = []
        for key, label in D["types"]:
            t = next((x for x in deck if x["type"] == key), None)
            await pg.goto(URL)
            await pg.wait_for_timeout(250)
            await pg.evaluate("id=>window.rolodex.open(id)", t["target_id"])
            await pg.wait_for_timeout(200)
            top = await pg.evaluate("""(()=>{const h=document.querySelector('#firmBody .fhead');
              const k=h&&h.firstElementChild;
              const labs=[...document.querySelectorAll('#firmBody > .row > .lab')].map(x=>x.textContent);
              return {first:k?k.className:'', text:k?k.textContent:'', labs:labs.slice(0,2),
                      verdict:/printer buyer/i.test(h?h.textContent:'')}})()""")
            firsts.append(label)
            if top["first"] != "ftype" or top["text"] != label or top["verdict"]:
                problems.append("%s does not open on its type: %s" % (t["short"], top))
            if top["labs"] != ["The firm", "The screen"]:
                problems.append("%s: the firm and the screen are not the first two sections: %s"
                                % (t["short"], top["labs"]))
        print("card top        : type above the name, then The firm and The screen, on",
              len(firsts), "types")

        # Build 90. Each List row carries its type, and the Type menu returns what
        # it counts.
        await pg.goto(URL)
        await pg.wait_for_timeout(300)
        await pg.evaluate("document.getElementById('vList').click()")
        await pg.wait_for_timeout(200)
        rowt = await pg.evaluate("""[...document.querySelectorAll('#tb tr .fbtn2')].map(b=>
            [b.dataset.id,(b.closest('td').querySelector('.tp')||{}).textContent||''])""")
        byid = {t["target_id"]: t for t in deck}
        off = [i for i, lab in rowt if i in byid and lab != TL[byid[i]["type"]]]
        if len(rowt) != len(deck) or off:
            problems.append("List rows missing their type marker: %d rows, %d wrong" % (len(rowt), len(off)))
        await pg.click('.fsel[data-kind="type"] > button')
        await pg.wait_for_timeout(150)
        menu = await pg.evaluate("""[...document.querySelectorAll('#fmenu button')].map(b=>
            [b.dataset.f,+(b.querySelector('s')||{}).textContent])""")
        seen = []
        for f, n in menu:
            key = f.split(":", 1)[1]
            want = sum(1 for t in deck if t["type"] == key)
            await pg.evaluate("k=>window.rolodex.setFilters({type:[k]})", key)
            shown = await pg.evaluate("window.rolodex.shown().map(t=>t.type)")
            seen.append("%s %d" % (TL[key], n))
            if n != want or len(shown) != want or set(shown) != {key}:
                problems.append("the Type menu's %s counts %d, returns %d, wants %d" % (key, n, len(shown), want))
        if len(menu) != len(D["types"]):
            problems.append("the Type menu lists %d types, the deck has %d" % (len(menu), len(D["types"])))
        await pg.evaluate("window.rolodex.setFilters({})")
        print("type menu       :", ", ".join(seen))
        if await pg.locator(".rolebar, .rolekey, .rk").count():
            problems.append("the Build 88 role switch, key or chips still render")

        # The List's column labels stay under the navigation while the list scrolls.
        await pg.evaluate("document.getElementById('vList').click()")
        await pg.wait_for_timeout(200)
        await pg.evaluate("document.getElementById('tb').scrollIntoView();window.scrollBy(0,2400)")
        await pg.wait_for_timeout(300)
        stick = await pg.evaluate("""(()=>{const th=document.querySelector('#stageList thead th');
            const nav=document.querySelector('nav');
            return {th:Math.round(th.getBoundingClientRect().top),nav:Math.round(nav.getBoundingClientRect().bottom),
                    y:Math.round(window.scrollY)}})()""")
        print("list header     : at %dpx under a %dpx bar, %dpx down the page" % (stick["th"], stick["nav"], stick["y"]))
        if abs(stick["th"] - stick["nav"]) > 2:
            problems.append("the List's column labels do not stay under the navigation: %s" % stick)

        await b.close()

    if problems:
        raise SystemExit("FAILED: " + "; ".join(problems))
    print("all checks passed")


if __name__ == "__main__":
    asyncio.run(main())
