# -*- coding: utf-8 -*-
"""Round three: what an outside reader found, and what it cost.

This round came from a review of the shipped deck rather than from a pass over
the data, and that is the finding about the method. Every correction below is
something the gates could not see, because each one is a sentence that was true
when it was written and stopped being true when the data moved underneath it.

The meta description said sixty-one firms. The roster said ninety-six. Nobody
saw it for thirty builds because it lives in the document head, where no view
renders it and no check read it. It is the line a Slack unfurl and a LinkedIn
card quote, so the preview of the page contradicted the headline of the page.
It is generated from the roster count now, and verify.py fails the build if the
two ever diverge again.

The Sources block claimed every contact was either a LinkedIn profile or a page
on the firm's own site. Forty of the two hundred and forty-one are neither: a
name carried from a page that named them, at a firm that publishes no staff page
to link. The search icon on those cards was already saying so. The sentence was
the only thing on the deck that was not, and it was falsifiable in four clicks
in the section that invites auditing. It prints the three counts now.

Three cards could not be opened. Two of them had already been found: earlier
rounds dropped the Houston Housing Authority's homepage and GreenEco's, because
one stopped resolving and the other led to a parked domain. Neither round set
`no_web_presence`, so those cards rendered as though a website simply had not
been looked for, while Cole Klein, Commander and Elpis carried the flag for the
same condition. Same fact, two presentations, which is the shape of an
inconsistency rather than a lie.

The Houston Housing Authority one was not an absence at all. The authority now
publishes as Housing Alliance HTX on a domain that resolves, with a leadership
page naming both people this deck carries. The old URL had not died; it moved.
"""

# ---------------------------------------------------------------- web presence

# A card with no openable page says so, the same way the three firms that never
# had a site say it. Without this a reader cannot tell "no site" from "nobody
# checked", and the deck already distinguishes those everywhere else.
NO_WEB = {
    "HOU-078": "Its published domain, greenecobuilds.com, has no DNS record at all. The "
               "similarly spelled greenecobuilders.com answers, and serves a parked-domain "
               "lander. The builder was bought by Rausch Coleman in 2020 and Lennar completed "
               "its purchase of Rausch Coleman on 10 February 2025.",
    "HOU-032": "The one page the card cited returns nothing to a script and redirects off the "
               "firm's own domain in a browser.",
    "HOU-127": "livelonestar.com answers 401 Forbidden to a browser and to a script, on both "
               "the bare domain and the www host. Nothing the firm publishes about itself "
               "can be read, which is also why this card names no one.",
    # These three already carried the flag and said nothing about it on the page,
    # because until Build 59 nothing rendered it. The flag without the sentence
    # is the same silence in a different place.
    "HOU-002": "No corporate site was found for the builder. This card stands on dated "
               "reporting of the project instead.",
    "HOU-016": "No corporate site was found for the builder. This card stands on dated "
               "reporting of the project instead.",
    "HOU-017": "No corporate site was found for the builder. This card stands on dated "
               "reporting of the project instead.",
}

# livelonestar.com is on the card as a website button that cannot be opened. A
# button that 401s is worse than no button, which is the rule audit.py already
# applied to GreenEco's parked domain.
DROP_HOMEPAGE = {"HOU-127"}

# ---------------------------------------------------------------- the rebrand

# The authority did not lose its site. It renamed. Both pages below were fetched
# and tested for the strings: /leadership carries Bryant and Rackleff with
# titles in its visible text and in its structured data, and /about carries
# "Houston Housing Authority" as the alternate name, which is what ties the new
# domain to the entity this card is about.
HOMEPAGE = {
    "HOU-003": "https://www.alliancehtx.org/",
}
TEAM_URL = {
    "HOU-003": ("https://www.alliancehtx.org/leadership",
                "The authority publishes as Housing Alliance HTX. Its about page carries "
                "Houston Housing Authority as the alternate name, and its own releases still "
                "use both."),
}
# The chief executive had a search link and no page. She has a page.
PERSON_SOURCE = {
    ("HOU-003", "Jamie Bryant"): (
        "https://www.alliancehtx.org/team-members/jamie-bryant",
        "Her own bio page gives the title and the February 2025 appointment."),
    ("HOU-003", "Neal Rackleff"): (
        "https://www.alliancehtx.org/leadership",
        "The leadership page carries the title."),
}
