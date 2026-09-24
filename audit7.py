# -*- coding: utf-8 -*-
"""Build 71. The pre-publication audit, applied to both markets.

Four readers went over the deck before it went to GitHub: the Houston copy, the
Dallas-Fort Worth copy, the page itself at four widths in both themes, and the
numbers against the data. What they found is applied here, after every earlier
pass, so each change is one line that says what it replaces.

The edits live in audit7/*.json as [scope, old, new] triples. A scope is a card
id or a top-level key of the page data. The old text must occur exactly once in
that scope, or the build fails, so an edit cannot land somewhere it was not
aimed. Fields whose names start with an underscore are working fields: they are
stripped before the edits run and never ship.

    PERSON   (card, name) -> fields to set on that contact
    VERDICT  (card, axis) -> (verdict, reason) where the card breaks its rubric
"""
import json, pathlib

HERE = pathlib.Path(__file__).parent
V = {"Yes": "clear", "Partly": "partial", "No": "fail"}


def strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if not str(k).startswith("_"):
                yield from strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings(v)


def _replace(obj, old, new):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if str(k).startswith("_"):
                continue
            if isinstance(v, str) and old in v:
                obj[k] = v.replace(old, new)
            else:
                _replace(v, old, new)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            if isinstance(v, str) and old in v:
                obj[i] = v.replace(old, new)
            else:
                _replace(v, old, new)


def strip_working(obj):
    """Drop keys that start with an underscore, except the figures register."""
    if isinstance(obj, dict):
        for k in [k for k in obj if str(k).startswith("_") and k != "_derived"]:
            del obj[k]
        for v in obj.values():
            strip_working(v)
    elif isinstance(obj, list):
        for v in obj:
            strip_working(v)


def load(market):
    if not (HERE / "audit7").is_dir():
        raise SystemExit("audit7/ is missing. Its edit files are research notes and are kept "
                         "on the build machine, outside the repository.")
    out = []
    for p in sorted((HERE / "audit7").glob(market + "_*.json")):
        for row in json.load(open(p, encoding="utf-8")):
            scope, old, new = row[0], row[1], row[2]
            out.append((p.name, scope, old, new))
    return out


def scope_of(D, scope):
    for t in D["targets"]:
        if t["target_id"] == scope:
            return t, None
    if scope in D:
        return D[scope], scope
    return None, None


def apply(D, market, person=None, verdict=None):
    """Apply every edit for a market. Returns a list of failures."""
    bad = []
    for fn, scope, old, new in load(market):
        tgt, key = scope_of(D, scope)
        if tgt is None:
            bad.append("%s: %s is not in the page data" % (fn, scope)); continue
        n = sum(s.count(old) for s in strings(tgt))
        if n != 1:
            bad.append("%s: %s %r found %d times" % (fn, scope, old[:70], n)); continue
        if isinstance(tgt, str):
            D[key] = tgt.replace(old, new)
        else:
            _replace(tgt, old, new)
    T = {t["target_id"]: t for t in D["targets"]}
    bad += people(T, person or {})
    for (tid, axis), (v, text) in (verdict or {}).items():
        ws = [w for w in T.get(tid, {}).get("why", []) if w["axis"] == axis]
        if len(ws) != 1:
            bad.append("verdict %s %s matched %d" % (tid, axis, len(ws))); continue
        ws[0].update(verdict=v, mark=V[v], text=text)
    return bad


def people(T, person):
    bad = []
    for (tid, name), fields in person.items():
        ps = [p for p in T.get(tid, {}).get("principals", []) if p.get("name") == name]
        if len(ps) != 1:
            bad.append("person %s %s matched %d" % (tid, name, len(ps))); continue
        ps[0].update(fields)
    return bad


def check(market, data_path):
    """Dry run for an edit file: how often each old string occurs in its scope."""
    D = json.load(open(data_path, encoding="utf-8"))
    strip_working(D)
    D.pop("competitor", None)
    rows = load(market)
    ok = 0
    for fn, scope, old, new in rows:
        tgt, _ = scope_of(D, scope)
        n = -1 if tgt is None else sum(s.count(old) for s in strings(tgt))
        if n == 1:
            ok += 1
        else:
            print("%-22s %-14s found %2d  %r" % (fn, scope, n, old[:80]))
    print("%d of %d edits land exactly once" % (ok, len(rows)))


# ---------------------------------------------------------------- both markets
def fix_market(D):
    """The printed-homes table and the timeline, corrected to their sources."""
    m = D["market"]
    for p in m["printed"]:
        if p["project"].startswith("Sunconomy"):
            # 3D Printing Industry, 8 January 2019: a permit for one house in Lago Vista.
            p.update(project="Sunconomy house", place="Lago Vista",
                     status="Permitted January 2019, no completion published")
    tl = m["timeline"]
    for e in tl:
        if e["label"].startswith("Sunconomy"):
            e["month"] = 1
        if e["label"] == "Lennar and ICON announce Wolf Ranch, 100 homes":
            # Lennar's newsroom, 26 October 2021, announced the hundred homes. Its
            # 10 November 2022 release says the community is under way.
            e.update(year=2021, month=10, label="Lennar and ICON announce 100 printed homes in Georgetown")
            tl.append({"year": 2022, "month": 11, "label": "Wolf Ranch printing under way",
                       "kind": "icon", "when": None})
    tl.sort(key=lambda e: (e["year"], e["month"]))


