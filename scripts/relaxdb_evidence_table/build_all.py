#!/usr/bin/env python3
"""Merge every existing evidence-row source into one workbook in the v0.3.2 Evidence format (Gina's agreed format).
Rerunnable: reads inputs only, writes out/RelaxDB_evidence_all_DRAFT.xlsx. Run with ~/.venvs/taskfactory/bin/python."""
import os
import csv, json, re, glob, sys, collections, importlib
from pathlib import Path
from urllib.parse import quote as urlquote
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

HERE = Path(__file__).resolve().parent
HOME = Path.home()
W = HOME / "dynamics_atlas_work"
WS = Path(os.environ["ATLAS_WORKSPACE"]) / "autoresearch/tasks/dynamics_atlas_stage1_loop_20261002/outputs"
V032 = WS / "gina_cpmg10_v03/out/RelaxDB_CPMG10_evidence_v0.3.2_draft.xlsx"
V02 = WS / "delivery_table_v02/out/Dynamics_Atlas_RelaxDB_v0.2_draft.xlsx"
OUT = HERE / "out" / "RelaxDB_evidence_all_DRAFT.xlsx"
sys.path.insert(0, str(HERE))
check_rows = importlib.import_module("check_rows")

sealed = set(map(str, json.load(open(HOME / "dynamics_atlas_eval/gold/splits.json"))["sealed"]))
spine_all = list(csv.DictReader(open(W / "outputs/spine_20261112/spine.csv")))
spine = [s for s in spine_all if s["entry_id"] not in sealed and s["status"] == "open"]
spine_by = {s["entry_id"]: s for s in spine}

ILLEGAL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
def clean(v):
    if v is None: return ""
    if isinstance(v, (int, float)) and not isinstance(v, bool): return v
    return ILLEGAL.sub("", str(v))

# ---- column contract -------------------------------------------------------------------------------------------------
wb32 = load_workbook(V032, read_only=True)
ev32 = list(wb32["Evidence"].iter_rows(values_only=True))
COLS = list(ev32[0]) + ["Filled by", "Checks passed"]
IDX = {c: i for i, c in enumerate(COLS)}
def blank(): return [""] * len(COLS)

stats = collections.OrderedDict()   # input -> dict(read, written, dropped Counter)
def stat(name):
    return stats.setdefault(name, {"read": 0, "written": 0, "dropped": collections.Counter()})

evidence = []       # list of dicts: cells (list), meta
def add(name, cells, entry, meta):
    st = stat(name)
    if entry in sealed:
        st["dropped"]["sealed entry"] += 1; return
    evidence.append({"cells": cells, "entry": entry, "input": name, **meta}); st["written"] += 1

# ---- input 1: v0.3.2 ------------------------------------------------------------------------------------------------
N1 = "1 CPMG-10 workbook v0.3.2"
for r in ev32[1:]:
    if not r or not r[0]: continue
    stat(N1)["read"] += 1
    cells = [clean(x) for x in r] + ["11-01 workbook v0.3.2", "quote checked against cached full text in v0.3.2"]
    add(N1, cells, str(r[1]), {"has_cond": True})

# ---- input 2: v0.2 table --------------------------------------------------------------------------------------------
N2 = "2 11-01 table v0.2"
wb02 = load_workbook(V02, read_only=True)
ev02 = list(wb02["Evidence"].iter_rows(values_only=True))
h2 = list(ev02[0]); i2 = {c: i for i, c in enumerate(h2)}
V02MAP = {"evidence_id": "evidence_id", "Protein (RelaxDB entry)": "entry", "Residues / region": "Residues / region",
          "Alternate-state structure": "Alternate-state structure", "Experiment": "Method",
          "Timescale (as reported)": "Timescale (as reported)", "Population (as reported)": "Population (as reported)",
          "Dynamics observed": "Dynamics observed", "Authors' conclusion": "Authors' conclusion",
          "Experiment and conditions": "Experiment and conditions", "Organism / construct vs entry": "Organism / construct vs entry",
          "Caveats / do not combine with": "Do not combine with / limits", "Paper": "paper", "Year": "year",
          "DOI link": "doi_link", "Open full text": "open_full_text", "Quote": "quote", "Location in paper": "location_in_paper",
          "Passage link": "passage_link", "What we read": "what_we_read", "Review priority": "Review priority"}
