# 流程要求 → 工具与证据清单

2026-09-26 静态核对。案例线源码位于 `<repo>/src/dynamics_atlas_harness/nmr_agent/`，只读，未改引擎。存在函数不等于已在 RfaH 上验证。本表区分已暴露接口、需组合现有方法和未提供能力；不是一份要求全部开发完成的清单。

| 流程要求 | 已有工具或实现 | 当前实际能力与 RfaH 用法 |
|---|---|---|
| F1/I1 输入与条件、全量覆盖 | `inventory`, `read_text`, `screen_dispersion`, `show_profile` | 已有工作区读取接口；RfaH 工作区未交。CEST 残差筛选是启发式，不是状态数/显著性检验。需从全部原始输入追踪排除；不能默认作者已筛的 47 条等于全部可用曲线 |
| I2 编号、物种、构建体、探针一致性 | `python`、序列/位移输入；现成序列比对/PDB 解析 | 现有工具主要围绕 15N 酰胺；不直接适用于 IL-2 的 13C 甲基。RfaH 峰组编号必须按采集/归属证据映射；编号加常数不证明它来自另一个样品或构建体 |
| B1 可用基线和优化诊断 | `fit_exchange`, `cest_sign_scan`, `bootstrap_global` | 已暴露二态、三态 star/linear、两态分组；无四/五态接口。bootstrap 为残基重抽样，不替代实验噪声重抽样或模型辨识性。不能要求 Agent 从这个接口识别五态 |
| B2 冻结参数跨实验预测 | `python` 可调用 `exchange.cpmg_r2eff_model` / `cest_model`；`multistate` 也有前向函数；ChemEx 有现成模拟 | **没有专门的预测工具，但未必需要新增工具**：可通过已有 Python 调用前向函数。`fit_exchange(fix=...)` 只固定部分参数，仍会重拟合位移/弛豫，不是完整冻结预测。必须保存 source_fit、冻结的物理参数、目标实验、检测态、预测/实测/误差/残差；若目标需单独校准基线等干扰参数，预先说明并计入自由度，不能称完全外部预测 |
| B2 RfaH 两组可观测峰 | 本地 `cpmg_r2eff_n` 返回 `[:,0]`；`cest_n` 返回 `[:,2]/p[0]`，二态函数也检测第一个状态 | 接口没有 `observed_state`。简单重命名可能在部分前向计算成立，但当前拟合布居上限、Δω 符号和多态全局约束都需相应处理，不能宣称等价已证。必须由适用后端支持两组读数；不能把同一样品两组峰误作独立变体各自推出两份不一致动力学 |
| D2 更复杂过程、可辨识性 | 优先 ChemEx 已有模型/约束/多状态检测 | [官方仓库](https://github.com/gbouvignies/ChemEx)及[发布记录](https://github.com/gbouvignies/ChemEx/releases)列有五/六态与多状态检测；[模型说明](https://gbouvignies.github.io/ChemEx/docs/user_guide/fitting/kinetic_models/)列常用模型。现成能力不等于本机 MCP 已开放或当前版本已通过 RfaH 正控。不再写新物理引擎；若首轮工具仍限制三态，预登记结论上限并把缺口单独归因 |
| D3 对照、扰动、占有率 | 通用数据工具及 `python`，复用单位点结合等既有方程 | 依赖实测对照/浓度/Kd；缺数据则建议实验。AdK 温度系列、IL-2/RfaH 2012 扰动谱的文献描述不算执行输入 |
| D4 稳健性、全量高信号覆盖 | 筛选、初值扫描、现有拟合和 Python | 支持部分检查；拟合输出为摘要，不能假装包含完整模型预测、全部干扰参数与完整精度。RfaH 需要确保参数可由观察回读，才可真实复算前向预测 |
| T1 多参照、逐区比较 | `reference_shifts`, `compare_references`，POTENCI | 接口已有 15N、共同交集和 regions；RfaH 实测两组可见态/其他核位移需要保留其原始观测身份。碳位移/二级结构指数可用已有工具或 Python，不能把当前 15N 比较器称全套实现 |
| T2 几何与参照可信度 | `pdb_ligand_distances`、现成 PDB 解析/序列对齐/DSSP | 当前工具只列配体/最近原子距离；不是结构对齐、NOE 指派、电子密度或配体验证服务。需要更深结构证据时用现成实现，缺数据则缩小结论 |
| S1 原始观察、研究状态、报告、候选 | `read_result`, `get_research_state`, `update_research_state`, `propose_experiment`, `finish` | 保留案例合同，不要求删除这些接口，不写 claims 双向转换。`finish` 原生 Atlas 候选即可给 Gina；字段有效不是证据等级通过 |
| C 显式反思 | `reflect` 与现有 C 组 MCP 闸门 | 保留原字段和归档。闸门机制含周期触发，不能在报告中改称纯差异触发；首次运行不偷偷改频率。所有闸门阻断调用算成本/开销 |

## 首条 RfaH C 运行前实际未交付的内容

检查位置：`<local-work>/` 与案例任务 `outputs/rfah/`。

- 只找到 `rfah_raw_sealed/`、`rfah_pc/`，没有 `rfah_ws_v1/`；不得使用封存原始作者目录或带 `author_init.toml` 的正控目录作为盲解题输入。
- 未找到 `POSITIVE_CONTROL_ZH.md`、`PREREG_RFAH_R1_ZH.md` 或 RfaH 泄露审计。用户报告正控在运行，但本轮未查询/中止/重开 Longleaf 作业，也不能把某时刻 χ² 当最终完成。
- `python3` 已有 `langchain_anthropic`、`langchain_openai`、`anthropic`、`openai`、`mcp`；该 Python 没有 ChemEx。检查环境变量只查存在性，三类 API key 均未设置，没有读取或输出任何密钥。现有 Claude 订阅 CLI 入口在案例运行器里，不能据此假设 LangChain 能使用订阅认证。

这三个方面是输入、科学能力与模型通道的真实依赖。先交五篇流程，不用更多回放或持久化代码绕过它们。真实运行将使用新标识，并单独记录哪些能力已交；未交能力不计 Agent 推理失败。
