# -*- coding: utf-8 -*-
"""One main line per firm, and every other number its own pages publish.

The deck carried 106 firms and 273 named people and no way to dial any of them.
This is the number layer. Every entry was read off a page the firm publishes,
and `phonecheck.py` re-fetches each page and asks whether the digits are in the
bytes before a build ships.

Why a main line is designated by rule rather than by eye. The first sweep over
this deck took the first number on each page and would have published four
wrong: MAREK's residential fax, Read King's fax, Braun's fax and Kendall's fax,
because a fax sits next to a phone and a regex cannot tell them apart. The rules
below are applied in order, the first that fits wins, and the rule used is
recorded on the record so a reader can see which one did the work.

    1  the page publishes exactly one number
    2  a tel: href sits in the site header or footer, on every page
    3  the page labels it main, office, corporate, general or headquarters
    4  it is the only Houston-area line among several
    5  none of the above, so no main line is designated

Rule 5 is the important one. A firm that publishes four community sales lines
and calls none of them the main line gets no main line here either. The card
prints the directory and says the page designates none. Guessing which of four
is the front door is exactly the kind of quiet judgment the audit rounds kept
finding, and it leaves no trace when it is wrong.

A fax is captured as a fax and is never a main line. A number published beside a
named person is captured with the words the page uses, not with a title invented
for it.

Nothing here comes from a contact aggregator. `build.py` sweeps every string in
the build for those hosts and exits on a hit, and `linkcheck.py` sweeps a wider
list still, which matters because a phone search returns whitepages and spokeo
before it returns the firm.

    PHONE   tid -> (digits, label, source_url, rule)   the main line
    MORE    tid -> [(digits, label), ...]              everything else published
    NOTE    tid -> one sentence about what else the page carries
    ABSENT  tid -> what was looked at, and what was on it
"""

# ---------------------------------------------------------------- main lines

