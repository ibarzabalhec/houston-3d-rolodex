# -*- coding: utf-8 -*-
"""Build 67. Every figure on a card, traced to a page.

figures.py listed 162 figures that were on no page their card cites. Five
readers took eight cards each and traced every one. Most were on the cited page
and the script could not see them: a Cloudflare challenge, a script-rendered
page, a price written "$370s", a percentage written "17.0%". Those are now
registered in figures.py as hand readings. The rest were one of four things, and
each is corrected here:

  a figure from a page the card did not cite   the page is added
  a sum presented as published                 the parts are printed beside it
  a figure the page contradicts                the page's figure replaces it
  a figure nothing publishes                   it is cut

Several cards also said something a cited page does not: a county, an
acquisition date, a founding history, a division that is no longer listed. Those
are fixed in the same pass.

The same pass fixed the headline figures that were not Houston figures. A
headline that counts closings now says whose: Houston, company-wide, or the
markets the figure covers. build.py fails on a closings headline that does not.
"""

# ---------------------------------------------------------------- off the deck
# A firm whose own chief executive says it left Greater Houston is not a Greater
# Houston prospect. It stays in the workbook with the reason.
OFF_DECK = {
    "HOU-065": "Off the deck: its chief executive said in June 2026 that Stylecraft "
               "exited the Houston metro two to three years earlier. It still lists "
               "homes at Ladera Creek in Conroe.",
}

# ------------------------------------------------------------- sources added
SOURCES = {
    "HOU-045": ["https://www.globenewswire.com/news-release/2022/06/10/2460684/0/en/"
                "Sekisui-House-Japan-s-Leading-Homebuilder-and-Diversified-Developer-"
                "Announces-Agreement-to-Acquire-Chesmar-Homes-of-Texas.html"],
    "HOU-008": ["https://www.fool.com/earnings/call-transcripts/2026/04/23/"
                "meritage-homes-mth-q1-2026-earnings-transcript/"],
    "HOU-062": ["https://lagomarintexascity.com/tricoast-homes-joins-the-fun-in-lago-mar/",
                "https://www.tricoasthomes.com/communities"],
    "HOU-083": ["https://braunenterprises.com/retail-houston/"],
    "HOU-039": ["https://www.chron.com/news/houston-texas/article/"
                "katy-sunterra-development-18649587.php",
                "https://landtejas.com/historical/sunterra/"],
    "HOU-081": ["https://houston.org/news/new-10-block-mixed-use-development-"
                "revitalize-eado-neighborhood/"],
    "HOU-073": ["https://therealdeal.com/texas/houston/2025/12/30/"
                "brohn-homes-plants-flag-in-houston-with-historymaker-deal/"],
    "HOU-022": ["https://www.daiwahouse.com/English/about/release/pdf/release_20210810e.pdf",
                "https://www.housingwire.com/articles/"
                "daiwa-house-dials-in-texas-400m-for-80-of-castlerock/"],
    "HOU-075": ["https://www.builderonline.com/builder-100/strategy/"
                "new-home-co-and-landsea-homes-unite-as-risewell-homes-following-merger/"],
    "HOU-147": ["https://investors.bldr.com/news/news-details/2026/"
                "Builders-FirstSource-Reports-First-Quarter-2026-Results/default.aspx"],
    "HOU-080": ["https://kinder.rice.edu/urbanedge/plant-second-ward-walkable-houston-east-end",
                "https://www.houstonchronicle.com/business/real-estate/article/"
                "Exclusive-Axelrad-developers-East-End-17291259.php"],
    "HOU-034": ["https://www.housingwire.com/articles/"
                "sumitomos-timber-complex-sharpens-its-edge-of-integration/"],
    "HOU-030": ["https://www.frpltd.com/blog/fidelis-to-develop-280000-square-foot-"
                "alvin-marketplace-along-future-grand-parkway-segment",
                "https://www.frpltd.com/about-fidelis/mission-values"],
    "HOU-007": ["https://www.signorellicompany.com/press/775/"
                "first-america-homes-rises-to-no-75-on-prestigious-builder-100-list",
                "https://www.signorellicompany.com/our-leadership/34/john-winniford"],
    "HOU-061": ["https://www.conroenews.org/article/local-builder-bets-on-willis-and-"
                "montgomery-as-affordability-reshapes-texas-housing"],
    "HOU-069": ["https://houstonagentmagazine.com/2020/02/06/making-moves-newmark-homes-"
                "appoints-top-leaders-edward-jones-becomes-latest-tenant-bridgeland/",
                "https://newmarkhomes.com/floorplans/houston"],
    "HOU-132": ["https://investor.drhorton.com/~/media/Files/D/D-R-Horton-IR/documents/"
                "quarterly-reports/2025-dhi-annual-report.pdf"],
    "HOU-011": ["https://www.sec.gov/Archives/edgar/data/1981792/000162828026009701/"
                "hhhearningsreleaseq42025.htm",
                "https://communityimpact.com/houston/cypress/development/2025/11/25/"
                "howard-hughes-opens-nearly-50000-square-foot-office-in-bridgeland/"],
    "HOU-044": ["https://communityimpact.com/houston/katy-fulshear/development/2025/12/11/"
                "rsk-real-estate-partners-to-construct-2nd-build-to-rent-community-in-katy/"],
    "HOU-006": ["https://www.tritenre.com/portfolio/the-landing-at-aliana"],
    "HOU-134": ["https://www.dsldhomes.com/communities/texas/houston/aldeana",
                "https://www.dsldhomes.com/communities/texas/houston/two-step-farm"],
    "HOU-021": ["https://www.dinersteincos.com/about-us"],
    # NAPCO's own domain has returned 404 on every page since 24 September 2026.
    # Its investor's portfolio page still lists it and links the domain.
    "HOU-145": ["https://www.mainstcapital.com/portfolio-companies/lower-middle-market/"
                "lower-middle-market-current/detail/5484/napco-precast"],
}

