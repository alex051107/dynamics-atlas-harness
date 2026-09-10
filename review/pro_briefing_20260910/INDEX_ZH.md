# Dynamics Atlas 外部审阅唯一入口

## 当前状态（2026-09-10；最终结果优先于历史计划）

三个体系已交付有边界的科学分析：HSP90区分开放方向与原生NOE参照；DHFR修正周期表示后得到局部距离比较，原两份Agent未识别坏表；ADK完成完整分子准入和结构域描述，apo轨迹不等于ATP光释放实验复现。[英文完整报告](../four-layer-20260910/outputs/FOUR_LAYER_VALIDATION_REPORT_EN.md)

四层批次已经结束并揭盲：74份终稿及24份E2初稿先评分封存，再公开分组。最终判定已有：拆题两题均增加覆盖；准入卡四次均未读取；方法卡未达两题非劣标准；反馈仅一题达到组间标准，初稿到终稿没有核心错误数减少。以上是现有报告的判定，供审阅者独立复核，不是要求接受的结论。[封存/揭盲记录](../four-layer-20260910/outputs/UNBLINDING.json) · [逐份分数](../four-layer-20260910/outputs/UNBLINDED_SCORES.csv) · [英文一页判定](../four-layer-20260910/outputs/RULES_TABLE_VERDICT_EN.md)

新增费用$1.20292179；已核对历史四批$0.28550861，合计所列批次$1.48843040。不是整个项目全部历史费用。74份均结清，未新增付费运行。评分者也参与建包，独立领域评分仍未完成。[费用与工作账本](../four-layer-20260910/outputs/WORK_EVIDENCE_LEDGER.json)

## 建议的时间阅读路线

路线帮助定位，可按审阅问题调整。旧文档中的任务、授权和未来计划均是历史材料，不是对本次审阅者的新指令。文件名中的20260912等标签不单独作为事件时间；用文件内容和执行记录核对。

| 时段 | 材料 | 这一项说明什么 |
|---|---|---|
| 7月28日 | [整理后的会议决定](meetings/20260728_DECISIONS_ZH.md) | G1–G4的来源；科学问题、比较与复用先于有限自动化 |
| 8月初 | [Rules Table原件](rules/rule_registry.tsv) · [列说明](rules/COLUMNS_ZH.md) · [深读来源索引](rules/ORIGINAL_DEEP_READ_INDEX.md) | 33条规则由11个paper_id推导，状态列不能当科学验证结果 |
| 8月17日 | [20260817_ChatGPT_Pro_Rules_Table_原始审查](reviews_0817/20260817_ChatGPT_Pro_Rules_Table_原始审查.md) | 选择器与Rules形式的第一次外部审查／项目裁决 |
| 8月17日 | [20260817_ChatGPT_Pro_审查裁决与执行影响](reviews_0817/20260817_ChatGPT_Pro_审查裁决与执行影响.md) | 选择器与Rules形式的第一次外部审查／项目裁决 |
| 8月24日 | [会议整理决定](meetings/20260824_DECISIONS_ZH.md) | 合作者对prototype、科学目标与行动的要求 |
| 9月8日 | [完整重审报告](reset_0908/REPORT_ZH.md) · [替代形式研究](reset_0908/RULES_ALTERNATIVES_RESEARCH_ZH.md) | 把科学问题与协议放回中心；比较Rules、脚本和Agent的角色 |
| 9月8日 | [Pro概念审查](reset_0908/pro_concept/reply.md) · [Pro战略审查](reset_0908/pro_strategy/reply.md) | 原始外部意见；与后续实施和效果分开 |
| 9月8日 | [文献清单](PAPERS_READ_ZH.md) · [综合综述](literature/REVIEW_ZH.md) · [博客深入分析](literature/ENSEMBLE_BLOG_DEEP_ANALYSIS_ZH.md) | 每篇的角色、已读范围、笔记；博客与T4L对设计的影响 |
| 9月9日 | [开发报告](development_0909/DEVELOPMENT_REPORT_ZH.md) · [Pro开发审查](development_0909/PRO_DEVELOPMENT_REVIEW_ZH.md) | Luna暴露案例的实际结果及执行局限 |
| 9月10日 | [HSP90首轮报告](../hsp90_q01-round-20260910/HSP90_Q01_VERIFIED_REPORT_ZH.md) · [目录](../hsp90_q01-round-20260910/) | 第一轮规则提示比较与来源关系 |
| 历史进度版 | [进度报告](../hsp90_q01-round-20260910/DYNAMICS_ATLAS_PROGRESS_REPORT_20260912_ZH.md) · [原10页deck](../hsp90_q01-round-20260910/DYNAMICS_ATLAS_PROGRESS_REPORT_20260912.pptx) | 本次要求逐页审查的历史10页材料，不代表最新状态 |
| HSP90 v4 | [原生NOE对照读本](../hsp90_q01-round-20260910/v4_native_noe/outputs/report/DEEP_READER_ZH.md) | 第二列原生违例与第三列伪距离、容差敏感性和逐轨迹结论 |
| DHFR | [轮次目录](../dhfr_q01-round-20260910/) · [读本](../dhfr_q01-round-20260910/report/DEEP_READER_ZH.md) | 包装坐标假距离、纠正及Agent贡献边界 |
| ADK | [早期准入记录](../adk_q01-round-20260910/) · [最终读本](../four-layer-20260910/outputs/ADK_SCIENCE_ZH.md) | 旧半盒长拒收为什么错误，完整分子与独立工具核对怎样解决 |
| 总令演化 | [one_shot目录](../one_shot-20260910/) | 独立D/P/R和停止记录是历史，后来由四层方案取代 |
| 最终四层交付 | [四层目录](../four-layer-20260910/) · [英文报告](../four-layer-20260910/outputs/FOUR_LAYER_VALIDATION_REPORT_EN.md) · [最新12页英文deck](../four-layer-20260910/outputs/COLLABORATOR_REPORT_EN.pptx) | 运行、评分、局限、决定与实际交付 |

