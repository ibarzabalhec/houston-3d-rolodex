# -*- coding: utf-8 -*-
"""The link layer: company pages, leadership pages, and per-person sources.

Every URL here was seen in a search result or on a page that was actually
fetched. Where a firm has none, NOTE says why, and that reason is rendered
rather than hidden. No URL is pattern-guessed.

COMPANY[target_id] = {"li": LinkedIn company page or None,
                      "li_note": why it is None,
                      "team": the firm's own leadership page or None,
                      "team_note": why it is None}

PERSON[(target_id, name)] = (url, what the page says)
"""

COMPANY = {
"HOU-001": {"li": "https://www.linkedin.com/company/wan-bridge-group/",
            "team": "https://wanbridge.com/leadership/"},
"HOU-002": {"li": "https://www.linkedin.com/company/cole-klein-builders",
            "team": "https://colekleinbuilders.com/about/"},
"HOU-003": {"li": "https://www.linkedin.com/company/houston-housing-authority",
            "team": "https://housingforhouston.com/leadership/executive-leadership/"},
"HOU-004": {"li": "https://www.linkedin.com/company/intown-homes",
            "team": "https://www.lovettcommercial.com/about",
            "team_note": "InTown's own site has no leadership page. The page here is Lovett "
                          "Commercial, the same ownership under Frank Liu."},
"HOU-005": {"li": "https://www.linkedin.com/company/radom-capital-llc",
            "team": "https://www.radomcapital.com/team"},
"HOU-006": {"li": "https://www.linkedin.com/company/triten-real-estate-partners",
            "team": "https://www.tritenre.com/team"},
"HOU-007": {"li": "https://www.linkedin.com/company/first-america-homes",
            "team": "https://www.firstamericahomes.com/about/"},
"HOU-008": {"li": "https://www.linkedin.com/company/meritage-homes",
            "team": "https://investors.meritagehomes.com/company-information/management-team"},
"HOU-009": {"li": "https://www.linkedin.com/company/century-communities",
            "team": "https://investors.centurycommunities.com/governance/executive-management/default.aspx"},
"HOU-010": {"li": "https://www.linkedin.com/company/camillo-companies",
            "team": "https://www.camillocompanies.com/about-us"},
"HOU-011": {"li": "https://www.linkedin.com/company/the-howard-hughes-corporation",
            "team": "https://investor.howardhughes.com/governance/leadership"},
"HOU-012": {"li": "https://www.linkedin.com/company/mihomes/",
            "team": "https://investors.mihomes.com/investor-relations/officers-directors/default.aspx"},
"HOU-013": {"li": "https://www.linkedin.com/company/perry-homes",
            "team": "https://www.perryhomes.com/about-perry-homes"},
"HOU-014": {"li": "https://www.linkedin.com/company/lgi-homes",
            "team": "https://investor.lgihomes.com/corporate-governance/management"},
"HOU-015": {"li": "https://www.linkedin.com/company/signorelli-company",
            "team": "https://www.signorellicompany.com/our-leadership"},
"HOU-016": {"li": None,
            "li_note": "No LinkedIn company page exists. The firm's only social presence is a "
                        "Facebook page for San Leon.",
            "team": None,
            "team_note": "No company website could be found at all, only a Facebook page and a "
                          "Texas LLC filing in Dickinson."},
"HOU-017": {"li": None,
            "li_note": "No LinkedIn company page for Elpis 3D. Searches return unrelated firms "
                        "using the same word.",
            "team": None,
            "team_note": "No company website could be found."},
"HOU-018": {"li": "https://www.linkedin.com/company/newquest-properties",
            "team": "https://www.newquest.com/about-us/leadership/"},
"HOU-019": {"li": "https://www.linkedin.com/company/camden-property-trust",
            "team": "https://investors.camdenliving.com/investors/governance/board-of-directors/default.aspx"},
"HOU-020": {"li": "https://www.linkedin.com/company/provident-realty-advisors",
            "team": "https://provident.net/our-team/"},
"HOU-021": {"li": "https://www.linkedin.com/company/the-dinerstein-companies/",
            "team": "https://www.dinersteincos.com/about-us"},
"HOU-022": {"li": "https://www.linkedin.com/company/castlerock-communities",
            "team": "https://www.c-rock.com/about"},
"HOU-023": {"li": "https://www.linkedin.com/company/david-weekley-homes",
            "team": "https://www.davidweekleyhomes.com/about-us/meet-the-team"},
"HOU-024": {"li": "https://www.linkedin.com/company/ashton-woods-homes",
            "team": "https://www.ashtonwoods.com/corporate-info"},
"HOU-025": {"li": "https://www.linkedin.com/company/taylor-morrison",
            "team": "https://newsroom.taylormorrison.com/Leadership"},
"HOU-026": {"li": "https://www.linkedin.com/company/christopher-todd-communities",
            "team": "https://www.christophertodd.com/our-story/"},
"HOU-027": {"li": "https://www.linkedin.com/company/greystar",
            "team": "https://www.greystar.com/business/about-greystar/our-leadership"},
"HOU-028": {"li": "https://www.linkedin.com/company/sueba-usa-corporation",
            "team": "https://suebausa.com/about-us/"},
"HOU-029": {"li": None,
            "li_note": "No LinkedIn company page was confirmed and Hanover's own site carries no "
                        "link to one.",
            "team": "https://www.hanoverco.com/leadership",
            "team_note": "The leadership page renders client-side, so the names on it could not be "
                          "read from a fetch. The people below were sourced elsewhere."},
"HOU-030": {"li": "https://www.linkedin.com/company/fidelis-realty-partners",
            "team": "https://www.frpltd.com/about-fidelis/mission-values"},
"HOU-031": {"li": "https://www.linkedin.com/company/read-king-inc-",
            "team": "https://www.read-king.com/team"},
"HOU-032": {"li": None,
            "li_note": "Urban Living is a generic name and several unrelated LinkedIn pages carry "
                        "it. None could be tied to the Houston firm, so none is claimed.",
            "team": None,
            "team_note": "urbanliving.com refuses automated retrieval, so no team page could be read."},
"HOU-033": {"li": "https://www.linkedin.com/company/coventryhomes",
            "team": None,
            "team_note": "Coventry's about page names no executives. It is a Dream Finders brand "
                          "and has no leadership page of its own."},
"HOU-034": {"li": "https://www.linkedin.com/company/brightlandhomes",
            "team": "https://www.drbgroup.com/about",
            "team_note": "Brightland publishes no leadership of its own. The page linked here is The "
                          "DRB Group, its parent since April 2025, which does."},
"HOU-035": {"li": "https://www.linkedin.com/company/avenue-community-development-coporation",
            "team": "https://avenuecdc.org/about-us/board-staff/"},
"HOU-036": {"li": "https://www.linkedin.com/company/midway",
            "team": "https://www.midway.team/our-people"},
"HOU-037": {"li": None,
            "li_note": "The Deal Company's site links only to Instagram and Facebook. No LinkedIn "
                        "company page was confirmed.",
            "team": "https://www.dealco.net/about/"},
"HOU-038": {"li": "https://www.linkedin.com/company/cameron-management",
            "team": "https://cameronmanagement.com/about"},
"HOU-039": {"li": "https://www.linkedin.com/company/land-tejas-companies",
            "team": "https://landtejas.com/about-us/our-leadership/"},
"HOU-040": {"li": "https://www.linkedin.com/company/the-johnson-development-corp",
            "team": "https://www.johnsondevelopment.com/our-leaders"},
"HOU-041": {"li": "https://www.linkedin.com/company/caldwell-companies",
            "team": "https://caldwellcos.com/our-team"},
"HOU-042": {"li": "https://www.linkedin.com/company/friendswood-development-company",
            "team": "https://friendswooddevelopment.com/people"},
"HOU-043": {"li": "https://www.linkedin.com/company/newland-communities-llc",
            "team": None,
            "team_note": "Newland's leadership page now redirects to Brookfield Residential, which "
                          "announces the acquisition and names nobody. The firm no longer publishes "
                          "its own leadership."},
"HOU-044": {"li": "https://www.linkedin.com/company/rsk-real-estate-partners",
            "team": "https://rskrealestatepartners.com/our-team/"},
"HOU-045": {"li": "https://www.linkedin.com/company/chesmar-homes",
            "team": None,
            "team_note": "Chesmar publishes no leadership page. Every name on this card came off "
                          "LinkedIn."},
"HOU-046": {"li": "https://www.linkedin.com/company/metronational",
            "team": "https://www.metronational.com/about-metronational/leadership"},
"HOU-047": {"li": "https://www.linkedin.com/company/baker-katz",
            "team": "https://bakerkatz.com/about-us/"},
"HOU-048": {"li": "https://www.linkedin.com/company/wulfe",
            "li_note": "The page reads Wulfe rather than Wulfe & Co. No other Houston firm uses "
                        "the name and the firm's own site uses the short form.",
            "team": "https://www.wulfe.com/people"},
"HOU-049": {"li": "https://www.linkedin.com/company/streetlights-residential",
            "team": "https://www.streetlights.com/leadership"},
"HOU-050": {"li": "https://www.linkedin.com/company/the-finger-companies",
            "team": "https://www.fingercompanies.com/our-company.html"},
"HOU-051": {"li": "https://www.linkedin.com/company/rice-management-company",
            "team": "https://iondistrict.com/team/"},
"HOU-052": {"li": "https://www.linkedin.com/company/medistar-corporation",
            "team": "https://www.medistarcorp.com/team/",
            "team_note": "The team page renders client-side, so the roster could not be read from "
                          "a fetch."},
"HOU-053": {"li": "https://www.linkedin.com/company/wolff-companies",
            "team": "https://wolffcompanies.com/about/leadership/"},
"HOU-054": {"li": "https://www.linkedin.com/company/stonelake-capital-partners",
            "team": "https://stonelake.com/stonelake-team/"},
"HOU-055": {"li": "https://www.linkedin.com/company/caf-capital-partners",
            "team": "https://cafcapital.com/about-us"},
"HOU-056": {"li": "https://www.linkedin.com/company/sarofim-realty-advisors",
            "team": None,
            "team_note": "Sarofim names nobody. Its site describes an investment committee of senior "
                          "officers with twenty-five years of experience and gives no individual on "
                          "any page. It is the only firm screened here with no publicly identifiable "
                          "person at all."},
"HOU-057": {"li": "https://www.linkedin.com/company/hartman-income-reit-management-llc",
            "li_note": "This page is Hartman, the Al Hartman entity. Silver Star Properties REIT "
                        "is separate, at linkedin.com/company/silver-star-reit.",
            "team": "https://hartman-properties.com/meet-hartman-team/"},
}

