from pathlib import Path
import json,csv
r=Path(__file__).resolve().parents[1];o=r/'outputs';assert(o/'UNBLINDING.json').exists()
v=json.loads((o/'FINAL_DECISIONS.json').read_text());g=json.loads((o/'GROUP_RESULTS.json').read_text());snap=json.loads((o/'CAMPAIGN_PROGRESS.json').read_text());e0=json.loads((o/'E0_COUNTS.json').read_text());flags=json.loads((o/'E2_FLAG_REVIEW.json').read_text())
case_names={'Q-D-defect':'DHFR缺陷表','Q-D-fixed':'DHFR修正表','Q-H2':'HSP90原生NOE','Q05':'Q05纳米盘','Q-A1':'ADK结构域','HSP90_Q01':'HSP90方向与参照'}
arm_names={'D':'普通资料','CARD':'准入卡','FEEDBACK':'一次反馈','P':'七条协议','R_old':'整段规则','R_scoped':'方法卡','ORIGINAL':'原题','SPLIT':'拆题'}
def group_table(exp):
 h='| 科学问题 | 条件 | n | 核心正确 /5 | 核心错误 | 过强结论 | 遗漏 /5 | 新增费用 $ |\n|---|---|---:|---:|---:|---:|---:|---:|\n'
 for x in g:
  if x['experiment']!=exp:continue
  a=x['median'];h+=f"| {case_names[x['case']]} | {arm_names[x['arm']]} | {x['n']} | {a['core_correct']:g} | {a['core_errors']:g} | {a['overclaim']:g} | {a['unnecessary_abstention']:g} | {x['cost_usd']:.5f} |\n"
 return h
lines=['# 四层验证：哪些辅助机制值得进入 Dynamics Atlas','']
for k,name in [('A','框题层'),('B','准入层'),('C','方法卡层'),('D','结论上限层')]:lines+= [f"**{k} {name}：{v[k]['label']}。** {v[k]['short']}",'']
lines+=['## 现在最重要的判断','',v['summary'],'',v['interpretation'],'','## 一、从 Rules Table 起步，到当前真正得到什么','',
'最初目标是从模拟、核磁和散射等不同来源资料得到有用、可核查、不过度的科学回答。早期整理33条候选规则，积累了分析前提与结论边界；Q05开发则暴露出关键方案仍主要由开发者安排。9月8日的项目报告与战略审查据此把科学问题和分析协议放回中心。', '',
'HSP90随后得到原生NOE与派生方向的实际对照；DHFR修正了包装坐标带来的假距离；ADK完成了完整分子距离准入和结构域描述。这些是科学资料与计算工作的成果。当前比较进一步检验：把哪些指导、检查或框题方式交给Agent，能在相同资料和工具上改变回答。', '',
'三个体系的来龙去脉、专业概念和数值见[科学读本](THREE_SYSTEMS_SCIENCE_ZH.md)。这份报告集中说明四层比较与投入决定。', '',
'## 二、历史错误怎样约束这次设计','',
f"检查了{e0['reviewed_answer_count']}份原答，其中{e0['unique_original_answers']}份出现了本次记录的问题；保留{e0['rows']}条相关观察、{e0['same_cause_groups']}个原因组。行数不是独立样本数，也不是Rules可以防住的错误数。最初表中一条证据不足的归因已经撤回，原稿和更正原因都保留。",'',
'| 编号 | 实际观察 | 原因组 | 当前结论检查回放 |','|---|---|---|---|']
for x in csv.DictReader((o/'E0_RETROSPECTIVE_AUDIT.csv').open()):
 clean=lambda s:s.replace('|','／').replace('\n',' ')
 lines.append(f"| {x['id']} | {clean(x['error'])} | {x.get('same_cause_group','')} | {x.get('ceiling_replay_detected_this_error','')} |")
