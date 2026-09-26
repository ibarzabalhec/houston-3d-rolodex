# -*- coding: utf-8 -*-
"""Build 84. Who is tied to whom.

Most ties sat in prose on one card of the pair: a brand names its parent, a
developer names its joint-venture partner, a trade names the builder it pours
for. The other card said nothing. This lists every tie once, and the page draws
it on both cards, as an ownership chart, a chart of a developer's communities
and builders, the masterplans a builder sells in, and the other ties.

Each written tie names the card whose printed text states it and quotes the
phrase. The build stops if the phrase is not on that card, so a tie can only
rest on words a reader can see. A tie's caption uses only words from its
phrase.

Kinds:
  owns      upper owns, controls or holds lower (a parent, a brand, a division)
  develops  upper develops the masterplan lower
  builds    lower builds in upper's masterplan (read from the market view's
            owner rosters and each developer card's builder list, not written here)
  partner   a joint venture, a shared deal, or a named working relationship
  supplies  upper supplies or pours for lower
  people    lower was founded or is run by people from upper

A node is a card id on this market's deck, or a plain name for a firm with no
card here.
"""
import re
from ties_text import card_text, norm

def E(k, a, b, rel, card, cite):
    """One tie: kind, the two ends, the caption, the card that states it and the phrase quoted."""
    return {"k": k, "a": a, "b": b, "rel": rel, "card": card, "cite": cite}

