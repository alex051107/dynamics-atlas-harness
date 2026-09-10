# 跑完之后自动出报告：Codex 汇报协议（v1，随计划 v3.3 §15 生效）

Dynamics Atlas · 2026-09-10 · **供 Codex 无人值守执行** · 每个体系的一轮结束、每次停止、每周末各触发一次

> 这份协议回答一个问题：Codex 跑完一轮（或停下来）之后，用本机哪几个 skill、按什么顺序、产出哪几个文件，让 PM 打开一个 HTML 就能看懂发生了什么，并且有一份能直接放到组会上的 slides。它不改变计划里的任何数字、判定或停止条件；汇报只引用 `HSP90_Q01_VERIFIED_REPORT_ZH.md`、`claims_check.csv`、`round_decision.json` 里已有的内容，不产生新结论。

## 0. 三个触发点，三种产出规模

| 触发 | 时机 | 产出 | 时间上限 |
|---|---|---|---|
| **轮末报告** | 一个体系的 §7 报告和 §8A `round_decision.json` 写完之后 | §2 全套：简报 HTML + 深度读本 HTML/PDF + 组会 slides PPTX + 索引 | 1 个工作日（计入该轮的阶段 E；HSP90 首轮上限因此从 7 天改为 8 天） |
| **停止简报** | §12 失败账本两次未解、§14.5 任一停止线到线、A0/A5/§5 任一分支停止、PM 叫停 | 只出 `STOP_BRIEF_ZH.md/.html` + `REPORT_INDEX.md`；不做 slides | 2 小时 |
| **周报** | 每个工作周末（计划 §14.1） | `WEEKLY_STATUS_<YYYYMMDD>.md/.html` 一页 | 1 小时 |

汇报永远排在判定之后：先写 `round_decision.json`，再做汇报。汇报做不完不推迟判定，也不阻止下一体系开工；做不完的部分记进 `review_report.md`。

## 1. 用哪些 skill，不用哪些

Codex 能看到两处 skill：工作区 `WS/.agents/skills/`（项目专属）和 `~/.codex/skills/`（全局）。本协议只用下面这些，**按顺序、各调一次**。

| 顺序 | Skill | 位置 | 在这里负责什么 | 不负责什么 |
|---|---|---|---|---|
| 1 | `atlas-science-report`（v1.2） | `WS/.agents/skills/atlas-science-report/` | **权威层**。定路线（本项目用"scientific-case route"）、冻结 `claim_source_map.jsonl`、术语表、图表契约、§10 八项 QA。先读它的 `references/skill_routing.md`、`report_template.md`、`narrative_quality.md`、`domain_language.md` | 不写新科学结论 |
| 2 | `plain-project-reporting-zh` | `~/.codex/skills/plain-project-reporting-zh/` | 写 PM 简报（`ROUND_BRIEF_ZH.md`）和周报：第一句先回答"这轮做出来了什么、判了什么、下一步是什么"，主文不出现文件名、字段名、SHA | 不写深度读本 |
| 3 | `storytelling-narrative` | `~/.codex/skills/storytelling-narrative/` | 给 slides 定一条主线（"从 X 到 Y，因为 Z"）和 ghost-deck 标题序列；读它的 `references/formats.md` 的 Slide deck 节 | 不碰数字 |
| 4 | `academic-pptx` | `~/.codex/skills/academic-pptx/` | slides 的内容与论证结构：action title、每张结果页一个主图、附录策略；读 `content_guidelines.md`、`slide_patterns.md` | 不负责生成文件 |
| 5 | `academic-ppt` | `~/.codex/skills/academic-ppt/` | 用 PptxGenJS 实际生成 `.pptx`（白底、单一强调色 `1E3A5F`、无阴影无渐变），交付 `.pptx` + 源 `.js` | 它引用的 `$slides` 在本机**不存在**，渲染与校验按 §4 的替代方案做 |
| 6 | `data-visualization` → `nature-figure`（`backend=python`）→ `matplotlib` | `~/.codex/skills/` 三个目录 | 结果图（≤ 4 张）：先定图表语义与图表契约，再用 matplotlib 实现，导出 PNG + SVG | 不改阈值、不选状态、不算新量 |
| 7 | `human-writing` | `~/.codex/skills/human-writing/` | 中文读本与简报冻结后的最后一遍改稿：读它的 `references/revision.md`，跑它的 prose checker；只改可读性，不改事实、术语、来源链接、不确定性 | 不当第一作者 |
| 8 | `humanizer-zh-plus` | `~/.codex/skills/humanizer-zh-plus/` | 只做诊断：`python3 ~/.codex/skills/humanizer-zh-plus/scripts/scan_ai_prose.py <file>`；只处理它标出的散文句子，表格、路径、术语、数值不动 | 不做主要写手 |