def fix_icon(D, place, local_fact):
    """ICON's record says what ICON's and Lennar's pages publish, and no more.

    The line used to say every ICON project on the public record is in the
    Austin area and none is in the reader's metro. ICON has printed outside the
    Austin area, so the line now names the three housing programmes the facts
    below it cite, and the metro fact describes printing by others there.
    """
    R = D["icon_record"]
    R["line"] = "Three ICON housing programmes, in Georgetown and Austin, and the Titan's published terms."
    for f in R["facts"]:
        if f[0].startswith("Wolf Ranch"):
            # Lennar's 10 November 2022 release: 1,574 to 2,112 square feet.
            f[1] = f[1].replace("1,500 to 2,112 square feet", "1,574 to 2,112 square feet")
            f[1] = f[1].replace("mid $400,000s; later coverage", "mid $400,000s. Later coverage")
    R["facts"] = [f for f in R["facts"] if f[0] != place] + [local_fact]


HOMES = "https://www.homes.com/news/houstons-3d-printed-housing-push-grows-with-two-new-developments/647676272/"
# Competitor sub-headings said what to conclude ("Why it matters", "Where they
# are soft", "The timing problem"). They now say what the line is. Text here is
# the same in both markets.
FACTS = {
    ("HiveASMBLD", "Their claim"): ("A customer's figures",
        "Steve Commander of Commander Home Builders told Homes.com the build timeline fell roughly "
        "50 percent, with 5 to 7 percent cost savings."),
    ("HiveASMBLD", "The timing problem"): ("Schedule",
        "HiveASMBLD had Gulf Shore Estates and Avenue J under construction in spring 2026. Titan "
        "deliveries start early 2027."),
    ("PERI 3D Construction", "Why it matters here"): ("In Houston",
        "A German formwork group printed a house inside the Houston city limits on a COBOD BOD2."),
    ("COBOD International", "Why it matters"): ("Sales model",
        "Titan is a machine sale. COBOD sells machines to contractors, PERI among them."),
    ("PRINT3D Technologies", "Track record"): ("Track record",
        "Seven structures by Community Impact's count, including three houses and a storage "
        "facility, sold between 2024 and 2026."),
    ("Sunconomy", "Why it matters"): ("Outcome",
        "A printed programme announced in Texas with an Apis Cor machine, and no published building."),
    ("Diamond Age", "Why it matters"): ("At closure", "Fifteen houses were open when it stopped."),
}
# Unsourced, or restating what the line and links already carry.
FACTS_DROP = {("HiveASMBLD", "Where they are soft"), ("PRINT3D Technologies", "Why it matters")}


def fix_competitors(D):
    for c in D["competitors"]:
        facts = []
        for f in c.get("facts", []):
            k = (c["name"], f[0])
            if k in FACTS_DROP:
                continue
            if k in FACTS:
                f = list(FACTS[k])
            facts.append(f)
        c["facts"] = facts
        if c["name"] == "HiveASMBLD" and not any(l[1] == HOMES for l in c.get("links", [])):
            c["links"].append(["Homes.com on Commander Home Builders' figures", HOMES])
    for p in D["market"]["printed"]:
        if p["project"] == "PRINT3D Technologies":
            p["status"] = "Seven structures by Community Impact's count, 2024 to 2026"


def tidy(D):
    """Empty notes left by a deleted sentence."""
    for t in D["targets"]:
        if t.get("card_notes"):
            t["card_notes"] = [n for n in t["card_notes"] if n and n.strip()]
    dedupe_people(D["targets"])


def dedupe_people(targets):
    """One person listed twice on a card keeps the entry that carries a link.
    Run before anything counts contacts."""
    for t in targets:
        seen, keep = {}, []
        for p in t.get("principals", []):
            k = p["name"].split(",")[0].strip().lower()
            if k in seen:
                q = seen[k]
                if not q.get("source_url") and p.get("source_url"):
                    keep[keep.index(q)] = p
                    seen[k] = p
                continue
            seen[k] = p
            keep.append(p)
        t["principals"] = keep


