# Dynamics Atlas engineering workbench v1 completion record

## Decision

Engineering workbench v1 is implemented for the two admitted exposed-development
cases. The reusable path is deterministic, recorded-replay by default, static for
review, and fail-closed on stale or cross-case references. It does not complete the
scientific gate.

`HUMAN GATE H1` remains `PENDING_DOMAIN_REVIEW`. Broad same-Rule scientific closure
is `BLOCKED_BROAD_CLOSURE` because no named official disposition exists for the nine
H1 items and the F04R02 packet-label mapping remains `DATA_INSUFFICIENT`.

## Exact repository identity

- GitHub repository: `alex051107/dynamics-atlas-harness`
- Base branch: `main`
- Exact fetched base: `03ae77efdfaabeaebbf2cf8cae5a490c15241be1`
- Delivery branch: `feature/dynamics-atlas-autonomous-engineering-v1`
- Exact review-repaired implementation head before final completion/status-only edits:
  `522fe7e2f07a5b08d0b2b73e5aa13bf7c609cdba`
- Final delivery head: the Draft PR head recorded by GitHub after this completion
  file is committed and pushed. A Git commit cannot contain its own hash; use
  `git rev-parse HEAD` or the PR metadata for the exact final delivery object.

The integrated prior work is exact and auditable:

| Prior work | Upstream commit | Integration commit | Decision |
|---|---|---|---|
| PR #16 source-review console | `75cb2a26d1ec95bfcc6936d69ce31fc6022d3c6c` | `94967ee` | integrated |
| PR #16 reviewer-schema repair | `1ee43e776d3e6e9529b1ed25a6b079335d21d48b` | `6262589` | integrated, then bounded repair |
| PR #17 concise root instructions | `055d80e0d5dfebb29d92168e456d98b18b8d8ed3` | `719c726` | integrated |

The engineering batches are `b89ca2f` (runner/provenance), `9902db5`
(H1 claim narrowing/advisory), `576be63` (CaseView/static workbench), and
`5ed99b6` (first final integrity-review repair). Exact-head re-review then found a
second bounded contract gap; `c8ab96e` binds authorization to admission/execution,
binds question and claim ceiling to the repository-backed public packet, rejects
duplicate active-evidence IDs and no-op active reevaluations, and adds an active
runner-to-CaseView round trip. Commit `d615361` then makes that repository packet
anchor mandatory for every case-run artifact and adds the full null-source downgrade
regression.

Commit `fb4bdd1` completes the same read-boundary repair by enforcing the runner's
fixed manifest state (`NOT_CALCULATED_BY_CASE_RUNNER`, `NOT_EVALUATED`, and
`PENDING_DOMAIN_REVIEW`), false network/credential/transport flags, repository
binding for recorded proposals, exact proposal receipts, public-packet derivation of
the Profiler-visible input, and Planner proposal/admission reconciliation.
Commit `522fe7e` makes the three JSON transport booleans type-exact as well as
value-exact, so integers such as `0` cannot stand in for `false`.

## Implemented end-to-end path

```text
admitted public HSP90 or ADK packet
  -> recorded Profiler proposal + explicit provenance
  -> content-addressed packet, visible-input, and proposal snapshots
  -> deterministic proposal admission
  -> freshly recomputed RuleResults and unresolved obligations
  -> fresh same-case legal action cards
  -> recorded Planner proposal + explicit provenance
  -> deterministic one-card authorization or abstention
  -> exactly the authorized descriptive action, or zero actions
  -> EvidenceResult
  -> explicitly linked same-RuleInstance reevaluation only
  -> case-run manifest with no calculated terminal scientific state
  -> artifact-only CaseView
  -> four-view static review workbench
  -> blank named human/domain review template
```

Selected card IDs are the sole execution input. A stale or cross-case card fails
before action artifacts. Descriptive evidence cannot create an active Rule effect or
forge a Rule `PASS`. The current two selected actions are descriptive, so their
before/after RuleResults remain unchanged.

## Runtime commands

Run HSP90 recorded replay into a new or empty output directory:

