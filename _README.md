# Rolodex · Greater Houston and Dallas-Fort Worth

__N__ Greater Houston builders, developers and wall contractors, each read against three counts for a construction printer, with __NP__ named contacts, a call list, an Excel export, the Houston market in figures, and the code and permitting route for a printed wall.

Live: https://ibarzabalhec.github.io/houston-3d-rolodex/

A second market, Dallas-Fort Worth, sits in the same file behind the switch on the home screen: __DFW_N__ firms, the same three counts and the same five views, in Dallas blue where Houston uses ICON orange. `build_dfw.py` builds it, and `MARKET=dfw` runs the verifier and the workbook against it.

One self-contained HTML file. No framework and no runtime network request. A security policy in the page has the browser block any request, and any script not written in the page. `docs/index.html` is the served copy. This README is written by `emit.py` from the page's own data, so its counts are the page's counts.

## The three counts

| Count | The question | Yes / Partly / No |
|---|---|---|
| **Repetition** | Builds the same plans, in one place. For a contractor: puts up the same wall, in one metro | written per firm, with the reason |
| **Printer fit** | One or two printers would cover it | 25 to 400 homes a year concentrated is a Yes. 400 to 1,500, purchasing at a parent, or no published figure is a Partly. Above 1,500 or a national purchasing desk is a No |
| **Track record** | Has paid for a new building method before. Energy ratings, cycle times and buyer software read No | the only count that uses the accent color |

Yes and Partly both count as holding. A No does not. Sections are assigned before the holds are counted, so a section and a grid cell are different sets.

## Sections

__SECTIONS__

The contractors are ordered along the wall value chain a printed wall would displace: nozzle, slab, tilt-up, precast, panel, masonry, ICF, general contractor. Beside them sit a __NS__-firm supply panel and __NN__ firms that meet the profile and publish no website.

## Five views

**List** the call file, and where the page opens · **Screen** the 3×3 grid · **Cover** a cover flow · **Field** the printers in the field, ICON's own record, and the code route with verbatim quotes · **Market** closings, permits by county and jurisdiction, and printed homes in Texas, each figure with a table and its sources.

One filter system across List, Screen and Cover. The call list persists in the browser. Excel export is written in the page, for the filtered set or the call list.

## Sourcing

Every number is a count of records, a published figure with its source named, or an assumption stated as one. A contact rests on a LinkedIn headline naming the firm, the firm's own site, or dated reporting, and the card says which. Phone numbers and email addresses come only from the firm's own pages. No data aggregator was used, no source URL was constructed, and no wiki is cited. The build refuses all three. The LinkedIn search links beside a name are searches, not sources.

## Build

```
pip install -r requirements.txt && python3 -m playwright install chromium
make            # build both markets, the workbooks and the intro, unit tests, headless verify,
                #   and xsscheck.py: the page built from data with markup on every string
make check      # ruff and the page's JavaScript (pip install -r requirements-dev.txt)
make gates      # the network gates, run by hand before sending:
                #   probe.py       every name is in the bytes of the page cited for it
                #   linkcheck.py   every source URL, status and banned-host sweep
                #   figures.py     every figure is in the bytes of the page cited for it
                #   phonecheck.py  every phone and email is in the bytes of its page
                #   marketcheck.py the same four for Dallas-Fort Worth
```

The data file is the source of truth: `build.py` and `build_dfw.py` write it to
`build/`, `emit.py` writes the page from it, and nothing downstream is edited by
hand. Corrections are late layers (`audit.py` to `audit13.py`), each applied only
while the text it replaces is still there. The build number and the page's date
live in `version.py`, the banned-source list in `policy.py`, and every path the
build reads or writes in `paths.py`. `docs/` is what GitHub Pages serves. `build/`
holds the build's own products and is not committed. The research inputs the build
reads stay on the build machine, in `internal/`, out of this repository, so a
fresh clone serves the built page from `docs/` but does not rebuild it.

