# Greater Houston Rolodex — handoff

Build 43 · 2026-09-12

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

## Live numbers

90 firms on the deck, 9 held off. 223 contacts, 109 LinkedIn profiles, 44 firms
with a named decider (42 confirmed, 2 to confirm), 32 press items across 11 firms,
22 contractors in the trade section, 3 firms publishing nobody at all, 0 open
items on the page.

## Files and chain

`data_a/b/c.py` + `builders.py` + `creative.py` + `screens.py` + `why.py` +
`machine.py` + `found.py` + `links.py` + `corrections.py` + `competitors.py` +
`research2.py` + `market.py` + `code.py` + **`trades.py`** + **`press.py`** +
**`resolved.py`** → `build.py` → `houston-data.json` → `_template.html` → HTML +
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
- `docs/ROADMAP.md` carries six research passes. Pass 1 (contractors) is done.
  Passes 2 to 6 are not: nationals as records, build-to-rent operators, firm main
  phone lines, the remaining register notes, payback-page inputs.
- Whether Screen or List should be the landing view. List is now the faster tool.
- The repository has never been pushed to GitHub.
