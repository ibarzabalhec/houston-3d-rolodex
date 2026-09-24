# Rolodex · Greater Houston and Dallas-Fort Worth

126 Greater Houston builders, developers and wall contractors, each read against three counts for a construction printer, with 295 named contacts, a call list, an Excel export, the Houston market in figures, and the code and permitting route for a printed wall.

Live: https://ibarzabalhec.github.io/houston-3d-rolodex/

A second market, Dallas-Fort Worth, sits in the same file behind the switch on the home screen: 126 firms, the same three counts and the same five views, in Dallas blue where Houston uses ICON orange. `build_dfw.py` builds it from `dfw/`, and `MARKET=dfw` runs the verifier and the workbook against it.

One self-contained HTML file. No framework, no runtime network request. `docs/index.html` is the served copy. This README is written by `build.py`, so its counts are the page's counts.

## The three counts

| Count | The question | Yes / Partly / No |
|---|---|---|
| **Repetition** | Builds the same plans, in one place. For a contractor: puts up the same wall, in one metro | written per firm, with the reason |
| **Printer fit** | One or two printers would cover it | 25 to 400 homes a year concentrated is a Yes. 400 to 1,500, purchasing at a parent, or no published figure is a Partly. Above 1,500 or a national purchasing desk is a No |
| **Track record** | Has paid for a new building method before | the only count that uses the accent colour |

Yes and Partly both count as holding. A No does not. Sections are assigned before the holds are counted, so a section and a grid cell are different sets.

## Sections

- **Already buying printed walls**, 3
- **Lennar and the firms it owns**, 3
- **Holds all three counts**, 12
- **One gap**, 31
- **Builds the wall, not the house**, 50
- **National builder**, 10
- **Custom and hybrid job**, 10
- **Land owner, not the buyer**, 7

The contractors are ordered along the wall value chain a printed wall would displace: nozzle, slab, tilt-up, precast, panel, masonry, ICF, general contractor. Beside them sit a 22-firm supply panel and 21 firms that meet the profile and publish no website.

## Five views

**List** the call file, and where the page opens · **Screen** the 3×3 grid · **Cover** a cover flow · **Field** the printers in the field, ICON's own record, and the code route with verbatim quotes · **Market** closings, permits by county and jurisdiction, and printed homes in Texas, each figure with a table and its sources.

One filter system across List, Screen and Cover. The call list persists in the browser. Excel export is written in the page, for the filtered set or the call list.

## Sourcing

Every number is a count of records, a published figure with its source named, or an assumption stated as one. A contact rests on a LinkedIn headline naming the firm, the firm's own site, or dated reporting, and the card says which. Phone numbers and email addresses come only from the firm's own pages. No data aggregator was used, no source URL was constructed, and no wiki is cited. The build refuses all three. The LinkedIn search links beside a name are searches, not sources.

## Build

```
make            # build, workbook, headless verify
python3 probe.py        # every name is in the bytes of the page cited for it
python3 linkcheck.py    # every source URL, status and banned-host sweep
python3 figures.py      # every figure is in the bytes of the page cited for it
python3 phonecheck.py   # every phone and email is in the bytes of its page
python3 marketcheck.py dfw/dfw-data.json   # the same four gates for Dallas-Fort Worth
```

