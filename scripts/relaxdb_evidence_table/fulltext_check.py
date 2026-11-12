#!/usr/bin/env python3
"""Fulltext check: is a recovered file the right paper and a real body?

  fulltext_check.py check --doi DOI FILE      verdict for one file (.pdf, .txt, .xml, .html)
  fulltext_check.py calibrate                 the check on the 96 existing full texts, the cached PDFs and a shifted-DOI negative set
  fulltext_check.py canary                    five planted defects plus three hardening defects; every one must be caught
  fulltext_check.py anchors                   8-word windows of a PMC text that survive in pdftotext of the same paper

Verdicts: PASS, FAIL, UNVERIFIED_IDENTITY (every other criterion passes but the paper has no abstract, so identity rests on the
title alone; never counted as a pass). Criteria, with basis: title (outside, Crossref/Europe PMC title in the first three
pages), abstract (outside, one full sentence of the Europe PMC/Crossref abstract), structure (direct, Methods AND Results
headings and a reference list), length and page floors (direct), PDF header and text layer (direct), PDF metadata DOI/title
(direct), page count against the Crossref page range (outside), paywall/login/landing phrases and nav ratio (direct),
institutional-access stamps (direct).

Network: www.ebi.ac.uk and api.crossref.org only, serially, for metadata. No model calls. Metadata is cached in
verification_runs/_fulltext_meta_cache.json. Helpers imported from pipeline_common.py; nothing else is imported from the pipeline.
"""
import os
import argparse
import collections
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline_common import RACE, RUNS, W, new_run, norm_doi, write_run, write_tsv  # noqa: E402

PDFTOTEXT = "/opt/homebrew/bin/pdftotext"
PDFINFO = "/opt/homebrew/bin/pdfinfo"
PDFTOPPM = "/opt/homebrew/bin/pdftoppm"
PDFSEPARATE = "/opt/homebrew/bin/pdfseparate"
META_HOSTS = {"www.ebi.ac.uk", "api.crossref.org"}
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/"
META_CACHE = RUNS / "_fulltext_meta_cache.json"
UA = {"User-Agent": "dynamics-atlas-verify-pipeline/0.2"}

TITLE_MIN = 0.75          # share of title content words found in the first three pages (a manuscript title may spell NMR out)
SHINGLE_MIN = 0.85        # share of a sentence's 4-word windows found, when the exact sentence is not found
MIN_SENT_WORDS = 8
BODY_FLOOR = 12000        # characters of body (abstract and references removed). The 96 existing texts over 3000 characters run from 17058 (min) to 146321, median 46638, p5 21528; the floor sits below the minimum
MIN_PDF_PAGES = 3
TEXT_PER_PAGE_MIN = 300   # non-space characters per page below which a PDF has no usable text layer
PAGES_ABOVE_RANGE = 10    # a PDF longer than the Crossref range by more than this is another document
FIRST_PAGES = 3
FIRST_CHARS = 9000       # "first three pages" of a text file with no page breaks

STOP = set("the and for with from that this into over under between during their its are was were has have been not but can via using use".split())
STAMPS = [r"(?m)^\W*downloaded (?:from|by|via)\b", r"(?m)^\W*access provided by", r"by university of north carolina", r"ezproxy",
          r"unc[- ]chapel hill libraries"]
PAYWALL = ["purchase this article", "buy this article", "rent this article", "get access to the full text", "access through your institution",
           "subscribe to continue", "get full access to this article", "view all access options", "log in to read",
           "sign in to read", "only available to subscribers", "to view the full text", "full text is not available",
           "unlock this article", "you do not have access to this", "purchase access", "instant access to the full article",
           "purchase pdf", "check access", "pay per view"]
NAV = ["skip to main content", "skip to content", "sign in", "log in", "login", "create account", "register", "cookie settings",
       "accept all cookies", "we use cookies", "cookie policy", "privacy policy", "terms of use", "download pdf", "share this article",
       "cite this article", "recommended articles", "related articles", "view related", "get rights and content", "advertisement",
       "subscribe", "enable javascript", "just a moment", "verify you are human", "captcha", "access denied", "my account",
       "institutional access", "citing articles", "article metrics", "export citation", "add to cart", "terms and conditions"]

HEAD_PRE = r"^[\W_]{0,6}(?:\d{1,2}(?:\.\d{1,2})*\.?\s*|[ivx]{1,4}\.\s*)?"
RE_METHODS = re.compile(HEAD_PRE + r"(?:materials?\s*(?:and|&)\s*methods?|methods?\s*(?:and|&)\s*materials?|methods?(?:\s+and\s+experiments?)?|experimental(?:\s+(?:procedures?|section|methods?|details?))?|online\s+methods?|star\s*\W?\s*methods?|methodology)\s*[:.]?\s*$", re.I)
RE_RESULTS = re.compile(HEAD_PRE + r"(?:results?(?:\s*(?:and|&)\s*discussion)?|results\s+and\s+analysis)\s*[:.]?\s*$", re.I)
RE_REFS = re.compile(HEAD_PRE + r"(?:references?(?:\s+and\s+notes)?|bibliography|literature\s+cited|reference\s+list|cited\s+references|works\s+cited)\s*[:.]?\s*$", re.I)
REF_TAIL_LINES = 8


