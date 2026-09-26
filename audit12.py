# -*- coding: utf-8 -*-
"""Build 85. The deck read as ICON's business development team would read it.

Four readers went through both markets as ICON BD: one per market for the
cards, one for the numbers, one for the Field, the code and ICON's own record.
Every finding applied here was checked against the page it rests on first.

What changed, by kind:

  ICON's record   ICON's own site lists Titan's price ($899K for printer and
                  pump), says Titan is for sale now, and gives a pace (a 2,500
                  square foot home in under seven days). The page said none of
                  that was published. ESR-4652 covers walls placed with the
                  Vulcan printer, and the code row read as if it covered Titan.
                  Wolf Ranch is "Finished 2025" on ICON's project page.
  The field       PERI's page gives printing from July 2022 to May 2023, not a
                  pause. SQ4D's first home was January 2020. CyBe's case pages
                  show Hive3D printing five casitas in Round Top, Texas.
                  PRINT3D's seven are structures, three of them houses, and it
                  makes and sells printers, so it leaves the call list and stays
                  in the Field view.
  One rule        A track record of paying for a new building method. Energy
                  ratings, cycle times, buyer software and supply commitments
                  read No. Construction-side technology and off-site framing
                  read Partly. The deck's own precedent is CastleRock, where a
                  parent's industrial method elsewhere reads No.
  Numbers         Kendall's 195 is on no page. Sandcastle's page says an average
                  of 50. Grand Homes says over 400, so it sits above the band.
                  David Weekley's press kit gives 943 Dallas-division closings.
                  PRINT3D counts 3 houses, and its houses are not placed in DFW.
  Both markets    A firm that is on both decks says the same thing on both.
  Copy            Absences are blanks. No steering. American spelling.

Verdicts and sections move where the rubric runs, so every count on the page
is taken after them. Text moves last, after audit11, and each edit applies only
while the text is still the old one, so a stale edit fails the build.
"""
import re

# ------------------------------------------------------------------ sources
TALKBIZ = "https://talkbusiness.net/2020/09/fayetteville-homebuilder-grows-houston-footprint-through-acquisition/"
GREENECO_BUILDER = "https://www.builderonline.com/firms/greeneco-builders/"
TECHCRUNCH_C = "https://techcrunch.com/2025/02/14/icon-a-pioneer-in-3d-home-printing-raises-56m-led-by-norwest-tiger-global/"
TRD = "https://therealdeal.com/texas/2026/03/12/icon-opens-3d-home-printing-tech-to-outside-builders/"
PIB_BUILDER = "https://www.builderonline.com/firms/partners-in-building"
ICON_PRICING = "https://www.iconbuild.com/technology/pricing"
ICON_TITAN = "https://www.iconbuild.com/technology"
ICON_SPECS = "https://www.iconbuild.com/technology/specs"
ICON_WOLF = "https://www.iconbuild.com/projects/wolf-ranch"
ICON_MUELLER = "https://www.iconbuild.com/projects/mueller"
ICON_WIMBERLEY = "https://www.iconbuild.com/projects/wimberley-springs"
ICON_CFV = "https://www.iconbuild.com/projects/community-first-village"
LENNAR_RC = "https://newsroom.lennar.com/2025-02-10-Lennar-Completes-Acquisition-of-Rausch-Coleman-Homes"
CYBE_CASITAS = "https://cybe.eu/cases/las-casitas/"
CYBE_OHIO = "https://cybe.eu/cases/sci-ohio/"
ABC13_SANLEON = "https://abc13.com/post/san-leon-development-aims-sustainability-ground/18943368/"
HOUSTONIA = "https://www.houstoniamag.com/home-and-real-estate/2025/12/3d-printed-houses-neighborhood-houston"
HOU_AMEND = "https://www.houstonpermittingcenter.org/media/9056/download"
ESR = "https://icc-es.org/wp-content/uploads/report-directory/ESR-4652.pdf"

# ------------------------------------------------------------------ verdicts
# Houston, merged into audit8.HOU_SCORE before the rubric runs (3 Yes, 2 Partly,
# 1 No). A section follows from the counts after it.
HOU_SCORE = {
    "HOU-073": {"innovation": 1},   # Brohn: a published build time
    "HOU-009": {"innovation": 1},   # Century: cycle time and a cost cut
    "HOU-131": {"innovation": 1},   # Caldwell Homes: energy ratings
    "HOU-007": {"innovation": 1},   # First America: refined stick framing
    "HOU-062": {"innovation": 1},   # Tricoast: energy checks
    "HOU-045": {"innovation": 1},   # Chesmar: a change of owner
    "HOU-067": {"innovation": 1},   # J. Patrick: energy ratings
    "HOU-008": {"innovation": 1},   # Meritage: cycle time
    "HOU-023": {"innovation": 1},   # David Weekley: a supply commitment
    "HOU-006": {"innovation": 1},   # Triten: a planned building
    "HOU-001": {"innovation": 2},   # Wan Bridge: construction software
    "HOU-128": {"repeatability": 1, "innovation": 2},  # Boxer: a partner, one house
}
# NYSE-listed builders that buy at company level sit with the other national
# builders, as they do on the Dallas-Fort Worth deck.
HOU_NATIONAL = {"HOU-009": "Century Communities", "HOU-008": "Meritage Homes"}

# Dallas-Fort Worth: the verdict word only. The reason is edited below.
DFW_V = {
    ("DFW-003a", "innovation"): "No",
    ("DFW-029", "innovation"): "No",
    ("DFW-023", "innovation"): "No",
    ("DFW-043", "innovation"): "No",
    ("DFW-011", "innovation"): "No",
    ("DFW-060", "innovation"): "No",
    ("DFW-062", "innovation"): "No",
    ("DFW-006", "innovation"): "No",
    ("DFW-041", "innovation"): "No",
    ("DFW-009", "machine_fit"): "No",
    ("DFW-048", "repeatability"): "No",
}
DFW_OFF = {"DFW-AD-001": "Makes and sells its own construction printers. It is in the Field view."}
# (low, high, year, source, what it covers)
DFW_CLOSINGS = {
    "DFW-011": (943, 943, 2025, "The firm's own press kit, Dallas division", "Dallas division"),
}

# ------------------------------------------------------------------ people
# Houston's own rule: at a builder of 400 homes a year or fewer that names no
# construction or purchasing head, the owner. Wan Bridge's two officers are
# marked on the Dallas-Fort Worth card from the same leadership page.
HOU_DECIDERS = {
    "HOU-002": ["Vanessa Cole", "Harry Klein"],
    "HOU-016": ["Steve Commander"],
    "HOU-017": ["Tony M. Brown"],
    "HOU-060": ["Kevin Holland", "John Payson"],
    "HOU-071": ["Greg Hawes"],
    "HOU-001": ["Danting Li", "Keith Clipp"],
}