PHONE = {
    # ---- rule 1, the page publishes one number and that is the end of it
    "HOU-005": ("7137834444", None, "https://www.radomcapital.com/", 1),
    "HOU-006": ("8322145000", None, "https://www.tritenre.com/", 1),
    "HOU-007": ("7138978986", None, "https://www.firstamericahomes.com/", 1),
    "HOU-011": ("2819297700", None, "https://www.howardhughes.com/contact/", 1),
    "HOU-015": ("7134521700", None, "https://www.signorellicompany.com/", 1),
    "HOU-019": ("7133542500", None, "https://www.camdenliving.com/", 1),
    "HOU-022": ("7136007000", None, "https://www.c-rock.com/", 1),
    "HOU-028": ("7139613588", None, "https://suebausa.com/", 1),
    "HOU-029": ("7132672100", None, "https://www.hanoverco.com/", 1),
    "HOU-030": ("7136236800", None, "https://www.frpltd.com/", 1),
    "HOU-035": ("7138648099", None, "https://avenuecdc.org/", 1),
    "HOU-036": ("7136295200", None, "https://www.midway.team/contact", 1),
    "HOU-039": ("7137836702", None, "https://landtejas.com/", 1),
    "HOU-040": ("7139609977", None, "https://www.johnsondevelopment.com/", 1),
    "HOU-042": ("2818751552", None, "https://friendswooddevelopment.com/contact-us", 1),
    "HOU-048": ("7136211700", None, "https://www.wulfe.com/", 1),
    # Build 65: the homepage replaced its 888 line with this one. It is the only
    # number on the page and it is also the tel: link in the header.
    "HOU-061": ("9362994373", None, "https://www.myaltahomes.com/", 1),
    "HOU-067": ("7137898004", None, "https://www.jpatrickhomes.com/", 1),
    "HOU-071": ("8328580755", None, "https://jamestownestatehomes.com/", 1),
    "HOU-073": ("5123346775", None, "https://www.brohnhomes.com/", 1),
    "HOU-080": ("7138217052", None, "https://www.conceptneighborhood.com/", 1),
    "HOU-081": ("7138044000", None, "https://www.pagewood.com/", 1),
    "HOU-105": ("8326636800", None, "https://www.encoreconcrete.com/", 1),
    "HOU-107": ("2812278225", None, "https://andradeconstructioncompanies.com/", 1),
    "HOU-109": ("7134776660", None, "https://tandtconstruction.com/", 1),
    "HOU-110": ("7134827712", None, "https://silverspurconcrete.com/", 1),
    "HOU-112": ("7138526500", None, "https://www.oriongroupholdingsinc.com/", 1),
    "HOU-117": ("7139149200", None, "https://www.blazerbuilding.com/", 1),
    "HOU-123": ("3462122153", None, "https://www.tionahomes.com/", 1),
    "HOU-125": ("8322657353", None, "https://www.nautiluscustomhomes.com/", 1),
    "HOU-126": ("8322243603", None, "https://www.auradwellings.com/", 1),
    "HOU-128": ("7137777368", None, "https://www.boxerproperty.com/", 1),
    "HOU-129": ("2818708727", None, "https://cive.com/", 1),
    "HOU-136": ("2814076466", None, "https://www.clayresidential.com/", 1),

    # One number, and the page says what it is for. The label is the page's
    # word, not a description of it. Century's only published number is the
    # warranty desk, and saying so is more use to a caller than calling it a
    # main line would be.
    "HOU-008": ("8336846527", "warranty",
                "https://www.meritagehomes.com/company/contact", 1),
    "HOU-009": ("8888855653", "warranty service",
                "https://www.centurycommunities.com/", 1),
    "HOU-013": ("8002473779", None, "https://www.perryhomes.com/contact-us", 1),
    "HOU-023": ("8447773717", None, "https://www.davidweekleyhomes.com/", 1),
    "HOU-113": ("8005392224", "headquarters", "https://bakerconstruction.com/", 1),
    "HOU-020": ("9723854100", "Dallas office", "https://provident.net/", 1),
    "HOU-133": ("2144490914", "Dallas office",
                "https://www.hillwoodcommunities.com/", 1),
    "HOU-118": ("8133976100", None, "https://leolaconstruction.com/houston/", 1),
    # The only number on the site sits in the privacy notice, as the number to
    # call to make a request. That is where it was found and that is what it says.
    "HOU-026": ("4804288994", "published in the privacy notice",
                "https://www.christophertodd.com/", 1),
    "HOU-065": ("9792004552", "office", "https://www.stylecraft.com/", 1),
    "HOU-069": ("7133460200", "office", "https://newmarkhomes.com/", 1),
    "HOU-103": ("2814059557", "office", "https://www.texasamconcrete.com/", 1),
    "HOU-124": ("4092564888", "office", "https://seaside-construction.com/", 1),
    "HOU-135": ("3462630547", None, "https://www.tilsonhomes.com/", 1),
    "HOU-010": ("8882349451", None, "https://www.camillocompanies.com/", 1),
    "HOU-130": ("8884986815", None, "https://www.longlakeltd.com/", 1),
    "HOU-037": ("7139939823", "office", "https://www.dealco.net/", 1),

    # ---- rule 2, a tel: href in the header or the footer, so on every page
    "HOU-001": ("7132199400", "corporate", "https://wanbridge.com/", 2),
    "HOU-068": ("2812401551", None, "https://www.westin-homes.com/", 2),
    "HOU-108": ("8329307739", None, "https://htxconcrete.com/", 2),
    "HOU-041": ("7136900000", "Houston and Cypress", "https://caldwellcos.com/", 2),
    "HOU-101": ("7139838002", "Houston", "https://www.keystoneconcrete.com/", 2),

    # ---- rule 3, the page labels it
    "HOU-060": ("2814825864", "office", "https://www.cervellehomes.com/", 3),
    "HOU-072": ("7139371121", "Houston office, corporate",
                "https://partnersinbuilding.com/", 3),
    "HOU-066": ("7138649190", "main", "https://www.sandcastlehouston.com/", 3),
    "HOU-063": ("2816098310", None, "https://kendallhomes.net/", 3),
    "HOU-119": ("7136811100", "office", "https://www.mldeer.com/", 3),
    "HOU-120": ("8322646282", "office", "https://icfconstructors.com/", 3),
    "HOU-114": ("2812070700", "Houston, at Katy", "https://rino-con.com/", 3),
    "HOU-083": ("7135410066", None, "https://braunenterprises.com/", 3),
    "HOU-004": ("7139613877", None, "https://intownhomes.com/", 3),
    "HOU-031": ("7137829000", None, "https://read-king.com/", 3),
    "HOU-047": ("7136212900", None, "https://bakerkatz.com/", 3),
    "HOU-038": ("7132241663", None, "https://cameronmanagement.com/contact", 3),
    "HOU-111": ("2812727900", None, "https://www.bcshouston.com/", 3),
    "HOU-106": ("7133752380", None, "https://grecostructures.com/contact/", 3),
    "HOU-104": ("2817843070", None, "https://www.botellobuilders.com/contact-us/", 3),
    # The corporate-info page gives the head office a street address in
    # Alpharetta and one number. The homepage gives a number per selling
    # community and none for the company.
    "HOU-024": ("7709989663", "corporate headquarters, Alpharetta, Georgia",
                "https://www.ashtonwoods.com/corporate-info", 3),

    # ---- read in a browser, because the host answers a script with a stub, a
    # 403, or a page that builds itself from JavaScript. VERIFIED below carries
    # the date and what was on the screen.
    "HOU-018": ("2814774300", "contact, corporate headquarters",
                "https://www.newquest.com/contact-us/", 1),
    "HOU-070": ("8326533600", None, "https://www.ravennahomes.com/", 1),
    "HOU-075": ("8888274421", None, "https://risewellhomes.com/", 2),
    "HOU-076": ("8665102449", None, "https://imaginationhomes.com/", 2),
    "HOU-116": ("2813135055", "Houston office",
                "https://burtonconstruction.com/", 4),
    # brightlandhomes.com now serves a DRB Homes customer-care page with no
    # number on it. DRB's own contact page gives the Houston office a street
    # address on West Sam Houston Parkway and this line.
    "HOU-034": ("2812016961", "Houston office, published by DRB Homes",
                "https://www.drbhomes.com/drbhomes/contact/contact-us", 3),
    "HOU-074": ("8775523727", None, "https://www.smithdouglas.com/", 2),
    "HOU-062": ("7134897738", "the Westway Park office",
                "https://www.tricoasthomes.com/", 3),
    "HOU-134": ("8447672713", "main office, Baton Rouge",
                "https://www.dsldhomes.com/", 3),

    # ---- rule 4, the only Houston-area line among several
    "HOU-033": ("7139032596", "Houston", "https://www.coventryhomes.com/connect/", 4),
    "HOU-077": ("2816647255", "Houston design studio",
                "https://sitterlehomes.com/contact/", 4),
    "HOU-115": ("7135331900", "Houston", "https://www.arch-con.com/contact-us/", 4),
    "HOU-122": ("2819159791", "Greater Houston",
                "https://www.everlastinghomesgroup.com/", 4),
    # Commercial and residential each publish a phone and a fax at their own
    # address. The commercial branch is the one that builds walls.
    "HOU-121": ("7136812626", "commercial, Judiway Street",
                "https://www.marekbros.com/houston/", 3),
}

