# 两份ADK普通答复与原文的逐句关系

两份来自相同冻结资料的独立普通Agent运行；它们不是两条新的MD轨迹。局部定义和四个首末变化由开发者独立重算，论文关系按正文与SI核对。

| 答复/原文片段 | 原始资料位置 | 核对与边界 |
|---|---|---|
| V037：“NMP…+0.0707…LID…+2.2904” | 冻结open_domain_distances.tsv，首/末各225帧；ADK_INDEPENDENT_RECOMPUTE.json | 新计算正确，不是论文报告值。 |
| V037：“闭态…+1.0909…+1.1764” | closed_domain_distances.tsv，首/末各167帧 | 新计算正确；窗口0–33.2与302.2–335.4ns。 |
| V037：“4.3 ms…TR-XSS…结构精修” | Orädd2021正文Results、Fig4；本地paper.md第41、55–57、65–83行 | 对应实验瞬态与模型解释，不从两个均值推出毫秒速率。 |
| V037：“MD为303.15 K…TR-XSS…294 K” | 正文Materials and Methods及SOURCE_CARD.md | 正确区分条件；沉积坐标无ATP/AMP。 |
| V045：“开态…主要是LID…闭态…两者…相近” | 两份冻结距离表；独立重算 | 对有限首末窗口成立；不能推广成普遍协同路径。 |
| V045：“项目域集合为LID118–160、NMP30–67…” | FIELD_DEFINITIONS.md；正文域定义段 | 主动说明项目子集与论文定义不同，避免冒充作者原始距离。 |
| V045：“最佳拟合的10个结构对显示…部分闭合” | 正文Results、补充FigS4–S6 | 论文借结构对散射拟合解释实验，当前距离表没有检验其散射拟合或盐桥机制。 |
| V045：“每个条件只有一条轨迹” | SOURCE_CARD.md及两条沉积轨迹 | 正确；未写实验/模拟温度差，盲评记条件单元缺失，不记科学错误。 |

论文：Orädd等，2021，Science Advances，doi:10.1126/sciadv.abi5514；[公开全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8597995/)；[沉积资料](https://zenodo.org/records/5583119)。原文与SI作为两个来源保存于ADK冻结包。V037、V045完整原答见blind目录和ADK_plain原始运行档案；不能用本表替换原答。