# ---------------------------------------------------------------- Houston
HOU_PERSON = {
    ("HOU-161", "Francisco Trevino"): {"role": "Title not published"},
}
HOU_VERDICT = {}
HOU_FIELDS = {
    # The card's own synopsis says Lennar builds the houses in Friendswood's communities.
    ("HOU-042", "channel_builders"): ["Lennar"],
}
HOU_SOURCES = {
    # Imagination Homes carried no source at all. Its own site, and the BUILDER
    # page its principal already cites.
    "HOU-076": ["https://imaginationhomes.com/",
                "https://www.builderonline.com/builder-100/strategy/imagination-homes-targets-attainable-entry-level-housing-in-texas/"],
}
# Closings bars labelled "Builder 100 firm page" for firms whose own cards place
# them below the Builder 100, or give no rank. A BUILDER firm page is what they are.
HOU_CLOSINGS_SOURCE = {
    "HOU-135": "BUILDER firm page, Texas-wide",
    "HOU-063": "BUILDER firm page",
    "HOU-077": "BUILDER firm page, company-wide",
    "HOU-069": "BUILDER firm page",
    "HOU-064": "BUILDER firm page",
}


# Sources whose date field disagrees with the page it points to.
HOU_SOURCE_DATE = {
    # KeyCrew's own byline and metadata: published 10 April 2025.
    ("HOU-001", "https://keycrew.co/journal/wan-bridge-groups-ting-qiao-on-elevating-the-build-to-rent-market/"): "2025-04-10",
}
# A closings bar needs a page the card cites. Kendall's 195 has none.
HOU_CLOSINGS_DROP = {"HOU-063"}


def houston(D):
    bad = []
    T = {t["target_id"]: t for t in D["targets"]}
    for (tid, url), d in HOU_SOURCE_DATE.items():
        hit = [s for s in T[tid]["sources"] if s["url"] == url]
        if len(hit) != 1:
            bad.append("source date: %s %s" % (tid, url)); continue
        hit[0]["date"] = d
    m = D["market"]
    m["closings"] = [c for c in m["closings"] if c["id"] not in HOU_CLOSINGS_DROP]
    m["closings_missing"] = m["closings_base"] - len(m["closings"])
    for (tid, k), v in HOU_FIELDS.items():
        T[tid][k] = v
    for tid, urls in HOU_SOURCES.items():
        have = {s["url"] for s in T[tid].get("sources", [])}
        for u in urls:
            if u not in have:
                T[tid].setdefault("sources", []).append({"url": u})
    for c in D["market"]["closings"]:
        if c["id"] in HOU_CLOSINGS_SOURCE:
            c["source"] = HOU_CLOSINGS_SOURCE[c["id"]]
    fix_competitors(D)
    fix_icon(D, "Houston", ["Printing in Houston",
             "HiveASMBLD has repeat production work inside Greater Houston, and PERI printed a house "
             "inside the city limits."])
    return bad


# ---------------------------------------------------------------- Dallas-Fort Worth
DFW_PERSON = {
    # Each card's own note says the person has left or works elsewhere.
    ("DFW-TR-074", "Joe Mazzenga"): {"decider": False, "departed": True},
    ("DFW-BTR-007", "Matthew McGhee"): {"decider": False, "departed": True},
    ("DFW-053", "Tom Cawthon"): {"decider": False, "departed": True},
    ("DFW-TR-084", "Daneel Nortier"): {"probable": True},
    # Realty News Report, 11 June 2026, as the Partners in Building card cites.
    ("DFW-031", "Chris Lemming"): {
        "role": "President, Partners In Building, since June 2026. Previously Division President, Dallas-Fort Worth",
        "source_url": "https://realtynewsreport.com/houston-home-builder-names-new-leader/",
        "source_evidence": "Named President in Realty News Report, June 11, 2026, after serving as "
                           "Division President for DFW."},
    ("DFW-031", "Jim Lemming"): {
        "role": "Chairman, Partners In Building, since June 2026",
        "source_url": "https://realtynewsreport.com/houston-home-builder-names-new-leader/",
        "source_evidence": "Named in Realty News Report, June 2026, as moving from Chief Executive "
                           "Officer to Chairman."},
    # The leadership page both Green Brick cards cite.
    ("DFW-003a", "Jed Dolson"): {
        "role": "President and Chief Operating Officer, Green Brick Partners",
        "source_evidence": "Named on Green Brick's leadership page as President and Chief Operating "
                           "Officer, previously President of the Texas region over the DFW brands."},
}
DFW_DROP_SOURCE = {
    # The pack held this link cut off mid-slug. It does not resolve as written.
    "DFW-BTR-005": "nexmetro_communitie",
}


def dfw(D):
    T = {t["target_id"]: t for t in D["targets"]}
    for tid, frag in DFW_DROP_SOURCE.items():
        T[tid]["sources"] = [s for s in T[tid]["sources"] if frag not in s["url"]]
    # The capital list renders objects with a text, a date and a link.
    for t in D["targets"]:
        t["capital_signals"] = [c if isinstance(c, dict) else {"text": c, "date": None, "url": None}
                                for c in t.get("capital_signals") or []]
    fix_competitors(D)
    fix_icon(D, "Dallas-Fort Worth", ["Printing in DFW",
             "Black Buffalo printed a house at 100 W. Bolt St., Fort Worth, in May 2024. PRINT3D "
             "Technologies of Allen sells printed houses in North Texas."])


if __name__ == "__main__":
    import sys
    check(sys.argv[1], sys.argv[2])