`nature-writing` / `nature-polishing` 只在需要**新写一段英文科学散文**（deck 正文）时按 `skill_routing.md` §2.2 调用，并按其要求声明 `paper_type / section / language / journal`；本项目 deck 正文短，多数情况下用 §7 报告里已冻结的句子改写即可，不必调用。

**明确不用：** `weekly-report`（那是 HSP90 LiGaMD3 论文项目和 TrpB 的周报格式，不是本项目）；`scholar-slides` 和 `nature-paper2ppt`（论文→slides，且需要 venv/Playwright 人工检查点）；`trpb-meeting-prep`、`p15-weekly-reporting`（别的项目）；`pptx`/`docx`/`slides`（Codex 侧未安装，学术 skill 里提到它们时按 §4 替代）。

## 2. 轮末报告：产出清单与目录

全部写进 `TASKn/outputs/report/`（`TASKn` = 该轮任务目录）：

```text
report/
  REPORT_INDEX.md                      ← PM 从这里开始：阅读顺序 + 每个文件一句话
  claim_source_map.jsonl               ← 事实脊柱（atlas-science-report §2 格式）
  ROUND_BRIEF_ZH.md / .html            ← PM 简报，一页，说人话
  DYNAMICS_ATLAS_<CASE>_DEEP_READER_ZH.md / .html / .pdf   ← 深度读本（给 PM 看的正文）
  DYNAMICS_ATLAS_<CASE>_COLLABORATOR_REPORT.pptx           ← 组会 slides（英文正文 + 中文讲稿在 notes）
  slide_build/build_deck.mjs           ← slides 源码（可再生成）
  render/deck.pdf, render/slide-XX.png ← slides 渲染 QA
  deck_qa.json                         ← 结构校验结果
  figures/fig_XX.png, fig_XX.svg       ← 结果图 ≤ 4 张
  ARCHIVE_MANIFEST.md                  ← 每个文件的来源与 sha256
  review_report.md                     ← atlas-science-report §10 八项 QA 的自检结果，含没做完的项
```

`<CASE>` 首轮为 `HSP90_Q01`。所有 HTML 自包含（内联 CSS、带目录、手机可读），PM 不需要装任何东西。

### 2.1 事实脊柱 `claim_source_map.jsonl`（先于一切）
每条重要陈述一行：`claim_id, exact_claim, status ∈ {Observed, Interpretation, Design proposal}, source_locator, artifact_version, numerator/denominator/unit/statistical_unit, allowed_wording, forbidden_upgrade, used_in`。来源只允许四处：`HSP90_Q01_VERIFIED_REPORT_ZH.md`、`check/*_claims_check.csv`、`round_decision.json`、`HSP90_SOURCE_AND_RUN_CARD.json`。Agent 原始答复里的数字只有在 `claims_check.csv` 标 `VERIFIED` 时才能进 Observed；`NOT_INDEPENDENTLY_VERIFIED` 的进 Interpretation 并注明。

### 2.2 PM 简报 `ROUND_BRIEF_ZH.md`（`plain-project-reporting-zh`）
一页，四段，顺序固定：
1. **这轮做出来了什么**：科学答复的一句话结论及条件（引 §7 报告第 3 节）。
2. **规则提示有没有用**：B 相对 A 多说/少说/说错了什么，一句一条，不下因果结论；`round_decision.json` 判了第几行、`proceed` 是什么。
3. **哪里没做成**：分支、失败账本、未核验项、人工介入了几处。
4. **下一步**：按判定，Codex 已经在做什么 / 停在哪等 PM。
主文零文件名零字段名；文末一节"复核信息"列 5 个以内的路径。

