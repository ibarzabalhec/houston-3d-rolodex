# -*- coding: utf-8 -*-
"""What kind of firm each card is, as a short marker: GC, Developer, Homebuilder.

Build 90. A reader opening a card, or scanning the List, wants the type of firm
first. The marker is the plain noun a reader in the trade would use. It says
nothing about whether a firm would buy a printer: Build 88 tried that
("Printer buyer", "Client") and it read as a verdict the page cannot make.

Every card on either deck is listed by id, with the words its type was read
from. The build stops on a card with no type, a type for a card not on the
deck, a type outside TYPES, or one firm with two types on the two decks.
"""

# In the order the Type menu lists them: who builds homes, who develops and
# owns, then the trades and plants in the order a wall gets made.
TYPES = (
    ("homebuilder", "Homebuilder"),
    ("btr", "Build-to-rent"),
    ("developer", "Developer"),
    ("land", "Land developer"),
    ("masterplan", "Masterplan"),
    ("owner", "Owner"),
    ("manager", "Property manager"),
    ("agency", "Public agency"),
    ("nonprofit", "Nonprofit"),
    ("gc", "GC"),
    ("concrete", "Concrete contractor"),
    ("precast", "Precast plant"),
    ("panel", "Panel plant"),
    ("masonry", "Masonry contractor"),
    ("trade", "Trade contractor"),
    ("supplier", "Supplier"),
)
LABEL = dict(TYPES)

