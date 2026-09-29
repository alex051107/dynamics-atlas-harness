"""Reference chemical-shift sets and structure-derived distances for the analysis agent.

- Workspace reference sets: JSON files `<variant>/references/<name>.json` holding
  {"description": ..., "conditions": ..., "shifts": {"V29N": 120.1, ...}}.
- Sequence-based random-coil prediction with POTENCI (Nielsen & Mulder, J Biomol NMR 2018;
  protein-nmr/POTENCI commit c9a6e83, MIT), run in a sandbox without network.
- PDB distances: backbone atom of each residue to the nearest atom of a chosen ligand, from an
  RCSB mmCIF file (coordinates only; titles and citations are not returned).
"""

from __future__ import annotations

import json
import os
import math
import re
import shutil
import subprocess
import sys
import textwrap
import urllib.request
from pathlib import Path
from typing import Any

def _find_potenci() -> Path:
    """POTENCI script location: $DYNAMICS_ATLAS_POTENCI, else the nearest ancestor holding external_tools/POTENCI."""
    env = os.environ.get("DYNAMICS_ATLAS_POTENCI")
    if env:
        return Path(env)
    for parent in Path(__file__).resolve().parents:
        cand = parent / "external_tools" / "POTENCI" / "potenci.py3"
        if cand.exists():
            return cand
    return Path("external_tools/POTENCI/potenci.py3")


POTENCI = _find_potenci()


def list_workspace_references(ws: Path) -> list[dict[str, Any]]:
    out = []
    for f in sorted(ws.glob("*/references/*.json")):
        # Resolve symlinks as well as lexical paths before reading any content.
        f = checked_reference_path(ws, f.parent.parent.name, f.stem)
        d = json.loads(f.read_text())
        out.append({"variant": f.parent.parent.name, "name": f.stem, "description": d.get("description"),
                    "conditions": d.get("conditions"), "n_shifts": len(d.get("shifts", {}))})
    return out


def checked_reference_path(ws: Path, variant: str, name: str) -> Path:
    for label, value in (("variant", variant), ("reference name", name)):
        if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", value):
            raise ValueError(f"{label} must be a simple identifier, not a path")
    root = ws.resolve()
    f = (root / variant / "references" / f"{name}.json").resolve()
    if root not in f.parents:
        raise PermissionError("reference path outside workspace")
    return f


def get_workspace_reference(ws: Path, variant: str, name: str) -> dict[str, Any]:
    f = checked_reference_path(ws, variant, name)
    if not f.exists():
        raise ValueError(f"no reference '{name}' for {variant}")
    return json.loads(f.read_text())


def potenci_random_coil(sequence: str, first_resnum: int, pH: float, temperature_k: float, ionic_m: float,
                        cache_dir: Path, potenci_path: Path = POTENCI) -> dict[str, Any]:
    if not potenci_path.exists():
        raise FileNotFoundError(f"POTENCI not found at {potenci_path}")
    cache_dir.mkdir(parents=True, exist_ok=True)
    key = f"{abs(hash(sequence)) % 10**8}_{pH:.2f}_{temperature_k:.1f}_{ionic_m:.3f}"
    work = cache_dir / key
    work.mkdir(exist_ok=True)
    shutil.copy(potenci_path, work / "potenci.py")
    profile = textwrap.dedent(f"""(version 1)(allow default)(deny network*)
        (deny file-write* (subpath "{Path.home()}"))(allow file-write* (subpath "{work.resolve()}"))""")
    if sys.platform == "darwin":
        cmd = ["/usr/bin/sandbox-exec", "-p", profile, "/opt/anaconda3/bin/python3", "potenci.py",
               sequence, f"{pH}", f"{temperature_k}", f"{ionic_m}"]
    else:  # Linux (Longleaf node): bubblewrap, no network, only the work dir writable
        from .sandbox import bwrap_cmd
        cmd = bwrap_cmd([sys.executable, "potenci.py", sequence, f"{pH}", f"{temperature_k}", f"{ionic_m}"], ro=[], rw=[work], cwd=work)
    p = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=300)
    outs = sorted(work.glob("outPOTENCI_*.txt"))
    if not outs:
        raise RuntimeError(f"POTENCI failed: {p.stdout[-500:]} {p.stderr[-500:]}")
    shifts: dict[str, float] = {}
    for line in outs[-1].read_text().splitlines():
        if line.startswith("#") or not line.strip():
            continue
        parts = line.split()
        num, aa = int(parts[0]), parts[1]
        vals = dict(zip(["N", "C", "CA", "CB", "H", "HA", "HB"], [float(x) for x in parts[2:9]]))
        resnum = num - 1 + first_resnum
        for at in ("N", "H", "CA", "CB", "C"):
            if vals.get(at):
                shifts[f"{aa}{resnum}{at}"] = vals[at]
    return {"description": "POTENCI sequence-based random-coil prediction", "conditions":
            {"pH": pH, "temperature_K": temperature_k, "ionic_strength_M": ionic_m},
            "note": "No predictions for terminal residues; pH correction applied only if pH != 7.0.",
            "shifts": shifts}


