# HSP90 首轮之后：收口、原生观测对照、规则窄修复、第二体系（v4）

Dynamics Atlas · 2026-09-10 · v4 · **供 Codex 无人值守执行** · 接在 v3.4 首轮（PR #27 `3ba975e`）之后 · 一次授权 1–7

> 依据：Pro 对首轮结果的审查（用户转贴，结论 CHANGES_REQUESTED_BOUNDED：保留科学结果和暂停自动推进，修改评价理由、论文关系表和报告表达；下一项科学工作是派生方向判据与原生 NOE 观测的对照）；本机审查 `REVIEW_HSP90_ROUND1_LOCAL_ZH.md`（读了四份原始答复、执行日志、冻结源表，全部计数独立重算一致，另核出 §15 汇报包缺失、REPLAY/HTML/STATUS 未更新、论文关系表为模板、凭证启动例外）。
>
> 路径约定沿用 v3.4：`WS`、`HARNESS_LUNA`（`feature/luna-runtime-v1`，PR #27）、`RT`、`TASK2` = `WS/autoresearch/tasks/dynamics_atlas_hsp90_first_round_v3_20260910`。新增 `TASK_B` = `WS/autoresearch/tasks/dynamics_atlas_hsp90_noe_crosswalk_v1_20260911`，`TASK_D` = `WS/autoresearch/tasks/dynamics_atlas_<sys>_plain_agent_v1_<date>`。`ACQ` = `WS/autoresearch/tasks/dynamics_atlas_hsp90_acquisition_20260725`。

## 0. 回到最初目标，本轮做四件事

最初目标：从异质蛋白资料得到有用、可复核、不过度的科学回答。Rules 是待检验的方法。首轮已经拿到一项这样的回答（闭合起始轨迹的有限时间开放方向变化），也暴露了一个比"引用编号"重要的问题：通用检查被绑到了带原实验专用条件的规则正文，专用术语进了答复。

**不重跑同题 A/B 去修出一个更漂亮的胜负。** 五条轨道，顺序执行，前一条交付后自动进入下一条：

| 轨道 | 做什么 | 天 | 费用 |
|---|---|---|---|
| A0 项目进度报告 | 先固定思路：从 Rules Table 起步讲到现在和下一步的一份给人看的报告 + 组会 deck，按 `REPORT_WRITING_GUIDE_ZH.md` 写 | 1 | $0 |
| A 首轮收口 | 改判定理由、重做论文关系表、改报告、补齐 §15 汇报包、更新过期文件和控制面板 | 2 | $0 |
| B 原生观测对照 | 派生方向判据 vs 作者沉积的 NOE 违例时间序列（本机已有，40 条 × 2 套 × 1001 帧），确定性脚本 | 3 | ≤ $0.03（可选一次 Agent 复核） |
| C 规则窄修复 | 渲染层区分"原条款范围"和"项目归纳的检查"，不改 33 条注册表 | 1（可与 B 并行） | ≤ $0.03（可选一次开发回归） |
| D 第二体系 | 普通 Agent + 成熟方法做一份科学答复，不以 Rules 增益为前提；只读盘点 → 有界下载 → 两次 A 运行 → 核对 → 汇报包 | 8 | ≤ $0.20，下载 ≤ 2 GB |

总停止线：自开工 ≤ 15 个工作日、模型费用总计 ≤ $0.30、下载 ≤ 2 GB；任一到线即停交报告。

### 0.5 节奏判断：执行不慢，交付太慢

- 执行本身不慢：首轮从授权到出报告 45 分钟（01:36 → 02:18 UTC），四次运行 $0.076；计划里按天写的上限没有起约束作用。
- 慢在对外交付：最近一份给组里看的报告是 8 月 6 日的周报 deck 和 8 月 23–24 日的会议材料；8 月 25 日到 9 月 4 日新建了约 45 个内部任务目录（原型、PR #1–#24、基准、交接、审计），STATUS 快照累计 160 个，没有一份对外报告。9 月 9–10 日计划改到 v3.4 用了一晚三轮 Pro 审查，跑只用了 45 分钟。
- 首轮跑完后，§15 要求的简报、读本、deck 一件没做，REPLAY 和 HTML 还是停机时的旧版。也就是说：会做，但把"做"当成了"交付"。
- 本版的纠正：完成条件按产物不按时间；每条轨道结束必须过 `report_bundle_check.py`；每周五一份给人看的更新；没有交付物不出新版计划；主动推进（A0→A→B→C→D 不等人），但每一步的边界句照写。