v02_cond = json.load(open(HERE / "v02_conditions.json"))
# condition fill of 11-12: only files that pass check_conditions are used; only empty cells are filled
sys.path.insert(0, str(HERE / "cond_fill")); check_cond = importlib.import_module("check_conditions")
CF, CF_SKIPPED = {}, 0
for _f in sorted(glob.glob(str(HERE / "cond_fill/out/*.jsonl"))):
    if check_cond.check(_f)[1]: CF_SKIPPED += 1; continue
    for _l in open(_f):
        if _l.strip(): _o = json.loads(_l); CF[_o["evidence_id"]] = _o
TRIP = {tuple(k.split("|")): True for k in json.load(open(HERE / "cond_fill/tripwire.json"))} if (HERE / "cond_fill/tripwire.json").exists() else {}
CF_FILLED = collections.Counter()
for r in ev02[1:]:
    if not r or not r[0]: continue
    stat(N2)["read"] += 1
    if r[i2["set"]] == "CPMG-10":
        stat(N2)["dropped"]["row of one of the 10 CPMG proteins (v0.3.2 workbook supersedes it)"] += 1; continue
    cells = blank()
    for c, src in V02MAP.items():
        cells[IDX[c]] = clean(r[i2[src]])
    found = str(r[i2["quote_found_in_local_full_text"]] or "")
    cells[IDX["Filled by"]] = "11-01 table (Codex)"
    cells[IDX["Checks passed"]] = {"yes": "quote found in local full text", "no": "quote NOT found in local full text"}.get(found, "no quote check recorded")
    vc = v02_cond.get(str(r[i2["evidence_id"]]), {})
    for col, k in (("Temperature (K)", "temperature"), ("pH", "ph"), ("Buffer", "buffer"), ("Ligand / substrate / metal", "ligand"),
                   ("Phosphate", "phosphate"), ("Construct", "construct"),
                   ("Related structures (not an alternate state)", "related_structures"), ("Exchange regime (as stated)", "exchange_regime")):
        cells[IDX[col]] = vc.get(k, "")
    if found == "yes": cells[IDX["Checks passed"]] = "quote and split conditions found in local full text"
    cf = CF.get(str(r[i2["evidence_id"]]))
    if cf:
        did = False
        for col, k in (("Temperature (K)", "temperature"), ("pH", "ph"), ("Buffer", "buffer"), ("Salt", "salt"), ("Ligand / substrate / metal", "ligand"), ("Phosphate", "phosphate")):
            v = str(cf.get(k) or "").strip()
            if v and not cells[IDX[col]]: cells[IDX[col]] = v; CF_FILLED[k] += 1; did = True
            elif not v and not cells[IDX[col]] and k in ("temperature", "ph", "buffer"):
                rs = (cf.get("empty_reasons") or {}).get(k)
                if rs == "not_reported_in_paper" and TRIP.get((cf["evidence_id"], k)): rs = "paper_text_mentions_it_unchecked"
                cells[IDX[col]] = f"[empty: {rs}]" if rs else ""
        cells[IDX["Condition sources"]] = "11-12 condition fill (each value has a verbatim snippet in the row text or the paper text)"
        if did: cells[IDX["Checks passed"]] += "; conditions added 11-12, snippet checked"
    add(N2, cells, str(r[i2["entry"]]), {"has_cond": True})

# ---- JSON rows (inputs 3-5) -----------------------------------------------------------------------------------------
def grab(pattern, text):
    m = re.search(pattern, text, re.S)
    return m.group(1).strip() if m else ""

