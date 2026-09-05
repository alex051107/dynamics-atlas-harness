# Dynamics Atlas：Rules Table 与 Agent Harness Master Plan

> 版本：v2.5
> 日期：2026-09-05
> 状态：Q01开发题级答复完成并获Pro科学内容审阅通过，覆盖1/20；Q09按实证续算，人类最终科学批准待审
> 适用范围：Dynamics Atlas prototype、Rules runtime、Profile Agent、Harness、registered operators 与科学验证路线

## 文档边界

本计划把三类信息分开记录：

- **Observed**：已经存在并可从本地 artifact 或运行 receipt 验证的事实；
- **Design**：本项目已经选择、后续实现必须遵守的架构；
- **Future**：尚未实现，也不能写成当前能力的功能。

文献证据、历史 Rule ID 和 source locator 继续保存在原有 Rules 资产中。本计划只规定这些资产如何进入 runtime，不重新解释论文，也不借架构文档提升任何 scientific claim。

---

# 0. 决策摘要

Dynamics Atlas 是一个 **scientific workflow compiler**：系统把用户问题、论文和数据整理成结构化 case，使用带来源的 Rules 编译出 case-specific scientific obligations，再通过已有证据、registered scientific operators 或人工判断解决这些 obligations，最终返回带 claim ceiling 和完整 trace 的 bounded conclusion。

本轮执行顺序已由用户在 2026-09-04 明确调整。

1. 从原始研究论文中选择 20 个具有科学内容、能够由数据与计算检验的问题。
2. 每题先说明论文结论、数据、比较对象、所需计算和选择理由。
3. 后续取得数据后，保持现有 Rules Table 不变，检查它能否选择合适的 Operator、要求必要的补充计算，并产生支持或不支持该结论的证据。
4. 比较实际结果与事先登记的论文结果，先定位最大、反复出现的失败，再决定改 Rules、补 Operator 或补数据。
5. 首轮计划与筛选已交付。用户随后授权首批至多 3 题的小规模数据取得、局部适配和短时 CPU 计算；下载完成、运行成功、科学结论一致分别记录。
6. 既有架构约束继续适用。以下 0A 节规定本轮实验方向；后文 2026-08-25 的实现状态与里程碑保留为历史，不再决定当前先后顺序。

贯穿所有阶段的约束：

> 每个新增对象必须解决当前 vertical slice 中一个已经观察到的问题。没有真实复用需求时，不增加 registry、service、ontology、planner 层或重复检查。

---

# 0A. 用论文数据检验 Rules Table 与 Operator

## 2026-09-04 最终验收目标与持续审阅

最终目标是让 Rules 与连接的 Operator 以较高正确率回答前述20个科学问题，并覆盖问题所需的科学内容。首题接入成功、规则触发、资料缺口诊断和一次局部计算都是中间结果。评测应分别记录完整覆盖、部分覆盖、正确回答、错误回答、合理弃权和资料不足；弃权或尚未实现不能计为正确科学回答。准确率目标及容差须由科学参照、可用数据和独立评测设计支持，不能在看到结果后任意设定。

用户授权持续执行提交PR、Pro独立审阅、完整收集回复、核实建议、修改和验证、再次提交审阅。审阅不设篇幅、发现数量或固定结论选项限制，Pro可以审查全部相关论文、数据、代码、实验设计和20题选择，质疑当前解释或建议更广的改进。原Rules与原始失败基线保留，修复另记版本；仍须用真实触发、实际计算和同一规则实例的证据重评检验增益。

[Q05当前可审查代码与执行证据](../research/paper_result_reproduction_screen_v1/q05_review_evidence/README.md)包含实际17条规则结果及数值方法对照。自动跟进不因首题诊断完成而停止；按每轮实际证据推进最终目标。

## 2026-09-04 Pro 审阅后的执行修订

2026-09-05 Pro16后：Q01有限时间原题科学内容通过具名ChatGPT6Pro审阅，完成证据依赖的题级答复；反向组差异、同时远离双参照和接触分歧会改变输出。开发题级内容覆盖1/20，保留PENDING_DOMAIN_REVIEW及人类最终权威，准确率未测，不新增Q01科学计算。Q09已核验36人工候选并按组改变处置，随后规则仅续算3个实际STOP点；1个较高损失点通过，较低未完成点仍保留。当前只做背景参数数值停止原因诊断，不重跑全33。见[Q01完成答复](../research/paper_result_reproduction_screen_v1/q01_question_answer_v1/REPORT_ZH.md)、[Q09实际续算](../research/paper_result_reproduction_screen_v1/q09_targeted_continuation_v1/REPORT_ZH.md)及[20题进度](../research/paper_result_reproduction_screen_v1/question_progress_v2.json)。下方为此前快照。

2026-09-05 Pro15后：Q01现已完成全40条绝对几何、相对20ns起点位移、局部接触分解及整轨迹排除的开放MD参照比较。终段lid位移中位数开放种子3.77Å、闭合种子9.71Å；原9条持续相反偏好候选均在首尾窗口更接近开放NMR参照、远离闭合参照。ES17等局部接触仍存在内部方向分歧，证据限制完整开放态解释。连续测量从保存坐标及原始NMR重新构建差为0，输入/参考绑定修复；同一Rules实例实际补算开1/关0，零新GROMACS和优化。302测试及全40产物核查通过。已形成原题有限时间结构答复草案，提交独立审阅；下一步把Q09已有10+26个人工诊断核验后接回方法义务，零重复拟合，不转记Rules补算。见[Q01科学答复](../research/paper_result_reproduction_screen_v1/q01_absolute_paths_v1/REPORT_ZH.md)。下方为此前快照。

2026-09-05 Pro14后：Q01完整40条轨迹已实际读取并核对19+5甲基接触，最大源评分差0.005Å。NMR范围方法在全部起点无法分类，原失败保留；同一窄规则据此触发复用数据的相对方向比较。20开放种子保持偏好，20闭合种子中9条在20连续采样点条件下持续偏向开放参照，两种阈值轨迹分类一致，5/50点敏感性为10/8条。这是有限时间相对方向，不是进入NMR状态、平衡人口或准确率增益。完整题级验收暂不加一。Q09另完成60–119的10次诊断与13来源组26拟合，23/26数值通过；不重复全局旧拟合。下一步让独立审阅检验完整路径/方法边界，并把具体方法证据接回Q09义务。见[Q01完整结果](../research/paper_result_reproduction_screen_v1/q01_relative_paths_v1/REPORT_ZH.md)。下方为此前快照。

