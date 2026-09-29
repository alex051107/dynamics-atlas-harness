"""Layer 2/3 lookup tools: keyword-overlap retrieval over a plain text file (no vector store)."""

from __future__ import annotations

import json
import math
import re
import time
from pathlib import Path

from langchain_core.tools import StructuredTool

NO_CONTENT = "无可用内容 (no content available)."
NO_MATCH = "No segment of the file matches this query."
_WORD = re.compile(r"[a-z0-9]+|[一-鿿]")
_STOP = {"the", "a", "an", "of", "and", "or", "to", "in", "is", "for", "on", "with", "at", "by", "it", "this", "that", "be", "as"}


def tokens(text: str) -> list[str]:
    return [t for t in _WORD.findall(text.lower()) if t not in _STOP and (len(t) > 1 or "一" <= t <= "鿿")]


def split_segments(text: str) -> list[str]:
    """Split at markdown headings when the file has any, else at blank lines."""
    if re.search(r"(?m)^#{1,6}\s", text):
        parts = re.split(r"(?m)^(?=#{1,6}\s)", text)
    else:
        parts = re.split(r"\n\s*\n", text)
    return [p.strip() for p in parts if p.strip()]


def rank_segments(query: str, segments: list[str]) -> list[tuple[float, str]]:
    """Score = sum of idf weights of the distinct query tokens found in the segment."""
    q = set(tokens(query))
    seg_tokens = [set(tokens(s)) for s in segments]
    n = len(segments)
    df = {t: sum(1 for st in seg_tokens if t in st) for t in q}
    scored = []
    for s, st in zip(segments, seg_tokens):
        score = sum(math.log(1 + n / df[t]) for t in q if df[t] and t in st)
        if score > 0:
            scored.append((score, s))
    scored.sort(key=lambda x: -x[0])
    return scored


def consult(path: str | None, query: str, top_k: int, max_chars: int) -> str:
    if not path or not Path(path).is_file():
        return NO_CONTENT
    text = Path(path).read_text()
    if not text.strip():
        return NO_CONTENT
    hits = rank_segments(query, split_segments(text))[:top_k]
    if not hits:
        return NO_MATCH
    return "\n\n---\n\n".join(s if len(s) <= max_chars else s[:max_chars] + " ... [segment truncated]" for _, s in hits)


def make_consult_tools(methods_file: str | None, cases_file: str | None, top_k: int = 3, max_chars: int = 2500,
                       log_path: Path | None = None) -> list[StructuredTool]:
    def build(name: str, description: str, path: str | None) -> StructuredTool:
        def run(query: str) -> str:
            out = consult(path, query, top_k, max_chars)
            if log_path is not None:
                with log_path.open("a") as f:
                    f.write(json.dumps({"tool": name, "query": query, "chars": len(out),
                                        "empty": out in (NO_CONTENT, NO_MATCH), "time": round(time.time(), 1)},
                                       ensure_ascii=False) + "\n")
            return out
        return StructuredTool.from_function(run, name=name, description=description)

    return [
        build("consult_methods", "Look up method experience: returns the few passages of the methods file most relevant to "
              "your query (keywords describing the situation or method question).", methods_file),
        build("consult_cases", "Look up stuck-point cases: returns the few worked instances of the cases file most relevant to "
              "your query (keywords describing the observation that is stuck or unexpected).", cases_file),
    ]
