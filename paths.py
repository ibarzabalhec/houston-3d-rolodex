"""Where the build reads and writes, in one place, so a file can move without a hunt.

Three trees, and only the first is published:

  docs/       committed and served by GitHub Pages: the page, its public data and
              the two workbooks. emit.py and build_xlsx.py write it.
  build/      not committed: what the build makes for its own use. The full data
              files, with the fields and firms the public copies leave out, the
              standalone page, the artifact copy and the workbooks.
  internal/   not committed, and never published: the research inputs the build
              reads, research scripts, fetch caches, the handoff, and the archive.
              internal/START_HERE.md says what is where.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent

DOCS = ROOT / "docs"
BUILD = ROOT / "build"
INTERNAL = ROOT / "internal"
INPUTS = INTERNAL / "inputs"
CACHE = INTERNAL / "cache"

# Build products (build.py, build_dfw.py, emit.py, build_xlsx.py)
HOU_DATA = BUILD / "houston-data.json"
DFW_DATA = BUILD / "dfw-data.json"
PAGE = BUILD / "ICON_Greater_Houston_Rolodex.html"
ARTIFACT = BUILD / "rolodex-artifact.html"
HOU_XLSX = BUILD / "ICON_Greater_Houston_Rolodex.xlsx"
DFW_XLSX = BUILD / "DFW_Rolodex.xlsx"

# Research inputs the build reads. They stay on the build machine.
AUDIT7 = INPUTS / "audit7"              # audit7.py's edit files
DFW_PACK = INPUTS / "dfw-pack"          # the first DFW research pack, as delivered
DFW_EDIT = INPUTS / "dfw-edit"          # the DFW cards rewritten in house style
DFW_HAND = INPUTS / "dfw-hand.json"     # dated hand readings of DFW pages


def hand_readings(data_file):
    """The hand readings for a market's data file (marketcheck.py)."""
    return DFW_HAND if pathlib.Path(data_file).name == DFW_DATA.name else \
        pathlib.Path(data_file).parent / "hand.json"


def out(path):
    """Make the parent folder of a file the build is about to write."""
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    return path
