# A restored file the same length as the one it replaced, written inside the
# same second, is invisible to CPython's mtime-and-size cache check. The
# build read a stale .pyc once and reported a figure the source no longer
# held. Nothing here is hot enough to need bytecode on disk.
export PYTHONDONTWRITEBYTECODE = 1

# One command builds the page, the workbook, and checks both in a headless browser.
.PHONY: all build xlsx intro verify clean
all: build xlsx intro verify
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
verify: build
	python3 verify.py
	MARKET=dfw python3 verify.py
clean:
	rm -rf __pycache__ ICON_Greater_Houston_Rolodex.html ICON_Greater_Houston_Rolodex.xlsx houston-data.json rolodex-artifact.html dfw/dfw-data.json DFW_Rolodex.xlsx
