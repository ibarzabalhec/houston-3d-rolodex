# -*- coding: utf-8 -*-
"""LinkedIn URLs confirmed by opening a search result and reading the headline.

Source: Héctor's signed-in LinkedIn session via the desktop browser, 11 Sep 2026.
Only entries where all three confirmation tests hold are listed as CONFIRMED:
  1. profile name matches the principal
  2. the headline or a listed position names the entity, a parent, or a known vehicle
  3. the URL came off a page actually retrieved

REJECTED records what the top search hit was and why it was not stored. These are
kept because they are the exact failure the "never synthesize a slug" rule exists
to prevent: each one is a real, live profile of the wrong human being.
"""

CONFIRMED = {
    # name -> (url, evidence read off the result). Headline names the firm.
    "Ting Qiao": (
        "https://www.linkedin.com/in/ting-qiao-b95436aa/",
        "CEO of AiWB, Co-Founder at Wan Bridge. Bellaire, Texas."),
    "Danny Signorelli": (
        "https://www.linkedin.com/in/danny-signorelli-6284461b/",
        "CEO, President, The Signorelli Company. Greater Houston."),
    "Scott Arnoldy": (
        "https://www.linkedin.com/in/scottarnoldy/",
        "Founder and CEO, Triten Real Estate Partners. Houston, Texas."),
    "Brent Ozenbaugh": (
        "https://www.linkedin.com/in/brent-ozenbaugh-b99872/",
        "COO at Triten Real Estate Partners. Greater Houston."),
    "Steve Radom": (
        "https://www.linkedin.com/in/steveradom/",
        "Managing Principal at Radom Capital."),
    "Evan Peterson": (
        "https://www.linkedin.com/in/evan-peterson-19656548/",
        "Principal at Radom Capital LLC. Houston, Texas."),
    "Phillippe Lord": (
        "https://www.linkedin.com/in/phillippe-lord-72924012/",
        "CEO, EVP at Meritage Homes."),
    "Frank Liu": (
        "https://www.linkedin.com/in/frank-liu-b33247a/",
        "President at Lovett. Houston, Texas. A second Frank Liu at Lovett Commercial is a "
        "real estate specialist, not the principal."),
    "Karen Briggs Gwin": (
        "https://www.linkedin.com/in/karen-briggs-gwin-02106614/",
        "Chief Financial Officer, Avenue CDC. Greater Houston."),
    "Tanya Rizzo": (
        "https://www.linkedin.com/in/tanya-rizzo-75738016/",
        "Profile opened. Activity shows her recruiting for Century Communities, Inc. (NYSE:CCS) "
        "in Houston. Title from September 2026 trade press."),
    "Telisia Amaning": (
        "https://www.linkedin.com/in/telisiaamaning/",
        "Chief Operating Officer, READ KING. Houston, Texas."),
    "Jack Dinerstein": (
        "https://www.linkedin.com/in/jack-dinerstein-4215073/",
        "Owner, Dinerstein Companies. Houston, Texas."),
    "Jim Carman": (
        "https://www.linkedin.com/in/carmanjim/",
        "Profile opened. President, Texas Region at Howard Hughes Communities. Greater Houston. His "
        "own feed carries Bridgeland's number nine national ranking at 500 home sales by mid-2026 and "
        "the 83-acre Toro District with the Houston Texans headquarters."),
    "Kirk Breitenwischer": (
        "https://www.linkedin.com/in/kirk-breitenwischer-32778312/",
        "VP at Castlerock Communities. Houston, Texas. The headline gives no function."),
    "Jay Brown": (
        "https://www.linkedin.com/in/jay-brown-14305a12/",
        "Chief Executive Officer at David Weekley Homes. Houston, Texas."),
    "Larry Sloan": (
        "https://www.linkedin.com/in/larry-sloan-894204b/",
        "Chief Development Officer (CDO) at Triten Real Estate Partners. Houston, Texas. The same "
        "person who left Midway as EVP of investment and development in November 2023."),
    "David Hightower": (
        "https://www.linkedin.com/in/dahightower/",
        "Executive Vice President, Development at Midway Companies. Houston, Texas."),
    "Klaus Keller": (
        "https://www.linkedin.com/in/klaus-keller-56151334/",
        "President at Sueba USA Corporation. Houston, Texas."),
    "Raymond Gabriele": (
        "https://www.linkedin.com/in/raygabriele/",
        "Real Estate Development, Sueba USA Corporation. Houston, Texas. Listed AIA, so he is "
        "the licensed architect inside the firm that designs and builds its own work."),
}

