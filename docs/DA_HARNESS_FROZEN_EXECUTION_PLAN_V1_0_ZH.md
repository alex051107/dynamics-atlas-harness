# Dynamics Atlas Rules Table Prototype 与 Agent Harness
## 冻结执行计划（给 Codex / Coding Agent）

**Plan ID:** `DA-HARNESS-FROZEN-PLAN-v1.0`  
**适用仓库:** `alex051107/dynamics-atlas-harness`  
**当前基线:** `target-architecture-v0.2`  
**本计划目的:** 固定下一阶段的执行顺序、对象边界、PR 拆分、验证标准、停止规则与科学 claim boundary，防止继续扩展 control-plane skeleton，却没有形成一个真正可评价的 Rules Table prototype。

---

# 0. 最高优先级指令

从本计划生效开始，不再把“增加更多架构文件”“增加更多静态 DAG 节点”或“再注册一个无关 canary”当作主要进展。

下一阶段的主线固定为：

```text
现有 review-led 方法学审计
→ 小型 Rules Prototype v1
→ rule-specific Resolution Policy
→ rule-specific Evaluation Contract
→ 一个真实 RuleInstance 路由到一个匹配 Operator
→ Operator output 回填原 obligation
→ 重新评价受影响 rule
→ 输出 bounded three-state conclusion
```

三种 prototype 终局状态固定为：

```text
SUPPORT_WITHIN_CEILING
CANNOT_SUPPORT_REQUESTED_CLAIM
ABSTAIN_OR_HUMAN_REVIEW
```

其中：

- `SUPPORT_WITHIN_CEILING`：现有 evidence 满足冻结合同，只支持到明确 claim ceiling。
- `CANNOT_SUPPORT_REQUESTED_CLAIM`：当前 dataset / evidence contract 存在明确 blocking failure，不能支持所请求层级；不等于该 biological claim 被证明为假。
- `ABSTAIN_OR_HUMAN_REVIEW`：允许的 source lookup 和 registered calculations 已完成，但 evidence 仍不足、冲突、不可比较，或需要领域判断。

所有 terminal state 在 prototype 阶段仍保留：

```text
human_final_authority = true
```

---

# 1. 当前基线：必须准确描述

当前仓库已经完成的真实路径是：

```text
existing rich X-EISD CaseGraph
→ RecordedCaseGraphProvider replay
→ deterministic CaseGraph admission
→ actual v0.3 Rules selector
→ 59 obligations
→ 15 selector unresolved inputs
→ coarse bundle Evaluation Contract
→ 16 total gaps
→ persistent RunPlan
→ 0 case-routed operators
→ RUN_PLAN_BLOCKED
```

另有：

```text
hsp90.directional_time_anatomy.v0
→ independent registered-operator canary
→ SUCCEEDED
```

但这个 HSP90 canary 没有被 X-EISD selected obligation 触发，也没有关闭 X-EISD gap。

当前已经证明：

1. rich CaseGraph 可以通过一个 future-Agent-compatible provider boundary；
2. CaseGraph admission、answer isolation、source identity 和 EvidenceEdge endpoint 检查可以运行；
3. Harness 能真实调用现有 v0.3 selector；
4. selector output 可以生成 persistent RunPlan；
5. existing analysis script 可以被包装并产生 receipt。

当前尚未证明：

1. 模型能从 raw question、papers 和 dataset 正确生成 CaseGraph；
2. review-led Rules Prototype 已被冻结；
3. selected rule 能正确选择 Operator；
4. Operator result 能回填并关闭原 obligation；
5. Rule-specific PASS / FAIL / UNRESOLVED 已实现；
6. `SUPPORT / CANNOT_SUPPORT / ABSTAIN` 已产生；
7. paper conclusion recovery、transfer 或 Agent value 已建立。

因此当前版本的准确名称是：

> `Harness Control-Plane Smoke v0.2`

不是：

- complete Agent Harness；
- complete Rules Table prototype；
- scientific conclusion engine；
- held-out validation system。

---

# 2. 不推倒现有 Rules，但重新组织其 runtime 作用

现有上游资产继续是唯一 scientific authoring authority：

```text
33-row Rule Registry
v0.3 typed bindings
v0.3 compiled rule index
existing deterministic selector
```

