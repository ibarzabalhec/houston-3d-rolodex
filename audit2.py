# -*- coding: utf-8 -*-
"""Round two, and what checking the checker cost.

Round one audited thirty cards. Round two audited the seventy-six it had not
touched, and re-ran the whole contact layer through a probe that does not read
pages at all: it fetches the bytes and asks whether the name is in them.

Round two found more than round one did. That is the finding about the method,
not about the deck: one pass finds what one pass looks at.

Three corrections in this file are corrections of round one.

The probe reported Cullen Burton missing from Burton Construction's leadership
page. He is on it. The site answers a script with a 182-byte bot stub and a
browser with the full roster, so the probe saw an empty page and called a real
person absent. probe.py now treats a body under two kilobytes as unreadable
rather than as evidence.

Round one published Derrick Hughes as Wan Bridge's construction vice president
on the strength of a fetch that returned his bio. The URL is a 404. He never
shipped, because the link checker ran before the build did.

Round one's reason-versus-mark check caught eight contradictions and missed two
more, HTX Concrete and T&T Construction, because both phrase the same rule in
words the pattern did not match. The check is wider now.

Every finding here was adjudicated against raw bytes before it was applied: the
page was fetched, and the figure or the name was either in it or was not. Agent
findings that failed that gate are not in this file.
"""

# ---------------------------------------------------------------- people

DROP_PEOPLE = {
    # Not on Ashton Woods' own executive list. The firm publishes Adam Weaver in
    # purchasing and Ken Newman in construction operations, added below.
    ("HOU-024", "DeKendrick Vidito"),
    # Neither name is anywhere in kendallhomes.net. The firm publishes one
    # executive, its founder.
    ("HOU-063", "Glenn Briggs"),
    ("HOU-063", "Jason Madden"),
    # Not on Perry's about page, and nothing outside a data broker carries
    # either name. Perry publishes no construction or purchasing officer.
    ("HOU-013", "Shane Huhn"),
    ("HOU-013", "Lauren Chachere"),
    # Not on David Weekley's own team page and not in the preferred-partners
    # release. No permitted source names him.
    ("HOU-023", "Chad Durham"),
    # Not on c-rock.com/about, which names two people and no chief financial
    # officer.
    ("HOU-022", "Bruce Torkelson"),
    # The card said it itself: no page outside a data aggregator names her with
    # a title at Sitterle. That is not a contact, it is a lead.
    ("HOU-077", "India Kinslow"),
    # Not on the Meritage management page. Three division names carried from
    # LinkedIn headlines with nothing published behind them.
    ("HOU-008", "Jayar Griffith"),
    ("HOU-008", "Jeremy Flach"),
    ("HOU-008", "Kyle Davison"),
    # Not on any Coventry page. His own headline gives no title.
    ("HOU-033", "Brian Grigsby"),
    # Not on First America's about page and not on the parent's leadership page.
    # The card also asserted a predecessor's departure date with nothing behind
    # it. Both go.
    ("HOU-007", "Mike Faul"),
    # The Signorelli leadership page names a Ragan Robinson, Director of
    # Investments. It does not name Troy Robinson, and neither does First
    # America's own about page. First America publishes no construction officer.
    ("HOU-007", "Troy Robinson"),
    # Named as Devon Street's founder in a 2023 acquisition announcement that
    # this URL no longer carries. Smith Douglas's January 2026 leadership
    # release names no Houston division leader.
    ("HOU-074", "Stephen Ray"),
}

# A contact whose name is not in the page cited for it, where the firm does
# publish the name somewhere else. The title was right and the link was wrong.
RESOURCE = {
    # The authority's own leadership page stopped resolving. Both titles stand on
    # the last version of it, and neither can be checked today.
    ("HOU-003", "Jamie Bryant"): None,
    ("HOU-003", "Neal Rackleff"): None,
    ("HOU-023", "John Schiegg"):
        "https://www.prnewswire.com/news-releases/david-weekley-homes-announces-2026-national-preferred-partners-302809074.html",
    ("HOU-007", "David Assid"): "https://www.signorellicompany.com/our-leadership",
    # Not on the firm's own about page. The Builder 100 firm page names him.
    ("HOU-134", "Saun Sullivan"): "https://www.builderonline.com/firms/dsld-homes/",
}

