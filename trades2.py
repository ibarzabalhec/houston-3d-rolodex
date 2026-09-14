# -*- coding: utf-8 -*-
"""The wall supply chain, Build 62.

Build 61 left the deck with 22 contractors, and a look at how they were found
explains what they were. Every one came through tilt-up.org project profiles,
because that is the one place in this trade where volume is public. The deck did
not choose tilt-up. The data chose it. Seventeen of the 22 scored Partly on
printer fit, which is what happens when you screen firms casting 87-ton panels
at 70 feet for a machine that prints a house wall.

Six sweeps went after the cells that were empty. The organising idea is the wall
value chain: who touches a wall between a cement plant and a finished house.

  binder     makes the cementitious material
  readymix   batches and trucks it
  nozzle     places it through a hose, including shotcrete and gunite
  slab       pours the horizontal, including the post-tension layer
  precast    casts the vertical off site
  panel      manufactures the vertical as a panel, any material
  masonry    lays the vertical unit by unit
  tiltup     casts the vertical flat on site and lifts it

Eighty-seven candidates came back. Thirty-one were cut. The bar is not sales
volume: five of the 87 publish a volume figure, so screening on volume selects
for having a marketing department and keeps the loud small firms while cutting
the large quiet ones. The bar is what a firm already owns, because a firm that
has financed heavy equipment has shown it can finance a machine, and unlike
revenue that evidence is on the page. A plant, a fleet, a certification that
required an audit, a parent with a capital process, or an executive bench.

The 28 below are the ones that cleared it. A twenty-ninth, Ecocast Homes, a
precast house-shell plant in Humble, was cut after the record was written: the
one page it cited now returns 404, the domain redirects to usaprecasthomes.com,
and the successor site carries neither the Humble plant nor the model this deck
had quoted. A record whose only source has gone does not ship. The nodes and the crews are not here,
because a post-tension plant is not a printer prospect and putting one on a grid
that measures printer fit is a category error. They are in supply.py.

A note on geography. Seven of these are plants outside the metro that sit inside
its supply radius. A plant is a fixed asset with a shipping distance, which is a
different fact from a contractor's service area, so each record states where the
plant is and what the firm says about its own market. Where a page does not
claim Houston, this file does not claim it either.
"""

# (tid, name, region, url, key_stat, synopsis, (rep, fit, innov, capital),
#  mvp_screen, (why_repetition, why_printer_fit, why_track_record),
#  people, projects, sources, flags)

