"""The build number and the date the page states.

One place, read by build.py, build_dfw.py and emit.py. The build number goes in
the page's <meta name="build"> so a stale render can be told from a fresh one
without printing a build number to the reader. The date is the page's "as of"
date: the kicker and the byline print it.
"""
BUILD = 91
DATE = "2026-09-26"
