# -*- coding: utf-8 -*-
"""The page's rules, checked against the served data without a browser.

verify.py renders the page and checks it in Chromium, which takes minutes.
These read docs/*.json, the exact data the page embeds, and run in under a
second, so a rule broken by a data edit shows up before the page is built
again. They skip when the build has not run.
"""
import json
import pathlib
import re
import unittest
import zipfile

import audit12
import audit13
import emit
import policy
from version import DATE

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARKETS = {"hou": ROOT / "docs" / "houston-data.json", "dfw": ROOT / "docs" / "dfw-data.json"}
URL_KEYS = ("url", "source_url", "linkedin_url", "homepage_url", "team_url", "company_li", "phone_source",
            "find_url", "site")
VERDICT = {"Yes": "clear", "Partly": "partial", "No": "fail"}


def strings(o, key=None):
    """Every string in the data, with the key it sits under."""
    if isinstance(o, dict):
        for k, v in o.items():
            yield from strings(v, k)
    elif isinstance(o, list):
        for v in o:
            yield from strings(v, key)
    elif isinstance(o, str):
        yield key, o


class PublicData(unittest.TestCase):
    def setUp(self):
        self.data = {mk: json.loads(p.read_text(encoding="utf-8")) for mk, p in MARKETS.items() if p.exists()}
        if not self.data:
            self.skipTest("docs/*.json not built yet (make build)")

    def test_only_the_deck_and_only_public_fields(self):
        for mk, d in self.data.items():
            for t in d["targets"]:
                self.assertNotEqual(t.get("group"), "out", (mk, t["target_id"]))
                for k in emit.PRIVATE:
                    self.assertNotIn(k, t, (mk, t["target_id"], k))

    def test_links_are_web_links(self):
        for mk, d in self.data.items():
            for key, s in strings(d):
                self.assertFalse(s.strip().lower().startswith(("javascript:", "data:", "vbscript:")), (mk, key, s[:60]))
                if key in URL_KEYS and s:
                    self.assertRegex(s, r"^https?://", (mk, key, s[:80]))

    def test_no_banned_source(self):
        for mk, d in self.data.items():
            for key, s in strings(d):
                self.assertIsNone(policy.banned_in(s), (mk, key, s[:80]))

    def test_house_style(self):
        spelling = [re.compile(a) for a, _ in audit12.SPELL]
        for mk, d in self.data.items():
            for key, s in strings(d):
                if key in URL_KEYS or s.startswith("http"):
                    continue
                self.assertNotIn("—", s, (mk, key, s[:80]))
                for rx in spelling:
                    self.assertIsNone(rx.search(s), (mk, key, rx.pattern, s[:80]))

    def test_every_card_carries_three_counts_that_agree_with_their_marks(self):
        for mk, d in self.data.items():
            for t in d["targets"]:
                axes = [w["axis"] for w in t["why"]]
                self.assertEqual(axes, ["repeatability", "machine_fit", "innovation"], (mk, t["target_id"]))
                for w in t["why"]:
                    self.assertEqual(VERDICT[w["verdict"]], w["mark"], (mk, t["target_id"], w["axis"]))
                    self.assertTrue(w["text"].strip(), (mk, t["target_id"], w["axis"]))

    def test_an_absence_is_a_blank(self):
        for mk, d in self.data.items():
            for t in d["targets"]:
                for k in ("people_absent", "web_absent"):
                    self.assertFalse(t.get(k), (mk, t["target_id"], k))

    def test_stat_strip_counts_its_sections(self):
        for mk, d in self.data.items():
            for value, _label, _pct, flt in d["stat_strip"]:
                if flt and "group" in flt:
                    n = sum(1 for t in d["targets"] if t["group"] in flt["group"])
                    self.assertEqual(int(value), n, (mk, flt))

    def test_readme_quotes_the_page_counts(self):
        readme = ROOT / "README.md"
        if "hou" not in self.data or not readme.exists():
            self.skipTest("README.md not written yet (make build)")
        text = readme.read_text(encoding="utf-8")
        deck = self.data["hou"]["targets"]
        self.assertIn("%d Greater Houston builders" % len(deck), text)
        self.assertIn("with %d named contacts" % sum(len(t["principals"]) for t in deck), text)
        if "dfw" in self.data:
            self.assertIn("home screen: %d firms" % len(self.data["dfw"]["targets"]), text)

    def test_every_card_says_what_kind_of_firm_it_is(self):
        for mk, d in self.data.items():
            labels = dict(d.get("types") or [])
            for t in d["targets"]:
                self.assertIn(t.get("type"), labels, (mk, t["target_id"]))
                self.assertLessEqual(len(labels[t["type"]].split()), 3, (mk, t["type"]))
                # Build 90. No verdict on the card about who would buy a printer.
                self.assertNotIn("role", t, (mk, t["target_id"]))
                self.assertNotIn("kind", t, (mk, t["target_id"]))
            # Nor an old role vocabulary served beside the cards.
            for k in ("role_labels", "role_notes", "roles"):
                self.assertNotIn(k, d, (mk, k))

    def test_screen_lines_state_facts(self):
        argue = re.compile(r"\b(%s)\b" % "|".join(audit13.BANNED), re.I)
        for mk, d in self.data.items():
            for t in d["targets"]:
                s = t.get("mvp_screen") or ""
                self.assertIsNone(argue.search(s), (mk, t["target_id"], s))
                self.assertLessEqual(len(s.split()), 26, (mk, t["target_id"], s))

    def test_internal_scoring_is_not_served(self):
        for mk, d in self.data.items():
            for t in d["targets"]:
                for k in ("tier", "scores", "capital_mark", "entity_type"):
                    self.assertNotIn(k, t, (mk, t["target_id"], k))

    def test_market_figures_are_well_formed(self):
        for mk, d in self.data.items():
            for r in d["market"]["closings"]:
                self.assertLessEqual(r["low"], r["high"], (mk, r["id"]))
            for r in d["market"]["printed"]:
                self.assertIsInstance(r["units"], int)
                self.assertGreater(r["units"], 0, (mk, r["project"]))


