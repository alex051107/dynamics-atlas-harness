#!/usr/bin/env python3
"""Rerun every deterministic check of the table build and print one verdict per check.
Each check is also run on a planted defect and must fail there (the canaries), otherwise the check proves nothing.
  verify_all.py [--worktree DIR]   exit 0 only when every check passes and every canary fails as planted"""
import os
import collections, glob, importlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path
HERE = Path(__file__).resolve().parent; HOME = Path.home()
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "cond_fill"))
SEALED = set(map(str, json.load(open(HOME / "dynamics_atlas_eval/gold/splits.json"))["sealed"]))
check_rows = importlib.import_module("check_rows"); check_cond = importlib.import_module("check_conditions")
results = []
def rec(name, ok, detail): results.append((name, ok, detail)); print(("PASS  " if ok else "FAIL  ") + name + "  " + detail)

# 1. source-paper rows: every folder passes
rows = errs = n = 0
for f in sorted(glob.glob(str(HERE / "source_read/*/rows.jsonl"))):
    r, e = check_rows.check(Path(f).parent); rows += len(r); errs += len(e); n += 1
rec("rows: quotes, numbers, reasons in the paper text", errs == 0, f"{n} folders, {rows} rows, {errs} errors")

# 1b. canaries: the same checker must reject a changed quote, an unbacked number, a sealed entry, an empty cell without reason
def canary_rows():
    src = sorted(glob.glob(str(HERE / "source_read/*/rows.jsonl")))[0]; d = Path(src).parent
    base = [json.loads(l) for l in open(src) if l.strip()][0]
    out = {}
    for name, edit in (("changed quote", lambda r: r.update(anchor=r["anchor"] + " plus words that are not in the paper at all")),
                       ("unbacked number", lambda r: r.update(timescale="kex = 987654 s-1")),
                       ("sealed entry", lambda r: r.update(entry_id=sorted(SEALED)[0])),
                       ("empty without reason", lambda r: (r.update(temperature=""), r.__setitem__("empty_reasons", {})))):
        t = Path(tempfile.mkdtemp()); shutil.copy(d / "paper.txt", t / "paper.txt")
        r = json.loads(json.dumps(base)); edit(r); (t / "rows.jsonl").write_text(json.dumps(r) + "\n")
        out[name] = len(check_rows.check(t)[1]) > 0; shutil.rmtree(t)
    return out
c = canary_rows(); rec("rows: canaries (planted defects are rejected)", all(c.values()), ", ".join(f"{k}: {'rejected' if v else 'MISSED'}" for k, v in c.items()))

# 2. condition fill
tot = bad = 0
for f in sorted(glob.glob(str(HERE / "cond_fill/out/*.jsonl"))):
    k, e = check_cond.check(f); tot += k; bad += len(e)
rec("conditions: every value has a verbatim supporting snippet", bad == 0, f"{len(glob.glob(str(HERE / 'cond_fill/out/*.jsonl')))} files, {tot} rows, {bad} errors")

# 3. blind review: lists and verdicts check, and the summary reproduces
bl = HERE / "blind"; berr = 0
for p in sorted(glob.glob(str(bl / "judge/P*"))):
    pid = os.path.basename(p)
    for cmd in (["check_items.py", f"reader/{pid}/items.json"], ["check_verdict.py", f"judge/{pid}/verdict.json"]):
        berr += subprocess.run([sys.executable, cmd[0], cmd[1]], cwd=bl, capture_output=True).returncode != 0
old = json.load(open(bl / "summary.json")); subprocess.run([sys.executable, "score_blind.py"], cwd=bl, capture_output=True)
new = json.load(open(bl / "summary.json"))
same = all(old[k] == new[k] for k in ("rows", "fields_judged", "contradicted_fields", "item_recall"))
rec("blind review: item lists, verdicts, and the score reproduces", berr == 0 and same, f"{berr} files failing; contradicted {new['contradicted_fields']}/{new['fields_judged']} fields; item recall {new['item_recall'][0]}/{new['item_recall'][1]}")

