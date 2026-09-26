# A restored file the same length as the one it replaced, written inside the
# same second, is invisible to CPython's mtime-and-size cache check. The
# build read a stale .pyc once and reported a figure the source no longer
# held. Nothing here is hot enough to need bytecode on disk.
export PYTHONDONTWRITEBYTECODE = 1

# `make` builds the page and the workbook, runs the unit tests, and checks the
# page in a headless browser. `make check` adds the linters. `make gates` runs
# the network gates, by hand, before sending.
.PHONY: all build xlsx intro test verify lint check gates clean
all: build xlsx intro test verify
build:
	python3 build.py
	python3 build_dfw.py
	python3 emit.py
xlsx: build
	python3 build_xlsx.py
	MARKET=dfw python3 build_xlsx.py
# The page carries the intro reel (emit.py adds its numbers, _reel.js draws it).
# This rebuilds the standalone copy in intro/ from the same code and data. Frames
# and video are made by hand: intro/frames.py and intro/export.py need a browser
# and ffmpeg.
intro: build
	python3 intro/build_intro.py
# Standard library only. Seconds, no browser, no network.
test: build
	python3 -m unittest discover -s tests -t .
# verify.py renders each market and checks it. xsscheck.py renders the page from
# data with markup appended to every string and checks that none of it runs.
verify: build
	python3 verify.py
	MARKET=dfw python3 verify.py
	python3 xsscheck.py
# ruff reads pyproject.toml. jscheck.py checks the built page's scripts with
# node, and lints them when eslint is installed. pip install -r requirements-dev.txt
lint: build
	@command -v ruff >/dev/null || { echo "ruff is not installed: pip install -r requirements-dev.txt"; exit 1; }
	ruff check .
	python3 jscheck.py
check: lint test
# Each reads the pages the deck cites, so each needs the network and takes a few
# minutes. They are not in `all`, because a build that fails when someone else's
# server is slow is a build nobody runs.
gates: build
	python3 probe.py
	python3 linkcheck.py
	python3 figures.py
	python3 phonecheck.py
	python3 marketcheck.py build/dfw-data.json
clean:
	rm -rf __pycache__ tests/__pycache__ .ruff_cache build