Harness 仓库不得复制并建立第二套 source-of-truth。

新的 Rules Prototype 使用 **overlay + manifest** 组织现有规则，而不是改写论文来源。

## 2.1 现有 review-led 资产应正式接入

本地已有：

- review-led methodology framework；
- paper portfolio mapping；
- current 33-rule re-audit；
- layered Rules Table proposal；
- executable-binding recommendations。

已有审计结果可作为起点：

```text
13 KEEP
11 MERGE
7 REVISE
2 DEFER
```

这些数字是 development audit，不自动等于 final scientific approval。Codex 必须把它们导入为可审查的 versioned overlay，而不是重新从零生成另一套结论。

## 2.2 固定七阶段方法学地图

Prototype v1 使用下面七个 reasoning stages：

```text
S1  Claim contract
S2  Native measurement
S3  Source reliability
S4  Support and forward model
S5  Cross-source roles and comparability
S6  Action / operator
S7  Evidence evaluation and claim limit
```

第二维度固定为：

```text
CASE
SOURCE
EDGE
```

两者不可混为一体。

例如：

- `S2 + SOURCE`：这份 source 实际测量什么？
- `S5 + EDGE`：两个 sources 是否比较同一 quantity，是否有 bridge，validation 是否独立？
- `S7 + CASE`：所有 blocking obligations 解决后，claim ceiling 到哪里？

---

# 3. Rules Prototype v1 的对象模型

对外仍可称为 Rules Table prototype，但 backend 必须分开以下对象。

## 3.1 Scientific Rule

回答：

> 科学上必须检查什么，为什么？

字段：

```text
rule_id
source_rule_ids
rule_family
methodology_stage
target_scope
source_passages / locators
atomic_paper_statement
reusable_review_question
why_it_matters
claim_ceiling
human_review_status
version
```

## 3.2 Applicability Binding

回答：

> 对什么 CASE / SOURCE / EDGE，在什么 typed conditions 下触发？

字段：

```text
binding_id
rule_id
scope
exact predicates
required fields
gap checks
claim scope
positive fixture
one-field negative fixture
version
```

## 3.3 Review Obligation

回答：

> 当前 case 中哪一个 target 必须回答哪项问题？

字段至少包括：

```text
obligation_id
rule_id
binding_id
target
reason_from_input
required_check
required_evidence
source_rule_trace
priority
blocking_class
claim_scope
resolution_policy_id
evaluation_contract_id
```

## 3.4 Resolution Policy

回答：

> 这项 obligation 应该怎样解决？

固定 action：

```text
DIRECT_EVALUATION
EVIDENCE_LOOKUP
REGISTERED_OPERATOR
REQUEST_NEW_DATA
HUMAN_REVIEW
```

一条 Rule 不永久一对一绑定一个 Operator。

正确关系：

```text
Rule
→ Binding
→ Obligation
→ Resolution Policy
→ zero / one / multiple possible actions
```

## 3.5 Evaluation Contract

回答：

> 哪些 EvidenceResults 构成 PASS、FAIL 或 UNRESOLVED？其 claim effect 是什么？

字段：

```text
evaluation_contract_id
obligation_family
required outputs
accepted producer types
PASS condition
FAIL condition
UNRESOLVED condition
HUMAN_REQUIRED condition
outcome_to_claim_effect
claim ceiling
human review requirement
version
```

---

# 4. Seed Rule Families

Prototype v1 不重新编译全部 33 条。

只冻结 6–8 个高价值 families，优先覆盖端到端 workflow，而不是追求表长。

建议 seed families：

1. `CLAIM_CONTRACT_AND_CEILING`
2. `SYSTEM_CONSTRUCT_CONDITION`
3. `NATIVE_OBSERVABLE_ESTIMAND`
4. `TIME_SEMANTICS_AND_STATISTICAL_UNIT`
5. `SOURCE_UNCERTAINTY_AND_SAMPLING`
6. `FORWARD_OR_PROBE_BRIDGE`
7. `CROSS_SOURCE_COMPARABILITY_AND_VALIDATION_INDEPENDENCE`
8. `NEXT_DISCRIMINATING_ACTION`

每个 family 只能在以下条件满足后进入 Prototype Active：