## 1. PM 一次性授权 **[一次签，回复"授权 1–7，按 v4 执行"]**

（授权 1 同时覆盖轨道 A0 的报告与 deck 提交。）

| 项 | 内容 |
|---|---|
| 1 | 轨道 A 的全部编辑在 `feature/luna-runtime-v1` 上提交（PR #27 继续用），PM 负责 push；`runs/`、案例数据、账本、凭证不入库 |
| 2 | 建 `TASK_B`、`TASK_D` 任务目录并写回执（同 v3.4 A1）；`TASK2` 继续用于轨道 A |
| 3 | 轨道 B 只用本机已沉积的作者数据做确定性分析，不下载、不跑 MD；可选一次 Agent A-only 运行 ≤ $0.03 作开发观察 |
| 4 | 轨道 C 只改 `RT/render_active_rules.py` 与新增 `RT/paper_method_family.json`；不改 `rule_registry.tsv`、选择器、method scope；可选一次 B 组开发回归 ≤ $0.03，结果标 `DEV_REGRESSION`，不与首轮比较、不改首轮判定 |
| 5 | 轨道 D：ADK 与 DHFR 只读盘点（≤ 50 MB 元数据）；选定体系后从 PDB / BMRB / Zenodo / ATLAS / mdCATH 下载 ≤ 2 GB（记 sha256、许可证）；Agent A-only ×2 ≤ $0.20；不跑 B 组，不跑新 MD |
| 6 | 凭证：PM 在 shell 里 `export OPENROUTER_API_KEY=…`，或存入 macOS 钥匙串后由启动脚本 `security find-generic-password -s openrouter -w` 读出；**不再从任何会话记录文件取 key**。首轮的 `CREDENTIAL_REUSE_CLARIFICATION.json` 记为一次性例外并写入决策日志 |
| 7 | A→B→C→D 自动推进，不等 PM；PM 随时一句"停"即停。绝对截止日写进 `TASK2/outputs/DEADLINE_V4.json`，不重置 |

## 2a. 轨道 A0：项目进度报告，先固定思路（1 个工作日，最先做）

Codex 很久没有给组里写报告了。在动任何修复之前，先按 `REPORT_WRITING_GUIDE_ZH.md` 写一份从头讲到尾的进度报告，把思路固定下来；后面所有轮末报告都沿用这条主线。

- 产物：`TASK2/outputs/report/DYNAMICS_ATLAS_PROGRESS_REPORT_20260912_ZH.md/.html` + `DYNAMICS_ATLAS_PROGRESS_REPORT_20260912.pptx`（8–10 页，组会用）+ 三句摘要放在 `REPORT_INDEX.md` 顶部。
- 内容按指南 §2 骨架：问题（G1–G4、Soojung 两次会的要求）→ 走过的路（指南 §7 时间线，只留改变判断的节点）→ 这一轮做了什么（v3.4 一题四答复）→ 结果三栏（科学：分区表；Agent：3 对 1 错；规则：专用条件迁移）→ 证明了什么、没证明什么 → 下一步（本计划轨道 A–D，各一行：做什么、多久、停止条件、需要 PM 决定什么）。
- 主线一句先写、先过冷读检查（指南 §6），再展开。数字只从 `direct_source_check.json`、核对表、`round_decision.json`、账本取，不新算。
- 完成条件：`report_bundle_check.py --profile progress` 通过（HTML ≥ 6 个 `<h2>`、deck ≥ 8 页每页有 notes、证据表 ≥ 20 行）；提交到 PR #27 的 `review/hsp90_q01-round-20260910/`。
- 时间上限 1 个工作日；写不完先交三句摘要 + 证据表 + 时间线，其余记未完成，不空着。

## 2. 轨道 A：首轮收口（2 个工作日，`TASK2` + PR #27）

