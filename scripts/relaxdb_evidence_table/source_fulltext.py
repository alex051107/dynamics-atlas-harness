#!/usr/bin/env python3
"""Free, legal full text for the RelaxDB source papers, judged by fulltext_check. Reuses access_fulltext.py's routes.

  source_fulltext.py run [--limit N] [--resume]    Europe PMC XML, preprint XML, open-access PDF links from OpenAlex
  source_fulltext.py drop                          judge PDFs the owner put in source_texts/drop/
  source_fulltext.py report                        write source_text_status.csv and still_needed.csv

Targets: rows of spine_20261112/source_papers.csv with a DOI, not already `have_full_text`, whose entry is not sealed.
Nothing goes to sources_cache. Files land in spine_20261112/source_texts/staging/ (rejected/ and unverified/ beside it).
No logins, no cookies, no proxy. A 403/429 or a challenge page stops that host for the rest of the run.
PDF hosts: access_fulltext's repository list plus the host of any link OpenAlex marks open access (is_oa) for a target.
"""
import os
import argparse
import collections
import csv
import json
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import access_fulltext as A  # noqa: E402

F = A.F
SPINE = A.WORK / "outputs/spine_20261112"
OUT = SPINE / "source_texts"
A.STAGING, DROP, RESULTS = OUT / "staging", OUT / "drop", OUT / "results.json"
SPLITS = Path.home() / "dynamics_atlas_eval/gold/splits.json"
OPENALEX = "https://api.openalex.org/works?per-page=50&select=doi,open_access,locations&filter=doi:"
A.GAP["api.openalex.org"] = 0.3


# An owner-supplied PDF whose DOI or title was found inside it is accepted when its only failures are layout checks
# built to catch wrong papers from automatic fetches (letters without section headings, author manuscripts with other page counts).
OWNER_SOFT = {"structure_methods", "structure_results", "structure_refs", "pages_range", "pdf_meta_title", "pdf_meta_doi", "access_stamp"}


def targets():
    sealed = set(map(str, json.loads(SPLITS.read_text())["sealed"]))
    by = {}
    for r in csv.DictReader((SPINE / "source_papers.csv").open()):
        if not r["doi"] or r["entry_id"] in sealed or r["text_status"] == "have_full_text":
            continue
        p = by.setdefault(r["doi"].lower(), {
            "doi": r["doi"].lower(), "tier": "A", "entries": [], "title": r["title"], "kind": r["text_status"], "text_chars": 0,
            "manifest_pmcid": r["pmcid"], "pmid": r["pmid"], "no_abstract": False, "openalex": None, "journal": r["journal"], "year": r["year"]})
        p["entries"].append(r["entry_id"])
    return list(by.values())


def add_openalex(net, papers):
    by = {p["doi"]: p for p in papers}
    dois = sorted(by)
    for i in range(0, len(dois), 40):
        r = net.get(OPENALEX + "|".join(urllib.parse.quote(d, safe="/") for d in dois[i:i + 40]), "application/json", route="openalex")
        if r["error"]:
            print("openalex:", r["error"], flush=True)
            continue
        for w in json.loads(r["body"])["results"]:
            d = (w.get("doi") or "").lower().replace("https://doi.org/", "")
            if d not in by:
                continue
            locs = w.get("locations") or []
            pdf = [x["pdf_url"] for x in locs if x.get("is_oa") and x.get("pdf_url")]
            A.HOSTS_C.update(urllib.parse.urlparse(u).hostname for u in pdf)
            by[d]["openalex"] = {"status": (w.get("open_access") or {}).get("oa_status"), "pdf": pdf,
                                 "landing": [x["landing_page_url"] for x in locs if x.get("is_oa") and x.get("landing_page_url")]}


def load():
    return json.loads(RESULTS.read_text()) if RESULTS.exists() else {"papers": {}, "host_blocks": {}, "drop": []}


def cmd_run(a):
    A.EGRESS = F.egress_route()
    prev, papers = load(), targets()[: a.limit or None]
    net = A.Net(prev["host_blocks"])
    add_openalex(net, papers)
    res = prev["papers"] if a.resume else {}
    for i, p in enumerate(papers, 1):
        if a.resume and p["doi"] in res:
            continue
        out = A.process(net, p, {"a", "b", "c"})
        out.update(final=A.final_of(out), journal=p["journal"], year=p["year"], oa_status=(p["openalex"] or {}).get("status"))
        res[p["doi"]] = out
        print(f"[{i}/{len(papers)}] {p['doi']} {p['kind']}: {out['final'].get('verdict') or 'no file'}", flush=True)
        RESULTS.write_text(json.dumps({"papers": res, "host_blocks": net.blocks, "drop": prev["drop"], "request_log": net.log}, indent=1, ensure_ascii=False))
    print("blocks", json.dumps(net.blocks, indent=1))
    return cmd_report(a)


