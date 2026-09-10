### Goal
两个决定：(1) 负责人现在下一步该做什么，以及这件事与最初目标的关系；(2) Rules Table 到底该是什么形式。对附件给出的"四层角色设计"和"四层验证实验"作可执行的裁决：原样执行、改哪几处并给替换文字、或不执行。

### Background
- 最初目标（PROJECT_MEMORY G1–G4）：从 MD、NMR、散射、FRET 等异质蛋白动力学资料得到有用、可复核、不过度的科学回答；比较不同来源的 landscape；固化可复用流程；Agent 是后置的、可独立失败的假设。
- 你 9 月 8 日的战略审查判定：Rules Table 作为可审阅载体合适，作为推断引擎未证明必要，作为研究组织中心不建议继续；推荐"科学问题 + 协议 + 成熟方法 + 逐项报告"，引擎与 Agent 作为待比较的执行方式。9 月 8 日概念审查要求规则围绕"待区分的科学差异"组织、约束推断关系而非给来源评级。8 月 17 日审查要求把表拆成 papers / source_rules / rule_index，判定由评价程序算。
- 此后实际发生：9/10 HSP90 一题四答复（A 普通 ×2、B 注册表规则提示 ×2）判 row 3 暂停扩展；v4 收口、原生 NOE 对照（1 Å 容差下 10 条开放方向轨迹中 9 条仍同时偏离两套 NOE 参照）、渲染修复；DHFR 一轮普通 Agent ×2（冻结后才发现坐标周期性缺陷，两份 Agent 均未识别）；ADK 只有盘点。费用累计 $0.108。
- 新提出的设计（附件 1）：33 条规则按性质拆成四层，框题（6 条，模板 + 人）、准入（10 条，冻结前代码检查）、分析（11 条，按方法族检索的短方法卡，唯一以文字给 Agent 的一层）、结论（6 条，提交后确定性检查一次反馈 + 报告措辞）。回溯本项目六个已发生错误：零个能靠提示文字防住，五个能靠准入或结论层代码防住，两个要靠框题层。
- 验证实验（附件 2）：E0 回溯审计（$0）；E1 准入检查器 + 六类植入缺陷 + Agent 拿卡/不拿卡；E2 提交后上限检查反馈 D vs D+检查；E3 按族方法卡 vs 整段规则 vs 七条手写协议；E4 拆题 vs 原题。每层跑前冻结有效/无效标准，盲评，72 次运行 ≤ $1.85，不限天数。
- 材料（GitHub，提交 `c2fefbc`，PR #26 所在分支 `review/rules-agent-study-plan-20260909`）：
  1 四层角色设计 https://github.com/alex051107/dynamics-atlas-harness/blob/c2fefbc3afa93f9d4204b2ebffb63b987cfdd21b/review/rules-agent-study-20260909/development-results/PRO_FORM_REVIEW_PACKET_20260910/01_RULES_TABLE_ROLE_DESIGN_ZH.md
  2 四层验证计划 v2（不限天数） https://github.com/alex051107/dynamics-atlas-harness/blob/c2fefbc3afa93f9d4204b2ebffb63b987cfdd21b/review/rules-agent-study-20260909/development-results/PRO_FORM_REVIEW_PACKET_20260910/02_FOUR_LAYER_VALIDATION_PLAN_ZH.md
  3 你三份分析的结论汇总与实际工作对照 https://github.com/alex051107/dynamics-atlas-harness/blob/c2fefbc3afa93f9d4204b2ebffb63b987cfdd21b/review/rules-agent-study-20260909/development-results/PRO_FORM_REVIEW_PACKET_20260910/03_FORM_QUESTION_ANSWERED_ZH.md
  4 按 G1–G4 的现状计划表 https://github.com/alex051107/dynamics-atlas-harness/blob/c2fefbc3afa93f9d4204b2ebffb63b987cfdd21b/review/rules-agent-study-20260909/development-results/PRO_FORM_REVIEW_PACKET_20260910/04_DYNAMICS_ATLAS_PLAN_TABLE_20260910_ZH.md
  5 博文摘要 https://github.com/alex051107/dynamics-atlas-harness/blob/c2fefbc3afa93f9d4204b2ebffb63b987cfdd21b/review/rules-agent-study-20260909/development-results/PRO_FORM_REVIEW_PACKET_20260910/05_BLOG_SUMMARY_ZH.md
  6 T4L 论文摘要与评价边界 https://github.com/alex051107/dynamics-atlas-harness/blob/c2fefbc3afa93f9d4204b2ebffb63b987cfdd21b/review/rules-agent-study-20260909/development-results/PRO_FORM_REVIEW_PACKET_20260910/06_PAPER_SUMMARY_T4L_JCIM_ZH.md
  7 博文原文 https://github.com/alex051107/dynamics-atlas-harness/blob/c2fefbc3afa93f9d4204b2ebffb63b987cfdd21b/review/rules-agent-study-20260909/development-results/PRO_FORM_REVIEW_PACKET_20260910/07_are-we-capturing-the-ensemble.md （Li, Thomasen, Cossio, RS Station 2026-08-31，https://rs-station.github.io/2026/08/31/are-we-capturing-the-ensemble.html ）
  8 论文原文 PDF https://github.com/alex051107/dynamics-atlas-harness/blob/c2fefbc3afa93f9d4204b2ebffb63b987cfdd21b/review/rules-agent-study-20260909/references/03_acs.jcim.6c02044.pdf 与 SI https://github.com/alex051107/dynamics-atlas-harness/blob/c2fefbc3afa93f9d4204b2ebffb63b987cfdd21b/review/rules-agent-study-20260909/references/05_ci6c02044_si_001.pdf （Bhakat, JCIM 2026, DOI 10.1021/acs.jcim.6c02044；文本版 https://github.com/alex051107/dynamics-atlas-harness/blob/c2fefbc3afa93f9d4204b2ebffb63b987cfdd21b/review/rules-agent-study-20260909/references/04_acs.jcim.6c02044.md ）
  你此前三份分析的原文在本机，未上传；以你自己的记录为准。5、6 是我的摘要，7、8 是原文；有出入以原文为准。若连接器读不到某个文件，写明哪些结论只依据本消息，不要把未见文件说成已审阅。

