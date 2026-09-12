# -*- coding: utf-8 -*-
"""Firms the directory found that the press did not.

The deck was assembled from trade press, master-planned-community builder
rosters and the Builder 100. None of those enumerate a privately held builder
that does not issue releases. The Greater Houston Builders Association member
directory does: 190 companies under Builder - Single Family alone.

Reading that list against the deck found 164 names not on it. Most are custom
and infill shops of one to five homes a year, below the band a printer serves.
Two were production builders that belong here, and one of them is the largest
privately held homebuilder in Greater Houston.

The first pass read one category. The directory carries six more: Build-to-Rent,
Build On Your Lot, ICF Homes, 50+ Communities, Multi-Family and Townhomes, and
Developers. Reading those found three more builders, and reading the two largest
builders in the metro by permit against the deck found that neither was on it.

Scores are (repeatability, machine_fit, innovation, capital_access), 3 clears,
2 partial, 0-1 fails.
"""

GAP = [

 # 782 closings in 2025 and 912 in 2024, 22 communities, 38 numbered plans across
 # four series. That is roughly 20 to 24 starts per plan per year, which is the
 # repetition the first count asks about, at a volume a machine works through.
 # It also develops its own land through Woodmere, so a pilot needs nobody else's
 # permission. The objection is on the record and in its own words: it sells
 # "job-built production methods" as a control advantage.
 ("HOU-130", "Long Lake, Ltd.", "Houston / Harris, Montgomery, Fort Bend",
  "https://www.longlakeltd.com/",
  "782 closings in 2025, 38 plans",
  "The largest privately held homebuilder in Greater Houston by its own "
  "description, founded 1997, with more than 29,000 homes delivered. 782 closings "
  "in 2025 and 912 in 2024, ranked 74th on the 2026 Builder 100. Sells in 22 "
  "Greater Houston communities from $249,990 to $627,900, including Sunterra Lakes "
  "and Sunterra North. Publishes 38 floor plans across four product lines, "
  "Briarwood, Discovery, Lake Ridge and Lakewood, and identifies them by number "
  "rather than name. Develops its own land through Woodmere Development Co., which "
  "bought 95 acres in Montgomery County in November 2024 and 494 acres beside "
  "Bridgeland in 2022. Its about page sells job-built production methods as a "
  "control advantage.",
  (3, 2, 0, 3),
  "782 closings across 22 communities on 38 numbered plans, and it develops its own "
  "land, so a pilot needs nobody else's permission.",
  ("22 communities on 38 plans in four series, about twenty starts per plan a year.",
   "782 closings in 2025 sits above the band one or two printers cover, so the first "
   "order is a line inside the business rather than the whole business.",
   "Nothing on record. Its about page argues the other way, for job-built production "
   "methods as a control advantage."),
  [("Craig Jones", "Chief Executive Officer"),
   ("Dustin Rodgers", "Vice President of Construction"),
   ("Dave Dronberger", "Construction Manager"),
   ("Aaron Alford", "Executive Vice President, Woodmere Development Co.")],
  [("The 38-plan library",
    "Four product lines, Briarwood, Discovery, Lake Ridge and Lakewood, identified by "
    "plan number. Creekwood Crossing sells plans 218, 252, 254, 264, 265 and 269 at "
    "1,876 to 2,837 square feet.",
    "repeatable",
    "A numbered plan library repeated across 22 communities is the condition the first "
    "count is looking for, and the reason a wall assembly changed once reaches every "
    "community at the same time.",
    "https://www.longlakeltd.com/new-homes/communities/creekwood-crossing/"),
   ("Woodmere Development Co.",
    "The firm's own land arm. 95 acres at Decker Prairie-Rosehill Road in Montgomery "
    "County, bought from the Brautigam family in November 2024. 494 acres beside "
    "Bridgeland in 2022.",
    "repeatable",
    "It owns the ground it builds on, so a method change does not need a land "
    "developer's approval first.",
    "https://therealdeal.com/texas/houston/2024/11/25/long-lake-purchased-100-acre-tract-in-houston-area/")],
  ["https://www.longlakeltd.com/",
   "https://www.longlakeltd.com/about/",
   "https://www.longlakeltd.com/new-homes/communities/",
   "https://www.builderonline.com/firms/long-lake-limited/",
   "https://sunterratx.com/homebuilders/long-lake/",
   "https://members.ghba.org/memberdirectory/Search/builder-single-family-132864"],
  []),

 # The opposite profile and worth keeping for it: low volume, but one named person
 # holds construction and purchasing together, and the price band absorbs a method
 # premium that Long Lake's does not. It has paid for above-code performance before,
 # which is not a structural method and is not counted as one.
 ("HOU-131", "Caldwell Homes", "Cypress, Porter, Willis / Harris, Montgomery",
  "https://www.caldwellhomes.com/",
  "Three 55+ communities, $448,600 to $875,000",
  "The homebuilding division of Caldwell Companies, launched February 2017, building "
  "single-storey homes for buyers aged 55 and over. Three Greater Houston "
  "communities: The Heritage at Towne Lake in Cypress, Fairway Pines at The "
  "Highlands in Porter, and Chambers Creek in Willis, where a new Heritage "
  "Collection opened in July 2026. Homes run $448,600 to $875,000 at 1,900 to 2,819 "
  "square feet, on a shared plan library whose names repeat across communities. "
  "Ranked 41st on the Houston area 2023 builder list, the only active-adult builder "
  "on it. No annual closings figure is published. Towne Lake is developed by its own "
  "parent, so part of its pipeline sits on ground the group controls.",
  (3, 3, 2, 2),
  "One person holds construction and purchasing, the plan library repeats across all "
  "three communities, and the price band absorbs a method premium.",
  ("The same named plans, Cardinal, Bluebell, Texas Paintbrush, Bayberry II and "
   "Waterlily, sell in more than one community.",
   "Three communities and a rank of 41 in the metro put it inside the band one or two "
   "printers cover.",
   "It has paid for above-code performance, ENERGY STAR certification and a 2020 PRISM "
   "award for an energy-efficient home, but nothing structural."),
  [("Fred Caldwell", "Chief Executive Officer"),
   ("Peter Barnhart", "President"),
   ("Tim Mayo", "Senior Vice President of Operations"),
   ("Kevin Johnson", "Vice President of Construction and Purchasing"),
   ("Anthony Moreno", "Vice President of Sales")],
  [("The Heritage at Towne Lake",
    "Cypress. Heritage Cove, Sunset Harbor Garden Homes and Sunset Harbor Villas, "
    "$448,600 to $875,000. Towne Lake is developed by Caldwell Companies, the parent.",
    "repeatable",
    "Single-storey product on a repeating plan library, on ground the group already "
    "controls.",
    "https://www.caldwellhomes.com/communities/towne-lake"),
   ("Fairway Pines at The Highlands",
    "Porter, Montgomery County, inside a 2,300-acre masterplan. Homes from $471,000, "
    "1,900 to 2,819 square feet.",
    "repeatable",
    "The same plan library again, in a second masterplan, which is what makes the "
    "library worth changing once.",
    "https://www.caldwellhomes.com/communities/the-highlands")],
  ["https://www.caldwellhomes.com/",
   "https://www.caldwellhomes.com/our-team",
   "https://www.caldwellhomes.com/communities",
   "https://www.caldwellhomes.com/communities/towne-lake",
   "https://www.caldwellhomes.com/communities/the-highlands",
   "https://caldwellcos.com/development/caldwell-homes/caldwell-homes",
   "https://www.constructiondive.com/news/caldwell-companies-launches-luxury-active-adult-homes-unit/436653/",
   "https://www.caldwellhomes.com/news/houston-area-2023-builder-rankings-list"],
  []),

 # First in the metro by permits and absent from the deck. It is also the only
 # firm on this deck that has already paid cash for a printed wall system: a
 # strategic investment in Apis Cor, announced March 2024. That fact sat in a
 # competitor profile and a timeline dot with no record attached to it.
 ("HOU-132", "D.R. Horton, Inc.", "Arlington HQ / Sugar Land, Richmond, Conroe",
  "https://www.drhorton.com/texas/houston",
  "372 Houston permits in August 2026, first in the metro",
  "The largest homebuilder in the United States by volume. 84,863 homes closed in "
  "the fiscal year to 30 September 2025 across 126 markets in 36 states, of which "
  "22,319 were in the South Central segment that holds Texas. Houston is named as a "
  "market in the annual report and no metro closings figure is published. Its own "
  "site listed 65 Houston-area communities and 668 standing homes, from $139,990 in "
  "Conroe to $878,600 in Pinehurst, sold under the D.R. Horton, Emerald Homes and "
  "Express Homes names. It owned 62 percent of Forestar Group at 30 September 2025, "
  "which sold 14,240 lots that year with 83 percent of them going to D.R. Horton. In "
  "March 2024 it made a strategic investment in Apis Cor, a manufacturer of "
  "construction 3D printing robots. No Houston division officer is published.",
  (3, 2, 3, 3),
  "It has already bought equity in a printed wall system, and it builds more houses "
  "in Houston than anyone else.",
  ("65 Houston communities and 668 standing homes at one time, on a national plan "
   "library.",
   "84,863 closings a year is far above the band one or two printers cover, so the "
   "first order is a pilot inside one division rather than a purchase.",
   "Strategic investment in Apis Cor, March 2024, amount undisclosed. It is the only "
   "equity position in a printed wall system on this deck."),
  [("Paul J. Romanowski", "President and Chief Executive Officer"),
   ("Michael J. Murray", "Executive Vice President and Chief Operating Officer"),
   ("Brad Conlon", "Senior Vice President of Business Development")],
  [("Apis Cor, March 2024",
    "Strategic investment in a manufacturer of construction 3D printing robots, "
    "announced 11 March 2024 by Apis Cor. Amount undisclosed. D.R. Horton issued no "
    "release of its own. Apis Cor named a multi-unit project in South Florida as the "
    "next step, after a new 3D printed wall system.",
    "method_risk",
    "It has already paid for a printed wall system. The incumbent has a name.",
    "https://www.prnewswire.com/news-releases/apis-cor-a-manufacturer-of-construction-3d-printing-robots-announces-strategic-investment-by-dr-horton-302084850.html"),
   ("Forestar Group",
    "62 percent owned at 30 September 2025. Forestar sold 14,240 lots in fiscal 2025, "
    "83 percent of them to D.R. Horton. Its Houston communities include Westland Ranch "
    "in League City, The Canopies in New Caney at 611 acres, and Fairwater in Magnolia.",
    "repeatable",
    "The lots and the houses are decided inside one group.",
    "https://www.forestar.com/communities/")],
  ["https://www.drhorton.com/texas/houston",
   "https://www.drhorton.com/texas/houston/inventory",
   "https://investor.drhorton.com/news-and-events/press-releases/2025/10-28-2025-103117295",
   "https://investor.drhorton.com/corporate-governance/executive-officers",
   "https://www.prnewswire.com/news-releases/apis-cor-a-manufacturer-of-construction-3d-printing-robots-announces-strategic-investment-by-dr-horton-302084850.html",
   "https://www.builderonline.com/building/d-r-horton-invests-in-3d-printing-robot-manufacturer-apis-cor_o",
   "https://blog.hbweekly.com/texas-homebuilding-leaders-august-2026/",
   "https://members.ghba.org/memberdirectory/Details/d-r-horton-americas-builder-emerald-homes-express-homes-755729"],
  []),

 # Twenty-fifth on the Builder 100 and three communities into Greater Houston.
 # Louisiana volume arriving in Texas, with no Texas officer on the record yet.
 ("HOU-134", "DSLD Homes", "Baton Rouge HQ / Bonney, Magnolia, Montgomery",
  "https://www.dsldhomes.com/",
  "3,989 closings in 2025, three Houston communities",
  "Production builder founded in Louisiana, ranked 25th on the 2026 Builder 100 with "
  "3,989 closings in 2025 and 4,116 in 2024. Of the 2025 figure, 3,642 were detached "
  "for sale and 347 were single-family build-to-rent. It describes itself as the "
  "largest privately held firm in its region, with more than 41,000 homes built and "
  "over 120 communities across Louisiana, southern Mississippi, Alabama, Tennessee, "
  "Texas and northwest Florida. Three Greater Houston communities: Aldean in Bonney "
  "at $264,990 to $319,990, Mostyn Springs in Magnolia at $239,990 to $325,990, and "
  "Two Step Farm in Montgomery at $348,990 to $485,990. No Texas or Houston division "
  "head is published.",
  (3, 2, 0, 3),
  "Three Houston communities opened out of a 120-community plan library, and a "
  "build-to-rent line inside it.",
  ("Three Houston communities drawn from a plan library that runs across six states.",
   "3,989 closings a year sits above the band one or two printers cover. The Houston "
   "division is three communities of it.",
   "Nothing on record. Its about page names energy efficiency and structural "
   "excellence and no method."),
  [("Saun Sullivan", "Chief Executive Officer")],
  [("The Houston entry",
    "Aldean in Bonney, Mostyn Springs in Magnolia and Two Step Farm in Montgomery. "
    "Three communities across Brazoria and Montgomery counties, $239,990 to $485,990.",
    "repeatable",
    "One plan library serving three counties out of one division.",
    "https://www.dsldhomes.com/communities/texas/houston"),
   ("The build-to-rent line",
    "347 of the 3,989 homes closed in 2025 were single-family build-to-rent.",
    "repeatable",
    "Rental product is held by the owner who pays to maintain it.",
    "https://www.builderonline.com/firms/dsld-homes/")],
  ["https://www.dsldhomes.com/",
   "https://www.dsldhomes.com/about-us",
   "https://www.dsldhomes.com/communities/texas/houston",
   "https://www.builderonline.com/firms/dsld-homes/"],
  []),

 # On-your-lot, which is the one production model with no subdivision behind it.
 # The plan set repeats and the sites do not. It carries its own construction
 # cost, so a method change needs no lender. Its wall specification is published,
 # and it is stick frame.
 ("HOU-135", "Tilson Home Corporation", "Houston / Spring, Katy, Willis, Angleton",
  "https://www.tilsonhomes.com/",
  "425 closings in 2024, 12 design centers in Texas",
  "Family-owned builder founded in Houston in 1932, building on land the buyer "
  "already owns. 425 closings in 2024 at $199 million, ranked 119th on the Builder "
  "100, against 745 closings and rank 75 in 2023. Twelve design centers across Texas, "
  "five of them on the Gulf Coast: Spring, Katy, Republic Grand Ranch in Willis, "
  "Angleton and Bryan. It carries the construction cost itself, stating it builds "
  "from 0 to 100 percent out of its own pocket with no interim construction loan and "
  "no draw schedule. It subcontracts the work, and says some of its subcontractors "
  "have built Tilson homes since 1962. The wall and foundation specification is "
  "published: post-tension slab engineered per site, 2x4 studs at 16 inches on "
  "center, full OSB wrap, open-cell spray foam. No construction or purchasing officer "
  "is published.",
  (3, 2, 0, 2),
  "One plan set repeated on scattered lots, and it funds its own construction, so a "
  "method change needs no lender.",
  ("One plan set sold from twelve design centers and built on lots the buyer already "
   "owns.",
   "425 closings a year sits inside the band one or two printers cover. The lots are "
   "scattered, so every house is a separate set-up.",
   "Nothing on record. It publishes its wall specification and it is stick frame."),
  [("Edward E. Martin Jr.", "Chief Executive Officer")],
  [("No construction loan",
    "The firm states it builds a home from 0 to 100 percent out of its own pocket, "
    "with no interim construction loan and no draw schedule.",
    "repeatable",
    "A method change needs no lender's sign-off on the collateral.",
    "https://www.tilsonhomes.com/blog/build-on-your-land-with-tilson-homes/"),
   ("The published specification",
    "Post-tension slab engineered per site, cables tensioned to 29,000 to 31,000 psi "
    "over a 28-day cure. Walls are 2x4 studs at 16 inches on center under a full OSB "
    "wrap, with open-cell spray foam to a third-party verified 3 ACH.",
    "method_risk",
    "It already engineers and pours concrete on every job, and the wall above it is "
    "framed.",
    "https://www.tilsonhomes.com/standard-features/")],
  ["https://www.tilsonhomes.com/",
   "https://www.tilsonhomes.com/about/",
   "https://www.tilsonhomes.com/where-we-build/",
   "https://www.tilsonhomes.com/standard-features/",
   "https://www.tilsonhomes.com/quality-construction/foundations/",
   "https://www.builderonline.com/firms/tilson-homes/",
   "https://members.texasbuilders.org/builder-directory/Details/tilson-home-corporation-726266"],
  []),

 # Detached rental at a size one or two printers cover, with the named
 # construction seat on the directory listing. The owner holds the house.
 ("HOU-136", "Clay Residential", "Houston / Cypress, Iowa Colony",
  "https://www.clayresidential.com/",
  "465 rental homes in two Houston communities",
  "Build-to-rent arm of Clay Development & Construction, a Houston industrial "
  "developer, formed as a new division in January 2022. It builds detached and "
  "attached rental homes under the Willow name and for-sale homes under its own. Two "
  "Greater Houston communities: Willow at Marvida in Cypress, 368 units split into "
  "134 detached homes and 234 attached villas at 1,382 to 2,900 square feet, "
  "completing 2026; and Willow at Sierra Vista in Iowa Colony, 97 detached rental "
  "homes at 1,548 to 1,980 square feet. At launch it stated a 2022 pipeline of 1,000 "
  "single-family and duplex rental homes across Houston, Austin, San Antonio and "
  "Dallas. No annual closings figure is published. The Greater Houston Builders "
  "Association lists it under Builder, Build-to-Rent.",
  (3, 3, 0, 2),
  "465 rental homes across two Houston communities, with the construction seat named "
  "on the record.",
  ("465 homes across two communities on three, four and five bedroom plans.",
   "Two communities and 465 homes sits inside the band one or two printers cover.",
   "Nothing on record. Its construction page names craftsmen, subcontractors and "
   "suppliers and no method."),
  [("Samuel Sanders", "Vice President of Construction Operations")],
  [("Willow at Marvida, Cypress",
    "368 units inside the 856-acre Marvida masterplan: 134 detached homes and 234 "
    "attached villas, three to five bedrooms at 1,382 to 2,900 square feet, "
    "completing 2026.",
    "repeatable",
    "234 attached villas repeat one wall assembly more times than any detached plan "
    "on this deck.",
    "https://rebusinessonline.com/clay-residential-breaks-ground-on-368-unit-single-family-rental-project-in-metro-houston/"),
   ("Willow at Sierra Vista, Iowa Colony",
    "97 detached rental homes at 1,548 to 1,980 square feet, three and four bedrooms, "
    "inside a Land Tejas community.",
    "repeatable",
    "Land Tejas is on this deck. The lot developer and the builder are both reachable.",
    "https://sierravistahouston.com/our-builders/clay-residential")],
  ["https://www.clayresidential.com/",
   "https://www.clayresidential.com/communities/",
   "https://www.clayresidential.com/construction/",
   "https://members.ghba.org/memberdirectory/Details/clay-residential-2924528",
   "https://rebusinessonline.com/clay-residential-breaks-ground-on-368-unit-single-family-rental-project-in-metro-houston/",
   "https://realtynewsreport.com/robert-clay-ventures-into-build-to-rent-single-family/"],
  []),
]