2026-09-05 当前更新：同一Q09R02已将全部33标记对/60观测纳入localK2、sharedK2、sharedK3条件比较，29次新优化保留4局部组和4全局搜索的数值stop；旧13次不重跑。规则实际派发作者前向结构参考比较，结构证据从缺失更新为已作描述性均值对照。全局仍未收敛，donor配置与SI中14个标记对的方法阶数有差距，不能判第三态。下一步根据源方法差距和数值贡献修正求解，再做科学模型比较；不通过改变参数追论文占比。见[全33实际结果](../research/paper_result_reproduction_screen_v1/q09_global_comparison_v1/REPORT_ZH.md)。以下为此前快照。

2026-09-05 后续实际结果：Q09已由另一条窄CASE义务完成19–119/19–132的共享K2、局部K2及共享K3比较，保留三组分10Å边界及等价局部人口解释；全33输入所有权已核对，尚未全33拟合。172L/148L坐标已取得，染料ACV执行仍有具体程序/方法缺口，未作残基距离替代。下一步扩展参考组与结构前向证据；完整20题答案仍0，不能用开发反例或单个低损失模型替代最终科学判断。见[实际模型比较](../research/paper_result_reproduction_screen_v1/q09_state_comparison_v1/REPORT_ZH.md)。

2026-09-05 实际更新：Q05共同权重Rules计算已执行，坐标形状资源授权待答复，仅阻塞该分支。Q09已先冻结当前Rules基线，再由新窄CASE义务执行donor3/仪器补查与IRF校准敏感性。最新两种校准均值使短距离19.7Å变为22.3–22.7Å；10个校准条件有1个数值stop，完整态数仍未决。下一步带着明确限制做跨变体条件比较及结构证据核对，保留原20题分母，避免无限修饰22–127。详情见[最新校准补算](../research/paper_result_reproduction_screen_v1/q09_calibration_sensitivity_v1/REPORT_ZH.md)。下面的初始人工结果与顺序作为历史记录保留。

当前按 **Q05 → Q01 → Q09** 逐题推进，Q15 候补，取代初筛的 Q09/Q01/Q05 顺序。Q05 作者矩阵已完成局部重加权：SAXS 平均归一化平方残差 10.02 → 1.53，熵有效集合比例为 1.49%，与论文约 18% 有差距。原始联合配置尚未核准；该人工参考脚本没有运行 Rules，也未复现坐标形状分布。

先冻结现行 Rules 的真实输出，再为实际触发的要求接通计算。专家预登记的必要检查若未触发，记漏判；人工指定的补算不计 Rules 成功。比较直接主计算与 Rules 补算时，固定输入、主方法、参数与预算，保留必需校正；关闭相关规则应取消对应补算，证据改变后重评同一规则实例。

数据不足、方法配置不明、Operator 缺口、纯路由失败与 Rules 漏判分别记录；方法和实现核准后才按预定容差判断科学不一致。论文一致和 Rules 增益分别报告。Q01 以轨迹为统计单位，Q05 保留模拟与实验重复，Q09 不把标记变体当生物重复。

论文先复用已有 Markdown，没有则找可用工具转换一次，再检索当前问题相关段落。公式、图表有歧义时核对对应 PDF 页。

具体来源、首个数值结果及限制见[Pro 审阅后续记录](../research/paper_result_reproduction_screen_v1/PRO_REVIEW_FOLLOWUP_ZH.md)。本节以下初筛状态和检查预算保留为提交首次审阅时的快照；当前状态以上述修订为准。初筛 JSON/CSV 不追改为已执行。

## 本轮要回答的问题

给定论文研究的具体体系、实验或模拟数据，现有 Rules Table 能否要求正确的计算，连接已有 Operator，并得到与论文相符且不过度解释的科学结论。

例如，一项研究报告蛋白在两种条件下的构象占比不同。有效检验需要读取两组数据，用论文定义或有依据的表征计算状态占比，保留独立重复和不确定性，再比较差异。登记温度、标记位置或数据角色只是准备步骤。

一次正确的停止也有价值，但停止不能计作论文结果复现成功。结构变化若没有活性测量或已验证的定量联系，只能支持结构结论。涉及催化或结合活性的题目必须提供相应实验数据。

## 问题怎样入选

优先复用现有文献库中的原始研究，替换旧 20 案里的通用指南、综述和纯字段声明题。20 个问题可以来自少于 20 篇论文。同篇两题必须使用不同科学结论、比较对象或判别量，并作为相关题组报告。

每题均须具备以下内容。

- 明确的体系和比较对象，例如两种条件、不同突变体、两种构象模型或两个测量方法。
- 能定位到原文 Results、图或表的论文结论。未核准具体图号时保留章节定位，禁止补造。
- 可计算的输入与输出。原始数据、作者处理后数据、已拟合模型和图片读数分别标注。
- 对现有 Rules 的实质要求，例如如何选择比较量、要求何种修正、处理不确定性或阻止无效比较。
- 当前 Operator 的准确匹配状态，以及所缺的适配、方法、数据或实现。
- 选题理由、预期计算量和最可能暴露的问题。

优先选数据入口清楚、计算规模可控、至少有一个独立比较对象的题目。数据尚未取得的候选可以保留，但不能称为可运行。不能为了凑够 20 题，把同一结果拆成两个改写问题。

## 数据与计算的完整路径

```text
论文中的体系问题
→ 论文结论与比较标准单独登记
→ 获取并核对数据、条件和来源
→ 现有 Rules Table 产生审查要求与计算需求
→ 匹配现有 Operator 的能力和输入合同
→ 执行主计算及 Rules 所要求的补充计算
→ 保存结果、不确定性与计算回执
→ 重新评估受影响的规则
→ 给出有证据边界的体系结论
→ 对照论文，归因成功或失败
```

Rules 决定什么证据足够、缺什么和哪种比较允许进行。Operator 执行计算。补充计算可以是分组统计、误差传播、模型到观测的预测、敏感性检查或状态占比估计。具体采用哪项必须由题目和规则依据决定，不能预先给每题套一组相同检查。

全文中的结论、目标数值及评判答案保存为独立参考文件。执行输入保留完成计算必需的方法、条件和数据，不把期望答案、覆盖标签或人工结论送进运算。人工在筛选时已见过论文，因此整批属于开发期验证。

## 三种能力分开记

