# -*- coding: utf-8 -*-
"""Unit tests for the pure helpers the builds and the gates rest on.

Standard library only: `python3 -m unittest discover -s tests -t .` (or
`make test`). Nothing here reads the network or the built page.
"""
import json
import unittest

import audit11
import audit12
import emit
import figures
import phonecheck
import policy
import probe
import ties_text


class FiguresGate(unittest.TestCase):
    """figures.py: every way a page might print the figure a card prints."""

    def test_million_reads_as_trade_abbreviations(self):
        v = figures.variants("$621 million")
        for want in ("621 million", "621 m", "621m", "621,000,000"):
            self.assertIn(want, v)
        # Build 86: the full form was once written as "621000000,000,000".
        self.assertNotIn("621000000,000,000", v)

    def test_price_bands_and_round_thousands(self):
        self.assertTrue({"370s", "370's", "370k"} <= figures.variants("$370,000"))
        self.assertIn("20k", figures.variants("20,000"))

    def test_years_list_names_bands_and_street_numbers_are_not_figures(self):
        text = ("It closed 1,062 homes in 2025, ranks on the Builder 100, sits at 3301 North Parkway, "
                "and reads against the 25 to 400 band.")
        self.assertEqual([f[0] for f in figures.figures_in(text)], ["1,062"])


class PhoneGate(unittest.TestCase):
    """phonecheck.py: the ten digits, however a page prints them."""

    def test_common_renderings(self):
        r = phonecheck.renderings("7136810446")
        for want in ("(713) 681-0446", "713-681-0446", "713.681.0446", "+1 713 681 0446"):
            self.assertIn(want, r)

    def test_digits_split_by_markup_still_count(self):
        self.assertTrue(phonecheck.found_on("7136810446", "call 713 681 0446 today", ""))
        self.assertFalse(phonecheck.found_on("7136810446", "call 713 681 0447 today", ""))


class NameGate(unittest.TestCase):
    """probe.py: a name is on the page only when forename and surname both are."""

    def test_suffixes_are_dropped(self):
        self.assertEqual(probe.parts("Frank Sitterle, Jr."), ["frank", "sitterle"])

    def test_surname_alone_is_not_a_hit(self):
        self.assertTrue(probe.hit("Dustin Rodgers", " dustin rodgers vice president ", ""))
        self.assertFalse(probe.hit("Dustin Rodgers", " rodgers vice president ", ""))


class Subscriptions(unittest.TestCase):
    """audit11.py: locked outlets are labelled and listed after free links."""

    def test_locked_hosts(self):
        self.assertEqual(audit11.host("https://www.houstonchronicle.com/a"), "houstonchronicle.com")
        self.assertTrue(audit11.locked("https://www.houstonchronicle.com/a"))
        self.assertFalse(audit11.locked("https://abc13.com/post/x"))

    def test_free_links_come_first_and_keep_their_order(self):
        paid = next(iter(audit11.PAID))
        xs = [{"url": paid}, {"url": "https://a.example/1"}, {"url": "https://a.example/2"}]
        self.assertEqual([x["url"] for x in audit11._paid_last(xs, lambda x: x["url"])],
                         ["https://a.example/1", "https://a.example/2", paid])


class Policy(unittest.TestCase):
    """policy.py: one banned list for every build and gate."""

    def test_aggregators_and_wikis_are_caught(self):
        for u in ("https://en.wikipedia.org/wiki/X", "https://www.zoominfo.com/c/x",
                  "https://www.houzz.com/pro/x", "https://pitchbook.com/profiles/x"):
            self.assertIsNotNone(policy.banned_in(u), u)

    def test_ordinary_prose_is_not_caught(self):
        for s in ("Its founder built his own house.", "https://www.iconbuild.com/technology",
                  "The Wiki Fund partnered on it."):
            self.assertIsNone(policy.banned_in(s), s)


class Copy(unittest.TestCase):
    """audit12.py: spelling, absences and the edit paths."""

    def test_spelling_is_american_but_brands_and_links_keep_theirs(self):
        d = {"a": "a multi-storey programme at the data centre", "url": "https://x.example/programme",
             "b": "Centre Living Homes", "c": ["neighbourhoods", "personalise"]}
        out = audit12.spell(d)
        self.assertEqual(out["a"], "a multi-story program at the data center")
        self.assertEqual(out["url"], "https://x.example/programme")
        self.assertEqual(out["b"], "Centre Living Homes")
        self.assertEqual(out["c"], ["neighborhoods", "personalize"])

    def test_absence_lines_are_recognised(self):
        for s in ("No leadership page. Names rest on LinkedIn headlines.", "About page names no officers.",
                  "Site names no owner or officer.", "No LinkedIn company page."):
            self.assertTrue(audit12.ABSENT.match(s), s)
        for s in ("Publishes as Housing Alliance HTX. Releases use both names.",
                  "Now a partner at Bluprint Ventures, per its team page."):
            self.assertFalse(audit12.ABSENT.match(s), s)

    def test_a_link_note_keeps_only_where_the_link_goes(self):
        m = audit12.LI_LINKS.match("No Ramble company page. Links to Hillwood Communities.")
        self.assertEqual(m.group(1), "Links to Hillwood Communities.")

    def test_edit_paths_resolve(self):
        t = {"key_stat": "k", "why": [{"axis": "innovation", "text": "w"}],
             "key_projects": [{"detail": "d"}], "principals": [{"name": "A B", "role": "r"}]}
        for path, want in (("key_stat", "k"), ("why.innovation", "w"), ("kp.0.detail", "d"),
                           ("pr.A B.role", "r")):
            obj, key = audit12._obj(t, path)
            self.assertEqual(obj[key], want, path)
        self.assertEqual(audit12._obj(t, "kp.3.detail")[0], None)


class Page(unittest.TestCase):
    """emit.py and ties_text.py: what reaches the page."""

    def test_embedded_data_cannot_close_its_script_element(self):
        d = {"a": "<b>x</b></script><!-- & y"}
        blob = emit._blob(d)
        for bad in ("<", ">", "&"):
            self.assertNotIn(bad, blob)
        self.assertEqual(json.loads(blob), d)

    def test_policy_hashes_each_script_and_skips_data_blocks(self):
        import base64
        import hashlib
        html = ('<meta http-equiv="Content-Security-Policy" content="__CSP__"><script>var a=1;</script>'
                '<script type="application/json">{"x":1}</script><script>\nvar b=2;\n</script>')
        pol = emit.csp(html)
        want = ["'sha256-%s'" % base64.b64encode(hashlib.sha256(s.encode()).digest()).decode()
                for s in ("var a=1;", "\nvar b=2;\n")]
        self.assertEqual(pol.split("script-src ", 1)[1].split(";", 1)[0].split(), want)
        self.assertTrue(pol.startswith("default-src 'none';"))
        self.assertNotIn("unsafe-inline';", pol.split("style-src", 1)[0])

    def test_card_text_normalises_space_and_quotes(self):
        self.assertEqual(ties_text.norm("Hillwood’s   Wolf Ranch "), "Hillwood's Wolf Ranch")


if __name__ == "__main__":
    unittest.main()