# People the firm's own pages named who were not in the record at all.
NEW_PEOPLE = {
"HOU-046": [("Scooter Hicks", "President, MetroNational"),
            ("Jason Johnson", "Chief Executive Officer, MetroNational"),
            ("Roy Johnson", "Executive Chairman, MetroNational")],
"HOU-051": [("John D. Lawrence", "Chief Investment Officer and President, Rice Management Company"),
            ("Jan Odegard", "Executive Director, the Ion")],
"HOU-043": [("Alan Bauer", "Senior Vice President and Houston Division Manager, Newland (2019)")],
"HOU-015": [("John Winniford", "President, Homebuilding, The Signorelli Company")],
"HOU-044": [("Neil Joshi", "Managing Member, RSK Real Estate Partners"),
            ("Gregg Erickson", "Vice President of Construction, RSK Real Estate Partners"),
            ("Hannah Ripkey", "Vice President of Development, RSK Real Estate Partners")],
"HOU-047": [("Jason Baker", "Leads the tenant representation team, Baker Katz"),
            ("Kenneth Katz", "Leads the investment and development practice, Baker Katz"),
            ("Martin Mendoza", "Oversees design and construction, Baker Katz")],
"HOU-048": [("Bob Sellingsloh", "President and Principal, Wulfe & Co."),
            ("Tammy Smith", "Director of Construction, Wulfe & Co.")],
"HOU-034": [("Ronny Salameh", "President and Chief Executive Officer, The DRB Group"),
            ("Young Nam", "Senior Vice President of Purchasing, The DRB Group")],
"HOU-002": [("Vanessa Cole", "Co-founder, Cole Klein Builders"),
            ("Harry Klein", "Co-founder, Cole Klein Builders")],
"HOU-053": [("David S. Wolff", "Chairman and President, Wolff Companies"),
            ("David L. Lane", "Executive Vice President and Chief Financial Officer, Wolff Companies")],
"HOU-040": [("Michael J. Smith", "President and Chief Executive Officer, Johnson Development")],
"HOU-041": [("Fred Caldwell", "Chief Executive Officer, Caldwell Companies")],
"HOU-042": [("Michael Reamer", "President, Friendswood Development Company")],
"HOU-039": [("Alan Brende", "Co-President, Land Tejas"),
            ("Melanie Ohl", "Co-President, Land Tejas")],
"HOU-049": [("Robert de Bruin", "President and Chief Executive Officer, StreetLights Residential")],
"HOU-050": [("Jill Jewett", "President and Corporate Director, The Finger Companies")],
"HOU-054": [("Kenneth E. Aboussie, Jr.", "Managing Partner, StoneLake Capital Partners"),
            ("John A. Kiltz", "Managing Partner, StoneLake Capital Partners")],
"HOU-052": [("Monzer Hourani", "Founder and Chief Executive Officer, Medistar Corporation")],
"HOU-055": [("Jason Geer", "President, CAF Capital Partners")],
"HOU-057": [("Allen Hartman", "President and Chief Executive Officer, Hartman vREIT XXI"),
            ("Gerald Haddock", "Chief Executive Officer and Chairman, Silver Star Properties REIT")],
}

