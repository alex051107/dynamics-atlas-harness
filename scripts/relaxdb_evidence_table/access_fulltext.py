#!/usr/bin/env python3
"""Recover full text for the race papers that have only an abstract or a PMC stub, and judge every file with fulltext_check.

  access_fulltext.py run [--resume] [--routes a,b,c,drop] [--limit N] [--stub-chars 5000]
  access_fulltext.py promote [--dry-run]       copy passing staged files into sources_cache (NOT part of `run`; run only when told)

Targets: every paper in race/*/fulltext_manifest.json whose status is not `fulltext`, or `fulltext` with cached text under
--stub-chars characters. Routes, in order, stopping at the first file that passes the check:
  a    Europe PMC / PMC XML by PMCID (PMCID from the Europe PMC DOI record, the manifest and the OpenAlex locations)
  b    Europe PMC preprint (PPR) XML for bioRxiv/medRxiv DOIs (10.1101/..., 10.64898/...), by the record's preprint id
  c    PDF links from access_20261110/openalex_oa_locations.json on repository, bioRxiv/medRxiv and PMC hosts only
  drop PDFs the owner placed in access_20261110/drop/, identified by content (also runs for papers a-c already recovered)
Nothing is written to sources_cache by `run`: every file goes to access_20261110/staging/ (passing files in the folder itself,
failed in rejected/, identity-unverified in unverified/) with a .source.json sidecar. No model calls, no logins or cookies, no
workaround of a block: a 403/429, a challenge page or a login redirect stops that host and the stop is kept in access_results.json.
Network: www.ebi.ac.uk, eutils.ncbi.nlm.nih.gov, the hosts below for route c, and (through fulltext_check) api.crossref.org.
"""
import os
import argparse
import collections
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]
WS = Path(os.environ["ATLAS_WORKSPACE"])
TASK = WS / "autoresearch/tasks/dynamics_atlas_stage1_loop_20261002/outputs/scale133_20261109"
RACE, A = TASK / "race", TASK / "access_20261110"
STAGING, DROP = A / "staging", A / "drop"
RESULTS = A / "access_results.json"
CACHE = WORK / "sources_cache"
sys.path.insert(0, str(WS / ".claude/skills/verify-atlas-pipeline/scripts"))
import fulltext_check as F  # noqa: E402

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id="
API_HOSTS = {"www.ebi.ac.uk", "eutils.ncbi.nlm.nih.gov"}
# route c: repository, preprint-server and PMC hosts that appear in the OpenAlex PDF lists. Everything else is skipped, not fetched.
HOSTS_C = {"www.biorxiv.org", "biorxiv.org", "www.medrxiv.org", "medrxiv.org", "pmc.ncbi.nlm.nih.gov",
           "research-explorer.ista.ac.at", "repository.kulib.kyoto-u.ac.jp", "hal.science", "chemrxiv.org"}
CANARY_ONLY = {"10.1021/acs.biochem.4c00321": "https://mpra.ub.uni-muenchen.de/86617/1/MPRA_paper_86617.pdf"}
PDF_URL_HINT = re.compile(r"\.pdf(?:$|[?#+])|/pdf(?:/|$)|/download|/bitstreams?/|/document(?:$|[/?])|\.full\.pdf", re.I)
BIORXIV_DOI = re.compile(r"^10\.(1101|64898)/", re.I)
GAP = {"www.ebi.ac.uk": 0.4, "eutils.ncbi.nlm.nih.gov": 0.4}
GAP_DEFAULT = 2.0
MAX_BYTES = 30 * 1024 * 1024
UA = "DynamicsAtlas-access/1.0 (research; polite single-threaded fetch)"
LOGIN_URL = re.compile(r"login|signin|sign-in|shibboleth|/idp/|/auth/|captcha|challenge|cdn-cgi|cookie[-_]?consent", re.I)
CHALLENGE_BODY = re.compile(r"just a moment|cf-chl|challenge-platform|enable javascript and cookies|verify you are human|captcha|"
                            r"access denied|pardon our interruption|checking your browser|sign in to continue|institutional login|"
                            r"proof of work|preparing to download", re.I)


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def keyof(doi):
    return re.sub(r"[^A-Za-z0-9._-]+", "_", doi.replace("/", "_"))


# ---------------------------------------------------------------- network

