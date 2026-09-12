# -*- coding: utf-8 -*-
"""Check the built deck in a headless browser before shipping.

Fails loudly rather than printing a clean report, so a broken build cannot be
sent by accident.
"""
import asyncio, json, pathlib
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).parent
URL = "file://" + str((ROOT / "ICON_Greater_Houston_Rolodex.html").resolve())
D = json.load(open(ROOT / "houston-data.json", encoding="utf-8"))


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

        chips = await pg.locator("#matrix .chip").count()
        print("console errors  :", errs or "none")
        print("chips in matrix :", chips, "of", D["stats"]["total"])
        if errs:
            problems.append("console errors")
        if chips != D["stats"]["total"]:
            problems.append("chip count does not match the roster")

        orange = await pg.locator("#matrix .chip.i-clear").count()
        want = sum(1 for t in D["targets"] if t["marks"]["innovation"] == "clear")
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
        for v, sel in (("vList", "#tb tr:not(.grp)"), ("vScroll", ".cf-card")):
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
        await pg.evaluate("document.querySelector('.chip[data-id=\"HOU-045\"]').click()")
        await pg.wait_for_timeout(250)
        on = await pg.locator("#stageFirm.on").count()
        idx_hidden = await pg.evaluate("document.getElementById('stageIndex').hidden")
        dec = await pg.locator("#firmBody .p1.dec").count()
        ev = await pg.locator("#firmBody .p1 .ev").count()
        li_icons = await pg.locator("#firmBody .ic.li").count()
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
        # number that counts holds, where a partial still counts.
        strip = await pg.eval_on_selector_all(".stat", "e=>e.map(x=>x.textContent)")
        holds = sum(1 for t in D["targets"] if t["holds"] == 3 and t["group"] != "out")
        want_a = sum(1 for t in D["targets"] if t["group"] == "a")
        lab = [x for x in strip if "all three counts" in x]
        print("stat strip      :", lab)
        if not lab or ("in on all three counts" not in lab[0]):
            problems.append("the three-count stat is not labelled as holding")
        if str(want_a) not in (lab[0] if lab else ""):
            problems.append("the three-count stat does not match the group count")

        # A firm that is both already printing and method-clear kept the black
        # ground and silently lost the accent the legend promises.
        both = [t for t in D["targets"]
                if t["group"] == "adopter" and t["marks"]["innovation"] == "clear"]
        if both:
            bg = await pg.evaluate(
                "getComputedStyle(document.querySelector('.chip.printing.i-clear')).backgroundColor")
            print("printing+clear  :", bg, "on", len(both), "firms")
            if bg != "rgb(255, 79, 0)":
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
        leftover = [t["entity_name"] for t in D["targets"] if t.get("audit_flags")]
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
        hdr = await pg.locator("#tb tr.grp", has_text="Builds the wall, not the house").count()
        rows_trade = await pg.evaluate(
            "(()=>{const r=[...document.querySelectorAll('#tb tr')];"
            "let on=false,n=0;for(const x of r){if(x.classList.contains('grp')){"
            "on=x.textContent.indexOf('Builds the wall')>=0;continue;}if(on)n++;}return n})()")
        print("contractors     :", len(trade), "in data |", rows_trade, "listed")
        if hdr != 1 or rows_trade != len(trade):
            problems.append("the contractor section does not list its firms")
        # the section filter reaches it
        await pg.evaluate("document.getElementById('vMatrix').click()")
        await pg.wait_for_timeout(250)
        await pg.click('.fsel > button >> nth=0')
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
        tabs = await pg.locator(".figs .ftable table").count()
        bars = await pg.locator("#mkBody .figs .fig .bar").count()
        print("market figures  :", figs, "| tables", tabs, "| closing bars", bars)
        if figs != 9 or tabs != 9:
            problems.append("the market view does not draw nine figures with tables (%d, %d)"
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
        for c in P["counties"]:
            y = P["place_years"][pyi]
            want = c["sf"][c["years"].index(y)]
            if by_cty.get(c["name"], 0) != want:
                problems.append("jurisdictions do not sum to %s County in %d" % (c["name"], y))
        if any(r.get("quantity") != "authorized" for r in P["msa"]):
            problems.append("a permit figure is not labelled as an authorisation")
        if len(P["geom"]) != 10:
            problems.append("the county map does not carry ten outlines")
        if not P["sources"] or any(not s0["url"].startswith("http") for s0 in P["sources"]):
            problems.append("a permit source is missing its link")
        # The cross-reads live here, not on the page. A reader is owed the number,
        # not the working that established it.
        import permits as _PM
        for lb, gg, yy, vv, key, _ind in _PM.CROSSREF:
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
        if cty_paths != 10:
            problems.append("the county map does not render ten counties")
        if cells != len(P["counties"]) * len(P["counties"][0]["years"]):
            problems.append("the county matrix does not render every cell")
        if jur != 25:
            problems.append("the jurisdiction chart does not render its top 25")
        if srcs < 5:
            problems.append("permit figures are missing their source links")

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
        # a segment opens the firms it counts, and the list survives an add
        await pg.click('.fig .seg[data-seg="a:partial"]', position={"x": 100, "y": 10})
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

        await b.close()

    if problems:
        raise SystemExit("FAILED: " + "; ".join(problems))
    print("all checks passed")


asyncio.run(main())
