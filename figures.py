# -*- coding: utf-8 -*-
"""Is the number on any page the card cites for it?

probe.py asks that question about names. This asks it about figures, which is
the other place a model invents things and the harder one to catch by reading,
because a wrong number looks exactly like a right one.

Four inventions were found by hand in one audit round, each of which had
survived every earlier read: a build-to-rent operator credited with "156 units
inside a single masterplan" when no source anywhere carries that number, a
builder with a catalogue of "eighty-two plans" that neither cited page states, a
firm with "195 closings in 2022, the latest published" whose only source
publishes no annual figure at all, and a builder selling across "more than twenty
communities" whose own communities page lists fourteen.

This tests all of them at once. For every card, take every figure it prints,
fetch every page it cites, and ask whether the figure is in the bytes. A figure
on none of its own card's pages is one of three things, and all three are
findings:

  invented   nothing published it and the card asserts it
  derived    the card did arithmetic and presented the result as published
  uncited    a real figure whose source is not on the card, so no reader can
             follow it

The script cannot tell those apart. A person reading the card and the page can,
in about thirty seconds, which is the point: it turns an unbounded re-read into
a short list.

    python3 figures.py              every card
    python3 figures.py HOU-011      one card

What it deliberately does not flag: years, ordinals under 13, and anything the
card already labels as an assumption. Years are noise because every page is full
of them. Small integers are noise because "three communities" matches any page
with a three on it.
"""
import html as _html
import json, pathlib, re, ssl, sys, urllib.error, urllib.request
import concurrent.futures as cf

