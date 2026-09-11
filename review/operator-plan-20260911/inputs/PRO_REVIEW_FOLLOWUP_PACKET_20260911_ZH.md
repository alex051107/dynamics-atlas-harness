# Dynamics Atlas：算子计划执行后的 ChatGPT Pro 跟进审查包

日期：2026-09-11  
用途：把上一批 Pro 材料与本次本地执行结果放到同一审查上下文，请 Pro 按 `PLAN_FOR_PRO_REVIEW_20260911_ZH.md` 对照审查。

## 1. 给审查者的任务

请审查附件 `PLAN_FOR_PRO_REVIEW_20260911_ZH.md`，并结合本包的当前执行结果回答计划第 5 节的 10 个问题。当前消息是对上一批 Pro 材料的跟进，不是要求重做旧审查。

对 1–10 每条给出一个且只有一个标签：

- `成立`
- `不成立`
- `证据不足`

每条附 1–3 句理由。至少指出一处必须修改的设计，并给出可以直接执行的替代写法或修改动作。能够核对的数字和引用标 `核对过`；无法从附件核对的标 `未核对`。总输出不超过 1500 个汉字。

请保留计划原有约束：不要建议扩充规则条数或换更强模型；不要把 n=4 的中位数比较当显著性检验；不要把本地运行回执、D1 表或 primary score 写成科学正确性、独立验证、泛化或正式批准。

第 5 节的 10 个判断点是：

1. 规则改写为算子前置条件/结论上限，且数值主张只能绑定算子输出，是否比文字贴进提示更能减少已观察错误，以及未防的新错。
2. 六个算子是否覆盖目标分析；OP3 的收敛判据、OP5 的半径边界、OP6 的 coverage 判定是否合理。
3. 在 40 条单向、非遍历轨迹上，用窗口占比差与轨迹 bootstrap 判“占比可信”是否可辩护。
4. F/D/O、两题、每组四次、五核心单元和双人盲评，能否区分算子增益与题目具体化效应。
5. 三行判定规则是否漏结果；“O 比 F 多一条正确且有信息内容”是否应改成可数标准。
6. 绑定检查在 8 份历史答复上抓 5/7 数值错且零误报的目标，以及第 12 行是否需要算子生成上限数组。
7. 11 条规则的保留/改写/删除送审是否足够，状态定义是否也应送审。
8. 让 F 交付 G1、让 O 相对 F/D 测 G4，是否符合原始共识。
9. 第 2 周实施量是否可行，最可能拖延的项目和应先砍掉的项目。
10. 是否有必须加入、否则会使结论无效的遗漏。

## 2. 上一批材料的状态

上一批材料是 2026-09-10 的四层 Rules 角色设计/验证实验审查包，已完整复制到本任务的 `inputs/pro_review_followup/prior_chatgpt_packet_20260910/`。其中包括：

- 上一批 Pro 提问 `00_PROMPT.md`（C1–C11、S1–S4）；
- 四层角色设计、四层验证计划、现状计划表和问题汇总；
- 博文原文与摘要；
- T4L 论文 PDF、SI PDF 与摘要。

这批文件用于恢复上下文和检查前后判断是否一致。它们不是本次算子评测的结果，也不应替代本次计划第 5 节的 10 条判断。若上一批问题在本会话中已有正式答案，请只指出它们哪些仍适用于当前结果；不要重复扩展架构。

## 3. 本次执行已经得到的本地事实

本次执行任务为 `dynamics_atlas_operator_plan_20260911`。本地 capsule 已交付；第二评分人缺失，外部 PR 未创建。当前仓库 live status 仍把下一动作限定为具名 human/domain source-science review，并禁止自动代码变更，所以没有把本地算子包转入 harness、没有推送、没有开 PR。

### 3.1 规则与算子

- 原始 33 条注册表未改；当前任务生成了 11 条 paper、33 条 source-rule、33 条 rule-index 的副本，并加了 3 条仅标记为“未经专家审”的项目规则。
- OP1–OP6 已实现并通过本任务的算子测试、固定 F 计算和一次合并 inline review；每个结果含 `result_id`、参数、输入身份和 claim boundary。
- 六行固定 HSP90 D1 的当前摘要：

| 行 | 固定结果 | 当前允许的解释 |
|---|---|---|
| D1-01 direction | closed-seeded opposite candidate：5/4/1（persistence 5/20/50 ns）；open-seeded 首持久 OPEN 20/20；无 return candidate | 有限窗口方向/反向候选；不能说平衡、速率或机制 |
| D1-02 NOE/reference | open-seeded agreement：0.5/1/2 Å 为 7/20、18/20、19/20 | 同源 crosswalk 和容差敏感性；不能说独立实验验证或动力学到达 |
| D1-03 population | 窗口差异均 <0.05，但大量 UNKNOWN；OP4 returns 0/40 | 不能把窗口稳定写成平衡 population 或 thermodynamic weight |
| D1-04 transition | 5 个 C→O persistent events，0 个 return | 事件存在；不能给 rate |
| D1-05 excursion | 42 个候选、3 个接受、1 个右删失；open/closed 半径 1.3538825899/2.6245272004 Å | 参考几何外逸和删失的描述；不能说新状态、机制或速率 |
| D1-06 coverage | closed-seeded `[ONLY_OPEN, ONLY_CLOSED, BOTH, NONE]=[0,0,0,1]`；open-seeded `[0.0001498501,0,0,0.9998501499]` | 相对于选定 NMR reference 的 coverage；不能说 MD-only 新状态 |

