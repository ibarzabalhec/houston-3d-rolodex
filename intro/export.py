# -*- coding: utf-8 -*-
"""Render the intro to MP4, frame by frame, from renderAt(t).

    python3 intro/export.py            landscape 1920x1080 and portrait 1080x1920, 60 fps

The last frame is held for one second so the clip does not end on a cut.
"""
import pathlib, shutil, subprocess, tempfile
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
FPS, DUR, HOLD = 60, 5.0, 1.0
SIZES = {"landscape": (1920, 1080, 1), "portrait": (540, 960, 2)}

with sync_playwright() as p:
    b = p.chromium.launch()
    for key, (w, h, dpr) in SIZES.items():
        tmp = pathlib.Path(tempfile.mkdtemp())
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=dpr)
        pg.goto((HERE / "intro.html").as_uri() + "?capture")
        pg.evaluate("window.introReady")
        n = int(DUR * FPS)
        for i in range(n + 1):
            pg.evaluate("t => window.renderAt(t)", i / FPS)
            pg.screenshot(path=str(tmp / ("f%04d.png" % i)))
        last = tmp / ("f%04d.png" % n)
        for j in range(1, int(HOLD * FPS)):
            shutil.copy(last, tmp / ("f%04d.png" % (n + j)))
        out = HERE / ("rolodex-intro-%s.mp4" % key)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(tmp / "f%04d.png"),
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "slow",
                        "-movflags", "+faststart", str(out)], check=True)
        shutil.rmtree(tmp)
        print("wrote", out.name, "%.1f MB" % (out.stat().st_size / 1e6))
    b.close()
