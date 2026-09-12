# -*- coding: utf-8 -*-
"""Findings that change a record after it was first written.

Each entry is applied by build.py on top of the evidence files, so the original
research stays intact and the correction is visible as its own line.
"""

# target_id -> flags appended to that firm's open items
FLAGS = {
    # Wan Bridge: the team has moved to AiWB
    "HOU-001": [
        "Two names appear here. Wan Bridge issued its New Braunfels build-to-rent release under its "
        "own name on 18 November 2025 with Ting Qiao quoted as co-founder and chief executive. Several "
        "staff profiles list AiWB as the current employer with Wan Bridge as past. Confirm which "
        "entity contracts before an approach.",
    ],
    # Firms where a construction-lead sweep came back empty at the right level
    "HOU-009": [
        "Century publishes a construction manager, a purchasing agent and a starts coordinator in "
        "Houston, all below the level that chooses a structural system. Tanya Rizzo is the one named contact."],
    "HOU-004": [
        "InTown Homes names a supervisor and a warranty coordinator and no construction VP or "
        "director, which is consistent with a smaller operation where Frank Liu decides."],
    "HOU-010": [
        "Camillo's own about page names a chief executive, a chief financial officer, a general "
        "counsel and presidents for Legend Homes and Academy Development. No construction or "
        "purchasing lead is published for any brand."],
    "HOU-028": [
        "Raymond Gabriele is listed AIA on LinkedIn, so the in-house architect that makes Sueba's "
        "vertical integration real is a named, reachable person. He is the method decision-maker here, "
        "not the president."],
    "HOU-007": [
        "John Winniford holds a title at both Signorelli and First America, and it is the same man. "
        "He ran Gehan, then Brightland, as president and chief executive for nearly a "
        "decade and delivered more than 22,000 homes from 2016. He became president of First America "
        "on 17 September 2025 and holds the title President, Homebuilding at Signorelli, the parent. "
        "He spent that decade inside a builder owned by Sumitomo Forestry, a timber group, and left it.",
        "Two of the three people who would have to agree are new. The president arrived in September "
        "2025 and the purchasing lead changed in April 2026.",
        "First America's purchasing changed hands this year. Kristen Rinewalt left in April 2026 after "
        "fifteen years running purchasing there, and Mike Faul now holds the title. Specifications "
        "are reviewed when a purchasing lead changes.",
        "The 750 closings figure for last year, across two markets, is stated in the outgoing "
        "purchasing lead's own post. No other published figure exists for the brand."],
    "HOU-015": [
        "John Winniford holds the title President, Homebuilding at Signorelli and is also president "
        "of First America Homes. Signorelli itself names a commercial-division construction manager "
        "and land-development managers, and no vice president or director of construction."],
    "HOU-045": [
        "Chesmar's construction and purchasing leadership sits in Houston, not at the McKinney head "
        "office. A vice president of construction for Houston North, a company-wide vice president of "
        "construction operations and a vice president of purchasing are all Houston-based, so a wall "
        "decision does not have to travel out of the metro. The separate McKinney and San Antonio "
        "vice presidents cover their own divisions."],
    "HOU-034": [
        "Brightland lost the chief executive who had run it for nearly a decade. John Winniford left "
        "in September 2025 for First America Homes, also screened here, after delivering "
        "more than 22,000 homes from 2016 and expanding the company into Colorado, Florida and "
        "Tennessee. The firm publishes no leadership page."],
    "HOU-003": [
        "The authority's board voted in January 2026 to operate as Housing Alliance HTX, reported by "
        "the Houston Chronicle and on the authority's own news page. The Cuney Homes announcement was "
        "made under the old name, which is the name kept here."],
    "HOU-043": [
        "Newland's own leadership page redirects to Brookfield Residential, which announces the "
        "acquisition and names nobody."],
    "HOU-057": [
        "Both entities now have a citable leadership page: Hartman's own team page names Allen "
        "Hartman, and Silver Star's names Gerald Haddock as chief executive and chairman. The "
        "do-not-approach attaches to the Silver Star side only."],
    "HOU-027": [
        "Greystar's Houston LinkedIn presence is property management, community managers, leasing "
        "managers, maintenance supervisors. No development or construction lead for Summerwell "
        "surfaced in the metro. The build decision for the rental product sits outside Houston."],
    "HOU-021": [
        "Dinerstein has almost no public leadership presence. A full-name company search returns the "
        "owner and then unnamed members for the chief financial officer and staff. There is no "
        "construction or preconstruction lead published."],
    "HOU-033": [
        "Coventry is a Dream Finders Homes brand. Both Houston division presidents carry DFH in their "
        "own titles, so the parent is not incidental, and any method conversation runs through Dream "
        "Finders as well as Coventry."],
    "HOU-014": [
        "LGI runs a vice president of construction per market, Austin, San Antonio, Nashville, Denver, "
        "Seattle, Charlotte, and Houston has its own. Purchasing is the one national role, and it sits "
        "at the Conroe head office. Both halves of a wall decision for the most standardised product "
        "screened here are inside Greater Houston."],
    "HOU-006": [
        "Triten's construction staff below Larry Sloan are construction managers. A Chief Construction "
        "Officer is titled to Triten Corporation, a separate Houston company sharing the name. The "
        "relationship between the two is unresolved."],
    "HOU-008": [
        "Meritage runs Houston as its own division with a division president, a vice president of "
        "operations and a vice president of land development in the metro, under a Sugar Land regional "
        "president. Three of the four decision levels a method change has to clear are inside Greater "
        "Houston."],
    # CastleRock: hypothesis tested, no transfer found
    "HOU-022": [
        "CastleRock publishes a chief financial officer and a vice president with no stated function. "
        "For a builder of 20,000 homes, no construction or purchasing lead is publicly identifiable, "
        "which is unusual at that scale.",
        "Daiwa House Industry holds 80 percent of CastleRock, acquired for about $408 million, "
        "announced 10 August 2021. Tested whether Daiwa's industrialised-housing methods reach the "
        "Texas operation: no technology transfer, prefab pilot, board seat or joint statement found. "
        "Trade press describes Japanese owners preserving the acquired builder without forcing "
        "synergies. The parent is not a route in, and it is not an obstacle either.",
    ],
    # Chesmar: the Sekisui hypothesis was tested and it holds
    "HOU-045": [
        "Sekisui House of Japan bought Chesmar on 10 June 2022 for about $514 million. On 4 September "
        "2025 Sekisui announced consolidating M.D.C. Holdings, Woodside, Holt and Chesmar into one "
        "company to accelerate the transfer of Sekisui technology into the US market, with the full "
        "structure from January 2026. Builder Magazine reported on 12 January 2026 that Sekisui is "
        "transferring its technology and product platforms into those brands, naming Chesmar.",
        "The commitment is documented at parent level and has not reached Texas. Every description of "
        "SHAWOOD manufacturing places frame fabrication in Japan for assembly on US sites. No US "
        "factory or panel line is announced, no Sekisui executive holds a Chesmar title, and no change "
        "to Chesmar's wall or framing method in Houston is on record.",
        "Risk to weigh against the opening: Sekisui plans a SHAWOOD-derived product line launch by the "
        "end of 2026. A parent that industrialises on its own terms could compete with a printed wall "
        "rather than adopt one.",
        "This is the opposite result to the Daiwa test at CastleRock, where no transfer was found at "
        "all, and softer than Sumitomo at Brightland, where the parent has put physical capital into "
        "a competing wood system.",
    ],
    # Brightland: the timber hypothesis now has evidence
    "HOU-034": [
        "Brightland's Houston listings are an area construction manager, sales counselors and "
        "online sales specialists, with no vice president or director of any function. The metro "
        "presence is a sales and field-supervision office; the decisions moved up to the DRB Group "
        "platform after the April 2025 consolidation. There is no local door here.",
        "The Sumitomo Forestry timber position is now evidenced, not speculative. Brightland was "
        "consolidated under The DRB Group on 1 April 2025. Sumitomo bought a Louisiana sawmill on "
        "1 July 2025 for $29 million, enough framing lumber for roughly 14,000 homes a year, to "
        "supply DRB and in-network panel and truss operations under a stated own-more-of-the-stack "
        "strategy. A concrete wall system competes against parent-company capital committed to wood. "
        "No document shows Brightland's own specification has changed.",
    ],
    # Midway: identity resolved
    "HOU-036": [
        "Parkway question resolved. Midway kept sole development control of East River and sold its "
        "interest in the Parkway Ventures joint venture to Parkway in December 2024. Bradley Freels "
        "is confirmed Chairman and Chief Executive Officer on Midway's own leadership page. "
        "Rob Sigler is Executive Vice President of Construction, Investment and Development, which "
        "is the title that decides a structural system here, and his own feed carries mass-timber "
        "construction from Kirksey. The method conversation at Midway has a named owner who has "
        "already shown interest in one alternative system. "
        "Larry Sloan, formerly EVP of investment and development, left in November 2023. He is now "
        "Chief Development Officer at Triten Real Estate Partners, also screened here, so the "
        "same person is reachable on the Triten card.",
    ],
    # Hartman: split the entity
    "HOU-057": [
        "Do not approach is confirmed, and it attaches to Silver Star Properties REIT specifically. "
        "Silver Star filed Chapter 11 twice, September 2023 and again 28 May 2026, disclosing $75 "
        "million of liabilities against $100 million of assets and four defaulted loans. Gerald "
        "Haddock is chief executive. An SEC inquiry opened February 2024 and Silver Star sued Al "
        "Hartman for fraud and breach of fiduciary duty in December 2023, settled in 2025 with "
        "Hartman paying legal fees.",
        "Hartman Properties, the separate private entity Al Hartman still leads, carries no "
        "bankruptcy or litigation of its own. If a Hartman approach is ever made it must be to that "
        "entity, and the principal is the same person Silver Star sued.",
    ],
}

