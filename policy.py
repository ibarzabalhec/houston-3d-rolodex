"""Source rules shared by the builds and the gates.

A name, a title, a year or a figure never rests on an encyclopedia, a wiki or a
contact-data aggregator. This is the one list: build.py and build_dfw.py stop the
build when any of these appears in the data, and linkcheck.py and marketcheck.py
report any link to one. Before Build 86 there were three lists, and the Houston
build's was missing fourteen of the names the rules ban.

Each entry is matched as a substring of a lower-cased URL or string. The trailing
dot keeps an ordinary word in prose from matching a host.
"""

BANNED = (
    # encyclopedias and wikis
    "wikipedia.", "wikimedia.", "wikiwand.", "dbpedia.", "fandom.", ".wiki/", "wiki.",
    "everipedia.", "infogalactic.",
    # contact-data aggregators and resold company databases
    "zoominfo.", "rocketreach.", "apollo.io", "crunchbase.", "pitchbook.", "buzzfile.",
    "signalhire.", "lusha.", "leadiq.", "dnb.com", "bbb.org", "yelp.", "theorg.",
    "glassdoor.", "zippia.", "wiza.", "leadar.", "contactout.", "hunter.io", "clearbit.",
    "datanyze.", "owler.", "whitepages.", "spokeo.", "manta.com", "bizapedia.",
    "corporationwiki.", "buildzoom.", "houzz.",
)


def banned_in(text):
    """The first banned pattern found in `text`, or None."""
    low = (text or "").lower()
    return next((b for b in BANNED if b in low), None)
