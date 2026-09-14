# -*- coding: utf-8 -*-
"""Twenty-one firms that are not printer prospects and should be called first.

The roster screens firms against three counts and puts them on a grid. A
post-tension plant does not belong on that grid: it will never buy a printer,
and scoring it against printer fit is a category error dressed as rigour. Two
kinds of firm are in that position, and both are more useful than most of the
roster.

NODES sell to every crew in the metro. Six sweeps established that this trade
does not publish volume: of 87 candidates, five published a figure you could put
on an axis and twenty-four published years in business instead. Builders publish
closings because the Builder 100 makes them. Nothing makes a wall contractor
publish anything. So the volumes exist, and they exist at the supplier who
batches the concrete, fabricates the tendons or sells the block. Ready Cable
sells cable, rebar and lumber to the crews rather than competing with them, and
knows who pours what. That is worth more than a directory.

CREWS have the hands. A gunite crew already places cementitious material through
a hose onto a vertical surface, to a profile, with no formwork. Houston Gunite
advertises on its own careers page for nozzlemen, top finishers, bottom finishers
and foremen. That is the print crew roster, already trained, in a metro with one
of the largest pool industries in the country. None of these firms has the
balance sheet to buy a machine and every one of them has the people to run one.
The card has to say which of those two things it is.

NO_SITE is the third finding and the reason the slab cell on the roster is thin.
Six firms listed in the Greater Houston Builders Association's foundation and
concrete categories, and eleven masonry contractors on the Associated Masonry
Contractors of Houston roster, publish no website at all. They are not small by
inference; they are unlisted. This deck cannot screen them and says so rather
than pretending the roster is the market.
"""