- 能回到 exact source locator；
- 有 reusable review question；
- 有 positive applicability fixture；
- 有 one-field negative fixture；
- required evidence 明确；
- blocking / advisory 地位明确；
- Resolution Policy 明确；
- Evaluation Contract 明确；
- claim ceiling 明确；
- human reviewer 状态明确。

---

# 5. Agent Harness 的固定目标架构

```text
Question + Papers + Data Manifest
                │
                ▼
        Profile Agent proposal
                │
        deterministic admission
                │
                ▼
       Canonical CaseWorkflow
                │
                ▼
     Frozen Rules Prototype v1
                │
        case-specific obligations
                │
                ▼
       Resolution Policy Router
      ┌─────────┼───────────┬────────────┐
      ▼         ▼           ▼            ▼
 DIRECT_EVAL  LOOKUP   REGISTERED_OP   HUMAN/NEW_DATA
      └─────────┴───────────┴────────────┘
                │
                ▼
 EvidenceResult + OperatorRunReceipt
                │
                ▼
   Rule-specific Evaluation Contract
                │
                ▼
        Claim-effect aggregation
                │
                ▼
      Bounded Conclusion Packet
                │
                ▼
             Human review
```

## 5.1 Case Graph 与 Execution DAG 分开

`CaseGraph` 表达 scientific semantics：

```text
CASE
SOURCE
EvidenceEdge
CLAIM
```

`AnalysisPlan / RunPlan` 表达 execution dependencies：

```text
load input
→ run operator
→ validate output
→ attach evidence
→ reevaluate rule
```

禁止把 DAG 执行成功写成 scientific comparison 成立。

## 5.2 Agent 权限

Profile Agent 可以：

- 解析 scientific claim；
- 枚举 sources；
- 提议 method、modality、evidence role；
- 提议 native observable、estimand、time semantics；
- 提议 EvidenceEdges；
- 保留 explicit unknown；
- 附 evidence pointers。

Profile Agent 不可以：

- 选择 Rule ID；
- 修改 rule applicability；
- 选择 terminal verdict；
- 读取 hidden reference；
- 注册 Operator；
- 把缺失字段按常识补齐。

Planner Agent 可以：

- 读取 selected obligations；
- 读取 Resolution Policies；
- 读取 live Operator Registry；
- 提议 AnalysisPlan nodes 和 execution edges；
- 选择已登记 operator candidate；
- 添加 output-validation 和 failure nodes。

Planner Agent 不可以：

- 任意写 Python；
- 安装 package；
- 调用未登记工具；
- 调整 threshold 直到得到预期结果；
- 删除 failed evidence；
- 修改 Rules。

---

# 6. 从 DataFlow-Harness 固定采用的设计

Prototype 必须保留以下原则：

1. **Persistent platform artifact**  
   Agent 不只输出一次性脚本；CaseWorkflow 与 AnalysisPlan 必须持久化。

2. **Live state retrieval**  
   Agent 每轮读取当前 canonical state、obligations、operator registry 和 plan。

3. **Typed proposal / mutation**  
   Agent 只提出结构化 change，不直接覆盖 canonical state。

4. **Validation before commitment**  
   每项 change 在写入前经过 structural、scientific-semantic 和 authority validation。

5. **Procedural Skills**  
   Operator metadata 只说明“有什么工具”；Skill 说明“怎样正确组织分析”。

6. **No semantic overclaim**  
   DAG/schema validity 只证明结构；不能代替 scientific semantic evaluation。

## 6.1 第一版不需要完整平台化

当前不建设：

- WebUI；
- multi-agent swarm；
- full MCP server；
- concurrent editing；
- generalized tool knowledge graph。

但在接真实 Agent 前，必须实现 `RVC-lite`：

```text
retrieve snapshot
→ propose typed mutation
→ validate
→ atomic commit or reject
→ append receipt
```

第一版可以继续使用：

- versioned JSON snapshots；
- append-only JSONL events；
- atomic filesystem writes。

只有出现真实并发 / 多用户需求后，再迁移 SQLite service 或完整 MCP。

---

# 7. 从 Anthropic Protein-Design Harness 固定采用的设计

这里借鉴的是 campaign harness discipline，不是指定 Claude 为 runtime model。

必须采用：

## 7.1 Constitution

新增：

