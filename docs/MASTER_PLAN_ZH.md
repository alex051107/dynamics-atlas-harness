# Dynamics Atlas：Rules Table 与 Agent Harness Master Plan

> 版本：v2.0
> 日期：2026-08-25
> 状态：目标架构已冻结；本地 vertical slice 已运行，真实 case route 仍受阻
> 适用范围：Dynamics Atlas prototype、Rules runtime、Profile Agent、Harness、registered operators 与科学验证路线

## 文档边界

本计划把三类信息分开记录：

- **Observed**：已经存在并可从本地 artifact 或运行 receipt 验证的事实；
- **Design**：本项目已经选择、后续实现必须遵守的架构；
- **Future**：尚未实现，也不能写成当前能力的功能。

文献证据、历史 Rule ID 和 source locator 继续保存在原有 Rules 资产中。本计划只规定这些资产如何进入 runtime，不重新解释论文，也不借架构文档提升任何 scientific claim。

---

# 0. 决策摘要

Dynamics Atlas 是一个 **scientific workflow compiler**：系统把用户问题、论文和数据整理成结构化 case，使用带来源的 Rules 编译出 case-specific scientific obligations，再通过已有证据、registered scientific operators 或人工判断解决这些 obligations，最终返回带 claim ceiling 和完整 trace 的 bounded conclusion。

当前执行决定如下：

1. 直接实现目标架构的 thin vertical slice，不再另建 proposal-only 小系统。
2. `CaseWorkflow` 是平台持有的 canonical artifact；CaseGraph 和 RunPlan 都属于它。
3. Rules 的 authoring truth 留在原 registry；typed binding 继续作为 runtime compiler 输入。
4. Harness 负责状态、routing、执行限制、receipt 和重新评估。
5. Operator 按 scientific capability 注册，再绑定 MDAnalysis、现有脚本或其他 backend。
6. 先接通一条真实 gap-resolution route，再扩充工具数量和规则覆盖面。
7. Request–Validate–Commit、并发编辑、WebUI 和 general scientific correctness 属于 Future。

贯穿所有阶段的约束：

> 每个新增对象必须解决当前 vertical slice 中一个已经观察到的问题。没有真实复用需求时，不增加 registry、service、ontology、planner 层或重复检查。

---

# 1. 系统承诺与输出边界

## 1.1 系统接收什么

```text
Scientific question
+ Paper / source manifest
+ Data manifest
+ Available metadata
+ Optional raw, processed or derived artifacts
```

输入可以不完整。缺失字段必须保留为显式 unknown，不能由模型按常识补齐。

## 1.2 系统返回什么

系统返回 `ConclusionPacket`，至少包含：

```text
case_id
requested_claim
current_claim_ceiling
resolved_rule_instances
unresolved_rule_instances
evidence_results
operator_run_receipts
terminal_state
human_review_items
provenance
```

Runtime 使用三组不同状态，避免把“流程跑通”写成“科学结论成立”。

### Routing state

```text
DIRECT_EVALUATION
EVIDENCE_LOOKUP
REGISTERED_OPERATOR
REQUEST_NEW_DATA
HUMAN_REVIEW
```

### Rule evaluation state

```text
PASS
FAIL
UNRESOLVED
NOT_APPLICABLE
HUMAN_REQUIRED
```

### Scientific conclusion state

```text
SUPPORT_WITHIN_CEILING
CANNOT_SUPPORT_REQUESTED_CLAIM
ABSTAIN_OR_HUMAN_REVIEW
```

`CANNOT_SUPPORT_REQUESTED_CLAIM` 只描述当前数据与 evidence contract。它不证明现实中的 biological claim 为假。

当前 prototype 尚未完成可泛化的 scientific conclusion aggregation。现阶段最多返回 contract-bounded routing/evaluation 结果，并要求 human review。

---

# 2. Canonical end-to-end flow

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
      Scientific Rule Compiler
                │
    RuleInstances + Claim Ceiling
                │
                ▼
         Resolution Router
      ┌─────────┼──────────┬────────────┐
      ▼         ▼          ▼            ▼
 DIRECT_EVAL  SOURCE_LOOKUP  OPERATOR_DAG  HUMAN/NEW_DATA
      └─────────┴──────────┴────────────┘
                │
                ▼
 EvidenceResult + OperatorRunReceipt
                │
                ▼
       Evaluation Contracts
                │
                ▼
       Claim Ceiling Compiler
                │
                ▼
        Conclusion Packet
