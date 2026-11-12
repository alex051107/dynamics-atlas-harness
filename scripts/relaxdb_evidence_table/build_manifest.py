#!/usr/bin/env python3
"""Build the manifest of source papers that have a checked full text and no reader folder yet.
  build_manifest.py OUT.json [--batches N]
Inputs: spine.csv, source_texts/source_text_status.csv (verdict PASS*), source_texts/results.json (drop files), source_texts/drop/ (supplements named supp_*).
A paper enters the manifest only with a PASS, PASS_OWNER_FILE or PASS_MANUAL identity verdict; sealed entries never do."""
import os
import csv, glob, json, os, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
W = Path.home() / "dynamics_atlas_work"
ST = W / "outputs/spine_20261112/source_texts"
sealed = set(map(str, json.load(open(Path.home() / "dynamics_atlas_eval/gold/splits.json"))["sealed"]))
spine = {r["entry_id"]: r for r in csv.DictReader(open(W / "outputs/spine_20261112/spine.csv"))}
out_path = Path(sys.argv[1]); nb = int(sys.argv[sys.argv.index("--batches") + 1]) if "--batches" in sys.argv else 5
have = {d.split("__", 1)[1] for d in os.listdir(HERE / "source_read") if "__" in d}
res = json.load(open(ST / "results.json"))
dropv = {d["doi"]: d for d in res["drop"] if d.get("doi") and not d["file"].startswith("supp_") and str(d.get("verdict")).startswith("PASS")}
supp_all = [f for f in os.listdir(ST / "drop") if f.startswith("supp_")]
out = []
for r in csv.DictReader(open(ST / "source_text_status.csv")):
    doi, key = r["doi"], r["doi"].replace("/", "_")
    ents = [e for e in r["entries"].split("|") if e not in sealed]
    if not r["verdict"].startswith("PASS") or not ents or key in have: continue
    cands = []
    if doi in dropv:
        cands = glob.glob(str(ST / "staging" / "**" / (Path(dropv[doi]["staged"]).stem + ".txt")), recursive=True)
    if not cands: cands = glob.glob(str(ST / "staging" / "**" / ("access_" + key + "__*.txt")), recursive=True)
    if not cands: print("no text file for", doi); continue
    m = re.search(r"PMC\d+", cands[0] + " " + dropv.get(doi, {}).get("file", ""))
    pmc = m.group(0) if m else ""
    supp = [f for f in supp_all if (pmc and f.startswith(f"supp_{pmc}_")) or key.lower() in f.lower()]
    s = spine[ents[0]]
    out.append({"doi": doi, "entries": ents, "title": r["title"], "pmcid": pmc, "main_text": cands[0], "exists": True,
                "preprint": doi == "10.1021/acs.biochem.1c00749", "local_supplements": [str(ST / "drop" / f) for f in supp],
                "card": {k: s[k] for k in ("protein_name", "uniprot", "sequence_length", "bmrb_id", "bmrb_temperature", "bmrb_pH", "bmrb_relaxation_field_MHz", "sheet_temperature_K", "sheet_field_MHz", "bmrb_sample_components")}})
out.sort(key=lambda x: x["entries"][0])
for i, x in enumerate(out): x["batch"] = i % nb + 1
json.dump(out, open(out_path, "w"), indent=1, ensure_ascii=False)
print(len(out), "papers without a reader folder yet;", sum(bool(x["local_supplements"]) for x in out), "with local supplements")
