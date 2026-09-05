请继续作为独立科学与工程审阅者，审查原20题的Rules→Operator→额外计算→科学判断能力。不要限于检查我列出的变更；可以审查整个仓库、任意原题、方法、论文及来源，使用你拥有的全部工具，自行做最有价值的复核和反例，质疑任务方向、完成条件与我对你上一轮建议的理解。请明确哪些实读/实算、哪些未验证，结论引用具体来源。本轮无需修改GitHub，审阅建议由我核验实施。

PR https://github.com/alex051107/dynamics-atlas-harness/pull/25
固定head：16f81d89df35619f8256f41f287d3aef8e2151a5
你上一轮锁定4a2c40a；本轮包含1d5423a的实际Q16科学计算，以及16f81d8的Q15验收修复。PR保持OPEN DRAFT，未合并。

原目标保持：以高正确率和实际内容覆盖回答原20个非平凡论文科学问题。当前完整开发答案1/20（Q01），Q05/Q09/Q15/Q16为4题部分实算，其余15未科学运行；人类最终批准0，准确率未测。不把on1/off0、工程反例或未决计为科学正确率。Q01冻结，Q09不再追D24标签，Q02曲线仅保存，Q17仅短来源核准。

先读：research/paper_result_reproduction_screen_v1/CURRENT_STATUS_ZH.md、README.md、questions_20.json、question_progress_v2.json、pro_review_round20/reply.md。下列路径都相对于research/paper_result_reproduction_screen_v1。

一、你的Pro20三个验收发现已一起修复，原数值保留：
- q15_pro20_admission_replay_v2/REPORT_ZH.md、receipt.json、before_defect_reproduction.json：我实复现缺数值、错误producer、越权ceiling被接受。
- q15_admitted_source_receipt_v2.json从此前已审阅4a2c40a的Gitblob建立明确先前来源身份，主计算/摘要/DEER/作者前向及旧背景报告五份均与本地相同。消费不再把新hash自动当验收。正常默认receipt固定，显式替换receipt意味着有意来源重新验收。
- src/dynamics_atlas_harness/q15_cross_modal_evidence_v1.py：评价器核验已准来源，重建便宜的关系/假设/限制并比对传入证据；labels、numbers、limits、hypothesis不能独立修改而被接受。claim ceiling来自重建合同。实际consumer CLI源文件改变反例被拒绝。
- q15_background_policy_v1.py：检查operator/policy/input/instance/alternative及重复覆盖，重新聚合12重复，拒绝总表/重复/选中计数矛盾。有效冲突可完成比较并保留方法依赖。
- replay_q15_pro20_evidence_v2.py零优化回放，五份原报告先核准；旧背景证据仅补policy元数据。原55/175一致、175/228张力及背景方向稳定不变。无新增APBS处理、DEER反演或Rules-extra。
- 来源合同明确FPS FRET_sim为FRET效率平均对应距离，不能推广到任意算术平均。Q15当前完成条件已删“唯一机制证明”，真实缺项是双标TMR/Cy5条件比较/自身校准及有边界的适用性评估。

二、本轮新的科学内容是Q16两位点同窗剂量/保护剂比较：
- q16_rules_probe_v2/为未改DraftRules实际11实例（6声明PASS/4未决/1NA），0数值动作。首版展示问题残留Q15，原始事实/权威投影已是Q16；首版完整保留，修正后原始11结果逐值一致，不追加覆盖。
- q16_condition_inventory_v1/：完整SourceData14块对应10组条件，4个主/SI重复逐值相同不能算额外实验。29/352无保护剂处理窗3.488µs，36/352为3.008；标准50%EG均6.88。raw窗和processed窗不混用。
- q16_common_window_v1/及src/dynamics_atlas_harness/q16_common_window_v1.py、scripts/run_q16_common_window_v1.py：先固定每对所有条件processed非负时间网格交集，不插值。使用raw实部、作者处理后的observed列（排除fit列）、raw/存档background三条路径；中心化/除自身RMS是明确形状约定，另保存原RMSE。没有输入作者拟合分布或状态标签。
- 实际新规则由时长差异触发on1/off0，同实例消费证据：处理后信号去保护剂/1→10mM剂量形状差异比为29/352:3.811、36/352:2.471，另两路径也同排序。25%EG与25%甘油一并算，未逐个位点送审。图和数值都公开。自动输出有界部分判断；无显著性、饱和常数、因果或闭合人口宣称，三路径不是独立重复。
- Q16入口补了同类先前来源身份检查，匹配已保存首个输入后才计算；真实文件变异CLI在operator前拒绝，未重算正常Q16。
- q16_figure5_inventory_v1/：仅159KB左右精确Range目录，651项确为smFRET资料，未下载1.75GB全包。论文Data availability明确EPR在出版社SourceData，Zenodo为smFRET；此档案不补DEER spin预测。SI Table2只找到MalE29/352与36/352 apo的spin预测均值，holo完整模拟分布仍未核准。

Q16当前只得到了真实制备敏感性的信号证据，尚未回答“短窗会掩盖多少长距离成分、无保护剂是否闭合占优”的原题剩余部分。我接下来处理实际长记录截短后的可辨识性/参照问题。请独立判断当前比较是否有效、能支持什么，以及最快且科学有效的下一步；可自己查看/分析原SourceData及方法，勿把我这段说明视为审阅范围限制。现有Python有NumPy/SciPy，未安装DeerLab/MDAnalysis，未获依赖安装授权；这只限制我本地执行，不限制你可用的审阅工具。

三、Q17短核准：q17_source_inventory_v1/记录固定作者repo四套ChRmine精修PDB和官方EMD-32377主/half-map入口；还未下载坐标/map。cc0.8/1.0 SCALE1.4/1.35且体素筛选等不同，不冒称纯噪声权重对照。不启动新精修或大计算。

验证：15项Q15定向测试与335项本地回归通过；之后加的Q16三行来源入口保护由真实变异CLI/原输入身份检查覆盖，初次插入漏行由该检查发现后修正，未重复无变化全仓测试。当前GitHub run33987087993请独立读回实际结果（3.11/3.12）。

请继续给出独立整体判断：修复是否解决真正问题，Q16是否取得符合原目标的科学增量，哪些剩余条件确实必要，哪些应删除或推迟；如果有新的实际反例请给出可复现依据。你可以超出以上清单提出更好的推进路线。不要把审阅通过等同于完整20题、人类科学批准或合并授权。