| 能力 | 证据 | 失败的归属 |
|---|---|---|
| 现有 Operator 对该数据能否完成主计算 | 当前注册项、输入兼容性和真实运行回执 | Operator 不覆盖、输入不满足或程序失败 |
| Rules 能否要求合适的操作和补充计算 | 选用规则、触发理由、实际动作及前后判断 | 漏规则、适用条件错误、证据标准缺失或错误调用 |
| 结果能否支持类似论文结论 | 计算输出与预登记论文参照的逐项比较 | 科学不一致、数据不足、方法不一致或过度推断 |

通用库已安装、函数存在、旧案例计算成功都不足以证明一个新题可以运行。原有精确输入的专用 Operator 要列明输入限制。缺少相应 Operator 的题目记录为能力缺口，不能用临时独立脚本冒充现有 Rules 连接已经成功。

## 2026-09-04 核对的计算范围

当前注册表只有一个可路由的科学计算 Operator，它绑定原有 HSP90 两份状态记录、40 条轨迹和固定持续长度参数。它报告描述性时间诊断，不能接收任意新论文轨迹，也不能输出平衡占比、速率或活性结论。

X-EISD 当前提供固定字段查找。HSP90 的单观测量 PyMBAR 诊断和 ADK 的 SciPy 静态对齐是已有案例计算组件；二者没有作为一般 Operator 接入有效 Rule 判定。MDAnalysis 轨迹投影在注册表中仍为阻塞状态。本轮检查的注册表没有可路由的 SAXS、FRET、NMR 前向计算或 ensemble 重加权能力。

因此，本轮选题同时暴露新数据的计算接入缺口。筛选结果须保留真实科学问题，不能改成登记字段或重读作者结论来制造通过。每题是否有输入、是否有可调用计算、规则能否判断和结果是否一致分别记账。

详细代码与回执位置见[当前 Operator 清单](../research/paper_result_reproduction_screen_v1/OPERATOR_READINESS.md)。

## 怎样比较论文结果

每题在运行前登记主要比较量、方向或模型排序、条件范围、独立统计单位，以及依据论文误差或方法精度制定的允许差异。没有足够依据时，数值容差保持待确定，不能设置统一的 5% 或看过结果再调阈值。

作者处理后数据可以检验下游计算；原始数据能够检验的处理环节更完整。直接重读作者的最终表格不算重新计算。只重现作者已有拟合模型的输出，也不能写成从原始观测恢复了该模型。

最终逐题记录五种结果。

1. 主计算完成，关键结果与论文一致，结论限制正确。
2. 主计算完成，结果或推理与论文不一致。
3. 数据足够，但现有 Rules 或连接关系不能形成有效执行路径。
4. 现有 Operator 缺少对应能力或无法处理输入。
5. 数据或方法说明不足，当前无法检验。

结果一致、错误支持和正确停止分别报告。不用一个通过率掩盖问题来源。同篇相关问题单独聚合，20 题不宣称为 20 个独立科学体系。

## 快速推进的节奏

本轮先交付计划和 20 个题目卡。后续从数据最明确、计算规模可控且科学信息量足够的题目里选 3 个组成首批。已有组件可复用时优先考虑，但保留题目的科学难度。没有匹配 Operator 的题目先记录无法执行及具体缺口，不把一次空运行计为科学失败。

首批即可暴露数据、Operator、规则判断与科学比较之间的主要断点。保留第一次失败结果，完成一批后再提出一项最有依据的修订。修订后的同题重跑记为修复回归，不能替代新题验证。

若最终要声称 Rules 带来了增量价值，后续应在相同输入和主要计算方法下比较 Operator 直接运行与 Rules 引导的补充计算。两条路径本身尚未比较时，只报告可运行性和科学结果一致性，不提前声称 Rules 有增益。

## 已筛选的二十题

本轮已从 10 篇原始研究筛出 20 题，包含 17 个蛋白或蛋白脂质体系问题、2 个 DNA 测量对照及 1 个论文模拟负对照。当前注册 Operator 尚未完整覆盖其中任何一题；HSP90题有相关既有诊断组件可核对。题目筛选完成，数值数据验收与科学运行均未完成。

完整[二十题、选择理由与计算路线](../research/paper_result_reproduction_screen_v1/REPORT_ZH.md)已保存。建议先核对 T4 溶菌酶 2.9 MB 衰减包、本地 HSP90 数据同源性及 nanodisc 作者数值文件，再决定首批的精确输入和计算范围。

## 本轮交付与检查预算

本轮修改现有计划，并交付 20 题总表、逐题依据与计算路线、数据入口记录和现有 Operator 清单。完整数据下载、依赖安装、科学运行和 Rule 修改不属于本次交付状态。

本轮检查一次任务上下文，一次题目数量、来源链接、必需字段和状态一致性检查，一次新正文的文字检查，并在交付时做一次合并审阅。没有源码实现变化，跳过运行测试、全量构建和重复哈希。仅在修复实际发现的问题后复查受影响部分。

---

# 1. 系统承诺与输出边界

## 1.1 系统接收什么

```text
Scientific question
+ Paper / source manifest
+ Data manifest
+ Available metadata
+ Optional raw, processed or derived artifacts
```

输入可以不完整。缺失字段必须保留为显式 unknown，不能由模型按常识补齐。

## 1.2 系统返回什么

系统返回 `ConclusionPacket`，至少包含：

```text
case_id
requested_claim
current_claim_ceiling
resolved_rule_instances
unresolved_rule_instances
evidence_results
operator_run_receipts
terminal_state
human_review_items
provenance
```

Runtime 使用三组不同状态，避免把“流程跑通”写成“科学结论成立”。

### Routing state

```text
DIRECT_EVALUATION
EVIDENCE_LOOKUP
REGISTERED_OPERATOR
REQUEST_NEW_DATA
HUMAN_REVIEW
```

### Rule evaluation state

```text
PASS
FAIL
UNRESOLVED
NOT_APPLICABLE
HUMAN_REQUIRED
```

### Scientific conclusion state

```text
SUPPORT_WITHIN_CEILING
CANNOT_SUPPORT_REQUESTED_CLAIM
ABSTAIN_OR_HUMAN_REVIEW
```

`CANNOT_SUPPORT_REQUESTED_CLAIM` 只描述当前数据与 evidence contract。它不证明现实中的 biological claim 为假。

当前 prototype 尚未完成可泛化的 scientific conclusion aggregation。现阶段最多返回 contract-bounded routing/evaluation 结果，并要求 human review。

