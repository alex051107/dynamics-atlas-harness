# 当前计算入口与 Operator 接通范围

核对日期：2026-09-04。范围：当前 harness 工作树的代码、注册表和已有执行记录；本轮未执行计算、测试、运行时探测或模型调用。此清单用于筛选论文结果复现问题。

**当前注册表只有一个可路由的科学计算 Operator，而且严格绑定既有 HSP90 数据包。另有 X-EISD 精确字段查找，以及 HSP90、ADK 两个能执行描述性计算的固定案例入口。它们尚不能构成面向新论文、新数据的一般计算路线。** 这说明新一轮实验需要逐题列明接入缺口，不能由缺少代码直接断定 Rules Table 的科学判断不可行。

## 1. 接通状态

| 入口 | 当前状态 | 实际输入与计算 | 当前可用范围 |
| --- | --- | --- | --- |
| HSP90 时间方向诊断 `hsp90.directional_time_anatomy.v1_case_bound` | `ROSTER_PASS`、`routable=true`；有已成功执行及输出检查记录 | 固定两份 TSV：逐帧状态赋值和路线预测；40 条轨迹、20–1020 ns、1 ns 保存间隔、每条1001帧；固定5/20/50保存帧持续长度。生成方向连续段、逐轨迹时间诊断、50帧时间箱和汇总。 | 仅原案例、原来源、原方法配置及一项 F04R02 时间诊断要求；支持同一数据包的描述性诊断。不能将新轨迹替换进去后声称仍属当前路线。 |
| HSP90 旧版 `hsp90.directional_time_anatomy.v0` | `CANARY_PASS`、`routable=false` | 调用上游既有分析脚本和两份固定 TSV，持续长度同上。 | 保留的 canary 适配器；注册表仍记录输出校验和案例/输入绑定未完整。不是第二个一般可路由 Operator。 |
| X-EISD 精确来源查找 | 案例内 `SOURCE_LOOKUP` 已接通；不是注册的数值科学计算 Operator | 对本地固定 review derivative 校验身份及 locator，返回预先声明的字段更新。三个白名单条目涉及 candidate pool、J-coupling 来源和二者关系。 | 只补现有 X-EISD 案例的声明字段。没有运行 X-EISD 优化/评分、Karplus 前向计算或 ensemble 重加权。 |
| HSP90 单一观测量相关性描述 | 固定 action card，可执行；`NO_ACTIVE_RULE_EFFECT` | 40×1021 的 CA46–CA60 距离矩阵及轨迹/组别 manifest；逐轨迹调用 PyMBAR statistical inefficiency，给出有效样本量及组内/组间描述。 | 特定观测量和给定窗口的描述；不是 Operator 注册项，不改变有效 Rule 结果，不判定全局平衡。 |
| ADK 静态参考相似度描述 | 固定 action card，可执行；有已有结果；`NO_ACTIVE_RULE_EFFECT` | 1E4V G10V chain A 的214个 Cα坐标，相对1AKE和4AKE参考；SciPy刚体对齐，比较全链RMSD。 | 单个静态结构对两个参考的几何相似度；不是动态状态、活性、动力学或突变效应的计算。 |
| MDAnalysis 轨迹结构投影 `trajectory.structural_state_projection.v1` | `REGISTERED_BLOCKED`、`routable=false`，spec-only | 设计输入为topology、trajectory、reference states、mapping和method profile；新案例的metric及alignment selection未冻结。 | 当前不能路由执行。注册表记载历史探测中运行时不可用，以及输入、方法配置、映射和指标未冻结；本轮未重新探测包是否安装。 |
| 旧 JSON pointer lookup | `SOFTWARE_CANARY_PASS`，但registry明确 `LEGACY_FIXTURE_ONLY` / `case_routing_allowed=false` | 在允许的本地JSON中读取指定pointer，拒绝越界路径及答案字段。 | 仅合成fixture命令；不能算作真实论文的一般检索或计算入口。 |

