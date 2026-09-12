# -*- coding: utf-8 -*-
"""What the audit round found, and what it changed.

Six independent passes were run against the cards, one batch each, with
instructions to assume the write-up was wrong until a source they opened
themselves said otherwise. Every URL on the deck was also checked for status.

The link check came back clean on the rules: no encyclopedia, no contact
aggregator, no constructed URL. The content pass did not come back clean.

Two people published on this deck as the person who can change a wall
specification have been dead for years. One firm was marked No on the count its
own evidence line answers Yes. One card said a firm does not pour walls while its
homebuilding division sat ten cards away in the A tier. One print time was
reported as seven days when the source says thirty hours.

Corrections are applied here rather than in the modules that hold the original
research, so the audit trail stays readable: the first draft is still in
data_*.py, and what a second look changed is here.

Findings that survived a check of the checker are not in this file. Two agent
findings were rejected: D.R. Horton's 62 percent of Forestar and the 83 percent
lot share are both verbatim in the FY2025 annual report, which the agent had not
opened.
"""

# ---------------------------------------------------------------- people

# Off the deck. A name that cannot be called is worse than no name.
DROP_PEOPLE = {
    # Died 22 November 2015. The obituary gives the same title the card carried.
    # https://www.dignitymemorial.com/obituaries/bellaire-tx/marilyn-vanderhider-6685972
    ("HOU-035", "Marilyn Vanderhider"),
    # Not on the firm's own leadership page, which names Shawn McAlpin as chief
    # executive and Cullen Burton as president.
    # https://burtonconstruction.com/leadership/
    ("HOU-116", "Brad Burton"),
    # Not on Wan Bridge's own leadership page, which lists seven people and no
    # construction or purchasing seat at all. Both names came from LinkedIn
    # headlines that attach to a different entity.
    #
    # An audit pass reported Derrick Hughes as the firm's Vice President of
    # Construction Operations and a fetch of wanbridge.com/leadership/derrick-hughes
    # returned a page saying so. That URL returns 404 and the name appears
    # nowhere in the leadership page's own markup. The finding was wrong, the
    # check of it was wrong, and no replacement is published here.
    ("HOU-001", "Randy Hutchinson"),
    ("HOU-001", "John Serra"),
    # Not on RSK's own team page, which lists nineteen people and three
    # construction directors. No Vice President of Construction exists there.
    ("HOU-044", "Gregg Erickson"),
    # Not on Hanover's leadership page, which enumerates its construction group.
    ("HOU-029", "Mark Wood"),
    # Neither is on M.L. Deer's own team page. The firm publishes no EVP and no
    # chief operating officer.
    ("HOU-119", "Jeff Raymer"),
    ("HOU-119", "Todd Riedel"),
    # Named once, in an April 2022 appointment release. Howard Hughes's current
    # Texas page routes the Houston seat to Jim Carman, who is already on the card.
    ("HOU-011", "Stephen Sams"),
}

# On the deck, from the firm's own page.
PEOPLE = {
    ("HOU-001", "Danting Li"): (
        "Chief Operating Officer and Co-Founder",
        "https://wanbridge.com/leadership/", None),
    ("HOU-001", "Keith Clipp"): (
        "Executive Vice President, Development and Operations",
        "https://wanbridge.com/leadership/",
        "The closest published seat to construction. Wan Bridge names seven "
        "leaders and none of them holds construction or purchasing."),
    ("HOU-001", "Kyle Spicer"): (
        "Senior Vice President of Land Acquisition",
        "https://wanbridge.com/leadership/", None),
    ("HOU-044", "Jim Foy"): (
        "Houston Director of Construction",
        "https://rskrealestatepartners.com/our-team/", None),
    ("HOU-044", "Corey Wilson"): (
        "Regional Director of Construction",
        "https://rskrealestatepartners.com/our-team/", None),
    ("HOU-044", "Kevin Calderon"): (
        "Purchasing Manager",
        "https://rskrealestatepartners.com/our-team/", None),
    ("HOU-116", "Cullen Burton"): (
        "President", "https://burtonconstruction.com/leadership/", None),
    ("HOU-119", "Marc Deer"): (
        "Managing General Partner", "https://www.mldeer.com/our-team", None),
    ("HOU-119", "Richard Rolland"): (
        "Managing General Partner", "https://www.mldeer.com/our-team", None),
    ("HOU-119", "Jack Baker"): (
        "Senior Project Manager, ML Deer Construction",
        "https://www.mldeer.com/our-team",
        "The only construction-side name the firm publishes."),
    ("HOU-035", "Kionta Carter"): (
        "Chief Programs Officer", "https://avenuecdc.org/about-us/board-staff/",
        None),
    ("HOU-035", "Angela Guerrero"): (
        "Director, Asset Management and Realty Services",
        "https://avenuecdc.org/about-us/board-staff/",
        "The closest published seat to how the houses get built. Avenue names no "
        "construction officer."),
}