### 2.3 深度读本 `DYNAMICS_ATLAS_<CASE>_DEEP_READER_ZH.md`（`atlas-science-report` §4 架构）
按该 skill 的 Part I–VI + 附录 A–E 结构写，但**只重组已有材料**：§7 报告的八节、`REPLAY.md`、B0 卡、`FIELD_DEFINITIONS.md`、核对表、`AGENT_RAW/` 摘录。每个"Analysis"章节的"Code walkthrough"指向 Agent 在 `events.jsonl` 里实际跑的代码和 Codex 的复现脚本，不新写分析。附录 B 的 figure_contract 覆盖 §2.5 的每张图。附录 E 的 Q&A 预答 Soojung 会问的问题（时间窗口、统计单位、departure 相对什么、为什么不能说占比）。

### 2.4 组会 slides `DYNAMICS_ATLAS_<CASE>_COLLABORATOR_REPORT.pptx`
路线：`storytelling-narrative`（主线与标题序列）→ `academic-pptx`（结构）→ `academic-ppt`（生成）。10–12 页，页序按 `atlas-science-report` §3 的 scientific-case 模板，落到本实验就是：

| 页 | Action title 要说明的事 | 主图/主表 |
|---|---|---|
| 1 | 题目 + 一句话目的 | — |
| 2 | 异质动力学资料为什么难比 | 一张示意 |
| 3 | 研究问题 Q01 原话 | 题面 |
| 4 | 为什么是 HSP90 / Henot 2022；open/closed/transition 的原文定义 | 原文 locator |
| 5 | 实际拿到的资料：40 条轨迹、20–1020 ns、逐帧派生量、三阈值分类表；力场与帧数两处文档记载分别保留 | B0 卡 |
| 6 | 冻结的分析逻辑：同一 Agent、同一资料，B 组多一份可质疑的规则提示；评分独立于规则 | 一张流程图 |
| 7–8 | 结果：按阈值分别统计的方向持续与离开/回返候选（只引 VERIFIED 数字，写明 n、单位、窗口） | fig_01/02 |
| 9 | 四份答复各自答对/过强/弃权/未完成 | 表 |
| 10 | B 相对 A 改变了什么；判定落在第几行；推进 ≠ Rules 有效 | 表 |
| 11 | 与 Henot 2022 逐主张关系（AGREE/DISAGREE/PAPER_SILENT/…） | HPA 表 |
| 12 | 结论、限制、下一步需要人决定什么 | — |
| 附录 | 人工介入清单、核对表摘要、参考文献 | — |

规矩：标题是完整句子不是标签；每页 speaker notes 写中文讲稿 + 用到的 `claim_id`；每个数字页脚标来源；"Thank you"页不要，最后停在结论页。

### 2.5 结果图 ≤ 4 张
候选：(1) 40 条轨迹 × 三阈值的 first_persistent_direction 与 departure 候选计数（按 seed lineage 分面）；(2) 一条有 departure 候选的轨迹的逐帧 `geometry_delta_A` / `contact_margin_A` 时间曲线并标出持续段；(3) 四份答复的核对状态堆叠条；(4) B−A 差异表的可视化（可省）。每张先写 `figure_contract`，再画；数据只从 `common/`、`hidden/reference_values.json`、`check/` 读；导出 PNG（300 dpi）+ SVG。

## 3. 语言链（每遍只跑一次）
1. 用 `claim_source_map.jsonl` 起草简报、读本、deck 文案（中文为主；deck 正文英文）。
2. `storytelling-narrative`：只用于 deck 的主线与标题序列。
3. 冻结事实后，`human-writing` 改中文简报与读本（读 `references/revision.md`，跑其 checker）。
4. `humanizer-zh-plus` 扫描：`scan_ai_prose.py` 跑简报与读本各一次，只改它点名的散文句；表格、代码、路径、数值、术语不动；破折号密度警告在技术 Markdown 里可忽略。
5. 改完后对照 `claim_source_map.jsonl` 复核：每个数字、每个 Observed/Interpretation 标签没变。

## 4. 生成与渲染的具体命令（本机已核实的工具）

