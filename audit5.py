# -*- coding: utf-8 -*-
"""Build 66. The fifth audit round: four reviewers, one lens each.

A content reviewer read every rendered string against the house rules and
against the rest of the page, and most of what it found is one kind of fault:
a card, a caption or a section header saying something another part of the page
disproves. The section called Already working with ICON held three firms, none
of which works with ICON, under a page whose own ICON block says ICON has no
Houston project. Nine cards carried an "only" that another card on the deck
contradicts. The Howard Hughes caption said it lists none of the builders
screened, over a chart that draws eleven of them. The landing's own pointer to
where the printer-fit bands are explained pointed at nothing.

Every edit below is an exact replacement that has to find its old text exactly
once inside the scope it names, or the build fails. A scope is a card id or a
top-level block of the page data. So a correction cannot go quietly stale: if
the text it corrects changes underneath it, the build stops and says which.

Marks move only where a card's own reason argued the other mark, the Leola rule
from Build 35. Three track records read Yes for paying an architect, for
converting old buildings and for a planned conversion that did not survive a
sale; none is a new building method, and two sister cards doing the same thing
already read No. DSLD's printer fit read Partly over a reason that says 3,989 a
year is above the band.
"""

# The mark follows the reason. (repeatability, machine_fit, innovation): 3 Yes,
# 2 Partly, 0-1 No.
SCORE = {
    "HOU-038": {"innovation": 1},     # Cameron: a conversion, and the sale ended it
    "HOU-037": {"innovation": 1},     # The Deal Co.: every project a conversion
    "HOU-005": {"innovation": 1},     # Radom: commissioned an architect
    "HOU-134": {"machine_fit": 1},    # DSLD: 3,989 a year, above the band
    "HOU-004": {"machine_fit": 2},    # InTown: no figure at all, "citywide volume"
}

# Two builders publish an annual figure on a card and were not drawn.
CLOSINGS = {
    "HOU-022": (1465, 1465, 2025, "Builder 100, company-wide"),
    "HOU-134": (3989, 3989, 2025, "Builder 100, company-wide, six states"),
}

# The masterplan lines and builder rosters the land-owner chart draws. Three of
# them disagreed with their own cards.
CHANNEL = {
    "HOU-133": ("Pomona, Valencia and Legacy in League City",
                ["Perry Homes", "Coventry Homes", "PulteGroup", "David Weekley Homes",
                 "Highland Homes", "Partners in Building", "Westin Homes"]),
    "HOU-040": ("Fifteen Houston masterplans by its own count, including Sienna, Cross "
                "Creek Ranch, Harvest Green, Veranda, Jordan Ranch, Woodforest and "
                "Grand Central Park", None),
    "HOU-041": ("Towne Lake, and The Highlands with more than 4,000 planned homes across "
                "thirteen builders", None),
    "HOU-039": ("Sunterra in Katy, eighteen builders on its own builder page", None),
}

# The chart matched builders to cards by exact name, so the three Build 65 cards
# read "not screened" under their own names.
OWNER_ALIAS = {
    "Lennar": "HOU-166", "Village Builders": None,
    "Highland Homes": "HOU-168", "Pulte Homes": "HOU-167", "PulteGroup": "HOU-167",
}

PHONE_ABSENT = {
    "HOU-016": "No number is published.",
    "HOU-017": "No number is published.",
    "HOU-127": "No number: the firm's site cannot be read.",
}