---

# 2. Canonical end-to-end flow

```text
Question + Papers + Data Manifest
                │
                ▼
        Profile Agent proposal
                │
        deterministic admission
                │
                ▼
       Canonical CaseWorkflow
                │
                ▼
      Scientific Rule Compiler
                │
    RuleInstances + Claim Ceiling
                │
                ▼
         Resolution Router
      ┌─────────┼──────────┬────────────┐
      ▼         ▼          ▼            ▼
 DIRECT_EVAL  SOURCE_LOOKUP  OPERATOR_DAG  HUMAN/NEW_DATA
      └─────────┴──────────┴────────────┘
                │
                ▼
 EvidenceResult + OperatorRunReceipt
                │
                ▼
       Evaluation Contracts
                │
                ▼
       Claim Ceiling Compiler
                │
                ▼
        Conclusion Packet
```

平台持有的完整对象是：

```text
CaseWorkflow
= CaseProfile
+ EvidenceItems
+ ComparisonEdges
+ RuleInstances
+ ExecutionPlan
+ EvidenceResults
+ ClaimState
+ Receipts
```

这条数据流是项目的固定主线。Profile Agent、typed binding、operator registry 和 future mutation service 都是其中的实现部件，不能各自发展成平行系统。

---

# 3. 2026-08-25 实现状态存档

本节保留当时的运行事实。2026-09-04 的选题与下一步以 0A 节和项目实时状态为准。

以下状态来自 2026-08-25 本地 run：

`dynamics-atlas-harness/runs/target_architecture_v0_2_20260825/`

| Component | Observed state | 当前证据 | 当前 claim ceiling |
|---|---|---|---|
| Profile prompt | `IMPLEMENTED` | `prompts/profile_case_v1.md` | 只提出 CaseGraph 字段 |
| Profile provider | `RECORDED_FIXTURE_ONLY` | stable provider interface | 尚未接真实便宜模型 |
| CaseGraph admission | `IMPLEMENTED` | `profile/case_graph_admission.json` | structural admission only |
| Rules selector | `EXISTING_V0_3_SELECTOR_INVOKED` | 59 obligations / 15 unresolved inputs | review obligations only |
| Evaluation Contract | `IMPLEMENTED_FOR_BUNDLE_ROUTING` | `evaluation/evaluation_contract.json` | 不产生 general scientific verdict |
| Persistent RunPlan | `IMPLEMENTED` | `run_plan.json` | execution state only |
| X-EISD case route | `RUN_PLAN_BLOCKED` | 16 gaps，0 个匹配 operator | 没有 case-resolution claim |
| HSP90 time-anatomy operator | `CANARY_PASS / NOT_ROUTABLE` | `operator_canary/operator_run_receipt.json` | frozen descriptive diagnostic only |
| HSP90 canary 与 X-EISD 的关系 | `INDEPENDENT_CANARY` | run summary 明确标记未被 case plan 路由 | 不能用来关闭 X-EISD gaps |
| Structural-state projection | `REGISTERED_BLOCKED` | MDAnalysis runtime、method profile、inputs 和 metric 未冻结 | 不得执行或报告 output |
| Request–Validate–Commit | `FUTURE` | 仅保留接口方向 | 无当前能力声明 |
| General semantic correctness | `NOT_EVALUATED` | human review required | 无泛化结论 |
| GitHub | `PRIVATE_BASELINE_AND_REMOTE_CI_PASS` | `main@ba318e5`、`v0.2.0-baseline`、Actions run `32853872659` | private repo delivery only |

当前 run 的精确摘要：

```text
PROFILE_READY
→ EXISTING_SELECTOR_INVOKED
→ 59 obligations
→ 15 unresolved selector inputs
→ RUN_PLAN_REQUIRED
→ 16 total gaps
→ no matching registered operator
→ RUN_PLAN_BLOCKED
```

第 16 个 gap 是 batch-level evidence evaluation 尚未完成。HSP90 canary 证明现有分析可以按 registry、fixed inputs、output contract 和 receipt 接入；它没有证明当前 X-EISD route 已解决。

---

# 4. 对象边界与权限

## 4.1 三个系统组件

| 组件 | 负责什么 | 不负责什么 |
|---|---|---|
| Rules | 适用条件、required evidence、evaluation contract、claim effect、source trace | 运行科学包；猜测缺失事实 |
| Harness | 构建和保存 workflow、routing、operator resolution、执行限制、receipt、受影响规则的重新评估 | 创造新规则；把执行成功升级成 scientific support |
| Operators | 在固定输入、参数和 runtime 下产生 EvidenceResult | 选择 Rule；修改 claim ceiling；直接输出 mechanism verdict |

Human review 保留以下权限：

- 批准新 rule 或 rule family；
- 冻结 method profile、metric 和 threshold；
- 判断 source passage 是否支持规则抽象；
- 批准 claim upgrade；
- 对 L3 scientific correctness 作最终判断。

## 4.2 Case Evidence Graph 与 Execution DAG

`Case Evidence Graph` 表达科学对象和比较关系：

```text
CASE
SOURCE
COMPARISON EDGE
CLAIM
RULE INSTANCE
EVIDENCE RESULT
```

`Execution DAG` 表达计算依赖：

```text
load registered inputs
→ calculate observable
→ validate output
→ evaluate affected rule
```

两种 edge 分开保存：

| Edge | 保存位置 | 含义 |
|---|---|---|
| `EvidenceEdge` | `CaseWorkflow.comparisons` | sources 比较什么、bridge 是否存在、最高可支持什么 claim |
| `ExecutionEdge` | `CaseWorkflow.execution_plan` | 哪个 step 的 output 可进入下一个 step |

DAG success 只说明 declared steps 执行完成。科学比较是否成立仍由 Rules、Evaluation Contract 和 human adjudication决定。

---

# 5. Profile Agent contract

## 5.1 最小职责

Profile Agent 只做以下工作：

1. 解析 requested scientific claim；
2. 枚举 papers、datasets 和 derived artifacts；
3. 提取 method、native observable、estimand、construct、condition、time semantics、spatial support、statistical unit、uncertainty 和 evidence role；
4. 提出中性的 source-to-source comparison edges；
5. 给字段附 evidence pointer；
6. 对无法确认的内容输出明确 unknown。

Profile Agent 不得：

- 选择 Rule ID；
- 选择 operator 或 terminal route；
- 输出 SUPPORT / CANNOT_SUPPORT；
- 写 expected relation 或 reference answer；
- 根据论文结论反推 input fields；
- 用模型自信度覆盖缺失 evidence pointer。

