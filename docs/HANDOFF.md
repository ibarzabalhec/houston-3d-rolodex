# Greater Houston Rolodex — handoff

Build 62 · 2026-09-14

The tool is called **Rolodex**, not ICON. It is built in ICON's visual language and screens for the Titan, but it does not wear ICON's name. It is outward-facing: no build numbers, no research narration, no internal memos on the page.

## Where it lives

- **Hosted**: published as a claude.ai artifact (Version 20), private until shared from the page's own share menu. The artifact declares the `downloads` capability so the in-page Excel export works in the viewer. To republish from a new session, pass the artifact URL as `url`; the file to publish is `rolodex-artifact.html`, which `build.py` emits alongside the standalone file.
- **Standalone**: `ICON_Greater_Houston_Rolodex.html` (self-contained, opens from disk) and `ICON_Greater_Houston_Rolodex.xlsx` (the full workbook).
- **Source**: a git repository, ready to push. `make` builds, exports and verifies. The served copies are in `docs/` so GitHub Pages can serve them from that folder.

## The thesis

A printer is bought by a builder, not by a landowner and not by a fund. The builder that buys one or two machines repeats a small plan set inside a handful of master planned communities and closes enough houses a year to keep a machine working, without being large enough to buy through a national purchasing desk.

## The three counts

1. **Repeats** enough units in one place.
2. **Printer fit**: one or two machines would cover it. Roughly 25 to 400 homes a year concentrated in a few communities clears it; 400 to 1,500, or purchasing at a parent, or no published figure, is partial; above 1,500 or bought nationally fails.
3. **Track record**: has paid for an unproven way of building. The only thing on the page that uses orange. Eight firms of 90.

A Partly still counts as holding. Only a No does not. This rule is now stated in the legend on every view and under the counts on every firm page.

## The sections

Labels are names, not sentences. The explanatory clause each used to carry is in a note under the section header in List view and in `group_notes` in the data.

- **Already buying printed walls** (3), with a competitor
- **Strong target** (12): holds all three counts
- **One gap** (28): holds two
- **Builds the wall, not the house** (22): contractors and trades, read on a different axis
- **Custom and hybrid job** (10): retail and hospitality adjacent, adaptive reuse, design-led
- **National builder** (7): purchasing at a national desk, so the first order is a pilot
- **Land owner, not the buyer** (6): masterplan owners; each lists the builders in the file that build inside it
- **Already working with ICON** (2)

## The four views