```text
constitution/ATLAS_PROTOTYPE_CONSTITUTION.md
```

内容固定：

- scientific authority；
- model authority；
- allowed actions；
- forbidden actions；
- held-out boundary；
- tool registration policy；
- output validation policy；
- deviation policy；
- claim boundary。

## 7.2 Per-case Dossier

每个 case 执行前冻结：

```text
protein
organism
construct
mutation
ligand / nucleotide / cofactor
oligomeric state
condition
scientific claim
dataset identity and version
source manifest
development / validation / held-out role
```

## 7.3 Tool Roster + Canary

Operator 不能因为“有脚本”就可路由。

状态统一为：

```text
DISCOVERED
SPECIFIED
CANARY_PASS
CONTRACT_REVIEWED
ROSTER_PASS
BLOCKED
DEPRECATED
```

只有：

```text
ROSTER_PASS
```

允许被真实 case route 选择。

## 7.4 Validate actual output

每次 Operator execution 必须验证：

- 实际读取的 files；
- 实际参数；
- 实际 frame / replica / row 数；
- 实际 output files；
- output schema；
- warnings；
- package / implementation version；
- claim ceiling。

不能只相信脚本配置或 expected output list。

## 7.5 Frozen gate artifacts

保存：

```text
state/gates/rule_release_v1.json
state/gates/operator_<id>.json
state/gates/case_<id>.json
state/gates/release_candidate.json
```

## 7.6 Append-only deviation ledger

所有以下事件进入：

```text
state/deviations.jsonl
```

包括：

- threshold change；
- input substitution；
- missing package；
- operator fallback；
- manual override；
- held-out contamination；
- source mismatch；
- failed canary。

---

# 8. PR 执行顺序

所有后续修改必须通过 branch + Pull Request。不得继续直接向 `main` 提交。

---

## PR 0 — `fix/baseline-boundary-normalization`

### 目的

修复当前 baseline 中会误导后续 routing 的状态与命名问题，不改变科学结果。

### 必须完成

1. Operator lifecycle 统一。
2. `hsp90.directional_time_anatomy.v0` 从当前模糊状态改为：
   ```text
   CANARY_PASS
   ```
   在 output schema 和 scientific contract 审查完成前，不得是 routable。
3. `runplan.py` 只允许：
   ```text
   status == ROSTER_PASS
   ```
   的 Operator 被真实 gap 匹配。
4. 旧 fixture registry 与目标 registry 明确分开：
   ```text
   config/operators.json
   ```
   必须明确标为 `LEGACY_FIXTURE_ONLY`，或移动到 tests fixture scope。
5. README 第一屏明确分开：
   ```text
   CURRENT OBSERVED
   TARGET ARCHITECTURE
   ```
6. 保持 X-EISD 59 / 15 / 16 baseline 不变。

### 测试

- canary 仍可显式运行；
- canary 不可被 case plan 自动路由；
- blocked Operator 不可路由；
- only ROSTER_PASS routes；
- existing baseline integration 仍产生相同 counts。

### Exit Gate

没有任何“文档不可用但代码可路由”的 Operator 状态。

---

## PR 1 — `feature/rules-prototype-v1`

### 目的

正式把现有 review-led audit 固定成一个小型 Rules Prototype v1。

### 必须创建

```text
methodology/methodology_map_v1.json
methodology/coverage_gap_register_v1.jsonl

registries/rule_family_overlay_v1.json
registries/seed_rules_manifest_v1.json
registries/seed_bindings_v1.json
registries/resolution_policies_v1.json
registries/evaluation_contracts_v1.json

tests/rules_prototype_v1/
docs/RULES_PROTOTYPE_V1_REVIEW_PACKET.md
```

### Overlay 原则

`rule_family_overlay_v1.json` 只保存：

```text
family_id
legacy member rule IDs
audit disposition
reasoning stage
prototype status
Resolution Policy ID
Evaluation Contract ID
review state
```

不复制 source passage 形成第二套 scientific authority。

### 必须处理现有 audit

对 33 条 legacy rules 建立显式 mapping：

```text
KEEP
MERGE
REVISE
DEFER
```

并说明：

- 哪些 family 进入 seed；
- 哪些保留 legacy-only；
- 哪些需 human review；
- 哪些属于 Operator profile，不属于 reusable Rule。