### Claims to verify
C1. 四层拆分与你 9 月 8 日"规则围绕待区分的科学差异组织、约束推断关系"的建议一致：框题层对应"要区分什么"，准入层对应"对象与条件、处理记录"，分析层对应"前向模型与平均律"，结论层对应"这份数据能说到哪"。
C2. 33 条按 `rule_class` 归入四层的分配（附件 1 §2 表）没有明显归错的规则；若有，指出规则编号与应归层。
C3. "只有分析层以文字给 Agent，其余三层在 Agent 之前由代码/模板、之后由代码/评分执行"，与 SYSTEM.md 的授权分工（Agent 提议、确定性系统拥有验证/路由/数值/上限、人拥有竞争解释）一致，且不构成新的自证路径。
C4. 附件 1 §3 的回溯表：六个错误中"提示文字能防 0 个、代码能防 5 个、框题能防 2 个"的归因成立；若某一项应改归其他层，给出理由。
C5. E1 的六类植入缺陷（周期性假距离、单位错、帧数不符、时间列打乱、条件标签互换、证据角色标错）覆盖了准入层 10 条规则要防的主要错误类；干净包零误报作为该层"未达标"的一票否决是合适的。
C6. E2 的四项确定性检查（上限词带条件、数字可溯源、统计单位与窗口、证据角色未混）作为结论层的最小实现是可执行的，且"只退回一次、不给数值"足以避免检查器代写答案。
C7. E3 的预期"HSP90/DHFR/ADK 只能取到 C007、C012 两族的少数方法卡"本身是关于表覆盖范围的有效结果，不应被解读为方法卡层无效。
C8. E4 的拆题模板（差异 / 证据约束 / 同读数的其他解释 / 请求层级）与博文"先验证目标差异是否留在可用信息里，再选推断方法"的要求一致，且竞争解释仍由人定。
C9. 四个实验的"有效/无效"标准（附件 2 §0 表）是可以失败的，且任何一层无效都不否定科学交付。
C10. 按 G1–G4 看，现在的下一步应是"先做 E0 与 E1a（零成本、纯代码），同时继续 ADK 科学交付；D/P/R 两轮由四层实验替代"，而不是先扩表、先重跑同题或先建引擎。
C11. 附件 5、6 两份摘要没有歪曲原文：博文的核心是"哪些分布差异在测量和处理后仍可区分"，不规定实现形式；T4L 论文最扎实的贡献是"起始结构选择改变有限时间内能采到什么"，而"四区域 ≠ 四个实验亚稳态、占比相近 ≠ 定量一致、smFRET 对照只验证一个信号特征"这些边界成立。四层设计里框题层的"覆盖 / 权重 / 实验辨识 / 机制"子问题划分与这两篇的含义一致。

### Strategic questions
S1. Rules Table 的最终形式应是：四层各自落成代码/模板/卡/检查器，表退为可重建的索引 | 保留单张表并加 `layer` 标签，只改渲染 | 不拆层，按你 8 月 17 日的三张表重构后再说。
S2. 下一步顺序应是：E0→E1a→ADK 交付→E2/E3/E4 | 先完成三体系科学交付再做任何实验 | 先做 E3（表作为提示的价值）因为它最直接回答"表有没有用"。
S3. 结论层检查器如果在干净包上出现误报，处理应是：该层判未达标并停止 | 允许一次阈值修正后重测 | 改为只记录不反馈。
S4. 对负责人"我不知道这个东西要做成什么形式"的回答，应写成哪一句：附件 1 §0 那句 | 你 9 月 8 日的最低复杂度推荐那句 | 另一句（请给出）。

### Output contract
C1–C11 每条恰好一个标签：
- VERIFIED <材料编号与节号>
- WRONG <替换文字：可直接粘贴进材料对应节的中文，Codex 拿到不用再问人>
- DATA_INSUFFICIENT <缺什么>
S1–S4 各给一个选项加一句理由。
最后用一段话回答负责人的两个问题：现在该做什么、Rules Table 该是什么形式；每句都要能对应到附件的节号或你之前审查的节号。
标签之间不加议论。不用置信度词。不复述材料。

### Stop conditions
- C1–C11、S1–S4 与最后一段全部作答后停止。总长 ≤ 1800 字。
- 不要求恢复三体系并行、24 份比较、五组六测试组的大实验或 Rules + Agent 组合组；不把再一轮审批设为开工条件。
- 引用博文给节名，引用你此前审查给节号，引用材料给编号与节号；无法核实的写 DATA_INSUFFICIENT，不推断。
