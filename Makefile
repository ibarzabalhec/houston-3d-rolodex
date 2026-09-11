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