### A1 判定文件：动作不变，理由分三栏
- 保留 `round_decision.json` 原件为 `round_decision_v1.json`。写新版 `round_decision.json`：`row: 3, proceed: false` 不变；`reason` 拆成三个字段，各自只说自己的事：
  - `format_conditions`：(b) 两份 B 未引用 rule_id；共同输出未要求引用；**记为评价设计限制，不是科学失败**。
  - `science_quality`：A1 主计数正确并给出核心覆盖诊断；A2 三处计数错误与一处内部矛盾（`A2-08/09/10`）；B1 主计数正确、"420 个常规箱"为局部措辞错误（不影响任何结论）；B2 主计数正确并补充 10/20（有内容的补充，未独立归因于规则）、未报核心覆盖数值（**内容差异，不是丢失**）。
  - `management_decision`：暂不自动扩展，原因两条：两份 B 都把 FRET 专用条件（RMP restraint / prior ensemble / fit objective；R0 / dye-AV）当作本题的必填或未解决带进答复（提示内容迁移，原句 B1 第 24 段、B2 第 39 段）；科学收益尚未稳定建立。**row 3 是"混合结果、未满足继续条件"，不写成"B 无科学增益"或"Rules 无效"。**
- 判据 (a) 改为 `true`（10/20 是新的、经复算、贴题的内容，写在"分析"节不影响其性质）；(c) 改为 `true_with_local_wording_issue`；(d) `true`；(b) `false`；(e)(f) `true`。总则"全部满足才推进"仍不满足，所以 proceed 不变。

### A2 论文关系表：逐答复重做
- 四份 `check/<run>_literature_relation.csv` 全部重写。每行一个可判断的主张：`agent_claim` 必须是 `answer.md` 的原句节选（≤ 60 字）+ 行号；`paper_claim` 用 `hidden/literature_claims.json` 的 8 条之一；`relation ∈ {AGREE, DISAGREE, PAPER_SILENT, AGENT_ABSTAIN, NOT_MENTIONED, NOT_REQUIRED, UNDETERMINED}`。**没提到、主动弃权、不需要回答是三种情况**，不能都写 AGENT_ABSTAIN。
- B1 的 CPMG 行：B1 只报告了"约 3–4% 作者占比"，不能把含速率、占比、自由能的整段论文陈述记 AGREE；拆成三行。
- 7/9/4 相关行：写明比较层级（作者 NOE/结构分组 vs 本轮方向分区），不再一行 AGREE 一行 UNDETERMINED 而不解释。
- 写 `RT/check_relation_tables.py`：拒绝占位句（如 "see matching claim audit"）、拒绝两份表内容相同、每行 `agent_claim` 必须能在对应 `answer.md` 里 grep 到。四份表过校验才算完成。

### A3 核对表加 `severity` 列
- `claims_check.csv` 加列 `severity ∈ {CORE, LOCAL, SUGGESTION}`：A2-08/09/10 → CORE；B1-12 → LOCAL；A1-07/A2-07/B1-07/B2-07（下一步建议）→ SUGGESTION，`status` 改为 `PROPOSAL_NOT_EXECUTED`（建议不需要"已执行"才算合格，只检查是否针对剩余问题、有无方法依据）；B2-12 `status` 改 `VERIFIED`，`method_note` 写"内容差异，非丢失"。数值行不动。

### A4 报告改写（`HSP90_Q01_VERIFIED_REPORT_ZH.md`，八节结构保留）
- 标题改为：**HSP90 的有限时间开放方向变化：科学结果与规则提示的开发观察**。
- 开头换成 Pro 给的三段（计数来自 `direct_source_check.json` 与核对表，不新算），紧接着放**分区表**（本机审查已从冻结表核实）：

  | 阈值（保存点） | 首个持续方向即 OPEN | 先 CLOSED 后 OPEN（离开候选） | 只有 CLOSED | 无持续方向 |
  |---|---|---|---|---|
  | 5 | 5（ES03/04/05/19/20，首段起于 37–114 ns） | 5（ES06/14/15/16/17，起于 115–621 ns） | 10 | 0 |
  | 20 | 5 | 4 | 9 | 2 |
  | 50 | 7 | 1（ES16，402 ns） | 10 | 2 |

  开放起始组三种阈值下 20/20 全程 OPEN。10/20 = 5 + 5 进主结果；5/4/1 的减少同时改变"哪些段合格"和"以哪段为参照"，不能画成转变持续时间分布。