class Refused(Exception):
    pass


class Net:
    """Serial, paced, host-guarded GET with a request log and per-host stops."""

    def __init__(self, blocks):
        self.blocks = dict(blocks)
        self.log = []
        self.last = {}
        self.cur_origin = None
        net = self

        class Hop(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, headers, newurl):
                host = urllib.parse.urlparse(newurl).hostname
                o = net.cur_origin
                if LOGIN_URL.search(newurl):
                    raise Refused(f"login/challenge redirect to {newurl[:120]}")
                if not (host == o or host.endswith("." + o) or o.endswith("." + host) or (o in API_HOSTS and host in API_HOSTS)):
                    raise Refused(f"redirect to another host: {host}")
                return super().redirect_request(req, fp, code, msg, headers, newurl)

        self.opener = urllib.request.build_opener(Hop)

    def blocked(self, host):
        return self.blocks.get(host)

    def block(self, host, why, url):
        self.blocks[host] = {"why": why, "url": url, "at": now()}

    def get(self, url, accept="*/*", cap=MAX_BYTES, route=""):
        out = self._get(url, accept, cap, route)
        if out["error"] != "host_blocked":
            self.log.append({k: out[k] for k in ("url", "host", "route", "status", "ctype", "bytes", "error")} | {"at": now()})
        return out

    def _get(self, url, accept, cap, route):
        host = urllib.parse.urlparse(url).hostname
        out = {"url": url, "host": host, "route": route, "status": None, "ctype": None, "bytes": 0, "body": b"", "error": None,
               "final_url": url}
        if self.blocked(host):
            out["error"] = "host_blocked"
            return out
        gap = GAP.get(host, GAP_DEFAULT)
        wait = self.last.get(host, 0) + gap - time.time()
        if wait > 0:
            time.sleep(wait)
        self.cur_origin = host
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
        self.last[host] = time.time()
        try:
            with self.opener.open(req, timeout=60) as r:
                out["status"], out["ctype"] = r.status, (r.headers.get("Content-Type") or "").lower()
                out["final_url"] = r.geturl()
                if r.headers.get("cf-mitigated"):
                    self.block(host, f"cf-mitigated: {r.headers.get('cf-mitigated')}", url)
                    out["error"] = "challenge"
                    return out
                length = int(r.headers.get("Content-Length") or 0)
                if length > cap:
                    out["error"] = f"too_large:{length}"
                    return out
                body = r.read(cap + 1)
                if len(body) > cap:
                    out["error"] = f"too_large:>{cap}"
                    return out
                out["body"], out["bytes"] = body, len(body)
        except urllib.error.HTTPError as e:
            out["status"], out["ctype"] = e.code, (e.headers.get("Content-Type") or "").lower()
            head = e.read(200000) if e.fp else b""
            out["bytes"] = len(head)
            if e.code in (403, 429) or (e.code in (401, 503) and CHALLENGE_BODY.search(head.decode("utf-8", "replace"))):
                self.block(host, f"HTTP {e.code}", url)
            out["error"] = f"http_{e.code}"
        except Refused as e:
            self.block(host, str(e), url)
            out["error"] = f"refused: {e}"
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
            out["error"] = f"network: {e}"
        return out


# ---------------------------------------------------------------- Europe PMC / PMC / preprint XML

def epmc_records(net, doi):
    url = EPMC + "search?" + urllib.parse.urlencode({"query": f'DOI:"{doi}"', "format": "json", "resultType": "core", "pageSize": 10})
    r = net.get(url, "application/json", route="lookup")
    if r["error"] or not r["body"]:
        return None, r
    try:
        res = json.loads(r["body"]).get("resultList", {}).get("result", [])
    except ValueError:
        return None, r
    return [x for x in res if F.norm_doi(x.get("doi")) == doi], r


def xml_to_text(raw):
    """The block-text rule of prefetch.fetch_source (article-title, title, p, table, caption, label)."""
    tree = ET.fromstring(raw)
    article = tree if tree.tag == "article" else tree.find(".//article")
    if article is None:
        raise ValueError("no article element")
    ids = {e.get("pub-id-type"): "".join(e.itertext()).strip() for e in article.findall("./front/article-meta/article-id")}
    text = "\n".join(" ".join(e.itertext()).strip() for e in tree.iter() if e.tag in ("article-title", "title", "p", "table", "caption", "label"))
    return text, ids