### 测试

每个 seed family 至少：

- 1 positive fixture；
- 1 one-field negative fixture；
- 1 missing-evidence fixture；
- 1 wrong-target fixture；
- exact source trace；
- no duplicate family ID；
- claim ceiling present；
- Resolution Policy present；
- Evaluation Contract present。

### Exit Gate

形成 6–8 个可解释、可匹配、可评价的 seed families。

### 强制停止

PR 完成后停止。不要自动开始修改 Operator 或 Agent。输出 review packet，等待 human approval。

---

## PR 2 — `feature/gap-taxonomy-and-rule-evaluation`

### 目的

将当前 coarse bundle evaluator 改成 rule-specific Stage-2 skeleton。

### 必须完成

1. 对当前 gaps 使用固定 taxonomy：
   ```text
   SOURCE_FACT_MISSING
   COMPUTABLE_EVIDENCE_MISSING
   DATA_NOT_AVAILABLE
   SCIENTIFIC_JUDGMENT_REQUIRED
   EVALUATION_RESULT_MISSING
   METHOD_PROFILE_MISSING
   ```
2. 每个 gap 必须反链到：
   ```text
   obligation_id(s)
   rule_id
   target
   required evidence
   resolution policy
   ```
3. Obligation priority：
   ```text
   BLOCKING
   REQUIRED
   ADVISORY
   ```
4. 实现 rule-specific EvaluationResult：
   ```text
   PASS
   FAIL
   UNRESOLVED
   NOT_APPLICABLE
   HUMAN_REQUIRED
   ```
5. 实现 claim-effect：
   ```text
   NO_ADDITIONAL_RESTRICTION
   LOWER_CLAIM_CEILING
   FORBID_REQUESTED_CLAIM
   REQUIRE_HUMAN_REVIEW
   ```
6. 不能继续采用：
   ```text
   every emitted obligation is equally blocking
   ```

### 测试

- blocking FAIL → `CANNOT_SUPPORT_REQUESTED_CLAIM`；
- all blocking PASS → `SUPPORT_WITHIN_CEILING`；
- unresolved blocking → `ABSTAIN_OR_HUMAN_REVIEW`；
- advisory unresolved 不应自动阻塞所有 conclusion；
- missing EvidenceResult 与 FAIL 不混淆；
- no scientific payload interpretation beyond frozen contracts。

### Exit Gate

在 synthetic / exposed fixtures 上，三种 terminal route 都可以由冻结 contract 产生。

---

## PR 3 — `feature/hsp90-real-rule-to-operator-route`

### 目的

首次关闭一条真实的：

```text
RuleInstance
→ registered capability
→ Operator execution
→ EvidenceResult
→ rule reevaluation
```

### 选择 HSP90 的原因

- 已有 development data；
- 已有 existing analysis script；
- 已有固定 inputs；
- 组内熟悉；
- 可以用来做 development，不承担 transfer claim。

### 必须完成

1. 创建 HSP90 `CaseDossier`。
2. 创建 HSP90 canonical `CaseGraph`。
3. 冻结一个最小 MD method profile：
   ```text
   observable
   statistical unit
   time semantics
   trajectory / replica identity
   allowed descriptive claim
   forbidden kinetic / equilibrium upgrades
   ```
4. 为 `hsp90.directional_time_anatomy.v0` 完成：
   - exact output schema；
   - actual-output validation；
   - contract review；
   - status → `ROSTER_PASS`。
5. 只能在一个真实 selected obligation 的 Resolution Policy 命中时运行 Operator。
6. 删除“CLI 额外独立 canary 证明 case route”的叙述。
7. Operator output 必须写成 `EvidenceResult` 并绑定 affected obligation。
8. 只重新评价 affected RuleInstance。
9. 输出三状态结论之一，保持 descriptive claim ceiling。

### 禁止

- `if hsp90` terminal verdict；
- 让 case name 决定 Operator；
- 用 canary result 关闭不匹配 gap；
- 输出 transition rate、population、free energy、mechanism；
- 把 HSP90 当 held-out。

### Exit Gate

至少一个真实 HSP90 obligation 从：

```text
UNRESOLVED
```

转为合法的：

```text
PASS
FAIL
或 HUMAN_REQUIRED
```

并有完整 input / parameter / output receipt。