HOU = [
    # Ownership
    E("owns", "Berkshire Hathaway", "Clayton Properties Group", "part of", "HOU-073",
      "Its parent, Clayton Properties Group, is part of Berkshire Hathaway."),
    E("owns", "Clayton Properties Group", "HOU-073", "", "HOU-073",
      "Its parent, Clayton Properties Group, is part of Berkshire Hathaway."),
    E("owns", "HOU-041", "HOU-131", "", "HOU-131", "Its parent, Caldwell Companies, develops Towne Lake"),
    E("owns", "HOU-015", "HOU-007", "", "HOU-015", "Sells lots but owns First America Homes"),
    E("owns", "Onsite ICF", "HOU-123", "division", "HOU-123", "It is a division of Onsite ICF."),
    E("owns", "Sekisui House", "HOU-045", "agreed to buy it in 2022", "HOU-045",
      "Sekisui House agreed to buy it for about $514 million in 2022."),
    E("owns", "Clay Development & Construction", "HOU-136", "build-to-rent division", "HOU-136",
      "Build-to-rent division of Houston industrial developer Clay Development & Construction"),
    E("owns", "HOU-023", "HOU-076", "a David Weekley Homes line", "HOU-076", "A David Weekley Homes line"),
    E("owns", "Dream Finders Homes", "McGuyer Homebuilders (MHI)", "bought in 2021", "HOU-033",
      "Dream Finders Homes bought its parent MHI in 2021"),
    E("owns", "McGuyer Homebuilders (MHI)", "HOU-033", "", "HOU-033",
      "Dream Finders Homes bought its parent MHI in 2021"),
    E("owns", "HOU-147", "HOU-148", "", "HOU-148", "Its parent is Builders FirstSource."),
    E("owns", "Satterfield and Pontikes", "HOU-106", "part of the family", "HOU-106",
      "Part of the Satterfield and Pontikes family"),
    E("owns", "Metromont", "HOU-142", "bought it 15 December 2025", "HOU-142",
      "Metromont bought it on 15 December 2025"),
    E("owns", "US LBM", "HOU-151", "Texas banner", "HOU-151", "It is the Texas banner for US LBM"),
    E("owns", "KPS Capital Partners", "Wells", "agreed to buy, February 2026", "HOU-138",
      "KPS Capital Partners agreed in February 2026 to buy Wells"),
    E("owns", "Wells", "HOU-138", "", "HOU-138", "Its parent, Wells, runs 13 plants"),
    E("owns", "Wells", "HOU-144", "Wells plants", "HOU-144", "Wells plants on one street in Hillsboro"),
    E("owns", "Sterling Infrastructure", "HOU-163", "", "HOU-163",
      "Its parent is publicly traded Sterling Infrastructure."),
    E("owns", "HOU-109", "Taylor Made Concrete", "delivery arm", "HOU-109",
      "its delivery arm is Taylor Made Concrete"),
    E("owns", "HOU-130", "Woodmere Development", "land arm", "HOU-130", "Its land arm, Woodmere Development"),
    E("owns", "Sumitomo Forestry", "HOU-034", "controlling stake, 2014", "HOU-034",
      "Sumitomo Forestry took a controlling stake in 2014"),
    E("owns", "Daiwa House", "HOU-022", "holds 80 percent", "HOU-022", "Daiwa House holds 80 percent"),
    E("owns", "HOU-166", "HOU-042", "wholly owned subsidiary since 2000", "HOU-042",
      "It has been a wholly owned Lennar subsidiary since 2000."),
    E("owns", "HOU-166", "Rausch Coleman Homes", "bought February 2025", "HOU-078",
      "Owned by Rausch Coleman, which Lennar bought in February 2025"),
    E("owns", "Rausch Coleman Homes", "HOU-078", "bought it in 2020", "HOU-078",
      "Rausch Coleman Homes bought it in 2020."),
    E("owns", "HOU-132", "Forestar Group", "owned 62 percent", "HOU-132", "It owned 62 percent of Forestar Group"),
    # Partners, supply and people
    E("partner", "HOU-008", "HOU-012", "co-acquired Trinity Landing", "HOU-008",
      "Trinity Landing, co-acquired with M/I Homes"),
    E("partner", "HOU-006", "HOU-005", "bought M-K-T Heights", "HOU-006",
      "it bought the 218,000 square foot M-K-T Heights with MetroNational and Radom Capital"),
    E("partner", "HOU-006", "MetroNational", "bought M-K-T Heights", "HOU-006",
      "it bought the 218,000 square foot M-K-T Heights with MetroNational and Radom Capital"),
    E("partner", "HOU-005", "MetroNational", "M-K-T Heights", "HOU-006",
      "it bought the 218,000 square foot M-K-T Heights with MetroNational and Radom Capital"),
    E("partner", "HOU-081", "HOU-082", "joint-venture partner on East Blocks", "HOU-082",
      "It is also Pagewood's joint-venture partner on East Blocks"),
    E("partner", "HOU-025", "HOU-026", "built the Cypress community", "HOU-026",
      "built its Cypress community with Taylor Morrison"),
    E("partner", "HOU-168", "HOU-040", "rental homes", "HOU-168", "175 rental homes with Johnson Development"),
    E("partner", "HOU-168", "Tricon", "Tricon communities", "HOU-168", "Three Tricon communities"),
    E("owns", "HOU-147", "Innovative Construction Group", "agreed to buy, August 2026", "HOU-147",
      "In August 2026 it agreed to buy the off-site framing producer PulteGroup bought in 2020."),
    E("partner", "HOU-167", "HOU-147", "agreed to sell framing plant, August 2026", "HOU-167",
      "in August 2026 it agreed to sell its framing plant"),
    E("partner", "HiveASMBLD", "HOU-002", "printed homes at Zuri Gardens", "HOU-002",
      "Already builds printed homes at Zuri Gardens with HiveASMBLD"),
    E("partner", "HiveASMBLD", "HOU-016", "prints with HiveASMBLD", "HOU-016", "Already prints with HiveASMBLD"),
    E("partner", "HiveASMBLD", "HOU-017", "prints with HiveASMBLD", "HOU-017", "Already prints with HiveASMBLD"),
    E("partner", "Interra Capital Group", "HOU-038", "kept it as manager", "HOU-038",
      "Interra Capital Group bought the buildings and kept it as manager"),
    E("supplies", "HOU-163", "HOU-132", "home foundations", "HOU-163",
      "Horton has taken more than 2,000 of its home foundations"),
    E("supplies", "HOU-103", "HOU-114", "concrete", "HOU-114", "Concrete by Texas A&M Concrete."),
    E("supplies", "HOU-105", "HOU-115", "poured its tilt-up panels", "HOU-115",
      "Encore Concrete Construction poured its award-listed tilt-up panels"),
    E("people", "HOU-013", "HOU-070", "founding brothers were division presidents", "HOU-070",
      "Its founding brothers were division presidents at Perry Homes"),
    E("people", "HOU-025", "HOU-062", "people from Taylor Morrison founded it", "HOU-062",
      "People from Taylor Morrison, Toll Brothers and Ryland Homes founded it"),
]