# Land developers. Same shape, different role: they sell lots and do not pour
# walls, so the second count reads No by construction. What they hold is the
# right to say a printer may work inside a community.
CHANNEL_ROWS = [

 # The deck already cites Wolf Ranch on the market tab and never named the party
 # that let it happen. Hillwood developed the community, and it runs three
 # masterplans in Greater Houston with a named Houston general manager.
 ("HOU-133", "Hillwood Communities", "Dallas HQ / Manvel, Pearland, League City",
  "https://www.hillwoodcommunities.com/",
  "Three Houston masterplans, 4,500 lots at build-out",
  "Residential land development arm of Hillwood, the Perot family company. Three "
  "Greater Houston master-planned communities: Pomona in Manvel, Valencia in Manvel "
  "at 440 acres and 938 single-family lots, and a 540-acre League City tract bought "
  "in May 2022 for 1,250 lots at $400,000 to $700,000. 4,500 lots across the three at "
  "build-out. Pomona took the Greater Houston Builders Association Prism award for "
  "Master-Planned Community of the Year in 2022 and 2023. Valencia's builders are "
  "Perry Homes, Coventry Homes and Pulte Homes. Hillwood Communities is also the "
  "developer of Wolf Ranch in Georgetown, where ICON and Lennar built the hundred-home "
  "Genesis Collection to a Bjarke Ingels Group design.",
  (3, 0, 3, 3),
  "It is the land developer of Wolf Ranch, and it runs three Houston masterplans with "
  "a Houston general manager named.",
  ("Three concurrent Houston masterplans and 4,500 lots at build-out.",
   "It develops lots and sells them to vertical builders. It does not pour walls.",
   "A hundred printed homes were built inside one of its own communities."),
  [("Fred Balda", "President"),
   ("Russell Bynum", "Senior Vice President, General Manager, Houston MSA"),
   ("Mark Meyer", "Senior Vice President, Planning and Innovation"),
   ("Patrick Cowden", "Senior Vice President, Development")],
  [("Wolf Ranch, Georgetown",
    "Hillwood Communities developed the community where ICON and Lennar built the "
    "Genesis Collection: 100 single-family houses on eight plans from 1,575 to 2,112 "
    "square feet, designed by Bjarke Ingels Group.",
    "method_risk",
    "A printer has already worked inside one of its communities, and it wrote about "
    "it on its own site.",
    "https://www.hillwoodcommunities.com/blog/the-future-of-housing-3d-printed-homes-in-georgetown-texas/"),
   ("Valencia, Manvel",
    "440 acres and 938 single-family lots on 40 to 70 foot homesites, $300,000 to "
    "$600,000. Builders are Perry Homes, Coventry Homes and Pulte Homes.",
    "repeatable",
    "Two of the three builders on this community are already on this deck.",
    "https://www.hillwood.com/newsroom/press-releases/hillwood-communities-expands-houston-footprint-announces-new-master-planned-community/")],
  ["https://www.hillwoodcommunities.com/",
   "https://www.hillwoodcommunities.com/leadership/",
   "https://www.hillwoodcommunities.com/texas-community-developer/",
   "https://www.hillwoodcommunities.com/blog/the-future-of-housing-3d-printed-homes-in-georgetown-texas/",
   "https://www.hillwood.com/newsroom/press-releases/hillwood-communities-expands-houston-footprint-announces-new-master-planned-community/",
   "https://www.builderonline.com/land/development/hillwood-communities-acquires-540-acres-for-third-master-plan-in-the-houston-area_o"],
  []),
]


