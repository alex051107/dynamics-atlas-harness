"""Tools the NMR analysis agent can call. Every tool acts only on the sanitized workspace
(or on BMRB with citation text stripped). Analysis tools require `purpose` and
`expectation` arguments so each action records why it was chosen and what each outcome
would mean; the loop logs them next to the observed result.
"""

from __future__ import annotations

import json
import math
import re
import subprocess
import textwrap
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Callable

import numpy as np

from . import exchange as ex
from . import multistate as ms
from . import references as refs
from .workspace import load_variant

WHY = {
    "purpose": {"type": "string", "description": "Which open question this action addresses and which observation prompted it."},
    "expectation": {"type": "string", "description": "What result you expect, and how each plausible outcome would change your next step or conclusion."},
}


def _schema(props: dict[str, Any], required: list[str], why: bool = True) -> dict[str, Any]:
    p = dict(props)
    req = list(required)
    if why:
        p.update(WHY)
        req += ["purpose", "expectation"]
    return {"type": "object", "properties": p, "required": req}


def _r(x: float, n: int = 3) -> float | None:
    if x is None or (isinstance(x, float) and not math.isfinite(x)):
        return None
    return round(float(x), n)


class ToolBox:
    def __init__(self, workspace: Path, run_dir: Path, allow_network_bmrb: bool = True,
                 blocked_bmrb_ids: tuple[str, ...] = ()):
        self.ws = workspace.resolve()
        self.run_dir = run_dir.resolve()
        self.allow_bmrb = allow_network_bmrb
        self.blocked_bmrb = set(blocked_bmrb_ids)
        self._cache: dict[str, dict[str, Any]] = {}
        self.fits: dict[str, Any] = {}      # fit_id -> summary, restored after a tool-server restart
        issued = []
        for p in (self.run_dir / "fits").glob("F*.json"):
            if re.fullmatch(r"F\d+", p.stem):
                self.fits[p.stem] = json.loads(p.read_text())
                issued.append(int(p.stem[1:]))
        for p in (self.run_dir / "py").glob("P*.py"):
            if re.fullmatch(r"P\d+", p.stem):
                issued.append(int(p.stem[1:]))
        self._n = max(issued, default=0)

    # ------------------------------------------------------------------ helpers
    def _v(self, variant: str) -> dict[str, Any]:
        candidate = (self.ws / variant).resolve()
        if candidate.parent != self.ws or candidate.name != variant:
            raise PermissionError("variant must name a direct workspace child")
        if variant not in self._cache:
            if not (self.ws / variant / "experiments.json").exists():
                raise ValueError(f"unknown variant '{variant}'")
            self._cache[variant] = load_variant(self.ws, variant)
        return self._cache[variant]

    def _exps(self, variant: str, names: list[str] | None) -> list[ex.Experiment]:
        v = self._v(variant)["experiments"]
        if not names:
            return list(v.values())
        missing = [n for n in names if n not in v]
        if missing:
            raise ValueError(f"unknown experiment(s) {missing}; available: {list(v)}")
        return [v[n] for n in names]

    def _new_id(self, prefix: str) -> str:
        self._n += 1
        return f"{prefix}{self._n:03d}"

    # -------------------------------------------------------------------- tools
    def inventory(self) -> dict[str, Any]:
        out: dict[str, Any] = {"files": sorted(str(p.relative_to(self.ws)) for p in self.ws.iterdir())}
        for vdir in sorted(p for p in self.ws.iterdir() if (p / "experiments.json").exists()):
            meta = json.loads((vdir / "experiments.json").read_text())
            out[vdir.name] = {
                "experiments": {k: {kk: vv for kk, vv in e.items() if kk not in ("residues", "path")} | {"n_residues": len(e["residues"])}
                                for k, e in meta["experiments"].items()},
                "other_files": sorted(p.name for p in vdir.iterdir() if p.is_file() and p.name != "experiments.json"),
            }
        return out

    def read_text(self, path: str, max_chars: int = 4000, offset: int = 0) -> dict[str, Any]:
        p = (self.ws / path).resolve()
        if self.ws.resolve() not in p.parents and p != self.ws.resolve():
            raise PermissionError("path outside workspace")
        if p.is_dir():
            return {"dir": sorted(x.name for x in p.iterdir())[:300]}
        t = p.read_text()
        offset = max(0, int(offset))
        end = min(len(t), offset + min(max(1, int(max_chars)), 4000))
        return {"path": path, "chars": len(t), "text": t[offset:end],
                "next_offset": end if end < len(t) else None}

    def read_result(self, observation_id: str, offset: int = 0, **_: Any) -> dict[str, Any]:
        if not re.fullmatch(r"O\d{6}", observation_id):
            raise ValueError("observation_id must be an issued O000001-style id")
        p = self.run_dir / "observations" / (observation_id + ".json")
        t = p.read_text()
        offset = max(0, int(offset))
        end = min(len(t), offset + 3500)
        return {"source_observation": observation_id, "chars": len(t), "text": t[offset:end],
                "next_offset": end if end < len(t) else None}

    def compare_references(self, reference_ids: list[str], residues: list[str] | None = None, variant: str | None = None,
                           fit_id: str | None = None, dw_key: str = "dwN", pH: float | None = None,
                           temperature_K: float | None = None, ionic_strength_M: float | None = None,
                           regions: dict[str, list[str]] | None = None, **_: Any) -> dict[str, Any]:
        """v2.1: with `regions`, every reference is compared within every region (same residue intersection
        per region) in one call; per-residue detail is returned only for the pooled set."""
        if not residues and not regions:
            raise ValueError("provide residues or nonempty regions")
        if regions:
            pooled = list(dict.fromkeys([r for rs in regions.values() for r in rs] + list(residues or [])))
            out = {"regions": {}, "pooled": None}
            for name, rs in regions.items():
                try:
                    c = self.compare_references(reference_ids, rs, variant, fit_id, dw_key, pH, temperature_K, ionic_strength_M)
                    out["regions"][name] = {"common_residues": c["common_residues"], "missing": c["missing"],
                                            "references": {k: {kk: v[kk] for kk in ("n", "pearson_r", "r_squared", "rmsd_ppm", "mean_residual_ppm")}
                                                           for k, v in c["references"].items()}}
                except ValueError as e:
                    out["regions"][name] = {"error": str(e)}
            out["pooled"] = self.compare_references(reference_ids, pooled, variant, fit_id, dw_key, pH, temperature_K, ionic_strength_M)
            out["limit"] = out["pooled"].get("limit")
            return out
        """Compare minor-state shifts with several references on exactly the same residue intersection.

        With variant + fit_id: ground = <variant> ground-state 15N shifts, dw = that fit's per-residue dw
        (dw_key 'dwN', or 'dwN1'/'dwN2' for three-state fits), references from reference_shifts.
        Without them: falls back to a supplied analysis_input.json in the workspace.
        """
        from .reference_comparison import compare
        if variant and fit_id:
            self._v(variant)
            if fit_id not in self.fits:
                raise ValueError(f"unknown fit_id {fit_id}")
            fit = self.fits[fit_id]
            if fit.get("variant") != variant:
                raise ValueError("fit_id belongs to a different variant")
            ground = {k[:-1]: v for k, v in json.loads((self.ws / variant / "ground_state_shifts.json").read_text()).items() if k.endswith("N")}
            dw = {r: d[dw_key] for r, d in fit["per_residue"].items() if d.get(dw_key) is not None}
            refs_n = {}
            for rid in reference_ids:
                got = self.reference_shifts("get", rid, variant, ["N"], pH=pH, temperature_K=temperature_K, ionic_strength_M=ionic_strength_M)
                refs_n[rid] = {k[:-1]: v for k, v in got["shifts"].items()}
            out = compare(ground, dw, refs_n, residues)
            out["source"] = {"variant": variant, "fit_id": fit_id, "dw_key": dw_key}
            return out
        inp = json.loads((self.ws / "analysis_input.json").read_text())
        cat = json.loads((self.ws / "references.json").read_text())["references"]
        refs_n = {r["id"]: r["shifts"]["N"] for r in cat if r["id"] in reference_ids}
        return compare(inp["ground_ppm"], inp["dw_ppm"], refs_n, residues)

    def screen_dispersion(self, variant: str, experiment: str, **_: Any) -> dict[str, Any]:
        e = self._exps(variant, [experiment])[0]
        rows = []
        skipped = []
        if e.kind.startswith("cpmg"):
            for res, prof in e.profiles.items():
                try:
                    nu, r2, s = ex.cpmg_r2eff_from_intensity(prof, e.time)
                except ValueError as exc:
                    skipped.append({"res": res, "reason": str(exc)})
                    continue
                if len(nu) < 4:
                    skipped.append({"res": res, "reason": "fewer than four valid CPMG frequencies"})
                    continue
                lo, hi = np.argsort(nu)[:2], np.argsort(nu)[-2:]
                d = r2[lo].mean() - r2[hi].mean()
                sd = math.sqrt(np.sum(s[lo] ** 2) / 4 + np.sum(s[hi] ** 2) / 4)
                rows.append({"res": res, "dR2": _r(d, 2), "sd": _r(sd, 2), "z": _r(d / sd if sd > 0 else 0, 1),
                             "R2_high_nu": _r(r2[hi].mean(), 1)})
            rows.sort(key=lambda r: -(r["dR2"] or 0))
            note = "dR2 = mean R2eff at the two lowest nu_CPMG minus the two highest (s^-1)."
        else:
            v = self._v(variant)
            for res, prof in e.profiles.items():
                if res not in v["cs_n"]:
                    skipped.append({"res": res, "reason": "no ground-state 15N shift; not a negative result"})
                    continue
                om = (v["cs_n"][res] - e.carrier_ppm) * e.nucleus_mhz
                d = ex.cest_one_state_residual(prof, e.time, e.b1_hz, om, e.nucleus_mhz, v["r1"].get(res, 1.0))
                rows.append({"res": res, "residual_dip": _r(d["dip"], 3), "z": _r(d["z"], 1),
                             "n_residual_peak_candidates": d.get("n_dips"),
                             "dip_offset_ppm_from_major": _r(d["offset_ppm"], 2), "one_state_red_chi2": _r(d["chi2_red"], 2)})
            rows.sort(key=lambda r: -(r["z"] or 0))
            note = ("Each profile is fitted with a no-exchange single-state model; residual_dip is the deepest (3-point smoothed) "
                    "shortfall of the data below that model more than 0.35 ppm from the major dip, in units of the normalised intensity. "
                    "z and peak counts are uncalibrated screening heuristics after fitting, not p-values or counts of conformational states. "
                    "Residual peaks may reflect an inadequate null model, calibration error or noise; inspect raw curves and controls.")
        return {"experiment": experiment, "variant": variant, "n_profiles": len(e.profiles), "n": len(rows),
                "skipped": skipped, "note": note, "rows": rows}

    def show_profile(self, variant: str, experiment: str, residue: str, fit_id: str | None = None, **_: Any) -> dict[str, Any]:
        e = self._exps(variant, [experiment])[0]
        if residue not in e.profiles:
            raise ValueError(f"{residue} not in {experiment}")
        prof = e.profiles[residue]
        if e.kind.startswith("cpmg"):
            nu, r2, s = ex.cpmg_r2eff_from_intensity(prof, e.time)
            o = np.argsort(nu)
            return {"columns": ["nu_cpmg_Hz", "R2eff", "sd"], "rows": [[_r(nu[i], 0), _r(r2[i], 2), _r(s[i], 2)] for i in o]}
        v = self._v(variant)
        m = prof.x > -1e5
        base = np.max(prof.intensity[m])
        ppm = e.carrier_ppm + prof.x[m] / e.nucleus_mhz
        o = np.argsort(ppm)
        return {"ground_state_shift_ppm": v["cs_n"].get(residue), "columns": ["ppm", "I/Imax", "sd"],
                "rows": [[_r(ppm[i], 2), _r(prof.intensity[m][i] / base, 3), _r(prof.error[m][i] / base, 3)] for i in o]}

    def fit_exchange(self, variant: str, residues: list[str], experiments: list[str] | None = None,
                     mode: str = "global", kex0: float = 500.0, pb0: float = 0.05,
                     dw_init: dict[str, float] | None = None, fix: dict[str, float] | None = None,
                     model: str = "two_state", groups: dict[str, list[str]] | None = None,
                     kex2_0: float = 1500.0, pc0: float = 0.02, dw2_init: dict[str, float] | None = None,
                     **_: Any) -> dict[str, Any]:
        v = self._v(variant)
        exps = self._exps(variant, experiments)
        if mode not in ("global", "per_residue"):
            raise ValueError("mode must be global or per_residue")
        if model != "two_state" and (groups is not None or fix or mode != "global"):
            raise ValueError("three-state fits do not implement groups, fixed parameters or per-residue kinetics")
        t0 = time.time()
        if model == "two_state":
            f = ex.fit_two_state(exps, residues, cs_n=v["cs_n"], r1=v["r1"], kex0=kex0, pb0=pb0, dw0=dw_init,
                                 fix=fix, per_residue_exchange=(mode == "per_residue"), groups=groups)
        elif model in ("three_state_star", "three_state_linear"):
            f = ms.fit_three_state(exps, residues, model.split("_")[-1], cs_n=v["cs_n"], r1=v["r1"], kex1_0=kex0,
                                   p1_0=pb0, kex2_0=kex2_0, p2_0=pc0, dw1_0=dw_init, dw2_0=dw2_init)
        else:
            raise ValueError(f"unknown model {model}")
        fid = self._new_id("F")
        flags = []
        for name, val in f.params.items():
            if name.startswith(("kex", "pb", "p1", "p2")):
                err = f.errors.get(name, float("nan"))
                if name.startswith(("pb", "p1", "p2")) and (val < 2e-4 or val > 0.44):
                    flags.append(f"{name} at bound ({val:.4g})")
                if name.startswith("kex") and (val < 2 or val > 9e4):
                    flags.append(f"{name} at bound ({val:.4g})")
                if math.isfinite(err) and val > 0 and err / val > 0.3:
                    flags.append(f"{name} poorly determined (rel. error {err / val:.0%})")
        if f.reduced_chi2 > 2:
            flags.append(f"reduced chi2 {f.reduced_chi2:.2f} > 2: model or error estimates inadequate")
        if model.startswith("three_state"):
            pa = 1.0 - f.params["p1"] - f.params["p2"]
            if pa < max(f.params["p1"], f.params["p2"]):
                flags.append("observed state A is not the most populated fitted state; the major/minor assignment is unsupported")
        if not f.optimization.get("success", False):
            flags.append("optimizer did not confirm convergence; do not rank models by this AIC/BIC alone")
        worst = sorted(((r, d["chi2"] / max(d["n"], 1)) for r, d in f.per_residue.items()), key=lambda t: -t[1])[:5]
        per = {r: {k: _r(val, 3) for k, val in d.items() if k.startswith(("dwN", "dwH"))}
               | {"chi2_per_point": _r(d["chi2"] / max(d["n"], 1), 2)} for r, d in f.per_residue.items()}
        gkeys = [k for k in f.params if k.startswith(("kex", "pb", "p1", "p2"))]
        out = {"fit_id": fid, "variant": variant, "model": model, "mode": ("groups" if groups else mode),
               "groups": groups, "experiments": [e.name for e in exps],
               "global": {k: _r(f.params[k], 5) for k in gkeys},
               "global_err": {k: _r(f.errors.get(k, float("nan")), 5) for k in gkeys},
               "chi2": _r(f.chi2, 1), "n_data": f.n_data, "n_params": f.n_params, "reduced_chi2": _r(f.reduced_chi2, 3),
               "aic": _r(f.aic, 1), "bic": _r(f.bic, 1), "per_residue": per, "worst_residues_chi2_per_point": worst,
               "flags": flags, "notes": f.notes, "optimization": f.optimization, "seconds": _r(time.time() - t0, 1),
               "sign_note": "CPMG alone does not determine the sign of dw; only CEST (or HSQC/HMQC data) does."}
        self.fits[fid] = out
        (self.run_dir / "fits").mkdir(parents=True, exist_ok=True)
        (self.run_dir / "fits" / f"{fid}.json").write_text(json.dumps(out, indent=1))
        return out

    def cest_sign_scan(self, variant: str, residues: list[str], kex: float, pb: float,
                       dw_abs: dict[str, float] | None = None, **_: Any) -> dict[str, Any]:
        v = self._v(variant)
        cest = [e for e in v["experiments"].values() if e.kind == "cest_n"]
        if not cest:
            raise ValueError("no CEST experiment for this variant")
        res = ex.cest_sign_scan(cest[0], residues, dw_abs or {}, kex, pb, v["cs_n"], v["r1"])
        return {"experiment": cest[0].name, "fixed": {"kex": kex, "pb": pb},
                "rows": {r: {k: (_r(val, 3) if isinstance(val, float) else val) for k, val in d.items()} for r, d in res.items()},
                "note": "Each sign is separately constrained and fitted from multiple amplitudes including 20 ppm. determined=True requires finite fits on both sides, delta chi2 > 4 and no bound hit. This is conditional on fixed kex/pb, not unconditional confidence."}

    def bootstrap_global(self, variant: str, residues: list[str], experiments: list[str] | None = None,
                         n_boot: int = 20, kex0: float = 500.0, pb0: float = 0.05,
                         dw_init: dict[str, float] | None = None, **_: Any) -> dict[str, Any]:
        v = self._v(variant)
        exps = self._exps(variant, experiments)
        n_boot = int(min(max(n_boot, 5), 50))
        t0 = time.time()
        b = ex.bootstrap_global(exps, residues, n_boot=n_boot, cs_n=v["cs_n"], r1=v["r1"], kex0=kex0, pb0=pb0, dw0=dw_init)
        b.pop("base", None)
        return {k: (_r(val, 5) if isinstance(val, float) else val) for k, val in b.items()} | {
            "method": "resample residues with replacement, refit global model", "seconds": _r(time.time() - t0, 1)}

    def bmrb_search(self, term: str, **_: Any) -> dict[str, Any]:
        if not self.allow_bmrb:
            raise PermissionError("BMRB access disabled in this run")
        url = "https://api.bmrb.io/v2/instant?term=" + urllib.parse.quote(term)
        with urllib.request.urlopen(url, timeout=30) as r:
            hits = json.loads(r.read())
        out = []
        for h in hits[:25]:
            eid = str(h.get("value"))
            if eid in self.blocked_bmrb:
                continue
            out.append({"id": eid, "submitted": h.get("sub_date")})
        return {"term": term, "hits": out,
                "note": "Titles and citations are withheld; call bmrb_entry for the molecular system, conditions and shifts."}

    def bmrb_entry(self, entry_id: str, atoms: list[str] | None = None, **_: Any) -> dict[str, Any]:
        if not self.allow_bmrb:
            raise PermissionError("BMRB access disabled in this run")
        entry_id = str(entry_id).strip()
        if not re.fullmatch(r"[0-9]+", entry_id):
            raise ValueError("entry_id must be a numeric BMRB accession")
        entry_id = str(int(entry_id))
        if str(entry_id) in self.blocked_bmrb:
            raise PermissionError(f"BMRB {entry_id} is withheld in this run (its record identifies the target study)")
        atoms = atoms or ["N", "H"]
        with urllib.request.urlopen(f"https://api.bmrb.io/v2/entry/{entry_id}?format=json", timeout=60) as r:
            e = list(json.loads(r.read()).values())[0]
        entities, conds, samples, shifts = [], {}, [], {}
        for sf in e["saveframes"]:
            cat = sf["category"]
            if cat == "entity":
                d = {t[0]: t[1] for t in sf["tags"]}
                entities.append({"name": d.get("Name"), "type": d.get("Type"), "polymer_type": d.get("Polymer_type"),
                                 "sequence": (d.get("Polymer_seq_one_letter_code") or "").replace("\n", "")})
            elif cat == "sample_conditions":
                for lp in sf["loops"]:
                    tags = lp["tags"]
                    for row in lp["data"]:
                        rd = dict(zip(tags, row))
                        conds[rd.get("Type")] = f"{rd.get('Val')} {rd.get('Val_units', '')}".strip()
            elif cat == "sample":
                for lp in sf["loops"]:
                    tags = lp["tags"]
                    for row in lp["data"]:
                        rd = dict(zip(tags, row))
                        samples.append(f"{rd.get('Mol_common_name')} {rd.get('Concentration_val')} {rd.get('Concentration_val_units')}")
            elif cat == "assigned_chemical_shifts":
                for lp in sf["loops"]:
                    if lp["category"] != "_Atom_chem_shift":
                        continue
                    tags = lp["tags"]
                    ix = {t: i for i, t in enumerate(tags)}
                    for row in lp["data"]:
                        atom = row[ix["Atom_ID"]]
                        if atom not in atoms:
                            continue
                        seq = row[ix.get("Auth_seq_ID", ix["Seq_ID"])]
                        if seq in (".", "?"):
                            seq = row[ix["Seq_ID"]]
                        key = f"{row[ix['Comp_ID']]}{seq}"
                        shifts.setdefault(atom, {})[key] = float(row[ix["Val"]])
        return {"entry": entry_id, "entities": entities, "sample_conditions": conds, "sample_components": samples[:12],
                "shifts": shifts, "note": "Residue keys use three-letter code + author numbering. Citation text withheld."}

    def reference_shifts(self, action: str = "list", name: str | None = None, variant: str | None = None,
                         atoms: list[str] | None = None, pH: float | None = None, temperature_K: float | None = None,
                         ionic_strength_M: float | None = None, **_: Any) -> dict[str, Any]:
        """List or fetch reference chemical-shift sets (workspace sets or sequence-based predictors)."""
        atoms = atoms or ["N", "H"]
        cat_path = self.ws / "references.json"
        catalogue = json.loads(cat_path.read_text())["references"] if cat_path.is_file() else []
        if action == "list":
            return {"workspace_sets": refs.list_workspace_references(self.ws)
                    + [{k: v for k, v in r.items() if k != "shifts"} for r in catalogue],
                    "predictors": [{"name": "random_coil_potenci", "needs": "variant (uses <variant>/sequence.json); optional pH, temperature_K, ionic_strength_M",
                                    "description": "Sequence-based random-coil shift prediction (POTENCI, Nielsen & Mulder 2018)"}],
                    "note": "Public BMRB entries can be fetched with bmrb_search / bmrb_entry."}
        if not variant:
            raise ValueError("variant is required")
        self._v(variant)
        if action != "get":
            raise ValueError("action must be list or get")
        cat_hit = [r for r in catalogue if r.get("id") == name]
        if cat_hit:
            d = {"description": cat_hit[0].get("description"), "conditions": cat_hit[0].get("conditions"),
                 "shifts": {f"{k}{at}": v for at, m in cat_hit[0]["shifts"].items() for k, v in m.items()}}
        elif name == "random_coil_potenci":
            sq = json.loads((self.ws / variant / "sequence.json").read_text())
            d = refs.potenci_random_coil(sq["sequence"], sq["first_residue_number"], pH if pH is not None else 7.0,
                                         temperature_K if temperature_K is not None else 298.0,
                                         ionic_strength_M if ionic_strength_M is not None else 0.1, self.run_dir / "potenci")
        else:
            d = refs.get_workspace_reference(self.ws, variant, name or "")
        sh = {k: v for k, v in d["shifts"].items() if any(k.endswith(a) and k[:-len(a)][-1:].isdigit() for a in atoms)}
        return {"name": name, "variant": variant, "description": d.get("description"), "conditions": d.get("conditions"),
                "note": d.get("note"), "n": len(sh), "shifts": sh}

    def pdb_ligand_distances(self, pdb_id: str, ligand: str | None = None, ligand_atoms: list[str] | None = None,
                             atom: str = "N", chain: str | None = None, **_: Any) -> dict[str, Any]:
        return refs.pdb_ligand_distances(pdb_id, ligand, ligand_atoms, atom, chain, cache_dir=self.run_dir / "pdb")

    def python(self, code: str, **_: Any) -> dict[str, Any]:
        """Run Python in the workspace under a macOS sandbox: no network, no reads outside workspace."""
        scratch = self.run_dir / "py"
        scratch.mkdir(parents=True, exist_ok=True)
        fid = self._new_id("P")
        script = scratch / f"{fid}.py"
        script.write_text(code)
        ws = str(self.ws.resolve())
        sc = str(scratch.resolve())
        home = str(Path.home())
        profile = textwrap.dedent(f"""
            (version 1)(allow default)(deny network*)
            (deny file-read* (subpath "/Users") (subpath "/Volumes")
                (subpath "/private/tmp") (subpath "/private/var/folders"))
            (allow file-read* (subpath "{ws}"))(allow file-read* (subpath "{sc}"))
            (deny file-write*)
            (allow file-write* (subpath "{sc}") (literal "/dev/null"))
        """)
        env = {"PATH": "/usr/bin:/bin", "PYTHONPATH": str(self.ws / "lib"), "HOME": sc, "MPLBACKEND": "Agg",
               "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "2"}
        try:
            p = subprocess.run(["/usr/bin/sandbox-exec", "-p", profile, "/opt/anaconda3/bin/python3", str(script)],
                               cwd=ws, capture_output=True, text=True, timeout=240, env=env)
            out, err, rc = p.stdout, p.stderr, p.returncode
        except subprocess.TimeoutExpired:
            out, err, rc = "", "timeout after 240 s", -1
        return {"id": fid, "returncode": rc, "stdout": out, "stderr": err,
                "note": "cwd = workspace (read-only); write files to the directory in os.environ['HOME']."}


# ---------------------------------------------------------------- tool specs

def tool_specs() -> list[dict[str, Any]]:
    from .atlas_candidate import REQUIRED_TEXT
    S = _schema
    res_list = {"type": "array", "items": {"type": "string"}, "description": "Residue labels like 'V29'."}
    specs = [
        ("inventory", "List variants, experiments (kind, field, delays, B1, residue counts) and other files in the workspace.", S({}, [], why=False)),
        ("read_text", "Read a workspace text file in pages; use next_offset to continue.", S({"path": {"type": "string"}, "max_chars": {"type": "integer"}, "offset": {"type": "integer"}}, ["path"], why=False)),
        ("read_result", "Retrieve a full earlier tool observation by its issued id, in pages. Results remain available after truncation.", S({"observation_id": {"type": "string"}, "offset": {"type": "integer"}}, ["observation_id"], why=False)),
        ("get_research_state", "Retrieve the current model-authored research notes, including withdrawals. These notes are not new tool evidence.", S({}, [], why=False)),
        ("compare_references", "Compare minor-state 15N shifts (ground + signed dw from one of your fits) with several reference sets on exactly the same residue intersection. Returns signed r, r-squared, RMSD to identity and per-residue residuals; no structural verdict. Give variant, fit_id and reference names from reference_shifts; residues explicitly, or regions to get every reference per region in one call.", S({"reference_ids": {"type": "array", "items": {"type": "string"}}, "residues": res_list, "regions": {"type": "object", "description": "Optional {region name: [residues]}: every reference is compared within every region in one call, plus a pooled comparison."}, "variant": {"type": "string"}, "fit_id": {"type": "string"}, "dw_key": {"type": "string", "description": "dwN (two-state) or dwN1/dwN2 (three-state)."}, "pH": {"type": "number"}, "temperature_K": {"type": "number"}, "ionic_strength_M": {"type": "number"}}, ["reference_ids"])),
        ("screen_dispersion", "Per-residue screen of one experiment: CPMG -> dR2 (low minus high nu_CPMG) with z-score; CEST -> depth and offset of the strongest dip away from the major-state dip.",
         S({"variant": {"type": "string"}, "experiment": {"type": "string"}}, ["variant", "experiment"])),
        ("show_profile", "Return the numeric profile of one residue (CPMG: nu_CPMG vs R2eff; CEST: ppm vs normalised intensity).",
         S({"variant": {"type": "string"}, "experiment": {"type": "string"}, "residue": {"type": "string"}}, ["variant", "experiment", "residue"])),
        ("fit_exchange", "Fit an exchange model (numerical Bloch-McConnell) to chosen residues and experiments. Two-state: mode='global' shares kex and pb; mode='per_residue' fits them per residue; groups= fits independent processes for residue groups. Three-state models are also available. Returns rates, populations, per-residue dw (ppm, minor minus major), chi2, AIC/BIC and flags. Compare models only on the same residues and experiments.",
         S({"variant": {"type": "string"}, "residues": res_list, "experiments": {"type": "array", "items": {"type": "string"}, "description": "Default: all experiments of the variant."},
            "mode": {"type": "string", "enum": ["global", "per_residue"]}, "kex0": {"type": "number"}, "pb0": {"type": "number"},
            "dw_init": {"type": "object", "description": "Optional starting dw (ppm) per residue; signs matter for CEST."},
            "fix": {"type": "object", "description": "Optional fixed values, keys 'kex' and/or 'pb' (two-state only)."},
            "model": {"type": "string", "enum": ["two_state", "three_state_star", "three_state_linear"],
                      "description": "two_state: A<->B. three_state_star: B<->A<->C (two minor states each exchanging with the major). three_state_linear: A<->B<->C. Three-state fits are global (shared rates) and slower (~10-60 s)."},
            "groups": {"type": "object", "description": "two_state only: {group name: [residues]}; each group gets its own kex and pb (independent processes), fitted jointly so chi2/AIC/BIC compare directly with the single global process."},
            "kex2_0": {"type": "number", "description": "three-state: starting kex of the second exchange (s^-1)."},
            "pc0": {"type": "number", "description": "three-state: starting population of state C."},
            "dw2_init": {"type": "object", "description": "three-state: starting dw (ppm) to state C per residue."}}, ["variant", "residues"])),
        ("cest_sign_scan", "For each residue, refit its CEST profile (kex/pb fixed) from several starting |dw| of both signs and report the best dw and whether the sign is determined.",
         S({"variant": {"type": "string"}, "residues": res_list, "kex": {"type": "number"}, "pb": {"type": "number"},
            "dw_abs": {"type": "object", "description": "Starting |dw| (ppm) per residue, e.g. from a CPMG fit."}}, ["variant", "residues", "kex", "pb"])),
        ("bootstrap_global", "Residue-resampling bootstrap of the global kex and pb (5-50 replicates, each a full refit, run in parallel; typically a few seconds to a minute in total).",
         S({"variant": {"type": "string"}, "residues": res_list, "experiments": {"type": "array", "items": {"type": "string"}},
            "n_boot": {"type": "integer"}, "kex0": {"type": "number"}, "pb0": {"type": "number"}, "dw_init": {"type": "object"}}, ["variant", "residues"])),
        ("bmrb_search", "Search BMRB by free text; returns entry IDs only.", S({"term": {"type": "string"}}, ["term"])),
        ("bmrb_entry", "Get one BMRB entry's molecular system, sample conditions and assigned shifts for chosen atoms (default N, H).",
         S({"entry_id": {"type": "string"}, "atoms": {"type": "array", "items": {"type": "string"}}}, ["entry_id"])),
        ("python", "Run a Python script (numpy, scipy, pandas available; workspace is read-only cwd; fitting library imports as `exchange`). Full output is retained under its observation_id and can be paged with read_result if the response is clipped.",
         S({"code": {"type": "string"}}, ["code"])),
        ("update_research_state", "Record durable research state: facts about the sample, hypotheses with evidence for/against, open questions, current plan. Only what you write here survives context trimming.",
         S({"facts": {"type": "array", "items": {"type": "string"}},
            "hypotheses": {"type": "array", "items": {"type": "object", "properties": {"id": {"type": "string"}, "statement": {"type": "string"},
                                                                                     "status": {"type": "string", "enum": ["open", "supported", "weakened", "rejected"]},
                                                                                     "for": {"type": "array", "items": {"type": "string"}}, "against": {"type": "array", "items": {"type": "string"}}}}},
            "open_questions": {"type": "array", "items": {"type": "string"}}, "plan": {"type": "array", "items": {"type": "string"}},
            "retracted": {"type": "array", "items": {"type": "string"}, "description": "Earlier statements you now withdraw, with the reason."}}, [], why=False)),
        ("propose_experiment", "Record a new measurement you would recommend (not executed).",
         S({"description": {"type": "string"}, "question_it_resolves": {"type": "string"}}, ["description", "question_it_resolves"], why=False)),
        ("reference_shifts", "List available reference chemical-shift sets and predictors (action='list'), or fetch one (action='get', name, variant, atoms).",
         S({"action": {"type": "string", "enum": ["list", "get"]}, "name": {"type": "string"}, "variant": {"type": "string"},
            "atoms": {"type": "array", "items": {"type": "string"}}, "pH": {"type": "number"}, "temperature_K": {"type": "number"},
            "ionic_strength_M": {"type": "number"}}, ["action"])),
        ("pdb_ligand_distances", "From a PDB entry (RCSB, coordinates only), list ligands, or compute each residue's backbone-atom distance to the nearest atom of a chosen ligand (optionally specific ligand atoms).",
         S({"pdb_id": {"type": "string"}, "ligand": {"type": "string"}, "ligand_atoms": {"type": "array", "items": {"type": "string"}},
            "atom": {"type": "string"}, "chain": {"type": "string"}}, ["pdb_id"])),
        ("finish", "End the analysis. Submit (1) the report (markdown): direct answers, numbers with uncertainties, the evidence behind each conclusion (cite fit ids / tool results), unresolved alternatives, claim limits, and which statements rest on outside knowledge rather than these data; and (2) atlas_entries: one structured record per conformational state pair you would enter in a state database.",
         S({"report": {"type": "string"},
            "atlas_entries": {"type": "array", "items": {"type": "object", "required": list(REQUIRED_TEXT) + ["source_observations"], "properties": {
                "source_observations": {"type": "array", "items": {"type": "string"}, "description": "Issued O000001-style observation ids supporting this candidate. Empty fields do not count as evidence."},
                "protein": {"type": "string"}, "construct_and_variant": {"type": "string"}, "conditions": {"type": "string"},
                "bound_ligands": {"type": "string", "description": "What is bound in both states (e.g. nucleotide, metal)."},
                "major_state": {"type": "string"}, "alternative_state": {"type": "string"},
                "kinetic_model": {"type": "string", "description": "Number of states/processes and why."},
                "exchange_parameters": {"type": "string", "description": "Rates and populations with uncertainties, fit ids."},
                "residues_and_regions": {"type": "string"},
                "structural_identity_evidence": {"type": "string", "description": "What the alternative state resembles, by region, with the comparison statistics; say whether local shift similarity, candidate correspondence or constrained structure."},
                "controls_and_artefact_checks": {"type": "string"},
                "functional_relevance": {"type": "string", "description": "Only what these data support; label outside knowledge."},
                "cannot_be_supported": {"type": "string"},
                "evidence_type": {"type": "string"},
                "proposed_tier": {"type": "string", "enum": ["strong", "weak", "candidate", "not_included"], "description": "A proposal; people decide the tier."},
                "provenance": {"type": "string"}}}}}, ["report", "atlas_entries"], why=False)),
    ]
    return [{"type": "function", "function": {"name": n, "description": d, "parameters": p}} for n, d, p in specs]


ANALYSIS_TOOLS = {"screen_dispersion", "show_profile", "fit_exchange", "cest_sign_scan", "bootstrap_global",
                  "bmrb_search", "bmrb_entry", "python", "reference_shifts", "pdb_ligand_distances", "compare_references"}
