# Exposed Paper-Blind Scientific Decision Capsule v1

## Outcome

This development capsule runs two exposed cases from public question and source/data
context through a fact-only Profiler proposal, current Draft Rules, a card-only
Planner proposal, selected evidence actions, and bounded human-facing packets.

Both cases finish at `ABSTAIN_OR_HUMAN_REVIEW` with
`scientific_disposition: NOT_EVALUATED`. No source-science decision, scientific
`SUPPORT`, Rule activation, Operator promotion, or portability claim was emitted.

The committed reproducible run is in
[`development_runs/exposed_paper_blind_scientific_decision_capsule_v1`](development_runs/exposed_paper_blind_scientific_decision_capsule_v1).

## Fixed scope

| Case | Role | Evidence action | Result boundary |
| --- | --- | --- | --- |
| HSP90 | Exposed development | Existing exact F04R02 directional-time-anatomy control plus new grouped sampling description | The existing control RuleInstance changes from `UNRESOLVED` to `PASS`; the public-packet cross-source claim remains unresolved. |
| ADK | Exposed portability-development | New reference-relative projection of RCSB 1E4V G10V Chain A against 1AKE/4AKE | One static non-reference sample is geometrically closer to the 1AKE reference under the declared whole-chain alignment; no dynamic, wild-type, population, kinetic, energetic, mechanistic, or portability statement is emitted. |
| DHFR | Untouched held-out candidate | None | Not accessed, searched, packetized, or run. |

The three capability categories are capped at the existing HSP90 exact control,
grouped observable sampling description, and reference-relative structural
proximity description. The latter two are development analysis adapters, not
routable Operators and not RuleResult producers.

## What the three arms show

Each case records:

1. **Arm A — development reference facts → Rules.** The reference is an isolated
   AI-authored draft marked `DEVELOPMENT_REFERENCE_DRAFT_NOT_HUMAN_APPROVED`; it is
   used only after the answer-blind run.
2. **Arm B — answer-blind Profiler facts → the same Rules.** The visible input
   excludes the sealed reference, legal actions, execution authority, and claim
   boundary. The Profiler can state facts and `UNKNOWN`s only.
3. **Arm C — full fixed capsule.** The Planner sees only produced unresolved items
   and legal card IDs. Deterministic code verifies its selection before running the
   exact HSP90 control and descriptive adapters.

The HSP90 Profiler matched the reference source identities and endpoint pair. The
ADK Profiler matched all three source identities and its one endpoint pair. Duplicate
unordered endpoint pairs are rejected before a Rules projection is created.

The Profiler's source descriptions remain unverified draft inputs. The runtime, not
the Profiler, supplies the case claim contract, evidence roles, comparison identity,
and comparison semantics used by the current Draft Rules. This prevents an Agent
from changing Rule multiplicity or authority through free-form metadata.

## Observed development results

### HSP90

- The active Draft Rules emitted 11 results: 5 `PASS`, 6 `UNRESOLVED`.
- The first blocker is NMR sample-system/composition metadata. The NMR-to-MD
  condition and forward-model bridge also remains unresolved.
- The existing exact case-bound F04R02 route preserved its identity and changed
  only that RuleInstance from `UNRESOLVED` to `PASS` after receipt and
  `EvidenceResult` validation.
- The grouped PyMBAR diagnostic retained all 40 trajectory IDs: 20 `R46A_ES` and
  20 `R60A_GS`, with within-group summaries and a separately labeled descriptive
  difference of trajectory means. It does not assess global equilibration.

### ADK

- The active Draft Rules emitted 17 results: 11 `PASS`, 6 `UNRESOLVED`.
- The first blocker is condition compatibility between the G10V static sample and
  its endpoint context.
- SciPy rigid alignment reports the G10V sample as closer to the 1AKE anchor
  (0.2488 Å) than to 4AKE (7.1087 Å), a gap of 6.8599 Å under the frozen
  whole-chain Chain A C-alpha mapping. This is reference-relative geometry for one
  static mutant sample, not an ADK dynamical result.

## Reproduction

The package declares the three exact runtime dependencies used by the capsule:

- `numpy==2.4.3`
- `pymbar==4.0.3`
- `scipy==1.17.1`

From a clean checkout:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install .
PYTHONPATH=src .venv/bin/python scripts/run_exposed_paper_blind_capsule_v1.py \
  --output-root /tmp/dynamics-atlas-capsule-v1
```

The runner refuses a nonempty output directory. Frozen input hashes are checked
before the numerical paths run. The structural adapter rejects endpoint
self-projection and a coordinate-equivalent copied endpoint, and the sampling adapter
rejects a trajectory/group row mismatch.

## Claim ceiling and next decision

This run proves a bounded development workflow can preserve answer-blind Agent
boundaries, expose real active Rule gaps, execute selected science-adjacent analyses,
reuse one existing same-Rule closure, and produce a human-review packet with concrete
blockers and next actions.

It does not establish source-science grounding, a biological HSP90 or ADK conclusion,
scientific validity of the two new adapters, Rule completeness, Agent generality, or
transfer to DHFR. The named F01/F02/F03/F04/F06 source-science review remains the
next scientific gate.