```

平台持有的完整对象是：

```text
CaseWorkflow
= CaseProfile
+ EvidenceItems
+ ComparisonEdges
+ RuleInstances
+ ExecutionPlan
+ EvidenceResults
+ ClaimState
+ Receipts
```

这条数据流是项目的固定主线。Profile Agent、typed binding、operator registry 和 future mutation service 都是其中的实现部件，不能各自发展成平行系统。

---

# 3. 当前真实状态

以下状态来自 2026-08-25 本地 run：

`dynamics-atlas-harness/runs/target_architecture_v0_2_20260825/`

| Component | Observed state | 当前证据 | 当前 claim ceiling |
|---|---|---|---|
| Profile prompt | `IMPLEMENTED` | `prompts/profile_case_v1.md` | 只提出 CaseGraph 字段 |
| Profile provider | `RECORDED_FIXTURE_ONLY` | stable provider interface | 尚未接真实便宜模型 |
| CaseGraph admission | `IMPLEMENTED` | `profile/case_graph_admission.json` | structural admission only |
| Rules selector | `EXISTING_V0_3_SELECTOR_INVOKED` | 59 obligations / 15 unresolved inputs | review obligations only |
| Evaluation Contract | `IMPLEMENTED_FOR_BUNDLE_ROUTING` | `evaluation/evaluation_contract.json` | 不产生 general scientific verdict |
| Persistent RunPlan | `IMPLEMENTED` | `run_plan.json` | execution state only |
| X-EISD case route | `RUN_PLAN_BLOCKED` | 16 gaps，0 个匹配 operator | 没有 case-resolution claim |
| HSP90 time-anatomy operator | `CANARY_SUCCEEDED` | `operator_canary/operator_run_receipt.json` | frozen descriptive diagnostic only |
| HSP90 canary 与 X-EISD 的关系 | `INDEPENDENT_CANARY` | run summary 明确标记未被 case plan 路由 | 不能用来关闭 X-EISD gaps |
| Structural-state projection | `REGISTERED_BLOCKED` | MDAnalysis runtime、method profile、inputs 和 metric 未冻结 | 不得执行或报告 output |
| Request–Validate–Commit | `FUTURE` | 仅保留接口方向 | 无当前能力声明 |
| General semantic correctness | `NOT_EVALUATED` | human review required | 无泛化结论 |
| GitHub | `LOCAL_CHANGES_PRESENT` | 本地 nested repo | 未完成远端 readback 时不写“已上传” |

当前 run 的精确摘要：

```text
PROFILE_READY
→ EXISTING_SELECTOR_INVOKED
→ 59 obligations
→ 15 unresolved selector inputs
→ RUN_PLAN_REQUIRED
→ 16 total gaps
→ no matching registered operator
→ RUN_PLAN_BLOCKED
```

第 16 个 gap 是 batch-level evidence evaluation 尚未完成。HSP90 canary 证明现有分析可以按 registry、fixed inputs、output contract 和 receipt 接入；它没有证明当前 X-EISD route 已解决。

---

# 4. 对象边界与权限

## 4.1 三个系统组件

| 组件 | 负责什么 | 不负责什么 |
|---|---|---|
| Rules | 适用条件、required evidence、evaluation contract、claim effect、source trace | 运行科学包；猜测缺失事实 |
| Harness | 构建和保存 workflow、routing、operator resolution、执行限制、receipt、受影响规则的重新评估 | 创造新规则；把执行成功升级成 scientific support |
| Operators | 在固定输入、参数和 runtime 下产生 EvidenceResult | 选择 Rule；修改 claim ceiling；直接输出 mechanism verdict |

Human review 保留以下权限：

- 批准新 rule 或 rule family；
- 冻结 method profile、metric 和 threshold；
- 判断 source passage 是否支持规则抽象；
- 批准 claim upgrade；
- 对 L3 scientific correctness 作最终判断。

## 4.2 Case Evidence Graph 与 Execution DAG

`Case Evidence Graph` 表达科学对象和比较关系：

```text
CASE
SOURCE
COMPARISON EDGE
CLAIM
RULE INSTANCE
EVIDENCE RESULT
```

`Execution DAG` 表达计算依赖：

```text
load registered inputs
→ calculate observable
→ validate output
→ evaluate affected rule
```

两种 edge 分开保存：

| Edge | 保存位置 | 含义 |
|---|---|---|
| `EvidenceEdge` | `CaseWorkflow.comparisons` | sources 比较什么、bridge 是否存在、最高可支持什么 claim |
| `ExecutionEdge` | `CaseWorkflow.execution_plan` | 哪个 step 的 output 可进入下一个 step |

DAG success 只说明 declared steps 执行完成。科学比较是否成立仍由 Rules、Evaluation Contract 和 human adjudication决定。

---

# 5. Profile Agent contract

## 5.1 最小职责

Profile Agent 只做以下工作：

1. 解析 requested scientific claim；
2. 枚举 papers、datasets 和 derived artifacts；
3. 提取 method、native observable、estimand、construct、condition、time semantics、spatial support、statistical unit、uncertainty 和 evidence role；
4. 提出中性的 source-to-source comparison edges；
5. 给字段附 evidence pointer；
6. 对无法确认的内容输出明确 unknown。

Profile Agent 不得：

- 选择 Rule ID；
- 选择 operator 或 terminal route；
- 输出 SUPPORT / CANNOT_SUPPORT；
- 写 expected relation 或 reference answer；
- 根据论文结论反推 input fields；
- 用模型自信度覆盖缺失 evidence pointer。

## 5.2 字段状态

```text
EXTRACTED
INFERRED_WITH_SUPPORT
UNKNOWN
CONFLICTING_SOURCES
HUMAN_CHECK_REQUIRED
```

模型 confidence 可以保留为诊断字段，不参与 deterministic routing。

## 5.3 当前与未来

当前实现：

```text
proposal
→ schema/evidence admission
→ versioned canonical JSON
```

未来实现：

```text
retrieve canonical state
→ propose typed patch
→ validate
→ commit or reject
```

后续接便宜模型时，只替换 Profile provider。下游 CaseWorkflow contract、Rules compiler 和 Harness 不随模型变化。

---

# 6. Rules Table 的位置与 runtime 设计

## 6.1 Authoring truth 保持原位

Rules 的 source-linked authoring registry 继续位于：

```text
autoresearch/tasks/
  dynamics_atlas_literature_card_male_pilot_20260805/
  outputs/ruleset/v0_1/rule_registry.tsv