DFW = [
    # Ownership
    E("owns", "DFW-003", "DFW-003a", "Green Brick Partners brand", "DFW-003a", "Green Brick Partners brand"),
    E("owns", "DFW-003", "DFW-003b", "part of Green Brick Partners", "DFW-003b",
      "It is part of Green Brick Partners"),
    E("owns", "DFW-003", "DFW-003c", "", "DFW-003c", "Green Brick owns it"),
    E("owns", "DFW-003", "DFW-003d", "operates under Green Brick", "DFW-003d",
      "It operates as CLH20 LLC under Green Brick"),
    E("owns", "DFW-003", "DFW-014", "", "DFW-014", "The parent is Green Brick"),
    E("owns", "DFW-007", "DFW-063", "affordable brand", "DFW-063", "PulteGroup's affordable brand"),
    E("owns", "DFW-007", "DFW-064", "active-adult brand", "DFW-064", "PulteGroup's active-adult brand"),
    E("owns", "DFW-010", "DFW-024", "luxury brand", "DFW-024", "Luxury brand of Perry Homes."),
    E("owns", "DFW-009", "DFW-038", "Ashton Woods brand", "DFW-038", "Ashton Woods brand"),
    E("owns", "DFW-048", "DFW-031", "bought it in February 2022", "DFW-031",
      "Partners In Building, a Houston custom builder, bought it in February 2022."),
    E("owns", "Qualico", "DFW-045", "part of the family", "DFW-045", "It is part of the Qualico family."),
    E("owns", "Curve Development", "DFW-BTR-009", "Cyrene brand", "DFW-BTR-009",
      "Curve Development developed it under its Cyrene brand"),
    E("owns", "Highland Homes", "DFW-BTR-007", "part of the family", "DFW-BTR-007",
      "It is part of the Highland Homes family."),
    E("owns", "Daiwa House", "DFW-061", "acquired its equity, September 2021", "DFW-061",
      "Daiwa House USA Holdings acquired its equity, September 2021"),
    E("owns", "DFW-061", "The Jones Company of Tennessee", "bought January 2024", "DFW-061",
      "It bought The Jones Company of Tennessee in January 2024."),
    E("owns", "Dream Finders Homes", "DFW-042", "", "DFW-042", "Dream Finders Homes (NASDAQ: DFH) now owns it."),
    E("owns", "Metromont", "DFW-TR-032", "acquired it December 15, 2025", "DFW-TR-032",
      "Metromont acquired it effective December 15, 2025."),
    E("owns", "BakerTriangle", "DFW-TR-092", "prefab division", "DFW-TR-092", "Prefab division of BakerTriangle"),
    E("owns", "Builders FirstSource", "DFW-TR-010", "plant", "DFW-TR-010",
      "Builders FirstSource plant on Enterprise Avenue in Fort Worth"),
    E("owns", "ERW Companies", "DFW-TR-085", "part of ERW Companies", "DFW-TR-085",
      "It is part of ERW Companies"),
    E("owns", "Wells", "DFW-TR-030", "Wells plants", "DFW-TR-030", "Wells, Hillsboro plants"),
    E("owns", "Wells", "GATE Precast", "bought July 2024", "DFW-TR-030", "Wells bought GATE Precast in July 2024."),
    E("owns", "Concrete Pumping Holdings", "DFW-TR-060", "", "DFW-TR-060",
      "the parent, Concrete Pumping Holdings"),
    E("owns", "Sterling Infrastructure", "DFW-TR-001", "subsidiary", "DFW-TR-001",
      "It is a subsidiary of Sterling Infrastructure"),
    E("owns", "UFP Industries", "DFW-TR-011", "part of the site-built components network", "DFW-TR-011",
      "It is part of UFP Industries' site-built components network."),
    # Masterplans
    E("develops", "DFW-CH-001", "DFW-CH-007", "", "DFW-CH-007", "Hillwood develops the lots"),
    E("develops", "DFW-CH-001", "DFW-CH-020", "Hillwood Communities masterplan", "DFW-CH-020",
      "Hillwood Communities masterplan"),
    E("develops", "DFW-CH-001", "DFW-CH-010", "", "DFW-CH-010", "Hillwood sells lots"),
    E("develops", "DFW-CH-018", "DFW-CH-011", "", "DFW-CH-011", "Huffines sells the lots"),
    E("develops", "DFW-CH-018", "DFW-CH-019", "", "DFW-CH-019",
      "It sells lots to several builders in one masterplan, so those builders, not Huffines, make the wall buy."),
    E("develops", "DFW-CH-014", "DFW-CH-012", "Johnson Development masterplan", "DFW-CH-012",
      "Johnson Development masterplan in McKinney"),
    E("develops", "DFW-CH-002", "DFW-CH-008", "develops and markets it", "DFW-CH-008",
      "Republic develops and markets it for LFC Land Company"),
    E("develops", "DFW-CH-002", "DFW-CH-005", "", "DFW-CH-005",
      "Republic Property Group sells the lots"),
    E("develops", "DFW-CH-017", "DFW-CH-016", "", "DFW-CH-016", "Tellus Group develops it."),
    E("develops", "DFW-CH-017", "DFW-CH-013", "bought it in 2018", "DFW-CH-013",
      "Tellus Group bought it from Terra Verde Group in 2018"),
    E("develops", "Cambridge Companies", "DFW-CH-015", "masterplanned community", "DFW-CH-015",
      "Masterplanned community in Celina by Cambridge Companies"),
    E("develops", "Blue Star Land LP", "DFW-CH-009", "", "DFW-CH-009", "Masterplan by Blue Star Land LP"),
    E("owns", "Jerry Jones Family of Companies", "Blue Star Land LP", "part of", "DFW-CH-009",
      "Blue Star Land LP, part of the Jerry Jones Family of Companies"),
    # Partners, supply and people
    E("partner", "DFW-CH-021", "DFW-BTR-010", "build-to-rent joint venture, 2025", "DFW-CH-021",
      "It formed a build-to-rent joint venture with Wan Bridge in 2025."),
    E("partner", "DFW-BTR-004", "DFW-BTR-007", "built the homes at Viridian", "DFW-BTR-004",
      "At Viridian in Arlington, HHS Residential built the homes"),
    E("partner", "DFW-029", "Belclaire", "sister brand", "DFW-029", "with a sister brand, Belclaire"),
    E("partner", "DFW-008", "Gallery Custom Homes", "sister brands", "DFW-008", "sister brands Gallery Custom Homes"),
    E("partner", "DFW-008", "Harwood Homes", "sister brands", "DFW-008",
      "sister brands Gallery Custom Homes and Harwood Homes"),
    E("supplies", "DFW-TR-001", "DFW-001", "Horton homes", "DFW-TR-001", "2,000+ Horton homes"),
    E("supplies", "DFW-TR-085", "DFW-008", "turnkey vendor", "DFW-TR-085",
      "First Texas Homes superintendent Christoph Heimsoth calls it a turnkey vendor."),
    E("people", "DFW-053", "DFW-081", "co-founder sold Darling Homes to Taylor Morrison", "DFW-081",
      "Co-founder Bill Darling sold Darling Homes to Taylor Morrison in 2013"),
]