def json_row(r, prefix, filled_by, checks):
    c = blank()
    oc = r.get("other_conditions") or ""
    er = r.get("empty_reasons") or {}
    def val(field, v):
        v = "" if v is None else str(v)
        if not v.strip() and field in er: return f"[empty: {er[field]}]"
        return v
    entry = str(r["entry_id"])
    c[IDX["evidence_id"]] = f"{prefix}{entry}-{r['row_id']}"
    c[IDX["Protein (RelaxDB entry)"]] = entry
    c[IDX["Residues / region"]] = val("residues_author", r.get("residues_author"))
    c[IDX["Alternate-state structure"]] = r.get("alt_state_structure") or ""
    rel = r.get("related_structures")
    if rel is None or rel == "": rel = grab(r"related structures:\s*(.*?)(?=;\s*regime \(authors\):|$)", oc)
    c[IDX["Related structures (not an alternate state)"]] = rel or ""
    c[IDX["Experiment"]] = r.get("experiment") or ""
    c[IDX["Timescale (as reported)"]] = val("timescale", r.get("timescale"))
    c[IDX["Population (as reported)"]] = val("population", r.get("population"))
    c[IDX["Exchange regime (as stated)"]] = grab(r"regime \(authors\):\s*(.*?)(?=;\s*related structures:|$)", oc)
    c[IDX["Dynamics observed"]] = r.get("dynamics_type") or ""
    c[IDX["Authors' conclusion"]] = r.get("author_claim") or ""
    c[IDX["Experiment and conditions"]] = oc
    c[IDX["Temperature (K)"]] = val("temperature", r.get("temperature"))
    c[IDX["pH"]] = val("ph", r.get("ph"))
    buf = val("buffer", r.get("buffer"))
    c[IDX["Buffer"]] = buf
    c[IDX["Ligand / substrate / metal"]] = r.get("ligand_or_partner") or ""
    c[IDX["Phosphate"]] = "yes" if "phosphate" in buf.lower() else ""
    c[IDX["Construct"]] = r.get("construct_or_mutation") or ""
    c[IDX["Same sample as RelaxDB entry?"]] = r.get("same_sample_as_deposit") or "not assessed"
    c[IDX["Organism / construct vs entry"]] = r.get("species_relation") or ""
    c[IDX["Caveats / do not combine with"]] = " ".join(x for x in [r.get("caveat_note"), r.get("artefact_note")] if x)
    c[IDX["Paper"]] = r.get("title") or ""
    c[IDX["Year"]] = r.get("year") or ""
    doi = (r.get("doi") or "").strip()
    c[IDX["DOI link"]] = f"https://doi.org/{doi}" if doi else ""
    m = re.fullmatch(r"(PMC\d+)\.txt", str(r.get("source_file") or ""))
    c[IDX["Open full text"]] = f"https://pmc.ncbi.nlm.nih.gov/articles/{m.group(1)}/" if m else ""
    anchor = r.get("anchor") or ""
    c[IDX["Quote"]] = anchor
    c[IDX["Location in paper"]] = r.get("locator") or ""
    base = c[IDX["Open full text"]] or c[IDX["DOI link"]]
    c[IDX["Passage link"]] = base + "#:~:text=" + urlquote(" ".join(anchor.split()[:8]), safe="") if base and anchor else ""
    c[IDX["What we read"]] = "abstract_only" if r.get("access") == "abstract_only" else ("full_text" if r.get("access") in (None, "", "full_text") else r.get("access"))
    c[IDX["Review priority"]] = "A - please check" if r.get("review_priority") else ""
    c[IDX["Filled by"]] = filled_by
    c[IDX["Checks passed"]] = checks
    return c, entry

def read_jsonl(p):
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []

known = {e["entry"] for e in evidence}   # entries already having rows (coverage.py rule for race entries)

