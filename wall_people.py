# -*- coding: utf-8 -*-
"""The contact layer for the 28 firms Build 62 added, and three corrections.

Build 62 shipped 28 records with 21 people between them, no LinkedIn profile, no
source page, no decision-maker mark and no phone number. Fifteen of the 28 had
nobody named at all. A rolodex whose new half cannot be called is not a rolodex,
and the deck's own headline stat quietly recorded it: 43 with a decision-maker
named was 45 percent of the roster at Build 61 and 35 percent at Build 62,
because the strip prints an absolute where the meaning is a proportion.

Four sweeps went back over the 28. Three of them corrected something already
shipped, which is the case for running the pass rather than trusting the first
one.

  DSRS Steel published three executives, David S. R. Stevens, Michael Henderson
  and Sarah Miller, and none of them can be corroborated anywhere: no profile,
  no coverage, no second page. The firm's own published contact address is
  dshultis@dsrssteel.com and its phone is shared with DSRS Development, whose
  page names Dean Shultis and Ralph Sharp as founders. DSRS is their initials.
  Those three names read as unreplaced website template filler, and they are off
  the card. This deck shipped three names that were probably never people.

  Tindall's Texas general manager changed on 5 August 2025. Greg Elliott was the
  outgoing one and the record quoted him, so the card was pointing at last year's
  decision-maker. Cecil Casinger has the seat.

  Heldenfels' own about page still calls Chad Petro Senior Vice President and
  General Manager. Metromont's acquisition release calls him President and Chief
  Executive Officer and says he continues in it. The firm's site is stale and the
  deck was repeating the stale title.

Two more things the pass turned up that change the pitch rather than the record.
All About Concrete was bought by High Street Capital in August 2026, so its
founder still signs and a sponsor now sits behind him. And Wells is under a
pending KPS Capital Partners acquisition. Both are on their cards.

A LinkedIn URL here was seen in a search result listing with the firm visible in
the headline. None of them fetched: LinkedIn refuses. That is the same standard
the rest of the deck holds, and probe.py skips the host for the same reason.
"""

# ------------------------------------------------------------------- removals
# (target_id, name) pairs to take off the deck, with why.
DROP_PEOPLE = {
    ("HOU-152", "David S. R. Stevens"):
        "Published on dsrssteel.com as Director and corroborated nowhere: no "
        "profile, no coverage, no second page on the firm's own site. The "
        "three names under that heading read as website template filler.",
    ("HOU-152", "Michael Henderson"):
        "Same heading, same absence of any corroboration.",
}

