# -*- coding: utf-8 -*-
"""The ten largest builders in Greater Houston, read against the deck.

BUILDER publishes a Local Leaders table for each metro every year: the ten
builders with the most closings, the count and the share. The 2026 edition is
2025 closings. It was read by hand in a browser on 24 September 2026, because
builderonline.com refuses a script, and it is registered in figures.py BYHAND.

The table found four things.

    Lennar, first in the metro at 6,362, had no card. Neither did PulteGroup,
    fifth at 1,146, or Highland Homes, tenth at 968. Dream Finders, eighth at
    1,048, was on the deck only as Coventry, its Houston brand.

    Six firms already on the deck published no Houston figure anywhere the deck
    had read. They do now, and two of their cards were wrong about it: D.R.
    Horton's said no metro figure is published, and its screen said it builds
    more houses in Houston than anyone else. It builds the second most.

    D.R. Horton read Partly on Printer fit over a reason that argues No. That is
    the Leola error from Build 35, and it is fixed the same way: the mark follows
    the reason.

    KB Home and Hovnanian, ninth and eighth in the 2025 edition, are not in the
    2026 edition, and neither publishes a Houston figure of its own. They stay
    off the deck. The handoff records why.

Two figures in the table are not one brand. Sekisui House U.S. sells in Houston
as Chesmar and under its other US brands, and Dream Finders sells as Coventry and
under its own name. Those two carry the figure with the parent named, never as
the brand's own count.

Scores are (repeatability, machine_fit, innovation, capital_access), 3 clears,
2 partial, 0-1 fails.
"""

LL = "https://www.builderonline.com/land/local-leaders-list/2026/houston-pasadena-the-woodlands-tx/"

# rank, name as BUILDER prints it, 2025 closings, 2025 share, card
TABLE = [
    (1, "Lennar Corp.", 6362, "17.0%", "HOU-166"),
    (2, "D.R. Horton", 4925, "13.1%", "HOU-132"),
    (3, "Perry Homes", 1809, "4.8%", "HOU-013"),
    (4, "Meritage Homes", 1428, "3.8%", "HOU-008"),
    (5, "PulteGroup", 1146, "3.1%", "HOU-167"),
    (6, "Ashton Woods Homes", 1115, "3.0%", "HOU-024"),
    (7, "Sekisui House U.S.", 1087, "2.9%", "HOU-045"),
    (8, "Dream Finders Homes", 1048, "2.8%", "HOU-033"),
    (9, "Century Communities", 1017, "2.7%", "HOU-009"),
    (10, "Highland Homes", 968, "2.6%", "HOU-168"),
]

_SRC = "BUILDER Local Leaders 2026, Houston metro"
CLOSINGS = {
    tid: (n, n, 2025,
          _SRC + (", Sekisui House U.S. across its Houston brands" if tid == "HOU-045"
                  else ", Dream Finders Homes, the parent" if tid == "HOU-033" else ""))
    for _r, _nm, n, _s, tid in TABLE
}

_ORD = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth",
        7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth"}

KEY_STAT = {
    tid: "%s Houston closings in 2025%s, %s in the metro"
         % (format(n, ","),
            " across Sekisui House U.S." if tid == "HOU-045"
            else " under Dream Finders" if tid == "HOU-033" else "",
            _ORD[r])
    for r, _nm, n, _s, tid in TABLE
}


# ---------------------------------------------------------------- new cards

L_HOU = "https://www.lennar.com/new-homes/texas/houston"
L_CONTACT = "https://www.lennar.com/contact?divisionNumber=HOULEN&market=HOU&state=TX"
L_10K = "https://www.sec.gov/Archives/edgar/data/920760/000162828026003870/len-20251130.htm"
L_2021 = ("https://newsroom.lennar.com/2021-10-26-Lennar-To-Build-Worlds-Largest-"
          "Neighborhood-Of-3D-Printed-Homes-With-ICON")