# input 3: run133 (Sonnet)
N3 = "3 11-11 run (Sonnet)"
state = json.load(open(W / "ledger/run133_state.json"))
run_status = {}
for e, v in state.items():
    if "fill" not in v: continue
    run_status[e] = v["status"]
    ok = bool(v["fill"].get("integrity_pass"))
    chk = "quote integrity check passed" if ok else "quote integrity check NOT passed"
    for r in read_jsonl(W / "cases" / v["fill"]["case"] / "rows.jsonl"):
        stat(N3)["read"] += 1
        c, ent = json_row(r, "", "11-11 run (Sonnet)", chk)
        add(N3, c, ent, {"has_cond": True})
known = {e["entry"] for e in evidence}

# input 4: race entries
N4 = "4 11-10 race (Opus arm B)"
for e in ["6470", "7432", "11080", "17783", "18477", "26513", "50734", "BPTI", "IL4", "IRSPTB", "PCF11", "VMIPII"]:
    if e in known or e in sealed: continue
    cs = sorted(glob.glob(str(W / f"cases/B1_r6_{e}_*")))
    if not cs: continue
    try:
        ok = bool(json.load(open(Path(cs[-1]) / "scorecard.json"))["integrity"]["pass"])
    except Exception:
        ok = False
    chk = "quote integrity check passed" if ok else "quote integrity check not recorded as passed"
    for r in read_jsonl(Path(cs[-1]) / "rows.jsonl"):
        stat(N4)["read"] += 1
        c, ent = json_row(r, "", "11-10 race (Opus arm B)", chk)
        add(N4, c, ent, {"has_cond": True})

# input 5: source_read (may be empty or grow)
N5 = "5 11-12 source-paper read"
stat(N5)
src_entries = set()
try:
    _man = json.load(open(HERE / "source_read/manifest.json"))
    manifest_title = {m["doi"].lower(): m.get("title", "") for m in _man}
    manifest_year = {m["doi"].lower(): m.get("year", "") for m in _man}
    manifest_pmc = {m["doi"].lower(): m.get("pmcid", "") for m in _man}
except Exception:
    manifest_title = {}; manifest_year = {}; manifest_pmc = {}
seen_ids = {e["cells"][0] for e in evidence}
for folder in sorted(glob.glob(str(HERE / "source_read/*/rows.jsonl"))):
    fdir = Path(folder).parent
    rows, errs = check_rows.check(fdir)
    bad = collections.defaultdict(list)
    for rid, kind, _ in errs: bad[rid].append(kind)
    doikey = fdir.name.split("__", 1)[-1]
    for r in rows:
        stat(N5)["read"] += 1
        rid = r.get("row_id", "?")
        if rid in bad:  # only rows that passed check_rows reach the workbook
            stat(N5)["dropped"]["failed the automatic row check: " + ", ".join(sorted(set(bad[rid])))] += 1
            continue
        chk = "all automatic checks passed (anchor and numbers found in paper text)"
        c, ent = json_row(r, "S-", "11-12 source-paper read with supplement", chk)
        dk = (r.get("doi") or "").lower()
        if not c[IDX["Paper"]]: c[IDX["Paper"]] = manifest_title.get(dk, "")
        if not c[IDX["Year"]]: c[IDX["Year"]] = manifest_year.get(dk, "") or ""
        if not c[IDX["Open full text"]] and manifest_pmc.get(dk):
            c[IDX["Open full text"]] = f"https://pmc.ncbi.nlm.nih.gov/articles/{manifest_pmc[dk]}/"
            if c[IDX["Quote"]]:
                c[IDX["Passage link"]] = c[IDX["Open full text"]] + "#:~:text=" + urlquote(" ".join(c[IDX["Quote"]].split()[:8]), safe="")
        if c[0] in seen_ids:
            c[0] = f"S-{ent}-{doikey}-{rid}"
        seen_ids.add(c[0])
        add(N5, c, ent, {"has_cond": True})
        if ent not in sealed: src_entries.add(ent)

# ---- derived tables -------------------------------------------------------------------------------------------------
def g(e, col): return e["cells"][IDX[col]]
NOVAL = ("", "not reported", "none", "no structure", "not stated", "not in record", "full text not available", "not applicable",
         "[empty", "not assessed")
