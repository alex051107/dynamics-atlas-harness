"""Load the sealed reference (Source Data MOESM5) and compute Table-2 style correlations."""
import json, sys
import numpy as np, openpyxl
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
SUPP = HERE / "reference_sealed/supp/41594_2023_1070_MOESM5_ESM.xlsx"

def load_ref(variant="WT"):
    ws = openpyxl.load_workbook(SUPP, read_only=True, data_only=True)[variant]
    rows = list(ws.iter_rows(values_only=True))[2:]
    g, dw, dwe, gdp, rc = {}, {}, {}, {}, {}
    for r in rows:
        if r[0] is not None and r[2] is not None: g[int(r[0])] = float(r[2])
        if r[4] is not None and r[6] is not None: dw[int(r[4])] = float(r[6]); dwe[int(r[4])] = float(r[7] or 0)
        if r[9] is not None and r[11] is not None: gdp[int(r[9])] = float(r[11])
        if len(r) > 15 and r[13] is not None and r[15] is not None: rc[int(r[13])] = float(r[15])
    return {"ground": g, "dw": dw, "dw_err": dwe, "gdp": gdp, "rc": rc}

def corr(x, y):
    x, y = np.asarray(x), np.asarray(y)
    r2 = np.corrcoef(x, y)[0, 1] ** 2
    rmsd = float(np.sqrt(np.mean((x - y) ** 2)))
    return round(float(r2), 3), round(rmsd, 2), len(x)

def table2(ground, dw, gdp, rc, dw_min=0.0, residues=None):
    out = {}
    def sel(lo, hi, need):
        return [n for n in sorted(dw) if lo <= n <= hi and all(n in d for d in need) and abs(dw[n]) >= dw_min
                and (residues is None or n in residues)]
    for name, (lo, hi) in {"SwitchI_29-37": (29, 37), "SwitchII_59-78": (59, 78)}.items():
        s = sel(lo, hi, [ground, rc])
        if len(s) > 2: out[f"{name} RC-GTP"] = corr([rc[n] - ground[n] for n in s], [dw[n] for n in s])
        s = sel(lo, hi, [ground, gdp])
        if len(s) > 2: out[f"{name} GDP-GTP"] = corr([gdp[n] - ground[n] for n in s], [dw[n] for n in s])
    s = sel(1, 86, [ground, gdp])
    if len(s) > 2: out["lobe1-86 GDP vs ES"] = corr([gdp[n] for n in s], [ground[n] + dw[n] for n in s])
    return out

if __name__ == "__main__":
    ref = load_ref(sys.argv[1] if len(sys.argv) > 1 else "WT")
    print({k: len(v) for k, v in ref.items()})
    print("PAPER Table 2 (WT): SwI RC 0.875/2.10, SwI GDP 0.951/3.05, SwII RC 0.473/3.39, SwII GDP 0.686/1.56, lobe GDP 0.881/2.15")
    for m in (0.0, 0.5):
        print(f"|dw|>={m}:", table2(ref["ground"], ref["dw"], ref["gdp"], ref["rc"], dw_min=m))