class Workbooks(unittest.TestCase):
    """A workbook built twice from the same data is the same file, so docs/ changes
    only when the roster does."""

    def test_workbooks_carry_the_page_date_not_the_build_time(self):
        books = [p for p in (ROOT / "docs").glob("*.xlsx")]
        if not books:
            self.skipTest("the workbooks have not been built")
        for p in books:
            with zipfile.ZipFile(p) as z:
                core = z.read("docProps/core.xml").decode("utf-8")
                stamps = {i.date_time[:3] for i in z.infolist()}
            self.assertEqual(re.findall(r"<dcterms:(?:created|modified)[^>]*>([^<]*)<", core),
                             [DATE + "T00:00:00Z"] * 2, p.name)
            self.assertEqual(stamps, {tuple(int(x) for x in DATE.split("-"))}, p.name)


if __name__ == "__main__":
    unittest.main()


class Strip(unittest.TestCase):
    """Build 91. The served page carries no code comments, and the stripper
    reads strings, templates and regular expressions as such."""

    def test_stripper_keeps_code(self):
        import strip
        src = ("var a='//not', b=\"/*no*/\", r=/\\/\\/x[/]/g; // gone\n"
               "var t=`a ${ {k:'}'}.k } // kept ${b}`; /* gone */ var d=a/2/1;\n")
        out = strip.js(src)
        for keep in ("'//not'", '"/*no*/"', "/\\/\\/x[/]/g", "`a ${ {k:'}'}.k } // kept ${b}`", "a/2/1"):
            self.assertIn(keep, out)
        self.assertNotIn("gone", out)
        self.assertEqual(strip.css("a{b:'/*x*/'}/* c */d{}"), "a{b:'/*x*/'}d{}")

    def test_page_has_no_comments(self):
        page = ROOT / "docs" / "index.html"
        if not page.exists():
            self.skipTest("build has not run")
        html = re.sub(r'<script id="rolodex-[a-z]+" type="application/json">.*?</script>', "",
                      page.read_text(encoding="utf-8"), flags=re.S)
        self.assertNotIn("/*", html)
        self.assertIsNone(re.search(r"\bBuild \d", html))
