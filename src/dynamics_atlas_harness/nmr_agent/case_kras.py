"""K-Ras (Hansen 2023) case assembly for workspace v3: evidence the authors had that the Dryad deposit lacks.

Added from the paper's Source Data (measured values only, answer-bearing columns never read):
- GDP-bound 15N CEST control profiles (MOESM3 sheets 'FigS4 - <V>+GDP CEST'; 10 residues per variant;
  B1 and saturation time from SI Table S1).
- GDP-bound 15N ground-state shifts, same buffer and temperature (MOESM5, GDP column only).
- GDP-bound measured 15N R1 (deposited NASR tables, R1_free).
Also: construct sequence per variant (A0 + native 1-169, checked against every residue label).
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import openpyxl

from .exchange import GAMMA_RATIO_N

GDP_B1 = {"WT": 42.0, "G12C": 44.0, "G12D": 45.0}   # Hz, SI Table S1
CARRIER = 118.0                                        # ppm, nominal (source data give a ppm axis)


def add_case_extras(ws: Path, supp_dir: Path, nasr_dir: Path, native_seq: str, audit: dict) -> None:
    moesm3 = openpyxl.load_workbook(supp_dir / "41594_2023_1070_MOESM3_ESM.xlsx", read_only=True, data_only=True)
    moesm5 = openpyxl.load_workbook(supp_dir / "41594_2023_1070_MOESM5_ESM.xlsx", read_only=True, data_only=True)
    nu_n = 850.16 * GAMMA_RATIO_N
    for v in ("WT", "G12D", "G12C"):
        seq = "A" + native_seq
        if v != "WT":
            seq = seq[:12] + v[-1] + seq[13:]
        (ws / v / "sequence.json").write_text(json.dumps({"first_residue_number": 0, "sequence": seq}, indent=1))
        # GDP-bound ground-state 15N shifts (columns J-L of MOESM5: Num, Res, 15N CS)
        rows = list(moesm5[v].iter_rows(values_only=True))[2:]
        gdp = {f"{r[10]}{int(r[9])}N": float(r[11]) for r in rows if r[9] is not None and r[11] is not None}
        gv = ws / f"{v}_GDP"
        (gv / "data" / "cest_15N_850MHz").mkdir(parents=True)
        (gv / "ground_state_shifts.json").write_text(json.dumps(gdp, indent=0))
        refdir = ws / v / "references"
        refdir.mkdir(exist_ok=True)
        (refdir / "GDP_bound_same_conditions.json").write_text(json.dumps({
            "description": f"Measured backbone 15N shifts of GDP-bound {v} K-Ras4B(1-169), same buffer, 298 K",
            "conditions": {"pH": 7.0, "temperature_K": 298, "buffer": "20 mM HEPES, 5 mM MgCl2"}, "shifts": gdp}, indent=0))
        audit["included"].append({"file": f"MOESM5 sheet {v}, GDP 15N column only", "as": f"{v}_GDP/ground_state_shifts.json, {v}/references/GDP_bound_same_conditions.json"})
        # GDP-bound R1
        r1 = {}
        with open(nasr_dir / f"KRas_{v}_GDP.csv") as fh:
            for row in csv.DictReader(fh):
                if row["R1_free"]:
                    r1[f"{row['Amino_acids']}{int(row['Residue_number'])}N"] = float(row["R1_free"])
        (gv / "measured_R1.json").write_text(json.dumps(r1, indent=0))
        # GDP-bound CEST profiles
        sheet = list(moesm3[f"FigS4 - {v}+GDP CEST"].iter_rows(values_only=True))
        residues, cur, pts = [], None, {}
        for r in sheet:
            if isinstance(r[0], str) and r[0].startswith("["):
                cur = r[0].strip("[]")[:-1]  # "[Y32N]" -> "Y32"
                pts[cur] = []
                continue
            if cur and isinstance(r[0], (int, float)) and r[1] is not None:
                pts[cur].append((float(r[0]), float(r[1]), float(r[2])))
        for res, p in pts.items():
            lines = ["# offset_hz_from_carrier intensity error"] + [f"{(ppm - CARRIER) * nu_n:.6g} {i:.6g} {e:.6g}" for ppm, i, e in p]
            (gv / "data" / "cest_15N_850MHz" / f"{res}.txt").write_text("\n".join(lines) + "\n")
            residues.append(res)
        meta = {"variant": f"{v}_GDP", "note": "GDP-bound control sample, same buffer and temperature. Only 10 residues' 15N CEST "
                "profiles are available (normalised intensities; offsets converted from the deposited ppm axis). "
                "No CPMG data are available for GDP-bound samples.",
                "experiments": {"cest_15N_850MHz": {"kind": "cest_n", "b0_1H_MHz": 850.16, "saturation_time_s": 0.15,
                                                    "carrier_ppm": CARRIER, "b1_Hz": GDP_B1[v], "pulse_program_family": "cest_15n",
                                                    "residues": residues, "path": "data/cest_15N_850MHz/"}}}
        (gv / "experiments.json").write_text(json.dumps(meta, indent=1))
        audit["included"].append({"file": f"MOESM3 sheet 'FigS4 - {v}+GDP CEST' (EXP columns)", "as": f"{v}_GDP/data/cest_15N_850MHz ({len(residues)} residues)"})
        audit["included"].append({"file": f"NASR KRas_{v}_GDP.csv R1_free", "as": f"{v}_GDP/measured_R1.json"})