# Production builders too large for one machine to matter, folded into the same
# section the deck already uses for them.
NATIONAL = {
    "HOU-132": "D.R. Horton", "HOU-134": "DSLD Homes",
}

# The land-developer line and the builders it puts on the ground.
CHANNEL = {
    "HOU-133": ("Pomona, Valencia and a 540-acre League City tract, 4,500 lots at "
                "build-out", ["Perry Homes", "Coventry Homes"]),
}

# Size for the grid's ordering only, where the firm publishes an annual closings
# figure that is not a Greater Houston figure. These stay off the closings chart,
# which compares firms at Houston scale.
SCALE = {
    "HOU-132": 84863,
    "HOU-134": 3989,
}

# The person who can change a wall specification, where the record names one.
DECIDERS = {
    ("HOU-130", "Dustin Rodgers"),
    ("HOU-131", "Kevin Johnson"),
    ("HOU-132", "Brad Conlon"),
    ("HOU-133", "Russell Bynum"),
    ("HOU-136", "Samuel Sanders"),
}

# Only where the seat says something the title does not.
DECIDER_NOTES = {
    "HOU-131": "Construction and purchasing sit with one person here, not two.",
}

PEOPLE_LINKS = {
    ("HOU-130", "Craig Jones"): (
        None, "https://www.builderonline.com/firms/long-lake-limited/", None),
    ("HOU-130", "Dustin Rodgers"): (
        "https://www.linkedin.com/in/dustin-rodgers-61a9908a/", None, None),
    ("HOU-130", "Dave Dronberger"): (
        "https://www.linkedin.com/in/dave-dronberger-9b098315/", None, None),
    ("HOU-130", "Aaron Alford"): (
        None, "https://wolffcompanies.com/news/in-off-market-deal-long-lake-buys-494-acres-next-to-bridgeland-for-new-community/",
        "Woodmere is Long Lake's own land arm, so this seat buys the ground the "
        "plans go on."),
    ("HOU-131", "Fred Caldwell"): (None, "https://www.caldwellhomes.com/our-team", None),
    ("HOU-131", "Peter Barnhart"): (None, "https://www.caldwellhomes.com/our-team", None),
    ("HOU-131", "Tim Mayo"): (None, "https://www.caldwellhomes.com/our-team", None),
    ("HOU-131", "Kevin Johnson"): (None, "https://www.caldwellhomes.com/our-team", None),
    ("HOU-131", "Anthony Moreno"): (None, "https://www.caldwellhomes.com/our-team", None),

    ("HOU-132", "Paul J. Romanowski"): (
        None, "https://investor.drhorton.com/corporate-governance/executive-officers",
        None),
    ("HOU-132", "Michael J. Murray"): (
        None, "https://investor.drhorton.com/corporate-governance/executive-officers",
        None),
    ("HOU-132", "Brad Conlon"): (
        None,
        "https://www.prnewswire.com/news-releases/apis-cor-a-manufacturer-of-construction-3d-printing-robots-announces-strategic-investment-by-dr-horton-302084850.html",
        "The seat that spoke for the company on the Apis Cor investment. He is not one "
        "of the four executive officers, so this sits below the officer tier."),

    ("HOU-133", "Fred Balda"): (
        None, "https://www.hillwoodcommunities.com/leadership/", None),
    ("HOU-133", "Russell Bynum"): (
        None, "https://www.hillwoodcommunities.com/leadership/", None),
    ("HOU-133", "Mark Meyer"): (
        None, "https://www.hillwoodcommunities.com/leadership/", None),
    ("HOU-133", "Patrick Cowden"): (
        None, "https://www.hillwoodcommunities.com/leadership/", None),

    ("HOU-134", "Saun Sullivan"): (
        None, "https://www.dsldhomes.com/about-us", None),

    ("HOU-135", "Edward E. Martin Jr."): (
        None, "https://www.builderonline.com/firms/tilson-homes/", None),

    ("HOU-136", "Samuel Sanders"): (
        None, "https://members.ghba.org/memberdirectory/Details/clay-residential-2924528",
        "Listed as the primary contact on the association's own member record."),
}

# Published annual closings, for the grid's ordering and the market chart.
CLOSINGS = {
    "HOU-130": (782, 782, 2025, "Builder 100 firm page"),
}
