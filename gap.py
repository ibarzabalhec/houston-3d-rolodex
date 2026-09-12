# -*- coding: utf-8 -*-
"""Firms the directory found that the press did not.

The deck was assembled from trade press, master-planned-community builder
rosters and the Builder 100. None of those enumerate a privately held builder
that does not issue releases. The Greater Houston Builders Association member
directory does: 190 companies under Builder - Single Family alone.

Reading that list against the deck found 164 names not on it. Most are custom
and infill shops of one to five homes a year, below the band a printer serves.
Two were production builders that belong here, and one of them is the largest
privately held homebuilder in Greater Houston.

Scores are (repeatability, machine_fit, innovation, capital_access), 3 clears,
2 partial, 0-1 fails.
"""

GAP = [

 # 782 closings in 2025 and 912 in 2024, 22 communities, 38 numbered plans across
 # four series. That is roughly 20 to 24 starts per plan per year, which is the
 # repetition the first count asks about, at a volume a machine works through.
 # It also develops its own land through Woodmere, so a pilot needs nobody else's
 # permission. The objection is on the record and in its own words: it sells
 # "job-built production methods" as a control advantage.
 ("HOU-130", "Long Lake, Ltd.", "Houston / Harris, Montgomery, Fort Bend",
  "https://www.longlakeltd.com/",
  "782 closings in 2025, 38 plans",
  "The largest privately held homebuilder in Greater Houston by its own "
  "description, founded 1997, with more than 29,000 homes delivered. 782 closings "
  "in 2025 and 912 in 2024, ranked 74th on the 2026 Builder 100. Sells in 22 "
  "Greater Houston communities from $249,990 to $627,900, including Sunterra Lakes "
  "and Sunterra North. Publishes 38 floor plans across four product lines, "
  "Briarwood, Discovery, Lake Ridge and Lakewood, and identifies them by number "
  "rather than name. Develops its own land through Woodmere Development Co., which "
  "bought 95 acres in Montgomery County in November 2024 and 494 acres beside "
  "Bridgeland in 2022. Its about page sells job-built production methods as a "
  "control advantage.",
  (3, 2, 0, 3),
  "782 closings across 22 communities on 38 numbered plans, and it develops its own "
  "land, so a pilot needs nobody else's permission.",
  ("22 communities on 38 plans in four series, about twenty starts per plan a year.",
   "782 closings in 2025 sits above the band one or two printers cover, so the first "
   "order is a line inside the business rather than the whole business.",
   "Nothing on record. Its about page argues the other way, for job-built production "
   "methods as a control advantage."),
  [("Craig Jones", "Chief Executive Officer"),
   ("Dustin Rodgers", "Vice President of Construction"),
   ("Dave Dronberger", "Construction Manager"),
   ("Aaron Alford", "Executive Vice President, Woodmere Development Co.")],
  [("The 38-plan library",
    "Four product lines, Briarwood, Discovery, Lake Ridge and Lakewood, identified by "
    "plan number. Creekwood Crossing sells plans 218, 252, 254, 264, 265 and 269 at "
    "1,876 to 2,837 square feet.",
    "repeatable",
    "A numbered plan library repeated across 22 communities is the condition the first "
    "count is looking for, and the reason a wall assembly changed once reaches every "
    "community at the same time.",
    "https://www.longlakeltd.com/new-homes/communities/creekwood-crossing/"),
   ("Woodmere Development Co.",
    "The firm's own land arm. 95 acres at Decker Prairie-Rosehill Road in Montgomery "
    "County, bought from the Brautigam family in November 2024. 494 acres beside "
    "Bridgeland in 2022.",
    "repeatable",
    "It owns the ground it builds on, so a method change does not need a land "
    "developer's approval first.",
    "https://therealdeal.com/texas/houston/2024/11/25/long-lake-purchased-100-acre-tract-in-houston-area/")],
  ["https://www.longlakeltd.com/",
   "https://www.longlakeltd.com/about/",
   "https://www.longlakeltd.com/new-homes/communities/",
   "https://www.builderonline.com/firms/long-lake-limited/",
   "https://sunterratx.com/homebuilders/long-lake/",
   "https://members.ghba.org/memberdirectory/Search/builder-single-family-132864"],
  []),

 # The opposite profile and worth keeping for it: low volume, but one named person
 # holds construction and purchasing together, and the price band absorbs a method
 # premium that Long Lake's does not. It has paid for above-code performance before,
 # which is not a structural method and is not counted as one.
 ("HOU-131", "Caldwell Homes", "Cypress, Porter, Willis / Harris, Montgomery",
  "https://www.caldwellhomes.com/",
  "Three 55+ communities, $448,600 to $875,000",
  "The homebuilding division of Caldwell Companies, launched February 2017, building "
  "single-storey homes for buyers aged 55 and over. Three Greater Houston "
  "communities: The Heritage at Towne Lake in Cypress, Fairway Pines at The "
  "Highlands in Porter, and Chambers Creek in Willis, where a new Heritage "
  "Collection opened in July 2026. Homes run $448,600 to $875,000 at 1,900 to 2,819 "
  "square feet, on a shared plan library whose names repeat across communities. "
  "Ranked 41st on the Houston area 2023 builder list, the only active-adult builder "
  "on it. No annual closings figure is published. Towne Lake is developed by its own "
  "parent, so part of its pipeline sits on ground the group controls.",
  (3, 3, 2, 2),
  "One person holds construction and purchasing, the plan library repeats across all "
  "three communities, and the price band absorbs a method premium.",
  ("The same named plans, Cardinal, Bluebell, Texas Paintbrush, Bayberry II and "
   "Waterlily, sell in more than one community.",
   "Three communities and a rank of 41 in the metro put it inside the band one or two "
   "printers cover.",
   "It has paid for above-code performance, ENERGY STAR certification and a 2020 PRISM "
   "award for an energy-efficient home, but nothing structural."),
  [("Fred Caldwell", "Chief Executive Officer"),
   ("Peter Barnhart", "President"),
   ("Tim Mayo", "Senior Vice President of Operations"),
   ("Kevin Johnson", "Vice President of Construction and Purchasing"),
   ("Anthony Moreno", "Vice President of Sales")],
  [("The Heritage at Towne Lake",
    "Cypress. Heritage Cove, Sunset Harbor Garden Homes and Sunset Harbor Villas, "
    "$448,600 to $875,000. Towne Lake is developed by Caldwell Companies, the parent.",
    "repeatable",
    "Single-storey product on a repeating plan library, on ground the group already "
    "controls.",
    "https://www.caldwellhomes.com/communities/towne-lake"),
   ("Fairway Pines at The Highlands",
    "Porter, Montgomery County, inside a 2,300-acre masterplan. Homes from $471,000, "
    "1,900 to 2,819 square feet.",
    "repeatable",
    "The same plan library again, in a second masterplan, which is what makes the "
    "library worth changing once.",
    "https://www.caldwellhomes.com/communities/the-highlands")],
  ["https://www.caldwellhomes.com/",
   "https://www.caldwellhomes.com/our-team",
   "https://www.caldwellhomes.com/communities",
   "https://www.caldwellhomes.com/communities/towne-lake",
   "https://www.caldwellhomes.com/communities/the-highlands",
   "https://caldwellcos.com/development/caldwell-homes/caldwell-homes",
   "https://www.constructiondive.com/news/caldwell-companies-launches-luxury-active-adult-homes-unit/436653/",
   "https://www.caldwellhomes.com/news/houston-area-2023-builder-rankings-list"],
  []),
]