---

## PR 4 — `feature/three-route-vertical-slice`

### 目的

同一 runtime 跑通三种 route。

### Route A — Direct Evaluation

```text
已有明确 structured evidence
→ deterministic evaluation
→ bounded conclusion
```

### Route B — Registered Operator

```text
computable evidence missing
→ matching ROSTER_PASS operator
→ EvidenceResult
→ rule reevaluation
```

### Route C — Explicit Stop

```text
data unavailable
或 scientific judgment required
→ ABSTAIN / REQUEST_NEW_DATA / HUMAN_REVIEW
```

### 要求

三条 route 共用：

- same CaseWorkflow schema；
- same Rules Prototype；
- same router；
- same conclusion aggregator；
- same provenance model。

不得出现：

```text
if hsp90
if adk
if xeisd
```

### Exit Gate

生成一份完整 `ConclusionPacket`：

```text
case_id
scientific_claim
selected rules
rule results
evidence results
operator receipts
claim ceiling
terminal state
first failed dependency
human review items
full provenance
```

---

## PR 5 — `feature/rvc-lite-caseworkflow`

### 目的

在接真实 Agent 前，实现最小 DataFlow-style control protocol。

### 必须完成

1. Canonical `CaseWorkflow` 版本号。
2. `MutationEnvelope`：
   ```text
   mutation_id
   case_id
   base_version
   mutation_type
   payload
   proposed_by
   model / prompt / skill version
   ```
3. 支持：
   ```text
   PROPOSE_CASE_GRAPH_PATCH
   PROPOSE_RUN_PLAN_PATCH
   ATTACH_EVIDENCE_RESULT
   UPDATE_RULE_RESULT
   ```
4. 三类 validator：
   - structural；
   - scientific-semantic；
   - authority。
5. Atomic commit。
6. Version conflict rejection。
7. Append-only mutation / validation receipt。
8. Snapshot replay。

### 暂不做

- WebSocket；
- concurrent multi-user editing；
- full MCP deployment；
- WebUI。

### Exit Gate

```text
same state + same mutation
→ same validation
→ same committed state
```

且 invalid mutation 不产生 partial write。

---

## PR 6 — `feature/live-low-cost-profile-agent`

### 目的

用真实低成本模型替换 RecordedCaseGraphProvider。

### 输入必须 answer-blind

允许：

- scientific question；
- paper / data manifest；
- Methods；
- source-located sections；
- raw / processed data metadata；
- CaseGraph schema；
- controlled vocabulary。

禁止：

- paper conclusion；
- Discussion；
- expected graph；
- expected rules；
- expected Operator；
- hidden reference；
- terminal verdict。

### Agent 输出

```text
ProposedCaseGraphMutation
```

每个 critical field：

```text
value
evidence pointer
confidence
status
```

status：

```text
EXTRACTED
INFERRED_WITH_SUPPORT
UNKNOWN
CONFLICTING_SOURCES
HUMAN_CHECK_REQUIRED
```

### Benchmark

比较：

```text
Recorded human reference
vs
Low-cost Agent proposal
```

指标：

- source-node precision / recall；
- method accuracy；
- modality accuracy；
- evidence-role accuracy；
- EvidenceEdge accuracy；
- evidence-pointer validity；
- appropriate UNKNOWN rate；
- downstream rule agreement；
- forbidden-answer leakage；
- human correction count；
- cost / latency。

### Exit Gate

Prototype engineering threshold：

```text
critical graph fields ≥ 90%
mandatory seed-rule agreement ≥ 90%
answer leakage = 0
unsafe claim upgrade = 0
≤ 1 substantive human correction per case
```

门槛未达到时，只修 Profile prompt、vocabulary 或 validator；不能通过增加 case-specific Rule 绕过 profiling error。

---

## PR 7 — `feature/adk-portability`

### 目的

检查 architecture 是否只是 HSP90 特例。

### 必须完成

1. ADK CaseDossier；
2. ADK CaseGraph；
3. generic structural-state projection capability；
4. case-supplied reference states 和 mapping；
5. no protein-name condition；
6. exposed portability evaluation。

### Operator

```text
trajectory.reference_state_projection.v1
```

必须在：

- runtime；
- trajectory；
- topology；
- references；
- mapping；
- alignment；
- metric；
- output schema；

