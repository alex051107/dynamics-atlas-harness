"""Token and cost accounting for every model call of a run (analysis and review)."""

from __future__ import annotations

import threading
from typing import Any

from langchain_core.callbacks import BaseCallbackHandler

from ..nmr_agent.agent import DEEPSEEK_PRICES, usage_cost


class UsageTracker(BaseCallbackHandler):
    """Collects the provider usage dict of every LLM call. Price table: nmr_agent.agent.DEEPSEEK_PRICES."""

    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []
        self._lock = threading.Lock()

    def on_llm_end(self, response, **kwargs: Any) -> None:
        for gens in response.generations:
            for g in gens:
                msg = getattr(g, "message", None)
                if msg is None:
                    continue
                rm = getattr(msg, "response_metadata", {}) or {}
                usage = dict(rm.get("token_usage") or {})
                um = getattr(msg, "usage_metadata", None) or {}
                if not usage and um:
                    usage = {"prompt_tokens": um.get("input_tokens", 0), "completion_tokens": um.get("output_tokens", 0)}
                model = rm.get("model_name") or rm.get("model") or "unknown"
                priced = model in DEEPSEEK_PRICES and "prompt_cache_hit_tokens" in usage
                with self._lock:
                    self.calls.append({"model": model, "usage": usage, "priced": priced,
                                       "cost_usd": usage_cost(usage, model) if priced else None})

    def summary(self) -> dict[str, Any]:
        p = sum(int(c["usage"].get("prompt_tokens") or 0) for c in self.calls)
        o = sum(int(c["usage"].get("completion_tokens") or 0) for c in self.calls)
        hit = sum(int(c["usage"].get("prompt_cache_hit_tokens") or (c["usage"].get("prompt_tokens_details") or {}).get("cached_tokens") or 0)
                  for c in self.calls)
        all_priced = bool(self.calls) and all(c["priced"] for c in self.calls)
        return {"model_calls": len(self.calls), "models_returned": sorted({c["model"] for c in self.calls}),
                "prompt_tokens": p, "completion_tokens": o, "cache_hit_tokens": hit,
                "cost_usd": round(sum(c["cost_usd"] for c in self.calls), 5) if all_priced else None,
                "cost_note": None if all_priced else "model not in the DeepSeek price table or usage lacked cache counts; tokens only"}
