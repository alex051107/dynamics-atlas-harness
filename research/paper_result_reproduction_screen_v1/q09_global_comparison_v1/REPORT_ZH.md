# 全33标记对已进入条件比较，数值搜索仍未完成

同一Q09R02规则对33组DA与27份独立文件身份的D0参考派发一次全量比较；参考似然只计一次。共有1,579,504,400个窗内光子，原始计数1,579,507,556，固定原窗口排除3156个。不同文件不等于生物重复，跨变体donor响应可交换性仍未建立。

| 候选 | 当前最低可行deviance | 状态 |
| --- | ---: | --- |
| local2 | 552302.844316 | 有未完成的数值搜索 |
| shared2 | 565108.038837 | 有未完成的数值搜索 |
| shared3 | 561706.720390 | 有未完成的数值搜索 |

23/27个局部参考组通过局部梯度验收，包括2组原结果零优化复用；4组数值stop。新做25次局部优化与4次全局优化，共29次、约678.8秒。全局每次120秒预算到期，所有可行点与各组梯度留下；未把局部失败删除后称全33完成。数值停止组为：local2:D0_07, local2:D0_13, local2:D0_19, local2:D0_20, shared2:0, shared2:1, shared3:0, shared3:1。

当前共享K2与共享K3的候选比例分别为[0.5613827934119625, 0.4386172065880375]、[0.5441730637112365, 0.3895200613928586, 0.06630687489590485]。这是未收敛条件模型的参数，不能作为蛋白态占比估计或论文结果复现。相同参数范围下已找到的localK2比sharedK2低，sharedK3也比sharedK2低；全33不能套用两变体的localK2⊆sharedK3关系。

局部梯度按所属参考组的光子尺度检查，共享比例按总目标尺度检查；优化仍是正确的deviance总和，不把每组任意等权。局部模型保留独立比例，共享模型才共用人口；各组保留原仪器、IRF、Lin与窗，不重采样19–86的混合仪器。

## 方法差距已经具体定位

本批冻结为22–127三donor、其他26参考组双donor的探索性假设，未声称前向适用性通过。随后按已有SI第21页原图核对，作者Table2a有15个三donor标记对，本配置与其中14个不同；source方法计数见../q09_deposited_structure_intake_v1/donor_order_source_audit.json。尤其70–119与70–132使用相同存档D0曲线，却在作者表中分别列三项、两项，原处理/参数共享关系仍不明。没有把作者寿命、振幅或态占比当作求解初值。下一轮需处理具体donor方法差距和求解尺度，再评价模型选择。

## 结构证据确实进入了同一规则重评

规则在有效衰减比较证据到达后要求作者前向结构比较，on执行1次结构Operator/off0。使用作者发布的172L/148L各33个平均染料距离，与本项目正域截断Gaussian实际均值对照。全局K2保留两种结构分配，K3保留六种全局分配；没有逐标记对独立排序或使用作者实验距离/误差/χ²。

shared2描述性RMS最小的全局分配为172L成分1、148L成分0（索引从0起），RMS=23.259Å，最大绝对偏差=86.000Å。所有分配与逐对残差均保留，不将最低RMS提升为已确定结构对应。

shared3描述性RMS最小的全局分配为172L成分0、148L成分2（索引从0起），RMS=19.997Å，最大绝对偏差=68.900Å。所有分配与逐对残差均保留，不将最低RMS提升为已确定结构对应。

没有合格的联合拟合/前向误差模型，因此这些均为描述性偏差，不给显著性或结构通过。作者前向计算与本地ACV运行分开，本地ACV仍0。原JSON单球AV1与正文三半径设置冲突保留；148L是T26E共价酶—产物几何参照，标签链A与作者链E同一实体，作者2019预测所用确切坐标版本未知。详见[结构来源验收](../q09_deposited_structure_intake_v1/REPORT_ZH.md)。

同一规则实例的最终理由包含SOLVER_COMPARISON_INCOMPLETE与AUTHOR_FORWARD_STRUCTURE_COMPARISON_ASSESSED_WITH_LIMITS，结构义务由缺失变为已做描述性比较；蛋白态数和完整科学答案仍未决。完整20题答案0，不能把33个标记对算成33个已答科学问题。

## 原结果、复核与运行

两变体localK2→sharedK3精确嵌入已补，目标13034.163116保持不变，原13次拟合未重跑；最新数值验收增加了强嵌套检查和缓存总计数核准。见[零优化修复结果](../q09_two_variant_nesting_v2/receipt.json)。

本批拟合启动后、发布前增强了生成的原生时间核绑定，原始evidence.original.json保留。零优化重新验收只更换input_id/request_id，所有29次拟合参数、初值、目标和失败保持完全相同；最终验证用现行源码重新计算。structure_evidence.json绑定这份衰减证据及作者前向来源。

280项本地回归PASS，无跳过。聚焦检查11项PASS；最终套件新增总数7项。真实数值复核与结构on/off、同实例重评通过。没有重复旧科学拟合或安装依赖。CI结果在交付receipt中记录。

从仓库根目录使用已有NumPy/SciPy环境，原数据放在INPUT_ROOT（内含eTCSPC_wildtype.zip和unpacked/eTCSPC）。全新运行：

```sh
PYTHONPATH=src OPENBLAS_NUM_THREADS=1 python scripts/run_q09_global_comparison_v1.py --input-root INPUT_ROOT --graph research/paper_result_reproduction_screen_v1/q09_global_comparison_v1/case_graph.json --output-dir NEW_RUN
```

已发布证据零优化回放：

```sh
PYTHONPATH=src OPENBLAS_NUM_THREADS=1 python scripts/replay_q09_global_comparison_v1.py --input-root INPUT_ROOT --evidence-dir research/paper_result_reproduction_screen_v1/q09_global_comparison_v1 --output-dir NEW_REPLAY
```

第一次原始绑定迁移才使用--readmit-pre-kernel-binding；对这里的最终evidence.json不要使用该选项。源ZIP/PDF/PDB未上传，来源与角色明细保留。