全部冻结后才成为 `ROSTER_PASS`。

### Claim ceiling

只允许：

```text
frames are closer to reference A / B
or ambiguous under the frozen representation
```

禁止：

- equilibrium population；
- transition rate；
- free-energy difference；
- mechanism。

### Exit Gate

同一个 generic OperatorSpec 和 router 能处理 HSP90 之外的 exposed case，不使用 `if adk`。

---

## PR 8 — `benchmark/frozen-heldout-v1`

### 目的

在 unchanged release candidate 上测试 generalization。

### Case

优先候选：

```text
E. coli DHFR
```

前提：

- exact case 没有用于 rules、prompt、operator 或 threshold development；
- independent curator 制作 answer-blind packet；
- hidden gold 与开发环境隔离。

若 DHFR 已暴露，则选择第四个 protein。

### 运行顺序

#### Arm 1 — Rules Table only

```text
hidden canonical CaseGraph
→ frozen matcher
```

测试 Rules selection。

#### Arm 2 — Agent profiling

```text
answer-blind raw packet
→ Agent proposal
→ validator
→ same matcher
```

测试 profiling。

#### Arm 3 — Harness execution

```text
selected obligations
→ frozen router
→ frozen Operators
→ EvidenceResults
→ conclusion
```

测试 planning / execution。

### 规则

- package freeze 后只运行一次；
- gold 在全部 runs 完成后解封；
- first-run result 必须保留；
- failure 后不在同一 case 上修复并重新称为 held-out；
- repair 进入 vNext，并换新 case。

---

# 9. Case 角色固定

| Case | 固定角色 | 允许用途 | 禁止用途 |
|---|---|---|---|
| X-EISD | control-plane exposed regression | selector adapter、gap taxonomy、source lookup route | Agent/Rules generalization |
| HSP90 | development anchor | rule-to-operator closure、evaluation contract、three-route slice | held-out claim |
| ADK | exposed portability | generic Operator、no-case-specific-branch | held-out claim after modification |
| qFit | regression | binding coverage、EDGE independence | transfer |
| CryoDRGN | regression | exact modality predicate | transfer |
| DHFR / fourth protein | held-out candidate | frozen first-run evaluation | prompt/rule/operator development |

---

# 10. Skills Registry

第一版至少建立以下 procedural Skills：

## `profile_case`

```text
extract requested claim
→ enumerate sources
→ preserve source-native objects
→ assign method / modality / role
→ propose EvidenceEdges
→ attach locators
→ preserve UNKNOWN
```

## `classify_gap`

```text
identify affected obligation
→ classify source fact / computable / unavailable / judgment
→ select Resolution Policy branch
```

## `review_cross_source_comparability`

```text
construct and condition
→ observable and estimand
→ statistical unit
→ time semantics
→ forward / probe bridge
→ shared error
→ validation independence
```

## `select_registered_operator`

```text
retrieve ROSTER_PASS operators
→ check route match
→ check prerequisites
→ select least-authority compatible operator
→ freeze dossier-supplied parameters
→ add output validation
```

## `prepare_conclusion_packet`

```text
collect RuleResults
→ collect EvidenceResults
→ collect receipts
→ identify blocking failures
→ enforce claim ceiling
→ report terminal state
→ report human decisions
```

Skills 只指导 Agent 组织流程，不能修改 Rules 或直接执行 shell。

---

# 11. 验证分层

## L0 — Structural correctness

- schema；
- ID；
- edge；
- DAG；
- I/O compatibility；
- version。

## L1 — Execution correctness

- actual files；
- actual parameters；
- actual Operator execution；
- output schema；
- provenance；
- deterministic / bounded stochasticity。

## L2 — Contract-level scientific semantics

- frozen observable；
- Rule applicability；
- Evaluation Contract；
- claim effect；
- claim ceiling。

## L3 — General scientific correctness

- expert adjudication；
- held-out transfer；
- paper conclusion agreement；
- cross-system usefulness。

当前 PR 0–6 最多建立 L0–L2 development evidence。

不得把 L0 / L1 PASS 写成 L3 scientific correctness。

---

# 12. 结论聚合规则

Prototype v1 采用简单且可审计的 aggregation。

