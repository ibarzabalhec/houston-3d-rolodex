# -*- coding: utf-8 -*-
"""The competitive field in printed construction, and ICON's own record.

Two things a Houston buyer will ask that this section has to answer. Who else
can print my walls, and why has ICON not built here yet.

The honest answer to the second is that it has not. Every ICON project on the
public record is in Austin or Georgetown. HiveASMBLD and PERI both have named
Houston activity. That absence is the point the screen is built to address.
"""

# ICON's own record, stated from published sources.
ICON = {
 "line": "Every ICON project on the public record is in the Austin area. None is in Houston.",
 "facts": [
  ["Wolf Ranch, Georgetown",
   "100 homes with Lennar, designed by Bjarke Ingels Group, printed on Vulcan. Eight floor plans "
   "and twenty-four elevations, 1,500 to 2,112 square feet. Lennar's November 2022 announcement "
   "put prices from the mid $400,000s; later coverage says $400,000. ICON's own page gives a 2025 "
   "completion, and by August 2024 ninety-eight of the hundred wall systems were printed."],
  ["Lennar in Houston",
   "Lennar owns Friendswood Development Company outright, and Friendswood is screened here. The "
   "relationship that built a hundred houses in Georgetown reaches Houston through that subsidiary."],
  ["Mueller, Austin",
   "Affordable homes with The Mueller Foundation, designed by Michael Hsu, from $195,000. Printing "
   "began the week of 31 July 2025. The same architect works for Radom Capital in Houston."],
  ["Community First! Village, Austin",
   "100 further printed homes with Mobile Loaves and Fishes. ICON's largest programme by count."],
  ["Titan, on the record",
   "A wall-system cost target of about $20 a square foot against a stated $30 to $35 conventional "
   "baseline. Reservations are open on a $5,000 deposit, training is set for the third quarter of "
   "2026 and deliveries from early 2027. No total machine price and no maximum print height has "
   "been published by ICON. A $899,000 figure circulates from a single trade outlet and is not "
   "confirmed anywhere else, so it is not quoted as fact here."],
  ["Houston",
   "No ICON project, partnership or public statement specific to Houston could be found. The "
   "newsroom, the site and general search all return nothing. HiveASMBLD has "
   "repeat production work inside Greater Houston and PERI printed a house "
   "inside the city limits."],
 ],
}

