# -*- coding: utf-8 -*-
"""The creative projects layer: retail and hospitality adjacent, design-led.

These firms do not repeat a plan, so the machine-fit count fails them and the
builder screen throws them out. That is the screen being too narrow rather than
the firms being wrong. They matter for a different reason: they hire named
architects, they take on hard builds, and they are the teams most likely to run
a hybrid job where a printed element sits inside a conventional project. One
built reference in a Houston design-led project is worth more attention than a
subdivision.

Triten is the proof the category is real. It financed a cross-laminated timber
office frame at The Mill, reported as one of Houston's first, on a site that
also keeps a 14,000 square foot 1890s brick building. One project, one team,
an unproven structural system and an adaptive reuse side by side. That is
precisely the shape of a hybrid print job.
"""

# Existing records that move into this group rather than being screened out.
CREATIVE = {
    "HOU-005": "Radom Capital",
    "HOU-072": "Partners in Building",
    "HOU-006": "Triten Real Estate Partners",
    "HOU-036": "Midway",
    "HOU-037": "The Deal Company (Sawyer Yards)",
    "HOU-038": "Cameron Management",
    "HOU-080": "Concept Neighborhood",
    "HOU-081": "Pagewood",
    "HOU-082": "Wile Interests",
    "HOU-083": "Braun Enterprises",
}

# (id, name, region, url, key_stat, synopsis, scores, verdict, why triple,
#  principals, projects, sources, flags)
NEW_CREATIVE = [

("HOU-080", "Concept Neighborhood", "East End, Harris", "https://www.conceptneighborhood.com/",
 "17 acres at The Plant, Second Ward",
 "Adaptive-reuse developer of Houston's East End founded in 2020 by six managing partners, two of "
 "whom launched the Axelrad beer garden, converting a former W-K-M warehouse campus into a "
 "walkable district.",
 (1, 1, 2, 1),
 "The only firm screened whose founders operate hospitality themselves rather than leasing "
 "to operators. Seventeen acres of industrial conversion in the East End.",
 ("Four blocks of eighty-year-old industrial buildings, each one different. There is no plan to repeat.",
  "Conversion work leaves little new wall. A printed element would have to be an addition rather "
  "than the building.",
  "They restored an 1890s building to open Axelrad and took a National Register industrial basilica "
  "on at The Factory. This is a team that chooses the harder build on purpose."),
 [("David Kelley", "Managing Partner, Projects and Finance"),
  ("Jeffrey Kaplan", "Managing Partner, Brokerage and Placemaking, co-founder of Axelrad"),
  ("Monte Large", "Partner, Design and Placemaking"),
  ("Jeremy Roberts", "Managing Partner, Projects and Legal")],
 [("The Plant", "Second Ward. Seventeen acres, more than four blocks of mostly historic buildings "
                "around eighty years old, including a former industrial laundry. Construction from "
                "late 2022.",
   "method_risk", "A district-scale conversion with room for a new-build element inside it.",
   "https://www.conceptneighborhood.com/projects"),
  ("Axelrad and The Factory", "An 1890s building restored as a beer garden, and a 1940s industrial "
                              "building on the National Register.",
   "method_risk", "Founders who operate the hospitality they build, so the brief is theirs to set.",
   "https://www.conceptneighborhood.com/projects")],
 ["https://www.conceptneighborhood.com/team", "https://www.conceptneighborhood.com/projects"],
 ["No outside architect is credited on any project. Design sits with a partner in house, which "
  "means a method conversation goes straight to a decision-maker rather than through a consultant."]),

("HOU-081", "Pagewood", "Houston", "https://www.pagewood.com/",
 "East Blocks, 513,000 sf across ten EaDo blocks",
 "Investment and development firm running industrial and office ground-up alongside East Blocks, a "
 "ten-block EaDo redevelopment with Wile Interests designed by Gensler.",
 (2, 1, 1, 2),
 "Ten contiguous EaDo blocks, 513,000 square feet in phase one, Gensler on design and SWA on "
 "landscape. It builds ground-up industrial elsewhere, so it is not conversion-only.",
 ("Ten blocks under one plan is concentration, but every building is its own problem.",
  "The phase-one programme is retail, office and parking rather than repeated units.",
  "It chose to keep eighty-year-old warehouses that would have been cheaper to demolish. The "
  "partner said so on the record."),
 [("Paul Coonrod", "Founder and Managing Principal"),
  ("Mat Volz", "Managing Principal"),
  ("Preston Luster", "Senior Construction Manager")],
 [("East Blocks", "EaDo. Phase one is 513,000 square feet: 196,000 retail, 112,000 office, 205,000 "
                  "parking, across four addresses. Redevelopment from the second quarter of 2024 "
                  "through 2027, with Gensler and SWA.",
   "method_risk", "Randolph Wile of the partner firm: by almost every measure it would be easier to "
                  "demolish and redevelop these blocks from a clean slate.",
   "https://www.pagewood.com/")],
 ["https://www.pagewood.com/team"],
 ["The creative work is a joint venture with Wile Interests, so both firms have to agree. The "
  "industrial side of Pagewood builds ground-up on its own."]),

("HOU-082", "Wile Interests", "Houston and Katy", "https://www.pagewood.com/",
 "Ground-up in Katy, adaptive reuse in EaDo",
 "Developer that builds ground-up medical office and retail in Katy and is the joint-venture "
 "partner on the East Blocks conversion in EaDo.",
 (2, 1, 1, 1),
 "The clearest does-both record among the smaller creative firms: ground-up medical and retail in "
 "Katy, conversion in EaDo.",
 ("Two quite different programmes in two submarkets. No repeated unit.",
  "Medical office and retail shells rather than houses.",
  "Its president is the one quoted explaining why the firm kept the old warehouses instead of "
  "clearing the site."),
 [("Randolph Wile", "Founder and President")],
 [("Katy Green and Medical Plaza West", "Katy. Ground-up Class A medical office and retail.",
   "repeatable", "Ground-up work, which is where a printed wall has something to do.",
   "https://www.bisnow.com/houston/news/office/modernized-medical-office-building-to-break-ground-in-katy-90935"),
  ("East Blocks", "EaDo. Joint venture with Pagewood on ten blocks of mid-century warehouses.",
   "method_risk", "Chose retention over demolition and said so publicly.",
   "https://therealdeal.com/texas/houston/2023/11/13/pagewood-wile-to-convert-eado-houston-warehouses/")],
 ["https://therealdeal.com/texas/houston/2023/11/13/pagewood-wile-to-convert-eado-houston-warehouses/"],
 ["The firm's own website is a placeholder with no content, so everything here comes from press. "
  "Reach the firm through the Pagewood relationship."]),

("HOU-083", "Braun Enterprises", "Houston, San Antonio and Austin",
 "https://braunenterprises.com/",
 "Ground-up retail in the Heights and small flex industrial",
 "Retail and boutique-office developer working across three Texas cities, building ground-up "
 "neighbourhood retail rather than converting.",
 (2, 2, 0, 1),
 "The one firm in this category that mostly builds new. Small-format ground-up retail is the "
 "one repeatable shell in this category.",
 ("Small retail buildings repeated across three cities, which is more repetition than anyone else "
  "in this category.",
  "Retail shells at 20,000 to 25,000 square feet. A printed wall competes with tilt-wall here, not "
  "with stick framing.",
  "No method evidence on record."),
 [("Dan Braun", "President")],
 [("2401 North Shepherd Drive", "Heights. A two-storey 24,000 square foot ground-up retail building "
                                "with about 150 second-storey parking spaces, by Tipps Architecture. "
                                "The existing auto-body building was demolished for it.",
   "repeatable", "Ground-up rather than conversion, which is rare in this category.",
   "https://bakerkatz.com/news/exclusive-see-a-houston-developers-latest-plans-for-a-two-story-heights-retail-project/")],
 ["https://braunenterprises.com/"],
 ["The firm's team page returns a 404. The president's title comes from his own LinkedIn."]),
]