# ------------------------------------------------------------------- the people
# tid -> [(name, role, linkedin, source_url, evidence, decider)]
# linkedin and source_url may be None. decider marks the person who can sign for
# capital equipment: the owner, the president, the general manager or the
# division head, which is the rule the deck already applies to a contractor.
PEOPLE = {

# ---- precast
"HOU-137": [
 ("Hussein Sinjari", "Vice President",
  "https://www.linkedin.com/in/hussein-sinjari-53376545",
  "https://www.legacyprecast.com/contact-us",
  "The firm's own contact page carries him as vice president. It publishes no "
  "president, owner or founder, so this is the highest rank Legacy discloses.",
  True),
 ("Charles Franke", "Chief of Estimating", None,
  "https://www.legacyprecast.com/contact-us",
  "The firm's own contact page. Estimating prices a method rather than choosing "
  "one.", False)],

"HOU-138": [
 ("Dan Juntunen", "Chief Executive Officer, Wells",
  "https://www.linkedin.com/in/dan-juntunen-b2765a14/", None,
  "Quoted as chief executive in KPS Capital Partners' acquisition release of 10 "
  "February 2026. Wells publishes no Texas leader and no plant manager: its "
  "company team page lists 36 people and not one carries a state or a plant in "
  "the title, so the corporate officer is the only published authority.", True)],

"HOU-139": [
 ("Asher Kazmann, P.E.", "President",
  "https://www.linkedin.com/in/asherkazmann/",
  "https://lockesolutions.com/people/",
  "The firm's own leadership page, and its own post of 10 September 2025 naming "
  "him a Houston Business Journal Most Admired CEO honoree.", True),
 ("Ivan Garcia", "Chief Financial Officer", None,
  "https://lockesolutions.com/people/",
  "The firm's own leadership page. The second signature on a capital purchase.",
  False),
 ("David Espino", "Director of Operations", None,
  "https://lockesolutions.com/people/",
  "The firm's own leadership page.", False),
 ("Chad Arpe", "Director of Sales and Marketing",
  "https://www.linkedin.com/in/chad-arpe-b1981050/",
  "https://lockesolutions.com/people/",
  "The firm's own leadership page. He is the name the precast trade directory "
  "lists as Locke's contact, and the title resolves him as sales.", False)],

"HOU-140": [
 ("Robert May", "Business Development",
  "https://www.linkedin.com/in/robert-may-18560560", None,
  "The Texas precast association names him as Tricon's contact and his own "
  "profile headline gives the function. Tricon publishes no leadership of any "
  "kind on any page that could be read, so there is no decision-maker to mark.",
  False)],

"HOU-141": [
 ("Garrett Weidman, P.E.", "Sales Manager", None,
  "https://www.coreslab.com/locations/austin-texas-precast-concrete/",
  "The plant's own page, with a direct line.", False),
 ("Bruce Wardlaw", "Project Consultant, Houston, East Texas and Multifamily",
  None, "https://www.coreslab.com/locations/austin-texas-precast-concrete/",
  "The plant's own page. The only staffing on this deck that names Houston and "
  "multifamily in one title.", False),
 ("Robb Harrington", "Project Consultant, Dallas-Fort Worth and North Texas",
  None, "https://www.coreslab.com/locations/austin-texas-precast-concrete/",
  "The plant's own page, which completes the Texas coverage map.", False)],

"HOU-142": [
 ("Chad Petro", "President and Chief Executive Officer",
  "https://www.linkedin.com/in/chad-petro-89b7a913/",
  "https://concreteproducts.com/index.php/2026/02/09/heldenfels-deal-positions-metromont-at-the-heart-of-texas-market/",
  "Metromont's chief executive names him as the continuing president and chief "
  "executive in the acquisition coverage of 9 February 2026. The firm's own "
  "about page still says Senior Vice President and General Manager and has not "
  "been updated.", True),
 ("Larry Miller, P.E.", "Vice President, Preconstruction and Business Development",
  None, "https://heldenfels.com/contact/", "The firm's own contact page.", False),
 ("Fred W. Heldenfels IV", "Founder", None, "https://heldenfels.com/about-us/",
  "The firm's own about page: he formed the company in 1995 and bought the "
  "precast and prestressed division assets. He sold to Metromont in December "
  "2025 and is likely exiting.", False)],

"HOU-143": [
 ("Cecil Casinger", "General Manager, Tindall Building Systems Texas", None,
  "https://tindallcorp.com/tindall-corporation-welcomes-new-general-manager/",
  "The firm's own release of 5 August 2025 welcoming him as general manager of "
  "the Texas division, with eighteen years in precast.", True),
 ("Greg Elliott", "Vice President, and the outgoing Texas general manager",
  "https://www.linkedin.com/in/greg-elliott-824a1458/",
  "https://tindallcorp.com/tindall-corporation-welcomes-new-general-manager/",
  "The same release identifies him as vice president and the outgoing general "
  "manager. His own profile headline still carries the general manager title, "
  "so a reader searching him will find the old seat.", False)],

"HOU-144": [
 ("Dan Juntunen", "Chief Executive Officer, Wells",
  "https://www.linkedin.com/in/dan-juntunen-b2765a14/", None,
  "The Hillsboro page names nobody, and this plant is the former Gate Precast "
  "architectural yard whose own leadership pages went when gateprecast.com "
  "started redirecting to wells.build. Corporate is the only published "
  "authority for either Texas site.", True)],

"HOU-145": [
 ("Kevin Medlin", "President",
  "https://www.linkedin.com/in/kevin-medlin-8693832b/",
  "https://www.napcoprecast.com/the-company/our-story",
  "The firm's own history, in the present tense: with president Kevin Medlin "
  "leading the company, NAPCO is expanding its portfolio and additional product "
  "lines.", True),
 ("Jaime Iragorri", "Founder", None,
  "https://www.napcoprecast.com/the-company/our-story",
  "The firm's own history: established NAPCO in 1995.", False)],

# ---- panel
"HOU-146": [
 ("Shane McCullough", "President", None,
  "https://futureframeusa.com/meet-our-team/",
  "The firm's own team page. Top officer of a single-plant manufacturer.", True),
 ("Glen Gilbert", "General Manager", None,
  "https://futureframeusa.com/meet-our-team/",
  "The firm's own team page. He runs the New Caney plant, which is the asset a "
  "machine would land in.", True),
 ("Brent Wheat", "Design Manager", None,
  "https://futureframeusa.com/meet-our-team/", "The firm's own team page.", False),
 ("Larry Howard", "Senior Account Manager",
  "https://www.linkedin.com/in/larry-howard-ab995b92/",
  "https://futureframeusa.com/meet-our-team/",
  "The firm's own team page gives this title. His profile headline reads "
  "general manager, so one of the two is out of date.", False)],

"HOU-147": [
 ("Jeff Oliver", "Director of Truss and Wall Panels",
  "https://www.linkedin.com/in/jeff-oliver-ab686814/", None,
  "His profile headline names the company and the product line. No geography is "
  "visible on it, so whether the Houston plants sit under him is not "
  "established. Builders FirstSource publishes corporate officers only and "
  "names no manager on any of its four Houston-area plant pages.", False)],

"HOU-148": [
 ("Brandon Buskohl", "Assistant General Manager",
  "https://www.linkedin.com/in/brandon-buskohl-40649a75/", None,
  "His profile headline names Trussway Manufacturing as a Builders FirstSource "
  "company, so it is current. An assistant general manager is below the bar "
  "this deck sets for a decision-maker. He is also the only plant-level leader "
  "the firm could be shown to have. trussway.com presents a certificate chain "
  "that fails verification through every route, so nothing on it could be read.",
  False)],

"HOU-149": [
 ("Dwain Hutton", "Executive Vice President, UFP Site Built", None,
  "https://ufpsitebuilt.com/leadershipteam",
  "The division's own leadership page. He heads the Site Built division, which "
  "is one level below UFP Industries corporate and the lowest published rung "
  "that would sign for a plant. Every regional role the page names is West, and "
  "the Huntsville plant page names nobody.", True)],

"HOU-150": [
 ("Don Groom", "President, Chief Executive Officer and Managing Partner",
  "https://www.linkedin.com/in/don-groom-a60811147",
  "https://www.trussworksllc.net/staff/don-groom",
  "His own staff page on the firm's site. Managing partner is ownership, not "
  "just office.", True),
 ("Justin Groom", "Executive Vice President, Manufacturing and Distribution",
  None, "https://www.trussworksllc.net/our-team",
  "The firm's own team page. He owns the plant floor.", True),
 ("Mike Bellows", "Partner", None, "https://www.trussworksllc.net/our-team",
  "The firm's own team page.", False),
 ("Tony Urban", "Partner", None, "https://www.trussworksllc.net/our-team",
  "The firm's own team page.", False)],

"HOU-151": [
 ("Mark Furse", "Market President",
  "https://www.linkedin.com/in/mark-furse-02b1b717/", None,
  "His profile headline names Texas Building Supply and a market president is a "
  "regional profit-and-loss seat. Which market is not visible on it, and he is "
  "separately associated with the San Antonio legacy banner, so whether he "
  "covers Houston is unconfirmed. The company publishes no leadership at all on "
  "its own site.", False)],

"HOU-152": [
 ("Dean Shultis", "Co-founder", None, "https://www.mccannpark.com/about",
  "The development company that shares this firm's telephone line names Dean "
  "Shultis and Ralph Sharp as its founders, and the contact address published "
  "in the steel firm's own footer is dshultis@dsrssteel.com. DSRS is the two "
  "surnames.", True),
 ("Ralph Sharp", "Co-founder", None, "https://www.mccannpark.com/about",
  "Named as co-founder on the same page.", False)],

"HOU-153": [],   # publishes no name anywhere

"HOU-155": [
 ("Paul McCurdy", "Chief Executive Officer", None,
  "https://www.citymasonry.com/team/",
  "The firm's own team page, and the Associated Masonry Contractors of Houston "
  "names him as the firm's principal contact with the same main line.", True),
 ("Glenn Whitehead", "Chief Operating Officer", None,
  "https://www.citymasonry.com/team/", "The firm's own team page.", False),
 ("Brad Burrows", "Chief Financial Officer", None,
  "https://www.citymasonry.com/team/", "The firm's own team page.", False),
 ("Edwin Rosales", "Vice President of Operations", None,
  "https://www.citymasonry.com/team/", "The firm's own team page.", False)],

"HOU-156": [
 ("Robert V. Barnes III", "President and Chief Executive Officer", None,
  "https://www.dmagazine.com/publications/d-ceo/2023/august/third-generation-family-run-company-dee-brown-inc-has-had-a-hand-in-some-of-north-texas-most-iconic-buildings/",
  "Named as president and chief executive in D CEO of 24 August 2023, which "
  "records that he took the seat in 2015 from his father. Also on the firm's "
  "own about page. No Houston division head is published, so the Tomball office "
  "has no separate signing authority.", True),
 ("Tim Hughes", "Senior Vice President, Construction Management", None,
  "https://www.deebrowncompanies.com/about", "The firm's own about page.", False),
 ("David Barnes", "Senior Vice President, Operations", None,
  "https://www.deebrowncompanies.com/about", "The firm's own about page.", False)],

"HOU-157": [
 ("Kevin M. Camarata", "Founder and Chief Executive Officer",
  "https://www.linkedin.com/in/kevin-camarata-6883731b9/",
  "https://members.agchouston.org/directory/Details/camarata-masonry-systems-ltd-2123442",
  "The firm's own about page gives him as founder, dated 1 August 2004. AGC "
  "Houston and his own profile headline both carry the chief executive title. "
  "He also chairs the Natural Stone Foundation.", True)],

"HOU-158": [
 ("Gerald Guzman", "President", None,
  "https://members.agchouston.org/directory/Details/winco-masonry-inc-2123266",
  "The AGC Houston member directory, which is the only non-aggregator source "
  "naming him. Winco's own site publishes no leadership at all: the only people "
  "on it are three clients in testimonials.", True)],

"HOU-159": [
 ("David Veazey", "President",
  "https://www.linkedin.com/in/david-veazey-0b585b17/",
  "https://masoncontractors.org/5-on-5/veazey-enterprises/",
  "His profile headline carries the title, and he writes the Mason Contractors "
  "Association interview under his own byline. The firm's own site names nobody.",
  True),
 ("Sharon Stelter", "Vice President", None,
  "https://members.asaonline.com/directory/Details/veazey-enterprises-inc-542938",
  "The American Subcontractors Association directory.", False)],

# ---- nozzle
"HOU-160": [
 ("Jonas Barboza", "Regional Director South, Texas",
  "https://www.linkedin.com/in/jonas-barboza-9794a1136/",
  "https://brundagebone.com/about/",
  "The firm's own management page. Regional director sits between the branch "
  "and the vice president of operations, and the Texas region is his. The vice "
  "president of operations named on that page has a scope that excludes Texas, "
  "so Houston escalates to the division president rather than through him.",
  True),
 ("Mark Young", "President, US Concrete Pumping", None,
  "https://brundagebone.com/about/",
  "The firm's own management page, and the parent's investor page. The division "
  "president above the Texas region, and not the public parent's chief "
  "executive.", False)],

"HOU-161": [
 ("Francisco Trevino", None,
  "https://www.linkedin.com/in/francisco-trevino-3b122822b/", None,
  "His profile headline names the company. No title is visible on it and the "
  "firm publishes no leadership anywhere on its own site, where his name "
  "appears only in a page's author metadata. He is the only person this firm "
  "can be connected to in any source this deck will use, and his role is "
  "unknown.", False)],

"HOU-162": [],   # publishes no name anywhere

# ---- slab
"HOU-163": [
 ("Gary Engasser", "President",
  "https://www.linkedin.com/in/gary-engasser-1b39b219/",
  "https://www.sec.gov/Archives/edgar/data/874238/000117184317001952/exh_991.htm",
  "Named as a co-founder staying with the company in Sterling's own acquisition "
  "release of 3 April 2017, filed with the SEC, and carried as president on the "
  "firm's own leadership page. President of the operating company rather than a "
  "Sterling corporate officer.", True),
 ("Rick Callihan", "Vice President", None,
  "https://www.tealstonelp.com/who-we-are/", "The firm's own leadership page.",
  False),
 ("Logan Lippoldt", "General Superintendent", None,
  "https://members.ghba.org/memberdirectory/Details/tealstone-residential-concrete-1307510",
  "The Greater Houston Builders Association lists him as the primary contact at "
  "Tealstone's Houston address on Fernbush Drive. A superintendent executes a "
  "specification rather than choosing one, and he is the named Houston contact "
  "at a firm whose leadership is in Denton.", False)],

"HOU-164": [
 ("Nathan Frazier", "Founder and Chief Executive Officer",
  "https://www.linkedin.com/in/nathan-frazier-frazier-528106104",
  "https://www.highstreetcapital.com/news/high-street-capital-invests-in-all-about-concrete/",
  "High Street Capital's announcement of its investment, August 2026, names him "
  "as founder and confirms him continuing as chief executive. The firm's own "
  "site has a Leadership heading that names nobody.", True),
 ("Don Edwards", "Chief Operating Officer", None,
  "https://www.highstreetcapital.com/news/high-street-capital-invests-in-all-about-concrete/",
  "Named in the same announcement as continuing chief operating officer.", False)],

"HOU-165": [
 ("Don Jackson", "Owner and President",
  "https://www.linkedin.com/in/don-jackson-2366351a/",
  "https://solidfoundationsltd.com/about.php",
  "The firm's own about page: started in 1999 by its owner and president. His "
  "profile headline carries the firm, which matters because the name is a "
  "common one. The only person this firm publishes.", True)],
}


