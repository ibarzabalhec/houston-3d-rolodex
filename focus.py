# -*- coding: utf-8 -*-
"""Point each record at the product a printer can serve.

A record that opens with a quarter of a million square feet of office is telling
the reader about a business ICON does not sell into. What matters, in this order:
land and lots, single-family, repeating low-rise residential, one and two storey
shell. Everything else is a clause, and only where it says something about how the
firm builds.

Applied last, so it overrides whatever the layers below produced.
"""

# target_id -> replacement synopsis
SYNOPSIS = {

# The Mill was described twice, most of it office square footage. What ICON can
# serve here is 294 low-rise units on one site, and the CLT frame is the method
# evidence, not the office programme.
"HOU-006":
  "Houston investor-developer. The Landing at Aliana is 294 units on one Fort Bend "
  "site, opening summer 2027. The Mill at 2219 Canal Street is a six-acre East End "
  "redevelopment framed in cross-laminated timber, reported as one of Houston's "
  "first, with 340 apartments and 100,000 square feet of office and retail built "
  "around a preserved 1890s brick mill. Michael Hsu and EDI on design. Triten and "
  "Radom Capital are the same pair across the Heights packing-plant cluster, M-K-T "
  "and the Swift BLDG.",

# East River's residential is the part a printer touches. The office and retail
# square footage sizes the project and then gets out of the way.
"HOU-036":
  "Houston investment and development firm. East River is a 150-acre redevelopment "
  "of the former turning-basin site on Buffalo Bayou, broken ground August 26, 2021 "
  "and planned at 60 city blocks. Phase One is 26 acres and opens with The Laura at "
  "360 units, alongside 360,000 square feet of office and retail. Midway kept sole "
  "development control of East River and sold its interest in the Parkway Ventures "
  "joint venture to Parkway in December 2024. Rob Sigler's own feed carries "
  "mass-timber construction from Kirksey. Larry Sloan left in November 2023 and is "
  "now Chief Development Officer at Triten Real Estate Partners, also screened here.",

# A land seller. Lots and acres are the product; the retail square footage is one
# clause because it says what else sits inside the same masterplan.
"HOU-015":
  "Privately held land developer with more than 16 master-planned communities and "
  "over 23,000 paper lots in pipeline as of August 6, 2026. Developer of Austin "
  "Point in Rosenberg, roughly 14,000 planned homes on an acreage cited as both "
  "4,700 and 6,400 in different releases, announced September 22, 2023. Valley Ranch "
  "in Liberty County carries more than 2,000 single-family homes and 1,000 "
  "multifamily units alongside 2.55 million square feet of retail. John Winniford "
  "holds the title President, Homebuilding at Signorelli and is also president of "
  "First America Homes. Signorelli itself names a commercial-division construction "
  "manager and land-development managers.",

# The lot pipeline is the point, not the holding-company reorganisation. The mass
# timber building is here because it is the one thing this firm has done that bears
# on how a wall gets built.
"HOU-011":
  "NYSE-listed master-planned community developer, headquartered inside The "
  "Woodlands, running three Greater Houston communities: The Woodlands, Bridgeland "
  "at 11,500 acres in Cypress, and The Woodlands Hills at 2,000 acres in Conroe and "
  "Willis. It sells finished lots to builders and does not build houses. 1,802 "
  "residential acres remain across the three as of June 30, 2026: 1,142 at "
  "Bridgeland, 597 at The Woodlands Hills, 63 at The Woodlands, which it expects to "
  "sell out in 2031. Company-wide it sold 621 residential acres in 2025 at an "
  "average $890,000 an acre. Bridgeland sold 812 new homes in 2025, eleventh in the "
  "country. It developed One Bridgeland Green, Greater Houston's first mass timber "
  "office building, framed in dowel-laminated and cross-laminated timber with "
  "low-carbon concrete, topped out December 2024 and opened November 2025. Pershing "
  "Square took 46.9 percent in May 2025.",
# Ground-up single-storey retail is a shell a printer can put up. Medical office is
# not the lead.
"HOU-082":
  "Developer of ground-up retail and medical office in Katy, and joint-venture "
  "partner on the East Blocks conversion in EaDo. Its own site is a placeholder with "
  "no content, so this record comes from press coverage.",

# The ten EaDo blocks are the work. The industrial ground-up matters because it is a
# tilt shell the same firm commissions on its own.
"HOU-081":
  "Investment and development firm. East Blocks is ten contiguous EaDo blocks, "
  "513,000 square feet in phase one, a joint venture with Wile Interests designed by "
  "Gensler with SWA on landscape. It also builds ground-up industrial on its own "
  "account, so it commissions a new shell as well as converting one. Preston Luster "
  "is the senior construction manager on the team page, and the two managing "
  "principals are the decision layer.",

# An office-to-residential conversion is residential work, and it is also almost no
# new exterior wall. Both halves of that belong in the first sentence.
"HOU-038":
  "Employee-owned owner of the Niels Esperson and Mellie Esperson towers in downtown "
  "Houston, converting up to 100 apartments into the 1927 and 1941 buildings under a "
  "programme reported in 2023 at about $50 million. The work is interior: the "
  "exterior wall stays. The unit count is published only as up to 100.",
}