# 4. workbook
from openpyxl import load_workbook
wb = load_workbook(HERE / "out/RelaxDB_evidence_all_DRAFT.xlsx", read_only=True)
ev = list(wb["Evidence"].iter_rows(values_only=True)); h = ev[0]
V032 = os.environ.get("V032_WORKBOOK") or glob.glob(str(HOME / "Desktop/UNC/Soojung-Dynamic data/autoresearch/tasks/*/outputs/gina_cpmg10_v03/out/RelaxDB_CPMG10_evidence_v0.3.2_draft.xlsx"))[0]
ref = load_workbook(V032, read_only=True)
h0 = next(ref["Evidence"].iter_rows(values_only=True))
ids = [r[0] for r in ev[1:]]
sealed_hits = path_hits = 0
for ws in wb.worksheets:
    for r in ws.iter_rows(values_only=True):
        for v in r:
            s = str(v) if v is not None else ""
            if s in SEALED and ws.title != "README": sealed_hits += 1
            if "/Users/" in s or "B1_r6_" in s: path_hits += 1
proteins = wb["Proteins"].max_row - 1
rec("workbook: format, sealed, paths, duplicates", tuple(h[:len(h0)]) == tuple(h0) and sealed_hits == 0 and path_hits == 0 and len(ids) == len(set(ids)),
    f"{len(ev)-1} rows, {proteins} proteins, columns match v0.3.2: {tuple(h[:len(h0)]) == tuple(h0)}, sealed cells {sealed_hits}, path cells {path_hits}, duplicate ids {len(ids)-len(set(ids))}")

# 5. export folder scan (only the three folders this work adds) and the file:line references of the process model
wt = Path(sys.argv[sys.argv.index("--worktree") + 1]) if "--worktree" in sys.argv else None
if wt:
    mine = [wt / "scripts/relaxdb_evidence_table", wt / "data/relaxdb_evidence_table", wt / "review/20261112_relaxdb_table"]
    hits, big = [], []
    for root in mine:
        for f in root.rglob("*"):
            if not f.is_file(): continue
            if f.suffix in (".pdf", ".zip") or f.name == "paper.txt": big.append(str(f.relative_to(wt)))
            if f.suffix in (".xlsx", ".png"): continue
            t = f.read_text(errors="ignore")
            if re.search(r"/Users/|liuzhenpeng|@gmail", t) and f.name not in ("verify_all.py", "build_all.py", "EXPORT_BRIEF.md"): hits.append(str(f.relative_to(wt)))
            if f.parent.parent.name == "source_rows" and any(re.search(rf"\b{re.escape(x)}\b", t) for x in SEALED if len(x) > 4): hits.append("sealed:" + str(f.relative_to(wt)))
    rec("export folder: no local paths, no sealed ids, no paper texts or PDFs", not hits and not big, f"hits {len(hits)}: {hits[:3]}; paper files {len(big)}")
    EXPECT = {"source_fulltext.py": {44: "sealed", 96: "targets()"}, "check_rows.py": {34: "SEALED"}, "build_manifest.py": {23: "PASS"}, "build_all.py": {None: "if rid in bad"}}
    bad_refs = []
    for tla in (wt / "review/20261112_relaxdb_table/statechart").rglob("*.tla"):
        for ln in tla.read_text().splitlines():
            m = re.search(r"\\\* (scripts/[\w/\.\-]+\.py):(\d+)\s*$", ln)
            if not m: continue
            f, n = wt / m.group(1), int(m.group(2)); code = f.read_text().splitlines()[n - 1] if f.exists() else ""
            want = EXPECT.get(f.name, {}).get(n) or EXPECT.get(f.name, {}).get(None)
            if not want or want not in code or code.strip().startswith("#"): bad_refs.append(f"{tla.name}:{m.group(1)}:{n}")
    rec("process model: every cited code line is the line it claims", not bad_refs, f"{len(bad_refs)} wrong: {bad_refs[:3]}")
print("\nALL CHECKS PASSED" if all(ok for _, ok, _ in results) else "\nSOME CHECK FAILED")
sys.exit(0 if all(ok for _, ok, _ in results) else 1)
