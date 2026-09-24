# -*- coding: utf-8 -*-
"""Build 68. Write the page, carrying every market that has been built.

build.py writes houston-data.json and build_dfw.py writes dfw/dfw-data.json.
This puts both into one page. The page parses only the market being viewed, and
the switch on the home screen moves between them. A market that has not been
built ships as an empty slot, and the switch hides itself.
"""
import json, os, pathlib, shutil

ROOT = pathlib.Path(__file__).parent


def _blob(p):
    if not p.exists():
        return ""
    d = json.load(open(p, encoding="utf-8"))
    return json.dumps(d, ensure_ascii=False).replace("</script>", "<\\/script>")


def main():
    hou = json.load(open(ROOT / "houston-data.json", encoding="utf-8"))
    html = (open(ROOT / "_template.html", encoding="utf-8").read()
            .replace("__DESC__", hou["meta_description"].replace('"', "&quot;"))
            .replace("__DATA_DFW__", _blob(ROOT / "dfw" / "dfw-data.json"))
            .replace("__DATA__", _blob(ROOT / "houston-data.json"))
            .replace("__FONTS__", open(ROOT / "_fonts.css", encoding="utf-8").read())
            .replace("__MARKET__", open(ROOT / "_market.js", encoding="utf-8").read()))
    open(ROOT / "ICON_Greater_Houston_Rolodex.html", "w", encoding="utf-8").write(html)

    # The hosted copy. The claude.ai viewer wraps a page in its own document
    # skeleton, so the artifact body is the page without its document wrapper.
    # The head script that settles the theme and the market before first paint
    # is carried across on its own.
    a = html.split("<style>", 1)[1]
    ti = html.index("<script>\n/* Build 67. The theme is settled")
    head = html[ti:html.index("</script>", ti) + len("</script>")]
    a = "<title>Rolodex</title>\n" + head + "\n<style>" + a
    a = a.replace("</head><body>", "", 1).replace("</body></html>", "", 1)
    open(ROOT / "rolodex-artifact.html", "w", encoding="utf-8").write(a)

    os.makedirs(ROOT / "docs", exist_ok=True)
    shutil.copy(ROOT / "ICON_Greater_Houston_Rolodex.html", ROOT / "docs" / "index.html")
    shutil.copy(ROOT / "ICON_Greater_Houston_Rolodex.html",
                ROOT / "docs" / "ICON_Greater_Houston_Rolodex.html")
    if (ROOT / "dfw" / "dfw-data.json").exists():
        shutil.copy(ROOT / "dfw" / "dfw-data.json", ROOT / "docs" / "dfw-data.json")
    print("html bytes        %d" % len(html))


if __name__ == "__main__":
    main()