## 5.2 字段状态

```text
EXTRACTED
INFERRED_WITH_SUPPORT
UNKNOWN
CONFLICTING_SOURCES
HUMAN_CHECK_REQUIRED
```

模型 confidence 可以保留为诊断字段，不参与 deterministic routing。

## 5.3 当前与未来

当前实现：

```text
proposal
→ schema/evidence admission
→ versioned canonical JSON
```

未来实现：

```text
retrieve canonical state
→ propose typed patch
→ validate
→ commit or reject
```

后续接便宜模型时，只替换 Profile provider。下游 CaseWorkflow contract、Rules compiler 和 Harness 不随模型变化。

---

# 6. Rules Table 的位置与 runtime 设计

## 6.1 Authoring truth 保持原位

Rules 的 source-linked authoring registry 继续位于：

```text
autoresearch/tasks/
  dynamics_atlas_literature_card_male_pilot_20260805/
  outputs/ruleset/v0_1/rule_registry.tsv
```

当前 33-row registry 中的文献 evidence、source locator、Rule ID 和历史判断不移动。Harness 以 read-only asset 方式引用它，避免出现第二套科学权威。

## 6.2 Prototype 保留三层

```text
Rule Evidence / Authoring Registry
        │
        ▼ compile
Typed Applicability Bindings
        │
        ▼ compile
Executable Rule Index
        │
        ▼ select
Case-specific RuleInstances
```

对应的当前资产是：

1. `rule_registry.tsv`：面向人类审查和 source trace；
2. `registry_bound_typed_bindings_v0_3.json`：17 个 baseline bindings 加 2 个 modality-repair injections；
3. `compiled_registry_rule_index_v0_3.json`：selector 的冻结输入与 compile receipt。

## 6.3 Typed binding 的意义

Rule row 回答“科学上要检查什么”。Typed binding 把这个判断编译成机器可执行条件：

```text
target_scope
exact predicates
required_fields
gap checks
claim scope
evidence evaluation requirement
```

它防止 selector 用 `MD`、`trajectory` 等自由文本关键词临时猜测 applicability。

当前 runtime 保留独立 typed bindings。理由来自实际行为：同一个 rich X-EISD CaseGraph 在旧 v0.1 snapshot 中产生 51 obligations / 17 unresolved；当前 v0.3 产生 59 obligations / 15 unresolved。Binding package 会改变 selection，不能在没有迁移测试时直接内嵌或删除。

面向架构读者时，typed binding 可以视为 `Scientific Rule Compiler` 的内部细节。未来只有在以下条件同时满足时才重构：

- 新 schema 能无损表达现有 predicates 和 required fields；
- v0.3 selector regression 保持一致，或差异获得人工批准；
- Rule Evidence Registry 仍是唯一 source authority；
- 迁移不会改变历史 Rule ID 和 evidence trace。

## 6.4 Runtime ScientificRule / RuleInstance

Runtime 需要表达：

```text
rule_id
rule_version
rule_family
target_scope
applies_when
required_evidence
evaluation_mode
evaluation_contract
outcome_to_claim_effect
resolution_routes
evidence_refs
status
```

`outcome_to_claim_effect` 是 Stage-2 的核心。例如：

```json
{
  "PASS": {
    "claim_effect": "NO_ADDITIONAL_RESTRICTION",
    "route": "CONTINUE"
  },
  "FAIL": {
    "claim_effect": "FORBID_KINETICS",
    "route": "RETURN_WITH_LOWER_CEILING"
  },
  "UNRESOLVED": {
    "claim_effect": "CAP_AT_SOURCE_LOCAL_CONSISTENCY",
    "route": "REGISTERED_OPERATOR_OR_HUMAN"
  }
}
```

现有 selector 已能产生 review obligations。它还不能从论文结果推导 observed discriminability，也不能独立给出 scientific SUPPORT。Rule selection 和 evidence evaluation 继续分开。

---

# 7. Harness runtime

Harness 是 control plane 和 execution runtime。它读取 canonical CaseWorkflow 与 live registries，限制允许的 action，执行 registered operator，验证实际 output，保存 receipt，并只重新评估受影响的 RuleInstances。

Prototype Harness 必须完成七个动作：

1. Load canonical CaseWorkflow；
2. Compile applicable RuleInstances；
3. Classify unresolved evidence gaps；
4. Resolve registered capability；
5. Validate prerequisites、inputs 和 execution edges；
6. Execute operator 并附加 EvidenceResult / receipt；
7. Re-evaluate affected rules 并更新 claim ceiling。

## 7.1 Obligation state machine

```text
OBLIGATION_OPEN

├── EVIDENCE_READY
│     → DIRECT_EVALUATION
│
├── SOURCE_FACT_MISSING
│     → EVIDENCE_LOOKUP
│
├── COMPUTABLE_EVIDENCE_MISSING
│     → REGISTERED_OPERATOR
│
├── DATA_NOT_AVAILABLE
│     → REQUEST_NEW_DATA
│
└── SCIENTIFIC_JUDGMENT_REQUIRED
      → HUMAN_REVIEW
```

完成后的 terminal state 是 `PASS`、`FAIL`、`UNRESOLVED`、`NOT_APPLICABLE` 或 `HUMAN_REQUIRED`。

`clean trace` 是所有节点的 invariant，不是单独的 workflow step。`complete` 的定义是：所有 blocking RuleInstances 获得合法 EvaluationResult，或者进入明确 terminal stop。

## 7.2 Persistence 与复用

复用单元有三类：

- Rules：复用 scientific constraint；
- Skills：复用领域程序性做法；
- Operators：复用固定 I/O、参数、runtime 和 output contract 的计算能力。

RunPlan 只连接这些单元。Agent 不为每个 case 生成一次性脚本，也不能绕过 registry 直接执行 arbitrary Python。

当前 JSON artifact 足以支持单进程 prototype。出现并发编辑、跨用户 mutation 或 rollback 的真实需求后，再加入 Request–Validate–Commit service。

---

# 8. Registered Operator system

## 8.1 Capability-first registry

Registry 登记 scientific capability：

```text
trajectory.reference_state_projection.v1
trajectory.sampling_diagnostics.v1
structure.flexibility_projection.v1
ensemble.experimental_observable_prediction.v1
```

实现 backend 单独绑定：