```text
if any BLOCKING RuleResult == FAIL:
    CANNOT_SUPPORT_REQUESTED_CLAIM

elif every BLOCKING RuleResult == PASS
     and no required evidence remains unresolved:
    SUPPORT_WITHIN_CEILING

else:
    ABSTAIN_OR_HUMAN_REVIEW
```

必须额外输出：

```text
current_claim_ceiling
failed_rule_ids
unresolved_rule_ids
advisory_rule_ids
first_failed_dependency
human_review_items
```

禁止只输出一句自然语言 verdict。

---

# 13. 当前两周的授权范围

Codex 当前只获准执行：

```text
PR 0
+
PR 1
```

PR 1 完成后必须停止并提交 review packet。

未获得 human approval 前，不得自动开始：

- PR 2 Stage-2 evaluator；
- HSP90 routed Operator；
- Agent integration；
- RVC-lite；
- ADK；
- held-out。

## Week 1

### Day 1

- 创建 `fix/baseline-boundary-normalization`；
- 修正 Operator lifecycle；
- 修正 README current / target distinction；
- 运行 focused tests；
- 提交 PR 0。

### Day 2–3

- 创建 `feature/rules-prototype-v1`；
- 导入已有 review-led map 和 33-rule audit；
- 建 rule-family overlay；
- 提议 seed families；
- 不修改 upstream registry。

### Day 4

- 为每个 seed family 补 Resolution Policy；
- 为每个 seed family补 Evaluation Contract skeleton；
- 写 blocking / advisory 分类。

### Day 5

- 生成 positive / negative / missing / wrong-target fixtures；
- 运行 tests；
- 生成 `RULES_PROTOTYPE_V1_REVIEW_PACKET.md`；
- 停止，等待人工审查。

## Week 2

只有 PR 1 获批后，才进入 PR 2。

---

# 14. 每个 PR 必须报告

```text
Observed gap
Change made
Contracts affected
Assets kept frozen
Validation actually run
Validation intentionally skipped
Allowed claim
Forbidden upgrade
Remaining risk
Next authorized action
```

不能只写：

```text
tests passed
```

必须写清 tests 证明了什么、没证明什么。

---

# 15. 强制 Stop Rules

出现以下任一情况必须停止：

1. source locator 无法验证；
2. review-led family 无法写出 one-field negative fixture；
3. Rule 没有 claim ceiling；
4. Evaluation Contract 依赖未冻结 threshold；
5. Operator 输入、metric 或 statistical unit 未冻结；
6. Operator 不是 `ROSTER_PASS`；
7. 需要 arbitrary shell / Python；
8. 需要 case-specific verdict branch；
9. held-out input 被污染；
10. Agent 需要看到 paper conclusion；
11. Operator output 无法反链到 actual inputs；
12. 结果只能靠自由 LLM 判断而没有 evidence contract。

Stop 的正确输出是：

```text
BLOCKED
ABSTAIN
REQUEST_NEW_DATA
HUMAN_REVIEW
```

不是临时放宽 gate。

---

# 16. Prototype 完成定义

Prototype 只有在以下链路真实运行后才算完成：

```text
answer-blind scientific claim + declared data
→ Profile proposal with explicit unknowns
→ deterministic admission
→ frozen Rules Prototype v1
→ case-specific obligations
→ direct route OR registered Operator OR explicit stop
→ EvidenceResult + actual-output receipt
→ affected-rule evaluation
→ bounded three-state conclusion
→ human-review packet
```

并同时满足：

- 没有第二套 Rules authority；
- 没有 unregistered Operator；
- 没有 case-specific terminal verdict；
- 没有把 canary success 写成 case-resolution success；
- 没有把 DAG success 写成 scientific support；
- 没有把 development case 写成 held-out；
- 每个 conclusion component 能回到 Rule、source、EvidenceResult 或 human decision。

---

# 17. Codex 的第一条具体行动

立即执行：

```text
Create branch:
fix/baseline-boundary-normalization
```

只完成 PR 0 范围。

完成后返回：

1. diff summary；
2. changed contracts；
3. tests and exact results；
4. unchanged X-EISD baseline counts；
5. current Operator routing statuses；
6. remaining risks；
7. whether PR 1 is safe to start。

不要在同一 branch 开始 Rules Prototype v1。