L_2022 = ("https://newsroom.lennar.com/2022-11-10-LENNAR-ANNOUNCES-VISIONARY-COMMUNITY-OF-"
          "3D-PRINTED-HOMES-WITH-ICON-IS-NOW-UNDERWAY-IN-GEORGETOWN,-TX")
L_VEEV = "https://www.builderonline.com/money/m-a/lennar-acquires-failed-modular-construction-startup-veev_o"
L_REAMER = ("https://friendswooddevelopment.com/news/lennar-houston-division-announces-"
            "michael-reamer-new-division-president")
L_REAMER23 = ("https://www.prnewswire.com/news-releases/lennar-helping-a-hero-bass-pro-shops-"
              "and-the-highlands-by-caldwell-communities-welcome-corporal-matthew-houston-"
              "usa-ret-an-amputee-injured-in-iraq-to-his-new-home-302016046.html")

P_HOU = "https://www.pulte.com/homes/texas/houston"
P_CENTEX = "https://www.centex.com/homes/texas/houston/conroe"
P_DELWEBB = "https://www.delwebb.com/homes/texas/houston"
P_FULSHEAR = ("https://www.pultegroupinc.com/investor-relations/news/news-details/2022/"
              "Del-Webb-Opens-Third-Houston-Area-Community-Del-Webb-Fulshear/default.aspx")
P_RYEHILL = ("https://www.pultegroupinc.com/investor-relations/news/news-details/2024/"
             "PulteGroup-Breaks-Ground-on-New-Master-Planned-Ryehill-Communities-in-Sugar-Land/"
             "default.aspx")
# The divestiture. The first draft of this card said PulteGroup owns an off-site
# framing plant. It sold it: the intent was announced on the January 2026 call and
# Builders FirstSource, which is on this deck, agreed to buy it in August.
P_ICG = "https://www.housingwire.com/articles/why-builders-firstsource-bought-icg-and-why-pulte-sold-it/"
P_FBR = "https://www.constructiondive.com/news/construction-robot-ai-florida-pultegroup/740963/"
P_10K = "https://www.sec.gov/Archives/edgar/data/822416/000082241617000008/a201610-k.htm"

H_HOU = "https://www.highlandhomes.com/houston/"
H_WHY = "https://www.highlandhomes.com/why-highland-homes"
H_CONTACT = "https://www.highlandhomes.com/contact"
H_ESOP = ("https://www.builderonline.com/builder-100/leadership/top-25-builder-highland-"
          "homes-completes-employee-stock-ownership-plan_o")
H_BRIDGE = "https://www.highlandhomes.com/houston/cypress/bridgeland"
H_SAMPLE = ("https://chartwellpartners.com/real-estate/highland-homes-announces-steve-"
            "sample-as-head-of-land-houston/")
HHS_ABOUT = "https://hhsresidential.com/about/"
HHS_LIN = ("https://chartwellpartners.com/real-estate/highland-homes-names-eddie-lin-as-"
           "managing-director-of-investments-for-hhs-residential/")
HHS_MCGHEE = ("https://homeaidhouston.org/newsroom/homeaid-and-highland-homes-break-ground-"
              "on-transitional-housing-unit-in-conroe/")
T_RELEASE = "https://triconhomes.com/resources/insights/tricon-opens-two-need-communities-in-texas/"
T_PEEK = "https://www.multihousingnews.com/tricon-completes-texas-single-family-rentals/"
T_VERANDA = ("https://yieldpro.com/2023/10/tricon-residential-celebrates-grand-opening-of-"
             "new-90-unit-built-to-rent-community-in-richmond-texas/")

