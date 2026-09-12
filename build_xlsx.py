# -*- coding: utf-8 -*-
"""Generate the single-tab XLSX workbench from houston-data.json.

One row per person. The LinkedIn column is editable and highlighted where empty,
because that is the column somebody will sit and fill in. Every count is a formula.
"""
import json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

D = json.load(open("houston-data.json", encoding="utf-8"))
WORD = {"clear": "Yes", "partial": "Partly", "fail": "No"}
GROUP = {"adopter": "Already buying printed walls", "a": "Strong target",
         "b": "Worth pursuing, one gap", "trade": "Builds the wall, not the house", "national": "National scale, pilot not purchase", "creative": "Creative project, hybrid job",
         "channel": "Masterplan owner", "icon": "Already working with ICON",
         "out": "Off deck, screened out"}
T = D["targets"]

def WHYT(t, i):
    w = t.get("why") or []
    return w[i]["text"] if len(w) > i else ""

INK   = "111111"
MUTED = "666666"
ICON  = "FF4F00"   # the one accent, same as the deck
HEADBG= "111111"
EDIT  = "FFE9DF"   # editable cells, pale ICON orange
BAND  = "FAFAFA"

wb = Workbook()
ws = wb.active
ws.title = "Contacts"

COLS = [
    ("Name", 26), ("Firm", 34), ("Title", 34), ("Group", 26), ("Holds", 7),
    ("Role", 13), ("Region", 30), ("Headline figure", 30),
    ("Repetition", 12), ("Repetition why", 48),
    ("Printer fit", 12), ("Printer fit why", 48),
    ("Track record", 13), ("Track record why", 48), ("Capital", 10),
    ("LinkedIn URL", 40), ("Find", 9), ("Status", 14), ("Company URL", 34),
    ("Screen result", 80), ("Open items", 60),
    ("Decides the wall", 15), ("How this person was verified", 70),
    ("Firm page for this person", 46), ("Company LinkedIn", 42), ("Leadership page", 42),
]
LI_COL, FIND_COL, ST_COL = 16, 17, 18   # 1-indexed
HDR = 6
first = HDR + 1

# ---------------------------------------------------------------- header block
ws["A1"] = "ICON · Greater Houston screen · contact workbench"
ws["A1"].font = Font(name="Arial", size=15, bold=True, color=INK)
ws["A2"] = ("Generated from houston-data.json · build %d · %s · public render. "
            "Do not hand-edit the HTML deck; it regenerates from the same file."
            % (D["build"], D["last_updated"]))
ws["A2"].font = Font(name="Arial", size=9, color=MUTED)

ws["A4"] = ("LEGEND. Column Q is a one-click LinkedIn people search for that name at that firm, run in your own "
            "signed-in session. Paste the profile URL into the shaded cell in column P and column R flips from "
            "ADD LINKEDIN to ok, with the counters in row 3 updating live. Every other column is generated and is "
            "overwritten on the next build. Column V marks the people who can change a wall specification, a vice "
            "president or director of construction or the head of purchasing; filter it to YES for the call list. "
            "Column W is the evidence behind the name, column X the firm's own page that names them, "
            "and columns Y and Z the company's LinkedIn and leadership pages. "
            "Example: https://www.linkedin.com/in/jane-doe-1a2b3c4d/")
ws["A4"].font = Font(name="Arial", size=9, italic=True, color=MUTED)
ws["A4"].alignment = Alignment(wrap_text=False)

# ---------------------------------------------------------------- rows
rows = []
for t in T:
    base = dict(
        firm=t["entity_name"], tier=GROUP[t["group"]], score=t["holds"],
        role=D["role_labels"].get(t["entity_role"], t["entity_role"]),
        region=t["region"], stat=t.get("key_stat") or "",
        rep=WORD[t["marks"]["repeatability"]], wall=WORD[t["marks"]["machine_fit"]],
        inn=WORD[t["marks"]["innovation"]], cap=WORD[t["capital_mark"]],
        repw=WHYT(t, 0), wallw=WHYT(t, 1), innw=WHYT(t, 2),
        url=t.get("homepage_url") or ("no website confirmed" if t.get("no_web_presence") else ""),
        cli=t.get("company_li") or "", team=t.get("team_url") or "",
        screen=t["mvp_screen"], flags=" | ".join(t.get("audit_flags", [])),
    )
    people = t.get("principals") or []
    if people:
        for p in people:
            r = dict(base); r["name"] = p["name"]; r["title"] = p["role"]
            r["li"] = p.get("linkedin_url") or ""
            r["find"] = p.get("find_url") or ""
            r["dec"] = "YES" if p.get("decider") else ""
            r["ev"] = " ".join(x for x in (p.get("li_evidence"), p.get("source_evidence")) if x)
            r["bio"] = p.get("source_url") or ""
            rows.append(r)
    else:
        r = dict(base); r["name"] = "no contact identified"; r["title"] = ""; r["li"] = ""; r["find"] = ""
        r["dec"] = ""; r["ev"] = ""; r["bio"] = ""
        rows.append(r)

last = HDR + len(rows)

