# -*- coding: utf-8 -*-
"""Second research pass, 11 September 2026: the builder and creative layers.

The first pass named these people from the firms' own pages and left every one
without a link. This pass went back for the links and for the volume figures
that were missing, and three of the figures changed a placement.

Stylecraft closes 973 homes a year, not "more than 300". Colina closes 540.
Both move from machine fit clear to partial: at that volume two printers are a
line inside the business rather than the business. Westin, which had no figure,
closes 1,062. Two firms carried as independents are brands of larger builders:
GreenEco has belonged to Rausch Coleman since 2020 and Imagination Homes is a
David Weekley line. Both are recorded as such.

Verification rests on the same rule as the first pass. A LinkedIn URL is held
only where a retrieved page shows the person's name and the firm together, and
the evidence sentence says which page that was. LinkedIn itself refuses
automated retrieval, so for most profiles that page is the search index entry
for the profile, which carries LinkedIn's own title tag. Where a firm's own
site links to the profile, that is recorded instead, because it is stronger.
Data aggregators (ZoomInfo, RocketReach and the like) were not used.
"""

# name -> (url, evidence)
LINKEDIN = {
    # Checked in the open-items pass. Three names alongside these had no profile
    # and no source outside a contact-data aggregator, so they came off the deck.
    "Diane Danilov": ("https://www.linkedin.com/in/diane-danilov-2431a212/",
        "Headline reads VP of Land & Business Development at Westin Homes. Houston, Texas."),
    "India Kinslow": ("https://www.linkedin.com/in/india-kinslow-824b2614b/",
        "Headline reads Director Of Purchasing at Sitterle Homes. San Antonio, which is where "
        "the firm's purchasing sits."),
    # Stylecraft
    "Doug French": ("https://www.linkedin.com/in/doug-french-bb28b074/",
        "Indexed title reads Doug French, Stylecraft Builders Inc. The firm's team page lists him as "
        "Owner, President and Chief Executive Officer."),
    "Bruce Hendren": ("https://www.linkedin.com/in/bruce-hendren-6a059068/",
        "Indexed title reads Bruce Hendren, Stylecraft. The firm's team page lists him as Vice "
        "President of Pre-Construction."),
    "Emily Runnion": ("https://www.linkedin.com/in/emilyrunnion/",
        "Indexed title reads Emily Runnion, Stylecraft. The firm's team page lists her as Director "
        "of the South Six Construction Group."),
    # Colina
    "Robert Davis": ("https://www.linkedin.com/in/robert-davis-684517136/",
        "Indexed title reads Robert Davis, Director of Construction, Colina Homes."),
    # GreenEco
    "George Kopecky": ("https://www.linkedin.com/in/george-kopecky-7ba08a26/",
        "Indexed title reads George Kopecky, President at GreenEco Builders. Named as the firm's "
        "principal in trade coverage of the 2020 sale to Rausch Coleman."),
    # Kendall
    "Glenn Briggs": ("https://www.linkedin.com/in/glenn-briggs-5231975/",
        "Indexed title reads Glenn Briggs, President at Kendall Homes."),
    "Jason Madden": ("https://www.linkedin.com/in/jason-madden-3610ba70/",
        "Indexed title reads Jason Madden, Vice President of Construction at Kendall Homes."),
    # Westin
    "Jason Golan": ("https://www.linkedin.com/in/jason-golan-0874a241/",
        "Indexed title reads Jason Golan, President at Westin Homes. The firm's own twentieth-"
        "anniversary release calls him Founder and Owner."),
    # Tricoast
    "Christina Wright": ("https://www.linkedin.com/in/christina-wright-4786b223/",
        "Indexed title reads Christina Wright, Director of Purchasing at Tricoast Homes."),
    # J. Patrick
    "Bo Banowsky": ("https://www.linkedin.com/in/bo-banowsky-3b11278/",
        "Indexed title reads Bo Banowsky, Purchasing Manager, J. Patrick Homes."),
    # Ravenna
    "Stephen Najvar": ("https://www.linkedin.com/in/stephennajvar/",
        "Indexed title reads Stephen Najvar, President at Ravenna Homes. A 2013 company release "
        "names him co-founder alongside his brother Kenneth Najvar, both formerly Perry Homes "
        "division presidents."),
    # Concept Neighborhood: the firm's own team page links each profile
    "David Kelley": ("https://www.linkedin.com/in/david-kelley-275240105/",
        "Linked from conceptneighborhood.com/team, which lists him as Managing Partner, Projects "
        "and Finance."),
    "Jeffrey Kaplan": ("https://www.linkedin.com/in/jeffrey-kaplan-71190150/",
        "Linked from conceptneighborhood.com/team, which lists him as Managing Partner, Brokerage "
        "and Placemaking."),
    "Monte Large": ("https://www.linkedin.com/in/montelarge/",
        "Linked from conceptneighborhood.com/team, which lists him as Partner, Design and Placemaking."),
    "Jeremy Roberts": ("https://www.linkedin.com/in/jeremyaaronroberts/",
        "Linked from conceptneighborhood.com/team, which lists him as Managing Partner, Projects "
        "and Legal."),
    # Braun
    "Dan Braun": ("https://www.linkedin.com/in/dan-braun-36451a15/",
        "Indexed title reads Dan Braun, President at Braun Enterprises. The firm's team page "
        "returns a 404, so this is the only link."),
    # Partners in Building
    "Dewey Hennessee": ("https://www.linkedin.com/in/dewey-hennessee-gmb-caps-cgp-95418531",
        "Indexed title reads Dewey Hennessee GMB CAPS CGP, Partners in Building. The title on file "
        "comes from the first pass and is not repeated in the index entry."),
    # Pagewood
    "Mat Volz": ("https://www.linkedin.com/in/mathew-volz-14684850/",
        "Indexed title reads Mathew Volz, Managing Principal at Pagewood. The firm's team page "
        "spells the name Mat."),
    # Urban Living
    "Vinod Ramani": ("https://www.linkedin.com/in/vinod-ramani-4a46788/",
        "Indexed title reads Vinod Ramani, Urban Living."),
    # Wile
    "Randolph Wile": ("https://www.linkedin.com/in/randolph-wile/",
        "Indexed title reads Randolph Wile, Wile Interests, Inc."),
    # Jamestown
    "Greg Hawes": ("https://www.linkedin.com/in/greg-hawes-86423023/",
        "Indexed title reads Greg Hawes, President, Jamestown Estate Homes LP. The firm's own team "
        "page calls him Manager and has him founding the firm in 2008 with his daughters."),
    # Sandcastle
    "Mike Dishberger": ("https://www.linkedin.com/in/mike-dishberger-01b66b9/",
        "Indexed title reads Mike Dishberger, CEO at Sandcastle Homes Inc. The firm's team page: "
        "Chief Executive Officer and Co-Owner, overseeing construction, purchasing and accounting."),
    "Mike Salomon": ("https://www.linkedin.com/in/mike-salomon-389b902a/",
        "Indexed title reads Mike Salomon, Owner, Sandcastle Homes, Inc. The firm's team page: "
        "President and Co-Owner, over land, sales and business development."),
    # Risewell
    "Jennifer Keller, P.E.": ("https://www.linkedin.com/in/jenniferkeller/",
        "Indexed title reads Jennifer Keller, P.E., Division President, Risewell Homes. The firm's "
        "team page lists her as Houston Division President."),
    "Matthew R. Zaist": ("https://www.linkedin.com/in/matthew-zaist-01949696/",
        "Indexed title reads Matthew Zaist, President and CEO at Risewell Homes. Confirmed on the "
        "firm's team page."),
    # Sitterle
    "Frank Sitterle, Jr.": ("https://www.linkedin.com/in/frank-sitterle-071b8246/",
        "Indexed title reads Frank Sitterle, President, Sitterle Homes. The firm's about page has "
        "him acquiring the company in 2005 with Jeff Buell."),
    "Chris Hightower": ("https://www.linkedin.com/in/chris-hightower-029b45112/",
        "Indexed title reads Chris Hightower, Division President at Sitterle Homes. The GHBA "
        "member directory lists him as Division President, Houston."),
}