def has_value(v):
    v = str(v).strip().lower()
    return bool(v) and not any(v.startswith(n) for n in NOVAL if n)

by_entry = collections.defaultdict(list)
for e in evidence: by_entry[e["entry"]].append(e)
def is_full(e): return g(e, "What we read") == "full_text"
def is_homolog(e): return str(g(e, "Organism / construct vs entry")).lower().startswith("homolog")
def is_ok(e): return "NOT" not in str(g(e, "Checks passed")) and "not recorded" not in str(g(e, "Checks passed"))
def good(e): return is_full(e) and is_ok(e) and not is_homolog(e)

ITEMS = [("Residues / region", "residues", False), ("Alternate-state structure", "alt-state PDB", False),
         ("Timescale (as reported)", "timescale", False), ("Population (as reported)", "population", False),
         ("Temperature (K)", "temperature", True), ("pH", "pH", True), ("Buffer", "buffer", True)]

def filled_by(entry):
    inputs = []
    for e in by_entry.get(entry, []):
        f = g(e, "Filled by")
        if f not in inputs: inputs.append(f)
    if not inputs: return "not filled"
    s = "; ".join(inputs)
    st = run_status.get(entry)
    if st and st != "FILLED": s += f" ({st})"
    return s

def dep_fields(s):
    t, to = (s["bmrb_temperature"], "BMRB") if s["bmrb_temperature"] else (s["sheet_temperature_K"], "Gina's sheet")
    if t and not s["bmrb_temperature"] and s["sheet_temperature_K"].strip() in ("298.5", "298.50"): t = "298.5 (possible placeholder)"
    f, fo = (s["bmrb_relaxation_field_MHz"], "BMRB") if s["bmrb_relaxation_field_MHz"] else (s["sheet_field_MHz"], "Gina's sheet")
    return [(t, to if t else ""), (f, fo if f else ""), (s["bmrb_pH"], "BMRB" if s["bmrb_pH"] else ""),
            (s["bmrb_sample_components"], "BMRB" if s["bmrb_sample_components"] else "")]

def cause(entry, col, is_cond):
    rs = by_entry.get(entry, [])
    if run_status.get(entry) == "FILL_CALLS_FAILED": return "calls failed"
    if not rs: return "not filled yet"
    pool = [e for e in rs if e["has_cond"]] if is_cond else rs
    full = [e for e in pool if good(e)]
    if full: return "read in full, not found"
    if is_cond and any(good(e) for e in rs): return "not filled yet"       # only rows from the 11-01 table, which has no condition columns
    ab = {(g(e, "DOI link") or g(e, "Paper")) for e in rs if not is_full(e)}
    if ab: return f"no full text read ({len(ab)} papers abstract only)"
    return "not filled yet"

proteins_rows, gaps_rows = [], []
for s in spine:
    en = s["entry_id"]; rs = by_entry.get(en, [])
    gd = [e for e in rs if good(e)]
    d = dep_fields(s)
    cnt = [sum(has_value(g(e, col)) for e in gd) for col, _, _ in ITEMS[:4]]
    papers = {(g(e, "DOI link") or g(e, "Paper")) for e in rs}
    proteins_rows.append([en, s["set"], s["protein_name"], s["uniprot"], s["sequence_length"], d[0][0], d[0][1], d[1][0], d[1][1],
                          d[2][0], d[2][1], d[3][0], d[3][1], len(rs), sum(is_full(e) for e in rs), len(papers - {""})] + cnt + [filled_by(en)])
    for col, label, is_cond in ITEMS:
        pool = [e for e in gd if (e["has_cond"] or not is_cond)]
        if not any(has_value(g(e, col)) for e in pool):
            gaps_rows.append([en, s["protein_name"], label, cause(en, col, is_cond), filled_by(en)])

