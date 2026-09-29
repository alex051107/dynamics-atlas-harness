import os
import unittest
from unittest.mock import patch

from dynamics_atlas_harness.nmr_agent import agent


class Endpoint(unittest.TestCase):
    def test_defaults_unchanged(self):
        env = {k: v for k, v in os.environ.items() if k not in (agent.BASE_URL_ENV, agent.API_KEY_ENV_ENV)}
        with patch.dict(os.environ, env, clear=True):
            self.assertEqual(agent.endpoint_url(), "https://openrouter.ai/api/v1/chat/completions")
            self.assertEqual(agent.api_key_env(), "OPENROUTER_API_KEY")
        self.assertEqual(agent.usage_cost({"cost": 0.25, "prompt_cache_hit_tokens": 5}, "deepseek-flash"), 0.25)
        self.assertEqual(agent.usage_cost({"prompt_tokens": 10}, "anthropic/claude-opus-5.5"), 0.0)

    def test_overrides(self):
        with patch.dict(os.environ, {agent.BASE_URL_ENV: "https://api.deepseek.com/chat/completions",
                                     agent.API_KEY_ENV_ENV: "DEEPSEEK_API_KEY"}):
            self.assertEqual(agent.endpoint_url(), "https://api.deepseek.com/chat/completions")
            self.assertEqual(agent.api_key_env(), "DEEPSEEK_API_KEY")

    def test_deepseek_cost_peak_and_offpeak(self):
        import time
        u = {"prompt_cache_hit_tokens": 1_000_000, "prompt_cache_miss_tokens": 1_000_000, "completion_tokens": 1_000_000}
        peak = time.strptime("2026-09-29 07:00", "%Y-%m-%d %H:%M")      # Tuesday 07 UTC
        off = time.strptime("2026-09-27 07:00", "%Y-%m-%d %H:%M")       # Sunday
        self.assertAlmostEqual(agent.usage_cost(u, "deepseek-flash", peak), 0.006 + 0.30 + 1.20)
        self.assertAlmostEqual(agent.usage_cost(u, "deepseek-flash", off), 0.003 + 0.15 + 0.60)


if __name__ == "__main__":
    unittest.main()
