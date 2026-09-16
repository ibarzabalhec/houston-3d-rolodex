# Research roadmap · Greater Houston Rolodex

For the next research session. Everything below is a research pass on the data modules, not a change to the page. Read `docs/HANDOFF.md` and `README.md` first. Build with `make`; it fails on any banned source, any unsourced figure it can detect, and any of about eighty page checks. Four more gates run by hand and are not optional before a push: `probe.py` (a name must be in the bytes of the page cited for it), `linkcheck.py` (every source URL swept for status and for a banned host), `figures.py` (a figure must be in the bytes of the page cited for it), `phonecheck.py` (the same for phone digits).

## The rules that do not move

Every number is a count of records, a published figure with its source named, or an assumption stated as one with what it rests on. No Wikipedia. No data aggregators (ZoomInfo, RocketReach, Apollo, org-chart sites, BBB records used as a leadership source). No constructed URL: a link is held only if it was seen in a search result or on a fetched page. A LinkedIn profile is held only where the retrieved page or the search-index title shows the person's name and the firm together; otherwise the firm's own page that names the person. Plain words, short sentences, no evaluative adjectives, nothing that tells the reader what to conclude, nothing about a departed employee beyond the fact of the departure, no em dashes. The tool is called Rolodex. The second count is Printer fit; Titan appears only where it is a fact about ICON.

A new firm record is a row in `builders.py` (production builders), `creative.py` (custom and hybrid), or `data_*.py` (the original layers), with a verdict sentence in `screens.py`, a why triple (Repetition, Printer fit, Track record) in `why.py` or on the row, a scores tuple (3 Yes, 2 Partly, 0 or 1 No), principals with a source per person in `links.py` `PERSON`, and a decider in `links.py` `DECIDERS` only where the title is the person who signs for a building method. Sections are assigned by `build.py`: adopter, icon (`machine.ICON_CLIENT`), channel, national (`NATIONAL`), creative (`CREATIVE`), then by count of holds. Held-off firms are listed in `competitors.py` and on the Johnson page, with the reason.

## Pass 1. Who buys and runs the machine (done, Build 34)

Run in Build 34. Twenty-one contractors now sit in the section "Builds the wall, not the house", plus six builders whose wall is already not wood and two firms that have paid for a printed building. What is still open from that pass: no executive is published for Keystone Concrete Placement, Harvey Cleary, Texas A&M Concrete, Encore Concrete Construction, Greco Structures, Andrade Construction, HTX Concrete, T&T Construction, Building Concrete Solutions, Leola Construction or M.L. Deer, so eleven of the twenty-one have no door. Baker Concrete Construction's own website was never read, so its Houston scope and leadership are unconfirmed. Blazer Building groups names under headings without printing a title beside each. Four firms surfaced in association directories with no website at all and are worth a phone call rather than more desk research: Tealstone Residential Concrete, Texas Concrete Placement, Future Frame USA and Lerma Construction Services. D.E. Harvey Builders was named general contractor on a tilt-wall building of more than four million square feet and was never reached; that is the largest unfinished thread.

Alongside the contractors, the public money they would bid on is still unrecorded: the City's Housing and Community Development Department and Harris County Community Services programmes, with a unit count and a dated award from the agenda item on the agency site. That is demand for a printed wall, not a buyer of a printer, and it belongs on the contractor's side rather than as a firm record.

## Before anything else: what a new session should check

Run `make` first. It builds, writes the workbook and runs about fifty headless checks, and it fails non-zero on any of them. Then read the last three entries in `docs/HANDOFF.md`, which record what the two reviews found and what was done about it.

Two faults in this file were both of the same kind, and a third of the same kind is the thing most likely to be there still: a section or a field was added to the page without being added to the code that fills it. The contractor reasons block was empty for two builds. Blank headline figures sat in a column for longer than that. When you add a section, a field or a count, grep for every place the existing ones are listed by name, and add a verifier check in the same commit.

## Pass 2. The nationals as records (done, Build 51)

Run in Build 51. What follows is the original brief, kept because the same
method applies to any national added later.