# People who clear the decider bar but were added from a firm's own page rather than
# from a LinkedIn sweep. Same bar: they can change a wall specification.
DECIDERS = {
    ("HOU-044", "Gregg Erickson"),
    ("HOU-048", "Tammy Smith"),
    ("HOU-047", "Martin Mendoza"),
    ("HOU-034", "Young Nam"),
    ("HOU-028", "Raymond Gabriele"),
}

# (target_id, person) -> (url, what that page says). Used where LinkedIn is null,
# and alongside it where the firm's own page is the better citation.
PERSON = {
("HOU-003", "Jamie Bryant"): (
    "https://housingforhouston.com/leadership/executive-leadership/",
    "Named President and Chief Executive Officer on the authority's own executive leadership page."),
("HOU-006", "Carter Bechtol"): (
    "https://www.tritenre.com/team/carter-becthol",
    "Triten's own bio page. Partner, Head of Triten Residential. The residential platform is the "
    "part of Triten that would buy a repeated wall."),
("HOU-007", "John Winniford"): (
    "https://www.signorellicompany.com/our-leadership/34/john-winniford",
    "Signorelli's own bio page. President, Homebuilding, running First America across Greater "
    "Houston and San Antonio with Dallas next. Thirty years in homebuilding, and President and "
    "Chief Executive of Brightland Homes, formerly Gehan, for nearly a decade, where he delivered "
    "more than 22,000 homes from 2016. Texas A&M finance degree. He has no usable LinkedIn profile: "
    "the only account under the name has one connection and reads owner in Austin."),
("HOU-008", "Hilla Sferruzza"): (
    "https://investors.meritagehomes.com/company-information/management-team",
    "Executive Vice President and Chief Financial Officer on Meritage's own management page."),
("HOU-008", "Steven J. Hilton"): (
    "https://investors.meritagehomes.com/company-information/management-team",
    "Executive Chairman of the Board on Meritage's own management page."),
("HOU-009", "Rob Francescon"): (
    "https://investors.centurycommunities.com/governance/executive-management/default.aspx",
    "Century's own executive management page. He became sole Chief Executive Officer and President "
    "on 1 January 2025, having been co-chief executive."),
("HOU-011", "David O'Reilly"): (
    "https://investor.howardhughes.com/governance/leadership",
    "Chief Executive Officer on Howard Hughes's own leadership page."),
("HOU-011", "Bill Ackman"): (
    "https://investor.howardhughes.com/governance/leadership",
    "Executive Chairman on Howard Hughes's own leadership page."),
("HOU-011", "Ryan Israel"): (
    "https://investor.howardhughes.com/governance/leadership",
    "Chief Investment Officer on Howard Hughes's own leadership page."),
("HOU-012", "Bob Schottenstein"): (
    "https://investors.mihomes.com/investor-relations/officers-directors/default.aspx",
    "Chairman, and Chief Executive Officer since January 2004, on M/I's own officers page."),
("HOU-012", "Jay McManus"): (
    "https://houstonagentmagazine.com/2021/08/23/m-i-homes-to-double-presence-in-houston-area/",
    "Named Houston division president for M/I Homes in trade coverage of the division's expansion. "
    "M/I's own site names corporate officers only."),
("HOU-013", "Kathy Britton"): (
    "https://www.perryhomes.com/about-perry-homes",
    "Perry's own page: Owner and Executive Chair, having succeeded her father Bob Perry as chief "
    "executive."),
("HOU-013", "Todd Chachere"): (
    "https://www.perryhomes.com/about-perry-homes",
    "Chief Executive Officer on Perry's own page."),
("HOU-014", "Eric Lipar"): (
    "https://investor.lgihomes.com/corporate-governance/management",
    "Chief Executive Officer and Chairman on LGI's own management page."),
("HOU-014", "Mike Snider"): (
    "https://investor.lgihomes.com/corporate-governance/management",
    "President and Chief Operating Officer on LGI's own management page."),
("HOU-014", "Charles Merdian"): (
    "https://investor.lgihomes.com/corporate-governance/management",
    "Chief Financial Officer and Treasurer on LGI's own management page."),
("HOU-015", "John Winniford"): (
    "https://www.signorellicompany.com/our-leadership/34/john-winniford",
    "President, Homebuilding. The same person who runs First America, which Signorelli owns, so a "
    "single approach reaches both the land position and the builder."),
("HOU-015", "Jeff Dewese"): (
    "https://www.signorellicompany.com/our-leadership/15/jeff-dewese",
    "Signorelli's own bio page. President, Land Division, overseeing land acquisition, planning and "
    "construction management for Granger Pines, Cielo and Austin Point."),
("HOU-015", "Harry Dinham"): (
    "https://www.signorellicompany.com/our-leadership/30/harry-dinham",
    "Signorelli's own bio page. Chief Financial Officer on the executive leadership team."),
("HOU-016", "Steve Commander"): (
    "https://www.galvnews.com/news/printing-the-future-san-leon-project-tests-new-model-for-coastal-housing/article_e6c622f8-f6cd-47f6-ad36-ed1cac45a3d4.html",
    "Quoted as the developer of the San Leon printed-home project, in partnership with HiveASMBLD. "
    "The only citable source: there is no company site and no LinkedIn page."),
("HOU-017", "Tony M. Brown"): (
    "https://www.homes.com/news/houstons-3d-printed-housing-push-grows-with-two-new-developments/647676272/",
    "Named managing member of Elpis 3D, speaking about the Avenue J printed duplex in the East End. "
    "The only citable source: there is no company site and no LinkedIn page."),
("HOU-018", "Steven D. Alvis"): (
    "https://www.newquest.com/about-us/leadership/", "Co-Founder and Managing Partner."),
("HOU-018", "Jay K. Sears"): (
    "https://www.newquest.com/about-us/leadership/", "Co-Founder and Managing Partner."),
("HOU-018", "Austin Alvis"): (
    "https://www.newquest.com/about-us/leadership/", "President and Chief Development Officer."),
("HOU-018", "Jeff Horton"): (
    "https://www.newquest.com/about-us/leadership/",
    "Chief Operating Officer and Head of Capital Markets."),
("HOU-019", "Alex Jessett"): (
    "https://investors.camdenliving.com/investors/governance/board-of-directors/default.aspx",
    "Chief Executive Officer, previously President and Chief Financial Officer, at Camden since 1999."),
("HOU-019", "Richard J. Campo"): (
    "https://investors.camdenliving.com/investors/governance/board-of-directors/default.aspx",
    "Executive Chairman, chief executive from the 1993 listing until 2026."),
("HOU-020", "Leon J. Backes"): (
    "https://provident.net/our-team/", "Founder and Chief Executive Officer, named on the firm's team page."),
("HOU-020", "Christen Vestal"): (
    "https://www.bisnow.com/houston/news/industrial/provident-realty-advisors-hires-christen-vestal-to-lead-forthcoming-houston-office-116393",
    "Hired to lead Provident's new Houston office as its first female development partner. She does "
    "not appear on the firm's current team page, so treat the role as needing confirmation."),
("HOU-021", "Brian Dinerstein"): (
    "https://www.dinersteincos.com/team/brian-dinerstein",
    "The firm's own bio page. Chief Executive Officer of a developer and operator with $4.3 billion "
    "under management."),
("HOU-021", "Brad Dinerstein"): (
    "https://www.dinersteincos.com/about-us", "Managing Partner of Development and Design."),
("HOU-021", "John Caltagirone"): (
    "https://www.dinersteincos.com/about-us", "President and Partner."),
("HOU-022", "Lance Wright"): (
    "https://www.c-rock.com/about",
    "CastleRock's own about page: a founding partner, serving as chief executive."),
("HOU-023", "Chris Weekley"): (
    "https://www.davidweekleyhomes.com/about-us/meet-the-team",
    "President and Vice Chairman. The firm's own page credits him with innovation and developer "
    "relationships, which is the brief a printed wall would land in."),
("HOU-023", "David Weekley"): (
    "https://www.davidweekleyhomes.com/about-us/meet-the-team",
    "Chairman, who started the company in 1976 at twenty-three."),
("HOU-024", "Ken Balogh"): (
    "https://www.ashtonwoods.com/corporate-info", "President and Chief Executive Officer."),
("HOU-024", "Lindsay Motley"): (
    "https://www.ashtonwoods.com/corporate-info",
    "Regional President. The firm's own announcement names her Austin division president."),
("HOU-024", "Ryan Lewis"): (
    "https://www.ashtonwoods.com/corporate-info", "Chief Operating Officer."),
("HOU-026", "Todd Wood"): (
    "https://www.christophertodd.com/our-story/",
    "Founded Christopher Todd Communities in 2016, after selling an organic bakery."),
("HOU-026", "Brent Long"): (
    "https://www.christophertodd.com/press-releases/brent-long-joins-christopher-todd-as-director-of-investment-and-land/",
    "Joined as Director of Investment and Land with twenty-five years in multifamily."),
("HOU-027", "Bob Faith"): (
    "https://www.greystar.com/contact-us/our-people/bob-faith",
    "Founder, Chairman and Chief Executive Officer on Greystar's own bio page."),
("HOU-027", "Brian Herwald"): (
    "https://www.greystar.com/business/about-greystar/newsroom/greystar-completes-first-logistics-project-in-houston",
    "Managing Director of Development, quoted on Greystar's first Houston logistics project."),
("HOU-028", "John Chiang"): (
    "https://suebausa.com/about-us/", "Executive Vice President and Chief Operating Officer."),
("HOU-029", "Brandt Bowden"): (
    "https://knowledge.uli.org/en/people/b/b/brandt-bowden-f34f",
    "Chief Executive Officer of Hanover, overseeing capital, development and construction, "
    "previously chief investment officer."),
("HOU-029", "Murry Bowden"): (
    "https://www.nmhc.org/meetings/meetings-pages/meeting-materials/j-murry-bowden-biography/",
    "Founder, Chairman and Chief Executive Officer, responsible for strategy and investment decisions."),
("HOU-029", "John Nash"): (
    "https://www.hanoverco.com/leadership",
    "President. Thirty-three years with Hanover, twenty-three of them as president, per the "
    "McCombs alumni network."),
("HOU-029", "John Garibaldi"): (
    "https://www.hanoverco.com/leadership",
    "President, Multifamily. Twenty-five years with the firm, starting as a development partner in "
    "Houston in 1999."),
("HOU-030", "K. Alan Hassenflu"): (
    "https://www.frpltd.com/about-fidelis/mission-values",
    "President and Chief Executive Officer, a founder in 2003, formerly senior managing director at "
    "Trammell Crow."),
("HOU-030", "Glenn Airola"): (
    "https://www.frpltd.com/about-fidelis/mission-values",
    "Executive Vice President, General Counsel and Chief Administrative Officer since 2007."),
("HOU-031", "Jeff Read"): ("https://www.read-king.com/team", "Principal."),
("HOU-031", "Ewing King"): ("https://www.read-king.com/team", "Principal."),
("HOU-031", "Blake Allen"): ("https://www.read-king.com/team", "Chief Financial Officer."),
("HOU-032", "Vinod Ramani"): (
    "https://www.bbb.org/us/tx/houston/profile/real-estate/urban-living-0915-52001132",
    "Listed as chief executive in the Better Business Bureau record for Urban Living. The firm's "
    "own site refuses automated retrieval, so this is a third-party citation, not the firm's."),
("HOU-035", "Mary Lawler"): (
    "https://avenuecdc.org/about-us/board-staff/",
    "Chief Executive Officer on Avenue's own board and staff page, marking twenty-five years of "
    "leadership."),
("HOU-036", "Bradley Freels"): (
    "https://www.midway.team/our-people",
    "Chairman and Chief Executive Officer on Midway's own people page. He has no findable LinkedIn "
    "profile, so this is the citation."),
("HOU-036", "Clark Thompson"): (
    "https://www.midway.team/our-people", "Executive Vice President and General Counsel."),
("HOU-037", "Jon Deal"): (
    "https://www.dealco.net/about/",
    "Founder and Chief Executive Officer, and co-developer of Sawyer Yards."),
("HOU-038", "Dougal A. Cameron"): (
    "https://cameronmanagement.com/team_member/dougal-a-cameron",
    "President. Founded the firm in 1995 after asset and project management at Hines."),
("HOU-038", "William T. Dom"): (
    "https://cameronmanagement.com/team_member/william-t-ted-dom",
    "Chief Operating Officer and partner since 2000, formerly an asset manager at Hines."),
("HOU-025", "Darin Rowe"): (
    "https://newsroom.taylormorrison.com/2022-11-14-Taylor-Morrison-Unveils-New-Build-To-Rent-Brand,-Yardly",
    "Build-to-Rent President, quoted on the launch of the Yardly brand. National, not Houston."),
("HOU-010", "Margaret Potter"): (
    "https://www.camillocompanies.com/about-us",
    "Camillo's own about page now names Dan Miller as chief executive and does not name her. "
    "Third-party org charts still show her as chief executive since 2013. Treat the title as stale "
    "until the firm confirms it."),
("HOU-010", "Meagan Yager"): (
    "https://www.camillocompanies.com/about-us",
    "Not on Camillo's current about page. A third-party org chart lists her as corporate vice "
    "president of marketing at Legend Homes, a Camillo brand. The page does list a Meagan Butler in "
    "property management, who is a different person."),
("HOU-051", "John D. Lawrence"): (
    "https://investments.rice.edu/people",
    "Chief Investment Officer and President of Rice Management Company, the owner of the Ion "
    "District, on Rice's own page."),
("HOU-051", "Jan Odegard"): (
    "https://iondistrict.com/team/",
    "Executive Director of the Ion, after eighteen years at Rice and a spell running the Ken "
    "Kennedy Institute."),
("HOU-046", "Scooter Hicks"): (
    "https://www.metronational.com/about-metronational/leadership",
    "President on MetroNational's own leadership page, under Jason Johnson as chief executive and "
    "Roy Johnson as executive chairman."),
("HOU-046", "Jason Johnson"): (
    "https://www.metronational.com/about-metronational/leadership",
    "Chief Executive Officer. He held the president title before 2023, which is why two different "
    "people appear as president across dated sources."),
("HOU-046", "Roy Johnson"): (
    "https://www.metronational.com/about-metronational/leadership", "Executive Chairman."),
("HOU-053", "David S. Wolff"): (
    "https://wolffcompanies.com/about/leadership/", "Chairman and President."),
("HOU-053", "David L. Lane"): (
    "https://wolffcompanies.com/about/leadership/",
    "Executive Vice President and Chief Financial Officer."),
("HOU-040", "Michael J. Smith"): (
    "https://www.johnsondevelopment.com/our-leaders", "President and Chief Executive Officer."),
("HOU-041", "Fred Caldwell"): (
    "https://caldwellcos.com/our-team", "Chief Executive Officer."),
("HOU-042", "Michael Reamer"): (
    "https://friendswooddevelopment.com/people", "President."),
("HOU-039", "Alan Brende"): (
    "https://landtejas.com/about-us/our-leadership/", "Co-President."),
("HOU-039", "Melanie Ohl"): (
    "https://landtejas.com/about-us/our-leadership/", "Co-President."),
("HOU-049", "Robert de Bruin"): (
    "https://www.streetlights.com/leadership", "President and Chief Executive Officer."),
("HOU-050", "Jill Jewett"): (
    "https://www.fingercompanies.com/our-company.html", "President and Corporate Director."),
("HOU-054", "Kenneth E. Aboussie, Jr."): (
    "https://stonelake.com/stonelake-team/", "Managing Partner."),
("HOU-054", "John A. Kiltz"): (
    "https://stonelake.com/stonelake-team/", "Managing Partner."),
("HOU-052", "Monzer Hourani"): (
    "https://www.medistarcorp.com/team/",
    "Founder and Chief Executive Officer. The team page renders client-side; the title is "
    "corroborated by Medistar's own LinkedIn posts."),
("HOU-055", "Jason Geer"): (
    "https://cafcapital.com/about-us", "President of CAF Capital Partners."),
("HOU-057", "Allen Hartman"): (
    "https://hartman-properties.com/meet-hartman-team/",
    "President and Chief Executive Officer of Hartman vREIT XXI, the entity that carries no "
    "bankruptcy of its own."),
("HOU-057", "Gerald Haddock"): (
    "https://silverstarreit.com/management-team/",
    "Chief Executive Officer and Chairman of Silver Star Properties REIT, elected executive "
    "chairman in August 2023 and appointed chief executive that December. This is the entity in "
    "Chapter 11."),
("HOU-044", "Neil Joshi"): (
    "https://rskrealestatepartners.com/our-team/", "Managing Member."),
("HOU-044", "Gregg Erickson"): (
    "https://rskrealestatepartners.com/our-team/",
    "Vice President of Construction. RSK is a small firm that names its construction lead on its "
    "own team page, which larger builders do not."),
("HOU-044", "Hannah Ripkey"): (
    "https://rskrealestatepartners.com/our-team/", "Vice President of Development."),
("HOU-047", "Jason Baker"): (
    "https://bakerkatz.com/about-us/",
    "Leads the tenant representation team, with more than twenty-five years in Houston retail. The "
    "page carries bios without formal titles."),
("HOU-047", "Kenneth Katz"): (
    "https://bakerkatz.com/about-us/",
    "Leads the real estate investment and development practice, covering ground-up development and "
    "redevelopment."),
("HOU-047", "Martin Mendoza"): (
    "https://bakerkatz.com/about-us/",
    "Joined in August 2024 responsible for overseeing design and construction phases. The page gives "
    "no title, so the function rather than the rank is what places him here."),
("HOU-048", "Bob Sellingsloh"): (
    "https://www.wulfe.com/people",
    "President and Principal, listed first under leadership. Ed Wulfe no longer appears on the leadership page."),
("HOU-048", "Tammy Smith"): (
    "https://www.wulfe.com/people", "Director of Construction."),
("HOU-034", "Ronny Salameh"): (
    "https://www.drbgroup.com/about",
    "President and Chief Executive Officer of The DRB Group, which has owned Brightland since "
    "April 2025."),
("HOU-034", "Young Nam"): (
    "https://www.drbgroup.com/about",
    "Senior Vice President of Purchasing at The DRB Group. Brightland publishes no leadership of its "
    "own, so the person who buys for the platform Brightland sits inside is the contact."),
("HOU-002", "Vanessa Cole"): (
    "https://colekleinbuilders.com/about/",
    "Co-founder. The firm's own about page names Vanessa Cole and Harry Klein as founders."),
("HOU-002", "Harry Klein"): (
    "https://colekleinbuilders.com/about/", "Co-founder."),
("HOU-043", "Alan Bauer"): (
    "https://www.westhouston.org/2019/01/18/welcome-to-the-2019-board-or-directors/",
    "Senior Vice President and Division Manager for Newland's Houston division, per the West "
    "Houston Association board announcement. Dated 2019 and unconfirmed since, because Newland no "
    "longer publishes its own leadership."),
}