```

当前 33-row registry 中的文献 evidence、source locator、Rule ID 和历史判断不移动。Harness 以 read-only asset 方式引用它，避免出现第二套科学权威。

## 6.2 Prototype 保留三层

```text
Rule Evidence / Authoring Registry
        │
        ▼ compile
Typed Applicability Bindings
        │
        ▼ compile
Executable Rule Index
        │
        ▼ select
Case-specific RuleInstances
```

对应的当前资产是：

1. `rule_registry.tsv`：面向人类审查和 source trace；
2. `registry_bound_typed_bindings_v0_3.json`：17 个 baseline bindings 加 2 个 modality-repair injections；
3. `compiled_registry_rule_index_v0_3.json`：selector 的冻结输入与 compile receipt。

## 6.3 Typed binding 的意义

Rule row 回答“科学上要检查什么”。Typed binding 把这个判断编译成机器可执行条件：

```text
target_scope
exact predicates
required_fields
gap checks
claim scope
evidence evaluation requirement
```

它防止 selector 用 `MD`、`trajectory` 等自由文本关键词临时猜测 applicability。

当前 runtime 保留独立 typed bindings。理由来自实际行为：同一个 rich X-EISD CaseGraph 在旧 v0.1 snapshot 中产生 51 obligations / 17 unresolved；当前 v0.3 产生 59 obligations / 15 unresolved。Binding package 会改变 selection，不能在没有迁移测试时直接内嵌或删除。

面向架构读者时，typed binding 可以视为 `Scientific Rule Compiler` 的内部细节。未来只有在以下条件同时满足时才重构：

- 新 schema 能无损表达现有 predicates 和 required fields；
- v0.3 selector regression 保持一致，或差异获得人工批准；
- Rule Evidence Registry 仍是唯一 source authority；
- 迁移不会改变历史 Rule ID 和 evidence trace。

## 6.4 Runtime ScientificRule / RuleInstance

Runtime 需要表达：

```text
rule_id
rule_version
rule_family
target_scope
applies_when
required_evidence
evaluation_mode
evaluation_contract
outcome_to_claim_effect
resolution_routes
evidence_refs
status
```

`outcome_to_claim_effect` 是 Stage-2 的核心。例如：

```json
{
  "PASS": {
    "claim_effect": "NO_ADDITIONAL_RESTRICTION",
    "route": "CONTINUE"
  },
  "FAIL": {
    "claim_effect": "FORBID_KINETICS",
    "route": "RETURN_WITH_LOWER_CEILING"
  },
  "UNRESOLVED": {
    "claim_effect": "CAP_AT_SOURCE_LOCAL_CONSISTENCY",
    "route": "REGISTERED_OPERATOR_OR_HUMAN"
  }
}
```

现有 selector 已能产生 review obligations。它还不能从论文结果推导 observed discriminability，也不能独立给出 scientific SUPPORT。Rule selection 和 evidence evaluation 继续分开。

---

# 7. Harness runtime

Harness 是 control plane 和 execution runtime。它读取 canonical CaseWorkflow 与 live registries，限制允许的 action，执行 registered operator，验证实际 output，保存 receipt，并只重新评估受影响的 RuleInstances。

Prototype Harness 必须完成七个动作：

1. Load canonical CaseWorkflow；
2. Compile applicable RuleInstances；
3. Classify unresolved evidence gaps；
4. Resolve registered capability；
5. Validate prerequisites、inputs 和 execution edges；
6. Execute operator 并附加 EvidenceResult / receipt；
7. Re-evaluate affected rules 并更新 claim ceiling。

## 7.1 Obligation state machine

```text
OBLIGATION_OPEN

