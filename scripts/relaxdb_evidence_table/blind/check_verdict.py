#!/usr/bin/env python3
"""check_verdict.py judge/Pxx/verdict.json : each contradiction quote is verbatim in paper.txt; each row and item is judged."""
import os
import json, re, sys, unicodedata
from pathlib import Path
def sq(s):
    s = unicodedata.normalize("NFKC", s).replace("−", "-").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", "", s).lower()
p = Path(sys.argv[1]); d = p.parent; text = sq((d / "paper.txt").read_text(errors="replace"))
v = json.load(open(p)); rows = json.load(open(d / "rows.json")); items = json.load(open(d / "items.json"))
bad = 0
ids = {r["row_id"] for r in rows}; got = {r["row_id"] for r in v["rows"]}
if ids != got: print("rows_not_all_judged", sorted(ids ^ got)); bad += 1
for r in v["rows"]:
    for c in r.get("contradictions", []):
        if sq(c.get("quote", "")) not in text or len(c.get("quote", "").split()) < 4: print(r["row_id"], "contradiction_quote_not_in_paper"); bad += 1
    for f, x in r["fields"].items():
        if x not in ("supported", "contradicted", "not_in_paper"): print(r["row_id"], "bad_verdict", f, x); bad += 1
        if x == "contradicted" and not any(c.get("field") == f for c in r.get("contradictions", [])): print(r["row_id"], "contradicted_without_quote", f); bad += 1
want = {i for i, it in enumerate(items) if it["kind"] in ("rate", "population", "state_pdb") and it.get("target") in ("target", "other_construct")}
have = {x["index"] for x in v["items"]}
if want != have: print("items_not_all_judged", sorted(want ^ have)); bad += 1
for x in v["items"]:
    if x["covered"] not in ("covered", "missing"): print("bad_covered", x); bad += 1
    if x["covered"] == "missing" and x.get("missing_is") not in ("real", "reader_error"): print("missing_without_class", x["index"]); bad += 1
print(len(v["rows"]), "rows,", len(v["items"]), "items,", bad, "errors"); sys.exit(1 if bad else 0)