# target_id -> replacement screen line
SCREEN = {
"HOU-011":
  "1,802 residential acres left to sell across three communities, and it paid to put "
  "up Greater Houston's first mass timber office. It sells lots, so the builder buys "
  "the wall.",
}

# target_id -> replacement headline figure
KEY_STAT = {
"HOU-011": "1,802 residential acres left to sell",
}

# The Track record count asks whether a firm has ever paid for a new way of
# building. Howard Hughes financed, branded and opened Greater Houston's first mass
# timber office building, with low-carbon concrete in the same structure. That is
# the count, met. It does not move the firm up the deck: a land owner is placed by
# what it sells, not by what it holds, and it still sells lots.
SCORE = {
"HOU-011": {"innovation": 3},
}

# Builders selling inside each masterplan, as the community's own site lists them.
# For a land owner this is the record: it names who buys the wall on ground this
# firm controls.
BUILDERS = {
"HOU-011": ["Lennar", "Perry Homes", "David Weekley Homes", "Highland Homes",
            "Chesmar Homes", "Coventry Homes", "Century Communities, Inc.",
            "Beazer Homes", "Westin Homes", "Tri Pointe Homes", "Ravenna Homes",
            "Newmark Homes", "Partners in Building", "J. Patrick Homes",
            "Brightland Homes"],
}

CHANNEL_LINE = {
"HOU-011": "Bridgeland, The Woodlands and The Woodlands Hills, as each community's "
           "own builder page lists them.",
}

# (target_id, name) -> (role, source url, evidence)
PEOPLE = {
("HOU-011", "Stephen Sams"): (
    "Senior Vice President, Master Planned Communities, Residential Development, Houston Region",
    "https://www.bridgeland.com/the-howard-hughes-corporation-appoints-stephen-sams-as-senior-vice-president-mpc-of-residential-development-in-the-houston-region/",
    "Named in the firm's own April 2022 appointment release, reporting to Jim Carman "
    "and covering The Woodlands, Bridgeland and The Woodlands Hills. No later source "
    "confirms he still holds it."),
}

# people whose title on the record is out of date
RETITLE = {
("HOU-011", "Jim Carman"): "President, Texas Region",
}

# (target_id, name) -> the decider seat, and whether it is confirmed
DECIDER = {
("HOU-011", "Stephen Sams"): False,
}