def fetch_xml(net, ident, route):
    """Europe PMC full-text XML of a PMCID or preprint id; PMCIDs fall back to the PMC eutils copy on 404/5xx, as prefetch does."""
    urls = [EPMC + ident + "/fullTextXML"]
    if ident.startswith("PMC"):
        urls.append(EUTILS + ident[3:])
    last = None
    for i, url in enumerate(urls):
        r = net.get(url, "application/xml", route=route)
        last = r
        if r["error"] in (None,) and r["body"]:
            try:
                text, ids = xml_to_text(r["body"])
            except (ET.ParseError, ValueError) as e:
                r["error"] = f"unreadable_xml: {e}"
                continue
            if i == 1 and ident[3:] not in {ids.get(k, "").replace("PMC", "") for k in ("pmcid", "pmc", "pmcaid")}:
                r["error"] = "eutils copy: article identity does not match the PMCID"
                continue
            if len(text) < 200:
                r["error"] = "unreadable_xml: under 200 characters"
                continue
            return r, text, ids
        if net.blocked(r["host"]):
            break
    return last, None, {}


# ---------------------------------------------------------------- staging

def stage(paper, route, ident, r, how, raw, text, ctype_ext, verdict_res, extra=None):
    """Write the file, its text and a sidecar to staging/ (or rejected/ or unverified/) and return the sidecar."""
    verdict = verdict_res["verdict"]
    folder = STAGING if verdict == "PASS" else STAGING / ("unverified" if verdict == "UNVERIFIED_IDENTITY" else "rejected")
    folder.mkdir(parents=True, exist_ok=True)
    stem = f"access_{keyof(paper['doi'])}__{route}_{keyof(ident)}"
    main = folder / f"{stem}.{ctype_ext}"
    main.write_bytes(raw)
    side = {
        "requested_doi": paper["doi"], "route": route, "source_id": ident, "source_url": r["url"], "final_url": r.get("final_url"),
        "host": r["host"], "retrieved_at": now(), "sha256": sha(raw), "bytes": len(raw), "content_type": r.get("ctype"),
        "how_obtained": how, "file": main.name, "text_file": None, "check": {"verdict": verdict, "reasons": verdict_res["reasons"]},
        "version": version_of(paper, route, r["host"]), "egress": EGRESS}
    if text is not None:
        tf = folder / f"{stem}.txt"
        tf.write_text(text)
        side["text_file"], side["text_sha256"] = tf.name, sha(text.encode())
    side.update(extra or {})
    (folder / f"{stem}.source.json").write_text(json.dumps(side, indent=1, ensure_ascii=False))
    return side


def version_of(paper, route, host):
    oa = paper.get("openalex") or {}
    inferred = {"b": "preprint (Europe PMC PPR record)", "a": "PMC deposit (accepted manuscript or published version; not stated by the XML)"}.get(route)
    if route == "c":
        inferred = "preprint (bioRxiv/medRxiv/chemRxiv host)" if re.search(r"rxiv", host) else "repository copy (version not stated)"
    return {"openalex_version": None, "openalex_note": "openalex_oa_locations.json carries no version field; OpenAlex was not queried (host not allowed)",
            "openalex_status": oa.get("status"), "inferred": inferred, "drop": "owner-supplied file; version unknown" if route == "drop" else None}


def judge_pdf(paper, raw_path, doi):
    meta = F.fetch_meta(doi, extra_title=paper.get("title"))
    return F.check_file(doi, raw_path, meta=meta)


def judge_and_stage_pdf(paper, route, ident, r, how, raw, doi=None, extra=None):
    """Check a PDF in a temp file, then stage it with its pdftotext -layout text."""
    tmp = STAGING / "_tmp_check.pdf"
    STAGING.mkdir(parents=True, exist_ok=True)
    tmp.write_bytes(raw)
    try:
        res = judge_pdf(paper, tmp, doi or paper["doi"])
        text = None
        if raw.lstrip(b"\xef\xbb\xbf").startswith(b"%PDF-"):
            p = subprocess.run([F.PDFTOTEXT, "-layout", str(tmp), "-"], capture_output=True, timeout=240)
            text = p.stdout.decode("utf-8", "replace") if p.returncode == 0 else None
    finally:
        tmp.unlink(missing_ok=True)
    side = stage(paper, route, ident, r, how, raw, text, "pdf", res, extra)
    return res, side