# (target_id, name) -> (url, what the page says)
SOURCES = {
    ("HOU-065", "Jordan York"): ("https://www.stylecraft.com/team/",
        "Team page lists Jordan York, Vice President of Construction. The only LinkedIn profile "
        "under the name is a charter pilot."),
    ("HOU-065", "Doug French"): ("https://www.stylecraft.com/team/",
        "Team page lists Doug French, Owner, President and Chief Executive Officer."),
    ("HOU-065", "Bruce Hendren"): ("https://www.stylecraft.com/team/",
        "Team page lists Bruce Hendren, Vice President of Pre-Construction."),
    ("HOU-065", "Emily Runnion"): ("https://www.stylecraft.com/team/",
        "Team page lists Emily Runnion, Director of South Six Construction Group."),
    ("HOU-073", "Roderick Flint"): (
        "https://brohnhomes.com/community-impact-features-brohn-homes-houston-vision/",
        "The firm's own post on the Houston launch names him Division President and quotes him on "
        "folding existing plans into Brohn's line."),
    ("HOU-060", "Kevin Holland"): ("https://www.cervellehomes.com/",
        "Homepage: the founder's standards carry forward under the guidance of Kevin Holland and "
        "John Payson. No title is published anywhere."),
    ("HOU-060", "John Payson"): ("https://www.cervellehomes.com/",
        "Homepage names him alongside Kevin Holland as carrying the founder's standards forward. "
        "No title is published."),
    ("HOU-061", "Dru Kahlenberg"): ("https://www.myaltahomes.com/about",
        "About page: CEO, who signs off on every piece of land and secures the financing behind "
        "every community."),
    ("HOU-061", "Scott Gilbert"): ("https://www.myaltahomes.com/about",
        "About page: President, focused on teams, vendor partnerships and efficient construction."),
    ("HOU-061", "Ashley Meinecke"): ("https://www.myaltahomes.com/about",
        "About page: AP and Purchasing Manager."),
    ("HOU-064", "Ken Williams"): ("https://www.colinahomes.com/about",
        "About page: Founder. Since 2007 he has helped over 4,500 families."),
    ("HOU-076", "Greg Grahmann"): (
        "https://www.builderonline.com/builder-100/strategy/imagination-homes-targets-attainable-entry-level-housing-in-texas/",
        "Builder names him director at Imagination Homes. He joined David Weekley Homes in 2013 and "
        "is separately listed as a division president there."),
    ("HOU-069", "Jeff Dye"): (
        "https://houstonagentmagazine.com/2020/02/06/making-moves-newmark-homes-appoints-top-leaders-edward-jones-becomes-latest-tenant-bridgeland/",
        "Houston Agent, February 2020: Jeff Dye assumed the position of president after 21 years "
        "with the firm."),
    ("HOU-067", "Tim Drone"): ("https://houstonagentmagazine.com/2026/02/10/j-patrick-homes-small-lots-grange/",
        "Quoted as President Tim Drone in February 2026 coverage of the firm's small-lot product."),
    ("HOU-081", "Paul Coonrod"): ("https://www.pagewood.com/team",
        "Team page: Founder and Managing Principal."),
    ("HOU-081", "Mat Volz"): ("https://www.pagewood.com/team", "Team page: Managing Principal."),
    ("HOU-081", "Preston Luster"): ("https://www.pagewood.com/team",
        "Team page: Senior Construction Manager."),
    ("HOU-082", "Randolph Wile"): (
        "https://therealdeal.com/texas/houston/2023/11/13/pagewood-wile-to-convert-eado-houston-warehouses/",
        "The Real Deal, November 2023, quotes Wile Interests president Randolph Wile."),
    ("HOU-072", "Jim Lemming"): ("https://www.housingwire.com/articles/partners-building-succession-plan/",
        "HousingWire, 15 June 2026: President and CEO Jim Lemming will transition to chairman, and "
        "his son Chris Lemming will assume the presidency."),
    ("HOU-072", "Chris Lemming"): ("https://www.housingwire.com/articles/partners-building-succession-plan/",
        "HousingWire, 15 June 2026: Chris Lemming assumes the presidency after an eighteen-month "
        "succession."),
    ("HOU-080", "David Kelley"): ("https://www.conceptneighborhood.com/team",
        "Team page: Managing Partner, Projects and Finance."),
    ("HOU-080", "Jeffrey Kaplan"): ("https://www.conceptneighborhood.com/team",
        "Team page: Managing Partner, Brokerage and Placemaking."),
    ("HOU-080", "Monte Large"): ("https://www.conceptneighborhood.com/team",
        "Team page: Partner, Design and Placemaking."),
    ("HOU-080", "Jeremy Roberts"): ("https://www.conceptneighborhood.com/team",
        "Team page: Managing Partner, Projects and Legal."),
    ("HOU-074", "Stephen Ray"): (
        "https://www.smithdouglas.com/blog/smith-douglas-homes-acquires-devon-street-homes-enters-houston-tx-market",
        "Smith Douglas's own announcement: Stephen Ray, Founder and President of Devon Street, will "
        "continue to lead the Houston division. No post-acquisition title is published."),
    ("HOU-071", "Greg Hawes"): ("https://jamestownestatehomes.com/team/greg-hawes/",
        "Team page: Manager. In his own words, he sold his interest in a prior firm and started "
        "Jamestown Estate Homes LP in 2008 with his daughters."),
    ("HOU-071", "Katy Hawes"): ("https://jamestownestatehomes.com/team/katy-hawes/",
        "Team page: Co-President."),
    ("HOU-071", "Matt Norris"): ("https://jamestownestatehomes.com/team/matt-norris/",
        "Team page: Co-President."),
    ("HOU-066", "Mike Dishberger"): ("https://www.sandcastlehouston.com/about-sandcastle/meet-our-team/",
        "Team page: Chief Executive Officer and Co-Owner, overseeing construction, purchasing and "
        "accounting. Texas Association of Builders Builder of the Year, 2016."),
    ("HOU-066", "Mike Salomon"): ("https://www.sandcastlehouston.com/about-sandcastle/meet-our-team/",
        "Team page: President and Co-Owner, managing land acquisition, sales and business development."),
    ("HOU-075", "Jennifer Keller, P.E."): ("https://www.risewellhomes.com/team",
        "Executive team page lists her under Division Presidents as Houston Division President."),
    ("HOU-075", "Matthew R. Zaist"): ("https://www.risewellhomes.com/team",
        "Executive team page: President and Chief Executive Officer."),
}