# target_id -> per-axis score override, applied before marks are computed.
# Only ever move a score on new evidence, and write the evidence into FLAGS.
SCORES = {
    # Chesmar: the parent's industrialised-construction commitment is documented and names
    # Chesmar directly. Moves innovation from absent to partial. Not to clear, because no
    # change to Chesmar's own Texas method is evidenced.
    "HOU-045": {"innovation": 2},
}

# target_id -> per-axis reason override, matched to a SCORES change
WHY_OVERRIDE = {
    "HOU-045": {"innovation": "Folded into Sekisui House U.S. in January 2026 under a stated mission to "
                              "transfer Sekisui construction technology into the legacy brands."},
}

# target_id -> replacement verdict line
VERDICTS = {
    "HOU-051": "A 16-acre Ion District owned by Rice Management Company, whose president and the "
               "Ion's executive director are both named. Institutional research space, not a "
               "repeated wall.",
    "HOU-046": "No ground-up start with figures. The president question is resolved: Scooter Hicks "
               "is president under Jason Johnson as chief executive.",
    "HOU-053": "Sells land. 587 acres at Beacon Hill. The leadership is four named people with "
               "titles, chairman, chief financial officer and two vice presidents.",
    "HOU-043": "3,600-acre Elyson, but Newland has been absorbed into Brookfield Residential and no "
               "longer publishes its own leadership. The one Houston name on record is from 2019.",
    "HOU-001": "Builds and holds build-to-rent and spent six years on its own construction software and "
               "site robotics. It has already paid for an unproven way of building, with its own money.",
    "HOU-034": "110 communities, but parent Sumitomo Forestry bought a sawmill and is integrating wood "
               "framing across the platform Brightland sits in.",
    "HOU-045": "Now part of Sekisui House U.S., whose stated mission is transferring Japanese "
               "construction technology into its US brands. The parent believes in industrialised "
               "building; nothing has reached Texas yet.",
    "HOU-057": "Silver Star Properties REIT is in its second Chapter 11 with four defaulted loans. "
               "Do not approach.",
}

