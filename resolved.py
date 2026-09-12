# -*- coding: utf-8 -*-
"""What the open items became.

The firm cards used to carry a list called Open items. It was a research
notebook: half of it told a reader something true about the firm, half of it
told a researcher what to do next. The second half does not belong on a page
somebody outside the project will read, so the list came off.

Nothing was thrown away. Sentences that carried a fact moved into the record,
either into the firm's own description or onto the contact they qualified.
Statements that a field is empty became one line in the method block, because
ninety separate notes saying nothing is published say less than one sentence
saying every empty field was checked. Everything unresolved went to
docs/OPEN_ITEMS.md, which is the internal register and is not published.
"""

# target_id -> sentences appended to the firm's description
FIRM_NOTES = {
 "HOU-002": [
  "Cole Klein Builders is currently building with HiveASMBLD, a Houston-based competitor.",
  "There is no person called Cole Klein. The firm's own about page names Vanessa Cole and Harry Klein as its founders, so the company name joins the two surnames."
 ],
 "HOU-016": [
  "Commander Home Builders is currently building with HiveASMBLD, a Houston competitor.",
  "The timeline and cost-savings figures are the owner's own statements and are not independently verified."
 ],
 "HOU-017": [
  "Elpis 3D Home Builders is currently building with HiveASMBLD."
 ],
 "HOU-001": [
  "Wan Bridge issued its November 2025 release under its own name. Several staff profiles list AiWB as the current employer and Wan Bridge as past."
 ],
 "HOU-004": [
  "InTown Homes, Lovett Commercial and Lovett Homes may be distinct legal entities under common ownership. The structure is not disambiguated.",
  "InTown Homes names a supervisor and a warranty coordinator on its site and no construction vice president or director."
 ],
 "HOU-128": [
  "The printed house is in Fort Worth. The firm is headquartered in Houston; the project is not."
 ],
 "HOU-073": [
  "Brohn sits under Clayton Properties Group, the homebuilding arm of Clayton Homes, which is owned by Berkshire Hathaway.",
  "Clayton describes Brohn as three affiliated entities under its umbrella. Where Houston purchasing sits, local or national, is not published."
 ],
 "HOU-009": [
  "The headquarters is taken from a general corporate record and is not reconfirmed on a company page.",
  "Century publishes a construction manager, a purchasing agent and a starts coordinator in Houston. Tanya Rizzo is the one named contact.",
  "Century Communities publishes no statement on modular, panelized or printed construction."
 ],
 "HOU-007": [
  "John Winniford became president of First America on 17 September 2025 and holds the title President, Homebuilding at Signorelli, the parent. He ran Gehan, then Brightland, as president and chief executive for nearly a decade and delivered more than 22,000 homes from 2016.",
  "Kristen Rinewalt left in April 2026 after fifteen years running purchasing at First America. Mike Faul now holds the title.",
  "The 750 closings figure covers two markets and comes from the outgoing purchasing lead's own post. No other published figure exists."
 ],
 "HOU-065": [
  "The 300-closings figure and the even-flow description come from a Builder Magazine profile of 2014 performance.",
  "HousingWire reports 973 homes and $310 million in 2025, up 17 percent."
 ],
 "HOU-123": [
  "Tiona Homes is a division of Onsite ICF, which produces and licenses its own foam-block wall system."
 ],
 "HOU-028": [
  "Raymond Gabriele is listed AIA on LinkedIn. He is the in-house architect behind Sueba's vertical integration."
 ],
 "HOU-045": [
  "Sekisui House of Japan bought Chesmar on 10 June 2022 for about $514 million. On 4 September 2025 Sekisui announced consolidating M.D.C. Holdings, Woodside, Holt and Chesmar into one company to accelerate the transfer of Sekisui technology into the US market, with the full structure from January 2026. Builder Magazine reported on 12 January 2026 that Sekisui is transferring its technology and product platforms into those brands, naming Chesmar.",
  "The parent commitment has not reached Texas. No US factory, no Sekisui executive at Chesmar, and no change to Chesmar's method is on record.",
  "Sekisui plans a SHAWOOD-derived product line launch by the end of 2026."
 ],
 "HOU-061": [
  "The chief executive is on record saying the firm does not compete on volume. Its entry price point is $170,000.",
  "The firm has six employees and no purchasing department. The purchasing manager also runs accounts payable."
 ],
 "HOU-063": [
  "The cumulative figure is the firm's own. No single-year closings number is published, so the annual rate is an average."
 ],
 "HOU-003": [
  "Existing and planned unit counts for Cuney Homes are not disclosed in the sourced article.",
  "The authority's board voted in January 2026 to operate as Housing Alliance HTX. The Cuney Homes announcement was made under the earlier name, which this record uses."
 ],
 "HOU-008": [
  "The land purchase price for Trinity Landing is not disclosed.",
  "The Meritage headquarters is taken from a general corporate record and is not reconfirmed on an investor-relations page.",
  "Meritage runs Houston as its own division with a division president, a vice president of operations and a vice president of land development in the metro, under a Sugar Land regional president."
 ],
 "HOU-074": [
  "The 324-closings figure is from 2022, before the acquisition."
 ],
 "HOU-010": [
  "Camillo publishes no construction-method or technology content. The zero records an absent search result.",
  "Camillo's own about page names a chief executive, a chief financial officer, a general counsel and presidents for Legend Homes and Academy Development. No construction or purchasing lead is published for any brand."
 ],
 "HOU-022": [
  "CastleRock publishes a chief financial officer and a vice president with no stated function. No construction or purchasing lead is publicly identifiable.",
  "Daiwa House Industry holds 80 percent of CastleRock, acquired for about $408 million and announced 10 August 2021. No technology transfer, prefab pilot, board seat or joint statement between the two is on record.",
  "CastleRock publishes no construction-method or technology content. The zero counts an absent record."
 ],
 "HOU-026": [
  "The Conroe acquisition price is not disclosed.",
  "Cottage Living was acquired rather than developed by the firm."
 ],
 "HOU-127": [
  "Live Lone Star buys homes built to the federal manufactured housing code rather than building them on site.",
  "The community figures date from March 2023 and have not been refreshed."
 ],
 "HOU-125": [
  "The method evidence dates from 2014 and 2015 and was earned under the predecessor name, Durable Residential Builders.",
  "Insulated concrete form is one of several wall methods the firm uses."
 ],
 "HOU-068": [
  "Builder reports 1,062 closings and $621 million in 2025, rank 60 on the 2026 Builder 100. The firm's twentieth-anniversary release, dated December 2014, names Jason Golan as founder."
 ],
 "HOU-064": [
  "The cumulative figure is the firm's own and covers eighteen years.",
  "Builder reports 540 closings in 2025 and 552 in 2024."
 ],
 "HOU-076": [
  "Imagination Homes launched in 2025 and is headquartered in Dallas. No volume figure exists yet.",
  "Imagination Homes is a David Weekley Homes line for entry-level product. Greg Grahmann is a David Weekley division president."
 ],
 "HOU-071": [
  "The firm publishes an eight to ten month build time from design to completion."
 ],
 "HOU-066": [
  "The firm's own retrospective puts volume at 40 to 60 homes a year since a 2005 peak of 59. Mike Dishberger oversees construction and purchasing himself."
 ],
 "HOU-020": [
  "The portfolio figures are company-stated."
 ],
 "HOU-075": [
  "The rename from New Home Company is recent, so older coverage uses the previous name.",
  "Risewell is the 2025 merger of Landsea Homes and The New Home Company, which closed 2,831 and 1,123 homes respectively in 2024. No Houston division figure is published."
 ],
 "HOU-033": [
  "Neither the Coventry nor the Dream Finders name carries a vice president or director of construction or purchasing in Houston. The two division presidents are the only names on file.",
  "Coventry is a Dream Finders Homes brand. Both Houston division presidents carry DFH in their own titles.",
  "Dream Finders' 2024 annual report describes procurement at local, regional and national levels, with national volume used to secure manufacturer pricing."
 ],
 "HOU-069": [
  "The closings figures appear to cover Houston and Austin together rather than Houston alone.",
  "Jeff Dye has been president since February 2020, after 21 years at the firm. No vice president of construction or head of purchasing is published."
 ],
 "HOU-077": [
  "Sitterle Homes is headquartered in San Antonio, where most of its volume sits."
 ],
 "HOU-120": [
  "The firm's named markets run from Houston to Corpus Christi, Dallas and McAllen."
 ],
 "HOU-104": [
  "Botello Builders began on residential work and moved to commercial."
 ],
 "HOU-105": [
  "Encore Concrete Construction was established in 2017."
 ],
 "HOU-101": [
  "The residential page names no client and no project, so the size of that division is unknown.",
  "The firm states that it owns its pump fleet and runs a yard in every location."
 ],
 "HOU-121": [
  "MAREK's walls are interior and non-structural."
 ],
 "HOU-111": [
  "The firm's site has no about pages, and nothing on it sizes the business."
 ],
 "HOU-129": [
  "The published size of the house differs between the printing contractor's release and broadcast coverage, so no figure is carried here."
 ],
 "HOU-119": [
  "M.L. Deer Construction builds commercial work only. No residential project appears on its site."
 ],
 "HOU-109": [
  "Two people carry T&T alongside RD DevCo and E&S Construction in one LinkedIn headline. Neither name appears on T&T's own site."
 ],
 "HOU-117": [
  "The firm states that it works through trade partner relationships rather than self-performing."
 ],
 "HOU-106": [
  "The parent describes Greco as a turnkey commercial concrete contractor operating throughout Texas, running for more than thirty years and established under the Greco name about ten years ago, with a pumping arm of two pump trucks.",
  "Greco lists multifamily among its markets but names no multifamily project.",
  "The parent's own site names Greco among the Satterfield and Pontikes family of companies."
 ],
 "HOU-102": [
  "Harvey Cleary's residential work is apartments and senior living rather than for-sale houses."
 ],
 "HOU-112": [
  "The award-listed panel record was set under the TAS name before the rebrand.",
  "Purchasing sits inside a listed parent company."
 ],
 "HOU-107": [
  "Andrade's published housing exposure is site utilities, not wall work.",
  "A second site carries the name Andrade Concrete and Construction, with a chief operating officer on LinkedIn. Whether the two are one business is unsettled."
 ],
 "HOU-108": [
  "Across the published projects the paving square footage is many times the tilt-wall square footage."
 ],
 "HOU-114": [
  "The tilt-wall page describes self-performed concrete work in the past tense. Whether the firm still owns concrete crews is unconfirmed.",
  "The homepage says 48 million square feet and the tilt-wall page says over 38 million. Both are anchored to 1991.",
  "The tilt-up page lists single and multi-family residences among applications, but no residential project is named on the site."
 ],
 "HOU-110": [
  "The firm's navigation names a residential concrete line covering driveways, engineered slabs, barndominiums and retaining walls."
 ],
 "HOU-113": [
  "The firm's own site names no executive and no Houston office. The Houston address comes from a trade association listing."
 ],
 "HOU-118": [
  "Leola counts more than 900 subcontractors and no direct field crew.",
  "The firm's headquarters and ownership sit in Florida."
 ],
 "HOU-115": [
  "Arch-Con does not own concrete crews. On its award-listed tilt-up job the panels were poured by Encore Concrete Construction, also screened here."
 ],
 "HOU-116": [
  "Self-perform scope is not stated on the firm's own site, so whether it owns concrete crews is unconfirmed."
 ],
 "HOU-006": [
  "The Mill square footage and unit count come from two sources whose detail differs, so the figures are approximate.",
  "The Mill is a 75,000 square foot six-storey office frame in cross-laminated timber, reported as one of Houston's first, alongside 340 apartments and a 14,000 square foot 1890s brick building kept and folded into the new structure. Michael Hsu and EDI were on design. One team ran an unproven structural system and an adaptive reuse on the same six-acre site.",
  "Triten and Radom Capital are the same pair across the Heights packing-plant cluster, M-K-T and the Swift BLDG."
 ],
 "HOU-005": [
  "Unit counts and square footage were not obtained for Heights Mercantile.",
  "Heights Mercantile mixes four restored 1920s and 1940s buildings with a new steel, glass and timber building on the same 2.3 acres.",
  "Michael Hsu Office of Architecture works for Radom here and for ICON at Mueller in Austin. The same architect has already drawn a printed building."
 ],
 "HOU-037": [
  "Sawyer Yards is more than two million square feet across twenty-seven buildings on fifty-five acres, eighteen of them reclaimed. Every project on record is a conversion."
 ],
 "HOU-038": [
  "The unit count is stated only as up to 100.",
  "The Esperson renovation is an office-to-residential conversion of two towers from 1927 and 1941 under a programme reported at about $50 million. The firm is employee owned."
 ],
 "HOU-072": [
  "Volume is spread across four markets in two states, so the Houston share is unknown.",
  "Jim Lemming moved to chairman in June 2026 after an eighteen-month succession. His son Chris Lemming is president."
 ],
 "HOU-036": [
  "Midway kept sole development control of East River and sold its interest in the Parkway Ventures joint venture to Parkway in December 2024. Bradley Freels is Chairman and Chief Executive Officer on Midway's own leadership page. Rob Sigler is Executive Vice President of Construction, Investment and Development, and his own feed carries mass-timber construction from Kirksey. Larry Sloan, formerly Executive Vice President of investment and development, left in November 2023 and is now Chief Development Officer at Triten Real Estate Partners, also screened here."
 ],
 "HOU-081": [
  "Pagewood's creative work is a joint venture with Wile Interests. Its industrial side builds ground-up on its own.",
  "Preston Luster is the senior construction manager on the team page. No vice president of construction is published, and the two managing principals are the decision layer."
 ],
 "HOU-080": [
  "No outside architect is credited on any project. Design sits with a partner in house."
 ],
 "HOU-082": [
  "The firm's own website is a placeholder with no content, so this record comes from press coverage."
 ],
 "HOU-014": [
  "The Q2 2026 transcript carries no construction-method or technology mention. The innovation score records that absence.",
  "LGI runs a vice president of construction in each market, including Houston. Purchasing is the one national role and it sits at the Conroe head office."
 ],
 "HOU-012": [
  "The Trinity Landing land price is not disclosed."
 ],
 "HOU-025": [
  "The Yardly retrospective article carries no confirmed publication date."
 ],
 "HOU-024": [
  "Community-level unit counts are not sourced."
 ],
 "HOU-034": [
  "Brightland's Houston listings are an area construction manager, sales counselors and online sales specialists, with no vice president or director of any function. The decisions moved up to the DRB Group platform after the April 2025 consolidation.",
  "Brightland was consolidated under The DRB Group on 1 April 2025. Sumitomo Forestry bought a Louisiana sawmill on 1 July 2025 for $29 million, enough framing lumber for roughly 14,000 homes a year, to supply DRB and in-network panel and truss operations under a stated own-more-of-the-stack strategy. No document shows Brightland's own specification has changed."
 ],
 "HOU-015": [
  "The cookie-cutter quote concerns land use and commercial mix, not construction method.",
  "John Winniford holds the title President, Homebuilding at Signorelli and is also president of First America Homes. Signorelli itself names a commercial-division construction manager and land-development managers, and no vice president or director of construction.",
  "Austin Point acreage is cited as both 4,700 and 6,400 acres in different releases, and the two are not reconciled."
 ],
 "HOU-011": [
  "The Q1 2026 earnings call carries no mention of construction technology, automation, modular, offsite, labour or cycle time."
 ],
 "HOU-041": [
  "Caldwell publishes no construction-method content. The zero counts an absent record."
 ],
 "HOU-040": [
  "Johnson Development publishes no construction-method content. The zero counts an absent record."
 ],
 "HOU-043": [
  "Newland's own leadership page redirects to Brookfield Residential, which announces the acquisition and names nobody."
 ],
 "HOU-078": [
  "GreenEco is owned by Rausch Coleman Homes, which Lennar bought on 10 February 2025. Lennar built the hundred-home Wolf Ranch community with ICON, so the relationship exists at corporate level.",
  "GreenEco was acquired by Rausch Coleman Homes in 2020. Lennar announced the completed acquisition of Rausch Coleman on 10 February 2025, naming Houston among the markets added. GreenEco still sells under its own name in Houston listings."
 ],
 "HOU-042": [
  "Friendswood is wholly owned by Lennar, which built the hundred-home Wolf Ranch community with ICON in Georgetown, designed by Bjarke Ingels Group and completed in 2025. The relationship exists at corporate level."
 ]
}