def houston_people(targets):
    T = {t["target_id"]: t for t in targets}
    for tid, names in HOU_DECIDERS.items():
        t = T.get(tid)
        if not t:
            raise SystemExit("audit12: no card %s" % tid)
        for nm in names:
            p = [p for p in t["principals"] if p.get("name") == nm]
            if len(p) != 1:
                raise SystemExit("audit12: %s has %d principals named %s" % (tid, len(p), nm))
            p[0]["decider"] = True


# ------------------------------------------------------------------ card text
# (card, field, old, new). field: key_stat, mvp_screen, synopsis, region,
# why.<axis>, kp.<i>.<field>, pr.<name>.<field>. The old text must be on the
# card, whole or in part; new replaces it.
CARD = {
    "hou": [
        ("HOU-073", "why.innovation",
         "Publishes a three and a half month average build time. Schedule is already how it competes.",
         "No method on record. Publishes a three and a half month average build time."),
        ("HOU-009", "kp.1.fit_signal", "A $20 per square foot wall claim competes for this budget.", ""),
        ("HOU-045", "why.innovation", "Folded into Sekisui House U.S. in January 2026.",
         "No method on record. Folded into Sekisui House U.S. in January 2026."),
        ("HOU-001", "why.innovation",
         "Six years on its own construction software, plus robotic site inspection.",
         "Six years on its own construction software, plus robotic site inspection. Software, not a "
         "wall method."),
        ("HOU-001", "mvp_screen",
         "Spent six years on its own construction software and site robotics, but no construction or "
         "purchasing lead is published.",
         "Spent six years on its own construction software and site robotics. Keith Clipp runs "
         "development and operations."),
        ("HOU-128", "key_stat", "Paid for a printed house in Fort Worth",
         "Partner on a printed house in Fort Worth, May 2024"),
        ("HOU-128", "why.innovation", "Walls printed in under 30 hours, May 2024.",
         "Partner on the Fort Worth house Black Buffalo 3D printed on its lot, May 2024."),
        ("HOU-128", "kp.0.detail",
         "Tarrant County. 40 by 40 foot house, Black Buffalo 3D NEXCON printer. Built in seven to eight days.",
         "Tarrant County. 40 by 40 foot house, Black Buffalo 3D NEXCON printer. Printed live, May 2024."),
        ("HOU-066", "key_stat", "40 to 60 homes a year on the firm's own count",
         "About 50 homes a year on the firm's own count"),
        ("HOU-060", "key_stat", "150 to 200 homes a year since 1990",
         "150 to 200 homes a year, 3,000-plus since 1990"),
        ("HOU-060", "synopsis", "with one community now selling.", "with one community selling in 2026."),
        ("HOU-060", "why.repeatability",
         "150 to 200 homes a year, every year, in the same southeast Houston corridor.",
         "150 to 200 homes a year, in one southeast Houston corridor."),
        ("HOU-061", "key_stat", "45 closings in 2025, all in Montgomery County, 70 planned for 2026",
         "About 45 closings in 2025, all in Montgomery County, 70 planned for 2026"),
        ("HOU-061", "mvp_screen", "but it has six staff and no purchasing department.",
         "and one purchasing manager buys its materials."),
        ("HOU-063", "synopsis", "It reports over $1 billion in revenue, its own count.",
         "It reports over $1 billion in revenue since 1993, its own count."),
        ("HOU-070", "mvp_screen",
         "Its price point implies volume below the machine band, and it publishes no closings figure.",
         "It sells semi-custom homes in the north and northwest corridor and publishes no closings "
         "figure."),
        ("HOU-070", "why.machine_fit",
         "Price point above $500,000 implies volume below the machine band. No closings figure published.",
         "No closings figure published. Homes from the $500,000s."),
        ("HOU-133", "why.innovation",
         "A hundred printed homes went into one of its communities. Lennar paid for the printing.",
         "Its own blog calls Wolf Ranch a collaboration of ICON, Lennar, BIG and Hillwood."),
        ("HOU-166", "mvp_screen",
         "Its division president controls home design and construction, so a first order would be a "
         "divisional pilot.",
         "Its division president controls home design and construction."),
        ("HOU-166", "why.machine_fit", " First order is a divisional pilot.", ""),
        ("HOU-166", "why.innovation", "LEN X invested in ICON in August 2021.",
         "LEN X invested in ICON in August 2021 and again in February 2025."),
        ("HOU-166", "kp.0.fit_signal", "Paid for by the parent.", "Built by Lennar, the parent."),
        ("HOU-166", "kp.1.fit_signal", "A Houston pilot sits inside an existing relationship.",
         "Lennar is an existing investor in ICON."),
        ("HOU-167", "mvp_screen", "and it sold its framing plant in 2026.",
         "and in August 2026 it agreed to sell its framing plant."),
        ("HOU-167", "kp.1.detail", "Bought 2020 for $104 million, sold 2026.",
         "Bought 2020 for $104 million. Sale agreed August 2026."),
        ("HOU-078", "mvp_screen",
         "It sells at one confirmed community, Tavola, and publishes no Houston volume figure.",
         "Part of Lennar through Rausch Coleman since February 2025. Its last published figure is 185 "
         "closings in 2016."),
        ("HOU-078", "synopsis",
         "Green-building focused production builder that orders windows per home, not per community, so it "
         "can adopt newer products. Rausch Coleman Homes bought it in 2020. Lennar built Wolf Ranch with "
         "ICON, so the relationship exists at corporate level.",
         "Katy builder of entry-level and move-up homes, family-owned until the sale. Rausch Coleman Homes "
         "bought it in 2020. The deal closed in July, per Talk Business & Politics. Lennar completed its "
         "purchase of Rausch Coleman on 10 February 2025."),
        ("HOU-078", "why.repeatability", "One confirmed community, Tavola in New Caney.",
         "Entry-level and move-up detached homes, per BUILDER."),
        ("HOU-078", "why.machine_fit", "No Houston volume figure published.",
         "185 closings in 2016, per BUILDER. No figure since the 2020 sale."),
        ("HOU-078", "why.innovation", "Nothing on record.", "No method on record."),
        ("HOU-078", "region", "Tavola, New Caney", "Katy"),
        ("HOU-072", "key_stat", "More than 300 homes a year in Texas and Tennessee",
         "286 closings in 2025 per BUILDER, Texas and Tennessee"),
        ("HOU-072", "why.machine_fit", "More than 300 homes a year, its own count.",
         "286 closings in 2025 per BUILDER, company-wide."),
        ("HOU-072", "synopsis", "Volume spans those four markets, so the Houston share is unknown.",
         "Its volume spans those four markets."),
        ("HOU-002", "why.innovation", "All 80 committed to printing with HiveASMBLD.",
         "All 80 committed to printing with HiveASMBLD. Reserved an ICON Titan, per The Real Deal, "
         "March 2026."),
        ("HOU-068", "why.machine_fit", "1,016 closings in 2024, Austin included.",
         "1,062 closings in 2025, Austin included."),
        ("HOU-068", "synopsis", "It closed 1,016 homes in 2024, Austin included,",
         "It closed 1,062 homes in 2025, Austin included,"),
        ("HOU-069", "why.machine_fit", "511 closings in 2024, Houston and Austin combined.",
         "483 closings in 2025, Houston and Austin combined."),
        ("HOU-069", "synopsis", "It closed 511 homes in 2024, Houston and Austin combined.",
         "It closed 483 homes in 2025, Houston and Austin combined."),
        ("HOU-022", "kp.1.name", "Houston production programme", "Production program"),
        ("HOU-022", "kp.1.detail", "300-plus communities. Houston is the founding market.",
         "300-plus communities, company-wide. Houston is the founding market."),
        ("HOU-024", "why.machine_fit", "Corporate purchasing function.",
         "1,115 Houston closings in 2025. Purchasing is a corporate function."),
        ("HOU-024", "pr.Lindsay Motley.role", "Regional President", "Regional President, Texas"),
        ("HOU-024", "pr.Lindsay Motley.source_evidence", "Firm announcement names her Austin division president.",
         "Corporate page."),
        ("HOU-006", "why.innovation", "Six-storey mass timber office, contingent on retail leasing.",
         "Six-story mass timber office planned, contingent on retail leasing."),
        ("HOU-113", "key_stat", "61 panels at 70 feet", "61 panels over 70 feet"),
        ("HOU-113", "why.innovation", "70-foot panels are size, not a new method.",
         "Panels over 70 feet are size, not a new method."),
        ("HOU-130", "why.repeatability", " About twenty starts per plan a year.", ""),
        ("HOU-143", "kp.0.detail", "Plant now 180,000 square feet.",
         "Plant 180,000 square feet after the expansion."),
        ("HOU-014", "pr.Kyle Hanna.li_evidence", "Conroe, the head office. ", ""),
    ],
    "dfw": [
        ("DFW-043", "why.innovation", "lets buyers personalise plans", "lets buyers personalize plans"),
        ("DFW-020", "why.innovation",
         "Construction In Focus profile, 2024. Energy Star appliances too. No new wall system.",
         "Some structural elements built off-site, per Construction In Focus, 2024. No new wall system."),
        ("DFW-011", "why.machine_fit", "987 DFW starts, April 2024 to March 2025, on Zonda data. Ranked 10th.",
         "943 Dallas-division closings in 2025, its own press kit."),
        ("DFW-009", "why.machine_fit", "1,289 DFW closings in 2025. Purchasing sits at the parent.",
         "1,289 DFW closings in 2025. Purchasing is a corporate function."),
        ("DFW-009", "mvp_screen", "Purchasing sits at the parent, and one regional president covers its "
         "Texas markets.",
         "Purchasing is a corporate function, and one regional president covers its Texas markets."),
        ("DFW-048", "why.repeatability", "Homes drawn from plan libraries.",
         "Every home is one-of-a-kind, by its own description."),
        ("DFW-048", "mvp_screen",
         "Builds luxury custom homes from plan libraries, so plans repeat, and its volume sits below the "
         "Builder 100.",
         "Every home is one-of-a-kind by its own description, so no plan set repeats, and its volume sits "
         "below the Builder 100."),
        ("DFW-061", "key_stat", "1,465 company-wide closings in 2025, Texas and Tennessee",
         "1,465 company-wide closings in 2025, across four states"),
        ("DFW-TR-032", "mvp_screen", "from one statewide plant,", "from its San Marcos and Corpus Christi plants,"),
        ("DFW-TR-032", "why.machine_fit", "One statewide plant. No DFW figure published.",
         "Two Texas plants. No DFW figure published."),
        ("DFW-TR-032", "region", "San Marcos plant, delivering across Texas including North Texas",
         "San Marcos and Corpus Christi plants, delivering across Texas"),
        ("DFW-TR-026", "synopsis", "with tilt-wall and design-build delivery, rooted in Austin.",
         "with tilt-wall and design-build delivery, founded in 1957."),
        ("DFW-TR-026", "key_stat", "Texas tilt-wall general contractor, no DFW office listed",
         "Texas tilt-wall general contractor, offices in Austin, Houston and San Antonio"),
        ("DFW-CH-001", "mvp_screen",
         "It sells lots, and when a hundred printed homes went into one of its communities, Lennar paid "
         "for the printing.",
         "It sells lots. It developed Wolf Ranch in Georgetown, where ICON printed 100 homes for Lennar."),
        ("DFW-TR-060", "synopsis",
         "Its parent, Concrete Pumping Holdings, appointed Bruce Young Chief Executive Officer in 2008.",
         "Bruce Young has been chief executive since 2008, now of the parent, Concrete Pumping Holdings."),
        ("DFW-TR-027", "key_stat", "More than 12,500 craftworkers, its own count",
         "More than 12,500 co-workers across the U.S., its own count"),
        ("DFW-044", "key_stat", "19 DFW listings now selling and four coming, on its site",
         "19 DFW listings selling and four coming, September 2026"),
        ("DFW-038", "synopsis", "It lists more than 100 available homes there, and no brand closings figure "
         "is published.", "In September 2026 it listed more than 100 available homes there."),
        ("DFW-003c", "synopsis", "Luxury single-family production builder, priced from the mid $700s to over "
         "$1.5 million.",
         "Luxury single-family production builder. Green Brick gives its price range as $790K to $1,880K, "
         "at 31 December 2023."),
        ("DFW-041", "mvp_screen",
         "Its parent, Sekisui House, will transfer its construction technology into its brands from 2026, "
         "but purchasing may sit with that parent.",
         "Sekisui House folded Chesmar into one U.S. company in January 2026, and purchasing may sit with "
         "that parent."),
    ],
}
# Sources a new sentence rests on.
ADD_SOURCE = {
    "hou": {"HOU-078": [TALKBIZ, GREENECO_BUILDER], "HOU-166": [TECHCRUNCH_C], "HOU-072": [PIB_BUILDER],
            "HOU-002": [TRD]},
    "dfw": {"DFW-002": [TECHCRUNCH_C]},
}
# Build-to-rent firms that build their own homes buy walls, as in Houston.
DFW_ROLE = {tid: "vertical_buyer" for tid in ("DFW-BTR-001", "DFW-BTR-005", "DFW-BTR-006", "DFW-BTR-007",
                                              "DFW-BTR-008", "DFW-BTR-009", "DFW-BTR-010")}

