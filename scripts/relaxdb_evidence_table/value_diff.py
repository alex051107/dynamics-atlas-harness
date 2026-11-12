#!/usr/bin/env python3
"""On the 21 papers Codex arm A and Sonnet v2 both read in full (IRSPTB, 7432, BPTI): which kinetic and population numbers
each arm wrote, which only one arm wrote, and what kind of quantity each one-arm number is (by the name written beside it).
  value_diff.py            -> prints per-kind counts and writes value_diff.csv"""
import os
import csv, glob, json, re, collections
from pathlib import Path
W = Path.home() / "dynamics_atlas_work"
S = Path("autoresearch/tasks/dynamics_atlas_stage1_loop_20261002/outputs/scale133_20261109")
ENTS = ["IRSPTB", "7432", "BPTI"]
NUM = re.compile(r"(?<![\w.])-?\d+(?:\.\d+)?(?:\s*[x×]\s*10\^?[-−]?\d+|[eE][-−]?\d+)?")
KIND = [("tumbling", r"tau_?[cm]\b|τ[cm]|tumbl|correlation time of the molecule|overall"),
        ("md_or_sim_length", r"\bns\b.*(simulat|trajector|MD)|(simulat|trajector|MD).*\bns\b"),
        ("exchange_rate", r"k_?ex|kex|k_?AB|k_?BA|k_?open|k_?close|k_?on|k_?off|exchange rate|s-1|s−1|s\^-1|/s\b"),
        ("Rex_or_R2", r"R_?ex|Rex|R2|R_2|R1|NOE"),
        ("chemical_shift_diff", r"Δω|delta-?omega|Δδ|ppm"),
        ("order_parameter", r"S2|S\^2|order parameter"),
        ("population", r"%|p_?[AB]\b|population|fraction|occupan")]
def rows(case):
    p = Path(case) / "rows.jsonl"
    return [json.loads(l) for l in open(p) if l.strip()] if p.exists() else []
def numbers(r):
    out = []
    for f in ("timescale", "population"):
        t = str(r.get(f) or "")
        for part in re.split(r";", t):
            for m in NUM.finditer(part):
                v = m.group(0).replace(" ", "").replace("−", "-")
                try:
                    if abs(float(re.split(r"[x×eE]", v)[0])) in (0, 1, 2) and len(v) == 1:
                        continue
                except ValueError:
                    pass
                out.append((v, f, part.strip()))
    return out
def kind(ctx):
    for k, rx in KIND:
        if re.search(rx, ctx, re.I):
            return k
    return "other"
def text_of(e, doi):
    for p in (W / "sources_cache").glob(doi.replace("/", "_") + "*.txt"):
        return p.read_text(errors="replace")
    return ""
A, B = {}, {}
for e in ENTS:
    for c in json.load(open(S / "race" / e / "arm_A.json"))["cases"]:
        if not c.get("bio_blocked"):
            for r in rows(W / "cases" / c["case"]):
                A.setdefault((e, (r.get("doi") or "").lower()), []).append(r)
    for r in rows(sorted(glob.glob(str(S / f"b_v2_test_sonnet/cases/B1_r6_{e}_*")))[-1]):
        B.setdefault((e, (r.get("doi") or "").lower()), []).append(r)
full = lambda d, k: k in d and all(r.get("access") != "abstract_only" for r in d[k])
common = [k for k in A if k[1] and full(A, k) and full(B, k)]
out, tally = [], collections.Counter()
for k in common:
    va = {v: (f, ctx) for r in A[k] for v, f, ctx in numbers(r)}
    vb = {v: (f, ctx) for r in B[k] for v, f, ctx in numbers(r)}
    txt = text_of(*k)
    for side, mine, other in (("A_only", va, vb), ("B_only", vb, va), ("both", {x: va[x] for x in va if x in vb}, {})):
        for v, (f, ctx) in mine.items():
            if side != "both" and v in other:
                continue
            kd = kind(ctx)
            tally[(side, kd)] += 1
            out.append({"entry": k[0], "doi": k[1], "side": side, "kind": kd, "value": v, "field": f,
                        "in_paper_text": (v in txt) if txt else "", "context": ctx[:160]})
print("papers compared", len(common), "rows A", sum(len(A[k]) for k in common), "rows B", sum(len(B[k]) for k in common))
for side in ("both", "A_only", "B_only"):
    print(side, sum(n for (s, _), n in tally.items() if s == side), {kd: n for (s, kd), n in sorted(tally.items()) if s == side})
with open(Path(__file__).with_name("value_diff.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