```bash
NODE_MODS=~/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules   # 已有 pptxgenjs、marked、playwright
R="$TASKn/outputs/report"

# 4.1 Markdown → HTML(+PDF)：复用 TASK0/scripts/render_plan.mjs 的做法（marked + Chromium 打印），改成接收文件名参数
cp "$TASK0/scripts/render_plan.mjs" "$TASKn/scripts/render_report.mjs"   # 把写死的 EXECUTION_PLAN_ZH 改为 argv[2]
node "$TASKn/scripts/render_report.mjs" "$R/ROUND_BRIEF_ZH.md"
node "$TASKn/scripts/render_report.mjs" "$R/DYNAMICS_ATLAS_HSP90_Q01_DEEP_READER_ZH.md"

# 4.2 slides：academic-ppt 的 PptxGenJS 流程，pptxgenjs 直接从 NODE_MODS 引
mkdir -p "$R/slide_build" && node "$R/slide_build/build_deck.mjs"       # 源码里 import pptxgenjs from "$NODE_MODS/pptxgenjs"

# 4.3 slides 结构校验（替代缺失的 $slides / pptx skill）：python-pptx 1.0.2 已在宿主机
python3 - <<'EOF'
from pptx import Presentation; import json,sys
p=Presentation(sys.argv[1] if len(sys.argv)>1 else "DYNAMICS_ATLAS_HSP90_Q01_COLLABORATOR_REPORT.pptx")
bad=[]
for i,s in enumerate(p.slides,1):
    title=s.shapes.title.text if s.shapes.title else ""
    notes=s.notes_slide.notes_text_frame.text if s.has_notes_slide else ""
    if len(title.split())<4: bad.append((i,"title-is-label",title))
    if not notes.strip(): bad.append((i,"no-notes",""))
json.dump({"slides":len(p.slides),"problems":bad},open("deck_qa.json","w"),ensure_ascii=False,indent=1)
print(len(p.slides),bad)
EOF

# 4.4 slides 渲染 QA：LibreOffice 已在 /opt/homebrew/bin/soffice
soffice --headless --convert-to pdf --outdir "$R/render" "$R/DYNAMICS_ATLAS_HSP90_Q01_COLLABORATOR_REPORT.pptx"
python3 -c "import fitz,sys;d=fitz.open('$R/render/DYNAMICS_ATLAS_HSP90_Q01_COLLABORATOR_REPORT.pdf');[p.get_pixmap(dpi=110).save(f'$R/render/slide-{i+1:02d}.png') for i,p in enumerate(d)]" \
  || echo "fitz 不在宿主机：保留 PDF 作为渲染证据，deck_qa.json 记 render_png=SKIPPED"
```

渲染出来的 PNG 逐张看一遍：文字溢出、图片压字、空占位符任一出现就改源码重生成；改两次还不行 → 交 PDF/PNG 版并在 `review_report.md` 记"PPTX 编辑版未通过视觉 QA"。

## 5. 索引与交付

`REPORT_INDEX.md` 固定格式：

```markdown
# <CASE> 轮末报告索引（<日期>）
阅读顺序：1) ROUND_BRIEF_ZH.html（5 分钟）→ 2) render/deck.pdf（组会 15 分钟）→ 3) DEEP_READER_ZH.html（复核用）
判定：round_decision.json → row=<n>, proceed=<true|false>
| 文件 | 一句话 | 大小 |
...
未完成项：<review_report.md 里没做完的>
```

然后把 `report/`（不含 `runs/`、案例数据、账本）复制到 `HARNESS_LUNA/review/<case>-round-<日期>/` 并在 `feature/luna-runtime-v1` 提交（计划授权 3 覆盖）；提交前 `grep -rn "/Users/\|sk-or-v1"` 必须为空。PM 打开 `REPORT_INDEX.md` 就能顺着看。

## 6. 停止简报与周报（轻量）

- **停止简报** `STOP_BRIEF_ZH.md/.html`（`plain-project-reporting-zh`）：四段：停在哪一步、触发了哪条停止条件（引计划节号）、已经保留了什么结果、PM 现在要决定什么。附失败账本链接。不做 slides，不做读本。
- **周报** `WEEKLY_STATUS_<YYYYMMDD>.md/.html`：计划 §14.1 的七项，第一句先说"这周推进到哪"，人话；不重复轮末报告内容。

## 7. 汇报阶段的硬边界
- 只引用已冻结的数字；汇报中出现的每个数字都能在 `claim_source_map.jsonl` 找到来源。
- 不因为要"讲得好看"补跑分析、改图阈值或重跑 Agent。
- "推进"永远不写成"Rules 有效"；"VERIFIED"永远不写成"科学正确"；开发者核对永远不写成"独立评审"。
- 汇报时间超上限：先交简报 + 索引，其余记未完成，不挤占下一体系的天数。
