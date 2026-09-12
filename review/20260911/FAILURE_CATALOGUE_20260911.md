# 失败目录：AI 运行与流水线在哪些地方表现差

2026-09-11。目的：把已发生的具体失败列全，给团队判断哪种形式的规则本可以防住每一处。不做汇总评价，只列观察、定位和防护形式的证据状态。

来源：`autoresearch/tasks/dynamics_atlas_one_shot_20260910/four_layer/outputs/`（E0 审计表、四层报告、E2 提示审查、E2 修订对照、E3 探索审查、E1b 卡访问审计、逐份原始分数）、`autoresearch/tasks/dynamics_atlas_operator_plan_20260911/outputs/`（报告、偏差记录、盲评分数、运行回执、16 份盲评答复）、`PROJECT_HANDBOOK_20260911_ZH.md` 第三部分（HSP90 逐步复盘）、`dynamics-atlas-harness-showcase/DEFINITIONS.md` 与 `RESULTS.md`、`dynamics-atlas-harness-luna-runtime-v1/review/dhfr_q01-round-20260910/AGENT_AUDIT_ZH.md`。路径均相对工作区根目录 `Soojung-Dynamic data/`。

## 一、逐条失败

| 编号 | 发生在哪一轮 | 发生了什么 | 阶段 | 根因类别 | 本可以防住它的规则形式 | 我们有没有证据这种形式有效 |
|---|---|---|---|---|---|---|
| 1 | HSP90 首轮 A2（零 Python 调用） | 把 5 点阈值的方向计数（11/9）写成另一阈值的数字，`answer.md:8` | 分析 | 转述不计算 | 算子前置条件（数值主张绑定 OP1 输出的 `result_id`） | 有，部分：`dynamics-atlas-harness-showcase/RESULTS.md`"Checking numbers"一节——按算子绑定重放 8 份历史答复，抓到 7 处目标错误里的 6 处，含本条；旧的 `ceiling_check.py` 对同一批 0/7（`autoresearch/tasks/.../E0_COUNTS.json`） |
| 2 | HSP90 首轮 A2 | 同一段落内 4/20 与 5/20 自相矛盾，`autoresearch/tasks/dynamics_atlas_one_shot_20260910/four_layer/outputs/E0_RETROSPECTIVE_AUDIT.csv` 第 2 行 | 分析 | 转述不计算 | 算子前置条件 | 有，同上（RESULTS.md 同一重放批次） |
| 3 | HSP90 首轮 A2 | 50 点阈值下把实际为 1 的相反候选数写成 0，同一份 `answer.md:8` | 分析 | 转述不计算 | 算子前置条件 | 有，同上 |
| 4 | HSP90 首轮 B1（规则组，`HSP90_Q01_B_b909c96b`） | 把 FRET 专用的 RMP restraint/prior ensemble 前提当作本题（NMR/MD）必填项，`answer.md:24` | 分析 | 不适用条件迁移 | 算子前置条件（前置条件写在算子卡自己身上，模型看不到规则原文） | 无，尚未测：`PROJECT_HANDBOOK_20260911_ZH.md` §2.1 只给出改写示例，未跑新一轮验证 |
| 5 | HSP90 首轮 B1（另一份输出 `HSP90_Q01_B_8813dc0f`） | 同一类前提误迁移，`answer.md:39` | 分析 | 不适用条件迁移 | 算子前置条件 | 无，同上 |
| 6 | HSP90 首轮 B1 | 把 50 ns 分箱结果称为"规则"箱、暗示可作独立统计单位，`answer.md:18`，实际箱内 CONFLICT 比例高（闭合起始 420 箱中 108 CONFLICT） | 判断 | 定义错误 | 算子前置条件（OP 输出自带统计单位说明） | 无，尚未测 |
| 7 | DHFR 普通 Agent A1（`DHFR_Q01_A_07534f46`） | 分析了物理上不成立的周期性镜像伪距离（18–94 Å），未识别/降级，`answer.md:25`；独立审计见 `dynamics-atlas-harness-luna-runtime-v1/review/dhfr_q01-round-20260910/AGENT_AUDIT_ZH.md` | 分析 | 输入缺陷 | 数据检查代码（建包时抽帧重算，容差 0.01 Å） | 有：`autoresearch/tasks/dynamics_atlas_operator_plan_20260911/outputs/OPERATOR_PLAN_REPORT_ZH.md` §4 记录新一轮抽帧核对最大差异 5.1411399333e-06 Å，PASS；这是同一缺口在后续任务里被实际堵上的证据 |
| 8 | DHFR A1 | WT N18–O3P 近距离比例转述错误（写约 9.2→15.7%，原表 9.09→44.24%），`answer.md:25` | 分析 | 转述不计算 | 算子前置条件 | 有：RESULTS.md 重放批次把 DHFR 转录错误列为"8, 9, 11"，6/7 检出里包含它们 |
| 9 | DHFR A1 | W22–O3P 近距离比例转述错误（写约 0.9→33.1%，原表 1.92→80.30%），`answer.md:25` | 分析 | 转述不计算 | 算子前置条件 | 有，同上 |
| 10 | DHFR A2（`DHFR_Q01_A_ef5da470`） | 把伪距离长尾直接解释为"构象切换"，`answer.md:62` | 分析 | 输入缺陷 | 数据检查代码 | 有，同第 7 行（后续任务抽帧核对已实装并 PASS） |
| 11 | DHFR A1 | L28R N18 均值转述反转了原表方向，`answer.md:25`；独立复核见 `autoresearch/tasks/dynamics_atlas_one_shot_20260910/four_layer/outputs/E0_N18_ORIGINAL_MEAN_CHECK.json` | 分析 | 转述不计算 | 算子前置条件 | 有，同第 1 行重放批次 |
| 12 | 纳米盘 / Q05（`Q05_C_4a249b26`） | 构造的 NOE 上限数组按原子对错位，`answer.md:17` | 分析 | 定义错误 | 算子前置条件（需新建 NOE 边界构造算子） | 无：`dynamics-atlas-harness-showcase/RESULTS.md`"Checking numbers"一节明确写"error 12 ... has no operator to check against"——这一条目前没有任何算子能查 |
| 13 | T4L（`T4L_C_be4d6c40`） | 提交流程里的确认语覆盖了已提交的科学答案，`answer.md:1` | 运行器 | 其他（提交管线缺陷） | 恢复规则（保留原始提交，确认语不得覆盖） | 有，部分：E0 审计表标记 `detected_on_replay: YES`，"prior offline replay in DEVELOPMENT_REPORT lines40,54"——问题在交付机制层面被事后重放发现过，但尚无提交时自动阻断的证据 |
| 14 | 四层测试 E1b 准入卡组（4 次运行） | 给了 Agent 准入卡文件，4 次全部只在工具日志里出现文件名、卡内容 0/4 被读取，`autoresearch/tasks/dynamics_atlas_one_shot_20260910/four_layer/outputs/E1B_CARD_ACCESS_AUDIT.json` | 数据准入 | 其他（提供的材料未被消费） | 数据检查代码（准入检查移进建包脚本，任一 FAIL 不出 `FREEZE.json`，不再指望 Agent 主动读卡） | 无：`PROJECT_HANDBOOK_20260911_ZH.md` §2.5 只是设计提案；`OPERATOR_PLAN_REPORT_ZH.md` §4 显示新一轮准入确已移到建包阶段且全部 PASS，但这一轮没有注入缺陷做检测率测试，不能证明检出率 |
| 15 | 四层测试 E2（结论检查器 `ceiling_check.py` 对 8 份历史答复重放） | 目标 7 处数值错误 0 处检出，唯一一次提示是误报（把 Å⁻¹ 指数 −1 当未匹配数字），`autoresearch/tasks/dynamics_atlas_one_shot_20260910/four_layer/outputs/FOUR_LAYER_VALIDATION_REPORT_ZH.md` §二 | 检查 | 其他（检查器只查"数字出现过"，不查数字对不对） | 算子前置条件（把"出现过"检查换成"绑定到 result_id 后比对具体字段"） | 有：同一批历史答复换成绑定检查后 6/7 检出（`RESULTS.md`），是同一批数据上两种检查形式的直接对照 |
| 16 | 四层测试 E2（9 次 `numeric_trace` 提示） | 9 条提示全部被判定为科学错误的误报，包括漏掉 V018 真实存在的 NA 归类错误，`autoresearch/tasks/dynamics_atlas_one_shot_20260910/four_layer/outputs/E2_FLAG_REVIEW.json` | 检查 | 其他 | 算子前置条件 | 有，同第 15 行（同一失败模式，同一替代方案的证据） |
| 17 | 四层测试 E2（反馈组，12 份初稿到终稿） | 核心错误数中位数未降低，3 份丢失了可回答内容，其中一份（V064）同时削弱了旧的方向措辞、又新增一处 LID/NMP 方向错误，`autoresearch/tasks/dynamics_atlas_one_shot_20260910/four_layer/outputs/E2_REVISION_COMPARISON.json` | 检查 | 修订丢内容 | 恢复规则（修订只能追加，不能覆盖已核实内容） | 无，尚未测新设计 |
| 18 | 四层测试 E3（整段规则组，`R_old`→`整段规则`对照） | 把 33 条规则原文整段贴给模型后，HSP90 核心正确中位数从协议组 4.5/5 掉到 2/5，核心错误从 0 升到 1.5，`autoresearch/tasks/dynamics_atlas_one_shot_20260910/four_layer/outputs/FOUR_LAYER_VALIDATION_REPORT_ZH.md` §六 | 分析 | 不适用条件迁移 | 算子前置条件（规则内容只作为算子的前置条件和参数范围，不再整段进提示） | 无，尚未测新设计；唯一现有证据是"整段文字"这一形式本身反而拖累了结果 |
| 19 | 四层测试 E3（方法卡组） | HSP90 方法卡组核心正确中位数 2.5/5，仍未达到不劣于协议组（4.5/5）的冻结标准，同上文件 §六 | 分析 | 不适用条件迁移 | 算子前置条件 | 无，尚未测 |
| 20 | 四层测试 E3 | 方法卡主判据（是否肯定采用 R0/dye/AV/RMP 为必要条件）在协议/整段规则/方法卡三组全部为零，无法据此区分三组表现，同上文件 §六 | rubric | 覆盖不全 | rubric 条目（改按"当前要求哪种计算"的操作标签检索，而不是按 NMR/SAXS 方法族） | 无：`autoresearch/tasks/dynamics_atlas_one_shot_20260910/four_layer/outputs/E3_EXPLORATORY_REVIEW_ZH.md` 末段只是提出这一建议，"不是本轮已证明的新实现" |
| 21 | 四层测试 E3（逐句探索性审查） | 方法卡内容与当前操作不匹配，仍被部分采纳或引入不必要的说明：V068（BME/MaxEnt 前提与当前 NOE 违例对照无关）、V072（识别出不适用仍添加卡片的核准状态措辞）、V057（正确指出纳米盘/IDP 不匹配，仍写一段非必要状态说明），`autoresearch/tasks/dynamics_atlas_one_shot_20260910/four_layer/outputs/E3_EXPLORATORY_REVIEW_ZH.md` | 分析 | 不适用条件迁移 | 算子前置条件 | 无，尚未测 |
| 22 | 四层测试 E4（框题/拆题对照） | 拆题把 HSP90 子问题覆盖从 2/3 提到 2.5/3，但核心错误总数从 1 增加到 2（中位数持平），`autoresearch/tasks/dynamics_atlas_one_shot_20260910/four_layer/outputs/FOUR_LAYER_VALIDATION_REPORT_ZH.md` §七 | 问题 | 覆盖不全 | rubric 条目（四栏框题模板，每个子问题标注必需算子，见 `PROJECT_HANDBOOK_20260911_ZH.md` §2.4） | 无，尚未测新模板 |
| 23 | 四层测试 E4（拆题版 SPLIT，`HSP90_Q01_SPLIT_0248b83c`） | 40 次调用预算中只用 7 次、0 次 Python，43 秒后交卷，第 (2) 小节写"本阶段没有逐条计算 NOE 违例"，题面要求的数据就在 `/source/native_noe/` 下，`PROJECT_HANDBOOK_20260911_ZH.md` §3.4 | 分析 | 跳过计算 | 算子前置条件（提交门要求每个子问题先跑对应 `run_operator`） | 有，间接：同一设计在算子绑定臂（O-arm）上把 HSP90 从 58.333% 提到 98.333%、ADK 从 73.611% 提到 100%（`autoresearch/tasks/dynamics_atlas_operator_plan_20260911/outputs/OPERATOR_PLAN_REPORT_ZH.md` §5），但拆题+零计算这一具体失败模式本身没有被同批数据重放 |
| 24 | 归档 80 次运行整体统计 | 每次运行调用 Python 的中位数为 2 次，4 次运行零 Python；系统提示只写"需要计算时实际执行"，不强制计算，`PROJECT_HANDBOOK_20260911_ZH.md` §0 与附录 A | 运行器 | 跳过计算 | 算子前置条件（提交门） | 有，同第 23 行（O-arm 对比） |
| 25 | 算子化评审当日（9 月 11 日） | OP6 参照邻域定义（半径取 NMR 系综 95 百分位 lid RMSD）未过控制：99.99% 开放起始帧落在两参照之外，与同一批里 18/20 轨迹和开放 NOE 一致矛盾，`dynamics-atlas-harness-showcase/DEFINITIONS.md` §3 | 判断 | 定义错误 | 体系预期规则（项目规则表里已有的 C005-RULE-001——"空间支持不同的量不能直接比较"——作为新算子定义冻结前的强制前置检查） | 无，且是负面证据：`dynamics-atlas-harness-showcase/RESULTS.md` 末段明确写"规则表已经有这条教训（C005-RULE-001），它没有被用到我们自己的定义上"——规则存在但没有被结构性地应用 |
| 26 | 算子化评审当日 | OP3"占比是否收敛"定义：0.05 阈值未标定，全窗口与自身比较恒为零，约 51% 的帧被判"两者皆非"，`dynamics-atlas-harness-showcase/DEFINITIONS.md` §4 | 判断 | 定义错误 | 结论上限（团队自己把这一行降级为"not usable as run"，只留描述性窗口比较） | 有：本条本身就是"结论上限"这一形式在评审阶段成功拦下过强结论的实例（未被写成 population 占比） |
| 27 | 算子化评审当日（ADK） | DHFR 事故后新增的通用检查——"任何超过半盒长的距离都判错"——在 ADK 上误报：62 Å、70 Å 的分子内合法距离超过 98 Å 盒长的一半，`dynamics-atlas-harness-showcase/RESULTS.md` §4"What it showed about the rules" | 检查 | 定义错误 | 数据检查代码（需要按测量类型分支：跨分子距离用最近镜像，分子内距离用完整分子） | 有，负面：这条检查本身在 ADK 上就是错的，证明未分支的通用规则不可靠 |
| 28 | HSP90 与 DHFR 建包阶段（长期存在） | 派生表与原始坐标之间从未做抽帧核对（`xtc_spot_check: NOT_ATTEMPTED`），是 DHFR 周期性伪距离能进入分析的同一缺口，`PROJECT_HANDBOOK_20260911_ZH.md` §3.2 | 数据准入 | 输入缺陷 | 数据检查代码（抽 3 帧从 xtc 重算，差 > 0.01 Å 判 FAIL） | 有：同第 7 行，`OPERATOR_PLAN_REPORT_ZH.md` §4 记录该检查已实装，最大差异 5.14e-06 Å，PASS |
| 29 | 算子计划轮（9 月 11 日）盲评 | 第二盲评人全程不可用，`agreement rate` 未测，`SCORING_DISAGREEMENTS.md` 明确没有填写虚构的分歧数字，`autoresearch/tasks/dynamics_atlas_operator_plan_20260911/outputs/blind/SECOND_SCORER_STATUS.json`、`SCORING_DISAGREEMENTS.md` | 评测 | 评分循环 | 恢复规则（评分人缺失时明确标注 `NOT_AVAILABLE`，不得据此编造一致率） | 有：本条就是"不编造缺失数据"这条恢复规则被正确执行的实例 |
| 30 | 算子计划轮运行器 | 首次模型 pilot 出现 `TOKEN_LIMIT`（HSP90 O-arm）与 `RESOURCE_LIMIT`（ADK D/O-arm），冻结从 rev1 改到 rev6 才稳定，`autoresearch/tasks/dynamics_atlas_operator_plan_20260911/outputs/DEVIATIONS.md` §1 | 运行器 | 运行限制 | 恢复规则（保留失败 pilot 目录，不为好看重跑已成功的 slot；截断工具读回；D-arm 16 次调用软锁） | 有：16/16 正式 D/O slot 最终全部到达 `COMPLETE`（`RUN_RECEIPTS_SUMMARY.csv`），修复未触碰已成功 slot |
| 31 | 算子计划轮 D-arm（自由分析臂，8 份答复） | 8 份 D-arm 答复全部未给出任何题目要求的数值，因工具调用/读取长度限制在此前设置中把读取切断，例：`autoresearch/tasks/dynamics_atlas_operator_plan_20260911/outputs/blind/answers/blind_07.md`"I cannot responsibly determine the four requested results from the fixed packet in this session..."；同类另见 blind_03/10/11/12/13/15/16.md；`dynamics-atlas-harness-showcase/RESULTS.md`"Rules as operators"一节独立确认"Seven of the eight free-analysis answers state that they could not read the question files and give no numbers" | 运行器 | 运行限制 | 算子前置条件（同一批题目换成 O-arm 后完成率从 58%/74% 升到 98%/100%，`OPERATOR_PLAN_REPORT_ZH.md` §5） | 有：本条与第 32 行、第 23/24 行共同构成本目录里最强的一组对照证据 |
| 32 | 算子计划轮 O-arm（算子绑定臂） | 算子已跑，仍有 blind_08、blind_09 未完整报告 persistence=20/50 的方向数值，组均 `operator_coverage`/`question_completeness` 停在 1.9/2.0，`autoresearch/tasks/dynamics_atlas_operator_plan_20260911/outputs/OPERATOR_PLAN_REPORT_ZH.md` §5 | 分析 | 覆盖不全 | rubric 条目（需要"每个参数值都要报告"的显式完整性检查，而不只是"算子跑过"） | 无，尚未测新 rubric |
| 33 | 多轮反复出现（HSP90/DHFR，UNBLINDED_SCORES.csv） | 相关性被写成因果的过强结论反复出现：V028"首末均值支持显著的构象可逆性"、V016"通过特定接触网络获得更强抑制表型"、V074 把接触增强直接归因抑制改善，`autoresearch/tasks/dynamics_atlas_one_shot_20260910/four_layer/outputs/UNBLINDED_SCORES.csv` | 判断 | 其他（因果升级） | 结论上限 | 有：这些实例本身是靠评分表里的 `overclaim` 列在评分阶段被系统性标出的（同一 CSV 逐份记录 overclaim=1），证明"结论上限"作为打分依据能稳定捕捉这类过强表述，但只在评分后发现，不是提交前拦截 |
| 34 | HSP90 定义设定阶段 | 结构域比对用的核心残基范围（40–97、137–220）与论文原文（11–97、137–223）不一致，记录中未查到原因，`dynamics-atlas-harness-showcase/DEFINITIONS.md`"Common setup" | 数据准入 | 定义错误 | 体系预期规则（冻结前要求逐项核对论文原定义，偏离必须显式记录理由） | 无：目前是被动发现（写审查文档时才注意到），没有主动核对机制 |