def attempt_xml(net, paper, route, ident, how):
    att = {"route": route, "id": ident, "url": None, "host": "www.ebi.ac.uk", "status": None, "bytes": 0, "outcome": None, "check": None, "file": None}
    r, text, ids = fetch_xml(net, ident, route)
    att.update(url=r["url"], host=r["host"], status=r["status"], bytes=r["bytes"])
    if text is None:
        att["outcome"] = r["error"] or "no_text"
        return att
    att["outcome"] = "file"
    xml_doi = F.norm_doi(ids.get("doi"))
    tmp = STAGING / "_tmp_check.txt"
    STAGING.mkdir(parents=True, exist_ok=True)
    tmp.write_text(text)
    try:
        res = F.check_file(paper["doi"], tmp, meta=F.fetch_meta(paper["doi"], extra_title=paper.get("title")), xml_text=True)
    finally:
        tmp.unlink(missing_ok=True)
    if xml_doi and xml_doi != paper["doi"]:
        res["verdict"] = "FAIL"
        res["reasons"].append("xml_doi_mismatch")
        res["measures"]["structure_only_fail"] = False
    res["text_chars"] = len(text)
    side = stage(paper, route, ident, r, how, r["body"], text, "xml", res, {"xml_doi": xml_doi or None, "text_chars": len(text)})
    att.update(check={k: res[k] for k in ("verdict", "reasons", "basis", "measures")}, file=side["file"], text_chars=len(text),
               criteria={k: v["status"] for k, v in res["criteria"].items()}, details={k: v["detail"] for k, v in res["criteria"].items() if v["status"] != "PASS"})
    return att


def attempt_pdf(net, paper, url):
    host = urllib.parse.urlparse(url).hostname
    att = {"route": "c", "id": None, "url": url, "host": host, "status": None, "bytes": 0, "outcome": None, "check": None, "file": None}
    if host not in HOSTS_C:
        att["outcome"] = "skipped: host is not a repository, preprint server or PMC host"
        return att
    if not PDF_URL_HINT.search(url):
        att["outcome"] = "skipped: link is a landing page, not a PDF"
        return att
    if net.blocked(host):
        att["outcome"] = "skipped: host stopped earlier in this project (" + net.blocked(host)["why"] + ")"
        return att
    r = net.get(url, "application/pdf", route="c")
    att.update(status=r["status"], bytes=r["bytes"])
    if r["error"]:
        att["outcome"] = r["error"]
        return att
    if "pdf" not in (r["ctype"] or ""):
        head = r["body"][:200000].decode("utf-8", "replace")
        att["outcome"] = f"not_pdf: content-type {r['ctype']}"
        if CHALLENGE_BODY.search(head) or LOGIN_URL.search(r["final_url"]):
            net.block(host, "challenge or login page instead of the PDF", url)
            att["outcome"] += "; challenge/login page, host stopped"
        return att
    att["outcome"] = "file"
    res, side = judge_and_stage_pdf(paper, "c", keyof(host), r, "OpenAlex PDF link on a repository/preprint/PMC host", r["body"])
    att.update(check={k: res[k] for k in ("verdict", "reasons", "basis", "measures")}, file=side["file"],
               criteria={k: v["status"] for k, v in res["criteria"].items()}, details={k: v["detail"] for k, v in res["criteria"].items() if v["status"] != "PASS"})
    return att


# ---------------------------------------------------------------- targets and lookups