- 逐句替换（原句 → 新句）：
  - "现有规则把该保存点记为开放方向" → "生成派生数据时采用的双读出判据，将该保存点记为开放方向"。
  - "B2 新增的持续开放段计数有用……没有形成……新的结论内容" → "B2 补充了不同事件定义下的 10/20 结果，改善了描述的具体程度；本轮没有将该贡献独立归因于规则提示"。
  - "即使放宽这一条……也让本轮难以满足其余严格条件" → 拆成三句：格式条件未满足（引用编号，设计限制）；科学质量（A1、B1、B2 主计数正确，A2 错误，B1 局部措辞错误，B2 内容差异）；管理决定（暂不扩展，原因见 A1 第三栏）。
  - "两份 B 都在答复中带入了 RMP 等词" → 先解释："RMP restraint、prior ensemble、fit objective 是 FRET 辅助建模论文（Dimura 2020）的专用条件；R0、dye/AV 是单分子 FRET 校准条件（Hellenkamp 2018）。它们经选择器映射进入了本题的规则提示。"
  - §5 表 A2 行"普通后续文本未覆盖它" → "提交后又发了一段普通文字，程序按冻结协议没把它当作修订"。
  - §8 "按预定五结果表归入第 3 行，自动推进为 false" → "本轮保留科学结果，但暂不自动扩展到下一蛋白；原因是提示适用性已有明确问题，而科学收益尚未稳定建立。"状态码和六条判据移到附录。
  - §4 CPMG 行加一句："少数交换态与闭合结构的对应是作者的模型解释，不是直接实验证明。"
- 加一段给 Soojung 的三句摘要（放 §3 末）：闭合起始组一半轨迹在 1 μs 内出现持续开放方向读数，开放起始组没有相反变化；这是派生判据下的方向不对称，不是论文意义上完整转变的复现；核心区域判据几乎不覆盖这批数据，下一步要把方向读数与作者的 NOE 违例对照。

### A5 补齐 §15 汇报包（按 `POST_RUN_REPORTING_PROTOCOL_ZH.md`，这次是硬性完成条件）
- `claim_source_map.jsonl` ≥ 25 行（每个进报告的数字一行）；`ROUND_BRIEF_ZH.md/.html`（`plain-project-reporting-zh`）；`DYNAMICS_ATLAS_HSP90_Q01_DEEP_READER_ZH.md/.html/.pdf`（`atlas-science-report` §4 结构，只重组已有材料）；`DYNAMICS_ATLAS_HSP90_Q01_COLLABORATOR_REPORT.pptx` 10–12 页 + `slide_build/build_deck.mjs` + `render/` + `deck_qa.json`；图 ≤ 3 张：(1) 分区表的条形图（按阈值分面）；(2) ES15 与 ES03 的逐帧 `geometry_delta_A`/`contact_margin_A` 与方向条带；(3) 四份答复核对状态；`REPORT_INDEX.md`；`review_report.md` 填 atlas §10 八项。
- 写 `RT/report_bundle_check.py`：检查上述文件存在且非空、HTML 含 ≥ 5 个 `<h2>`、PPTX 页数 ≥ 10 且每页有 notes、claim map 行数 ≥ 25。**不通过，轨道 A 不算完成，不进轨道 B。**

### A6 更新过期文件与控制面板
- `TASK2/outputs/REPLAY.md` 重写（现在是认证停机时的旧版）：命令、冻结哈希、系统提示与 A/B 用户提示原文（B 的规则文本以哈希引用）、确定性/LLM 边界、换问题要改哪些文件。
- 重新渲染 `outputs/HSP90_Q01_VERIFIED_REPORT_ZH.html`（现在是旧版）。
- `WS/autoresearch/DYNAMICS_ATLAS_STATUS.md` 加 v0.254：四次运行完成、费用、row 3 / proceed false 及三栏理由、轨道 A–D 计划；`DYNAMICS_ATLAS_DECISION_LOG.jsonl` 追加 `DA-20260910-003`（首轮完成与判定）、`DA-20260910-004`（凭证一次性例外的记录）、`DA-20260910-005`（采用 v4）。
- PR #27 正文改成当前状态（不再写"代码已准备好进行案例准备、没有新的科学结果"）；`RT/agent_run.py` 文件头 docstring 改为"任务级 Luna 运行器，首轮四次运行已完成，见 review/…"；`RT/README.md` 同步。
- `TASK2/outputs/WEEKLY_STATUS_20260912.md/.html`。
- 提交信息说明只改评价与文档，数值与原始答复未动。

## 3. 轨道 B：派生方向判据 vs 作者原生 NOE 违例（3 个工作日，`TASK_B`）