def _parse_mmcif_atoms(text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    atoms, cols, i = [], [], 0
    while i < len(lines):
        if lines[i].startswith("_atom_site."):
            while i < len(lines) and lines[i].startswith("_atom_site."):
                cols.append(lines[i].split(".", 1)[1].strip())
                i += 1
            while i < len(lines) and lines[i].startswith(("ATOM", "HETATM")):
                vals = lines[i].split()
                if len(vals) == len(cols):
                    atoms.append(dict(zip(cols, vals)))
                i += 1
            break
        i += 1
    return atoms


def pdb_ligand_distances(pdb_id: str, ligand: str | None, ligand_atoms: list[str] | None = None,
                         atom: str = "N", chain: str | None = None, cache_dir: Path | None = None) -> dict[str, Any]:
    pdb_id = pdb_id.strip().upper()
    if not re.fullmatch(r"[1-9][A-Z0-9]{3}", pdb_id):
        raise ValueError("pdb_id must be a four-character PDB accession")
    cache = (cache_dir / f"{pdb_id}.cif") if cache_dir else None
    if cache and cache.exists():
        text = cache.read_text()
    else:
        with urllib.request.urlopen(f"https://files.rcsb.org/download/{pdb_id}.cif", timeout=60) as r:
            text = r.read().decode()
        if cache:
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(text)
    atoms = [a for a in _parse_mmcif_atoms(text) if a.get("pdbx_PDB_model_num", "1") == "1"]
    hets = sorted({(a["auth_comp_id"], a["auth_asym_id"]) for a in atoms if a["group_PDB"] == "HETATM" and a["auth_comp_id"] != "HOH"})
    chains = sorted({a["auth_asym_id"] for a in atoms if a["group_PDB"] == "ATOM"})
    if not ligand:
        return {"pdb": pdb_id, "protein_chains": chains, "ligands_present": [f"{c}:{ch}" for c, ch in hets],
                "note": "Call again with ligand (and optionally ligand_atoms, e.g. ['PG','O1G','O2G','O3G'])."}
    ch = chain or (chains[0] if chains else None)
    lig = [a for a in atoms if a["auth_comp_id"] == ligand.upper() and (not ligand_atoms or a["auth_atom_id"] in ligand_atoms)]
    if not lig:
        raise ValueError(f"ligand {ligand} {ligand_atoms or ''} not found; present: {[c for c, _ in hets]}")
    L = [(float(a["Cartn_x"]), float(a["Cartn_y"]), float(a["Cartn_z"])) for a in lig]
    rows = {}
    for a in atoms:
        if a["group_PDB"] != "ATOM" or a["auth_asym_id"] != ch or a["auth_atom_id"] != atom:
            continue
        xyz = (float(a["Cartn_x"]), float(a["Cartn_y"]), float(a["Cartn_z"]))
        d = min(math.dist(xyz, q) for q in L)
        rows[f"{a['auth_comp_id']}{a['auth_seq_id']}"] = round(d, 2)
    return {"pdb": pdb_id, "chain": ch, "ligand": ligand.upper(), "ligand_atoms_used": sorted({a["auth_atom_id"] for a in lig}),
            "backbone_atom": atom, "distance_A": rows,
            "note": "Author residue numbering of the PDB file; residue keys use three-letter codes."}