def load_targets(stub_chars):
    openalex = {}
    for o in json.loads((A / "openalex_oa_locations.json").read_text()):
        openalex.setdefault(o["doi"], o)
    papers, by_doi = [], {}
    for f in sorted(RACE.glob("*/fulltext_manifest.json")):
        d = json.loads(f.read_text())
        for p in d["papers"]:
            stub = p["status"] == "fulltext" and p["text_chars"] < stub_chars
            if p["status"] == "fulltext" and not stub:
                continue
            kind = "stub<3000" if stub and p["text_chars"] < 3000 else "stub3000-%d" % (stub_chars - 1) if stub else "abstract_only"
            key = p["doi"] or "nodoi:" + hashlib.sha1(p["title"].encode()).hexdigest()[:10]
            if key in by_doi:
                by_doi[key]["entries"].append(d["entry"])
                if p["tier"] == "A":
                    by_doi[key]["tier"] = "A"
                continue
            rec = {"doi": p["doi"], "tier": p["tier"], "entries": [d["entry"]], "title": p["title"], "kind": kind, "text_chars": p["text_chars"],
                   "manifest_pmcid": p.get("pmcid") or "", "pmid": p.get("pmid") or "", "no_abstract": not p.get("abstract"),
                   "openalex": openalex.get(p["doi"])}
            by_doi[key] = rec
            papers.append(rec)
    return papers, openalex


def pmcids_from_urls(urls):
    out = []
    for u in urls:
        m = re.search(r"/(PMC\d+)", u, re.I) or re.search(r"ncbi\.nlm\.nih\.gov/pmc/articles/(\d+)", u)
        if m:
            out.append(m.group(1).upper() if m.group(1).upper().startswith("PMC") else "PMC" + m.group(1))
    return out


def process(net, paper, routes):
    doi = paper["doi"]
    out = {"doi": doi, "tier": paper["tier"], "entries": paper["entries"], "title": paper["title"], "kind": paper["kind"],
           "manifest_text_chars": paper["text_chars"], "no_abstract": paper["no_abstract"], "attempts": [], "lookup": None}
    if not doi:
        out["final"] = {"verdict": None, "note": "no DOI on record: no route attempted (the check needs a DOI for its metadata)"}
        return out
    recs, lk = epmc_records(net, doi) if "a" in routes or "b" in routes else (None, {})
    out["lookup"] = {"status": lk.get("status"), "error": lk.get("error"), "records": [
        {k: x.get(k) for k in ("source", "id", "pmcid", "isOpenAccess", "inEPMC", "inPMC")} for x in recs or []]}
    oa = paper["openalex"] or {}
    urls = (oa.get("pdf") or []) + (oa.get("landing") or [])
    done = False
    if "a" in routes:
        cands = []
        for x in recs or []:
            if x.get("pmcid"):
                cands.append(x["pmcid"].upper())
        cands += [paper["manifest_pmcid"].upper()] if paper["manifest_pmcid"] else []
        oa_p = pmcids_from_urls(urls)
        cands += oa_p
        for pmcid in dict.fromkeys(cands):
            how = "Europe PMC fullTextXML (PMCID " + pmcid + (" from OpenAlex link)" if pmcid in oa_p else " from DOI lookup or manifest)")
            att = attempt_xml(net, paper, "a", pmcid, how)
            att["pmcid_source"] = "openalex" if pmcid in oa_p else "europepmc/manifest"
            out["attempts"].append(att)
            if att["check"] and att["check"]["verdict"] == "PASS":
                done = True
                break
    if not done and "b" in routes and BIORXIV_DOI.match(doi):
        for x in recs or []:
            if x.get("source") == "PPR":
                att = attempt_xml(net, paper, "b", x["id"], "Europe PMC preprint fullTextXML (" + x["id"] + ")")
                if att["outcome"] and att["outcome"].startswith("http_500"):
                    time.sleep(3)
                    att = attempt_xml(net, paper, "b", x["id"], "Europe PMC preprint fullTextXML, second try after a 500")
                out["attempts"].append(att)
                if att["check"] and att["check"]["verdict"] == "PASS":
                    done = True
                    break
        if not any(a["route"] == "b" for a in out["attempts"]):
            out["attempts"].append({"route": "b", "id": None, "outcome": "no preprint record in Europe PMC for this DOI", "check": None})
    if not done and "c" in routes:
        for url in (oa.get("pdf") or []):
            att = attempt_pdf(net, paper, url)
            out["attempts"].append(att)
            if att["check"] and att["check"]["verdict"] == "PASS":
                break
    return out