固定 D1 没有模型参与。独立实现复算 24 项关键计数，状态为 `PASS`、最大差异 0.0；这只是固定输入上的算术/规则一致性检查。

### 3.2 运行边界与输入

- HSP90 40,040 行、anatomy 120 行、80 个 native 文件和 NMR archive shape 通过；ADK 两张输入表为 2,253/1,678 行并通过。
- 三帧生产抽查最大差异为 `5.1411399333e-06 Å`，计划阈值为 `0.01 Å`，结果 `PASS`。
- 8 个 O-arm 的匿名 alias 全部解析到实际结果文件，绑定为 8/8 PASS、0 missing、0 unbound；历史绑定重放为 6/7 检出、0 误报，第 12 行保持 `NO_OPERATOR`。
- 首次模型 pilot 出现 token/resource limit。修复了工具读回截断、D-arm 软锁、O-arm coverage lock 和结果绑定兼容；成功 slot 没有为了好看重跑，16 个成功答复跨越了记录中的 runtime revision。这是方法学限制。

### 3.3 F/D/O 评测、费用与盲评

模型为 `openai/gpt-5.6-luna`、medium，F 为固定无模型脚本；正式 D/O 16 次完成，F 2 次完成。正式 D/O 费用 `$0.15744935`，失败 pilot/recovery `$0.03244836`，总费用 `$0.18989771`，无 `UNKNOWN_CHARGE`，低于 `$0.60` 上限。

| 题目 | F 固定参考 | D free analysis | O operator-bound |
|---|---:|---:|---:|
| HSP90_Q02 | 60/60 = 100.000% | 140/240 = 58.333% | 236/240 = 98.333% |
| ADK_Q02 | 36/36 = 100.000% | 106/144 = 73.611% | 144/144 = 100.000% |

评分来自单份 primary rubric：64 行、先封存后揭盲。第二评分人不可用，未生成 agreement 或分歧数字。HSP90 O 组有两份答复没有完整报告 persistence=20/50 的方向数值；评分保留这一缺失，没有把限制性措辞当成数值正确。

独立模型 payload 对照为 36 个结果文件，ADK 原始 TSV 复算为 24 项，均通过；它们验证数值一致性，不是独立科学验证。人工写卡、写评分依据和事后核对时间没有单独计时。

## 4. 需要你特别复核的结论边界

请把当前本地结果当作“计划实际跑完后暴露出的设计证据”，重点判断：

1. D1 的 OP3/OP4 结果是否足以支持计划对 population/transition 的结论上限，还是应把某些行改成更窄的 `evidence insufficient`。
2. F 作为固定参考的 100% 是否只是评分依据，是否会把算子 Agent 的输出设计成“追近 F”而非独立科学回答；O 比 F 多一条信息的判定是否需要重写。
3. 单一 primary scorer、第二评分缺失、成功 slot 跨 runtime revision，是否足以让本轮只能作开发诊断，不能作正式增益结论；若是，指出它影响哪些计划判定。
4. 当前没有外部 PR、没有 source-science approval，是否改变“计划完成”的措辞，而不应被本地运行证据掩盖。
5. 下一步只能给出受限审查建议，不要要求自动绕过 live gate、创建 PR、继续付费实验或修改 `main`。

## 5. 证据文件

本消息附件优先级：

1. `PLAN_FOR_PRO_REVIEW_20260911_ZH.md`：原计划和正式 10 问；
2. `PRO_REVIEW_FOLLOWUP_PACKET_20260911_ZH.md`：本跟进包；
3. `OPERATOR_PLAN_REPORT_ZH.md`：本次完整本地报告；
4. `DEVIATIONS.md`：失败、修复和未完成事项；
5. `WORK_EVIDENCE_LEDGER.json`：步骤级证据与 claim ceiling；
6. `E_CAMPAIGN_RESULT.json`、`GROUP_SCORES.json`、`SCORE_SEAL.json`、`INDEPENDENT_RECOMPUTE_MODEL.json`：运行、评分封存和数值一致性记录；
7. `prior_chatgpt_packet_20260910/`：上一批 Pro 材料原件。

如果某项数字只能从本跟进包看到而未从原始证据附件核对，请标 `未核对`。请把“本地运行通过”“评分记录完整”“Pro 审查通过”“科学结论成立”严格分开。
