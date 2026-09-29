"""Review node internals: fit inventory read from the run directory, review call, verdict parsing."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage

CHECKS = ("UNREPORTED_FITS", "RETRACTIONS_WITHOUT_TEST", "DATA_TYPES_FITTED_SEPARATELY")


def experiment_kinds(workspace: Path | None) -> dict[str, str]:
    """experiment name -> kind (cpmg_n, cest_n, ...) from the workspace's experiments.json files."""
    kinds: dict[str, str] = {}
    if workspace is None:
        return kinds
    for p in [workspace / "experiments.json", *sorted(workspace.glob("*/experiments.json"))]:
        if p.is_file():
            try:
                for name, e in json.loads(p.read_text()).get("experiments", {}).items():
                    kinds[name] = str(e.get("kind", "other"))
            except (ValueError, AttributeError):
                continue
    return kinds


def _kind(name: str, kinds: dict[str, str]) -> str:
    if name in kinds:
        return kinds[name].split("_")[0]          # cpmg_n -> cpmg, cest_n -> cest
    low = name.lower()
    return "cpmg" if "cpmg" in low else "cest" if "cest" in low else "other"


def _observation_fit_ids(run_dir: Path) -> dict[str, str]:
    """fit_id -> observation id that produced it (so an observation citation counts as citing the fit)."""
    out: dict[str, str] = {}
    for p in sorted((run_dir / "observations").glob("O*.json")):
        try:
            d = json.loads(p.read_text())
        except ValueError:
            continue
        r = d.get("result") if isinstance(d, dict) else None
        if d.get("tool") == "fit_exchange" and not d.get("error") and isinstance(r, dict) and r.get("fit_id"):
            out[r["fit_id"]] = p.stem
    return out


def collect_fit_inventory(run_dir: Path, report: str, workspace: Path | None = None) -> dict[str, Any]:
    kinds = experiment_kinds(workspace)
    fit_obs = _observation_fit_ids(run_dir)
    cited_ids = set(re.findall(r"\bF\d+\b", report))
    cited_obs = set(re.findall(r"\bO\d{6}\b", report))
    fits = []
    for p in sorted((run_dir / "fits").glob("F*.json"), key=lambda q: int(re.sub(r"\D", "", q.stem) or 0)):
        try:
            f = json.loads(p.read_text())
        except ValueError:
            continue
        fid = f.get("fit_id", p.stem)
        exps = list(f.get("experiments") or [])
        types = sorted({_kind(e, kinds) for e in exps})
        fits.append({
            "fit_id": fid, "observation_id": fit_obs.get(fid), "model": f.get("model"), "mode": f.get("mode"),
            "experiments": exps, "data_types": types, "n_residues": len(f.get("per_residue") or {}),
            "grouped": bool(f.get("groups")), "global": f.get("global"), "reduced_chi2": f.get("reduced_chi2"),
            "aic": f.get("aic"), "bic": f.get("bic"), "flags": f.get("flags") or [],
            "cited_in_report": fid in cited_ids or fit_obs.get(fid) in cited_obs})
    existing = {f["fit_id"] for f in fits}
    by_type: dict[str, list[str]] = {}
    for f in fits:
        by_type.setdefault(f["data_types"][0] if len(f["data_types"]) == 1 else "mixed", []).append(f["fit_id"])
    return {
        "n_fits": len(fits),
        "data_types_in_workspace": sorted({_kind(n, kinds) for n in kinds}) if kinds else None,
        "fits_by_data_type": by_type,
        "flagged_fit_ids": [f["fit_id"] for f in fits if f["flags"]],
        "uncited_fit_ids": [f["fit_id"] for f in fits if not f["cited_in_report"]],
        # tool fit ids are zero-padded (F003); un-padded tokens such as F130 are far more often residue names
        "cited_but_missing": sorted(i for i in cited_ids - existing if re.fullmatch(r"F0\d\d", i)),
        "fits": fits}


def read_report(run_dir: Path, messages: list[BaseMessage]) -> str | None:
    """REPORT.md written by the tool server; else the report argument of the last finish call in the transcript."""
    p = run_dir / "REPORT.md"
    if p.is_file() and p.read_text().strip():
        return p.read_text()
    for m in reversed(messages):
        for tc in getattr(m, "tool_calls", None) or []:
            if tc.get("name") == "finish" and isinstance(tc.get("args", {}).get("report"), str):
                return tc["args"]["report"]
    return None


def review_messages(review_prompt: str, report: str, inventory: dict[str, Any]) -> list[BaseMessage]:
    return [SystemMessage(content=review_prompt),
            HumanMessage(content="REPORT\n======\n" + report + "\n\nFIT INVENTORY (JSON, prepared by a program from the run directory)\n"
                         "====================================================================\n"
                         + json.dumps(inventory, ensure_ascii=False, indent=1))]


def parse_verdict(text: str) -> dict[str, Any] | None:
    """Extract {verdict, findings, required_actions} from a model reply; None when it cannot be parsed."""
    if isinstance(text, list):
        text = "".join(b.get("text", "") if isinstance(b, dict) else str(b) for b in text)
    candidates = [text] + re.findall(r"\{.*\}", text, flags=re.S)
    for c in candidates:
        try:
            d = json.loads(c)
        except ValueError:
            continue
        if isinstance(d, dict) and d.get("verdict") in ("pass", "revise"):
            actions = [str(a) for a in (d.get("required_actions") or []) if str(a).strip()]
            findings = d.get("findings") if isinstance(d.get("findings"), list) else []
            if d["verdict"] == "revise" and not actions:
                d["verdict"] = "pass"          # a revise without a concrete action cannot be acted on
            return {"verdict": d["verdict"], "findings": findings, "required_actions": actions}
    return None


def feedback_text(round_no: int, max_rounds: int, actions: list[str]) -> str:
    items = "\n".join(f"- {a}" for a in actions)
    return (f"Independent review of your report (return {round_no} of at most {max_rounds}). The report was not accepted yet. "
            f"Do the following, then call finish again with the complete revised report and atlas_entries:\n{items}")
