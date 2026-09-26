# -*- coding: utf-8 -*-
"""Comments out of the served page.

Build 91. The template's CSS and scripts carry the reasoning for each choice, by
build number, and a reader who opened the page source read all of it. The
source keeps its comments. The page ships without them.

Standard library only, so the Mac rebuilds the same bytes as the container.
Strings, template literals and regular expression literals are read as such, so
a "//" inside a URL or a "/*" inside a pattern is left alone. `jscheck.py` and
the verifier run on the stripped page, so a script this breaks fails the build.
"""
import re

# A "/" after one of these starts a regular expression, not a division.
_RE_BEFORE = set("(,=:[!&|?{};+-*%<>~^")
_RE_WORDS = {"return", "typeof", "case", "in", "of", "new", "delete", "void", "throw", "else", "do", "yield", "await"}


def js(src):
    out, i, n = [], 0, len(src)
    last = ""        # the last significant character or word written
    stack = []       # open template literals: brace depth inside each ${ }
    while i < n:
        c = src[i]
        nx = src[i + 1] if i + 1 < n else ""
        if stack and c == "}" and stack[-1] == 0:
            stack.pop()
            j = _template(src, i + 1, out_start=True)
            out.append(src[i:j[0]])
            i = j[0]
            if j[1]:
                stack.append(0)
            last = "`"
            continue
        if stack and c == "{":
            stack[-1] += 1
        elif stack and c == "}":
            stack[-1] -= 1
        if c == "/" and nx == "/":
            j = src.find("\n", i)
            i = n if j < 0 else j
            continue
        if c == "/" and nx == "*":
            j = src.find("*/", i + 2)
            if j < 0:
                raise ValueError("unclosed block comment")
            # Keep a line break where the comment had one, so no two
            # statements meet on one line through automatic semicolons.
            out.append("\n" if "\n" in src[i:j] else " ")
            i = j + 2
            continue
        if c in "'\"":
            j = i + 1
            while j < n and src[j] != c:
                if src[j] == "\\":
                    j += 1
                elif src[j] == "\n":
                    raise ValueError("line break in a string at %d" % i)
                j += 1
            out.append(src[i:j + 1])
            i = j + 1
            last = c
            continue
        if c == "`":
            j, opened = _template(src, i + 1, out_start=True)
            out.append(src[i:j])
            i = j
            if opened:
                stack.append(0)
            last = "`"
            continue
        if c == "/" and (last == "" or last in _RE_BEFORE or last in _RE_WORDS):
            j, cls = i + 1, False
            while j < n:
                d = src[j]
                if d == "\\":
                    j += 2
                    continue
                if d == "\n":
                    raise ValueError("line break in a regular expression at %d" % i)
                if d == "[":
                    cls = True
                elif d == "]":
                    cls = False
                elif d == "/" and not cls:
                    break
                j += 1
            j += 1
            while j < n and (src[j].isalpha()):
                j += 1
            out.append(src[i:j])
            i = j
            last = "/"
            continue
        m = re.match(r"[A-Za-z_$][\w$]*", src[i:i + 40])
        if m:
            w = m.group(0)
            out.append(w)
            i += len(w)
            last = w
            continue
        out.append(c)
        if not c.isspace():
            last = c
        i += 1
    return _tidy("".join(out))


def _template(src, i, out_start):
    """From inside a template literal to its end or its next ${. Returns the
    index after the stop and whether a ${ opened."""
    n = len(src)
    while i < n:
        d = src[i]
        if d == "\\":
            i += 2
            continue
        if d == "`":
            return i + 1, False
        if d == "$" and i + 1 < n and src[i + 1] == "{":
            return i + 2, True
        i += 1
    raise ValueError("unclosed template literal")


def css(src):
    out, i, n = [], 0, len(src)
    while i < n:
        c = src[i]
        if c == "/" and src.startswith("/*", i):
            j = src.find("*/", i + 2)
            if j < 0:
                raise ValueError("unclosed CSS comment")
            i = j + 2
            continue
        if c in "'\"":
            j = i + 1
            while j < n and src[j] != c:
                j += 2 if src[j] == "\\" else 1
            out.append(src[i:j + 1])
            i = j + 1
            continue
        out.append(c)
        i += 1
    return _tidy("".join(out))


def _tidy(s):
    """Lines left empty, or holding only spaces, by a removed comment go."""
    s = re.sub(r"[ \t]+\n", "\n", s)
    return re.sub(r"\n{2,}", "\n", s)


def page(html):
    """Every <style> and every script that is not a JSON data block, stripped."""
    def st(m):
        return m.group(1) + css(m.group(2)) + m.group(3)

    def sc(m):
        if "application/json" in m.group(1):
            return m.group(0)
        return "<script" + m.group(1) + ">" + js(m.group(2)) + "</script>"
    html = re.sub(r"(<style[^>]*>)(.*?)(</style>)", st, html, flags=re.S)
    html = re.sub(r"<script([^>]*)>(.*?)</script>", sc, html, flags=re.S)
    return re.sub(r"<!--(?!\[).*?-->", "", html, flags=re.S)