# ---------------------------------------------------------------- rule 5

# The page publishes several numbers and designates none of them the main line.
# Nothing is picked. The card prints the directory and says so.
NO_MAIN = {
    "HOU-131": "https://www.caldwellhomes.com/",
    "HOU-132": "https://www.drhorton.com/contact-us-page",
    "HOU-025": "https://www.taylormorrison.com/contact-us",
}

# ---------------------------------------------------------------- the rest

# Every other number the same page publishes, with the words the page gives it.
# Where no label can be read, none is written. The point of keeping these is
# that a wrong pick of main line above costs a reader one click instead of
# being invisible.
MORE = {
    "HOU-060": [("7138764219", "Pedregal sales, Kathi"),
                ("2817946106", "Pedregal sales, Susan"),
                ("7138990437", "Pedregal sales, Chris"),
                ("2817487450", "Pedregal sales, Pam")],
    "HOU-072": [("9793378293", "Brazos Valley office and model"),
                ("4699023200", "Dallas and Fort Worth office"),
                ("9727327800", "Dallas and Fort Worth office"),
                ("6154864003", "Nashville office")],
    "HOU-131": [("2816646776", "Chambers Creek"),
                ("2813783364", "Towne Lake"),
                ("7137706066", "The Highlands"),
                ("9794315544", "Mission Ranch")],
    "HOU-132": [("8323445000", "Houston Central and Houston Southeast, Richmond"),
                ("9367776600", "Houston North, Conroe"),
                ("2815662100", "Houston Southwest, Richmond"),
                ("9367776656", "fax, Houston North"),
                ("9793930810", "Brazos Valley, College Station")],
    "HOU-033": [("7373874393", "Austin"),
                ("9723668789", "Dallas and Fort Worth"),
                ("2107916860", "San Antonio")],
    "HOU-077": [("2104629050", "San Antonio design studio"),
                ("5124560963", "Austin design studio"),
                ("2108175948", None)],
    "HOU-101": [("5129313033", "Austin"),
                ("2106514055", "San Antonio"),
                ("8667944385", None)],
    "HOU-121": [("7136816540", "fax, commercial"),
                ("7136819213", "residential, Piney Woods Drive"),
                ("7136810446", "fax, residential")],
    "HOU-122": [("3104646046", "Greater Los Angeles"),
                ("8665597456", "toll free")],
    "HOU-114": [("2812070707", "fax, Houston"),
                ("5123993026", "Austin and Central Texas")],
    "HOU-115": [("2144207900", "Dallas"),
                ("5125068000", "Austin")],
    "HOU-001": [("2816537948", "leasing")],
    "HOU-004": [("7134261156", "fax")],
    "HOU-068": [("2812403252", "fax")],
    "HOU-063": [("2813984011", "fax")],
    "HOU-066": [("2815436360", "sales")],
    "HOU-120": [("2813983806", "fax")],
    "HOU-104": [("2817910117", None)],
    "HOU-106": [("2819550311", None)],
    "HOU-111": [("2814478100", None)],
    "HOU-119": [("7136811114", "fax")],
    # The same seven digits appear a second time on the page behind a 936
    # prefix. Both strings are in the bytes, so both are here.
    "HOU-108": [("9369307739", "as printed elsewhere on the same page")],
    "HOU-038": [("7133330811", "published beside the chief operating officer")],
    "HOU-062": [("9362364896", "call today, beside a named consultant")],
    "HOU-025": [("2815983000", "Houston, customer care"),
                ("2816198241", "Houston, online sales manager")],
    "HOU-116": [("5125381520", "Austin office"),
                ("2104688241", "San Antonio office"),
                ("6026105100", "Phoenix office")],
    "HOU-083": [("7135410661", "fax")],
    "HOU-041": [("9792607000", "College Station")],
    "HOU-031": [("7137829522", "fax")],
    "HOU-047": [("7136212999", "fax")],
}