```bash
PYTHONPATH=src python3 -m dynamics_atlas_harness run-case \
  --case-id HSP90_NTD_EXPOSED_PAPER_BLIND_V1 \
  --output-dir /tmp/dynamics-atlas-hsp90-engineering-v1
```

Run static ADK recorded replay:

```bash
PYTHONPATH=src python3 -m dynamics_atlas_harness run-case \
  --case-id ADK_EXPOSED_PORTABILITY_V1 \
  --output-dir /tmp/dynamics-atlas-adk-engineering-v1
```

Both commands require the exposed-capsule optional numerical dependencies. Importing
the core CLI or using other core commands does not eagerly import those dependencies.

## CaseView and static workbench

`build_case_view(case_or_run_root) -> CaseView` projects either a committed exposed
capsule case directory or a `run-case` output directory. It reads artifacts only. A
required missing or malformed artifact, unsafe path, cross-case ID, stale proposal
hash, stale action card, stale EvidenceResult, or mismatched RuleInstance link raises
an integrity error. Optional absence is represented as `UNAVAILABLE`; `UNKNOWN`
remains `UNKNOWN`.

Rebuild the source-science workspace and workbench from repository artifacts:

```bash
PYTHONPATH=src python3 scripts/build_source_science_review_workspace_v1.py \
  --output-dir review/source_science_v1

PYTHONPATH=src python3 scripts/render_review_console_v0.py \
  --status governance/current_execution_status.json \
  --capsule-root evidence/paper_blind_exposed_v1/development_runs/exposed_paper_blind_scientific_decision_capsule_v1 \
  --review-workspace review/source_science_v1 \
  --output-dir review_console
```

Serve the generated files locally:

```bash
python3 -m http.server 8000 --directory review_console
```

Open `http://127.0.0.1:8000/`. The four primary views are:

1. Case Overview
2. Source -> Rule -> Evidence Trace
3. Conclusion and Provenance
4. Human Review

The page distinguishes `AGENT_PROPOSAL`, `PLATFORM_ADMITTED_FACT`, `RULE_RESULT`,
`DESCRIPTIVE_EVIDENCE_NO_ACTIVE_RULE_EFFECT`, `ACTIVE_RULE_EVIDENCE`,
`EXISTING_EXACT_CONTROL_REGRESSION`, `CONCLUSION_PACKET`, and `HUMAN_REVIEW`. It has
no model call, credential handling, execution button, form submission, database,
background worker, or scientific-state mutation path. The committed
`reviewer_form.json` is a blank `DRAFT` export/template.

## Source-science reconciliation

`evidence/source_science_advisory_v1/advisory_reconciliation.json` contains all nine
F01/F02/F03/F04/F06 H1 items. Every row records the exact locator checked, atomic
source-supported statement, separately labeled project interpretation, HSP90/ADK
application, agreement/mismatch/`DATA_INSUFFICIENT`, smallest bounded repair,
advisory disposition, and unresolved human question.

The automated advisory distribution is:

- 3 `ADVISORY_APPROVE_AS_WRITTEN`
- 5 `ADVISORY_APPROVE_WITH_BOUNDED_REVISION`
- 1 `DATA_INSUFFICIENT` (`NDSR-F04R02`)

Official reviewer identity, role, date, disposition, and note remain blank. These
advisory values do not activate any Rule, Resolution Policy, Evaluation Contract,
Operator, scientific phase, or conclusion.

## Broad same-Rule closure result

Result: `BLOCKED_BROAD_CLOSURE`.

No public HSP90 or ADK obligation currently has the complete combination of named
source-science approval, confirmed applicability, frozen policy/contract, mature
case-general evidence action, validated active-Rule EvidenceResult, and same broad
RuleInstance reevaluation. The existing HSP90 F04R02 route is a separate exact
same-packet control regression. It cannot count as broad public HSP90 closure.

The smallest human/source requirements are:

1. a named H1 reviewer records complete, keyed official dispositions after checking
   the primary passages or exact case artifacts;