## 二、汇总计数

### 按根因类别

| 根因类别 | 条数 | 编号 |
|---|---:|---|
| 转述不计算 | 6 | 1, 2, 3, 8, 9, 11 |
| 不适用条件迁移 | 5 | 4, 5, 18, 19, 21 |
| 定义错误 | 6 | 6, 12, 25, 26, 27, 34 |
| 输入缺陷 | 3 | 7, 10, 28 |
| 跳过计算 | 2 | 23, 24 |
| 覆盖不全 | 3 | 20, 22, 32 |
| 修订丢内容 | 1 | 17 |
| 运行限制 | 2 | 30, 31 |
| 评分循环 | 1 | 29 |
| 其他 | 5 | 13, 14, 15, 16, 33 |
| **合计** | **34** | |

### 按可能的防护形式

| 防护形式 | 条数 | 编号 | 现有效果证据 |
|---|---:|---|---|
| 算子前置条件 | 18 | 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 15, 16, 18, 19, 21, 23, 24, 31 | 强：8 处（第 1/2/3/8/9/11/15/16 行）在同一批历史答复上实测有效（RESULTS.md 6/7 检出）；第 23/24/31 行有 O-arm 对 D-arm 的成绩对照（58–74% → 98–100%）；其余 8 处（4/5/12/18/19/21/32 相关设计提案）尚未跑新一轮验证 |
| 数据检查代码 | 5 | 7, 10, 14, 27, 28 | 一半已实测：第 7/10/28 行的抽帧核对在算子计划轮已实装并 PASS；第 14 行的建包阶段准入门还未做注入缺陷检测测试；第 27 行是负面证据（未分支的通用检查本身出过错） |
| 恢复规则 | 4 | 13, 17, 29, 30 | 部分已验证：第 29/30 行在算子计划轮里被实际执行且确认有效；第 13 行只有一次事后重放证据；第 17 行的"修订不得覆盖"尚未在新设计里测试 |
| rubric 条目 | 3 | 20, 22, 32 | 无：三条都还是设计建议，没有跑过对照 |
| 体系预期规则 | 2 | 25, 34 | 负面证据为主：第 25 行说明"规则已存在但没被结构性应用"，第 34 行是设计缺口 |
| 结论上限 | 2 | 26, 33 | 有：两条都是"结论上限"已经在评审或评分阶段实际拦下过强表述的正例，但都发生在事后审查，不是提交前拦截 |
| 文字提示 | 0 | — | 本目录里没有一条失败是靠"文字提示"这一形式被证明防住的；相反，第 18 行是"整段文字规则"本身把结果拖差的证据 |
| 无规则能防 | 0 | — | 第 12 行目前实质等同于"无规则能防"（尚无算子可查），未单独归类 |

