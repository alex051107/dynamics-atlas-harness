"""Summarise what each v3 run actually did (evidence for the preregistered judgement).

Usage: python v3_actions.py RUN_DIR [...]
"""
import json, sys
from pathlib import Path

def summarise(rd):
    rd = Path(rd)
    acts = [json.loads(l) for l in open(rd / "actions.jsonl")]
    s = {"run": rd.name, "calls": len(acts), "errors": sum(a["error"] for a in acts), "reflections": 0,
         "models_tried": set(), "groups_fits": 0, "gdp_control_used": set(), "pdb": [], "reference_comparisons": [],
         "references_listed": False}
    for a in acts:
        t, g, r = a["tool"], a["args"], a["result"] if isinstance(a["result"], dict) else {}
        if t == "reflect": s["reflections"] += 1
        if t == "fit_exchange" and not a["error"]:
            s["models_tried"].add(g.get("model", "two_state") + ("+groups" if g.get("groups") else "") + ("/" + g.get("mode", "global")))
            if g.get("groups"): s["groups_fits"] += 1
        if g.get("variant", "").endswith("_GDP"): s["gdp_control_used"].add(f"{t}:{g['variant']}")
        if t == "pdb_ligand_distances": s["pdb"].append((g.get("pdb_id"), g.get("ligand"), g.get("ligand_atoms")))
        if t == "reference_shifts" and g.get("action") == "list": s["references_listed"] = True
        if t == "compare_references" and not a["error"]:
            s["reference_comparisons"].append({"variant": g.get("variant"), "fit": g.get("fit_id"), "n_res": len(g.get("residues", [])),
                "res": ",".join(g.get("residues", [])[:12]),
                "refs": {k: (round(v["r_squared"], 3) if v["r_squared"] is not None else None, round(v["rmsd_ppm"], 2), v["n"]) for k, v in r.get("references", {}).items()}})
    s["models_tried"] = sorted(s["models_tried"]); s["gdp_control_used"] = sorted(s["gdp_control_used"])
    atlas = rd / "ATLAS_ENTRIES.json"
    s["atlas_entries"] = len(json.loads(atlas.read_text()) or []) if atlas.exists() else 0
    s["report"] = (rd / "REPORT.md").exists()
    return s

if __name__ == "__main__":
    for rd in sys.argv[1:]:
        s = summarise(rd)
        comps = s.pop("reference_comparisons")
        print(json.dumps(s, ensure_ascii=False))
        for c in comps: print("   compare:", json.dumps(c, ensure_ascii=False))