2. a typed mapping resolves the F04R02 overlay labels to stable dossier, manifest,
   receipt, EvidenceResult, RuleResult, and ConclusionPacket identities;
3. a later human decision explicitly releases any source-grounded Rule or next
   scientific phase.

## ADK and held-out boundaries

Current ADK is `ADK_STATIC_STRUCTURAL_CAPABILITY_EXPOSURE` and
`DYNAMIC_PORTABILITY_NOT_EVALUATED`. It contains static structural context and a
descriptive reference-relative proximity result. It has no admitted trajectory or
ensemble, topology, construct/condition package, mapping, alignment, dynamic metric,
statistical unit, or frozen dynamic output contract. No dynamic ADK route was
invented.

No DHFR or other held-out case was accessed, generated, or evaluated. No hidden gold
was added to this repository.

## Agent mode and provenance

The reproducible default is `RECORDED_PROPOSAL_REPLAY`. Profiler and Planner receipts
record canonical visible-input, parsed-proposal, and admission hashes. Provider,
model, prompt version/hash, raw-response hash, timestamp, cost, and independent
answer-blindness are explicit unavailable values when they were not recorded.

Each new run persists its public packet, Profiler-visible input, and both parsed
proposals under `inputs/`. CaseView recomputes those snapshot hashes, both receipt
visible-input hashes, both parsed-proposal hashes, both admission hashes, and the
receipt-to-manifest source-path binding before returning integrity `PASS`.

The older OpenRouter Profiler screening client remains separate. It is not imported
or called by `run-case`; no current live Planner transport exists. This task read no
credential, made no live model call, and spent no credits. Live-Agent code availability
therefore does not become an Agent-performance result.

## Validation results

Focused implementation checks completed before the final campaign:

- reusable runner: 6 tests passed;
- runner + proposal provenance + lazy CLI: 11 tests passed;
- initial CaseView + review console: 13 tests passed;
- stabilized byte-reproduction/advisory visibility repair check: 2 tests passed;
- H1 source/advisory check: the initial five-test run exposed one incorrect global
  registry assumption for case-bound F04R02; after repair, the two affected tests
  passed.

The first four-role final review found bounded integrity defects in same-Rule identity
checking, run-root proposal provenance, active-evidence classification, the published
review Schema, and the local review-template link. Commit `5ed99b6` repaired all five
and added the corresponding negative tests. The combined affected suite then ran 23
tests: `OK`.

Exact-head engineering re-review found that a mutually edited authorization copy and
manifest claim ceiling could still pass internal copy checks, and that duplicate or
no-op active reevaluations were accepted by the producer but rejected by CaseView.
Commit `c8ab96e` repaired those contracts. On that exact implementation state, all 11
CaseView tests passed; two focused active-evidence runner tests passed, including a
runner-to-CaseView round trip. The latter focused invocation used an import-only
`pymbar.timeseries` stub because the retained local Python environment no longer had
the optional PyMBAR dependency; neither test executes a numerical action path. Both
previously generated real HSP90 and ADK run roots reprojected through the repaired
CaseView with integrity `PASS`.

Authority and reproducibility re-review then showed that removing the public-packet
source path could downgrade the repository binding to internal self-consistency.
Commit `d615361` requires that safe repository-relative source for every case-run
artifact and moves the synthetic fixture to a real repository-backed packet. All 12
CaseView tests passed, including a mutually forged packet/manifest/hash plus null-source
regression; the preserved real HSP90 and ADK runs again reprojected with integrity
`PASS`.

Engineering re-review also showed that direct edits to runner-owned terminal and
human-review fields could still be projected. Commit `fb4bdd1` makes those fields and
the replay provenance contract invariant for case-run artifacts. All 16 CaseView
tests passed, including terminal/review/transport mutations, recorded-proposal source
divergence, a forged Profiler-visible input, and a Planner admission not derived from
its proposal. Both preserved real runs again projected with integrity `PASS`. A
Python 3.11 `-S` core import/CLI smoke passed with NumPy, SciPy, PyMBAR, and jsonschema
absent.

