# -*- coding: utf-8 -*-
"""The five-second intro reel, built from the public data file.

Every number the reel shows is read from docs/<market>-data.json at build time,
the same records the page renders, so the reel cannot drift from the deck.

    python3 intro/build_intro.py            Houston
    python3 intro/build_intro.py dfw        Dallas-Fort Worth

Writes intro/intro.html (or intro/intro-dfw.html): one self-contained file with
the page's own fonts embedded.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
HERE = pathlib.Path(__file__).resolve().parent

ORDER = ['adopter', 'a', 'b', 'trade', 'creative', 'national', 'channel', 'icon']
# The categories beat: four kinds of firm the research covers, each read from
# the records. A firm sits in one category at most. Contractors are placed by
# their link in the wall chain, as the page places them.
DEVELOPER = {"developer", "btr_developer", "multifamily_developer", "nonprofit_developer", "pe_developer"}
CATS = [
    ("Homebuilders", lambda t: t["entity_type"] == "homebuilder"),
    ("Developers", lambda t: t["group"] != "trade" and t["entity_type"] in DEVELOPER),
    ("General contractors", lambda t: t.get("chain") == "gc"),
    ("Concrete casters", lambda t: t.get("chain") in ("tiltup", "precast")),
]
ACCENT = {"houston": "#FF4F00", "dfw": "#0A3A8C"}


def main(mk="houston"):
    src = ROOT / "docs" / ("houston-data.json" if mk == "houston" else "dfw-data.json")
    P = json.load(open(src, encoding="utf-8"))
    T = P["targets"]
    closings = {c["id"]: c for c in P["market"]["closings"]}

    firms = []
    for g in ORDER:
        for t in T:
            if t["group"] != g:
                continue
            c = closings.get(t["target_id"])
            cat = next((i for i, (_, fn) in enumerate(CATS) if fn(t)), -1)
            firms.append({
                "cat": cat,
                "g": g,
                "tr": t["marks"]["innovation"] == "clear",
                "fit": t["marks"]["machine_fit"],
                "dec": bool(t.get("has_decider")),
                "v": ((c["low"] * c["high"]) ** 0.5) if c else None,
            })
    assert len(firms) == len(T), "a firm sits outside the section order"

    cats = [{"label": lab, "n": sum(f["cat"] == i for f in firms)} for i, (lab, _) in enumerate(CATS)]
    msa = P["permits"]["msa"][-1]
    head = P["headline_html"].replace("<br>", "\n").replace("<b>", "").replace("</b>", "")
    lines = [l.strip() for l in head.split("\n") if l.strip()]
    D = {
        "place": P["place"]["name"],
        "permits": msa["sf"],
        "permits_year": msa["year"],
        "permits_source": "Census Building Permits Survey, via HUD SOCDS",
        "firms": firms,
        "n": len(firms),
        "track": sum(f["tr"] for f in firms),
        "dec": sum(f["dec"] for f in firms),
        "pub": sum(f["v"] is not None for f in firms),
        "band": P["market"]["bands"][0][:2],
        "band2": P["market"]["bands"][1][:2],
        "cats": cats,
        "title": lines,
        "by": P["byline"].split(" · ")[0],
        "accent": ACCENT[mk],
    }
    # The strip on the page prints the same decision-maker count. Stop if they part.
    strip = {s[1]: s[0] for s in P["stat_strip"]}
    assert str(D["n"]) == strip["firms screened"], "roster count differs from the strip"
    dec_label = next(k for k in strip if "decision-maker" in k)
    assert str(D["dec"]) == strip[dec_label], "decision-maker count differs from the strip"

    fonts = (ROOT / "_fonts.css").read_text(encoding="utf-8")
    page = (HERE / "_intro.html").read_text(encoding="utf-8")
    js = json.dumps(D, ensure_ascii=False).replace("</", "<\\/")
    out = page.replace("/*__FONTS__*/", fonts).replace("__DATA__", js)
    name = "intro.html" if mk == "houston" else "intro-%s.html" % mk
    (HERE / name).write_text(out, encoding="utf-8")
    print("categories:", ", ".join("%s %d" % (c["label"], c["n"]) for c in cats))
    print("wrote intro/%s: %d firms, %d track record, %d with a decision-maker, %d publish closings, "
          "%s permits %d" % (name, D["n"], D["track"], D["dec"], D["pub"], f"{D['permits']:,}", D["permits_year"]))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "houston")