WALL = [

# ==================================================================== precast
# Nine plants. Off-site production of structural wall, with capital equipment
# already on the books, a QC lab and a batch plant. The count that separates them is not repetition, which
# they all clear, but whether one or two printers would be a line inside the
# business or the business itself.

("HOU-137", "Legacy Precast",
 "Brookshire, Waller County, about an hour from downtown Houston",
 "https://www.legacyprecast.com/",
 "50-acre plant, batching well over 100 yards an hour",
 "Precast and prestressed building systems on a 50-acre plot in Brookshire, "
 "making wall panels, shear walls, spandrels, double tees, beams, columns and "
 "stairs for parking garages, industrial buildings, data centres and schools. "
 "Its own site names Houston, Dallas, Austin and San Antonio as its markets. "
 "Founded May 2013 by seven partners. It holds PCI plant certification from "
 "2014 and PCI architectural certification from 2018, and it published "
 "certified Environmental Product Declarations in June 2022, built on a full "
 "year of operating data from the Brookshire plant, to ISO 14025 and ISO 21930.",
 (3, 2, 2, 2),
 "A batch plant, casting beds, a quality regime, and a business built on making "
 "structural wall somewhere other than the site.",
 ("Eight certified structural product lines cast repeatedly on the same beds, "
  "in one plant, for one region.",
  "A plant batching well over 100 yards an hour is larger than one or two "
  "printers would cover. A machine would be a line inside it, not the business, "
  "which is the same reading a large builder gets.",
  "It published Environmental Product Declarations in 2022 before any customer "
  "required them, on its own operating data. Paying for a measurement nobody "
  "asked for is evidence of treating production method as a competitive "
  "question, though an EPD is not a new way of building."),
 [("Hussein Sinjari", "Vice President"),
  ("Charles Franke", "Chief of Estimating")],
 [("Environmental Product Declarations",
   "Certified EPDs first issued 3 June 2022, prepared to ISO 14025 and ISO "
   "21930 on a full year of operating data from the Brookshire plant.",
   "method_risk",
   "A producer that measures its own carbon before a customer asks is a "
   "producer that has already thought about how it makes things.",
   "https://www.legacyprecast.com/epd")],
 ["https://www.legacyprecast.com/", "https://www.legacyprecast.com/epd",
  "https://www.legacyprecast.com/about-us",
  "https://concreteproducts.com/index.php/2014/09/16/well-anchored/"],
 ["The 50-acre figure and the batching rate come from a 2014 trade profile of "
  "the plant's opening and have not been restated since.",
  "The PCI certification category is not published. The site says plant and "
  "architectural certification without naming the tier."]),

("HOU-138", "Wells, Pearland plant",
 "Pearland, Brazoria County",
 "https://wells.build/contact/locations/pearland-texas/",
 "32,000 square foot plant, 125-plus projects a year",
 "Hollowcore building systems from a plant on Veterans Drive in Pearland, with "
 "design assist through installation and maintenance, serving Houston, Austin "
 "and projects across the state. The plant carries C21 architectural "
 "certification. Wells is a top-three North American producer of architectural "
 "and structural precast, rolled up from heritage Wells, Gate Precast and "
 "Spancrete, running 13 production facilities. KPS Capital Partners agreed to "
 "acquire the company with closing expected at the end of March 2026.",
 (3, 2, 1, 3),
 "The only precast plant inside the Houston metro proper, and a narrow one: "
 "hollowcore is a single product line rather than a flexible casting yard.",
 ("One product made repeatedly in one plant for one region.",
  "A plant turning 125-plus projects a year is bigger than one or two machines "
  "would cover, and hollowcore is a plank product rather than a wall product, "
  "so a printer would serve a line the plant does not currently run.",
  "No record of paying for an unproven method. The published history is "
  "consolidation and certification, not experiment."),
 [("Dan Juntunen", "Chief Executive Officer, Wells")],
 [],
 ["https://wells.build/contact/locations/pearland-texas/",
  "https://concreteproducts.com/index.php/2026/02/10/private-equity-operator-kps-outlines-wells-acquisition-agreement/"],
 ["A private equity close expected March 2026 cuts both ways: capital appetite "
  "may rise, and so may the number of people who have to approve a purchase.",
  "No plant manager or local executive is named on the Pearland page."]),

("HOU-139", "Locke Solutions",
 "Houston, Almeda Genoa Road, with a second plant in Alvarado",
 "https://lockesolutions.com/",
 "41,750 square foot plant, four 50-ton bridge cranes",
 "Custom precast producer in south Houston with an underground tunnel system "
 "serving three production bays, working on stormwater, manholes, trench, pull "
 "boxes, spread footings, light pole bases, LNG and data centre work. It runs a "
 "mobile plant program that produces precast at the customer's own premises or "
 "active jobsite. The Texas precast association's directory categorises Locke "
 "under structural precast, insulated wall panels and hollow-core slabs, which "
 "the firm's own site does not confirm.",
 (3, 2, 3, 2),
 "A producer that already moves production to the point of use is solving the "
 "same problem a printer solves, from a Houston plant with cranes and bays.",
 ("Custom precast made repeatedly in one Houston plant across three production "
  "bays.",
  "The plant is large enough that a printer would be an added line rather than "
  "the business, and the product mix is utility structures rather than wall.",
  "It runs a mobile plant program, producing precast on the customer's own "
  "site rather than shipping it. Standing up production at the point of use is "
  "a paid-for change in how the product gets made."),
 [],
 [("Mobile plant program",
   "Locke can produce precast on the customer's premises or at an active "
   "jobsite rather than only in the plant.",
   "method_risk",
   "A producer that has already decided the factory should move to the job.",
   "https://lockesolutions.com/mobile-plants/")],
 ["https://lockesolutions.com/", "https://lockesolutions.com/about-us/",
  "https://lockesolutions.com/mobile-plants/"],
 ["The bulk of the published catalogue is drainage and utility product, which "
  "sits against this deck's wall bar. The plant and the mobile programme carry "
  "this record, not the product mix.",
  "The insulated wall panel line appears only in the trade association "
  "directory and not on the firm's own site.",
  "The site shows contacts without titles, so no executive is named here."]),

("HOU-140", "Tricon Precast",
 "Houston, Henry Road, with a second Texas plant",
 "https://www.triconprecast.com",
 "ACI and PCI Level 1 certified quality control",
 "Houston-headquartered precast producer running two Texas manufacturing "
 "facilities and operations offices in Florida, serving the Gulf Coast. The "
 "published product line is bridges and highways, precast substructures, "
 "retaining walls and sound walls, with an industrial division serving "
 "petrochemical, LNG, oil and gas, pipeline and power. Quality control teams "
 "hold ACI field, strength and aggregate certifications and PCI Level 1, and "
 "technicians carry NPCA production quality school certification. The "
 "facilities run SOTA batching equipment.",
 (3, 2, 1, 2),
 "A Houston precast plant with a certified QC regime and a batching line, on a "
 "product mix that is infrastructure rather than building wall.",
 ("Bridge and substructure elements cast repeatedly from two Texas plants.",
  "Two plants running certified batching is more capacity than one or two "
  "printers would cover, and none of the published product is building wall.",
  "No record of paying for an unproven method. The published position is "
  "certification and quality control."),
 [],
 [],
 ["https://www.triconprecast.com"],
 ["The firm's own site returned only metadata to a fetch. Everything here rests "
  "on the Texas precast association listing and the industrial division's site, "
  "so the record is thinner than it looks.",
  "No executive is named on any page that could be read."]),

("HOU-141", "Coreslab Structures (Texas)",
 "Cedar Park plant, with a project consultant covering Houston",
 "https://www.coreslab.com/locations/austin-texas-precast-concrete/",
 "The group's only Texas plant",
 "Architectural and structural precast for parking garages, cladding and total "
 "precast buildings, in the Texas market since 1988, from a plant on Anderson "
 "Mill Road in Cedar Park, which is the group's only Texas plant. It assigns "
 "project consultants by territory, "
 "and the Houston territory carries multifamily in the same title.",
 (3, 2, 1, 3),
 "The only precast producer screened whose own staffing names Houston and "
 "multifamily in one title.",
 ("A complete line of architectural and structural products cast repeatedly "
  "from one Texas plant since 1988.",
  "A plant serving the whole state from Cedar Park is larger than one or two "
  "printers would cover, and Houston is a sales territory rather than a "
  "production location.",
  "No record of paying for an unproven method."),
 [("Bruce Wardlaw", "Project Consultant, Houston, East Texas and Multifamily"),
  ("Garrett Weidman", "Sales Manager")],
 [],
 ["https://www.coreslab.com/locations/austin-texas-precast-concrete/",
  "https://www.coreslab.com/"],
 ["The plant is in Cedar Park, roughly 160 miles from Houston. Houston is "
  "covered by a named consultant, not by a facility.",
  "No plant acreage or annual output is published."]),

("HOU-142", "Heldenfels Enterprises, a Metromont company",
 "San Marcos and Corpus Christi plants",
 "https://heldenfels.com/",
 "85-acre plant in San Marcos",
 "Fabricates and installs precast prestressed structures for highway, marine, "
 "industrial and building construction, including prestressed wall panels, "
 "structural columns, box beams, bridge girders, piles, raker beams, seating "
 "risers and stairs. Metromont completed its acquisition of the firm on 15 "
 "December 2025, with Metromont's chief executive stating the addition expands "
 "its precast capabilities in the Texas market.",
 (3, 2, 1, 3),
 "The largest precast footprint inside Houston's supply radius, in the first "
 "year under a new parent, which is when a producer entertains new capability.",
 ("Prestressed elements cast repeatedly from an 85-acre yard for one region.",
  "Eighty-five acres of casting is well beyond what one or two printers would "
  "cover, and the product is infrastructure and stadium work rather than house "
  "wall.",
  "No record of paying for an unproven method on its own account."),
 [("Chad Petro", "Senior Vice President and General Manager")],
 [],
 ["https://heldenfels.com/", "https://heldenfels.com/about-us"],
 ["Neither the firm's own pages nor the acquisition release names Houston. It "
  "claims Texas-wide highway, marine and industrial coverage, and it built "
  "Reliant Stadium. Houston service is likely and is not quoted here.",
  "San Marcos is roughly 160 miles from Houston."]),

("HOU-143", "Tindall Corporation, Texas division",
 "San Antonio",
 "https://tindallcorp.com/",
 "40-acre plant, 190-plus employees",
 "Precast and prestressed construction elements including a precast modular "
 "cell line, serving data centre development and multi-use commercial across "
 "the south-central states from a 40-acre San Antonio facility operating since "
 "2008. The plant has nearly doubled production, and an expansion announced on "
 "14 July 2023 added 69 thousand square feet and about 150 people, taking it to "
 "180,000 square feet. Its general "
 "manager is quoted on the firm's own site on diversifying capability beyond "
 "average precast solutions.",
 (3, 2, 2, 3),
 "A precast producer running a volumetric modular line, with a general manager "
 "on record wanting to widen what the plant makes.",
 ("Structural elements and modular cells cast repeatedly from one plant for "
  "one region.",
  "Forty acres and 190 people is more capacity than one or two printers would "
  "cover, and the plant's product is commercial and data centre rather than "
  "house wall.",
  "It built a precast modular cell line, which is a different product from "
  "structural elements and required new moulds, new handling and a new market. "
  "Paying to add a production line is the habit this count looks for, though a "
  "modular cell is not a new building method."),
 [("Greg Elliott", "Vice President and General Manager, Texas")],
 [("Texas plant expansion",
   "Announced 14 July 2023: 69 thousand square feet added and about 150 team "
   "members, taking the plant to 180,000 square feet.",
   "schedule",
   "A plant in a capex posture is a plant whose management is already "
   "approving equipment.",
   "https://tindallcorp.com/tindall-texas-expansion/")],
 ["https://tindallcorp.com/",
  "https://tindallcorp.com/tindall-texas-expansion/",
  "https://tindallcorp.com/tindall-celebrates-over-a-decade-of-precast-production-in-texas/"],
 ["The plant is in San Antonio, roughly 200 miles from Houston, and no page "
  "names Houston. The stated market is the south-central states."]),

("HOU-144", "Wells, Hillsboro plants",
 "Hillsboro, two plants on North Waco Street",
 "https://wells.build/contact/locations/hillsboro-texas/",
 "102,000 combined square feet, 320-plus people",
 "Two plants on one street, one dedicated to architectural systems and one to "
 "structural systems, together 102,000 square feet with 320-plus team members "
 "and 30-plus projects a year, carrying AA architectural certification. The "
 "structural plant occupies about 25 acres of a 50-acre site, leaving the rest "
 "for expansion, and produces double tees, inverted T beams, lite walls, shear "
 "walls, columns, stairs and spandrels.",
 (3, 2, 1, 3),
 "A two-plant campus making both architectural and structural wall, with half "
 "its site still empty.",
 ("Wall and structural elements cast repeatedly across two dedicated plants.",
  "A hundred thousand square feet across two plants is beyond what one or two "
  "printers would cover.",
  "No record of paying for an unproven method."),
 [],
 [],
 ["https://wells.build/contact/locations/hillsboro-texas/"],
 ["The plant page names Texas and Oklahoma and does not name Houston. "
  "Hillsboro is roughly 240 miles away, which is at the outer edge of a precast "
  "shipping radius.",
  "The 25-acre and 50-acre site figures come from a 2017 trade profile written "
  "when the plant belonged to Gate Precast."]),

("HOU-145", "NAPCO Precast",
 "San Antonio, Low Bid Lane",
 "https://www.napcoprecast.com/",
 "500-plus projects since 1994",
 "Precast and prestressed products for parking structures, multi-family "
 "residential, commercial buildings and sports and entertainment, from a single "
 "San Antonio facility operating since 1994. Its own site counts more than 500 "
 "completed projects including more than 20 HEB stores, and more than 30 years "
 "of precast and prestressed experience.",
 (3, 2, 1, 2),
 "One of only two precast producers screened whose published markets include "
 "multi-family residential.",
 ("Parking structures and multi-family elements cast repeatedly from one plant "
  "since 1994.",
  "A single plant serving the whole state is larger than one or two printers "
  "would cover, though smaller than the multi-plant producers on this deck.",
  "No record of paying for an unproven method."),
 [],
 [],
 ["https://www.napcoprecast.com/"],
 ["Houston is not claimed anywhere on the site. San Antonio is roughly 200 "
  "miles away.",
  "No acreage, no output figure and no named leadership on any page read."]),

# ====================================================================== panel
# Nine firms that already manufacture wall off site and sell it to production
# builders. This cell has the business model closest to selling printed wall:
# the logistics, the builder relationship and the factory economics are solved.

("HOU-146", "Future Frame USA",
 "New Caney plant, Conroe office, Montgomery County",
 "https://futureframeusa.com/",
 "Automated wall panel line, 17,000 square feet",
 "An offsite manufacturer built for the Texas home builder, producing wall "
 "panels and floor trusses on intelligent high-capacity CNC machines accurate "
 "to within one sixteenth of an inch, on a stated claim of reducing "
 "construction time by roughly 30 percent. It describes its own product as a "
 "new design engineered method of framing offered as a precision alternative to "
 "stick framing. It is on the City of Houston's registered fabricator list for "
 "trusses and wall panels.",
 (3, 3, 3, 2),
 "An automated plant making wall for Houston production builders, at a size one "
 "or two machines would cover.",
 ("Wall panels made repeatedly for production builders inside one metro, from "
  "one plant.",
  "A 17,000 square foot plant serving Texas production builders is the scale "
  "where one or two machines would cover a real share of the wall it ships.",
  "It converted a plant to automated CNC panel production and sells the method "
  "itself as the product, against stick framing. Paying to replace a building "
  "method with a manufactured one is exactly what this count asks."),
 [("Shane McCullough", "President"),
  ("Glen Gilbert", "General Manager"),
  ("Brent Wheat", "Design Manager")],
 [("New Caney plant",
   "Expanded into a 17,000 square foot space in New Caney in 2023, running "
   "CNC machines accurate to within one sixteenth of an inch.",
   "repeatable",
   "An automated wall line already selling to Texas production builders.",
   "https://communityimpact.com/houston/lake-houston-humble-kingwood/business/2023/07/20/future-frame-usa-expands-into-17000-square-foot-space-in-new-caney/")],
 ["https://futureframeusa.com/", "https://futureframeusa.com/about-us/",
  "https://futureframeusa.com/meet-our-team/",
  "https://www.houstonpermittingcenter.org/media/2146/download"],
 ["No output figure, no headcount and no named builder customer is published."]),

("HOU-147", "Builders FirstSource",
 "Four Houston-area component plants: Conroe, Cut N Shoot, East Houston and Houston",
 "https://www.bldr.com/",
 "Four Houston-area component plants",
 "The largest supplier of building products and manufactured components in the "
 "country, operating about 570 locations in 43 states, with four component "
 "plants in the Houston area. Two of them, Conroe and Cut N Shoot, publish "
 "their facility type as trusses, wall panels and components. Its own annual "
 "report describes manufactured products as factory-built substitutes for "
 "job-site framing including wall panels, states that its manufacturing "
 "facilities use automated robotic truss lines, and that prefabricated "
 "components are engineered offsite using specialised equipment.",
 (3, 1, 2, 3),
 "The one counterparty in Houston already treating offsite prefabrication and "
 "robotic production as stated strategy in a filing.",
 ("Wall panels and components made repeatedly across four Houston-area plants "
  "for production builders in the same metro.",
  "Four plants inside a network of 570 locations is far beyond what one or two "
  "printers would cover, and purchasing at this scale sits at a national desk.",
  "It runs automated robotic truss lines and says so in its own annual report, "
  "and has invested in digital solutions around the offsite model. Automating "
  "production is the habit, though robotic trusses are an improvement on "
  "framing rather than a replacement for it."),
 [],
 [],
 ["https://www.bldr.com/products/manufactured-components",
  "https://www.bldr.com/location/conroe-tx-truss/CONRTXMF",
  "https://www.bldr.com/location/cut-n-shoot-tx-truss/CUTNTXMF",
  "https://www.sec.gov/Archives/edgar/data/1316835/000095017024018584/bldr-20231231.htm"],
 ["Two of the four Houston plant pages render only a corporate shell to a "
  "fetch, so the East Houston and Houston facility types are unconfirmed.",
  "No Houston-level executive is named. The filing gives no manufacturing "
  "facility count and no Texas properties table."]),

("HOU-148", "Trussway Manufacturing",
 "Houston headquarters, Alcorn Street",
 "https://trussway.com/products/",
 "About $340 million in sales, 1,000 employees",
 "A Houston-headquartered manufacturer of prefabricated wall panels, roof "
 "trusses, floor trusses, components and rough openings, weighted toward "
 "multifamily, founded 1972 and running six manufacturing facilities with "
 "about $340 million of annualised sales, 1,000 employees and more than 340 "
 "customer accounts. Builders FirstSource acquired it in 2022. Its own product "
 "page states that prefabricated wall panels save time on the job site, reduce "
 "waste and increase structural quality.",
 (3, 1, 1, 3),
 "A wall panel manufacturer headquartered in Houston, selling into the "
 "multifamily builders on this deck, now inside a national parent.",
 ("Wall panels made repeatedly from a Houston plant for multifamily builders "
  "in the same metro.",
  "Six plants and $340 million of sales is beyond what one or two printers "
  "would cover, and purchasing now sits with a national parent.",
  "No record of paying for an unproven method on its own account."),
 [],
 [],
 ["https://trussway.com/products/",
  "https://www.sbcacomponents.com/tmat-directory/trussway",
  "https://www.bldr.com/who-we-are/in-the-news/builders-firstsource-acquires-trussway"],
 ["Every figure here comes from the 2022 acquisition release and is "
  "enterprise-wide rather than Houston-plant level.",
  "The chief executive named in that release may no longer hold the title, so "
  "no person is carried on this record."]),

("HOU-149", "UFP Site Built",
 "Huntsville plant, about 70 miles north, within five Texas plants",
 "https://ufpsitebuilt.com/",
 "Five Texas plants, wall panels at Huntsville",
 "A component manufacturer whose Huntsville plant makes roof trusses, floor "
 "trusses, floor cassettes, wall panels, timber trusses and stair systems, one "
 "of five Texas plants alongside Hillsboro, Kyle, San Antonio and Temple. Its "
 "own offsite page argues the case for the model: wall panels let a builder "
 "stand walls with fewer people, on a shorter schedule, with less loose product "
 "stored on site.",
 (3, 2, 1, 3),
 "A wall panel plant 70 miles from Houston inside a parent that publishes "
 "offsite manufacturing as its stated argument.",
 ("Wall panels and cassettes made repeatedly from one Texas plant for builders "
  "across the region.",
  "One plant within five Texas plants is more capacity than one or two "
  "printers would cover, though a single plant is the closer end of that range.",
  "No record of paying for an unproven method. Manufacturing wall panels is "
  "this industry's ordinary business rather than an adoption, and the offsite "
  "argument on its site is marketing for the product it already sells."),
 [],
 [],
 ["https://ufpsitebuilt.com/our-locations",
  "https://ufpsitebuilt.com/our-locations/huntsville-tx",
  "https://ufpsitebuilt.com/woodsolutions"],
 ["The Huntsville page names Texas and surrounding areas and does not name "
  "Houston.",
  "No output figure, headcount or named executive is published for the plant."]),

("HOU-150", "Trussworks Operations",
 "Caldwell plant, about 90 minutes from Houston",
 "https://www.trussworksllc.net/",
 "Wall panels for production builder projects",
 "A component manufacturer with plants in Caldwell and Mabank, Texas, plus five "
 "more across Oklahoma, Missouri, Arizona, Arkansas and Colorado and one "
 "opening in Florida in January 2027. The published product line is roof "
 "trusses, floor trusses, wall panels, LVL beams and timber truss, and the "
 "stated customer segment is large-scale multifamily, commercial and production "
 "builder projects. It is on the City of Houston's registered fabricator list.",
 (3, 2, 1, 2),
 "A wall panel plant inside Houston's trucking radius whose own stated customer "
 "segment is production builders and multifamily.",
 ("Wall panels made repeatedly from one plant for production builders across "
  "the region.",
  "Two Texas plants inside a seven-plant group is more than one or two printers "
  "would cover, and Caldwell is a regional plant rather than a Houston one.",
  "No record of paying for an unproven method."),
 [],
 [],
 ["https://www.trussworksllc.net/", "https://www.trussworksllc.net/locations",
  "https://www.houstonpermittingcenter.org/media/2146/download"],
 ["No output figure, headcount, named executive or named customer is published.",
  "Registered with the City of Houston to fabricate, which is the only "
  "published evidence tying the plant to Houston jobs."]),

("HOU-151", "Texas Building Supply, a US LBM company",
 "Houston branch on Railhead Lane, panel plants in San Antonio, Taylor and Van Alstyne",
 "https://texasbuildingsupply.com/",
 "Wall panels trucked into a Houston branch",
 "The Texas banner for US LBM, formed from Oldham, Foxworth-Galbraith, JP Hart "
 "and Arrowhead Stairs and Trim. Its component line publishes interior and "
 "exterior wall panels in 2x4, 2x6, 2x8, 2x10 and 2x12 framing including raked "
 "and tall walls, roof trusses up to 14 feet tall and wood-webbed floor trusses "
 "up to 24 inches deep and 40 feet long. The three sites branded as component "
 "plants are San Antonio, Taylor and Van Alstyne, so the Houston location is a "
 "branch fed by out-of-market panel lines.",
 (3, 2, 1, 3),
 "Already trucks manufactured wall into Houston from plants elsewhere, which "
 "is the logistics problem a local machine removes.",
 ("Wall panels made repeatedly across three Texas plants and delivered into "
  "Houston.",
  "Three panel plants inside a national parent is more capacity than one or two "
  "printers would cover, and Houston is distribution rather than production.",
  "No record of paying for an unproven method."),
 [],
 [],
 ["https://texasbuildingsupply.com/products/components/",
  "https://texasbuildingsupply.com/locations",
  "https://uslbm.com/family_of_companies/texas-building-supply-3/",
  "https://www.houstonpermittingcenter.org/media/2146/download"],
 ["The Houston location is a sales and distribution branch, not a panel plant. "
  "The registered fabricator list carries the Taylor plant for wall panels, not "
  "the Houston address.",
  "No principals, figures or automation content published."]),

("HOU-152", "DSRS Steel",
 "Houston, Pleasantville Drive, plus San Antonio and Central Texas",
 "https://dsrssteel.com/",
 "A 150-home development on cold-formed steel",
 "A cold-formed steel framing contractor offering full turnkey framing covering "
 "plan review, engineering, fabrication, delivery, installation, inspections "
 "and closeout documentation, and separately selling engineered material "
 "packages for self-install. Its published range runs from three million dollar "
 "estates to 150-home subdivisions, including the McCann Park development in "
 "Houston, and it markets moisture-resilient storm-ready assemblies for the "
 "Gulf Coast and fast, predictable framing aimed at production builders.",
 (3, 3, 3, 2),
 "Already sold a Houston production builder a 150-home subdivision framed in "
 "something other than wood, and self-performs the installation.",
 ("A manufactured wall system installed repeatedly across Houston subdivisions "
  "and custom work in one metro.",
  "A firm framing subdivisions of this size, self-performing, is the scale "
  "where one or two machines would cover a real share of the wall it puts up.",
  "Its entire business is replacing site-framed wood with a manufactured "
  "system, sold to production builders on schedule and resilience. Carrying "
  "the engineering, fabrication and installation of a non-conventional wall is "
  "the adoption behaviour this count is looking for."),
 [("David S. R. Stevens", "Director"),
  ("Michael Henderson", "Head of Operations")],
 [("McCann Park Development",
   "A 150-home development in Houston named on the firm's own site.",
   "repeatable",
   "Production housing framed in cold-formed steel, which is a builder already "
   "sold on a manufactured wall.",
   "https://dsrssteel.com/")],
 ["https://dsrssteel.com/"],
 ["No years-in-business figure is published, so the firm's age is unknown.",
  "The 150-home development is named without a date or a builder."]),

("HOU-153", "Texas Lite Gauge Steel MFG",
 "Texas, Houston telephone exchange",
 "https://txlitegaugesteel.com/",
 "Prefab walls to plus or minus 0.3mm",
 "Custom light gauge steel design, supply and install, producing commercial "
 "stud and track, truss packages, prefab walls and, on request, residential "
 "prefab walls and trusses, to a stated factory tolerance of plus or minus "
 "0.3mm, on 25 years of construction experience. Its own site says the product "
 "can be used in both residential and commercial projects and that it ships "
 "anywhere in the continental United States.",
 (2, 3, 1, 1),
 "Manufactures and installs prefabricated wall to a published tolerance, at a "
 "size where a machine would be a real share of the business.",
 ("Prefabricated wall made and installed repeatedly, though the site names no "
  "market, no city and no repeat customer.",
  "A single-line steel fabricator is the scale where one or two machines would "
  "cover a real share of what it ships.",
  "No record of paying for an unproven method. A published factory tolerance "
  "is a manufacturing specification, not a change of method."),
 [],
 [],
 ["https://txlitegaugesteel.com/", "https://txlitegaugesteel.com/?loc=aboutcontent"],
 ["The site never states a city. It says only Texas-based, and the telephone "
  "exchange is a Houston one. The location is unconfirmed.",
  "No named principal, no headcount and no plant address."]),

# ==================================================================== masonry
# Five firms. Masonry is the trade a printed wall most directly displaces, and
# the deck carried none of it until now. The two that publish panelised or
# prefabricated masonry are the warmest conversations in the cell.

("HOU-155", "City Masonry",
 "Tomball, serving Texas and the Gulf Coast",
 "https://www.citymasonry.com/",
 "Over 4 million square feet of masonry in the past year",
 "A commercial, industrial and institutional masonry contractor founded in "
 "1988, working in brick, block and stone from veneer to load-bearing masonry. "
 "Its own about page publishes annual revenue of 20 to 40 million dollars and "
 "over four million square feet of masonry laid in the past year.",
 (3, 2, 1, 3),
 "The largest published masonry throughput in the metro, on load-bearing as "
 "well as veneer work, which is the wall a printer would replace.",
 ("Four million square feet of the same trade laid repeatedly across one "
  "region, on commercial and institutional work.",
  "Four million square feet a year is more wall than one or two printers would "
  "cover. A machine would be a line inside the business.",
  "No record of paying for an unproven method. The published position is craft "
  "and workforce training."),
 [("Paul McCurdy", "Chief Executive Officer"),
  ("Glenn Whitehead", "Chief Operating Officer"),
  ("Edwin Rosales", "Vice President of Operations")],
 [],
 ["https://www.citymasonry.com/", "https://www.citymasonry.com/about-us/",
  "https://www.citymasonry.com/team/"],
 ["Load-bearing masonry is named as a capability without a project to attach "
  "it to.",
  "The revenue figure is published as a 20 to 40 million dollar range, which "
  "is the firm's own banding rather than a number."]),

("HOU-156", "Dee Brown",
 "Tomball office, Richardson headquarters",
 "https://www.deebrowncompanies.com/",
 "Publishes prefabricated masonry wall systems",
 "A third-generation stone and masonry contractor founded 31 October 1955, "
 "with a Houston-area office in Tomball. Its published services include masonry "
 "load-bearing and non-load-bearing brick and CMU systems and prefabricated "
 "stone and masonry wall systems, supported by a 7,700 square foot fabrication "
 "facility and a fleet of repair trucks. Its own site states an interest in new "
 "ways to use terra cotta, porcelain, prefabricated materials and adhered "
 "veneers.",
 (3, 2, 2, 3),
 "The only masonry contractor screened that already sells a prefabricated wall "
 "system and says in its own words that it is looking for new ones.",
 ("Load-bearing and veneer masonry laid repeatedly across one region for seven "
  "decades.",
  "A firm of this age and reach puts up more wall than one or two printers "
  "would cover, and the prefabricated line is one product among many.",
  "It runs a 7,700 square foot fabrication facility producing prefabricated "
  "stone and masonry wall systems, which is capital spent to move wall "
  "production off the scaffold. It states an interest in prefabricated "
  "materials on its own site."),
 [("Robert V. Barnes III", "President and Chief Executive Officer"),
  ("Tim Hughes", "Senior Vice President, Construction Management")],
 [("Prefabricated masonry wall systems",
   "Published as a service line alongside load-bearing brick and CMU systems, "
   "supported by a 7,700 square foot fabrication facility.",
   "method_risk",
   "A masonry contractor that already prefabricates wall has made the argument "
   "to its own customers that wall can be made somewhere other than the wall.",
   "https://www.deebrowncompanies.com/services")],
 ["https://www.deebrowncompanies.com/", "https://www.deebrowncompanies.com/about",
  "https://www.deebrowncompanies.com/services",
  "https://www.deebrowncompanies.com/contact"],
 ["The headquarters is in Richardson, near Dallas. Houston is an office, and "
  "no Houston-specific volume is published.",
  "No annual square footage or revenue figure is published."]),

("HOU-157", "Camarata Masonry Systems",
 "Houston, West Hardy Road, with offices in Florida and North Carolina",
 "http://www.camaratamasonry.com/",
 "Publishes panelisation of stone and masonry",
 "A masonry, natural stone, tile and terrazzo subcontractor founded 1 August "
 "2004, describing itself as one of the largest in those specialties "
 "nationwide, working across arenas, education, entertainment, healthcare, "
 "government, religious, residential and multi-family, and retail. Named "
 "projects include Minute Maid Park, Reliant Stadium, the Rice University Music "
 "and Performing Arts Center and the ExxonMobil World Headquarters campus. Its "
 "about page publishes panelisation of natural stone and masonry as a "
 "capability.",
 (3, 2, 2, 2),
 "A Houston-headquartered masonry contractor that already panelises stone and "
 "masonry, on a project list that runs to stadiums and a corporate campus.",
 ("Masonry and stone laid repeatedly across one metro on large institutional "
  "and commercial work.",
  "A firm of this reach puts up more wall than one or two printers would cover, "
  "and multi-family is one sector among eight.",
  "It publishes panelisation of natural stone and masonry as a capability, "
  "which is production moved off the scaffold and into a shop. There is no "
  "record of adopting a new material."),
 [("Kevin M. Camarata", "Founder")],
 [],
 ["http://www.camaratamasonry.com/", "https://www.camaratamasonry.com/about-us"],
 ["The site answers a browser and refuses a script, so this record was read by "
  "hand rather than fetched.",
  "No crew count, revenue or annual square footage is published. The homepage "
  "offers only hundreds of satisfied clients in multiple states.",
  "It is the only firm listed under AGC Houston's masonry category."]),

("HOU-158", "Winco Masonry",
 "Porter, Montgomery County",
 "http://www.wincomasonry.com/",
 "Serving Texas for over 52 years",
 "A commercial masonry subcontractor working in face brick veneer, cast stone, "
 "concrete masonry units, natural stone and glass-fibre reinforced concrete, "
 "certified by the Air Barrier Association of America for building envelope "
 "work. Published project categories are education, government, healthcare, "
 "higher education, hotels and residential, office and recreational, and "
 "religious.",
 (3, 2, 1, 2),
 "Fifty-two years of commercial masonry from Montgomery County, with an "
 "envelope certification that required an audit.",
 ("Brick, block and cast stone laid repeatedly across one region for more than "
  "half a century.",
  "A firm with projects running all over town at once puts up more wall than "
  "one or two printers would cover.",
  "No record of paying for an unproven method. The published position is "
  "envelope certification and schedule reliability."),
 [("Gerald Guzman", "President")],
 [],
 ["http://www.wincomasonry.com/",
  "https://www.wincomasonry.com/office-recreational",
  "https://members.agchouston.org/directory/Details/winco-masonry-inc-2123266"],
 ["The site answers a browser and refuses a script, so this record was read by "
  "hand rather than fetched.",
  "No crew count or annual volume is published."]),

("HOU-159", "Veazey Enterprises",
 "Houston, Appleton Street, serving Greater Houston and Galveston",
 "https://vzmasonry.com/",
 "Four generations, operating since the early 1960s",
 "A masonry contractor serving hospitals, colleges, office buildings, churches, "
 "hotels, shopping centres, banks and fire stations across Greater Houston and "
 "Galveston, employing its own superintendents and foremen. The firm traces to "
 "Veazey Corporation, founded 1964, and was established under its present name "
 "in 1998.",
 (3, 2, 1, 2),
 "Four generations of commercial masonry inside the metro, on the institutional "
 "work where load-bearing block is still specified.",
 ("Commercial masonry laid repeatedly across one metro for four generations.",
  "A firm running its own superintendents across hospitals, colleges and hotels "
  "puts up more wall than one or two printers would cover.",
  "No record of paying for an unproven method."),
 [("David Veazey", "President")],
 [],
 ["https://vzmasonry.com/", "https://masoncontractors.org/5-on-5/veazey-enterprises/"],
 ["No crew count, revenue or annual volume is published.",
  "The president is named in a trade association interview rather than on the "
  "firm's own site, which publishes no leadership page."]),

# ===================================================================== nozzle
# Three firms that own the equipment. The gunite and shotcrete crews, which hold
# the skill a printer needs and not the balance sheet, are in supply.py.

("HOU-160", "Brundage-Bone Concrete Pumping",
 "Houston, two yards on West Old Spanish Trail and Sellers Road",
 "https://brundagebone.com/locations/houston/",
 "Boom pumps from 17 to 65 metres, plus placing booms",
 "A concrete pumping contractor with two Houston yards, running boom pumps from "
 "17 to 65 metres in a range of boom styles, line pumps including high pressure "
 "pumps for long vertical and horizontal runs, placing booms, and truck-mounted "
 "conveyors and telebelts for difficult mixes. All its operators are OSHA 10 "
 "and ACPA certified. It advertises specialised services including low carbon "
 "and pervious concrete pumping.",
 (3, 2, 1, 3),
 "A firm whose entire business is placing somebody else's concrete with owned "
 "capital equipment, which is the commercial shape of operating a printer for "
 "a builder.",
 ("Placement work repeated daily across one metro from two standing yards.",
  "A fleet spanning 17 to 65 metre booms across two yards is more placement "
  "capacity than one or two printers would cover.",
  "No record of paying for an unproven method. It advertises low carbon and "
  "pervious concrete pumping, and advertising a capability is not the same as "
  "having bought one."),
 [],
 [],
 ["https://brundagebone.com/locations/houston/"],
 ["The site answers a browser and returns a stub to a script, so this record "
  "was read by hand rather than fetched.",
  "No local manager is named on the Houston page, and no fleet count is given "
  "for the two Houston yards."]),

("HOU-161", "Texan Pumpers Company",
 "Kingwood, serving a 150-mile radius",
 "https://texconpumping.com/",
 "Over 30 pump trucks, 45 to 50 percent annual growth",
 "A concrete pumping company founded in 2017, operating over 30 pump trucks "
 "from 32-metre to 65-metre boom pumps out of a Kingwood office across a "
 "150-mile radius, with 40-plus staff and reported year-over-year growth of 45 "
 "to 50 percent. Its published customer base is major contractors, home "
 "builders and industrial clients across Texas.",
 (3, 2, 1, 2),
 "The fastest-growing pumping fleet in the metro, already selling placement to "
 "home builders, and still buying equipment.",
 ("Placement repeated daily for home builders and contractors across one "
  "region from one yard.",
  "Thirty-plus trucks is more placement capacity than one or two printers "
  "would cover, though a single-yard operation is the closer end of that range.",
  "No record of paying for an unproven method. The published position is fleet "
  "growth and service."),
 [],
 [],
 ["https://texconpumping.com/"],
 ["No named principal is published anywhere on the site.",
  "The growth figure is the firm's own and carries no period or base."]),

("HOU-162", "Omega Industries",
 "Houston, within a footprint including Dallas, Austin, San Antonio and Los Angeles",
 "https://omegaindinc.com/houston/service/gunite-shotcrete/",
 "$30 million bonding capacity, 1,200-plus projects",
 "A gunite and shotcrete contractor for commercial and industrial projects "
 "including retaining walls, swimming pools, tunnels and infrastructure, "
 "publishing four distinct methods: dry-mix gunite, wet-mix shotcrete, "
 "fibre-reinforced shotcrete and steel-reinforced gunite. Its own site records "
 "30 million dollars of bonding capacity, more than 1,200 completed projects, "
 "zero liens and zero OSHA violations.",
 (3, 2, 2, 3),
 "The only firm on this deck that both shoots concrete through a nozzle to a "
 "profile and carries an audited balance sheet large enough to buy equipment.",
 ("Shotcrete and gunite placed repeatedly across a multi-city footprint "
  "including Houston.",
  "A contractor bonded at 30 million dollars across four cities places more "
  "material than one or two printers would cover.",
  "It runs four distinct placement methods including fibre-reinforced "
  "shotcrete, each requiring different equipment and crew training. Carrying "
  "four methods rather than one is capital committed to how material gets "
  "placed."),
 [],
 [],
 ["https://omegaindinc.com/houston/service/gunite-shotcrete/"],
 ["The main office is in Dallas. Houston is one of four city footprints and no "
  "Houston yard address or crew count is published.",
  "The page shows project contacts by first name only, so no principal is "
  "named here."]),

# ====================================================================== slab
# Three firms. The cell is thinner than it should be, and the reason is a
# finding rather than a gap: the high-volume Houston slab crews are largely
# crew-based operations with no web presence at all. Five firms listed in the
# Greater Houston Builders Association's foundation categories publish no
# website of any kind. They are in supply.py under what could not be read.

("HOU-163", "Tealstone Residential Concrete",
 "Entire Houston region, plus Dallas-Fort Worth, Austin and San Antonio",
 "https://www.tealstonelp.com/",
 "10,000-plus slabs placed a year",
 "A residential concrete contractor pouring single-family foundations and "
 "flatwork for production builders, as a subsidiary of Sterling Infrastructure, "
 "a publicly traded infrastructure group. Its own residential page records more "
 "than 10,000 slabs placed annually, 500 million dollars of bonding capacity, "
 "and more than 2,000 home foundations placed for D.R. Horton across more than "
 "20 communities. Sterling's own site states that Tealstone builds foundations "
 "for single family homes throughout the Dallas-Fort Worth, Houston and Phoenix "
 "areas.",
 (3, 1, 1, 3),
 "The largest residential slab operation found in Texas, owned by a public "
 "infrastructure group with a capital allocation process, and the only "
 "contractor on this deck that publishes which builder it pours for.",
 ("Ten thousand foundations a year for production builders, repeated across "
  "the same communities in the same metros.",
  "Ten thousand slabs a year is far beyond what one or two printers would "
  "cover. A machine would be a pilot line, not a replacement for the slab business.",
  "No record of paying for an unproven method. The published position is scale, "
  "bonding and builder relationships."),
 [],
 [("D.R. Horton foundations",
   "More than 2,000 home foundations placed for D.R. Horton across more than 20 "
   "communities, on the firm's own residential page.",
   "repeatable",
   "The only published contractor-to-builder relationship found anywhere in "
   "this sweep, and it is with the largest builder in the country.",
   "https://tealstonelp.com/residential/")],
 ["https://www.tealstonelp.com/", "https://tealstonelp.com/residential/",
  "https://www.strlco.com/who-we-are/our-companies/"],
 ["A 2021 corporate brochure gives 6,000-plus slabs and 1 million cubic yards "
  "a year, and the current site gives 10,000-plus. Both are carried here "
  "because the deck does not pick between two published figures.",
  "No executive is named on the firm's own site. The names in the brochure are "
  "customers giving testimonials, not Tealstone people."]),

("HOU-164", "All About Concrete",
 "Tomball, Houston primary, also Dallas-Fort Worth, Austin and San Antonio",
 "https://allaboutconcretellc.net/",
 "Turn-key concrete for production builders",
 "A turn-key concrete contractor serving residential production builders, light "
 "commercial contractors and developers, handling everything from initial "
 "design collaboration to final installation. It records Greater Houston "
 "Builders Association Distinguished Member status for 2024, 2025 and 2026.",
 (3, 3, 1, 1),
 "Turn-key concrete for residential production builders in Houston, in the "
 "firm's own words.",
 ("Turn-key concrete repeated for production builders across the same Houston "
  "submarkets.",
  "A single-office contractor serving production builders is the scale where "
  "one or two machines would cover a real share of the work it takes on.",
  "No record of paying for an unproven method, and no method content on the "
  "site at all."),
 [],
 [],
 ["https://allaboutconcretellc.net/"],
 ["No figures of any kind are published: no crew count, no slabs a year, no "
  "years in business.",
  "No principal is named.",
  "Post-tension is not mentioned anywhere on the site, which is unusual for a "
  "Houston production slab contractor and worth asking about."]),

("HOU-165", "Solid Foundations",
 "Conroe, Montgomery County, and across the state",
 "https://solidfoundationsltd.com/about.php",
 "Founded 1999, rebar and post-tension foundations",
 "A full service concrete contractor founded in 1999, running a dedicated "
 "rebar-foundation and post-tension service line, describing itself as a "
 "turn-key contractor in the Houston area and throughout the state. Its "
 "published project list runs to churches, parking garages, shopping centres, "
 "banks and university buildings.",
 (2, 3, 1, 2),
 "A Conroe contractor with a standing post-tension line, positioned in the "
 "north Houston growth corridor where the production communities are.",
 ("A standing post-tension foundation line repeated across the region, though "
  "the published project list is commercial rather than production residential.",
  "A single-office contractor of this size is the scale where one or two "
  "machines would cover a real share of the work it takes on.",
  "No record of paying for an unproven method."),
 [("Don Jackson", "Owner and President")],
 [],
 ["https://solidfoundationsltd.com/about.php"],
 ["The project list skews commercial. Residential volume is asserted by trade "
  "association category rather than by anything on the firm's own page.",
  "No crew count or annual volume is published."]),
]


