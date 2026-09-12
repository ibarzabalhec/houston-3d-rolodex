# -*- coding: utf-8 -*-
"""Press and public record, firm by firm.

What a call opens with. Every item here is a headline that was actually
returned by a search and whose link was read off the result rather than
assembled, with the outlet and, where the result carried one, the date. The
headline is the publisher's, not ours. Nothing here is summarised or
characterised: if the value of an item is not obvious from its own headline,
it does not belong in this file.

Only firms where something was actually found appear. A firm with no entry has
not been searched or returned nothing, and the page says which.
"""

# target_id -> [(date, outlet, headline, url)]
# date is the date the search result carried, or "" where it carried none.
PRESS = {

"HOU-002": [
  ("2026-02", "The Architect's Newspaper",
   "Zuri Gardens, a 3D-printed Texas community, shows promise for attainable housing",
   "https://www.archpaper.com/2026/02/zuri-gardens-3d-printed-texas-community/"),
  ("2025-12-03", "Houstonia Magazine",
   "Houston's First 3D Printed Home Community, Zuri Gardens",
   "https://www.houstoniamag.com/home-and-real-estate/2025/12/3d-printed-houses-neighborhood-houston"),
  ("2025-08-13", "CultureMap Houston",
   "Houston debuts 3D-printed affordable homes at Zuri Gardens",
   "https://houston.culturemap.com/news/real-estate/innovative-3d-printed-affordable-housing-development-rises-in-houston/"),
  ("", "City of Houston",
   "New Homes for South Houston, Garver Heights and Zuri Gardens",
   "https://houstontx.gov/housing/homes/sh-garver-zuri.html"),
],

"HOU-016": [
  ("2026-04-08", "Houston Agent Magazine",
   "HiveASMBLD launches 3D-printed Gulf Shore Estates in San Leon",
   "https://houstonagentmagazine.com/2026/04/08/hiveasmbld-3d-printed-gulf-shore-estates-san-leon/"),
  ("2026-04-10", "The Galveston County Daily News",
   "Printing the future: San Leon project tests new model for coastal housing",
   "https://www.galvnews.com/news/printing-the-future-san-leon-project-tests-new-model-for-coastal-housing/article_e6c622f8-f6cd-47f6-ad36-ed1cac45a3d4.html"),
  ("2026-04-22", "ABC13 Houston",
   "San Leon development aims for sustainability from the ground up",
   "https://abc13.com/post/san-leon-development-aims-sustainability-ground/18943368/"),
  ("2026-04-03", "Houston Business Journal",
   "Houston-based company to build 3D-printed home community in San Leon",
   "https://www.bizjournals.com/houston/news/2026/04/03/hiveasmbld-3d-printed-homes-community-san-leon.html"),
  ("2026-04-30", "Intelligent Build.tech",
   "Partnership to develop an innovative 3D-printed residential community",
   "https://www.intelligentbuild.tech/2026/04/30/partnership-to-develop-an-innovative-3d-printed-residential-community/"),
  ("", "Realty News Report",
   "3D Printed Homes Coming to Galveston County Coast",
   "https://realtynewsreport.com/3d-printed-homes-coming-to-galveston-county-coast/"),
],

"HOU-017": [
  ("", "Houston Chronicle",
   "3D-printed duplex under construction in Houston's East End",
   "https://www.houstonchronicle.com/business/article/3d-print-affordable-houston-east-end-22153531.php"),
  ("2026-04-22", "Homes.com",
   "Houston's 3D-printed housing push grows with two new developments",
   "https://www.homes.com/news/houstons-3d-printed-housing-push-grows-with-two-new-developments/647676272/"),
],

"HOU-001": [
  ("2026-04-25", "Houston Chronicle",
   "Why Houston's booming build-to-rent sector could slow",
   "https://www.houstonchronicle.com/business/article/houston-build-to-rent-housing-21293194.php"),
  ("2025-03-14", "Houston Business Journal",
   "Wan Bridge readjusts build-to-rent development goal",
   "https://www.bizjournals.com/houston/news/2025/03/14/wan-bridge-adjusts-build-to-rent-goal.html"),
  ("2025-11-24", "Realty News Report",
   "Build-To-Rent Boom: Dellrose, Yardly and More",
   "https://realtynewsreport.com/build-to-rent-boom-dellrose-yardly-and-more/"),
  ("", "Wan Bridge",
   "In The News, the firm's own index, which carries a March 2026 launch at Frontera Shores",
   "https://wanbridge.com/in-the-news/"),
],

"HOU-065": [
  ("2026-07-24", "Builder Magazine",
   "How Stylecraft Is Building Bigger While Staying Local",
   "https://www.builderonline.com/builder-100/leadership/how-stylecraft-is-building-bigger-while-staying-local/"),
  ("2026-06-11", "HousingWire",
   "Stylecraft Builders' micro approach to margin, pace and growth",
   "https://www.housingwire.com/articles/stylecraft-builders-margin-pace-and-growth/"),
],

"HOU-007": [
  ("2026-08-10", "CEOWORLD magazine",
   "Danny Signorelli Leads First America Homes Expansion Across Houston and Texas",
   "https://ceoworld.biz/2026/08/10/danny-signorelli-leads-first-america-homes-expansion-across-houston-and-texas/"),
  ("", "The Signorelli Company",
   "First America Homes, on the parent's own site",
   "https://www.signorellicompany.com/first-america-homes"),
],

"HOU-045": [
  ("", "Builder Magazine",
   "Chesmar Homes, with the note that Sekisui House U.S. is the 2026 Builder of the Year",
   "https://www.builderonline.com/organization/chesmar-homes/"),
  ("", "Baytown-West Chambers County Economic Development Foundation",
   "Japanese Homebuilder Builds U.S. Momentum With Acquisition of Houston Company",
   "https://baytownedf.org/news/article/japanese-homebuilder-builds-u.s-momentum-with-acquisition-of-houston-company"),
],

"HOU-115": [
  ("2026-07-21", "Construction Owners",
   "Arch-Con Tops Out 330-Unit Artis Montrose Apartment Project",
   "https://www.constructionowners.com/news/arch-con-reaches-topping-out-milestone-on-330-unit-artis-montrose-apartment-project"),
  ("", "Arch-Con Corporation",
   "Artis Montrose tops out nine months after breaking ground",
   "https://www.arch-con.com/artis-montrose-tops-out/"),
  ("", "Arch-Con Corporation",
   "Arch-Con Advances First Phase of The Hangar Multifamily",
   "https://www.arch-con.com/millie-at-the-hangar/"),
  ("", "Arch-Con Corporation",
   "Silo Springs breaks ground in West Houston",
   "https://www.arch-con.com/silo-springs/"),
],

"HOU-102": [
  ("2026", "Engineering News-Record",
   "ENR 2026 Top 400 Contractors, where the firm is ranked 72",
   "https://www.enr.com/toplists/2026-Top-400-Contractors-1"),
  ("2023-08-08", "Engineering News-Record",
   "Harvey, Harvey-Cleary, a Little Bit of Everything Firm",
   "https://www.enr.com/articles/56905-harvey-l-harvey-cleary-a-little-bit-of-everything-firm"),
],

"HOU-129": [
  ("2023-02-07", "Bisnow Houston",
   "Next Stop, Apartments: 2-Story 3D-Printed House Lays Foundation For Bigger Projects Ahead",
   "https://www.bisnow.com/news/houston/construction-development/next-stop-apartments-3d-printed-house-lays-foundation-for-bigger-projects-ahead-117549"),
  ("2023-02-24", "Built Offsite",
   "Largest 3D printed hybrid home takes shape",
   "https://builtoffsite.com.au/news/largest-3d-printed-hybrid-home-takes-shape/"),
  ("2025-03", "Construction In Focus",
   "CIVE, Construction and Design at their Finest",
   "https://constructioninfocus.com/2025/03/cive-construction-and-design-at-their-finest/"),
],

"HOU-128": [
  ("2013-10-30", "Boxer Property",
   "Boxer Announces Executive Leadership Changes, which is where the current titles come from "
   "and which puts engineering and construction under the president",
   "https://www.boxerproperty.com/blog/roles-responsibilities-evolve-executives/"),
],

}