### B0 事实与原料（本机已核实）
- 作者沉积的违例时间序列：`ACQ/data/contract/MD/ANALYSE/{R46A,R60A}/VIOLATION/{ES,GS}/<traj>/avg_up_violations_time.dat`，每文件 1001 帧（第 1–1001 帧），第 2 列 = 按 N 个态特异 NOE 对平均的上限违例（Å），第 3 列 = 伪距离版本。`ES` = 闭态特异 NOE 集，`GS` = 开态特异 NOE 集（对应 `Tools/VIOLATION/NOE_specific_{ES,GS}_2022-01-07_distances.itp`）。80 个文件的路径与 sha256 已在 `WS/autoresearch/tasks/dynamics_atlas_hsp90_v1_science_20260728/results/round2/contact_input_manifest.json`。
- 派生表里的 `contact_margin_A` 就是 `V_closed − V_open`（`run_hsp90_v1.py` 第 1128–1141 行），对齐规则：违例文件第 1–1001 帧 ↔ 派生表 20–1020 ns 的 1001 点。**沿用这一对齐，不另定。**
- 论文定义（Methods，`henot_2022_article.txt` 第 617–632 行）：V = (1/N) Σ max(0, d_ij − d_ij^viol)，d^viol = ⟨d_ij⟩ + 2σ（20 个 NMR 结构束）。V = 0 即与该态的 NOE 完全兼容。
- 作者分类（SI Fig. 7a/7b 图注，`henot_2022_supplement.txt` 第 470–482 行）：20 条闭合起始轨迹分为 a–c 兼容闭态 NOE（3）、d–g 近闭态（4）、h–p 向开态转变（9）、q–t 两者皆非（4）。
- 抽样（审查时看过）：ES15 的 V_open 由前 100 ns 均值 9.1 Å 降至末 100 ns 1.1 Å，V_closed 由 8.2 升至 25.7 Å；开放起始 GS01 全程 V_open 0.1–0.5 Å、V_closed 28–30 Å。

### B1 建任务与冻结（半天）
- `init_task.py --task-id dynamics_atlas_hsp90_noe_crosswalk_v1_20260911 --goal "派生方向判据与作者 NOE 违例的逐轨迹对照"`；回执 PASS。
- 复制 80 个 `.dat`、`frame_state_assignments.tsv`、`trajectory_time_anatomy.tsv`、`directional_runs.tsv` 到 `TASK_B/inputs/`，逐文件 sha256 与 `contact_input_manifest.json` / 首轮冻结哈希比对，写 `TASK_B/inputs/MANIFEST.json`。任一不符 → 停，写缺口报告。
- **运行前冻结**分析规则 `TASK_B/protocol/PREREGISTERED_RULES.md`（哈希进 `frozen_crosswalk_v1.json`）：
  1. 逐帧原生类别：`OPEN_NOE` 若 V_open ≤ τ 且 V_closed > τ；`CLOSED_NOE` 若 V_closed ≤ τ 且 V_open > τ；`BOTH_FAR` 若两者 > τ；`BOTH_NEAR` 若两者 ≤ τ。τ 预注册三档 {0.5, 1.0, 2.0} Å，主报告用 1.0 Å，其余作敏感性；**不为对上 7/9/4 调 τ**。
  2. 开放起始参照带：20 条开放起始轨迹全部 20 020 点的 V_open 第 95 百分位 = `p95_open`；一条闭合起始轨迹"进入开态 NOE 兼容区"= V_open ≤ p95_open 且连续 ≥ 50 个点（真实时间 ≥ 49 ns）；记首次进入时间与之后是否离开（≥ 50 点 V_open > p95_open）。
  3. 逐轨迹交叉表：首轮的方向分区（阈值 5 与 50：首开 / 先闭后开 / 只闭 / 无）× 原生类别时间占比（四类）× 首次进入开态兼容区时间 × 末 100 ns 的 V_open、V_closed 均值。
  4. 作者分类对照：用 `fitz` 渲染 SI 第 16–17 页，若图面板标有轨迹编号，则把 a–t 映射到 ES 编号，做逐轨迹交叉表；否则只做组级对照（本轮 10/10 vs 作者 7/9/4），记 `PANEL_MAPPING: NOT_AVAILABLE`，不猜。
  5. 判读规则（预注册）：某条轨迹的 OPEN_CONSENSUS 段内 `OPEN_NOE` 占比 ≥ 0.8 → "方向读数与原生观测一致"；OPEN_CONSENSUS 段内 `BOTH_FAR` 占比 ≥ 0.5 → "方向读数只说明相对偏好，未接近开态原生定义"；介于两者 → "部分一致"。开放起始组作为阳性对照必须 ≥ 18/20 落在"一致"，否则停止并报告规则本身有问题。