# (scope, old, new). Scope is a card id or a top-level key of the page data.
EDITS = [

 # ---- sections. Header names what the section is, not what to think of it.
 ("group_notes", "In on all three counts.",
  "Builders and developers. Adopters and contractors that hold all three sit in "
  "their own sections."),
 ("group_notes", "Already reachable through an existing ICON relationship.",
  "Lennar's Houston division and two firms Lennar owns. LEN X invested in ICON in "
  "August 2021, and Lennar built Wolf Ranch with ICON."),
 ("group_notes", "Purchasing sits at a national desk.",
  "Purchasing runs at company level, across several states."),

 # ---- the contractor chain: two headers described firms that do not match them
 ("chain", "Owns the job and self-performs the concrete", "General contractor"),
 ("chain", "Houston builders do not put up their own walls. The general contractor "
           "that self-performs concrete is the one that would run the machine.",
  "Two of the seven self-perform concrete on the record: Harvey Cleary, through IQI "
  "Construction, and T&T. The rest publish no self-performed concrete, or say they "
  "hire it out."),
 ("chain", "Places it through a hose", "Pumps or sprays concrete"),
 ("chain", "A crew here already places cementitious material through a hose onto a "
           "surface, to a profile, with no formwork.",
  "Omega sprays gunite and shotcrete onto a surface. Brundage-Bone and Texan Pumpers "
  "pump concrete into forms."),

 # ---- limits
 ("limits", "Trade press, the builder lists each master-planned community publishes, "
            "the Builder 100, and the Greater Houston Builders Association member "
            "directory. The directory carries 190 companies across seven categories. "
            "Reading all seven against this deck, and reading the metro permit leaders "
            "against it, added five firms. The rest is custom and infill work of a few "
            "homes a year, below the volume a printer is bought for.",
  "Trade press, the builder lists each master-planned community publishes, the "
  "Builder 100, BUILDER's Local Leaders table for Greater Houston, and the Greater "
  "Houston Builders Association member directory. The directory lists 190 companies "
  "in seven categories, and five firms are on this deck from it and from the metro "
  "permit leaders. Local Leaders added three: Lennar, PulteGroup and Highland Homes. "
  "The rest of the directory builds a few custom or infill homes a year."),
 ("limits", "Firms whose product is retail shell, mid-rise or one-off architecture are "
            "held out of the deck and kept in the workbook.",
  "One-off and retail work sits in the Custom and hybrid section. Mid-rise "
  "multifamily is held out of the deck and kept in the workbook."),

 # ---- ICON's own record
 ("icon_record", "100 further printed homes with Mobile Loaves and Fishes. ICON's "
                 "largest programme by count.",
  "100 further printed homes with Mobile Loaves and Fishes."),
 ("icon_record", " A $899,000 figure circulates from a single trade outlet and is not "
                 "confirmed anywhere else, so it is not quoted as fact here.", ""),
 ("icon_record", "No ICON project, partnership or public statement specific to Houston "
                 "could be found. The newsroom, the site and general search all return "
                 "nothing.",
  "ICON has published no Houston project."),
 ("icon_record", "Lennar owns Friendswood Development Company outright, and Friendswood "
                 "is screened here. The relationship that built a hundred houses in "
                 "Georgetown reaches Houston through that subsidiary.",
  "Lennar's Houston division is on this deck, with Friendswood, its Houston land arm, "
  "and GreenEco, which came with Rausch Coleman in February 2025."),

 # ---- code and precedent: two of three rows called unfinished work built
 ("code", "23 of 26 homes printed, Commander Home Builders, printed by HiveASMBLD.",
  "26 homes planned, 23 to be printed, Commander Home Builders with HiveASMBLD. One "
  "under construction in April 2026."),
 ("code", "One printed duplex, Elpis 3D Home Builders, printed by HiveASMBLD.",
  "One duplex, Elpis 3D Home Builders with HiveASMBLD, started March 2026. No "
  "completion published."),

 # ---- market figures
 ("market", "23 of 26 printed", "23 of 26 to be printed"),
 ("market", "One duplex", "One duplex, started March 2026"),
 ("market", "Sunconomy eco-village announced, Montgomery",
  "Sunconomy permits a printed house in Lago Vista"),
 ("market", "Diamond Age closes, 15 of 43 homes unfinished",
  "Diamond Age closes with fifteen houses unfinished"),
 ("market", "CRH buys Eco Material, HiveASMBLD's cement supplier",
  "CRH agrees to buy Eco Material, HiveASMBLD's cement supplier"),
 ("market", "Stated by the outgoing purchasing lead, two markets",
  "The Signorelli Company, the parent"),

 # ---- the field
 ("competitors", "Its one Texas connection is the Sunconomy eco-village in Montgomery, "
                 "announced since about 2019 with nothing completed.",
  "Its one Texas connection is Sunconomy, which permitted a printed house in Lago "
  "Vista in 2019 and has published no completion."),

 # ---- supply panel and its notes
 ("supply_notes", "Of 87 firms found, five published a figure and twenty-four "
                  "published years in business instead.",
  "Of 87 candidates, five publish a figure and twenty-four publish years in business "
  "instead."),
 ("supply_notes", "A gunite crew already places cementitious material through a hose "
                  "onto a vertical surface, to a profile, with no formwork. One of "
                  "these firms advertises on its own careers page for nozzlemen, top "
                  "finishers, bottom finishers and foremen. None of them has the "
                  "balance sheet to buy a machine and every one of them has the people "
                  "to run one.",
  "A gunite crew places cementitious material through a hose onto a surface, to a "
  "profile. One of these firms advertises on its own careers page for nozzlemen, top "
  "finishers, bottom finishers and foremen."),
 ("supply", " The single best source for which Houston crews pour at volume, which no "
            "directory publishes.", ""),
 ("supply", "Three named officers and a Houston plant. Worth knowing that its own page "
            "says it uses tried-and-true methods vetted over decades and is in business "
            "to cut cable, not corners. A good source and, on its own account, a poor "
            "prospect.",
  "Three named officers and a Houston plant. Its own page says it uses "
  "tried-and-true methods vetted over decades and is in business to cut cable, not "
  "corners."),
 ("supply", "The newest of the Houston post-tension plants, which usually means the "
            "one still winning accounts rather than defending them.",
  "The most recently founded of the post-tension plants on this panel, in 2010."),
 ("supply", "A producer two years old is still building a book, which makes it the "
            "ready-mix call most likely to be taken and most likely to trial a mix.",
  "Founded in 2023, with a named general manager, operations manager and sales "
  "manager."),
 ("supply", "Positioned exactly where the production growth is, and building two more "
            "plants, which means a company with capital and an appetite for new "
            "accounts.",
  "Two plants in the north and northwest of the metro, and two more under "
  "development at Brookshire and Jacintoport."),
 ("supply", "The site answered a stub to a script and was read by hand.", None),
 ("supply", "The only Houston ready-mix producer with a published low-carbon product "
            "actually poured here in quantity, which is the conversation a printed wall "
            "needs its material supplier to have already had.",
  "Publishes Vertua, a low-carbon concrete, as poured in the Houston metro."),
 ("supply", "No Houston plant count could be confirmed: the site is behind a bot "
            "defence that returns an encoded blob to a script.", None),
 ("supply", "A Katy batch plant sits inside the densest production housing corridor in "
            "the metro.",
  "One of its two Houston-area batch plants is in Katy."),
 ("supply", "White cement and calcium aluminate cement in a Houston book is unusual, "
            "and calcium aluminate is the rapid-set chemistry a printed wall needs to "
            "stand up between layers.",
  "Stocks calcium aluminate cement, which sets rapidly, and white cement."),
 ("supply", "The only firm in the whole material sweep publishing proprietary product "
            "development of its own: the Suncoast Stud Reinforcement System and a "
            "barrier cable embed bracket. A supplier that engineers its own hardware is "
            "a supplier that will engage on a new method.",
  "Publishes hardware of its own design: the Suncoast Stud Reinforcement System and a "
  "barrier cable embed bracket."),

 # ---- firms with no website
 ("no_site_note", "Twenty-one firms that meet the profile on trade association "
                  "category and geography and publish no website at all: six in the "
                  "Greater Houston Builders Association's foundation and concrete "
                  "categories, eleven on the Associated Masonry Contractors of Houston "
                  "roster, and four more. They are not small by inference, they are "
                  "unlisted. This deck cannot screen them.",
  "Twenty-one firms that meet the profile on trade association category and "
  "geography and publish no working website: six in the Greater Houston Builders "
  "Association's foundation and concrete categories, ten on the Associated Masonry "
  "Contractors of Houston roster, three precast plants and two pumpers. This deck "
  "cannot screen them."),
 ("no_site", " The dual turnkey listing is the strongest unconfirmed signal in the set.", ""),
 ("no_site", " No website in any search result.", ""),
 ("no_site", ", which suggests subdivision masonry fencing at volume", ""),
 ("no_site", "Appears residential brick oriented, which is the production-homebuilder "
             "seam. The site sits in an http redirect loop.",
  "The site sits in an http redirect loop."),
 ("no_site", " The site forces an https to http redirect no fetcher follows.",
  " The site redirects between https and http in a loop."),
 ("no_site", "Same redirect loop. Waller County is next door to Legacy Precast's "
             "Brookshire plant.",
  "The site redirects in a loop."),
 ("no_site", "An American Concrete Pumping Association listing and nothing fetchable.",
  "An American Concrete Pumping Association listing."),
 ("no_site", "Same.", "An American Concrete Pumping Association listing."),

 # ---- the "only" claims another card on the deck disproves
 ("HOU-138", "The only precast plant inside the Houston metro proper, and a narrow one: "
             "hollowcore is a single product line rather than a flexible casting yard.",
  "A hollowcore plant in Pearland. Hollowcore is one product line, a floor and roof "
  "plank."),
 ("HOU-156", "The only masonry contractor screened that already sells a prefabricated "
             "wall system and says in its own words that it is looking for new ones.",
  "It already sells a prefabricated masonry wall system and says on its own site that "
  "it is looking for new ones."),
 ("HOU-120", " The only contractor screened whose whole business is a non-conventional "
             "wall.", ""),
 ("HOU-101", "The only concrete contractor screened that publishes a standing "
             "residential division. It already buys its own formwork systems and placing "
             "booms.",
  "A standing residential division beside structural and commercial, and it owns its "
  "formwork systems and placing booms."),
 ("HOU-108", "One of two contractors screened that names an actual multifamily project "
             "on its own site. The published work is paving-heavy.",
  "Names a garden-style apartment project on its own site. The published work is "
  "mostly paving."),
 ("HOU-104", " That is the only published size in this section, and at that size one or "
             "two printers cover a real share of a year's wall.",
  " At that size one or two printers would cover part of a year's wall."),
 ("HOU-006", "Triten describes mass timber as a relatively rare alternative to steel and "
             "concrete. Specifying and financing a CLT frame is the one documented case "
             "in Houston of a developer paying for an unproven structural system.",
  "Triten describes mass timber as a relatively rare alternative to steel and "
  "concrete. No source shows the building was built."),
 ("HOU-006", "Financed a cross-laminated timber frame at The Mill. 294 units at Aliana "
             "land in Titan's first delivery window.",
  "Planned a cross-laminated timber office at The Mill in 2021, and no source shows it "
  "was built. 294 units at Aliana open in summer 2027."),
 ("HOU-015", "Signorelli can specify a wall method on its own lots through its own "
             "builder without a third-party veto, which no other master-planned "
             "developer screened can do.",
  "Signorelli can specify a wall method on its own lots through its own builder."),
 ("HOU-162", "The only firm on this deck that both shoots concrete through a nozzle to a "
             "profile and carries an audited balance sheet large enough to buy equipment.",
  "It shoots gunite and shotcrete through a nozzle to a profile, and carries an audited "
  "balance sheet."),
 ("HOU-141", "The plant's own page. The only staffing on this deck that names Houston and "
             "multifamily in one title.",
  "The plant's own page, which names Houston and multifamily in the one title."),
 ("HOU-141", "The only precast producer screened whose own staffing names Houston and "
             "multifamily in one title.",
  "Its own staffing page names Houston and multifamily in one title."),
 ("HOU-163", "The largest residential slab operation found in Texas, owned by a public "
             "infrastructure group with a capital allocation process, and the only "
             "contractor on this deck that publishes which builder it pours for.",
  "A residential slab contractor owned by a public infrastructure group, and it "
  "publishes which builder it pours for."),
 ("HOU-110", "The only contractor screened that pairs tilt-wall with a published "
             "residential concrete line, including engineered slabs.",
  "Tilt-wall beside a published residential concrete line, including engineered slabs."),
 ("HOU-080", "The only firm screened whose founders operate hospitality themselves rather "
             "than leasing to operators.",
  "Its founders operate hospitality themselves rather than leasing to operators."),
 ("HOU-011", " The one documented case of this firm paying to be first with a structural "
             "system.", ""),
 ("HOU-001", "The only firm screened with dated, named-executive evidence of sustained "
             "premium spend on unproven construction technology.",
  "Six years of in-house construction software, and robots on site."),

 # ---- statements about ICON and printing that other parts of the page disprove
 ("HOU-132", "It is the only equity position in a printed wall system on this deck.",
  "Apis Cor makes construction 3D printers."),
 ("HOU-004", "Attached three-story townhomes are the highest wall-share residential "
             "product type screened. Party walls on both sides, three storeys inside "
             "Titan's 27-foot envelope, and the same unit repeated across dozens of "
             "sites.",
  "Party walls on both sides, three storeys, and the same unit repeated across dozens "
  "of sites."),
 ("HOU-004", "Three-storey attached townhomes at citywide volume, built by one owner who "
             "also develops the land.",
  "No annual figure is published. On the bands, a firm with no published figure is a "
  "Partly."),
 ("HOU-017", "Attached party-wall product delivered by printing, inside the city limits, "
             "on a roughly three-month cycle. Small, but it is a completed Houston "
             "reference for printed party walls.",
  "One duplex, started March 2026. No completion published."),
 ("HOU-016", " This is a Houston-market operator quoting real printed-wall performance.",
  ""),

 # ---- cards that contradict themselves
 ("HOU-023", "125,000 homes, Houston HQ, 50 years. Its supplier recognition covers "
             "insulation and fire-stopping, not the envelope.",
  "John Schiegg, Vice President of Purchasing and Supply Chain Services, is quoted on "
  "its 2026 preferred-partner list."),
 ("HOU-081", "Ten contiguous EaDo blocks, 513,000 square feet in phase one, Gensler on "
             "design and SWA on landscape.",
  "Ten contiguous EaDo blocks and 513,000 square feet planned, with Gensler on design "
  "and SWA on landscape."),
 ("HOU-045", "Builder at Sienna, with four Texas divisions.",
  "Builder at Sienna, selling across five Texas regions."),
 ("HOU-022", "20,000 homes since 2004 is roughly a thousand a year, above the band but "
             "not beyond a two-machine pilot.",
  "1,465 closings in 2025 on the Builder 100 sits inside the 400 to 1,500 band."),
 ("HOU-038", "It is taking on a $50 million conversion of two landmark towers from 1927 "
             "and 1941, which is a harder build than anything a printer would be asked "
             "to do.",
  "No method on record. The planned $50 million conversion of two towers from 1927 and "
  "1941 is not shown surviving the 2024 sale."),
 ("HOU-038", "Paying a premium to work inside a 1927 structural envelope is direct "
             "evidence of tolerance for non-standard construction conditions.",
  "The conversion is not shown surviving the 2024 sale."),
 ("HOU-038", "Willing to take on a hard build, but almost no new exterior wall.",
  "Almost no new exterior wall."),
 ("HOU-005", "Commissioned Michael Hsu for Montrose Collective, four-street frontage, "
             "$104.75M financed.",
  "No method on record. Its architect, Michael Hsu, also drew ICON's homes at Mueller "
  "in Austin."),
 ("HOU-005", "Retail frontage on four streets with a stacked mixed programme is a "
             "massing conventional framing prices badly. Commissioning Michael Hsu is "
             "evidence of paying a design premium.",
  "Michael Hsu Office of Architecture also drew ICON's homes at Mueller in Austin."),
 ("HOU-037", "Twenty years of building inside awkward industrial structures.",
  "No method on record. Every project is a conversion of an industrial building."),
 ("HOU-037", "Two decades of converting industrial structures into occupied space. "
             "Sustained willingness to build inside awkward existing fabric, repeated 27 "
             "times.",
  "27 industrial buildings converted on one campus since 2005."),

 # ---- No reasons that argued for the firm
 ("HOU-076", "The strategy is explicitly about attainability, so a wall cost saving "
             "lands on the stated strategy.",
  "No method on record. Its stated strategy is attainable entry-level product."),
 ("HOU-075", "The division president is a professional engineer, which is rare and "
             "matters for a method conversation.",
  "No method on record. The Houston division president is a licensed professional "
  "engineer."),
 ("HOU-066", "It runs land through final inspection in house, so no third party sits in "
             "a method decision.",
  "No method on record. It runs land through final inspection in house."),
 ("HOU-063", "The firm's published positioning is against speed and cost cutting. A "
             "printed wall would be measured on the firm's own terms.",
  "No method on record. Its published positioning is against speed and cost cutting."),
 ("HOU-034", "Owner Sumitomo Forestry is a timber group, which may cut against a "
             "concrete wall.",
  "Nothing on record. Its owner, Sumitomo Forestry, is a timber group and bought a "
  "sawmill in 2025."),

 # ---- land owners: one figure per card
 ("HOU-039", "Sells lots. Sunterra carries 2,303 acres and 15 builders.",
  "Sells lots. Sunterra carries eighteen builders on its own builder page."),
 ("HOU-039", ", the largest single roster screened, and eleven of them are on this deck",
  ""),
 ("HOU-040", "Sells lots across 14 Houston masterplans. Buys no walls.",
  "Sells lots across fifteen Houston masterplans. Buys no walls."),
 ("HOU-040", " Channel value is high and direct wall purchasing is nil. Johnson "
             "Development publishes no construction-method content.",
  " It sells lots and buys no walls."),
 ("HOU-041", "Sells lots. Towne Lake and The Highlands carry 4,000 homes across 12 "
             "builders.",
  "Sells lots. The Highlands alone carries more than 4,000 planned homes across "
  "thirteen builders."),
 ("HOU-133", "Two of these four builders are on this deck.",
  "Three of these four builders are on this deck: Coventry, Perry and PulteGroup."),
 ("HOU-133", "Four of these ten builders are on this deck.",
  "Six of these ten builders are on this deck."),

 # ---- wrong or self-contradicting about Houston
 ("HOU-065", " Read the record as a Bryan-College Station builder with a Conroe tail, "
             "not a Houston builder.", ""),
 ("HOU-013", "120 communities and local ownership. Its published innovation page covers "
             "smart-home features and floor plans.",
  "Family-owned since 1967 and headquartered in Houston. Its published innovation page "
  "covers smart-home features and floor plans."),
 ("HOU-013", "Wall-heavy product and decision-making in the same city as the printer.",
  "Detached single-family, with its headquarters in Houston."),
 ("HOU-130", "The largest privately held homebuilder in Greater Houston by its own "
             "description, founded 1997,",
  "Privately held homebuilder founded 1997,"),
 ("HOU-130", "782 closings in 2025 sits above the band one or two printers cover, so the "
             "first order is a line inside the business rather than the whole business.",
  "782 closings in 2025 sits in the 400 to 1,500 band, so the first order is a line "
  "inside the business."),
 ("HOU-131", ", and the price band absorbs a method premium", ""),

 # ---- one fact, said once
 ("HOU-028", "346 units, with its own architect and general contractor in-house. No "
             "third party in a method decision.",
  "Its own affiliates were architect and general contractor at Fort Bend Town Center."),
 ("HOU-028", "346 units with its own architect and its own general contractor. No third "
             "party is in the decision.",
  "346 units on one site."),
 ("HOU-028", "346 units on one site. Sueba affiliates act as architect and general "
             "contractor, so design and construction method are decided inside one "
             "company.",
  "346 units on one site, from studio to three bedroom."),
 ("HOU-142", "The largest precast footprint inside Houston's supply radius, in the first "
             "year under a new parent, which is when a producer entertains new "
             "capability.",
  "Metromont bought it on 15 December 2025 and kept its president, Chad Petro."),
 ("HOU-142", " The first year under a new parent is when a producer's capital budget "
             "gets rewritten.", ""),
 ("HOU-119", " A printer is a gantry that places concrete.", ""),
 ("HOU-119", "A printer is a gantry. The firm already puts them up for other people.",
  "Installs gantry, jib, bridge and portal cranes for other firms."),
 ("HOU-128", " The printed house is in Fort Worth. The firm is headquartered in Houston; "
             "the project is not.", ""),
 ("HOU-128", "The firm has already paid to watch a wall go up without a framing crew.",
  "A printed house the firm paid for."),
 ("HOU-034", " The decisions moved up to the DRB Group platform after the April 2025 "
             "consolidation. Brightland was consolidated under The DRB Group on 1 April "
             "2025.",
  " Brightland was consolidated under The DRB Group on 1 April 2025, and its decisions "
  "sit on that platform."),
 ("HOU-105", " Encore Concrete Construction was established in 2017.", ""),
 ("HOU-117", " The firm states that it works through trade partner relationships rather "
             "than self-performing.", ""),
 ("HOU-042", "The channel leads directly to Lennar, which is a vertical builder. "
             "Friendswood is wholly owned by Lennar, which built the hundred-home Wolf "
             "Ranch community with ICON in Georgetown, designed by Bjarke Ingels Group "
             "and completed in 2025. The relationship exists at corporate level.",
  "It sells lots inside its own masterplans and Lennar builds the houses. Lennar's "
  "Houston division is a separate record on this deck."),
 ("HOU-078", " The energy-product claims this card used to carry came from a page that "
             "no longer exists.", ""),
 ("HOU-127", ", which is the problem", ""),
 ("HOU-127", "livelonestar.com answers 401 Forbidden to a browser and to a script on "
             "both hosts, so nothing the firm publishes about itself can be read, "
             "including who runs it.",
  "Nobody is named: the firm's own site cannot be read."),
 ("HOU-127", "livelonestar.com answers 401 Forbidden to a browser and to a script, on "
             "both the bare domain and the www host. Nothing the firm publishes about "
             "itself can be read, which is also why this card names no one.",
  "livelonestar.com answers 401 Unauthorized on both hosts, so nothing the firm "
  "publishes about itself can be read."),
]