# The field. Ordered by how much they matter to a Houston conversation.
COMPETITORS = [
{
 "name": "HiveASMBLD",
 "links": [
  ["Their site",
   "https://www.hiveasmbld.com/"],
  ["The merger and the two chief executives",
   "https://www.hiveasmbld.com/about"],
  ["Their own project list",
   "https://www.hiveasmbld.com/projects"],
  ["Texas Tribune on the material partner, 6 October 2023",
   "https://www.texastribune.org/2023/10/06/texas-houses-3D-printers-climate/"],
 ],
 "where": "Houston",
 "status": "live",
 "line": "The only printer with repeat production work inside Greater Houston.",
 "facts": [
  # The date discrepancy this used to note came from a contact aggregator, which
  # the deck does not cite for anything else either.
  ["Formed", "January 2024, merging Hive3D, founded by Timothy Lankau in 2022, and ASMBLD Modular, "
             "founded by Ethan Wong. Both are named as co-chief executive on the firm's own about "
             "page, in Houston."],
  # Build 58 cut this back. It had named a cement company in Jewett, Texas, a
  # director of technology, a parent and a $2.1 billion sale, and not one of
  # those strings is on any page the card can cite. The Texas Tribune names the
  # material partner and nothing else here survives.
  ["Material", "The Texas Tribune reports Hive3D partnered with Eco Material Technologies of Utah, "
               "whose chief executive is quoted on the emissions claim for the cement it supplies."],
  ["In market", "Zuri Gardens, 80 homes, with a $1.8 million City of Houston subsidy. Gulf Shore "
                "Estates, 23 of 26 homes. Avenue J, a two-unit duplex. Lumen Villas in Marfa. None "
                "is confirmed complete."],
  ["Their claim", "Steve Commander of Commander Home Builders is on record at roughly 50 percent "
                  "faster and 5 to 7 percent cheaper."],
  ["Where they are soft", "Published compressive strength appears as both 6,500 and 8,000 psi "
                          "across outlets. A four-day whole-house estimate was called potentially "
                          "optimistic by their own staff after clogged nozzles and blown hoses. No "
                          "funding figure is public, and their own chief development officer has "
                          "acknowledged a gap between demonstration and production scale."],
  ["The timing problem", "They are building now. Titan deliveries start early 2027. Anyone who "
                         "signs with them this year is unavailable until their next phase."],
 ],
},
{
 "name": "PERI 3D Construction",
 "links": [
  ["Their site",
   "https://www.peri3dconstruction.com/en"],
  ["The Spring Branch project page",
   "https://www.peri-usa.com/projects/houston-3d.html"],
  ["Their own release on the Houston house",
   "https://www.peri-usa.com/company/press/houston-3d.html"],
  ["PERI on the COBOD BOD2 it distributes",
   "https://www.peri3dconstruction.com/en/cobod-bod2"],
  ["ABC13 Houston on the build",
   "https://abc13.com/post/3d-printing-printed-homes-spring-branch-home-built-with-cive/12850103/"],
 ],
 "where": "Germany, printing in Houston",
 "status": "live",
 "line": "Printed in Spring Branch, inside the city. Houston is not a Hive monopoly.",
 "facts": [
  ["The project", "A house in Spring Branch, Houston, marketed as the nation's largest printed home. "
                  "Published area figures conflict sharply between outlets, from 4,000 to 30,000 "
                  "square feet, and the build paused for months without explanation."],
  ["The machine", "PERI prints with COBOD's BOD2, so the capability is available to anyone in Texas "
                  "who buys the same machine. PERI is a customer of the printer, not its maker."],
  ["Why it matters here", "Houston is not a single-supplier market. A European formwork group "
                          "printed a showcase house inside the city limits, on a machine any Texas "
                          "contractor can buy."],
 ],
},
{
 "name": "COBOD International",
 "links": [
  ["Their site",
   "https://cobod.com/"],
  ["Their company page, which names the shareholders",
   "https://cobod.com/company/"],
  ["The BOD2 product page",
   "https://cobod.com/technology/3d-construction-printers/bod2/"],
 ],
 "where": "Denmark",
 "status": "live",
 "line": "Sells the printer to anyone, which is the model Titan now competes with directly.",
 "facts": [
  ["What it is", "A printer manufacturer rather than a builder, backed by GE, CEMEX, Holcim and "
                 "PERI. It sells the BOD2 to contractors."],
  ["Why it matters", "Titan is a machine sale. COBOD sells machines to contractors in Texas today, "
                     "so a builder pricing a printer can price both."],
 ],
},
{
 "name": "PRINT3D Technologies",
 "links": [
  ["Their site",
   "https://www.print3dtechnologies.com/"],
  ["Their model list with starting prices",
   "https://www.print3dtechnologies.com/builds"],
  ["The two founders",
   "https://www.print3dtechnologies.com/about"],
  ["Community Impact on the build count and prices, 26 May 2026",
   "https://communityimpact.com/dallas-fort-worth/allen/real-estate/2026/05/26/allen-based-print3d-technologies-brings-3d-printing-innovation-to-homebuilding/"],
 ],
 "where": "Allen, Texas",
 "status": "live",
 "line": "Selling finished printed houses in North Texas at $103,000 and $175,000.",
 "facts": [
  ["Track record", "Seven structures on its own count, including three houses and a storage "
                   "facility, sold between 2024 and 2026."],
  ["Why it matters", "The lowest published price for a printed house in Texas."],
 ],
},
{
 "name": "Apis Cor",
 "links": [
  ["Their site",
   "https://apis-cor.com/"],
  ["Their printing technology",
   "https://apis-cor.com/technologies"],
  ["The D.R. Horton investment release, 11 March 2024",
   "https://www.prnewswire.com/news-releases/apis-cor-a-manufacturer-of-construction-3d-printing-robots-announces-strategic-investment-by-dr-horton-302084850.html"],
 ],
 "where": "Melbourne, Florida",
 "status": "live",
 "line": "D.R. Horton put strategic money into it in March 2024. Horton builds in Greater Houston.",
 "facts": [
  ["Backing", "Strategic investment from D.R. Horton, announced March 2024, amount undisclosed."],
  ["Texas", "Its one Texas connection is the Sunconomy eco-village in Montgomery, announced since "
            "about 2019 with nothing completed."],
 ],
},
{
 "name": "Sunconomy",
 "links": [
  ["3D Printing Industry on the Lago Vista permit, 8 January 2019",
   "https://3dprintingindustry.com/news/sunconomy-to-develop-3d-printed-concrete-homes-in-texas-146575/"],
 ],
 # Build 58 moved this out of Montgomery. The 110-home eco village and the
 # Montgomery location came off the firm's own page, which now answers 403 to a
 # browser as well as to a script, so neither can be checked or linked. What is
 # left is the one page that still resolves.
 "where": "Texas",
 "status": "stalled",
 "line": "Signed with Apis Cor in 2016, permitted one house in 2019, and published nothing since.",
 "facts": [
  ["The record", "3D Printing Industry reported in January 2019 that Sunconomy had permits for its "
                 "first printed house, in Lago Vista, and that it had signed with Apis Cor in 2016. "
                 "No completion has been published in the seven years since."],
  ["Its own site", "sunconomy.com answers a browser with 403 Forbidden, so nothing the firm "
                   "publishes about itself can be read or cited here."],
  ["Why it matters", "It is the precedent a cautious builder will raise: a printed programme "
                     "announced in Texas with an Apis Cor machine that produced no published "
                     "building."],
 ],
},
{
 "name": "Alquist 3D",
 "links": [
  ["Their site",
   "https://www.alquist3d.com/"],
  ["Construction Dive on the Walmart work and the leasing model, 2 December 2025",
   "https://www.constructiondive.com/news/walmart-3d-print-alquist-retailers/806851/"],
  ["The A1 and A1X launch and a fourteen-robot sale, 15 April 2026",
   "https://www.prnewswire.com/news-releases/alquist-sells-14-3d-construction-printing-robots-launches-a1-series-to-enable-national-scale-deployment-302742621.html"],
  ["The 2026 retail rollout, 24 November 2025",
   "https://www.prnewswire.com/news-releases/alquist-to-scale-3d-print-construction-technology-via-walmart-and-other-commercial-retail-projects-in-2026-302623710.html"],
 ],
 # Build 58 dropped Iowa and Virginia. Neither word is on either source the card
 # cites, and no other reachable page carried them.
 "where": "Greeley, Colorado",
 "status": "live",
 "line": "Pivoted to selling printers and doing commercial work for Walmart. No Texas project found.",
 "facts": [
  ["What changed", "Moved from printing houses to selling its A1 and A1X machines. The A1X is "
                   "leased to contractors through an equipment rental partner rather than sold "
                   "outright, and the printing is done for retail clients."],
  ["Texas", "No Texas project found. Construction Dive names Colorado, Tennessee and Missouri."],
 ],
},
{
 "name": "Mighty Buildings",
 "links": [
  ["Their site, now carrying a LUMUS byline",
   "https://www.mightybuildings.com/about-us"],
  ["3D Printing Industry on the sale process, 21 January 2025",
   "https://3dprintingindustry.com/news/mighty-buildings-up-for-sale-following-headcount-reduction-235813/"],
  ["3DPrint.com on the same sale process",
   "https://3dprint.com/315768/house-3d-printing-company-mighty-buildings-up-for-sale/"],
 ],
 "where": "Oakland, California",
 "status": "sold",
 "line": "Put itself up for sale in January 2025 after raising more than $150 million.",
 "facts": [
  ["What happened", "Headcount cut, then the whole company offered for sale in January 2025, having "
                    "raised over $150 million from well-known investors. Since acquired and "
                    "rebranded under LUMUS."],
 ],
},
{
 "name": "Diamond Age",
 "links": [
  ["HousingWire on the shutdown, 12 December 2024",
   "https://www.housingwire.com/articles/diamond-age-shuts-down-after-hard-battle-for-new-investment/"],
  ["3D Printing Industry on the asset auction, 17 January 2025",
   "https://3dprintingindustry.com/news/diamond-age-to-sell-assets-in-new-online-auction-235736/"],
 ],
 "where": "Phoenix, Arizona",
 # Build 58 corrected the denominator. The card said fifteen of forty-three
 # contracted homes. Forty-three is on neither source. HousingWire gives thirty
 # printed between 2022 and early 2024 and fifteen still being built at the end.
 "status": "closed",
 "line": "Shut down on 12 December 2024 with fifteen houses still being built.",
 "facts": [
  ["What happened", "HousingWire reports the founders confirmed the shutdown on 12 December 2024. "
                    "The company had printed thirty homes at Mountain View Estates between 2022 "
                    "and early 2024, and was still building the final fifteen when it stopped."],
  ["Why it matters", "A printer supplier that fails mid-community leaves the builder holding the "
                     "site. Fifteen houses were open when this one stopped."],
 ],
},
{
 "name": "Black Buffalo 3D",
 "links": [
  ["3D Printing Industry on the Chapter 11 filing",
   "https://3dprintingindustry.com/news/3d-construction-printer-maker-black-buffalo-3d-files-for-bankruptcy-247981/"],
  ["3DPrint.com on the same filing",
   "https://3dprint.com/323054/black-buffalo-3d-files-for-chapter-11-bankruptcy/"],
  ["VoxelMatters on the Fort Worth live print, 24 May 2024",
   "https://www.voxelmatters.com/black-buffalo-3d-live-print-home-texas/"],
  ["CandysDirt on the Fort Worth address and Boxer's lot, 28 May 2024",
   "https://candysdirt.com/2024/05/28/you-can-see-a-3d-printed-home-get-built-in-fort-worth-right-now/"],
 ],
 "where": "New Jersey",
 "status": "bankrupt",
 "line": "Filed Chapter 11 on 24 December 2025.",
 "facts": [
  ["What happened", "Chapter 11 on 24 December 2025. Its Texas presence was one house in Fort "
                    "Worth, printed live over two days in May 2024 with Boxer Property of Houston "
                    "as the development partner. No coverage after June 2024 confirms it was "
                    "completed."],
 ],
},
{
 "name": "SQ4D",
 "links": [
  ["Their site",
   "https://www.sq4d.com/"],
  ["Their own project index, which lists four",
   "https://www.sq4d.com/projects/"],
  ["Their page on the largest permitted printed home",
   "https://www.sq4d.com/largest-3d-printed-home/"],
  ["3D Printing Industry on the 1,900 square foot build",
   "https://3dprintingindustry.com/news/sq4d-3d-prints-1900-sq-ft-home-in-48-hours-167141/"],
 ],
 "where": "Long Island, New York",
 "status": "live",
 "line": "Four units in about six years, none in Texas.",
 "facts": [["Track record", "Four units built since 2017, all on Long Island. Specifications and "
                            "pricing are not published."]],
},
{
 "name": "CyBe Construction",
 "links": [
  ["Their site",
   "https://cybe.eu/"],
  ["Their own case page for the Florida house",
   "https://cybe.eu/cases/3d-printed-houses-florida/"],
  ["3DPrinting.com on the Florida villa, 23 March 2023",
   "https://3dprinting.com/news/cybe-to-3d-print-floridas-first-villa/"],
 ],
 "where": "Netherlands and Florida",
 "status": "live",
 "line": "One confirmed American house, in Florida.",
 "facts": [["Track record", "One named United States home, in Florida. No Texas project and no "
                            "published funding."]],
},
]

# The line that writes itself from the status field, used in the section header.
CONSOLIDATION = (
 "Three of the twelve are gone or going: Diamond Age closed in December 2024 with fifteen houses "
 "unfinished, Black Buffalo filed Chapter 11 in December 2025, and Mighty Buildings put itself up "
 "for sale in January 2025 after raising more than $150 million."
)