def cmd_drop(a):
    A.EGRESS = F.egress_route()
    state, known, out = load(), {p["doi"]: p for p in targets()}, []
    for path in sorted(DROP.glob("*.pdf")) if DROP.exists() else []:
        doc = F.read_pdf(path)
        rec = {"file": path.name, "doi": None, "verdict": None}
        if doc.get("header_ok") and "raw" in doc:
            first = "\n".join(doc["raw"].split("\f")[:2]) + "\n" + doc["info"]
            hit = [d for d in (F.norm_doi(x).rstrip(".)") for x in re.findall(r"10\.\d{4,9}/[^\s\"'<>]+", first)) if d in known]
            if not hit:
                sq = F.squash("\n".join(doc["raw"].split("\f")[:3]))
                for d, p in known.items():
                    toks = F.content_tokens(p["title"])
                    if len(toks) >= 6 and sum(t in sq for t in toks) / len(toks) >= 0.95:
                        hit = [d]
                        break
            if hit:
                raw = path.read_bytes()
                fake = {"url": "file://drop/" + path.name, "host": "owner drop folder", "ctype": "application/pdf"}
                res, side = A.judge_and_stage_pdf({"doi": hit[0], "title": known[hit[0]]["title"], "openalex": None}, "drop", A.sha(raw)[:12],
                                                  fake, "owner download placed in source_texts/drop/", raw)
                chars = len(doc["raw"])
                soft = set(res["reasons"]) <= OWNER_SOFT and chars >= 12000
                rec.update(doi=hit[0], verdict="PASS" if res["verdict"] == "PASS" else "PASS_OWNER_FILE" if res["verdict"] == "FAIL" and soft else res["verdict"],
                           reasons=res["reasons"], staged=side["file"], chars=chars)
        out.append(rec)
        print(rec["file"], rec["doi"] or "NOT IDENTIFIED", rec["verdict"], flush=True)
    state["drop"] = out
    RESULTS.write_text(json.dumps(state, indent=1, ensure_ascii=False))
    return cmd_report(a)


def cmd_report(a):
    state = load()
    dropped = {d["doi"]: d for d in state["drop"] if str(d.get("verdict")).startswith("PASS") and not d["file"].startswith("supp_")}
    manual = json.loads((OUT / "manual_accept.json").read_text()) if (OUT / "manual_accept.json").exists() else {}
    rows, need = [], []
    for p in targets():
        r = state["papers"].get(p["doi"], {})
        fin = r.get("final") or {}
        verdict = dropped[p["doi"]]["verdict"] if p["doi"] in dropped else "PASS_MANUAL" if p["doi"] in manual else fin.get("verdict") or "NO_FILE"
        why = "; ".join(dict.fromkeys(str(x.get("outcome"))[:70] for x in r.get("attempts", []) if not (x.get("check") or {}).get("verdict") == "PASS"))
        row = {"doi": p["doi"], "entries": "|".join(p["entries"]), "year": p["year"], "journal": p["journal"], "title": p["title"],
               "status_before": p["kind"], "oa_status": r.get("oa_status") or "", "verdict": verdict,
               "route": "drop" if p["doi"] in dropped else fin.get("route") or "", "file": (dropped.get(p["doi"]) or {}).get("staged") or fin.get("file") or "",
               "why_not": manual.get(p["doi"], "") if verdict.startswith("PASS") else why,
               "how_to_get": "" if verdict.startswith("PASS") else how_to_get(r, p)}
        rows.append(row)
        if not verdict.startswith("PASS"):
            need.append({k: row[k] for k in ("how_to_get", "doi", "entries", "year", "journal", "title", "oa_status", "why_not")} | {"url": "https://doi.org/" + p["doi"]})
    for name, data in (("source_text_status.csv", rows), ("still_needed.csv", sorted(need, key=lambda x: (x["how_to_get"], x["journal"], x["year"])))):
        with (OUT / name).open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(data[0]))
            w.writeheader()
            w.writerows(data)
    print("targets", len(rows), dict(collections.Counter(r["verdict"] for r in rows)))
    print("by status_before", {k: dict(v) for k, v in _cross(rows).items()})
    return 0


def how_to_get(r, p):
    pmc = [a["id"] for a in r.get("attempts", []) if a.get("route") == "a" and a.get("id")]
    if pmc:
        return "free, no login: PMC page https://pmc.ncbi.nlm.nih.gov/articles/" + pmc[0] + "/ (PDF button)"
    if r.get("oa_status") in ("gold", "hybrid", "bronze", "green"):
        return "free, no login: publisher or repository copy (OpenAlex says " + r["oa_status"] + ")"
    return "UNC subscription"


def _cross(rows):
    out = collections.defaultdict(collections.Counter)
    for r in rows:
        out[r["status_before"]][r["verdict"]] += 1
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["run", "drop", "report"])
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--resume", action="store_true")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    DROP.mkdir(exist_ok=True)
    return {"run": cmd_run, "drop": cmd_drop, "report": cmd_report}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
