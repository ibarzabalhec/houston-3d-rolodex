# -*- coding: utf-8 -*-
"""The builder layer: Greater Houston and suburban builders working inside
master planned communities.

The thesis this layer serves: a printer is bought by a builder, not by a
landowner and not by a fund. The builder that buys one or two machines repeats
a small plan set inside a handful of communities and closes enough houses a
year to keep a machine working, without being large enough to buy through a
national purchasing desk.

Excluded after checking, and worth recording so nobody researches them twice:
Highland Homes (3,482 Texas closings in 2025), Drees (2,286 closings and about
200 floor plans), Shea Homes and TRI Pointe, formerly Trendmaker, all of which
buy at national scale. On Point Custom Homes, Thompson Custom Homes and Frankel
Design Build design every house from scratch, which is the opposite of the plan
repetition the machine needs. Sterling Creek Homes is headquartered in Llano,
not Houston.
"""

# (id, name, region, url, key_stat, synopsis, scores, verdict, why triple,
#  principals, projects, sources, flags)
# scores: repeatability, machine_fit, innovation, capital_access  (0-3)

BUILDERS = [

("HOU-060", "Cervelle Homes", "Friendswood, Galveston-Harris", "https://www.cervellehomes.com/",
 "150 to 200 homes a year since 1990",
 "Production builder in southeast Houston, founded 1990 by a civil engineer, that has built more "
 "than 3,000 homes in one corridor and organises its product as two standing plan categories "
 "rather than a catalogue.",
 (3, 3, 0, 2),
 "150 to 200 homes a year from two standing plan families in one corridor. Inside the band one "
 "machine serves.",
 ("Between 150 and 200 homes a year, every year, in the same southeast Houston corridor.",
  "At that volume one machine is a meaningful share of output rather than a pilot.",
  "No method statement on record. The efficiency claim is about using the same trades since 1990."),
 [("Kevin Holland", "Leadership named on the firm's own site"),
  ("John Payson", "Leadership named on the firm's own site")],
 [("Pedregal South", "League City. The current selling community.",
   "repeatable", "A single community absorbing a repeated plan set is the shape a machine needs.",
   "https://www.cervellehomes.com/")],
 ["https://www.cervellehomes.com/"],
 ["Two people are named as leadership on the site without titles. Confirm which one owns "
  "construction before approaching."]),

("HOU-061", "Alta Homes", "Willis and Conroe, Montgomery", "https://www.myaltahomes.com/",
 "45 closings in 2025, 70 planned for 2026",
 "Six-person builder in Montgomery County selling from the $170,000s to the mid $300,000s across "
 "four communities in Willis, Conroe and Montgomery, with three more announced.",
 (3, 3, 0, 1),
 "45 closings in 2025 and 70 planned for 2026, all inside one county. Small enough that one "
 "machine changes the business rather than supplementing it.",
 ("Four communities inside a single county, with three more announced in the same corridor.",
  "45 closings in 2025 and 70 planned for 2026. One machine would cover most of a year's walls.",
  "No method evidence. Six people, so the decision sits with the two founders."),
 [("Dru Kahlenberg", "Chief Executive Officer"),
  ("Scott Gilbert", "President"),
  ("Ashley Meinecke", "Accounts Payable and Purchasing Manager")],
 [("Lexington Heights, Crockett Meadows, Lake Conroe Village", "Willis, Conroe and Montgomery.",
   "repeatable", "Entry-price product from the $170,000s, where a wall cost saving is the whole margin.",
   "https://www.myaltahomes.com/communities")],
 ["https://www.myaltahomes.com/team", "https://www.myaltahomes.com/communities"],
 ["The chief executive is on record saying the firm does not compete on volume. Price sensitivity "
  "at the $170,000 entry point sets the margin, not scale.",
  "At six employees there is no purchasing department. The purchasing manager also runs accounts "
  "payable, which means the decision sits with the two principals."]),

("HOU-062", "Tricoast Homes", "Houston, multi-county", "https://www.tricoasthomes.com/",
 "Seven floor plans across ten communities",
 "Builder founded in 2020 by former Taylor Morrison, Toll Brothers and Ryland people, selling from "
 "roughly $280,000 across Sunterra, Lago Mar, Marvida and Canterra Creek.",
 (3, 2, 1, 1),
 "Seven plans, ten communities, founded 2020. The tightest published plan set in the file, and no "
 "closings figure yet to size it against.",
 ("Seven floor plans carried across ten communities. Plan repetition is the operating model.",
  "No closings figure is published. A 2020 startup may not yet be at machine scale.",
  "Every home gets internal and third-party energy verification, which is a process discipline "
  "rather than a method change."),
 [("Christian Sommer", "President and Chief Executive Officer"),
  ("Keith Blum", "Executive Vice President and Chief Operating Officer"),
  ("Christina Wright", "Director of Purchasing")],
 [("Sunterra, Lago Mar, Canterra Creek", "Katy, Texas City and Iowa Colony.",
   "repeatable", "Seven plans repeated across ten communities in three counties.",
   "https://www.tricoasthomes.com/plans")],
 ["https://www.tricoasthomes.com/about-us", "https://www.tricoasthomes.com/plans"],
 ["No annual closings figure is published. The firm is five years old, so the volume question is "
  "open and is the first thing to ask."]),

("HOU-063", "Kendall Homes", "Katy, with communities in Conroe, Willis and New Caney",
 "https://kendallhomes.net/",
 "More than 4,000 homes since 1993",
 "Family builder founded in 1993, selling from the $300,000s to the $800,000s across Conroe, "
 "Willis, New Caney and the Lake Conroe corridor.",
 (3, 3, 0, 1),
 "Above 100 homes a year on average, across a small set of "
 "communities in one corridor. A named vice president of construction.",
 ("Communities clustered in Conroe, Willis and New Caney rather than spread across the metro.",
  "More than 4,000 homes since 1993 is an average above 100 a year, inside the band a machine serves.",
  "The firm's published positioning is against speed and cost cutting. A printed wall would be "
  "measured on the firm's own terms."),
 [("Glenn Briggs", "President"),
  ("Jason Madden", "Vice President of Construction")],
 [("Waukegan Way, Meadow Glen, Deer Pines, Canyon Creek", "Conroe.",
   "repeatable", "Four communities in one county taking the same plan set.",
   "https://kendallhomes.net/")],
 ["https://kendallhomes.net/"],
 ["The cumulative figure is the firm's own. No single-year closings number is published, so the "
  "annual rate is an average rather than a current run rate."]),

("HOU-064", "Colina Homes", "Houston, 20 communities", "https://www.colinahomes.com/",
 "More than 4,500 homes since 2007",
 "Affordable production builder founded in 2007 by Ken Williams, selling on no-haggle pricing "
 "across more than twenty communities from downtown to Katy, Conroe, League City and Magnolia.",
 (3, 3, 0, 1),
 "More than 4,500 homes since 2007, an average above 230 a year, on a no-haggle affordable model. "
 "A named director of construction.",
 ("More than twenty communities, all inside Greater Houston, taking a standard plan set.",
  "An average above 230 homes a year puts two machines inside a plausible share of output.",
  "No method evidence. The published positioning is price and floor plan, not construction."),
 [("Ken Williams", "Founder"),
  ("Robert Davis", "Director of Construction")],
 [("Enclave at Willis, Mill Creek Trails, Grand Magnolia", "Willis and Magnolia.",
   "repeatable", "Affordable product where the wall is the largest controllable line.",
   "https://www.colinahomes.com/")],
 ["https://www.colinahomes.com/about"],
 ["No LinkedIn company page exists for the firm, only individual employee profiles.",
  "The cumulative figure is the firm's own and covers eighteen years. No single-year number is "
  "published."]),

("HOU-065", "Stylecraft Builders", "College Station, building in Conroe and Huntsville",
 "https://www.stylecraft.com/",
 "More than 300 closings a year, 8 to 9 plans per community",
 "Family builder founded in 1982 in College Station, now building in Huntsville and Conroe, that "
 "runs an even-flow production model releasing a fixed number of starts a week rather than "
 "reacting to sales.",
 (3, 3, 2, 2),
 "Eight or nine plans per community and a published even-flow production model that releases a "
 "fixed number of starts a week. The only builder screened that operates on cadence.",
 ("Eight or nine floor plans per community, named by square footage, repeated across the corridor.",
  "More than 300 closings a year. Two machines would carry a real share of that.",
  "It runs an even-flow production system, releasing a fixed number of starts a week rather than "
  "chasing demand. A firm that already thinks in takt time is one that can price a printer."),
 [("Doug French", "Owner, President and Chief Executive Officer"),
  ("Jordan York", "Vice President of Construction"),
  ("Bruce Hendren", "Vice President of Pre-Construction"),
  ("Emily Runnion", "Director of the South Six Construction Group")],
 [("Sterling Ridge, Rockbridge East, Spring Lake", "Huntsville. Nine and eight plans respectively.",
   "repeatable", "A published plan count per community, which almost no builder discloses.",
   "https://www.stylecraft.com/new-homes/tx/north-houston/communities/"),
  ("Ladera Creek", "Conroe.",
   "method_risk", "Plans named by square footage, which is how a firm thinks when the plan is a unit "
   "of production rather than a design.",
   "https://www.stylecraft.com/")],
 ["https://www.stylecraft.com/team/",
  "https://www.builderonline.com/builder-100/leadership/builder-100-spotlight-stylecraft-builders_o"],
 ["The 300-closings figure and the even-flow description come from a Builder Magazine profile of "
  "2014 performance. The cadence model is on record; the current volume is not.",
  "Individual profiles for the four named leaders were not found. They are named with titles on "
  "the firm's own team page, which is the citation."]),

("HOU-066", "Sandcastle Homes", "Inner Loop Houston", "https://www.sandcastlehouston.com/",
 "About 50 homes a year since 2004",
 "Inner Loop infill builder founded in 1995, averaging about fifty closings a year in Rice "
 "Military, Sawyer Heights, Garden Oaks, Sunset Heights and Montrose.",
 (2, 3, 1, 1),
 "About fifty homes a year, stated by the firm, on small infill sites rather than in one "
 "community. The volume fits a machine; the sites are scattered.",
 ("Infill lots scattered across six inner-loop neighbourhoods rather than one site.",
  "About fifty closings a year. One machine covers most of that, if it can be moved economically.",
  "It runs land through final inspection in house, so no third party sits in a method decision."),
 [("Mike Dishberger", "Chief Executive Officer"),
  ("Mike Salomon", "Owner and co-founder")],
 [("Rice Military, Sawyer Heights, Garden Oaks, Montrose", "Currently selling inner-loop infill.",
   "repeatable", "Fifty homes a year on small sites, which is the mobility question for a printer.",
   "https://www.sandcastlehouston.com/about-sandcastle/")],
 ["https://www.sandcastlehouston.com/about-sandcastle/"],
 ["Scattered infill is the hardest geography for a machine that has to be set up and taken down. "
  "Ask what a move between lots costs before quoting anything."]),

("HOU-067", "J. Patrick Homes", "Houston, 12 submarkets", "https://www.jpatrickhomes.com/",
 "Volume Builder of the Year, 12 submarkets",
 "Semi-custom builder founded in 1990, named Volume Builder of the Year at the Houston PRISM "
 "awards, selling from the $370,000s to the $900,000s across twelve submarkets including Sienna, "
 "Jordan Ranch, Artavia and The Woodlands Hills.",
 (2, 2, 1, 1),
 "A semi-custom builder that won a volume award and publishes no volume. Named purchasing and "
 "construction managers.",
 ("Twelve submarkets is wide for a builder this size, which spreads the plan set thin.",
  "No closings figure is published anywhere, so the machine question cannot be sized.",
  "Energy Star and Environments for Living certification, with whole-home dehumidifiers standard. "
  "A firm that pays for third-party verification has paid for something unproven before."),
 [("Tim Drone", "President"),
  ("Bo Banowsky", "Purchasing Manager"),
  ],
 [("Sienna, Jordan Ranch, Artavia, The Woodlands Hills", "Four master planned communities.",
   "repeatable", "Semi-custom plans repeated inside named communities rather than one-off design.",
   "https://www.jpatrickhomes.com/where-we-build/")],
 ["https://www.jpatrickhomes.com/about-j-patrick/", "https://www.jpatrickhomes.com/where-we-build/"],
 ["The four names come from a contact-data aggregator rather than the firm's own site, which "
  "publishes no leadership page. Confirm each before use."]),

("HOU-068", "Westin Homes", "Sugar Land", "https://www.westin-homes.com/",
 "Builds in Lago Mar, Del Bello Lakes, Meridiana and Sienna",
 "Founder-led semi-custom builder in Sugar Land, active only in Houston and Austin, with the "
 "widest footprint in the south suburban master planned communities of any builder screened.",
 (3, 2, 0, 2),
 "The widest footprint across the south suburban masterplans of any builder here, a named vice "
 "president of construction, and no published volume.",
 ("Lago Mar, Del Bello Lakes, Meridiana, Sienna, Legacy and Marvida. The same plans in six masterplans.",
  "No closings figure is published, so the fit cannot be sized. Two markets only.",
  "No method evidence. The published language is about plans refined over time, not construction."),
 [("Jason Golan", "President"),
  ("Diane Danilov", "Vice President of Land and Business Development")],
 [("Lago Mar, Del Bello Lakes, Meridiana", "Texas City, Manvel and Rosharon.",
   "repeatable", "Three south-suburban masterplans taking one plan set.",
   "https://www.westin-homes.com/"),
  ("Sienna and Marvida", "Missouri City and Cypress.",
   "repeatable", "Two more masterplans on opposite sides of the metro.",
   "https://www.westin-homes.com/")],
 ["https://www.westin-homes.com/about"],
 ["The construction and purchasing names come from a contact-data aggregator. The firm publishes "
  "no leadership page, so confirm before use."]),

("HOU-069", "Newmark Homes", "Katy", "https://newmarkhomes.com/",
 "483 closings in 2025, 511 in 2024",
 "Houston builder reconstituted in 2009 when former TOUSA executives bought the Newmark brand out "
 "of bankruptcy, now in more than twenty communities including Bridgeland, Elyson, Sienna, "
 "Meridiana and The Highlands.",
 (2, 2, 1, 2),
 "483 closings in 2025 across more than twenty communities and more than 150 plans. Real volume, "
 "spread thin.",
 ("More than 150 named plans across more than twenty communities. The plan set is the problem here.",
  "483 closings in 2025 and 511 in 2024. The volume supports machines; the dispersion does not.",
  "It runs a proprietary energy programme under its own name, and a separate custom division for "
  "one-off work, so the production line is deliberately kept separate."),
 [],
 [("Bridgeland, Elyson, Dunham Pointe", "Cypress, Katy and Cypress.",
   "repeatable", "Three of the largest masterplans in the metro, all taking Newmark product.",
   "https://newmarkhomes.com/"),
  ("Meridiana and Sienna", "Rosharon and Missouri City.",
   "repeatable", "The same builder on both sides of the metro.",
   "https://newmarkhomes.com/")],
 ["https://www.builderonline.com/firms/newmark-homes/"],
 ["No executive is named on the firm's own site and no LinkedIn company page was confirmed. For a "
  "builder closing 483 homes a year this is the largest contact gap in the set.",
  "The closings figures appear to cover Houston and Austin together rather than Houston alone."]),

("HOU-070", "Ravenna Homes", "Cypress", "https://ravennahomes.com/",
 "Seven communities, from the $500,000s",
 "Semi-custom builder in Cypress selling from the $500,000s across Artavia, Audubon, Bridgeland, "
 "Cross Creek West, The Highlands and The Woodlands Hills.",
 (2, 2, 0, 1),
 "Seven communities in the north and northwest growth corridor, from the $500,000s, with a named "
 "president and no published volume.",
 ("Seven communities, all in the north and northwest corridor, which keeps the plan set together.",
  "No closings figure is published. Price point above $500,000 implies volume below the machine band.",
  "No method evidence beyond energy efficiency and smart home options."),
 [("Stephen Najvar", "President")],
 [("Artavia, Audubon, The Highlands", "Conroe, Magnolia and Porter.",
   "repeatable", "Three Montgomery County masterplans taking the same product.",
   "https://ravennahomes.com/")],
 ["https://ravennahomes.com/"],
 ["No volume figure and no construction or purchasing lead identified."]),

("HOU-071", "Jamestown Estate Homes", "Houston, 16 communities",
 "https://jamestownestatehomes.com/",
 "About 75 homes a year, 82 floor plans",
 "Family builder founded in 2008 by Greg Hawes with his daughters, building about seventy-five "
 "homes a year from a catalogue of eighty-two plans across sixteen communities from Sienna to "
 "Montgomery.",
 (2, 3, 0, 1),
 "About seventy-five homes a year against eighty-two floor plans, which is close to one plan per "
 "house. Volume fits a machine; the catalogue does not.",
 ("Eighty-two plans for about seventy-five houses a year. The catalogue is wider than the output.",
  "About seventy-five homes a year, stated by the firm. One machine would carry most of it.",
  "No method evidence. The published build time is eight to ten months, which is the number a "
  "printed wall argument would have to move."),
 [("Greg Hawes", "Founder"),
  ("Katy Hawes", "Co-President"),
  ("Matt Norris", "Co-President")],
 [("Grand Central Park and Artavia", "Conroe. Seventy-foot lots from the $850,000s.",
   "repeatable", "Large-lot product in two Conroe masterplans.",
   "https://jamestownestatehomes.com/"),
  ("Sienna and Towne Lake", "Missouri City and Cypress.",
   "repeatable", "The same catalogue on the other side of the metro.",
   "https://jamestownestatehomes.com/")],
 ["https://jamestownestatehomes.com/about-us/",
  "https://jamestownestatehomes.com/why-choose-jamestown/"],
 ["The firm publishes an eight to ten month build time from design to completion. That is the "
  "cycle a printed wall has to shorten, and it is the clearest schedule target in the set."]),

("HOU-072", "Partners in Building", "Houston, build on your lot",
 "https://partnersinbuilding.com/",
 "More than 300 homes a year",
 "Custom builder founded in 1986, now closing more than 300 homes a year across Houston, Dallas, "
 "the Brazos Valley and Nashville on a build-on-your-lot model, with a formal vice president of "
 "purchasing.",
 (1, 3, 0, 2),
 "More than 300 homes a year and a vice president of purchasing, which almost no custom builder "
 "has. Every house is one-of-a-kind.",
 ("Build on your lot, one-of-a-kind by its own description. There is no plan set to repeat.",
  "More than 300 homes a year. The volume is there even if the repetition is not.",
  "No method evidence."),
 [("Jim Lemming", "Chief Executive Officer and Owner"),
  ("Dewey Hennessee", "Vice President of Purchasing")],
 [("Towne Lake, Harvest Green, Firethorne", "Cypress, Richmond and Katy.",
   "repeatable", "Community work alongside the build-on-your-lot business.",
   "https://partnersinbuilding.com/greater-houston/northwest/towne-lake")],
 ["https://partnersinbuilding.com/40th-anniversary"],
 ["A custom builder with a vice president of purchasing is rare. The "
  "role only exists where somebody is standardising something.",
  "Volume is spread across four markets in two states, so the Houston share is unknown."]),

("HOU-073", "Brohn Homes", "Austin, with a Houston division",
 "https://www.brohnhomes.com/",
 "Average build time of 3.5 months",
 "Clayton Properties Group builder, part of Berkshire Hathaway, that entered Houston by acquiring "
 "HistoryMaker Homes' Houston division and now sells across the north, west and south suburbs "
 "with a published average build time of three and a half months.",
 (3, 2, 2, 3),
 "A published average build time of three and a half months, which is the shortest on record here, "
 "and Berkshire Hathaway capital behind it. Purchasing may run through the parent.",
 ("Communities across the north, west and south suburbs on a plan set inherited from HistoryMaker.",
  "No Houston closings figure is published, and purchasing may sit with Clayton rather than locally.",
  "It publishes an average build time of three and a half months across all products. A firm that "
  "measures and publishes cycle time has already made schedule a competitive variable."),
 [("Roderick Flint", "Division President, Houston")],
 [("Houston debut by acquisition", "Bought HistoryMaker Homes' Houston division and kept its plans.",
   "schedule", "An average build time of three and a half months, published by the builder.",
   "https://communityimpact.com/sponsored/award-winning-brohn-homes-makes-major-houston-debut-what-it-means-for-the-community/")],
 ["https://communityimpact.com/sponsored/award-winning-brohn-homes-makes-major-houston-debut-what-it-means-for-the-community/"],
 ["Brohn sits under Clayton Properties Group, the homebuilding arm of Clayton Homes, which is "
  "owned by Berkshire Hathaway. Purchasing may run partly through the parent. Establish where the "
  "wall decision is made before spending time locally."]),

("HOU-074", "Smith Douglas Homes", "Houston, formerly Devon Street Homes",
 "https://www.smithdouglas.com/",
 "324 closings in 2022 as Devon Street",
 "Public builder that entered Houston in 2023 by acquiring Devon Street Homes, which had closed "
 "324 homes across fifteen communities the year before and controlled about 1,500 lots.",
 (3, 2, 1, 3),
 "324 closings across fifteen communities in the year before it was acquired, on standardised "
 "entry-level product. Now public, which usually moves purchasing upward.",
 ("324 homes across fifteen communities, on a standardised first-time-buyer product.",
  "The volume band fits, but the parent listed in January 2024 and purchasing may have centralised.",
  "The model is standardisation for entry-level buyers. That is not evidence of paying for a "
  "method that was new at the time."),
 [("Stephen Ray", "Founder of Devon Street Homes, continuing to direct the Houston division")],
 [("Fulshear Lakes", "Fulshear.", "repeatable",
   "Entry-level product in a Fort Bend masterplan.",
   "https://www.builderonline.com/builder-100/smith-douglas-homes-enters-houston-market-with-devon-street-homes-acquisition_o")],
 ["https://www.builderonline.com/builder-100/smith-douglas-homes-enters-houston-market-with-devon-street-homes-acquisition_o"],
 ["The 324-closings figure is 2022, before the acquisition. The Houston division was built from a "
  "local company rather than dropped in, so the local team may still hold the specification."]),

("HOU-075", "Risewell Homes", "Sunterra, Katy", "https://risewellhomes.com/",
 "Formerly The New Home Company",
 "The rebranded New Home Company, operating eleven divisions nationally, with a Houston division "
 "led by a named division president building in Sunterra.",
 (2, 2, 1, 3),
 "A national platform with a Houston division president who is a licensed engineer, building in Sunterra.",
 ("One Houston community confirmed, Sunterra. Too early to read the plan strategy.",
  "Eleven divisions nationally means purchasing scale above the band a single machine serves.",
  "The division president is a professional engineer, which is rare and matters for a method "
  "conversation."),
 [("Jennifer Keller, P.E.", "Division President, Houston"),
  ("Matthew R. Zaist", "President and Chief Executive Officer")],
 [("Sunterra", "Katy.", "repeatable",
   "A builder position in a 2,303-acre masterplan.",
   "https://risewellhomes.com/team")],
 ["https://risewellhomes.com/team",
  "https://members.ghba.org/memberdirectory/Details/risewell-homes-fka-new-home-co-1416702"],
 ["The rename from New Home Company is recent, so older coverage uses the previous name.",
  "A division president who is a professional engineer is the right person for a structural "
  "conversation and an unusual one to find at division level."]),

("HOU-076", "Imagination Homes", "Meridiana, Rosharon", "https://imaginationhomes.com/",
 "Entry-level, launched 2025",
 "New builder launched in 2025 on an explicitly attainable entry-level strategy, starting in the "
 "high $200,000s, that has joined the builder lineup at Meridiana.",
 (3, 3, 1, 1),
 "A 2025 startup built around attainable entry-level product with a curated plan set, now selling "
 "at Meridiana. No incumbent method to displace.",
 ("A deliberately narrow curated plan set aimed at first-time buyers and right-sizers.",
  "New and small. One machine would be most of the capacity.",
  "The strategy is explicitly about attainability, so a wall cost saving lands on the stated strategy."),
 [("Greg Grahmann", "Leads the company")],
 [("Meridiana", "Rosharon. Joined the builder lineup at a south-suburban masterplan.",
   "repeatable", "Entry-level product from the high $200,000s in an established masterplan.",
   "https://www.prnewswire.com/news-releases/imagination-homes-launches-breaks-ground-on-first-community-302539487.html")],
 ["https://www.prnewswire.com/news-releases/imagination-homes-launches-breaks-ground-on-first-community-302539487.html"],
 ["Launched in 2025 and headquartered in Dallas. No volume figure exists yet, which is expected "
  "rather than a gap.",
  ]),

("HOU-077", "Sitterle Homes", "San Antonio, building in Houston",
 "https://www.sitterlehomes.com/",
 "More than 100 plans across four markets",
 "Family-owned semi-custom builder founded in San Antonio in 1964, building in Houston at Lakes of "
 "Bella Terra West, Sunset Harbor at Towne Lake, Veranda and The Lagos at Aliana.",
 (2, 2, 0, 2),
 "Four Houston communities from a San Antonio base, with a named director of purchasing. Houston "
 "is the secondary market.",
 ("Four Houston communities out of a four-market footprint. The plan catalogue is shared across all four.",
  "No volume figure. Houston is secondary to San Antonio, so the local share is small.",
  "No method evidence."),
 [("Frank Sitterle, Jr.", "President and co-owner"),
  ("India Kinslow", "Director of Purchasing")],
 [("Lakes of Bella Terra West, Veranda, The Lagos at Aliana", "Richmond and Fort Bend.",
   "repeatable", "Three Fort Bend communities taking a shared plan catalogue.",
   "https://www.sitterlehomes.com/")],
 ["https://www.sitterlehomes.com/"],
 ["The purchasing director was sourced from a contact-data aggregator rather than the firm's own "
  "site. Confirm before use.",
  "Headquarters and most volume sit in San Antonio, so a Houston-only pitch may go to the wrong city."]),

("HOU-078", "GreenEco Builders", "Tavola, New Caney", "https://greenecobuilders.com/",
 "Orders windows per home to keep adopting newer products",
 "Green-building focused production builder in Tavola that uses radiant barrier roof decking and "
 "orders windows per house rather than per community so it can adopt newer energy products as they "
 "are released.",
 (2, 2, 2, 1),
 "A builder that changes its specification mid-community on purpose. Small, thinly documented, and "
 "the only one here whose stated reason for a purchasing choice is keeping the option to switch.",
 ("One confirmed community, Tavola in New Caney. The footprint is small.",
  "No volume figure and no leadership identified, so the fit cannot be sized.",
  "It orders windows per home rather than per community specifically so it can adopt newer energy "
  "products as they appear. That is a procurement habit built for method change."),
 [],
 [("Tavola", "New Caney. Radiant barrier roof decking, stated at up to 17 percent attic heat reduction.",
   "method_risk", "Radiant barrier decking specified ahead of code.",
   "https://www.har.com/blog_27737")],
 ["https://www.har.com/blog_27737",
  "https://newsroom.lennar.com/2025-02-10-Lennar-Completes-Acquisition-of-Rausch-Coleman-Homes"],
 ["No volume and no price band are published for the brand. The per-home window ordering is the "
  "only method evidence on record for the brand itself."]),
]