DECIDER = {
    ("HOU-044", "Jim Foy"): True,
    ("HOU-116", "Cullen Burton"): True,
}

RETITLE = {
    # Wan Bridge's own leadership page titles him Co-Founder. The chief-executive
    # wording came from a LinkedIn headline and attached to a different entity.
    ("HOU-001", "Ting Qiao"): "Co-Founder",
    # Elected 2026-2027 President of the American Concrete Institute, and titled
    # vice president and general manager in the same trade report.
    ("HOU-101", "Scott Anderson"):
        "Vice President and General Manager, Keystone Structural Concrete",
    # Signorelli's own bio page. No source gives him a chief-executive title at
    # First America; Danny Signorelli holds that at the parent.
    ("HOU-007", "John Winniford"): "President, Homebuilding",
}

# ---------------------------------------------------------------- records

KEY_STAT = {
    "HOU-016": "23 of 26 planned homes to be printed, one under way",
    "HOU-078": "Owned by Rausch Coleman, which Lennar bought in February 2025",
    "HOU-039": "Sunterra in Katy, eighteen builders inside it",
    "HOU-040": "Fifteen concurrent Houston masterplans",
    "HOU-041": "Towne Lake and The Highlands, more than 4,000 homes at The "
               "Highlands alone",
    "HOU-133": "Three Houston masterplans, 700 acres at Legacy alone",
}

SCORE = {
    # The card marked No on the count its own evidence line answers. It financed
    # and opened Greater Houston's first mass timber office building.
    "HOU-011": {"innovation": 3},
    # It sells lots and it also builds, through Caldwell Homes, which is on this
    # deck under its own name.
    "HOU-041": {"machine_fit": 2},
    # The cited Kinder Institute piece is a 2017 opinion piece on transit-oriented
    # development. It says nothing about a building method.
    "HOU-035": {"innovation": 0},
    # Hillwood developed the land at Wolf Ranch. Lennar bought the printing.
    "HOU-133": {"innovation": 2},
    # The count read Partly off a page that returns 404. With the page gone the
    # record is empty.
    "HOU-078": {"innovation": 0},
    # The deck states a rule on the machine-fit bands: a firm with no published
    # figure is a Partly. Fourteen reasons say that sentence and five of them sat
    # under a Yes. The rule wins.
    "HOU-119": {"machine_fit": 2},
    "HOU-105": {"machine_fit": 2},
    "HOU-107": {"machine_fit": 2},
    "HOU-110": {"machine_fit": 2},
    "HOU-111": {"machine_fit": 2},
    # Third-party energy certification and no structural method is the same
    # evidence Caldwell Homes carries, and that record reads Partly. The same
    # evidence has to earn the same mark.
    "HOU-067": {"innovation": 2},
}

