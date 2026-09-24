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
# Build 66. The workbook had its own names for the sections, four of them
# different from the page's. It takes the page's now.
GROUP = dict(D["group_labels"]); GROUP["out"] = "Held off the deck"
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
    ("Track record", 13), ("Track record why", 48),
    ("LinkedIn URL", 40), ("Find", 9), ("Status", 14), ("Company URL", 34),
    ("Screen result", 80),
    ("Decides the wall", 15), ("How this person was verified", 70),
    ("Firm page for this person", 46), ("Company LinkedIn", 42), ("Leadership page", 42),
    ("Latest press", 70),
    # Appended rather than inserted. LI_COL, FIND_COL and ST_COL below, the
    # wrap and centre sets, and the legend prose all name column positions, so
    # anything slipped into the middle of this list silently moves them.
    ("Phone", 18), ("Phone label", 26), ("Phone source", 46),
    ("Email", 32), ("Email source", 46),
]
# Build 66. The legend named columns by letter and every letter from V on was
# one to the right of the column it meant, so the deciders counter summed the
# evidence column and read 0. Letters are now looked up from the names. The
# Capital column is gone: it was a fourth mark the page never shows.
def CI(name):
    return next(i for i, (n, _w) in enumerate(COLS, 1) if n == name)
def L(name):
    return get_column_letter(CI(name))
LI_COL, FIND_COL, ST_COL = CI("LinkedIn URL"), CI("Find"), CI("Status")
HDR = 6
first = HDR + 1

# ---------------------------------------------------------------- header block
ws["A1"] = "Rolodex · Greater Houston · contacts"
ws["A1"].font = Font(name="Arial", size=15, bold=True, color=INK)
ws["A2"] = "Héctor Ibarzábal · %s" % D["last_updated"]
ws["A2"].font = Font(name="Arial", size=9, color=MUTED)

ws["A4"] = ("Column %s is a LinkedIn people search for that name at that firm. Paste a profile URL into the "
            "shaded cell in column %s and column %s changes from ADD LINKEDIN to ok. Column %s marks the "
            "people who can change a wall specification; filter it to YES for the call list. Column %s is the "
            "evidence behind the name and column %s the firm's own page that names them. Columns %s to %s "
            "carry the firm's main line, its label and the page it is published on, and columns %s and %s "
            "the firm's email and its page. Both are the firm's, not the person's."
            % (L("Find"), L("LinkedIn URL"), L("Status"), L("Decides the wall"),
               L("How this person was verified"), L("Firm page for this person"),
               L("Phone"), L("Phone source"), L("Email"), L("Email source")))
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
        inn=WORD[t["marks"]["innovation"]],
        repw=WHYT(t, 0), wallw=WHYT(t, 1), innw=WHYT(t, 2),
        url=t.get("homepage_url") or ("no website confirmed" if t.get("no_web_presence") else ""),
        cli=t.get("company_li") or "", team=t.get("team_url") or "",
        screen=t["mvp_screen"],
        # Firm level, so it repeats down every row for that firm, including the
        # row a firm with no named contact gets.
        phone=(lambda d: "(%s) %s-%s" % (d[:3], d[3:6], d[6:]) if d else "")(t.get("phone")),
        phonelab=t.get("phone_label") or "",
        phonesrc=t.get("phone_source") or "",
        email=t.get("email") or "",
        emailsrc=t.get("email_source") or "",
        press=(lambda ps: ("%s %s. %s  %s" % (ps[0]["date"], ps[0]["outlet"],
                                              ps[0]["headline"], ps[0]["url"])).strip()
               if ps else "")(sorted(t.get("press") or [],
                                     key=lambda p: p["date"], reverse=True)),
    )
    people = t.get("principals") or []
    if people:
        for p in people:
            r = dict(base); r["name"] = p["name"]; r["title"] = p.get("role") or ""
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
ws["D3"] = '=COUNTIF($%s$%d:$%s$%d,"ok")' % (L("Status"), first, L("Status"), last)
ws["E3"] = "Still to add"
ws["F3"] = '=COUNTIF($%s$%d:$%s$%d,"ADD LINKEDIN")' % (L("Status"), first, L("Status"), last)
ws["I3"] = "Wall deciders"
ws["J3"] = '=COUNTIF($%s$%d:$%s$%d,"YES")' % (L("Decides the wall"), first, L("Decides the wall"), last)
ws["G3"] = GROUP["a"]
ws["H3"] = '=SUMPRODUCT((COUNTIF(OFFSET($B$%d,ROW($B$%d:$B$%d)-ROW($B$%d),0,1,1),$B$%d:$B$%d)>0)*($D$%d:$D$%d="%s")/COUNTIF($B$%d:$B$%d,$B$%d:$B$%d&""))' % (
    first, first, last, first, first, last, first, last, GROUP["a"], first, last, first, last)
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

WRAP = {CI(n) for n in ("Repetition why", "Printer fit why", "Track record why",
                        "Screen result", "How this person was verified")}
CENTRE = [CI(n) for n in ("Holds", "Repetition", "Printer fit", "Track record")]
KEYS = ["name", "firm", "title", "tier", "score", "role", "region", "stat",
        "rep", "repw", "wall", "wallw", "inn", "innw",
        "li", None, None, "url", "screen", "dec", "ev", "bio", "cli", "team", "press",
        "phone", "phonelab", "phonesrc", "email", "emailsrc"]

