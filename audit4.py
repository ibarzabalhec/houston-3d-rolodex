# -*- coding: utf-8 -*-
"""Round four: the cards that named their evidence and withheld the link.

Eighteen contacts on this deck carried a role string that was not a role. They
read "Owner, named on the firm's own about page" and "Listed under Senior
Leadership on the firm's own team page", and `source_url` was null on every one
of them. The card was telling a reader exactly where to check and then not
letting him. That is the same defect the outside reviewer caught in the Sources
block one level up, and it is worse on a card, because a reader who wants to
call someone has to find the page himself.

Five more cards named an outlet in prose and cited nothing. Westin, Colina,
Sitterle, First America and CastleRock each say Builder reports this or ranks
them that. None carried a builderonline.com link. The figures were right. They
were assertions anyway.

Fixing both meant opening every page. That is where the round earned itself,
because four of the eighteen claims did not survive their own page:

  Blazer's roster is on a page called Who We Are, not a team page, and it
  publishes no titles at all. Four people were carried with the sentence
  "Listed under Senior Leadership" standing in for a title. Each of the four has
  an individual bio page on the same site that gives a real one, including the
  business development seat, which is the single most useful line on the card
  and was not on it.

  T&T's about page never writes the strings Ryan Taylor, Jeff Taylor or Dianna
  Taylor. It names the founder C.A. Taylor and then uses first names. Three
  cards asserted a full name the page does not print.

  Silver Spur's owner was carried "after eighteen years selling ready-mix to the
  largest general contractors in Houston". That clause is on neither page the
  card cites. It is gone.

  Aura's chief executive was sourced to an Urban Land article that answers 403
  to every script, and the company's own site names nobody at all: eight pages
  fetched, zero occurrences of the surname. He is real, and a trade interview
  published by Marek Brothers out of AGC Houston's Cornerstone carries the exact
  title. That is the citation now.

And one of the five outlet claims was filed against the wrong page. First
America's firm page on builderonline.com does not say rank 75. It says rank 109,
because it has not been updated. Rank 75 is on the 2026 Builder 100 list itself.
Citing the firm page would have pointed a reader at a number that contradicts
the card.
"""

# ------------------------------------------------------------------- sources
# The outlet the prose already names. Each was opened and read, and the figures
# on the card were checked against the figures on the page before it went here.
#
#   Westin      1,062 closings and $621M in 2025, rank 60. On the page.
#   Colina      540 closings in 2025 and 552 in 2024. On the page.
#   Sitterle    372 closings and $210M in 2022, and 2022 is the last year the
#               page carries, which is what the card says about it.
#   First       rank 75, 750 closings, $197M, on the 2026 list, not the firm
#               page. See the note above.
#   CastleRock  1,465 closings, $617M, rank 49 for 2025.
#   Aura        the only readable page that carries the chief executive's title.
SOURCES = {
    "HOU-068": ["https://www.builderonline.com/firms/westin-homes/"],
    "HOU-064": ["https://www.builderonline.com/firms/colina-homes/"],
    "HOU-077": ["https://www.builderonline.com/firms/sitterle-homes/"],
    "HOU-007": ["https://www.builderonline.com/builder-100/builder-100-list/2026/"],
    "HOU-022": ["https://www.builderonline.com/firms/castlerock-communities/"],
    "HOU-126": ["https://www.marekbros.com/the-future-is-factory-built/"],
}

# ------------------------------------------------------------------ synopsis
# An exact substring, replaced once. build.py fails if the old text is not there
# or appears twice, so a silent miss is not possible. This is the mechanism the
# meta description needed and did not have for thirty builds.
SYNOPSIS = {
    "HOU-022": [(
        "Ranked 49th on the 2025 USA Top Builders list.",
        "Its own about page ranks it 49th on the 2025 USA Top Builders list. "
        "Builder records 1,465 closings and $617 million in 2025, rank 49 on "
        "the Builder 100.",
    )],
}

# -------------------------------------------------------------------- people
# (target, name) -> (role, page, what the page says)
#
# The role is a role again. The evidence sentence carries what the role string
# used to assert, and the page it asserts it from is one click away.
_BLAZER = "https://www.blazerbuilding.com/team/%s/"
_RINO = "https://rino-con.com/leadership/"
_TT = "https://tandtconstruction.com/about-us/"
_SATPON = "https://www.satpon.com/about/team/"
_EVER = "https://www.everlastinghomesgroup.com/"
_HC = "https://www.harveycleary.com/about-us/"
_BOT = "https://www.botellobuilders.com/"
_NAU = "https://www.nautiluscustomhomes.com/about-us"