WHY = {
    "HOU-011": (
        "Three communities on one metro's edge, 1,802 residential acres still to "
        "sell.",
        "It sells finished lots. The builder who buys them buys the wall.",
        "It financed and opened Greater Houston's first mass timber office "
        "building, with low-carbon concrete in the same structure."),
    "HOU-041": (
        "The Highlands alone carries more than 4,000 planned homes across "
        "thirteen builders, and Towne Lake is a second community.",
        "It sells lots, and through Caldwell Homes it also builds. The wall "
        "decision exists inside the group.",
        "Caldwell Companies publishes no construction-method content. Caldwell "
        "Homes, its own division, is screened separately on this deck."),
    "HOU-035": (
        "Five developments in one neighbourhood since 2002.",
        "Five affordable developments in one neighbourhood, at a scale one "
        "machine covers.",
        "Nothing on record. The resilience reading came from a 2017 Rice Kinder "
        "Institute piece about transit-oriented development, which says nothing "
        "about how anything is built."),
    "HOU-133": (
        "Three concurrent Houston masterplans, 700 acres at Legacy alone.",
        "It develops lots and sells them to vertical builders. It does not pour "
        "walls.",
        "A hundred printed homes were built inside one of its own communities. "
        "Hillwood developed the ground. Lennar bought the printing."),
    "HOU-039": (
        "Sunterra carries eighteen builders inside one community.",
        "It sells lots. Eighteen builders buy the wall.",
        "Nothing on record about construction method."),
    "HOU-040": (
        "Fifteen concurrent Houston masterplans, by its own count.",
        "It sells lots and does not pour walls.",
        "Johnson Development publishes no construction-method content."),
    "HOU-016": (
        "23 of 26 planned homes at one address, on one printer.",
        "Twenty-six homes on one site is inside the band one machine serves.",
        "It is printing now. The first home was under construction in April 2026 "
        "and none is finished."),
    "HOU-078": (
        "One confirmed community, Tavola in New Caney. The footprint is small.",
        "No volume figure is published for the Houston operation.",
        "Nothing on record. The energy-product claims this card used to carry came "
        "from a page that no longer exists."),
    "HOU-067": (
        "Twelve submarkets is wide for a builder this size, which spreads the "
        "plan set thin.",
        "No closings figure is published anywhere, so the machine question cannot "
        "be sized.",
        "It has paid for above-code performance, Energy Star and Environments for "
        "Living certification with whole-home dehumidifiers standard, but nothing "
        "structural."),
    "HOU-044": (
        "156 and 210 units on two Katy sites about a mile apart.",
        "Two projects and no published unit count beyond them. The firm publishes "
        "three construction directors and a purchasing manager.",
        "No method evidence found."),
    "HOU-119": (
        "Commercial buildings across the Gulf Coast. The structures differ project "
        "to project.",
        "No revenue, crew count or project count is published. On the bands, a "
        "firm with no published figure is a Partly.",
        "It carries insulated concrete form construction in its standard menu "
        "alongside tilt-wall and masonry, so it has sold and built a concrete wall "
        "system rather than only a wood one. No named project is published to "
        "date it."),
    "HOU-017": (
        "One duplex. Two units.",
        "One duplex. Proof the method works in the city limits, not a volume "
        "that keeps a machine busy.",
        "It is printing now. Construction started March 2026 and no completion "
        "is published."),
}