# (target_id, name) -> corrected role
TITLES = {
    ("HOU-072", "Jim Lemming"): "Chairman, formerly President and Chief Executive Officer until June 2026",
    ("HOU-076", "Greg Grahmann"): "Director, Imagination Homes; Division President, David Weekley Homes",
    ("HOU-060", "Kevin Holland"): "Leads the firm with John Payson; no title published",
    ("HOU-060", "John Payson"): "Leads the firm with Kevin Holland; no title published",
    ("HOU-074", "Stephen Ray"): "Leads the Houston division; Founder and President of Devon Street Homes before the 2023 sale",
    ("HOU-071", "Greg Hawes"): "Founder; Manager on the firm's own page, President on LinkedIn",
    ("HOU-066", "Mike Dishberger"): "Chief Executive Officer and Co-Owner; oversees construction and purchasing",
    ("HOU-066", "Mike Salomon"): "President and Co-Owner",
}

# target_id -> [(name, role)] added to the card
PEOPLE = {
    "HOU-078": [("George Kopecky", "President")],
    "HOU-069": [("Jeff Dye", "President")],
    "HOU-072": [("Chris Lemming", "President, since June 2026")],
    "HOU-077": [("Chris Hightower", "Division President, Houston")],
}

# target_id -> headline figure
STATS = {
    "HOU-065": "973 homes and $310 million in 2025, up 17 percent",
    "HOU-064": "540 closings in 2025, 552 in 2024",
    "HOU-068": "1,062 closings and $621 million in 2025",
    "HOU-063": "195 closings in 2022, the latest published",
    "HOU-069": "483 closings and $306 million in 2025",
    "HOU-072": "More than 300 homes a year in Texas and Tennessee",
    "HOU-066": "40 to 60 homes a year on the firm's own count",
    "HOU-071": "About 75 homes a year on the firm's own count",
    "HOU-077": "372 closings company-wide in 2022, no Houston figure",
    # A blank column reads as an oversight. Where no figure is published, the
    # column says what the record actually holds instead.
    "HOU-045": "No unit count published; owned by Sekisui House U.S.",
    "HOU-044": "366 build-to-rent units across two Katy projects",
    "HOU-042": "Sells lots inside its own masterplans; Lennar builds",
    # The land owners publish acreage and builder rosters, not closings.
    "HOU-039": "Sunterra, 2,303 acres in Katy, fifteen builders",
    "HOU-040": "Fourteen concurrent Houston masterplans",
    "HOU-041": "Towne Lake and The Highlands, about 4,000 homes",
    "HOU-043": "Elyson, 3,600 acres in Katy",
}

