# -*- coding: utf-8 -*-
"""Build 68. Write the page, carrying every market that has been built.

build.py writes build/houston-data.json and build_dfw.py writes build/dfw-data.json.
This puts both into one page. The page parses only the market being viewed, and
the switch on the home screen moves between them. A market that has not been
built ships as an empty slot, and the switch hides itself.
"""
import base64
import collections
import copy
import hashlib
import json
import os
import pathlib
import re
import shutil

import audit11
import paths
import reel
import ties
from version import BUILD

ROOT = pathlib.Path(__file__).parent


# Build 71. The page is an external tool. What it ships is what it shows: the
# firms on the deck and the fields the page renders. Firms held off the deck, the
# reasons they were held off, audit flags, phone-selection rules, verification
# dates and the figures register stay in the build's own data files, which the
# gates read, and never reach the page or the served JSON.
PRIVATE = ("audit_flags", "phone_rule", "phone_shared", "off_reason", "last_verified", "new_layer")
# Build 87. Fields the page never reads. The scores and tier letters are the
# build's own ranking, and an outside reader has no use for a working field.
# The reel and the ties read some of these, so they are dropped after both run.
UNREAD = ("tier", "scores", "capital_mark", "hue_hex", "tail", "categories", "entity_type", "entity_role",
          "channel_builders", "clears", "holds", "deciders", "people_absent")
# Build 90. Market-level fields the page never reads. role_labels is the role
# vocabulary from before Build 88, still written by build.py for its own use.
UNREAD_TOP = ("role_labels", "axis_titles")


def public(d, mk):
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
    # Build 84. Links behind a subscription carry a label on the page. A link on
    # a locked outlet with no label stops the build (audit11.py).
    # Build 84. Who is tied to whom, drawn at the foot of each card (ties.py).
    d["ties"] = ties.ties(d, mk)
    d["paid"], loose = audit11.paid(d)
    if loose:
        raise SystemExit("subscription links unlabelled or listed first: " + ", ".join(loose))
    for t in d["targets"]:
        for k in UNREAD:
            t.pop(k, None)
    for k in UNREAD_TOP:
        d.pop(k, None)
    return d


def _load_public(src, mk):
    """The public copy of one market's data, or None when that market is not built."""
    if not src.exists():
        return None
    with open(src, encoding="utf-8") as f:
        return public(json.load(f), mk)


def _blob(d):
    """The market's data as it is embedded in the page.

    <, > and & are written as JSON unicode escapes, as Django's json_script does,
    so no string in the data can close the script element that carries it or
    open an HTML comment inside it. JSON.parse reads the escapes back unchanged.
    """
    if d is None:
        return ""
    s = json.dumps(d, ensure_ascii=False)
    return s.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")


def _served(d, dst):
    if d is not None:
        with open(dst, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)


# Build 71. One page carries two markets, so what a link preview reads names both.
DESC = ("Builders, developers and wall contractors in Greater Houston and Dallas-Fort Worth, "
        "screened against three counts for a construction printer, with named decision-makers, "
        "sources, a market view and the permitting route. By Héctor Ibarzábal.")


def csp(html):
    """The Content-Security-Policy the served page carries.

    The page makes no network request and runs no script but its own, and this
    has the browser enforce both: nothing may be fetched, and a script runs only
    if its hash is one of the page's own. A string in the data that got past the
    escaping as markup still could not run a handler or load anything. The JSON
    data blocks are not scripts to the browser, so they carry no hash.
    """
    digests = []
    for attrs, body in re.findall(r"<script([^>]*)>(.*?)</script>", html, re.S):
        if "application/json" not in attrs:
            h = base64.b64encode(hashlib.sha256(body.encode("utf-8")).digest()).decode("ascii")
            digests.append("'sha256-%s'" % h)
    return ("default-src 'none'; script-src %s; style-src 'unsafe-inline'; img-src data: blob:; "
            "font-src data:; base-uri 'none'; form-action 'none'" % " ".join(digests))


def render(hou, dfw):
    """The page, carrying each market's public data (None for a market not built)."""
    def part(name):
        return (ROOT / name).read_text(encoding="utf-8")
    html = (part("_template.html")
            .replace("__DESC__", DESC.replace('"', "&quot;"))
            .replace("__BUILD__", str(BUILD))
            .replace("__DATA_DFW__", _blob(dfw))
            .replace("__DATA__", _blob(hou))
            .replace("__FONTS__", part("_fonts.css"))
            .replace("__MARKET__", part("_market.js"))
            .replace("__REEL__", part("_reel.js")))
    return html.replace("__CSP__", csp(html), 1)


def artifact(html):
    """The hosted copy. The claude.ai viewer wraps a page in its own document
    skeleton and sets its own policy, so the artifact body is the page without its
    document wrapper or its policy meta. The head script that settles the theme
    and the market before first paint is carried across on its own."""
    a = html.split("<style>", 1)[1]
    ti = html.index("<script>\n/* Build 67. The theme is settled")
    head = html[ti:html.index("</script>", ti) + len("</script>")]
    a = "<title>Rolodex</title>\n" + head + "\n<style>" + a
    return a.replace("</head><body>", "", 1).replace("</body></html>", "", 1)


# The List's order, which the README's section list follows.
SECTION_ORDER = ("adopter", "icon", "a", "b", "trade", "national", "creative", "channel")


def readme(hou, dfw):
    """README.md, from the public data the page embeds.

    The README said ninety firms for thirty builds while the deck grew to 124, so
    it is written from the page's own counts. It is written here, after both
    markets are built, so the Dallas-Fort Worth count is this build's.
    """
    deck = hou["targets"]
    g = collections.Counter(t["group"] for t in deck)
    return ((ROOT / "_README.md").read_text(encoding="utf-8")
            .replace("__N__", "%d" % len(deck))
            .replace("__NP__", "%d" % sum(len(t["principals"]) for t in deck))
            .replace("__NS__", "%d" % len(hou.get("supply", [])))
            .replace("__NN__", "%d" % len(hou.get("no_site", [])))
            .replace("__DFW_N__", "%d" % (dfw["stats"]["total"] if dfw else 0))
            .replace("__SECTIONS__", "\n".join(
                "- **%s**, %d" % (hou["group_labels"][k], g[k]) for k in SECTION_ORDER if g.get(k))))


def main():
    # Each market's public copy is made once: the page embeds it and docs/ serves it.
    hou = _load_public(paths.HOU_DATA, "hou")
    dfw = _load_public(paths.DFW_DATA, "dfw")
    html = render(hou, dfw)
    page = paths.out(paths.PAGE)
    page.write_text(html, encoding="utf-8")
    paths.ARTIFACT.write_text(artifact(html), encoding="utf-8")

    os.makedirs(ROOT / "docs", exist_ok=True)
    shutil.copy(page, ROOT / "docs" / "index.html")
    shutil.copy(page, ROOT / "docs" / "ICON_Greater_Houston_Rolodex.html")
    _served(dfw, ROOT / "docs" / "dfw-data.json")
    _served(hou, ROOT / "docs" / "houston-data.json")
    (ROOT / "README.md").write_text(readme(hou, dfw), encoding="utf-8")
    print("html bytes        %d" % len(html))


if __name__ == "__main__":
    main()
