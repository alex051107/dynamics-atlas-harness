#!/usr/bin/env python3
"""check_items.py reader/Pxx/items.json : every item's quote must be verbatim in the folder's paper.txt (whitespace and dash tolerant)."""
import os
import json, re, sys, unicodedata
from pathlib import Path
def sq(s):
    s = unicodedata.normalize("NFKC", s).replace("−", "-").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", "", s).lower()
p = Path(sys.argv[1]); text = sq((p.parent / "paper.txt").read_text(errors="replace"))
items = json.load(open(p)); bad = 0
for i, it in enumerate(items):
    q = it.get("quote") or ""
    if len(q.split()) < 6 or sq(q) not in text: print(i, "quote_not_in_paper", q[:70]); bad += 1
    if it.get("kind") not in {"rate", "population", "state_pdb", "condition", "residues", "order"}: print(i, "bad_kind", it.get("kind")); bad += 1
print(len(items), "items,", bad, "errors"); sys.exit(1 if bad else 0)