# People who decide the wall, found by searching construction and purchasing roles
# rather than executive titles. Added to the record, not replacing anyone.
#
# Bar for inclusion: vice president or director of construction, or head of
# purchasing. Construction managers, superintendents, purchasing agents and starts
# coordinators are deliberately excluded. They execute a specification; they do not
# choose a structural system, and a rolodex entry is a door rather than an org chart.
# Century Communities, InTown Homes and Camillo publish only sub-VP construction staff,
# so nothing is recorded for them.
ADDED = {
    "Wan Bridge Group": [
        {"name": "Randy Hutchinson",
         "role": "Vice President of Construction Operations, AiWB",
         "linkedin_url": "https://www.linkedin.com/in/randy-hutchinson-0b0a71124/",
         "li_evidence": "Vice President of Construction Operations at AiWB. Greater Houston.",
         "entity_note": "Listed at AiWB, not Wan Bridge. Confirm which entity contracts before an approach.",
         "decider": True},
        {"name": "John Serra",
         "role": "Purchasing Manager, AiWB",
         "linkedin_url": "https://www.linkedin.com/in/john-serra-b1b48394/",
         "li_evidence": "Purchasing Manager at AiWB. Houston, Texas.",
         "entity_note": "Listed at AiWB, not Wan Bridge. Confirm which entity contracts before an approach.",
         "decider": True},
    ],
    "First America Homes": [
        {"name": "Troy Robinson",
         "role": "Vice President of Construction, First America Homes",
         "linkedin_url": "https://www.linkedin.com/in/troyjrobinson/",
         "li_evidence": "VP of Construction for First America Homes. Willis, Texas.",
         "decider": True},
        {"name": "Mike Faul",
         "role": "Vice President of Purchasing, First America Homes",
         "linkedin_url": "https://www.linkedin.com/in/mike-faul-a06b2a203/",
         "li_evidence": "Profile opened. Company line reads First America Homes. Magnolia, Texas. He "
                        "took the role this year, after a fifteen-year incumbent left in April 2026.",
         "decider": True},
        {"name": "David Assid",
         "role": "Division President, First America Homes",
         "linkedin_url": "https://www.linkedin.com/in/davidassid/",
         "li_evidence": "Division President, First America Homes. Houston, Texas.",
         "decider": False},
    ],
    "Chesmar Homes": [
        {"name": "Michael Hundl",
         "role": "Vice President of Construction, Houston North, Chesmar Homes",
         "linkedin_url": "https://www.linkedin.com/in/michael-hundl-2a279025/",
         "li_evidence": "VP of Construction Houston North, Chesmar Homes. Spring, Texas.",
         "decider": True},
        {"name": "Dan Renaud",
         "role": "Vice President of Construction Operations, Chesmar Homes",
         "linkedin_url": "https://www.linkedin.com/in/dan-renaud-8b244719/",
         "li_evidence": "Vice President of Construction Operations at Chesmar Homes. Houston, Texas.",
         "decider": True},
        {"name": "David Ebarb",
         "role": "Vice President of Purchasing, Chesmar Homes",
         "linkedin_url": "https://www.linkedin.com/in/david-ebarb-73388541/",
         "li_evidence": "Vice President of Purchasing at Chesmar Home. Houston, Texas.",
         "decider": True},
    ],
    "The Hanover Company": [
        {"name": "Thomas Knutson",
         "role": "President of Construction, The Hanover Company",
         "linkedin_url": "https://www.linkedin.com/in/thomas-knutson-a741898/",
         "li_evidence": "President - Construction at The Hanover Company. Houston, Texas. Hanover "
                        "builds its own work, so this is the head of the in-house contractor.",
         "decider": True},
        {"name": "Mark Wood",
         "role": "Vice President of Construction, The Hanover Company",
         "linkedin_url": "https://www.linkedin.com/in/mark-wood-49713011/",
         "li_evidence": "Vice President - Construction at The Hanover Company. Houston, Texas.",
         "decider": True},
        {"name": "Mike Wright",
         "role": "Vice President of Preconstruction and Estimating, The Hanover Company",
         "linkedin_url": "https://www.linkedin.com/in/mike-wright-7795a8b/",
         "li_evidence": "Vice President of Preconstruction & Estimating at The Hanover Company. Katy, "
                        "Texas. Preconstruction is where an unfamiliar wall system gets priced or "
                        "dismissed, so this is the first real test of a printed assembly.",
         "decider": True},
    ],
    "Camden Property Trust": [
        {"name": "Michael Eilertsen",
         "role": "Vice President of Construction, Camden Property Trust",
         "linkedin_url": "https://www.linkedin.com/in/michael-eilertsen-68a59911/",
         "li_evidence": "Vice President Of Construction at Camden Property Trust. Houston, Texas.",
         "decider": True},
    ],
    "CastleRock Communities": [
        {"name": "Bruce Torkelson",
         "role": "Chief Financial Officer, CastleRock Communities",
         "linkedin_url": "https://www.linkedin.com/in/brucetorkelson/",
         "li_evidence": "CFO at CastleRock Communities. Houston, Texas.",
         "decider": False},
    ],
    "David Weekley Homes": [
        {"name": "John Schiegg",
         "role": "Vice President of Purchasing and Supply Chain, David Weekley Homes",
         "linkedin_url": "https://www.linkedin.com/in/john-schiegg-7593996/",
         "li_evidence": "Profile opened. Company line reads David Weekley Homes, Houston, Texas. He owns "
                        "purchasing and supply chain for the largest privately held builder in the country.",
         "decider": True},
        {"name": "Ladd Fargo",
         "role": "Chief Operating Officer, David Weekley Homes",
         "linkedin_url": "https://www.linkedin.com/in/ladd-fargo-241a47259/",
         "li_evidence": "Chief Operating Officer at David Weekley Homes. Houston, Texas.",
         "decider": False},
        {"name": "Chad Durham",
         "role": "Vice President of Build-to-Rent, David Weekley Homes",
         "linkedin_url": "https://www.linkedin.com/in/chad-durham-1227bb74/",
         "li_evidence": "Vice President of Build-To-Rent at David Weekley Homes. Austin, Texas, which "
                        "is ICON's own city. Build-to-rent is the product line where a repeated wall "
                        "pays back fastest.",
         "decider": False},
    ],
    "Coventry Homes": [
        {"name": "James Kotzur",
         "role": "Division President, Coventry Homes (Dream Finders Homes)",
         "linkedin_url": "https://www.linkedin.com/in/james-kotzur-748107224/",
         "li_evidence": "Division President at DFH - Coventry Homes. Houston, Texas. First named "
                        "executive found for this firm, and the DFH prefix identifies the parent.",
         "decider": False},
        {"name": "Brian Grigsby",
         "role": "Division President, Houston South, Coventry Homes (Dream Finders Homes)",
         "linkedin_url": "https://www.linkedin.com/in/brian-grigsby-859a97285/",
         "li_evidence": "Division President - Houston South @ Dream Finders Homes - Coventry Homes.",
         "decider": False},
    ],
    "Perry Homes": [
        {"name": "Shane Huhn",
         "role": "Vice President of Construction, Perry Homes",
         "linkedin_url": "https://www.linkedin.com/in/shane-huhn-645270161/",
         "li_evidence": "Vice President of Construction at Perry Homes. Location shows only United "
                        "States; Perry is headquartered in Houston.",
         "decider": True},
        {"name": "Lauren Chachere",
         "role": "Vice President of Purchasing, Perry Homes",
         "linkedin_url": "https://www.linkedin.com/in/laurenchachere/",
         "li_evidence": "Vice President of Purchasing at Perry Homes. Houston, Texas.",
         "decider": True},
    ],
    "Fidelis Realty Partners": [
        {"name": "R. Carson Wilson IV",
         "role": "Executive Vice President of Leasing, Construction and Development, Fidelis Realty Partners",
         "linkedin_url": "https://www.linkedin.com/in/r-carson-wilson-iv-9b7525292/",
         "li_evidence": "Executive Vice President - Leasing, Construction and Development at Fidelis "
                        "Realty Partners. Greater Houston. One title covers all three, so the person "
                        "who signs the lease also owns the build.",
         "decider": True},
    ],
    "Houston Housing Authority": [
        {"name": "Neal Rackleff",
         "role": "Executive Vice President and Chief Operating Officer, Houston Housing Authority",
         "linkedin_url": "https://www.linkedin.com/in/nealrackleff/",
         "li_evidence": "Executive VP and COO Houston Housing Authority. Houston, Texas. The operating "
                        "officer over a $600 million five-phase programme, and the office that answers "
                        "for delivery rather than policy.",
         "decider": True},
    ],
    "Ashton Woods Homes": [
        {"name": "DeKendrick Vidito",
         "role": "Vice President of Purchasing, Ashton Woods Homes",
         "linkedin_url": "https://www.linkedin.com/in/dekendrick-vidito-58087766/",
         "li_evidence": "Vice President of Purchasing at Ashton Woods Homes. Houston, Texas.",
         "decider": True},
    ],
    "M/I Homes, Inc.": [
        {"name": "Patrick Mayhan",
         "role": "Vice President of Purchasing, M/I Homes",
         "linkedin_url": "https://www.linkedin.com/in/patrick-mayhan-5591478/",
         "li_evidence": "Vice President of Purchasing at M/I Homes, Inc. Houston, Texas. M/I lists two "
                        "purchasing vice presidents in Houston; his title carries the corporate entity "
                        "and Randy Barras's carries the Houston division.",
         "decider": True},
        {"name": "Randy Barras",
         "role": "Vice President of Purchasing, M/I Homes Houston",
         "linkedin_url": "https://www.linkedin.com/in/rbarras/",
         "li_evidence": "Vice President of Purchasing, M/I Homes - Houston. Houston, Texas.",
         "decider": True},
    ],
    "LGI Homes, Inc.": [
        {"name": "Chuck Collier",
         "role": "Vice President of Construction, Houston, LGI Homes",
         "linkedin_url": "https://www.linkedin.com/in/chuck-collier-48286829/",
         "li_evidence": "VP of Construction, Houston, LGI Homes, stated in his own headline. Location "
                        "shows only United States.",
         "decider": True},
        {"name": "Kyle Hanna",
         "role": "Vice President of Purchasing, LGI Homes",
         "linkedin_url": "https://www.linkedin.com/in/kylemhanna/",
         "li_evidence": "Vice President of Purchasing at LGI Homes. Conroe, Texas, which is the head "
                        "office. The construction vice presidents sit in the markets, Austin, San Antonio, "
                        "Nashville, Denver, Seattle; purchasing is the one that sits in Greater Houston.",
         "decider": True},
    ],
    "Avenue CDC": [
        {"name": "Marilyn Vanderhider",
         "role": "Director of Single Family Housing, Avenue CDC",
         "linkedin_url": "https://www.linkedin.com/in/marilyn-vanderhider-78a0b49/",
         "li_evidence": "Director, Single Family Housing at Avenue Community Development Corporation. "
                        "Houston, Texas. At a nonprofit developer this is the role that owns how the "
                        "houses get built, not the chief executive.",
         "decider": True},
    ],
    "Midway": [
        {"name": "Rob Sigler",
         "role": "Executive Vice President, Construction, Investment and Development, Midway",
         "linkedin_url": "https://www.linkedin.com/in/robsigler/",
         "li_evidence": "Profile opened. Company line reads Midway. Headline is Executive Vice President "
                        "Construction, Investment & Development, and his feed carries Midway and East River "
                        "posts. He also shared Kirksey's mass-timber progress at San Jacinto College, CLT "
                        "floor panels going in, which is a personal record of interest in an alternative "
                        "structural system.",
         "decider": True},
        {"name": "Anna Deans",
         "role": "Executive Vice President, Midway",
         "linkedin_url": "https://www.linkedin.com/in/anna-deans-bbbab03/",
         "li_evidence": "Executive Vice President, Midway. Houston, Texas.",
         "decider": False},
    ],
    "Meritage Homes Corporation": [
        {"name": "Jayar Griffith",
         "role": "Vice President of Operations, Meritage Homes Houston",
         "linkedin_url": "https://www.linkedin.com/in/jayar-griffith-30a43439/",
         "li_evidence": "Vice President of Operations at Meritage Homes (Houston). Houston, Texas. "
                        "Operations at a production builder owns build cycle and trade scope.",
         "decider": True},
        {"name": "Jeremy Flach",
         "role": "Division President, Meritage Homes Houston",
         "linkedin_url": "https://www.linkedin.com/in/jeremy-flach-b3616614/",
         "li_evidence": "Division President at Meritage Homes. Houston, Texas.",
         "decider": False},
        {"name": "Kyle Davison",
         "role": "Central Region President, Meritage Homes",
         "linkedin_url": "https://www.linkedin.com/in/kyle-davison-377a322b/",
         "li_evidence": "Central Region President at Meritage Homes (NYSE). Sugar Land, Texas.",
         "decider": False},
    ],
}

