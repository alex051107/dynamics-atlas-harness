"""Deterministic grading of one run directory against the sealed reference (Table 1 + Source Data MOESM5).

Usage: python grade_run.py RUN_DIR [RUN_DIR ...]
Prints, per variant, every global fit (experiments, residue count, kex, p1, k21) with its deviation from
Table 1 and the sign/value agreement of per-residue dwN with the authors' final signed values.
"""
import glob, json, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent))
from ref_tables import load_ref

TABLE1 = {"WT": {"kex": (400, 12), "p1": (10.15, 0.47), "k21": (40.6, 2.2)},
          "G12C": {"kex": (326, 11), "p1": (6.97, 0.17), "k21": (22.7, 0.9)},
          "G12D": {"kex": (301, 17), "p1": (9.00, 0.44), "k21": (27.1, 2.0)}}
REF = {v: load_ref(v) for v in TABLE1}

def grade(run_dir, offset=0):
    out = []
    fits = sorted(glob.glob(str(Path(run_dir) / "fits" / "*.json")))
    for f in fits:
        d = json.load(open(f))
        if d.get("mode") != "global" or "kex[*]" not in d["global"]:
            continue
        v = d["variant"]; kex = d["global"]["kex[*]"]; pb = d["global"]["pb[*]"]
        ref = REF[v]; rows = []
        for r, x in d["per_residue"].items():
            n = int("".join(c for c in r[1:] if c.isdigit())) - offset
            if "dwN" in x and n in ref["dw"]:
                rows.append((r, ref["dw"][n], x["dwN"]))
        has_cest = any("cest" in e for e in d["experiments"])
        sign = sum(np.sign(a) == np.sign(b) for _, a, b in rows)
        absr = np.corrcoef([abs(a) for _, a, _ in rows], [abs(b) for _, _, b in rows])[0, 1] if len(rows) > 2 else float("nan")
        t = TABLE1[v]
        out.append({"fit": d["fit_id"], "variant": v, "n_res": len(d["per_residue"]), "cest": has_cest,
                    "kex": round(kex, 1), "kex_dev_%": round(100 * (kex - t["kex"][0]) / t["kex"][0], 1),
                    "p1_%": round(100 * pb, 2), "p1_dev_%": round(100 * (100 * pb - t["p1"][0]) / t["p1"][0], 1),
                    "k21": round(kex * pb, 1), "sign_agree": f"{sign}/{len(rows)}" if has_cest else "n/a (no CEST)",
                    "abs_dw_r": round(float(absr), 3), "red_chi2": d.get("reduced_chi2")})
    return out

if __name__ == "__main__":
    args = sys.argv[1:]
    off = 0
    if args and args[0].startswith("--offset="):
        off = int(args.pop(0).split("=")[1])
    for rd in args:
        print("\n##", rd)
        for r in grade(rd, off):
            print(r)