TYPE = {
    # Greater Houston
    "HOU-002":      "homebuilder",  # Homebuilder, printed homes
    "HOU-016":      "homebuilder",  # Homebuilder, printed homes
    "HOU-017":      "homebuilder",  # Homebuilder, printed duplex
    "HOU-123":      "homebuilder",  # ICF homebuilder
    "HOU-001":      "btr",          # Build-to-rent developer and builder
    "HOU-126":      "homebuilder",  # Modular homebuilder
    "HOU-060":      "homebuilder",  # Production homebuilder
    "HOU-061":      "homebuilder",  # Production homebuilder
    "HOU-073":      "homebuilder",  # Production homebuilder
    "HOU-168":      "homebuilder",  # Production and rental homebuilder
    "HOU-003":      "agency",       # Public housing authority
    "HOU-130":      "homebuilder",  # Production homebuilder
    "HOU-074":      "homebuilder",  # Entry-level homebuilder
    "HOU-131":      "homebuilder",  # Active-adult homebuilder
    "HOU-010":      "btr",          # Build-to-rent builder and owner
    "HOU-022":      "homebuilder",  # Production homebuilder
    "HOU-136":      "btr",          # Build-to-rent builder
    "HOU-122":      "homebuilder",  # Custom homebuilder, concrete panel walls
    "HOU-007":      "homebuilder",  # Production homebuilder
    "HOU-004":      "homebuilder",  # Townhome builder
    "HOU-127":      "developer",    # Manufactured-home community developer
    "HOU-125":      "homebuilder",  # Custom homebuilder
    "HOU-124":      "homebuilder",  # Custom coastal homebuilder
    "HOU-135":      "homebuilder",  # Build-on-your-lot homebuilder
    "HOU-068":      "homebuilder",  # Semi-custom homebuilder
    "HOU-064":      "homebuilder",  # Affordable production homebuilder
    "HOU-076":      "homebuilder",  # Entry-level homebuilder, a David Weekley line
    "HOU-071":      "homebuilder",  # Family homebuilder
    "HOU-063":      "homebuilder",  # Family homebuilder
    "HOU-066":      "homebuilder",  # Infill homebuilder
    "HOU-062":      "homebuilder",  # Production homebuilder
    "HOU-128":      "owner",        # Commercial property owner
    "HOU-020":      "developer",    # Industrial and rental developer
    "HOU-075":      "homebuilder",  # Production homebuilder
    "HOU-026":      "btr",          # Build-to-rent operator
    "HOU-033":      "homebuilder",  # Production homebuilder, a Dream Finders brand
    "HOU-069":      "homebuilder",  # Production homebuilder
    "HOU-077":      "homebuilder",  # Production homebuilder
    "HOU-035":      "nonprofit",    # Nonprofit housing developer
    "HOU-045":      "homebuilder",  # Production homebuilder
    "HOU-067":      "homebuilder",  # Semi-custom homebuilder
    "HOU-044":      "btr",          # Build-to-rent builder
    "HOU-070":      "homebuilder",  # Semi-custom homebuilder
    "HOU-028":      "developer",    # Apartment developer with its own builder
    "HOU-152":      "trade",        # Steel framing contractor
    "HOU-146":      "panel",        # Wall panel and truss plant
    "HOU-139":      "precast",      # Precast concrete plant
    "HOU-120":      "concrete",     # ICF wall contractor
    "HOU-104":      "concrete",     # Concrete contractor
    "HOU-156":      "masonry",      # Masonry contractor
    "HOU-101":      "concrete",     # Concrete placement contractor
    "HOU-121":      "trade",        # Drywall and interiors contractor
    "HOU-162":      "concrete",     # Shotcrete contractor
    "HOU-143":      "precast",      # Precast concrete plant
    "HOU-129":      "gc",           # Design-build firm
    "HOU-157":      "masonry",      # Masonry and stone contractor
    "HOU-137":      "precast",      # Precast concrete plant
    "HOU-117":      "gc",           # Apartment general contractor
    "HOU-147":      "panel",        # Building products supplier and panel plants
    "HOU-155":      "masonry",      # Masonry contractor
    "HOU-141":      "precast",      # Precast concrete plant
    "HOU-106":      "concrete",     # Tilt-up concrete contractor
    "HOU-102":      "gc",           # General contractor with its own concrete crews
    "HOU-142":      "precast",      # Precast concrete plant
    "HOU-112":      "concrete",     # Tilt-up concrete contractor
    "HOU-151":      "panel",        # Wall panel plants
    "HOU-149":      "panel",        # Wall panel and truss plant
    "HOU-144":      "precast",      # Precast concrete plant
    "HOU-138":      "precast",      # Hollowcore plank plant
    "HOU-105":      "concrete",     # Tilt-up concrete contractor
    "HOU-145":      "precast",      # Precast concrete plant
    "HOU-114":      "gc",           # General contractor, tilt-up
    "HOU-165":      "concrete",     # Foundation contractor
    "HOU-161":      "concrete",     # Concrete pumping company
    "HOU-103":      "concrete",     # Tilt-up concrete contractor
    "HOU-140":      "precast",      # Precast concrete plant
    "HOU-150":      "panel",        # Truss and wall panel plant
    "HOU-159":      "masonry",      # Masonry contractor
    "HOU-158":      "masonry",      # Masonry contractor
    "HOU-164":      "concrete",     # Concrete contractor
    "HOU-153":      "panel",        # Light-gauge steel fabricator
    "HOU-113":      "concrete",     # Tilt-up and structural concrete contractor
    "HOU-160":      "concrete",     # Concrete pumping company
    "HOU-163":      "concrete",     # Residential foundation contractor
    "HOU-148":      "panel",        # Wall panel and truss plant
    "HOU-118":      "trade",        # Shell contractor
    "HOU-115":      "gc",           # General contractor
    "HOU-111":      "concrete",     # Concrete contractor
    "HOU-119":      "gc",           # General contractor, ICF and tilt-wall
    "HOU-109":      "concrete",     # Concrete and civil contractor
    "HOU-107":      "concrete",     # Site and concrete subcontractor
    "HOU-116":      "gc",           # General contractor
    "HOU-108":      "concrete",     # Tilt-up and site concrete contractor
    "HOU-110":      "concrete",     # Concrete and metal building contractor
    "HOU-006":      "developer",    # Apartment and mixed-use developer
    "HOU-072":      "homebuilder",  # Custom homebuilder, build on your lot
    "HOU-083":      "developer",    # Retail and office developer
    "HOU-005":      "developer",    # Mixed-use developer
    "HOU-081":      "developer",    # Investment and development firm
    "HOU-036":      "developer",    # Mixed-use developer
    "HOU-037":      "developer",    # Adaptive-reuse developer
    "HOU-082":      "developer",    # Commercial developer
    "HOU-038":      "manager",      # Property manager
    "HOU-080":      "developer",    # Adaptive-reuse developer
    "HOU-132":      "homebuilder",  # National homebuilder
    "HOU-167":      "homebuilder",  # National homebuilder
    "HOU-009":      "homebuilder",  # National homebuilder
    "HOU-134":      "homebuilder",  # National homebuilder
    "HOU-014":      "homebuilder",  # National homebuilder
    "HOU-012":      "homebuilder",  # National homebuilder
    "HOU-008":      "homebuilder",  # National homebuilder
    "HOU-025":      "homebuilder",  # National homebuilder
    "HOU-024":      "homebuilder",  # National homebuilder
    "HOU-023":      "homebuilder",  # National homebuilder
    "HOU-013":      "homebuilder",  # National homebuilder
    "HOU-034":      "homebuilder",  # National homebuilder
    "HOU-011":      "land",         # Masterplan developer
    "HOU-015":      "land",         # Land developer
    "HOU-041":      "land",         # Masterplan developer
    "HOU-133":      "land",         # Masterplan developer
    "HOU-039":      "land",         # Land developer
    "HOU-040":      "land",         # Masterplan developer
    "HOU-043":      "land",         # Land developer
    "HOU-166":      "homebuilder",  # National homebuilder, Houston division
    "HOU-042":      "land",         # Land developer, owned by Lennar
    "HOU-078":      "homebuilder",  # Entry-level and move-up homebuilder, owned by Lennar
    # Dallas-Fort Worth
    "DFW-BTR-010":  "btr",          # Build-to-rent developer and builder
    "DFW-020":      "homebuilder",  # Production homebuilder
    "DFW-032":      "homebuilder",  # Production homebuilder
    "DFW-026":      "homebuilder",  # Production homebuilder
    "DFW-027":      "homebuilder",  # Production and custom homebuilder
    "DFW-BTR-001":  "btr",          # Single-family rental owner and builder
    "DFW-003b":     "homebuilder",  # Townhome builder, a Green Brick brand
    "DFW-003d":     "homebuilder",  # Single-family and townhome builder, a Green Brick brand
    "DFW-BTR-005":  "btr",          # Build-to-rent developer
    "DFW-014":      "homebuilder",  # Move-up homebuilder, a Green Brick brand
    "DFW-045":      "homebuilder",  # Production homebuilder
    "DFW-003c":     "homebuilder",  # Luxury homebuilder, a Green Brick brand
    "DFW-003a":     "homebuilder",  # Entry-level and move-up homebuilder, a Green Brick brand
    "DFW-079":      "homebuilder",  # Production homebuilder
    "DFW-BTR-006":  "btr",          # Build-to-rent developer and builder
    "DFW-029":      "homebuilder",  # Production homebuilder
    "DFW-078":      "homebuilder",  # Townhome builder
    "DFW-BTR-008":  "btr",          # Build-to-rent builder and owner
    "DFW-037":      "homebuilder",  # Family homebuilder
    "DFW-BTR-009":  "btr",          # Build-to-rent community
    "DFW-008":      "homebuilder",  # Production homebuilder
    "DFW-023":      "homebuilder",  # Semi-custom production homebuilder
    "DFW-035":      "homebuilder",  # Villa and townhome builder
    "DFW-BTR-007":  "btr",          # Build-to-rent builder
    "DFW-043":      "homebuilder",  # Semi-custom homebuilder
    "DFW-021":      "homebuilder",  # Production homebuilder
    "DFW-034":      "homebuilder",  # Production homebuilder
    "DFW-022":      "homebuilder",  # Homebuilder and developer
    "DFW-031":      "homebuilder",  # Homebuilder, owned by Partners in Building
    "DFW-044":      "homebuilder",  # Production homebuilder
    "DFW-033":      "homebuilder",  # Production homebuilder
    "DFW-038":      "homebuilder",  # Entry-level homebuilder, an Ashton Woods brand
    "DFW-030":      "homebuilder",  # Production homebuilder
    "DFW-081":      "homebuilder",  # Move-up homebuilder
    "DFW-028":      "homebuilder",  # Production homebuilder
    "DFW-024":      "homebuilder",  # Luxury homebuilder, a Perry Homes brand
    "DFW-042":      "homebuilder",  # Production homebuilder, a Dream Finders brand
    "DFW-073":      "homebuilder",  # Luxury homebuilder
    "DFW-025":      "homebuilder",  # Production and semi-custom homebuilder
    "DFW-TR-051":   "concrete",     # ICF and concrete contractor
    "DFW-TR-074":   "panel",        # Wall panel and truss plant
    "DFW-TR-050":   "concrete",     # ICF wall contractor
    "DFW-TR-092":   "panel",        # Exterior wall panel plant
    "DFW-TR-091":   "trade",        # Framing and interiors contractor
    "DFW-TR-040":   "masonry",      # Masonry contractor
    "DFW-TR-093":   "trade",        # SIP envelope contractor
    "DFW-TR-012":   "supplier",     # Building materials dealer
    "DFW-TR-010":   "panel",        # Truss and wall panel plant
    "DFW-TR-031":   "precast",      # Precast concrete plant
    "DFW-TR-026":   "gc",           # General contractor with its own concrete crews
    "DFW-TR-032":   "precast",      # Precast concrete plant
    "DFW-TR-085":   "concrete",     # Residential foundation contractor
    "DFW-TR-064":   "concrete",     # Tilt-up concrete contractor
    "DFW-TR-030":   "precast",      # Precast concrete plant
    "DFW-TR-002":   "concrete",     # Residential concrete contractor
    "DFW-TR-086":   "masonry",      # Masonry and stucco contractor
    "DFW-TR-083":   "masonry",      # Residential masonry contractor
    "DFW-TR-081":   "masonry",      # Masonry contractor
    "DFW-TR-084":   "concrete",     # Foundation contractor
    "DFW-TR-089":   "masonry",      # Masonry and stucco contractor
    "DFW-TR-082":   "masonry",      # Masonry and stucco contractor
    "DFW-TR-088":   "masonry",      # Masonry contractor
    "DFW-TR-042":   "masonry",      # Masonry contractor
    "DFW-TR-079":   "gc",           # Tilt-up general contractor
    "DFW-TR-090":   "masonry",      # Residential masonry contractor
    "DFW-TR-071":   "masonry",      # Masonry contractor
    "DFW-TR-087":   "concrete",     # Post-tension foundation company
    "DFW-TR-022":   "gc",           # General contractor
    "DFW-TR-020":   "concrete",     # Tilt-up concrete contractor
    "DFW-TR-041":   "masonry",      # Masonry and precast installer
    "DFW-TR-025":   "gc",           # Construction manager
    "DFW-TR-027":   "concrete",     # Tilt-up and structural concrete contractor
    "DFW-TR-060":   "concrete",     # Concrete pumping company
    "DFW-TR-023":   "concrete",     # Structural concrete contractor
    "DFW-TR-024":   "gc",           # General contractor
    "DFW-TR-021":   "gc",           # General contractor
    "DFW-TR-001":   "concrete",     # Residential foundation contractor
    "DFW-TR-011":   "panel",        # Truss and wall panel plant
    "DFW-047":      "homebuilder",  # Custom homebuilder, SIP walls
    "DFW-048":      "homebuilder",  # Custom homebuilder, build on your lot
    "DFW-001":      "homebuilder",  # National homebuilder
    "DFW-007":      "homebuilder",  # National homebuilder
    "DFW-061":      "homebuilder",  # Production homebuilder, run from Houston
    "DFW-011":      "homebuilder",  # National homebuilder
    "DFW-010":      "homebuilder",  # National homebuilder
    "DFW-052":      "homebuilder",  # National homebuilder
    "DFW-063":      "homebuilder",  # National homebuilder, a PulteGroup brand
    "DFW-060":      "homebuilder",  # National homebuilder
    "DFW-064":      "homebuilder",  # Active-adult homebuilder, a PulteGroup brand
    "DFW-003":      "homebuilder",  # National homebuilder and land developer
    "DFW-058":      "homebuilder",  # National homebuilder
    "DFW-050":      "homebuilder",  # National homebuilder
    "DFW-054":      "homebuilder",  # National homebuilder
    "DFW-055":      "homebuilder",  # National homebuilder
    "DFW-062":      "homebuilder",  # National homebuilder
    "DFW-006":      "homebuilder",  # National homebuilder
    "DFW-053":      "homebuilder",  # National homebuilder
    "DFW-051":      "homebuilder",  # National luxury homebuilder
    "DFW-009":      "homebuilder",  # National homebuilder
    "DFW-059":      "homebuilder",  # National homebuilder
    "DFW-CH-015":   "masterplan",   # Masterplanned community
    "DFW-CH-021":   "land",         # Masterplan developer
    "DFW-CH-001":   "land",         # Masterplan developer
    "DFW-CH-018":   "land",         # Land developer
    "DFW-CH-003":   "land",         # Land developer
    "DFW-CH-014":   "land",         # Masterplan developer
    "DFW-CH-008":   "masterplan",   # Masterplanned community
    "DFW-CH-020":   "masterplan",   # Masterplanned community
    "DFW-CH-016":   "masterplan",   # Masterplanned community
    "DFW-CH-004":   "masterplan",   # Masterplanned community
    "DFW-CH-007":   "masterplan",   # Masterplanned community
    "DFW-CH-002":   "land",         # Land developer
    "DFW-CH-011":   "masterplan",   # Masterplanned community
    "DFW-CH-019":   "masterplan",   # Masterplanned community
    "DFW-CH-009":   "masterplan",   # Masterplanned community
    "DFW-CH-017":   "land",         # Masterplan developer
    "DFW-BTR-004":  "owner",        # Single-family rental owner
    "DFW-CH-012":   "masterplan",   # Masterplanned community
    "DFW-CH-010":   "masterplan",   # Masterplanned community
    "DFW-CH-005":   "masterplan",   # Masterplanned community
    "DFW-CH-013":   "masterplan",   # Masterplanned community
    "DFW-002":      "homebuilder",  # National homebuilder
}