# A cited page that supports nothing on the card. Stylecraft's Builder spotlight
# is a May 2015 article about 2014.
DROP_SOURCES = {
    "HOU-065": ["https://www.builderonline.com/builder-100/leadership/"
                "builder-100-spotlight-stylecraft-builders_o"],
}

# A project row pointing at a page that does not carry the project.
PROJECT_URL = {
    ("HOU-075", "https://risewellhomes.com/team"):
        "https://risewellhomes.com/texas/houston-new-homes/neighborhoods/sunterra",
    ("HOU-006", "https://www.tritenre.com/about"):
        "https://www.tritenre.com/portfolio/the-landing-at-aliana",
}

# A person whose cited page no longer says what the card said it says.
PERSON = {
    ("HOU-075", "Jennifer Keller, P.E."): {
        "role": "Division President",
        "li_evidence": "Indexed title reads Jennifer Keller, P.E., Division President, "
                       "Risewell Homes. The firm's team page listed her as Houston Division "
                       "President on 12 September 2026, and on 24 September lists ten "
                       "division presidents and no Houston division.",
        "source_url": None,
    },
}

# ---------------------------------------------------------------- headlines
KEY_STAT = {
    "HOU-022": "1,465 closings company-wide in 2025",
    "HOU-068": "1,062 closings and $621 million in 2025, Houston and Austin together",
    "HOU-069": "483 closings and $306 million in 2025, Houston and Austin together",
    "HOU-135": "425 closings in 2024 across Texas, 12 design centers",
    "HOU-134": "3,989 closings company-wide in 2025, three Houston communities",
    "HOU-007": "1,300+ homes planned across 14 new Texas communities",
    "HOU-020": "$7.5B invested company-wide since 1991",
    "HOU-034": "110 communities and 17,000+ homes company-wide at its 2023 rename",
    "HOU-073": "Average build time of 3.5 months, company-wide",
    "HOU-061": "45 closings in 2025, all in Montgomery County, 70 planned for 2026",
    "HOU-062": "Nine floor plans across nine communities",
    "HOU-067": "Volume Builder of the Year, ten communities",
    "HOU-039": "Sunterra in Katy, eighteen builder names on its own page",
    "HOU-018": "$3.1B owned assets, 12M sf managed",
    "HOU-075": "The 2025 merger of Landsea Homes and The New Home Company",
    "HOU-136": "465 rental homes in two Houston communities, 368 and 97",
}

# A closings headline must say whose closings. These say it another way.
CLOSINGS_WAIVER = {
    "HOU-064": "every community on its own site is in Greater Houston",
    "HOU-130": "every community on its own site is in Greater Houston",
    "HOU-074": "Devon Street built only in Houston",
}