```text
capability:
  trajectory.reference_state_projection.v1

implementation:
  mdanalysis.reference_state_projection.v1

backend:
  MDAnalysis
```

`MDAnalysis`、`MDTraj`、`deeptime` 或 `ProDy` 本身只是 package candidate。只有冻结 OperatorSpec、runtime probe、canary、output contract 和 claim boundary 后，它们才进入 Harness。

## 8.2 OperatorSpec

```text
operator_id
capability
supported rule families
supported methods / modalities
required inputs
fixed or dossier-supplied parameters
implementation_ref
runtime and package versions
input schema
output schema
validation checks
failure routes
allowed claims
forbidden claims
provenance requirements
registry status
```

建议生命周期：

```text
DISCOVERED
→ SPECIFIED
→ REGISTERED_BLOCKED or CANARY_PASS
→ CONTRACT_REVIEWED
→ ROSTER_PASS
```

## 8.3 当前 roster

| Capability / Operator | Backend | 状态 | 可以证明什么 | 仍缺什么 |
|---|---|---|---|---|
| `hsp90.directional_time_anatomy.v0` | existing standard-library analysis | canary succeeded | 现有 HSP90 分析可经 registry、fixed inputs、output contract 和 receipt 复用 | 尚未匹配当前 X-EISD gaps；scientific review 仍需人工 |
| `trajectory.structural_state_projection.v1` | planned MDAnalysis adapter | `REGISTERED_BLOCKED` | 只证明 spec 已登记 | MDAnalysis runtime、case inputs、mapping、method profile、metric 和 parameters |
| NMR package candidate | meeting reference | `DISCOVERED_UNIDENTIFIED` | 会议中确实提到 Gina 使用的 NMR package | 聊天记录中的准确 package 名称和链接 |

当前技能目录中已经有 `molecular-dynamics` skill，其模板使用 OpenMM 与 MDAnalysis，并覆盖 RMSD、RMSF、Rg 和 contacts。Skill 是 operator discovery 与程序性知识来源，不能替代本项目的 OperatorSpec 和 canary。

## 8.4 下一项通用 operator

优先候选是：

```text
trajectory.reference_state_projection.v1
```

只有在当前真实 gap 与它匹配、输入已存在并且 method profile 可冻结时才实施。

最小输入：

```text
topology
trajectory files
replica IDs
reference ensemble A
reference ensemble B
alignment selection
frozen distance metric
frame policy
```

最小输出：

```text
per-frame distance to reference A
per-frame distance to reference B
relative projection or margin
ambiguous frames
actual files read
frame counts
parameters
warnings
provenance
```

允许的最高 claim：在冻结 representation 和 metric 下，frames 更接近 reference A、reference B，或无法区分。

禁止升级到：equilibrium population、transition rate、free-energy difference、unique pathway 或 biological mechanism。

如果 16 个当前 gaps 中没有一项满足输入合同，下一步应走 source lookup、已有 EvidenceResult 接入或 explicit stop，不能为了展示 operator route 强行调用无关分析。

---

# 9. Direct Evaluation、EvidenceResult 与 Evaluation Contract

这三个对象按以下顺序工作：

```text
RuleInstance
→ Resolution Router
→ Direct Evaluation OR Registered Operator
→ EvidenceResult
→ Evaluation Contract
→ RuleResult
```

## 9.1 Direct Evaluation

Direct Evaluation 只处理已经存在、可以确定性判断的 evidence：

- required metadata 是否存在；
- source ID、construct ID、condition ID 是否精确一致；
- validation evidence 是否在 lineage 中标记为未参与 fitting；
- bridge receipt 是否存在；
- operator output 是否符合 schema；
- frozen threshold 是否通过。

它不能从自然语言推断 scientific equivalence，不能从 Discussion passage 推导 mechanism，也不能临时建立阈值。

## 9.2 EvidenceResult

EvidenceResult 记录事实与来路：

```text
evidence_result_id
source_rule_instance_ids
producer_type
producer_id
actual_inputs
parameters
outputs
quality_checks
warnings
provenance
claim_ceiling
```

Operator 输出 evidence facts。`SUPPORT`、`MECHANISM` 和 claim upgrade 由 Evaluation Contract 与 human review控制。

## 9.3 Evaluation Contract

Evaluation Contract 规定 EvidenceResult 如何转成 RuleResult。例如：

```text
required outputs:
- per-replica observable series
- effective sample size
- window sensitivity

PASS:
- all required outputs present
- frozen acceptance criterion satisfied

FAIL:
- frozen criterion explicitly violated

UNRESOLVED:
- output exists but criterion cannot be evaluated
```

当前实现只完成 current-bundle sufficiency routing。Scientific PASS/FAIL 需要 rule-specific contracts 与真实 EvidenceResults，尚未完成。

---

# 10. Semantic correctness 分层

| 层级 | 当前安排 | 含义 |
|---|---|---|
| L0 Structural correctness | 现在 | schema、ID、edge、DAG、I/O compatibility |
| L1 Execution correctness | 现在 | 实际文件、参数、operator execution、output schema、provenance |
| L2 Contract-level scientific semantics | prototype 逐条实现 | frozen observable、rule、criterion 和 claim effect 是否按合同执行 |
| L3 General scientific correctness | future validation lane | 规则能否跨体系成立，结论能否通过 expert 与 held-out evidence |

当前代码只实现 current-bundle sufficiency routing，不是 semantic checker。未来的 L2 checker 应命名为 `Contract-Level Semantic Checker`。L3 属于 Scientific Adjudication，不能由 schema、DAG 或 package success替代。

---

# 11. Prototype scope 与反过度工程纲领

## 11.1 当前 target prototype 必须有

- 一个明确的 Profile prompt 和可替换 provider interface；
- 一个 canonical CaseWorkflow / rich CaseGraph contract；
- 现有 v0.3 Rules selector 的只读 adapter；
- RuleInstances / obligations 与 claim ceiling；
- direct-bundle route；
- persistent RunPlan；
- capability-first Operator Registry；
- 至少一项真实 analysis canary；
- EvidenceResult 与 OperatorRunReceipt；
- explicit blocked / human stop；
- 可追溯 ConclusionPacket。

## 11.2 当前不建设

- 新 Rules database；
- 全自动 rule authoring；
- arbitrary Python execution；
- 多 Agent swarm；
- 自动安装大量 scientific packages；
- operator knowledge graph；
- production WebUI；
- 并发 mutation service；
- general semantic correctness model；
- 大规模 held-out benchmark。

