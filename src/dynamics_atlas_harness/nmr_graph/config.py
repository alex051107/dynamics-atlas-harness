"""Run configuration (YAML or JSON). Relative file paths are resolved against the config file's directory."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field, fields
from pathlib import Path
from typing import Any

FILE_KEYS = ("methods_file", "cases_file", "review_prompt_file")


@dataclass
class GraphConfig:
    name: str = "custom"
    model: str = "deepseek-flash"
    base_url: str = "https://api.deepseek.com"
    api_key_env: str = "DEEPSEEK_API_KEY"
    arm: str = "A"                          # arm passed to the existing NMR tool server (tool behaviour)
    include_base_prompt: bool = True        # the existing NMR_AGENT base prompt (tool rules, finish format)
    prompt_files: list[str] = field(default_factory=list)    # layer 0, layer 1, ... concatenated after the base prompt
    methods_file: str | None = None
    cases_file: str | None = None
    review_prompt_file: str | None = None
    enable_consult_tools: bool = False
    enable_review: bool = False
    max_review_rounds: int = 2
    max_tool_calls: int = 70                # enforced by the NMR tool server; finish stays available past the cap
    result_chars: int = 6000
    consult_top_k: int = 3
    consult_max_chars: int = 2500           # per returned segment
    max_tokens: int | None = 8000
    temperature: float | None = None
    block_bmrb: list[str] = field(default_factory=list)


def load_config(path: Path) -> GraphConfig:
    path = Path(path).resolve()
    text = path.read_text()
    if path.suffix == ".json":
        raw: dict[str, Any] = json.loads(text)
    else:
        import yaml
        raw = yaml.safe_load(text) or {}
    known = {f.name for f in fields(GraphConfig)}
    unknown = set(raw) - known
    if unknown:
        raise ValueError(f"unknown config keys: {sorted(unknown)}")
    cfg = GraphConfig(**raw)

    def resolve(p: str | None) -> str | None:
        return None if p is None else str((path.parent / p).resolve() if not Path(p).is_absolute() else Path(p))

    cfg.prompt_files = [resolve(p) for p in cfg.prompt_files]
    for k in FILE_KEYS:
        setattr(cfg, k, resolve(getattr(cfg, k)))
    return cfg


def sha256_or_none(p: str | None) -> str | None:
    if not p or not Path(p).is_file():
        return None
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def file_hashes(cfg: GraphConfig) -> dict[str, dict[str, Any]]:
    """path + sha256 of every content file the config names (sha256 null when the file does not exist)."""
    out: dict[str, dict[str, Any]] = {}
    for i, p in enumerate(cfg.prompt_files):
        out[f"prompt_file_{i}"] = {"path": p, "sha256": sha256_or_none(p)}
    for k in FILE_KEYS:
        p = getattr(cfg, k)
        if p:
            out[k] = {"path": p, "sha256": sha256_or_none(p)}
    return out


def config_dict(cfg: GraphConfig) -> dict[str, Any]:
    return asdict(cfg)