PEOPLE = {
    ("HOU-024", "Adam Weaver"): (
        "Senior Vice President of Purchasing",
        "https://www.ashtonwoods.com/corporate-info", None),
    ("HOU-024", "Ken Newman"): (
        "Senior Vice President of Construction Operations",
        "https://www.ashtonwoods.com/corporate-info", None),
    ("HOU-063", "David Wickens"): (
        "Founder", "https://kendallhomes.net/",
        "The only executive the firm publishes."),
    ("HOU-066", "Jo Dunham"): (
        "Vice President of Construction",
        "https://www.sandcastlehouston.com/about-sandcastle/meet-our-team/", None),
    ("HOU-066", "Katie Pritchard"): (
        "Purchasing Manager",
        "https://www.sandcastlehouston.com/about-sandcastle/meet-our-team/", None),
    ("HOU-113", "Martin Jordana"): (
        "President, Central and Great West Region",
        "https://bakerconstruction.com/leadership/",
        "The regional seat that covers Texas."),
    ("HOU-113", "Karl Watson"): (
        "Chief Executive Officer, Baker Construction Enterprises",
        "https://bakerconstruction.com/leadership/", None),
    ("HOU-113", "Dan T. Baker"): (
        "Executive Vice Chair and President",
        "https://bakerconstruction.com/leadership/", None),
    ("HOU-103", "Adrian Villarreal"): (
        "Co-founder",
        "https://www.texasamconcrete.com/blogs/news/texas-concrete-contractor-makes-it-big",
        None),
    ("HOU-103", "Marcos Chavez"): (
        "Co-founder",
        "https://www.texasamconcrete.com/blogs/news/texas-concrete-contractor-makes-it-big",
        None),
    ("HOU-077", "Jeff Buell"): (
        "Co-owner", "https://sitterlehomes.com/about-us/",
        "The about page records the two of them acquiring the company in 2005 and "
        "assigns neither a title."),
}

DECIDER = {
    ("HOU-024", "Adam Weaver"): True,
    ("HOU-024", "Ken Newman"): True,
    ("HOU-066", "Jo Dunham"): True,
    ("HOU-113", "Martin Jordana"): True,
}

RETITLE = {
    # The firm publishes him as Hachem. Hugo is a LinkedIn display name.
    ("HOU-129", "Hugo Domloj"): "President and Chief Executive Officer",
    # Every one of these is the title on the page the card already cites, and
    # every one of them was published as something else.
    ("HOU-030", "R. Carson Wilson IV"): "Vice President, Leasing",
    ("HOU-030", "Glenn Airola"):
        "Executive Vice President, General Counsel and Chief Administrative Officer",
    ("HOU-030", "K. Alan Hassenflu"): "President and Chief Executive Officer",
    ("HOU-024", "Lindsay Motley"): "Regional President",
    ("HOU-066", "Mike Dishberger"): "Chief Executive Officer and Co-Owner",
    ("HOU-077", "Frank Sitterle, Jr."): "Co-owner",
    ("HOU-103", "David Buzzelli"): "Vice President",
    # The parent's leadership page, verbatim.
    ("HOU-007", "David Assid"): "Houston Division President, Homebuilding",
}

RENAME = {
    ("HOU-129", "Hugo Domloj"): "Hachem Domloj",
}

# ---------------------------------------------------------------- records

KEY_STAT = {
    "HOU-063": "Founded 1993, more than 4,000 homes on the firm's own count",
    "HOU-010": "10,000th rental home, May 2023",
    "HOU-081": "East Blocks phase one, 30,000 sf across two warehouses",
    "HOU-006": "341 units at The Mill, 294 more under construction at Aliana",
    "HOU-032": "Its own domain no longer resolves to a site",
    "HOU-064": "540 closings in 2025, fourteen communities published",
    "HOU-014": "153 active selling communities, 36 markets, 21 states",
}

