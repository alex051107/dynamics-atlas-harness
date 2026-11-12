#!/usr/bin/env python3
"""For rows whose empty cell was explained as 'not_reported_in_paper', check whether the paper text still contains a pH, temperature or buffer pattern.
A hit does not prove the reader wrong (the text may state the item for another experiment), so such cells are shown as 'paper text mentions it, unchecked'.
Writes cond_fill/tripwire.json {evidence_id|field: true}."""
import os
import glob, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
rows = {r["evidence_id"]: r for r in json.load(open(HERE / "input_rows.json"))}
PAT = {"ph": re.compile(r"\bpH\s*\*?\s*[=:~]?\s*\d"), "temperature": re.compile(r"\d\s*(?:°|º|˚)\s*C\b|\b\d{3}(?:\.\d)?\s?K\b|degrees? C"),
       "buffer": re.compile(r"\b\d+(?:\.\d+)?\s?mM\s+[A-Za-z][A-Za-z\-]+(?:\s+(?:buffer|phosphate|acetate|HEPES|MES|Tris|MOPS|citrate))?|\bbuffer\b", re.I)}
cache, out = {}, {}
for f in sorted(glob.glob(str(HERE / "out/*.jsonl"))):
    for l in open(f):
        if not l.strip(): continue
        o = json.loads(l); r = rows.get(o["evidence_id"])
        for fld, rs in (o.get("empty_reasons") or {}).items():
            if rs != "not_reported_in_paper" or fld not in PAT or not r or not r["paper_text"]: continue
            if r["paper_text"] not in cache: cache[r["paper_text"]] = open(r["paper_text"], errors="replace").read()
            if PAT[fld].search(cache[r["paper_text"]]): out[f"{o['evidence_id']}|{fld}"] = True
json.dump(out, open(HERE / "tripwire.json", "w"), indent=0)
print(len(out), "empty cells flagged")
