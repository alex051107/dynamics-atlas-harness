"""Two-state chemical-exchange models and fits for CPMG and CEST NMR data.

Pure numpy/scipy. The models are numerical Bloch-McConnell propagations:

* CPMG (15N in-phase or 1HN): transverse magnetization of states A (major, observed)
  and B (minor), echo blocks tau-180-2tau-180-tau with ideal instantaneous pulses,
  tau = T / (4 ncyc), so nu_CPMG = ncyc / T. R2eff = -ln(I(ncyc) / I(0)) / T.
* CEST (15N): 6x6 Bloch-McConnell (x, y, z for A and B) under a continuous B1 field
  of strength b1 (Hz) at each offset, starting from +z; recovery toward equilibrium
  is suppressed (phase-cycled sequence), so intensity = scale * Mz_A(T).

Conventions follow ChemEx: kex = kab + kba, pb = minor population, kab = kex * pb
(A->B), kba = kex * pa. Chemical-shift differences dw are in ppm (B minus A).

Known simplifications (stated so results are not over-read): finite pulse widths,
scalar couplings, cross-correlated relaxation and B1 inhomogeneity are ignored; R2 of
the minor state is set equal to R2 of the major state.
"""

from __future__ import annotations

import math
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from scipy.sparse import lil_matrix

GAMMA_RATIO_N = 0.101329118  # |gamma_15N / gamma_1H|


# --------------------------------------------------------------------------- data


@dataclass
class Profile:
    residue: str            # e.g. "V29"
    resnum: int
    x: np.ndarray           # ncyc (CPMG) or offset in Hz from carrier (CEST)
    intensity: np.ndarray
    error: np.ndarray


@dataclass
class Experiment:
    name: str               # identifier, e.g. "n15_cpmg_850"
    kind: str               # "cpmg_n", "cpmg_h", "cest_n"
    b0_mhz: float           # 1H Larmor frequency
    time: float             # time_t2 (CPMG) or time_t1 (CEST), seconds
    carrier_ppm: float | None = None
    b1_hz: float | None = None
    profiles: dict[str, Profile] = field(default_factory=dict)

    @property
    def nucleus_mhz(self) -> float:
        return self.b0_mhz * (GAMMA_RATIO_N if self.kind.endswith("_n") else 1.0)


THREE_TO_ONE = {"ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q", "GLU": "E", "GLY": "G",
                "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P", "SER": "S",
                "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V"}


def residue_label(name: str) -> tuple[str, int]:
    """'S017N' / 'S017N-HN.out' / 'S17H' -> ('S17', 17)."""
    core = name.split("-")[0].split(".")[0]
    if len(core) > 3 and core[:3].upper() in THREE_TO_ONE and core[3].isdigit():
        aa, rest = THREE_TO_ONE[core[:3].upper()], core[3:]
    else:
        aa, rest = core[0], core[1:]
    digits = "".join(ch for ch in rest if ch.isdigit())
    num = int(digits)
    return f"{aa}{num}", num