The final engineering consistency pass identified the JSON boolean `0 == false`
edge. Commit `522fe7e` closed it; the affected manifest-invariant test passed with all
three transport flags checked against both `true` and integer `0` mutations.

Fresh release validation for the prior repaired implementation commit
`5ed99b6158b483d234c13ec448d01253fb118f90` completed as follows:

- a clean Git archive full discovery ran under Python `3.14.0` with
  `numpy==2.4.3`, `scipy==1.17.1`, `pymbar==4.0.3`, and
  `jsonschema==4.26.0`: 170 tests ran, `OK`, with two expected skips that require
  the parent Dynamics Atlas workspace;
- the same clean archive installed as a core package under Python `3.11.14` with
  `--no-deps --no-build-isolation`; CLI parser/import smoke passed while NumPy,
  SciPy, PyMBAR, and jsonschema were all absent;
- the repository CI matrix now runs the full declared optional-dependency suite on
  Python 3.11 and 3.12. That exact-final-head clean-checkout matrix is the full-suite
  evidence for `522fe7e` and its completion/status commit; results belong to the Draft
  PR check readback because a committed file cannot record its own commit hash;
- both repaired `run-case` commands completed; each CaseView had integrity `PASS`,
  five content-addressed input snapshots, one descriptive EvidenceResult, zero
  active-Rule EvidenceResults, and terminal state
  `NOT_CALCULATED_BY_CASE_RUNNER`;
- all five source-review workspace files, the static HTML, and local copies of the
  blank review form and Schema regenerated from repository artifacts;
- the scoped delivery-artifact scan over the two run roots, review workspace, and
  static console found no parent-workspace absolute path, `file://`, `<script`,
  `<form`, or `fetch(` surface. A pip install target is not a delivery artifact and
  normally contains an interpreter shebang and `direct_url.json` build provenance;
- all nine official reviewer identities and dispositions remained blank;
- `git diff --check` passed.

The earlier local receipt labeled its optional-dependency interpreter as Python 3.11;
final reproducibility review identified that it was Python 3.14. The fresh results
above replace that receipt. PyMBAR emitted its standard statistical-inefficiency
caution and reported that the optional JAX acceleration package is absent; neither
message is a test failure.

## Known limitations and human-only remainder

- Official H1 is still pending.
- F04R02 traceability is still `DATA_INSUFFICIENT`.
- The runner registry contains only the two explicitly curated public development
  packets. A future case requires independent curation and explicit registry
  admission; there is no protein-name verdict branch.
- Current selected actions are descriptive and do not exercise an active broad
  same-Rule EvidenceResult in either public case.
- The runner does not calculate a terminal ConclusionPacket.
- Optional scientific routes require a repository checkout because their frozen
  `evidence/`, `registries/`, and configuration artifacts are repository-owned rather
  than wheel package data. Core installed CLI behavior is independently smoke-tested;
  full optional reproduction passed from the clean extracted Git archive with
  `PYTHONPATH=src`.
- Provider/model/prompt/raw-response/timestamp/cost provenance cannot be recovered
  from older recorded proposal files that did not store it.
- No current live Planner mode is admitted.
- Dynamic ADK portability, held-out behavior, general Rule coverage, general Operator
  routing, Agent value, transfer, production readiness, and biological correctness
  remain untested.

Human-only work is the named H1 review, F04 mapping decision, any Rule/phase release,
future public-case curation, and any later held-out authorization.

## Allowed claim and forbidden upgrade

Allowed claim: this branch implements and tests a reproducible, bounded engineering
workbench for recorded HSP90 and static-ADK development artifacts. It includes fresh
Rule-derived legal actions, exact authorization, descriptive action execution,
same-Rule attachment controls, explicit proposal provenance, an artifact-only
CaseView, a four-view static review console, and an advisory-only H1 package.

Forbidden upgrade: none of those artifacts proves source-science approval, broad
HSP90 closure, ADK dynamics portability, independent answer blindness, live-Agent
performance, semantic correctness, scientific support, biological correctness,
transfer, production readiness, or held-out performance.
