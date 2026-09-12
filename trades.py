# -*- coding: utf-8 -*-
"""The contractor layer: firms that put up the wall for somebody else.

Why this layer exists. Greater Houston production builders do not self-perform
their walls. They buy the shell from a trade. So the firm that would own and run
a printer here is often not the builder whose name is on the sign, it is the
concrete, shell or framing contractor the builder hires, or the general
contractor that self-performs concrete. Twenty-two of those are screened here, twenty-one wall and shell contractors plus the Houston design-build firm that engineered the printed house in Spring Branch.

How the three counts are read for a contractor. Repetition asks whether the
firm puts up the same wall repeatedly inside one metro rather than a different
structure every time. Printer fit asks whether one or two printers would cover a
real share of the wall it puts up in a year, on the same bands as the builder
layer, with a firm whose purchasing sits at a corporate desk scored Partly for
the same reason a national builder is. Track record asks the same question it
asks everywhere: has this firm ever paid for a building method that was new at
the time.

A structural finding from the sweep, recorded because it shapes the layer.
Houston's structural concrete trade is almost entirely commercial and
industrial. Of the contractors screened, one publishes a standing residential
division, one publishes a residential slab line, and two name a multifamily
project. For most of these firms a printed house wall would be a new market,
not an extension of the one they are in. That is stated on each record rather
than smoothed over.

Excluded after checking, and recorded so nobody researches them twice. M&M
Erectors, Big 4 Erectors, Postel Erection Group and MSD Building Corp erect
panels but own no forming, rebar or placing crew, so a printer would replace a
trade they already buy from someone else. Ceco Concrete Construction
self-performs in Houston, but its product is cast-in-place high-rise formwork,
which a twelve-foot gantry does not serve. CapForm, Texcon, Bob Moore
Construction and CMC Construction Services work in Houston from offices in
Carrollton, Dallas, Grapevine and Fort Worth. C3S is a testing and engineering
lab, Pinnacle Structural Engineers and Bihner Chen are engineers, and Locke
Solutions and Flexicore of Texas manufacture precast in a plant, which competes
with a printer rather than calling for one. Rugged Robotics is a Houston
construction-robotics company whose published customers are all outside Texas.
"""

# Records that belong in the contractor section. The section is assigned before
# the count of holds, exactly as the builder sections are.
TRADES = {
    "HOU-101": "Keystone Concrete Placement",
    "HOU-102": "Harvey Cleary",
    "HOU-103": "Texas A&M Concrete",
    "HOU-104": "Botello Builders",
    "HOU-105": "Encore Concrete Construction",
    "HOU-106": "Greco Structures",
    "HOU-107": "Andrade Construction Companies",
    "HOU-108": "HTX Concrete",
    "HOU-109": "T&T Construction",
    "HOU-110": "Silver Spur Concrete Contractors",
    "HOU-111": "Building Concrete Solutions",
    "HOU-112": "ORION",
    "HOU-113": "Baker Concrete Construction",
    "HOU-114": "Rino Construction",
    "HOU-115": "Arch-Con Corporation",
    "HOU-116": "Burton Construction",
    "HOU-117": "Blazer Building",
    "HOU-118": "Leola Construction",
    "HOU-119": "M.L. Deer Construction",
    "HOU-120": "ICF Constructors",
    "HOU-121": "MAREK",
    "HOU-129": "CIVE",
}

