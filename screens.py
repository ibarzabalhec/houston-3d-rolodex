# -*- coding: utf-8 -*-
"""One-line verdict per target. This is the authoritative screen text.

build.py replaces every record's mvp_screen with the line here and fails loudly
if a target_id is missing, so there is exactly one place this text lives.
Keep each line to one or two short sentences. The evidence blocks carry the detail.
"""

VERDICT = {
# already printing
"HOU-002": "80 printed homes on one site, the largest printed project in the metro. HiveASMBLD supplies it.",
"HOU-016": "23 of 26 homes printed. Owner cites 50 percent faster and 5 to 7 percent cheaper. HiveASMBLD supplies it.",
"HOU-017": "One printed duplex in the East End. Proof of printed party walls inside the city limits. HiveASMBLD supplies it.",

# all three hold
"HOU-001": "Builds and holds build-to-rent, and spent six years on its own construction software and site robotics.",
"HOU-007": "1,300 homes a year and it markets its wall assembly. The parent owns the land, so nobody else vetoes the method.",
"HOU-004": "Three-storey attached townhomes at citywide volume. The same owner commissioned OMA for POST Houston.",
"HOU-006": "Financed a cross-laminated timber frame at The Mill. 294 units at Aliana land in Titan's first delivery window.",
"HOU-009": "1,200 homes across only 18 plans on one site, with a record 112-day cycle and a 5 percent direct-cost cut.",
"HOU-008": "1,000 homes at Trinity Landing and a sub-110-day cycle held four quarters. No wall-system statement on record.",
"HOU-005": "Michael Hsu at Montrose Collective, $104.75M financed. Fifteen projects in one district, so volume is concentrated rather than deep.",
"HOU-035": "Five affordable developments in one neighbourhood, framed post-Harvey by Rice's Kinder Institute. $3.4M is the only figure.",
"HOU-036": "East River is 60 blocks on one site. No capital figure disclosed and the Parkway relationship is unresolved.",
"HOU-028": "346 units, with its own architect and general contractor in-house. No third party to veto a method change.",

# two of three hold
"HOU-003": "$600M across five phases to 2032. Federal money and open procurement, but no method track record.",
"HOU-014": "The most standardised product here, headquartered in the metro. Its Q2 2026 call mentions method, labour and cycle time zero times.",
"HOU-024": "14 named Houston communities and a Texas regional president. No firm-specific method evidence found.",
"HOU-010": "10,800 rental homes across 115 communities, built and held. No construction-method statement anywhere.",
"HOU-022": "20,000 homes since 2004. Daiwa House owns a stake, which is worth testing. No published method evidence.",
"HOU-023": "125,000 homes, Houston HQ, 50 years. Its supplier recognition covers insulation and fire-stopping, not the envelope.",
"HOU-013": "120 communities and local ownership. Its published innovation page covers smart-home features and floor plans.",
"HOU-031": "36 freestanding emergency centres and over 100 build-to-suits, the most repeated small-commercial format screened.",
"HOU-032": "Attached townhome production, which is the right product type. Ownership sourced only from a contact database.",
"HOU-019": "$155M into 389 build-to-rent homes, Houston HQ, holds long term. Figures date to 2022.",
"HOU-027": "156 units inside Sunterra, a Houston-based development director, and a 10,000-home national brand. Costs withheld.",
"HOU-011": "11,400 acres and $900M from Pershing Square, but it sells lots, so the builder buys the wall rather than Howard Hughes.",
"HOU-012": "1,000 homes at Trinity Landing and three Houston land deals in six months under a named division president.",
"HOU-018": "$3.1B portfolio and a repeated Town Center format. Retail shells compete against tilt-wall, not stick framing.",
"HOU-020": "$7.5B invested and parcHAUS funds seven rental communities under a named Houston director. No Houston site named.",
"HOU-025": "A 240-home Houston build-to-rent community and a dedicated brand. The division president role dates to 2018 and is unconfirmed.",
"HOU-021": "186 build-to-rent homes with Harrison Street and 70 years in Houston. Launch coverage is amenities only.",
"HOU-034": "110 communities. Owner Sumitomo Forestry is a timber group and may prefer timber framing.",
"HOU-026": "314 homes in Conroe and a stated shift to self-development. Its declared technology is smart-home fittings.",
"HOU-033": "Close to 100 communities inside Dream Finders, which bought parent MHI in 2021. Two Houston division presidents are named.",
"HOU-030": "Two land positions in target counties within 24 months. Every purchase price is undisclosed.",
"HOU-029": "An in-house construction arm and a Houston HQ since 1982, but no Houston project could be sourced.",
"HOU-045": "Spring HQ and a builder role at Sienna. No community unit counts, and the innovation search returned directory links only.",
"HOU-044": "Two Katy duplex projects a mile apart, 366 units. No capital figure and no method evidence.",
"HOU-037": "Twenty years converting industrial buildings, 27 of them. Adaptive reuse leaves little new wall to print.",
"HOU-047": "More than 80 retail projects, but recent Houston activity is buying existing centres rather than building.",
"HOU-048": "7.2M sf across nine centres. Current activity is leasing and management, not ground-up.",

# screened out
"HOU-039": "Sells lots. Sunterra's 2,303 acres and 15 builders make it the best channel in Houston, not a customer.",
"HOU-038": "Interior conversion of a 1927 tower. Willing to take on a hard build, but almost no new exterior wall.",
"HOU-015": "Sells lots, but owns First America Homes, which is a strong target. Approach the pair together.",
"HOU-041": "Sells lots. Towne Lake and The Highlands carry 4,000 homes across 12 builders. No published method evidence.",
"HOU-040": "Sells lots across 14 Houston masterplans. Channel value is high, wall purchasing is nil.",
"HOU-042": "Sells lots, wholly owned by Lennar since 2000, so the route is Lennar. No named executives found.",
"HOU-046": "No ground-up start with figures, and two people hold the President title across different dated sources.",
"HOU-051": "A 16-acre Ion District, but no leadership name could be sourced from any page, so there is no contact to call.",
"HOU-054": "Big-box industrial. Tilt-wall concrete is the incumbent and the wall is a low share of total cost.",
"HOU-049": "A 20-storey concrete tower. Wall assembly is a small share of high-rise cost.",
"HOU-050": "High-rise and mid-rise owner-operator. No ground-up start sourced.",
"HOU-043": "3,600-acre Elyson, but no executive confirmed and the HQ rests on a third-party listing. Too thin to action.",
"HOU-053": "Sells land. 587 acres at Beacon Hill. The leadership page lists four names with no titles.",
"HOU-052": "$550M at Texas A&M Innovation Plaza, but the product is high-rise institutional.",
"HOU-055": "Buys existing multifamily. No ground-up Houston development identified.",
"HOU-056": "$1.2B under management and no named Houston ground-up position.",
"HOU-057": "Corporate identity unresolved between Hartman and Silver Star. Do not approach until clarified.",
}

# Six signal labels for 63 signals was more taxonomy than the evidence supports.
# geometry folds into method_risk (both are paying for the harder thing).
# capital is dropped: every card already carries its own capital block.
SIGNAL_MERGE = {"geometry": "method_risk", "capital": "repeatable"}
