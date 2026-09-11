# -*- coding: utf-8 -*-
"""The second count, replacing wall share of cost.

Wall share stopped doing any work once the roster became mostly detached
single-family builders: for a house, the wall always carries enough. The
question that actually separates these firms is whether one or two machines
would cover a real share of what they build in a year.

Bands used, applied to houses rather than to revenue:
  3  roughly 25 to 400 homes a year, concentrated in a few communities
  2  400 to 1,500 a year, or the right volume with the purchasing decision
     sitting at a parent, or the right volume with no figure published
  1  above 1,500 a year, bought through a national desk, or a product that
     is not a repeatable low-rise wall at all

MACHINE[target_id] = (score, the reason, in one sentence)
"""

MACHINE = {
# already printing
"HOU-002": (3, "Eighty printed homes on one site is inside the band one machine serves."),
"HOU-016": (3, "Twenty-six homes on one site, twenty-three of them already printed."),
"HOU-017": (2, "One duplex. Proof the method works in the city limits, not a volume that keeps a "
               "machine busy."),

# builders and owner-builders already in the file
"HOU-001": (3, "Builds and holds whole build-to-rent communities, so the output is concentrated "
               "where a machine can stand still."),
"HOU-007": (2, "About 750 closings last year across two markets. A machine would be a line inside "
               "the business rather than the business."),
"HOU-004": (3, "Three-storey attached townhomes at citywide volume, built by one owner who also "
               "develops the land."),
"HOU-009": (2, "1,200 homes on one site is the right concentration, but Century buys nationally."),
"HOU-008": (1, "A national builder closing thousands a year through a corporate purchasing desk."),
"HOU-045": (2, "Four Texas divisions under a Japanese parent. Volume is above the band and the "
               "parent is industrialising on its own terms."),
"HOU-035": (3, "Five affordable developments in one neighbourhood, at a scale one machine covers."),
"HOU-028": (3, "346 units with its own architect and its own general contractor. No third party "
               "is in the decision."),
"HOU-003": (2, "A $600 million programme in five phases, but the product is multifamily and the "
               "procurement is public."),
"HOU-014": (1, "Thousands of closings a year across a dozen states, bought from one office."),
"HOU-024": (1, "A national builder with a corporate purchasing function."),
"HOU-010": (2, "10,800 rental homes held across 115 communities. The volume is far above one "
               "machine, though the build-and-hold model is the right one."),
"HOU-022": (2, "20,000 homes since 2004 is roughly a thousand a year, above the band but not "
               "beyond a two-machine pilot."),
"HOU-023": (1, "125,000 homes and a national purchasing and supply chain function."),
"HOU-013": (1, "120 communities and thousands of closings a year, bought centrally."),
"HOU-032": (3, "Attached townhome production at a volume one machine could carry."),
"HOU-020": (2, "Seven rental communities funded under one Houston director. The firm is run "
               "from Dallas."),
"HOU-026": (3, "156 units inside a single masterplan, built to hold. One machine covers a "
               "community at a time."),
"HOU-033": (2, "Two Houston divisions inside Dream Finders, so the volume fits and the purchasing "
               "may not be local."),
"HOU-034": (1, "110 communities inside the DRB platform, bought by a parent that has put capital "
               "into wood."),
"HOU-044": (2, "A small developer with its own vice president of construction, and no published "
               "unit count to size it."),
"HOU-012": (1, "A national builder, bought centrally, however good the Houston division is."),
"HOU-025": (1, "A national builder with a national build-to-rent brand."),

# multifamily, retail and mixed-use: the wall is not the product
"HOU-006": (1, "Industrial and outdoor storage. There is no repeated house here."),
"HOU-005": (1, "Adaptive reuse and retail. Every project is its own building."),
"HOU-036": (1, "Sixty blocks of mixed-use. The buildings are one-offs, whatever the acreage."),
"HOU-019": (1, "A national multifamily REIT. Mid-rise structure is not a printed low-rise wall."),
"HOU-027": (1, "A global operator. The rental product is managed, not repeated by one builder."),
"HOU-021": (1, "Student and multifamily mid-rise, one building at a time."),
"HOU-029": (1, "Multifamily mid-rise with its own general contractor, which helps, but the product "
               "is not a printed wall."),
"HOU-031": (1, "Freestanding retail shells, which compete against tilt-wall concrete."),
"HOU-018": (1, "Retail centres. Tilt-wall is the incumbent and it is cheap."),
"HOU-030": (1, "Retail. The construction lead is real; the product is not."),
"HOU-047": (1, "Retail brokerage and development, with no repeated low-rise wall."),
"HOU-048": (1, "Retail management and leasing."),
"HOU-037": (1, "Converting industrial buildings leaves almost no new wall to print."),
"HOU-011": (1, "Sells lots. The builder buys the wall."),
"HOU-038": (1, "Converting two 1927 and 1941 office towers to residential. No new exterior wall."),

# the masterplan channel
"HOU-039": (1, "Sells lots. Fifteen builders inside Sunterra buy the walls."),
"HOU-015": (2, "Sells lots and owns First America Homes, so the machine question belongs to the "
               "builder it controls."),
"HOU-041": (1, "Sells lots. Twelve builders across Towne Lake and The Highlands buy the walls."),
"HOU-040": (1, "Sells lots across fourteen masterplans. The channel value is the builders inside them."),
"HOU-042": (1, "Sells lots, wholly owned by Lennar, so the route is Lennar."),
"HOU-043": (1, "Sells lots at Elyson, now inside Brookfield Residential."),
}