├── EVIDENCE_READY
│     → DIRECT_EVALUATION
│
├── SOURCE_FACT_MISSING
│     → EVIDENCE_LOOKUP
│
├── COMPUTABLE_EVIDENCE_MISSING
│     → REGISTERED_OPERATOR
│
├── DATA_NOT_AVAILABLE
│     → REQUEST_NEW_DATA
│
└── SCIENTIFIC_JUDGMENT_REQUIRED
      → HUMAN_REVIEW
```

完成后的 terminal state 是 `PASS`、`FAIL`、`UNRESOLVED`、`NOT_APPLICABLE` 或 `HUMAN_REQUIRED`。

`clean trace` 是所有节点的 invariant，不是单独的 workflow step。`complete` 的定义是：所有 blocking RuleInstances 获得合法 EvaluationResult，或者进入明确 terminal stop。

## 7.2 Persistence 与复用

复用单元有三类：

- Rules：复用 scientific constraint；
- Skills：复用领域程序性做法；
- Operators：复用固定 I/O、参数、runtime 和 output contract 的计算能力。

RunPlan 只连接这些单元。Agent 不为每个 case 生成一次性脚本，也不能绕过 registry 直接执行 arbitrary Python。

当前 JSON artifact 足以支持单进程 prototype。出现并发编辑、跨用户 mutation 或 rollback 的真实需求后，再加入 Request–Validate–Commit service。

---

# 8. Registered Operator system

## 8.1 Capability-first registry

Registry 登记 scientific capability：

```text
trajectory.reference_state_projection.v1
trajectory.sampling_diagnostics.v1
structure.flexibility_projection.v1
ensemble.experimental_observable_prediction.v1
```

实现 backend 单独绑定：

```text
capability:
  trajectory.reference_state_projection.v1

implementation:
  mdanalysis.reference_state_projection.v1

backend:
  MDAnalysis