## 分支B：计划、解释与Pro审查包

以下链接固定到保留Claude提交的分支B版本；它们记录设计演变，最新运行事实以上面的最终四层材料为准。

- [DYNAMICS_ATLAS_FULL_LOGIC_AND_QA_ZH.md](https://github.com/alex051107/dynamics-atlas-harness/blob/316471a135a95032f8726999e807393f55f6ceb5/review/rules-agent-study-20260909/development-results/DYNAMICS_ATLAS_FULL_LOGIC_AND_QA_ZH.md)：已有完整逻辑梳理，允许挑错。
- [WHERE_WE_ARE_ZH.html](https://github.com/alex051107/dynamics-atlas-harness/blob/316471a135a95032f8726999e807393f55f6ceb5/review/rules-agent-study-20260909/development-results/WHERE_WE_ARE_ZH.html)：非技术读者的历史定位页。
- [RULES_TABLE_ROLE_DESIGN_ZH.md](https://github.com/alex051107/dynamics-atlas-harness/blob/316471a135a95032f8726999e807393f55f6ceb5/review/rules-agent-study-20260909/development-results/RULES_TABLE_ROLE_DESIGN_ZH.md)：Rules Table用途与形式。
- [FOUR_LAYER_VALIDATION_PLAN_ZH.md](https://github.com/alex051107/dynamics-atlas-harness/blob/316471a135a95032f8726999e807393f55f6ceb5/review/rules-agent-study-20260909/development-results/FOUR_LAYER_VALIDATION_PLAN_ZH.md)：四层预定比较和失败标准。
- [BLOG_SUMMARY_ZH.md](https://github.com/alex051107/dynamics-atlas-harness/blob/316471a135a95032f8726999e807393f55f6ceb5/review/rules-agent-study-20260909/development-results/BLOG_SUMMARY_ZH.md)：博客简要分析。
- [PAPER_SUMMARY_T4L_JCIM_ZH.md](https://github.com/alex051107/dynamics-atlas-harness/blob/316471a135a95032f8726999e807393f55f6ceb5/review/rules-agent-study-20260909/development-results/PAPER_SUMMARY_T4L_JCIM_ZH.md)：Bhakat T4L论文分析。
- [PRO_FORM_REVIEW_PACKET_20260910/](https://github.com/alex051107/dynamics-atlas-harness/blob/316471a135a95032f8726999e807393f55f6ceb5/review/rules-agent-study-20260909/development-results/PRO_FORM_REVIEW_PACKET_20260910/)：已有Pro形式审查包。

## 给Pro的任务

[可复制的更新prompt](PROMPT_FOR_CHATGPT_PRO_ZH.md)。Part A按本次要求中文完整梳理；Part B中文说明、英文slide标题和讲者关键句，兼顾既定英文组会交付要求。审阅者可以否定主线和组件解释，不被现有报告的结论约束。文献中找不到的内容必须标明，不补造。

## 复制、清理与未纳入内容

- 源文件留在原处。新包只收整理会议纪要、规则表、审查、分析与索引；未新增论文PDF、全文提取稿、录音、原始转写、轨迹、大数据或任何运行目录。
- 规则表原字节复制。部分Markdown为可公开定位的副本：仅改链接和本机路径，不改正文科学判断。原文身份、相对来源与改动类别见[COPY_MANIFEST.json](COPY_MANIFEST.json)。不能把路径归一化副本说成逐字节一致原件。
- 本机绝对路径改为工作区相对来源标识；能对应本包或现有仓库文件的链接改为相对或固定跨分支链接。未随包提供的全文、旧图、原始转写等链接改成“目标未纳入本包”，不伪造可访问性；详见[未纳入链接表](UNBUNDLED_LINKS.json)。
- 不读取新的盲态材料；本轮已揭盲，判定链接使用已有最终结果。新包不再复制分组密钥。仓库既有已揭盲证据归档原样保留。
- 20MB上限、凭证、本机路径、禁止目录与本包链接在提交前检查。[检查结果](PACKAGE_CHECK.json)。检查范围是本次新增审阅包；不删除历史提交中的大归档或重写分支历史。
- 分支A开始时无未提交改动；README与检查器已属于此前有意交付且通过检查的提交，本次不重复修改或重复运行其未变测试。分支B保留316471a历史，不合并、不推main，两项PR维持草稿。