- 声明主张上限：同一数据包的派生再分析；不是新的实验验证；不估计平衡占比或速率；不判定作者分类对错。

### B2 计算（1 天）
- 一个脚本 `TASK_B/scripts/noe_crosswalk_v1.py`（numpy/pandas，只读输入，输出到 `TASK_B/outputs/`）：`per_frame_native_class.tsv`（40 040 行）、`per_trajectory_crosswalk.tsv`（40 行）、`group_summary.json`（含三档 τ 的敏感性）、`author_panel_mapping.json`。
- 图 ≤ 3 张（`data-visualization` → `nature-figure backend=python` → `matplotlib`，先写 figure_contract）：(1) 三条示例轨迹（ES15 先闭后开、ES03 首开、ES01 只闭）的 V_open、V_closed 曲线加方向条带；(2) 40 条轨迹的"OPEN_CONSENSUS 占比 vs OPEN_NOE 占比"散点，按 seed lineage 与分区着色；(3) 分区 × 原生类别的交叉热图。
- 一次哈希：输入清单 + 脚本 + 输出。

### B3 报告与汇报包（1 天）
- `TASK_B/outputs/HSP90_NOE_CROSSWALK_REPORT_ZH.md/.html`，回答 Pro 的三个问题并各配一行证据：开放方向片段是否伴随开态特异 NOE 违例降低；是否仍同时偏离两套参照；哪些结果只说明方向偏好、哪些更接近原生结构解释。
- 三种结果都写成有用结论：一致 → 首轮方向分析的结构解释有依据；部分一致 → 给出适用范围（哪些轨迹、哪个阈值）；不一致 → 修正对派生判据的解释，并明确写"不是要 Agent 更忠实地使用它"。
- §15 汇报包（简报 + 读本 + 6–8 页 deck）+ `report_bundle_check.py` 通过；STATUS 与决策日志各加一条。
- 可选 B4（时间够才做，≤ $0.03）：把 80 个 `.dat` 与 `PREREGISTERED_RULES.md` 加进一份新的公开包，跑一次 Agent A-only，看它是否独立得到同一交叉表；记为开发观察，不是 A/B。

## 4. 轨道 C：规则适用性的窄修复（1 个工作日，可与 B 并行，`RT`）

- 问题定位（已核实）：选择器给出的义务是通用的（如 `required_check: Audit generator or parentage, prior-data reuse …`），但渲染时把注册表整条 `proposed_project_rule / required_fields / abstain_route` 当作"必填 / 弃权路线"呈现；C003-RULE-002（Dimura 2020，FRET 辅助建模，`transfer_scope: only within declared candidate support`）和 C001-RULE-002（Hellenkamp 2018，smFRET，`transfer_scope: requires explicit calibration provenance`）的专用条件因此进了 B 的答复。注册表自带的 `transfer_scope`、`paper_id` 已足够做区分。
- 改动只在渲染层：
  1. 新增 `RT/paper_method_family.json`：12 篇论文（C001–C012）→ 方法家族（从注册表 `paper_title` 手填，如 hellenkamp_2018 → `smFRET`；dimura_2020 → `FRET_ASSISTED_MODELING`；fuertes_2017 → `SAXS,smFRET`；wankowicz_bonomi_2026 → `GENERAL_ENSEMBLE`；…），每条带 `source: rule_registry.tsv paper_title`。
  2. `render_active_rules.py`：每个 `rule_id` 块先渲染**义务本身**（`required_check` 与 `reason_from_input`，这是选择器对本题的项目归纳）；注册表条款渲染为"原条款（来源 `paper_id`，方法家族 X，transfer_scope 原文）"；只有当案例元数据档里的方法集合与该家族相交、或 `rule_class ∈ {claim_ceiling, estimand_non_equivalence, evidence_role_separation}`（与方法无关的类）时，才显示"必填：… 弃权路线：…"；否则显示"本题适用性未确认：以上条件不作为必填或弃权理由"。
  3. 不删任何原文；不改注册表；不改选择器；不改 method scope。
