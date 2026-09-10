# Luna开发结果与下一项科学比较

先读[下一阶段行动计划](NEXT_SCIENTIFIC_STEP_ZH.md)，再读[修订报告](DEVELOPMENT_REPORT_ZH.md)。需要转交Pro时可复制[完整审查提示](PRO_NEXT_STEP_PROMPT_ZH.md)。[领域核对简报](DOMAIN_REVIEW_BRIEF_ZH.md)列出专家需要确认的具体科学边界。

本次采纳[Pro返回审查](PRO_DEVELOPMENT_REVIEW_ZH.md)的归因纠正，完成一次[离线答案保存修复](post_development_review/README.md)。没有新增模型会话、科学拟合、规则或正式题。

十二次历史运行的初稿、终稿、回执和执行记录均保留。第二批T4L B/C初稿和终稿分别展示，离线回放不会替代真实终稿计分。

[运行费用](development_results.json) · [科学核对](SCIENTIFIC_AUDIT_ZH.md) · [原低成本计划](LOW_COST_EXECUTION_PLAN_ZH.md)

原DEVELOPMENT_REVIEW_PACKET.zip保留最初开发交付，未包含本次报告修订。阅读当前计划和结论请使用本目录最新Markdown。执行记录省略重复request，保留模型响应、工具结果和错误。完整原始请求保留本地，来源见父目录references；此包未包括全部矩阵，不是完整离线复现环境。

## 2026-09-09 晚：三体系操作计划（替代 NEXT_SCIENTIFIC_STEP_ZH.md 的下一阶段方案）

- [THREE_SYSTEMS_OPERATIONAL_PLAN_ZH.md](THREE_SYSTEMS_OPERATIONAL_PLAN_ZH.md)：建 Rules 回路系统 → HSP90 四站 → 结果包交 Pro → ADK/DHFR 只读盘点按规则选一个 → 第二、第三体系。每步含输入、动作、输出、完成标准、停止条件。暂不等领域专家，Pro 审结果包；结论保持"开发暴露、未领域确认"。
- [PRO_CONFIRM_THREE_SYSTEMS_PROMPT_ZH.md](PRO_CONFIRM_THREE_SYSTEMS_PROMPT_ZH.md)：请 Pro 审查该计划的提示。
- `NEXT_SCIENTIFIC_STEP_ZH.md` 中的"四来源 × 3 组 × 2 次 = 24 份"比较停放，未启动。

## 2026-09-09 深夜：Pro 审查 v1 → HSP90 首轮有界计划 v2（供 Codex 执行）

- [PRO_REVIEW_OF_OPERATIONAL_PLAN_V1_ZH.md](PRO_REVIEW_OF_OPERATIONAL_PLAN_V1_ZH.md)：Pro 对 v1 的完整审查（CHANGES_REQUESTED_BOUNDED）。两处事实纠错已本地复核为真。
- [HSP90_FIRST_ROUND_PLAN_V2_ZH.md](HSP90_FIRST_ROUND_PLAN_V2_ZH.md)：v2。一个问题（Q01）、同一 Agent、A/B 各两次共四份、C 停、7 个工作日、≤ $0.20；评分依据独立于规则选择；`common/ arm_B/ hidden/` 三分隔离；三列核对；两层报告；四结果表由 PM 决定下一步。§11 逐条处置 Pro 意见。
- [REVIEW_PROMPT_HSP90_FIRST_ROUND_V2_ZH.md](REVIEW_PROMPT_HSP90_FIRST_ROUND_V2_ZH.md)：给审阅者的提示（十问，强调执行者是 Codex）。
- `THREE_SYSTEMS_OPERATIONAL_PLAN_ZH.md`（v1）已标 superseded，保留为记录。

## 2026-09-09 深夜（二）：Pro 审查 v2 → v3 交付版（供 Codex 执行）

- [PRO_REVIEW_OF_PLAN_V2_ZH.md](PRO_REVIEW_OF_PLAN_V2_ZH.md)：Pro 对 v2 的完整审查（CHANGES_REQUESTED_BOUNDED，"改几处后执行，不再重做路线设计"）。
- [HSP90_FIRST_ROUND_PLAN_V3_ZH.md](HSP90_FIRST_ROUND_PLAN_V3_ZH.md)：v3 交付版。范围、规模、费用上限、七天到期与 v2 相同。改动：运行器显式 `--task-root`、A/B 去掉公开事实依赖、共同提示改指实际文件、挂载断言按实际可读范围、`FIELD_DEFINITIONS.md` 七条字段含义（每轨迹三行、departure 相对第一个持续方向、帧数式时间约定）、B0 分"论文声明 / 本轮输入已核对"、元数据角色改为"开发者整理未经领域确认"、核对看全文、§8 加"混合/负面/不稳定"行、选择器失败与运行器修改两个分支、B4 跳过。§11.1 逐条处置 Pro 意见；§11.2 列本机核实 v2 引用后新增的修正（注册表实为逗号分隔、选择器状态门槛、旧 readiness 为 false、Docker 镜像无构建记录、无 MDAnalysis、AMBER99SB 出自 Zenodo 描述、主张矩阵是指针文件、收敛题输入的真实位置等）。
- [REVIEW_PROMPT_HSP90_FIRST_ROUND_V3_ZH.md](REVIEW_PROMPT_HSP90_FIRST_ROUND_V3_ZH.md)：给审阅者的核对提示（六问，只核对处置是否到位，不再审路线）。
- `HSP90_FIRST_ROUND_PLAN_V2_ZH.md` 已标 superseded，保留为记录。

