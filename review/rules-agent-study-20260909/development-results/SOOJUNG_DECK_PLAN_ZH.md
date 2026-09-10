# Soojung 1 对 1 讨论 deck：逐页计划（初稿）

2026-09-10 · 对应文件 `SOOJUNG_DISCUSSION_20260910_EN.pptx`（18 页正文 + 参考文献 + 6 页附录；v2，按独立审查意见重排）· 30 分钟，其中讨论 7 分钟

## 会议目的

让 Soojung 判断三件事。整套 workflow 合不合理；先测的三个 system 选得对不对；rules table 最终应该做成什么形式，才能让 Agent 这条线产生增益。

## 主线

从 X 到 Y，因为 Z。从"让 Agent 进入 rules table、按规则调 operation 和补分析"这个原始设想，到"规则按用途拆成四层、逐层实测、只有框题层达标"，因为三个真实体系走完流程后，错误出在数据进来和数字出去两头，不在提醒文字。

## 时间分配

| 段 | 页 | 分钟 |
|---|---|---|
| 原始设想、workflow、案例与比较设计 | 2–4 | 6 |
| 三个体系走流程 | 5–9 | 10 |
| 每种用途测了什么 | 10–15 | 7 |
| 怎么搭：讨论 | 16–18 | 7 |

## 逐页计划

| 页 | 标题（完整句子） | 这一页要让她明白的一件事 | 放什么结果 | 图或表 | 数据出处 |
|---|---|---|---|---|---|
| 1 | Dynamics Atlas: the Rules Table, tested on three systems | 今天讨论的是系统怎么搭 | 无 | 标题页 | — |
| 2 | The original idea: an AI analyst enters the Rules Table and follows the rules to choose operations and extra analyses | 原始设想；表是什么；一条规则长什么样 | 11 篇、33 条；C006-RULE-003 原文 | 流程图 + 字段表 + 规则原文 | rule_registry.tsv |
| 3 | What a new system goes through today: six steps, and the table can act at four of them | 六步 workflow；表在哪一步起作用（用白话名：data checks / question framing / method guidance / conclusion checks） | 六步、执行者、四种用途 | 六格流程图 + 两行标注 | RULES_TABLE_ROLE_DESIGN_ZH.md |
| 4 | How anything here was tested: four cases, a criterion for choosing them, and the same comparison design throughout | 四个案例（含纳米盘开发案例）；选体系的标准；condition / grading key / core unit 的定义 | 案例表；术语表 | 两张表 | Bengtsen 2020；FOUR_LAYER_VALIDATION_PLAN_ZH.md |
| 5 | HSP90 (Henot 2022): the paper shows a transiently populated closed state; on the same 40 trajectories we asked one narrower question, direction persistence | 论文本来证明什么；我们问了什么；两种分区不必相等 | 论文 7/9/4 vs 我们 10/20 = 5+5、5/4/1 | 首轮审计图（10/20、5/20 柱图）+ 论文/我们小表 | HSP90 首轮 fig_02 |
| 6 | HSP90, the measurement that mattered: at 1 Å tolerance, 9 of the 10 open-direction trajectories end far from both NOE references | 离开闭态 ≠ 到达开态；这个问题是人加的 | 9/1/0 vs 对照 1/1/18；2 Å 下 3 条 | 逐轨迹末窗口散点图（x 闭态违例、y 开态违例、三条容差线）+ 小表 | per_trajectory_crosswalk.tsv（新图） |
| 7 | HSP90, first comparison: rules pasted into the prompt did not improve the counts and imported conditions that belong to FRET | 第一版规则用法的具体害处 | 四份答复表；泄漏来源两条规则 | 四行表 + 黄框 | HSP90_Q01_VERIFIED_REPORT_ZH.md |
| 8 | DHFR (Cetin 2023): the paper links 4′-DTMP's recovered inhibition of L28R to closer local contacts; we reproduced the direction, after finding an input artifact | 论文逻辑；修正前后；输入错误提醒文字防不住 | Ki；8.69→4.62、10.44→4.81；0/2 发现 | 修正前后 M20–O3P 距离直方图（四条件，3.5 Å 参考线）+ 小表 | derived / derived_mic 逐帧表（新图） |
| 9 | ADK (Orädd 2021): the paper tracks a millisecond ATP-binding response; the deposited ligand-free MD supports only domain-distance descriptions, and it broke my own data check | 论文与数据的错位；半盒长规则错在哪 | 四个变化；56 Å 延展、69.8/62.2 Å | LID/NMP–CORE 距离时间序列（首末窗口阴影）+ 小表 + 黄框 | E1a/reference/ADK 逐帧表（新图） |
| 10 | Looking back at every answer so far: 13 error observations, none preventable by reminder text; they sit at data entry and at the numbers going out | 错误住在哪一步 | 13 处、7 组、3 处重放检出 | 五行归因表 | E0_RETROSPECTIVE_AUDIT.csv |
| 11 | The Agent step is real analysis: sealed container, read-only data, Python written and run, a structured answer submitted, one to two cents per run | Agent 一次运行做什么；为什么保留 | 40 次调用、25 分钟、1 到 2 美分 | 三列表 + 黄框 | Luna runtime v1 |
| 12 | So the 33 rules were split by job into four uses; the design question became: what information reaches the Agent, in what form, at which step | 四种用途各自回答什么、谁执行、Agent 收到什么 | 6/10/11/6 | 五列表 | RULES_TABLE_ROLE_DESIGN_ZH.md §2 |
| 13 | Each use got its own test that could fail: what triggered it, the one thing changed, and the pass criterion written down before running | 三个测的问题的前因后果与预期 | 触发 / 唯一变量 / 题与次数 / 预设标准 | 五列表 + 脚注 | FOUR_LAYER_VALIDATION_PLAN_ZH.md |
| 14 | Result: only explicit sub-questions met its criterion; the data-check card, method cards and one feedback pass did not | 四行结果与判定；框题增益来自人写的子问题；Q05 例外 | 覆盖 2→2.5、2→3；0/4；4.5/2/2.5、4.5/5/4.5；1/3、0/12、0/9 | 四行表，红绿判定 | UNBLINDED_SCORES.csv |
| 15 | Why each use failed matters more than that it failed: delivery, applicability and traceability are three different problems | 三种失败机制指向的修法 | 卡 4/4 列出 0/4 读；HSP90 1 张 BME 卡、DHFR/ADK 0 张；重放 0/7、1 误报 | 三行表 | E1B_CARD_ACCESS_AUDIT.json 等 |
| 16 | How the Rules Table should be built from here: three forms, what each assumes, and what this round's evidence says about each | 以原始设想为锚的三种形式；形式 2 证据最强但放弃设想；形式 3 的论证桥（真正起作用的检查都是物理的、可执行的） | 三行表 | 五列表 + 黄框 | 第 14、15 页 |
| 17 | Are the three systems the right ones? By the criterion from slide 4, only HSP90 fully qualifies; DHFR and ADK earned their place as workflow tests | 三个体系的判定；要第四个体系 | 六列表 | 表 + 黄框 | 第 5–9 页 |
| 18 | Conclusions, and the three things I need from you | 三句结论；三个问题 | — | 三条 + 黄框 | — |
| 19 | References | — | — | — | — |
| A1–A6 | 能说不能说 / 33 条按用途 / 逐组分数 / 费用 / HSP90 三条示例轨迹图 / 术语 | 备查 | — | 表、图 | — |