# Extra evidence to attach to firms already in the file, now that the category exists.
EXTRA = {
"HOU-006": [
    "The Mill is the hybrid precedent. A 75,000 square foot six-storey office frame in "
    "cross-laminated timber, reported as one of Houston's first, alongside 340 apartments and a "
    "14,000 square foot 1890s brick building kept and folded into the new structure. Michael Hsu "
    "and EDI on design. One team ran an unproven structural system and an adaptive reuse on the "
    "same six-acre site.",
    "Triten and Radom Capital are the same pair across the Heights packing-plant cluster, M-K-T and "
    "the Swift BLDG. ",
],
"HOU-005": [
    "Heights Mercantile mixes four restored 1920s and 1940s buildings with a new steel, glass and "
    "timber building on the same 2.3 acres, which is the hybrid shape in miniature.",
    "Michael Hsu Office of Architecture works for Radom here and for ICON at Mueller in Austin. The "
    "same architect has already drawn a printed building.",
],
"HOU-037": [
    "Sawyer Yards is more than two million square feet across twenty-seven buildings on fifty-five "
    "acres, eighteen of them reclaimed. Every project on record is conversion, so a printed wall "
    "would have to arrive as a new building on the campus rather than as a retrofit.",
],
"HOU-038": [
    "The Esperson renovation is an office-to-residential conversion of two towers from 1927 and "
    "1941 under a programme reported at about $50 million. The firm is employee owned, which means "
    "the people who would run a pilot also own the outcome.",
],
"HOU-042": [
    "Friendswood is wholly owned by Lennar. ICON and Lennar built the hundred-home Wolf Ranch "
    "community in Georgetown together, designed by Bjarke Ingels Group and completed in 2025. The "
    "introduction into Houston already exists at corporate level; it has not been used "
    "here.",
],
}