# The cell each contractor occupies in the wall value chain, for the 51 on the
# roster. This is the ordering the contractor section reads in, because the
# chain is the structure: the deck's first contractor pass produced 22 firms
# that were all one cell and looked like a market.
#
# The order runs the way a wall gets made. Placement first, because a crew with
# a hose is doing most of what a printer does. Then the horizontal, then the
# three ways the vertical gets made, then the firm that owns the job.
CELL_ORDER = ["nozzle", "slab", "tiltup", "precast", "panel", "masonry", "icf", "gc"]

CELL_LABEL = {
    "nozzle":  "Places it through a hose",
    "slab":    "Pours the horizontal",
    "tiltup":  "Casts the vertical flat, on site",
    "precast": "Casts the vertical off site",
    "panel":   "Manufactures the vertical as a panel",
    "masonry": "Lays the vertical unit by unit",
    "icf":     "Forms the vertical and leaves the form in",
    "gc":      "Owns the job and self-performs the concrete",
}

CELL_NOTE = {
    "nozzle":  "A crew here already places cementitious material through a hose "
               "onto a surface, to a profile, with no formwork.",
    "slab":    "Owns the lot before anyone else arrives, owns the builder "
               "relationship and owns the pump. Wall scope would double the "
               "revenue per lot with the same customer and no new sale.",
    "tiltup":  "Casts wall flat on the slab and lifts it. The panels are "
               "measured in tons and storeys, which is why most of this cell "
               "reads Partly on printer fit.",
    "precast": "A plant, casting beds and a quality lab. The equipment a printer "
               "would sit beside is already financed.",
    "panel":   "Already manufactures wall off site and sells it to the "
               "production builders on this deck. The logistics, the builder "
               "relationship and the factory economics are solved.",
    "masonry": "The trade a printed wall most directly displaces. Two firms "
               "here already sell a panelised or prefabricated version of their "
               "own product.",
    "icf":     "Has already sold a customer on a wall that is not stick-built, "
               "which is the adoption behaviour that is hardest to find.",
    "gc":      "Houston builders do not put up their own walls. The general "
               "contractor that self-performs concrete is the one that would "
               "run the machine.",
}