Screen (3×3 matrix), List (table with per-row add and add-all), Cover (iPod cover flow ported from the Americas rolodex, real geometry), Field (competitors and ICON's own record).

**One filter system across Screen, List and Cover**: five controls (Section, Repetition, Printer fit, Track record, Decider), each a menu whose option counts respect everything else applied. Applied values show as removable chips with a Reset all that is present whenever anything is on. Search composes with filters. Field disables search.

**Excel export in the page**: a real `.xlsx` written in-page (store-only ZIP, no library). "Excel (n)" in the filter bar exports the current filtered set; "Download Excel" on the call sheet exports the picks. One row per contact, fifteen columns, frozen header, autofilter. In the hosted viewer it goes through `claude.use("downloads")`; as a file it uses an anchor download.

**Call list persists** in localStorage. **Browser Back closes a firm page** instead of leaving the tool.

## The audit, and what it changed (Build 24)

Four reviewers drove the file: visual, interaction, content, accessibility. Worst findings, all fixed:

- The headline stat read "10 clear all three counts" for a number that counts holds. Relabelled, and the matrix note states it is not the same ten as the top-right cell.
- The view switcher rendered 7px wide on phones. Real breakpoint now; verified by hit-testing at 320/390/430.
- Printing from the roster gave a blank page. A print-only roster table now exists.
- Orange carried five meanings and vanished on the three firms that are both printing and method-proven. One meaning now; ink on orange (5.7:1) instead of white (3.3:1).
- Small grey text at 2.43:1 raised to 5.33:1.
- 44 open items narrated the author's own searches ("sweep returned", "score provisional"). Rewritten as facts about the firm. Findings sort above caveats.
- Cover flow: tap opened non-focused cards, caption went stale during drag, no keyboard access, arrow keys stolen from search, reduced-motion ignored. All fixed. Drag went from 18.6 to 51.8 fps.
- Focus dropped to body on every firm open and close. Managed now.
- A named decider who has left, sits at another entity, or is a probable match now reads "Confirm" in the list, not "Named", and can be filtered either way.

## The second research pass (Build 25, `research2.py`)

The builder and creative layers had names and no links. This pass added 27 LinkedIn profiles and company-page sources, and three figures changed placements:

- **Stylecraft** closes 973 homes a year (HousingWire), not "more than 300". Machine fit Yes → Partly.
- **Colina** closes 540. Yes → Partly.
- **Westin** closes 1,062 (was unsized).
- **GreenEco** has belonged to Rausch Coleman since 2020. **Imagination Homes** is a David Weekley line. Both recorded; Imagination's machine fit moved to Partly.
- **Partners in Building**: Jim Lemming moved to chairman in June 2026; Chris Lemming is president.
- **Newmark** now has a name: Jeff Dye, president since 2020.
- **Sitterle**: Chris Hightower, Division President Houston, added; India Kinslow has no verifiable page.
- **The builder layer never had a decider pass.** Nine deciders added by the same bar. Named deciders 15 → 24.

Verification: a LinkedIn URL is held only where a retrieved page shows the name and firm together, and the evidence sentence says which page. LinkedIn blocks automated retrieval, so for most that page is the search-index entry carrying LinkedIn's own title tag. Where a firm's site links the profile (Concept Neighborhood), that is recorded instead. Aggregators (ZoomInfo etc.) were not used. No URL was constructed.

## Build 26: type and rhetoric

Archivo (variable, 400 to 800) replaces the Helvetica fallback as the display and UI face; IBM Plex Mono replaces Menlo for labels. Both are embedded as latin-subset data URIs from `_fonts.css`, so the standalone file and the hosted page render identically and offline. The headline's connective line moved from #8C8C8C to #6B6B6B. The legend is one line: swatches, then the Partly rule. The stat numbers are 38px at weight 800.

A rhetoric pass removed every superlative, metaphor and instruction from the copy: "the strongest argument", "nobody else has", "shortest path", "the door", "is the point", "which is the problem", "worth a call", "precisely", "simply". The rule the copy now follows: a sentence carries a year, a figure, a proper noun or a named counterparty, states a fact about the firm, and does not tell the reader what to conclude. Screen sentences for 25 firms were rewritten in `research2.VERDICTS`, applied last. The matrix note is grammatical at any count.

## Build 27: the Market view

A fifth view, Market, with five figures drawn at build time from the same records (`market.py` holds the published figures with sources; `build.py` computes the `market` block; `_market.js` draws plain SVG, no library). Published annual closings for the 13 firms that publish one, with the machine-fit bands shaded behind the bars; method appetite by section as stacked bars, with decider and link counts in the table; land owners and the builders inside their communities as a bipartite with clickable names; printed homes in Texas by project and printer; the field 2017 to 2027 as a vertical timeline. Every figure has a table under it and a tooltip on every mark. Nothing is estimated: 48 firms publish no annual figure and are not drawn. Stat strip on the view: 61 screened, 14 hold machine fit, 6 of those with method evidence, 8 have paid for an unproven method, 22 with a confirmed decider.

## Build 28: code and precedent, method, hero

**Code and permitting** (`code.py`, shown on the Field view as two tables: five questions with one-line answers and a source each, then three precedents). HB 2127 and interpretive clauses were cut on the rule that the table shows the route without saying so. The finding that matters: Houston adopted the 2021 IRC from 1 January 2024 with Appendices A, B, C, H, K, L, M, Q, T, U and V, and **Appendix AW (3D-printed building construction) is not among them**. A printed wall therefore enters the city under IRC R104.11 (alternative materials and methods) on an ICC-ES evaluation report to AC509. ICON holds ESR-4652 (reissued June 2026; bearing, non-bearing and shear walls to 12 ft; SDC A and B; special inspection required). Outside the city, Local Government Code 233.153/154 apply the county seat's IRC with third-party inspection at foundation, framing and completion. Government Code Chapter 3000 (HB 2439, 2019) bars a governmental entity from prohibiting a product approved by a national model code within three cycles. HB 2127 (2023) excludes building codes. Precedents: Zuri Gardens (80 homes, $1.8M TIRZ bond proceeds, HCDD infrastructure reimbursement), Avenue J duplex, Gulf Shore Estates (unincorporated Galveston County).

**Sourcing rule, applied.** Every number on the page is a count of records, a published figure with its source named, or an assumption stated as one with what it rests on. The machine-fit bands are declared an assumption: the only published cadence is about three weeks per home for one Vulcan and one crew at Wolf Ranch (Engadget, Aug 2024), roughly seventeen wall systems a year per printer; ICON has published no Titan throughput. `code.METHOD` renders as "How each number is produced" at the foot of the Market view; the closings caption points to it.

**Hero.** A full-width signature strip under the masthead: the 13 published closings as dots on the machine-fit bands, two end labels, tooltips, click opens the firm, staggered rise on load (off under reduced motion), hidden below 760px where the Market view carries the full figure.

## Build 32: vocabulary, quotes, repo

The three counts were renamed so a reader at ICON needs no glossary: **Repetition** (builds the same plans, in one place), **Printer fit** (one or two printers would cover it), **Track record** (has paid for a new building method before). "Decider" became **Decision-maker**. The rule reads: *Yes and Partly both keep a firm in. Only a No takes it out.* The headline reads *sized for the Titan*. The cover cards lost their one-letter tier badge and abbreviated badges; the legend's already-buying swatch now shows the white dot the chips carry. Three verbatim quotes sit under the code tables: the ICC's own sentence on Houston's 2021 adoption naming 3-D printing, ESR-4652's scope sentence, and STRUCTURE on R104.11. Scratch files removed; README, Makefile, requirements and .gitignore added; outputs copied to `docs/`.

## Build 32: the second count is Printer fit

The count was briefly labelled *Titan fit*. It now reads **Printer fit**, for the same reason the tool is called Rolodex and not ICON: the product name stays out of the methodology. The headline is a question, *Who in Greater Houston is ready to print?*, and the kicker names a construction printer, not the product. Titan remains where it is a fact: ICON's record, the timeline, the ESR question, the bands note. ICON's own term for the method is *additive construction* (its newsroom: "commercial-scale additive manufacturing"; Project Olympus under NASA's additive construction work); the page uses plain words instead and says "printed wall".

## Build 33: the ICON-side review

Three reviewers (a recruiter on ICON's talent team, the hiring manager for the BD role, a Houston builder of thirty years) went through the page. Applied from their reports, each checked against a source first: the byline moved to the masthead and a description meta tag was added; every sentence that read as gossip or as a jab was cut or rewritten (Wan Bridge departures, the departed First America purchasing lead, "Payson shares the founder's surname", "not a man who ran a builder of 22,000 homes", Alta's "no innovation budget", Perry's "never touches how the building is built", Apis Cor's "it was not ICON", COBOD's "puts ICON in COBOD's business"); GreenEco moved to the ICON group because Lennar completed its purchase of Rausch Coleman on 10 February 2025; Friendswood and GreenEco read Partly on track record with the parent named; Camillo's people are now the four on its own about page (the former chief executive and a marketing name from an org chart were removed); Kyle Davison was removed from Westin (the citation was a December 2014 release; he is at Meritage); Coventry's screen sentence names its two division presidents and the Dream Finders purchase of MHI (13 September 2021, $150 million) is sourced; the Sueba CityCentre and BLVD Place claim was removed (the firm's own page does not make it); Smith Douglas's Devon Street purchase is dated 2023; the Housing Authority rebrand is one sourced flag; Jamestown plots the firm's own figure of about 75 a year; the phone List has a sideways-scroll cue. Nine firms now sit in Strong target.

Not applied, by Héctor's decision: no "why Houston" line (the role is in Houston), no first-person block, no thesis or ninety-day plan on the page. The reviewers' larger findings (contractors as the real buyer, the nationals, BTR operators, a firm main line per record, the payback page inputs) are written up as `docs/ROADMAP.md` for the next research session.

## Build 34: the contractor layer

The reviewers' central finding was that Greater Houston production builders do not put up their own walls, so the firm that would own and run a printer here is often the trade they hire, and there was not one on the deck. Four sweeps went out: insulated concrete form and concrete-home builders; tilt-wall, shell and structural concrete contractors and the general contractors that self-perform concrete; every printed building in Texas with the firms attached; and the trade base the screened builders actually name. Twenty-nine records came out of it and the roster went from 61 firms to 90.

A new section, **Builds the wall, not the house**, holds twenty-one concrete, shell and wall contractors and the general contractors that self-perform concrete. The three counts are read differently there and the page says so: Repetition asks whether the firm puts up the same wall again and again inside one metro, Printer fit asks whether one or two printers would cover a share of the wall it puts up in a year on the same bands, and Track record is unchanged. The decision-maker rule also changes, and the page says that too: at a builder the person is the one who can change a wall specification, at a contractor it is the one who signs for equipment, so the badge on a contractor's card reads *Signs for the machine*. Named decision-makers went from 24 to 36.

Six builders whose wall is already not wood joined the builder flow rather than the contractor section, because they build the house: Everlasting Homes on structural concrete insulated panels, Tiona Homes and Seaside Construction on insulated concrete form, Nautilus Custom Homes, Aura Dwellings on volumetric modular, and Live Lone Star on factory-built product. Two firms that have already paid for a printed building joined the proven-adopter section: Boxer Property, a Houston commercial owner that partnered on a printed house in Fort Worth, and CIVE, the Houston design-build firm that engineered the printed house in Spring Branch.

Three findings from the sweeps are recorded in `trades.py` rather than smoothed over. Houston's structural concrete trade is almost entirely commercial and industrial, so for most of these firms a printed house wall would be a new market. Houston production builders publish almost nothing about their shell trade base: of the builders screened, one publishes a partner list and it is all manufacturers and distributors. And no Greater Houston contractor surfaced anywhere as having publicly adopted construction robotics, which is a gap in the record rather than a search that failed.

The hero and market closings captions now count builders rather than all firms, since a contractor closes no homes. The verifier gained four checks on the new section: that it exists and lists its firms, that it is offered in the section filter and filters to the right count, and that at least one contractor carries a decision-maker.

## Build 35: polish on the expanded deck

A reviewer drove the 90-firm build cold at four widths and found things the expansion had broken. All of it is fixed.

**Numbers that disagreed with each other.** The closings figure was drawn against three different denominators on the same page, 69 on the hero, 78 on the market figure and a stale forty-eight in the method note. There is now one number, computed once in `build.py` as the builders on the deck, read by both figures and stated in the method: 13 of 68. Partners in Building carried 250 homes a year in its synopsis and 300 everywhere else; the later sourced figure, 300, is now the only one. It also sat under National builder while carrying a Yes on Printer fit, which contradicted that section's own note. It is a build-on-your-lot custom builder, so it moved to Custom and hybrid job, where its record already said it belonged.

**A rule that was not true.** "Yes and Partly both keep a firm in. Only a No takes it out" appeared five times, and twenty-five firms with a No on Printer fit were on the deck. It now reads: Yes and Partly both count as holding a count, a No does not, and the section says where the holds landed.

**Circular reasons in the contractor layer.** Fourteen of the twenty-two Printer fit reasons opened "a contractor of this size" and then named no size. Every one is rewritten to say what it rests on, and where a firm publishes no size the reason says so and the mark follows the published band rule, which makes it a Partly. That moved ICF Constructors off a Yes it had not earned. Leola Construction's own reason said 9,900 homes a year is far above what one or two printers cover while the mark read Partly; it is now a No. Baker Concrete Construction shipped with "the firm's own website was not read in this pass"; the site was read, the firm trades as Baker Construction, it carries more than 12,500 people nationally, and the mark is now a No with that as the reason.

**Two firms in the wrong section.** Boxer Property and CIVE had been filed under Already buying printed walls, which took that count from three to five. Boxer's printed house is in Fort Worth and CIVE engineered rather than paid for one, so neither has a printed wall standing in Greater Houston. Boxer now takes its section from its counts and CIVE sits with the contractors, where a firm that built the wall for somebody else belongs. The section is back to three.

**Smaller things.** The em dash appeared 54 times in the Decision-maker column, in a file whose house rule bans it; empty cells now read "none published", which is also more informative. The method claimed "No URL was constructed" while the call sheet printed 135 built LinkedIn keyword searches, so the claim is now scoped to source URLs and the searches are described for what they are. "Several firms publish nobody" is now the real count, 16 of 90, with 14 of those in the contractor section, named as the largest single gap in the file. A Better Business Bureau record was doing duty as a leadership source for Urban Living; it is gone, the LinkedIn holding stands on its own, and `BANNED_SOURCES` now refuses eleven contact-data aggregators the way it already refused wikis, so the build fails if one returns. The matrix note called the method "unproven" where the legend says "new at the time". The scope note is a builder rule and now says so, because most of the contractor trade in Houston is commercial. On a phone the cover view showed the count badges upside down in the card reflection, which read as a fault, and spent most of a screen on a legend the card face already spells out; both are gone below 640. The background survey marker read 23°N / 99°W, which is not Houston; it reads 29°N / 95°W.

## Build 36: the last sweep

A record-integrity pass before the session closed, and it found the largest silent fault in the file.

**The contractor reasons were never on the page.** The block in `build.py` that turns three sentences into the three counts on a firm card ran only for a fixed list of sections, and the contractor section was added to the page without being added to that list. All twenty-two contractor records shipped in Builds 34 and 35 with an empty reasons block: the card showed the verdict, the firm, the contacts and the evidence, and nothing at all under Three counts. The reasons existed in the data the whole time under a private key, which is why a reviewer reading the JSON could quote them and a reader on the page could not see them. Fixed, and the verifier now fails the build if any record outside the land-owner section carries anything other than three reasons.

**Contractors read the first count differently, and now the card says so.** A contractor has no plan set, so the axis title on those cards reads *Repetition: puts up the same wall, in one metro* rather than *builds the same plans, in one place*. The other two are unchanged.

**Seven blank headline figures.** Chesmar, RSK and Friendswood showed an empty column, and so did all four land owners, which reads as an oversight rather than as an absence. Each now says what the record holds: acreage and builder rosters for the land owners, the Sekisui ownership for Chesmar, 366 units for RSK. Jamestown's headline still carried the 2020 figure the chart stopped drawing in Build 33; it now matches. The verifier fails on a blank.

**Text.** Zero em dashes, zero aggregator citations, zero wiki citations, no remaining "Titan fit", no remaining instance of the old rule sentence, and the last two "unproven method" strings are gone. Trailing whitespace is now stripped at build time rather than carried into the workbook. One doubled article introduced by an earlier sweep was repaired.

## Build 37: the LinkedIn pass

Run through Héctor's own signed-in Chrome on 12 September 2026, because this session had spent its web search budget and LinkedIn refuses automated fetches. The evidence standard is unchanged: a search-result headline naming the person and the firm together. Roles that execute a specification rather than choose one were not recorded, so no project managers, estimators, superintendents, safety or accounting staff entered the file.

Twenty-five people across thirteen contractors. Firms publishing nobody fell from sixteen to three. Named decision-makers rose from 36 to 44, and LinkedIn profiles held from 77 to 101.

The ones that matter. Scott Clarke, Chief Operating Officer at Harvey-Cleary Builders, on the firm with the deepest owned trade in the section. Mark Scully, President, and Tim Manherz, Vice President, at Encore Concrete Construction, which is employee-owned and therefore decides capital internally. Trent Tellepsen, President, and Daniel Lara, Vice President, at Building Concrete Solutions. Todd Riedel, Chief Operating Officer, and Jeff Raymer, Executive Vice President, at M.L. Deer, the firm that already sells insulated concrete form and installs gantry cranes. Ryan Taylor, Owner at T&T Construction. Scott Anderson and Rodney Horn, both Vice Presidents at Keystone. David Buzzelli, Vice President at Texas A&M Concrete, which also confirms against the firm's own dated news post. And at CIVE, Hugo Domloj, Founder and Chief Executive, alongside Hikmat Zerbe, whose headline confirms the head of structural engineering that broadcast coverage quoted on the printed house in Spring Branch.

Two structural findings came out of the same pass and are recorded as open items rather than as fact. A Satterfield and Pontikes recruiter and a business development specialist for Greco Structures and Rollcon both surface on a Greco search, which suggests Greco sits inside that group and changes who signs. Two people carry T&T Construction alongside RD DevCo and E&S Construction in one headline, which suggests a related group of companies.

Three firms still publish nobody: Baker Construction, where the national leadership is not a Houston decision anyway, plus Live Lone Star and Seaside Construction, which were never part of this pass. Rino Construction returns no owner or officer under either of its names, only project managers and a controller, and that is now stated on the record.

## Build 38: the contractor records verified

The people were in after Build 37 but the records themselves were still the thinnest evidence in the file, and ten of the twenty-two had never been opened directly. This pass read the firms' own pages. One record was simply wrong, four questions closed, and several confirmed absences are now stated as confirmed rather than assumed.

**Harvey Cleary was wrong.** Its record said residential exposure was not published. The firm runs a standing residential market page naming The Cooper Apartments, a 72-unit multifamily building, alongside Camden Conte, Brava and The Watermark at Houston Heights. It also publishes $2 billion in construction volume, more than 700 employees, a 1957 founding and first place on a 2023 ENR ranking for Texas and Louisiana. Repetition moved from Partly to Yes, the headline figure is now the volume rather than a list of trades, and the founders and the two men who took ownership in 1987 are named.

**Greco sits inside Satterfield and Pontikes.** The LinkedIn signal was right and the parent's own site confirms it, naming Greco among its family of companies and describing it as a turnkey commercial concrete contractor working throughout Texas, running more than thirty years and about ten under the Greco name, with a pumping arm of two pump trucks. Trey Green is Senior Vice President of the parent's Self Perform Group and oversees Greco, so he is the person who signs. Greco lists multifamily among its markets.

**T&T is a third-generation family firm with real numbers.** Established in Pasadena in 1969 by C.A. Taylor, 65 employees on average, more than 1,000 Greater Houston projects, with Jeff and Dianna Taylor as second-generation co-owners and Ryan Taylor leading since 2001. The record's "no crew count published" is gone. The RD DevCo and E&S Construction group the LinkedIn headlines implied appears nowhere on T&T's own site and stays open.

**Rino does not self-perform concrete now.** Its tilt-wall page reads that the firm self-performed its concrete work for many years, in the past tense. Its leadership page names Steve Salverino as chief executive, Jacob Aswad as president and Justin Henderson as vice president. The two square footage figures are a stale page rather than two scopes: 48 million on the homepage, an older 38 million on a page that was not refreshed, both anchored to 1991. The one job with Multi-Family in its name is a corporate headquarters and a warehouse.

**Smaller corrections.** Trent Mitchell at Silver Spur is Owner, published, after eighteen years selling ready-mix to Houston general contractors, so the presentation caveat comes off. Andrade was founded in 2003 by Victor Andrade; the second domain carrying the name Andrade Concrete and Construction is a placeholder with no address, services or people, so whether the two are one business is unsettled and now says so. Keystone's residential division places custom home foundations, master plan communities, and additions and flatwork, and the firm states it owns its pump fleet and runs a yard in every location. Building Concrete Solutions names The Travis at 3300 Main and Gables Residential Westcreek, two apartment buildings, which most of this section cannot show.

**Confirmed absences, which are worth as much as the finds.** Texas A&M Concrete publishes nothing beyond its job range, names nobody, and shows no residential work. Botello's projects are schools, healthcare, a museum and dealerships, with no residential. Encore names six projects and not one is multifamily, despite listing elevated multifamily as a project type, and its employee ownership appears only as a badge. ICF Constructors publishes no volume figure anywhere, including on its own page about financial strength, which describes high business volume without a number.

## Build 39: the second LinkedIn pass

The scope Héctor approved was the blank firms plus the deciders who had no profile. Build 37 did the first half; this is the second. Profiles held rose from 101 to 107, and deciders with no profile fell from 24 to 18.

Found: Justin Segal, President of Boxer Property, and Andrew Segal alongside him. Michael Scheurich, Chief Executive at Arch-Con. Phil Nevlud at MAREK, whose headline reads Division President without naming the firm, held because a search of his name with MAREK returns him and nobody else and the firm's own site gives the title. And at Botello Builders, where the firm's own site calls all three brothers founders and gives no titles, LinkedIn gives two: Eleazar Botello is President and Eden Botello is Operations Manager.

One correction worth more than the profiles. Burton Construction's own about page names Brad Burton as founder and stops there. The current chief executive is Shawn McAlpin, who appears nowhere on the firm's site. The record named the wrong person as the one who signs, and now names both.

Two confirmed absences, recorded so the next session does not look again. Matt Zetlmeisl at ICF Constructors has no LinkedIn profile at all; a surname search returns ten people, none of them him and none in Texas construction, so the firm's own site is the only route to him. Trey Green returns nothing against the parent's name and exists only on Satterfield and Pontikes' own team page.

## Build 40: the press layer

An evidence pass over the key firms, run through Chrome against the open web because the session's web search budget was spent. Thirty-two dated items across eleven firms, each one a headline a search actually returned, with the outlet, the date the result carried, and a link read off the result rather than assembled. The headline is the publisher's. Nothing is summarised or characterised, and a firm with no list has either not been searched or returned nothing, which the method block says.

It renders as a section called In the press on the firm page, under the evidence and above the open items, and the most recent item is carried into the workbook as a new column.

What it turned up beyond the links. The Gulf Shore Estates project at Commander has six separate outlets on it across April 2026, including the Galveston County Daily News and ABC13, which is more coverage than any other firm on the deck. Bisnow's piece on the Spring Branch printed house is headlined "Next Stop, Apartments", which is a better opening line for a CIVE call than anything in the record. Stylecraft has two trade profiles inside two months, Builder in July 2026 and HousingWire in June. Arch-Con topped out a 330-unit apartment building in July 2026, which is the multifamily project its own record said was missing. Harvey Cleary sits at 72 on the 2026 ENR Top 400.

One thing checked and dismissed. A Boxer Property post titled "Boxer Announces Executive Leadership Changes" turned out to be dated October 2013 and is the origin of the current titles rather than a change to them. It is kept because it puts engineering and construction under the president, which is who would own a method decision there.

## Build 41: the open items came off the page

The firm cards carried a section called Open items. It was a research notebook, and half of it told a researcher what to do next rather than telling a reader anything true about a firm. This page is read by people outside the project, so the section is gone. Nothing was thrown away.

**Integrity first, because the deletion would otherwise have hidden something.** Six of the items were the only place the page disclosed that a name came from a contact-data aggregator, while the method block says flatly that aggregators were not used. Five people sat on the deck with no source at all behind them. Checked one by one: Diane Danilov is real, her LinkedIn headline reads VP of Land and Business Development at Westin Homes, and India Kinslow's reads Director of Purchasing at Sitterle Homes in San Antonio, which is where that firm's purchasing sits. Matthew Roland returns nothing at Westin, the only Patrick Mustoe on LinkedIn owns a firm in Eugene, Oregon, and Art Maya returns nothing. Those three came off the deck. Matthew Roland was a marked decision-maker, so Westin's decision-maker is now Diane Danilov, on evidence rather than on a database.

**Then the other 258 items were sorted.** Twenty-eight were instructions or notes about the research process and were deleted. Seventy-two carried a fact and moved into the record: into the firm's description, its screen line, or onto the contact they qualified. Twenty-one qualified a named contact and now sit in that person's evidence line, where a reader meets them. Nineteen were entity facts and went into the description. The rest, 110 notes across 75 firms, were statements that a field is empty, and ninety separate notes saying nothing is published say less than one sentence saying every empty field was checked. That sentence is now in the method block under Empty fields.

**The register survives.** `internal/OPEN_ITEMS.md` holds every unresolved note by firm. It sits outside `docs/`, which is the directory GitHub Pages serves, and the verifier fails the build if it ever appears there or if any firm carries an open item again.

The workbook lost its Open items column and the firm card lost the section. What a reader now sees on a card is the screen, the three counts, the firm, who to call, the evidence, the press and the sources.

## Build 42: an absence is a blank, not a sentence

The page used to tell the reader when it had nothing. A decision-maker cell read
"none published". A print roster cell read the same. Two blocks in the limits list
explained what an empty field meant and how many firms published nobody, and the
press block closed by naming the firms that had returned nothing. All of that is
gone. Where a field has no value it is now empty, and the reader draws the
obvious conclusion without being told.

What stayed are the absences that are the reason for a mark the reader can see.
"No crew count, revenue or annual volume is published. On the bands, a firm with
no published figure is a Partly" explains a Partly that is printed on the card,
so it is evidence, not narration. The "Who decides" block stayed for the same
reason: it explains the caveat chip.

The limits list went from ten blocks to eight. The `.yn.none` rule came out of the
stylesheet.

## Build 43: the subtraction pass

Build 42 took the absence language off the fields. This one takes it out of the
sentences.

Twenty-eight sentences came off the deck. Three kinds:

**The score narrating itself.** "The zero records an absent search result" and
"The zero counts an absent record" appeared on four firms. The zero is on the
card. The sentence explaining the zero is the author talking about the author.

**A sentence for an empty cell.** "No construction or purchasing lead is
published for any brand", "No vice president of construction or head of
purchasing is published", "No named executives found on any retrieved page".
The roster next to each one was already blank, so the sentence was the second
telling.

**A screen line restating a mark.** "No published method evidence", "No
wall-system statement on record", "No firm-specific method evidence found", "No
closings figure to size it against". Each of those sits under a count chip that
already reads No or Partly, and the legend states once what an unpublished
figure does to a band.

What stayed: absences that are findings about the firm. Sueba has no third party
in a method decision. Provident names no Houston site. Concept Neighborhood
credits no outside architect. Chesmar's parent has no US factory and no Texas
change on record. M.L. Deer publishes no residential project. Those carry a
proper noun or contradict something a reader would otherwise assume.

Three more came out for a different reason. "Right product and right repetition"
told the reader what to conclude. "Daiwa House owns a stake, which is worth
testing" did the same. Midway's screen ended on "the Parkway relationship is
unresolved", which was an open item that had already been resolved in the
record: Midway sold out of the joint venture in December 2024, and the screen
now says so.

Three limits blocks lost a closing clause each, all of the same kind: the Sources
block explaining that an empty field carries a stated reason (it does not any
more), the contractor block explaining that a record says so when no residential
work is published, and the press block promising nothing was characterised, which
the preceding sentence already established.

The verifier now reads every rendered cell and chip and fails the build on
"none published", "not disclosed", "n/a", "unknown", "TBD", "no data" and
"could not be found".

## Build 44: the market tab gets a market

The tab had no denominator. Everything on it was bottom-up: closings for the 13
firms that publish one, the printer bands, the section counts, the printed
projects, the timeline. It could not answer whether 90 firms is most of Houston
or a corner of it.

It now carries the Census Building Permits Survey: single-family units authorised
across the ten-county metro, 1980 to 2025, then the same figure by county and by
permit-issuing jurisdiction.

**The one rule this build is built around.** Permits are not closings. Census
counts units authorised, which is phase one of the five it defines for new
residential construction. The builder figures on the same page count houses
handed over. They are never added, divided, or drawn on one axis, and the
verifier fails the build if one figure contains both. There is deliberately no
"the deck covers X per cent of Houston" line: the numerator would be closings
from 13 firms and the denominator permits for the whole metro, and the quotient
would be meaningless in a way that is easy to quote and hard to see.

**Where it came from.** Census publishes 2019 onward only as .xls and blocks its
plain-text archive to automated reads, so the series came from HUD's SOCDS query
tool, which republishes the same survey at metro, county and jurisdiction level.
Query: CBSA 26420, Annual, series Single Family and All Permits.

**What reconciles.** 112 jurisdictions sum to the ten counties, and the ten
counties sum to the metro, exactly, in every year of overlap. Zero difference,
not rounded agreement. Both are verifier checks now.

**What cross-reads.** 2025 single family is 46,341 here and 46,343 as NAHB's
chief economist gave it at the GHBA mid-year forecast. 2024 all-units is 65,747
here and 65,747 in the Census annual highlights. 2025 all-units is 65,197 here
and 65,075 in the highlights, which is a preliminary-to-final revision. None of
these is independent of Census, because every Houston permit figure in
circulation comes from it, and the page says so rather than presenting agreement
as corroboration. Texas A&M's TRERC republishes the same survey; the Greater
Houston Partnership publishes contract awards in dollars, which is a different
quantity. Both are named on the page for the same reason.

**The archived tables disagree with the current ones**, and the page prints both.
2018 single family was 40,321 as first published and is 40,887 now. The gap is
identical in the total and the single-family row for every year from 2014 to
2018, so it sits entirely in single family. Census revises and re-bases; the
chart marks the 2023 re-basing with a dashed line.

**Four figures**, each with its own source links under it, which is what the
`figure()` helper gained a slot for:

- The metro series, 1980 to 2025, one column a year.
- A county choropleth, real TxDOT outlines, with a year slider. Shading is grey
  to ink on a square-root scale, never orange: on this page orange means only
  that a firm has paid for a new building method, and one meaning per colour is
  the rule.
- The same counties as a matrix, 2000 to 2025, with two readings. Share of metro
  shows a county gaining ground; against its own peak shows its own cycle. There
  is no absolute-units shading, because Harris would take the dark end of every
  row and nothing else would read.
- Permit-issuing jurisdictions, ranked, by year. Outlined bars are unincorporated
  county area, solid bars are cities.

**What it says.** Harris County peaked in 2002 to 2007 and has not returned.
Montgomery, Fort Bend, Liberty, Waller, San Jacinto and Austin counties are all
at or near their own peaks in the last five years. And the three largest
permit-issuing jurisdictions in the metro are not cities: unincorporated Harris,
unincorporated Montgomery and unincorporated Fort Bend, at 11,014, 9,056 and
5,673 in 2025, against 4,774 for the City of Houston.

The workbook gained a Permits sheet, kept separate from Contacts for the same
reason the figures are kept apart.

## Build 45: the map, drawn properly

The outlines were the problem. TxDOT's service simplifies each county on its own,
so at the tolerance Build 44 used, two counties' shared border came back as two
different lines up to about 600 metres apart. At the size the map draws that is
nearly two pixels, which is why every seam read as a doubled or broken line.

The outlines are now pulled at about 130 metres and snapped to three decimals,
which is under a pixel at this scale, so a shared border lands on one line. 3,536
points across 18 rings, 67KB in the payload.

What changed in the drawing:

- **One boundary layer, on top of the fills.** Counties are filled with no stroke;
  every outline is then drawn once in a single grey hairline above them. Because
  the shared edges now coincide, two counties' seam renders as one line, and the
  metro's outer edge is the same weight as every interior border.
- **Labels sit at each county's pole of inaccessibility**, not its centroid: the
  interior point farthest from any edge, found by a coarse grid pass and two
  refinements. A centroid puts "Waller" on the Harris border; this does not.
  Counties with little room get the same label one step smaller rather than
  losing their figure.
- **The ramp starts at #EDEDED**, not near-white, so the quietest county still
  reads as a filled shape against the page.
- **The key is one continuous strip** in the empty lower left, labelled at its two
  ends only, instead of six swatches with a number under each. The old one also
  ran off the right edge, because `.axt` sets `text-anchor: middle` in CSS and was
  overriding the `text-anchor="end"` attribute. There are now `.axs` and `.axe`
  classes for that.
- **Below 700px the map keeps a working size and scrolls inside its own wrapper.**
  Scaled to a phone column it was ten unreadable labels.

## Build 46: the list stops being a table on a phone

The List view had seven columns inside a 358px column. The fix in an earlier
build was to make the firm name sticky and let the rest scroll sideways, with a
hint reading "Swipe sideways for the counts". The firm column takes whatever
width the other six do not, which on a phone is about 500px, so the sticky cell
covered the whole viewport and the columns you were swiping toward stayed
underneath it. The counts were unreachable. Two smaller faults sat next to it:
the section header spanned six columns in a seven-column table, leaving a stray
cell, and its note was clipped at the scroll edge.

Below 640px each firm is now one stacked block. Name on its own line, the three
counts and the decision-maker as labelled chips in two columns, the headline
figure underneath, and the call-list button in the top right corner. No sideways
scroll anywhere, and the headline figure comes back rather than being hidden to
buy width.

The markup did not change, so the desktop table and everything reading it are
untouched. Each count cell carries a `data-l` attribute with its short column
name, which the stacked layout prints as the chip's label and the table ignores.
A labelled cell with nothing in it hides itself, so a firm with no named decider
does not print a "Decision-maker" label over an empty space.

The verifier now opens List at 320, 390 and 430 and fails the build if the table
scrolls sideways, if any count sits past the right edge, or if a label prints
with nothing under it.

## Build 47: the working comes off the market tab

The tab was carrying the evidence that the figures are right, as well as the
figures. A reader is owed the number. The checking is the build's job.

Gone:

- **"The same number, read twice."** Two tables: the metro figure against every
  other published reading of it, and the archived Census tables for 2014 to 2018
  against the same years now. The largest disagreement in the second table was
  about 600 homes in 2018, on a base of 40,000. A reader who sees that spends
  attention on a rounding difference and learns nothing about Houston.
- **The dashed "universe re-based" marker** on the metro series, which existed to
  explain that second table.
- **"How the permit figures are produced,"** all eight blocks of it. Census's own
  definitions of authorisation, units versus structures, seasonal adjustment and
  the CBSA rename are the discipline this build is held to, not reading for a
  client. What ships has already been checked against them.
- **A second copy of the source list** under the method block. Every figure
  already carries its own sources.
- **Five source links** that were provenance for the cut tables and pointed at
  nothing left on the page.
- **Two sentences of design rationale** in the map and matrix captions, explaining
  why the ramp is grey and why the matrix is not shaded in absolute units. That is
  an argument with myself, held in front of the reader.

The checks did not go anywhere. They moved into `verify.py`, where the build fails
if the metro figure drifts from the published cross-read (it prints "46341 vs NAHB
46343, gap 2" on every run), if an archived Census year moves by more than 1,200
units, or if survey method or cross-reads ever ship on the page again. The
definitions live on in `permits.py` as `_DEFS`, read by whoever touches a figure
next.

Two method blocks became one, and it holds only the deck's own rubric, which a
reader does need in order to read a mark.

Ten figures became nine. What a reader needs about the quantity now sits in two
sentences of the first caption: a permit is an authorisation and not a closing,
and Census counts townhouses as single family.

## Build 48: what the record is about

Four changes, one principle behind all of them: a record should be about the
product a printer can put up.

**Published annual closings stopped being about printers.** It was drawing the
machine-fit bands behind the bars and colouring each bar by that count, which is
the job of Track record by section, one figure below it. It now answers one
question, how big each builder is in houses closed a year, and answers it once.

**"How each number is produced" came off the tab.** Six blocks explaining the
deck's own rubric, on a page whose figures already carry their captions and their
sources. The market tab now explains nothing about itself.

**Howard Hughes was on the deck and barely on it.** The record opened with a $900
million Pershing Square investment, which tells a reader nothing about land. It now
opens with what it sells: three Greater Houston communities and 1,802 residential
acres still to sell at June 30, 2026, being 1,142 at Bridgeland, 597 at The
Woodlands Hills and 63 at The Woodlands, which sells out in 2031. 621 residential
acres sold company-wide in 2025 at an average $890,000 an acre. Bridgeland sold 812
new homes in 2025, eleventh in the country.

Its Track record count moved from No to Yes. Howard Hughes financed, branded and
opened One Bridgeland Green, Greater Houston's first mass timber office building,
dowel-laminated and cross-laminated timber with low-carbon concrete in the same
structure, topped out December 2024 and opened November 2025. The count asks
whether a firm has ever paid for a new way of building. That is the count, met. It
does not move the firm up the deck, because a land owner is placed by what it
sells and it still sells lots.

Fifteen builders now hang off the record, read from each community's own builder
page, eleven of which are already screened here. Jim Carman is retitled President,
Texas Region. Stephen Sams is added as the residential land seat, marked Confirm,
because the only dated source for the title is April 2022.

That change exposed something: **all six land owners carried marks with no reasons
under them.** Survivable while every one of them read No on the third count, since
an absence explains itself, but Howard Hughes now reads Yes there. All six have
their three reasons, and the verifier requires them.

**Six records were rewritten to lead with the right product.** Triten opened on
75,000 square feet of office and described The Mill twice; it now opens on 294
units at Aliana, with the timber frame kept because that is method evidence and the
office compressed to a clause. Midway opens on The Laura at 360 units. Signorelli
opens on 23,000 paper lots. Pagewood opens on the ten EaDo blocks. Wile leads with
ground-up retail. Cameron Management leads with the residential conversion and says
plainly that the exterior wall stays.

`focus.py` holds all of it and runs last, so it overrides whatever the layers below
produced. Its docstring carries the rule: land and lots, single-family, repeating
low-rise residential, one and two storey shell, then everything else as a clause,
and only where it says something about how the firm builds.

## Build 49: the background, the grid, and a fact printed three times

**The atmosphere has never been visible, and the reason is one line of CSS.**
`.bg` carries `background: var(--paper)`, an opaque white sheet, at `z-index:-1`.
`#atmos` is also at `z-index:-1` and comes first in the DOM. Two siblings at the
same z-index paint in document order, so the ground has been painting over the
canvas since the deck was built. Everything was running underneath it: the
marching-squares contour pass, the peak drift, the amplitude LFOs, the elevation
labels, the gleam sweep, the 29°N/95°W corner mark. A hard red rectangle painted
straight onto the canvas did not reach the screen, which is how the occlusion was
confirmed rather than guessed. `.bg` moves to `z-index:-2`.

Two things were wrong underneath it as well. The renderer was ported from the
Americas rolodex and still read that deck's tokens, `--accent-warm` and
`--text-primary`, neither of which exists here, so it fell back to a gold that is
not in this palette. It reads `--ink` now, and the index contours carry their
weight through alpha and line width rather than hue, because on this page the
accent means one thing. Alphas were also tuned for a canvas at half opacity;
index contours now land near the same grey as the page's own hairlines.

**The grid now reads in priority order.** Both axes ran outward from the bottom
left, which is the convention for a scatter but the opposite of how anyone reads a
page: the top-left cell, the first thing the eye lands on, held the single firm
that repeats nothing. Columns are reversed, so top left is now Repetition Yes ·
Printer fit Yes and holds the nine firms that clear both counts. Inside every
cell, chips are ordered by published annual closings, largest first, and a firm
that publishes a figure carries it on the chip. Westin at 1,062 now leads its
cell instead of sitting eleventh in insertion order. The sub-line says both rules.

**An evidence line that only repeats the title is gone.** Under a name reading
"Managing Partner, Projects and Finance", Concept Neighborhood printed "Linked
from conceptneighborhood.com/team, which lists him as Managing Partner, Projects
and Finance" and then "Team page: Managing Partner, Projects and Finance", under
an icon that is already that link. Three copies of one fact. `focus.restates_title`
strips a leading provenance clause and drops the line when what is left is the
title in either direction of containment, which catches the case where the record
carries an extra clause the team page does not. 208 evidence lines became 198. The
187 that stayed say something the name, title and link do not: a title four years
old, a person listed at the parent, a figure that came from someone's own post.

## Build 59: what an outside reader found, and why no gate had

Every correction here came from a review of the shipped deck rather than from a
pass over the data. That is the finding about the method: each one is a sentence
that was true when it was written and stopped being true when the data moved
underneath it, and none of the four gates was looking at sentences of that kind.

**The meta description said sixty-one firms.** The roster says ninety-six. It sat
wrong for thirty builds because it lives in the document head, where no view
renders it and nothing read it. It is the line a Slack unfurl, a LinkedIn card
and a search result quote, so the preview of the page contradicted the headline
of the page it was previewing. It is generated from the roster count now, and
`verify.py` fails the build if the number in it is not the roster count.

**The Sources block made a claim a reader could falsify in four clicks.** It said
every contact was either a LinkedIn profile whose headline names the firm or a
page on the firm's own site. Of 241 contacts, 91 are the first and 111 are the
second. The other 39 are a third thing: a name carried from a page that named
them, at a firm that publishes no staff page to link, reachable through a search.
The search icon on those cards was already telling the truth. The sentence was
the only thing on the deck that was not. It prints the three counts now, and the
verifier fails the build if they stop matching the contacts.

**The decider stat is the one a reader probes first, so it carries its own
evidence.** 62 people hold the mark across 43 firms. 37 have a LinkedIn profile,
12 have a page that names them, 13 have neither at firms with no staff page at
all. Those 13 are marked **No link** on their own row rather than leaving a
reader to infer it from an icon, and the methodology block prints the split.

**Three cards a reviewer could not open, and the flag that existed but rendered
nowhere.** `no_web_presence` has been in the data from the beginning and reached
only the Excel export, so six cards said nothing on the page about whether the
firm has a site. Worse, three carried the flag and three did not, for the same
condition, because two earlier rounds dropped a dead homepage without setting it.
The flag now renders as a tag where the website button would be, with a sentence
saying what was looked at, and the build fails if a roster card has neither a
homepage nor the flag.

- **Houston Housing Authority** was not an absence at all. The authority now
  publishes as Housing Alliance HTX on a domain that resolves, with a leadership
  page carrying both people this deck names. The old URL had not died, it moved.
  Build 55 had dropped it as dead; this restores it, and gives the chief
  executive a page instead of a search.
- **GreenEco Builders** has no site. Its published domain has no DNS record at
  all, and the similarly spelled domain is a parked lander.
- **Live Lone Star** answers 401 to a browser and to a script on both hosts. The
  website button is gone, because a button that 401s is worse than none.

**The headline broke this deck's own rule.** It asked a question and carried the
counts, which appear in the strip below it anyway. It is a statement now:
*Greater Houston builders and developers, screened for a construction printer.*
The verifier fails the build if the headline contains a question mark or a digit.

**43 and 42 were the same word for two different things.** The screen counts
firms with a decision-maker named; the market view counts the firms where nobody
on that mark carries a caveat. Both labels now say which.

**One thing in the review did not hold.** GreenEco's George Kopecky was reported
as having no link at all. He has a LinkedIn profile, and it is on the card.

## Build 62: the deck was not a contractor list, it was a tilt-up list

Twenty-two contractors, and seventeen of them scoring Partly on printer fit.
That pattern is the tell. Every one of the 22 was found through tilt-up.org
project profiles, because that is the one place in this trade where volume is
public. **The deck did not choose tilt-up. The data chose it**, and a screen that
measures firms casting 87-ton panels at 70 feet against a machine that prints a
house wall will keep returning Partly, because the question does not fit.

So the round began by drawing the thing the roster was a slice of: the wall value
chain, meaning everyone who touches a wall between a cement plant and a finished
house. Twelve cells. The deck had two.

Six sweeps went at the empty ones and returned **87 candidates**, each one a claim
about a page. `internal/gate.py` went and read the pages: 75 answered a script,
six names were not on the page cited for them, fourteen figures were not on the
firm's own homepage.

**The bar is not sales volume, and working out why is the finding of the round.**
Of 87 firms, **five publish a volume figure and twenty-four publish years in
business instead.** Builders publish closings because the Builder 100 makes them.
Nothing makes a wall contractor publish anything. So screening on volume would
have selected for having a marketing department: it would have kept the loud
small firms and cut the large quiet ones, and Houston Gunite has been shooting
concrete since 1984 and publishes no number at all.

The bar is **what a firm already owns**, because a firm that has financed heavy
equipment has shown it can finance a machine, and unlike revenue that evidence is
on the page. A plant, a fleet, a certification that required an audit, a parent
with a capital process, or an executive bench.

**Four roles, because one flat bar would have cut the best finding.** Applied
without thought, the capacity test removes all seven gunite crews, which hold the
single most relevant skill on the list. So:

- **28 could carry a machine** and are on the roster, scored, on the grid.
- **14 know the volumes.** Post-tension plants, ready-mix producers, a binder
  trader, an ICF distributor. They will never buy a printer and they hold the
  numbers this trade does not publish.
- **7 have the crew.** The gunite and shotcrete firms. Houston Gunite advertises
  on its own careers page for **nozzlemen, top finishers, bottom finishers and
  foremen**, which is the print crew roster, already trained, in a metro with one
  of the largest pool industries in the country.
- **4 are already inside this market on the other side** and belong in the Field
  section, not the roster. Eco Material Technologies supplies the near-zero-carbon
  rapid-set cement for Zuri Gardens, the printed community HiveASMBLD is
  building: someone has solved material qualification for printing in Houston and
  it is not ICON. Lone Star Ready Mix and Dynamic Concrete Pumping share a
  Hockley yard under one family, which is a vertically integrated printing
  competitor on the way up.

Thirty-one were cut outright, with the reason recorded in `internal/capacity.py`
for each: retail driveway outfits, two-page sites with no crew and no equipment,
bridge and utility precast against a bar that is wall, and a truss plant whose
City of Houston fabricator registration says trusses where its own site says wall
panels.

**The contractor section now reads in the order a wall gets made.** Places it
through a hose, pours the horizontal, casts the vertical flat on site, casts it
off site, manufactures it as a panel, lays it unit by unit, forms it and leaves
the form in, owns the job. Fifty contractors across eight links, the largest
holding nine. `verify.py` fails the build if a contractor has no place in the
chain, if the counts do not add, or **if more than half the section sits in one
link**, which is the exact shape Build 61 shipped with and nothing noticed.

**The supply panel is deliberately not on the grid.** Scoring a post-tension
plant against printer fit is a category error dressed as rigour, and a row of
empty count cells would say those firms failed rather than that they were never
asked. They sit under the contractor list with what they are and why they matter,
and the build fails if anything there is also a scored record.

**And the panel carries the third finding: twenty-one firms that publish no
website at all.** Six in the Greater Houston Builders Association's foundation
and concrete categories, eleven on the Associated Masonry Contractors of Houston
roster, four more elsewhere. They are not small by inference, they are unlisted.
It is also why the slab link is thinner than it should be, and the deck says so
rather than presenting the roster as the market.

Two records did not survive their own sources, which is the argument for running
the gate rather than trusting the sweep. **Ecocast Homes** was written up and cut:
the one page it cited now returns 404, the domain redirects to
usaprecasthomes.com, and the successor site carries neither the Humble plant nor
the model that had been quoted. **Tindall** had its expansion figure rewritten,
because the page says "69 thousand square feet" and the record said 69,000.

Three track-record scores were tightened on review. Manufacturing wall panels is
this industry's ordinary business rather than a method adoption, so UFP Site
Built went to No; advertising low-carbon pumping is not the same as having bought
it, so Brundage-Bone went to No; a published factory tolerance is a manufacturing
specification, so Texas Lite Gauge went to No.

`figures.py` gained one more fix: **"Eighty-five acres" was being read as the
figure 80**, because the word eighty matched on its own and the hyphen after it
was never looked at. Unsourced figures fell from 171 to 162.

The roster stands at **124 firms, 50 of them contractors**, with 21 more in the
supply panel and 21 named as unlisted.

`linkcheck.py` also learned to retry. Twelve threads against 662 URLs look like
an attack to a small host, and a trade association directory came back 404 in the
sweep and 200 three times in a row on its own. A second attempt after a pause now
separates a host under load from a page that is gone.

**Gates: five, and two known-transient link failures.** `make` builds and
verifies, `probe.py` reports zero names missing across 154 readable contacts,
`phonecheck.py` holds 129 numbers, `figures.py` reports 162 of 866 figures
unbound. `linkcheck.py` sweeps 662 URLs and reports five failures: four are
rebusinessonline.com, which is down site-wide including its own homepage, and one
is the AGC Houston directory throttling under the sweep while answering a single
request. Neither is a dead page and neither is in BLOCKED, because mislabelling
an outage as a refusal is how a real 404 gets ignored later.

## Build 61: show it, do not say it

Three notes from a read of the shipped page, and one principle under all three:
a page that explains what it could demonstrate is asking a reader to do work the
page should have done.

**The methodology block ran to nine entries and about nine hundred words, and
seven of the nine described something the page already shows.** What a Partly
means is printed under the counts on every firm page and in the legend on every
view. What is in the contractor section is the note on the section. What a press
item carries is the outlet and the date printed on the item itself. Text that
repeats what a card shows is text a reader has to get past to reach the cards.
It is **four entries and 264 words** now, and they are the four things a card
cannot show: how the roster was assembled, where the decision-maker bar sits,
what a contact is evidenced by, and what was deliberately left out. The one
paragraph worth keeping, how the three counts read for a contractor, moved onto
the contractor section's own note, four screens closer to the firms it governs.

**Every number in the stat strip was already a filter, and none of them said
so.** 96, 13, 43, 3, 22. A reader could set all five by hand in the bar below and
had no way to know the figures above were the same thing. They are buttons now.
Clicking one applies its filter and opens the List, because the List drops what
does not match and the Screen only dims it: 22 contractors shown as 22 rows is
the answer, 22 contractors shown as 74 grey chips is a description of the answer.
Clicking the same one again clears it, and the first, the whole roster, resets
everything. The pressed state is drawn in ink, not orange: orange means the track
record on this page and it does not get a second job.

`verify.py` clicks all five on every build and fails if a stat prints 22 and its
filter returns 21. A figure and the set it describes cannot drift apart silently.

**The one thing a reader reaches for first was the one thing that was not a
link.** The twelve competitor cards in Field got 40 links in Build 58 and the
competitor's own name sat above them as plain text. Same on every firm page: the
firm's name was text and its website was a pill four inches below. The name is
the link now, in both places, and the site is read off the link list rather than
assembled. Three competitors are shut or bankrupt and publish nothing, so those
headers stay plain, which is the same distinction the firm cards already draw
about a missing website.

Two things came out with it. The row labelled "Their site" is gone from each
competitor's link list, and the Website pill is gone from every firm header:
both printed a URL the name now carries. On a card with no site, the "No website
published" tag is also the reason the name is not a link. The build fails if a
competitor publishes a site and its name is not the link, and forty firm cards
are checked per build for the same thing.

## Build 60: the cards that named their evidence and withheld the link

Build 59 ended on a lesson rather than a fix: an outside reader found six real
defects in one pass, and the gates found none of them, because every one was a
sentence rather than a value. This round is that lesson applied. Nothing below
was corrected by hand and left corrected. Each one became a check, and each check
then found cases the review had missed.

**The front page contradicted itself.** The note under the grid read *the top
right cell holds 8 firms*. Eight firms do clear both counts. They are in the
**top left** cell, and the hero paragraph four hundred pixels above says so in
words: both axes run outward from the top left. A reader checking one sentence
against the other found the document wrong about its own diagram. The corner was
typed and the count was generated, so nothing compared them. `verify.py` now
derives both from the grid — the template walks each axis from the end of
`order`, which fixes the row and the column — and fails the build if the sentence
names a different corner or a different count. Reverse the axis order and the
sentence has to follow.

**Eighteen contacts claimed a page and linked none.** Their role strings read,
verbatim, *Founder, named on the firm's own about page* and *Listed under Senior
Leadership on the firm's own team page*, with `source_url` null on every one.
That is the card telling a reader exactly where to check and then not letting
him: the same defect the reviewer caught in the Sources block, one level down.
The role is a role again, the assertion moved into the evidence line, and the
page is one click away. The build fails if a role string names a page the card
does not carry — and the gate found **eight more** the review's list had missed,
at Harvey Cleary, Botello Builders and Nautilus Custom Homes. Twenty-six in all.

**Opening every one of those pages cost four claims.** Which is the argument for
the round, because each was asserted with confidence and none was true:

- **Blazer Building's roster is not a team page.** It is called Who We Are, and
  it publishes names under Senior Leadership with **no titles at all**. Four
  people were carried with the sentence "Listed under Senior Leadership" standing
  in for a title. Each has an individual bio page on the same site that gives a
  real one: Chris Richardson founded the firm in 1978, Chad Hillman is president
  of Blazer Building Southwest, Brian Henderson is vice president of construction,
  and Matt Fuqua is **business development** — the single most useful line on a
  card in a business-development rolodex, and it was not on it.
- **T&T Construction's about page never writes the names.** It names the founder,
  C.A. Taylor, and then uses first names: Jeff, Dianna, Ryan. Three contacts
  asserted a full name the page does not print. The evidence line now says what
  the page says, and says that it uses first names.
- **Silver Spur's owner lost a clause.** He was carried "after eighteen years
  selling ready-mix to the largest general contractors in Houston". That is on
  neither page the card cites. It is gone. What the page does carry, ExxonMobil
  World Headquarters and Baylor College of Medicine among his work, is there
  instead.
- **Aura Dwellings' chief executive was sourced to a page no one can read.** The
  Urban Land article answers 403 to every script, and the company's own site names
  nobody at all: eight pages fetched, zero occurrences of the surname. Rame Hruska
  is real, and an AGC Houston *Cornerstone* interview republished by Marek
  Brothers carries the exact title, in bytes a script can check. That is the
  citation now, and the evidence line says the company publishes no one.

**Five cards named an outlet and cited nothing.** Westin, Colina, Sitterle, First
America and CastleRock each say *Builder reports* this or *ranked Nth* that, and
not one carried a `builderonline.com` link. The figures were right. They were
assertions anyway. All five now carry the page — and one of the five was about to
be filed against the wrong one: First America's firm page on builderonline does
not say rank 75, it says rank 109, because it has not been updated. Rank 75 is on
the 2026 Builder 100 list itself. Citing the firm page would have pointed a
reader at a number that contradicts the card.

**`figures.py` was reporting sourced figures as unsourced, on notation.** Builder
prints `$621 M` where a card writes `$621 million`, and CastleRock's own page
prints `20k+` where the card writes 20,000. Every one of those read as a figure
on no page the card cites. The variant table now covers the abbreviations, and
the five Builder pages are recorded in a `BYHAND` block with the figures that
were read off them, the way `probe.py` records a page that refuses scripts. The
unsourced count fell from **205 to 160**, and 45 of those were never findings.

**Gates: five, all green.** `make` builds and verifies, `probe.py` reports zero
names missing from the page cited for them across 153 readable contacts,
`linkcheck.py` sweeps 595 URLs with none dead and no banned source,
`figures.py` reports 160 of 783 figures unbound, and `phonecheck.py` holds 129
numbers against the pages that publish them.

## Build 58: the field section gets links, and four of its claims do not survive them

The Field section named twelve competitors and carried not one link. A reader
who wanted to know who the competition is had twelve names and no way to reach
any of them. It now carries **40 links across all twelve**, each with the host
printed beside the label so a reader can see whose page it is before clicking:
the firm's own site, or somebody reporting on them.

Every link was gated the way the contact layer is: fetched, and tested for the
company's name in the page bytes. 36 passed outright. Of the twelve that did
not, two were dead and are gone (`bb3d.io/3d-printing/` 404s, and the LUMUS page
404s), one was a 301 to a homepage and is gone (`cybe.eu/cybe-florida/`), two
were redirects whose destinations are now cited instead (COBOD moved
`/about-us/ownership-structure/` to `/company/` and `/solution/bod2/` to
`/technology/3d-construction-printers/bod2/`), and the rest are hosts that
refuse scripts and render in a browser, each opened by hand before it shipped.
Two builderonline URLs were dropped rather than carried on a browser read,
because both companies already had cleaner links.

**Four claims did not survive their own sources**, which is the argument for
doing the links at all:

- **HiveASMBLD's material.** The card named a cement company in Jewett, Texas, a
  director of technology, a parent, and a $2.1 billion sale. None of those
  strings is on any page the card can cite. The Texas Tribune names Eco Material
  Technologies of Utah as the partner, and that is now all the card says.
- **Diamond Age.** The card said fifteen of forty-three contracted homes were
  left unfinished. Forty-three is on neither source. HousingWire gives thirty
  homes printed between 2022 and early 2024, and fifteen still being built when
  the founders confirmed the shutdown on 12 December 2024.
- **Alquist 3D.** Located as "Colorado and Iowa", with work in "Colorado,
  Virginia, Tennessee, Alabama and Missouri". Iowa and Virginia appear on
  neither source. It is Greeley, Colorado, and Construction Dive names Colorado,
  Tennessee and Missouri.
- **Sunconomy.** The 110-home Montgomery eco village came off the firm's own
  page, which now answers 403 to a browser as well as to a script, so it cannot
  be checked or cited. The one page that still resolves reports a permit for a
  house in Lago Vista in January 2019 and an Apis Cor agreement signed in 2016.
  The card says that, and says its own site no longer answers. The Houston
  footprint claim went with it, including from ICON's own block, which had
  listed Sunconomy alongside HiveASMBLD and PERI as named Houston activity.

A reference to a contact aggregator as the source of a disputed founding date
also came out of the HiveASMBLD block. The deck does not cite those for a name
or a title and should not cite one for a year either.

**Gates.** `linkcheck.py` now harvests competitor links, so all 581 URLs on the
deck are swept for status and for banned sources. `verify.py` fails the build if
a competitor carries no link, if a link has no label, or if a link held in the
data does not reach the page. That last one is the check that matters: the data
can carry a link and the render can still drop it, which is how the section went
twelve builds with none.

**One unrelated thing the sweep caught.** `landtejas.com` answered scripts until
Build 57 and now times them out on every attempt. Opened by hand: the site loads
and its footer still carries the number the deck holds. It is recorded as
blocked-to-scripts with the date, in both `linkcheck.BLOCKED` and
`phones.VERIFIED`.

**Still open here.** ICON's own block in the same section carries no links. It is
the only block in the Field section without them.

## Build 57: the number gets its own row

Build 56 put the phone block at the top of **Who to call**, and the heading then
lied: the first thing under it was a number, which is not a who. The named
people keep that heading. The numbers, their labels, the source link, the
directory and the stated absences move to **Phone numbers**, a row of its own
directly below, whose label is true in all three states.

The main line sits on its own line at 22px with its label and its source link on
a second line beneath it. The three ran together on one line before.

Section labels in the left column go from 10px at weight 600 to 12px at weight
700, one step up in contrast.

## Build 56: the number layer

The deck carried 106 firms, 273 named people and no phone number. It now carries
143 numbers across 89 records, a stated absence on the other 17, and a fourth
mechanical gate that tests every digit against the page it is cited to.

**Firm level, not person level.** No firm on this deck publishes a direct dial
for its purchasing officer. The only sources that do are the contact aggregators
the deck is barred from, and `build.py`'s banned-source sweep would exit on any
of them. A person's row is unchanged.

**How a main line is designated.** In order, first fit wins, and the rule used is
recorded on the record and shown on the card:

1. the page publishes exactly one number
2. a `tel:` link in the site header or footer, so on every page
3. the page labels it main, office, corporate, general or headquarters
4. the only Houston-area line among several
5. none of the above, so no main line is designated

Rule 5 is the point of the list. Three records hit it: Caldwell Homes publishes
four community sales lines, D.R. Horton publishes a division office in every
state, Taylor Morrison gives each division a Customer Care number and an Online
Sales Manager number and calls neither the main line. Those cards print the
directory and say the page designates none. The first sweep, which took the
first number on each page, would have published MAREK's residential fax, Read
King's fax, Braun's fax and Kendall's fax as main lines.

**Nothing published is discarded.** Where a page carries more than one number,
the card prints one and folds the rest into a `<details>` directory, each with
the wording the page gives it. Where a page carries more than a directory can
usefully hold, a note gives the count instead: Ashton Woods publishes a number
per selling community, fifteen of them in the Houston area, and none for the
company.

**What a blank means.** Seventeen records ship a sentence rather than an empty
field. Nine are firms whose own pages route every enquiry through a form:
Chesmar, LGI, M/I, Greystar, Dinerstein, Harvey Cleary, RSK, Colina, Newland.
Two are firms that no longer have their own site: Brightland now serves a DRB
Homes page, and Newland redirects to Brookfield. Six have no page on the card at
all.

**`phonecheck.py`**, the fourth gate, run by hand like `linkcheck.py` and
`figures.py`. It fetches every cited page and tests the digits against every
rendering a page might use. It found nothing wrong with the hand-typed entries
and two things wrong with itself. Four sites send a browser a page full of
office numbers and send a script the same page with every number missing,
because the numbers are assembled by JavaScript: drbhomes, tricoasthomes,
smithdouglas and dsldhomes. Not finding a number on one of those proves nothing,
which is the lesson `probe.py` learned about names in Build 53. The guard is
mechanical: a page with no phone-shaped string anywhere and no `tel:` link is
unreadable for this purpose and resolves against `PHONES.VERIFIED`, a dated
record of what a browser showed. Fourteen numbers stand on browser reads.

**No List column.** `ROADMAP.md` asks for one. `verify.py`'s responsive gate
fails when a list cell sits past the right edge at 320 pixels, and an eighth
column does that; its `emptyLabelled` check separately fails on a `Phone` cell
with nothing under it, which is what a firm with no published number produces.
The number is on the firm page, on the call sheet in printable text, and in both
workbooks. The List stays a triage table. Deliberate departure, recorded here.

**Files.** `phones.py` (the data, hand written), `phonecheck.py` (the gate),
`internal/harvest_phones.py` (reconnaissance, not in `make`), plus the number
layer through `build.py`, `_template.html`, `build_xlsx.py` and `linkcheck.py`.
`verify.py` gained a shape check that fails the build on a number with no source
link, a number that is not ten dialable digits, the same number on two firms, or
a fax printed as a main line.

## Build 55: the figures gate, and five cards that contradicted themselves

Asked whether I was worried some of this was invented, the right answer was to
test it rather than say so. Two tests, one weak and one not.

**The weak one.** All 98 LinkedIn URLs, checked for the shapes a fabricated slug
takes: a surname absent from its own slug, a forename absent, one URL on two
different people. Four name mismatches, all benign (`raygabriele`, `bartonk`,
`dahightower`, and a percent-encoded accent), and one duplicate that is the same
man correctly on two cards. No structural tell. That is worth little: 73 of the
98 carry a hex suffix, which is the shape that cannot be judged by looking, and
neither linkcheck nor probe can open linkedin.com at all. The contact layer's
softest 91 entries remain untested by anything.

**The one that found something.** `figures.py` is new and does for numbers what
`probe.py` does for names: take every figure a card prints, fetch every page that
card cites, and ask whether the figure is in the bytes. 779 figures across 106
cards. Restricted to cards where every cited page came back readable, 27 were
printing a figure that is on none of them.

**Five of those were self-inflicted, and they were live.** Build 53 rewrote
eleven synopses and touched nothing else on those cards:

- Perry Homes printed "120+ communities, 65,000+ homes sold" as its headline
  figure directly above a synopsis saying the about page publishes no homes-sold
  total. That page contains neither string in any form.
- LGI said 153 active selling communities in the synopsis and "more than 185" in
  an evidence item on the same card.
- Pagewood said phase one was 30,000 square feet in the synopsis, while the
  superseded evidence item sat beside its replacement still saying 513,000.
- Triten said The Mill delivered as 341 apartments and the evidence item said 340,
  at the old address, with the office component the synopsis had just said does
  not appear in the firm's own portfolio.
- Midway had The Laura at 360 units and opening. It is 359 and opened in 2024.
  That one was reported in round two and never applied.

**The gate.** `audit2.SUPERSEDED` is a register: correcting a figure means naming
the figure it replaces. `build.py` then refuses to build while the old one is
printed anywhere on that card, in the synopsis, the headline, a reason, an
evidence item or a title. It was tested by feeding it a live string and watching
it fail the build.

**A stale `.pyc` read for the source.** While testing the gate, a restored file
the same byte length as the one it replaced, written inside the same second, was
invisible to CPython's mtime-and-size check, and the build reported a figure the
source no longer held. `PYTHONDONTWRITEBYTECODE` is now set in the Makefile.
Nothing here is hot enough to need bytecode on disk, and a cached artifact
standing in for its source is the same failure as everything else in this audit.

**What is left, stated as two different things.** 25 cards still print a figure
that is on no page they cite. Eight of them name a publisher in words without
linking it: Westin, Colina and Sitterle all say "Builder reports" and cite only
the firm's homepage, so the Builder 100 firm page is the source and it is not on
the card. That is a link-the-claim job. The other 17 need a look each; several
are price bands on sites that render prices from script, which the checker cannot
read and should not be trusted to have refuted. None of the 25 is known to be
invented, and none of them should be described as verified either.

96 firms, 241 contacts, 43 with a named decider.

## Build 54: the browser round, and the probe's own false positive

Build 53 left 41 contacts on pages a script cannot read: hosts that answer 403,
sites that render their names from JavaScript, and one that serves a 182-byte bot
stub. Those were reported as unread rather than as clean. This build opened them
in a real browser.

**Twelve pages read by hand.** Nine confirmed every name on them: Burton
Construction, LGI, M/I, Camden, Century, Howard Hughes, Risewell, and the Builder
firm pages for Tilson and Long Lake. Two are unreadable even in a browser:
houstonagentmagazine sits on a Cloudflare interstitial, and NewQuest's leadership
page renders 1,373 characters of navigation and no names after ten seconds.

**The probe was over-reporting, and that is the finding of this build.** It tested
each contact against `source_url` **or the firm's `team_url`**. For a contact
whose only link is a LinkedIn headline, that fallback tested them against the
firm's investor-relations officers page, where a division purchasing lead would
never appear. Absence there says nothing. Eight real contacts were one decision
away from being deleted on that test: Chuck Collier and Kyle Hanna at LGI, Patrick
Mayhan and Randy Barras at M/I, Michael Eilertsen at Camden, Tanya Rizzo at
Century, Jim Carman at Howard Hughes, Kirk Breitenwischer at CastleRock.

The probe now tests only the page cited for that person. Contacts whose sole
source is a LinkedIn headline are reported in their own list, 90 of them, because
there is no firm page to check them against and saying so is the honest answer.
That is the deck's own rule from the roadmap: a LinkedIn profile is held where the
page or the search-index title shows the person and the firm together, otherwise
the firm's own page.

`probe.py` also gained a `VERIFIED` table: a page a script cannot read, opened in
a browser, with the date and what was on it. Those stop being reported as unknown
and start being reported as read. It is the same pattern as `linkcheck.py`'s
BLOCKED list, and it exists so that the next person can tell a stale note from a
fresh one.

**Two findings survived the browser.** Joshua Cantu carried no link of any kind on
the Burton Construction card and is not among the eight people its leadership page
names. Greg Grahmann's card gave him a David Weekley division presidency; the
cited Builder article, read in a browser, quotes him only as "director at
Imagination Homes," and the division-president words that a text search found on
that page came from a sidebar link to an unrelated story about KB Home.

96 firms, 241 contacts, 43 with a named decider. 152 contacts stand on a firm page
that names them and 0 are missing from it. 90 stand on a LinkedIn headline. 14
sit on pages nothing can read.

## Build 53: recursive evaluation, and what the second pass cost the first

Build 52 audited thirty cards and called it an audit. It was a sample. This build
ran the loop properly: audit, gate every finding against raw bytes, apply, then
audit the corrections and the seventy-six cards the first round never opened.

Round two found more than round one did, on cards round one had not looked at.
That is a fact about the method, not about the deck.

**Three of round two's findings are corrections of round one.**

The name probe reported Cullen Burton missing from Burton Construction's
leadership page. He is on it. The site answers a script with a 182-byte bot stub
and a browser with the full roster, so the probe read an empty page and called a
real person absent. `probe.py` now treats a body under two kilobytes, or a page
that renders fewer than 400 words with no hit, as unreadable rather than as
evidence. That second guard cleared two more false positives, at DSLD and Smith
Douglas, whose pages ship 40,000 and 53,000 words of script-rendered chrome.

Round one published Derrick Hughes as Wan Bridge's construction vice president on
the strength of a fetch that returned his bio. The URL is a 404. He never
shipped, because the link checker ran before the build did.

Round one's reason-versus-mark check caught eight contradictions and missed two,
HTX Concrete and T&T Construction, because both phrase the deck's own band rule
in words the pattern did not match. The pattern is wider now and also fails a
machine-fit Yes written over an absent figure. It then caught a contradiction I
introduced in this build, on Kendall Homes.

**The gate.** No finding in this build was applied on an agent's word. Each one
was adjudicated by fetching the page and testing whether the figure or the name
is in the bytes. Thirty-one claims were tested that way. Nineteen were confirmed
and applied, and the rest were either refuted or could not be read and were left
alone. Two examples of each: Coventry Homes is not on Sienna's builder list and
Sienna is not on Coventry's community list, so "active builder in Sienna" is
gone; Pagewood's own release puts phase one at two warehouses of 15,000 square
feet each, against the 513,000 the card published, which is the whole ten-block
district. Against that, the Camillo post does not name Matt Hansen and the
Tricoast pages render from script, so neither claim was acted on.

**`probe.py` is new and it is the part that scales.** For every contact with a
readable source, it fetches the bytes and asks whether the name is in them. No
model reads the page. On first run it flagged fifteen contacts whose name is not
in the page cited for them, eight of them people published as the person who can
change a wall specification. After the corrections it flags none. Forty-one
contacts sit on pages that refuse scripts or render from JavaScript, and those
are reported as unread rather than as clean.

**What the contact layer lost.** DeKendrick Vidito at Ashton Woods, Shane Huhn
and Lauren Chachere at Perry, Chad Durham at David Weekley, Glenn Briggs and
Jason Madden at Kendall, Bruce Torkelson at CastleRock, India Kinslow at
Sitterle, Jayar Griffith, Jeremy Flach and Kyle Davison at Meritage, Brian
Grigsby at Coventry, Mike Faul and Troy Robinson at First America, Stephen Ray at
Smith Douglas. Fifteen names, none of them on a page their own firm publishes.
Where the firm publishes someone in that function, that person replaced them:
Adam Weaver and Ken Newman at Ashton Woods, Jo Dunham and Katie Pritchard at
Sandcastle, Martin Jordana at Baker Construction, David Wickens at Kendall.

**Records that changed shape.** Urban Living's only source was its own domain,
which is now a parked lander, so the record holds nothing and moved off the
roster. Cameron Management lost the Esperson towers to a MetLife foreclosure in
August 2024 and is the manager, not the owner. Triten's cross-laminated timber
was an expectation in a 2021 article, contingent on retail leasing, and does not
appear in the firm's own portfolio entry, so Track record moved to Partly and the
card now leads on the 294 units under construction at Aliana. Leola Construction
self-performs slab masonry, framing and drywall, which is the opposite of the
"no direct field crew" the card had used to score it. Baker Construction
publishes fourteen executives on a page the card said named none. CIVE's founder
is Hachem Domloj, not Hugo. Perry Homes builds in Florida. LGI has 153 active
communities, not 185, in 21 states, not a dozen.

**Four gates now run over the deck**, and all four are clean:

    make                 build, workbook, and about sixty checks including
                         reason versus mark
    python3 probe.py     every contact's name against the bytes of its source
    python3 linkcheck.py every URL's status, and the source rules

0 dead links. 0 rule breaks. 0 contacts missing from their cited page. 0 reasons
arguing against their own mark.

96 firms, 242 contacts, 43 with a named decider, 3 with no contact published.

## Build 52: the audit round

Six independent passes were run against the cards, one batch each, with
instructions to assume the write-up was wrong until a source the agent opened
itself said otherwise. Every URL the deck publishes was checked for status and
swept against the source rules.

The rules held. 533 URLs, no encyclopedia, no contact aggregator, no constructed
link. The content did not hold.

**Two people published as the person who can change a wall specification could
not be called.** Marilyn Vanderhider, carried on Avenue CDC as Director of Single
Family Housing with a link to her LinkedIn, died on 22 November 2015. Brad
Burton, carried on Burton Construction as founder, is not on the firm's own
leadership page, which names Shawn McAlpin as chief executive and Cullen Burton
as president. Both are off the deck.

**Seven more named contacts were not on the pages they were sourced to.** Randy
Hutchinson and John Serra at Wan Bridge, Gregg Erickson at RSK, Mark Wood at
Hanover, Jeff Raymer and Todd Riedel at M.L. Deer, Stephen Sams at Howard Hughes.
In each case the firm publishes a team page and the name is not on it. Where the
firm publishes someone in that function, that person replaced them: Jim Foy,
Houston Director of Construction at RSK; Marc Deer and Richard Rolland at M.L.
Deer. Wan Bridge publishes seven leaders and no construction or purchasing seat
at all, so that card now says so instead of naming one.

**A reason arguing against its own mark, in eight places.** Howard Hughes was
marked No on Track record directly above its own sentence saying it financed and
opened Greater Houston's first mass timber office building. That shipped for four
builds. Five trade records used the deck's own band sentence, "a firm with no
published figure is a Partly," under a Yes. Avenue CDC read Partly on a count
whose only evidence was a 2017 Kinder Institute piece about transit-oriented
development, which says nothing about how anything is built. J. Patrick Homes
read No on the same energy-certification evidence Caldwell Homes reads Partly on.

`verify.py` now fails the build on this class: a reason that opens with a
negation under a non-fail mark, a reason that names a verdict other than its own
mark, or a verdict that disagrees with its mark. 291 reasons, none contradict.

**Caldwell Companies said it does not pour walls** while Caldwell Homes, its own
homebuilding division, sat ten cards away in the A tier. Printer fit moved to
Partly and both records now point at each other.

**Boxer Property had the print time backwards.** The card said the walls printed
over seven to eight days. The source says the walls printed in under 30 hours and
seven to eight days covered the whole house. On a deck about printing walls that
is the number.

**Stylecraft exited the Houston metro.** Its chief executive said so on the
record to HousingWire in June 2026, in the same interview the deck already cites
for its closings figure. The record stays, because Ladera Creek in Conroe is
still live inventory inside the metro, and the card now says what he said.

Also corrected: Chesmar no longer operates as a distinct brand as of January
2026; Hillwood's League City tract is Legacy, more than 700 acres with ten
builders, not the 540 acres and 1,250 lots published in Build 51; Sunterra
carries eighteen builders, not fifteen; Johnson Development publishes fifteen
masterplans, not fourteen; Signorelli's Valley Ranch is in Montgomery County, not
Liberty, and the 6,400-acre figure the card hedged against appears in no source;
Commander Home Builders has one printed home under construction, not
twenty-three built; GreenEco's own domain is a parked-domain lander and the page
carrying its product claims returns 404, so both are gone and the record carries
what the ownership chain supports; Scott Anderson at Keystone is vice president
and general manager, and 2026-2027 president of the American Concrete Institute.

**A correction that had to be corrected.** An audit pass reported Derrick Hughes
as Wan Bridge's Vice President of Construction Operations, and a fetch of
`wanbridge.com/leadership/derrick-hughes` returned a bio saying exactly that. The
URL is a 404 and the name appears nowhere in the leadership page's own markup.
The finding was wrong, the check of it was wrong, and the name never shipped. A
fetch that reads a page is not evidence the page exists.

**Two agent findings were rejected.** D.R. Horton's 62 percent of Forestar and
the 83 percent lot share are both verbatim in the FY2025 annual report, which the
agent had not opened.

`linkcheck.py` is new and runs by hand, not in `make`, because a build that fails
when someone else's server is slow is a build nobody runs. It reports status on
every published URL, separates the hosts that refuse scripted requests from the
ones that are actually dead, and sweeps every source domain against the rules.

Corrections live in `audit.py` rather than in the modules holding the original
research, so the first draft stays readable next to what a second look changed.

97 firms, 247 contacts, 46 with a named decider. All checks pass.

## Build 51: the rest of the directory, and the builder that already bought one

Build 50 read one category of the Greater Houston Builders Association directory,
Builder - Single Family. The directory carries six more. Reading Build-to-Rent,
Build On Your Lot, ICF Homes, 50+ Communities, Multi-Family and Townhomes, and
Developers against the deck, and then reading the metro's permit leaders against
it, added five firms and found one omission that mattered more than any of them.

**D.R. Horton was not on the deck.** First in Greater Houston by permits in
August 2026 at 372, 65 communities and 668 standing homes on its own site, and
84,863 closings in the fiscal year to 30 September 2025. It is also the only firm
on this deck that has put equity into a printed wall system: a strategic
investment in Apis Cor, announced 11 March 2024, amount undisclosed. That fact
was already in the file, as a line in a competitor profile and a dot on the
field timeline, with no record attached to it. The named counterparty is Brad
Conlon, Senior Vice President of Business Development, in Arlington. No Houston
division officer is published, and the one Houston executive with a titled public
record left for Mattamy in August 2026, so the directory listings carrying his
name are stale and he is not on the card.

**Hillwood Communities was not on the deck either.** The market tab has cited
Wolf Ranch since Build 12 and never named the party that let a printer into it.
Hillwood Communities developed that community. It also runs three Greater Houston
masterplans, Pomona and Valencia in Manvel and a 540-acre League City tract, 4,500
lots at build-out, with a named Houston general manager, Russell Bynum, and a
named Senior Vice President of Planning and Innovation, Mark Meyer.

Also added: **DSLD Homes** (25th on the Builder 100, 3,989 closings in 2025,
three Houston communities, no Texas officer published), **Tilson Home
Corporation** (425 closings in 2024, on-your-lot, funds its own construction with
no interim loan, and publishes a stick-frame wall specification), and **Clay
Residential** (465 rental homes across two Houston communities, with the Vice
President of Construction Operations named on the association's own record).

Screened and not added, each for a stated reason: AOG Living builds apartments and
its pipeline is in Austin and Dallas; McCord Development holds 4,300 acres at
Generation Park with one 251-unit apartment building and no residential wall
product; America's Home Place publishes no volume and builds one-off custom;
ITEX Group builds three and four storey workforce multifamily; Forestar is 62
percent owned by D.R. Horton and reads as a clause inside that record rather than
a card of its own.

**A fact printed three times, again.** Build 49 cut evidence lines that only
restated a person's title. The filter was too narrow and caught 7 of them. It now
strips provenance clauses anywhere in the line, not only at the front, and
compares what is left to the title by token set rather than substring. 30 more
lines went, all of the form "Chief Executive Officer on LGI's own management
page" or "Vice President of Purchasing at Perry Homes. Houston, Texas." The link
beside the name already says where it came from. The evidence label changed from
"Company bio." to "Source.", because a press release is not a company bio.

**Quantities, again.** D.R. Horton's 84,863 and DSLD's 3,989 are company-wide
across 126 and 120-plus communities respectively. They do not go on the closings
chart, which compares firms at Houston scale and tops out at Westin's 1,062. They
carry a grid ordering figure instead, in `gap.SCALE`, so the largest builder on
the deck leads its cell rather than sorting last for want of a number. Tilson's
425 is Texas-wide from the Builder 100 and does go on the chart, labelled.

97 firms, 243 contacts, 50 with a named decider. All checks pass.

## Build 50: the directory the deck had never been checked against

The deck was assembled from trade press, master-planned-community builder rosters
and the Builder 100. None of those enumerate a privately held builder that does
not issue releases, which is most of the band a printer is bought for. The
Greater Houston Builders Association member directory does, and it is public and
browsable: 190 companies under Builder, Single Family, plus 70 under Build On
Your Lot and 46 under Multi-Family and Townhomes.

The directory was harvested in the browser rather than by fetch, because the page
renders all 190 cards client-side and a fetch truncates partway. Read against the
deck, 164 names were not on it.

Most of those 164 are the answer to the question rather than a gap. The Single
Family category holds custom and infill shops of one to five homes a year
alongside production builders, and they sit below the volume a machine is bought
for. Cross-referencing the directory against the masterplan rosters already held
narrowed it to thirteen names with live communities, and of those, all but two
were nationals the deck already carries or already reads as a No on Printer fit.

**Two were real, and one of them is significant.**

**Long Lake, Ltd.** closed 782 homes in 2025 and 912 in 2024, ranks 74th on the
2026 Builder 100, and describes itself as the largest privately held homebuilder
in Greater Houston. 22 communities from $249,990 to $627,900. 38 floor plans
across four product lines, identified by number rather than name, which is about
twenty starts per plan a year. It develops its own land through Woodmere
Development Co., so a pilot needs nobody else's permission. Its own about page
sells job-built production methods as a control advantage, which is the objection
written down in advance. Dustin Rodgers is Vice President of Construction.

**Caldwell Homes** is the opposite profile and is here for it: a 55+ single-storey
builder in three communities at $448,600 to $875,000, ranked 41st in the metro,
publishing no closings figure. Kevin Johnson holds Vice President of Construction
and Purchasing, one person for both, which is the shortest decision chain on the
deck. It has paid for above-code performance, ENERGY STAR and a 2020 PRISM energy
award, and nothing structural, so Track record reads Partly rather than Yes.

Note that Caldwell Homes is the homebuilding division of Caldwell Companies, which
was already on the deck as a land owner. They are one group and two records,
because one sells lots and the other builds houses.

The deck says how it was drawn now, in a new limits block. 90 firms became 92,
and 47 carry a named decision-maker.

## Live numbers

92 firms on the deck, 9 held off. 233 contacts, 111 LinkedIn profiles, 47 firms
with a named decider, 32 press items across 11 firms, 22 contractors, 0 open
items on the page.

The permit layer: 46 years of metro single-family authorisations, 26 years by
county across 10 counties, 6 years across 112 permit-issuing jurisdictions.

## Files and chain

`data_a/b/c.py` + `builders.py` + `creative.py` + `screens.py` + `why.py` +
`machine.py` + `found.py` + `links.py` + `corrections.py` + `competitors.py` +
`research2.py` + `market.py` + `code.py` + `trades.py` + `press.py` +
`resolved.py` + `permits.py` + `focus.py` + **`gap.py`** → `build.py` → `houston-data.json` → `_template.html` → HTML +
`rolodex-artifact.html` + `docs/` copies; `build_xlsx.py` → XLSX; `verify.py`
renders headless and fails on any of about fifty-five checks, including every
audit finding above, any wiki or contact-aggregator citation, any record missing
its three reasons, any blank headline figure, and any open item reaching the page.
`make` runs build, workbook and verify. `window.rolodex` is a supported scripting
surface (filters, call list, workbook builder).

## Still open

- 18 named deciders have no LinkedIn profile. Jordan York (Stylecraft) has a
  company page only. Matt Zetlmeisl and Trey Green were searched and are not on
  the platform.
- No volume figure: Tricoast, J. Patrick, Ravenna, GreenEco. Kendall's latest is 2022.
- Brohn's purchasing (local or Clayton) is not published anywhere.
- `internal/OPEN_ITEMS.md` holds 110 notes across 75 firms. It is the research
  queue, and it stays outside `docs/`.
- `docs/ROADMAP.md` carries six research passes. Pass 1 (contractors) is done and
  pass 2 (nationals as records) is done as of Build 51. Passes 3 to 6 are not:
  build-to-rent operators, firm main phone lines, the remaining register notes,
  payback-page inputs.
- D.R. Horton: no Houston division officer is published anywhere outside a data
  aggregator. The Apis Cor investment has no published follow-up two and a half
  years on, and the South Florida multi-unit project it named has not been shown
  to exist.
- DSLD Homes and Tilson Homes each carry one named person. Neither publishes a
  construction or purchasing officer.
- Whether Screen or List should be the landing view. List is now the faster tool.
- Both Houston Housing Authority domains stopped resolving. Its card now says so
  and carries its leadership titles without a link. A Houston affordable-housing
  body trades as Housing Alliance HTX at alliancehtx.org, and nothing on that
  site says it is the same organisation, so the deck does not claim it is.
- Three contacts sit behind houstonagentmagazine's Cloudflare interstitial, which
  a browser does not clear either: Jeff Dye, Jay McManus and Tim Drone. Four more
  sit on NewQuest's leadership page, which renders no names at all.
- 25 cards print a figure on no page they cite. Eight name a publisher without
  linking it and are a mechanical fix; run `python3 figures.py` for the list.
- 91 contacts stand on a LinkedIn headline with no firm page that names them.
  That is inside the deck's own rule and it is also the softest evidence on it.
  `probe.py` lists them; a phone call is what would harden them.
- `linkcheck.py` BLOCKED holds 30 hosts that refuse scripted requests. Each was
  confirmed by hand once. Re-confirm before adding to it.
- Nine named contacts sit on firms that publish no team page at all, so nothing
  confirms or denies them: Kendall, Long Lake, Westin, Perry, Partners in
  Building, Keystone Concrete Placement, Texas A&M Concrete, Tricoast, LGI.
- The repository has never been pushed to GitHub.