# (id, name, region, url, key_stat, synopsis, scores, verdict, why triple,
#  principals, projects, sources, flags)
# scores: repeatability, machine_fit, innovation, capital_access  (0-3)
NEW_TRADES = [

("HOU-101", "Keystone Concrete Placement", "Houston, with Austin, San Antonio and College Station",
 "https://www.keystoneconcrete.com/",
 "1,500 craftsmen, 975,000 cubic yards a year",
 "Family-owned concrete placement contractor running three placement divisions, structural, "
 "commercial and residential, plus sitework and utilities, with its own placing booms, hydraulic "
 "self-jacking formwork systems and tower cranes.",
 (3, 2, 2, 3),
 "The only concrete contractor screened that publishes a standing residential division. It already "
 "buys its own formwork systems and placing booms.",
 ("Three standing placement divisions in one metro, so the same work recurs rather than arriving "
  "one project at a time.",
  "1,500 craftsmen and 975,000 cubic yards a year on the firm's own count. One or two printers "
  "would be a line inside the business rather than the business.",
  "It owns a fleet of placing booms and multiple complete hydraulic self-jacking formwork systems "
  "on its own account. Buying capital equipment to change how concrete gets placed is the habit "
  "this count is looking for, though formwork is not a new method."),
 [],
 [("Residential concrete placement", "Its own residential page places custom home foundations, "
   "master plan communities, and large additions and flatwork.",
   "repeatable", "Master plan communities is production housing, which is the repeated foundation a "
   "printed wall would stand on.",
   "https://www.keystoneconcrete.com/residential"),
  ("Driscoll Apartments", "Named on the firm's own structural placement page.",
   "repeatable", "Multifamily placement work, the closest published example of a repeated wall on its record.",
   "https://www.keystoneconcrete.com/")],
 ["https://www.keystoneconcrete.com/", "https://www.keystoneconcrete.com/residential"],
 ["No executive is named anywhere on the firm's own site. Its contact page says only that it is a "
  "member of the Stewart family of companies.",
  "The residential page names no client and no project, so the size of that division is unknown.",
  "It states that it owns its pump fleet and runs a yard in every location, which is the equipment "
  "posture a machine purchase would sit inside."]),

("HOU-102", "Harvey Cleary", "Houston, with Austin, San Antonio, Denver and Washington",
 "https://www.harveycleary.com/",
 "$2 billion in volume, 700-plus employees, founded 1957",
 "General contractor founded in 1957 that self-performs an unusually deep set of structural trades "
 "through IQI Construction LLC, described on its own site as a captured company and solely owned "
 "and operated entity, and that runs a standing residential market alongside its commercial work.",
 (3, 2, 1, 3),
 "It owns formwork, rebar, place and finish, tiltwall erection, architectural precast and tower "
 "crane erection, and it builds apartments. No other firm screened discloses that much owned trade.",
 ("A standing residential market inside the firm, with multifamily buildings delivered repeatedly "
  "alongside the commercial work.",
  "$2 billion in construction volume and more than 700 employees on the firm's own count. One or "
  "two printers would be a line inside a business that size rather than the business.",
  "No method statement on record. Owning the equipment and the crews is not the same as having "
  "paid for a method that was new at the time."),
 [("David E. Harvey Sr.", "Founder, named on the firm's own about page"),
  ("David Harvey Jr.", "Took ownership in 1987, named on the firm's own about page"),
  ("Joseph Cleary", "Took ownership in 1987, named on the firm's own about page")],
 [("IQI Construction LLC", "The captured entity that performs the self-perform scope, named on the firm's own site.",
   "repeatable", "The crews and the equipment already sit inside the company rather than being hired in.",
   "https://www.harveycleary.com/self-perform-work/"),
  ("The Cooper Apartments", "Named on the firm's own residential market page as a 72-unit multifamily "
   "building with a fitness center and rooftop amenity space.",
   "repeatable", "A 72-unit apartment building is the repeated wall a printer serves.",
   "https://www.harveycleary.com/markets/residential/"),
  ("Camden Conte, Brava, The Watermark at Houston Heights", "Further residential buildings named on "
   "the firm's own site.",
   "repeatable", "Residential is a standing market here, not a one-off.",
   "https://www.harveycleary.com/markets/residential/")],
 ["https://www.harveycleary.com/self-perform-work/",
  "https://www.harveycleary.com/markets/residential/",
  "https://www.harveycleary.com/about-us/"],
 ["The current officer roster is not published. The firm names its founders and the two men who "
  "took ownership in 1987, and nothing below that.",
  "Its residential work is apartments and senior living rather than for-sale houses, so the wall "
  "is a multifamily wall."]),

("HOU-103", "Texas A&M Concrete", "Houston, Harris",
 "https://www.texasamconcrete.com/",
 "79 panels and 52,116 square feet of tilt-up wall on one job",
 "Turnkey concrete contractor that supplies, forms, places and finishes its own work, with a "
 "tilt-up record carried in the Tilt-Up Concrete Association's own project archive.",
 (3, 2, 1, 2),
 "Two award-listed tilt-up jobs in Houston, one at 79 panels and 52,116 square feet of wall. "
 "Panels repeat; the buildings behind them do not.",
 ("Tilt-up panel production repeats inside one metro even when the buildings differ.",
  "The firm's own site gives a job range of $500,000 to $15 million. A printer would be one line "
  "in a book that size.",
  "No method statement on record. Its published involvement is in concrete standards committees, "
  "not in new methods."),
 [],
 [("TCC Multi-Family Interiors", "Houston. 79 panels, tallest 43 feet 6 inches, 52,116 square feet of "
   "tilt-up wall, built January to December 2019. Tilt-Up Achievement Award 2020.",
   "repeatable", "A panel count at that scale is the volume a printed wall has to beat on cost per square foot.",
   "https://tilt-up.org/projects/profile/?id=5900")],
 ["https://www.texasamconcrete.com/", "https://tilt-up.org/projects/profile/?id=5900"],
 ["The firm's own site names no executive and no employee count. Earlier trade coverage carried "
  "both; those figures are from 2014 and are not repeated here.",
  "No residential or multifamily work appears anywhere on its own site."]),

("HOU-104", "Botello Builders", "Houston, working Harris, Fort Bend, Brazoria and Montgomery",
 "https://www.botellobuilders.com/",
 "150-plus employees, founded 2007 by three brothers",
 "Self-performing concrete subcontractor that grew from three people to more than 150 in office "
 "and field, covering foundations and piers, tilt-up walls, retaining walls and slabs on metal "
 "deck across four counties.",
 (3, 3, 1, 2),
 "A 150-person self-performing concrete sub, still owned by the three brothers who started it. One "
 "or two printers would cover a real share of the wall it puts up.",
 ("Tilt-up and foundation work repeating across four counties from one Houston yard.",
  "150 office and field staff on the firm's own count. That is the only published size in this "
  "section, and at that size one or two printers cover a real share of a year's wall.",
  "No method statement on record. Its published work is conventional tilt-up and foundations."),
 [("Eleazar Botello", "Founder, named on the firm's own site"),
  ("Eden Botello", "Founder, named on the firm's own site"),
  ("Jose Botello", "Founder, named on the firm's own site")],
 [("Keating Toyota of Manvel", "Manvel, Brazoria. July 2020.",
   "repeatable", "Retail and automotive shells are the repeat tilt-up product.",
   "https://www.botellobuilders.com/"),
  ("Fall Creek MOB", "Humble, Harris. February 2020.",
   "repeatable", "Medical office shell, another repeated tilt-up form.",
   "https://www.botellobuilders.com/")],
 ["https://www.botellobuilders.com/"],
 ["The firm began on residential work and moved to commercial. A printed house wall would be a "
  "return to a market it left, not a new one.",
  "No title is published for any of the three founders beyond founder."]),

("HOU-105", "Encore Concrete Construction", "Spring, Harris and Montgomery",
 "https://www.encoreconcrete.com/",
 "Employee-owned, and lists elevated multifamily as a project type",
 "Commercial concrete contractor established in 2017, carrying a 100 percent employee-owned mark "
 "on its own homepage, with tilt-up warehouses, data centres and elevated multifamily buildings in "
 "its published project types.",
 (3, 3, 1, 2),
 "Employee-owned, so the capital decision is made inside the company. Elevated multifamily is one "
 "of the seven project types it publishes.",
 ("Tilt-up warehouses, retail centres and schools repeating inside the Houston market.",
  "No crew count or annual volume is published. The one published job runs to 32 panels across four "
  "floors. On the bands, a firm with no annual figure is a Partly.",
  "No method statement on record. The 2025 tilt-up award is for execution, not for a new method."),
 [],
 [("Modern Heart and Vascular", "Humble, Harris. 100,962 square feet, 32 panels, four floors. "
   "Tilt-Up Achievement Award 2025. General contractor Arch-Con Corporation.",
   "repeatable", "A four-storey panel job. The evaluation report for a printed wall covers walls to twelve feet.",
   "https://tilt-up.org/projects/profile/?id=6722"),
  ("Elevated multifamily buildings", "Named as one of seven project types on the firm's own site.",
   "repeatable", "Housing work published by the firm itself rather than inferred.",
   "https://www.encoreconcrete.com/")],
 ["https://www.encoreconcrete.com/", "https://tilt-up.org/projects/profile/?id=6722"],
 ["No executive is named on the firm's own site.",
  "No multifamily project is named. The project type is published; a built example is not.",
  "Established 2017, so the track record is nine years."]),

("HOU-106", "Greco Structures", "Houston, working Harris and Fort Bend",
 "https://grecostructures.com/",
 "49 panels, tallest 52 feet 7 inches, on one job",
 "Concrete subcontractor inside the Satterfield and Pontikes family of companies, working for "
 "general contractors across elevated post-tensioned decks, mass concrete and tilt-up, with an "
 "award-listed panel record at the top of the height range the trade attempts and multifamily "
 "among the markets it lists.",
 (3, 2, 1, 3),
 "Panels at 52 feet and elevated post-tensioned decks. The work repeats inside one metro and is "
 "bought by general contractors rather than by owners.",
 ("Panel and deck work recurring across Houston projects for a standing set of general contractors.",
  "No crew count or annual volume is published, and the purchase would clear through the parent's "
  "self-perform group rather than through Greco. On the bands, both of those are a Partly.",
  "No method statement on record."),
 [("Trey Green", "Senior Vice President, Self Perform Group, Satterfield and Pontikes, named on the "
   "parent's own team page as overseeing Greco Structures, Rollcon, Rocket Pumping and Westway"),
  ("George A. Pontikes Jr.", "Chief Executive Officer and Chairman, Satterfield and Pontikes")],
 [("HCC West Houston Expansion", "Katy, Harris. 49 panels, tallest 52 feet 7 inches, 45,000 square feet "
   "of tilt-up wall on a 125,000 square foot building. Tilt-Up Achievement Award 2022.",
   "repeatable", "The evaluation report for a printed wall reaches twelve feet. These panels are four times that.",
   "https://tilt-up.org/projects/profile/?id=6324")],
 ["https://grecostructures.com/", "https://tilt-up.org/projects/profile/?id=6324",
  "https://www.satpon.com/approach/spfc/", "https://www.satpon.com/about/team/"],
 ["Greco's own site names no officer and publishes no crew count or annual volume. The parent's "
  "site is where the people are.",
  "The parent describes Greco as a turnkey commercial concrete contractor operating throughout "
  "Texas, running for more than thirty years and established under the Greco name about ten years "
  "ago, with a pumping arm of two pump trucks.",
  "Greco lists multifamily among its markets but names no multifamily project."]),

("HOU-107", "Andrade Construction Companies", "Houston, working Harris and Brazoria",
 "https://andradeconstructioncompanies.com/",
 "Owns earthwork, utilities and concrete",
 "Self-performing subcontractor across three scopes at once, earthwork, utilities and concrete, "
 "carrying small and minority business certification and membership of the Tilt-Up Concrete "
 "Association, the American Concrete Institute and the American Society of Concrete Contractors.",
 (2, 3, 1, 2),
 "It owns the earthwork, the utilities and the concrete on the same site, so a printer would stand "
 "on a slab its own crews poured.",
 ("Site and concrete packages recurring across Houston jobs, though the buildings themselves differ.",
  "No crew count, revenue or annual volume is published. On the bands, a firm with no published "
  "figure is a Partly.",
  "No method statement on record."),
 [("Victor Andrade", "Founder, named on the firm's own about page as having started the firm in 2003")],
 [("Mesa Apartments", "Utilities package, named on the firm's own site.",
   "repeatable", "Multifamily site work, which puts the firm on housing jobs already.",
   "https://andradeconstructioncompanies.com/")],
 ["https://andradeconstructioncompanies.com/"],
 ["No crew count or revenue is published.",
  "Its published housing exposure is site utilities, not wall work.",
  "A second web presence, andradeconcrete.com, carries the name Andrade Concrete and Construction "
  "and is a placeholder page with no address, services or people. A chief operating officer is held "
  "on LinkedIn under that second name. Whether the two are one business is unsettled."]),

("HOU-108", "HTX Concrete", "Houston, working Harris, Fort Bend and Brazoria",
 "https://htxconcrete.com/",
 "Names a garden-style multifamily project on its own site",
 "Turnkey commercial concrete and site development contractor that calls tilt-wall panels its own "
 "specialty and publishes a multifamily category alongside retail, industrial and institutional "
 "work.",
 (2, 3, 1, 2),
 "One of two contractors screened that names an actual multifamily project on its own site. The "
 "published work is paving-heavy.",
 ("Commercial shells and paving across the metro. The published square footages are weighted to "
  "paving rather than to wall.",
  "No annual volume is published. The one published wall figure is 12,000 square feet of tilt wall "
  "against 155,000 gross square feet of paving on the same job.",
  "No method statement on record."),
 [],
 [("Cypress Creek Lakes Apartments", "Cypress, Harris. Described on the firm's own site as a luxury "
   "garden-style multifamily development, designed by Meeks and Partners.",
   "repeatable", "Garden-style multifamily is the repeated wall a printer serves best.",
   "https://htxconcrete.com/"),
  ("Center at Pearland Parkway", "Pearland, Brazoria. 12,000 square feet of tilt wall and 155,000 "
   "gross square feet of paving.",
   "method_risk", "The ratio of paving to wall in the published work is the thing to test on the call.",
   "https://htxconcrete.com/")],
 ["https://htxconcrete.com/"],
 ["No executive is named on the firm's own site.",
  "Across the published projects the paving square footage is many times the tilt wall square "
  "footage. Confirm how much wall it actually puts up in a year."]),

("HOU-109", "T&T Construction", "Pasadena, Harris",
 "https://tandtconstruction.com/",
 "65 employees, 1,000-plus Houston projects since 1969",
 "Third-generation family concrete and civil contractor established in Pasadena in 1969, running "
 "site work, tilt-wall building construction and industrial pads, and owning its ready-mix "
 "delivery through Taylor Made Concrete on volumetric mixers.",
 (2, 3, 2, 2),
 "It owns the mix as well as the placing. A printer is fed concrete continuously, and this firm "
 "delivers its own.",
 ("Industrial and commercial concrete recurring across the east side of the metro.",
  "65 employees on average and more than 1,000 Greater Houston projects since 1969, on the firm's "
  "own count. No annual wall figure is published, so this sits at a Partly.",
  "It bought volumetric mixers and stood up its own delivery arm rather than buying ready-mix from "
  "a plant. That is paying for a different way to get concrete to a site, though it is not a wall "
  "method."),
 [("Ryan Taylor", "Third generation, took leadership in 2001, named on the firm's own about page"),
  ("Jeff Taylor", "Second-generation co-owner, named on the firm's own about page"),
  ("Dianna Taylor", "Second-generation co-owner, named on the firm's own about page")],
 [("Taylor Made Concrete", "The firm's own concrete delivery arm, using volumetric mixers.",
   "method_risk", "Owning the mix is the part of a printed wall that is hardest to source on demand.",
   "https://tandtconstruction.com/")],
 ["https://tandtconstruction.com/about-us/", "https://tandtconstruction.com/taylormade/"],
 ["No residential or multifamily work appears on its own site.",
  "Two people carry T&T alongside RD DevCo and E&S Construction in one LinkedIn headline. Neither "
  "name appears anywhere on T&T's own site, so the group question is open."]),

("HOU-110", "Silver Spur Concrete Contractors", "Tomball and north Houston, Harris and Montgomery",
 "https://silverspurconcrete.com/",
 "Publishes a custom residential concrete line",
 "Third-generation design-build concrete and metal building contractor that manages design, labour "
 "and scheduling in house, carrying both tilt-wall construction and a named residential concrete "
 "line including engineered slabs.",
 (2, 3, 1, 2),
 "The only contractor screened that pairs tilt-wall with a published residential concrete line, "
 "including engineered slabs.",
 ("Commercial concrete and metal buildings recurring across the north side of the metro.",
  "No crew count, revenue or project size is published anywhere on the site. On the bands, a firm "
  "with no published figure is a Partly.",
  "No method statement on record."),
 [("Trent Mitchell", "Owner, named on the firm's own about page, after eighteen years selling "
   "ready-mix to the largest general contractors in Houston")],
 [("Custom residential concrete", "Named on the firm's own site, covering driveways, culvert "
   "installation, engineered slabs and retaining walls.",
   "repeatable", "A firm already pouring engineered residential slabs pours the surface a printer stands on.",
   "https://silverspurconcrete.com/")],
 ["https://silverspurconcrete.com/"],
 ["No crew count, revenue or project size is published. The completed-projects counter on the "
  "about page has a label and no number in it. The scale is unverified.",
  "The residential concrete pages would not load. The line is named in the navigation, with "
  "driveways, engineered slabs, barndominiums and retaining walls under it, but the detail is "
  "unread."]),

("HOU-111", "Building Concrete Solutions", "Houston, Harris",
 "https://www.bcshouston.com/",
 "Runs Revit, Tekla, AutoCAD and Navisworks in house",
 "Specialty concrete contractor working either as general contractor or as subcontractor across "
 "site concrete, foundations, tilt-wall and elevated concrete, and building three-dimensional "
 "working models for clash detection before it pours.",
 (2, 3, 2, 2),
 "A concrete subcontractor that models its own work in three dimensions before pouring it. A "
 "printed wall arrives as a model too.",
 ("Concrete packages recurring across Houston projects under both delivery models.",
  "No crew count, revenue or project size is published. Nothing on the site sizes the work, so on "
  "the bands this is a Partly.",
  "It bought and staffed a modelling stack, Revit, Tekla, AutoCAD and Navisworks, to plan its "
  "pours. A printed wall arrives as a model first, so the habit transfers, though modelling is "
  "not itself a building method."),
 [],
 [("Three-dimensional preconstruction modelling", "Named on the firm's own site, used for clash "
   "detection and preconstruction planning.",
   "method_risk", "The firm already works from a model rather than from a paper set.",
   "https://www.bcshouston.com/"),
  ("The Travis at 3300 Main and Gables Residential Westcreek", "Two multifamily buildings named on "
   "the firm's own work page, alongside hospital and parking structures.",
   "repeatable", "Apartment work already on the record, which most of this section does not have.",
   "https://www.bcshouston.com/our-work")],
 ["https://www.bcshouston.com/", "https://www.bcshouston.com/our-work"],
 ["No executive is named on the firm's own site and no crew count, revenue or project size is "
  "published. The president and vice president here are held from LinkedIn alone.",
  "Its about pages do not exist. Nothing on the site sizes the business."]),

("HOU-112", "ORION", "Houston, Harris",
 "https://www.oriongroupholdingsinc.com/",
 "257 panels and 175,820 square feet of wall on one job",
 "Turnkey concrete contractor, formerly TAS Commercial Concrete Construction, acquired in 2015 and "
 "rebranded under its listed parent in January 2024, covering place and finish, site preparation, "
 "layout, forming and rebar placement.",
 (3, 2, 1, 3),
 "The largest single panel production found in the metro, at 257 panels on one school. Purchasing "
 "now runs through a listed parent.",
 ("Panel production at the top of the metro's range, recurring across institutional and commercial "
  "work.",
  "The concrete business is large enough that a printer is a line item, and the capital decision "
  "sits with a listed parent rather than in Houston.",
  "No method statement on record."),
 [("Travis Boone", "Chief Executive Officer, Orion Group Holdings, quoted in the firm's own release "
   "of 29 January 2024")],
 [("Sam Houston High School", "Houston, Harris. 257 panels in four thicknesses, 175,820 square feet "
   "of tilt-up wall on a 338,969 square foot building. Tilt-Up Achievement Award 2019.",
   "repeatable", "A 257-panel job is the production rate a printed wall is measured against.",
   "https://tilt-up.org/projects/profile/?id=5900")],
 ["https://www.oriongroupholdingsinc.com/investors/press-release/2024/29-01-2024-120203346",
  "https://tilt-up.org/projects/profile/?id=5900"],
 ["The award-listed panel record was set under the TAS name before the rebrand.",
  "Purchasing sits inside a listed parent, so expect a corporate capital process rather than an "
  "owner's decision.",
  "No residential or multifamily work is published."]),

("HOU-113", "Baker Construction", "Houston industrial office, Harris, inside a national firm",
 "https://bakerconstruction.com/",
 "61 panels at 70 feet, the heaviest about 87 tons",
 "Concrete specialty contractor, formerly trading as Baker Concrete Construction, with a standing "
 "Houston industrial office inside a national business of more than 12,500 people, named as the "
 "concrete subcontractor on the tallest tilt-wall job under way in the metro.",
 (3, 1, 1, 3),
 "Named on a 61-panel job at 70 feet, with the heaviest panel at about 87 tons. That is the top of "
 "what the trade attempts here. The firm is national.",
 ("Panel and structural concrete work recurring across the Houston market.",
  "More than 12,500 people across the United States on the firm's own count, and first on a "
  "national ranking of concrete specialty contractors. A machine purchase at that size runs through "
  "a national desk, which the bands score as a No.",
  "No method statement on record. Working at the top of the panel size range is difficulty, not a "
  "new method."),
 [],
 [("Harris Health Central Fill Pharmacy", "Houston, Harris. 145,000 square feet, 61 panels at 70 feet, "
   "heaviest about 87 tons. General contractor Skanska, erector MSD Building Corp, owner Harris "
   "Health System. Completion expected August 2026.",
   "repeatable", "A four-storey tilt-wall job in Houston, well above what a printed wall is evaluated for.",
   "https://www.bisnow.com/houston/news/construction-development/skanska-overcomes-challenges-on-texas-sized-tiltwall-project-131013")],
 ["https://www.bisnow.com/houston/news/construction-development/skanska-overcomes-challenges-on-texas-sized-tiltwall-project-131013",
  "https://bakerconstruction.com/",
  "https://web.abchouston.org/03-00-00-Concrete/Baker-Concrete-Construction,-Industrial-461"],
 ["The firm's own site names no executive and no Houston office. The Houston address comes from a "
  "trade association listing.",
  "It is on the deck as the contractor on the metro's tallest tilt-wall job, not as a likely buyer. "
  "A firm of 12,500 people decides equipment centrally."]),

("HOU-114", "Rino Construction", "Katy, Harris and Fort Bend, with Austin",
 "https://rino-con.com/",
 "Operating since 1991, tilt-up its stated specialty",
 "General contractor, formerly Rosenberger Construction, whose stated specialty is tilt-up and "
 "which has historically self-performed concrete, working warehouse, office, healthcare, retail "
 "and church work across Houston and Central Texas.",
 (3, 2, 1, 2),
 "Thirty-five years of tilt-up as the stated specialty. Its own site puts the self-performed "
 "concrete in the past tense.",
 ("Tilt-up buildings recurring across two Texas metros since 1991, at 48 million square feet on "
  "its own count.",
  "48 million square feet since 1991 on the firm's own homepage. A second page still carries an "
  "older 38 million. No annual figure is published, so this sits at a Partly.",
  "No method statement on record."),
 [("Steve Salverino", "Chief Executive Officer, named on the firm's own leadership page"),
  ("Jacob Aswad", "President, named on the firm's own leadership page"),
  ("Justin Henderson", "Vice President, named on the firm's own leadership page")],
 [("TCC Multi-Family Interiors", "Houston, Harris. 79 panels, completed December 2019, with Texas A&M "
   "Concrete as the concrete contractor.",
   "method_risk", "On this job the panels were subcontracted, so the crew that would run a printer is "
   "not necessarily inside the company.",
   "https://tilt-up.org/projects/profile/?id=5900")],
 ["https://rino-con.com/", "https://rino-con.com/services/construction-types/tilt-wall-tilt-up-construction/",
  "https://tilt-up.org/projects/profile/?id=5900"],
 ["Its tilt-wall page reads that the firm self-performed its concrete work for many years, in the "
  "past tense, so whether it still owns concrete crews is the first thing to establish.",
  "The homepage says 48 million square feet and the tilt-wall page still says over 38 million. "
  "Both are anchored to 1991, so the second looks like a page that was not refreshed.",
  "Its tilt-up page lists single and multi-family residences among possible applications, but no "
  "residential project is named anywhere on the site. The one job with Multi-Family in its name is "
  "a two-storey corporate headquarters and a warehouse."]),

("HOU-115", "Arch-Con Corporation", "Houston, Harris",
 "https://www.arch-con.com/",
 "Reversed the standard tilt-wall sequence to save a month",
 "General contractor running eight divisions including Multifamily and Community, which published "
 "an account of erecting a building's steel diaphragm before its tilt-wall panels in order to pour "
 "concrete and panels at the same time.",
 (2, 2, 2, 3),
 "It published how it reordered a standard method to win a month of schedule. It buys its "
 "concrete rather than pouring it.",
 ("Eight divisions across commercial, retail, healthcare and multifamily. The buildings differ "
  "project to project.",
  "No annual volume is published. The one published job runs to 770,640 square feet, and the panels "
  "on it were poured by somebody else.",
  "It reordered the standard tilt-wall sequence on a 770,640 square foot job, setting a 275-ton "
  "lattice boom crane on the perimeter to avoid the slab, and published the result. That is "
  "method appetite rather than the purchase of a new method."),
 [("Michael G. Scheurich", "Founder and Chief Executive Officer"),
  ("Jason M. Cooper", "President"),
  ("Daniel J. O'Hare", "Chief Financial Officer")],
 [("Grand National MDC", "Houston, Harris. 770,640 square feet, developer Hines, taken from "
   "ground-breaking to dried-in in just over four months by reversing the panel sequence.",
   "method_risk", "The published reason for the change was schedule, which is the same argument a printed wall makes.",
   "https://www.arch-con.com/steel-before-panels")],
 ["https://www.arch-con.com/", "https://www.arch-con.com/steel-before-panels"],
 ["It does not own concrete crews. On its award-listed tilt-up job the panels were poured by "
  "Encore Concrete Construction, also screened here.",
  "No multifamily project size is published."]),

("HOU-116", "Burton Construction", "Houston, with Austin, San Antonio and Phoenix",
 "https://burtonconstruction.com/",
 "Founded 2004, with multifamily in its published portfolio",
 "General contractor founded in 2004 covering office, mixed-use, medical, industrial, retail, "
 "hospitality and multifamily, carrying a 2024 Tilt-Up Achievement Award on its own about page.",
 (2, 2, 1, 2),
 "Twenty-two years old, founder still named, a tilt-up award in 2024 and multifamily in the "
 "published portfolio.",
 ("Commercial and multifamily work across four metros. The buildings differ project to project.",
  "No revenue, crew count or project size is published. On the bands, a firm with no published "
  "figure is a Partly.",
  "No method statement on record. The tilt-up award is for execution."),
 [("Brad Burton", "Founder, named on the firm's own about page")],
 [],
 ["https://burtonconstruction.com/"],
 ["Self-perform scope is not stated on the firm's own site, so whether it owns concrete crews is "
  "unconfirmed.",
  "No multifamily project is named and no revenue or crew count is published."]),

("HOU-117", "Blazer Building", "Houston, Harris, with Texas growth markets",
 "https://www.blazerbuilding.com/",
 "Over 44,000 apartment homes in 45-plus years",
 "Houston-headquartered multifamily general contractor building suburban garden-style, medium "
 "density mid-rise and high-density mid-rise over concrete podium, plus wrap-style parking, "
 "working through trade partners rather than self-performing.",
 (3, 2, 1, 3),
 "Over 44,000 apartment homes and 200-plus projects. Garden-style apartments repeat the same wall "
 "more than any other product here.",
 ("Garden-style and mid-rise apartment buildings repeating across Texas markets from a Houston "
  "office.",
  "Over 44,000 apartment homes in 45 years, so the wall volume is there. It states that it works "
  "through trade partners rather than self-performing, so the machine would sit with a subcontractor "
  "rather than with Blazer.",
  "No method statement on record. The only construction-method language on the site is the list of "
  "building types it builds."),
 [("Chris Richardson", "Listed under Senior Leadership on the firm's own team page"),
  ("Chad Hillman", "Listed under Senior Leadership on the firm's own team page"),
  ("Matt Fuqua", "Listed under Senior Leadership on the firm's own team page"),
  ("Brian Henderson", "Listed under Senior Leadership and Construction Supervision on the firm's own team page")],
 [("Hartwood at Spring Shadows", "Houston, Harris. Named on the firm's own project pages.",
   "repeatable", "A Houston garden-style community, which is the wall a printer would repeat.",
   "https://www.blazerbuilding.com/projects/spring-shadows/")],
 ["https://www.blazerbuilding.com/who-we-are/", "https://www.blazerbuilding.com/what-we-build/"],
 ["It states that it works through trade partner relationships rather than self-performing, so it "
  "would buy the printed wall rather than run the machine.",
  "The team page groups names under headings without printing a title beside each. No individual "
  "title is recorded here.",
  "No annual unit rate is published, only the cumulative total."]),

("HOU-118", "Leola Construction", "Houston division, working Harris, Fort Bend, Montgomery and Waller",
 "https://leolaconstruction.com/houston/",
 "9,900 homes a year company-wide, across 300 communities",
 "Shell contractor whose Houston division carries slab masonry, wood framing and drywall on single "
 "family and townhome communities, delivering the whole wall package under one contract through a "
 "network of more than 900 subcontractors.",
 (3, 1, 1, 2),
 "It sells the entire wall package to production builders, which is the procurement a printed wall "
 "would displace. It owns almost no direct field labour.",
 ("Single family and townhome communities across the north and west of the metro, taking the same "
  "wall package community after community.",
  "9,900 homes a year on the firm's own count, company-wide across Florida and Texas, far above "
  "what one or two printers cover. It also counts more than 900 subcontractors and no direct field "
  "crew, so there is nobody inside the firm to put on a machine.",
  "No method statement on record."),
 [],
 [("Houston division", "Named on the firm's own site as partnering with builders and developers on "
   "single family and townhome communities in Katy, Cypress, Sugar Land, Conroe and The Woodlands.",
   "repeatable", "The wall package for production housing, sold as one contract.",
   "https://leolaconstruction.com/houston/")],
 ["https://leolaconstruction.com/houston/", "https://leolaconstruction.com/"],
 ["It counts more than 900 subcontractors and no direct field crew, so there is no crew to redeploy "
  "onto a machine.",
  "Headquarters and ownership sit in Florida, so a Houston equipment decision would be made "
  "elsewhere.",
  "About thirty names appear on the firm's own about page without titles beside them. None is "
  "recorded here."]),

("HOU-119", "M.L. Deer Construction", "Houston, Harris, and the Texas Gulf Coast",
 "https://www.mldeer.com/",
 "Carries insulated concrete form buildings as a standard offering",
 "Commercial general contractor and construction manager of more than 25 years that publishes five "
 "building types it offers, prefabricated metal, tilt-wall, masonry, insulated concrete form and "
 "conventional wood frame, and that also installs gantry, jib, bridge and portal cranes.",
 (2, 3, 2, 2),
 "It already sells a concrete wall system to commercial clients, and it installs gantry cranes. "
 "A printer is a gantry that places concrete.",
 ("Commercial buildings across the Gulf Coast. The structures differ project to project.",
  "No revenue, crew count or project count is published. On the bands, a firm with no published "
  "figure is a Partly.",
  "It carries insulated concrete form construction in its standard menu alongside tilt-wall and "
  "masonry, so it has sold and built a concrete wall system rather than only a wood one. No named "
  "project is published to date it."),
 [],
 [("Crane installation", "The firm installs gantry, jib, bridge and portal cranes, named on its own site.",
   "method_risk", "A printer is a gantry. The firm already puts them up for other people.",
   "https://www.mldeer.com/houston-commercial-construction-icf-buildings")],
 ["https://www.mldeer.com/houston-commercial-construction-icf-buildings", "https://www.mldeer.com/"],
 ["No executive is named on the firm's own site, and no revenue, crew count or project count is "
  "published.",
  "It builds commercial work only. No residential project appears on the site.",
  "No insulated concrete form project is named, so the offering is published but not dated."]),

("HOU-120", "ICF Constructors", "Katy, Harris and Fort Bend, and the Texas coast",
 "https://icfconstructors.com/",
 "Crews trained on 12 form systems, ICF since 2002",
 "Insulated concrete form installer and shell contractor whose crews are full-time employees "
 "trained in no less than twelve different brands and types of insulated concrete form, working "
 "custom homes, safe rooms, condominiums and light commercial.",
 (3, 2, 3, 1),
 "Twenty-four years building concrete walls instead of wood ones, with its own crews. The only "
 "contractor screened whose whole business is a non-conventional wall.",
 ("The same wall system, installed again and again across Houston and the coast since 2002.",
  "No crew count or homes-a-year figure is published. On the bands, a firm with no published "
  "figure is a Partly, and that is the first thing to establish on the call.",
  "Its entire business is a wall method that was new when it adopted it. The crews are trained on "
  "twelve form systems and run a twenty-step checklist before every placement."),
 [("Matt Zetlmeisl", "Owner, named on the firm's own homepage as having owned and operated it since 2002")],
 [("Rockport rebuild", "Rockport, Aransas. Insulated concrete form used for all exterior walls and "
   "the suspended floor slab, 4,375 square feet of living space on 6,700 square feet of form, "
   "25 days of installation, 300 cubic yards of concrete, floor elevated 14 feet above mean flood "
   "level on more than 40 poured-in-place columns.",
   "method_risk", "On the coast the wind and water case for a concrete wall is already made.",
   "https://icfmag.com/2020/02/hurricane-harvey-rebuild/")],
 ["https://icfconstructors.com/about/", "https://icfconstructors.com/projects/",
  "https://icfconstructors.com/financial-strength/", "https://icfmag.com/2020/02/hurricane-harvey-rebuild/"],
 ["No crew count, revenue or homes-a-year figure is published anywhere, including on the page "
  "about the firm's financial strength, which describes high business volume without a number.",
  "Its named markets run from Houston to Corpus Christi, Dallas and McAllen, so Houston is one of "
  "several. Confirm how much of the work is local."]),

("HOU-121", "MAREK", "Houston, Harris, with Austin, Dallas and Fort Worth",
 "https://www.marekbros.com/houston/",
 "Runs its own prefabrication plant, founded 1938",
 "Specialty wall contractor founded in 1938, self-performing drywall assemblies, ceilings, "
 "fireproofing, insulation and paint, with a standing multifamily division, a standing single "
 "family division, and a warehouse on the edge of Houston producing prefabricated wall panels.",
 (3, 2, 2, 3),
 "It already owns a prefabrication plant and runs separate multifamily and single family "
 "divisions, with a named leader on each. The walls it builds are interior, not structural.",
 ("Interior wall and ceiling packages repeating across multifamily and single family work in one "
  "metro.",
  "No employee count or annual unit figure is published. On the bands, a firm with no published "
  "figure is a Partly.",
  "It built and staffed a prefabrication plant producing wall panels and interior components "
  "offsite, and publishes what that saved on a hospital project. That is paying to move wall work "
  "into a factory, which is the nearest thing to the argument for a printer."),
 [("Phil Nevlud", "Division President"),
  ("Ronald Marek", "Multifamily Director"),
  ("Chris Trojanowsky", "Single Family Division Manager"),
  ("Jorge Rodriguez", "Managing Director, Field Operations")],
 [("Prefabrication plant", "A warehouse in an industrial park on the edge of Houston producing "
   "prefabricated wall panels and interior components.",
   "method_risk", "The firm already runs a factory that makes walls, which is the capability a printer needs.",
   "https://www.marekbros.com/the-future-is-factory-built/")],
 ["https://www.marekbros.com/houston/", "https://www.marekbros.com/the-future-is-factory-built/"],
 ["Its walls are interior and non-structural. A printed exterior wall would be a new trade for the "
  "firm, not an extension of the one it holds. Say so rather than glossing it.",
  "No employee count or annual unit figure is published."]),
]


