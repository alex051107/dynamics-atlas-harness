"""Derive behavioural-check workspaces from a built workspace.

no_sign_evidence: remove CEST and HSQC/HMQC data (the only sources of dw signs).
renumbered:       add a constant to every residue number, with the mapping stated in TASK.md.
"""

from __future__ import annotations

import csv
import io
import json
import re
import shutil
from pathlib import Path


def no_sign_evidence(src: Path, dst: Path) -> None:
    shutil.copytree(src, dst)
    for vdir in [p for p in dst.iterdir() if (p / "experiments.json").exists()]:
        meta = json.loads((vdir / "experiments.json").read_text())
        for name in [k for k, e in meta["experiments"].items() if e["kind"] == "cest_n"]:
            shutil.rmtree(vdir / meta["experiments"][name]["path"])
            del meta["experiments"][name]
        (vdir / "experiments.json").write_text(json.dumps(meta, indent=1))
        for f in vdir.glob("hsqc_minus_hmqc_*.txt"):
            f.unlink()
    t = (dst / "TASK.md").read_text()
    t = t.replace(", 15N CEST at 850 MHz (150 ms saturation)", "")
    t = t.replace(", and HSQC-minus-HMQC 15N peak-position differences where available", "")
    (dst / "TASK.md").write_text(t)


def _shift_label(label: str, off: int) -> str:
    m = re.fullmatch(r"([A-Z])(\d+)([A-Z]*)", label)
    return f"{m.group(1)}{int(m.group(2)) + off}{m.group(3)}" if m else label


def renumbered(src: Path, dst: Path, off: int = 200) -> None:
    shutil.copytree(src, dst)
    for vdir in [p for p in dst.iterdir() if (p / "experiments.json").exists()]:
        meta = json.loads((vdir / "experiments.json").read_text())
        for e in meta["experiments"].values():
            d = vdir / e["path"]
            for f in sorted(d.glob("*.txt")):
                f.rename(d / f"_{_shift_label(f.stem, off)}.txt")
            for f in sorted(d.glob("_*.txt")):
                f.rename(d / f.name[1:])
            e["residues"] = [_shift_label(r, off) for r in e["residues"]]
        (vdir / "experiments.json").write_text(json.dumps(meta, indent=1))
        for name in ("ground_state_shifts.json", "measured_R1.json"):
            p = vdir / name
            if p.exists():
                p.write_text(json.dumps({_shift_label(k, off): v for k, v in json.loads(p.read_text()).items()}, indent=0))
        for f in vdir.glob("hsqc_minus_hmqc_*.txt"):
            lines = [ln if ln.startswith("#") or not ln.strip() else " ".join([_shift_label(ln.split()[0], off)] + ln.split()[1:])
                     for ln in f.read_text().splitlines()]
            f.write_text("\n".join(lines) + "\n")
    for f in (dst / "relaxation_15N_850MHz").glob("*.csv"):
        rows = list(csv.reader(io.StringIO(f.read_text())))
        for r in rows[1:]:
            if r and r[0].strip().lstrip("-").isdigit():
                r[0] = str(int(r[0]) + off)
        buf = io.StringIO()
        csv.writer(buf, lineterminator="\n").writerows(rows)
        f.write_text(buf.getvalue())
    t = (dst / "TASK.md").read_text()
    t = t.replace("## Data in this workspace",
                  f"## Residue numbering in this workspace\nEvery residue number in this workspace's files equals the native K-Ras number plus {off} "
                  f"(e.g. file residue G{12 + off} is native G12). Region definitions above and public databases use native numbering.\n\n## Data in this workspace")
    (dst / "TASK.md").write_text(t)


def synthetic_minor_equals_reference(src: Path, dst: Path, variant: str, ref_shifts: dict[str, dict[int, float]],
                                     kex: float = 380.0, pb: float = 0.10, seed: int = 7) -> dict:
    """Negative control: replace one variant's profiles with simulations whose minor state has exactly the
    reference-state shifts (dw = ref - ground for every residue with a reference value, else 0).

    ref_shifts: {"N": {resnum: ppm}, "H": {resnum: ppm}}. R2 per residue/experiment is taken from the real
    data (R2eff at the highest nu_CPMG; 15 s^-1 for CEST); noise equals the file errors.
    """
    import numpy as np
    from . import exchange as ex
    from .workspace import load_variant

    shutil.copytree(src, dst)
    v = load_variant(src, variant)
    shifts = json.loads((src / variant / "ground_state_shifts.json").read_text())
    rng = np.random.default_rng(seed)
    meta = json.loads((src / variant / "experiments.json").read_text())
    used = {}
    for ename, info in meta["experiments"].items():
        e = v["experiments"][ename]
        nuc = "H" if e.kind == "cpmg_h" else "N"
        for res, prof in e.profiles.items():
            n = prof.resnum
            g = shifts.get(f"{res}{nuc}")
            ref = ref_shifts.get(nuc, {}).get(n)
            dw = (ref - g) if (g is not None and ref is not None) else 0.0
            used[f"{res}{nuc}"] = round(dw, 3)
            x, err = prof.x, prof.error
            if e.kind.startswith("cpmg"):
                try:
                    nu, r2, _ = ex.cpmg_r2eff_from_intensity(prof, e.time)
                    r2int = float(np.clip(np.nanmin(r2[np.argsort(nu)[-3:]]), 1.0, 60.0))
                except ValueError:
                    continue
                i0 = float(prof.intensity[x == 0].mean())
                nuc_mhz = e.nucleus_mhz
                r2e = np.zeros_like(x, dtype=float)
                m = x > 0
                r2e[m] = ex.cpmg_r2eff_model(x[m] / e.time, e.time, kex, pb, dw, nuc_mhz, r2int)
                y = i0 * np.exp(-r2e * e.time)
                y[~m] = i0
            else:
                om = (v["cs_n"][res] - e.carrier_ppm) * e.nucleus_mhz if res in v["cs_n"] else 0.0
                mk = x > -1e5
                y = np.empty_like(x, dtype=float)
                r1v = v["r1"].get(res, 1.0)
                mod = ex.cest_model(x[mk], e.time, e.b1_hz, kex, pb, om, dw, e.nucleus_mhz, r1v, 15.0)
                scale = float(np.max(prof.intensity[mk])) / float(np.max(mod))
                y[mk] = scale * mod
                y[~mk] = scale  # far-off reference: no saturation, no delay
            y = y + rng.normal(0, err)
            col = "ncyc" if e.kind.startswith("cpmg") else "offset_hz_from_carrier"
            lines = [f"# {col} intensity error"] + [f"{a:.6g} {b:.6g} {c:.6g}" for a, b, c in zip(x, y, err)]
            (dst / variant / info["path"] / f"{res}.txt").write_text("\n".join(lines) + "\n")
    return {"variant": variant, "kex": kex, "pb": pb, "dw_used": used}
