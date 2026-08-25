# Dynamics Atlas Harness 目标架构

## 核心判断

Harness 的职责是固定“为什么调用、何时调用、允许产生什么证据”，不是重新实现科学分析库。正确的复用单元有三类：

1. Rules 负责科学适用条件、required checks 和 claim ceiling；
2. Skills 负责专家维护的程序性做法；
3. Operators 负责固定输入、参数、runtime 和 output contract 的实际计算。

RunPlan 只连接这些单元。DAG 本身不提供科学正确性。

## 数据流

```text
UserRequest + PaperManifest + DataManifest
                │
                ▼
        Profile Agent proposal
                │
       deterministic admission
                │
                ▼
       Canonical rich CaseGraph
   ┌────────────┴────────────┐
   │ EvidenceItems           │ EvidenceEdges
   │ source-native semantics │ scientific comparison relation
   └────────────┬────────────┘
                ▼
   existing Rules selector + typed bindings
                │
       ReviewObligations + claim ceiling
                │
                ▼
        Evaluation Contract
          ┌─────┴─────┐
          │           │
  sufficient bundle   unresolved gap
          │           │
 direct bounded       persistent RunPlan
 result + human       ExecutionEdges → registered operator
 review               → EvidenceResult → reevaluate
```

### 两种 edge 必须分开

| Edge | 所属对象 | 含义 |
|---|---|---|
| `EvidenceEdge` | CaseGraph | 两个 scientific sources 之间比较什么、bridge 是否存在、可支持哪一级 claim |
| `ExecutionEdge` | RunPlan | 一个步骤的输出何时成为下一个步骤的输入 |

把两者混在一个 DAG 里，会让“执行成功”看起来像“科学比较成立”。当前 schema 用 `comparisons` 保存 EvidenceEdges，用 `execution_edges` 保存运行依赖。

## 各层权限

| 层 | 可以做 | 不可以做 |
|---|---|---|
| Profile Agent | 从问题、paper、data 提出 CaseGraph 字段和 unknowns | 选 Rule、注册工具、猜答案 |
| Admission | 校验 schema、来源身份、edge endpoint、answer isolation | 补写科学字段 |
| Rules selector | 根据 typed fields 实例化 obligations 和 gaps | 推断 observed result 或 terminal verdict |
| Evaluation Contract | 检查 required EvidenceResults 是否齐全并选择 direct/gap route | 自行解释未冻结的科学语义 |
| RunPlan | 保存 operator dependency、状态、blocked reason | 把 DAG success 当科学 success |
| Registered operator | 在固定 runtime/input/parameter 下产生 EvidenceResult | 改 Rule、扩大 claim ceiling |
| Human review | 批准 method/profile/claim upgrade 和最终判断 | 不应被“流程跑通”替代 |

## Profile Prompt 为什么必须存在

Profile Agent 不是一个抽象框。`prompts/profile_case_v1.md` 明确规定：

- 输入是 question、paper/data manifest 和 source-located content；
- 输出必须符合现有 rich CaseGraph contract；
- 缺失信息写成 `MISSING`、`PARTIAL` 或明确 unknown；
- 不出现 Rule ID、operator ID、reference answer 或 verdict。

当前 recorded provider 只是稳定接口 fixture。未来更换便宜模型时，不改后面的 deterministic pipeline。

## Harness 参考模式

- DataFlow-Harness：复用持久 DAG、live registry、procedural Skills 和 typed mutation 的思路；Request–Validate–Commit 暂缓。
- [BioExcel Building Blocks](https://biobb-documentation.readthedocs.io/en/latest/arguments.html)：tool wrapper 显式声明 input paths、output paths 和 properties。OperatorSpec 采用相同最小接口。
- [CWL v1.2.1](https://www.commonwl.org/v1.2/Workflow.html)：step input 只连接已声明的 upstream output，且参数有 schema。RunPlan 只允许注册过的连接。
- [AiiDA provenance](https://aiida.readthedocs.io/projects/aiida-core/en/stable/topics/provenance/concepts.html)：区分产生数据的 calculation 与解释调用逻辑的 workflow。Atlas 分开保存 EvidenceResult provenance 和 RunPlan logic。
- [ToolUniverse custom tools](https://github.com/mims-harvard/ToolUniverse/blob/main/plugin/skills/tooluniverse-custom-tool/references/python-tool.md)：工具返回统一 status/data，并用 input/return schema 验证。
- SciToolAgent 的 tool dependency/compatibility graph 适合未来 operator 数量很大时参考；当前两项 operator 不需要 knowledge graph。

## 不 over-engineer 的执行纲领

1. 先接现有 CaseGraph、selector 和一项旧分析，不建新数据库。
2. 一个重复 gap 出现前，不建设通用 ontology、自动 tool graph 或 planner。
3. 同一 code state 每个验证类别最多跑一次；失败后只跑受影响类别。
4. 不为了“全覆盖”注册无法 probe 的工具；blocked spec 比假 integration 更有价值。
5. 不让 RunPlan node 细化到实现内部函数；一个 node 对应一个可审计科学动作或 deterministic gate。
6. Request–Validate–Commit 在需要 editable concurrent workflow 时再加入；当前 JSON state 已足够证明 data flow。

## 当前 control-plane smoke 的精确边界

X-EISD case flow 已走到 `RUN_PLAN_BLOCKED`。HSP90 Operator canary 已成功，但它不是 X-EISD plan 的下游 node，也没有达到 `ROSTER_PASS`。当前变更只统一 baseline 和 Operator lifecycle，不连接新的 Rule、Operator 或 case route。后续阶段必须经过单独人工 gate，不能把无关 HSP90 canary 接上去让流程看似 complete。