SYNOPSIS = {
    "HOU-011":
        "NYSE-listed master-planned community developer, headquartered inside The "
        "Woodlands, running three Greater Houston communities: The Woodlands, "
        "Bridgeland at 11,500 acres in Cypress, and The Woodlands Hills at 2,000 "
        "acres in Conroe and Willis. It sells finished lots to builders and does "
        "not build houses. 1,802 residential acres remain across the three as of "
        "June 30, 2026: 1,142 at Bridgeland, 597 at The Woodlands Hills and 63 at "
        "The Woodlands. It expects The Woodlands to sell out in 2031, Bridgeland "
        "in 2032 and The Woodlands Hills in 2035. Company-wide it sold 621 "
        "residential acres in 2025 at an average $890,000 an acre. Bridgeland sold "
        "812 new homes in 2025, eleventh in the country. It developed One "
        "Bridgeland Green, Greater Houston's first mass timber office building, "
        "framed in dowel-laminated and cross-laminated timber with low-carbon "
        "concrete, topped out December 2024 and opened November 2025. Pershing "
        "Square took 46.9 percent in May 2025.",

    "HOU-041":
        "Land developer of Towne Lake in Cypress and The Highlands in Porter, the "
        "latter 2,300 acres with more than 4,000 planned homes across thirteen "
        "builders. It sells lots, and it also builds: Caldwell Homes is its own "
        "homebuilding division and is screened separately on this deck. Caldwell "
        "Companies publishes no construction-method content of its own.",

    "HOU-039":
        "Develops lots and sells them to builders. Sunterra in Katy carries "
        "eighteen builders on its own builder page, the largest single roster "
        "screened, and eleven of them are on this deck. Starwood Capital took a "
        "majority interest on December 29, 2021. Sunterra's acreage is published "
        "as 2,303 in the 2021 announcement and 1,039 on Land Tejas's own community "
        "page, and the two have not been reconciled.",

    "HOU-040":
        "Land developer running fifteen concurrent Houston-area masterplans by its "
        "own count, including Sienna and Cross Creek West. Channel value is high "
        "and direct wall purchasing is nil. Johnson Development publishes no "
        "construction-method content.",

    "HOU-133":
        "Residential land development arm of Hillwood, the Perot family company. "
        "Three Greater Houston master-planned communities: Pomona in Manvel; "
        "Valencia in Manvel, 440 acres and 938 single-family lots on 45 to 70 foot "
        "homesites from the $300s to the $800s, with Beazer Homes, Coventry Homes, "
        "Perry Homes and Pulte Homes building; and Legacy in League City, more "
        "than 700 acres from $400,000 to above $1 million, with ten builders "
        "including Coventry Homes, David Weekley Homes, Partners in Building, "
        "Perry Homes and Westin Homes. Pomona took the Greater Houston Builders "
        "Association Prism award for Master-Planned Community of the Year in 2022 "
        "and 2023. Hillwood Communities is also the developer of Wolf Ranch in "
        "Georgetown, where ICON and Lennar built the hundred-home Genesis "
        "Collection to a Bjarke Ingels Group design.",

    "HOU-035":
        "Nonprofit community development corporation building affordable homes "
        "since 1991 and operating in Houston's Near Northside since 2002, with "
        "five named developments in the neighbourhood. The City of Houston "
        "contributed $3.4 million toward the $11.8 million acquisition and "
        "rehabilitation of the Avenue Center. Avenue publishes no construction "
        "officer.",

    "HOU-016":
        "Builder of Gulf Shore Estates in San Leon, roughly 40 miles southeast of "
        "downtown Houston, where 23 of 26 planned homes are to be 3D printed in "
        "partnership with HiveASMBLD. The first home was under construction in "
        "April 2026 at about 1,850 square feet and $385,000, with three bedrooms, "
        "two bathrooms and a 250 square foot garage. None is finished. Commander "
        "Home Builders is currently building with HiveASMBLD, a Houston "
        "competitor. The timeline and cost-savings figures are the owner's own "
        "statements and are not independently verified.",

    "HOU-017":
        "Builder of Avenue J, a two-unit 3D-printed duplex in Houston's East End "
        "of roughly 1,727 square feet per unit priced at $365,000 each, built in "
        "partnership with HiveASMBLD. Construction started March 2026 against a "
        "June 2026 move-in target. The printer's own project page still lists it "
        "as started, and no completion is published. Elpis 3D Home Builders is "
        "currently building with HiveASMBLD.",

    "HOU-002":
        "Builder and developer of Zuri Gardens, an 80-home community on 13 acres "
        "near Hobby Airport in southeast Houston, built with 3D-printed "
        "construction in partnership with Houston construction-technology firm "
        "HiveASMBLD and Green Cement of Jewett, Texas. The houses are hybrid: the "
        "ground floor is printed concrete and the second storey is engineered "
        "wood, so the printed scope is the lower level rather than the whole "
        "house. Homes priced in the mid to high $200,000s. Cole Klein Builders is "
        "currently building with HiveASMBLD, a Houston-based competitor. There is "
        "no person called Cole Klein. The firm's own about page names Vanessa Cole "
        "and Harry Klein as its founders, so the company name joins the two "
        "surnames.",

    "HOU-065":
        "Family builder founded in 1982 in College Station, running an even-flow "
        "production model that releases a fixed number of starts a week rather "
        "than reacting to sales. HousingWire reports 973 homes and $310 million in "
        "2025, up 17 percent. In the same June 2026 interview its chief executive "
        "described the firm's decision to exit the Houston metro two to three "
        "years earlier as an example of its discipline. It still lists inventory "
        "at Ladera Creek in Conroe, inside the metro, and its North Houston "
        "communities are in Huntsville, outside it. Read the record as a "
        "Bryan-College Station builder with a Conroe tail, not a Houston builder.",

    "HOU-045":
        "Production builder headquartered in Spring, selling across five Texas "
        "regions, with a builder role at Sienna. Sekisui House of Japan bought "
        "Chesmar on 10 June 2022 for about $514 million. On 4 September 2025 "
        "Sekisui announced consolidating M.D.C. Holdings, Woodside, Holt and "
        "Chesmar into one company. Builder Magazine reported on 12 January 2026 "
        "that under that realignment Woodside, Chesmar and Holt will be absorbed "
        "into the unified entity and will no longer operate as distinct brands, "
        "and that certain Chesmar entities will be liquidated and merged. Chesmar "
        "publishes no Houston community unit counts and no construction-method "
        "content, and no change to its method is on record.",

    "HOU-007":
        "Homebuilding division of The Signorelli Company, ranked 75th on the 2026 "
        "Builder 100 list. Announced plans on August 6, 2026 to deliver more than "
        "1,300 single-family homes across 14 new Texas communities, including the "
        "359-home Azalea District at Valley Ranch priced from the $300,000s. The "
        "parent published the volume figure: 750 homes sold in 2025, against 540 "
        "in 2024. Publishes its wall assembly as a marketing position: advanced "
        "framing at 16 inch on-centre spacing using up to 30 percent more lumber, "
        "in its own words. John Winniford became president of First America on 17 "
        "September 2025 and holds the title President, Homebuilding at Signorelli, "
        "the parent. He ran Gehan, then Brightland, as president and chief "
        "executive for nearly a decade and delivered more than 22,000 homes from "
        "2016.",

    "HOU-073":
        "Clayton Properties Group builder, part of Berkshire Hathaway, that "
        "entered Houston by acquiring HistoryMaker Homes' Houston division and now "
        "sells across the north, west and south suburbs. Its own site publishes an "
        "average build time of three and a half months, qualified there as an "
        "average across all communities and product types as of 2025, not a "
        "Houston figure. It has stated a target of 1,000 homes a year in the "
        "Houston area within five years. Where Houston purchasing sits, local or "
        "national, is not published.",

    "HOU-015":
        "Privately held land developer with more than 16 master-planned "
        "communities and over 23,000 paper lots in pipeline as of August 6, 2026. "
        "Developer of Austin Point in Rosenberg, roughly 14,000 planned homes on "
        "4,700 acres, announced September 22, 2023. Valley Ranch, a 1,400-acre "
        "community in New Caney in Montgomery County, carries more than 2,000 "
        "single-family homes and 1,000 multifamily units alongside 2.55 million "
        "square feet of retail. John Winniford holds the title President, "
        "Homebuilding at Signorelli and is also president of First America Homes. "
        "Signorelli itself names a commercial-division construction manager and "
        "land-development managers.",

    "HOU-078":
        "Green-building focused production builder selling at Tavola in New Caney. "
        "GreenEco was acquired by Rausch Coleman Homes in 2020, and Lennar "
        "completed its purchase of Rausch Coleman on 10 February 2025, naming "
        "Houston among the markets added. Lennar built the hundred-home Wolf Ranch "
        "community with ICON, so the relationship exists at corporate level. "
        "GreenEco's own domain no longer resolves to a site.",

    "HOU-001":
        "Houston-headquartered build-to-rent developer operating since 2016 across "
        "Houston, Austin and Dallas. Announced five new Texas build-to-rent "
        "projects on March 12, 2025, including Canvas on Founders Hill in Fulshear "
        "and Eldridge Tower in Houston. Held five projects under way with five to "
        "seven more in the pipeline as of April 10, 2025. Its leadership page "
        "names seven people and none of them holds construction or purchasing, so "
        "the seat that would specify a wall is not published.",

    "HOU-126":
        "Architect-founded modular builder on Clinton Drive producing factory-built "
        "homes, accessory dwelling units and hospitality units, with a published "
        "product line and starting prices from $99,000 for the smallest accessory "
        "unit. Its own site names no individual.",
}