ROOT = pathlib.Path(__file__).parent
CACHE = ROOT / "internal" / "figures_pages.json"

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,*/*"}
CTX = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")

SKIP_HOST = ("linkedin.com",)

# A figure this size is in every page on the web. Below the floor it is noise.
FLOOR = 13
# Years are on every page ever published.
YEAR = re.compile(r"^(19|20)\d\d$")

NUM = re.compile(r"""
    \$?                          # optional currency
    \d{1,3}(?:,\d{3})+           # 1,234 or 1,234,567
  | \$?\d+(?:\.\d+)?\s*(?:million|billion|percent|%)   # 4.7 million, 17 percent
  | \$?\d{2,}                    # bare integer of two digits or more
""", re.X | re.I)

# Numbers the deck writes as words, which a page may write as digits.
WORDS = {
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "twenty-one": 21, "twenty-two": 22, "twenty-three": 23, "twenty-four": 24,
    "twenty-five": 25, "twenty-six": 26, "twenty-eight": 28, "thirty": 30,
    "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "seventy-five": 75,
    "eighty": 80, "eighty-two": 82, "ninety": 90, "hundred": 100,
}


def flatten(body):
    s = body.decode("utf-8", "replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = _html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"\s+", " ", s)


# Pages that answer a script 403 and a browser the full page, read by hand, with
# the figures that were on them. Without this the five Builder firm pages added
# in Build 60 read as unfetchable, so every closing figure on those cards kept
# counting as unsourced after it had been sourced. A page here is treated as read
# and its text is the text below, which is deliberately only the figures: this is
# a record of what was checked, not a cache of the page.
BYHAND = {
    # Build 80. Read on 2026-09-25 with a fetcher the site allows; scripts are refused.
    "https://houstonagentmagazine.com/2026/08/17/kresston-mpc-60-80-foot-homesites/":
        "2026-09-25: 17 August 2026. J. Patrick Homes and Toll Brothers will build on 31 80-foot lots.",
    "https://www.globenewswire.com/news-release/2026/08/05/3339652/0/en/howard-hughes-holdings-inc-reports-second-quarter-2026-results.html":
        "2026-09-25: release of 5 August 2026. Completed the acquisition of 100% of Vantage Group Holdings for "
        "cash consideration of approximately $2.1 billion on June 4, 2026. Issued and sold $1.0 billion of Series A "
        "Non-Voting Exchangeable Perpetual Preferred Stock to an affiliate of Pershing Square. Sold Creekside Park "
        "and Creekside Park The Grove in The Woodlands for $127.3 million.",
    "https://www.multihousingnews.com/tricon-completes-texas-single-family-rentals/":
        "2026-09-24: 4 April 2025. Tricon Peek Road, developed in a partnership with "
        "Johnson Development and HHS Residential, comprises 175 new single-family homes "
        "in Katy. Tricon Trinity Falls, 126 homes in McKinney, also with HHS Residential.",
    "https://www.pultegroupinc.com/investor-relations/news/news-details/2022/Del-Webb-Opens-Third-Houston-Area-Community-Del-Webb-Fulshear/default.aspx":
        "2026-09-24: release of 6 October 2022. Del Webb Fulshear opens 8 October 2022, "
        "the third Del Webb community in the Houston area. Lindy Oliva, President of "
        "PulteGroup's Houston Division.",
    "https://www.pultegroupinc.com/investor-relations/news/news-details/2024/PulteGroup-Breaks-Ground-on-New-Master-Planned-Ryehill-Communities-in-Sugar-Land/default.aspx":
        "2026-09-24: release of 3 July 2024, Ryehill, Sugar Land, about 2,500 homes "
        "across Ryehill and Del Webb Sugar Land. Lindy Oliva, Houston Division President.",
    # Build 65. Read through a separate fetcher on 2026-09-24; builderonline
    # refuses this script. The whole table, so every card that cites it can be
    # checked against the same text.
    "https://www.builderonline.com/land/local-leaders-list/2026/houston-pasadena-the-woodlands-tx/":
        "2026-09-24: 2026 Local Leaders, Houston-Pasadena-The Woodlands, TX. 2025 "
        "closings and 2025 market share. 1 Lennar Corp. 6,362 17.0%. 2 D.R. Horton "
        "4,925 13.1%. 3 Perry Homes 1,809 4.8%. 4 Meritage Homes 1,428 3.8%. 5 "
        "PulteGroup 1,146 3.1%. 6 Ashton Woods Homes 1,115 3.0%. 7 Sekisui House U.S. "
        "1,087 2.9%. 8 Dream Finders Homes 1,048 2.8%. 9 Century Communities 1,017 "
        "2.7%. 10 Highland Homes 968 2.6%. Top ten: 20,905 closings, 55.7%.",
    # Build 67. Each read on 2026-09-24 through a separate fetcher, because this
    # script is refused, is served a Cloudflare challenge, or cannot see text that
    # a page renders from script or prints in an image label. Only the figures and
    # the words around them are recorded.
    "https://houstonagentmagazine.com/2026/03/19/m-i-homes-meritage-homes-trinity-landing/":
        "2026-09-24: 19 March 2026. M/I Homes and Meritage Homes closed on 309 acres "
        "along Highway 90 in Dayton for Trinity Landing. Plans for the community include "
        "1,000 homes on 45-, 50- and 60-foot lots. Trinity Landing is M/I Homes' third "
        "land purchase in the past six months.",
    "https://www.homes.com/news/houstons-3d-printed-housing-push-grows-with-two-new-developments/647676272/":
        "2026-09-24: ranging in size from about 1,000 to 2,100 square feet. Prices will "
        "range from the low $200,000s to about $385,000. Each residence in the duplex will "
        "be about 1,727 square feet. Pricing for each unit is $365,000.",
    "https://brundagebone.com/locations/houston/":
        "2026-09-24: Concrete Boom Pumps (17m - 65m). Two Houston addresses. All "
        "operators are OSHA 10 and ACPA certified.",
    "https://wells.build/contact/locations/hillsboro-texas/":
        "2026-09-24: 102K combined sq ft facility. 320+ team members. 30+ projects each "
        "year. AA architectural certification.",
    "https://wells.build/contact/locations/pearland-texas/":
        "2026-09-24: 32K sq ft facility. 125+ projects each year. 3201 Veterans Dr. C21 "
        "architectural certification.",
    "https://concreteproducts.com/index.php/2026/02/10/private-equity-operator-kps-outlines-wells-acquisition-agreement/":
        "2026-09-24: 10 February 2026. 13 production facilities. A top three North "
        "American player. Projected closing by the end of March.",
    "https://www.globenewswire.com/news-release/2022/06/10/2460684/0/en/Sekisui-House-Japan-s-Leading-Homebuilder-and-Diversified-Developer-Announces-Agreement-to-Acquire-Chesmar-Homes-of-Texas.html":
        "2026-09-24: June 10, 2022. Approximately $514 million. Plans to acquire an "
        "interest in Chesmar Homes on July 1, 2022.",
    "https://investors.bldr.com/news/news-details/2026/Builders-FirstSource-Reports-First-Quarter-2026-Results/default.aspx":
        "2026-09-24: approximately 570 locations across 43 states.",
    "https://www.sec.gov/Archives/edgar/data/1981792/000162828026053303/hhhsupplemental2q26.htm":
        "2026-09-24: land bank at June 30, 2026, residential saleable acres. Bridgeland "
        "1,142, sellout 2032. The Woodlands Hills 597, sellout 2035. The Woodlands 63, "
        "sellout 2031.",
    "https://www.globenewswire.com/news-release/2025/05/05/3073918/0/en/Pershing-Square-to-Invest-900-million-to-Acquire-Nine-Million-Newly-Issued-Shares-of-Howard-Hughes-Holdings-and-Transform-HHH-Into-a-Diversified-Holding-Company.html":
        "2026-09-24: Pershing Square will now own 46.9% of HHH shares outstanding.",
    "https://developingresilience.uli.org/case/bridgeland/":
        "2026-09-24: an 11,400-acre master-planned community, home to 65,000 residents "
        "when complete in 2037. Began construction in October 2003, home sales began in 2006.",
    "https://investor.howardhughes.com/news-releases/news-release-details/howard-hughes-corporationr-breaks-ground-woodlands-hills":
        "2026-09-24: November 15, 2017. A 2,000-acre development. More than 4,500 residences.",
    "https://www.builderonline.com/builder-100/smith-douglas-homes-enters-houston-market-with-devon-street-homes-acquisition_o":
        "2026-09-24: In 2022, Devon Street closed 324 homes across 15 communities with "
        "revenues in excess of $100 million. Currently controls nearly 1,500 lots in the "
        "area.",
    "https://benzinga.com/real-estate/22/03/26269992/dallas-based-real-estate-developer-launches-private-equity-offering-for-development-of-build-to-rent":
        "2026-09-24: 24 March 2022. Target investor IRR: 18% - 22%. Target equity "
        "multiple: 1.9x - 2.2x. seven parcHAUS single-family rental communities.",
    "https://concreteproducts.com/index.php/2014/09/16/well-anchored/":
        "2026-09-24: Output is equal to well over 100 yd./hour of self-consolidating "
        "concrete mixes. 50-acre plot. Founded in May 2013 by seven partners.",
    "https://www.newquest.com/about-us/":
        "2026-09-24: 12M SF Retail Space Managed. $3.1B Owned Assets Portfolio. The "
        "138-acre tract of land sale to CBL REIT for the 800,000-square-foot Pearland "
        "Town Center Mall that opened in 2008.",
    "https://ravennahomes.com/":
        "2026-09-24: The Woodlands Hills From The $500's. Seven communities listed.",
    "https://www.tricoasthomes.com/":
        "2026-09-24: Canterra Creek 60' Iowa Colony From the $399's. La Segarra 40' "
        "Brookshire From the $279's. Sunterra 40' & 50' Katy From the $324's. Lago Mar "
        "Texas City From the $364's.",
    "https://www.tricoasthomes.com/communities":
        "2026-09-24: Showing 9 Communities.",
    "https://www.tricoasthomes.com/plans":
        "2026-09-24: Showing 9 Available Plans.",
    "https://lagomarintexascity.com/tricoast-homes-joins-the-fun-in-lago-mar/":
        "2026-09-24: 2 March 2021. Founded in 2020. Taylor Morrison, Toll Brothers and "
        "Ryland Homes. Seven floor plans to Lago Mar starting in the $280,000s.",
    "https://sunterratx.com/homebuilders/":
        "2026-09-24: eighteen builder names listed under New Homes for Sale.",
    "https://www.globenewswire.com/news-release/2026/08/06/3340350/0/en/Citing-strong-market-fundamentals-Signorelli-chooses-rapid-Texas-expansion-for-award-winning-homebuilding-division.html":
        "2026-09-24: expected to deliver more than 1,300 single-family homes. The Azalea "
        "District at Valley Ranch in northeast Montgomery County will feature 359 homes by "
        "First America Homes, pricing starting in the $300s. More than 16 master-planned "
        "and neighborhood communities. Over 23,000 paper lots in the pipeline.",
    "https://www.globenewswire.com/news-release/2026/09/04/3356358/28788/en/LGI-Homes-Inc-Reports-August-2026-Home-Closings.html":
        "2026-09-24: As of August 31, 2026, the Company had 153 active selling "
        "communities. Closed over 80,000 homes since its founding in 2003.",
    "https://www.builderonline.com/firms/tilson-homes/":
        "2026-09-24: 2024 closings 425, revenue $199 M, rank 119. 2023 closings 745, "
        "revenue $328 M, rank 75.",
    "https://www.builderonline.com/firms/newmark-homes/":
        "2026-09-24: 2025 closings 483, revenue $306 M. 2024 closings 511, revenue $322 M.",
    "https://www.builderonline.com/firms/long-lake-limited/":
        "2026-09-24: 2025 closings 782, revenue $259 M, rank 74. 2024 closings 912, "
        "revenue $357 M.",
    "https://www.builderonline.com/firms/dsld-homes/":
        "2026-09-24: 2026 rank 25. 2025 closings 3,989. 2024 closings 4,116. Detached for "
        "sale 3,642. Single-family build-to-rent 347.",
    "https://www.dsldhomes.com/about-us":
        "2026-09-24: have built homes for over 41,000 families. actively building in more "
        "than 120 communities.",
    "https://www.encoreconcrete.com/":
        "2026-09-24: 100 percent employee-owned mark on the homepage, as an image label.",
    "https://kendallhomes.net/":
        "2026-09-24: priced from the $300s to the $800s.",
    "https://www.housingwire.com/articles/stylecraft-builders-margin-pace-and-growth/":
        "2026-09-24: 11 June 2026. Selling 973 homes for $310 million. Sales volume up "
        "17.0% from 2024 to 2025. Exit the Houston metro two to three years ago.",
    "https://www.builderonline.com/builder-100/strategy/new-home-co-and-landsea-homes-unite-as-risewell-homes-following-merger/":
        "2026-09-24: 2 December 2025. Landsea Homes closed 2,831 homes in 2024. New Home "
        "Co. closed 1,123 homes.",
    "https://www.daiwahouse.com/English/about/release/pdf/release_20210810e.pdf":
        "2026-09-24: 10 August 2021. 80.0%. Approx. US$408 million.",
    "https://investor.drhorton.com/~/media/Files/D/D-R-Horton-IR/documents/quarterly-reports/2025-dhi-annual-report.pdf":
        "2026-09-24: At September 30, 2025, we owned 62% of Forestar Group. Forestar sold "
        "14,240 lots, of which 83% were sold to D.R. Horton.",
    "https://houstonagentmagazine.com/2020/02/06/making-moves-newmark-homes-appoints-top-leaders-edward-jones-becomes-latest-tenant-bridgeland/":
        "2026-09-24: February 2020. Jeff has been with Newmark for 21 years.",
    "https://www.sec.gov/Archives/edgar/data/1981792/000162828026009701/hhhearningsreleaseq42025.htm":
        "2026-09-24: sale of 621 residential acres at an average price of $890,000 per acre.",
    "https://www.builderonline.com/firms/westin-homes/":
        "2026-09-14: Westin Homes, Sugar Land TX. 2025 closings 1,062, revenue "
        "$621 M, Builder 100 rank 60. 2024 closings 1,016, revenue $625 M, rank 67.",
    "https://www.builderonline.com/firms/colina-homes/":
        "2026-09-14: Colina Homes, Houston TX. 2025 closings 540, revenue $84 M, "
        "rank 96. 2024 closings 552, revenue $129 M, rank 97.",
    "https://www.builderonline.com/firms/sitterle-homes/":
        "2026-09-14: Sitterle Homes, San Antonio TX. 2022 closings 372, revenue "
        "$210 M. 2021 closings 323, revenue $185 M. 2022 is the last year carried, "
        "and the page does not mention Houston.",
    "https://www.builderonline.com/builder-100/builder-100-list/2026/":
        "2026-09-14: 2026 The Top 100. First America Homes at rank 75, 750 "
        "closings, $197 million, for 2025.",
    "https://www.builderonline.com/firms/castlerock-communities/":
        "2026-09-14: CastleRock Communities, Houston TX. 2025 closings 1,465, "
        "revenue $617 M, rank 49. 2024 closings 1,465, revenue $645 M, rank 48. "
        "No cumulative homes or communities count on the page.",
}


# Build 67. Two ways a page read as readable when it was not. A Cloudflare
# challenge is two thousand bytes of HTML, so it passed the length test and every
# figure on the card was then checked against the challenge text. And a server
# that compresses whatever it is asked for returned bytes that decoded to noise:
# DSLD's about page sat in the cache as 948,000 characters of it.
CHALLENGE = re.compile(r"Attention Required! \| Cloudflare|Just a moment\.\.\.|"
                       r"cf-browser-verification|Enable JavaScript and cookies to continue")


def _noise(txt):
    return txt.count("\ufffd") > max(50, len(txt) // 200)


# Build 67. A figure the card computed from published parts, where every part is
# printed on the card and on a page it cites. The check passes the sum only if
# every part is on the cited pages, so the register cannot hide an invented
# component. The card must print the parts; verify.py does not check that, a
# person reading the card does.
DERIVED = {
    "HOU-136": {"465": ["368", "97"]},          # Willow at Marvida + Sierra Vista
    "HOU-044": {"366": ["156", "210"]},         # two Katy duplex projects
    "HOU-011": {"1,802": ["1,142", "597", "63"]},  # land bank, three MPCs
    "HOU-019": {"389": ["200", "189"]},         # Long Meadow Farms + Woodmill Creek
}


def fetch(url):
    try:
        with urllib.request.urlopen(
                urllib.request.Request(url, headers=UA), timeout=30, context=CTX) as r:
            ct = (r.headers.get("Content-Type") or "").lower()
            if not any(k in ct for k in ("html", "xml", "text")):
                return None
            body = r.read(3_000_000)
            enc = (r.headers.get("Content-Encoding") or "").lower()
            if "gzip" in enc:
                import gzip
                body = gzip.decompress(body)
            elif "br" in enc:
                try:
                    import brotli
                    body = brotli.decompress(body)
                except Exception:
                    return None
            if len(body) < 2000:
                return None
            txt = flatten(body)
            if CHALLENGE.search(txt[:5000]) or _noise(txt):
                return None
            return txt
    except Exception:
        return None


def page_text(cache, url):
    """What the check reads for one URL: the fetched text, plus anything read by
    hand for it. A hand reading adds to a page; it never replaces one."""
    return " ".join(x for x in (cache.get(url) or "", flatten(BYHAND[url].encode("utf-8"))
                                if url in BYHAND else "") if x)


def variants(tok):
    """Every way a page might print the same quantity."""
    t = tok.strip().lower().replace("$", "").replace("%", " percent")
    t = re.sub(r"\s+", " ", t).strip()
    out = {t}
    bare = t.replace(",", "")
    out.add(bare)
    m = re.match(r"^([\d.]+)\s*(million|billion|percent)$", t)
    if m:
        n, unit = float(m.group(1)), m.group(2)
        if unit == "million":
            out |= {"%s million" % m.group(1), "%d,000,000" % int(n * 1e6) if n == int(n) else ""}
            out.add("{:,}".format(int(n * 1e6)) if n == int(n) else "")
            # Build 60. Trade tables abbreviate: Builder prints "$621 M" where the
            # card writes "$621 million". Five real, checked figures on three cards
            # were reported unsourced on that difference alone, which is the kind
            # of false positive that trains a reader to skim the report.
            out |= {"%s m" % m.group(1), "%sm" % m.group(1),
                    "%s mm" % m.group(1), "%s mil" % m.group(1)}
        if unit == "billion":
            out.add("{:,}".format(int(n * 1e9)) if n == int(n) else "")
            out |= {"%s b" % m.group(1), "%sb" % m.group(1), "%s bn" % m.group(1)}
        if unit == "percent":
            out |= {"%s%%" % m.group(1), "%s per cent" % m.group(1)}
    # Build 67. Price bands print in hundreds: J. Patrick's page says "from the
    # $370s" and Tricoast's "From the $279's" where the card writes $370,000s.
    if bare.isdigit() and len(bare) >= 6 and bare.endswith("000"):
        k = bare[:-3]
        out |= {"%ss" % k, "%s's" % k, "%s’s" % k, "%sk" % k}
    m = re.match(r"^(\d+) percent$", t)
    if m:
        out |= {"%s.0%%" % m.group(1), "%s.0 percent" % m.group(1)}
    if bare.isdigit():
        out.add("{:,}".format(int(bare)))
        # Marketing counters round to thousands: CastleRock's own about page says
        # "20k+ Homes since 2004" where the card says 20,000.
        if int(bare) >= 1000 and int(bare) % 1000 == 0:
            out |= {"%dk" % (int(bare) // 1000), "%d k" % (int(bare) // 1000)}
    return {v for v in out if v}


# The printer-fit bands are the deck's own declared assumption, stated in the
# method block with what they rest on. A reason that names the band it is read
# against is quoting the rubric, not citing a figure, so the band's own edges are
# not looked for on the firm's pages.
BAND = re.compile(r"\b(?:25 to 400|400 to 1,500|25 to 1,500)(?= band\b)")


# Build 67. Not quantities: the day in a date ("17 September 2025", "March 19,
# 2026"), the name of a list ("the Builder 100") and a street number. Each was
# reported as an unsourced figure, and a report that is one part noise gets
# skimmed.
_MON = (r"(?:January|February|March|April|May|June|July|August|September|"
        r"October|November|December)")
NOTFIG = re.compile(
    r"\b(\d{1,2})(?=\s+%s\b)|%s\s(\d{1,2})(?=,?\s+(?:19|20)\d\d)"
    r"|Builder (100)\b|\b(\d{3,6})(?=\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+"
    r"(?:Parkway|Street|St|Road|Rd|Drive|Dr|Boulevard|Blvd|Avenue|Ave|Lane|Way|Freeway|Highway)\b)"
    % (_MON, _MON))


def _blank(m):
    s = m.group(0)
    for i in range(1, 5):
        if m.group(i):
            a, b = m.start(i) - m.start(0), m.end(i) - m.start(0)
            s = s[:a] + " " * (b - a) + s[b:]
    return s


def figures_in(text):
    found = []
    text = BAND.sub(lambda m: " " * len(m.group(0)), text or "")
    text = NOTFIG.sub(_blank, text)
    for m in NUM.finditer(text or ""):
        tok = m.group(0)
        bare = re.sub(r"[^\d.]", "", tok)
        if not bare:
            continue
        if YEAR.match(bare.split(".")[0]) and "," not in tok and "$" not in tok:
            continue
        try:
            if float(bare.split(".")[0] or 0) < FLOOR and "million" not in tok.lower() \
                    and "billion" not in tok.lower():
                continue
        except ValueError:
            continue
        found.append((tok.strip(), max(0, m.start() - 55), m.end() + 25))
    for w, n in WORDS.items():
        # Build 62. "Eighty-five acres" was being read as the figure 80, because
        # the word eighty matched on its own and the hyphen after it was not
        # looked at. A compound number word is one number, not two, and the
        # second half is what carries the value.
        for m in re.finditer(r"\b%s\b(?!\s*-\s*\w)" % re.escape(w), text or "", re.I):
            if n >= FLOOR:
                found.append((str(n), max(0, m.start() - 55), m.end() + 25))
    return found


def main():
    d = json.load(open(ROOT / "houston-data.json", encoding="utf-8"))
    only = [a for a in sys.argv[1:] if a.startswith("HOU-")]
    targets = [t for t in d["targets"] if not only or t["target_id"] in only]

    cache = {}
    if CACHE.exists():
        cache = json.load(open(CACHE, encoding="utf-8"))
    for u in [u for u, v in cache.items() if v and (CHALLENGE.search(v[:5000]) or _noise(v))]:
        del cache[u]

    want = set()
    for t in targets:
        for u in ([t.get("homepage_url")] + [s.get("url") for s in t.get("sources", [])]
                  + [k.get("url") for k in t.get("key_projects", [])]
                  + [n.get("url") for n in t.get("news", [])]):
            if u and u.startswith("http") and not any(h in u for h in SKIP_HOST) \
                    and u not in cache:
                want.add(u)

    if want:
        print("fetching %d pages not already cached" % len(want), file=sys.stderr)
        with cf.ThreadPoolExecutor(16) as ex:
            for u, txt in zip(sorted(want), ex.map(fetch, sorted(want))):
                cache[u] = txt or ""
        CACHE.parent.mkdir(exist_ok=True)
        json.dump(cache, open(CACHE, "w"), ensure_ascii=False)

    n_fig = n_off = 0
    off_cards = 0
    blind = []
    for t in targets:
        urls = [u for u in ([t.get("homepage_url")]
                            + [s.get("url") for s in t.get("sources", [])]
                            + [k.get("url") for k in t.get("key_projects", [])]
                            + [n.get("url") for n in t.get("news", [])])
                if u and u.startswith("http") and not any(h in u for h in SKIP_HOST)]
        readable = [u for u in urls if page_text(cache, u)]
        blob = " ".join(page_text(cache, u) for u in readable).lower()

        text = " ".join(filter(None, [
            t.get("synopsis"), t.get("key_stat"),
            " ".join(w["text"] for w in t.get("why", [])),
            " ".join(k["detail"] for k in t.get("key_projects", [])),
            " ".join(n["what"] for n in t.get("news", []))]))

        hits = figures_in(text)
        n_fig += len(hits)
        if not readable:
            if hits:
                blind.append(t["target_id"])
            continue
        miss = []
        der = DERIVED.get(t["target_id"], {})
        for tok, a, b in hits:
            if any(v in blob for v in variants(tok)):
                continue
            if tok in der and all(any(v in blob for v in variants(p)) for p in der[tok]):
                continue
            miss.append((tok, re.sub(r"\s+", " ", text[a:b]).strip()))
        if miss:
            off_cards += 1
            n_off += len(miss)
            print("\n%-9s %-30s  %d of %d cited pages readable"
                  % (t["target_id"], t["short"][:30], len(readable), len(urls)))
            seen = set()
            for tok, ctx in miss:
                if tok in seen:
                    continue
                seen.add(tok)
                print("   %-14s ...%s..." % (tok, ctx[:88]))

    if blind:
        print("\nNo cited page readable, so not checked: %s" % ", ".join(blind))
    print("\n%d figures across %d cards. %d on no page the card cites, over %d cards."
          % (n_fig, len(targets), n_off, off_cards))
    print("A figure here is invented, derived, or from a source the card does not "
          "list. Open the card and one page to tell which.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