def run_cmd(cmd, timeout=180):
    return subprocess.run(cmd, capture_output=True, timeout=timeout)


# ---------------------------------------------------------------- egress record

def egress_route():
    """The default route interface and whether a tunnel interface with an address is up (a VPN)."""
    out = {"default_interface": None, "tunnels_up_with_address": []}
    try:
        text = run_cmd(["route", "-n", "get", "default"], 10).stdout.decode(errors="replace")
        m = re.search(r"interface:\s*(\S+)", text)
        out["default_interface"] = m.group(1) if m else None
        for name in run_cmd(["ifconfig", "-l"], 10).stdout.decode().split():
            if name.startswith("utun"):
                info = run_cmd(["ifconfig", name], 10).stdout.decode(errors="replace")
                if re.search(r"\binet6? (?!fe80)", info) and "UP" in info.split("\n")[0]:
                    out["tunnels_up_with_address"].append(name)
    except (OSError, subprocess.SubprocessError) as e:
        out["error"] = str(e)
    out["default_route_through_tunnel"] = bool(out["default_interface"] and out["default_interface"].startswith("utun"))
    return out


# ---------------------------------------------------------------- metadata (Crossref, Europe PMC)

_last_call = {}


def http_get(url, timeout=40):
    host = urllib.parse.urlparse(url).hostname
    if host not in META_HOSTS:
        raise RuntimeError(f"host not allowed in the fulltext check: {host}")
    gap = 1.0 if host == "api.crossref.org" else 0.35
    wait = _last_call.get(host, 0) + gap - time.time()
    if wait > 0:
        time.sleep(wait)
    last = None
    for attempt in range(3):
        try:
            _last_call[host] = time.time()
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (400, 403, 404):
                raise
            last = e
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = e
        time.sleep(2 * (attempt + 1))
    raise last


def plain(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def page_span(raw):
    m = re.fullmatch(r"\s*(\d+)\s*[-–]\s*(\d+)\s*", raw or "")
    if not m:
        return None
    a, b = m.group(1), m.group(2)
    if len(b) < len(a):
        b = a[:len(a) - len(b)] + b
    a, b = int(a), int(b)
    return b - a + 1 if 0 <= b - a < 400 else None


def load_meta_cache():
    try:
        return json.loads(META_CACHE.read_text())
    except (OSError, ValueError):
        return {}


def fetch_meta(doi, extra_title=None, extra_abstract=None):
    """Titles, abstracts and the page range of a DOI from Europe PMC and Crossref. Cached; errors are kept in the record."""
    doi = norm_doi(doi)
    cache = load_meta_cache()
    if doi in cache:
        meta = cache[doi]
    else:
        meta = {"doi": doi, "titles": [], "abstracts": [], "page_raw": None, "epmc": {}, "errors": []}
        try:
            reply = json.loads(http_get(EPMC + "search?" + urllib.parse.urlencode(
                {"query": f'DOI:"{doi}"', "format": "json", "resultType": "core", "pageSize": 5})))
            for r in reply.get("resultList", {}).get("result", []):
                if norm_doi(r.get("doi")) != doi:
                    continue
                if r.get("title"):
                    meta["titles"].append({"src": "europepmc", "text": plain(r["title"]).rstrip(".")})
                if r.get("abstractText"):
                    meta["abstracts"].append({"src": "europepmc", "text": plain(r["abstractText"])})
                meta["epmc"] = {k: r.get(k) for k in ("source", "id", "pmcid", "pmid", "isOpenAccess", "inEPMC", "inPMC") if r.get(k)}
                meta["page_raw"] = meta["page_raw"] or r.get("pageInfo")
                break
        except (urllib.error.URLError, RuntimeError, ValueError, TimeoutError) as e:
            meta["errors"].append(f"europepmc: {e}")
        try:
            msg = json.loads(http_get("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/()")))["message"]
            if msg.get("title"):
                meta["titles"].append({"src": "crossref", "text": plain(msg["title"][0]).rstrip(".")})
            if msg.get("abstract"):
                meta["abstracts"].append({"src": "crossref", "text": re.sub(r"^\s*abstract\s*", "", plain(msg["abstract"]), flags=re.I)})
            if msg.get("page"):
                meta["page_raw"] = msg["page"]
        except urllib.error.HTTPError as e:
            meta["errors"].append(f"crossref: HTTP {e.code}")
        except (urllib.error.URLError, RuntimeError, ValueError, TimeoutError) as e:
            meta["errors"].append(f"crossref: {e}")
        cache = load_meta_cache()
        cache[doi] = meta
        META_CACHE.parent.mkdir(parents=True, exist_ok=True)
        META_CACHE.write_text(json.dumps(cache, indent=1, ensure_ascii=False))
    meta = dict(meta)
    meta["titles"] = list(meta["titles"]) + ([{"src": "manifest", "text": extra_title}] if extra_title else [])
    meta["abstracts"] = list(meta["abstracts"]) + ([{"src": "manifest", "text": extra_abstract}] if extra_abstract else [])
    meta["page_span"] = page_span(meta.get("page_raw"))
    return meta