# greenecobuilders.com redirects to a parked-domain lander. A website button
# that opens a parking page is worse than no button, so the record carries none.
DROP_HOMEPAGE = {"HOU-078"}

# ---------------------------------------------------------------- evidence

DROP_PROJECTS = {
    # Its only source returns 404, and with it the roof-decking figure.
    ("HOU-078", "Tavola"),
    # Superseded by Hillwood's own live community page: a fourth builder, wider
    # homesites and a higher band.
    ("HOU-133", "Valencia, Manvel"),
    # The count and the square footage are not on the page this cited. They are
    # in the launch report, which the record already carries.
    ("HOU-136", "Willow at Sierra Vista, Iowa Colony"),
    # The cited article is dated November 2024 and the deal is not dated in it.
    ("HOU-130", "Woodmere Development Co."),
    # "LoMa" is the material, not the name of the house, and the figures in this
    # item were wrong in both directions. Replaced below.
    ("HOU-128", "LoMa house"),
}

# An evidence item whose only link is dead keeps the fact and moves to a page
# that resolves.
EDIT_PROJECT_URL = {
    ("HOU-006", "The Mill"): "https://www.tritenre.com/about",
}

# The same community, two acreages, on one card. The deck's rule is that both
# numbers appear and the disagreement is stated.
EDIT_PROJECT_DETAIL = {
    ("HOU-011", "Bridgeland"):
        "Cypress, Harris County. 11,400 acres in the ULI case study and 11,500 in "
        "the firm's current releases, a difference it has not reconciled. "
        "Construction begun October 2003, home sales from 2006, roughly 65,000 "
        "residents projected at 2037 buildout.",
}

