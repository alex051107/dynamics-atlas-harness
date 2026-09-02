# Live Agent Decision Closure v1

## Decision

`LIVE_AGENT_DECISION_CLOSURE_V1_COMPLETE` 已在 development-only claim ceiling 内成立。

这次不是另一个 model smoke。真实 `openai/gpt-5.6-luna` Planner proposal 已经与现有 exact X-EISD lookup、
deterministic authorization、active EvidenceResult、same-Rule reevaluation 和 Stage-2 reducer 接成一条因果链。
正向臂把目标 RuleInstance 从 `UNRESOLVED` 改为 `PASS`；paired card-removed 臂由同一模型 abstain，并留下零
execution receipt。两臂的现有 reducer 终局都是 `ABSTAIN_OR_HUMAN_REVIEW`。

本轮 profile 明确标为 `RECORDED_PROFILE_LIVE_PLANNER`。没有为 X-EISD 制造 answer-bearing public Profiler packet，
也没有把 recorded canonical profile 写成 full live Profiler success。

## Repository identity

- Repository：`alex051107/dynamics-atlas-harness`
- Branch：`feature/live-agent-decision-closure-v1`
- Exact base：`da584173ee64bfad9854132a3418ed1e871c69f5`
- Base identity：PR #19 merge commit
- Frozen live-campaign checkpoint：`d0446d37184bf683671cf89aeb03f0bc0a51bee0`
- Exact delivery head：由最终 Draft PR metadata 记录；tracked 文档不写入会被自身提交立即替换的 SHA

PR #19 在合并前已收窄为：

- `LIVE_MODEL_PROPOSAL_TRANSPORT_V1_COMPLETE`
- `DETERMINISTIC_COMMON_FLOW_REGRESSION_V1_COMPLETE`
- `LIVE_AGENT_DECISION_CLOSURE_NOT_YET_ESTABLISHED`

本轮从该 bounded baseline 开始，没有把 PR #19 的 HSP90 descriptive path 或 no-Agent common-flow matrix
倒写成 active-rule live evidence。

## Canonical path

```text
recorded X-EISD profile with one declared source field removed
  -> fresh deterministic RuleResults and unresolved obligation
  -> exact current legal lookup card, or the paired card-removed state
  -> live Luna Planner proposal
  -> strict proposal admission
  -> deterministic authorization or abstention
  -> exact allowlisted repository lookup, or zero execution
  -> validated EvidenceResult
  -> same RuleInstance reevaluation
  -> existing X-EISD route packet
  -> existing Stage-2 ConclusionPacket
  -> CaseView
  -> static read-only workbench
```

模型只能返回 `SELECT_ACTIONS` 与当前合法 card ID，或者 `ABSTAIN_NO_ACTION`。它不能决定 lookup ID、locator、
field update、Rule status、downstream dependencies 或 terminal disposition。

## Model, transport, credential, and cost

| Item | Observed result |
|---|---|
| Model | `openai/gpt-5.6-luna` |
| Provider | exact OpenAI provider through existing OpenRouter transport |
| Reasoning | low |
| Output contract | strict JSON Schema, no tools |
| Hosted tools / function execution | none |
| Automatic retries | 0 |
| Frozen max output tokens | 4096 |
| HTTP attempts | 3 |
| Completed calls | 2 |
| Completed-call provider-reported cost | USD 0.00072385 |
| Campaign cap | USD 1.00; 6 attempts; 4 completed calls |
| Campaign state | `CLOSED_FROZEN` |
| Semantic prompt tuning | 0 |
| Held-out access | none |

第一次 request 在任何 generation 前收到 HTTP 400：OpenAI strict-schema endpoint 不接受
`selected_card_ids.uniqueItems`。该 response 没有 response ID、usage 或 provider-reported cost。唯一一次获准的
schema compatibility repair 只把 provider-facing schema 归一到其 strict subset；冻结 prompt、visible input、
proposal semantics 和 deterministic uniqueness check 均未改变。失败 request/raw response/receipt 与 repair
receipt 均被保留。随后两个 paired arms 各完成一次，没有再调用其他模型。

Credential 由获准的本机 Excel Benchmark secret loader 注入 inherited environment。key 值没有被打印、记录、
hash、写入 artifact 或提交，也没有扫描 shell history、keychain、home directory 或无关 repository。

## Profiler result

`RECORDED_PROFILE_LIVE_PLANNER`