# target_id -> extra projects, appended
PROJECTS = {
"HOU-011": [
  ("One Bridgeland Green",
   "20203 Bridgeland Creek Parkway, Cypress. Around 50,000 square feet over three "
   "storeys. Spruce-pine-fir lumber, dowel-laminated timber decking, cross-laminated "
   "timber shear walls, low-carbon concrete. Lake|Flato design, Kirksey architect of "
   "record, Tellepsen general contractor. Topped out December 12, 2024, opened "
   "November 2025.",
   "method_risk",
   "Greater Houston's first mass timber office building, developed by the land owner "
   "itself rather than by a tenant. The one documented case of this firm paying to be "
   "first with a structural system.",
   "https://www.bridgeland.com/news/howard-hughes-celebrates-topping-out-of-one-bridgeland-green-greater-houstons-first-mass-timber-office-building/"),
  ("Bridgeland",
   "11,500 acres in Cypress, Harris County. 1,142 residential acres remaining at June "
   "30, 2026. 177 acres sold in 2025. 812 new homes sold in 2025, eleventh nationally "
   "and third in Texas. Around 22,000 residents against 70,000 at buildout.",
   "repeatable",
   "The largest single block of unsold residential land on the deck, and the ground "
   "fifteen builders already screened here are buying lots on.",
   "https://www.sec.gov/Archives/edgar/data/1981792/000162828026053303/hhhsupplemental2q26.htm"),
  ("The Woodlands Hills",
   "About 2,000 acres in Conroe and Willis, Montgomery County, more than 4,500 "
   "residences planned. 597 residential acres remaining at June 30, 2026. Net new home "
   "sales up 34 per cent year over year in the second quarter of 2026.",
   "repeatable",
   "The fastest-growing of the three, and the one with the most land left per acre sold.",
   "https://www.sec.gov/Archives/edgar/data/1981792/000162828026053303/hhhsupplemental2q26.htm"),
],
}

# target_id -> extra sources
SOURCES = {
"HOU-011": [
  "https://www.sec.gov/Archives/edgar/data/1981792/000162828026053303/hhhsupplemental2q26.htm",
  "https://www.bridgeland.com/homes/builders-model-homes/",
  "https://thewoodlandshills.com/homes/home-builders/",
  "https://communities.howardhughes.com/regions/texas/",
  "https://communities.howardhughes.com/press-releases/summerlin-and-bridgeland-rank-among-top-15-best-selling-master-planned-communities-nationwide/",
],
}

# target_id -> the three reasons, in the order the counts are printed.
# Channel records carried marks with nothing behind them. That was survivable while
# every one of them read No on the third count, because an absence explains itself.
# Howard Hughes now reads Yes there, so all six get their reasons.
WHY = {
"HOU-011": (
  "Three communities on one metro's edge, 1,802 residential acres still to sell.",
  "It sells finished lots. The builder who buys them buys the wall.",
  "Financed and opened Greater Houston's first mass timber office building, with "
  "low-carbon concrete in the same structure."),

"HOU-015": (
  "More than 16 masterplans and over 23,000 paper lots in pipeline.",
  "It sells lots, but it owns First America Homes, and one president runs both.",
  "Nothing on record about how anything inside its communities is built."),

"HOU-039": (
  "Sunterra alone is 2,303 acres in Katy with fifteen builders inside it.",
  "It sells lots. Fifteen builders buy the wall.",
  "Nothing on record about construction method."),

"HOU-041": (
  "Towne Lake and The Highlands carry about 4,000 planned homes across 12 builders.",
  "It sells lots and does not pour walls.",
  "Publishes no construction-method content."),

"HOU-040": (
  "Fourteen concurrent Houston masterplans.",
  "It sells lots across all fourteen. The builders inside buy the wall.",
  "Publishes no construction-method content."),

"HOU-043": (
  "One Houston community, Elyson, at 3,600 acres in Katy.",
  "It sells lots, and the platform now sits inside Brookfield Residential.",
  "Nothing on record about construction method."),
}