NEW = [

 # Lennar closes more houses in Greater Houston than any other builder, and it
 # is ICON's own customer at corporate level: it invested in ICON's Series B and
 # built Wolf Ranch with it. So it goes where Friendswood and GreenEco already
 # sit, in the section for firms already working with ICON, and the Houston ask
 # is a division pilot inside an existing relationship rather than a cold call.
 ("HOU-166", "Lennar, Houston Division", "Houston / 36 cities, Angleton to Bay City",
  L_HOU,
  KEY_STAT["HOU-166"],
  "6,362 Greater Houston closings in 2025, a 17.0 percent share, first in the metro "
  "on BUILDER's Local Leaders table. Builds in 36 cities and neighbourhoods across "
  "the Houston area, from Angleton to Bay City. Its annual report gives each "
  "division president local control of home design and construction, and keeps "
  "strategy, land and financing at corporate. It credits national purchasing "
  "programmes and its Everything's Included approach for its costs. LEN X, its "
  "venture arm, took part in ICON's Series B in August 2021, and Lennar then built "
  "the 100-home Wolf Ranch community in Georgetown with ICON, designed with Bjarke "
  "Ingels Group. It bought the remaining assets of the modular builder Veev in "
  "January 2024. Friendswood Development, its Houston land arm, and GreenEco, which "
  "came with Rausch Coleman in February 2025, are separate records on this deck.",
  (3, 1, 3, 3),
  "Its annual report puts home design and construction with the division president, "
  "and the parent has already built 100 printed homes with ICON.",
  ("Value-engineered homes with the same features included as standard, built in 36 "
   "Houston-area cities.",
   "6,362 Houston closings in 2025 is far above the band one or two printers cover, "
   "and purchasing runs through national programmes, so the first order is a pilot "
   "inside the division.",
   "LEN X invested in ICON in August 2021, and Lennar built the 100-home Wolf Ranch "
   "community with ICON in Georgetown."),
  [("Michael Reamer", "Division President, Houston")],
  [("Wolf Ranch, Georgetown",
    "100 printed homes with ICON, designed with Bjarke Ingels Group, under way on "
    "10 November 2022.",
    "method_risk",
    "A printed community already paid for by the parent.",
    L_2022),
   ("LEN X and ICON's Series B",
    "Lennar's venture arm took part in ICON's Series B round in August 2021.",
    "method_risk",
    "The parent is an ICON investor, so a Houston pilot sits inside an existing "
    "relationship.",
    L_2021)],
  [L_HOU, L_CONTACT, L_10K, L_2021, L_2022, L_VEEV, L_REAMER, L_REAMER23, LL],
  []),

 ("HOU-167", "PulteGroup, Houston Division", "Houston / Pulte, Centex and Del Webb",
  P_HOU,
  KEY_STAT["HOU-167"],
  "Sells in Greater Houston under three brands: Pulte Homes, Centex and Del Webb. Del "
  "Webb Fulshear, its third Houston-area community for buyers 55 and over, opened on "
  "8 October 2022, and the division broke ground on Ryehill in Sugar Land on 3 July "
  "2024. 1,146 Houston closings in 2025, a 3.1 percent share, fifth in the metro on "
  "BUILDER's Local Leaders table. Its annual report for 2016 says it negotiates "
  "certain materials on a national or regional basis. It bought Innovative "
  "Construction Group, an off-site framing producer in the Jacksonville area, in "
  "2020, and sold it in 2026: Builders FirstSource agreed to buy it in August. Its "
  "chief executive said on 22 July 2026 that PulteGroup wants to be a user of new "
  "construction methods and would prefer not to be the operator. In February 2025 it "
  "piloted FBR's Hadrian X robotic wall system at TerraWalk, Babcock Ranch, Florida.",
  (3, 1, 3, 3),
  "Its chief executive said in July 2026 that it wants to use new building methods "
  "and not operate them, and it sold its off-site framing plant the same year.",
  ("Pulte, Centex and Del Webb communities across Greater Houston, from Conroe to "
   "Fulshear and Sugar Land.",
   "1,146 Houston closings in 2025 sits inside the 400 to 1,500 band, but certain "
   "materials are negotiated nationally or regionally, so a method change is a "
   "corporate pilot.",
   "Owned an off-site framing producer from 2020 until 2026, and piloted FBR's "
   "Hadrian X robotic wall system in Florida in February 2025."),
  [("Lindy Oliva", "Houston Division President")],
  [("Hadrian X pilot, Babcock Ranch",
    "FBR's robotic wall system at the TerraWalk community, February 2025.",
    "method_risk",
    "A robotic wall on a house it sold, with the chief operating officer quoted on it.",
    P_FBR),
   ("Innovative Construction Group",
    "An off-site framing producer, bought in 2020 for $104 million and sold in 2026.",
    "method_risk",
    "The chief executive said it would prefer to use new methods and not operate them.",
    P_ICG)],
  [P_HOU, P_CENTEX, P_DELWEBB, P_FULSHEAR, P_RYEHILL, P_ICG, P_FBR, P_10K, LL],
  []),

 # HHS Residential is Highland's build-to-rent arm, and it is the thread the
 # outside review found. It puts up the same detached house for one rental owner,
 # Tricon, at 90 to 175 homes a site, three times over in Greater Houston. That is
 # the first count asked in its plainest form. It is one card, not two, because
 # HHS is a Highland Homes company and one firm signs for both.
 ("HOU-168", "Highland Homes / HHS Residential", "Houston / Brookshire to Willis",
  H_HOU,
  KEY_STAT["HOU-168"],
  "Texas homebuilder founded in 1985 by Rod Sanders and Jean Ann Brock, "
  "headquartered in Plano and owned by its employees through a stock ownership plan. "
  "Builds in four Texas regions: Austin, Dallas-Fort Worth, Houston and San Antonio. "
  "968 Houston closings in 2025, a 2.6 percent share, tenth in the metro on BUILDER's "
  "Local Leaders table. HHS Residential, founded in 2019 and described by Tricon as "
  "part of the Highland Homes family, builds single-family communities for rental "
  "owners and keeps a Houston office on West Sam Houston Parkway. It built three "
  "Tricon build-to-rent communities in Greater Houston: Veranda in Richmond, 90 "
  "homes; Willow Creek in Tomball; and Peek Road in Katy, 175 homes, the last with "
  "Johnson Development.",
  (3, 2, 1, 3),
  "Through HHS Residential it builds the same detached house for one rental owner, "
  "90 to 175 homes a site.",
  ("Three build-to-rent communities for one owner, Tricon, in Richmond, Tomball and "
   "Katy, beside for-sale communities from Brookshire to Willis.",
   "968 Houston closings in 2025 sits inside the 400 to 1,500 band, so a machine "
   "would be a line inside the business.",
   "Nothing on record. Its own site describes energy features, not a change to the "
   "wall."),
  [("Steve Sample", "Head of Land, Houston"),
   ("Matt McGhee", "Vice President, HHS Residential"),
   ("Eddie Lin", "Managing Director of Investments, HHS Residential")],
  [("Tricon Peek Road, Katy",
    "175 single-family rental homes, developed with Johnson Development and HHS "
    "Residential, completed April 2025.",
    "repeatable",
    "One owner, one detached product, repeated across a whole site.",
    T_PEEK),
   ("Tricon Veranda, Richmond",
    "90 single-family rental homes, with Johnson Development as developer and HHS "
    "Residential as builder, opened October 2023.",
    "repeatable",
    "The same owner and builder, two years earlier.",
    T_VERANDA)],
  [H_HOU, H_WHY, H_CONTACT, H_ESOP, H_BRIDGE, H_SAMPLE, HHS_ABOUT, HHS_LIN,
   HHS_MCGHEE, T_RELEASE, T_PEEK, T_VERANDA, LL],
  []),
]

