#!/usr/bin/env python3
"""check_conditions.py OUT.jsonl : every filled value needs a verbatim snippet found in the row's own conditions text or in the cached paper text, and every number of the value must be inside the snippet. Every empty value needs a reason."""
import os
import json, re, sys, unicodedata
from pathlib import Path
HERE = Path(__file__).parent
ROWS = {r["evidence_id"]: r for r in json.load(open(HERE / "input_rows.json"))}
FIELDS = ["temperature", "ph", "buffer", "salt", "ligand", "phosphate"]
REASONS = {"not_in_row_text_and_paper_not_cached", "not_reported_in_paper", "abstract_only_no_conditions", "not_applicable"}
NUM = re.compile(r"\d+(?:\.\d+)?")
def sq(s):
    s = unicodedata.normalize("NFKC", s).replace("−", "-").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", "", s).lower()
_cache = {}
def paper(path):
    if path not in _cache: _cache[path] = sq(Path(path).read_text(errors="replace"))
    return _cache[path]
def check(path):
    errs, n = [], 0
    for l in open(path):
        if not l.strip(): continue
        o = json.loads(l); n += 1; rid = o.get("evidence_id")
        r = ROWS.get(rid)
        if not r: errs.append((rid, "unknown_evidence_id", "")); continue
        for f in FIELDS:
            v = str(o.get(f) or "").strip()
            if v:
                s = (o.get("support") or {}).get(f) or {}
                snip = sq(s.get("snippet") or "")
                src = s.get("source")
                if len(snip) < 4: errs.append((rid, "no_snippet", f)); continue
                hay = sq(r["experiment_and_conditions"] + " " + r["quote"]) if src == "cell" else (paper(r["paper_text"]) if src == "paper" and r["paper_text"] else "")
                if snip not in hay: errs.append((rid, "snippet_not_in_source", f"{f}: {s.get('snippet','')[:60]}"))
                for num in NUM.findall(v):
                    if num not in sq(s.get("snippet") or ""): errs.append((rid, "number_not_in_snippet", f"{f}: {num}"))
            elif f in ("temperature", "ph", "buffer"):
                er = (o.get("empty_reasons") or {}).get(f)
                if er not in REASONS: errs.append((rid, "empty_without_reason", f))
                if er == "not_in_row_text_and_paper_not_cached" and r["paper_text"]: errs.append((rid, "reason_wrong_paper_is_cached", f))
                if er == "abstract_only_no_conditions" and r["what_we_read"] != "abstract_only": errs.append((rid, "reason_wrong_not_abstract_only", f))
    return n, errs
if __name__ == "__main__":
    n, errs = check(sys.argv[1])
    for e in errs: print(*e, sep="\t")
    print(f"{n} rows, {len(errs)} errors"); sys.exit(1 if errs else 0)