# ---------------------------------------------------------------- notes

# Where the page carries more than a directory can usefully hold, the count says
# it instead of a list. A reader who wants a specific community office has the
# link.
NOTE = {
    "HOU-024": "The homepage publishes a separate number for each selling "
               "community, fifteen of them in the Houston area, and none for "
               "the company.",
    "HOU-025": "The contact page gives each division an office address and two "
               "numbers under those two headings. The Houston office is on "
               "Briarpark Drive.",
    "HOU-134": "The footer lists a regional office in each state the builder "
               "operates in. Texas is served from the Baton Rouge main office, "
               "on this same number.",
    "HOU-034": "brightlandhomes.com now serves a DRB Homes customer care page, "
               "which publishes no number.",
    "HOU-132": "The contact page lists a division office in every state the "
               "builder operates in. The Houston entries are above.",
}

# ---------------------------------------------------------------- absences

# A record with no number, and what was looked at to establish that. A blank
# field says nothing. These say what was on the page.
ABSENT = {
    "HOU-127": "The site answers a browser with the same 401 it answers a "
               "script with. Nothing on it can be read.",
    "HOU-064": "The contact page publishes a street address, an email address "
               "and a form. It publishes no number.",
    "HOU-082": "The site is a placeholder. The whole page reads Coming Soon.",
    "HOU-043": "newlandco.com redirects to Brookfield Residential Land. That "
               "site's own contact page publishes an enquiry form and no number.",
    "HOU-045": "The contact page describes a three-step consultation and ends "
               "in a form. It publishes no number.",
    "HOU-044": "The contact page publishes a Chicago street address and a form. "
               "It publishes no number.",
    "HOU-102": "The contact page names five offices, Houston among them, and "
               "gives a form and no number for any of them.",
    "HOU-014": "Neither the homepage nor the customer care page publishes a "
               "number. Every enquiry routes through a form.",
    "HOU-012": "The homepage publishes no number and sends enquiries to each "
               "community's own page.",
    "HOU-027": "The contact page offers a help centre and an email address for "
               "the chief executive. It publishes no number.",
    "HOU-021": "The contact page publishes an enquiry form and no number.",
    # No page on the card to read a number off. The first four have no web
    # presence at all and stand on dated reporting; the last two are named
    # inside someone else's release or on a page that renders nothing.
    "HOU-002": "The firm's own site publishes no number on any page the card "
               "cites.",
    "HOU-016": "The firm publishes no website. Everything on this card comes "
               "from dated reporting.",
    "HOU-017": "The firm publishes no website. Everything on this card comes "
               "from dated reporting.",
    "HOU-003": "The authority's own leadership page stopped resolving, and the "
               "card stands on dated reporting that carries no number.",
    "HOU-078": "The builder is named inside its acquirer's release. It has no "
               "site of its own on this card.",
    "HOU-032": "The one page the card cites returns nothing to a script, and "
               "in a browser it redirects off the firm's own domain.",
}