def cmd_canary_wrongpaper(a):
    """The OpenAlex PDF link of 10.1021/acs.biochem.4c00321 on mpra.ub.uni-muenchen.de is a different paper (an economics archive).
    One request fetches it as a real-world wrong-paper canary; the check must not pass it. Not part of any route's counts."""
    global EGRESS
    EGRESS = F.egress_route()
    prev = json.loads(RESULTS.read_text()) if RESULTS.exists() else {}
    net = Net(prev.get("summary", {}).get("host_blocks", {}))
    out = {}
    for doi, url in CANARY_ONLY.items():
        r = net.get(url, "application/pdf", route="canary")
        rec = {"doi": doi, "url": url, "status": r["status"], "bytes": r["bytes"], "error": r["error"], "ctype": r["ctype"]}
        if not r["error"] and r["body"]:
            tmp = STAGING / "canary"
            tmp.mkdir(parents=True, exist_ok=True)
            f = tmp / "mpra_wrongpaper.pdf"
            f.write_bytes(r["body"])
            res = F.check_file(doi, f)
            rec.update(verdict=res["verdict"], reasons=res["reasons"], caught=res["verdict"] != "PASS",
                       details={k: v["detail"] for k, v in res["criteria"].items() if v["status"] != "PASS"})
        out[doi] = rec
    prev["canary_wrongpaper"] = out
    prev["canary_wrongpaper_blocks"] = net.blocks
    RESULTS.write_text(json.dumps(prev, indent=1, ensure_ascii=False))
    print(json.dumps(out, indent=1))
    return 0 if all(v.get("caught") for v in out.values()) else 1


def final_of(out):
    rank = {"PASS": 3, "UNVERIFIED_IDENTITY": 2, "FAIL": 1}
    best = None
    for a in out["attempts"] + out.get("drop_attempts", []):
        if a.get("check"):
            v = a["check"]["verdict"]
            if best is None or rank[v] > rank[best["verdict"]]:
                best = {"verdict": v, "route": a["route"], "file": a["file"], "host": a.get("host")}
    return best or out.get("final") or {"verdict": None, "note": "no file recovered"}


# ---------------------------------------------------------------- drop folder

def process_drop(papers):
    """PDFs placed by the owner, identified by their content. Originals are never moved, renamed or deleted."""
    found, results = {}, []
    pdfs = sorted(p for p in DROP.iterdir() if p.is_file() and p.suffix.lower() == ".pdf") if DROP.exists() else []
    allm = []
    for f in sorted(RACE.glob("*/fulltext_manifest.json")):
        for p in json.loads(f.read_text())["papers"]:
            allm.append((f.parent.name, p))
    for path in pdfs:
        rec = {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path.read_bytes()), "doi": None, "how_identified": None, "check": None}
        doc = F.read_pdf(path)
        if not doc.get("header_ok") or "raw" not in doc:
            rec["outcome"] = "not a readable PDF"
            results.append(rec)
            continue
        first = "\n".join(doc["raw"].split("\f")[:2]) + "\n" + doc["info"]
        dois = collections.Counter(F.norm_doi(d).rstrip(".)") for d in re.findall(r"10\.\d{4,9}/[^\s\"'<>]+", first))
        known = {F.norm_doi(p["doi"]): p for _, p in allm if p["doi"]}
        hit = [d for d, _ in dois.most_common() if d in known]
        paper = None
        if hit:
            paper, rec["how_identified"] = known[hit[0]], "DOI in the first two pages or PDF metadata"
        else:
            sq = F.squash("\n".join(doc["raw"].split("\f")[:3]))
            best = (0.0, None)
            for _, p in allm:
                toks = F.content_tokens(p["title"])
                if len(toks) >= 6:  # short generic titles ("Protein dynamics studied by NMR") match unrelated papers
                    frac = sum(t in sq for t in toks) / len(toks)
                    if frac > best[0]:
                        best = (frac, p)
            if best[1] and best[0] >= 0.95:
                paper, rec["how_identified"] = best[1], f"title match {best[0]:.0%}"
        if not paper:
            rec["outcome"] = "not identified: no known DOI in the first pages and no title match"
            results.append(rec)
            continue
        rec["doi"] = F.norm_doi(paper["doi"])
        raw = path.read_bytes()
        fake = {"url": "file://drop/" + path.name, "host": "owner drop folder", "ctype": "application/pdf"}
        target = {"doi": rec["doi"], "title": paper["title"], "openalex": None}
        res, side = judge_and_stage_pdf(target, "drop", sha(raw)[:12], fake, "owner download placed in access_20261110/drop/", raw)
        rec.update(outcome="file", check={k: res[k] for k in ("verdict", "reasons", "basis", "measures")}, file=side["file"],
                   details={k: v["detail"] for k, v in res["criteria"].items() if v["status"] != "PASS"})
        results.append(rec)
    return results