# "target_id|person" -> sentences appended to that contact's evidence
PERSON_NOTES = {
 "HOU-016|Steve Commander": [
  "No LinkedIn profile is held for Steve Commander. The similar handle belongs to a regional retail operations leader, not the San Leon builder."
 ],
 "HOU-017|Tony M. Brown": [
  "No LinkedIn profile is held for Tony M. Brown. The closest match is a Tony Brown in Knoxville, Tennessee."
 ],
 "HOU-004|Frank Liu": [
  "Frank Liu's exact title at each entity is not confirmed on a company page.",
  "No LinkedIn profile is held for Frank Liu. No profile under that name is identifiable as the InTown and Lovett principal."
 ],
 "HOU-007|John Winniford": [
  "No LinkedIn profile is held for John Winniford. The profile under that name does not name Signorelli or Brightland. His Signorelli bio is linked instead."
 ],
 "HOU-035|Nicole Cassier": [
  "Nicole Cassier's LinkedIn headline gives her title but not her employer."
 ],
 "HOU-060|Kevin Holland and John Payson": [
  "No title is published for Kevin Holland or John Payson on the firm's site, in the GHBA directory or on LinkedIn."
 ],
 "HOU-074|Stephen Ray": [
  "Stephen Ray's post-acquisition title is not published, and no LinkedIn profile matches him at either Devon Street or Smith Douglas."
 ],
 "HOU-068|Matthew Roland and Diane Danilov": [
  "No LinkedIn profile is held for Matthew Roland or Diane Danilov. Only data aggregators carry their titles, and those were not used."
 ],
 "HOU-071|Greg Hawes": [
  "Greg Hawes is Manager on the firm's own page and President on his LinkedIn. No profile is held for Katy Hawes or Matt Norris."
 ],
 "HOU-062|Christian Sommer and Keith Blum": [
  "No LinkedIn profile is held for Christian Sommer or Keith Blum. Christina Wright, Director of Purchasing, is the one linked contact."
 ],
 "HOU-077|India Kinslow": [
  "No page outside a data aggregator names India Kinslow with a title at Sitterle, so no link is held for her."
 ],
 "HOU-067|Patrick Mustoe and Art Maya": [
  "No LinkedIn profile is held for Patrick Mustoe or Art Maya, and no annual volume is published."
 ],
 "HOU-120|Matt Zetlmeisl": [
  "Matt Zetlmeisl has no LinkedIn profile. The firm's own site is the only source that names him."
 ],
 "HOU-106|Trey Green": [
  "Trey Green is named on Satterfield and Pontikes' own team page and returns no LinkedIn result against the parent's name."
 ],
 "HOU-112|Travis Boone": [
  "Travis Boone runs the listed parent, not the Houston concrete business."
 ],
 "HOU-005|Barton Kelly": [
  "Barton Kelly's LinkedIn headline reads Vice President at Radom Capital; the firm's own team page lists him as Principal. The titles conflict."
 ],
 "HOU-037|Jon Deal": [
  "Jon Deal's title comes from a third-party database, not from a company page."
 ],
 "HOU-036|Bradley Freels": [
  "No LinkedIn profile is held for Bradley Freels. The name matches other people's profiles, none of them at Midway."
 ],
 "HOU-025|Amy Rino": [
  "Amy Rino is now Chief Customer Officer at Taylor Morrison in Scottsdale, not Houston division president. No current Houston division leader is identified."
 ],
 "HOU-034|Young Nam": [
  "Young Nam's LinkedIn headline gives the title and metropolitan area but does not name The DRB Group. Name, function and geography match the parent's page."
 ]
}

# target_id -> a replacement screen sentence
SCREEN_NOTES = {
 "HOU-007": "Two of the three people who would have to agree are new. The president arrived in September 2025 and the purchasing lead changed in April 2026."
}
