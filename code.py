# -*- coding: utf-8 -*-
"""Code, permitting and precedent for printed walls in Greater Houston.

Every line carries the document it comes from. Where a document could not be
retrieved in full, the line says what was read (a summary page, a press
account) rather than the primary text.

Retrieved 11 September 2026.
"""

CODE_LINE = "Houston has no zoning. A printed wall is a building-code question."

# Question, answer, source url, source label. One line each.
CODE = [
 ["Does zoning apply?",
  "No. Houston has no zoning. Chapter 42 governs subdivision, setbacks and parking. A masterplan's "
  "deed restrictions are where an exterior material can be refused.",
  "https://www.houstontx.gov/planning/DevelopRegs/", "City of Houston Planning, Development Regulations"],
 ["What code, inside the city?",
  "2021 IRC, in force 1 January 2024. Appendix AW (3D-printed construction) is not adopted, so a printed "
  "wall enters under R104.11, alternative materials and methods, on an ICC-ES report to AC509.",
  "https://www.houstonpermittingcenter.org/media/9056/download", "Houston Amendments to the 2021 IRC"],
 ["Does ICON hold that report?",
  "Yes. ESR-4652, reissued June 2026: bearing, non-bearing and shear walls to 12 feet, Seismic Design "
  "Categories A and B, special inspection required.",
  "https://icc-es.org/wp-content/uploads/report-directory/ESR-4652.pdf", "ICC-ES ESR-4652"],
 ["What code, in the county?",
  "The IRC in force at the county seat (LGC 233.153), with third-party inspection at foundation, framing "
  "and completion (233.154). Harris County's seat is Houston.",
  "https://codes.findlaw.com/tx/local-government-code/loc-gov-t-sect-233-154.html", "Texas LGC 233.153, 233.154"],
 ["Can a city or county refuse it?",
  "Not if a national model code approves it within three cycles. Government Code Chapter 3000, in force "
  "1 September 2019. Exceptions: historic districts, state- or federally-funded housing.",
  "https://www.tml.org/DocumentCenter/View/2892/HB--2439-Building-Materials-QA-Sep-2021", "Texas Government Code 3000; TML Q&A"],
]

# Verbatim, from the documents themselves. Quote, who said it, source url, label.
QUOTES = [
 ["The updated I-Codes include requirements for energy storage systems to help facilitate their "
  "implementation and improved construction methods for tiny homes, 3-D printing and the use of "
  "intermodal shipping containers as buildings.",
  "International Code Council, on Houston's adoption of the 2021 codes, 25 October 2023",
  "https://www.iccsafe.org/about/periodicals-and-newsroom/houstons-city-council-approves-adoption-of-the-2021-international-codes/",
  "ICC newsroom"],
 ["The walls are intended for use as bearing walls, non-load bearing walls and shear walls with wall "
  "heights up to 12 feet (3.7 m) tall in Seismic Design Categories A or B.",
  "ICC-ES ESR-4652, ICON 3D-Printed Concrete Wall Systems, Section 2.0, Uses; reissued June 2026",
  "https://icc-es.org/wp-content/uploads/report-directory/ESR-4652.pdf",
  "ICC-ES ESR-4652"],
 ["Section R104.11 of the 2021 International Residential Code (IRC) allows for alternative materials "
  "and methods, such as 3D-printed structures.",
  "STRUCTURE magazine, From Nozzle to Neighborhood, on the Wolf Ranch engineering",
  "https://www.structuremag.org/article/from-nozzle-to-neighborhood/",
  "STRUCTURE magazine"],
]

# Project, where, what was permitted, source url, source label.
PRECEDENT = [
 ["Zuri Gardens", "City of Houston, near Hobby Airport",
  "80 printed homes. $1.8 million in TIRZ bond proceeds approved by council; HCDD infrastructure reimbursement. Sales from summer 2026.",
  "https://houston.innovationmap.com/zuri-gardens-houston-2674387821.html", "InnovationMap; Houstonia"],
 ["Avenue J", "City of Houston, East End",
  "One printed duplex, Elpis 3D Home Builders, printed by HiveASMBLD.",
  "https://www.houstonchronicle.com/business/article/3d-print-affordable-houston-east-end-22153531.php", "Houston Chronicle"],
 ["Gulf Shore Estates", "Unincorporated Galveston County, San Leon",
  "23 of 26 homes printed, Commander Home Builders, printed by HiveASMBLD.",
  "https://www.houstonchronicle.com/business/article/houston-real-estate-3d-printed-home-hiveasmbld-20824540.php", "Houston Chronicle"],
]

# The machine-fit bands, and what they rest on. Stated once, here, and shown
# wherever the bands are drawn.
BANDS_METHOD = (
 "The bands are an assumption, not a published figure. What is published: at Wolf Ranch one "
 "Vulcan printer and one crew took about three weeks to print a home's walls by August 2024, which is "
 "on the order of seventeen wall systems a year per printer (Engadget, 8 August 2024). ICON has "
 "published no throughput for Titan: a $20 per square foot wall target, a $5,000 deposit, training in "
 "the third quarter of 2026 and deliveries from early 2027 (ICON newsroom, 11 March 2026), and a "
 "market-opening threshold of six to ten printers in one market (Builder). The bands assume Titan runs "
 "materially faster than Vulcan did at Wolf Ranch and will be redrawn when ICON publishes a rate."
)
BANDS_SOURCES = [
 ("https://www.engadget.com/home/a-robotics-company-has-3d-printed-nearly-a-hundred-homes-in-texas-225830931.html", "Engadget, 8 August 2024"),
 ("https://www.iconbuild.com/newsroom/icon-announces-first-commercial-rollout-of-its-3d-printing-construction-technology-for-builders", "ICON newsroom, 11 March 2026"),
 ("https://www.builderonline.com/design/technology/icons-next-phase-building-a-scalable-platform-for-3d-printed-housing/", "Builder"),
]

# How each number on the page is produced. Shown on the Market view.
METHOD = [
 ["Counts on the page",
  "Every count (firms screened, in on all three, named decision-maker, and the stat strips) is a count of "
  "the records behind the page, taken when the page is generated. None is estimated or rounded."],
 ["Yes, Partly, No",
  "Each verdict is written per firm with its reason, from the sources on the firm's page. A Partly "
  "records partial evidence; a No records an absent record, not a finding against the firm. Yes and Partly both keep a firm in. Only a No takes it out."],
 ["Annual closings",
  "Only published figures are drawn: Builder 100 firm pages, HousingWire, or the firm's own site, each "
  "named in the tooltip and the table. A range is the firm's own range. Where a figure is dated, the "
  "year is shown. Forty-eight firms publish none and are not drawn."],
 ["Machine-fit bands", BANDS_METHOD],
 ["Printed units",
  "Units per project as reported by the developer or the printer, with the outlet named. A project "
  "announced and unbuilt is drawn at zero."],
 ["Contacts",
  "A LinkedIn URL is held only where a retrieved page shows the person's name and the firm together; "
  "the sentence under the name says which page. Aggregators were not used. A URL was never constructed."],
]