PROJECTS = {
    "HOU-128": [
        ("100 West Bolt Street, Fort Worth",
         "Tarrant County. A 40 foot by 40 foot house whose walls printed in under "
         "30 hours in May 2024 on a Black Buffalo 3D NEXCON printer. Seven to "
         "eight days covered the whole house. Boxer Property is the partner on "
         "the project; the printing contractor is the developer.",
         "method_risk",
         "The firm has already paid to watch a wall go up without a framing crew.",
         "https://candysdirt.com/2024/05/28/you-can-see-a-3d-printed-home-get-built-in-fort-worth-right-now/")],
    "HOU-101": [
        ("American Concrete Institute presidency",
         "Scott Anderson, vice president and general manager of Keystone "
         "Structural Concrete, was elected 2026-2027 president of the American "
         "Concrete Institute, reported 10 April 2026.",
         "method_risk",
         "The seat that would place a printed wall in Houston also chairs the "
         "body that writes the concrete code.",
         "https://concreteproducts.com/index.php/2026/04/10/keystone-structural-vp-gm-anderson-elected-aci-president/")],
    "HOU-133": [
        ("Valencia, Manvel",
         "440 acres and 938 single-family lots on 45 to 70 foot homesites, from "
         "the $300s to the $800s. Builders are Beazer Homes, Coventry Homes, "
         "Perry Homes and Pulte Homes.",
         "repeatable",
         "Two of these four builders are on this deck.",
         "https://www.valenciabyhillwood.com/new-homes/"),
        ("Legacy, League City",
         "More than 700 acres, new home prices from $400,000 to above $1 million, "
         "with ten builders: Beazer Homes, Coventry Homes, David Weekley Homes, "
         "Drees, Highland Homes, Partners in Building, Perry Homes, Shea Homes, "
         "Village Builders and Westin Homes.",
         "repeatable",
         "Four of these ten builders are on this deck.",
         "https://www.hillwoodcommunities.com/lifestyle-communities/legacy/")],
    "HOU-136": [
        ("Willow at Sierra Vista",
         "97 single-family rental homes in a Land Tejas community south of "
         "Houston, first homes from spring 2022, stated at launch.",
         "repeatable",
         "Land Tejas is on this deck. The lot developer and the builder are both "
         "reachable.",
         "https://realtynewsreport.com/robert-clay-ventures-into-build-to-rent-single-family/")],
    "HOU-130": [
        ("Woodmere Development Co.",
         "The firm's own land arm. 95 acres at Decker Prairie-Rosehill Road in "
         "Montgomery County, bought from the Brautigam family and reported in "
         "November 2024. 494 acres beside Bridgeland in 2022.",
         "repeatable",
         "It owns the ground it builds on, so a method change does not need a "
         "land developer's approval first.",
         "https://therealdeal.com/texas/houston/2024/11/25/long-lake-purchased-100-acre-tract-in-houston-area/")],
    "HOU-035": [
        ("Avenue Center, Near Northside",
         "The City of Houston contributed $3.4 million toward the $11.8 million "
         "acquisition and rehabilitation of the Avenue Center, announced 20 May "
         "2022.",
         "repeatable",
         "A rehabilitation, not a ground-up build, so it says nothing about how "
         "Avenue puts up a wall.",
         "https://houstontx.gov/housing/communication/2022/0520b.html")],
}

