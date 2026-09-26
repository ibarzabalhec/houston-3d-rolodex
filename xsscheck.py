# -*- coding: utf-8 -*-
"""Render the page from poisoned data and check that no string runs as markup.

The page writes its records into the DOM with innerHTML, and the records are
text read off other people's web pages. Every data string has to be escaped
where it renders. This proves it for every string at once: it appends markup
that would run a script to each text value in both markets' public data (and a
quote that would break out of an attribute to each link), builds the page from
that copy without the page's security policy, walks every view, opens every
firm and the call sheet, and builds the in-page workbook. It fails if a payload
became an element, an event-handler attribute or a call, if the page threw, or
if the workbook it builds is not well-formed XML.

Run after emit.py: `python3 xsscheck.py` (or `make verify`). Needs Playwright.
"""
import asyncio
import io
import pathlib
import sys
import tempfile
import zipfile
from xml.etree import ElementTree

from playwright.async_api import async_playwright

import emit
import paths

ROOT = pathlib.Path(__file__).parent
TEXT = '<img src=x onerror="__x(1)"><svg onload="__x(2)">&amp;'
LINK = '#"><img src=x onerror="__x(3)">\' onmouseover=\'__x(4)'
URL_KEYS = {"url", "source_url", "linkedin_url", "homepage_url", "team_url", "company_li", "phone_source",
            "find_url", "site", "li_search"}
VIEWS = ("vList", "vMatrix", "vScroll", "vField", "vMarket")
HOOK = "window.__x=function(n){(window.__hits=window.__hits||[]).push(n)};"
# Every element with an event-handler attribute, and every element a payload
# would have made, anywhere in the document.
FOUND = ("(()=>{const bad=[];for(const e of document.querySelectorAll('*')){"
         "for(const a of e.attributes){if(/^on/i.test(a.name))bad.push(e.tagName+' '+a.name);}}"
         "document.querySelectorAll('img[src=x]').forEach(()=>bad.push('IMG src=x'));"
         "return {bad:bad.slice(0,8),n:bad.length,hits:window.__hits||[]}})()")


def poison(o, key=None):
    """The data with a payload on every text value and every link.

    Values without a space are left alone: they are ids, keys, dates and figures
    the page matches on, and a changed id tests the page's lookups, not its
    escaping.
    """
    if isinstance(o, dict):
        return {k: poison(v, k) for k, v in o.items()}
    if isinstance(o, list):
        return [poison(v, key) for v in o]
    if isinstance(o, str) and o:
        if key in URL_KEYS or o.startswith("http"):
            return o + LINK
        if " " in o:
            return o + " " + TEXT
    return o


def workbook_ok(data):
    """True when every XML part of the workbook the page built parses."""
    with zipfile.ZipFile(io.BytesIO(bytes(data))) as z:
        for name in z.namelist():
            if name.endswith((".xml", ".rels")):
                ElementTree.fromstring(z.read(name))
    return True


async def walk(b, url, market):
    pg = await b.new_page(viewport={"width": 1280, "height": 900})
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    await pg.add_init_script(HOOK)
    await pg.goto(url + ("#market=dfw" if market == "dfw" else ""))
    await pg.wait_for_timeout(500)
    seen = []
    for v in VIEWS:
        await pg.click("#" + v)
        await pg.wait_for_timeout(200)
        seen.append(await pg.evaluate(FOUND))
    # The filter menus are written when they open.
    await pg.click("#vList")
    for k in range(await pg.locator(".fsel > button").count()):
        await pg.evaluate("k=>document.querySelectorAll('.fsel > button')[k].click()", k)
        seen.append(await pg.evaluate(FOUND))
    await pg.keyboard.press("Escape")
    ids = await pg.evaluate("window.rolodex.shown().map(t=>t.target_id)")
    for i in ids:
        await pg.evaluate("id=>window.rolodex.open(id)", i)
        found = await pg.evaluate(FOUND)
        if found["n"] or found["hits"]:
            seen.append(found)
            break
    await pg.evaluate("ids=>window.rolodex.setCallList(ids)", ids)
    await pg.evaluate("document.querySelector('#openCall').click()")
    # An image's error event fires after it fails to load, so look twice.
    for _ in range(2):
        await pg.wait_for_timeout(300)
        seen.append(await pg.evaluate(FOUND))
    xl = await pg.evaluate("(async()=>{const w=window.rolodex.buildWorkbook(window.rolodex.shown());"
                           "return Array.from(new Uint8Array(await w.arrayBuffer()))})()")
    try:
        xml = workbook_ok(xl)
    except (zipfile.BadZipFile, ElementTree.ParseError) as e:
        xml = str(e)
    await pg.close()
    bad = [s for s in seen if s["n"] or s["hits"]]
    print("%-3s poisoned    : %d firms opened, %d views, call sheet, workbook %s, page errors %d, payloads run %d"
          % (market, len(ids), len(VIEWS), "well-formed" if xml is True else "BROKEN", len(errs),
             sum(s["n"] + len(s["hits"]) for s in bad)))
    problems = []
    if bad:
        problems.append("%s: a data string rendered as markup: %s" % (market, bad[0]))
    if errs:
        problems.append("%s: the page threw on poisoned data: %s" % (market, errs[0][:200]))
    if xml is not True:
        problems.append("%s: the workbook is not well-formed XML: %s" % (market, xml))
    return problems


async def main():
    hou = emit._load_public(paths.HOU_DATA, "hou")
    dfw = emit._load_public(paths.DFW_DATA, "dfw")
    if hou is None:
        sys.exit("xsscheck: build the data first (make build)")
    # The policy would stop a payload from running, which is the point of it, and
    # would hide an escaping bug here. This copy is built without it.
    html = emit.render(poison(hou), poison(dfw) if dfw else None)
    html = html.replace(html[html.index('<meta http-equiv="Content-Security-Policy"'):
                             html.index("\n", html.index('<meta http-equiv="Content-Security-Policy"')) + 1], "")
    problems = []
    with tempfile.TemporaryDirectory() as tmp:
        page = pathlib.Path(tmp) / "poisoned.html"
        page.write_text(html, encoding="utf-8")
        async with async_playwright() as p:
            b = await p.chromium.launch()
            for market in ("hou", "dfw") if dfw else ("hou",):
                problems += await walk(b, "file://%s?intro=0" % page, market)
            await b.close()
    if problems:
        for x in problems:
            print("   " + x)
        sys.exit("FAILED: xsscheck")
    print("xsscheck        : every data string renders as text")


if __name__ == "__main__":
    asyncio.run(main())