# ------------------------------------------------------------------ the numbers
# tid -> (ten digits, label, source url, rule)
# Rules follow phones.py: 1 the page publishes one number; 2 the page designates
# a main line; 3 the page gives a local office for this metro; 5 the page
# publishes several and designates none.
PHONE = {
 "HOU-137": ("2813752050", "direct line", "https://www.legacyprecast.com/contact-us", 5),
 "HOU-138": ("2814853273", "Pearland plant", "https://wells.build/contact/locations/pearland-texas/", 3),
 "HOU-139": ("8328047062", "the only number published",
             "https://lockesolutions.com/contact-us/", 1),
 "HOU-140": ("2819319832", "Houston, Henry Road", "https://tricon-industrial.com/contact", 3),
 "HOU-141": ("5122500755", "main", "https://www.coreslab.com/locations/austin-texas-precast-concrete/", 2),
 "HOU-142": ("5123962376", "San Marcos main", "https://heldenfels.com/contact/", 2),
 "HOU-143": ("8002801215", "Texas division main", "https://tindallcorp.com/contact/", 2),
 "HOU-144": ("2545827200", "Hillsboro plant", "https://wells.build/contact/locations/hillsboro-texas/", 3),
 "HOU-145": ("2105099100", "the only number published", "https://www.napcoprecast.com/contact", 1),
 "HOU-146": ("2812319200", "Conroe office", "https://futureframeusa.com/contact/", 1),
 "HOU-147": ("9367032950", "Cut N Shoot plant",
             "https://www.bldr.com/location/cut-n-shoot-tx-truss/CUTNTXMF", 3),
 "HOU-148": ("7136916900", "Houston, Alcorn Street",
             "https://www.sbcacomponents.com/tmat-directory/trussway", 3),
 "HOU-149": ("9362953411", "Huntsville plant",
             "https://ufpsitebuilt.com/our-locations/huntsville-tx", 3),
 "HOU-150": ("9795670400", "the line published against every location",
             "https://www.trussworksllc.net/locations", 5),
 "HOU-151": ("2814470384", "Houston branch", "https://texasbuildingsupply.com/locations", 3),
 "HOU-152": ("5129649960", "the only number published", "https://dsrssteel.com/", 1),
 "HOU-153": ("2817991501", "call or text", "https://txlitegaugesteel.com/", 5),
 "HOU-155": ("7136911000", "main office", "https://www.citymasonry.com/contact-us/", 2),
 "HOU-156": ("2815470030", "Houston office", "https://www.deebrowncompanies.com/contact", 3),
 "HOU-157": ("2818761111", "main", "http://www.camaratamasonry.com/", 2),
 "HOU-158": ("2813542515", "the only number on the firm's own site",
             "http://www.wincomasonry.com/", 1),
 "HOU-159": ("7136956500", "main line", "https://vzmasonry.com/", 2),
 "HOU-160": ("7134551464", "West Old Spanish Trail yard",
             "https://brundagebone.com/locations/houston/", 5),
 "HOU-161": ("7135883500", "the only number published", "https://texconpumping.com/", 1),
 "HOU-162": ("9725323340", "Dallas, the only number published",
             "https://omegaindinc.com/houston/contact-us/", 1),
 "HOU-163": ("9403832887", "Denton office, the only number on the firm's own site",
             "https://www.tealstonelp.com/contact-us/", 1),
 "HOU-164": ("2813704470", "Tomball", "https://allaboutconcretellc.net/partner-with-us/", 1),
 "HOU-165": ("2817984821", "main", "https://solidfoundationsltd.com/about.php", 2),
}

