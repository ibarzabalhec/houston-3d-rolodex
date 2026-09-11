# Research roadmap · Greater Houston Rolodex

For the next research session. Everything below is a research pass on the data modules, not a change to the page. Read `docs/HANDOFF.md` and `README.md` first. Build with `make`; it fails on any banned source, any unsourced figure it can detect, and any of about forty page checks.

## The rules that do not move

Every number is a count of records, a published figure with its source named, or an assumption stated as one with what it rests on. No Wikipedia. No data aggregators (ZoomInfo, RocketReach, Apollo, org-chart sites, BBB records used as a leadership source). No constructed URL: a link is held only if it was seen in a search result or on a fetched page. A LinkedIn profile is held only where the retrieved page or the search-index title shows the person's name and the firm together; otherwise the firm's own page that names the person. Plain words, short sentences, no evaluative adjectives, nothing that tells the reader what to conclude, nothing about a departed employee beyond the fact of the departure, no em dashes. The tool is called Rolodex. The second count is Printer fit; Titan appears only where it is a fact about ICON.

A new firm record is a row in `builders.py` (production builders), `creative.py` (custom and hybrid), or `data_*.py` (the original layers), with a verdict sentence in `screens.py`, a why triple (Repetition, Printer fit, Track record) in `why.py` or on the row, a scores tuple (3 Yes, 2 Partly, 0 or 1 No), principals with a source per person in `links.py` `PERSON`, and a decider in `links.py` `DECIDERS` only where the title is the person who signs for a building method. Sections are assigned by `build.py`: adopter, icon (`machine.ICON_CLIENT`), channel, national (`NATIONAL`), creative (`CREATIVE`), then by count of holds. Held-off firms are listed in `competitors.py` and on the Johnson page, with the reason.

## Pass 1. Who buys and runs the machine

The reviewers' main finding: Houston production builders self-perform nothing. The buyer and operator of a printer here may be a wall or shell subcontractor, a concrete contractor, or a panel supplier. There is not one on the page.

Build a list of Greater Houston framing, shell, concrete and tilt-wall contractors and panel suppliers that work for the builders already screened. Sources: the builders' own vendor or trade-partner pages, GHBA and TAB member directories (the firm's own listing, not a directory scrape), ABC and AGC Houston chapter member pages, trade press (Builder, HBJ, Realty News Report, Community Impact), the contractors' own sites. For each: what they build, for whom (named builder clients on their own site), crew size or annual volume if published, whether they own any equipment beyond hand tools, and who runs the company. Screen them on the same three counts with the printer-fit question rewritten for a contractor: would one or two printers cover a share of the walls this firm puts up in a year for the builders it already serves. Decide with Héctor whether contractors are a fourth section or a separate table under Field. Do not add them to the deck until that is decided. Alongside the contractors, note the public money they would bid on: the City's Housing and Community Development Department and Harris County Community Services programmes, with a unit count and a dated award from the agenda item on the agency site. That is demand for a printed wall, not a buyer of a printer, and it is recorded on the contractor's side, not as a firm record.

## Pass 2. The nationals as records

D.R. Horton, Lennar, Pulte, KB Home, Highland, Tri Pointe and Trendmaker, Toll, Beazer, Long Lake, Saratoga, Rausch Coleman (now Lennar). Our own Johnson page lists several as "not screened". For each: Houston closings from Builder 100 or the 10-K segment table (the firm's own filing on its investor site, not a summary), the Houston division president and VP of construction from the firm's own division page or a dated release, where the wall assembly is decided (corporate or division, from the 10-K or a stated purchasing structure), and any printed-wall or method statement on record. Lennar's Wolf Ranch and D.R. Horton's Apis Cor investment are already in the field; the record should carry the source line, not the interpretation. They go into the national section, which already exists.

## Pass 3. Build-to-rent operators

AMH (American Homes 4 Rent), Tricon, Invitation Homes, Progress Residential, NexMetro, Quinn Residences, Quarterra. For each: Houston units built or under way from the firm's own investor deck or 10-K, whether it builds or buys (AMH builds; Invitation buys), the Houston development lead named on the firm's own page or a dated release, and any method statement. Those that build go on the deck; those that only buy are channel, like the land developers.

## Pass 4. Contact channels

The call list carries 157 named people and no phone number. Add one firm main line per record, taken from the firm's own contact page only, into a `phone` field on the record, with the page URL as source. No personal numbers, no aggregator numbers. Where the firm publishes no number, leave the field empty and say so. The List, firm page and Excel export need the column added; `verify.py` needs a check that every phone on the page has a source URL on the same record.

## Pass 5. Open items from the handoff

LinkedIn, firm-site or dated-release evidence for Matthew Roland and Diane Danilov (Westin), Christian Sommer and Keith Blum, Patrick Mustoe and Art Maya, Katy Hawes and Matt Norris (Jamestown), Stephen Ray (Smith Douglas), Jordan York. Annual volume for Tricoast, J. Patrick, Ravenna, GreenEco. Brohn's purchasing structure after the HistoryMaker deal. Westin's VP of Construction is the one decider on the page with no source; find one or remove the decider mark. Camillo: a construction or purchasing lead for Legend Homes or SimplyHome, from the firm's own pages only. Wan Bridge: which entity contracts, Wan Bridge or AiWB; the firm's own site, its releases, and the Texas SOS filing are the sources.

## Pass 6. The payback page (inputs only)

The page the hiring manager asked for: which combination of Houston accounts reaches six to ten printers by 2028, with payback per account. This session collects inputs, all sourced, and does not build the page. Wall square feet per home by plan size (the builders' own plan pages give square footage and stories; wall area is derived and the derivation stated). Conventional wall cost per square foot in Houston from a published estimator or a builder's stated cost, not ICON's $30 to $35 figure. Titan's published terms: $20 per square foot wall target, $5,000 deposit, training Q3 2026, deliveries 2027 (already in `code.py`). Crew size and cadence: the only published number is Wolf Ranch, about three weeks a home, one Vulcan, one crew (Engadget, 8 August 2024). Anything on Titan throughput must be marked as absent until ICON publishes it.

## What not to do

Do not add a "why Houston" line. Do not add a first-person block, a thesis statement, or a ninety-day plan to the page; those belong in the cover letter and the interview. Do not name the job or the employer on the page. Do not soften a No into a Partly without a source that supports it. Do not touch the visual system, the filter model, the export, or the verifier's existing checks except to add a check for what you add.