# The person who can change a wall specification, where the record names one.
DECIDERS = {
    ("HOU-130", "Dustin Rodgers"),
    ("HOU-131", "Kevin Johnson"),
}

# Only where the seat says something the title does not.
DECIDER_NOTES = {
    "HOU-131": "Construction and purchasing sit with one person here, not two.",
}

PEOPLE_LINKS = {
    ("HOU-130", "Craig Jones"): (
        None, "https://www.builderonline.com/firms/long-lake-limited/", None),
    ("HOU-130", "Dustin Rodgers"): (
        "https://www.linkedin.com/in/dustin-rodgers-61a9908a/", None, None),
    ("HOU-130", "Dave Dronberger"): (
        "https://www.linkedin.com/in/dave-dronberger-9b098315/", None, None),
    ("HOU-130", "Aaron Alford"): (
        None, "https://wolffcompanies.com/news/in-off-market-deal-long-lake-buys-494-acres-next-to-bridgeland-for-new-community/",
        "Woodmere is Long Lake's own land arm, so this seat buys the ground the "
        "plans go on."),
    ("HOU-131", "Fred Caldwell"): (None, "https://www.caldwellhomes.com/our-team", None),
    ("HOU-131", "Peter Barnhart"): (None, "https://www.caldwellhomes.com/our-team", None),
    ("HOU-131", "Tim Mayo"): (None, "https://www.caldwellhomes.com/our-team", None),
    ("HOU-131", "Kevin Johnson"): (None, "https://www.caldwellhomes.com/our-team", None),
    ("HOU-131", "Anthony Moreno"): (None, "https://www.caldwellhomes.com/our-team", None),
}

# Published annual closings, for the grid's ordering and the market chart.
CLOSINGS = {
    "HOU-130": (782, 782, 2025, "Builder 100 firm page"),
}
