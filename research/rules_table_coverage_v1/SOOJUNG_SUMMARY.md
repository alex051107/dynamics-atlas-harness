# Rules Table Coverage Challenge v1 给 Soojung 的简要说明

这轮工作完成了对现有 Rules Table 的一次定向 coverage check。我们先从 20 个已暴露的 development cases 和 15 个原始论文来源中写出科学审查问题，再把这些问题与冻结的 Rules Table 对照。PR 没有改 canonical Rule，也没有运行 Agent、Operator 或 H1 结论。

## 这张表目前能做什么

Rules Table 有七个 family 和十二条 runtime Rule。F02 记录构建体、体系和条件声明。F03 记录 source-native observable、estimand、时间语义和统计单位。F06 处理 source role 与 SOURCE 之间的 comparability。F04、F05、F07 仍是 Candidate Map Only。它们已经标出需要审查的科学问题，但没有可执行合同，也不能产生可信的 local PASS。

## 20 个案例给出的结果

20 个 case 共整理出 40 个 mandatory review obligations。

- 分类表示层面，40 个问题都能放进现有 family。
- 可执行合同层面，14 个问题得到精确覆盖，23 个只得到部分覆盖。
- 19 个问题落在 F04、F05、F07 的 Candidate Map Only 条目上。它们说明系统识别到了需要，尚未构成可执行 Rule 成功。
- 2 个问题需要人类 source-science 判断，1 个属于 source-specific 的方法问题。
- 没有 obligation 完全找不到 family，也没有 obligation 被明确标成 CASE、SOURCE 或 EDGE target 错位。

所以当前最准确的状态是 `RULES_TABLE_PARTIALLY_COVERED_WITH_RECURRING_GAPS`。分类结构已经能容纳这一批问题。可执行的 scientific contracts 还不完整。

## 这轮最有价值的发现

F02R01 和 F03R01 目前只要看到一个带 `source_id` 的 SOURCE 就会触发。它们因此会要求 general guide、review 和 methods paper 填写样品组成或单一 native measurement record。这个现象出现在 4 个 case、3 个独立来源，共形成 8 个额外 declaration obligations。

这个发现叫 `CR-001`。发现本身成立，修复位置还没有确定。source purpose 可能应在 CaseGraph admission 或 source typing 时确定。也可能在未来由 applicability 复用已有的 `source.case_evidence_scope == CLAIM_EVIDENCE` 边界。现在不能直接修改 Binding，因为这个判断必须先证明不循环，也不能漏掉 review 或 methods paper 中嵌入的 empirical evidence object。

## 需要 Soojung 抽查的三件事

1. Case 001 的 general guide 是否应进入 empirical SOURCE，还是应保留为 method/reference source。请看 `GRO-P01-ABSTRACT` 和 `GRO-P01-SCOPE`。
2. Case 008 的 NMR、SAXS、SANS 和 MD 整合论文应作为一个 SOURCE，还是应拆成 modality-level SOURCE objects，再连接到 integrated representation。请看 `BEN-P01-ABSTRACT` 和 `BEN-P01-INTRO`。
3. Case 020 的 F03 source-local semantics 是否需要 F02 context 作为前置条件。现行合同允许 F03 单独声明 native semantics，F06 的 EDGE comparability 才要求相关 F02 和 F03 证据一起成立。请看 `GOM-P01-ABSTRACT`、`GOM-P02-FIG1` 和 `GOM-P02-FIG2`。

Case 020 现已改成 `HUMAN_JUDGMENT_ONLY`。一个来源不足以证明 F02 到 F03 存在通用 dependency，也不足以触发 Rule repair。

## 讨论后可作出的三个决定

1. source purpose 的 ownership 应放在 admission 或 typing，还是可以安全地留给 future applicability guard。
2. integrative publication 的 SOURCE granularity 应由什么 source-science 原则决定。
3. Case 020 的上下文要求是否只服务于 EDGE 或 CASE interpretation，还是应成为 F03 的 source-local prerequisite。

本轮结论只支持这样一句话。当前 Rules Table 已与 20 个 exposed-development cases 的 source-first 审查义务进行系统对照，并清楚区分了精确覆盖、部分覆盖、Candidate Map defer、SOURCE applicability overtrigger 和必须由人判断的问题。它还没有构成 Rules release、H1 结论、Agent 价值证据或 scientific validation。