paper_acc = collections.OrderedDict()
for e in evidence:
    k = (g(e, "DOI link") or g(e, "Paper")).lower()
    p = paper_acc.setdefault(k, {"Paper": g(e, "Paper"), "Year": g(e, "Year"), "DOI link": g(e, "DOI link"), "Open full text": "",
                                  "entries": set(), "n": 0, "full": False})
    p["entries"].add(e["entry"]); p["n"] += 1
    p["full"] = p["full"] or is_full(e)
    if not p["Open full text"]: p["Open full text"] = g(e, "Open full text")
    if not p["Paper"]: p["Paper"] = g(e, "Paper")
    if not p["Year"]: p["Year"] = g(e, "Year")
papers_rows = [[p["Paper"], p["Year"], p["DOI link"], p["Open full text"], ", ".join(sorted(p["entries"])), p["n"],
                "full_text" if p["full"] else "abstract_only"] for p in paper_acc.values()]
papers_rows.sort(key=lambda r: (str(r[2]).lower(), str(r[0])))

PDB = re.compile(r"\b([1-9][A-Z0-9]{3})\b")
struct = collections.OrderedDict()
for e in evidence:
    txt = str(g(e, "Alternate-state structure"))
    for pid in PDB.findall(txt):
        if not re.search(r"[A-Z]", pid): continue
        k = (e["entry"], pid)
        if k not in struct: struct[k] = [e["entry"], pid, txt, [g(e, "evidence_id")]]
        else: struct[k][3].append(g(e, "evidence_id"))
struct_rows = [[a, b, t, ", ".join(ids)] for (a, b), (_, _, t, ids) in sorted(struct.items())]

# ---- write workbook -------------------------------------------------------------------------------------------------
OUT.parent.mkdir(parents=True, exist_ok=True)
wbo = Workbook(); wbo.remove(wbo.active)
HF = Font(bold=True); HFILL = PatternFill("solid", fgColor="DDE6F0")
def sheet(name, header, rows, widths=None, wrap=()):
    ws = wbo.create_sheet(name); ws.append(header)
    for c in ws[1]: c.font = HF; c.fill = HFILL; c.alignment = Alignment(wrap_text=True, vertical="top")
    for r in rows: ws.append([clean(x) for x in r])
    ws.freeze_panes = "B2"
    if ws.max_row > 1: ws.auto_filter.ref = f"A1:{get_column_letter(len(header))}{ws.max_row}"
    for i, h in enumerate(header, 1):
        ws.column_dimensions[get_column_letter(i)].width = (widths or {}).get(h, 22)
    for h in wrap:
        ci = header.index(h) + 1
        for row in ws.iter_rows(min_row=2, min_col=ci, max_col=ci):
            for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
    return ws

readme = [["Draft. Rows from 11-11 have not had a blind accuracy check."],
          [""], ["Sheets"],
          ["Proteins: one row per open RelaxDB protein (spine), deposited conditions with the origin of each value, and counts. A sheet temperature of exactly 298.5 K with no BMRB value is marked as a possible placeholder. The four value counts use full-text rows on the target or another construct of the same protein (homolog rows excluded) whose quote passed its automatic check."],
          ["Evidence: every row, in the column order of the 11-01 workbook (v0.3.2), plus 'Filled by' and 'Checks passed'. Rows that came from the 11-01 table (v0.2) have their condition columns (temperature, pH, buffer and so on) split from the original reader records and each value checked against the local full text of that row's paper; a blank there means the paper text gave no value. '[empty: reason]' marks a cell the reader left empty with a stated reason."],
          ["Papers: one row per DOI."],
          ["Structures: one row per protein and PDB id found in 'Alternate-state structure'."],
          ["Gaps: one row per protein and item without a full-text value, with the cause the data shows."],
          [""], ["Evidence rows per input (read / written)"]]
for n, st in stats.items():
    readme.append([f"{n}: read {st['read']}, written {st['written']}" + "".join(f"; dropped {c} ({why})" for why, c in st["dropped"].items())])
