# Rolodex · Greater Houston

Sixty-one Greater Houston builders and developers, each placed against three counts for ICON's Titan construction printer, with named decision-makers, verified links, a call list, an Excel export, a market view in figures, and the code and permitting route for a printed wall.

One self-contained HTML file. No framework, no build-time dependency beyond Python, no network request at runtime. The served copy is `docs/index.html`.

## The three counts

| Count | The question | Yes / Partly / No |
|---|---|---|
| **Repetition** | Builds the same plans, in one place | written per firm, with the reason |
| **Printer fit** | One or two printers would cover it | 25 to 400 homes a year concentrated is a Yes; 400 to 1,500, or purchasing at a parent, or no published figure, is a Partly; above 1,500 or a national desk is a No |
| **Track record** | Has paid for a new building method before | the only count that uses the accent colour |

Yes and Partly both keep a firm in. Only a No takes it out.

The first two counts place a firm on a 3×3 grid. Sections (already buying printed walls, strong target, one gap, custom and hybrid job, national builder, land owner, already working with ICON) are assigned before the count of holds, so a grid cell and a section are different sets; the page says so where the two could be confused.

## Five views

**Screen** the grid · **List** a table with per-row add and add-all · **Cover** an iPod-style cover flow · **Field** twelve competitors, ICON's own record, and the code and permitting route with verbatim quotes from the documents · **Market** five figures with a table and a source under each, and a note on how every number is produced.

One filter system across Screen, List and Cover: five controls, applied values as removable chips, a reset that is present whenever anything is on. The call list persists. Excel export is written in the page (a real `.xlsx`, no library) for either the current filtered set or the call list.

## Sourcing

Every number on the page is a count of records, a published figure with its source named in the tooltip and the table, or an assumption stated as one with what it rests on. A LinkedIn URL is held only where a retrieved page shows the person's name and the firm together; the sentence under the name says which page. Data aggregators were not used. No URL was constructed. No wiki is cited anywhere; the build refuses one.

## Build

```
pip install -r requirements.txt
playwright install chromium
make
```

`build.py` reads the data modules and writes `houston-data.json`, the standalone page, the artifact body and the served copies in `docs/`. `build_xlsx.py` writes the workbook. `verify.py` renders the page in headless Chromium and fails on any of about forty checks: console errors, every count against the data, the accent cascade, keyboard reach, focus management, print output, the in-page workbook, phone hit-testing, and the market figures.

## Layout

```
data_a.py data_b.py data_c.py builders.py creative.py   firm records, by layer
screens.py why.py machine.py                            verdicts, reasons, the printer-fit count
found.py links.py corrections.py research2.py          verification, links, corrections, second research pass
competitors.py code.py market.py                        the field, code and permitting, published figures
_template.html _market.js atmos.js _fonts.css           the page, the figures, the background, embedded type
build.py build_xlsx.py verify.py                        the chain
docs/                                                   served copies and the handoff
```

## Handoff

`docs/HANDOFF.md` carries the build history, the audit findings and what changed, the research passes, and what is still open. `docs/ROADMAP.md` is the research plan for the next pass.

Héctor Ibarzábal · September 2026