这轮没有 live Profiler call。原因是仓库已有可重算的 X-EISD canonical profile 和 exact lookup contract，但没有一个
既 answer-blind 又满足完整 annotation envelope 的 X-EISD public Profiler packet。使用 recorded profile 保留了
源字段、Rule applicability 和 lookup target 的既有身份，同时让实验只检验 live Planner 到 active evidence 的缺口。

允许的 claim 是 live Planner decision closure。禁止写成 `FULL_PROFILER_ENVELOPE_PASS` 或 end-to-end live
Profiler + Planner closure。

## Paired Planner result

| Arm | Visible legal cards | Luna proposal | Deterministic authorization | Execution | Target Rule | Existing reducer |
|---|---:|---|---|---|---|---|
| `XEISD_LOOKUP_CARD_PRESENT` | 1 exact lookup card | `SELECT_ACTIONS` | `AUTHORIZED_EXACT_ALLOWLISTED_LOOKUP` | 1 lookup; 1 EvidenceResult; 0 operator | `UNRESOLVED -> PASS` | `ABSTAIN_OR_HUMAN_REVIEW` |
| `XEISD_LOOKUP_CARD_REMOVED` | 0 | `ABSTAIN_NO_ACTION` | `AUTHORIZED_ABSTENTION_ZERO_EXECUTION` | 0 lookup; 0 EvidenceResult; 0 operator | `UNRESOLVED -> UNRESOLVED` | `ABSTAIN_OR_HUMAN_REVIEW` |

两臂共享同一个 frozen unresolved base-state hash。card-removed input 没有 fake distractor card，也没有把 lookup
替换成另一个隐藏 action。模型看不到 expected selection、sealed reference 或 terminal verdict。

## Exact evidence route and same-Rule transition

正向臂选择：

```text
XEISD_RANDOM_COMPOSITION_EXACT_LOOKUP_V1
```

确定性 action 使用 existing allowlist：

```text
lookup_id: XEI-LOOKUP-RANDOM-DECLARATIONS
locator: XEI-M04
target: SOURCE / xeisd_random_candidate_pool
```

EvidenceResult 的 exact affected RuleInstance：

```text
F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION
::SOURCE::xeisd_random_candidate_pool
```

该 identity before/after 保持不变，status 为 `UNRESOLVED -> PASS`。fresh reevaluation 同时改变两个冻结合同中声明的
downstream dependencies：

- `F02R02_EDGE_CONDITION_COMPATIBILITY::EDGE::xeisd_random_pool_vs_j_coupling_question`
- `F06R02_EDGE_COMPARABILITY::EDGE::xeisd_random_pool_vs_j_coupling_question`

`unrelated_rule_changes=[]`。这两个 dependency transitions 来自已有 evaluation contracts，不是模型创建的 Rule、
threshold 或 effect。

## ConclusionPacket and stop arm

正向臂复用已有 `materialize_xeisd_conclusion_packet` 与 `materialize_stage2_conclusion_packet`。它没有创建新 reducer。
目标 declaration Rule 通过后，H1 source-science gate 仍未释放，因此 Stage-2 terminal disposition 正确保持：

```text
ABSTAIN_OR_HUMAN_REVIEW
```

stop 臂在 model abstention 后没有调用 lookup 或 operator，没有产生 EvidenceResult，也没有改变任何 RuleResult。
它仍通过同一 existing reducer 生成 `ABSTAIN_OR_HUMAN_REVIEW`，并有单独的 exact stop receipt。

## F04R02 engineering mapping

`ENGINEERING_TRACEABILITY_RESOLVED_HUMAN_SCIENCE_GATE_RETAINED`

F04R02 的 deterministic identity chain 现在显式连接：

```text
case dossier
  -> operator input manifest
  -> rule overlay / binding / evaluation contract / resolution policy
  -> trajectory packet
  -> operator receipt
  -> EvidenceResult
  -> same-Rule RuleResult
  -> ConclusionPacket artifact lineage
```

Validators 会 fail closed 拒绝 dossier、manifest、overlay、contract、receipt、EvidenceResult、RuleResult 或
ConclusionPacket 的跨 case／跨 identity 拼接。pre-operator RuleResult 的 `evidence_ref` 为 null；post-operator
RuleResult 精确引用同一 RuleInstance 的 EvidenceResult 与 operator receipt。