# Absence lines: a blank says it. Kept where the line is a fact.
KEEP_NOTE = {
    "HOU-016": ("team_note", "Facebook page. Texas LLC filed in Dickinson."),
}
ABSENT = re.compile(
    r"^(No |Nobody|None |Only a Facebook|Two names, no titles|Owner only|About page names no|"
    r"Site names no|Its own pages name no|Its published pages name no|Plant page names no|"
    r"Dallas branch page names no|Team page names nobody|The whole page reads|Appears in its acquirer|"
    r"Contact page (ends in|lists an address|is a form)|Address, email and form|Chicago street address|"
    r"Five offices, Houston included\. Contact form|newlandco\.com redirects|livelonestar|greenecobuilds|"
    r"Brightland publishes no|One home-page line naming)")
LI_LINKS = re.compile(r"^(?:No (?:\w+ ){0,3}(?:company )?page|No InTown leadership page|Brightland publishes no "
                      r"leadership)\. ((?:Links to|Linked page is) .+)$")
NOTE_TRIM = [(re.compile(r"\s*No current head named\.$"), ""),
             (re.compile(r"\s*No phone from the community or Oxland\.$"), "")]


def _obj(t, path):
    head, _, rest = path.partition(".")
    if head in ("key_stat", "mvp_screen", "synopsis", "region", "team_note", "phone_note"):
        return t, head
    if head == "why":
        return next((w for w in t.get("why") or [] if w.get("axis") == rest), None), "text"
    if head == "kp":
        i, key = rest.split(".", 1)
        kp = t.get("key_projects") or []
        return (kp[int(i)] if int(i) < len(kp) else None), key
    if head == "pr":
        name, _, key = rest.rpartition(".")
        return next((p for p in t.get("principals") or [] if p.get("name") == name), None), key
    return None, None


