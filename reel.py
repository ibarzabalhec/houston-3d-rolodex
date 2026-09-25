# -*- coding: utf-8 -*-
"""The intro reel's numbers, read from a market's public data.

emit.py adds the result to each market's data as `reel`, and the page draws the
reel from it (_reel.js). intro/build_intro.py uses the same function for the
standalone file. Nothing here is typed: every count is a count of the records
the page renders, and the build stops if one differs from the page's strip.
"""

ORDER = ['adopter', 'a', 'b', 'trade', 'creative', 'national', 'channel', 'icon']
SOURCE = "Census Building Permits Survey, via HUD SOCDS"


def _developer(t):
    """A developer or build-to-rent firm, outside the land owners and the wall trade."""
    e = t["entity_type"]
    return ("develop" in e or e.startswith("btr")) and t["group"] not in ("trade", "channel")


# Four kinds of firm the research covers, one per eighth of a second. A firm
# sits in one at most. Contractors are placed by their link in the wall chain,
# as the page places them. A kind with no firms in a market is left out.
CATS = [
    ("Homebuilders", lambda t: t["entity_type"] == "homebuilder"),
    ("Developers", _developer),
    ("General contractors", lambda t: t.get("chain") == "gc"),
    ("Concrete casters", lambda t: t.get("chain") in ("tiltup", "precast")),
]


def reel_data(P):
    T = [t for t in P["targets"] if t.get("group") != "out"]
    closings = {c["id"]: c for c in P["market"]["closings"]}
    cats = [(lab, fn) for lab, fn in CATS if any(fn(t) for t in T)]
    firms = []
    for g in ORDER:
        for t in T:
            if t["group"] != g:
                continue
            c = closings.get(t["target_id"])
            firms.append({
                "cat": next((i for i, (_, fn) in enumerate(cats) if fn(t)), -1),
                "tr": t["marks"]["innovation"] == "clear",
                "fit": t["marks"]["machine_fit"],
                "dec": bool(t.get("has_decider")),
                "v": round((c["low"] * c["high"]) ** 0.5, 1) if c else None,
            })
    if len(firms) != len(T):
        raise SystemExit("reel: a firm sits outside the section order")
    msa = P["permits"]["msa"][-1]
    head = P["headline_html"].replace("<br>", "\n").replace("<b>", "").replace("</b>", "")
    R = {
        "place": P["place"]["name"],
        "key": P["place"].get("key", "houston"),
        "permits": msa["sf"],
        "permits_year": msa["year"],
        "permits_source": SOURCE,
        "firms": firms,
        "n": len(firms),
        "track": sum(f["tr"] for f in firms),
        "dec": sum(f["dec"] for f in firms),
        "band": P["market"]["bands"][0][:2],
        "band2": P["market"]["bands"][1][:2],
        "cats": [{"label": lab, "n": sum(f["cat"] == i for f in firms)} for i, (lab, _) in enumerate(cats)],
        "title": [l.strip() for l in head.split("\n") if l.strip()],
        "by": P["byline"].split(" · ")[0],
    }
    strip = {s[1]: s[0] for s in P["stat_strip"]}
    if str(R["n"]) != strip.get("firms screened"):
        raise SystemExit("reel: roster count %d differs from the strip" % R["n"])
    lab = next(k for k in strip if "decision-maker" in k)
    if str(R["dec"]) != strip[lab]:
        raise SystemExit("reel: decision-maker count %d differs from the strip" % R["dec"])
    return R