PERSON = {
    ("HOU-120", "Matt Zetlmeisl"): (
        "Owner",
        "https://icfconstructors.com/about/",
        "The firm's own about page: owned and operated by Matt Zetlmeisl since 2002."),

    # Four people who had no title, on a firm whose roster page publishes none.
    # Every title below is from that person's own bio page on the same site.
    ("HOU-117", "Chris Richardson"): (
        "Founder",
        _BLAZER % "chris-richardson",
        "His own bio page on the firm's site: founded the company in 1978. The "
        "Who We Are page lists him under Senior Leadership."),
    ("HOU-117", "Chad Hillman"): (
        "President, Blazer Building Southwest",
        _BLAZER % "chad-hillman",
        "His own bio page: president of Blazer Building Southwest, over operations, "
        "project management, financial oversight and relationships with owners, "
        "developers, lenders and subcontractors. Before it, vice president of "
        "construction, general superintendent and superintendent."),
    ("HOU-117", "Matt Fuqua"): (
        "Business Development",
        _BLAZER % "matt-fuqua",
        "His own bio page: business development, affordable and conventional "
        "multi-family and active adult housing, over twenty years with Blazer."),
    ("HOU-117", "Brian Henderson"): (
        "Vice President of Construction",
        _BLAZER % "brian-henderson",
        "His own bio page: joined in 2014, served as assistant superintendent and "
        "superintendent, now vice president of construction. The Who We Are page "
        "lists him under both Senior Leadership and Construction Supervision."),

    # The leadership page answers 200 and ships none of the three names to a
    # script. It renders them from JavaScript, which is the same condition four
    # of the phone sites are in, and it is why probe.py needs the hand entry.
    ("HOU-114", "Steve Salverino"): (
        "Chief Executive Officer", _RINO,
        "The firm's own leadership page carries the title."),
    ("HOU-114", "Jacob Aswad"): (
        "President", _RINO,
        "The firm's own leadership page carries the title."),
    ("HOU-114", "Justin Henderson"): (
        "Vice President", _RINO,
        "The firm's own leadership page carries the title."),

    # The page prints one surname, the founder's, and first names after it. The
    # card said it printed three full names. It does not.
    ("HOU-109", "Ryan Taylor"): (
        "Third generation, assumed leadership in 2001", _TT,
        "The firm's own about page: C.A. Taylor started the firm in Pasadena in "
        "1969, his son Jeff joined and it became Taylor and Taylor, and Jeff's son "
        "Ryan joined in 1988 and assumed leadership in 2001. The page uses first "
        "names after the founder and does not print the surname beside Ryan."),
    ("HOU-109", "Jeff Taylor"): (
        "Second-generation co-owner", _TT,
        "The firm's own about page: Jeff and his wife Dianna continued the family "
        "business as co-owners. The page uses first names after the founder."),
    ("HOU-109", "Dianna Taylor"): (
        "Second-generation co-owner", _TT,
        "The firm's own about page: Jeff and his wife Dianna continued the family "
        "business as co-owners. The page uses first names after the founder."),

    ("HOU-107", "Victor Andrade"): (
        "Founder",
        "http://andradeconstructioncompanies.com/about-us/",
        "The firm's own about page: founded by Victor Andrade in 2003 in residential "
        "construction, into commercial in 2013."),

    # "after eighteen years selling ready-mix to the largest general contractors
    # in Houston" was in the role string and on neither page the card cites.
    ("HOU-110", "Trent Mitchell"): (
        "Owner",
        "https://www.silverspurconcrete.com/about-silver-spur-concrete-contractors/",
        "The firm's own about page names him as owner and lists ExxonMobil World "
        "Headquarters, the Texas Children's maternity ward and Baylor College of "
        "Medicine among his commercial and industrial work."),

    ("HOU-112", "Travis Boone"): (
        "Chief Executive Officer, Orion Group Holdings",
        "https://www.oriongroupholdingsinc.com/investors/press-release/2024/29-01-2024-120203346",
        "Quoted as chief executive in the firm's own release of 29 January 2024, "
        "announcing that TAS Concrete Construction would trade as Orion."),

    ("HOU-106", "Trey Green"): (
        "Senior Vice President, Self Perform Group, Satterfield and Pontikes",
        _SATPON,
        "The parent's own team page: he oversees the Self Perform group of Greco "
        "Structures, Rollcon, Rocket Pumping and Westway Construction."),
    ("HOU-106", "George A. Pontikes Jr."): (
        "Chief Executive Officer and Chairman, Satterfield and Pontikes",
        _SATPON,
        "The parent's own team page: he founded Satterfield and Pontikes with "
        "Tommy Satterfield in 1989."),

    ("HOU-126", "Rame Hruska"): (
        "Co-founder and Chief Executive Officer",
        "https://www.marekbros.com/the-future-is-factory-built/",
        "Quoted in AGC Houston's Cornerstone for winter 2025 to 2026, reposted 25 "
        "February 2026, as a co-founder and chief executive of Aura Dwellings and "
        "Hospitality. The company's own site names no one."),

    ("HOU-122", "Franck Boursier"): (
        "Chief Executive Officer and co-founder", _EVER,
        "The firm's own site carries him as chief executive and a founder in the "
        "business record it publishes."),
    ("HOU-122", "George Mock"): (
        "General Manager", _EVER,
        "The firm's own site carries him as general manager and a founder in the "
        "business record it publishes."),

    # Eight more the gate found that the review's list of eighteen had missed,
    # which is the argument for writing the gate rather than working the list.
    ("HOU-102", "David E. Harvey Sr."): (
        "Founder", _HC,
        "The firm's own about page: David E. Harvey, Sr. and Gerald D. Hines "
        "founded it in 1957, and Harvey was already a proponent of tiltwall."),
    ("HOU-102", "David Harvey Jr."): (
        "Took ownership in 1987", _HC,
        "The firm's own about page: he and Joseph Cleary both started at Harvey, "
        "in 1977 and 1976, and both took ownership in 1987, renaming it Harvey Cleary."),
    ("HOU-102", "Joseph Cleary"): (
        "Took ownership in 1987", _HC,
        "The firm's own about page: he and David Harvey, Jr. both took ownership "
        "in 1987, renaming Harvey Builders to Harvey Cleary."),

    ("HOU-104", "Eleazar Botello"): (
        "Founder", _BOT,
        "The firm's own site: founded in early 2007 by Eleazar, Eden and Jose "
        "Botello, starting in residential work."),
    ("HOU-104", "Eden Botello"): (
        "Founder", _BOT,
        "The firm's own site: founded in early 2007 by Eleazar, Eden and Jose "
        "Botello, starting in residential work."),
    ("HOU-104", "Jose Botello"): (
        "Founder", _BOT,
        "The firm's own site: founded in early 2007 by Eleazar, Eden and Jose "
        "Botello, starting in residential work."),

    ("HOU-125", "Ker Thomson"): (
        "Founder and Designer", _NAU,
        "The firm's own about page: in design and layout since the late 1990s, "
        "and in 2007 formed Nautilus's predecessor, Durable Residential Builders, "
        "out of a building-systems project with Texas A&M."),
    ("HOU-125", "Jim Kuchenbrod"): (
        "Construction lead", _NAU,
        "The firm's own about page: a navy veteran, in all aspects of residential "
        "construction for more than thirty-five years."),
}

# The roster page, where the card had none and the prose claimed one.
TEAM_URL = {
    "HOU-117": ("https://www.blazerbuilding.com/who-we-are/",
                "The roster is on the Who We Are page. It lists names under Senior "
                "Leadership and Construction Supervision and publishes no titles. "
                "Each name links to a bio page that does."),
    "HOU-114": ("https://rino-con.com/leadership/",
                "Three officers, with titles. The page renders its roster from "
                "script, so a fetch returns none of the names."),
    "HOU-109": ("https://tandtconstruction.com/about-us/",
                "A family history rather than a roster. It names the founder and "
                "then uses first names."),
    "HOU-110": ("https://www.silverspurconcrete.com/about-silver-spur-concrete-contractors/",
                "One name, the owner's."),
    "HOU-106": ("https://www.satpon.com/about/team/",
                "The parent's roster. Greco Structures publishes none of its own."),
    "HOU-102": (_HC, "A company history rather than a roster. It names the founders "
                     "and the two who bought the firm in 1987."),
    "HOU-104": (_BOT, "One line on the home page naming the three brothers who "
                      "founded it."),
    "HOU-125": (_NAU, "Two names, with paragraphs rather than titles."),
}