# Second and further numbers. A third element gives the page, for a number the
# firm publishes somewhere other than the page its main line sits on.
MORE = {
 "HOU-137": [("8554425502", "toll free")],
 "HOU-140": [("8773874266", "toll free")],
 "HOU-142": [("3615331031", "Corpus Christi office")],
 "HOU-147": [("9362732256", "Conroe plant",
              "https://www.bldr.com/location/conroe-tx-truss/CONRTXMF")],
 "HOU-149": [("2545802846", "Hillsboro plant", "https://ufpsitebuilt.com/our-locations"),
             ("2542464767", "Temple plant", "https://ufpsitebuilt.com/our-locations")],
 "HOU-151": [("2103376474", "San Antonio and Taylor component plants"),
             ("9037120071", "Van Alstyne component plant")],
 "HOU-153": [("8324558883", "framing packages",
              "https://txlitegaugesteel.com/inquiry.html")],
 "HOU-156": [("2143216443", "Dallas office")],
 "HOU-157": [("9544268352", "Florida office"), ("9803089922", "North Carolina office")],
 "HOU-160": [("2815288484", "Sellers Road yard, trading as HiTech")],
 "HOU-163": [("9402686691", "the number registered against the Houston address",
              "https://members.ghba.org/memberdirectory/Details/tealstone-residential-concrete-1307510")],
}