# Builders and owners found in the same sweep whose wall is already not wood.
# These belong in the builder flow, not the contractor section, because they
# build the house rather than the wall for somebody else.
NEW_METHOD = [

("HOU-122", "Everlasting Homes Building Group", "Houston, Harris",
 "https://www.everlastinghomesgroup.com/",
 "Six Houston homes on structural concrete insulated panels",
 "Custom builder whose walls, floors and roofs are one structural concrete insulated panel system, "
 "high-density expanded polystyrene with continuous steel wire mesh and high-strength shotcrete, "
 "with six named Houston projects and national recognition for a flood-ready house.",
 (1, 2, 3, 2),
 "It already builds every wall out of concrete instead of wood, and has six Houston houses to show "
 "for it. The work is custom, so no two plans repeat.",
 ("Custom luxury houses, each designed for its site. Nothing repeats.",
  "No annual volume is published. On the bands, a firm with no published figure is a Partly.",
  "Its entire product is a concrete wall system that was new to this market when it adopted it. It "
  "has paid for the method, promoted it on television, and had a house recognised for it."),
 [("Franck Boursier", "Chief Executive Officer and co-founder, named in the firm's own media coverage"),
  ("George Mock", "General Manager, named in trade coverage of the Braesvalley house")],
 [("Braesvalley Estate", "Houston, Harris. A 4,700 square foot house on the structural concrete "
   "insulated panel system, designed with a nine-foot lower floor built to flood and be repurposed "
   "rather than raising the existing house.",
   "method_risk", "A flood answer built into the wall, which is the argument a printed wall makes here.",
   "https://www.greenbuildermedia.com/blog/prefab-3d-modular-panels-built-for-tough-houston-weather")],
 ["https://www.everlastinghomesgroup.com/",
  "https://www.greenbuildermedia.com/blog/prefab-3d-modular-panels-built-for-tough-houston-weather",
  "https://www.fox26houston.com/news/concrete-homes-natural-disasters"],
 ["No annual volume, revenue or employee count is published.",
  "It builds a concrete wall system already, so a printer would replace a method it has invested "
  "in rather than a method it dislikes. That cuts both ways on the call."]),

("HOU-123", "Tiona Homes", "Greater Houston, Harris",
 "https://www.tionahomes.com/",
 "Builds only in insulated concrete form",
 "Residential builder that builds every home in insulated concrete form, serving both individual "
 "buyers and organisations running larger housing projects, and controlling the forming material "
 "as well as the build through its parent.",
 (2, 2, 3, 2),
 "Every house it builds has a concrete wall. It controls the forming material as well as the "
 "build, which is also the reason to check what it would be giving up.",
 ("One wall system across Greater Houston. The plans are not published, so repetition is partial.",
  "No volume figure is published. On the bands, a firm with no published figure is a Partly.",
  "It builds only in insulated concrete form, and its parent produces and licenses the block "
  "system. The method is the business."),
 [("Steve Ross", "Founder and Chief Executive Officer"),
  ("Jacob Ross", "Product Manager"),
  ("Victor Ramos", "Construction Leader")],
 [("Insulated concrete form programme", "Named on the firm's own about page as the system it builds "
   "every home with, outperforming wood on strength, energy efficiency and resilience.",
   "method_risk", "A builder whose walls are already concrete has made the argument to its own buyers.",
   "https://www.tionahomes.com/aboutus")],
 ["https://www.tionahomes.com/aboutus", "https://www.onsite-icf.com/aboutus"],
 ["It is a division of Onsite ICF, which produces and licenses its own foam-block wall system. A "
  "printer would compete with the product the parent sells. Read the relationship before the call.",
  "No volume, crew count or completed-home figure is published anywhere."]),

("HOU-124", "Seaside Construction", "Galveston, Galveston County",
 "https://seaside-construction.com/",
 "Adopted insulated concrete form in 2019 for coastal work",
 "Custom coastal builder on Galveston Island that moved to insulated concrete form in 2019 because "
 "of moisture, salt air, driving rain and hurricanes, and carries the insulated concrete form "
 "category in the Greater Houston Builders Association directory.",
 (1, 2, 3, 2),
 "It changed its wall method seven years ago, on purpose, because of the coast. Custom work, so no "
 "plan repeats.",
 ("Custom beach houses, each one different.",
  "No annual volume is published. On the bands, a firm with no published figure is a Partly.",
  "It adopted insulated concrete form in 2019 and states the coastal reasons for the change on its "
  "own site."),
 [],
 [("Coastal insulated concrete form programme", "Galveston. Adopted in 2019 against moisture "
   "infiltration, salt air corrosion, driving rain, heavy winds and hurricanes.",
   "method_risk", "The wind and water case for a concrete wall is already made to its buyers.",
   "https://seaside-construction.com/icf-home-construction/")],
 ["https://seaside-construction.com/icf-home-construction/",
  "https://members.ghba.org/memberdirectory/Search/builder-icf-insulated-concrete-forms-homes-132766"],
 ["No executive is named with a title on the firm's own site. One contact name appears without one.",
  "No annual volume or completed-home count is published."]),

("HOU-125", "Nautilus Custom Homes", "Houston, Harris",
 "https://www.nautiluscustomhomes.com/",
 "Built extensively in insulated concrete form and structural insulated panels",
 "Custom builder of zero energy ready homes whose construction lead has built in wood, steel, "
 "insulated concrete form and structural insulated panels, and whose predecessor firm built, "
 "installed and distributed the forms for an award-winning Houston house.",
 (1, 2, 3, 2),
 "Its predecessor firm compared seven wall systems before choosing one, and won a national award "
 "for the house that came out of it. The award evidence is a decade old.",
 ("Custom houses designed one at a time.",
  "No annual volume is published. On the bands, a firm with no published figure is a Partly.",
  "The predecessor firm examined around 300 products and at least seven wall systems before "
  "selecting insulated concrete form, and the resulting Houston house was certified three ways and "
  "won Best Large Residential at the 2014 national awards."),
 [("Ker Thomson", "Founder and Designer, named on the firm's own about page"),
  ("Jim Kuchenbrod", "Construction lead, named on the firm's own about page")],
 [("Ker Thomson Home", "Houston, Harris. Insulated concrete form walls with triple-pane "
   "hurricane-rated windows, certified by IBHS Fortified, LEED Platinum and Zero Energy Ready, and "
   "winner of Best Large Residential at the 2014 National ICF Builder Awards.",
   "method_risk", "A builder that compared seven wall systems before choosing one has done the comparison before.",
   "https://buildblock.com/ker-thomson-home-houston-tx-triple-certified-ibhs-usgbc-doe-house-country/")],
 ["https://www.nautiluscustomhomes.com/about-us",
  "https://www.icfmag.com/2015/09/durable-energy-builder-home/",
  "https://buildblock.com/ker-thomson-home-houston-tx-triple-certified-ibhs-usgbc-doe-house-country/"],
 ["The method evidence dates from 2014 and 2015 and was earned under the predecessor name, Durable "
  "Residential Builders. Confirm the firm is still building before spending time.",
  "Insulated concrete form is one of several wall methods it uses, not the only one."]),

("HOU-126", "Aura Dwellings and Hospitality", "Houston, Harris",
 "https://www.auradwellings.com/",
 "Factory-built modular homes and accessory dwellings",
 "Architect-founded modular builder on Clinton Drive producing factory-built homes, accessory "
 "dwelling units and hospitality units, with a published product line and starting prices from "
 "$99,000 for the smallest accessory unit.",
 (2, 2, 3, 1),
 "It moved its wall production into a factory and publishes the price list.",
 ("A published product line rather than one-off design, though no built volume is published.",
  "No annual volume is published. On the bands, a firm with no published figure is a Partly.",
  "Its whole model is factory-built construction rather than site framing. It has already paid to "
  "move wall production off the site."),
 [("Rame Hruska", "Co-founder and Chief Executive Officer, named in trade coverage")],
 [("Published product line", "ADU Cubo from $99,000, ADU Uno from $229,000, Rise Series from "
   "$370,000, Terrace Series from $362,000, Courtyard Series from $569,000.",
   "repeatable", "A published catalogue with fixed prices is the repetition a machine needs.",
   "https://www.auradwellings.com/")],
 ["https://www.auradwellings.com/",
  "https://www.greenbuildermedia.com/blog/prefab-3d-modular-panels-built-for-tough-houston-weather"],
 ["No project name, location or completion date appears on the firm's own site. Built volume is "
  "unverified.",
  "Volumetric modular is a competing offsite method, so a printer would replace an investment "
  "rather than fill a gap."]),

("HOU-127", "Live Lone Star", "Houston, working Harris and Brazoria",
 "https://livelonestar.com/",
 "Seven communities and about 3,000 lots in development",
 "Developer of factory-built home communities, with a flagship of 420 homes on 55 acres in "
 "Pearland and further communities under way in San Antonio and Hockley, selling homes from about "
 "$80,000 with a monthly lot rent.",
 (3, 1, 2, 2),
 "Its entire model is factory-built housing on land it controls. The product is delivered to the "
 "lot rather than built on it, which is the problem.",
 ("Seven communities and about 3,000 lots taking the same factory product.",
  "The homes are bought finished from manufacturers and set on a lot. A site printer does not "
  "serve that, whatever the volume.",
  "It built a business on factory-produced housing rather than site-built housing, though it buys "
  "the homes rather than making them."),
 [],
 [("The Landing at Pearland", "Pearland, Brazoria. 420 homes on 55 acres with a 6,000 square foot "
   "clubhouse, homes from about $80,000 to $170,000 and lot rent of $675 a month.",
   "repeatable", "One site absorbing 420 near-identical homes is the volume a machine wants.",
   "https://therealdeal.com/texas/houston/2023/03/10/live-lone-star-opens-its-first-manufactured-home-development/")],
 ["https://therealdeal.com/texas/houston/2023/03/10/live-lone-star-opens-its-first-manufactured-home-development/",
  "https://thelandingatpearland.com/"],
 ["It buys homes built to the federal manufactured housing code rather than building them on site. "
  "A printed site-built wall is a different regulatory product, not a substitute.",
  "No executive is named on the firm's own site or in the coverage.",
  "The community figures are from March 2023 and have not been refreshed."]),
]