# ---------------------------------------------------------------- evidence
# An evidence line under a name exists to say something the name, the title and
# the link do not already say: that a title is four years old, that the person
# sits at the parent rather than the division, that a figure came from their own
# post. It does not exist to narrate where a link came from. "Linked from
# conceptneighborhood.com/team, which lists him as Managing Partner, Projects and
# Finance" prints the title a second time and the URL a second time, under an icon
# that is already the URL.
#
# Returns True when a line is only the title restated, with or without a clause
# naming the page the icon already links to.
import re as _re


def _norm(s):
    return _re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


# Provenance is the sentence that says where a fact came from. The link beside
# the name already says that. These patterns cut the provenance out of an
# evidence line so that what is left can be tested: if the remainder is only the
# title again, the line says nothing the card does not already carry, and it goes.
_PROVENANCE = [
    # "linked from the team page which lists him as", "named on the about page as"
    _re.compile(r"^linked from [a-z0-9 ]*?(team|about|leadership|people|staff)[a-z0-9 ]*?"
                r" which lists (him|her|them) as "),
    _re.compile(r"^named (on|in) (the |its |their )?[a-z ]*?(page|release|listing|record)"
                r"( as| named| naming)? "),
    # "team page:", "about page lists him as", "executive team page lists her under X as"
    _re.compile(r"^(the )?(executive |management |corporate )?"
                r"(team|about|leadership|staff|people|management|officers|governance|"
                r"company|home|member|bio|board and staff)"
                r"( and [a-z]+)? page:? ?"
                r"(lists|names|gives|reads|carries|shows)? ?"
                r"(him|her|them)? ?(under [a-z ]+? )?(as )?"),
    # "the firm's own bio page.", "Meritage's own management page:", "Perry's own page:"
    _re.compile(r"^([a-z.&/ ]{1,26} s|the (firm|company|authority|association) s) own "
                r"[a-z ]*?(page|site|post|release|announcement|listing|record|bio):? ?"),
    _re.compile(r"^listed (first )?(under [a-z ]+? )?(as )?"),
    # trailing: "... on LGI's own management page", "... on the firm's own team page"
    _re.compile(r",? (on|per|from) ([a-z.&/ ]{1,26} s|the (firm|company|authority|"
                r"association|division) s|its|their) own [a-z ]*?"
                r"(page|site|release|announcement|listing|record)\.?$"),
    _re.compile(r",? (on|in|per) (the |its |their )?[a-z ]*?"
                r"(team|about|leadership|people|staff|management|officers|governance|"
                r"member|bio) [a-z]*? ?page\.?$"),
]


def _strip_provenance(e, name=""):
    """Cut the where-it-came-from clauses, and the person's own name with them."""
    if name:
        n = _norm(name)
        for part in ([n] + [p for p in n.split() if len(p) > 2]):
            e = _re.sub(r"\b" + _re.escape(part) + r"\b", " ", e)
        e = _re.sub(r"\s+", " ", e).strip()
    changed = True
    while changed:
        changed = False
        for pat in _PROVENANCE:
            e2 = pat.sub("", e).strip(" ,.")
            if e2 != e:
                e, changed = e2, True
    return e


_STOP = {"the", "a", "an", "of", "and", "on", "at", "in", "for", "to", "s",
         "his", "her", "their", "its", "as", "with"}


def _tok(s):
    return [w for w in s.split() if w not in _STOP]


def restates_title(evidence, role, name=""):
    """True when the line, stripped of provenance, is only the title again."""
    e, r = _norm(evidence), _norm(role)
    if not e or not r:
        return False
    e = _strip_provenance(e, name)
    if not e:
        return True
    et, rt = _tok(e), _tok(r)
    if not et:
        return True
    es, rs = set(et), set(rt)
    if es <= rs:
        return True
    if rs <= es and len(et) - len(rt) <= 2:
        return True
    # "AP and Purchasing Manager" against "Accounts Payable and Purchasing
    # Manager": short, and almost all of it is the title.
    return len(et) <= 6 and len(es & rs) >= 0.6 * len(es)