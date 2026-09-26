# -*- coding: utf-8 -*-
"""Frames of the reel as the page plays it, for checking by eye.

    python3 intro/pagecheck.py          sheets in intro/_frames/page_*.png
"""
import asyncio
import pathlib
from playwright.async_api import async_playwright
from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
PAGE = (HERE.parent / "ICON_Greater_Houston_Rolodex.html").resolve().as_uri()
OUT = HERE / "_frames"
OUT.mkdir(exist_ok=True)
TIMES = [0.3, 1.2, 2.2, 3.2, 3.7, 4.1, 4.8, 6.4]
RUNS = [("hou_desk_light", 1280, 720, 1, "light", ""), ("hou_phone_dark", 390, 844, 2, "dark", ""),
        ("dfw_desk_dark", 1280, 720, 1, "dark", "#market=dfw"), ("dfw_phone_light", 390, 844, 2, "light", "#market=dfw")]


async def run(b, key, w, h, dpr, scheme, hsh):
    ctx = await b.new_context(viewport={"width": w, "height": h}, device_scale_factor=dpr, color_scheme=scheme)
    pg = await ctx.new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    await pg.goto(PAGE + hsh)
    t0 = await pg.evaluate("performance.now()")
    shots = []
    for t in TIMES:
        now = await pg.evaluate("performance.now()")
        wait = t * 1000 - (now - t0)
        if wait > 0:
            await pg.wait_for_timeout(wait)
        f = OUT / ("page_%s_%.1f.png" % (key, t))
        await pg.screenshot(path=str(f))
        shots.append((t, f))
    state = await pg.evaluate("""() => ({reel: !!document.getElementById('reel'),
        cls: document.documentElement.className, opened: sessionStorage.getItem('rolodex-opened'),
        beads: document.querySelectorAll('.pbead').length})""")
    print(key, "errors:", errs or "none", "| after:", state)
    await ctx.close()
    cols = 4
    tw = 480 if w > 600 else 200
    ims = [Image.open(f).convert("RGB") for _, f in shots]
    th = int(ims[0].height * tw / ims[0].width)
    sheet = Image.new("RGB", (cols * (tw + 8) + 8, ((len(ims) + cols - 1) // cols) * (th + 28) + 8), "#888")
    d = ImageDraw.Draw(sheet)
    for i, ((t, _), im) in enumerate(zip(shots, ims, strict=True)):
        x, y = 8 + (i % cols) * (tw + 8), 8 + (i // cols) * (th + 28)
        sheet.paste(im.resize((tw, th)), (x, y + 20))
        d.text((x, y + 4), "%s t=%.1f" % (key, t), fill="#000")
    sheet.save(OUT / ("page_%s.png" % key))


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for r in RUNS:
            await run(b, *r)
        await b.close()

asyncio.run(main())