readme.append([f"Total Evidence rows: {len(evidence)}; open proteins: {len(spine)}."])
ws = wbo.create_sheet("README")
for r in readme: ws.append(r)
ws.column_dimensions["A"].width = 140
for row in ws.iter_rows():
    for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
ws["A1"].font = HF

PH = ["entry", "set", "protein", "UniProt", "length", "deposited temperature (K)", "temperature from", "field (MHz)", "field from",
      "pH", "pH from", "sample components", "sample components from", "evidence rows", "full-text rows", "papers",
      "full-text rows with residues", "full-text rows with alt-state PDB", "full-text rows with timescale",
      "full-text rows with population", "Filled by"]
sheet("Proteins", PH, proteins_rows, {"protein": 40, "sample components": 50, "Filled by": 40})
ev_ws = sheet("Evidence", COLS, [e["cells"] for e in evidence],
              {"evidence_id": 14, "Protein (RelaxDB entry)": 16, "Residues / region": 50, "Alternate-state structure": 50, "Related structures (not an alternate state)": 40,
               "Experiment and conditions": 60, "Authors' conclusion": 50, "Caveats / do not combine with": 50, "Paper": 50, "Quote": 60,
               "DOI link": 36, "Open full text": 36, "Passage link": 36, "Checks passed": 40, "Filled by": 32})
sheet("Papers", ["Paper", "Year", "DOI link", "Open full text", "Entries", "Evidence rows", "What we read"], papers_rows, {"Paper": 60, "DOI link": 36, "Open full text": 36, "Entries": 30})
sheet("Structures", ["Protein (RelaxDB entry)", "PDB ID", "State as assigned", "Row id"], struct_rows, {"State as assigned": 80, "Row id": 40}, wrap=("State as assigned",))
sheet("Gaps", ["Protein (RelaxDB entry)", "Protein", "Item", "Cause", "Filled by"], gaps_rows, {"Protein": 40, "Cause": 44, "Filled by": 40})
wbo.move_sheet("README", offset=len(wbo.sheetnames))
wbo.save(OUT)

# ---- self-check -----------------------------------------------------------------------------------------------------
print("SELF-CHECK")
tr = tw = 0
for n, st in stats.items():
    d = sum(st["dropped"].values())
    print(f"  {n}: read {st['read']}, written {st['written']}, dropped {d}" + "".join(f"  [{c} x {why}]" for why, c in st["dropped"].items()))
    assert st["read"] == st["written"] + d
    tr += st["read"]; tw += st["written"]
print(f"  total read {tr}, written {tw}; Evidence sheet rows {len(evidence)}")
print(f"  proteins in Proteins sheet: {len(proteins_rows)} (expect 131)")
chk = load_workbook(OUT, read_only=True)
sealed_hits = path_hits = 0
for ws in chk:
    for row in ws.iter_rows(values_only=True):
        for v in row:
            if not isinstance(v, str): continue
            if "/Users/" in v or "B1_r6_" in v: path_hits += 1
            toks = set(re.split(r"[,\s]+", v)) if len(v) < 400 else set()
            if (v in sealed or toks & sealed) and ws.title != "README": sealed_hits += 1
            if ws.title == "Evidence" and any(v.startswith(s + "-") or v.startswith("S-" + s + "-") for s in sealed) and re.fullmatch(r"(S-)?[A-Za-z0-9]+-\w+", v): sealed_hits += 1
print(f"  sealed ids found in any cell: {sealed_hits} (expect 0)")
print(f"  cells containing '/Users/' or 'B1_r6_': {path_hits} (expect 0)")
ids = [e["cells"][0] for e in evidence]
print(f"  evidence_id duplicates: {len(ids) - len(set(ids))} (expect 0)")
print(f"  other sheets: Papers {len(papers_rows)}, Structures {len(struct_rows)}, Gaps {len(gaps_rows)}")
print(f"  source_read entries picked up: {sorted(src_entries) or 'none yet'}")
print(f"  written: {OUT}")
