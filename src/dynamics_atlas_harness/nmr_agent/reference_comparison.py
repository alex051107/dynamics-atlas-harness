"""Paired chemical-shift comparisons. No reference-specific structural verdicts."""
from __future__ import annotations

import math
import numpy as np


def compare(ground: dict, dw: dict, references: dict, residues: list[str]) -> dict:
    if not references:
        raise ValueError("select at least one reference")
    requested = list(dict.fromkeys(residues))
    mappings = [ground, dw, *references.values()]
    common = [r for r in requested if all(r in d and isinstance(d[r], (int, float))
              and math.isfinite(d[r]) for d in mappings)]
    if not common:
        raise ValueError("no finite common residues")
    result = {"requested": requested, "common_residues": common,
              "missing": {r: [name for name, d in {"ground": ground, "dw": dw, **references}.items()
                              if r not in d or d[r] is None] for r in requested if r not in common},
              "comparison": "x = reference minus ground; y = signed fitted dw. RMSD is to identity, not regression.",
              "references": {}}
    y = np.array([dw[r] for r in common])
    for name, ref in references.items():
        x = np.array([ref[r] - ground[r] for r in common])
        residual = y - x
        valid_corr = len(common) >= 3 and np.ptp(x) > 0 and np.ptp(y) > 0
        r = float(np.corrcoef(x, y)[0, 1]) if valid_corr else None
        result["references"][name] = {
            "n": len(common), "pearson_r": r, "r_squared": r*r if r is not None else None,
            "rmsd_ppm": float(np.sqrt(np.mean(residual**2))),
            "mean_residual_ppm": float(residual.mean()),
            "per_residue": {k: {"reference_minus_ground_ppm": float(a), "dw_ppm": float(b),
                                "minor_minus_reference_ppm": float(c)}
                            for k, a, b, c in zip(common, x, y, residual)}}
    result["limit"] = "Descriptive comparisons only; fit/measurement/predictor uncertainties and condition mismatch are not included in these point metrics. Correlation and RMSD are not independent evidence or a solved structure."
    return result