SCORE = {
    # Nothing about this firm is published anywhere the deck can cite. Its own
    # domain is a parked lander and it was the only source on the card.
    "HOU-032": {"repeatability": 0, "machine_fit": 0, "innovation": 0},
    # The Mill's timber frame was an expectation in a 2021 article, contingent on
    # retail leasing. The delivered building is a concrete podium under five
    # storeys of wood frame, and the firm's own portfolio entry carries no office
    # component at all. An intention is not a track record.
    "HOU-006": {"innovation": 2, "machine_fit": 2},
    # Three cards state the band rule and then break it.
    "HOU-108": {"machine_fit": 2},
    "HOU-109": {"machine_fit": 2},
    "HOU-063": {"machine_fit": 2},
    # "Search ended early" is not a finding of absence.
    "HOU-022": {"innovation": 1},
    # The sentence carrying the No is false: the 2026 partner list names cladding,
    # roofing, weather barrier, structural connectors and engineered framing.
    "HOU-023": {"innovation": 2},
}

WHY = {
    "HOU-032": (
        "Nothing is published. The firm's own site is a parked domain.",
        "No community, unit count or volume figure survives on any page the deck "
        "can cite.",
        "Nothing on record."),
    "HOU-064": (
        "Fourteen communities on its own communities page, all inside Greater "
        "Houston, taking a standard plan set.",
        "540 closings in 2025 and 552 in 2024 across fourteen published "
        "communities. Two machines would carry a fifth of output at most.",
        "No method evidence. The published positioning is price and floor plan, "
        "not construction."),
    "HOU-063": (
        "Communities clustered on the Lake Conroe corridor, with outliers at Bay "
        "City and West Columbia.",
        "No annual closings figure is published. On the bands, a firm with no "
        "published figure is a Partly.",
        "The firm's published positioning is against speed and cost cutting. A "
        "printed wall would be measured on the firm's own terms."),
    "HOU-010": (
        "Three brands and a lot bank of 25,000 to 35,000 residential lots held at "
        "any time.",
        "The rental portfolio passed its ten thousandth home in May 2023, far "
        "above one machine, though the build-and-hold model is the right shape.",
        "No construction-method statement found anywhere."),
    "HOU-026": (
        "314 homes in Conroe and 240 in Cypress.",
        "240 homes on nineteen acres in Cypress, built to hold. One machine "
        "covers a community at a time.",
        "Its stated technology package is smart-home fittings, not structure."),
    "HOU-006": (
        "341 units at The Mill, 294 more under construction at Aliana.",
        "The Landing at Aliana is 294 units of three-storey garden-style housing "
        "on one Fort Bend site. That is the repeating low-rise the band covers.",
        "It expected to use cross-laminated timber on a six-storey office "
        "building at The Mill in 2021, contingent on retail leasing. The building "
        "is not in its own portfolio entry and no source shows it was built."),
    "HOU-071": (
        "About seventy-five houses a year across sixteen communities.",
        "About seventy-five homes a year, stated by the firm. One machine would "
        "carry most of it.",
        "No method evidence. The published build time is eight to ten months, "
        "which is the number a printed wall argument would have to move."),
    "HOU-118": (
        "Single family and townhome communities across the north and west of the "
        "metro, taking the same wall package community after community.",
        "9,900 homes a year on the firm's own count, company-wide across Florida "
        "and Texas, far above what one or two printers cover.",
        "No method statement on record."),
    "HOU-023": (
        "Houston is the firm's home market and it builds across the metro.",
        "A national builder with a national supply chain.",
        "Its 2026 preferred-partner list names cladding, roofing, weather "
        "barrier, structural connectors and engineered framing. That is the "
        "envelope, and it is a supply-chain commitment rather than a method."),
    "HOU-022": (
        "20,000 homes since 2004, 1,600 closed in a single year.",
        "20,000 homes since 2004 is roughly a thousand a year, above the band but "
        "not beyond a two-machine pilot.",
        "Daiwa House holds the majority and is an industrialised builder in "
        "Japan. Nothing published connects that to CastleRock's own method."),
    "HOU-014": (
        "153 active selling communities on one systematic plan set.",
        "Thousands of closings a year across 36 markets in 21 states.",
        "Nothing on record."),
}