# Lennar goes with its two subsidiaries; PulteGroup with the other nationals.
ICON_CLIENT = {
    "HOU-166": "LEN X invested in ICON in August 2021, and Lennar built the "
               "hundred-home Wolf Ranch community with ICON in Georgetown. The "
               "relationship exists at corporate level.",
}
NATIONAL = {"HOU-167": "PulteGroup"}
SHORT = {"HOU-166": "Lennar", "HOU-167": "PulteGroup", "HOU-168": "Highland / HHS"}

# tid -> [(name, role, linkedin, source_url, evidence, decider)], the wall_people shape.
PEOPLE = {
    "HOU-166": [
        ("Michael Reamer", "Division President, Houston", None, L_REAMER23,
         "Titled Lennar Houston Division President in a release of 14 December 2023. "
         "Friendswood's announcement dates his appointment to early 2021, succeeding "
         "John Hammond. The annual report gives a division president home design and "
         "construction.", True)],
    "HOU-167": [
        ("Lindy Oliva", "Houston Division President", None, P_RYEHILL,
         "Titled Houston Division President in the Ryehill release of 3 July 2024, and "
         "President of the Houston Division in the Fulshear release of 6 October 2022.",
         True)],
    "HOU-168": [
        ("Steve Sample", "Head of Land, Houston", None, H_SAMPLE,
         "Named to the role on 3 November 2022.", False),
        ("Matt McGhee", "Vice President, HHS Residential", None, HHS_MCGHEE,
         "Named in a HomeAid Houston release of June 2022.", False),
        ("Eddie Lin", "Managing Director of Investments, HHS Residential", None, HHS_LIN,
         "Named to a newly created role running the build-to-rent portfolio.", False)],
}