# Build 66. The screen line sits directly under the headline figure on the firm
# page and beside it in the list, and on 30 cards it opened by saying the figure
# again. Each now carries the next fact instead. The whole line is replaced, so
# each entry is the full new line.
SCREEN = {
    "HOU-002": "The largest printed project in the metro. HiveASMBLD prints it.",
    "HOU-007": "750 homes sold in 2025. It markets its wall assembly, and the parent owns "
               "the land.",
    "HOU-065": "A published even-flow model that releases a fixed number of starts a week, "
               "with eight or nine plans per community.",
    "HOU-060": "Two standing plan families in one corridor.",
    "HOU-136": "The construction seat is named on the record.",
    "HOU-061": "All four communities in one county, and six staff with no purchasing "
               "department.",
    "HOU-003": "Federal money and open procurement, and no method on record.",
    "HOU-130": "Numbered plans across 22 communities, and it develops its own land, so a "
               "pilot needs nobody else's permission.",
    "HOU-074": "Fifteen communities of standardised entry-level product, now inside a listed "
               "builder. The Houston purchasing structure is not published.",
    "HOU-022": "Daiwa House holds 80 percent, and CastleRock publishes no method content.",
    "HOU-026": "A stated shift to self-development. Its declared technology is smart-home "
               "fittings.",
    "HOU-068": "Across the south suburban masterplans, with a named vice president of "
               "construction.",
    "HOU-064": "552 closings in 2024 on a no-haggle affordable model. A named director of "
               "construction.",
    "HOU-020": "parcHAUS funds seven rental communities under a named Houston director. No "
               "Houston site named.",
    "HOU-069": "More than twenty communities and more than 150 plans.",
    "HOU-044": "Two Katy duplex projects a mile apart.",
    "HOU-070": "The north and northwest growth corridor, with a named president and no "
               "published volume.",
    "HOU-152": "Sold a Houston production builder a subdivision framed in something other "
               "than wood, and self-performs the installation.",
    "HOU-104": "A self-performing concrete sub, still owned by the three brothers who "
               "started it.",
    "HOU-117": "Built through trade partners, across 200-plus projects.",
    "HOU-106": "Elevated post-tensioned decks beside the panels. The work repeats inside one "
               "metro and is bought by general contractors rather than by owners.",
    "HOU-112": "Purchasing now runs through a listed parent.",
    "HOU-072": "A vice president of purchasing, and every house is one-of-a-kind. The "
               "presidency passed from Jim to Chris Lemming in June 2026.",
    "HOU-036": "Midway kept sole development control after selling out of the Parkway joint "
               "venture in December 2024.",
    "HOU-005": "Michael Hsu designed Montrose Collective. Fifteen projects in one district.",
    "HOU-037": "Every project a conversion of an industrial building.",
    "HOU-025": "A dedicated build-to-rent brand. The division president role dates to 2018 "
               "and is unconfirmed.",
    "HOU-034": "Its parent, Sumitomo Forestry, bought a sawmill in 2025 to supply wood "
               "framing across the platform Brightland sits in.",
    "HOU-011": "It paid to put up Greater Houston's first mass timber office, and it sells "
               "lots, so the builder buys the wall.",
    "HOU-043": "Newland is now inside Brookfield Residential and publishes no leadership of "
               "its own. The one Houston name on record is from 2019.",
}