# Firms removed from the deck. They were screened, they did not fit, and pages
# that say so are pages nobody reads. Kept here so the work is not repeated.
DROPPED = {
    "HOU-046": "MetroNational. No ground-up start with figures.",
    "HOU-049": "StreetLights Residential. Twenty-storey concrete towers.",
    "HOU-050": "The Finger Companies. High-rise and mid-rise owner-operator.",
    "HOU-051": "Rice Management Company. Institutional research space at the Ion District.",
    "HOU-052": "Medistar Corporation. High-rise institutional and medical.",
    "HOU-053": "Wolff Companies. Sells land at Beacon Hill.",
    "HOU-054": "StoneLake Capital Partners. Big-box industrial, where tilt-wall is the incumbent.",
    "HOU-055": "CAF Capital Partners. Buys existing multifamily.",
    "HOU-056": "Sarofim Realty Advisors. No named person anywhere and no ground-up position.",
    "HOU-057": "Hartman and Silver Star. Second Chapter 11, four defaulted loans.",
}


# The masterplan channel. These firms sell lots; the builders inside their
# communities buy the walls. Only builders that are themselves in this file are
# listed, so the map connects to something.
CHANNEL = {
"HOU-039": ("Sunterra, 2,303 acres in Katy, with fifteen builders",
            ["Tricoast Homes", "Risewell Homes", "Greystar (Summerwell)"]),
"HOU-041": ("Towne Lake and The Highlands, about 4,000 homes across twelve builders",
            ["Partners in Building", "Jamestown Estate Homes", "Sitterle Homes", "Ravenna Homes",
             "Newmark Homes"]),
"HOU-040": ("Fourteen Houston masterplans including Sienna, Cross Creek Ranch, Harvest Green, "
            "Veranda, Jordan Ranch, Woodforest and Grand Central Park",
            ["Westin Homes", "J. Patrick Homes", "Jamestown Estate Homes", "Newmark Homes",
             "Sitterle Homes", "Partners in Building", "Shea Homes"]),
"HOU-042": ("Wholly owned by Lennar since 2000", []),
"HOU-043": ("Elyson, 3,600 acres in Katy, now inside Brookfield Residential",
            ["Newmark Homes"]),
"HOU-015": ("Valley Ranch, Austin Point, Granger Pines and Cielo",
            ["First America Homes"]),
}


# Production homebuilders too large for a single machine to matter. They are not
# a bad target, they are a different one: a corporate pilot rather than a
# purchase, and the decision sits with a national purchasing desk.
NATIONAL = {
    "HOU-014": "LGI Homes", "HOU-013": "Perry Homes", "HOU-023": "David Weekley Homes",
    "HOU-024": "Ashton Woods Homes", "HOU-012": "M/I Homes", "HOU-025": "Taylor Morrison",
    "HOU-034": "Brightland Homes", "HOU-072": "Partners in Building",
}


# Firms already inside ICON's own book. These are here to be acknowledged, not
# prospected. Pointing a business-development file at a company's existing
# clients is the fastest way to look like you did not do the reading.
ICON_CLIENT = {
    "HOU-042": "Wholly owned by Lennar, which built the hundred-home Wolf Ranch community with "
               "ICON in Georgetown, designed by Bjarke Ingels Group and completed in 2025. The "
               "relationship exists at corporate level. Treat Friendswood as a relationship to "
               "acknowledge, not a lead to work.",
}