## 三、表现最差的三处

**第一，"零计算转述"这一根因贡献了全部 34 条里的 8 条（第 1/2/3/8/9/11/23/24 行），是单一最大的错误来源。** 它不是靠文字提醒能解决的：HSP90 首轮规则组（B1，第 4/5 行）确实读了规则、也确实照办了，办的是不适用的事；而零计算的答案（A2、拆题版 SPLIT）根本没有触发任何规则判断的机会，因为它们没有算。唯一在同一批数据上被证明有效的形式是"算子前置条件+绑定检查"：把"提交"这个动作本身变成"必须先有一次算子调用产出的 `result_id`"，同一套题从 58–74%（D-arm）提到 98–100%（O-arm，第 23/24/31 行）。这说明规则表下一步该往哪走已经有答案：文字规则和整段规则（第 18 行）不只是无效，甚至会拖累结果；能验证起作用的只有"把规则变成运行时强制的前置条件"这一种形式。

**第二，方法卡/整段规则层（C 层）贡献了 5 条"不适用条件迁移"（第 4/5/18/19/21 行），且是本目录里唯一有直接负面数字的类别：HSP90 核心正确中位数从协议组 4.5/5 被规则本身拖到 2/5（整段规则）或 2.5/5（方法卡）。** 这与"规则表没用但至少无害"的预期不同——规则表原文进入提示后，不是空转，是主动引入了新的错误（FRET 专用前提被套到 NMR 题上）。这也解释了为什么 2.1 节的改写方案把"适用条件"放在四句话的第一句：现在的检索方式（按方法族）本身就是这条失败的根因，第 20 行的方法卡主判据（R0/dye/AV/RMP）在三组里全部为零、完全没有区分力，证明当前的规则表检索粒度对这道题从未真正起效，无论文字怎么改都改不动"检索错了论文"这件事，除非把 rubric 条目从"方法族"换成"操作标签"。

**第三，运行环境本身（运行限制+数据准入长期缺口）贡献了独立于内容对错的一整类失败：8/8 的自由分析臂答复因读取长度/调用次数限制而完全交白卷（第 31 行），HSP90/DHFR 长期没有抽帧核对（第 7/10/28 行），第二盲评人始终缺席（第 29 行）。** 这类问题的共同点是：防住它们靠的都不是"规则内容"，而是"运行器和建包脚本层面的强制机制"（数据检查代码、恢复规则），且这是本目录里证据最扎实的一类——抽帧核对已经实装并通过（差异 5.14e-06 Å），O-arm 相对 D-arm 的完成率提升是本目录唯一有干净对照组的数字。这三处合起来指向同一个结论：接下来该投入的不是"写更多规则"，而是"把已经证明有效的运行时强制机制（算子前置条件、建包期数据检查）覆盖到还没覆盖的算子（如第 12 行的 NOE 边界构造）和还没测的场景（第 14/17/20/22/25/32/34 行的设计提案）"。
