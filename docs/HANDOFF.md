# Greater Houston Rolodex — handoff

Build 32 · 2026-09-11

The tool is called **Rolodex**, not ICON. It is built in ICON's visual language and screens for the Titan, but it does not wear ICON's name. It is outward-facing: no build numbers, no research narration, no internal memos on the page.

## Where it lives

- **Hosted**: published as a claude.ai artifact (Build 32, Version 7), private until shared from the page's own share menu. The artifact declares the `downloads` capability so the in-page Excel export works in the viewer. To republish from a new session, pass the artifact URL as `url`; the file to publish is `rolodex-artifact.html`, which `build.py` emits alongside the standalone file.
- **Standalone**: `ICON_Greater_Houston_Rolodex.html` (self-contained, opens from disk) and `ICON_Greater_Houston_Rolodex.xlsx` (the full workbook).
- **Source**: a git repository, ready to push. `make` builds, exports and verifies. The served copies are in `docs/` so GitHub Pages can serve them from that folder.

## The thesis

A printer is bought by a builder, not by a landowner and not by a fund. The builder that buys one or two machines repeats a small plan set inside a handful of master planned communities and closes enough houses a year to keep a machine working, without being large enough to buy through a national purchasing desk.

## The three counts

1. **Repeats** enough units in one place.
2. **Machine fit**: one or two machines would cover it. Roughly 25 to 400 homes a year concentrated in a few communities clears it; 400 to 1,500, or purchasing at a parent, or no published figure, is partial; above 1,500 or bought nationally fails.
3. **Method appetite**: has paid for an unproven way of building. The only thing on the page that uses orange. Eight firms of 61.

A Partly still counts as holding. Only a No does not. This rule is now stated in the legend on every view and under the counts on every firm page.

## The sections

Labels are names, not sentences. The explanatory clause each used to carry is in a note under the section header in List view and in `group_notes` in the data.

- **Already buying printed walls** (3), with a competitor
- **Strong target** (10): holds all three counts
- **One gap** (24): holds two
- **Custom and hybrid job** (9): retail and hospitality adjacent, adaptive reuse, design-led
- **National builder** (8): purchasing at a national desk, so the first order is a pilot
- **Land owner, not the buyer** (6): masterplan owners; each lists the builders in the file that build inside it
- **Already working with ICON** (1): Friendswood, owned by Lennar. Acknowledged, not prospected.

## The four views

Screen (3×3 matrix), List (table with per-row add and add-all), Cover (iPod cover flow ported from the Americas rolodex, real geometry), Field (competitors and ICON's own record).

**One filter system across Screen, List and Cover**: five controls (Section, Repeats, Machine fit, Method appetite, Decider), each a menu whose option counts respect everything else applied. Applied values show as removable chips with a Reset all that is present whenever anything is on. Search composes with filters. Field disables search.

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

## Live numbers

61 firms on the deck, 9 held off. 157 contacts, 78 LinkedIn profiles, 24 firms with a named decider (22 confirmed, 2 to confirm), 186 open items.

## Files and chain

`data_a/b/c.py` + `builders.py` + `creative.py` + `screens.py` + `why.py` + `machine.py` + `found.py` + `links.py` + `corrections.py` + `competitors.py` + **`research2.py`** → `build.py` → `houston-data.json` → `_template.html` → HTML + `rolodex-artifact.html`; `build_xlsx.py` → XLSX; `verify.py` renders headless and fails on any of about thirty checks, including every audit finding above. The build refuses any wiki citation. `window.rolodex` is a supported scripting surface (filters, call list, workbook builder).

## Still open

- No LinkedIn for: Matthew Roland and Diane Danilov (Westin), Christian Sommer and Keith Blum (Tricoast), Patrick Mustoe and Art Maya (J. Patrick), Katy Hawes and Matt Norris (Jamestown), Stephen Ray (Smith Douglas), Jordan York (Stylecraft, company page only).
- No volume figure: Tricoast, J. Patrick, Ravenna, GreenEco. Kendall's latest is 2022.
- Brohn's purchasing (local or Clayton) is not published anywhere.
- Whether Screen or List should be the landing view. List is now the faster tool.
- Clone the source into `~/projects`.