# A closings figure on the Market chart that counts more than Greater Houston.
# The bar keeps its figure, and the chart marks it and says what it covers.
CLOSINGS_WIDE = {
    "HOU-134": "company-wide, six states",
    "HOU-022": "company-wide",
    "HOU-068": "Houston and Austin",
    "HOU-007": "two markets",
    "HOU-069": "Houston and Austin",
    "HOU-135": "Texas-wide",
    "HOU-077": "four Texas markets",
    "HOU-072": "four markets in two states",
}

SCREEN = {
    "HOU-144": "A two-plant campus making both architectural and structural wall.",
    "HOU-062": "Founded 2020 by builders from Taylor Morrison, Toll Brothers and Ryland. "
               "No closings figure yet.",
    "HOU-083": "Ground-up retail in the Heights, and an adaptive reuse project in Timbergrove.",
    "HOU-039": "Sells lots. Sunterra's own builder page lists eighteen names.",
    "HOU-018": "A repeated Town Center format. Retail shells compete against tilt-wall, "
               "not stick framing.",
    "HOU-073": "A published average build time of three and a half months, and Berkshire "
               "Hathaway capital behind it. Purchasing may run through the parent.",
    "HOU-075": "A national builder selling at Sunterra. Its team page lists no Houston "
               "division president.",
    "HOU-069": "97 floor plans on its own site, and a proprietary energy programme under "
               "its own name.",
    "HOU-044": "Two Katy duplex projects, one on Galileo Way and one at Katy Pointe "
               "Boulevard.",
    "HOU-134": "Three Houston communities opened by a builder active in more than 120, and "
               "a build-to-rent line inside it.",
}

