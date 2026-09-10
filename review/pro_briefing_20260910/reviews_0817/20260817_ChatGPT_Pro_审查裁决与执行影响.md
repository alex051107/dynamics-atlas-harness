---
title: ChatGPT Pro 审查裁决与两层系统执行影响
analysis_date: 2026-08-17
source_role: external_methodology_review
scientific_authority: false
status: adjudicated_first_batch_complete
---

# ChatGPT Pro 审查裁决与两层系统执行影响

这次审查回答的是一个很具体的问题。现有 Rules Table、逐来源 metadata 和 Rust selector，是否已经形成一套能够交给程序执行的科学判断方法。

答案仍然是，可以继续，但当前只能把 Rules Table 当作有来源的候选规则账本。两篇答案盲 baseline 已经证明旧 selector 会保守停下，却只完整覆盖 X-EISD 八项关键概念中的两项、PRE 八项中的一项。ChatGPT Pro 没有推翻这个判断。它提出的主要改动，是把程序下一轮的任务再收窄一些，先根据逐来源 metadata 生成完整、可追溯的审查义务，随后再让另一层读取论文事实或 operator 输出，判断科学路线。

本次已经保存审查原文，并逐项与冻结计划、两份 baseline 结果和现有输入合同核对。能够直接采纳的建议进入第一批合同。会改变冻结资产或增加科学假设的建议被留到后续实验。当前仍没有证据证明 selector 可用，也没有证据支持 held-out、独立验证、Agent 效果或上线能力。

## 审查准确理解了什么

1. 它准确读取了 2/8 与 1/8 的完整覆盖结果，也承认两案都没有发生 unsupported claim upgrade。
2. 它准确区分了 metadata-only review-obligation selector 与 source-fact 或 operator-backed evidence evaluator。前一层只能说明应该检查什么，后一层才可能决定科学路线。
3. 它准确保留了逐来源 node 与 comparison edge。一个来源缺 uncertainty，不能把整个案例写成全部来源都缺 uncertainty。一条 edge 缺 bridge，也不能把其他 edge 一并判为不可比较。
4. 它准确指出 free-text alias 和固定 top-8 只能作为失败诊断。展示八张卡可以保留，后端不能因此丢掉 mandatory obligations。
5. 它接受了暂不迁移 SQLite、暂不加入 MESMER、暂不拆出多项 Skills 的约束。

## 可以直接采纳的建议

| 建议 | 本轮决定 | 采用理由 | 进入哪一步 |
| --- | --- | --- | --- |
| Rules Table 保留为 source-linked candidate registry | 采纳 | 20 栏适合保存论文事实、项目推导和来源位置，当前不适合直接充当运行时 predicate | 保留现有冻结 registry，不原地迁移 |
| selector 直接读取 `evidence_items` 与 `comparisons` | 采纳 | 旧 flat projection 已经造成 source 和 edge 身份丢失 | 第三批 task-local selector |
| selector 只输出 mandatory review obligations | 采纳 | observed paper result 不存在于 metadata，不能由第一层猜出 | 第一批输出合同 |
| obligation 必须绑定 `CASE`、`SOURCE` 或 `EDGE` | 采纳 | practical guidance 需要指明检查对象与触发字段 | 第一批输出合同 |
| 科学层取消固定 top-8 | 采纳 | 固定截断已经漏掉 X-EISD identifiability 与 PRE validation obligations | 第三批 selector |
| 第二层只接收有 provenance 的 paper fact 或 operator output | 采纳 | 这样可以区分观察事实、计算结果和人工 reference | 第一批输入合同 |
| 加入反事实与不变性测试 | 采纳 | 它能识别 keyword、顺序和无关文本造成的假成功 | 第三批 selector 后的同一实验批次 |
| reserve paper 留到一次限定修复之后 | 采纳 | X-EISD 与 PRE 会参与修复，不能再承担 transfer 证据 | 第五批 |
| SQLite 若以后接入必须保留 `runs` | 采纳 | 不同 selector、registry 和输入版本的结果不能互相覆盖 | 通过 selector 里程碑后再实施 |

## 采纳，但要改写的建议

### 三种职责不等于三个科学权威

ChatGPT Pro 把早期材料理解成三个独立权威层。这个表述需要纠正。现有计划区分 registry、derived selector view 和 case-local result，是为了分开来源、检索与运行结果，并没有给三者同等科学权威。

下一版会写得更明确。论文与 locator 支持 source facts，版本化 registry 保存候选项目规则，selector index 只是可重建视图，run receipt 保存本次程序读了什么和输出了什么。任何运行结果都不能反向改写论文事实。

### 两阶段比较已经是冻结计划的一部分