# target_id -> {axis: score}. Only machine fit moves, and only where a figure
# or an owner changed the band.
SCORES = {
    "HOU-042": {"innovation": 2},    # the parent has paid for a printed wall; the brand has not
    "HOU-065": {"machine_fit": 2},   # 973 a year: two printers are a line, not the business
    "HOU-064": {"machine_fit": 2},   # 540 a year
    "HOU-076": {"machine_fit": 2},   # purchasing sits with David Weekley
}

# target_id -> the machine-fit reason that replaces the one on file
MACHINE_WHY = {
    "HOU-065": "973 homes in 2025 across Bryan-College Station, Conroe and Huntsville. Two machines "
               "would be a production line inside the business rather than the business.",
    "HOU-064": "540 closings in 2025 and 552 in 2024 across about twenty communities. Two machines "
               "would carry a fifth of output at most.",
    "HOU-068": "1,062 closings in 2025 and 1,016 in 2024 across Houston and Austin. Two machines "
               "would be a line inside the business.",
    "HOU-063": "195 closings in 2022 and 189 in 2021, the latest figures published. Inside the band "
               "one or two machines serve.",
    "HOU-076": "A David Weekley Homes line, so purchasing sits with a national builder. One machine "
               "would cover the brand's output; the decision would not be the brand's alone.",
    "HOU-078": "Owned by Rausch Coleman Homes since 2020, and Lennar completed its purchase of "
               "Rausch Coleman on 10 February 2025. No volume figure is published for the brand; "
               "purchasing sits with the parent.",
    "HOU-072": "More than 300 homes a year on the firm's own count, across Texas and Tennessee.",
}