# The number layer, in the phones.py shape: tid -> (digits, label, source, rule).
PHONE = {
    "HOU-166": ("8886718175", "Houston new-home consultants, toll-free", L_CONTACT, 1),
    "HOU-167": ("2818016008", "Houston sales", P_HOU, 1),
    "HOU-168": ("2815179800", "Houston office", H_CONTACT, 3),
}
MORE = {
    "HOU-168": [("9727893535", "HHS Residential", HHS_ABOUT)],
}

# A firm inbox, read off the firm's own contact page. Never a person's address,
# and never one assembled from a name and a domain.
EMAIL = {
    "HOU-002": ("newhome@colekleinbuilders.com", "New homes",
                "https://colekleinbuilders.com/contact/"),
    "HOU-064": ("info@colinahomes.com", "General enquiries",
                "https://www.colinahomes.com/contact"),
    "HOU-168": ("information@hhsresidential.com", "HHS Residential", HHS_ABOUT),
}


# ---------------------------------------------------------------- existing cards

# The mark follows the reason. D.R. Horton's reason has always said far above
# the band; its mark said Partly.
SCORE = {"HOU-132": {"machine_fit": 1}}

WHY = {
    ("HOU-132", "machine_fit"):
        "4,925 Houston closings in 2025, and 84,863 company-wide, are far above the "
        "band one or two printers cover, so the first order is a pilot inside one "
        "division rather than a purchase.",
    ("HOU-013", "machine_fit"):
        "1,809 Houston closings in 2025, across nine markets in two states. The "
        "volume is above the band one or two printers cover, and it is bought "
        "centrally.",
    ("HOU-008", "machine_fit"):
        "1,428 Houston closings in 2025 sits inside the 400 to 1,500 band, but a "
        "national builder buys through a corporate purchasing desk.",
    ("HOU-045", "machine_fit"):
        "Sekisui House U.S., the parent, closed 1,087 homes in Greater Houston in "
        "2025, inside the 400 to 1,500 band. The parent is folding its US builders "
        "into one company, so purchasing may move.",
    ("HOU-033", "machine_fit"):
        "Dream Finders, the parent, closed 1,048 homes in Greater Houston in 2025, "
        "inside the 400 to 1,500 band. Purchasing may sit at the parent.",
    ("HOU-009", "machine_fit"):
        "1,017 Houston closings in 2025 sits inside the 400 to 1,500 band, and "
        "Mirabella puts 1,200 homes on one site.",
}