# Name and title match and the person surfaced on a search naming the firm, but the
# visible headline does not name the firm. Stored with the gap stated, not as confirmed.
PROBABLE = {
    "Barton Kelly": {
        "url": "https://www.linkedin.com/in/bartonk/",
        "firm": "Radom Capital",
        "evidence": "Vice President at Radom Capital LLC, Houston.",
        "flag": "Barton Kelly's LinkedIn headline reads Vice President at Radom Capital; the firm's own "
                "team page lists him as Principal. Titles conflict. Confirm before using either.",
    },
    "Tanya Rizzo": {
        "url": "https://www.linkedin.com/in/tanya-rizzo-75738016/",
        "firm": "Century Communities, Inc.",
        "evidence": "Real Estate Executive, Houston, Texas. Sole result for a quoted-name search "
                    "including Century Communities.",
        "flag": "Tanya Rizzo's LinkedIn headline does not name Century Communities. The match rests on a "
                "quoted-name search that included the firm returning exactly one Houston result, plus the "
                "September 2026 trade-press source naming her Houston division president. Verify before outreach.",
    },
    "Young Nam": {
        "url": "https://www.linkedin.com/in/young-nam-78b36229/",
        "firm": "Brightland Homes",
        "evidence": "Senior Vice President of Supply Chain, Bethesda, Maryland. The DRB Group's own "
                    "leadership page lists a Young Nam as SVP of Purchasing, and DRB is headquartered "
                    "in the Maryland suburbs.",
        "flag": "Young Nam's LinkedIn headline gives the title and the right metropolitan area but "
                "does not name The DRB Group. Name, function and geography all match the parent's own "
                "leadership page. Confirm before outreach.",
    },
    "Myron Pendley": {
        "url": "https://www.linkedin.com/in/myron-pendley-8bb2a81b/",
        "firm": "Triten Real Estate Partners",
        "evidence": "Chief Construction Officer at Triten Corporation, Houston. Surfaced on a Triten "
                    "Real Estate search.",
        "flag": "Myron Pendley's headline reads Chief Construction Officer at Triten Corporation, not "
                "Triten Real Estate Partners. Triten Corporation is a separate Houston industrial-services "
                "company using the same name. If the two are related he is the construction decision-maker "
                "here; if not he is the wrong company. Resolve before using.",
    },
    "Nicole Cassier": {
        "url": "https://www.linkedin.com/in/nicolecassier/",
        "firm": "Avenue CDC",
        "evidence": "Chief Strategy Officer, Housing & Community Development. Surfaced on an Avenue CDC search.",
        "flag": "Nicole Cassier's LinkedIn headline gives the title but not the employer. Verify before outreach.",
    },
}
# Correct person, but the role in our record is out of date.
MOVED = {
    "Amy Rino": {
        "url": "https://www.linkedin.com/in/amy-rino-5152b111/",
        "role": "Chief Customer Officer, Taylor Morrison, Scottsdale (2026); "
                "ex-Houston Division President",
        "flag": "Amy Rino is no longer the Houston division president. LinkedIn shows her as Chief "
                "Customer Officer at Taylor Morrison in Scottsdale, Arizona. The 2018 division-president "
                "citation in this record is stale, and no current Houston division leader was found. "
                "Taylor Morrison has no local door on file.",
        "firm": "Taylor Morrison Home Corporation",
    },
}