def cards(D, mk):
    bad = []
    T = {t["target_id"]: t for t in D["targets"]}
    for tid, path, old, new in CARD[mk]:
        t = T.get(tid)
        if not t:
            bad.append("audit12: no card %s" % tid)
            continue
        obj, key = _obj(t, path)
        cur = obj.get(key) if obj is not None else None
        if not isinstance(cur, str) or old not in cur:
            bad.append("audit12: %s %s no longer says %r" % (tid, path, old))
            continue
        obj[key] = cur.replace(old, new, 1)
    for tid, urls in ADD_SOURCE[mk].items():
        t = T.get(tid)
        if not t:
            bad.append("audit12: no card %s for a source" % tid)
            continue
        have = {s.get("url") for s in t.get("sources") or []}
        t.setdefault("sources", [])
        t["sources"] += [{"url": u, "date": None} for u in urls if u not in have]
    if mk == "dfw":
        for tid, role in DFW_ROLE.items():
            if tid in T:
                T[tid]["entity_role"] = role
    # Absences
    for t in D["targets"]:
        for k in ("phone_absent", "web_absent", "people_absent"):
            v = t.get(k)
            if v and not v.startswith("Email only"):
                t[k] = None
        if t.get("no_web_presence"):
            t["no_web_presence"] = False
        for k in ("team_note", "company_li_note"):
            v = t.get(k)
            if not v:
                continue
            m = LI_LINKS.match(v)
            if m:
                t[k] = m.group(1)
            elif ABSENT.match(v):
                t[k] = None
        if t["target_id"] in KEEP_NOTE:
            k, v = KEEP_NOTE[t["target_id"]]
            t[k] = v
        for k in ("team_note", "phone_absent"):
            for rx, to in NOTE_TRIM:
                if t.get(k):
                    t[k] = rx.sub(to, t[k])
        v = t.get("phone_note")
        if v:
            v = re.sub(r"\s*(No number|None for the company)\.$", "", v).strip()
            t["phone_note"] = v or None
    return bad


# ------------------------------------------------------------------ closings
def closings(D, mk):
    bad = []
    rows = {r["id"]: r for r in (D.get("market") or {}).get("closings") or []}
    T = {t["target_id"]: t for t in D["targets"]}
    if mk == "hou":
        fix = {
            "HOU-066": dict(low=50, high=50, source="The firm's own site, an average of 50 a year"),
            "HOU-072": dict(low=286, high=286, year=2025, source="BUILDER firm page"),
            "HOU-061": dict(source="Conroe News, citing the chief executive, with 70 planned for 2026"),
        }
        for tid, f in fix.items():
            if tid not in rows:
                bad.append("audit12: no closings row %s" % tid)
                continue
            rows[tid].update(f)
            if "high" in f and tid in T:
                T[tid]["vol"] = f["high"]
        # No page the card cites carries 195.
        if "HOU-063" in T:
            T["HOU-063"]["vol"] = None
    else:
        if "DFW-023" in rows:
            # "over 400": above the band, and drawn as a floor.
            rows["DFW-023"]["over"] = True
        else:
            bad.append("audit12: no closings row DFW-023")
        if "DFW-061" in rows:
            rows["DFW-061"]["wide"] = "company-wide, four states"
    D["market"]["closings"] = sorted(rows.values(), key=lambda r: -r["high"])
    return bad