# What the card should say about the number, where the number needs explaining.
NOTE = {
 "HOU-138": "The plant's own line. Wells publishes a corporate switchboard as well, and it is the same number for both Texas plants, so it is not carried on either record.",
 "HOU-144": "The plant's own line. Wells names no Texas leader at either plant, so an escalation from here goes to the corporate office rather than to a manager on site.",
 "HOU-150": "The firm prints this one line against all eight of its locations, "
            "so it is a central number rather than the Caldwell plant.",
 "HOU-160": "Two Houston yards, neither designated the main line. Corporate is "
            "in Denver and is not carried here.",
 "HOU-162": "A Dallas number. Houston is a service area page rather than a "
            "staffed office: no Houston address and no Houston line is published.",
 "HOU-163": "The firm's own site publishes only the Denton office. The Greater "
            "Houston Builders Association carries a Houston address on Fernbush "
            "Drive against a second number, which also has a Denton area code.",
 "HOU-152": "One line serves both this firm and DSRS Development, and it "
            "carries an Austin area code on a Houston address.",
 "HOU-153": "Two numbers, neither designated the main line, and the site never "
            "states a city. The firm's own social accounts put it in Rosharon.",
}

# ------------------------------------------------------------------ the notes
# Sentences that go on the card as open items, because they change who signs.
FLAGS = {
 "HOU-138": ["KPS Capital Partners agreed to acquire Wells on 10 February 2026. "
             "A sponsor change puts capital authority in motion."],
 "HOU-142": ["Metromont completed its acquisition on 15 December 2025 and "
             "retained Chad Petro. The first year under a new parent is when a "
             "producer's capital budget gets rewritten.",
             "The firm's own about page still carries his pre-acquisition title."],
 "HOU-143": ["The Texas general manager changed on 5 August 2025. Greg Elliott's "
             "own profile still carries the general manager title, so a reader "
             "searching him will find the seat he has left."],
 "HOU-147": ["No Houston-area or Texas leader is published. Two of the four "
             "Houston plant pages render only a corporate shell to a fetcher, so "
             "their facility types could not be confirmed."],
 "HOU-148": ["trussway.com presents a certificate chain that fails verification "
             "through every route tried, so nothing on the firm's own site could "
             "be read."],
 "HOU-152": ["The three executives published on the firm's own site could not be "
             "corroborated anywhere and are not carried here. The founders named "
             "on the development company that shares its phone line are."],
 "HOU-161": ["The firm publishes no leadership. The one name attached to it "
             "appears in a page's author metadata and on a profile headline, "
             "with no title on either."],
 "HOU-162": ["No founder, owner or officer is named anywhere on the firm's site "
             "or in any coverage found."],
 "HOU-164": ["High Street Capital announced its investment in August 2026, "
             "keeping the founder as chief executive. A sponsor now sits behind "
             "the signature.",
             "The Texas Association of Builders directory names a different "
             "person as president and chief executive. The dated August 2026 "
             "announcement is the better source and the conflict is unresolved."],
}