# ---------------------------------------------------------------- promote

def cmd_promote(a):
    n = 0
    for side_path in sorted(STAGING.glob("access_*.source.json")):
        side = json.loads(side_path.read_text())
        if side["check"]["verdict"] != "PASS":
            continue
        for name in (side["file"], side.get("text_file"), side_path.name):
            if not name:
                continue
            src, dst = STAGING / name, CACHE / name
            if dst.exists():
                print("exists, skipped:", dst.name)
                continue
            print(("would copy " if a.dry_run else "copy ") + name)
            if not a.dry_run:
                shutil.copy2(src, dst)
        n += 1
    print(f"{n} passing staged papers {'listed' if a.dry_run else 'copied'} (access_ prefix, sources_cache)")
    return 0


# ---------------------------------------------------------------- Edison URLs for the owner

def edison_urls(dois):
    out = collections.defaultdict(set)

    def walk(n):
        if isinstance(n, dict):
            d, u = n.get("doi"), n.get("pdf_url")
            if d and u and F.norm_doi(d) in dois:
                out[F.norm_doi(d)].add(u)
            for v in n.values():
                walk(v)
        elif isinstance(n, list):
            for v in n:
                walk(v)
    for f in sorted((WORK / "outputs/edison").glob("*.raw.json")):
        try:
            walk(json.loads(f.read_text()))
        except ValueError:
            pass
    return {k: sorted(v) for k, v in out.items()}


# ---------------------------------------------------------------- run

def summarise(results, drop, net):
    per_route = {}
    for route in ("a", "b", "c", "drop"):
        atts = [(p, x) for p in results.values() for x in (p["attempts"] if route != "drop" else [])
                if x["route"] == route]
        if route == "drop":
            atts = [(None, x) for x in drop if x.get("doi")]
        tried = {(p["doi"] if p else x["doi"]) for p, x in atts if x.get("outcome") and not str(x["outcome"]).startswith("skipped") and x["outcome"] not in ("no preprint record in Europe PMC for this DOI",)}
        got = {(p["doi"] if p else x["doi"]) for p, x in atts if x.get("outcome") == "file"}
        verdict = collections.defaultdict(set)
        for p, x in atts:
            if x.get("check"):
                verdict[x["check"]["verdict"]].add(p["doi"] if p else x["doi"])
        per_route[route] = {"papers_attempted": len(tried), "file_recovered": len(got), "pass": len(verdict["PASS"]),
                            "unverified_identity": len(verdict["UNVERIFIED_IDENTITY"]), "fail": len(verdict["FAIL"] - verdict["PASS"]),
                            "pass_rate_denominator": "papers whose route was attempted", "pass_rate": (len(verdict["PASS"]) / len(tried)) if tried else None,
                            "outcomes_without_file": dict(collections.Counter(re.sub(r"\d+", "N", str(x["outcome"]))[:70] for _, x in atts if x.get("outcome") != "file"))}
    per_host = collections.defaultdict(lambda: {"requests": 0, "status": collections.Counter(), "bytes": 0})
    for e in net.log:
        h = per_host[e["host"]]
        h["requests"] += 1
        h["status"][str(e["status"] or e["error"])] += 1
        h["bytes"] += e["bytes"] or 0
    for h in per_host.values():
        h["status"] = dict(h["status"])
    verdicts, reasons, structure_only = collections.Counter(), collections.Counter(), []
    for p in results.values():
        for x in p["attempts"]:
            if x.get("check"):
                verdicts[x["check"]["verdict"]] += 1
                reasons.update(x["check"]["reasons"])
                if x["check"]["measures"].get("structure_only_fail"):
                    structure_only.append({"doi": p["doi"], "route": x["route"], "file": x["file"]})
    return {"per_route": per_route, "per_host": dict(per_host), "host_blocks": net.blocks, "check_verdicts": dict(verdicts),
            "failure_reasons": dict(reasons), "structure_only_fails": structure_only}


EGRESS = {}