# (key, name, kind, cell, region, url, line, why, people, note)
SUPPLY = [

# ------------------------------------------------------------------ the nodes
("ready-cable", "Ready Cable", "node", "slab",
 "Two Houston branches within eight Texas locations",
 "https://www.readycable.net/",
 "Supplies the full residential slab package, post-tension cable, rebar and "
 "lumber, to concrete contractors. Founded 1988.",
 "Sells to the pouring crews rather than competing with them, and supplies "
 "every part of a production slab. The single best source for which Houston "
 "crews pour at volume, which no directory publishes.",
 [], None),

("builders-pt", "Builders Post-Tension", "node", "slab",
 "Houston, Richey Road, plus Dallas-Fort Worth and Denver",
 "https://www.builderspt.com/",
 "A PTI Type I Category A certified plant supplying concrete reinforcement for "
 "residential slabs on ground.",
 "Nearly every production slab in Katy, Cypress, Conroe, Fulshear and Richmond "
 "is post-tensioned, and the tendons come from a plant like this one.",
 [], None),

("houston-pt", "Houston Post Tension", "node", "slab",
 "Houston, San Antonio Road",
 "https://www.houstonposttension.com/",
 "Post-tension cable, rebar and lumber for commercial, multifamily, single "
 "family, slab on grade and elevated projects. Established 1987.",
 "Nearly forty years of supplying both the residential and the elevated side, "
 "so it sees the whole slab market rather than one end of it.",
 [("Chris Myers", "Elevated Rebar and PT Division Manager")], None),

("suncoast-pt", "Suncoast Post-Tension", "node", "slab",
 "Houston headquarters, Northchase Drive, with plants nationally",
 "https://www.suncoast-pt.com/",
 "Unbonded post-tension with slab on ground as a named line, and in-house "
 "engineering producing field installation drawings.",
 "The only firm in the whole material sweep publishing proprietary product "
 "development of its own: the Suncoast Stud Reinforcement System and a barrier "
 "cable embed bracket. A supplier that engineers its own hardware is a supplier "
 "that will engage on a new method.",
 [], None),

("pts-texas", "Post-Tension Services of Texas", "node", "slab",
 "Houston plant on Aldine Westfield Road, Dallas headquarters",
 "https://post-tension.com/post-tension-foundation-company/",
 "A PTI Type I Category A plant serving Texas, Louisiana, Oklahoma, New Mexico "
 "and Colorado.",
 "Three named officers and a Houston plant. Worth knowing that its own page "
 "says it uses tried-and-true methods vetted over decades and is in business to "
 "cut cable, not corners. A good source and, on its own account, a poor "
 "prospect.",
 [("Derek Tuttle", "President"),
  ("Justin Zuckerbrow", "Vice President"),
  ("Brett Hunter", "National Sales Director")], None),

("core-supply", "Core Supply", "node", "slab",
 "Houston, Bammel Road, four Texas locations",
 "https://thecoresupply.com/",
 "A PTI Type I Category A plant doing rebar fabrication, post-tension, wood "
 "products and concrete accessories. Operating since 2010.",
 "The newest of the Houston post-tension plants, which usually means the one "
 "still winning accounts rather than defending them.",
 [], "Its own team page names nobody."),

("transco-rm", "TransCo Ready Mix", "node", "readymix",
 "Houston, multiple locations",
 "https://www.transcorm.com/",
 "A ready-mix producer founded in 2023 as a joint venture between TransCo Group "
 "and Rasmussen Group.",
 "A producer two years old is still building a book, which makes it the ready-"
 "mix call most likely to be taken and most likely to trial a mix.",
 [("Matt Fontenot", "General Manager"),
  ("Kyle DiNapoli", "Operations Manager"),
  ("Wade Carroll", "Sales Manager")], None),

("onsite-rm", "On-Site Concrete and Materials", "node", "readymix",
 "Greater Houston",
 "https://www.onsiteconcretetx.com/",
 "Volumetric mixing: batches at the job rather than at a plant, so the mix is "
 "controlled at the point of placement rather than made at a plant and "
 "delivered. Twenty-five years in Greater Houston.",
 "Technically the closest batching arrangement in the metro to a printer's "
 "feed, and the firm already says specialty mixes are what it is for.",
 [], None),

("alliance-rm", "Alliance Concrete Ready Mix and Materials", "node", "readymix",
 "Pinehurst and Porter, with Brookshire and Jacintoport under development",
 "https://alliancereadymix.us/",
 "Two plants batching 24 hours a day Monday through Saturday across north and "
 "northwest Greater Houston, to ASTM C94.",
 "Positioned exactly where the production growth is, and building two more "
 "plants, which means a company with capital and an appetite for new accounts.",
 [], "The site answered a stub to a script and was read by hand."),

("cemex-hsc", "Cemex USA, Houston Shell and Concrete", "node", "readymix",
 "Houston metro",
 "https://houston.cemexusa.com/",
 "The Houston Shell and Concrete brand now redirects to Cemex. Pours Vertua "
 "low-carbon concrete in the metro at scale.",
 "The only Houston ready-mix producer with a published low-carbon product "
 "actually poured here in quantity, which is the conversation a printed wall "
 "needs its material supplier to have already had.",
 [], "No Houston plant count could be confirmed: the site is behind a bot "
     "defence that returns an encoded blob to a script."),

("srm", "SRM Concrete", "node", "readymix",
 "Texas-wide including Houston",
 "https://www.smyrnareadymix.com/",
 "The largest ready-mixed producer in Texas after acquiring 82 plants and 11 "
 "volumetric mixer loading sites from Vulcan Materials.",
 "The eleven volumetric loading sites are the specific question: volumetric "
 "batching is the delivery method a printer feed most resembles.",
 [], None),

("texas-materials", "Texas Materials, a CRH company", "node", "readymix",
 "Eight Houston-area locations, two of which batch concrete",
 "https://texasmaterials.com/",
 "Asphalt and concrete plants at FM 529 in Houston and in Katy, plus crushed "
 "concrete, inside a group of more than 1,700 locations.",
 "A Katy batch plant sits inside the densest production housing corridor in "
 "the metro.",
 [], None),

("otto-cement", "Otto Cement", "node", "binder",
 "Houston, Market Street",
 "https://ottocement.com/",
 "A Houston-based binder trader carrying slag, gray and white cement, calcium "
 "aluminate cement, fly ash, aggregate and limestone, by truck, rail and barge.",
 "White cement and calcium aluminate cement in a Houston book is unusual, and "
 "calcium aluminate is the rapid-set chemistry a printed wall needs to stand up "
 "between layers.",
 [], None),

("nubuild-icf", "NuBuild ICF", "node", "icf",
 "Columbus, Texas, serving the Gulf Coast and Central Texas",
 "https://nubuildicf.com/",
 "A Nudura distributor that works through established and experienced "
 "contractors rather than installing itself.",
 "Its president built his own Nudura house before starting the distributorship, "
 "and a distributor who sells through crews can name every crew in Houston that "
 "actually sets an insulated form.",
 [("Ken Moore", "President"), ("Todd Moore", "CAD designer")], None),

# ------------------------------------------------------------------ the crews
("houston-gunite", "Houston Gunite", "crew", "nozzle",
 "Houston, Proctor Street",
 "https://houstongunite.net/",
 "A family-owned commercial and residential pool and spa shell contractor, "
 "serving Houston since 1984.",
 "Its own careers page advertises for nozzlemen, top finishers, bottom "
 "finishers, foremen and CDL drivers. That is the crew a printer needs, named "
 "and recruited by a firm that has been shooting concrete for forty years.",
 [], None),

("south-coast-gunite", "South Coast Gunite", "crew", "nozzle",
 "Houston to Beaumont, south to Galveston",
 "https://southcoastgunite.com/",
 "Family-owned gunite and shotcrete on custom pools, spas, rock features and "
 "structural work, over twenty years on the Gulf Coast.",
 "Runs both methods and does structural work as well as pools: commercial "
 "aquatic structures, engineered retaining walls and structural concrete that "
 "has to perform under load. Its own page draws the distinction cleanly, that "
 "gunite adds water at the nozzle and shotcrete is batched before the hose.",
 [], None),

("union-gunite", "Union Gunite", "crew", "nozzle",
 "Missouri City, Greater Houston",
 "https://www.uniongunite.com/",
 "Supply-and-install gunite and shotcrete, from backyard pools to large "
 "commercial projects, adept with both and publishing minimal rebound.",
 "Supply and install means one firm controls both the material and the nozzle, "
 "which is the whole operation a printer replaces.",
 [], None),

("united-gunite", "United Gunite", "crew", "nozzle",
 "Cypress, serving Katy, Sugar Land, Tomball, Humble and The Woodlands",
 "https://www.unitedgunite.com/",
 "Gunite placement for pool contractors, publishing real-time precise "
 "measurement of quantity used on each job.",
 "Instrumented placement. A crew already metering how much material goes into a "
 "shell in real time has the habit a printed wall's quality control depends on.",
 [], None),

("pool-works", "Pool Works", "crew", "nozzle",
 "Houston, West Tidwell, and Liberty Hill",
 "https://poolworkstx.com/gunite/",
 "A gunite subcontractor providing shell services to builders and contractors "
 "rather than building pools itself, over thirty years.",
 "Already sells nozzle work as a subcontracted service to other people's "
 "projects, which is the commercial shape of running a printer for a builder.",
 [], None),

("jr-pool-plastering", "JR Pool Plastering", "crew", "nozzle",
 "Four Houston locations",
 "https://jrpoolplastering.com/",
 "Gunite shell and plaster finish under one firm, serving Greater Houston for "
 "over forty years.",
 "Runs the shell and the finish coat, so it carries both the placement crew and "
 "the surface crew. Its own description of a gunite pool as one monolithic "
 "structure without seams or joints is the argument a printed wall makes.",
 [], None),

("ccp-shotcrete", "CCP Shotcrete and Pumping", "crew", "nozzle",
 "Austin yard, projects across Texas including Houston",
 "https://www.curtisconcretepumping.com/",
 "A shotcrete placement contractor for below-grade structural walls, culvert "
 "and tunnel linings, shoring, skateparks and architectural applications.",
 "The purest structural shotcrete description found anywhere in Texas: this is "
 "a firm whose business is already shooting structural wall rather than pool "
 "shells. Both owners work in the field.",
 [], "The yard is in Austin. The site names Houston among its project cities."),
]