- 测试 `test_rules_bridge_offline.py` 加两例：对首轮冻结的 `review_obligations.json`，C003-RULE-002 与 C001-RULE-002 渲染为"适用性未确认"，其余五条不变；块数与配对不变。
- 可选开发回归（≤ $0.03）：用新渲染的 `ACTIVE_RULES.md` 跑一次 B。结果只回答"专用术语是否还进答复"，标 `DEV_REGRESSION`，放 `TASK2/outputs/dev_regression/`，不与首轮四份比较，不改 `round_decision.json`。
- 报告里区分三种都叫"规则"的东西：定义数据标签的判据、给 B 的科学提醒、控制推进的管理条件。

## 5. 轨道 D：第二体系，普通 Agent + 成熟方法（8 个工作日，`TASK_D`）

**前提是轨道 A 已交付（`report_bundle_check.py` 通过），不以 Rules 增益为前提。** 这是回到项目原始目标的科学工作，不是 Rules 实验。

- D1 只读盘点（1.5 天，$0）：按 v3.4 §14.2 的 D0–D4 表和三条科学准入规则 (a)(b)(c) 各写一份 `<SYS>_DATA_LANDSCAPE.md`，选一个；元数据盘点只是暂定准入，下载后、运行前复核。ADK 本机有 1AKE/4AKE Cα 与 8/30 公开包（历史资产含项目结论，进 `hidden/`）；DHFR 本机无。都不合格 → `NEITHER_QUALIFIES`，停。
- D2 下载（授权 5）：≤ 2 GB，`DOWNLOAD_MANIFEST.json` 记 `url, sha256, size, license`；每次下载前核全局累计。
- D3 案例包（2 天）：B0 来源卡（论文声明 / 本轮输入已核对两层）、B1 盘点与 `FIELD_DEFINITIONS.md`（只写判据，不放汇总结果与答题提示）、B2 题面（论文自己陈述的一个可比较性质，作者报告带 locator，作者主张是待检验对象）、rubric（公开问题 + 数据 + 论文，运行前冻结）、`literature_claims.json` 6–10 条、B3 冻结。预处理只做论文方法节已有的既定分析，预处理与建包 ≤ 2 天；需新科学方法或改 `RT` 逻辑 → 停，记范围限制。
- D4 运行：`run_order = [A, A]`（同一 Agent 两次，观察可重复性；无 B）；≤ $0.20；分支与 §5 同 v3.4。
- D5 核对与报告：三列核对 + 全文主张 + **逐答复真实引文**的论文关系表（用轨道 A 的校验脚本）；两层报告；§15 汇报包；`report_bundle_check.py` 通过；STATUS 与决策日志各一条。
- 结束即停，不进第三体系；是否再做 B 组、是否做第三体系由 PM 看轨道 B/C 结果后决定。

## 6. 时间、费用、停止线

| 轨道 | 工作日 | 模型费用 | 下载 | 检查命令 | 哈希 |
|---|---|---|---|---|---|
| A0 | 1 | 0 | 0 | 1（汇报包检查） | 0 |
| A | 2 | 0 | 0 | 3（关系表校验、汇报包检查、harness 套件） | 0 |
| B | 3 | ≤ $0.03 | 0 | 2（清单比对、阳性对照） | 1 |
| C | 1 | ≤ $0.03 | 0 | 1（桥接测试） | 0 |
| D | 8 | ≤ $0.20 | ≤ 2 GB | 4 | 1 |
| **合计** | **15** | **≤ $0.26（上限 $0.30）** | **≤ 2 GB** | **11** | **2** |

- 开工当天写 `TASK2/outputs/DEADLINE_V4.json`（绝对日期，不重置）；每次模型请求和下载前核全局累计（`TASK2`、`TASK_B`、`TASK_D` 账本合计）。
- 任一 `UNKNOWN_CHARGE.json` → 全部停。失败账本两次修补未解 → 该轨道停，交报告，不进下一轨道。需交互登录、额外授权、隔离或准入不满足 → 停。
- 每个工作周末一页 `WEEKLY_STATUS_<日期>.md/.html`（`plain-project-reporting-zh`）。周报不替代停止条件。

## 7. 防止首轮问题重演的机制