# ------------------------------------------------------------------ ICON
ICON_FACTS = {
    "Titan, on the record": (
        "Announced 11 March 2026. ICON: multi-story walls at roughly $20 a square foot, a $5,000 deposit, "
        "training from the third quarter of 2026, deliveries from early 2027. ICON's pricing page, "
        "September 2026: $899,000 for printer and pump, print material $620 a cubic yard, designs $2,000 "
        "to $5,000. Its Titan page: available to purchase, deliveries beginning in 2027. Jason Ballard to "
        "Builder: the target is small and mid-sized builders."),
    "Wolf Ranch, Georgetown": (
        "100 homes with Lennar, co-designed by BIG. Printer: Vulcan. Announced 26 October 2021, printing "
        "by November 2022. Eight plans, 1,574 to 2,112 square feet, expected from the mid $400,000s. "
        "Finished 2025, per ICON's project page. ICON, 2 June 2026: its first completed residential "
        "community."),
    "Austin and the Hill Country": (
        "Community First! Village: 100 more homes under way from December 2024, with a Lennar Foundation "
        "gift. ICON's project page: 117 structures there, 2019 to 2026. Mueller: three one-bedroom homes "
        "from $195,000 and nearly a dozen two- and three-bedrooms, printing from July 2025. ICON's page: "
        "12 finished, 2026. Wimberley Springs: eight homes from the upper $800,000s, July 2024. ICON's "
        "page: five finished, 2025."),
    "Lennar in Houston": (
        "Lennar's Houston division. Friendswood Development, its Houston land company since 2000. GreenEco "
        "Builders, which came with Rausch Coleman in February 2025."),
    "Houston": (
        "Mars Dune Alpha: 1,700 square foot NASA habitat at Johnson Space Center, 2021. Second crew mission "
        "inside: 19 October 2025 to 31 October 2026. ICON's site places its 117 sold homes in Central and "
        "West Texas. HiveASMBLD prints at Zuri Gardens, Gulf Shore Estates and Avenue J. PERI printed a "
        "house inside city limits."),
    "Dallas-Fort Worth": (
        "ICON's site places its 117 sold homes in Central and West Texas. The Army Corps of Engineers' Fort "
        "Worth District ran the Fort Bliss agreement, per ICON. Black Buffalo printed a Fort Worth house in "
        "May 2024. PRINT3D Technologies of Allen builds printed houses and sells its own printers."),
    "The company": (
        "Homes and structures completed: more than 245, per ICON, 11 March 2026. ICON's site, September "
        "2026: 263 structures built since 2017, 117 homes sold since 2020. TechCrunch: 114 layoffs filed "
        "January 2025, over a quarter of staff. $56 million Series C, February 2025, co-led by Norwest and "
        "Tiger Global, with LEN X among the existing backers."),
}
ICON_LINE = ("Central and West Texas housing. Army barracks in Texas, with Louisiana under way. NASA habitat "
             "in Houston. Titan: its first system for outside builders.")
ICON_LINKS = [
    ["ICON's Titan pricing, September 2026", ICON_PRICING],
    ["ICON's Titan page, September 2026", ICON_TITAN],
    ["ICON's Titan specifications", ICON_SPECS],
    ["ICON's Wolf Ranch project page", ICON_WOLF],
    ["ICON's Mueller project page", ICON_MUELLER],
    ["ICON's Wimberley Springs project page", ICON_WIMBERLEY],
    ["ICON's Community First! Village project page", ICON_CFV],
    ["Lennar completes Rausch Coleman, 10 February 2025", LENNAR_RC],
]


def icon(D, mk):
    bad = []
    ir = D.get("icon_record") or {}
    if not ir:
        return ["audit12: no ICON record"]
    ir["line"] = ICON_LINE
    have = {f[0] for f in ir["facts"]}
    for f in ir["facts"]:
        if f[0] in ICON_FACTS:
            f[1] = ICON_FACTS[f[0]]
    need = {"Titan, on the record", "Wolf Ranch, Georgetown", "Austin and the Hill Country", "The company",
            "Houston" if mk == "hou" else "Dallas-Fort Worth"}
    if need - have:
        bad.append("audit12: the ICON record lacks %s" % sorted(need - have))
    urls = {l[1] for l in ir["links"]}
    for l in ir["links"]:
        if l[1] == TRD:
            l[0] = "The Real Deal on the first reservations, March 2026"
    ir["links"] += [l for l in ICON_LINKS if l[1] not in urls]
    return bad


# ------------------------------------------------------------------ the field
FIELD = {
    "HiveASMBLD": {
        "facts": {
            "In market": "Zuri Gardens: 80 homes, $1.8 million city subsidy. Gulf Shore Estates: 23 of 26. "
                         "Avenue J: duplex. Marfa: Lumen Villas, nine homes, started 2025. None confirmed "
                         "complete.",
            "Schedule": "Spring 2026: Gulf Shore Estates and Avenue J under way. Cole Klein, its Zuri Gardens "
                        "customer, reserved an ICON Titan, per The Real Deal.",
        },
        "links": [["The Real Deal on the first Titan reservations, March 2026", TRD]],
    },
    "PERI 3D Construction": {
        "where": "Germany, printed in Houston",
        "facts": {
            "The project": "Marketed as the nation's largest printed home. PERI's page gives 30,000 square "
                           "feet, ABC13 4,000. Printing ran July 2022 to May 2023, per PERI.",
            "In Houston": "A German formwork group printed a house inside Houston.",
        },
    },
    "COBOD International": {"facts": {"Sales model": "Sells machines to contractors, PERI among them."}},
    "PRINT3D Technologies": {
        "line": "Builds printed houses and sells its own printers. Model starting prices run $120,000 to "
                "$550,000, on its own list.",
        "facts": {"Track record": "Seven structures built by May 2026, three of them houses and one a 16-unit "
                                  "storage facility, per Community Impact. The first house, 2024, cost "
                                  "$103,000."},
    },
    "Apis Cor": {
        "line": {"hou": "D.R. Horton invested strategically in March 2024.",
                 "dfw": "D.R. Horton, first on BUILDER's DFW Local Leaders table, invested strategically in "
                        "March 2024."},
        "facts": {"Texas": "Texas project: Sunconomy's Lago Vista house, permitted 2019, no completion "
                           "published."},
    },
    "Sunconomy": {"drop": ["Its own site"]},
    "Alquist 3D": {
        "facts": {
            "What changed": "Moved from pilots to selling machines: 12 A1X and 2 A1 systems sold, April 2026. "
                            "FMGI owns and leases the A1X. Prints commercial buildings for Walmart.",
            "Texas": "No Texas project. Walmart work in Missouri, Tennessee and Alabama, per Construction "
                     "Dive.",
        },
    },
    "SQ4D": {
        "line": "Four projects on its own list, the first finished January 2020. No Texas project.",
        "facts": {"Track record": "First permitted home, 1,900 square feet, finished January 2020 in "
                                  "Calverton, New York."},
    },
    "CyBe Construction": {
        "line": "Case pages show houses in Florida, Texas and Ohio.",
        "facts": {"Track record": "Florida: a house, on its case page. Round Top, Texas: five rental casitas "
                                  "printed by Hive3D Builders on a CyBe RC, from mid 2023. Ohio: a 1,300 "
                                  "square foot home by its partner SCI, October 2024."},
        "links": [["Their case page for Las Casitas, Round Top, Texas", CYBE_CASITAS],
                  ["Their case page for the SCI home, Ohio", CYBE_OHIO]],
    },
    "Von Perry": {
        "line": "Dallas startup. Began building a printed house near Nevada, Collin County, December 2021.",
    },
}