```

`MDAnalysis`、`MDTraj`、`deeptime` 或 `ProDy` 本身只是 package candidate。只有冻结 OperatorSpec、runtime probe、canary、output contract 和 claim boundary 后，它们才进入 Harness。

## 8.2 OperatorSpec

```text
operator_id
capability
supported rule families
supported methods / modalities
required inputs
fixed or dossier-supplied parameters
implementation_ref
runtime and package versions
input schema
output schema
validation checks
failure routes
allowed claims
forbidden claims
provenance requirements
registry status
```

建议生命周期：

```text
DISCOVERED
→ SPECIFIED
→ REGISTERED_BLOCKED or CANARY_PASS
→ CONTRACT_REVIEWED
→ ROSTER_PASS
```

## 8.3 当前 roster

| Capability / Operator | Backend | 状态 | 可以证明什么 | 仍缺什么 |
|---|---|---|---|---|
| `hsp90.directional_time_anatomy.v0` | existing standard-library analysis | canary succeeded | 现有 HSP90 分析可经 registry、fixed inputs、output contract 和 receipt 复用 | 尚未匹配当前 X-EISD gaps；scientific review 仍需人工 |
| `trajectory.structural_state_projection.v1` | planned MDAnalysis adapter | `REGISTERED_BLOCKED` | 只证明 spec 已登记 | MDAnalysis runtime、case inputs、mapping、method profile、metric 和 parameters |
| NMR package candidate | meeting reference | `DISCOVERED_UNIDENTIFIED` | 会议中确实提到 Gina 使用的 NMR package | 聊天记录中的准确 package 名称和链接 |

当前技能目录中已经有 `molecular-dynamics` skill，其模板使用 OpenMM 与 MDAnalysis，并覆盖 RMSD、RMSF、Rg 和 contacts。Skill 是 operator discovery 与程序性知识来源，不能替代本项目的 OperatorSpec 和 canary。

## 8.4 下一项通用 operator

优先候选是：

```text
trajectory.reference_state_projection.v1
```

只有在当前真实 gap 与它匹配、输入已存在并且 method profile 可冻结时才实施。

最小输入：

```text
topology
trajectory files
replica IDs
reference ensemble A
reference ensemble B
alignment selection
frozen distance metric
frame policy
```

最小输出：

```text
per-frame distance to reference A
per-frame distance to reference B
relative projection or margin
ambiguous frames
actual files read
frame counts
parameters
warnings
provenance
```

允许的最高 claim：在冻结 representation 和 metric 下，frames 更接近 reference A、reference B，或无法区分。

禁止升级到：equilibrium population、transition rate、free-energy difference、unique pathway 或 biological mechanism。

如果 16 个当前 gaps 中没有一项满足输入合同，下一步应走 source lookup、已有 EvidenceResult 接入或 explicit stop，不能为了展示 operator route 强行调用无关分析。

---

# 9. Direct Evaluation、EvidenceResult 与 Evaluation Contract

这三个对象按以下顺序工作：

```text
RuleInstance
→ Resolution Router
→ Direct Evaluation OR Registered Operator
→ EvidenceResult
→ Evaluation Contract
→ RuleResult
```

## 9.1 Direct Evaluation

Direct Evaluation 只处理已经存在、可以确定性判断的 evidence：

- required metadata 是否存在；
- source ID、construct ID、condition ID 是否精确一致；
- validation evidence 是否在 lineage 中标记为未参与 fitting；
- bridge receipt 是否存在；
- operator output 是否符合 schema；
- frozen threshold 是否通过。

它不能从自然语言推断 scientific equivalence，不能从 Discussion passage 推导 mechanism，也不能临时建立阈值。

## 9.2 EvidenceResult

EvidenceResult 记录事实与来路：

```text
evidence_result_id
source_rule_instance_ids
producer_type
producer_id
actual_inputs
parameters
outputs
quality_checks
warnings
provenance
claim_ceiling
```

Operator 输出 evidence facts。`SUPPORT`、`MECHANISM` 和 claim upgrade 由 Evaluation Contract 与 human review控制。

## 9.3 Evaluation Contract

Evaluation Contract 规定 EvidenceResult 如何转成 RuleResult。例如：

```text
required outputs:
- per-replica observable series
- effective sample size
- window sensitivity

PASS:
- all required outputs present
- frozen acceptance criterion satisfied

FAIL:
- frozen criterion explicitly violated