# target_id -> open items
FLAGS = {
    "HOU-065": [
        "The volume on file was more than 300 closings a year. HousingWire reports 973 homes and "
        "$310 million in 2025, up 17 percent. Printer fit moves from Yes to Partly on that figure."],
    "HOU-064": [
        "Builder reports 540 closings in 2025 and 552 in 2024. Printer fit moves from Yes to Partly."],
    "HOU-068": [
        "Builder reports 1,062 closings and $621 million in 2025, rank 60 on the 2026 Builder 100. "
        "The firm's twentieth-anniversary release, dated December 2014, names Jason Golan as "
        "founder. The division president it names then is now Central Region President at Meritage "
        "Homes and is listed there.",
        "No LinkedIn profile is held for Matthew Roland or Diane Danilov. Only data aggregators "
        "carry their titles, and those were not used."],
    "HOU-078": [
        "GreenEco was acquired by Rausch Coleman Homes in 2020. Lennar announced the completed "
        "acquisition of Rausch Coleman on 10 February 2025, naming Houston among the markets added. "
        "It still sells under its own name in Houston listings. The route is Lennar."],
    "HOU-076": [
        "Imagination Homes is a David Weekley Homes line for entry-level product, and Greg Grahmann "
        "is a David Weekley division president. The wall decision runs through the parent."],
    "HOU-073": [
        "Whether Brohn's Houston division purchases locally or through Clayton's national desk is "
        "not published anywhere. Clayton describes Brohn as three affiliated entities under its "
        "umbrella, which says nothing about purchasing."],
    "HOU-033": [
        "Dream Finders' 2024 annual report describes procurement across local, regional and national "
        "levels, with national volume used to secure manufacturer pricing. Coventry's Houston "
        "purchasing is therefore a hybrid, and a wall specification would clear both."],
    "HOU-069": [
        "Jeff Dye has been president since February 2020, after 21 years at the firm. He is the "
        "first named person on this card. No vice president of construction or head of purchasing "
        "is published."],
    "HOU-072": [
        "Jim Lemming moved to chairman in June 2026 after an eighteen-month succession; his son "
        "Chris Lemming is president. The chief executive title on file from the first pass is stale."],
    "HOU-062": [
        "No LinkedIn profile is held for Christian Sommer or Keith Blum, and no volume figure is "
        "published. Christina Wright, Director of Purchasing, is the one linked contact."],
    "HOU-067": [
        "No annual volume is published. No LinkedIn profile is held for Patrick Mustoe or Art Maya."],
    "HOU-070": [
        "A founder-run firm with no other executive published anywhere. No annual volume figure."],
    "HOU-060": [
        "No title is published for Kevin Holland or John Payson on the site, in the GHBA directory "
        "or on LinkedIn."],
    "HOU-081": [
        "Preston Luster is the senior construction manager on the team page. No vice president of "
        "construction is published; the two managing principals are the decision layer."],
    "HOU-077": [
        "No page outside a data aggregator names India Kinslow with a title at Sitterle, so no link "
        "is held for her. The GHBA directory and LinkedIn both name Chris Hightower as Division "
        "President, Houston, and he is added. Company-wide closings were 372 in 2022; no Houston "
        "figure is published."],
    "HOU-071": [
        "Greg Hawes is Manager on the firm's own page and President on his LinkedIn. The firm's "
        "latest published figure is 20 homes and $22 million in 2020, when the Houston Business "
        "Journal ranked it first among Houston custom builders. No LinkedIn profile is held for "
        "Katy Hawes or Matt Norris."],
    "HOU-066": [
        "The firm's own retrospective puts volume at 40 to 60 homes a year since a 2005 peak of 59. "
        "Mike Dishberger oversees construction and purchasing himself, so he is the wall decision."],
    "HOU-074": [
        "Stephen Ray's post-acquisition title is not published anywhere. No LinkedIn profile could "
        "be matched to him at either Devon Street or Smith Douglas. Smith Douglas closed about "
        "2,200 homes company-wide in 2023; no Houston breakout has been filed."],
    "HOU-075": [
        "Risewell is the 2025 merger of Landsea Homes and The New Home Company, which closed 2,831 "
        "and 1,123 homes respectively in 2024. No Houston division figure is published."],
}