SOURCES = {
    "HOU-128": ["https://candysdirt.com/2024/05/28/you-can-see-a-3d-printed-home-get-built-in-fort-worth-right-now/"],
    "HOU-101": ["https://concreteproducts.com/index.php/2026/04/10/keystone-structural-vp-gm-anderson-elected-aci-president/"],
    "HOU-133": ["https://www.hillwoodcommunities.com/lifestyle-communities/legacy/",
                "https://www.valenciabyhillwood.com/new-homes/"],
    "HOU-035": ["https://houstontx.gov/housing/communication/2022/0520b.html",
                "https://avenuecdc.org/about-us/board-staff/"],
    "HOU-065": ["https://www.housingwire.com/articles/stylecraft-builders-margin-pace-and-growth/"],
    "HOU-045": ["https://www.builderonline.com/builder-100/strategy/sekisui-house-finalizes-u-s-rebrand-after-m-d-c-holdings-acquisition/"],
    "HOU-039": ["https://sunterratx.com/homebuilders/"],
    "HOU-040": ["https://www.johnsondevelopment.com/mpc_houston"],
    "HOU-041": ["https://caldwellcos.com/development/caldwell-homes/caldwell-homes"],
    "HOU-016": ["https://www.galvnews.com/news/printing-the-future-san-leon-project-tests-new-model-for-coastal-housing/article_e6c622f8-f6cd-47f6-ad36-ed1cac45a3d4.html"],
    "HOU-001": ["https://wanbridge.com/leadership/"],
    "HOU-044": ["https://rskrealestatepartners.com/our-team/"],
    "HOU-116": ["https://burtonconstruction.com/leadership/"],
    "HOU-119": ["https://www.mldeer.com/our-team"],
    "HOU-015": ["https://www.signorellicompany.com/valley-ranch"],
    "HOU-126": ["https://urbanland.uli.org/development-and-construction/top-down-construction-mass-timber-and-nanotechnology-reshape-building"],
}

# A source that turned out not to say what it was cited for, or that is gone.
DROP_SOURCES = {
    # 404. The Mill keeps its own about-page source.
    ("HOU-006", "https://tritenre.com/news/this-historic-reuse-project-shows-the-latest-ways-timber-and-offices-are-changing-industrial-areas"),
    # 404.
    ("HOU-109", "https://tandtconstruction.com/taylormade/"),
    # 404. It carried the headline figure and the whole track-record reading.
    ("HOU-078", "https://www.har.com/blog_27737"),
    # A parked domain.
    ("HOU-078", "https://greenecobuilders.com/"),
    # The category search, not the firm's member record.
    ("HOU-130", "https://members.ghba.org/memberdirectory/Search/builder-single-family-132864"),
    # A 2017 opinion piece on transit-oriented development, cited for a method.
    ("HOU-035", "https://kinder.rice.edu/urbanedge/harvey-be-turning-point-equitable-transit-oriented-development-houston"),
    # Does not mention Aura Dwellings or its founder.
    ("HOU-126", "https://www.greenbuildermedia.com/blog/prefab-3d-modular-panels-built-for-tough-houston-weather"),
}