UNRESOLVED:
- output exists but criterion cannot be evaluated
```

当前实现只完成 current-bundle sufficiency routing。Scientific PASS/FAIL 需要 rule-specific contracts 与真实 EvidenceResults，尚未完成。

---

# 10. Semantic correctness 分层

| 层级 | 当前安排 | 含义 |
|---|---|---|
| L0 Structural correctness | 现在 | schema、ID、edge、DAG、I/O compatibility |
| L1 Execution correctness | 现在 | 实际文件、参数、operator execution、output schema、provenance |
| L2 Contract-level scientific semantics | prototype 逐条实现 | frozen observable、rule、criterion 和 claim effect 是否按合同执行 |
| L3 General scientific correctness | future validation lane | 规则能否跨体系成立，结论能否通过 expert 与 held-out evidence |

当前代码只实现 current-bundle sufficiency routing，不是 semantic checker。未来的 L2 checker 应命名为 `Contract-Level Semantic Checker`。L3 属于 Scientific Adjudication，不能由 schema、DAG 或 package success替代。

---

# 11. Prototype scope 与反过度工程纲领

## 11.1 当前 target prototype 必须有

- 一个明确的 Profile prompt 和可替换 provider interface；
- 一个 canonical CaseWorkflow / rich CaseGraph contract；
- 现有 v0.3 Rules selector 的只读 adapter；
- RuleInstances / obligations 与 claim ceiling；
- direct-bundle route；
- persistent RunPlan；
- capability-first Operator Registry；
- 至少一项真实 analysis canary；
- EvidenceResult 与 OperatorRunReceipt；
- explicit blocked / human stop；
- 可追溯 ConclusionPacket。

## 11.2 当前不建设

- 新 Rules database；
- 全自动 rule authoring；
- arbitrary Python execution；
- 多 Agent swarm；
- 自动安装大量 scientific packages；
- operator knowledge graph；
- production WebUI；
- 并发 mutation service；
- general semantic correctness model；
- 大规模 held-out benchmark。

## 11.3 每项新增工作的 admission test

开始新增 registry、schema、validator 或 service 前，必须回答：

1. 它解决哪个已观察到的 gap 或重复？
2. 现有对象为什么不能表达？
3. 它会改变哪个 public contract？
4. 最小的验证是什么？
5. 哪个条件出现后立即停止扩展？

答不出第 1 项时，不实施。

---

# 12. 交付阶段：按可运行行为推进

## Milestone 0 — Thin bridge

**状态：已完成。**

已证明 Profile fixture、frozen Rules 和 operator fixture 可以通过受约束的 provider/operator interface 串接。它没有证明真实科学分析完成。

## Milestone 1 — Target architecture local slice

**状态：已运行，case route blocked。**

已完成：

```text
Profile proposal
→ deterministic admission
→ actual v0.3 selector
→ Evaluation Contract
→ persistent RunPlan
→ registered-operator resolution
→ explicit blocked state
```

并行完成一个 HSP90 existing-analysis canary。该 canary 没有被当前 X-EISD route 使用。

## Milestone 2 — Close one real case gap

**状态：下一步。**

一次只选择一个高价值 gap：

1. 对 16 个 gaps 按 `SOURCE_FACT_MISSING`、`COMPUTABLE_EVIDENCE_MISSING`、`DATA_NOT_AVAILABLE`、`SCIENTIFIC_JUDGMENT_REQUIRED` 分类；
2. 选择已有输入、与 requested claim 有直接关系的一项；
3. 优先复用现有 EvidenceResult 或 analysis script；
4. 需要新 backend 时，先冻结 capability、method profile、inputs、metric 和 output contract；
5. 运行一次 canary；
6. 把 operator output 接回原 RuleInstance；
7. 只重新评估受影响规则。

Exit condition：至少一项真实 gap 从 `UNRESOLVED` 转成合法 RuleResult，且 receipt 能证明实际读取的 inputs、parameters 和 outputs。

Early stop：输入、method semantics 或 frozen metric 任一缺失时，保存 blocked reason，不安装依赖、不编造 fixture。

## Milestone 3 — Three-route vertical slice

同一套 runtime 支持：

```text
A. current evidence sufficient
   → direct bounded return

B. evidence missing but computable
   → registered operator
   → EvidenceResult
   → affected-rule reevaluation

C. evidence unavailable or requires judgment
   → explicit stop / human / new data
