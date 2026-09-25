# -*- coding: utf-8 -*-
"""Contact sheets of the intro at set times, for checking by eye.

    python3 intro/frames.py            desktop 1280x720 and phone 390x844
"""
import pathlib, sys
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "_frames"
OUT.mkdir(exist_ok=True)
TIMES = [0.04, 0.12, 0.3, 0.62, 0.86, 1.08, 1.3, 1.62, 1.85, 2.12, 2.4, 2.53, 2.62, 2.8,
         3.06, 3.3, 3.55, 3.8, 4.05, 4.3, 4.44, 4.6, 4.8, 5.0]
SIZES = {"desk": (1280, 720, 1), "phone": (390, 844, 2)}

with sync_playwright() as p:
    b = p.chromium.launch()
    for key, (w, h, dpr) in SIZES.items():
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=dpr)
        errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto((HERE / "intro.html").as_uri() + "?capture")
        pg.evaluate("window.introReady")
        shots = []
        for t in TIMES:
            pg.evaluate("t => window.renderAt(t)", t)
            f = OUT / ("%s_%05.2f.png" % (key, t))
            pg.screenshot(path=str(f))
            shots.append((t, f))
        print(key, "errors:", errs or "none")
        # contact sheet, six across
        cols = 6 if key == "desk" else 8
        tw = 420 if key == "desk" else 195
        ims = [Image.open(f) for _, f in shots]
        th = int(ims[0].height * tw / ims[0].width)
        rows = (len(ims) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * (tw + 8) + 8, rows * (th + 30) + 8), "#888")
        d = ImageDraw.Draw(sheet)
        for i, ((t, _), im) in enumerate(zip(shots, ims)):
            x, y = 8 + (i % cols) * (tw + 8), 8 + (i // cols) * (th + 30)
            sheet.paste(im.convert("RGB").resize((tw, th)), (x, y + 22))
            d.text((x, y + 4), "t=%.2f" % t, fill="#000")
        sheet.save(OUT / ("sheet_%s.png" % key))
    b.close()
print("sheets in", OUT)