# Builder lists on developer cards name firms by their trade name, which is not
# always the name on the firm's own card.
ALIAS = {"hou": {"Lennar": "HOU-166", "Highland Homes": "HOU-168", "PulteGroup": "HOU-167"}, "dfw": {}}

STOP = {"a", "an", "the", "of", "in", "on", "at", "to", "it", "its", "and", "for", "with", "by", "from", "as"}


def _words(s):
    return [w for w in re.findall(r"[a-z0-9$][a-z0-9$&'.,-]*", s.lower().replace("’", "'"))]


def _stem(w):
    return w.strip(".,'").replace("'s", "")


def ties(d, mk):
    """The ties for one market's public data, checked. Raises on a bad tie."""
    T = {t["target_id"]: t for t in d["targets"]}
    edges = [dict(e) for e in (HOU if mk == "hou" else DFW)]
    bad = []
    for e in edges:
        for n in (e["a"], e["b"]):
            if re.match(r"^(HOU|DFW)-", n) and n not in T:
                bad.append("%s is not on the deck" % n)
        t = T.get(e["card"])
        if not t:
            bad.append("cite card %s is not on the deck" % e["card"])
            continue
        if norm(e["cite"]) not in card_text(t):
            bad.append("%s does not say: %s" % (e["card"], e["cite"]))
        cw = {_stem(w) for w in _words(e["cite"])}
        for w in _words(e["rel"]):
            if _stem(w) not in STOP and _stem(w) not in cw:
                bad.append("caption word %r is not in the cite on %s" % (w, e["card"]))
        e.pop("cite")
    # builds: the market view's rosters, then each developer card's own list
    seen = {(e["a"], e["b"]) for e in edges}
    for o in (d.get("market") or {}).get("owners") or []:
        for b in o.get("builders") or []:
            n = b.get("id") if b.get("id") in T else b["name"]
            if o["id"] in T and (o["id"], n) not in seen:
                edges.append({"k": "builds", "a": o["id"], "b": n, "rel": "", "card": o["id"]})
                seen.add((o["id"], n))
    byname = {}
    for t in d["targets"]:
        byname.setdefault(t["entity_name"], t["target_id"])
        byname.setdefault(t["short"], t["target_id"])
    byname.update(ALIAS[mk])
    for t in d["targets"]:
        for nm in t.get("channel_builders") or []:
            b = byname.get(nm) or nm
            if b != t["target_id"] and (t["target_id"], b) not in seen:
                edges.append({"k": "builds", "a": t["target_id"], "b": b, "rel": "", "card": t["target_id"]})
                seen.add((t["target_id"], b))
    # One owner above each firm, so the ownership chart is a tree.
    up = {}
    for e in edges:
        if e["k"] in ("owns", "develops"):
            if e["b"] in up and up[e["b"]] != e["a"]:
                bad.append("%s has two owners, %s and %s" % (e["b"], up[e["b"]], e["a"]))
            up[e["b"]] = e["a"]
    if bad:
        raise SystemExit("ties.py:\n  " + "\n  ".join(bad))
    return edges
