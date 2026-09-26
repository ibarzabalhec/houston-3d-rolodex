# -*- coding: utf-8 -*-
"""The public text of one card, as the page prints it. ties.py reads a cite
against this and nothing else, so a tie can only rest on words a reader sees."""
import re

def card_text(t):
    parts = [t.get("entity_name"), t.get("short"), t.get("synopsis"), t.get("mvp_screen"), t.get("key_stat"),
             t.get("channel_line")]
    for w in t.get("why") or []:
        parts.append(w.get("text"))
    for k in t.get("key_projects") or []:
        parts += [k.get("name"), k.get("detail"), k.get("fit_signal")]
    for p in t.get("principals") or []:
        parts += [p.get("role"), p.get("source_evidence")]
    for c in t.get("capital_signals") or []:
        parts.append(c.get("text"))
    for n in t.get("news") or []:
        parts.append(n.get("what"))
    parts += t.get("card_notes") or []
    return norm(" ".join(x for x in parts if isinstance(x, str)))

def norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'")).strip()