## 2026-09-10：Pro 审查 v3 → v3.1（交付版，直接交 Codex）

- [PRO_REVIEW_OF_PLAN_V3_ZH.md](PRO_REVIEW_OF_PLAN_V3_ZH.md)：Pro 对 v3 的审查（CHANGES_REQUESTED_BOUNDED，主要处置已到位，五处局部文字修正后执行）。
- [HSP90_FIRST_ROUND_PLAN_V3_ZH.md](HSP90_FIRST_ROUND_PLAN_V3_ZH.md)：已就地更新为 v3.1，§11.3 逐条处置：A1 先于 A0、规则渲染保留对象与检查配对、B0 来源差异分别保留、字段定义移出汇总结果与答题提示、A-only 分支贯穿 §5–§7。这是交 Codex 执行的版本。

## 2026-09-10：v3.2 一次授权、条件推进（明天开工版）

- [HSP90_FIRST_ROUND_PLAN_V3_ZH.md](HSP90_FIRST_ROUND_PLAN_V3_ZH.md)：v3.2 = v3.1 + §1 授权 1–9 + §8A 自动判定规则 + §14 第二、第三体系的条件推进（顺序、不并行；只读盘点后按写死规则选 ADK 或 DHFR；总停止线 21 个工作日 / $0.60 / 4 GB）。PM 贴一句"授权 1–9，按 v3.2 执行"即可开工。
- [REVIEW_PROMPT_HSP90_PLAN_V3_2_ZH.md](REVIEW_PROMPT_HSP90_PLAN_V3_2_ZH.md)：给 Pro 审 v3.2 新增部分（§8A、§14、授权 6–9）的提示，九条待核主张加两个选项题。

## 2026-09-10：v3.3 交付版（Pro 对 v3.2 的七处替换已合入）

- [PRO_REVIEW_OF_PLAN_V3_2_ZH.md](PRO_REVIEW_OF_PLAN_V3_2_ZH.md)：Pro 对 v3.2 新增部分的审查（C1–C6、C8 WRONG 附替换文字；C7、C9 VERIFIED；S1 改后执行；S2 Codex 判、PM 可叫停）。
- [HSP90_FIRST_ROUND_PLAN_V3_ZH.md](HSP90_FIRST_ROUND_PLAN_V3_ZH.md)：v3.3，§11.4 逐条处置。PM 贴"授权 1–9，按 v3.3 执行"即开工。

## 2026-09-10：v3.4 + 汇报协议

- [POST_RUN_REPORTING_PROTOCOL_ZH.md](POST_RUN_REPORTING_PROTOCOL_ZH.md)：跑完自动出报告的协议。轮末：PM 简报 HTML + 深度读本 HTML/PDF + 组会 slides PPTX + 索引；停止：只出停止简报；周末：一页周报。指定 skill 顺序（atlas-science-report → plain-project-reporting-zh / storytelling-narrative → academic-pptx → academic-ppt / data-visualization → nature-figure → matplotlib / human-writing → humanizer-zh-plus），明确不用 weekly-report、scholar-slides、nature-paper2ppt。
- [HSP90_FIRST_ROUND_PLAN_V3_ZH.md](HSP90_FIRST_ROUND_PLAN_V3_ZH.md)：v3.4 = v3.3 + §15 汇报协议；每轮加 1 天汇报，HSP90 首轮上限 8 天，总停止线 21 天不变。

## 2026-09-10：首轮结果的本机审查 → v4 计划 + 报告写作指南

- [REVIEW_HSP90_ROUND1_LOCAL_ZH.md](REVIEW_HSP90_ROUND1_LOCAL_ZH.md)：对 PR #27 `3ba975e` 的独立审查。用冻结源表重算全部计数（一致）；row 3 动作保留、理由改；补出 5/5/10 分区表；核出 §15 汇报包缺失、REPLAY/HTML/STATUS 未更新、论文关系表为模板、凭证启动例外；确认作者 NOE 违例序列在本机。
- [HSP90_ROUND2_PLAN_V4_ZH.md](HSP90_ROUND2_PLAN_V4_ZH.md)：接首轮之后的执行计划。A0 进度报告 → A 首轮收口 → B 派生方向 vs 原生 NOE 对照（本机数据，预注册规则）→ C 规则渲染层窄修复 → D 第二体系普通 Agent。一次授权 1–7，15 个工作日 / $0.30 / 2 GB。
- [REPORT_WRITING_GUIDE_ZH.md](REPORT_WRITING_GUIDE_ZH.md)：怎样写逻辑严密、别人看得懂的报告：一句主线、五拍结构、固定骨架、段落写法、边界句、deck 写法、冷读检查、项目时间线骨架、节奏规则。