ChatGPT Pro 把“要求 metadata selector 复现 terminal route”判为错误。这个批评适用于旧验证合同，但不适用于 2026-08-16 已冻结的下一步计划。baseline adjudication 已经确认 `EVALUATION_CONTRACT_GAP`，并明确把 terminal route 放到 evidence evaluator。

因此，本轮不需要推翻计划，只需要把两层 JSON 边界真正写出来。

### observability 先作为候选输入扩展

`case.observability_target` 与 `evidence_item.detection_boundary` 有实际价值。它们可以让系统比较目标事件、观测窗口和空间支持。当前还不能把它们写成跨方法数值阈值，也不能让提交者预填 `ADEQUATE`。

本轮记录字段语义和缺失状态。第二批只有在字段能改变 X-EISD、PRE 或后续 MD fixture 的 obligation 时，才建立 metadata v0.3 candidate。现有 v0.2 和两篇 baseline 输入保持冻结。

### candidate-pool lineage 先验证最小表达

X-EISD 已经证明 pool generation、parent pool 和 prior data reuse 会改变可解释性。下一批可以测试一个很小的 `support_lineage` 表达，并细化现有 candidate-support obligation。当前不建立通用 prior ontology，也不把 X-EISD 再计作独立验证。

### 失败状态按阶段分开

外部审查给出的十一种状态不能放进一个枚举。全文缺失、方法未登记和 reference 泄漏属于 intake 或 admission。`INPUT_CONTRACT_GAP`、`RULE_COVERAGE_GAP` 与 `SELECTOR_GAP` 属于第一层比较。`EVIDENCE_FACT_MISSING`、`EVALUATOR_GAP` 与 `VALIDATION_NONDISCRIMINATING` 属于第二层。`UNSAFE_CLAIM_UPGRADE` 是两层都要检查的安全结果。

## 当前不采纳的内容

1. 不重写冻结的 20 栏 registry。字段归属表可以作为下一版设计草案，迁移要等 typed selector 证明有用。
2. 不为 chemical-species heterogeneity 新增通用 stop rule。当前只有 review-level 提醒，缺少本轮需要的 primary-source derivation 与案例。
3. 不把 observability adequacy 写成 submitter Boolean 或统一阈值。adequacy 必须由目标事件、来源能力和证据事实共同决定。
4. 不建立完整 SQLite 五表、队列、并发 worker、Agent harness 或上线接口。它们没有覆盖本轮的主要风险。
5. 不把 ChatGPT Pro 的外部检索引用当成本地论文证据。科学字段仍回到本地 PDF、Deep Read 和 locator。

## 这次审查带来的实际改变

第一批合同现在需要明确四件事。

1. selector 输出固定为 `DRAFT_REVIEW_PLAN`，不能携带 terminal route 或 paper conclusion。
2. 每个 obligation 都要写清 target、触发字段、规则来源和是否需要第二层证据。
3. evaluator 输入只接受带 locator 的 paper-reported fact，或带名称、版本、参数与 output locator 的 operator output。
4. 失败状态分属 intake、selector 和 evaluator，避免一个大枚举把不同问题混在一起。

X-EISD 示例只展示第一层如何要求检查 candidate-pool lineage 与 identifiability，不写论文最后答案。PRE 示例只展示第二层如何接收“留出 PRE 没有区分 ensemble sizes”这一已报告事实，不预填 terminal route。

## 接下来怎么判断这套方法是否值得继续

第一批完成后，下一步是薄的 typed sidecar。它只覆盖 X-EISD 与 PRE 当前需要的候选规则。再下一步才实现 task-local selector，并做两篇 paper case、字段删除反事实和同义词、排序、无关文本不变性测试。

一次限定修复后，只要仍有 mandatory obligation 漏选、target 错位、reference 泄漏、case-specific branch、无关文本敏感或 unsafe claim upgrade，就停止当前 runtime representation。Rules Table 仍保留为审计账本，不靠继续加权重掩盖失败。

## 仍由人决定的一件事

真实 biological claim 中，哪些解释构成合理的 competing explanations，以及哪一种匹配条件的正交 observable 足以区分它们，仍需要 Alex、Soojung 或 Stephanie 作科学判断。程序可以强制追溯、完整性、停止和结论上限，不能从 metadata 自动发明正确的生物学竞争集合。

## 来源

- [ChatGPT Pro 原始审查](<20260817_ChatGPT_Pro_Rules_Table_原始审查.md>)
- 两篇论文 baseline 的完整语义裁决（该链接目标未纳入本包）
- baseline 之后的两层最小计划（该链接目标未纳入本包）
- 逐来源 metadata contract v0.2（该链接目标未纳入本包）
