# Soojung 1 对 1 讨论 deck：逐页计划（初稿）

2026-09-10 · 对应文件 `SOOJUNG_DISCUSSION_20260910_EN.pptx`（16 页正文 + 参考文献 + 5 页附录）· 30 分钟，其中讨论 7 分钟

## 会议目的

让 Soojung 判断三件事。整套 workflow 合不合理；先测的三个 system 选得对不对；rules table 最终应该做成什么形式，才能让 Agent 这条线产生增益。

## 主线

从 X 到 Y，因为 Z。从"让 Agent 进入 rules table、按规则调 operation 和补分析"这个原始设想，到"规则按用途拆成四层、逐层实测、只有框题层达标"，因为三个真实体系走完流程后，错误出在数据进来和数字出去两头，不在提醒文字。

## 时间分配

| 段 | 页 | 分钟 |
|---|---|---|
| 原始设想与 workflow | 2–4 | 5 |
| 三个体系走流程 | 5–8 | 10 |
| 每层测了什么 | 9–13 | 8 |
| 怎么搭：讨论 | 14–16 | 7 |

## 逐页计划

| 页 | 标题（完整句子） | 这一页要让她明白的一件事 | 放什么结果 | 图或表 | 数据出处 |
|---|---|---|---|---|---|
| 1 | Dynamics Atlas: the Rules Table, tested on three systems | 今天讨论的是系统怎么搭，不是汇报进度 | 无 | 标题页，四段时间分配 | — |
| 2 | The original idea: an Agent enters the Rules Table and follows a set of rules to choose operations and extra analyses | 原始设想是什么；表是什么，一条规则长什么样 | 11 篇论文、33 条；一条规则原文 C006-RULE-003 | 上半流程图（新体系 → 表 → Agent 按规则选操作 → 数字 → 有边界的答案）；左下字段表；右下规则原文 | rule_registry.tsv |
| 3 | What a new system goes through today, and where the Rules Table acts at each step | 新体系进来后的六步 workflow；表在哪一步起作用 | 六步：intake / package / frame / run / check / report；执行者行；四层对应行 | 六格流程图，下面两行标注（谁执行、哪层） | RULES_TABLE_ROLE_DESIGN_ZH.md |
| 4 | The Agent step is real analysis… for one to two cents | Agent 一次运行到底做什么，能做什么，不能做什么 | 40 次工具调用上限、25 分钟、1 到 2 美分、74 次 1.20 美元 | 三列表（得到什么 / 不能做什么 / 记录什么）+ 黄框说明 Agent 线为什么保留 | Luna runtime v1, CAMPAIGN_PROGRESS.json |
| 5 | HSP90 (Henot 2022): the paper visualises a transiently populated closed state; we tested one property… | 论文本来证明什么；我们挑了哪个性质；差距；规则在首轮怎么起作用 | 论文 7/9/4 vs 我们 10/20 = 5+5、5/4/1；四份答复表，B 组带入 RMP 等条件 | 上表三列（论文 / 我们 / 差距）；下表四份答复 | HSP90_Q01_VERIFIED_REPORT_ZH.md |
| 6 | HSP90, the measurement that mattered: at 1 Å tolerance, 9 of the 10 open-direction trajectories still violate both NOE references | 方向变化不等于到达状态；这个问题是人加的，不是规则给的 | 9/1/0 vs 对照 1/1/18；论文措辞对照 | 左柱图（两组三类），右小表（论文 vs 我们四行）+ 黄框 | v4 NOE crosswalk group_summary.json |
| 7 | DHFR (Cetin 2023): the paper links 4′-DTMP's recovered inhibition of L28R to closer local contacts; we reproduced the distance direction, after finding… | 论文的逻辑；我们的数；差距；输入错误提醒文字防不住 | Ki 表 1 数值；M20–O3P 8.69→4.62、10.44→4.81；VMD 1e-5 Å；两份 Agent 0/2 发现 | 三列表 + 黄框 | dhfr_q01-round-20260910 |
| 8 | ADK (Orädd 2021): the paper tracks a millisecond ATP-binding response…; the deposited apo MD only supports domain-distance descriptions, and it broke my own admission rule | 论文与沉积数据的错位；我自己的准入规则错了；框题在 ADK 上有效 | 四个首末变化；盒长 98–100、延展 56、69.8/62.2 Å；GROMACS 0.005 Å | 三列表 + 黄框 | ADK_SCIENCE_ZH.md |
| 9 | Looking back at 13 error observations in 8 answers: none would have been prevented by more reminder text | 错误在哪一步；什么能防 | 13 处、7 个同因组、3 处重放检出 | 五行归因表（错误 / 步骤 / 提醒能否 / 什么能防） | E0_RETROSPECTIVE_AUDIT.csv |
| 10 | So the 33 rules were split by job into four layers; the design question became "what information reaches the Agent…" | 四层各自回答什么、谁执行、Agent 收到什么 | 6/10/11/6 | 五列表 | RULES_TABLE_ROLE_DESIGN_ZH.md §2 |
| 11 | Each layer got its own falsifiable test: what changed, what we expected…, and the criterion written down before running | 三个测的问题的前因后果和预期 | 每层：触发事件 / 唯一变量 / 题与次数 / 预设标准 | 五列表 + 脚注（评分方式） | FOUR_LAYER_VALIDATION_PLAN_ZH.md |
| 12 | Result: only explicit sub-questions met its criterion; the admission card, method cards and one feedback pass did not | 四层结果和判定；Q05 例外 | 覆盖 2→2.5、2→3；卡 0/4；HSP90 4.5/2/2.5、Q05 4.5/5/4.5；反馈 1/3、0/12、0/9 | 四行表，红绿判定列 | UNBLINDED_SCORES.csv |
| 13 | Why each layer failed is more useful than that it failed: delivery, applicability and traceability are three different problems | 三种失败机制各指向什么修法 | 卡列出 4/4 读 0/4；HSP90 取到 1 张 BME 卡、DHFR/ADK 0 张；重放 0/7、1 误报 | 三行表 | E1B_CARD_ACCESS_AUDIT.json 等 |
| 14 | How the Rules Table should be built from here: three forms… | 以原始设想为锚的三种形式；证据分别支持到哪 | 形式 1 修四层；2 规则服务协议作者；3 规则变成算子配置 | 五列表 + 黄框（我倾向 3，以 2 为基线） | 第 12、13 页 |
| 15 | Are the three systems the right ones? By the criterion "MD plus an experiment that constrains the difference…", only HSP90 fully qualifies | 判三个体系的标准；下一个体系要什么 | 论文结果 / 我们结果 / 实验约束 / 测了什么 / 是否保留 | 六列表 + 黄框问第四个体系 | 第 5–8 页 |
| 16 | Conclusions, and the three things I need from you | 三句结论；三个要她答的问题 | — | 三条 + 黄框三问 | — |
| 17 | References | — | — | 列表 | — |
| A1–A5 | 能说不能说 / 33 条按层 / 逐组分数 / 费用 / 术语 | 备查 | — | 表 | — |

## 每页备注

每页 notes 里有英文讲稿（SAY）和一条追问预案（GRILL）。中英对照的完整讲稿见 `SOOJUNG_SPEAKER_SCRIPT_BILINGUAL.md`。

## 已知取舍

- 不写谁做了什么（人、Codex、Claude、Pro 的分工）。
- 不引用 8/24 她的原话。
- DHFR 冻结前没做物理检查，slide 上写 "curator-side defect"，不展开。
- 三个体系页都详细，每页一个三列表（论文 / 我们 / 差距）加一行"表在哪一步起作用"。
- 第 14 页三种形式都摆，第二种标明"放弃了原始设想"，我的倾向写在黄框里。