D.R. Horton, Lennar, Pulte, KB Home, Highland, Tri Pointe and Trendmaker, Toll, Beazer, Long Lake, Saratoga, Rausch Coleman (now Lennar). Our own Johnson page lists several as "not screened". For each: Houston closings from Builder 100 or the 10-K segment table (the firm's own filing on its investor site, not a summary), the Houston division president and VP of construction from the firm's own division page or a dated release, where the wall assembly is decided (corporate or division, from the 10-K or a stated purchasing structure), and any printed-wall or method statement on record. Lennar's Wolf Ranch and D.R. Horton's Apis Cor investment are already in the field; the record should carry the source line, not the interpretation. They go into the national section, which already exists.

## Pass 3. Build-to-rent operators

AMH (American Homes 4 Rent), Tricon, Invitation Homes, Progress Residential, NexMetro, Quinn Residences, Quarterra. For each: Houston units built or under way from the firm's own investor deck or 10-K, whether it builds or buys (AMH builds; Invitation buys), the Houston development lead named on the firm's own page or a dated release, and any method statement. Those that build go on the deck; those that only buy are channel, like the land developers.

## Pass 4. Contact channels — done in Build 56

143 numbers across 89 records, a stated absence on the other 17, a designation
rule recorded on every main line, and `phonecheck.py` testing each digit against
the page cited for it. Two departures from what this pass asked for, both in the
Build 56 handoff entry: where a page publishes several numbers the rest are kept
in a directory rather than discarded, and the List gets no column because an
eighth one fails the responsive gate at 320 pixels.

What is still open here: email. The deck carries no address for any firm or
person, and several of the seventeen absences above are firms that publish an
address and a form instead of a number.

## Pass 7. The wall value chain (done, Builds 62 and 63)

Six sweeps established that the original 22 contractors were all tilt-up, because
tilt-up.org is the only place panel counts are public. The section is now 50
contractors ordered along the chain a printed wall would displace: nozzle, slab,
tilt-up, precast, panel, masonry, ICF, general contractor. Beside it sit a 21-firm
supply panel (material and crew base, not buyers) and 21 firms that meet the
profile and publish no website at all. Build 63 gave the 28 new records their
people, profiles, sources and phone numbers.

The finding that governs any future contractor pass: **this trade does not publish
volume.** Of 87 candidates, 5 published a figure and 24 published years in
business. Builders publish closings because the Builder 100 makes them. So the
capital bar on a contractor is what the firm already owns, never sales volume.

## Pass 8. The outside review, tiers 2 and 3

Not started. The list is in `docs/HANDOFF.md` under Still open, in the order a
reader hits it. GreenEco's only source never names GreenEco, and it sits in the
group an ICON reader opens first. Six headline figures are arithmetic presented as
published. Seven headline figures are not Houston figures. 99 of 256 source
entries are bound to no claim. Then the mobile faults.

## Pass 5. Open items from the handoff

LinkedIn, firm-site or dated-release evidence for Matthew Roland and Diane Danilov (Westin), Christian Sommer and Keith Blum, Patrick Mustoe and Art Maya, Katy Hawes and Matt Norris (Jamestown), Stephen Ray (Smith Douglas), Jordan York. Annual volume for Tricoast, J. Patrick, Ravenna, GreenEco. Brohn's purchasing structure after the HistoryMaker deal. Westin's VP of Construction is the one decider on the page with no source; find one or remove the decider mark. Camillo: a construction or purchasing lead for Legend Homes or SimplyHome, from the firm's own pages only. Wan Bridge: which entity contracts, Wan Bridge or AiWB; the firm's own site, its releases, and the Texas SOS filing are the sources.

## Pass 6. The payback page (inputs only)

The page the hiring manager asked for: which combination of Houston accounts reaches six to ten printers by 2028, with payback per account. This session collects inputs, all sourced, and does not build the page. Wall square feet per home by plan size (the builders' own plan pages give square footage and stories; wall area is derived and the derivation stated). Conventional wall cost per square foot in Houston from a published estimator or a builder's stated cost, not ICON's $30 to $35 figure. Titan's published terms: $20 per square foot wall target, $5,000 deposit, training Q3 2026, deliveries 2027 (already in `code.py`). Crew size and cadence: the only published number is Wolf Ranch, about three weeks a home, one Vulcan, one crew (Engadget, 8 August 2024). Anything on Titan throughput must be marked as absent until ICON publishes it.

## What not to do

Do not add a "why Houston" line. Do not add a first-person block, a thesis statement, or a ninety-day plan to the page; those belong in the cover letter and the interview. Do not name the job or the employer on the page. Do not soften a No into a Partly without a source that supports it. Do not touch the visual system, the filter model, the export, or the verifier's existing checks except to add a check for what you add.