# ---------------------------------------------------------------- text helpers

def nfkc(s):
    return unicodedata.normalize("NFKC", s or "").lower()


def squash(s):
    return re.sub(r"[\W_]+", "", nfkc(s))


def words(s):
    s = re.sub(r"-\s*\n\s*", "", nfkc(s))
    return re.findall(r"[^\W_]+", s)


def content_tokens(title):
    toks = [t for t in words(title) if len(t) >= 3 and t not in STOP]
    return list(dict.fromkeys(toks))


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(\[])", re.sub(r"\s+", " ", text or "").strip())
    return [p for p in parts if len(words(p)) >= MIN_SENT_WORDS]


def shingles(ws, n=4):
    return {tuple(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def collapse(s):
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- reading the file

def read_pdf(path):
    path = str(path)
    head = Path(path).read_bytes()[:16]
    out = {"kind": "pdf", "header_ok": head.lstrip(b"\xef\xbb\xbf").startswith(b"%PDF-"), "pages": None, "info": "", "error": None}
    if not out["header_ok"]:
        return out
    try:
        info = run_cmd([PDFINFO, path], 60)
        xmp = run_cmd([PDFINFO, "-meta", path], 60)
        out["info"] = info.stdout.decode("utf-8", "replace") + "\n" + xmp.stdout.decode("utf-8", "replace")
        m = re.search(r"^Pages:\s+(\d+)", out["info"], re.M)
        out["pages"] = int(m.group(1)) if m else None
        lay = run_cmd([PDFTOTEXT, "-layout", path, "-"], 240)
        raw = run_cmd([PDFTOTEXT, path, "-"], 240)
        if lay.returncode != 0 and raw.returncode != 0:
            out["error"] = (lay.stderr or raw.stderr).decode(errors="replace")[:200]
            return out
        out["layout"] = lay.stdout.decode("utf-8", "replace")
        out["raw"] = raw.stdout.decode("utf-8", "replace")
    except (OSError, subprocess.SubprocessError) as e:
        out["error"] = str(e)
    return out


def read_any(path):
    p = Path(path)
    if p.suffix.lower() == ".pdf":
        return read_pdf(p)
    raw = p.read_bytes().decode("utf-8", "replace")
    if p.suffix.lower() in (".html", ".htm", ".xml"):
        raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
        raw = re.sub(r"<(?:br|/p|/div|/li|/h\d|/tr)[^>]*>", "\n", raw, flags=re.I)
        raw = html.unescape(re.sub(r"<[^>]+>", " ", raw))
        raw = re.sub(r"[ \t]+", " ", raw)
    return {"kind": "text", "raw": raw, "layout": raw, "pages": None, "info": "", "header_ok": True, "error": None}


# ---------------------------------------------------------------- criteria

def crit(status, basis, detail, **m):
    return {"status": status, "basis": basis, "detail": detail, **m}


def find_headings(text):
    lines = [l.strip() for l in text.splitlines()]
    heads = {"methods": False, "results": False, "refs_at": None, "refs_tail": 0, "refs_heading_any": False, "label_run": 0}
    for i, s in enumerate(lines):
        if not s or len(s) > 80:
            continue
        cands = [s]
        nxt = next((l for l in lines[i + 1:i + 3] if l), "")
        if len(s) < 40 and 0 < len(nxt) < 40:
            cands.append(s + " " + nxt)
        for c in cands:
            if RE_METHODS.match(c):
                heads["methods"] = True
            if RE_RESULTS.match(c):
                heads["results"] = True
        if RE_REFS.match(s):
            heads["refs_heading_any"] = True
            tail = sum(1 for l in lines[i + 1:] if l)
            if tail >= REF_TAIL_LINES:
                heads["refs_at"] = i
                heads["refs_tail"] = tail
    nums = {int(l) for l in lines if re.fullmatch(r"\d{1,3}", l)}
    n = 0
    while n + 1 in nums:
        n += 1
    heads["label_run"] = n
    return heads


def structure_of(doc):
    """Headings from reading-order text first, then from layout text split at wide gaps (two-column pages).
    "body_text" is the text whose lines the reference-heading index refers to."""
    h = find_headings(doc["raw"])
    h["body_text"] = doc["raw"]
    if not (h["methods"] and h["results"] and h["refs_at"] is not None) and doc["kind"] == "pdf":
        segs = []
        for line in doc["layout"].splitlines():
            segs.extend(re.split(r"\s{3,}", line.strip()) if line.strip() else [""])
        seg_text = "\n".join(segs)
        h2 = find_headings(seg_text)
        if h["refs_at"] is None and h2["refs_at"] is not None:
            h["refs_at"], h["refs_tail"], h["body_text"] = h2["refs_at"], h2["refs_tail"], seg_text
        h["methods"] = h["methods"] or h2["methods"]
        h["refs_heading_any"] = h["refs_heading_any"] or h2["refs_heading_any"]
        h["results"] = h["results"] or h2["results"]
    return h


def body_chars(heads, abstract_len):
    text = heads["body_text"]
    if heads["refs_at"] is not None:
        text = "\n".join(text.splitlines()[:heads["refs_at"]])
    return max(0, len(collapse(text)) - abstract_len)


def check_doc(doi, doc, meta, body_floor=None):
    """The criteria for one read file against its metadata. Returns verdict, reasons, criteria and measures."""
    floor = BODY_FLOOR if body_floor is None else body_floor
    C, reasons = {}, []

    def fail(name, detail, basis="direct", **m):
        C[name] = crit("FAIL", basis, detail, **m)
        reasons.append(name)

    def ok(name, detail, basis="direct", **m):
        C[name] = crit("PASS", basis, detail, **m)

    # format
    if doc["kind"] == "pdf":
        if not doc["header_ok"]:
            fail("pdf_header", "file does not start with %PDF-")
            return finish(C, reasons, {})
        ok("pdf_header", "%PDF- header present")
        if doc["error"] or "raw" not in doc:
            fail("pdf_readable", f"pdftotext failed: {doc['error']}")
            return finish(C, reasons, {})
        per_page = len(re.sub(r"\s", "", doc["raw"])) / max(1, doc["pages"] or 1)
        if per_page < TEXT_PER_PAGE_MIN:
            fail("no_text_layer", f"{per_page:.0f} non-space characters per page; scanned or image-only", pages=doc["pages"])
            return finish(C, reasons, {"chars_per_page": round(per_page)})
        ok("no_text_layer", f"{per_page:.0f} non-space characters per page", chars_per_page=round(per_page))
    alltext = doc["raw"] + "\n" + doc["layout"]
    low = nfkc(alltext)
    if len(re.sub(r"\s", "", doc["raw"])) < 200:
        fail("text_present", "fewer than 200 non-space characters")
        return finish(C, reasons, {})

    # institutional-access stamps
    stamp = [re.sub(r"\(\?m\)|\^|\\W\*|\(\?:|\)|\\b", "", p) for p in STAMPS if re.search(p, low)]
    (fail if stamp else ok)("access_stamp", ("access stamp found: " + ", ".join(stamp)) if stamp else "no access stamp")

    # paywall, login and landing pages
    pay = [p for p in PAYWALL if p in low]
    lines = [l.strip().lower() for l in doc["raw"].splitlines() if l.strip()]
    nav_lines = [l for l in lines if len(l) < 140 and any(n in l for n in NAV)]
    nav_distinct = {n for n in NAV if any(n in l for l in nav_lines)}
    nav_ratio = len(nav_lines) / max(1, len(lines))
    landing = len(nav_distinct) >= 4 or (nav_ratio >= 0.08 and len(nav_distinct) >= 2)
    if pay:
        fail("paywall", "paywall phrase: " + "; ".join(pay[:3]))
    else:
        ok("paywall", "no paywall phrase")
    if landing:
        fail("landing", f"{len(nav_distinct)} distinct navigation phrases ({', '.join(sorted(nav_distinct)[:5])}); nav-line ratio {nav_ratio:.2f}")
    else:
        ok("landing", f"{len(nav_distinct)} navigation phrases; nav-line ratio {nav_ratio:.2f}")

    # title in the first three pages
    if doc["kind"] == "pdf":
        rp, lp = doc["raw"].split("\f"), doc["layout"].split("\f")
        first = "\n".join(rp[:FIRST_PAGES] + lp[:FIRST_PAGES])
    else:
        first = doc["raw"][:FIRST_CHARS]
    sq_first = squash(first)
    best = (0.0, None)
    for t in meta["titles"]:
        toks = content_tokens(t["text"])
        if len(toks) >= 2:
            frac = sum(tok in sq_first for tok in toks) / len(toks)
            if frac > best[0]:
                best = (frac, t["src"])
    if not meta["titles"]:
        C["title"] = crit("UNCHECKABLE", "outside", "no title in Crossref or Europe PMC")
    elif best[0] >= TITLE_MIN:
        ok("title", f"{best[0]:.0%} of title words in the first three pages ({best[1]} title)", "outside", fraction=round(best[0], 3))
    else:
        fail("title", f"{best[0]:.0%} of title words in the first three pages (need {TITLE_MIN:.0%})", "outside", fraction=round(best[0], 3))

    # abstract sentence
    sq_all = squash(alltext)
    ws_all = words(doc["raw"])
    sh_all = shingles(words(doc["raw"])) | shingles(words(doc["layout"]))
    abstract_len, found, total, best_cov = 0, None, 0, 0.0
    for a in meta["abstracts"]:
        abstract_len = max(abstract_len, len(collapse(a["text"])))
        for s in sentences(a["text"]):
            total += 1
            sq = squash(s)
            if sq and sq in sq_all:
                found, best_cov = (a["src"], s[:80]), 1.0
                break
            sh = shingles(words(s))
            cov = sum(g in sh_all for g in sh) / len(sh) if sh else 0
            best_cov = max(best_cov, cov)
            if cov >= SHINGLE_MIN:
                found = (a["src"], s[:80])
                break
        if found:
            break
    if total == 0:
        C["abstract"] = crit("UNCHECKABLE", "outside", "the paper has no abstract in Europe PMC or Crossref")
    elif found:
        ok("abstract", f"abstract sentence found ({found[0]}): {found[1]}...", "outside", coverage=round(best_cov, 3))
    else:
        fail("abstract", f"none of {total} abstract sentences found (best word-window coverage {best_cov:.0%})", "outside", coverage=round(best_cov, 3))

    # structure and length
    heads = structure_of(doc)
    for name, key in (("structure_methods", "methods"), ("structure_results", "results")):
        (ok if heads[key] else fail)(name, f"{key} heading {'found' if heads[key] else 'not found'}")
    if heads["refs_at"] is not None:
        ok("structure_refs", f"References heading with {heads['refs_tail']} lines after it")
    elif doc.get("xml_text") and (heads["refs_heading_any"] or heads["label_run"] >= 10):
        # the Europe PMC XML-to-text rule keeps only article titles, so a converted reference list can be short or only numbers
        ok("structure_refs", f"Europe PMC XML text: References heading {'present' if heads['refs_heading_any'] else 'absent'}, numbered labels 1..{heads['label_run']}")
    else:
        fail("structure_refs", f"no References heading followed by {REF_TAIL_LINES}+ lines")
    body = body_chars(heads, abstract_len)
    (ok if body >= floor else fail)("body_length", f"body {body} characters without abstract and references (floor {floor})", body_chars=body)

    # PDF only: pages and metadata
    if doc["kind"] == "pdf":
        n = doc["pages"]
        if n is not None and n < MIN_PDF_PAGES:
            fail("pdf_pages", f"{n} pages (floor {MIN_PDF_PAGES})", pages=n)
        else:
            ok("pdf_pages", f"{n} pages", pages=n)
        span = meta.get("page_span")
        if span and n:
            if n < span or n > span + PAGES_ABOVE_RANGE:
                fail("pages_range", f"{n} PDF pages against Crossref/Europe PMC range {meta.get('page_raw')} ({span} pages)", "outside")
            else:
                ok("pages_range", f"{n} PDF pages against range {meta.get('page_raw')} ({span} pages)", "outside")
        else:
            C["pages_range"] = crit("UNCHECKABLE", "outside", "no numeric page range in Crossref or Europe PMC")
        info = doc["info"]
        fields = "\n".join(l for l in info.splitlines() if re.match(r"(Title|Subject|Keywords):", l))
        xmp = "\n".join(re.findall(r"<(?:prism:doi|pdfx:doi|crossmark:DOI|dc:identifier|prism:url)[^>]*>([^<]+)<", info, flags=re.I))
        dois = {norm_doi(d) for d in re.findall(r"10\.\d{4,9}/[^\s\"'<>]+", fields + "\n" + xmp)}
        dois = {d.rstrip(".)") for d in dois}
        target = norm_doi(doi)
        if dois and target not in dois:
            fail("pdf_meta_doi", f"PDF metadata names {sorted(dois)[:3]}, not {target}")
        elif dois:
            ok("pdf_meta_doi", "PDF metadata DOI matches")
        else:
            C["pdf_meta_doi"] = crit("UNCHECKABLE", "direct", "PDF metadata has no DOI")
        mt = re.search(r"^Title:\s*(.+)$", info, re.M)
        mtoks = content_tokens(mt.group(1)) if mt else []
        ttoks = {tok for t in meta["titles"] for tok in content_tokens(t["text"])}
        if len(mtoks) >= 4 and ttoks:
            frac = sum(tok in ttoks for tok in mtoks) / len(mtoks)
            (ok if frac >= 0.6 else fail)("pdf_meta_title", f"{frac:.0%} of the PDF metadata title words occur in the paper's title")
        else:
            C["pdf_meta_title"] = crit("UNCHECKABLE", "direct", "PDF metadata title absent or uninformative")
    return finish(C, reasons, {"body_chars": body, "nav_ratio": round(nav_ratio, 3), "pages": doc.get("pages")})


def finish(C, reasons, measures):
    measures = dict(measures, structure_only_fail=bool(reasons) and all(r.startswith("structure_") for r in reasons))
    unchecked_abstract = C.get("abstract", {}).get("status") == "UNCHECKABLE"
    if reasons:
        verdict = "FAIL"
    elif unchecked_abstract or "abstract" not in C or "title" not in C or C["title"]["status"] != "PASS":
        verdict = "UNVERIFIED_IDENTITY"
    else:
        verdict = "PASS"
    basis = "outside" if verdict == "PASS" else "direct"
    return {"verdict": verdict, "basis": basis, "reasons": reasons, "criteria": C, "measures": measures}


def check_file(doi, path, meta=None, body_floor=None, xml_text=False, **meta_hint):
    """xml_text: the file is the Europe PMC/PMC XML converted to text (reference lists are not in it)."""
    meta = meta or fetch_meta(doi, **meta_hint)
    doc = read_any(path)
    doc["xml_text"] = xml_text
    res = check_doc(doi, doc, meta, body_floor)
    res["file"] = str(path)
    res["doi"] = norm_doi(doi)
    return res


# ---------------------------------------------------------------- commands

def manifest_papers():
    out = []
    for f in sorted(RACE.glob("*/fulltext_manifest.json")):
        d = json.loads(f.read_text())
        for p in d["papers"]:
            out.append((d["entry"], p))
    return out


def one_line(res):
    bad = [f"{k}: {v['detail']}" for k, v in res["criteria"].items() if v["status"] == "FAIL"]
    return res["verdict"] + (" | " + " | ".join(bad)[:400] if bad else "")


def cmd_check(a):
    res = check_file(a.doi, a.file)
    print(json.dumps(res, indent=1, ensure_ascii=False) if a.json else one_line(res))
    return 0 if res["verdict"] == "PASS" else 1


def calibrate_sets():
    cache = W / "sources_cache"
    texts = []
    for entry, p in manifest_papers():
        if p["status"] == "fulltext" and p["text_chars"] >= 3000 and p.get("cache_file"):
            texts.append((entry, p["doi"], cache / p["cache_file"], p))
    pdfs = []
    for f in sorted(cache.glob("10.*.pdf")):
        if re.search(r"_si\b|_SI|supp|_si_", f.name, re.I):
            continue
        doi = f.name[:-4].replace("_", "/", 1)
        pdfs.append((doi, f))
    return texts, pdfs


def tf(res):
    c = res["criteria"]
    return {"title_fraction": c.get("title", {}).get("fraction"), "abstract_coverage": c.get("abstract", {}).get("coverage")}


def cmd_calibrate(a):
    texts, pdfs = calibrate_sets()
    run = new_run("fulltext-calibrate")
    rows, bodies = [], []
    t0 = time.time()
    for entry, doi, path, p in texts:
        res = check_file(doi, path, body_floor=0, xml_text=True, extra_title=p["title"])
        bodies.append(res["measures"].get("body_chars", 0))
        rows.append({"set": "existing_text", "doi": doi, "file": path.name, "verdict": res["verdict"], "detail": one_line(res),
                     "body_chars": res["measures"].get("body_chars"), **tf(res)})
    for doi, path in pdfs:
        res = check_file(doi, path, body_floor=0)
        rows.append({"set": "cached_pdf", "doi": doi, "file": path.name, "verdict": res["verdict"], "detail": one_line(res),
                     "body_chars": res["measures"].get("body_chars"), **tf(res)})
    neg_fail = 0
    for i, (entry, doi, path, p) in enumerate(texts):
        other = texts[(i + 1) % len(texts)]
        if other[1] == doi:
            continue
        res = check_file(other[1], path, body_floor=0, xml_text=True)
        neg_fail += res["verdict"] == "PASS"
        rows.append({"set": "shifted_doi_negative", "doi": other[1], "file": path.name, "verdict": res["verdict"],
                     "detail": one_line(res), "body_chars": res["measures"].get("body_chars"), **tf(res)})
    write_tsv(run.run_dir / "calibration.tsv", rows, ["set", "doi", "file", "verdict", "detail", "body_chars", "title_fraction", "abstract_coverage"])
    bodies.sort()
    q = lambda f: bodies[int(f * (len(bodies) - 1))] if bodies else 0
    print(f"existing texts over 3000 characters: {len(texts)}; body characters min {bodies[0] if bodies else 0}, p5 {q(.05)}, p10 {q(.1)}, "
          f"median {q(.5)}, max {bodies[-1] if bodies else 0}")
    for s in ("existing_text", "cached_pdf", "shifted_doi_negative"):
        c = collections.Counter(r["verdict"] for r in rows if r["set"] == s)
        run.add("fulltext-calibrate", s, "INFO", "direct", dict(c))
    run.add("fulltext-calibrate", "negatives_accepted", "PASS" if neg_fail == 0 else "FAIL", "outside",
            f"{neg_fail} of {sum(r['set'] == 'shifted_doi_negative' for r in rows)} shifted-DOI texts passed")
    write_run(run, {"egress": egress_route(), "seconds": round(time.time() - t0), "body_floor_in_force": 0})
    return 0


def sips_scan(pdf, out_pdf, tmp):
    png = tmp / "page"
    run_cmd([PDFTOPPM, "-f", "1", "-l", "1", "-r", "110", "-png", str(pdf), str(png)])
    img = next(tmp.glob("page*.png"))
    run_cmd(["/usr/bin/sips", "-s", "format", "pdf", str(img), "--out", str(out_pdf)])


def landing_html(title, abstract, others, nrefs=45):
    nav = "<nav>Skip to main content | Sign in | My account | Cookie settings</nav>"
    recs = "".join(f"<li><a href='#'>{t}</a><p>{ab}</p></li>" for t, ab in others)
    refs = "".join(f"<li>{t}. J. Mol. Biol. {2000 + i % 20}, {100 + i}:{200 + i}-{210 + i}.</li>" for i, (t, _) in zip(range(nrefs), others * 8))
    return (f"<html><body>{nav}<h1>{title}</h1><h2>Abstract</h2><p>{abstract}</p><p>Keywords: relaxation; dynamics; NMR</p>"
            f"<h2>Recommended articles</h2><ul>{recs}</ul><h2>References</h2><ol>{refs}</ol>"
            f"<footer>Terms and conditions | Privacy policy | Cite this article | Download PDF</footer></body></html>")


def paywall_html(title, abstract):
    return (f"<html><body><div>Skip to main content</div><div>Access through your institution</div><h1>{title}</h1>"
            f"<p>Abstract</p><p>{abstract}</p><div>Purchase PDF - $39.95</div><div>We use cookies to help provide and enhance our service.</div>"
            f"<div>Sign in</div><div>Get full access to this article</div></body></html>")


def cmd_canary(a):
    texts, pdfs = calibrate_sets()
    run = new_run("fulltext-canary")
    tmp = run.run_dir / "tmp"
    tmp.mkdir()
    good = None
    for doi, path in pdfs:
        if check_file(doi, path)["verdict"] == "PASS":
            good = (doi, path)
            break
    other = next(((d, p) for d, p in pdfs if good and d != good[0] and read_pdf(p).get("raw") and len(read_pdf(p)["raw"]) > 5000), None)
    if not good or not other:
        run.add("fulltext", "canary base", "FAIL", "direct", "need one cached PDF that passes the check and a second PDF of another paper")
        write_run(run, {})
        return 1
    (doi_a, pdf_a), (doi_b, pdf_b) = good, other
    meta_a, meta_b = fetch_meta(doi_a), fetch_meta(doi_b)
    abs_a = max((x["text"] for x in meta_a["abstracts"]), key=len)
    title_a = meta_a["titles"][0]["text"]
    others = [(m["titles"][0]["text"], max(x["text"] for x in m["abstracts"])) for m in (fetch_meta(d) for d, _ in pdfs[:12])
              if m["titles"] and m["abstracts"] and m["doi"] != norm_doi(doi_a)][:10]
    # five planted defects (brief) and three hardening defects
    cases = []
    cases.append(("control: the real PDF", pdf_a, doi_a, "PASS", None))
    cases.append(("1 different paper under this DOI", pdf_b, doi_a, "FAIL", {"title", "abstract"}))
    (tmp / "paywall.html").write_text(paywall_html(title_a, abs_a))
    cases.append(("2 saved paywall page", tmp / "paywall.html", doi_a, "FAIL", {"paywall"}))
    (tmp / "landing.html").write_text(landing_html(title_a, abs_a, others))
    cases.append(("3 long landing page quoting title and abstract", tmp / "landing.html", doi_a, "FAIL", {"landing", "structure_methods", "structure_results"}))
    first = tmp / "page1.pdf"
    run_cmd([PDFSEPARATE, "-f", "1", "-l", "1", str(pdf_a), str(tmp / "p%d.pdf")])
    shutil.move(tmp / "p1.pdf", first)
    cases.append(("4 first page of the real PDF only", first, doi_a, "FAIL", {"pdf_pages", "body_length", "structure_methods", "structure_results"}))
    scan = tmp / "scan.pdf"
    sips_scan(pdf_a, scan, tmp)
    cases.append(("5 scanned page 1, no text layer", scan, doi_a, "FAIL", {"no_text_layer"}))
    lay = read_pdf(pdf_a)["layout"]
    (tmp / "stamped.txt").write_text("Access provided by University of North Carolina at Chapel Hill\n" + lay)
    cases.append(("6 real text with an institutional-access stamp", tmp / "stamped.txt", doi_a, "FAIL", {"access_stamp"}))
    (tmp / "notpdf.pdf").write_text(paywall_html(title_a, abs_a))
    cases.append(("7 HTML saved under a .pdf name", tmp / "notpdf.pdf", doi_a, "FAIL", {"pdf_header"}))
    noabs = dict(meta_a, abstracts=[])
    cases.append(("8 control with no abstract on record", pdf_a, doi_a, "UNVERIFIED_IDENTITY", None, noabs))
    ok_all = True
    for case in cases:
        name, path, doi, want, expect = case[:5]
        meta = case[5] if len(case) > 5 else meta_a if doi == doi_a else meta_b
        res = check_file(doi, path, meta=meta)
        if want == "FAIL":
            caught = res["verdict"] == "FAIL" and bool(expect & set(res["reasons"]))
        else:
            caught = res["verdict"] == want
        ok_all &= caught
        run.add("fulltext-canary", name, "PASS" if caught else "FAIL", "direct",
                f"expected {want}{' via ' + '/'.join(sorted(expect)) if expect else ''}; got {res['verdict']} [{', '.join(res['reasons'])}]")
    landing_body = check_doc(doi_a, read_any(tmp / "landing.html"), meta_a)["measures"].get("body_chars", 0)
    run.add("fulltext-canary", "landing page is long enough to pass the length floor on its own", "PASS" if landing_body >= BODY_FLOOR else "FAIL",
            "direct", f"landing body {landing_body} characters, floor {BODY_FLOOR}")
    ok_all &= landing_body >= BODY_FLOOR
    write_run(run, {"base_pdf": str(pdf_a), "other_pdf": str(pdf_b), "doi": doi_a, "egress": egress_route(), "floor": BODY_FLOOR})
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok_all else 1


def cmd_anchors(a):
    """8-word windows of a PMC text that appear verbatim in pdftotext of the same paper (scorer normalisation)."""
    sys.path.insert(0, str(Path.home() / "dynamics_atlas_eval/eval"))
    from common import norm_text  # noqa: E402  the scorer's own normalisation; nothing under gold is opened
    cache = W / "sources_cache"
    pairs = []  # (doi, PMC-derived text file, PDF file)
    pmc_by_doi = {}
    for sc in cache.glob("PMC*.source.json"):
        try:
            d = (json.loads(sc.read_text()).get("article_identifiers") or {}).get("doi")
        except ValueError:
            continue
        txt = sc.with_name(sc.name.replace(".source.json", ".txt"))
        if d and txt.exists() and txt.stat().st_size > 5000:
            pmc_by_doi[norm_doi(d)] = txt
    for pdf in sorted(cache.glob("10.*.pdf")):
        doi = norm_doi(pdf.name[:-4].replace("_", "/", 1))
        if doi in pmc_by_doi and not re.search(r"_si", pdf.name, re.I):
            pairs.append((doi, pmc_by_doi[doi], pdf))
    stage = Path(a.staging) if getattr(a, "staging", None) else None
    if stage and stage.exists():
        for xml_txt in sorted(stage.glob("access_*__[ab]_*.txt")):
            for pdf in stage.glob(xml_txt.name.split("__")[0] + "__c_*.pdf"):
                pairs.append((xml_txt.name.split("__")[0], xml_txt, pdf))
    rows = []
    for doi, txt, pdf in pairs:
        p = {"doi": doi}
        ref = norm_text(txt.read_text(errors="replace")).split()
        windows = {tuple(ref[i:i + 8]) for i in range(len(ref) - 7)}
        rec = {"doi": p["doi"], "pmc_windows": len(windows)}
        for mode, args in (("layout", ["-layout"]), ("raw", [])):
            pt = run_cmd([PDFTOTEXT, *args, str(pdf), "-"], 240).stdout.decode("utf-8", "replace")
            pw = norm_text(pt).split()
            have = {tuple(pw[i:i + 8]) for i in range(len(pw) - 7)}
            rec[mode + "_kept"] = round(len(windows & have) / max(1, len(windows)), 3)
            lines = [l.strip() for l in pt.splitlines() if l.strip()]
            rep = collections.Counter(lines)
            rec[mode + "_repeated_lines"] = sum(c for l, c in rep.items() if c >= 3 and len(l) < 100)
            rec[mode + "_words"] = len(pw)
        rec["pmc_words"] = len(ref)
        rows.append(rec)
    for r in rows:
        print(json.dumps(r))
    if rows:
        for mode in ("layout", "raw"):
            ks = [r[mode + "_kept"] for r in rows]
            print(f"{mode}: papers {len(rows)}, windows kept mean {sum(ks) / len(ks):.3f}, min {min(ks):.3f}, max {max(ks):.3f}")
    else:
        print("no paper has both a PMC text and a PDF in the cache")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    c = sp.add_parser("check")
    c.add_argument("--doi", required=True)
    c.add_argument("--json", action="store_true")
    c.add_argument("file")
    c.set_defaults(fn=cmd_check)
    for name, fn in (("calibrate", cmd_calibrate), ("canary", cmd_canary)):
        sp.add_parser(name).set_defaults(fn=fn)
    an = sp.add_parser("anchors")
    an.add_argument("--staging", help="also pair staged Europe PMC XML text with a staged PDF of the same DOI")
    an.set_defaults(fn=cmd_anchors)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