# (scope, old, new). Each old must be found exactly once in its scope.
EDITS = [
    # Cole Klein. Houstonia: printing is used for parts of the first floor. Eco
    # Material's release names PozzoSlag and PozzoCem as what the homes were built
    # with; PozzoCem Vite was the live demonstration.
    ("HOU-002", "The houses are hybrid: the ground floor is printed concrete and the second "
                "storey is engineered wood, so the printed scope is the lower level rather "
                "than the whole house.",
     "The houses are hybrid. Houstonia reports that only parts of the first floor are "
     "printed, and the second storey is engineered wood."),
    ("HOU-002", "whose PozzoCem Vite is the printed mix at Zuri Gardens by its own release "
                "of 13 November 2025.",
     "whose release of 13 November 2025 says the homes were built with its PozzoSlag and "
     "PozzoCem cements."),
    ("HOU-002", "Priced roughly $250,000 to $275,000.", "Priced in the mid to high $200,000s."),

    # Chesmar. 10 June 2022 is the agreement; the purchase was set for 1 July.
    ("HOU-045", "Sekisui House of Japan bought Chesmar on 10 June 2022 for about $514 million.",
     "Sekisui House of Japan agreed on 10 June 2022 to buy Chesmar for about $514 million."),

    # Meritage. No transcript line says AI is deployed across every part of the
    # business. The headquarters sentence was a note about the research.
    ("HOU-008", " The Meritage headquarters is taken from a general corporate record and is "
                "not reconfirmed on an investor-relations page.", ""),
    ("HOU-008", " CEO describes deploying AI across every part of the business.", ""),
    ("HOU-008", "Cycle-time and AI programme", "Cycle time"),
    ("HOU-008", "AI across the business and sub-110-day cycles. Nothing on wall systems.",
     "A sub-110-day construction cycle held for four quarters. Nothing on wall systems."),

    # Tricoast. The founding history, the seven plans and the $280,000s are from
    # a March 2021 Lago Mar release and describe Lago Mar. The firm's own site now
    # shows nine plans and nine communities from the $279,000s.
    ("HOU-062", "Builder founded in 2020 by former Taylor Morrison, Toll Brothers and Ryland "
                "people, selling from roughly $280,000 across Sunterra, Lago Mar, Marvida "
                "and Canterra Creek.",
     "Builder founded in 2020 by people from Taylor Morrison, Toll Brothers and Ryland "
     "Homes, by a Lago Mar release of March 2021. Its own site lists nine plans across nine "
     "communities, from the $279,000s at La Segarra in Brookshire to the $399,000s at "
     "Canterra Creek in Iowa Colony."),
    ("HOU-062", "Seven floor plans carried across ten communities.",
     "Nine floor plans carried across nine communities."),

    # Braun. Its own site says ground-up development, redevelopment and
    # repositioning, and lists an adaptive reuse project. One building size is
    # published, 24,000 square feet, in 2018.
    ("HOU-083", "building ground-up neighbourhood retail rather than converting.",
     "doing ground-up development, redevelopment and repositioning by its own description."),
    ("HOU-083", "Small retail buildings repeated across three cities, which is more "
                "repetition than anyone else in this category.",
     "Small retail buildings repeated across three cities."),
    ("HOU-083", "Retail shells at 20,000 to 25,000 square feet.",
     "Its one published building is 24,000 square feet."),
    ("HOU-083", "by Tipps Architecture.", "by Tipps Architecture, reported in 2018."),

    # Land Tejas. The 2021 announcement prints no acreage; the Chronicle's 2024
    # article prints 2,303. The builder page lists eighteen names, one of them
    # Lennar's own Village Builders brand.
    ("HOU-039", "Sunterra in Katy carries eighteen builders on its own builder page.",
     "Sunterra in Katy lists eighteen builder names on its own builder page."),
    ("HOU-039", "Sunterra's acreage is published as 2,303 in the 2021 announcement and 1,039 "
                "on Land Tejas's own community page, and the two have not been reconciled.",
     "The Houston Chronicle put Sunterra at 2,303 acres in 2024. Land Tejas's own Sunterra "
     "page says 1,039 acres."),
    ("HOU-039", "Sunterra carries eighteen builders inside one community.",
     "Sunterra lists eighteen builder names inside one community."),
    ("HOU-039", "It sells lots. Eighteen builders buy the wall.",
     "It sells lots. The builders buy the wall."),

    # J. Patrick. Its own page lists ten communities.
    ("HOU-067", "across twelve submarkets including", "across ten communities including"),
    ("HOU-067", "Twelve submarkets is wide for a builder this size, which spreads the plan "
                "set thin.",
     "Ten communities spreads the plan set across many sites."),

    # Smith Douglas. The lot count is from August 2023, not 2022.
    ("HOU-074", "which had closed 324 homes across 15 communities with about 1,500 lots in "
                "2022.",
     "which had closed 324 homes across 15 communities in 2022 and controlled nearly 1,500 "
     "lots when the purchase was announced in August 2023."),

    # Pagewood. The two 2023 reports disagree on what 513,000 covers.
    ("HOU-081", "The district figure of 513,000 square feet is the full ten-block programme, "
                "not phase one.",
     "The Greater Houston Partnership put the whole development at 513,000 square feet in "
     "2023."),

    # NewQuest. $3.1 billion is owned assets, not the value of the 12 million
    # square feet it manages. Pearland Town Center was a land sale to CBL.
    ("HOU-018", "Houston retail developer managing a 12 million square foot portfolio valued "
                "at $3.1 billion. Master developer of a repeated Town Center format across "
                "Greater Houston including Fort Bend Town Center in Missouri City, Cy-Fair "
                "Town Center, Stone Hill Town Center and the 800,000 square foot Pearland "
                "Town Center Mall.",
     "Houston retail developer managing 12 million square feet of retail, with $3.1 billion "
     "of owned assets by its own page. Developer of a repeated Town Center format across "
     "Greater Houston, including Fort Bend Town Center in Missouri City, Cy-Fair Town Center "
     "and Stone Hill Town Center. It sold the 138-acre site of the 800,000 square foot "
     "Pearland Town Center to CBL."),
    ("HOU-018", "across Harris, Fort Bend, Galveston and Brazoria counties.",
     "across Harris, Fort Bend and Galveston counties."),

    # Brohn. A superlative against the deck.
    # (screen line replaced above)

    # Risewell. The team page lists ten division presidents and no Houston one.
    ("HOU-075", "The rebranded New Home Company, operating eleven divisions nationally, with "
                "a Houston division led by a named division president building in Sunterra. "
                "The rename from New Home Company is recent, so older coverage uses the "
                "previous name.",
     "Risewell Homes is the name Landsea Homes and The New Home Company took after their "
     "2025 merger, so older coverage uses the old names. It sells at Sunterra in Katy. Its "
     "team page lists ten division presidents and none for Houston."),
    ("HOU-075", "Eleven divisions nationally means purchasing scale above the band a single "
                "machine serves.",
     "Ten divisions on its team page means purchasing scale above the band a single machine "
     "serves."),
    ("HOU-075", "No method on record. The Houston division president is a licensed "
                "professional engineer.", "No method on record."),

    # Fidelis. The 280,000 square foot plan was announced in March 2026.
    ("HOU-030", "Bought acreage near the Grand Parkway in Alvin, Brazoria County in November "
                "2024 for a planned 280,000 square foot Alvin Marketplace,",
     "Bought acreage near the Grand Parkway in Alvin, Brazoria County in November 2024, and "
     "in March 2026 announced a 280,000 square foot Alvin Marketplace on it,"),
    ("HOU-030", "Land acquired November 2024.", "Land acquired November 2024, plan announced "
                                               "March 2026."),

    # First America. Valley Ranch is in Montgomery County, as Signorelli's own card
    # says. The firm's announcement of Winniford is dated 15 September 2025.
    ("HOU-007", "Liberty County. 359 homes", "New Caney, Montgomery County. 359 homes"),
    ("HOU-007", "became president of First America on 17 September 2025",
     "became president of First America in September 2025"),

    # Alta. The entry price is said twice; so is the headcount.
    ("HOU-061", " Its entry price point is $170,000.", ""),
    ("HOU-061", " The firm has six employees and no purchasing department.", ""),

    # Tilson. Rank 119 is on BUILDER's list below the Builder 100.
    ("HOU-135", "ranked 119th on the Builder 100", "ranked 119th by BUILDER"),

    # Newmark. Its own floor-plan page shows 97 plans. No page counts its
    # communities.
    ("HOU-069", "now in more than twenty communities including", "selling in communities including"),
    ("HOU-069", "More than 150 named plans across more than twenty communities. The plan set "
                "is the problem here.",
     "97 floor plans on its own site, across Houston and Austin. The plan set is the problem "
     "here."),

    # Howard Hughes. The office is 49,000 square feet. The acreage total is a sum.
    ("HOU-011", "Around 50,000 square feet over three storeys.",
     "49,000 square feet over three storeys."),
    ("HOU-011", "1,802 residential acres remain across the three as of June 30, 2026: 1,142 at "
                "Bridgeland, 597 at The Woodlands Hills and 63 at The Woodlands.",
     "Its June 30, 2026 filing lists 1,142 residential acres left at Bridgeland, 597 at The "
     "Woodlands Hills and 63 at The Woodlands, 1,802 in all."),

    # Camden. The article prints the two counts; 389 is their sum.
    ("HOU-019", "Invested $155 million in two Houston-suburb build-to-rent communities:",
     "Invested $155 million in two Houston-suburb build-to-rent communities, 389 homes in all:"),

    # RSK. No source gives the distance between the two sites.
    ("HOU-044", "Two Katy build-to-rent duplex projects within about a mile of each other, "
                "156 and 210 units.",
     "Two Katy build-to-rent duplex projects: 156 duplexes on Galileo Way, and 210 at Clay "
     "Road and Katy Pointe Boulevard, due in 2026."),
    ("HOU-044", "156 and 210 units on two Katy sites about a mile apart.",
     "156 and 210 duplexes on two Katy sites."),

    # DSLD. The community is Aldeana.
    ("HOU-134", "Aldean in Bonney at", "Aldeana in Bonney at"),
    ("HOU-134", "Aldean in Bonney, Mostyn", "Aldeana in Bonney, Mostyn"),

    # Westin. A superlative against the deck, with no source.
    ("HOU-068", ", with the widest footprint in the south suburban master planned communities "
                "of any builder screened", ""),

    # Brundage-Bone. The page lists two Houston addresses and does not call them yards.
    ("HOU-160", "with two Houston yards", "with two Houston addresses"),
    # Wells, Hillsboro. The page prints no acreage.
    ("HOU-144", " The structural plant occupies about 25 acres of a 50-acre site, leaving the "
                "rest for expansion, and produces",
     " The structural plant produces"),
    ("HOU-144", "A hundred thousand square feet across two plants",
     "102,000 square feet across two plants"),
]