| 首轮出现的问题 | 本版机制 |
|---|---|
| §15 汇报包一件没做，`review_report.md` 空，claim map 0 行 | `report_bundle_check.py` 是每条轨道的完成条件；不通过不进下一轨道（A5、B3、D5） |
| REPLAY.md、HTML 是认证停机时的旧版 | A6 明确重写清单；每条轨道结束前 `grep -L` 检查这些文件的修改时间晚于最后一次运行 |
| STATUS 与决策日志停在运行前 | 每条轨道结束各追加一条，作为完成条件写进 A6/B3/D5 |
| 论文关系表是模板，三份文件相同 | `check_relation_tables.py`：占位句、跨文件相同内容、原句不可定位三种情况都拒绝 |
| 判定理由把格式、科学、管理揉在一起 | `round_decision.json` 三栏结构；以后每轮沿用 |
| 凭证从会话记录文件取回 | 授权 6：shell export 或钥匙串；启动脚本发现 key 不在环境变量里直接停，不去找文件 |
| 规则正文把专用条件当通用必填 | 轨道 C 渲染层修复 + 测试 |
| "常规箱"这类局部措辞被当作核心错误 | `severity` 列；只有 CORE 级 MISMATCH 才进管理决定 |
| 计划按天给上限，实际 45 分钟跑完却跳过了汇报 | 完成条件按产物不按时间；时间只是停止线 |
| 两周多没有给组里的报告，内部产物却有几十个 | 轨道 A0 先出进度报告；每周五一份对外更新；没有交付物不出新版计划；内部任务目录每周 ≤ 3 个（指南 §8） |

## 8. 处置表

### 8.1 Pro 对首轮结果的审查

| Pro 意见 | 处置 | 落在 |
|---|---|---|
| 保留科学结果与暂停自动推进；修改评价理由 | FIX | A1 |
| 10/20 是有内容的补充，不因写在"分析"节被排除；未报 A1 每项诊断 ≠ 退化；"常规箱"是局部错误；不引用编号不是科学失败也不补写 | FIX：判据 (a)(c)(d) 改值，proceed 不变，理由三栏 | A1、A3 |
| 把三个科学问题作为正文主线；5/4/1 揭示事件定义；核心近空是覆盖诊断；与论文是有限定性对应 | FIX：新开头 + 分区表 + 逐句替换 | A4 |
| 方法适用性在"义务—规则正文"之间丢失；保留原条款范围，跨方法检查单独表述；不重写 33 条 | FIX | 轨道 C |
| 论文关系表不是逐主张对应；AGENT_ABSTAIN 滥用；建议不应标 NOT_LOCATED | FIX | A2、A3 |
| 下一项科学工作：派生方向 vs 原生 NOE 读出；有期限；不调阈值追 7/9/4 | FIX：原料已在本机，确定性脚本 | 轨道 B |
| 不要把其他蛋白的科学工作绑在 Rules 增益上 | FIX | 轨道 D |
| 标题、开头、六句替换、CPMG 作者模型解释 | FIX | A4 |
| PR 正文与运行器 docstring 过期 | FIX | A6 |

### 8.2 本机审查新增

| 发现 | 处置 |
|---|---|
| §15 汇报包缺失 | A5 + 完成检查 |
| REPLAY/HTML/STATUS/决策日志未更新 | A6 |
| 凭证启动例外 | 授权 6 + 决策日志记录 |
| 5/5/10 分区没写进报告 | A4 主表 |
| 作者 NOE 违例序列与 SI Fig 7 分类在本机 | 轨道 B 原料 |
| A2 失败模式（0 次计算、混阈值） | rubric 已罚错误计数；不强制 Python；D 轮沿用 |

## 9. 给 Codex 的一句话

不重跑 HSP90 同题 A/B。先按 `REPORT_WRITING_GUIDE_ZH.md` 写一份从 Rules Table 起步讲到现在和下一步的进度报告与组会 deck（轨道 A0，1 天），再把首轮收口做完（理由三栏、关系表逐句、报告改写、汇报包补齐、过期文件与控制面板更新，`report_bundle_check.py` 通过），再做派生方向与作者 NOE 违例的对照分析（本机数据，预注册规则，三个工作日），并行做规则渲染层的窄修复；然后用普通 Agent 做第二体系的科学答复，不以 Rules 增益为前提。授权 1–7 到位后自动推进、不等人，15 个工作日、$0.30、2 GB 到线即停；每周五交一份给人看的更新；任何一条轨道停下都交报告，不补造结果。
