# ChatGPT Pro 全仓审查 prompt

这段 prompt 要 ChatGPT Pro 审查整个 private repo、已合并 PR #19 和当前 Draft PR #20。重点是判断仓库实际证明了什么、PR #20 是否应合并、哪些入口应继续保留，以及下一科学 milestone 应进入 H1 broad Rule release 还是 independently curated new/held-out case。

它把多模型 proposal transport、无 Agent common-flow regression 和 Luna active Rule closure 分开，要求审查者直接指出错误 claim 和具体修改位置。预期回复包含一个明确 Decision、逐项 claim 核验、仓库分层、PR #20 修改项和三个带 exit gate 的下一阶段。

```text
### Goal
Audit the complete current Dynamics Atlas Harness repository and Draft PR #20, then decide the smallest truthful repository changes and the next scientific milestone.

### Repository identity
- Private repository: https://github.com/alex051107/dynamics-atlas-harness
- Current main: da584173ee64bfad9854132a3418ed1e871c69f5
- Merged PR #19: https://github.com/alex051107/dynamics-atlas-harness/pull/19
- Current Draft PR #20: https://github.com/alex051107/dynamics-atlas-harness/pull/20
- PR #20 base: da584173ee64bfad9854132a3418ed1e871c69f5
- Treat the current PR #20 head, CI, files, and merge state from GitHub metadata as authoritative.
- If this private repository is unavailable to you, return DATA_INSUFFICIENT and list the exact files or archive needed. Do not reconstruct missing code or artifacts from this prompt.

### Stable project authority
The project has four linked goals.
G1 studies which quantities are reliable across heterogeneous protein-dynamics evidence.
G2 studies cross-modal conformational-landscape comparability.
G3 turns verified methods, inputs, contracts, provenance, execution, and review into a reusable harness.
G4 tests whether a constrained Agent reduces routine work without increasing unsafe scientific claims.
G4 may fail and must not replace G1 or G2. Human/domain reviewers own molecule/condition/comparability decisions, new scientific methods, Rule or threshold release, and final scientific judgment.

### Current canonical runtime
scientific question + declared sources + declared data
-> recorded or live Profile proposal
-> deterministic admission
-> RuleInstances and unresolved obligations
-> legal action cards
-> recorded or live Planner proposal
-> deterministic authorization
-> direct evaluation / exact lookup / registered computation / stop
-> EvidenceResult
-> same-Rule reevaluation
-> bounded ConclusionPacket
-> human scientific review

The model may emit only Profile and Planner proposals. It never executes a scientific tool, creates a Rule, changes a threshold, registers an Operator, writes evidence, mutates RuleResults, or emits the scientific conclusion.

### Claims to verify
C1. PR #19 truthfully establishes LIVE_MODEL_PROPOSAL_TRANSPORT_V1_COMPLETE and DETERMINISTIC_COMMON_FLOW_REGRESSION_V1_COMPLETE, while its successful MiniMax HSP90 path performs one descriptive action, changes zero RuleInstances, and calculates no ConclusionPacket.
C2. PR #19 common-flow scenarios are all NO_AGENT_DETERMINISTIC_SCENARIO and therefore do not establish live-Agent coverage of direct, lookup, registered-computation, or stop routes.
C3. The PR #19 multi-model evidence is diagnostic rather than a leaderboard. Qwen 2.5 1.5B, DeepSeek v4 Flash, Luna, MiniMax M2.5, and Terra produced different fail-closed or partial results. Only MiniMax completed the PR #19 proposal-to-descriptive-action path.
C4. No PR #19 Profiler response passed both core admission and the full annotation envelope. The successful MiniMax transport reused a core-admitted Profiler proposal whose annotation diagnostic failed with UNKNOWN_STATUS_CORE_VALUE_MISMATCH.
C5. PR #20 uses RECORDED_PROFILE_LIVE_PLANNER. It does not claim a live X-EISD Profiler success.
C6. In PR #20, Luna selects XEISD_RANDOM_COMPOSITION_EXACT_LOOKUP_V1 in the card-present arm. Deterministic code executes the exact allowlisted lookup, attaches one active EvidenceResult, and changes F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION::SOURCE::xeisd_random_candidate_pool from UNRESOLVED to PASS.
C7. The PR #20 card-removed arm exposes the same frozen unresolved base state with zero legal cards. Luna returns ABSTAIN_NO_ACTION; lookup, operator, evidence, and Rule-change counts are zero.
C8. Both PR #20 arms reuse the existing X-EISD route reducer and Stage-2 reducer and terminate at ABSTAIN_OR_HUMAN_REVIEW. No real scientific SUPPORT is emitted.
C9. F04R02 deterministic engineering traceability is resolved across dossier, manifest, typed contract, trajectory, receipt, EvidenceResult, same-Rule RuleResult, and ConclusionPacket lineage. Official scientific disposition and the legacy HSP90-TIME-ANATOMY-CONTRACT-V1 alias remain human-gated.
C10. The current README has one preferred development path, while run-fixture, run-prototype, run-demo, run-smoke, run-case, older target-architecture docs, and older evidence trees are retained primarily for compatibility, regression, or historical reproduction.
C11. H1 remains PENDING_DOMAIN_REVIEW. Broad HSP90 closure, ADK dynamics portability, Agent value, transfer, production readiness, and held-out success are not established.
C12. After PR #20 review, the next scientific milestone must be either a named H1 release of one broad computable Rule or one independently curated new/held-out case. More prompt tuning or another model panel on the exposed cases would not answer the current scientific question.

### Strategic questions
S1. Classify PR #20 as PASS, CHANGES_REQUESTED_BOUNDED, or BLOCKED. Name every merge-blocking issue with an exact file and behavior. Do not request a broad rewrite when a bounded change closes the observed defect.
S2. Identify the one canonical product path and classify current commands, modules, docs, and artifact groups as KEEP_NOW, DEPRECATE_BUT_RETAIN, DELETE_ONLY_IF_BYTE_IDENTICAL_OR_SUPERSEDED, or HUMAN_ONLY_BLOCKED.
S3. Determine whether repository discoverability is sufficient after docs/DYNAMICS_ATLAS_REPOSITORY_HANDOFF_ZH.md and the README start-here links. Name any remaining duplication that could cause a new developer to run a historical path as current.
S4. Decide which next scientific milestone is evidence-ready: NAMED_H1_BROAD_RULE_RELEASE, INDEPENDENTLY_CURATED_NEW_OR_HELD_OUT_CASE, or DATA_INSUFFICIENT. State the exact admission evidence and exit gate. Do not choose another model comparison campaign as the milestone.
S5. Give the smallest three repository changes that improve scientific usefulness after PR #20. Each change must name the existing failure layer, files likely affected, validation needed, and the claim that would become newly supportable.
S6. Identify any claim in README, docs/LIVE_AGENT_COMMON_FLOWS_V1.md, docs/LIVE_AGENT_DECISION_CLOSURE_V1.md, governance/current_execution_status.json, or the workbench that is broader than the committed evidence.

### Required evidence to inspect
- README.md
- AGENTS.md
- governance/current_execution_status.json
- docs/DYNAMICS_ATLAS_REPOSITORY_HANDOFF_ZH.md
- docs/LIVE_AGENT_COMMON_FLOWS_V1.md
- docs/LIVE_AGENT_DECISION_CLOSURE_V1.md
- src/dynamics_atlas_harness/cli.py
- src/dynamics_atlas_harness/case_runner_v1.py
- src/dynamics_atlas_harness/live_agent_common_flows_v1.py
- src/dynamics_atlas_harness/live_agent_decision_closure_v1.py
- src/dynamics_atlas_harness/openrouter_proposal_transport_v1.py
- src/dynamics_atlas_harness/real_case_vertical_slice_v1.py
- src/dynamics_atlas_harness/minimal_stage2_exposed_conclusions_v1.py
- src/dynamics_atlas_harness/case_view_v1.py
- src/dynamics_atlas_harness/common_flow_scenarios_v1.py
- evidence/live_agent_common_flows_v1/development_runs/authorized_campaign_final_20260830/live_agent_campaign_manifest.json
- evidence/live_agent_common_flows_v1/development_runs/authorized_campaign_final_20260830/live_agent_development_matrix.json
- evidence/common_flow_scenarios_v1/development_runs/common_flow_scenarios_v1/common_flow_matrix.json
- evidence/live_agent_decision_closure_v1/development_runs/authorized_campaign_20260830_schema_repair1/live_agent_decision_closure_manifest_v1.json
- evidence/live_agent_decision_closure_v1/development_runs/authorized_campaign_20260830_schema_repair1/paired_arm_matrix.json
- review/live_agent_decision_closure_v1/index.html
- tests for live-agent common flows, decision closure, common-flow scenarios, governance, CaseView, workbench, and clean-checkout behavior
- GitHub PR #19 and PR #20 commits, file diffs, reviews, and CI metadata

### Output contract
Start with exactly one Decision: PASS | CHANGES_REQUESTED_BOUNDED | BLOCKED.

For C1-C12, return a table with exactly one label per claim:
- VERIFIED <file, artifact, commit, or GitHub metadata>
- WRONG <corrected claim and evidence>
- DATA_INSUFFICIENT <missing evidence>

Then provide:
1. Canonical runtime map, with current and historical paths separated.
2. KEEP_NOW / DEPRECATE_BUT_RETAIN / DELETE_ONLY_IF_BYTE_IDENTICAL_OR_SUPERSEDED / HUMAN_ONLY_BLOCKED list.
3. PR #20 merge blockers or the statement NO_MERGE_BLOCKER_FOUND.
4. Exact wording replacements for every overbroad claim found.
5. One selected next scientific milestone or DATA_INSUFFICIENT, with admission evidence, stop condition, and exit gate.
6. Three bounded repository changes in dependency order.
7. Allowed claim after PR #20 and forbidden upgrades.

Do not provide chain-of-thought, confidence labels, model scores, or a model leaderboard. Do not treat CI, internal subagent review, static HTML, a proposal, or a synthetic fixture as scientific approval. Do not invent citations or hidden repository contents.

### Stop conditions
- All C1-C12 claims are labeled and S1-S6 are answered.
- Every requested code or artifact claim has an exact repository or GitHub locator.
- Total output is at most 2500 words.
```

收到回复后，先复核两处。第一，ChatGPT Pro 给出的 GitHub SHA、CI、文件和 artifact locator 是否真实存在。第二，它如果推荐 H1 或 held-out 路线，是否同时写明了 admission evidence、stop condition 和 claim ceiling。缺少其中一项，先不要把建议写进项目状态。