def field(D, mk):
    bad = []
    C = {c["name"]: c for c in D.get("competitors") or []}
    for name, f in FIELD.items():
        c = C.get(name)
        if not c:
            if name in ("Von Perry",) and mk == "hou":
                continue
            bad.append("audit12: no Field entry %s" % name)
            continue
        if "where" in f:
            c["where"] = f["where"]
        if "line" in f:
            c["line"] = f["line"][mk] if isinstance(f["line"], dict) else f["line"]
        for title, text in (f.get("facts") or {}).items():
            x = [x for x in c.get("facts") or [] if x[0] == title]
            if len(x) != 1:
                bad.append("audit12: %s has no fact %r" % (name, title))
                continue
            x[0][1] = text
        for title in f.get("drop") or []:
            c["facts"] = [x for x in c.get("facts") or [] if x[0] != title]
        have = {l[1] for l in c.get("links") or []}
        c["links"] = (c.get("links") or []) + [l for l in f.get("links") or [] if l[1] not in have]
    if mk == "dfw" and D.get("consolidation"):
        D["consolidation"] = D["consolidation"].replace("eighteen months after its Fort Worth print",
                                                        "nineteen months after its Fort Worth print")
    return bad


# ------------------------------------------------------------------ code
CODE_Q = {
    "Does zoning apply?": "Zoning",
    "What code, inside the city?": "Code inside the city",
    "What code, inside Dallas?": "Code inside Dallas",
    "What code, inside Fort Worth?": "Code inside Fort Worth",
    "Does ICON hold that report?": "ICON's ICC-ES report",
    "What code, in the county?": "Code in unincorporated counties",
    "Can a city or county refuse it?": "State limit on local refusal",
}
CODE_A = {
    "ICON's ICC-ES report": (
        "ESR-4652, reissued June 2026. It covers walls placed with ICON's Vulcan printer, Model 2.5 series: "
        "bearing, non-bearing and shear walls to 12 feet, Seismic Design Categories A and B, with special "
        "inspection. The report does not name Titan."),
    "State limit on local refusal": (
        "Government Code Chapter 3000, effective 1 September 2019: a city or county may not bar a material "
        "a national model code approves within the last three code cycles. Exceptions include historic "
        "designations, state or federal housing programs, and what a building needs for windstorm and hail "
        "insurance."),
}
CODE_A_HOU = {
    "Zoning": ("Houston has no zoning. Chapter 42: subdivision, platting and building lines. Chapter 26: "
               "parking. Masterplan deed restrictions can refuse an exterior material."),
    "Code inside the city": (
        "2021 IRC, in force 1 January 2024. Appendix AW not adopted. Printed walls enter under R104.11, "
        "alternative materials and methods, on an ICC-ES report to AC509, with an engineered design under "
        "R301.1.3."),
}
CODE_A_DFW = {
    "Zoning": "Both cities zone. Masterplan deed restrictions can also refuse an exterior material.",
}
QUOTE_VULCAN = {
    "text": "The ICON wall systems must be placed using the proprietary ICON Vulcan printer, operated by "
            "qualified personnel as determined by ICON.",
    "who": "ICC-ES ESR-4652, Section 4.2, Installation, reissued June 2026",
    "url": ESR, "source": "ICC-ES ESR-4652"}
QUOTE_R102 = {
    "text": "Appendices A, B, C, H, K, L, M, Q, T, U, and V are hereby adopted and made part of this code.",
    "who": "Houston Amendments to the 2021 IRC, R102.5. Appendix AW, 3-D printed building construction, is "
           "not on the list.",
    "url": HOU_AMEND, "source": "Houston Amendments to the 2021 IRC"}


def code(D, mk):
    bad = []
    K = D.get("code") or {}
    for it in K.get("items") or []:
        q = it.get("q")
        if q not in CODE_Q:
            bad.append("audit12: code row %r not renamed" % q)
            continue
        it["q"] = CODE_Q[q]
        a = CODE_A.get(it["q"]) or (CODE_A_HOU if mk == "hou" else CODE_A_DFW).get(it["q"])
        if a:
            it["a"] = a
        if it["q"] == "Code in unincorporated counties":
            it["a"] = it["a"].replace("Ft. Worth is Tarrant County's.", "Tarrant County's is Fort Worth.")
    qs = K.get("quotes") or []
    if mk == "hou":
        qs = [q for q in qs if "iccsafe.org" not in (q.get("url") or "")]
        qs.insert(0, QUOTE_R102)
    i = next((n for n, q in enumerate(qs) if q.get("url") == ESR), None)
    if i is None:
        bad.append("audit12: the ESR quote left the code block")
    else:
        qs.insert(i + 1, QUOTE_VULCAN)
    K["quotes"] = qs
    P = {p["project"]: p for p in K.get("precedent") or []}
    if mk == "hou":
        z = P.get("Zuri Gardens")
        if z:
            z["what"] = ("80 homes, ground floors printed. $1.8 million TIRZ bond proceeds, council-approved, "
                         "plus HCDD infrastructure reimbursement. On the market from early summer 2026, per "
                         "InnovationMap.")
            z["source"] = "InnovationMap"
            z["more"] = [{"url": HOUSTONIA, "source": "Houstonia"}]
        a = P.get("Avenue J")
        if a:
            a["what"] = ("Elpis 3D Home Builders and HiveASMBLD duplex, started March 2026. Houston "
                         "Chronicle, 5 April 2026: completion expected by July.")
        g = P.get("Gulf Shore Estates")
        if g:
            g["what"] = ("26 homes planned, 23 to print. HiveASMBLD with Commander Home Builders. "
                         "Construction under way, April 2026, per ABC13.")
            # The Chronicle page on this row is about Zuri Gardens.
            g["more"] = [{"url": ABC13_SANLEON, "source": "ABC13"}]
        if not (z and a and g):
            bad.append("audit12: a Houston precedent row is missing")
    else:
        b = P.get("Bolt Street house")
        if b:
            b["what"] = ("One house, about 1,500 square feet, printed live May 2024 by Black Buffalo 3D. The "
                         "Fort Worth Report: said to be the first ICC-ES-approved residence with load-bearing "
                         "printed walls. Chapter 11 followed, December 2025.")
        p = P.get("PRINT3D Technologies")
        if p:
            p["what"] = ("Seven structures by May 2026, three of them houses. Many cities have no process to "
                         "inspect a printed home, its co-founder said, so it builds outside city limits.")
        if not (b and p):
            bad.append("audit12: a DFW precedent row is missing")
    return bad


