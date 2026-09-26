"""Build a sanitized analysis workspace from a ChemEx-format deposit, and load it back.

The solver only ever sees this workspace. Measured inputs (profiles, experiment
settings, ground-state shifts, measured R1, HSQC/HMQC shift differences, relaxation
tables) are copied; fitted outputs from the depositors (global kex/pb, per-residue
dw, fitted R2, residue classification comments) are dropped. Every inclusion and
exclusion is written to LEAK_AUDIT.json so the audit can be checked afterwards.
"""

from __future__ import annotations

import json
import re
import shutil
import tomllib
from pathlib import Path
from typing import Any

from .exchange import Experiment, Profile, classify, profile_files, read_profile, residue_label

EXCLUDED_PARAMETER_HINTS = ("global", "dw", "indiv", "r2", "signed")


def _parse_value_table(path: Path) -> dict[str, float]:
    out: dict[str, float] = {}
    for line in path.read_text().splitlines():
        m = re.match(r"\s*([A-Z]\d+[A-Z]*)\s*=\s*([-+\d.eE]+)", line)
        if m:
            name = m.group(1)
            res, _ = residue_label(name)
            nuc = "H" if name.endswith("H") else "N"
            out[f"{res}{nuc}"] = float(m.group(2))
    return out


def build_workspace(deposit_dir: Path, nasr_dir: Path | None, out_dir: Path, task_text: str,
                    variant_map: dict[str, str]) -> dict[str, Any]:
    """variant_map: deposit folder name -> label shown to the solver (e.g. 'WT+GTP' -> 'WT')."""
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    audit: dict[str, Any] = {"included": [], "excluded": [], "transformations": []}
    for folder, label in variant_map.items():
        src = deposit_dir / folder
        vdir = out_dir / label
        (vdir / "data").mkdir(parents=True)
        meta: dict[str, Any] = {"variant": label, "experiments": {}}
        for toml_path in sorted((src / "experiments").glob("*.toml")):
            cfg = tomllib.loads(toml_path.read_text())
            exp = cfg.get("experiment", {})
            kind = classify(exp.get("name", ""))
            if kind is None:
                audit["excluded"].append({"file": str(toml_path.relative_to(deposit_dir)),
                                          "reason": "shift-difference config; data copied separately"})
                continue
            data_dir = (toml_path.parent / cfg["data"]["path"]).resolve()
            b0 = float(cfg["conditions"]["h_larmor_frq"])
            ename = {"cpmg_n": "cpmg_15N", "cpmg_h": "cpmg_1HN", "cest_n": "cest_15N"}[kind] + f"_{round(b0)}MHz"
            edir = vdir / "data" / ename
            edir.mkdir()
            residues = []
            for fname in profile_files(cfg["data"]):
                p = data_dir / fname
                if not p.exists():
                    continue
                res, _ = residue_label(fname)
                x, y, e = read_profile(p)
                col = "ncyc" if kind.startswith("cpmg") else "offset_hz_from_carrier"
                lines = [f"# {col} intensity error"] + [f"{a:.6g} {b:.6g} {c:.6g}" for a, b, c in zip(x, y, e)]
                (edir / f"{res}.txt").write_text("\n".join(lines) + "\n")
                residues.append(res)
            residues.sort(key=lambda r: residue_label(r)[1])
            info = {"kind": kind, "b0_1H_MHz": b0,
                    "relaxation_delay_s" if kind.startswith("cpmg") else "saturation_time_s":
                        exp.get("time_t2") if kind.startswith("cpmg") else exp.get("time_t1"),
                    "carrier_ppm": exp.get("carrier"), "b1_Hz": exp.get("b1_frq"), "pw90_s": exp.get("pw90"),
                    "pulse_program_family": exp.get("name"), "residues": residues, "path": f"data/{ename}/"}
            meta["experiments"][ename] = {k: v for k, v in info.items() if v is not None}
            audit["included"].append({"file": str(toml_path.relative_to(deposit_dir)), "as": f"{label}/{ename}",
                                      "note": "settings + profiles only; profile-list comments (depositor exchange classification) dropped"})
        # measured tables
        tables: dict[str, dict[str, float]] = {}
        for p in sorted((src / "parameters").glob("*.toml"), key=lambda q: (q.stem.lower().startswith("cest"), q.name)):
            stem = p.stem.lower()
            if stem.startswith("cs"):
                tables.setdefault("ground_state_shifts_ppm", {}).update(_parse_value_table(p))
                audit["included"].append({"file": str(p.relative_to(deposit_dir)), "as": f"{label}/ground_state_shifts.json"})
            elif stem.startswith(("r1", "n15_r1", "cest_r1")):
                if "measured_R1_s-1" not in tables:
                    tables["measured_R1_s-1"] = {k: v for k, v in _parse_value_table(p).items() if k.endswith("N")}
                    audit["included"].append({"file": str(p.relative_to(deposit_dir)), "as": f"{label}/measured_R1.json"})
                else:
                    audit["excluded"].append({"file": str(p.relative_to(deposit_dir)), "reason": "duplicate R1 table"})
            else:
                audit["excluded"].append({"file": str(p.relative_to(deposit_dir)),
                                          "reason": "depositor fitted/initial exchange parameters (answer-bearing)"})
        if "ground_state_shifts_ppm" in tables:
            (vdir / "ground_state_shifts.json").write_text(json.dumps(tables["ground_state_shifts_ppm"], indent=0))
        if "measured_R1_s-1" in tables:
            (vdir / "measured_R1.json").write_text(json.dumps(tables["measured_R1_s-1"], indent=0))
        sq = src / "data" / "hsqc_hmqc"
        for f in sorted(sq.glob("sqmq_*.txt")) if sq.exists() else []:
            rows = ["# residue  delta(HSQC-HMQC)_ppb  error_ppb   (15N peak position difference; its sign relates to the sign of dw_N)"]
            for line in f.read_text().splitlines():
                s = line.split("#")[0].split()
                if len(s) >= 3:
                    res, _ = residue_label(s[0])
                    rows.append(f"{res} {s[1]} {s[2]}")
            mhz = re.findall(r"\d+", f.stem)[0]
            (vdir / f"hsqc_minus_hmqc_{mhz}MHz.txt").write_text("\n".join(rows) + "\n")
            audit["included"].append({"file": str(f.relative_to(deposit_dir)), "as": f"{label}/hsqc_minus_hmqc_{mhz}MHz.txt"})
        for f in sorted(sq.glob("*.inp")) if sq.exists() else []:
            audit["excluded"].append({"file": str(f.relative_to(deposit_dir)), "reason": "raw peak-picking duplicate"})
        (vdir / "experiments.json").write_text(json.dumps(meta, indent=1))
    if nasr_dir is not None:
        ndir = out_dir / "relaxation_15N_850MHz"
        ndir.mkdir()
        for f in sorted(nasr_dir.glob("*.csv")):
            name = f.name.replace("KRas_", "").replace(".csv", "")
            shutil.copy(f, ndir / f"{name}.csv")
            audit["included"].append({"file": f.name, "as": f"relaxation_15N_850MHz/{name}.csv",
                                      "note": "measured R1/R2 with and without nanoparticles and derived order parameters"})
    (out_dir / "TASK.md").write_text(task_text)
    expected = set(variant_map.values()) | {"TASK.md"} | ({"relaxation_15N_850MHz"} if nasr_dir is not None else set())
    extra = sorted(p.name for p in out_dir.iterdir()) and sorted(set(p.name for p in out_dir.iterdir()) - expected)
    if extra:
        raise RuntimeError(f"unexpected entries in workspace (sync conflict copies?): {extra}")
    (out_dir.parent / f"{out_dir.name}_LEAK_AUDIT.json").write_text(json.dumps(audit, indent=1))
    return audit


def load_variant(ws: Path, variant: str) -> dict[str, Any]:
    vdir = ws / variant
    meta = json.loads((vdir / "experiments.json").read_text())
    exps: dict[str, Experiment] = {}
    for ename, info in meta["experiments"].items():
        t = info.get("relaxation_delay_s", info.get("saturation_time_s"))
        e = Experiment(ename, info["kind"], info["b0_1H_MHz"], float(t), info.get("carrier_ppm"), info.get("b1_Hz"))
        for res in info["residues"]:
            x, y, err = read_profile(vdir / info["path"] / f"{res}.txt")
            e.profiles[res] = Profile(res, residue_label(res)[1], x, y, err)
        exps[ename] = e
    shifts = json.loads((vdir / "ground_state_shifts.json").read_text()) if (vdir / "ground_state_shifts.json").exists() else {}
    r1 = json.loads((vdir / "measured_R1.json").read_text()) if (vdir / "measured_R1.json").exists() else {}
    cs_n = {k[:-1]: v for k, v in shifts.items() if k.endswith("N")}
    return {"experiments": exps, "cs_n": cs_n, "r1": {k[:-1]: v for k, v in r1.items()}}