# --------------------------------------------------------------- the absences
# A card with nobody on it has to say why, the same way a card with no website
# does. Build 62 shipped fifteen of these and every one of them was silent, so a
# reader could not tell "this firm publishes no leadership" from "nobody looked".
# audit_flags has been empty since Build 41, when open items came off the page,
# so an absence now lives in its own field and renders where the contacts would.
NO_PEOPLE = {
 "HOU-162": "No founder, owner, president or officer is named anywhere on the "
            "firm's own site, in its blog, on its careers page or in any "
            "coverage found. The only personal names on the site are two first "
            "names in customer testimonials.",
 "HOU-153": "The firm names nobody on any page: not the home page, the about "
            "panel, the FAQ or the inquiry page, and no name surfaced in search. "
            "It does not state a city either.",
}

# The three that were already on the deck and already silent. Same condition,
# same treatment.
NO_PEOPLE.update({
 "HOU-127": "livelonestar.com answers 401 Forbidden to a browser and to a "
            "script on both hosts, so nothing the firm publishes about itself "
            "can be read, including who runs it.",
 "HOU-124": "The builder publishes no leadership page and names no one on the "
            "pages that could be read. Its ICF adoption is documented and its "
            "people are not.",
 "HOU-074": "The builder's own site renders its people from script, so a fetch "
            "returns the page without them. The same rendering is why no number "
            "could be read off it either.",
})