状态与范围来源：[科学 Operator 注册表](../../config/registered_operators.json#L6)（旧HSP90第6行、可路由HSP90第58行、MDAnalysis第120行）；[旧fixture注册表](../../config/operators.json#L2)；[固定案例action cards](../../src/dynamics_atlas_harness/exposed_paper_blind_capsule_v1.py#L72)。

## 2. 关键边界与执行证据

HSP90的路由要求当前规则结果确实是指定的未解决项，随后检查精确case、source、method profile和manifest；泛化的RunPlan匹配器同样只接受 `ROSTER_PASS` 且可路由的条目。它不是“任何MD缺口都交给HSP90脚本”。[精确路由逻辑](../../src/dynamics_atlas_harness/real_case_vertical_slice_v1.py#L1203)、[RunPlan匹配条件](../../src/dynamics_atlas_harness/runplan.py#L41)。

既有HSP90执行记录为 `SUCCEEDED`，输出检查为 `PASS`；输入时序和数量由固定manifest约束。它证明原数据和原合同的执行路径已跑通，科学判断仍待审核。输出不得升级为转移速率、平衡布居、自由能、完整路径、机制或突变效应。[输入manifest](../../evidence/real_case_vertical_slice_v1/hsp90_operator_input_manifest_v1.json#L34)、[已有执行记录](../../evidence/real_case_vertical_slice_v1/outputs/hsp90_b1_rule_to_operator/operator_run_receipt.json#L50)、[结论范围](../../config/registered_operators.json#L110)。

X-EISD查找读取的更新值已在allowlist中声明；函数不从论文文本推导科学量。其J-coupling条目还明确不验证Karplus模型。它可作为元数据准备步骤，不能计为复算论文的J-coupling或X-EISD结果。[查找实现](../../src/dynamics_atlas_harness/real_case_vertical_slice_v1.py#L197)、[allowlist](../../evidence/real_case_vertical_slice_v1/xeisd_source_lookup_allowlist_v1.json#L23)。

HSP90的PyMBAR入口显式标为非Rule evaluator、非Operator、非平衡检测器；ADK函数只输出静态参考相似度。ADK已有结果记录了SciPy版本、两个对齐RMSD和 `NO_ACTIVE_RULE_EFFECT`。这两条可作为新实验中待复用的计算组件；新问题仍需明确输入、适用条件和结果如何进入科学判断。[HSP90相关性函数](../../src/dynamics_atlas_harness/sampling_diagnostics_v1.py#L1)、[返回结果范围](../../src/dynamics_atlas_harness/sampling_diagnostics_v1.py#L173)、[ADK计算与输入限制](../../src/dynamics_atlas_harness/structural_state_projection_v1.py#L64)、[ADK已有结果](../../evidence/live_agent_common_flows_v1/development_runs/authorized_campaign_live_20260830/recorded_replay/adk/actions/ADK_STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION_V1/evidence_result.json#L676)。

已有八场景验收把T7列为注册Operator执行，把T8列为不受有效Rule控制的描述性计算；两者都不是论文结果复现验收。[验收范围](../../research/rules_prototype_acceptance_v1/REPORT.md#L13)。

## 3. 对20题筛选的约束

当前两个Operator注册表中没有注册可运行的SAXS散射前向计算、FRET效率/距离转换、NMR PRE/NOE/J-coupling前向计算、X-EISD评分/优化、ensemble拟合或重加权路线。此结论只针对这里实际检查的注册表与执行分派，不表示电脑或其他研究项目里不存在有关代码。安装某个科学包、出现论文方法名或拥有旧脚本，均不等于已接入Operator。

候选题的计算路线应分别标明：**原案例精确路线可用**、**既有描述性组件可复用但新题未接通**、或**所需科学计算未接入**。在新题中遇到后两种情况，先记录数据/计算接入缺口；拿到计算结果后，才能检验Rules是否能据证据作出恰当判断。不可把尚未接入工具的失败计为Rules科学判据失败。

## 4. 本轮检查记录

本子任务仅进行了源文件和已有JSON记录的定向阅读，并生成本清单；没有执行任何科学函数、测试、build、模型调用或hash计算。记录中的 `SUCCEEDED` / `PASS` 均为已有文件记载，本轮未重跑。筛选交付已完成一次合并检查与审阅；本次 PR 仅检查可移植链接、字段一致性和发布范围。