SCREEN = {
    "HOU-132": "It has already bought equity in a maker of construction 3D printers, "
               "and it pulled more Houston permits in August 2026 than any other builder.",
}

# (old, new): each old string must be found exactly once, or the build fails.
SYNOPSIS = {
    "HOU-132": [("Houston is named as a market in the annual report and no metro "
                 "closings figure is published.",
                 "4,925 Greater Houston closings in 2025, second in the metro on "
                 "BUILDER's Local Leaders table.")],
    "HOU-013": [("and no construction or purchasing officer.",
                 "and no construction or purchasing officer. BUILDER's Local Leaders "
                 "table puts it third in Greater Houston, with 1,809 closings in 2025.")],
    "HOU-033": [("carries DFH in his own title.",
                 "carries DFH in his own title. Dream Finders closed 1,048 homes in "
                 "Greater Houston in 2025, eighth in the metro on BUILDER's Local "
                 "Leaders table.")],
    "HOU-045": [("Chesmar publishes no Houston community unit counts",
                 "Sekisui House U.S. closed 1,087 homes in Greater Houston in 2025 "
                 "across its brands, seventh in the metro. Chesmar publishes no "
                 "Houston community unit counts")],
    "HOU-147": [("specialised equipment.",
                 "specialised equipment. It agreed in August 2026 to buy Innovative "
                 "Construction Group, the off-site framing producer PulteGroup "
                 "bought in 2020.")],
    "HOU-002": [("with HiveASMBLD, a Houston-based competitor.",
                 "with HiveASMBLD, a Houston-based competitor. Green Cement is a "
                 "product line of Eco Material Technologies, whose PozzoCem Vite is "
                 "the printed mix at Zuri Gardens by its own release of 13 November "
                 "2025. CRH completed its $2.1 billion purchase of Eco Material on 22 "
                 "September 2025. The City's housing department names Cole Klein as "
                 "developer of a second community, Garver Gardens, 200 homes, 160 of "
                 "them affordable.")],
}

# Sources the edits above rest on.
SOURCES = {
    "HOU-132": [LL], "HOU-013": [LL], "HOU-008": [LL], "HOU-024": [LL],
    "HOU-045": [LL], "HOU-033": [LL], "HOU-009": [LL],
    "HOU-002": ["https://colekleinbuilders.com/",
                "https://colekleinbuilders.com/contact/",
                "https://www.globenewswire.com/news-release/2025/11/13/3187443/0/en/"
                "Eco-Material-Technologies-Powers-Zuri-Gardens-Houston-s-First-3D-"
                "Printed-Community-with-Near-Zero-Carbon-Cement.html",
                "https://www.crh.com/media/press-releases/2025/crh-completes-2-1b-"
                "acquisition-of-eco-material-technologies/",
                "https://houstontx.gov/housing/homes/sh-garver-zuri.html"],
    "HOU-064": ["https://www.colinahomes.com/contact"],
    "HOU-147": [P_ICG],
}

# Cole Klein has a site. The card said it did not, while linking the site's own
# about page as its leadership page.
HOMEPAGE = {"HOU-002": "https://colekleinbuilders.com/"}
PHONE_ABSENT = {
    "HOU-002": "The firm's own contact page publishes a street address and an email "
               "address, and no number.",
}

# The supply panel, in the supply.py shape.
SUPPLY_ROWS = [
    ("eco-material", "Eco Material Technologies, a CRH company", "node", "binder",
     "South Jordan, Utah; its Green Cement business is based in The Woodlands",
     "https://ecomaterial.com/",
     "Makes PozzoCem Vite, a rapid-setting near-zero-carbon cement, and PozzoSlag. CRH "
     "completed its $2.1 billion purchase on 22 September 2025.",
     "Its PozzoCem Vite is the printed mix in the 80 homes at Zuri Gardens, and its "
     "own projects page says the mix lets a robot finish a home shell in about two "
     "weeks.",
     [], None),
]
