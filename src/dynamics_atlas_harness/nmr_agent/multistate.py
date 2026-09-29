"""N-state exchange models (used for three-state alternatives to the two-state model).

Rate-matrix convention: K[i, j] (i != j) is the rate constant from state i to state j (s^-1).
State 0 is the major, observed state. Shifts are given per minor state as dw (ppm, state k minus state 0).
Same simplifications as exchange.py: ideal pulses, equal R2 (and R1) in all states.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.linalg import expm


def rates_three_state(topology: str, kex1: float, p1: float, kex2: float, p2: float) -> tuple[np.ndarray, np.ndarray]:
    """Populations and rate matrix for 3 states A(0), B(1), C(2).

    topology 'linear': A <-> B <-> C, kex1 = kAB + kBA, kex2 = kBC + kCB.
    topology 'star':   B <-> A <-> C, kex1 = kAB + kBA, kex2 = kAC + kCA.
    p1 = pB, p2 = pC; detailed balance within each connected pair.
    """
    pA = 1.0 - p1 - p2
    if pA <= 0:
        raise ValueError("populations exceed 1")
    p = np.array([pA, p1, p2])
    K = np.zeros((3, 3))

    def pair(i, j, kex):
        tot = p[i] + p[j]
        K[i, j] = kex * p[j] / tot
        K[j, i] = kex * p[i] / tot

    pair(0, 1, kex1)
    if topology == "linear":
        pair(1, 2, kex2)
    elif topology == "star":
        pair(0, 2, kex2)
    else:
        raise ValueError(topology)
    return p, K


def _exchange_generator(K: np.ndarray) -> np.ndarray:
    """dM/dt contribution: G = K^T - diag(row sums)."""
    return K.T - np.diag(K.sum(axis=1))


def cpmg_r2eff_n(nu_cpmg: np.ndarray, T: float, p: np.ndarray, K: np.ndarray, dw_ppm: np.ndarray,
                 nucleus_mhz: float, r2: float) -> np.ndarray:
    n = len(p)
    om = np.concatenate([[0.0], 2 * math.pi * np.asarray(dw_ppm) * nucleus_mhz])
    L = _exchange_generator(K).astype(complex) - r2 * np.eye(n) - 1j * np.diag(om)
    ncyc = np.rint(nu_cpmg * T).astype(int)
    tau = T / (4.0 * np.maximum(ncyc, 1))
    lam, V = np.linalg.eig(L)
    Vi = np.linalg.inv(V)
    E1 = np.einsum("ij,nj,jk->nik", V, np.exp(lam[None, :] * tau[:, None]), Vi)
    E2 = np.einsum("ij,nj,jk->nik", V, np.exp(lam[None, :] * 2 * tau[:, None]), Vi)
    U = E1 @ np.conj(E2) @ E1
    mu, W = np.linalg.eig(U)
    Wi = np.linalg.inv(W)
    Un = np.einsum("nij,nj,njk->nik", W, mu ** ncyc[:, None], Wi)
    ma = (Un @ p.astype(complex))[:, 0]
    return -np.log(np.clip(ma.real / p[0], 1e-12, None)) / T


def cest_n(offsets_hz: np.ndarray, T: float, b1_hz: float, p: np.ndarray, K: np.ndarray, omega_a_hz: float,
           dw_ppm: np.ndarray, nucleus_mhz: float, r1: float, r2: float) -> np.ndarray:
    n = len(p)
    nof = len(offsets_hz)
    w1 = 2 * math.pi * b1_hz
    G = _exchange_generator(K)
    L = np.zeros((nof, 3 * n, 3 * n))
    for s in range(n):
        om = 2 * math.pi * (omega_a_hz + (0.0 if s == 0 else dw_ppm[s - 1] * nucleus_mhz) - offsets_hz)
        b = 3 * s
        L[:, b, b] = -r2
        L[:, b, b + 1] = -om
        L[:, b + 1, b] = om
        L[:, b + 1, b + 1] = -r2
        L[:, b + 1, b + 2] = -w1
        L[:, b + 2, b + 1] = w1
        L[:, b + 2, b + 2] = -r1
    for s in range(n):
        for t in range(n):
            for c in range(3):
                L[:, 3 * s + c, 3 * t + c] += G[s, t]
    m0 = np.zeros(3 * n)
    m0[2::3] = p
    try:
        lam, V = np.linalg.eig(L)
        coef = np.linalg.solve(V, np.broadcast_to(m0.astype(complex), (nof, 3 * n))[..., None])[..., 0]
        out = np.einsum("nij,nj->ni", V, np.exp(lam * T) * coef)[:, 2].real / p[0]
        if np.all(np.isfinite(out)):
            return out
    except np.linalg.LinAlgError:
        pass
    return (expm(L * T) @ m0)[:, 2] / p[0]


def fit_three_state(experiments, residues, topology: str = "star", *, cs_n=None, r1=None,
                    kex1_0: float = 400.0, p1_0: float = 0.08, kex2_0: float = 1500.0, p2_0: float = 0.02,
                    dw1_0: dict | None = None, dw2_0: dict | None = None):
    """Global three-state fit (shared kex1, p1, kex2, p2; per-residue dw to each minor state).

    Returns an exchange.FitResult so chi2/AIC/BIC are directly comparable with two-state fits
    on the same residues and experiments.
    """
    from scipy.optimize import least_squares
    from scipy.sparse import lil_matrix

    from . import exchange as ex

    blocks, notes = ex.build_blocks(experiments, residues, cs_n, r1)
    if not blocks:
        raise ValueError("no data blocks for the requested residues/experiments")
    res_list = sorted({b.res for b in blocks}, key=lambda r: ex.residue_label(r)[1])
    has_h = {b.res for b in blocks if b.exp.kind == "cpmg_h"}
    names, x0, lo, hi = [], [], [], []

    def add(nm, v, a, b):
        names.append(nm); x0.append(v); lo.append(a); hi.append(b)

    add("kex1", kex1_0, 1.0, 1e5); add("p1", p1_0, 1e-4, 0.45)
    add("kex2", kex2_0, 1.0, 1e5); add("p2", p2_0, 1e-4, 0.45)
    for r in res_list:
        add(f"dwN1[{r}]", (dw1_0 or {}).get(r, 1.0), -25.0, 25.0)
        add(f"dwN2[{r}]", (dw2_0 or {}).get(r, 0.5), -25.0, 25.0)
        if r in has_h:
            add(f"dwH1[{r}]", 0.1, -3.0, 3.0)
            add(f"dwH2[{r}]", 0.05, -3.0, 3.0)
    for b in blocks:
        add(f"R2[{b.res}|{b.exp.name}]", float(np.clip(np.min(b.y) if b.exp.kind.startswith("cpmg") else 10.0, 1.0, 80.0)), 0.1, 200.0)
        if b.exp.kind == "cest_n":
            add(f"scale[{b.res}|{b.exp.name}]", 1.0, 0.1, 10.0)
    idx = {n: i for i, n in enumerate(names)}
    slices, start = [], 0
    for b in blocks:
        slices.append(slice(start, start + len(b.y)))
        start += len(b.y)
    n_data = start

    def resid(q):
        out = np.empty(n_data)
        try:
            p, K = rates_three_state(topology, q[0], q[1], q[2], q[3])
        except ValueError:
            return np.full(n_data, 1e3)
        for b, sl in zip(blocks, slices):
            r2 = q[idx[f"R2[{b.res}|{b.exp.name}]"]]
            if b.exp.kind == "cpmg_n":
                dw = np.array([q[idx[f"dwN1[{b.res}]"]], q[idx[f"dwN2[{b.res}]"]]])
                m = cpmg_r2eff_n(b.x, b.exp.time, p, K, dw, b.exp.nucleus_mhz, r2)
            elif b.exp.kind == "cpmg_h":
                dw = np.array([q[idx[f"dwH1[{b.res}]"]], q[idx[f"dwH2[{b.res}]"]]])
                m = cpmg_r2eff_n(b.x, b.exp.time, p, K, dw, b.exp.nucleus_mhz, r2)
            else:
                dw = np.array([q[idx[f"dwN1[{b.res}]"]], q[idx[f"dwN2[{b.res}]"]]])
                m = q[idx[f"scale[{b.res}|{b.exp.name}]"]] * cest_n(b.x, b.exp.time, b.exp.b1_hz, p, K, b.omega_a_hz,
                                                                     dw, b.exp.nucleus_mhz, b.r1, r2)
            out[sl] = (b.y - m) / b.s
        return out

    J = lil_matrix((n_data, len(names)), dtype=int)
    for j, nm in enumerate(names):
        if "[" not in nm:
            J[:, j] = 1
            continue
        key = nm[nm.index("[") + 1:-1]
        rk, _, ek = key.partition("|")
        for b, sl in zip(blocks, slices):
            if b.res == rk and (not ek or b.exp.name == ek):
                J[sl, j] = 1
    sol = least_squares(resid, np.array(x0), bounds=(np.array(lo), np.array(hi)), jac_sparsity=J, x_scale="jac", max_nfev=300)
    chi2 = float(np.sum(sol.fun ** 2))
    errors = {}
    try:
        Jd = sol.jac.toarray() if hasattr(sol.jac, "toarray") else sol.jac
        cov = np.linalg.pinv(Jd.T @ Jd)
        sc = max(chi2 / max(n_data - len(names), 1), 1.0)
        errors = {n: float(s) for n, s in zip(names, np.sqrt(np.clip(np.diag(cov) * sc, 0, None)))}
    except np.linalg.LinAlgError:
        notes.append("covariance unavailable")
    params = {n: float(v) for n, v in zip(names, sol.x)}
    per_res = {}
    per_kind = {}
    for b, sl in zip(blocks, slices):
        d = per_res.setdefault(b.res, {"chi2": 0.0, "n": 0})
        d["chi2"] += float(np.sum(sol.fun[sl] ** 2)); d["n"] += len(b.y)
        k = per_kind.setdefault(b.exp.kind, {"chi2": 0.0, "n": 0})
        k["chi2"] += float(np.sum(sol.fun[sl] ** 2)); k["n"] += len(b.y)
    for r in res_list:
        for k in ("dwN1", "dwN2", "dwH1", "dwH2"):
            if f"{k}[{r}]" in params:
                per_res[r][k] = params[f"{k}[{r}]"]
                per_res[r][k + "_err"] = errors.get(f"{k}[{r}]", float("nan"))
    notes.append(f"three-state {topology}: states A (major), B (p1), C (p2); kex1 couples A-B; kex2 couples "
                 + ("B-C" if topology == "linear" else "A-C"))
    optimization = {"success": bool(sol.success), "status": int(sol.status), "message": str(sol.message),
                    "nfev": int(sol.nfev), "optimality": float(sol.optimality),
                    "parameters_at_bounds": [n for n, active in zip(names, sol.active_mask) if active]}
    return ex.FitResult(params, errors, chi2, n_data, len(names), res_list, per_res, notes, optimization, per_kind)
