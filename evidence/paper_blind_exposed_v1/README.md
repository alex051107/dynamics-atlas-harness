# HSP90 and ADK development integration capsule

This directory contains one reproducible two-case development capsule. It starts
with public scientific questions, replays recorded fact-only Profiler and Planner
proposals, evaluates the active Draft Rules, materializes legal Planner cards from
the fresh unresolved state, runs only selected descriptive actions, and writes
human-facing abstention packets. HSP90 and ADK are exposed development cases. DHFR
is not accessed.

The two public actions have narrow roles:

- HSP90 uses a grouped observable-dependence description on the supplied 40
  trajectories. It preserves the `R46A_ES` and `R60A_GS` groups and reports
  trajectory-local PyMBAR estimates within the supplied window.
- ADK uses one non-reference G10V coordinate sample and reports its static
  reference-relative geometry against the two frozen anchor structures.

Neither action updates an active RuleResult. Both generated EvidenceResults carry
`NO_ACTIVE_RULE_EFFECT`. The existing HSP90 F04R02 same-Rule closure remains in a
separate `EXISTING_EXACT_CONTROL_REGRESSION` sidecar. It is not selected by the
public-case Planner and does not resolve the broad HSP90 NMR-to-MD question.

## What is and is not being tested

The committed Profiler and Planner JSON files are recorded proposal fixtures. The
run records them as `RECORDED_PROPOSAL_REPLAY_ONLY` and
`ANSWER_BLINDNESS_NOT_INDEPENDENTLY_VERIFIED`: the repository does not claim that
an isolated live Agent read the papers, selected the actions independently, or
understood the scientific question.

The sealed development references remain outside the public Agent-visible packet.
They are AI-authored comparison drafts, not human-approved gold standards or
source-science decisions. The reference comparison separates
`BOUNDARY_CONSISTENCY` from agent-authored content that still requires human
semantic review.

Every human packet remains:

```text
scientific_disposition = NOT_EVALUATED
source_science_review_status = PENDING_DOMAIN_REVIEW
terminal_disposition = ABSTAIN_OR_HUMAN_REVIEW
```

The capsule establishes no paper-understanding result, source-science approval,
scientific correctness, broad HSP90 Rule-to-evidence closure, ADK dynamics
portability, Agent value, or general Rules coverage.

## Reproduce the development run

Install the optional dependency group used only by this capsule:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install '.[exposed-capsule-v1]'
PYTHONPATH=src .venv/bin/python scripts/run_exposed_paper_blind_capsule_v1.py \
  --output-root /tmp/dynamics-atlas-capsule-v1
```

The runner requires an empty output directory. It verifies frozen asset identity
before a descriptive adapter runs. It refuses stale Planner references, cards that
do not address a fresh unresolved item, cross-case selections, forged Rule effects,
and selected actions with missing frozen prerequisites.

The generated `human_decision_packet.json` files list fresh active RuleResults,
descriptive EvidenceResults, the separate HSP90 control regression, unresolved
development items, and neutral resolution options. They do not rank experiments or
produce scientific support.