旧 `HSP90-TIME-ANATOMY-CONTRACT-V1` 没有被自动映射成 runtime contract。它保持
`PENDING_HUMAN_ALIAS_OR_DEPRECATION_DECISION`，`runtime_authority=NONE`。Official H1 disposition、legacy
alias 的科学语义和任何 broad HSP90 Rule release 仍由具名 human reviewer 决定；当前
`scientific_disposition=NOT_EVALUATED`，EvidenceResult 为 `PENDING_HUMAN_VALIDATION`。

## Canonical commands

新授权 campaign 的 canonical runtime interface：

```bash
dynamics-atlas run-agent-decision-closure \
  --campaign-config /path/to/new-authorized-decision-closure-campaign.json \
  --output-dir /tmp/dynamics-atlas-live-decision-closure
```

提交的 exact campaign 已关闭。用当前 tracked config 运行会在 credential 读取和网络前返回
`LIVE_AGENT_DECISION_CLOSURE_CAMPAIGN_CLOSED`；新输出目录不会解锁它。

重建 paired read-only workbench：

```bash
dynamics-atlas build-workbench \
  --status governance/current_execution_status.json \
  --artifact-root evidence/live_agent_decision_closure_v1/development_runs/authorized_campaign_20260830_schema_repair1/XEISD_LOOKUP_CARD_PRESENT \
  --artifact-root evidence/live_agent_decision_closure_v1/development_runs/authorized_campaign_20260830_schema_repair1/XEISD_LOOKUP_CARD_REMOVED \
  --output-dir review/live_agent_decision_closure_v1
```

Committed snapshot：`review/live_agent_decision_closure_v1/index.html`。它只读，不执行 model、lookup、Operator 或
scientific mutation。

## Validation

本地 focused integration set 同时覆盖 live decision closure、F04 typed mapping、common-flow regeneration 和 Stage-2
reducer，共运行 45 项。第一次结果为 44 pass，唯一 failure 是旧测试仍匹配宽泛错误文本；新 validator 已更早以
`invalid scientific_evaluation_status` 正确拒绝。更新 assertion 后，受影响的 Stage-2 17 项全部通过。F04 专项 10
项、governance consistency 3 项和 recorded/live comparison workbench 1 项也分别通过。

Paired workbench 已从两个 committed arm roots 重建；静态检查确认两臂、Luna/OpenAI identity、proposal、
authorization、正向 `UNRESOLVED -> PASS`、stop `ABSTAIN_NO_ACTION`、两个
`ABSTAIN_OR_HUMAN_REVIEW` ConclusionPackets 与累计 cost 均可见。

本机完整 discovery 找到 207 项：196 项直接通过，3 项 current-status/assertion drift 在本轮修复并通过各自 focused
rerun；剩余 8 项只因系统 Python 3.14 没有仓库声明的 `pymbar` 而在 import 时停止。本轮没有擅自安装 dependency。
依赖完整环境的 Python 3.11/3.12 full suite 由 Draft PR GitHub CI 对 exact merge ref 执行；其结果以 PR metadata
为准。Final delivery 另执行 clean archive smoke、secret/local-path scan 与 `git diff --check`。

## Scientific authority and claim ceiling

H1 保持 `PENDING_DOMAIN_REVIEW`。F04 official source-science disposition、public HSP90 broad Rule release、ADK
dynamics portability 和 held-out result 均未被本轮修改。

允许的 claim：一个 real Luna Planner proposal 在 development-only X-EISD paired counterfactual 中选择了 current
exact lookup；确定性代码把 evidence attach 到 exact RuleInstance，使其从 `UNRESOLVED` 变为 `PASS`，现有 reducer
生成 bounded `ABSTAIN_OR_HUMAN_REVIEW` ConclusionPacket；移除 card 后，同一模型 abstain，系统零执行并保持 Rule
unresolved。

禁止升级为：full live Profiler、live Agent 已覆盖 direct/lookup/computation/stop 四类 route、multi-card Planner utility、
Agent value、模型正确理解论文、source-science approval、scientific SUPPORT、broad HSP90 closure、ADK dynamics
portability、generalization、transfer、production readiness 或 held-out success。

下一 scientific milestone 只能是：具名 H1 reviewer 释放一个 broad computable Rule，或由独立 curator 接纳一个新／
held-out case。本轮 exposed-case prompts 和 campaign 已冻结，不再继续调参或扩 model/provider matrix。