lines+=['', '**最有信息量的零费用结果是：当前结论检查器在历史8份原答的回放中，未检出7处目标核心数值错误，唯一一条提示是误报。** 正确单位Å⁻¹的指数−1被当作未匹配数字。另一个错误计算已经出现在工具日志中，所以可以通过“数字出现过”检查。原先3条“已回放检出”指两份DHFR输入检查和一份交付问题回放，不是这次结论检查器检出。', '',
'原答定位、具体引文和不同回放的范围见[E0审计表](E0_RETROSPECTIVE_AUDIT.csv)与[回放审查](E0_CEILING_REPLAY_REVIEW_ZH.md)。', '',
'## 三、共同实验条件与评分边界','',
f"本轮计划72次四层对照，加2次ADK普通答复。实际完成{sum(x['completed_attempts']for x in snap['experiments'])}次尝试，保存{sum(x['accepted_answers']for x in snap['experiments'])}份合法答复。所有条件使用Luna medium、同一冻结容器与成熟工具，每题每条件4次，顺序预先随机化。ADK普通答复单列，不并入四次一组的效果比较。",'',
'普通组已经获得整理好的来源说明与派生表。当前测的是辅助组件在这一基线上的变化，不包括从原始论文自动发现问题、自动修理坏坐标和自动构建工具的总体能力。HSP90、DHFR和Q05已暴露；ADK仅一个新来源。', '',
'全部运行结束后统一隐藏条件，按五个冻结核心单元逐份评分；随后封存评分，再揭盲。以下正确、错误、过强结论与遗漏均为每题四次的中位数，原始分数全部保留。遗漏不等同于明确说错；不必要弃权沿原计划操作定义包括可回答内容未覆盖。E2首次与最终提交另作对照。', '',
'当前评分者也参与建包，条件标签隐藏但不等于独立领域专家双盲。Claude核对了材料与设计，未替代这批答复的独立专家评分。详细过程、TOKEN_LIMIT处理和冻结后意见处置见[方法与局限](METHODS_AND_LIMITS_ZH.md)。', '',
'## 四、B准入层：自动核对与可信参照的贡献分开','',v['B']['reason'],'',
'纯代码检查检出6/6植入缺陷，3个干净包零误报。实际能力包括元数据与受信声明比对、行数和时间检查、矩阵与参照比对，以及读取上游物理检查结果。七个名称并不等于七种完整科学检查。三个干净包与参照完全相同，零误报是较弱的自一致性控制。', '',
'①包装坐标、②单位、⑤条件标签和⑥证据角色依赖数值或来源参照；③缺行也需要可信预期行数。④的时间单调可从表内检查，但对齐仍需参照。ADK全帧GROMACS核对提供独立数值证据，却不是另一份独立生成表上的误报试验。覆盖与容差见[E1a能力审计](E1A_CHECK_COVERAGE_AUDIT.json)。', '',group_table('E1b'), '',
'## 五、D结论层：一次反馈实际改好了什么','',v['D']['reason'],'',group_table('E2'), '',
v['D']['detail'],'',
'E2三题均没有PUBLIC_FACTS输入，证据角色分支未实际被测。数字出现、宽泛否定词和全文出现时间单位，都不能单独保证某一科学主张的来源、上限或统计解释正确。已运行后的意见没有用于回改检查器再测同题。实际提示及独立语义判断见[E2提示逐条审查](E2_FLAG_REVIEW.json)，首次/终稿分数见[修订比较](E2_REVISION_COMPARISON.json)。', '',
'## 六、C方法卡层：检索命中能否带来科学收益','',v['C']['reason'],'',group_table('E3'),'',
v['C']['detail'],'',
'HSP90按NMR方法族只取到1张BME重加权卡，Q05取到4张，DHFR和ADK的MD内部分析取到0张。HSP90当前NOE违例对照无需重新拟合权重。Q05因SAXS匹配还取到了针对平均FRET与聚合物分布的卡。实验方法相同，不代表当前操作相同。', '',
'冻结的主判据只统计肯定采用R0、dye、AV、RMP作为本题必要条件，否定或忠实介绍来源不计入。审查后提出的BME等词不追加入主判据；若有不当迁移，在[逐句探索性分析](E3_EXPLORATORY_REVIEW_ZH.md)单列。更完整的设计解释见[方法卡适用性分析](METHOD_CARD_DESIGN_ANALYSIS_ZH.md)。', '',
'## 七、A框题层：明确需求后多回答了什么','',v['A']['reason'],'',group_table('E4'),'',v['A']['detail'],'',
'E4最终冻结按两道题的子问题覆盖改善判断，不按计划概览中的泛写三题。两版共用评分依据；拆题版要求更多内容，因此这是框题包的效果。正确覆盖更多要求值得记录，但不能据此宣称Agent自主发现问题的能力提高。', '',
'## 八、ADK普通答复与三个科学结果怎样交付','',group_table('ADK_plain'),'',
'ADK的独立复算支持：开态起始NMP–CORE首末变化+0.071 Å、LID–CORE +2.290 Å；闭态起始分别+1.091与+1.176 Å。全帧指定原子对与GROMACS差约0.005 Å；域间描述量由SciPy独立实现复算，差小于1e−10 Å。两个首末窗口都没有共同闭合，分布仍重叠。', '',
'这些来自项目预定的完整分子Cα距离，不是作者前向散射复现。沉积结构无ATP/AMP；实验为光释放ATP加AMP，温度和时钟不同。两份普通Agent到底做对哪些内容、与原文逐句是什么关系，见[ADK原答与论文关系](ADK_PAPER_RELATIONSHIPS.md)。', '',
'HSP90的10/20曾出现开放方向与原生NOE下9条仅相对趋开并不矛盾；DHFR的修正局部距离是开发者计算，旧原答未发现输入缺陷。这些边界在[三个体系科学读本](THREE_SYSTEMS_SCIENCE_ZH.md)保留。', '',
'## 九、费用、时间与完整性','',
'| 批次 | 实际尝试 / 计划 | 合法答复 | 费用 $ | 上限 $ |','|---|---:|---:|---:|---:|']
for x in snap['experiments']:lines.append(f"| {x['experiment']} | {x['completed_attempts']}/{x['planned']} | {x['accepted_answers']} | {x['settled_cost_usd']:.8f} | {x['cap_usd']:.2f} |")
lines+=['',f"新增合计 **${snap['total_settled_new_cost_usd']:.8f}**，总上限$1.85。对账的历史四批16份答复共$0.28550861另列；它不是项目全部历史消费。ADK两份只在本轮ADK_plain记一次。没有以模型墙钟时间代替人工纠错时间，25%人工节省未测。",'',
v['execution_note'],'',
'## 十、下一步的投入决定','',v['next_action'],'',
'不扩大33条注册表，不用同题修订后的重跑冲掉本轮失败，也不以本次小样本推算总体正确率。科学工作继续按具体问题、成熟方法、逐项证据和有限结论推进。组件若需要修正，只能作为明确的新版本，在新的问题与预先确定的判据下检验。', '',
'## 复核入口','',
'- [一页结论](ROUND_BRIEF_ZH.md) · [完整三体系读本](THREE_SYSTEMS_SCIENCE_ZH.md) · [12页组会材料](COLLABORATOR_REPORT.pptx)',
'- [逐份原始分数与条件](UNBLINDED_SCORES.csv) · [工作证据账本](WORK_EVIDENCE_LEDGER.json) · [偏离说明](DEVIATIONS.md)',
'- [如何查看原答和冻结输入](REPLAY_GUIDE_ZH.md) · [来源对应表](claim_source_map.jsonl) · [最终审查记录](review_report.md)',
'- [PR #27](https://github.com/alex051107/dynamics-atlas-harness/pull/27)，保留原答、首次提交、工具输出、运行回执与费用。未合并。','']
(o/'FOUR_LAYER_VALIDATION_REPORT_ZH.md').write_text('\n'.join(lines))
brief=['# Dynamics Atlas：本轮投入判断','',f"**{v['summary']}**",'']
for k,name in [('A','框题'),('B','准入'),('C','方法卡'),('D','结论反馈')]:brief += [f"- **{name}：{v[k]['label']}。** {v[k]['short']}"]
brief+=['','三项科学结果：HSP90的方向变化不等于接近开态；DHFR修正周期表示后两种抑制剂的局部距离不同；ADK两条轨迹的首末窗口未显示共同闭合。它们是资料核对和计算得到的结果，与辅助组件的增量分开。','',v['next_action'],'',f"本轮完成{sum(x['completed_attempts']for x in snap['experiments'])}次尝试，费用${snap['total_settled_new_cost_usd']:.4f}。每题每组四次，主要是暴露开发材料，只有一个新ADK来源；不报告总体正确率或人工时间节省。",'', '[完整报告与逐题证据](FOUR_LAYER_VALIDATION_REPORT_ZH.md) · [三体系读本](THREE_SYSTEMS_SCIENCE_ZH.md) · [组会材料](COLLABORATOR_REPORT.pptx)']
(o/'ROUND_BRIEF_ZH.md').write_text('\n'.join(brief));(o/'RULES_TABLE_VERDICT_ZH.md').write_text('\n'.join(brief));print('Report and one-page decision written from sealed results')