# counters, all formulas
ws["A3"] = "Contacts"
ws["B3"] = "=COUNTA($A$%d:$A$%d)" % (first, last)
ws["C3"] = "LinkedIn held"
ws["D3"] = '=COUNTIF($R$%d:$R$%d,"ok")' % (first, last)
ws["E3"] = "Still to add"
ws["F3"] = '=COUNTIF($R$%d:$R$%d,"ADD LINKEDIN")' % (first, last)
ws["I3"] = "Wall deciders"
ws["J3"] = '=COUNTIF($V$%d:$V$%d,"YES")' % (first, last)
ws["G3"] = "Strong targets"
ws["H3"] = '=SUMPRODUCT((COUNTIF(OFFSET($B$%d,ROW($B$%d:$B$%d)-ROW($B$%d),0,1,1),$B$%d:$B$%d)>0)*($D$%d:$D$%d="Strong target")/COUNTIF($B$%d:$B$%d,$B$%d:$B$%d&""))' % (
    first, first, last, first, first, last, first, last, first, last, first, last)
for c in ("A3", "C3", "E3", "G3", "I3"):
    ws[c].font = Font(name="Arial", size=9, color=MUTED)
for c in ("B3", "D3", "F3", "H3", "J3"):
    ws[c].font = Font(name="Arial", size=12, bold=True, color=INK)

# header row
thin = Side(style="thin", color="E4E4E4")
for i, (label, width) in enumerate(COLS, 1):
    c = ws.cell(row=HDR, column=i, value=label)
    c.font = Font(name="Arial", size=9, bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor=HEADBG)
    c.alignment = Alignment(vertical="center", horizontal="left")
    ws.column_dimensions[get_column_letter(i)].width = width
ws.row_dimensions[HDR].height = 22

KEYS = ["name", "firm", "title", "tier", "score", "role", "region", "stat",
        "rep", "repw", "wall", "wallw", "inn", "innw", "cap",
        "li", None, None, "url", "screen", "flags", "dec", "ev", "bio", "cli", "team"]

for ri, r in enumerate(rows):
    row = first + ri
    band = (ri % 2 == 1)
    for ci, key in enumerate(KEYS, 1):
        if ci == ST_COL:
            v = '=IF(P%d="","ADD LINKEDIN","ok")' % row
        elif ci == FIND_COL:
            v = ('=HYPERLINK("%s","search")' % r["find"].replace('"', '""')) if r.get("find") else ""
        else:
            v = r.get(key, "")
        c = ws.cell(row=row, column=ci, value=v)
        c.font = Font(name="Arial", size=10, color=INK)
        c.alignment = Alignment(vertical="top", wrap_text=(ci in (10, 12, 14, 20, 21, 23)))
        c.border = Border(bottom=thin)
        if band and ci != LI_COL:
            c.fill = PatternFill("solid", fgColor=BAND)
    ws.cell(row=row, column=4).font = Font(name="Arial", size=10, bold=True, color=INK)
    ws.cell(row=row, column=4).alignment = Alignment(horizontal="left", vertical="top")
    for ci in (5, 9, 11, 13, 15):
        ws.cell(row=row, column=ci).alignment = Alignment(horizontal="center", vertical="top")
    # editable LinkedIn cell
    li = ws.cell(row=row, column=LI_COL)
    if not r.get("li"):
        li.fill = PatternFill("solid", fgColor=EDIT)
    st = ws.cell(row=row, column=ST_COL)
    st.font = Font(name="Arial", size=9, bold=True, color=ICON)
    st.alignment = Alignment(horizontal="center", vertical="top")

ws.auto_filter.ref = "A%d:%s%d" % (HDR, get_column_letter(len(COLS)), last)
ws.freeze_panes = "B%d" % first
ws.sheet_view.showGridLines = False

# assumption note at the end of the table
note = ws.cell(row=last + 2, column=1,
    value=("NOTE. A filled LinkedIn cell means the profile was opened or the search result read and the headline "
           "named the firm; column W records what was read. Where that test failed the cell is left empty rather "
           "than guessed, because a fabricated slug passes visual inspection and then fails in front of the person "
           "it names. Column Q searches for the empty ones in your own session. Each of the three counts reads "
           "Yes, Partly or No, with the reason in the column beside it. Yes and Partly both keep a firm in. Only a No takes it out. "
           "Holds counts how many of the three are Yes or Partly. Capital is a qualifier, not a count. Source: ICON Greater Houston screen, build %d, %s." % (D["build"], D["last_updated"])))
note.font = Font(name="Arial", size=9, italic=True, color=MUTED)

wb.save("ICON_Greater_Houston_Rolodex.xlsx")
import shutil, os
os.makedirs("docs", exist_ok=True)
shutil.copy("ICON_Greater_Houston_Rolodex.xlsx", "docs/ICON_Greater_Houston_Rolodex.xlsx")
print("rows %d  (people %d, firms without a contact %d)" % (
    len(rows),
    sum(len(t["principals"]) for t in T),
    sum(1 for t in T if not t["principals"])))
print("range A%d:%s%d" % (HDR, get_column_letter(len(COLS)), last))
