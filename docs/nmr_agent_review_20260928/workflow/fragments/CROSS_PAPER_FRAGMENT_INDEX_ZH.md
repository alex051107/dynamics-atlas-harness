# 跨论文决策片段索引（首批五篇，交 Codex 流程线）

2026-09-26。五篇论文共 37 条片段：AdK 2015 7 条、IL-2 2020 8 条、K-Ras 2023 8 条、RfaH 2012 6 条、RfaH 2025 8 条。逐条内容见同目录 `DECISION_FRAGMENTS_*_ZH.md`；每条有原文定位、明确/重建标签、Agent 对应类型和对 Codex 提示原句的合同效果。

对照的是 Codex 当前的求解提示 `docs/science_workflow/SYSTEM_PROMPT.md`。37 条里没有与它抵触的；它的六段结构可以承载全部卡点，但有 10 处写得太笼统，科学家实际会做的动作没有落到字面上。下面先给这 10 条修改建议，再给按段的明细。

## 给 Codex 段合同的 10 条修改建议

| # | 段 | 建议写进合同的动作 | 依据片段 | 影响的原句 |
|---|---|---|---|---|
| R1 | inventory | 每条证据标注物种、构建体、编号体系和测量条件；跨物种、跨构建体合用前给出等价性证据，否则分列 | AdK 3；RfaH2025 1；K-Ras 1 | "inventory: distinguish measured inputs, derived quantities, references, and missing controls." |
| R2 | inventory | 信号缺失（未归属区段、看不到的次要态峰、平坦的弥散曲线、低于检测限）要作为信息记录，并写明方法窗口；不当作阴性 | AdK 1、2；IL-2 1；RfaH2012 1 | "Do not infer a scientific negative from unavailable data, tool errors, or an execution budget limit." |
| R3 | inventory → discriminate | 主动找对照：过程应当不存在或应被改变的样品（另一配体态、突变体、切割构建体），并在 discriminate 里分析它 | K-Ras 5；RfaH2012 4、5；IL-2 5 | "missing controls" |
| R4 | baseline | 用一种数据拟合出的模型，接受前要去预测另一种数据（CEST 模型预测 CPMG、两个磁场互相预测）；预测失败是模型错，不是噪声 | RfaH2025 3；K-Ras 2 | "When … results conflict, inspect the affected evidence and review the discrepancy." |
| R5 | discriminate | 状态数的阶梯规则：只在某类数据未被解释时加一个态；每一步列出候选拓扑和拟合优度；χ² 接近 1 且残差无系统结构时停止；拓扑分不出时并列报告，只把在各拓扑下都稳定的量写进结论 | RfaH2025 4、5；K-Ras 2；IL-2 2 | "Do not presume a number of conformational states, topology …" |
| R6 | discriminate | 用选择性扰动把交换归到具体过程：比较不同配体、金属、突变条件下的 kex、布居和 Δω；只作用于一个过程的扰动最有区分力 | AdK 5；IL-2 5、7；RfaH2012 3 | "choose a check that can distinguish them" |
| R7 | interpret | 次要态结构：在同一残基交集上、逐区与多类参照比较（其他配体/构建体的实测态、序列无规卷曲预测、锁定某态的突变体）；同源模型或位移驱动建模（CS-ROSETTA 类）得到的参照标为假设 | K-Ras 3；IL-2 3、4；RfaH2025 6、7、8；RfaH2012 2 | "compare plausible references on comparable data" |
| R8 | interpret | 偏离最佳参照的残基：先检查局部化学（离两态间不同的配体基团多近），再谈构象差异；用结构做参照前核对其关键配体和金属的归属 | K-Ras 4；AdK 6 | "explain discrepancies without treating resemblance as a unique mechanism or a solved structure." |
| R9 | interpret | 给交换过程命名功能步骤，需要独立测量（动力学、结合）一致；证据的时间尺度与所论过程不匹配时降为假设 | AdK 4、7；IL-2 6；K-Ras 6 | "Each candidate claim states its scope, epistemic status, evidence references and limits."；"State what the tools cannot test." |
| R10 | synthesize | 条目范围等于样品范围（孤立结构域不写成全长蛋白）；文献对应（如"state 1"）、功能关联单独标为外部知识或假设 | RfaH2025 1；RfaH2012 6；K-Ras 7、8 | "Use epistemic_status observed, model_conditioned, or hypothesis." |