# Firms that meet the profile on trade association category and geography and
# publish no website at all. Every one is a phone call. The pattern is the
# finding: the volume side of this trade is not on the internet.
NO_SITE = [
    ("Excell Foundation", "slab", "Conroe",
     "Listed by the Greater Houston Builders Association under both Turnkey "
     "Concrete and Foundations, and in the Texas Association of Builders "
     "directory. The dual turnkey listing is the strongest unconfirmed signal "
     "in the set."),
    ("Noble Concrete Construction", "slab", "Fulshear",
     "GHBA Concrete and Turnkey Concrete, and a Texas Association of Builders "
     "member."),
    ("Lexus Concrete", "slab", "Houston", "GHBA Foundations and Concrete."),
    ("Titan Foundations", "slab", "Conroe", "GHBA Concrete."),
    ("Caymex", "slab", "Montgomery", "GHBA Concrete and Foundations."),
    ("Alamo dba Dorsett", "slab", "Pasadena", "GHBA Concrete."),
    ("Ranch Masonry", "masonry", "Houston",
     "A contractor member of the Associated Masonry Contractors of Houston and "
     "of the Mason Contractors Association of America. No website in any search "
     "result."),
    ("Galindo and Boyd Houston", "masonry", "Houston",
     "AMCH member. The firm's own name carries Wall Systems."),
    ("Hoggatt", "masonry", "Pasadena",
     "AMCH member. The page title reads masonry fencing and hardscape, which "
     "suggests subdivision masonry fencing at volume."),
    ("BR Brick and Masonry", "masonry", "Houston",
     "Appears residential brick oriented, which is the production-homebuilder "
     "seam. The site sits in an http redirect loop."),
    ("D and H Masonry", "masonry", "Conroe and Spring", "Site in a redirect loop."),
    ("W.W. Bartlett", "masonry", "Houston", "AMCH contractor member."),
    ("Surock", "masonry", "Spring and Magnolia", "AMCH contractor member."),
    ("Paul Yeatts Enterprises", "masonry", "Houston", "AMCH contractor member."),
    ("Masonry Revival", "masonry", "Houston", "AMCH contractor member."),
    ("Ranch Stucco and Masonry", "masonry", "Houston", "AMCH contractor member."),
    ("Flexicore of Texas", "precast", "Houston",
     "Listed by the Texas precast association under building systems, building "
     "products and bridges, with AASHTO beams, structural precast, piles and "
     "marine structures. The site forces an https to http redirect no fetcher "
     "follows."),
    ("East Texas Precast", "precast", "Waller",
     "Same redirect loop. Waller County is next door to Legacy Precast's "
     "Brookshire plant."),
    ("Valley PreStress Products", "precast", "Eagle Lake",
     "No website. The trade directory names David Malaer and gives AASHTO I "
     "beams, deck slabs and box girders. About sixty miles west of Houston."),
    ("Whaley Concrete Pumping", "nozzle", "Houston",
     "An American Concrete Pumping Association listing and nothing fetchable."),
    ("Axis Pumping", "nozzle", "Houston", "Same."),
]