## 11.3 每项新增工作的 admission test

开始新增 registry、schema、validator 或 service 前，必须回答：

1. 它解决哪个已观察到的 gap 或重复？
2. 现有对象为什么不能表达？
3. 它会改变哪个 public contract？
4. 最小的验证是什么？
5. 哪个条件出现后立即停止扩展？

答不出第 1 项时，不实施。

---

# 12. 交付阶段：按可运行行为推进

## Milestone 0 — Thin bridge

**状态：已完成。**

已证明 Profile fixture、frozen Rules 和 operator fixture 可以通过受约束的 provider/operator interface 串接。它没有证明真实科学分析完成。

## Milestone 1 — Target architecture local slice

**状态：已运行，case route blocked。**

已完成：

```text
Profile proposal
→ deterministic admission
→ actual v0.3 selector
→ Evaluation Contract
→ persistent RunPlan
→ registered-operator resolution
→ explicit blocked state
```

并行完成一个 HSP90 existing-analysis canary。该 canary 没有被当前 X-EISD route 使用。

## Milestone 2 — Close one real case gap

**状态：下一步。**

一次只选择一个高价值 gap：

1. 对 16 个 gaps 按 `SOURCE_FACT_MISSING`、`COMPUTABLE_EVIDENCE_MISSING`、`DATA_NOT_AVAILABLE`、`SCIENTIFIC_JUDGMENT_REQUIRED` 分类；
2. 选择已有输入、与 requested claim 有直接关系的一项；
3. 优先复用现有 EvidenceResult 或 analysis script；
4. 需要新 backend 时，先冻结 capability、method profile、inputs、metric 和 output contract；
5. 运行一次 canary；
6. 把 operator output 接回原 RuleInstance；
7. 只重新评估受影响规则。

Exit condition：至少一项真实 gap 从 `UNRESOLVED` 转成合法 RuleResult，且 receipt 能证明实际读取的 inputs、parameters 和 outputs。

Early stop：输入、method semantics 或 frozen metric 任一缺失时，保存 blocked reason，不安装依赖、不编造 fixture。

## Milestone 3 — Three-route vertical slice

同一套 runtime 支持：

```text
A. current evidence sufficient
   → direct bounded return

B. evidence missing but computable
   → registered operator
   → EvidenceResult
   → affected-rule reevaluation

C. evidence unavailable or requires judgment
   → explicit stop / human / new data
```

Exit condition：三条 route 共用同一 CaseWorkflow、Rules compiler 和 Harness，不出现 `if hsp90`、`if adk` 或 case-specific terminal verdict。

## Milestone 4 — Live Profile model adapter

在 deterministic chain 稳定后接真实模型。保留两种后端：

- 便宜 agent/model provider；
- Codex subagent simulation，用于 provider contract 测试。

两者必须输出相同 Profile schema。模型错误与 Harness 错误分别记录。

Exit condition：answer-blind input 可以生成可 admission 的 proposal；critical unknowns 不被静默补全。

## Milestone 5 — Contract-level science and portability

- 为 seed RuleInstances 冻结 L2 Evaluation Contracts；
- 在 HSP90 development case 上调试；
- 使用 ADK 或其他 exposed case 检查 portability；
- 冻结后再选择 held-out protein；
- expert adjudication 与 held-out 结果进入独立 scientific validation report。

Request–Validate–Commit、并发编辑和 WebUI 只有在 workflow 需要多轮外部 mutation 时才进入新 milestone。

---

# 13. 科学验证路线与工程路线分开

工程阶段回答：

```text
workflow 能否构建、执行、停止和复现？
```

科学验证回答：

```text
Rule、observable、criterion 和 bounded conclusion 是否正确？
```

推荐 case 角色：

| Case | 角色 | 允许用途 |
|---|---|---|
| HSP90 | development anchor | prompt、operator、Rules 和 failure path 调试 |
| ADK | exposed portability case | 检查架构是否依赖 HSP90 特例 |
| 新 protein | frozen held-out | release freeze 后的一次性 generalization test |

如果某个 case 参与 rule、prompt、operator 或 threshold 修改，它立即变为 exposed case，不再用于 held-out claim。

Benchmark 分成三个问题：

1. hidden canonical CaseGraph → matcher：测 Rules selection；
2. answer-blind raw input → Profile Agent → same matcher：测 profiling；
3. selected obligations → Harness → Operators → Evaluation：测 planning 与 execution。

失败归因使用：

```text
PROFILE
VOCABULARY
BINDING
RESOLUTION_POLICY
OPERATOR
EVALUATOR
SCIENTIFIC_RULE
```

---

# 14. 现有资产迁移

| 现有资产 | 目标位置 / 用法 | 动作 |
|---|---|---|
| 33-row `rule_registry.tsv` | Rule Evidence / authoring truth | 原位保留，只读引用 |
| v0.3 typed bindings | Scientific Rule Compiler input | 当前保留；未来按 regression 结果决定是否内嵌 |
| v0.3 compiled index + selector | deterministic rule selection | 通过 workspace adapter 调用，不复制逻辑 |
| rich metadata contract | CaseProfile / CaseGraph admission | 直接复用 |
| HSP90 time-anatomy script | existing-analysis operator | 已登记并完成 independent canary |
| ADK structural projection script | generic operator candidate | 提取 capability 前先冻结 method/profile 与新 case inputs |
| qFit / CryoDRGN assets | regression 或 future operator candidates | 不写成已注册能力 |
| scientific skills | procedural knowledge / discovery | 不自动等价为 OperatorSpec |
| 会议中 NMR package | discovery item | 找到准确聊天链接后再登记，不凭记忆命名 |

已有资产只有在目标架构中拥有明确 owner、contract 和 claim boundary 后才转换。不能转换的内容留作参考，不建兼容层维持表面复用。

---

# 15. 状态、仓库与知识库

## 15.1 状态所有权

- 项目级 live gate：`autoresearch/DYNAMICS_ATLAS_STATUS.md`；
- 人工确认的目标或优先级变化：`autoresearch/DYNAMICS_ATLAS_DECISION_LOG.jsonl`；
- 本次实现任务：`autoresearch/tasks/dynamics_atlas_target_architecture_prototype_20260825/`；
- Harness 代码、schemas、docs 和 run receipts：`dynamics-atlas-harness/`。

`CURRENT_STATUS.md` 只保存任务级 snapshot 和 evidence links。每个事实只由一个文件拥有，其他文档链接它。

