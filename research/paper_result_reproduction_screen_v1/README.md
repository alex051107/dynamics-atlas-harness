# Paper-result reproduction screen v1

Screened on 2026-09-04 against the post-PR24 implementation at `914bc00816c7fe9222bd960a4eda56cd01e8a5c6`. The initial report and JSON/CSV preserve the screening snapshot: 20 questions from 10 primary papers, all `NOT_RUN` at initial submission. Later review, Q05 numerical work and an actual Rules probe are recorded below.

The goal is to test whether paper data, frozen Rules, connected Operators and justified additional calculations can produce a bounded scientific conclusion comparable to a paper result. The initial screen found zero complete registered routes for these new questions; this is an integration gap, not twenty scientific failures.

## Read this packet

- [Revised Master Plan, section 0A](../../docs/MASTER_PLAN_ZH.md#0a-用论文数据检验-rules-table-与-operator): current goal, execution sequence and comparison logic. Dated later sections preserve historical milestones.
- [Twenty questions and selection reasons](REPORT_ZH.md): paper targets, figure/section locators, inputs, calculations, comparison and data limitations.
- [JSON roster](questions_20.json) and [CSV roster](questions_20.csv): machine-readable screening proposals.
- [Actual Operator scope](OPERATOR_READINESS.md): code and existing-receipt references; no new runtime probe.
- [Pro review prompt](PRO_REVIEW_PROMPT_ZH.md): request an actionable first pilot and challenge the design.

## Current pilot order

Initial reviewed priority: Q05 nanodisc → Q01 HSP90 → Q09 T4 lysozyme; Q15 HiSiaP is the next candidate. While Q05 trajectory/reader resource authorization is pending, Q09 small-input and method work proceeds under the existing loop authorization. This supersedes the initial Q09/Q01/Q05 order. These are data-inspection priorities, not three immediately runnable registered routes. A 2.9 MB archive does not establish fitting simplicity.

The roster contains 17 protein/protein-lipid questions, 2 DNA measurement controls and 1 paper-simulated negative control. Q09/Q10/Q11 share T4L data. These exposed development questions are not a held-out evaluation or twenty independent systems.

## Current follow-up

[Current Q05 code and execution evidence](q05_review_evidence/README.md) provides the actual intake probe, full rule outputs, previous entry failures, local numerical source and fixed-method comparisons for independent review. The [earlier Pro follow-up](PRO_REVIEW_FOLLOWUP_ZH.md) remains a historical record at7381608. No complete scientific reproduction or Rules-controlled numerical gain is claimed. The final objective is high-correctness answers and content coverage across all20 questions; reviewer scope and response length are unrestricted.

## Initial delivery validation (historical)

The screening received a combined count/source/state check and one independent delivery review. PR packaging uses one focused check for 20 unique IDs, unchanged JSON/CSV records, `NOT_RUN` status, portable links, absence of personal absolute paths in added content, expected changed files and whitespace. No scientific calculations, runtime tests, builds or data hashes are needed for this documentation-only change.

No raw paper PDFs, author prediction matrices, canonical Rules changes or new registered Operators are included; generated numerical review results and authored source are now included. A Pro review is advice; it does not establish a scientific result or authorize merging.

## Round4: confirmed semantics repairs

[Q05 R1 actual results and remaining scientific work](q05_semantic_repair_r1/README.md):7 declaration PASS,8 UNRESOLVED,2 NOT_APPLICABLE; no scientific numerical obligation. Original R0 evidence remains preserved. The continuing objective is full scientific correctness and coverage across the original20 questions.

## 第四轮修复与固定权重审计

见 [第四轮修复](PRO_ROUND4_REPAIR_ZH.md) 和 [作者权重回算](q05_author_weight_audit_v1/REPORT_ZH.md)。当前科学完整回答仍为 0/20；声明测试通过不计科学正确率。

## 第一项共同权重数值规则

[实际运行与同实例重评](q05_joint_numeric_v1/REPORT_ZH.md)：新增 CASE 规则触发一次主计算，三通道损失下降，数值最优性通过；绝对相容性与完整Q05仍未决。

## 第六轮接口修复与证据复算

[Q05 v2](q05_joint_numeric_v2/REPORT_ZH.md)核验作者来源、重算数值证据并绑定实际请求；九项针对性测试与247项本地完整回归通过。结果数值与v1相同，完整科学答案未增加。

## Q09原始衰减与方法核对；Q05形状准备

[Q09实际输入](q09_decay_admission_v1/REPORT_ZH.md)已解析33组181份数值文件；[方法与显式映射](q09_method_admission_v1/REPORT_ZH.md)记录原SI公式的无FRET极限冲突、w=12Å对应sigma=6Å、重复参考及混合仪器条件。[Q05形状准备](q05_shape_preparation_v1/REPORT_ZH.md)包含真实原子清单与六项合成检查，真实轨迹0帧。这些新增准备没有改变完整科学答案0/20，也没有增加Rules运行数。

## 首个实际Q09 DA/D0联合拟合批次

[22–127 PQ联合拟合](q09_pq_joint_v3/REPORT_ZH.md)在独立IRF和共享donor寿命下，同时拟合真实DA/D0，单列DA内部donor-only比例。四组预定初值经数值缩放修复后通过梯度检查；原失败与重跑均保留。[先行IBH donor-only诊断](q09_donor_calibration_v2/REPORT_ZH.md)随批提供。它们是条件开发计算，尚无K3/33组全局比较、Q09 Rules触发或完整科学答案。

## Q09规则控制的donor与仪器诊断

[新方法诊断义务](q09_forward_adequacy_v1/REPORT_ZH.md)已实际派发并同实例重评。原Rules基线17个实例没有数值义务；新Q09窄规则触发三寿命donor校准、保持FRET两成分的联合重算及有限f0轮廓。联合deviance从18923.6172降到13880.0482，距离和donor-only系数随donor模型明显变化。IRF首尾中位数0但均有非零计数；校准误差尚未传播，态数仍未决。关闭规则不派发该补查，完整正确人工流程若得出相同结论不计Rules增益。

[共享IBH参考组](q09_shared_ibh_v1/REPORT_ZH.md)保留两DA/一D0及四次拟合，一个初值落入更差边界解，未宣称所有初值一致。新的[零优化回放](q09_forward_adequacy_v1/REPLAY.md)直接从原始数据和保存参数重算证据，不必重新制造历史失败。完整科学回答仍0/20。