def cmd_run(a):
    global EGRESS
    EGRESS = F.egress_route()
    routes = set(a.routes.split(","))
    prev = json.loads(RESULTS.read_text()) if RESULTS.exists() else {}
    papers, openalex = load_targets(a.stub_chars)
    if a.limit:
        papers = papers[:a.limit]
    net = Net(prev.get("summary", {}).get("host_blocks", {}))
    results = {} if not a.resume else {k: v for k, v in prev.get("papers", {}).items()}
    print(f"targets {len(papers)}; routes {sorted(routes)}; egress {EGRESS}", flush=True)
    for i, paper in enumerate(papers, 1):
        key = paper["doi"] or paper["title"][:40]
        if a.resume and key in results and routes & {"a", "b", "c"}:
            continue
        if routes & {"a", "b", "c"}:
            results[key] = process(net, paper, routes)
        else:
            results[key] = prev.get("papers", {}).get(key) or {"doi": paper["doi"], "tier": paper["tier"], "entries": paper["entries"],
                                                                "title": paper["title"], "kind": paper["kind"], "attempts": [], "no_abstract": paper["no_abstract"]}
        v = final_of(results[key])
        print(f"[{i}/{len(papers)}] {paper['doi'] or '(no doi)'} tier {paper['tier']} {paper['kind']}: " + (v.get("verdict") or "no file")
              + (f" via {v['route']}" if v.get("route") else ""), flush=True)
        RESULTS.write_text(json.dumps({"generated": now(), "egress": EGRESS, "papers": results, "drop": prev.get("drop", [])}, indent=1, ensure_ascii=False))
    drop = process_drop(papers) if "drop" in routes else prev.get("drop", [])
    dropped = collections.defaultdict(list)
    for d in drop:
        if d.get("doi"):
            dropped[d["doi"]].append(d)
    for p in results.values():
        p["drop_attempts"] = [{"route": "drop", "file": d["file"], "check": d["check"], "host": "owner drop folder"} for d in dropped.get(p["doi"], []) if d.get("check")]
        p["final"] = final_of(p)
    summary = summarise(results, drop, net)
    # coverage
    groups = collections.defaultdict(lambda: collections.Counter())
    still_a = []
    for p in results.values():
        v = (p["final"] or {}).get("verdict") or "NONE"
        groups[p["kind"]][v] += 1
        if v != "PASS" and p["tier"] == "A":
            still_a.append({"doi": p["doi"], "tier": p["tier"], "entries": p["entries"], "title": p["title"], "best": v})
    summary["coverage_by_kind"] = {k: dict(v) for k, v in groups.items()}
    summary["tier_A_without_passing_text"] = still_a
    missing = {p["doi"] for p in results.values() if (p["final"] or {}).get("verdict") != "PASS" and p["doi"]}
    ed = edison_urls(missing)
    summary["edison_urls_for_owner_count"] = len(ed)
    summary["unidentified_drop_files"] = [d["file"] for d in drop if not d.get("doi")]
    RESULTS.write_text(json.dumps({"generated": now(), "egress": EGRESS, "summary": summary, "papers": results, "drop": drop,
                                   "request_log": net.log, **{k: prev[k] for k in ("canary_wrongpaper",) if k in prev}}, indent=1, ensure_ascii=False))
    lines = ["doi\ttier\tentries\ttitle\tedison_pdf_url (NOT fetched)"]
    for p in results.values():
        if p["doi"] in ed:
            lines.append(f"{p['doi']}\t{p['tier']}\t{','.join(p['entries'])}\t{p['title']}\t{' | '.join(ed[p['doi']])}")
    (A / "access_edison_urls_for_owner.tsv").write_text("\n".join(lines) + "\n")
    print(json.dumps(summary["per_route"], indent=1))
    print("coverage", json.dumps(summary["coverage_by_kind"]))
    print("blocks", json.dumps(summary["host_blocks"]))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    r = sp.add_parser("run")
    r.add_argument("--routes", default="a,b,c,drop")
    r.add_argument("--resume", action="store_true")
    r.add_argument("--limit", type=int)
    r.add_argument("--stub-chars", type=int, default=5000)
    r.set_defaults(fn=cmd_run)
    sp.add_parser("canary-wrongpaper").set_defaults(fn=cmd_canary_wrongpaper)
    p = sp.add_parser("promote")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(fn=cmd_promote)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