## 每页备注

每页 notes 里有英文讲稿（SAY）和一条追问预案（GRILL）。逐页念的中英对照讲稿见 `SOOJUNG_SLIDE_SCRIPT_BILINGUAL.md`；不按页、把每件事讲透的扫盲稿见 `SOOJUNG_FULL_EXPLANATION_ZH.md`。

## v2 相对 v1 的改动（依据独立审查）

- 新增第 4 页：四个案例（含纳米盘开发案例）、选体系的标准、condition / grading key / core unit 定义，解决第 5 页之后术语悬空。
- HSP90 拆成科学、NOE 对照、首轮对照三页；每个体系页配一张她能自己判断的图（散点 + 容差线、修正前后直方图、结构域距离时间序列）。
- Agent 运行页后移到测试设计之前。
- 第 3 页去掉 A–D 字母标签，改白话名；第 12 页才定义 A–D。
- 第 14 页写明框题增益来自人写的子问题；第 16 页补上从证据到形式 3 的论证桥，形式 2 标为当前证据最强。
- 附录 A1 "评分者独立于建包者"改到不能说的一列；新增 A5 三条示例轨迹图。

## 已知取舍

- 不写谁做了什么（人、Codex、Claude、Pro 的分工）。
- 不引用 8/24 她的原话。
- DHFR 冻结前没做物理检查，slide 上写 "curator-side defect"，不展开。
- 三个体系页都详细，每页一张图加一个小表（论文 / 我们），黄框写"表在哪一步起作用"。
- 第 16 页三种形式都摆，第二种标明"放弃了原始设想"，我的倾向写在黄框里。