# Two firms with a printed building on their record. Neither has a printed wall
# standing in Greater Houston, so neither joins the section that counts those.
# Boxer is an owner and takes its section from its counts. CIVE built the wall
# for somebody else, which is what the contractor section holds.
PRINTED_ADOPTERS = [

("HOU-128", "Boxer Property", "Houston, Harris",
 "https://www.boxerproperty.com/",
 "Paid for a printed house in Fort Worth",
 "Houston-headquartered commercial property owner and manager founded in 1992, overseeing more "
 "than 15 million square feet across 16 cities, which partnered on a printed house in Fort Worth "
 "and whose founder said in print that the future is printed houses made out of concrete.",
 (2, 2, 3, 3),
 "A Houston owner with 15 million square feet that has paid for a printed building, in Fort Worth, "
 "and said in print why.",
 ("Commercial buildings across sixteen cities. The product is not a repeated house plan.",
  "A portfolio this size could absorb a machine, though the firm is an owner rather than a builder "
  "and would hire the crew.",
  "It partnered on a printed house in Fort Worth with a printing contractor and its founder is on "
  "the record saying the future is printed concrete houses."),
 [("Andrew Segal", "Chairman and Chief Executive Officer"),
  ("Justin Segal", "President"),
  ("Blake Morris", "Chief Financial Officer"),
  ("John Rentz", "Vice President and General Counsel")],
 [("LoMa house", "100 West Bolt Street, Fort Worth, Tarrant. About 1,000 square feet, walls printed "
   "over seven to eight days in May 2024 on a printing contractor's machine, with Boxer as the "
   "development partner.",
   "method_risk", "The firm has already carried the risk of a printed building once.",
   "https://candysdirt.com/2024/05/28/you-can-see-a-3d-printed-home-get-built-in-fort-worth-right-now/")],
 ["https://www.boxerproperty.com/about-us/",
  "https://candysdirt.com/2024/05/28/you-can-see-a-3d-printed-home-get-built-in-fort-worth-right-now/",
  "https://www.voxelmatters.com/black-buffalo-3d-live-print-home-texas/"],
 ["No coverage after June 2024 confirms the Fort Worth house was completed. Treat completion as "
  "unverified.",
  "The printed house is in Fort Worth, not Houston. The firm is Houston-headquartered; the project "
  "is not."]),

("HOU-129", "CIVE", "Houston, Harris",
 "https://cive.com/",
 "Engineer and design-build partner on the printed house in Spring Branch",
 "Full-service design-build firm blending architecture, engineering and construction that "
 "collaborated with a printing contractor and an architect on a printed single-family residence in "
 "Spring Branch, described on its own site as the first of its kind in the United States.",
 (2, 2, 3, 2),
 "A Houston design-build firm that has already engineered and delivered a printed building. The "
 "technical staff to run a machine is already inside it.",
 ("Design-build projects, each one different.",
  "No headcount, revenue or annual project figure is published. On the bands, a firm with no "
  "published figure is a Partly.",
  "It engineered and delivered a printed house in Houston in collaboration with a printing "
  "contractor, and publishes the project on its own site."),
 [],
 [("Spring Branch printed residence", "Houston, Harris. Printing ran from July 2022 to May 2023, "
   "with CIVE as engineer and design-build partner alongside the printing contractor and the "
   "architect. The published size differs between sources and is not repeated here.",
   "method_risk", "A Houston firm outside the printing trade that has engineered a printed building.",
   "https://cive.com/us-first-multi-story-3d-printed-home-houston-tx/")],
 ["https://cive.com/us-first-multi-story-3d-printed-home-houston-tx/",
  "https://abc13.com/post/3d-printing-printed-homes-spring-branch-home-built-with-cive/12850103/"],
 ["Its own project page names no individual. A structural engineering lead was named in broadcast "
  "coverage of the house; confirm the title on the firm's own page before recording it.",
  "The published size of the house differs between the printing contractor's release and broadcast "
  "coverage, so no figure is carried here.",
  "The owner of the Spring Branch house is not published anywhere."]),
]


