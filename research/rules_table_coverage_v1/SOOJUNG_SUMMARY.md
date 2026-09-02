# Rules Table Coverage Challenge v1 给 Soojung 的简要说明

这轮工作完成了对现有 Rules Table 的一次范围受限检查。我们先从 20 个已暴露的 development cases 和 15 个原始论文来源中独立写出科学审查问题，再把这些问题与冻结的 Rules Table 对照。没有修改任何 canonical Rule，也没有做 Agent、Operator 或 H1 结论。

## Rules Table 目前包含什么

表中有七个 family、十二条 runtime Rule。F02 管构建体和条件，F03 管 source-native observable、estimand 和统计单位，F06 管 source role 与 source 和 source 之间的 comparison。F04、F05、F07 目前仍是 Candidate Map Only。它们表示科学问题已经被识别，但还不是可执行、可产生 local PASS 的 Rule。

## 20 个案例给出的结果

20 个 case 共产生 40 个必须回答的科学审查问题。其中 14 个被现有 Rule 精确覆盖，23 个只被部分覆盖，1 个需要人类科学判断，1 个是单篇方法问题，1 个暴露了可能的依赖顺序问题。没有发现必须问题完全无对应 family，也没有发现 CASE、SOURCE、EDGE target 被明确分配错误。

F02、F03 和 F06 在经验来源中最稳定地表达了实际审查需要。它们分别处理实验或模拟对象及条件是否清楚、测量原生输出到底是什么，以及两个来源能否以正确的角色和关系放在一起讨论。F04、F05、F07 的问题也经常出现，但它们仍然是 deferred maps，不应被说成系统已经解决这些问题。

## 一个重复出现的过触发问题

当前 F02R01 和 F03R01 只要看到一个 SOURCE 和 `source_id` 就会触发。这样会让它们错误地要求综述、方法论文和 general guide 提供“一个样品组成”和“一个原生测量记录”。这个模式在三个独立来源中重复出现，共造成四个 case、八个不必要的 Rule-instance obligation。

因此留下了一个未实施的候选修复 `CR-001`。未来可以把这两条 Rule 的 SOURCE applicability 收窄到“已承认的 empirical 或 claim-evidence object，且有明确 source purpose”的情形。这个建议还没有修改 Rule。它需要先确认这种 source-purpose 判断不会形成循环。

## 仍需要 source-science 判断的问题

- 一篇整合 NMR、SAXS、SANS、MD 的文章，应视为一个 publication-level source，还是按 modality 拆成多个 source object？
- 构建体/条件信息是否应成为解释 F03 measurement semantics 的显式前置条件？目前只有一个直接例子，还不足以改 Rule。
- Maximum-entropy 的偏差与非唯一性如何进入通用 identifiability 规则？目前仍是方法特异性问题。

## 建议讨论的三个决定

1. `CR-001` 是否已经足够具体，可以单独形成一个小型 Rules vNext proposal？
2. 谁来确定 integrative evidence 的 source-object granularity，以及何时需要从 F02 到 F03 的依赖？
3. 在后续审查里，F04、F05、F07 哪一种反复出现的 Candidate Map need 最值得优先发展成可执行 Rule？

这轮最强的结论是，现有 Rules Table 已被系统地对照过这 20 个 exposed-development case 的 source-first 审查义务，能够清楚区分精确覆盖、部分覆盖、过触发、局部依赖问题和必须由人判断的问题。它还不是科学验证、Rules release、H1 结论或 Agent 价值证明。