# Pages a script cannot read that were opened in a browser by hand, with the
# date and what was on them. Same discipline as probe.VERIFIED: a host that
# answers 403 to urllib is not evidence of anything either way.
VERIFIED = {
    "https://burtonconstruction.com/":
        "2026-09-13: four offices, each with a Tel. Houston 281-313-5055, "
        "Austin 512-538-1520, San Antonio 210-468-8241, Phoenix 602-610-5100.",
    "https://www.newquest.com/contact-us/":
        "2026-09-13: one number, (281) 477-4300, under Contact Info and again "
        "in the footer beside the corporate headquarters address.",
    "https://www.ravennahomes.com/":
        "2026-09-13: one number, 832-653-3600, in the footer beside the "
        "Cypress address, as text and as a tel: link.",
    "https://risewellhomes.com/":
        "2026-09-13: no number in the visible text. One tel: link, "
        "888-827-4421.",
    "https://imaginationhomes.com/":
        "2026-09-13: one number, 866-510-2449, in the footer, as text and as "
        "a tel: link.",
    "https://www.drbhomes.com/drbhomes/contact/contact-us":
        "2026-09-13: a division office per state, each with an address and a "
        "number. Houston and College Station share 2050 W Sam Houston Pkwy S., "
        "Suite 1600, on 281.201.6961.",
    "https://www.tricoasthomes.com/":
        "2026-09-13: the footer reads Tricoast Homes, 4601 Westway Park, "
        "Houston, TX 77041, Phone: (713) 489-7738. A second number, "
        "(936) 236-4896, sits above it beside a named consultant.",
    "https://www.smithdouglas.com/":
        "2026-09-13: 877-552-3727, in the header as Get In Touch and again as "
        "a Call Now button, on every page.",
    "https://landtejas.com/":
        "2026-09-14: the site stopped answering scripts between builds. In a "
        "browser it loads and carries one tel: link, 713-783-6702.",
    "https://www.taylormorrison.com/contact-us":
        "2026-09-13: a block per division, each with an email address, an "
        "Online Sales Manager number and a Customer Care number. Houston, at "
        "3250 Briarpark Drive Suite 300, reads 281-619-8241 and 281-598-3000. "
        "Neither is called the main line.",
    "https://www.dsldhomes.com/":
        "2026-09-13: the footer lists an office per state. DSLD Homes Main "
        "Office, 7660 Pecue Lane, Baton Rouge, PH 844.767.2713, and the Texas "
        "entry gives the same address and the same number.",
}