# Who signs for a machine at a contractor. At a builder the decision-maker is a
# vice president or director of construction, or the head of purchasing, because
# those roles can change a wall specification. At a contractor the specification
# is somebody else's; what this firm decides is whether to buy the equipment, and
# that is signed by the owner, the president or the division head. Those are the
# people marked here, and the difference is stated on the page.
TRADE_DECIDERS = {
    ("HOU-104", "Eleazar Botello"),
    ("HOU-104", "Eden Botello"),
    ("HOU-104", "Jose Botello"),
    ("HOU-106", "Trey Green"),
    ("HOU-110", "Trent Mitchell"),
    ("HOU-112", "Travis Boone"),
    ("HOU-115", "Michael G. Scheurich"),
    ("HOU-115", "Jason M. Cooper"),
    ("HOU-116", "Brad Burton"),
    ("HOU-120", "Matt Zetlmeisl"),
    ("HOU-121", "Phil Nevlud"),
    ("HOU-121", "Ronald Marek"),
    ("HOU-121", "Chris Trojanowsky"),
    ("HOU-122", "Franck Boursier"),
    ("HOU-122", "George Mock"),
    ("HOU-123", "Steve Ross"),
    ("HOU-125", "Ker Thomson"),
    ("HOU-126", "Rame Hruska"),
    ("HOU-128", "Andrew Segal"),
    ("HOU-128", "Justin Segal"),
}

