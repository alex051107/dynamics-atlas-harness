#!/usr/bin/env python3
"""Check rows written by a source-paper reader against the paper text. No model.
  check_rows.py source_read/<entry>__<doi_key>      -> prints one line per error, exit 1 on any
Errors: anchor_not_in_text, number_not_in_text, empty_without_reason, bad_reason, bad_enum, sealed_entry, missing_field."""
import os
import json, re, sys, unicodedata
from pathlib import Path
SEALED = set(map(str, json.load(open(Path.home() / "dynamics_atlas_eval/gold/splits.json"))["sealed"]))
REQ = ["entry_id", "doi", "method_class", "experiment", "temperature", "ph", "buffer", "ligand_or_partner", "construct_or_mutation",
       "residues_author", "timescale", "population", "alt_state_structure", "related_structures", "author_claim", "stance",
       "species_relation", "same_sample_as_deposit", "anchor", "locator", "caveat_note", "empty_reasons"]
NEED_REASON = ["temperature", "ph", "buffer", "residues_author", "timescale", "population"]
REASONS = {"not_reported_in_paper", "in_figure_or_SI_not_in_text", "not_applicable_to_this_method", "text_not_available"}
METHODS = {"nmr_relaxation_dispersion", "nmr_spin_relaxation", "nmr_exchange_broadening", "nmr_ensemble_restraints", "xray_multitemp_ensemble",
           "time_resolved_structural", "fret", "epr_deer", "hdx_ms", "md_simulation", "pdb_structure_comparison", "other"}
STANCE = {"supports_dynamics", "no_dynamics_in_window", "unclear_second_process", "artefact_suspected"}
REL = {"target", "same_protein_other_construct", "homolog"}
NUM = re.compile(r"\d+(?:[.,]\d+)*")

def squash(s):
    s = unicodedata.normalize("NFKC", s).replace("−", "-").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", "", s).lower()

def check(folder):
    folder = Path(folder)
    text = squash((folder / "paper.txt").read_text(errors="replace"))
    digits = text.replace(",", "")
    errs = []
    rows = [json.loads(l) for l in (folder / "rows.jsonl").read_text().splitlines() if l.strip()]
    for r in rows:
        rid = r.get("row_id", "?")
        for f in REQ:
            if f not in r: errs.append((rid, "missing_field", f))
        if str(r.get("entry_id")) in SEALED: errs.append((rid, "sealed_entry", r.get("entry_id")))
        for f, allowed in (("method_class", METHODS), ("stance", STANCE), ("species_relation", REL)):
            if r.get(f) not in allowed: errs.append((rid, "bad_enum", f"{f}={r.get(f)}"))
        a = r.get("anchor") or ""
        if len(a.split()) < 8 or squash(a) not in text: errs.append((rid, "anchor_not_in_text", a[:70]))
        for f in ("timescale", "population", "temperature", "ph"):
            for n in NUM.findall(str(r.get(f) or "")):
                if n.replace(",", "") not in digits: errs.append((rid, "number_not_in_text", f"{f}: {n}"))
        for pdb in re.findall(r"\b[1-9][A-Za-z0-9]{3}\b(?=:)", str(r.get("alt_state_structure") or "")):
            if pdb.lower() not in text: errs.append((rid, "number_not_in_text", f"pdb: {pdb}"))
        er = r.get("empty_reasons") or {}
        for f in NEED_REASON:
            if not str(r.get(f) or "").strip():
                if f not in er: errs.append((rid, "empty_without_reason", f))
                elif er[f] not in REASONS: errs.append((rid, "bad_reason", f"{f}={er[f]}"))
    return rows, errs

if __name__ == "__main__":
    rows, errs = check(sys.argv[1])
    for e in errs: print(*e, sep="\t")
    print(f"{len(rows)} rows, {len(errs)} errors")
    sys.exit(1 if errs else 0)