# additional deciders, by the same bar: VP or director of construction, or head of purchasing
# The builder layer was added after the decider pass ran and never received it,
# so firms whose whole case rests on a named construction lead showed none.
DECIDERS = {
    ("HOU-068", "Diane Danilov"),      # VP of Land and Business Development, the only
                                       # Westin officer with an independent source
    ("HOU-065", "Jordan York"),        # VP of Construction
    ("HOU-065", "Bruce Hendren"),      # VP of Pre-Construction, where the specification is set
    ("HOU-063", "Jason Madden"),       # VP of Construction
    ("HOU-062", "Christina Wright"),   # Director of Purchasing
    ("HOU-064", "Robert Davis"),       # Director of Construction
    ("HOU-067", "Bo Banowsky"),        # Purchasing Manager, the purchasing function at a firm this size
    ("HOU-061", "Ashley Meinecke"),    # AP and Purchasing Manager, the purchasing function at 45 homes a year
    ("HOU-072", "Dewey Hennessee"),    # VP of Purchasing
    ("HOU-066", "Mike Dishberger"),    # CEO who runs construction and purchasing at a 50-home firm
}

# target_id -> the screen sentence, applied after every other verdict layer.
# Rewritten where the first pass reached for a superlative, a metaphor or an
# instruction, and where a figure from this pass changed what the sentence says.
VERDICTS = {
    "HOU-001": "Builds and holds build-to-rent. Spent six years on its own construction software "
               "and site robotics.",
    "HOU-007": "1,300 homes a year and it markets its wall assembly. The parent owns the land, so no "
               "third party sits in the method decision.",
    "HOU-065": "973 homes in 2025 on a published even-flow model that releases a fixed number of "
               "starts a week. Eight or nine plans per community.",
    "HOU-028": "346 units, with its own architect and general contractor in-house. No third party "
               "in a method decision.",
    "HOU-045": "Now part of Sekisui House U.S., whose stated mission is transferring Japanese "
               "construction technology into its US brands. Nothing has reached Texas yet.",
    "HOU-078": "Orders windows per home rather than per community so it can adopt newer products. "
               "Owned by Rausch Coleman Homes, which Lennar bought in February 2025.",
    "HOU-060": "150 to 200 homes a year from two standing plan families in one corridor. Inside the "
               "band one machine serves.",
    "HOU-061": "45 closings in 2025 and 70 planned for 2026, all inside one county. One machine "
               "would cover the whole programme.",
    "HOU-032": "Attached townhome production, the product type a printed party wall serves. "
               "The owner is held on a LinkedIn headline alone; the firm's own site publishes nobody.",
    "HOU-074": "324 closings across fifteen communities in the year before it was acquired, on "
               "standardised entry-level product. Now part of a listed builder; the Houston "
               "purchasing structure is not published.",
    "HOU-022": "20,000 homes since 2004. Daiwa House owns a stake. No published method evidence.",
    "HOU-068": "1,062 closings in 2025 across the south suburban masterplans, with a named vice "
               "president of construction.",
    "HOU-064": "540 closings in 2025 and 552 in 2024 on a no-haggle affordable model. A named "
               "director of construction.",
    "HOU-076": "A 2025 David Weekley Homes line built around attainable entry-level product with a "
               "curated plan set, selling at Meridiana.",
    "HOU-066": "About fifty homes a year, stated by the firm, on small infill sites rather than in "
               "one community. The volume fits a machine; the sites are scattered.",
    "HOU-062": "Seven plans, ten communities, founded 2020. No closings figure to size it against.",
    "HOU-069": "483 closings in 2025 across more than twenty communities and more than 150 plans. "
               "A president is named; no construction or purchasing lead is published.",
    "HOU-067": "A semi-custom builder that won a volume award and publishes no volume. Named "
               "purchasing and construction managers.",
    "HOU-083": "Builds new rather than converting: small-format ground-up retail in the Heights.",
    "HOU-082": "Ground-up medical and retail in Katy, conversion in EaDo.",
    "HOU-072": "More than 300 homes a year and a vice president of purchasing. Every house is "
               "one-of-a-kind. The presidency passed from Jim to Chris Lemming in June 2026.",
    "HOU-015": "Sells lots, but owns First America Homes, which holds all three counts. One "
               "president runs both.",
    "HOU-039": "Sells lots. Sunterra carries 2,303 acres and 15 builders.",
    "HOU-040": "Sells lots across 14 Houston masterplans. Buys no walls.",
    "HOU-042": "Sells lots, wholly owned by Lennar since 2000. Lennar built a hundred printed homes "
               "with ICON at Wolf Ranch.",
}
