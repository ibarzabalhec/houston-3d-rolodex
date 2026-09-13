# A restored file the same length as the one it replaced, written inside the
# same second, is invisible to CPython's mtime-and-size cache check. The
# build read a stale .pyc once and reported a figure the source no longer
# held. Nothing here is hot enough to need bytecode on disk.
export PYTHONDONTWRITEBYTECODE = 1

# One command builds the page, the workbook, and checks both in a headless browser.
.PHONY: all build xlsx verify clean
all: build xlsx verify
build:
	python3 build.py
xlsx: build
	python3 build_xlsx.py
verify: build
	python3 verify.py
clean:
	rm -rf __pycache__ ICON_Greater_Houston_Rolodex.html ICON_Greater_Houston_Rolodex.xlsx houston-data.json rolodex-artifact.html