# ------------------------------------------------------------- read by hand
# Pages that refuse a script and serve a browser, with the numbers that were on
# them. A host answering 403 is not evidence of anything, so these are recorded
# as read rather than left unknown, dated, with what was seen.
VERIFIED = {
 "https://wells.build/contact/locations/pearland-texas/":
     "2026-09-14: the Pearland plant page, 3201 Veterans Dr, with 281.485.3273 "
     "as the location's contact number and a stated 55-plus team members.",
 "https://wells.build/contact/locations/hillsboro-texas/":
     "2026-09-14: the Hillsboro page, 1220 and 1700 N Waco Street, with "
     "254.582.7200 as the location's main contact line.",
 "https://tricon-industrial.com/contact":
     "2026-09-14: Tricon Industrial, a division of Tricon Precast, at the same "
     "15055 Henry Road address. Telephone 281-931-9832, toll free "
     "877-387-4266, fax 281-931-0061. The 281 number matches the one the Texas "
     "precast association lists for Tricon Precast.",
 "http://www.camaratamasonry.com/":
     "2026-09-14: Main 281-876-1111, fax 281-876-1120, Florida office "
     "954-426-8352, North Carolina office 980-308-9922. AGC Houston lists the "
     "same main line.",
 "http://www.wincomasonry.com/":
     "2026-09-14: one number, 281.354.2515, with 21240 West Hammond Drive, "
     "Porter. The AGC Houston listing adds 281-354-1655, which is not on the "
     "firm's own site and is almost certainly the fax, so it is not carried.",
 "https://brundagebone.com/locations/houston/":
     "2026-09-14: two Houston yards. 4707 West Old Spanish Trail Drive at "
     "713-455-1464, and 15503 Sellers Rd trading as HiTech at 281-528-8484. "
     "Neither is designated the main line. Corporate is 303-289-7497 in Denver "
     "and is not carried.",
}
