"""LangGraph framework for the NMR science-analysis agent.

analyze (create_agent tool loop over the existing NMR MCP server + optional consult tools)
  -> review (programmatic fit inventory + one independent model call) -> conditional edge back to analyze.
Content (thinking method, requirements, method experience, stuck-point cases, review prompt) lives in
files named by the run configuration; this package contains structure only.
"""
