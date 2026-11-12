#!/usr/bin/env python3
"""Locate cached text files of a paper by DOI and/or PMCID. Prints candidate paths, best first (largest plain text)."""
import os
import glob, os, re, sys
from pathlib import Path
SC = Path.home() / "dynamics_atlas_work/sources_cache"
def find(doi, pmcid=""):
    key = doi.lower().replace("/", "_")
    pats = [f"*{key}*"] + ([f"*{pmcid}*"] if pmcid else [])
    out = []
    for p in pats:
        for f in glob.glob(str(SC / p)):
            n = os.path.basename(f).lower()
            if n.endswith((".txt", ".md")) and "_si" not in n and "provenance" not in n and "layout" not in n and os.path.getsize(f) > 8000:
                out.append(f)
    return sorted(set(out), key=lambda f: -os.path.getsize(f))
if __name__ == "__main__":
    for f in find(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else ""): print(f, os.path.getsize(f))