for ri, r in enumerate(rows):
    row = first + ri
    band = (ri % 2 == 1)
    for ci, key in enumerate(KEYS, 1):
        if ci == ST_COL:
            v = '=IF(%s%d="","ADD LINKEDIN","ok")' % (L("LinkedIn URL"), row)
        elif ci == FIND_COL:
            v = ('=HYPERLINK("%s","search")' % r["find"].replace('"', '""')) if r.get("find") else ""
        else:
            v = r.get(key, "")
        c = ws.cell(row=row, column=ci, value=v)
        c.font = Font(name="Arial", size=10, color=INK)
        c.alignment = Alignment(vertical="top", wrap_text=(ci in WRAP))
        c.border = Border(bottom=thin)
        if band and ci != LI_COL:
            c.fill = PatternFill("solid", fgColor=BAND)
    ws.cell(row=row, column=4).font = Font(name="Arial", size=10, bold=True, color=INK)
    ws.cell(row=row, column=4).alignment = Alignment(horizontal="left", vertical="top")
    for ci in CENTRE:
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
           "named the firm; the verification column records what was read. Where that test failed the cell is left empty rather "
           "than guessed, because a fabricated slug passes visual inspection and then fails in front of the person "
           "it names. The Find column searches for the empty ones in your own session. Each of the three counts reads "
           "Yes, Partly or No, with the reason in the column beside it. Yes and Partly both count as holding a count. A No does not. "
           "Holds counts how many of the three are Yes or Partly. Rolodex, Greater Houston, %s." % D["last_updated"]))
note.font = Font(name="Arial", size=9, italic=True, color=MUTED)

# ------------------------------------------------------------------ permits
# A second sheet, because it holds a different quantity. Census counts units
# AUTHORISED BY PERMIT; the Contacts sheet counts houses a builder closes.
# They are never put in one table.
P = D.get("permits") or {}
if P:
    ps = wb.create_sheet("Permits")
    ps.sheet_view.showGridLines = False
    hdr = Font(name="Arial", size=9, bold=True, color="FFFFFF")
    fill = PatternFill("solid", fgColor=HEADBG)
    yrs = P["counties"][0]["years"]

    ps.cell(row=1, column=1, value="Single-family units authorised by building permit, %s"
            % P["geo"]["name"]).font = Font(name="Arial", size=11, bold=True, color=INK)
    ps.cell(row=2, column=1, value=("Source: HUD SOCDS, republishing the Census Building Permits Survey. "
            "An authorisation is not a start, a completion or a closing. Census counts townhouses and row "
            "houses as single family. The jurisdictions sum to the counties and the counties sum to the "
            "metro exactly, in every year.")).font = Font(name="Arial", size=9, italic=True, color=MUTED)

    r = 4
    ps.cell(row=r, column=1, value="County").font = hdr
    ps.cell(row=r, column=1).fill = fill
    for j, y in enumerate(yrs):
        c = ps.cell(row=r, column=2 + j, value=y); c.font = hdr; c.fill = fill
    for c2 in sorted(P["counties"], key=lambda x: -x["sf"][-1]):
        r += 1
        ps.cell(row=r, column=1, value=c2["name"]).font = Font(name="Arial", size=10, color=INK)
        for j, v in enumerate(c2["sf"]):
            ps.cell(row=r, column=2 + j, value=v).font = Font(name="Arial", size=10, color=INK)
    r += 1
    ps.cell(row=r, column=1, value="Metro total").font = Font(name="Arial", size=10, bold=True, color=INK)
    msa = {m["year"]: m["sf"] for m in P["msa"]}
    for j, y in enumerate(yrs):
        ps.cell(row=r, column=2 + j, value=msa.get(y)).font = Font(name="Arial", size=10, bold=True, color=INK)

    r += 3
    ps.cell(row=r, column=1, value="Permit-issuing jurisdiction").font = hdr
    ps.cell(row=r, column=1).fill = fill
    ps.cell(row=r, column=2, value="County").font = hdr
    ps.cell(row=r, column=2).fill = fill
    for j, y in enumerate(P["place_years"]):
        c = ps.cell(row=r, column=3 + j, value=y); c.font = hdr; c.fill = fill
    for pl in sorted(P["places"], key=lambda x: -x["sf"][-1]):
        r += 1
        ps.cell(row=r, column=1, value=pl["name"]).font = Font(name="Arial", size=10, color=INK)
        ps.cell(row=r, column=2, value=pl["county"]).font = Font(name="Arial", size=10, color=MUTED)
        for j, v in enumerate(pl["sf"]):
            ps.cell(row=r, column=3 + j, value=v).font = Font(name="Arial", size=10, color=INK)
    ps.column_dimensions["A"].width = 38
    ps.column_dimensions["B"].width = 16
    for j in range(len(yrs)):
        ps.column_dimensions[get_column_letter(3 + j)].width = 9
    ps.freeze_panes = "C5"

wb.save("ICON_Greater_Houston_Rolodex.xlsx")
import shutil, os
os.makedirs("docs", exist_ok=True)
shutil.copy("ICON_Greater_Houston_Rolodex.xlsx", "docs/ICON_Greater_Houston_Rolodex.xlsx")
print("rows %d  (people %d, firms without a contact %d)" % (
    len(rows),
    sum(len(t["principals"]) for t in T),
    sum(1 for t in T if not t["principals"])))
print("range A%d:%s%d" % (HDR, get_column_letter(len(COLS)), last))
