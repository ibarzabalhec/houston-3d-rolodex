# -*- coding: utf-8 -*-
"""The figures behind the market view.

Everything here is a published number with a source. Where a firm publishes a
range, both ends are kept. Where a firm publishes nothing, it is absent from
the chart and the caption says how many that is. No figure is estimated.
"""

# target_id -> (low, high, year, source). low == high for a single figure.
CLOSINGS = {
    "HOU-068": (1062, 1062, 2025, "Builder 100, 2026 list"),
    "HOU-065": (973, 973, 2025, "HousingWire"),
    "HOU-007": (750, 750, 2025, "Stated by the outgoing purchasing lead, two markets"),
    "HOU-064": (540, 540, 2025, "Builder 100 firm page"),
    "HOU-069": (483, 483, 2025, "Builder 100 firm page"),
    "HOU-077": (372, 372, 2022, "Builder 100 firm page, company-wide"),
    "HOU-074": (324, 324, 2022, "As Devon Street Homes, before the sale"),
    "HOU-072": (300, 300, 2026, "The firm's own site, Texas and Tennessee"),
    "HOU-063": (195, 195, 2022, "Builder 100 firm page"),
    "HOU-060": (150, 200, 2026, "The firm's own site"),
    "HOU-066": (40, 60, 2026, "The firm's own site"),
    "HOU-061": (45, 45, 2025, "The firm's own site; 70 planned for 2026"),
    "HOU-071": (75, 75, 2026, "The firm's own site, about seventy-five a year"),
}

# The machine-fit bands, as stated in the method note.
BANDS = [(25, 400, "One or two printers"), (400, 1500, "A line inside the business")]

# Printed homes in Texas on the public record: (project, place, printer, units, status)
PRINTED = [
    ("Wolf Ranch", "Georgetown", "ICON, with Lennar", 100, "Completed 2025"),
    ("Community First! Village", "Austin", "ICON", 100, "Programme"),
    ("Zuri Gardens", "Houston", "HiveASMBLD, for Cole Klein", 80, "Under way"),
    ("Gulf Shore Estates", "San Leon", "HiveASMBLD, for Commander", 23, "23 of 26 printed"),
    ("Avenue J", "Houston", "HiveASMBLD, for Elpis", 2, "One duplex"),
    ("Spring Branch house", "Houston", "PERI, on a COBOD printer", 1, "Paused for months"),
    ("Sunconomy eco-village", "Montgomery", "Apis Cor", 0, "Announced 2019, unbuilt"),
]

# The field in time: (year, month, label, kind). kind: "in" for an entry or launch,
# "out" for a closure, sale or filing, "icon" for ICON's own record.
TIMELINE = [
    (2017, 1, "SQ4D prints its first unit, Long Island", "in"),
    (2019, 6, "Sunconomy eco-village announced, Montgomery", "in"),
    (2022, 6, "Hive3D founded, Houston", "in"),
    (2022, 11, "Lennar and ICON announce Wolf Ranch, 100 homes", "icon"),
    (2024, 1, "HiveASMBLD formed from Hive3D and ASMBLD", "in"),
    (2024, 3, "D.R. Horton invests in Apis Cor", "in"),
    (2024, 12, "Diamond Age closes, 15 of 43 homes unfinished", "out"),
    (2025, 1, "Mighty Buildings put up for sale", "out"),
    (2025, 6, "Wolf Ranch completed", "icon"),
    (2025, 7, "CRH buys Eco Material, HiveASMBLD's cement supplier", "in"),
    (2025, 7, "ICON prints at Mueller, Austin", "icon"),
    (2025, 12, "Black Buffalo files Chapter 11", "out"),
    (2026, 9, "Titan training, third quarter", "icon"),
    (2027, 1, "Titan deliveries begin", "icon"),
]