# The 29 added in Build 62 carry their cell from the sweep that found them.
CELL = {
    # precast
    "HOU-137": "precast", "HOU-138": "precast", "HOU-139": "precast",
    "HOU-140": "precast", "HOU-141": "precast", "HOU-142": "precast",
    "HOU-143": "precast", "HOU-144": "precast", "HOU-145": "precast",
    # panel
    "HOU-146": "panel", "HOU-147": "panel", "HOU-148": "panel",
    "HOU-149": "panel", "HOU-150": "panel", "HOU-151": "panel",
    "HOU-152": "panel", "HOU-153": "panel", "HOU-154": "panel",
    # masonry
    "HOU-155": "masonry", "HOU-156": "masonry", "HOU-157": "masonry",
    "HOU-158": "masonry", "HOU-159": "masonry",
    # nozzle
    "HOU-160": "nozzle", "HOU-161": "nozzle", "HOU-162": "nozzle",
    # slab
    "HOU-163": "slab", "HOU-164": "slab", "HOU-165": "slab",
}

# The 22 the first contractor pass found, placed in the same chain so the whole
# section reads in one order. Seven of them turn out to be general contractors
# that self-perform rather than wall subcontractors, which is a distinction the
# section never drew.
CELL.update({
    "HOU-101": "slab",     # Keystone Concrete Placement, three placement divisions
    "HOU-102": "gc",       # Harvey Cleary, general contractor self-performing concrete
    "HOU-103": "tiltup",   # Texas A&M Concrete
    "HOU-104": "slab",     # Botello Builders, foundations and piers as well as tilt-up
    "HOU-105": "tiltup",   # Encore Concrete Construction
    "HOU-106": "tiltup",   # Greco Structures
    "HOU-107": "slab",     # Andrade, earthwork utilities and concrete
    "HOU-108": "tiltup",   # HTX Concrete
    "HOU-109": "gc",       # T&T Construction
    "HOU-110": "slab",     # Silver Spur, named residential concrete line
    "HOU-111": "tiltup",   # Building Concrete Solutions
    "HOU-112": "tiltup",   # ORION
    "HOU-113": "tiltup",   # Baker Construction
    "HOU-114": "tiltup",   # Rino Construction
    "HOU-115": "gc",       # Arch-Con Corporation
    "HOU-116": "gc",       # Burton Construction
    "HOU-117": "gc",       # Blazer Building
    "HOU-118": "gc",       # Leola, shell contractor delivering the whole wall package
    "HOU-119": "icf",      # M.L. Deer Construction
    "HOU-120": "icf",      # ICF Constructors
    "HOU-121": "panel",    # MAREK, own prefabrication plant
    "HOU-129": "gc",       # CIVE, design-build, printed the Spring Branch house
})
WALL_IDS = {r[0] for r in WALL}