SYNOPSIS = {
    "HOU-032":
        "Houston developer and brokerage of inner-loop townhome communities. Its "
        "own domain, the only source this record ever had, now redirects to a "
        "parked-domain lander with no communities, no leadership and no content. "
        "Nothing published supports a current operation, so the record is held "
        "off the roster rather than carried on a page that no longer exists.",

    "HOU-064":
        "Affordable production builder founded in 2007 by Ken Williams, selling "
        "on no-haggle pricing across fourteen communities published on its own "
        "site, from Katy and Cypress to Magnolia, Willis, Splendora and Texas "
        "City. Builder reports 540 closings in 2025 and 552 in 2024.",

    "HOU-033":
        "Houston-founded production homebuilder established 1988, now a "
        "subsidiary of NASDAQ-listed Dream Finders Homes. Operates close to 100 "
        "unique communities across four Texas markets with more than 55,000 homes "
        "closed company-wide, thirty of them in Greater Houston. Coventry is a "
        "Dream Finders Homes brand and its Houston division president carries DFH "
        "in his own title.",

    "HOU-068":
        "Founder-led semi-custom builder in Sugar Land, active only in Houston and "
        "Austin, with the widest footprint in the south suburban master planned "
        "communities of any builder screened. Its own communities index lists "
        "twenty-eight Houston communities. Builder reports 1,062 closings and $621 "
        "million in 2025, rank 60 on the 2026 Builder 100. The firm's twentieth-"
        "anniversary release, dated December 2014, names Jason Golan as founder.",

    "HOU-066":
        "Inner Loop infill builder founded in 1995, averaging about fifty closings "
        "a year in Rice Military, Sawyer Heights, Garden Oaks, Sunset Heights and "
        "Montrose. Its own team page publishes a vice president of construction "
        "and a purchasing manager, so both functions are staffed under the chief "
        "executive rather than held by him.",

    "HOU-063":
        "Family builder founded in 1993, selling from the $300,000s to the "
        "$800,000s. Its own site publishes communities in Conroe, Willis, New "
        "Caney and New Waverly on the Lake Conroe corridor, and at Alvin, Dayton, "
        "Bay City and West Columbia at the edges of the metro. The firm publishes "
        "more than 4,000 homes since 1993 and over $1 billion in revenue, and no "
        "single-year closings figure. Its only published executive is its founder.",

    "HOU-010":
        "Houston real estate group founded in 1989 running three brands: "
        "SimplyHome single-family build-to-rent, which announced its ten "
        "thousandth rental home in May 2023, Legend Homes for-sale production "
        "housing, and Academy Development. Holds 25,000 to 35,000 residential lots "
        "owned or in development at any time. Camillo publishes no "
        "construction-method or technology content.",

    "HOU-081":
        "Investment and development firm whose business spans industrial "
        "development and acquisitions, adaptive reuse, traditional multifamily and "
        "build-to-rent communities. East Blocks is ten contiguous EaDo blocks; "
        "phase one broke ground in April 2026 and is the adaptive reuse of two "
        "15,000 square foot warehouses at 1107 Hutchins Street and 2202 Dallas "
        "Street, 30,000 square feet combined, completion expected August 2026. The "
        "district figure of 513,000 square feet is the full ten-block programme, "
        "not phase one. Gensler on design, SWA on landscape, in joint venture with "
        "Wile Interests. Preston Luster is the senior construction manager on the "
        "team page, and the two managing principals are the decision layer.",

    "HOU-026":
        "Arizona build-to-rent operator that made its first Texas acquisition on "
        "October 17, 2024, buying the 314-home, 40-acre Cottage Green in Conroe, "
        "Montgomery County, rebranded Cottage Living. Also built the 240-home "
        "Christopher Todd Communities at Cypress on almost nineteen gated acres "
        "with Taylor Morrison. The Conroe acquisition price is not disclosed. "
        "Cottage Living was acquired rather than developed by the firm.",

    "HOU-022":
        "Privately held homebuilder founded April 1, 2004 in Houston with more "
        "than 20,000 homes built across 300-plus communities and a 2020 milestone "
        "of over 1,600 closings in a single year. Ranked 49th on the 2025 USA Top "
        "Builders list. Daiwa House Industry holds 80 percent, acquired for about "
        "$408 million and announced 10 August 2021, funding expansion into "
        "Arizona, Tennessee and Alabama. Builder in Austin Point Phase I. Its own "
        "about page names two people: a chief executive and a senior executive "
        "vice president. No technology transfer, prefab pilot, board seat or joint "
        "statement between CastleRock and Daiwa House is on record, and CastleRock "
        "publishes no construction-method content.",

    "HOU-006":
        "Houston investor-developer. The Landing at Aliana is 294 units of "
        "three-storey garden-style housing on one Fort Bend site, under "
        "construction from March 2026, opening summer 2027 and completing 2028, "
        "with NewQuest Properties. The Mill is a six-acre East End redevelopment "
        "of a preserved 1890s brick mill, delivered in 2025 as 341 apartments over "
        "a cast-in-place concrete podium with five storeys of wood frame above it. "
        "A six-storey cross-laminated timber office building was reported in 2021 "
        "as a second phase, contingent on retail leasing; it does not appear in "
        "the firm's own portfolio entry. Michael Hsu and EDI on design. Triten and "
        "Radom Capital are the same pair across the Heights packing-plant cluster, "
        "M-K-T and the Swift BLDG.",

    "HOU-071":
        "Family builder founded in 2008 by Greg Hawes with his daughters, building "
        "about seventy-five homes a year across sixteen communities from Sienna to "
        "Montgomery. The firm publishes an eight to ten month build time from "
        "design to completion. No plan count is published on either page the "
        "record cites.",

    "HOU-118":
        "Shell contractor whose Houston division carries slab masonry, wood "
        "framing and drywall on single family and townhome communities, delivering "
        "the whole wall package under one contract and describing those stages as "
        "work it performs under one accountable roof. It also works through a "
        "network of more than 900 subcontractors. The firm's headquarters and "
        "ownership sit in Florida.",

    "HOU-113":
        "Concrete specialty contractor, formerly trading as Baker Concrete "
        "Construction, with a standing Houston industrial office inside a national "
        "business of more than 12,500 people, named as the concrete subcontractor "
        "on the tallest tilt-wall job under way in the metro. Its own leadership "
        "page names fourteen executives including a president for the Central and "
        "Great West region, which is the seat that covers Texas. The locations "
        "page names five regional headquarters and no Texas office; the Houston "
        "address comes from a trade association listing.",

    "HOU-103":
        "Turnkey concrete contractor that supplies, forms, places and finishes its "
        "own work, with a tilt-up record carried in the Tilt-Up Concrete "
        "Association's own project archive. Its own news post names two "
        "co-founders and a vice president.",

    "HOU-030":
        "Houston retail developer managing roughly 26 million square feet across "
        "nearly 100 properties in 12 states. Bought acreage near the Grand Parkway "
        "in Alvin, Brazoria County in November 2024 for a planned 280,000 square "
        "foot Alvin Marketplace, and separately acquired 33 acres in New Caney, "
        "Montgomery County. Its own page carries a lower set of portfolio figures, "
        "10 million square feet across 60-plus properties in four states, and the "
        "two have not been reconciled.",

    "HOU-038":
        "Property and facilities manager of the Niels Esperson and Mellie Esperson "
        "towers in downtown Houston, 1927 and 1941, where it had planned to convert "
        "office floors to apartments. MetLife foreclosed in August 2024 after a "
        "default on a loan issued in December 2018, and Interra Capital Group "
        "acquired the buildings; Cameron Management was retained as the property "
        "and facilities management team for a designated period. It no longer owns "
        "the buildings the conversion sat in, and no source shows the conversion "
        "surviving the sale.",

    "HOU-013":
        "Houston-founded builder, family owned since 1967, now building across "
        "Houston, Austin, Dallas-Fort Worth and San Antonio and, since February "
        "2024, across Florida in Orlando, Tampa, Sarasota, Port St. Lucie and "
        "Jacksonville. Its own about page describes the markets it builds in "
        "rather than a homes-sold total, and it publishes no construction or "
        "purchasing officer.",

    "HOU-023":
        "Houston-founded national builder, the largest privately held builder in "
        "the country by its own description, headquartered in Houston and building "
        "across it. Its 2026 National Preferred Partners list names 27 suppliers "
        "including James Hardie on cladding, GAF on roofing, DuPont on weather "
        "barrier, Simpson Strong-Tie on structural connectors and Weyerhaeuser on "
        "engineered framing. John Schiegg is quoted in that release as Vice "
        "President of Purchasing and Supply Chain Services.",

    "HOU-014":
        "Systematic production builder headquartered in The Woodlands, closing "
        "thousands of homes a year across 36 markets in 21 states, with 153 active "
        "selling communities as of 31 August 2026 and more than 80,000 homes "
        "closed since 2003. Purchasing is a national function.",

    "HOU-076":
        "Entry-level builder launched in 2025, whose first community was Rose Hill "
        "in Denison, north Texas. It joined the builder lineup at Magnolia Springs "
        "in Greater Houston in December 2025 and at Meridiana in Manvel in January "
        "2026. Greg Grahmann is named in trade coverage as director of Imagination "
        "Homes and as having joined David Weekley Homes in 2013.",

    "HOU-070":
        "Semi-custom builder in Cypress across Artavia, Audubon, Bridgeland, Cross "
        "Creek West, The Highlands and The Woodlands Hills. Its own about page says "
        "the founding brothers worked as division presidents at a major Houston "
        "builder and does not name the builder.",

    "HOU-003":
        "Public housing authority for the City of Houston, running a five-phase "
        "redevelopment of Cuney Homes in the Third Ward, opened 1943, announced 22 "
        "October 2025 and running 2025 to 2032 on more than $600 million including "
        "a $50 million HUD grant. Unit counts are not disclosed in the "
        "announcement. Both domains the authority published, "
        "housingauthorityhouston.org and housingforhouston.com, stopped resolving, "
        "so the leadership titles below are the last ones it published rather than "
        "ones that can be checked today.",

    "HOU-074":
        "Georgia builder that entered Houston by acquiring Devon Street Homes in "
        "2023, which had closed 324 homes across 15 communities with about 1,500 "
        "lots in 2022. Its January 2026 leadership announcement names regional and "
        "division presidents for the Southeast, Atlanta and Chattanooga and no "
        "Houston division leader, and no current company page publishes one.",

    "HOU-077":
        "San Antonio builder founded in 1964, now in four Texas markets including "
        "Houston. Builder's last published figures are 372 closings and $210 "
        "million in 2022, with nothing filed since. Its own about page records two "
        "co-owners acquiring the company in 2005 and assigns neither a title.",
}

