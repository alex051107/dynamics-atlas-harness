#!/usr/bin/env python3
"""One row per open RelaxDB protein, one column per item Gina asked for on 09-29 plus deposit conditions (10-22).
A literature cell counts as filled only from a full-text row on the target or another construct of the same protein
(homolog rows do not count) whose quotes passed the integrity check. Writes coverage.csv and prints the totals."""
import os
import csv, json, collections, glob
from pathlib import Path
from openpyxl import load_workbook
W = Path.home() / "dynamics_atlas_work"
WS = Path(os.environ["ATLAS_WORKSPACE"]) / "autoresearch/tasks/dynamics_atlas_stage1_loop_20261002/outputs"
sealed = set(map(str, json.load(open(Path.home() / "dynamics_atlas_eval/gold/splits.json"))["sealed"]))
spine = {r["entry_id"]: r for r in csv.DictReader(open(W / "outputs/spine_20261112/spine.csv"))}
LIT = ["residues", "alt_state_pdb", "experiments", "timescale", "population"]

def norm_v02(r, h):
    g = lambda k: str(r[h.index(k)] or "").strip()
    rel = g("Organism / construct vs entry").lower()
    return {"entry": g("entry"), "doi": g("doi_link").replace("https://doi.org/", "").lower(), "full": g("what_we_read") == "full_text",
            "ok": g("quote_found_in_local_full_text") == "yes", "homolog": rel.startswith("homolog"),
            "residues": g("Residues / region"), "alt_state_pdb": g("Alternate-state structure"), "experiments": g("Method"),
            "timescale": g("Timescale (as reported)"), "population": g("Population (as reported)")}

def norm_b(r, ok):
    alt = (r.get("alt_state_structure") or "").strip()
    return {"entry": str(r["entry_id"]), "doi": (r.get("doi") or "").lower(), "full": r.get("access") != "abstract_only", "ok": ok,
            "homolog": r.get("species_relation") == "homolog", "residues": r.get("residues_author") or "",
            "alt_state_pdb": "" if alt.lower().startswith("none") else alt, "experiments": r.get("method_class") or "",
            "timescale": r.get("timescale") or "", "population": r.get("population") or ""}

rows = collections.defaultdict(list); origin = {}
wb = load_workbook(WS / "delivery_table_v02/out/Dynamics_Atlas_RelaxDB_v0.2_draft.xlsx", read_only=True)
ev = list(wb["Evidence"].iter_rows(values_only=True))
for r in ev[1:]:
    x = norm_v02(r, ev[0]); rows[x["entry"]].append(x); origin[x["entry"]] = "11-01 table (Codex)"
state = json.load(open(W / "ledger/run133_state.json"))
for e, v in state.items():
    if "fill" not in v: continue
    p = W / "cases" / v["fill"]["case"] / "rows.jsonl"
    for l in (p.read_text().splitlines() if p.exists() else []):
        if l.strip(): rows[e].append(norm_b(json.loads(l), bool(v["fill"].get("integrity_pass"))))
    origin[e] = "11-11 run (Sonnet)" + ("" if v["status"] == "FILLED" else f", {v['status']}")
for e in ["6470", "7432", "11080", "17783", "18477", "26513", "50734", "BPTI", "IL4", "IRSPTB", "PCF11", "VMIPII"]:
    if e in rows or e in sealed: continue
    cs = sorted(glob.glob(str(W / f"cases/B1_r6_{e}_*")))
    if cs:
        for l in open(Path(cs[-1]) / "rows.jsonl"):
            if l.strip(): rows[e].append(norm_b(json.loads(l), True))
        origin[e] = "11-10 race (Opus arm B)"

import check_rows
for fo in sorted(glob.glob(str(Path(__file__).parent / "source_read/*/rows.jsonl"))):
    fd = Path(fo).parent; rr, ee = check_rows.check(fd); badr = {x[0] for x in ee}
    for r in rr:
        e = str(r["entry_id"])
        if e in sealed: continue
        rows[e].append(norm_b(r, r.get("row_id") not in badr))
        origin[e] = origin.get(e, "11-12 source-paper read") if e in origin and origin[e] != "not filled" else "11-12 source-paper read"

def dep(s):
    t = s["bmrb_temperature"] or ("" if s["sheet_temperature_K"] in ("", "298.5") else s["sheet_temperature_K"])
    return {"dep_temperature": t, "dep_field": s["bmrb_relaxation_field_MHz"] or s["sheet_field_MHz"], "dep_pH": s["bmrb_pH"],
            "dep_buffer": s["bmrb_sample_components"]}

out = []
for e, s in spine.items():
    if e in sealed: continue
    rs = rows.get(e, [])
    good = [r for r in rs if r["full"] and r["ok"] and not r["homolog"]]
    rec = {"entry": e, "set": s["set"], "protein": s["protein_name"][:60], "filled_by": origin.get(e, "not filled"),
           "rows": len(rs), "full_text_rows": len(good), "papers_full_text": len({r["doi"] for r in good})}
    for f in LIT:
        rec[f] = sum(bool(r[f].strip()) for r in good)
    rec.update({k: bool(v) for k, v in dep(s).items()})
    out.append(rec)
with open(Path(__file__).with_name("coverage.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
n = len(out)
print("open proteins", n, collections.Counter(r["filled_by"].split(",")[0] for r in out))
print("no full-text row at all:", sum(r["full_text_rows"] == 0 for r in out))
for f in LIT + ["dep_temperature", "dep_field", "dep_pH", "dep_buffer"]:
    print(f"{f:16s} filled for {sum(bool(r[f]) for r in out):3d} of {n}")
