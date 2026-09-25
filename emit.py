# -*- coding: utf-8 -*-
"""Build 68. Write the page, carrying every market that has been built.

build.py writes houston-data.json and build_dfw.py writes dfw/dfw-data.json.
This puts both into one page. The page parses only the market being viewed, and
the switch on the home screen moves between them. A market that has not been
built ships as an empty slot, and the switch hides itself.
"""
import copy, json, os, pathlib, shutil

import reel

ROOT = pathlib.Path(__file__).parent


# Build 71. The page is an external tool. What it ships is what it shows: the
# firms on the deck and the fields the page renders. Firms held off the deck, the
# reasons they were held off, audit flags, phone-selection rules, verification
# dates and the figures register stay in the build's own data files, which the
# gates read, and never reach the page or the served JSON.
PRIVATE = ("audit_flags", "phone_rule", "phone_shared", "off_reason", "last_verified", "new_layer")


def public(d):
    d = copy.deepcopy(d)
    d["targets"] = [t for t in d["targets"] if t.get("group") != "out"]
    for t in d["targets"]:
        for k in PRIVATE:
            t.pop(k, None)
    for k in [k for k in d if k.startswith("_")]:
        d.pop(k)
    # The intro reel's numbers, read from the records the page renders. reel.py
    # stops the build if a count differs from the page's strip.
    d["reel"] = reel.reel_data(d)
    return d


def _blob(p):
    if not p.exists():
        return ""
    d = public(json.load(open(p, encoding="utf-8")))
    return json.dumps(d, ensure_ascii=False).replace("</script>", "<\\/script>")


def _served(src, dst):
    if src.exists():
        json.dump(public(json.load(open(src, encoding="utf-8"))), open(dst, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)


# Build 71. One page carries two markets, so what a link preview reads names both.
DESC = ("Builders, developers and wall contractors in Greater Houston and Dallas-Fort Worth, "
        "screened against three counts for a construction printer, with named decision-makers, "
        "sources, a market view and the permitting route. By Héctor Ibarzábal.")


def main():
    hou = json.load(open(ROOT / "houston-data.json", encoding="utf-8"))
    html = (open(ROOT / "_template.html", encoding="utf-8").read()
            .replace("__DESC__", DESC.replace('"', "&quot;"))
            .replace("__DATA_DFW__", _blob(ROOT / "dfw" / "dfw-data.json"))
            .replace("__DATA__", _blob(ROOT / "houston-data.json"))
            .replace("__FONTS__", open(ROOT / "_fonts.css", encoding="utf-8").read())
            .replace("__MARKET__", open(ROOT / "_market.js", encoding="utf-8").read())
            .replace("__REEL__", open(ROOT / "_reel.js", encoding="utf-8").read()))
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
    _served(ROOT / "dfw" / "dfw-data.json", ROOT / "docs" / "dfw-data.json")
    _served(ROOT / "houston-data.json", ROOT / "docs" / "houston-data.json")
    print("html bytes        %d" % len(html))


if __name__ == "__main__":
    main()