# The competitor that already supplies this market.
COMPETITOR = {
    "name": "HiveASMBLD",
    "line": "The only printer with repeat production work inside Greater Houston. Not the only one printing here: PERI built a showcase house in Spring Branch.",
    "facts": [
        ["Formed", "January 2024, merging Hive3D (Timothy Lankau, 2022) and ASMBLD Modular (Ethan Wong). "
                   "Co-chief executives. Houston. PitchBook lists 2023, which conflicts."],
        ["Material", "Green Cement of Jewett, Texas, David McNitt as Director of Technology. Green Cement "
                     "is a subsidiary of Eco Material Technologies, which CRH plc acquired for $2.1 billion "
                     "in July 2025. The material supply sits behind a major building-products group."],
        ["In market", "Zuri Gardens, 80 homes, with a $1.8 million City of Houston subsidy. Gulf Shore "
                      "Estates, 23 of 26 homes. Avenue J, a two-unit duplex."],
        ["Their claim", "Steve Commander of Commander Home Builders is on record at roughly 50 percent "
                        "faster and 5 to 7 percent cheaper."],
        ["Where they are soft", "Published compressive strength appears as both 6,500 and 8,000 psi across "
                                "outlets. A four-day whole-house estimate was called potentially optimistic "
                                "by their own staff after clogged nozzles and blown hoses. No funding figure "
                                "is public."],
        ["The timing problem", "They are building now. Titan deliveries start early 2027. Anyone who signs "
                               "with them this year is unavailable to ICON until their next phase."],
    ],
}