## 15.2 GitHub

每个可运行 milestone 形成一个相关功能 batch：

```text
implementation
→ focused validation
→ status / receipt update
→ local diff review
→ commit
→ private remote push
→ remote readback
```

只有 private visibility、authentication、push 和 remote readback 都通过后，状态才写“已同步 GitHub”。Force push、public visibility、collaborator 或权限变化需要单独批准。

## 15.3 Obsidian

每个交付阶段同步四项内容：

- 当前 architecture decision；
- 已观察运行结果；
- blocker 与 next allowed action；
- 对应 repo artifact / receipt 链接。

同步前先确认真实 vault 和目标 note。Obsidian note 不复制完整 registry 或 run output，只链接 authority artifacts。

---

# 16. 验证节奏

验证按风险执行，避免重复确认同一 code state。

| Functional batch | 风险 | 计划检查 | Runner 次数 | 独立 review | Hash | Trigger | Early stop | 必须更新的状态 |
|---|---|---|---:|---:|---:|---|---|---|
| Master Plan 修订 | 事实层混写、术语冲突、AI 腔 | 一次 prose scan + 人工 source check | 1 | 0 | 0 | 文档初稿完成 | 核心事实与 run receipt 冲突时先修文档 | task status、work log |
| 单项 gap closure | 错路由、错误 input、claim upgrade | 一次 focused operator/route check set | 1 | 0；public contract 改变时合并 review 1 次 | 0；首次 frozen import 可 1 次 | implementation 与 inputs 冻结 | prerequisite 缺失即 `REGISTERED_BLOCKED` | run receipt、progress、CURRENT_STATUS |
| Three-route milestone | cross-module contract drift | 一次 target architecture integration suite | 1 | 1 次 combined architecture review | 0 | 三条 route 都实现 | 任一路由需要 case-specific verdict 时停止 | review report、Status |
| Final prototype delivery | 回归与交付错报 | 一次 full test suite；build/lint 仅在相关配置变化时各 1 次 | test 1；其他按触发 | 1 次 final combined review | transfer integrity 需要时 1 次 | release candidate 冻结 | 失败后只重跑受影响类别，再做一次最终组合检查 | final report、Decision/Status（仅真实变化） |

同一 input、implementation version 和风险下，每个类别最多运行一次。修复后只重跑受影响类别；没有新风险时跳过重复 full test、hash 和 reviewer。

---

# 17. 参考设计及采用边界

| 参考 | 采用内容 | 不采用内容 |
|---|---|---|
| DataFlow-Harness | persistent editable artifact、live registry、typed workflow construction、procedural Skills | 把 DAG/schema validity 当 semantic correctness；当前先不做完整 RVC |
| BioExcel Building Blocks | 显式 input paths、output paths、properties 的 wrapper contract | 全量搬入 BioBB stack |
| CWL | declared upstream output 才能连接 step input；typed parameters | 当前不引入完整 CWL runtime |
| AiiDA | calculation provenance 与 workflow logic 分开 | 当前不建设 provenance database |
| ToolUniverse / SciToolAgent | tool schema、capability metadata、dependency ideas | 当前两个 operator 不建设大规模 tool knowledge graph |
| Anthropic protein-design harness | constitution、dossier、tool roster、canary、actual-output validation | 超长单体 prompt、GPU campaign、subagent swarm |

来源：

- DataFlow-Harness：He et al. (2026) local source-of-record PDF；原 PDF 不进入本仓库
- BioBB arguments：<https://biobb-documentation.readthedocs.io/en/latest/arguments.html>
- CWL Workflow v1.2：<https://www.commonwl.org/v1.2/Workflow.html>
- AiiDA provenance：<https://aiida.readthedocs.io/projects/aiida-core/en/stable/topics/provenance/concepts.html>
- ToolUniverse custom tool schema：<https://github.com/mims-harvard/ToolUniverse/blob/main/plugin/skills/tooluniverse-custom-tool/references/python-tool.md>
- SciToolAgent：<https://github.com/HICAI-ZJU/SciToolAgent>
- Anthropic binder-design prompt：<https://huggingface.co/datasets/Anthropic/claude-protein-binder-design/blob/main/prompts/prompts/multi_target_binder_design_prompt.md>

这些参考只提供 design patterns。Dynamics Atlas 的 scientific authority 仍来自本地 source-linked Rules、case-specific evidence 和 human review。

---

# 18. Prototype 完成定义

Prototype 达到目标架构 milestone，需要同时满足：

```text
answer-blind question + source/data manifest
→ Profile proposal with explicit unknowns
→ deterministic admission
→ existing Rules compiler
→ case-specific RuleInstances
→ direct route OR registered operator route OR explicit stop
→ EvidenceResult + receipt
→ affected-rule evaluation
→ bounded ConclusionPacket
```

并满足以下边界：

- 没有第二套 Rules authority；
- 没有 unregistered operator execution；
- 没有 case-specific terminal verdict；
- 没有把 package success 写成 scientific support；
- 没有把 development case 写成 held-out；
- 没有为了完整感增加当前不需要的平台层；
- 每项结论都能回到 source、Rule、EvidenceResult 或明确 human decision。

本计划保留目标架构和历史运行边界。2026-09-04 用户授权本轮计划修订与 20 题筛选，执行顺序以 0A 节为准。后续数据运行和实现变化按实际数据、计算规模及项目状态另行记录。


## Pro17 后续进展（2026-09-05）

Q01科学答复与题级输出通过Pro17并冻结。Q09已修复第二轮选回旧候选的问题：真实保存结果现在只选择两个最新未完成点，0重新拟合；313本地回归通过。下一项新增题目推进Q15，已核对SI校正参数与公式，现有66文件为63DCBS+3背景、0APBS。开发题级内容完成1/20、最终人类批准0、准确率未测。


## Pro18之后的实际科学进展（2026-09-05）

Q15两个位点的140个APBS文件完成首次主计算：55/175平均效率增加0.08199、175/228减少0.02617，后者重复间差异跨零。详见research/paper_result_reproduction_screen_v1/q15_apbs_comparison_v1/。这是条件荧光分析，原Q15的换染料和正交证据仍待完成，0Rules-extra。Q09修复完整历史绑定及连续零动作文件衔接，三个已有人工背景派生点经零拟合验收，D01数值分支结束、D24较低点保留。319本地测试通过，下一轮同PR开放Pro审阅。Q01冻结，开发完整内容1/20、准确率未测。