# ------------------------------------------------------------------ market
PRINTED = [
    {"project": "Wolf Ranch", "place": "Georgetown", "printer": "ICON, with Lennar", "units": 100,
     "status": "Finished 2025, per ICON"},
    {"project": "Community First! Village", "place": "Austin", "printer": "ICON", "units": 100,
     "status": "100 under way from December 2024. ICON's page: 117 structures, 2019 to 2026"},
    {"project": "Zuri Gardens", "place": "Houston", "printer": "HiveASMBLD, for Cole Klein", "units": 80,
     "status": "Under way"},
    {"project": "Gulf Shore Estates", "place": "San Leon", "printer": "HiveASMBLD, for Commander", "units": 23,
     "status": "23 of 26 to be printed"},
    {"project": "Mueller", "place": "Austin", "printer": "ICON", "units": 12, "status": "Finished 2026, per ICON"},
    {"project": "Lumen Villas", "place": "Marfa", "printer": "HiveASMBLD", "units": 9,
     "status": "Started 2025, per HiveASMBLD"},
    {"project": "Wimberley Springs", "place": "Wimberley", "printer": "ICON", "units": 5,
     "status": "Finished 2025, per ICON. Eight announced, July 2024"},
    {"project": "Las Casitas", "place": "Round Top", "printer": "Hive3D, on a CyBe printer", "units": 5,
     "status": "Five rental casitas, from mid 2023, per CyBe"},
    {"project": "PRINT3D houses", "place": "Mabank and other Texas sites", "printer": "PRINT3D", "units": 3,
     "status": "Three houses among seven structures by May 2026, per Community Impact"},
    {"project": "Avenue J", "place": "Houston", "printer": "HiveASMBLD, for Elpis", "units": 2,
     "status": "One duplex, started March 2026"},
    {"project": "Spring Branch house", "place": "Houston", "printer": "PERI, on a COBOD printer", "units": 1,
     "status": "Printed July 2022 to May 2023, per PERI"},
    {"project": "Bolt Street house", "place": "Fort Worth", "printer": "Black Buffalo 3D, with Boxer Property",
     "units": 1, "status": "Printed May 2024"},
    {"project": "Von Perry house", "place": "Nevada, Collin County", "printer": "Von Perry", "units": 1,
     "status": "Begun December 2021, last reported August 2022"},
]
TIMELINE_FIX = {
    "SQ4D prints its first unit, Long Island":
        dict(year=2020, month=1, label="SQ4D finishes a 1,900 square foot printed house, Calverton, New York"),
    "Hive3D founded, Houston": dict(month=1, when="2022"),
    "Wolf Ranch completed": dict(month=12, when="2025", label="Wolf Ranch finished, per ICON"),
    "ICON delivers ten barracks at Fort Bliss": dict(label="Fort Bliss barracks open, two of ten"),
}
BANDS = ("An assumption, not a published figure. Yes: 25 to 400 homes a year, one or two printers. The "
         "Titans column assumes up to about 200 houses a year per Titan. ICON's Titan page: a 2,500 square "
         "foot home printed in under seven days, and an estimated two to three days of printing for a 2,200 "
         "to 4,000 square foot home. Wolf Ranch: one Vulcan and crew, about three weeks a home by August 2024 "
         "(Engadget, 8 August 2024). Zuri Gardens: a home shell in about two weeks, per the cement supplier "
         "(Eco Material).")


def market(D, mk):
    bad = []
    M = D.get("market") or {}
    M["printed"] = [dict(r) for r in PRINTED]
    seen = set()
    for e in M.get("timeline") or []:
        f = TIMELINE_FIX.get(e.get("label"))
        if f:
            seen.add(e["label"])
            e.update(f)
    if set(TIMELINE_FIX) - seen:
        bad.append("audit12: timeline rows not found: %s" % sorted(set(TIMELINE_FIX) - seen))
    M["timeline"] = sorted(M.get("timeline") or [], key=lambda e: (e["year"], e["month"]))
    if isinstance(D.get("bands_method"), dict):
        D["bands_method"]["text"] = BANDS
        src = D["bands_method"].setdefault("sources", [])
        if not any(s.get("url") == ICON_TITAN for s in src):
            src.insert(0, {"url": ICON_TITAN, "label": "ICON's Titan page, September 2026"})
    for m in D.get("method") or []:
        if m.get("title") == "Printer-fit bands":
            m["text"] = BANDS
        elif m.get("title") == "Printed units":
            m["text"] = "As reported by the developer or the printer, outlet named."
    if mk == "dfw":
        for o in M.get("owners") or []:
            if o.get("id") == "DFW-CH-011":
                o["line"] = o["line"].replace("Brightland", "DRB Homes")
                for b in o["builders"]:
                    if b["name"] == "Brightland":
                        b["name"] = "DRB Homes"
    return bad


# ------------------------------------------------------------------ views
GROUP_NOTES = {
    "hou": {
        "a": "Builders and developers outside the national and custom sections. Adopters and contractors "
             "with all three sit apart.",
        "trade": "Houston builders hire out walls. The three counts judge the wall.",
        "icon": "Lennar's Houston division, and two firms Lennar owns. LEN X invested in ICON in August 2021 "
                "and February 2025. Lennar built Wolf Ranch with ICON.",
    },
    "dfw": {
        "a": "Builders and developers outside the national and custom sections. Adopters and contractors "
             "with all three sit apart.",
        "trade": "DFW builders hire out walls. The three counts judge the wall.",
        "icon": "Lennar's DFW business. LEN X invested in ICON in August 2021 and February 2025. Lennar built "
                "Wolf Ranch with ICON.",
    },
}
DRAWN = {
    "hou": "Trade press, masterplan builder lists, the Builder 100, BUILDER's Local Leaders table and the "
           "Greater Houston Builders Association directory.",
    "dfw": "BUILDER's Local Leaders table, BUILDER firm pages, masterplan builder lists, trade press and firm "
           "websites.",
}
SCOPE_HOU = ("Greater Houston and its suburban counties. Not covered: architects, engineers, permitting "
             "authorities. One-off and retail work: the Custom and hybrid section. Held out, kept in the "
             "workbook: a builder whose chief executive says it left the metro.")