def read_profile(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    rows = []
    for line in path.read_text().splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        parts = s.split()
        rows.append([float(parts[0]), float(parts[1]), float(parts[2])])
    arr = np.array(rows, dtype=float)
    return arr[:, 0], arr[:, 1], arr[:, 2]


def classify(name: str) -> str | None:
    if name.startswith("cest_15n"):
        return "cest_n"
    if name.startswith("cpmg_15n"):
        return "cpmg_n"
    if name.startswith("cpmg_1hn"):
        return "cpmg_h"
    return None


def load_experiment(toml_path: Path, label: str | None = None) -> Experiment | None:
    cfg = tomllib.loads(toml_path.read_text())
    exp = cfg.get("experiment", {})
    kind = classify(exp.get("name", ""))
    if kind is None:
        return None
    cond = cfg.get("conditions", {})
    data = cfg.get("data", {})
    data_dir = (toml_path.parent / data.get("path", "./")).resolve()
    time = exp.get("time_t1") if kind == "cest_n" else exp.get("time_t2")
    e = Experiment(name=label or toml_path.stem, kind=kind, b0_mhz=float(cond["h_larmor_frq"]),
                   time=float(time), carrier_ppm=exp.get("carrier"), b1_hz=exp.get("b1_frq"))
    for fname in profile_files(data):
        p = data_dir / fname
        if not p.exists():
            continue
        res, num = residue_label(fname)
        x, y, err = read_profile(p)
        e.profiles[res] = Profile(res, num, x, y, err)
    return e


def profile_files(data: dict[str, Any]) -> list[str]:
    """ChemEx lists profiles either as [[spin, file], ...] or as a {spin: file} table."""
    prof = data.get("profiles", [])
    if isinstance(prof, dict):
        return [str(v) for v in prof.values()]
    return [str(e[1]) for e in prof]


def cest_one_state_residual(prof: Profile, T: float, b1_hz: float, omega_a_hz: float, nucleus_mhz: float,
                            r1: float, exclude_ppm: float = 0.35) -> dict[str, float]:
    """Fit a no-exchange (single-state) CEST model and report the deepest residual dip away from the major dip."""
    m = prof.x > -1e5
    x, y, s = prof.x[m], prof.intensity[m], prof.error[m]
    norm = np.max(y)
    y, s = y / norm, s / norm

    def resid(p):
        return (y - p[1] * cest_model(x, T, b1_hz, 0.0, 0.0, omega_a_hz, 0.0, nucleus_mhz, r1, p[0])) / s

    sol = least_squares(resid, [10.0, 1.0], bounds=([0.1, 0.1], [300.0, 10.0]))
    r = -sol.fun * s  # model minus data, positive where data dip below the one-state model
    far = np.abs(x - omega_a_hz) > exclude_ppm * nucleus_mhz
    if far.sum() < 3:
        return {"dip": 0.0, "z": 0.0, "offset_ppm": float("nan"), "chi2_red": float("nan")}
    # smooth over 3 neighbouring offsets to suppress single-point noise
    order = np.argsort(x)
    rs = np.convolve(r[order], np.ones(3) / 3, mode="same")
    fs = far[order]
    k = int(np.argmax(np.where(fs, rs, -np.inf)))
    noise = float(np.median(s)) / math.sqrt(3)
    # count separate residual dips (local maxima with z > 5, at least 0.6 ppm apart)
    xs = x[order]
    peaks = [i for i in range(1, len(rs) - 1) if fs[i] and rs[i] >= rs[i - 1] and rs[i] >= rs[i + 1]
             and noise > 0 and rs[i] / noise > 5]
    peaks.sort(key=lambda i: -rs[i])
    kept = []
    for i in peaks:
        if all(abs(xs[i] - xs[j]) / nucleus_mhz > 0.6 for j in kept):
            kept.append(i)
    return {"dip": float(rs[k]), "z": float(rs[k] / noise) if noise > 0 else 0.0, "n_dips": len(kept),
            "offset_ppm": float((x[order][k] - omega_a_hz) / nucleus_mhz),
            "chi2_red": float(np.sum(sol.fun ** 2) / max(len(y) - 2, 1))}


def read_shift_table(path: Path) -> dict[str, float]:
    """Parse a ChemEx-style `[section]\\n NAME = value` table into {residue: value}."""
    out: dict[str, float] = {}
    cfg = tomllib.loads(path.read_text())
    for section in cfg.values():
        if not isinstance(section, dict):
            continue
        for k, v in section.items():
            try:
                res, _ = residue_label(k)
            except (ValueError, IndexError):
                continue
            if isinstance(v, (int, float)):
                out[res] = float(v)
    return out


# --------------------------------------------------------------------- CPMG model


def cpmg_r2eff_from_intensity(prof: Profile, T: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return (nu_cpmg, R2eff, sigma) using the mean of ncyc=0 points as reference."""
    ref_mask = prof.x == 0
    if not ref_mask.any():
        raise ValueError(f"{prof.residue}: no ncyc=0 reference point")
    i0 = prof.intensity[ref_mask].mean()
    if i0 <= 0:
        raise ValueError(f"{prof.residue}: non-positive reference intensity")
    s0 = math.sqrt(np.sum(prof.error[ref_mask] ** 2)) / ref_mask.sum()
    m = ~ref_mask & (prof.intensity > 0)
    ncyc = prof.x[m]
    inten = prof.intensity[m]
    r2 = -np.log(inten / i0) / T
    sig = np.sqrt((prof.error[m] / inten) ** 2 + (s0 / i0) ** 2) / T
    return ncyc / T, r2, sig


def cpmg_r2eff_model(nu_cpmg: np.ndarray, T: float, kex: float, pb: float, dw_ppm: float,
                     nucleus_mhz: float, r2: float) -> np.ndarray:
    pa = 1.0 - pb
    kab, kba = kex * pb, kex * pa
    dw = 2 * math.pi * dw_ppm * nucleus_mhz  # rad/s
    L = np.array([[-r2 - kab, kba], [kab, -r2 - 1j * dw - kba]], dtype=complex)
    ncyc = np.rint(nu_cpmg * T).astype(int)
    tau = T / (4.0 * np.maximum(ncyc, 1))
    # E(t) = V diag(exp(lam t)) V^-1, batched over tau
    lam, V = np.linalg.eig(L)
    Vi = np.linalg.inv(V)

    def E(t: np.ndarray) -> np.ndarray:
        d = np.exp(lam[None, :] * t[:, None])
        return np.einsum("ij,nj,jk->nik", V, d, Vi)

    E1 = E(tau)
    E2 = E(2 * tau)
    U = E1 @ np.conj(E2) @ E1
    mu, W = np.linalg.eig(U)
    Wi = np.linalg.inv(W)
    Un = np.einsum("nij,nj,njk->nik", W, mu ** ncyc[:, None], Wi)
    m0 = np.array([pa, pb], dtype=complex)
    ma = (Un @ m0)[:, 0]
    ratio = np.clip(ma.real / pa, 1e-12, None)
    return -np.log(ratio) / T


# --------------------------------------------------------------------- CEST model


def cest_model(offsets_hz: np.ndarray, T: float, b1_hz: float, kex: float, pb: float,
               omega_a_hz: float, dw_ppm: float, nucleus_mhz: float, r1: float, r2: float,
               r2b: float | None = None) -> np.ndarray:
    """Mz_A(T)/pa for each rf offset (Hz from carrier). omega_a_hz is state-A offset from carrier."""
    pa = 1.0 - pb
    kab, kba = kex * pb, kex * pa
    r2b = r2 if r2b is None else r2b
    w1 = 2 * math.pi * b1_hz
    n = len(offsets_hz)
    oa = 2 * math.pi * (omega_a_hz - offsets_hz)
    ob = oa + 2 * math.pi * dw_ppm * nucleus_mhz
    L = np.zeros((n, 6, 6))
    for base, om, R2, kout in ((0, oa, r2, kab), (3, ob, r2b, kba)):
        L[:, base + 0, base + 0] = -R2 - kout
        L[:, base + 0, base + 1] = -om
        L[:, base + 1, base + 0] = om
        L[:, base + 1, base + 1] = -R2 - kout
        L[:, base + 1, base + 2] = -w1
        L[:, base + 2, base + 1] = w1
        L[:, base + 2, base + 2] = -r1 - kout
    for i in range(3):
        L[:, 3 + i, i] = kab
        L[:, i, 3 + i] = kba
    m0 = np.zeros(6)
    m0[2], m0[5] = pa, pb
    try:
        lam, V = np.linalg.eig(L)
        c = np.linalg.solve(V, np.broadcast_to(m0.astype(complex), (n, 6))[..., None])[..., 0]
        mt = np.einsum("nij,nj->ni", V, np.exp(lam * T) * c)
        out = mt[:, 2].real / pa
        if np.all(np.isfinite(out)):
            return out
    except np.linalg.LinAlgError:
        pass
    P = expm(L * T)  # fallback for defective matrices
    return (P @ m0)[:, 2] / pa


# ------------------------------------------------------------------- fitting core


@dataclass
class FitResult:
    params: dict[str, float]
    errors: dict[str, float]
    chi2: float
    n_data: int
    n_params: int
    residues: list[str]
    per_residue: dict[str, dict[str, float]]
    notes: list[str] = field(default_factory=list)
    optimization: dict[str, Any] = field(default_factory=dict)
    per_kind: dict[str, dict[str, float]] = field(default_factory=dict)   # experiment kind -> {chi2, n}

    @property
    def reduced_chi2(self) -> float:
        dof = max(self.n_data - self.n_params, 1)
        return self.chi2 / dof

    @property
    def aic(self) -> float:
        return self.chi2 + 2 * self.n_params

    @property
    def bic(self) -> float:
        return self.chi2 + self.n_params * math.log(max(self.n_data, 1))

    def summary(self) -> dict[str, Any]:
        return {
            "params": {k: round(v, 6) for k, v in self.params.items()},
            "errors": {k: round(v, 6) for k, v in self.errors.items()},
            "chi2": round(self.chi2, 2), "n_data": self.n_data, "n_params": self.n_params,
            "reduced_chi2": round(self.reduced_chi2, 3), "aic": round(self.aic, 2), "bic": round(self.bic, 2),
            "residues": self.residues, "notes": self.notes, "optimization": self.optimization,
        }


class _Block:
    """One residue in one experiment: data plus a model callable."""

    def __init__(self, exp: Experiment, prof: Profile, omega_a_hz: float | None, r1: float | None):
        self.exp = exp
        self.prof = prof
        self.res = prof.residue
        if exp.kind.startswith("cpmg"):
            self.x, self.y, self.s = cpmg_r2eff_from_intensity(prof, exp.time)
        else:
            m = prof.x > -1e5  # drop the far-off reference point; scale is fitted
            self.x, self.y, self.s = prof.x[m], prof.intensity[m], prof.error[m]
            self.ynorm = np.max(self.y)
            self.y = self.y / self.ynorm
            self.s = self.s / self.ynorm
        self.omega_a_hz = omega_a_hz
        self.r1 = r1


def build_blocks(experiments: list[Experiment], residues: list[str], cs_n: dict[str, float] | None = None,
                 r1: dict[str, float] | None = None) -> tuple[list[_Block], list[str]]:
    blocks, notes = [], []
    for exp in experiments:
        for res in residues:
            prof = exp.profiles.get(res)
            if prof is None:
                continue
            if exp.kind == "cest_n":
                if cs_n is None or res not in cs_n:
                    notes.append(f"{exp.name}:{res} skipped (no ground-state 15N shift)")
                    continue
                om = (cs_n[res] - exp.carrier_ppm) * exp.nucleus_mhz
                r1v = (r1 or {}).get(res, 1.0)
                if r1 is None or res not in r1:
                    notes.append(f"{exp.name}:{res} R1 not given; fixed at 1.0 s^-1")
                blocks.append(_Block(exp, prof, om, r1v))
            else:
                try:
                    blocks.append(_Block(exp, prof, None, None))
                except ValueError as err:
                    notes.append(str(err))
    return blocks, notes


def fit_two_state(experiments: list[Experiment], residues: list[str], *, cs_n: dict[str, float] | None = None,
                  r1: dict[str, float] | None = None, kex0: float = 500.0, pb0: float = 0.05,
                  dw0: dict[str, float] | None = None, fix: dict[str, float] | None = None,
                  per_residue_exchange: bool = False, dw_sign_free: bool = True,
                  groups: dict[str, list[str]] | None = None,
                  dw_bounds: dict[str, tuple[float, float]] | None = None) -> FitResult:
    """Fit a two-state model. Global (shared kex, pb) unless per_residue_exchange or groups.

    groups: {group name: residues}; each group gets its own kex and pb (independent processes),
    all groups are fitted jointly so chi2/AIC/BIC compare directly with the global fit.

    Parameters per residue: dwN (ppm), dwH (ppm, only if a 1H CPMG block exists),
    R2 per experiment, and a scale per CEST block. `fix` may pin 'kex' and/or 'pb'.
    """
    fix = dict(fix or {})
    if len(residues) != len(set(residues)):
        raise ValueError("residues must be unique")
    if groups is not None:
        if per_residue_exchange:
            raise ValueError("choose groups or per_residue_exchange, not both")
        members = [r for rs in groups.values() for r in rs]
        if not groups or any(not rs for rs in groups.values()):
            raise ValueError("groups must be nonempty")
        if len(members) != len(set(members)) or set(members) != set(residues):
            raise ValueError("groups must partition the requested residues exactly once")
    blocks, notes = build_blocks(experiments, residues, cs_n, r1)
    if not blocks:
        raise ValueError("no data blocks for the requested residues/experiments")
    res_list = sorted({b.res for b in blocks}, key=lambda r: residue_label(r)[1])
    if groups and any(not set(rs).intersection(res_list) for rs in groups.values()):
        raise ValueError("each group must contain usable data")
    names: list[str] = []
    x0: list[float] = []
    lo: list[float] = []
    hi: list[float] = []

    def add(name, v, a, b):
        names.append(name); x0.append(v); lo.append(a); hi.append(b)

    if groups:
        res_group = {r: g for g, rs in groups.items() for r in rs}
        missing = [r for r in res_list if r not in res_group]
        if missing:
            raise ValueError(f"residues not assigned to any group: {missing}")
        group_names = list(groups)
    else:
        res_group = {r: (r if per_residue_exchange else "*") for r in res_list}
        group_names = res_list if per_residue_exchange else ["*"]
    groups_iter = group_names
    for g in groups_iter:
        if "kex" not in fix:
            add(f"kex[{g}]", kex0, 1.0, 1e5)
        if "pb" not in fix:
            add(f"pb[{g}]", pb0, 1e-4, 0.5)
    has_h = {b.res for b in blocks if b.exp.kind == "cpmg_h"}
    has_cest = {b.res for b in blocks if b.exp.kind == "cest_n"}
    for r in res_list:
        d0 = (dw0 or {}).get(r, 1.0)
        if dw_bounds and r in dw_bounds:
            lower, upper = dw_bounds[r]
            add(f"dwN[{r}]", float(np.clip(d0, lower + 1e-8, upper - 1e-8)), lower, upper)
        elif r in has_cest or dw_sign_free:
            add(f"dwN[{r}]", d0 if d0 != 0 else 1.0, -25.0, 25.0)
        else:
            add(f"dwN[{r}]", abs(d0) or 1.0, 0.0, 25.0)
        if r in has_h:
            add(f"dwH[{r}]", 0.1, -3.0, 3.0)
    for i, b in enumerate(blocks):
        add(f"R2[{b.res}|{b.exp.name}]", float(np.clip(np.min(b.y) if b.exp.kind.startswith("cpmg") else 10.0, 1.0, 80.0)), 0.1, 200.0)
        if b.exp.kind == "cest_n":
            add(f"scale[{b.res}|{b.exp.name}]", 1.0, 0.1, 10.0)
    idx = {n: i for i, n in enumerate(names)}

    def get(p, name, default=None):
        i = idx.get(name)
        return p[i] if i is not None else default

    def ex_params(p, res):
        g = res_group[res]
        return get(p, f"kex[{g}]", fix.get("kex")), get(p, f"pb[{g}]", fix.get("pb"))

    slices = []
    start = 0
    for b in blocks:
        slices.append(slice(start, start + len(b.y)))
        start += len(b.y)
    n_data = start

    def resid(p):
        out = np.empty(n_data)
        for b, sl in zip(blocks, slices):
            kex, pb = ex_params(p, b.res)
            r2 = get(p, f"R2[{b.res}|{b.exp.name}]")
            if b.exp.kind == "cpmg_n":
                m = cpmg_r2eff_model(b.x, b.exp.time, kex, pb, get(p, f"dwN[{b.res}]"), b.exp.nucleus_mhz, r2)
            elif b.exp.kind == "cpmg_h":
                m = cpmg_r2eff_model(b.x, b.exp.time, kex, pb, get(p, f"dwH[{b.res}]"), b.exp.nucleus_mhz, r2)
            else:
                m = get(p, f"scale[{b.res}|{b.exp.name}]") * cest_model(
                    b.x, b.exp.time, b.exp.b1_hz, kex, pb, b.omega_a_hz, get(p, f"dwN[{b.res}]"),
                    b.exp.nucleus_mhz, b.r1, r2)
            out[sl] = (b.y - m) / b.s
        return out

    # Jacobian sparsity: global params touch everything; residue params touch own blocks.
    J = lil_matrix((n_data, len(names)), dtype=int)
    for j, name in enumerate(names):
        if name.startswith(("kex[", "pb[")):
            g = name[name.index("[") + 1:-1]
            for b, sl in zip(blocks, slices):
                if res_group[b.res] == g:
                    J[sl, j] = 1
            continue
        key = name[name.index("[") + 1:-1]
        res_key, _, exp_key = key.partition("|")
        for b, sl in zip(blocks, slices):
            if b.res == res_key and (not exp_key or b.exp.name == exp_key):
                J[sl, j] = 1
    sol = least_squares(resid, np.array(x0), bounds=(np.array(lo), np.array(hi)), jac_sparsity=J,
                        x_scale="jac", max_nfev=400)
    chi2 = float(np.sum(sol.fun ** 2))
    errors: dict[str, float] = {}
    try:
        Jd = sol.jac.toarray() if hasattr(sol.jac, "toarray") else sol.jac
        cov = np.linalg.pinv(Jd.T @ Jd)
        scale = max(chi2 / max(n_data - len(names), 1), 1.0)
        sd = np.sqrt(np.clip(np.diag(cov) * scale, 0, None))
        errors = {n: float(s) for n, s in zip(names, sd)}
    except np.linalg.LinAlgError:
        notes.append("covariance unavailable")
    params = {n: float(v) for n, v in zip(names, sol.x)}
    per_res: dict[str, dict[str, float]] = {}
    per_kind: dict[str, dict[str, float]] = {}
    for b, sl in zip(blocks, slices):
        d = per_res.setdefault(b.res, {"chi2": 0.0, "n": 0})
        d["chi2"] += float(np.sum(sol.fun[sl] ** 2))
        d["n"] += len(b.y)
        k = per_kind.setdefault(b.exp.kind, {"chi2": 0.0, "n": 0})
        k["chi2"] += float(np.sum(sol.fun[sl] ** 2))
        k["n"] += len(b.y)
    for r in res_list:
        for key in ("dwN", "dwH"):
            if f"{key}[{r}]" in params:
                per_res[r][key] = params[f"{key}[{r}]"]
                per_res[r][key + "_err"] = errors.get(f"{key}[{r}]", float("nan"))
    if fix:
        notes.append(f"fixed: {fix}")
    optimization = {"success": bool(sol.success), "status": int(sol.status), "message": str(sol.message),
                    "nfev": int(sol.nfev), "optimality": float(sol.optimality),
                    "parameters_at_bounds": [n for n, active in zip(names, sol.active_mask) if active]}
    return FitResult(params, errors, chi2, n_data, len(names), res_list, per_res, notes, optimization, per_kind)


def _boot_replicate(args):
    experiments, base_res, per_res, kw, seed = args
    rng = np.random.default_rng(seed)
    pick = list(rng.choice(base_res, size=len(base_res), replace=True))
    exps, names, cs, r1, dw0 = [], [], {}, {}, {}
    for i, r in enumerate(pick):
        nm = f"{r}_{i}"
        names.append(nm)
        if kw.get("cs_n") and r in kw["cs_n"]:
            cs[nm] = kw["cs_n"][r]
        if kw.get("r1"):
            r1[nm] = kw["r1"].get(r, 1.0)
        dw0[nm] = per_res[r].get("dwN", 1.0)
    for e in experiments:
        e2 = Experiment(e.name, e.kind, e.b0_mhz, e.time, e.carrier_ppm, e.b1_hz, {})
        for nm, r in zip(names, pick):
            if r in e.profiles:
                p = e.profiles[r]
                e2.profiles[nm] = Profile(nm, p.resnum, p.x, p.intensity, p.error)
        exps.append(e2)
    kw2 = {k: v for k, v in kw.items() if k not in ("cs_n", "r1", "dw0")}
    try:
        fb = fit_two_state(exps, names, cs_n=cs or None, r1=r1 or None, dw0=dw0, **kw2)
        return fb.params["kex[*]"], fb.params["pb[*]"]
    except Exception:  # a failed replicate is counted, not raised
        return None


def bootstrap_global(experiments: list[Experiment], residues: list[str], n_boot: int = 20, seed: int = 0,
                     workers: int = 4, **kw) -> dict[str, Any]:
    """Residue-level bootstrap of the global kex/pb (resample residues with replacement, refit), run in parallel."""
    from concurrent.futures import ProcessPoolExecutor

    base = fit_two_state(experiments, residues, **kw)
    kw = dict(kw)
    kw["kex0"] = base.params.get("kex[*]", kw.get("kex0", 500.0))
    kw["pb0"] = base.params.get("pb[*]", kw.get("pb0", 0.05))
    jobs = [(experiments, base.residues, base.per_residue, kw, seed + i) for i in range(n_boot)]
    with ProcessPoolExecutor(max_workers=workers) as pool:
        res = [r for r in pool.map(_boot_replicate, jobs) if r is not None]
    kex_b = [r[0] for r in res]
    pb_b = [r[1] for r in res]
    return {"base": base.summary(), "n_boot_ok": len(kex_b), "n_boot": n_boot,
            "kex_mean": float(np.mean(kex_b)) if kex_b else None, "kex_sd": float(np.std(kex_b, ddof=1)) if len(kex_b) > 1 else None,
            "pb_mean": float(np.mean(pb_b)) if pb_b else None, "pb_sd": float(np.std(pb_b, ddof=1)) if len(pb_b) > 1 else None}


def _fit_renamed(exps, names, cs, r1, dw0, kw):
    # residue_label() cannot parse renamed keys, so patch profile residue names directly
    return fit_two_state(exps, names, cs_n=cs, r1=r1, dw0=dw0, **kw)


def cest_sign_scan(cest: Experiment, residues: list[str], dw_abs: dict[str, float], kex: float, pb: float,
                   cs_n: dict[str, float], r1: dict[str, float] | None = None,
                   grid: tuple[float, ...] = (2.0, 5.0, 10.0, 15.0, 20.0)) -> dict[str, dict[str, float]]:
    """Fit each residue's CEST profile (kex/pb fixed) from several starting |dw| values of both signs.

    Starts: the given |dw| (e.g. from CPMG) plus `grid` (ppm). Large |dw| are easily missed when the only
    start is a small CPMG value, so the grid is always tried. Reports the best fit per sign and whether
    the sign is supported conditionally on fixed kex/pb (opposite signs are fitted
    under separate bounds; unconstrained convergence is not evidence against the other sign).
    """
    out: dict[str, dict[str, float]] = {}
    for r in residues:
        if r not in cest.profiles or r not in cs_n:
            continue
        starts = sorted({round(abs(dw_abs.get(r, 1.0)) or 1.0, 3), *grid})
        best = {1: (float("inf"), 0.0), -1: (float("inf"), 0.0)}
        for s0 in starts:
            for sgn in (1, -1):
                bounds = (0.0, 25.0) if sgn > 0 else (-25.0, 0.0)
                f = fit_two_state([cest], [r], cs_n=cs_n, r1=r1, fix={"kex": kex, "pb": pb},
                                  dw0={r: sgn * s0}, dw_bounds={r: bounds})
                d = f.params[f"dwN[{r}]"]
                if f.chi2 < best[sgn][0]:
                    best[sgn] = (f.chi2, d)
        side = 1 if best[1][0] <= best[-1][0] else -1
        both_finite = all(math.isfinite(best[s][0]) for s in (1, -1))
        dchi = abs(best[1][0] - best[-1][0]) if both_finite else float("nan")
        at_bound = abs(best[side][1]) > 24.99 or abs(best[side][1]) < 1e-6
        out[r] = {"dw_best": best[side][1], "chi2_best": best[side][0],
                  "dw_best_other_sign": best[-side][1], "chi2_best_other_sign": best[-side][0],
                  "sign": float(side), "dchi2": dchi,
                  "determined": bool(both_finite and dchi > 4.0 and not at_bound),
                  "at_parameter_bound": at_bound, "starts_ppm": starts}
    return out