## 2026-09-10：三体系收官令

- [THREE_SYSTEMS_COMPLETION_ORDER_ZH.md](THREE_SYSTEMS_COMPLETION_ORDER_ZH.md)：现状表（HSP90 两轮完成、DHFR 一轮完成未入库、ADK 只有盘点）、偏离审查、授权 8–10、DHFR 入库 → ADK 建包（冻结前物理硬门）→ 两次普通 Agent → 三体系总记录 + 工作证据表与红旗清单。
- [DYNAMICS_ATLAS_PLAN_TABLE_20260910_ZH.md](DYNAMICS_ATLAS_PLAN_TABLE_20260910_ZH.md)（[HTML](DYNAMICS_ATLAS_PLAN_TABLE_20260910_ZH.html)）：按 G1–G4 的完整计划表、时间线、今天汇报的 14 页页序与可说/不可说清单、下一步总表。
- [RULES_HARNESS_INCREMENT_ROUNDS_2_3_ZH.md](RULES_HARNESS_INCREMENT_ROUNDS_2_3_ZH.md)：增量效益测试第二、三轮。A/B/C 三组（普通 / Rules / Rules+Harness 确定性检查一次反馈），每组每题 4 次；第二轮 3 题（HSP90 原生对照、DHFR 缺陷表、DHFR 修正表），第三轮 ADK 2 题（Rules 未见过）；评分依据与检查器运行前冻结，盲评，预注册判定表；≤ $1.50、7 个工作日。
- [ONE_SHOT_ORDER_ZH.md](ONE_SHOT_ORDER_ZH.md)：一口气跑完的总令：DHFR 入库 → 第二轮增量测试 → ADK 收官 → 第三轮 → 总报告 + 一页 RULES_TABLE_VERDICT（第一行三选一）。授权 8–14，11 个工作日，≤ $1.55。
- [FORM_QUESTION_ANSWERED_ZH.md](FORM_QUESTION_ANSWERED_ZH.md)：9 月 8 日报告与 Pro 三轮分析对"该不该做 Rules Table"的结论汇总，与 9 月 9–10 日实际工作的对照；结论：形式已收敛，要改的是测试设计（D/P/R，R−P 才是问题）。
- 增量测试与一口气总令改为 v2：三组 D（整理资料）/ P（七条手写协议）/ R（注册表规则），不设 Harness 组；判定改用 Pro 的质量/效率两条路径。
- [RULES_TABLE_ROLE_DESIGN_ZH.md](RULES_TABLE_ROLE_DESIGN_ZH.md)：Rules Table 在系统里该放在哪的四层设计（框题 / 准入 / 分析 / 结论），33 条按层归类，六个已发生错误的回溯审计表，每层最小实现，对 D/P/R 测试的含义。
- [FOUR_LAYER_VALIDATION_PLAN_ZH.md](FOUR_LAYER_VALIDATION_PLAN_ZH.md)：四层设计的验证实验：E0 回溯审计（$0）、E1 准入检查器 + 植入缺陷、E2 提交后上限检查反馈、E3 按族方法卡 vs 整段规则 vs 协议、E4 拆题 vs 原题；每层跑前冻结有效/无效标准；72 次运行、≤ $1.85、14 个工作日。替代一口气总令的 D/P/R 两轮。
- [PRO_FORM_REVIEW_PACKET_20260910/](PRO_FORM_REVIEW_PACKET_20260910/)：给 Pro 的"形式与下一步"审查包：00 提示（C1–C11、S1–S4）、01 四层设计、02 四层验证计划 v2（不限天数）、03 形式问题汇总、04 计划表、05 博文摘要、06 T4L 论文摘要、07 博文原文；论文 PDF 与 SI 在 references/03、05。
- [WHERE_WE_ARE_ZH.html](WHERE_WE_ARE_ZH.html)：给负责人的说明书。最初的科学问题、博文与 T4L 论文带来的设计指令、已跑出的证据、四层系统最终形态、Rules Table 的归宿、当前进度、四个实验各自在证明什么。
- [DYNAMICS_ATLAS_FULL_LOGIC_AND_QA_ZH.html](DYNAMICS_ATLAS_FULL_LOGIC_AND_QA_ZH.html)（[Markdown](DYNAMICS_ATLAS_FULL_LOGIC_AND_QA_ZH.md)）：全程说明与问答。13 个阶段的逻辑表、三个转折点、四层系统与实测进展、中途纠正过的判断、合作者/方法审查/大厂面试三类问答（含英文 90 秒版本）、数字速查与术语。WHERE_WE_ARE_ZH.html 同步修正了过时进度和混用的错误计数。
