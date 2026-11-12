#!/usr/bin/env python3
"""Score the blind review from judge/*/verdict.json. Prints counts with Wilson 95% intervals and writes summary.json."""
import os
import json, math, glob, collections, re
from pathlib import Path
def wilson(k, n, z=1.96):
    if n == 0: return (None, None)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return round((c - h) / d, 3), round((c + h) / d, 3)
rows = fields = contra = notin = rows_with_contra = 0
byfield = collections.Counter(); items = collections.Counter(); kinds = collections.defaultdict(collections.Counter)
details = []; missing_real = []
for f in sorted(glob.glob("judge/P*/verdict.json")):
    pid = f.split("/")[1]; v = json.load(open(f)); man = {m["pid"]: m for m in json.load(open("sample_manifest.json"))}[pid]
    its = json.load(open(f"judge/{pid}/items.json"))
    for r in v["rows"]:
        rows += 1; c = 0
        for fld, x in r["fields"].items():
            fields += 1
            if x == "contradicted": contra += 1; c += 1; byfield[fld] += 1; details.append((pid, r["row_id"], fld))
            if x == "not_in_paper": notin += 1
        rows_with_contra += c > 0
    for x in v["items"]:
        k = its[x["index"]]["kind"]
        if x["covered"] == "covered": items["covered"] += 1; kinds[k]["covered"] += 1
        elif x["missing_is"] == "real": items["missing_real"] += 1; kinds[k]["missing_real"] += 1; missing_real.append((pid, k, its[x["index"]]["value"][:50], x.get("reason", "")[:80]))
        else: items["reader_error"] += 1
n_items = items["covered"] + items["missing_real"]
out = {"papers": 15, "rows": rows, "fields_judged": fields, "contradicted_fields": contra, "rows_with_a_contradiction": rows_with_contra,
       "field_error_rate": [contra, fields, *wilson(contra, fields)], "row_error_rate": [rows_with_contra, rows, *wilson(rows_with_contra, rows)],
       "not_in_paper_fields": notin, "contradicted_by_field": dict(byfield), "contradicted_list": details,
       "items_covered": items["covered"], "items_missing_real": items["missing_real"], "reader_errors": items["reader_error"],
       "item_recall": [items["covered"], n_items, *wilson(items["covered"], n_items)],
       "recall_by_kind": {k: dict(v) for k, v in kinds.items()}, "missing_real_list": missing_real}
cited = re.compile(r"cite|literature|prior|earlier|previous|ref \d|refs \d|assay readout|upper bound|Discussion", re.I)
cited_n = sum(1 for m in missing_real if cited.search(m[3]) or cited.search(m[2]))
out["missing_split"] = {"cited_from_earlier_work_or_not_dynamics": cited_n, "measured_in_the_paper": len(missing_real) - cited_n}
out["item_recall_if_cited_values_excluded"] = [items["covered"], items["covered"] + len(missing_real) - cited_n, *wilson(items["covered"], items["covered"] + len(missing_real) - cited_n)]
json.dump(out, open("summary.json", "w"), indent=1, ensure_ascii=False)
for k in ("papers", "rows", "fields_judged", "contradicted_fields", "field_error_rate", "rows_with_a_contradiction", "row_error_rate", "not_in_paper_fields", "contradicted_by_field", "item_recall", "reader_errors", "recall_by_kind"): print(k, out[k])
for m in missing_real: print("MISSING", m)
