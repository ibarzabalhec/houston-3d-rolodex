# -*- coding: utf-8 -*-
"""The five-second intro reel, as a standalone file for testing and video.

The page plays the same reel first, from the same code (_reel.js) and the same
numbers (reel.py, read from the public data file). This writes one
self-contained copy with the page's fonts embedded, plus replay and half speed.

    python3 intro/build_intro.py            Houston
    python3 intro/build_intro.py dfw        Dallas-Fort Worth

Writes intro/intro.html (or intro/intro-dfw.html).
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
import jsonio  # noqa: E402
import reel  # noqa: E402

ACCENT = {"houston": "#FF4F00", "dfw": "#0A3A8C"}


def main(mk="houston"):
    src = ROOT / "docs" / ("houston-data.json" if mk == "houston" else "dfw-data.json")
    P = jsonio.read(src)
    D = reel.reel_data(P)
    D["accent"] = ACCENT[mk]
    page = (HERE / "_intro.html").read_text(encoding="utf-8")
    out = (page.replace("/*__FONTS__*/", (ROOT / "_fonts.css").read_text(encoding="utf-8"))
               .replace("/*__REEL__*/", (ROOT / "_reel.js").read_text(encoding="utf-8"))
               .replace("__DATA__", json.dumps(D, ensure_ascii=False).replace("</", "<\\/")))
    name = "intro.html" if mk == "houston" else "intro-%s.html" % mk
    (HERE / name).write_text(out, encoding="utf-8")
    print("categories:", ", ".join("%s %d" % (c["label"], c["n"]) for c in D["cats"]))
    print("wrote intro/%s: %d firms, %d track record, %d with a decision-maker, %s permits %d"
          % (name, D["n"], D["track"], D["dec"], f"{D['permits']:,}", D["permits_year"]))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "houston")
