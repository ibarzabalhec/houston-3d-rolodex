# -*- coding: utf-8 -*-
"""Check the page's JavaScript: syntax always, lint when ESLint is installed.

The page's scripts are written inline in _template.html, _market.js and _reel.js
and only meet in the built page, so this reads them from there: every <script>
that is not a JSON data block, joined in page order into one file, which is the
scope the browser runs them in.

  node --check   fails on a syntax error. Needs Node.
  eslint         fails on an undefined name, a redeclared variable, a duplicate
                 key or unreachable code, and reports unused names. It runs only
                 when `eslint` is on PATH. The browser's own globals are read
                 from Chromium through Playwright, which the build already uses,
                 so no npm package is needed.

Run after emit.py: `python3 jscheck.py` (or `make lint`).
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).parent
PAGE = ROOT / "ICON_Greater_Houston_Rolodex.html"

RULES = {
    "no-undef": "error", "no-redeclare": "error", "no-dupe-keys": "error", "no-unreachable": "error",
    "no-self-assign": "error", "no-dupe-else-if": "error", "no-duplicate-case": "error",
    "use-isnan": "error", "valid-typeof": "error", "no-sparse-arrays": "error",
    "no-loss-of-precision": "error",
    "no-unused-vars": ["warn", {"args": "none", "caughtErrors": "none"}],
}


def page_scripts(html):
    """The page's executable scripts, in order. JSON data blocks are skipped."""
    out = []
    for attrs, body in re.findall(r"<script([^>]*)>(.*?)</script>", html, re.S):
        if "application/json" not in attrs:
            out.append(body)
    return out


def browser_globals():
    """Every global name a page can read in Chromium."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        names = b.new_page().evaluate(
            "(()=>{const s=new Set();let o=window;"
            "while(o){Object.getOwnPropertyNames(o).forEach(k=>s.add(k));o=Object.getPrototypeOf(o);}"
            "return [...s]})()")
        b.close()
    return sorted(n for n in names if re.match(r"^[A-Za-z_$][\w$]*$", n))


def main():
    if not PAGE.exists():
        sys.exit("jscheck: build the page first (make build)")
    js = "\n;\n".join(page_scripts(PAGE.read_text(encoding="utf-8")))
    with tempfile.TemporaryDirectory() as tmp:
        src = pathlib.Path(tmp) / "page.js"
        src.write_text(js, encoding="utf-8")
        if not shutil.which("node"):
            sys.exit("jscheck: node is not installed, so the syntax check cannot run")
        r = subprocess.run(["node", "--check", str(src)], capture_output=True, text=True)
        if r.returncode:
            sys.exit("jscheck: syntax error\n" + r.stderr)
        print("js syntax       : %d scripts, %d bytes, clean" % (js.count("\n;\n") + 1, len(js)))
        if not shutil.which("eslint"):
            print("js lint         : eslint not installed, skipped")
            return
        (pathlib.Path(tmp) / "globals.json").write_text(json.dumps(browser_globals()))
        (pathlib.Path(tmp) / "eslint.config.mjs").write_text(
            'import fs from "node:fs";\n'
            'const names = JSON.parse(fs.readFileSync(new URL("./globals.json", import.meta.url)));\n'
            'export default [{files: ["**/*.js"], languageOptions: {ecmaVersion: 2022, sourceType: "script",\n'
            '  globals: Object.fromEntries(names.map(n => [n, "readonly"]))},\n'
            '  rules: %s}];\n' % json.dumps(RULES))
        r = subprocess.run(["eslint", "--no-color", "-c", "eslint.config.mjs", "page.js"],
                           cwd=tmp, capture_output=True, text=True)
        out = (r.stdout + r.stderr).strip()
        if r.returncode:
            sys.exit("jscheck: eslint found errors\n" + out)
        print("js lint         : %s" % ("clean" if not out else "warnings\n" + out))


if __name__ == "__main__":
    main()