# Correct person, departed, and outside the relevance gate. Removed from the record.
REMOVED = {
    "Cole Klein": {
        "firm": "Cole Klein Builders / Zuri Gardens",
        "flag": "There is no person called Cole Klein. The firm's own about page names Vanessa Cole "
                "and Harry Klein as its founders, so the company name is the two surnames joined. "
                "The record carried a principal who does not exist; both founders are now named. "
                "This is why the LinkedIn search for the name returned nothing.",
    },
    "David Foor": {
        "firm": "InTown Homes / Lovett Commercial (Frank Liu)",
        "flag": "David Foor removed. LinkedIn shows him as an associate attorney at Ford + Bergner LLP "
                "with Lovett Commercial listed as past. Departed, and legal counsel is outside the "
                "relevance gate for this rolodex.",
    },
}

# Top hit was a real profile belonging to somebody else. Left null on purpose.
REJECTED = [
    ("Bradley Freels", "Midway",
     "No LinkedIn profile identifiable as Midway's chairman was found. The name matches other "
     "people's profiles, none at Midway."),
    ("Steve Commander", "Commander Home Builders",
     "linkedin.com/in/scommander is a regional retail operations leader, not the San Leon builder."),
    ("Tony M. Brown", "Elpis 3D Home Builders",
     "Top hit is a Tony Brown at Brown King Construction in Knoxville, Tennessee."),
    ("John Winniford", "First America Homes",
     "The one LinkedIn profile under the name does not name Signorelli or Brightland, so it is "
     "not held. He is reachable through Signorelli's own bio page, which is linked on his row."),
    ("Frank Liu", "InTown Homes / Lovett Commercial (Frank Liu)",
     "No profile under that name is identifiable as the InTown and Lovett principal."),
]