```

Exit condition：三条 route 共用同一 CaseWorkflow、Rules compiler 和 Harness，不出现 `if hsp90`、`if adk` 或 case-specific terminal verdict。

## Milestone 4 — Live Profile model adapter

在 deterministic chain 稳定后接真实模型。保留两种后端：

- 便宜 agent/model provider；
- Codex subagent simulation，用于 provider contract 测试。

两者必须输出相同 Profile schema。模型错误与 Harness 错误分别记录。

Exit condition：answer-blind input 可以生成可 admission 的 proposal；critical unknowns 不被静默补全。

## Milestone 5 — Contract-level science and portability

- 为 seed RuleInstances 冻结 L2 Evaluation Contracts；
- 在 HSP90 development case 上调试；
- 使用 ADK 或其他 exposed case 检查 portability；
- 冻结后再选择 held-out protein；
- expert adjudication 与 held-out 结果进入独立 scientific validation report。

Request–Validate–Commit、并发编辑和 WebUI 只有在 workflow 需要多轮外部 mutation 时才进入新 milestone。

---

# 13. 科学验证路线与工程路线分开

工程阶段回答：

```text
workflow 能否构建、执行、停止和复现？
```

科学验证回答：

```text
Rule、observable、criterion 和 bounded conclusion 是否正确？
```

推荐 case 角色：

| Case | 角色 | 允许用途 |
|---|---|---|
| HSP90 | development anchor | prompt、operator、Rules 和 failure path 调试 |
| ADK | exposed portability case | 检查架构是否依赖 HSP90 特例 |
| 新 protein | frozen held-out | release freeze 后的一次性 generalization test |

如果某个 case 参与 rule、prompt、operator 或 threshold 修改，它立即变为 exposed case，不再用于 held-out claim。

Benchmark 分成三个问题：

1. hidden canonical CaseGraph → matcher：测 Rules selection；
2. answer-blind raw input → Profile Agent → same matcher：测 profiling；
3. selected obligations → Harness → Operators → Evaluation：测 planning 与 execution。

失败归因使用：

```text
PROFILE
VOCABULARY
BINDING
RESOLUTION_POLICY
OPERATOR
EVALUATOR
SCIENTIFIC_RULE
```

---

# 14. 现有资产迁移

| 现有资产 | 目标位置 / 用法 | 动作 |
|---|---|---|
| 33-row `rule_registry.tsv` | Rule Evidence / authoring truth | 原位保留，只读引用 |
| v0.3 typed bindings | Scientific Rule Compiler input | 当前保留；未来按 regression 结果决定是否内嵌 |
| v0.3 compiled index + selector | deterministic rule selection | 通过 workspace adapter 调用，不复制逻辑 |
| rich metadata contract | CaseProfile / CaseGraph admission | 直接复用 |
| HSP90 time-anatomy script | existing-analysis operator | 已登记并完成 independent canary |
| ADK structural projection script | generic operator candidate | 提取 capability 前先冻结 method/profile 与新 case inputs |
| qFit / CryoDRGN assets | regression 或 future operator candidates | 不写成已注册能力 |
| scientific skills | procedural knowledge / discovery | 不自动等价为 OperatorSpec |
| 会议中 NMR package | discovery item | 找到准确聊天链接后再登记，不凭记忆命名 |

已有资产只有在目标架构中拥有明确 owner、contract 和 claim boundary 后才转换。不能转换的内容留作参考，不建兼容层维持表面复用。

---

# 15. 状态、仓库与知识库

## 15.1 状态所有权

- 项目级 live gate：`autoresearch/DYNAMICS_ATLAS_STATUS.md`；
- 人工确认的目标或优先级变化：`autoresearch/DYNAMICS_ATLAS_DECISION_LOG.jsonl`；
- 本次实现任务：`autoresearch/tasks/dynamics_atlas_target_architecture_prototype_20260825/`；
- Harness 代码、schemas、docs 和 run receipts：`dynamics-atlas-harness/`。

`CURRENT_STATUS.md` 只保存任务级 snapshot 和 evidence links。每个事实只由一个文件拥有，其他文档链接它。

## 15.2 GitHub

每个可运行 milestone 形成一个相关功能 batch：

```text
implementation
→ focused validation
→ status / receipt update
→ local diff review
→ commit
→ private remote push
→ remote readback
```

只有 private visibility、authentication、push 和 remote readback 都通过后，状态才写“已同步 GitHub”。Force push、public visibility、collaborator 或权限变化需要单独批准。

## 15.3 Obsidian

每个交付阶段同步四项内容：

- 当前 architecture decision；
- 已观察运行结果；
- blocker 与 next allowed action；
- 对应 repo artifact / receipt 链接。

同步前先确认真实 vault 和目标 note。Obsidian note 不复制完整 registry 或 run output，只链接 authority artifacts。

---

# 16. 验证节奏

验证按风险执行，避免重复确认同一 code state。

| Functional batch | 风险 | 计划检查 | Runner 次数 | 独立 review | Hash | Trigger | Early stop | 必须更新的状态 |
|---|---|---|---:|---:|---:|---|---|---|
| Master Plan 修订 | 事实层混写、术语冲突、AI 腔 | 一次 prose scan + 人工 source check | 1 | 0 | 0 | 文档初稿完成 | 核心事实与 run receipt 冲突时先修文档 | task status、work log |
| 单项 gap closure | 错路由、错误 input、claim upgrade | 一次 focused operator/route check set | 1 | 0；public contract 改变时合并 review 1 次 | 0；首次 frozen import 可 1 次 | implementation 与 inputs 冻结 | prerequisite 缺失即 `REGISTERED_BLOCKED` | run receipt、progress、CURRENT_STATUS |
| Three-route milestone | cross-module contract drift | 一次 target architecture integration suite | 1 | 1 次 combined architecture review | 0 | 三条 route 都实现 | 任一路由需要 case-specific verdict 时停止 | review report、Status |
| Final prototype delivery | 回归与交付错报 | 一次 full test suite；build/lint 仅在相关配置变化时各 1 次 | test 1；其他按触发 | 1 次 final combined review | transfer integrity 需要时 1 次 | release candidate 冻结 | 失败后只重跑受影响类别，再做一次最终组合检查 | final report、Decision/Status（仅真实变化） |

同一 input、implementation version 和风险下，每个类别最多运行一次。修复后只重跑受影响类别；没有新风险时跳过重复 full test、hash 和 reviewer。

---

# 17. 参考设计及采用边界

| 参考 | 采用内容 | 不采用内容 |
|---|---|---|
| DataFlow-Harness | persistent editable artifact、live registry、typed workflow construction、procedural Skills | 把 DAG/schema validity 当 semantic correctness；当前先不做完整 RVC |
| BioExcel Building Blocks | 显式 input paths、output paths、properties 的 wrapper contract | 全量搬入 BioBB stack |
| CWL | declared upstream output 才能连接 step input；typed parameters | 当前不引入完整 CWL runtime |
| AiiDA | calculation provenance 与 workflow logic 分开 | 当前不建设 provenance database |
| ToolUniverse / SciToolAgent | tool schema、capability metadata、dependency ideas | 当前两个 operator 不建设大规模 tool knowledge graph |
| Anthropic protein-design harness | constitution、dossier、tool roster、canary、actual-output validation | 超长单体 prompt、GPU campaign、subagent swarm |

来源：

- DataFlow-Harness：He et al. (2026) local source-of-record PDF；原 PDF 不进入本仓库
- BioBB arguments：<https://biobb-documentation.readthedocs.io/en/latest/arguments.html>
- CWL Workflow v1.2：<https://www.commonwl.org/v1.2/Workflow.html>
- AiiDA provenance：<https://aiida.readthedocs.io/projects/aiida-core/en/stable/topics/provenance/concepts.html>
- ToolUniverse custom tool schema：<https://github.com/mims-harvard/ToolUniverse/blob/main/plugin/skills/tooluniverse-custom-tool/references/python-tool.md>
- SciToolAgent：<https://github.com/HICAI-ZJU/SciToolAgent>
- Anthropic binder-design prompt：<https://huggingface.co/datasets/Anthropic/claude-protein-binder-design/blob/main/prompts/prompts/multi_target_binder_design_prompt.md>

这些参考只提供 design patterns。Dynamics Atlas 的 scientific authority 仍来自本地 source-linked Rules、case-specific evidence 和 human review。

---

# 18. Prototype 完成定义

Prototype 达到目标架构 milestone，需要同时满足：

```text
answer-blind question + source/data manifest
→ Profile proposal with explicit unknowns
→ deterministic admission
→ existing Rules compiler
→ case-specific RuleInstances
→ direct route OR registered operator route OR explicit stop
→ EvidenceResult + receipt
→ affected-rule evaluation
→ bounded ConclusionPacket
```

并满足以下边界：

- 没有第二套 Rules authority；
- 没有 unregistered operator execution；
- 没有 case-specific terminal verdict；
- 没有把 package success 写成 scientific support；
- 没有把 development case 写成 held-out；
- 没有为了完整感增加当前不需要的平台层；
- 每项结论都能回到 source、Rule、EvidenceResult 或明确 human decision。

下一个允许动作已经固定：对当前 16 个真实 gaps 分类，选择一项已有输入且可由现有能力解决的 gap，完成一条 `RuleInstance → registered capability → EvidenceResult → reevaluation` 路由。若 prerequisite 不满足，保留 blocked receipt 并转向 source lookup 或另一项真实 gap。