SUPPLY_LABELS = {"node": "Material suppliers", "crew": "Gunite and shotcrete crews"}
SUPPLY_NODE = "Few wall trades publish volume. Suppliers of concrete, tendons and block hold the numbers. " \
              "They sell to the crews."
SUPPLY_WHY = {
    "Ready Cable": ("Supplies pouring crews every part of a production slab. Not a competitor.",
                    "Supplies pouring crews every part of a production slab."),
    "Houston Post Tension": ("Nearly forty years supplying residential and elevated slabs. Sees the whole "
                             "slab market.", "Residential and elevated slab supply since 1987."),
    "SRM Concrete": ("Eleven volumetric loading sites. Volumetric batching is closest to a printer feed.",
                     "Eleven volumetric loading sites."),
    "NuBuild ICF": ("Its president built his own Nudura house. It can name every Houston crew setting "
                    "insulated forms.", "Its president built his own Nudura house."),
    "Houston Gunite": ("Hiring nozzlemen, top and bottom finishers, foremen and CDL drivers. The crew a printer "
                       "needs. Forty years shooting concrete.",
                       "Hiring nozzlemen, top and bottom finishers, foremen and CDL drivers. Forty years "
                       "shooting concrete."),
    "Union Gunite": ("Controls both material and nozzle, the whole operation a printer replaces.",
                     "Controls both material and nozzle."),
    "United Gunite": ("Instrumented placement. Crews meter material per shell in real time, a habit "
                      "printed-wall quality control needs.",
                      "Instrumented placement. Crews meter material per shell in real time."),
    "Pool Works": ("Sells nozzle work as a subcontract, the model for running a printer for a builder.",
                   "Sells nozzle work as a subcontract."),
    "JR Pool Plastering": ("Carries placement and surface crews. Calls a gunite pool one monolithic structure "
                           "without seams or joints, the printed-wall argument.",
                           "Carries placement and surface crews. Calls a gunite pool one monolithic structure "
                           "without seams or joints."),
    "Suncoast Post-Tension, Dallas": ("Sells tendons to DFW slab crews. Knows which pour at volume.",
                                      "Sells tendons to DFW slab crews."),
    "Tuf-N-Lite, Tiltwall Headquarters": ("Sells to DFW tilt-panel contractors. Knows who they are.",
                                          "Sells to DFW tilt-panel contractors."),
    "Acme Brick": ("Supplies masonry a printed wall would replace on production houses.",
                   "Supplies brick for production houses."),
    "Cowtown Materials": ("Light-gauge framing, which printed walls would replace in multifamily and "
                          "commercial.", "Light-gauge framing for multifamily and commercial."),
}


def views(D, mk):
    bad = []
    D.setdefault("group_notes", {}).update(GROUP_NOTES[mk])
    for lim in D.get("limits") or []:
        if lim[0] == "How the list was drawn":
            lim[1] = DRAWN[mk]
        elif lim[0] == "Scope" and mk == "hou":
            lim[1] = SCOPE_HOU
        elif lim[0] == "Who decides":
            lim[1] = re.sub(r"\s*Caveat on \d+ of \d+: [^.]*\.", "", lim[1])
        elif lim[0] == "Sources":
            lim[1] = lim[1].replace(" Nothing inferred.", "")
    if D.get("supply_labels"):
        D["supply_labels"].update(SUPPLY_LABELS)
    if (D.get("supply_notes") or {}).get("node"):
        D["supply_notes"]["node"] = SUPPLY_NODE
    for s in D.get("supply") or []:
        f = SUPPLY_WHY.get(s.get("name"))
        if f and s.get("why") == f[0]:
            s["why"] = f[1]
        if s.get("note") == "Team page names nobody.":
            s["note"] = None
    # A tile that counts nothing is left off.
    D["stat_strip"] = [s for s in D.get("stat_strip") or [] if not (s[0] == "0" and s[3])]
    return bad


# ------------------------------------------------------------------ spelling
# American throughout, as ICON's own pages write. "Centre Living" is a brand.
SPELL = [
    (r"\bmulti-storey\b", "multi-story"), (r"\bstoreys\b", "stories"), (r"\bstorey\b", "story"),
    (r"\bprogrammes\b", "programs"), (r"\bprogramme\b", "program"), (r"\bProgramme\b", "Program"),
    (r"\bcentres\b", "centers"), (r"\bcentre\b", "center"), (r"\bon-centre\b", "on-center"),
    (r"\bcatalogue\b", "catalog"), (r"\bneighbourhoods\b", "neighborhoods"),
    (r"\bneighbourhood\b", "neighborhood"), (r"\bfibre\b", "fiber"), (r"\blabour\b", "labor"),
    (r"\bstandardised\b", "standardized"), (r"\bStandardised\b", "Standardized"),
    (r"\bcentralised\b", "centralized"), (r"\bPanelising\b", "Panelizing"), (r"\bpanelised\b", "panelized"),
    (r"\bpanelisation\b", "panelization"), (r"\bmetres\b", "meters"), (r"\bEnquiries\b", "Inquiries"),
    (r"\benquiries\b", "inquiries"), (r"\borganisations\b", "organizations"), (r"\bmoulds\b", "molds"),
    (r"\bmodelling\b", "modeling"), (r"\bMobilisation\b", "Mobilization"), (r"\bpersonalise\b", "personalize"),
    (r"\bauthorised\b", "authorized"),
    # one date format for one fact
    (r"sworn in as Texas Comptroller on August 1, 2026", "sworn in as Texas Comptroller on 1 August 2026"),
]
_SPELL = [(re.compile(a), b) for a, b in SPELL]
SKIP_KEYS = {"url", "source_url", "linkedin_url", "homepage_url", "team_url", "company_li", "phone_source",
             "email", "target_id", "id"}


def spell(o, key=None):
    if isinstance(o, dict):
        for k, v in o.items():
            o[k] = spell(v, k)
        return o
    if isinstance(o, list):
        return [spell(v, key) for v in o]
    if isinstance(o, str) and key not in SKIP_KEYS and not o.startswith("http"):
        for rx, to in _SPELL:
            o = rx.sub(to, o)
    return o


def final(D, mk):
    """All text and page edits, after audit11. Returns a list of problems."""
    bad = cards(D, mk)
    bad += closings(D, mk)
    bad += icon(D, mk)
    bad += field(D, mk)
    bad += code(D, mk)
    bad += market(D, mk)
    bad += views(D, mk)
    for k in list(D.keys()):
        if k not in ("paid",):
            D[k] = spell(D[k], k)
    # A source added here goes before any subscription link, as audit11 orders them.
    import audit11
    audit11.second(D)
    return bad