# Both of the Houston Housing Authority's published domains stopped resolving.
DROP_HOMEPAGE = {"HOU-032", "HOU-003"}
DROP_TEAM_URL = {"HOU-003"}

# Wile Interests carried Pagewood's domain as its own homepage.
HOMEPAGE = {
    "HOU-082": "https://www.wileinterests.com/",
}

# ---------------------------------------------------------------- evidence

DROP_PROJECTS = {
    # The cited release is the firm's north Texas launch and names neither.
    ("HOU-076", "Meridiana"),
}

EDIT_PROJECT_URL = {
    # id=5900 is Sam Houston High School, another firm's job. The project these
    # two cards describe, with these exact figures, is id=6094.
    ("HOU-103", "TCC Multi-Family Interiors"): "https://tilt-up.org/projects/profile/?id=6094",
    ("HOU-114", "TCC Multi-Family Interiors"): "https://tilt-up.org/projects/profile/?id=6094",
    # The president title is on the acquisition release, not the appointment one.
    ("HOU-026", "Cottage Living"):
        "https://www.christophertodd.com/press-releases/christopher-todd-capital-makes-first-texas-btr-acquisition/",
}

PROJECTS = {
    "HOU-081": [
        ("East Blocks phase one",
         "1107 Hutchins Street and 2202 Dallas Street, two warehouses of 15,000 "
         "square feet each, 30,000 square feet combined. Groundbreaking April "
         "2026, completion expected August 2026.",
         "repeatable",
         "Two buildings of one size, done twice, is the shape a repeated wall "
         "assembly needs.",
         "https://www.pagewood.com/press/pagewood-breaks-ground-on-phase-1-of-east-blocks")],
    "HOU-023": [
        ("2026 National Preferred Partners",
         "Twenty-seven suppliers named, including James Hardie on cladding, GAF on "
         "roofing, DuPont Performance Building Solutions on weather barrier, Owens "
         "Corning, Simpson Strong-Tie on structural connectors and Weyerhaeuser "
         "Trus Joist on engineered framing.",
         "method_risk",
         "The firm commits to a named supplier for every layer of the wall, which "
         "is the list a printed wall would have to enter.",
         "https://www.prnewswire.com/news-releases/david-weekley-homes-announces-2026-national-preferred-partners-302809074.html")],
}