## 按段明细

| 段 | 片段 | 卡点类型 | Agent 对应 |
|---|---|---|---|
| frame | AdK 3；RfaH2025 1；K-Ras 1 | 样品与构建体决定结论上限；跨物种合用 | 可执行（标注与等价性检查）/ 结论边界 / 湿实验不作为动作 |
| inventory | AdK 6；IL-2 1；RfaH2025 2；K-Ras 5 | 参照结构的配体归属；信号缺失；次要态归属；对照样品 | 多数可执行（PDB、BMRB 公开） |
| baseline | RfaH2025 3；IL-2 2；RfaH2012 1 | 全局模型能否预测另一类数据 | 可执行（需原始数据：K-Ras、RfaH 2025 有） |
| discriminate | K-Ras 2、5；IL-2 2、5、7；AdK 1、5；RfaH2012 3、4、5；RfaH2025 4、5 | 状态数与拓扑；交换区间；选择性扰动；伪影与对照 | 状态数、对照在有原始数据时可执行；扰动多为建议实验 |
| interpret | K-Ras 3、4、6；IL-2 3、4、6、8；AdK 2、4、7；RfaH2012 2；RfaH2025 6、7、8 | 多参照逐区比较；偏离残基；功能归属；时间尺度；模型结构的地位 | 参照比较可执行；功能归属多为结论边界 |
| synthesize | K-Ras 7、8；RfaH2012 6；IL-2 8 | 外部知识与功能关联的标注；待测的传递路径 | 结论边界 + 建议实验 |

## Agent 对应类型的分布

按各文件末尾汇总表的主类型统计（37 条）：可在数据库环境直接执行 20 条（AdK 3、IL-2 5、K-Ras 5、RfaH 7；多依赖 BMRB、PDB，以及 K-Ras、RfaH 2025 的原始弛豫数据），结论边界 10 条，只能作为建议实验 6 条（湿实验：温度系列、扰动样品、切割构建体、滴定），湿实验且不作为动作 1 条（K-Ras 1）。

这个分布说明两件事：只有当原始交换数据公开时，Agent 才能重做 baseline 和 discriminate 两段的核心动作；而 interpret 段的多参照比较、偏离残基的化学解释，大多只靠公开位移库和结构库就能做。

## 两处需要 Codex 线裁定的开放问题

1. R5 的停止规则比多数作者实际做得更严：IL-2 与 K-Ras 的作者没有比较多态模型，直接采用全局两态（IL-2 2、K-Ras 2）。合同采用 R5 时，评测里"没有比较多态模型"应记为过程缺失，而不是结论错误。
2. R7 中"锁定某态的突变体参照"通常要靠文献先验才找得到（K-Ras 运行里 Agent 靠对 T35S 的先验知识找到 BMRB 52072）。合同是否允许求解会话使用这类先验检索、以及如何标注，需要定下来。

## RfaH 2025 作为下一个开发案例的封存划分

按用户 2026-09-26 批准的默认划分执行，补充片段文件中提出的两点：Figshare 存档里的 MATLAB 拟合程序（编码了作者的五态拓扑、初值和权重）与 `outputs/` 结果一并封存，只放行原始数据与实验参数；存档目录名本身写有"5state""4state""branched/linear"，构建工作区时要改成中性名称。详见 `DECISION_FRAGMENTS_RFAH_2012_2025_ZH.md` 末节。
