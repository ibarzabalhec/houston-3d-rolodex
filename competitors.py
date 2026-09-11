# -*- coding: utf-8 -*-
"""The competitive field in printed construction, and ICON's own record.

Two things a Houston buyer will ask that this section has to answer. Who else
can print my walls, and why has ICON not built here yet.

The honest answer to the second is that it has not. Every ICON project on the
public record is in Austin or Georgetown. HiveASMBLD, PERI and Sunconomy all
have named Houston-area activity. That absence is the point the screen
is built to address.
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
   "newsroom, the site and general search all return nothing. HiveASMBLD, PERI and "
   "Sunconomy each have named Houston-area activity."],
 ],
}

# The field. Ordered by how much they matter to a Houston conversation.
COMPETITORS = [
{
 "name": "HiveASMBLD",
 "where": "Houston",
 "status": "live",
 "line": "The only printer with repeat production work inside Greater Houston.",
 "facts": [
  ["Formed", "January 2024, merging Hive3D, founded by Timothy Lankau in 2022, and ASMBLD Modular, "
             "founded by Ethan Wong. Co-chief executives, Houston. PitchBook lists 2023, which conflicts."],
  ["Material", "Green Cement of Jewett, Texas, with David McNitt as Director of Technology. Green "
               "Cement is a subsidiary of Eco Material Technologies, bought by CRH plc for $2.1 "
               "billion in July 2025. The material supply sits behind a major building-products group."],
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
 "where": "Montgomery, Texas",
 "status": "stalled",
 "line": "Inside the Houston footprint, and seven years without a building.",
 "facts": [
  ["The project", "A 110-home eco-village in Montgomery County, announced with Apis Cor and still "
                  "unbuilt after more than seven years."],
  ["Why it matters", "It is the local precedent a cautious builder will raise: a printed community "
                     "announced in this metro that never got built."],
 ],
},
{
 "name": "Alquist 3D",
 "where": "Colorado and Iowa",
 "status": "live",
 "line": "Pivoted to selling printers and doing commercial work for Walmart. No Texas project found.",
 "facts": [
  ["What changed", "Moved from printing houses to selling its A1 and A1X machines, plus a Walmart "
                   "commercial rollout."],
  ["Texas", "No Texas project found. Its work is in Colorado, Virginia, Tennessee, Alabama and, "
            "from 2026, Missouri."],
 ],
},
{
 "name": "Mighty Buildings",
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
 "where": "Phoenix, Arizona",
 "status": "closed",
 "line": "Shut down on 12 December 2024, leaving 15 of 43 contracted homes unfinished.",
 "facts": [
  ["What happened", "Closed entirely, with fifteen of forty-three contracted houses left unfinished."],
  ["Why it matters", "A printer supplier that fails mid-community leaves the builder holding the "
                     "site. Fifteen of forty-three is the figure on record."],
 ],
},
{
 "name": "Black Buffalo 3D",
 "where": "New Jersey",
 "status": "bankrupt",
 "line": "Filed Chapter 11 on 24 December 2025.",
 "facts": [
  ["What happened", "Chapter 11 on 24 December 2025. Its Texas presence was a single live-print "
                    "demonstration house in Fort Worth."],
 ],
},
{
 "name": "SQ4D",
 "where": "Long Island, New York",
 "status": "live",
 "line": "Four units in about six years, none in Texas.",
 "facts": [["Track record", "Four units built since 2017, all on Long Island. Specifications and "
                            "pricing are not published."]],
},
{
 "name": "CyBe Construction",
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