SOURCES = {
    "HOU-064": ["https://www.colinahomes.com/communities"],
    "HOU-063": ["https://kendallhomes.net/"],
    "HOU-066": ["https://www.sandcastlehouston.com/about-sandcastle/meet-our-team/"],
    "HOU-024": ["https://www.ashtonwoods.com/corporate-info"],
    "HOU-113": ["https://bakerconstruction.com/leadership/"],
    "HOU-118": ["https://leolaconstruction.com/houston/"],
    "HOU-081": ["https://www.pagewood.com/press/pagewood-breaks-ground-on-phase-1-of-east-blocks",
                "https://www.pagewood.com/"],
    "HOU-006": ["https://www.tritenre.com/portfolio/the-mill",
                "https://www.arch-con.com/themilltopsout/"],
    "HOU-038": ["https://realtynewsreport.com/historic-esperson-buildings-acquired-in-foreclosure-sale/"],
    "HOU-023": ["https://www.prnewswire.com/news-releases/david-weekley-homes-announces-2026-national-preferred-partners-302809074.html",
                "https://www.davidweekleyhomes.com/about-us/meet-the-team"],
    "HOU-013": ["https://www.perryhomes.com/about-perry-homes"],
    "HOU-014": ["https://www.globenewswire.com/news-release/2026/09/04/3356358/28788/en/LGI-Homes-Inc-Reports-August-2026-Home-Closings.html"],
    "HOU-129": ["https://cive.com/about/"],
    "HOU-103": ["https://tilt-up.org/projects/profile/?id=6094"],
    "HOU-114": ["https://tilt-up.org/projects/profile/?id=6094"],
    "HOU-077": ["https://sitterlehomes.com/about-us/"],
    "HOU-070": ["https://www.ravennahomes.com/about/"],
    "HOU-033": ["https://www.coventryhomes.com/new-homes/tx/houston/"],
    "HOU-068": ["https://www.westin-homes.com/communities/houston"],
}

DROP_SOURCES = {
    # Both are the parked lander.
    ("HOU-032", "https://urbanliving.com/"),
    ("HOU-032", "https://urbanliving.com/developments.php"),
    # id=5900 is another firm's job.
    ("HOU-103", "https://tilt-up.org/projects/profile/?id=5900"),
    ("HOU-114", "https://tilt-up.org/projects/profile/?id=5900"),
    # Does not carry the community the card cites it for.
    ("HOU-076", "https://www.prnewswire.com/news-releases/imagination-homes-launches-breaks-ground-on-first-community-302539487.html"),
}