# The same firm on both decks: one type. Checked by apply().
SAME_FIRM = (
    ("HOU-001", "DFW-BTR-010"), ("HOU-010", "DFW-BTR-008"), ("HOU-022", "DFW-061"),
    ("HOU-033", "DFW-042"), ("HOU-075", "DFW-044"), ("HOU-072", "DFW-048"),
    ("HOU-132", "DFW-001"), ("HOU-167", "DFW-007"), ("HOU-023", "DFW-011"),
    ("HOU-013", "DFW-010"), ("HOU-009", "DFW-060"), ("HOU-012", "DFW-055"),
    ("HOU-008", "DFW-006"), ("HOU-025", "DFW-053"), ("HOU-024", "DFW-009"),
    ("HOU-014", "DFW-054"), ("HOU-166", "DFW-002"), ("HOU-133", "DFW-CH-001"),
    ("HOU-040", "DFW-CH-014"), ("HOU-146", "DFW-TR-074"), ("HOU-163", "DFW-TR-001"),
    ("HOU-156", "DFW-TR-040"), ("HOU-102", "DFW-TR-026"), ("HOU-142", "DFW-TR-032"),
    ("HOU-144", "DFW-TR-030"), ("HOU-141", "DFW-TR-031"), ("HOU-113", "DFW-TR-027"),
    ("HOU-160", "DFW-TR-060"), ("HOU-164", "DFW-TR-002"),
)


def apply(data, market):
    """Set the type on every card on the deck, and check the table covers it."""
    deck = [t for t in data["targets"] if t.get("group") != "out"]
    ids = {t["target_id"] for t in deck}
    prefix = "HOU-" if market == "hou" else "DFW-"
    listed = {k for k in TYPE if k.startswith(prefix)}
    missing = sorted(ids - listed)
    stray = sorted(listed - ids)
    if missing or stray:
        raise SystemExit("firm_types.py: cards with no type %s, types for cards not on the deck %s"
                         % (missing, stray))
    for t in deck:
        kind = TYPE[t["target_id"]]
        if kind not in LABEL:
            raise SystemExit("firm_types.py: %s has type %r" % (t["target_id"], kind))
        t["type"] = kind
    present = {t["type"] for t in deck}
    data["types"] = [[k, lab] for k, lab in TYPES if k in present]
    for a, b in SAME_FIRM:
        if TYPE[a] != TYPE[b]:
            raise SystemExit("firm_types.py: %s and %s are one firm with two types" % (a, b))
    return data