# Where the title on file is not enough to say the person signs, the caveat goes
# on the contact rather than on the firm.
TRADE_DECIDER_NOTES = {
    "HOU-112": "Travis Boone runs the listed parent, not the Houston concrete business. The capital "
               "decision would sit with him; the work does not.",
}

# target_id -> [(name, role, linkedin_url, headline evidence, is_decider)]
# One LinkedIn pass, 12 September 2026, run in a signed-in session. The evidence
# is the search-result headline naming the person and the firm together, which is
# the same standard the builder layer holds to. Project managers, estimators,
# superintendents, safety and accounting are not recorded: they execute a
# specification rather than choose one.
TRADE_PEOPLE = {
    "HOU-101": [
        ("Scott Anderson", "Vice President, Keystone Structural Concrete",
         "https://www.linkedin.com/in/scott-anderson-266878141/",
         "Headline reads Vice President at Keystone Structural Concrete. Houston, Texas.", True),
        ("Rodney Horn", "Vice President, Keystone Concrete and Key-Scape",
         "https://www.linkedin.com/in/rodney-horn-963a8048/",
         "Headline reads Vice President at Keystone Concrete, LLC/Key-Scape Landscaping. Houston, "
         "Texas. Keyscape is the landscaping arm named on the firm's own site.", True),
    ],
    "HOU-102": [
        ("Scott Clarke", "Chief Operating Officer",
         "https://www.linkedin.com/in/scott-clarke-a2a1a521/",
         "Headline reads Chief Operating Officer at Harvey | Harvey-Cleary Builders. Houston, Texas.", True),
        ("Jarrod Portelance", "Project Director",
         "https://www.linkedin.com/in/jarrodportelance/",
         "Headline reads Project Director at Harvey | Harvey-Cleary Builders. Houston, Texas.", False),
    ],
    "HOU-103": [
        ("David Buzzelli", "Vice President",
         "https://www.linkedin.com/in/david-buzzelli-faci-77109b29/",
         "Headline reads Vice President of Texas A&M Concrete, LLC. Houston, Texas. He is also named "
         "as a founder in the firm's own dated news post.", True),
    ],
    "HOU-105": [
        ("Mark Scully", "President",
         "https://www.linkedin.com/in/mark-scully-596648201/",
         "Headline reads President at Encore Concrete Construction. Spring, Texas.", True),
        ("Tim Manherz", "Vice President",
         "https://www.linkedin.com/in/tim-manherz-9a2b62148/",
         "Headline reads Vice President at Encore Concrete Construction. Greater Houston.", True),
    ],
    "HOU-106": [
        ("Thomas Valentine", "Operations Manager",
         "https://www.linkedin.com/in/thomas-valentine-6b1a7b117/",
         "Headline reads Operations Manager at Greco Structures. Spring, Texas.", False),
        ("Jordan Lopez", "Business Development, Greco Structures and Rollcon",
         "https://www.linkedin.com/in/jordan-lopez-528225229/",
         "Headline reads Business Development Specialist for Greco Structures & Rollcon. Houston, Texas.", False),
    ],
    "HOU-107": [
        ("Eric Rice", "Business Development Manager",
         "https://www.linkedin.com/in/eric-rice-177124352/",
         "Headline reads Business Development Manager at Andrade Construction Companies. Houston, Texas.", False),
        ("Luis Andrade", "Chief Operating Officer, Andrade Concrete and Construction",
         "https://www.linkedin.com/in/luis-andrade-128317159/",
         "Headline reads COO at Andrade Concrete & Construction Inc., which is a different registered "
         "name from Andrade Construction Companies. Confirm the two are the same business.", False),
    ],
    "HOU-108": [
        ("J. Cameron Guinn", "Vice President, Business Development",
         "https://www.linkedin.com/in/j-cameron-guinn-2047686/",
         "Headline reads Vice President Business Development at HTX Concrete. Houston, Texas.", False),
        ("Tony Le", "Chief Estimator",
         "https://www.linkedin.com/in/tony-le-81ba0032/",
         "Headline reads Chief Estimator at HTX Concrete. Houston, Texas.", False),
    ],
    "HOU-109": [
        ("Ryan Taylor", "Owner",
         "https://www.linkedin.com/in/ryan-taylor-594162139/",
         "Headline reads Owner at T&T Construction. Greater Houston.", True),
    ],
    "HOU-111": [
        ("Trent Tellepsen", "President",
         "https://www.linkedin.com/in/trent-tellepsen-b8608024/",
         "Headline reads President at Building Concrete Solutions. Houston, Texas.", True),
        ("Daniel Lara", "Vice President",
         "https://www.linkedin.com/in/daniel-lara-24329570/",
         "Headline reads Vice President at Building Concrete Solutions. Houston, Texas.", True),
        ("Jorge Hernandez", "Manager of Operations",
         "https://www.linkedin.com/in/jorge-hern%C3%A1ndez-614616204/",
         "Headline reads Manager of Operations at Building Concrete Solutions. Houston, Texas.", False),
    ],
    "HOU-114": [
        ("Jeff Rager", "Senior Project Manager",
         "https://www.linkedin.com/in/jeff-rager-b0ab6a380/",
         "Headline reads Senior Project Manager, Rino (Rosenberger) Construction. Spring, Texas, and "
         "it carries both names, which confirms the rename.", False),
        ("James Abbate", "Controller",
         "https://www.linkedin.com/in/james-abbate/",
         "Headline reads Controller at Rosenberger Construction. Katy, Texas.", False),
    ],
    "HOU-118": [
        ("Chris Vogler", "Business Development Manager",
         "https://www.linkedin.com/in/chris-vogler-56239a52/",
         "Headline reads Business Development Manager at Leola Construction. Spring, Texas. He is the "
         "only Leola person in Greater Houston that a search returns.", False),
    ],
    "HOU-119": [
        ("Todd Riedel", "Chief Operating Officer",
         "https://www.linkedin.com/in/todd-riedel-2b37185/",
         "Headline reads COO at ML Deer Construction. Houston, Texas.", True),
        ("Jeff Raymer", "Executive Vice President",
         "https://www.linkedin.com/in/jeff-raymer-b29060a/",
         "Headline reads Executive Vice President at ML Deer Construction. Houston, Texas.", True),
    ],
    "HOU-129": [
        ("Hugo Domloj", "Founder and Chief Executive Officer",
         "https://www.linkedin.com/in/hachem-domloj/",
         "Headline reads Founder & CEO at CIVE, Inc. Houston, Texas.", True),
        ("Hikmat Zerbe", "Head of Structural Engineering",
         "https://www.linkedin.com/in/hikmat-zerbe-b3139669/",
         "Headline reads Head of Structural Engineering at CIVE. Houston, Texas. He is the person "
         "broadcast coverage quoted on the printed house in Spring Branch.", True),
        ("Clemente Barrera", "Vice President of Construction",
         None,
         "Headline reads Vice President of Construction at CIVE. Houston, Texas. No profile URL was "
         "captured in the pass.", False),
    ],
}

# Open items raised by the same pass.
TRADE_PEOPLE_FLAGS = {
    "HOU-106": "The parent's own site names Greco among the Satterfield and Pontikes family of "
               "companies, so the LinkedIn signal was right. The person who signs sits at the "
               "parent, in the self-perform group.",
    "HOU-109": "Neither RD DevCo nor E&S Construction appears anywhere on T&T's own site, so the "
               "group the LinkedIn headlines imply is unconfirmed.",
    "HOU-114": "Its own leadership page names a chief executive, a president and a vice president. "
               "LinkedIn returns only project managers and a controller under either firm name.",
    "HOU-118": "Only one Leola person in Greater Houston surfaces at all, in business development. "
               "The firm is Florida-owned and the leadership sits there.",
}
