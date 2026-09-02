# F03 暴露式开发校准 v1：Fuertes 2017 SAXS / smFRET

## 校准结论

`KEEP_CURRENT_F03_PATTERN`。

Fuertes 等人（2017）的这一个暴露式来源对表明，现有 F03 所要求的六项来源语义字段足以保留两类测量之间最关键的区分：SAXS 的原始对象是 `I(q)` 对 `q` 的散射曲线，`R_G` 由曲线经分析得到；smFRET 的原始对象是 `E_FRET`，文中的 `R_E,L` 由平均效率、距离分布模型和染料对参数推得。现有模式可将原始观测量、报告量、空间支持和聚合语义写成不同字段，F03 的既有 claim ceiling 也把本地 PASS 限定为“来源测量语义已声明”。本轮不修改任何 canonical Rule、binding、contract、policy 或来源证据包。

H1 保持 `PENDING`。这份校准不构成来源科学裁决、跨来源可比性、方法可靠性、验证结论或科学 SUPPORT。

## 范围、输入与冻结顺序

本轮由 `DA-20260901-059` 授权，分支基线为 `da584173ee64bfad9854132a3418ed1e871c69f5`。唯一主来源是 Fuertes et al., *PNAS* 2017, DOI `10.1073/pnas.1704692114`；本地原始 PDF 的 SHA-256 为 `a602b61013478d3f27b725a37f4a13ad1427b8e661b44b84063b4ee672c791d8`。使用的是主文，未读取 Supporting Information。

| 阶段 | 可见输入 | 产物与状态 |
| --- | --- | --- |
| Pass A：来源优先 | 原始 PDF、由该 PDF 生成的文本导出、一个中性的提取 schema；没有当前 F03 Rule ID、binding、contract 或 PASS 预期 | `source_first_record.json` 已先冻结，SHA-256 为 `d5fa872c3f8a847ff8bd662c41aa4c00b7a4d2f9c8fe7a89ebc2551ffdf0e595`。隔离标签为 `SOURCE_FIRST_PROCEDURALLY_SEPARATED_NOT_INDEPENDENT`。 |
| Pass B：冻结模式投影 | Pass A 冻结件及 F03R01、B-F03R01、EC-F03R01、RP F02/F03 和 `SEP-F03-MEASUREMENT` 的冻结副本 | 这是 task-local 的预期契约投影，不是新的 Rule runtime 执行。 |

Pass A 的来源定位包括：PDF p. 1 / PNAS E6342（摘要和引言），p. 2 / E6343（Figure 1 与相邻引言），p. 3 / E6344（Figure 2、Eqs. 1–2），E6348（讨论）和 Methods。完整 locator 与原子陈述在 `source_first_record.json`。

## Pass A 读到的测量语义

| 来源对象 | 主文直接呈现的原始对象 | 主文报告或推得的量 | 来源支持的变换与边界 |
| --- | --- | --- | --- |
| SAXS | `I(q)` 对 `q` 的散射曲线 | `R_G,U` / `R_G,L` 及由完整曲线得到的尺寸或形状信息 | `R_G` 通过 Guinier 关系或 `P(r)` 从曲线计算；散射强度是分子和构象的加权平均，空间支持是全局链尺度。见 `FUE-P02-FIG1-INTRO`、`FUE-P03-FIG2-EQ1-EQ2`。 |
| smFRET | 双标记蛋白的 burst-wise `E_FRET` 及其均值 | `R_E,L`，即染料间的推断距离代理 | 均值 `E_FRET` 通过 `P(r_D,A; R_E,L)` 与染料对 `R_0` 映射；`P` 的形式需事先选择，柔性 linker 使 `R_E,L` 与实际 `R_E,U` 有别。空间支持是特定末端 donor–acceptor 对。见 `FUE-P01-INTRO`、`FUE-P03-FIG2-EQ1-EQ2`、`FUE-P10-METHODS`。 |

论文还描述了两种测量不同的浓度和平均方式。它把 SAXS 讨论为全局距离分布的积分信息，把 smFRET 讨论为一个端到端染料距离的差分平均；该讨论支持在解释前保留测量语义的差异，未给出可迁移的跨模态换算规则。见 `FUE-P07-DISCUSSION`。

## Pass B：冻结 F03 投影

下表逐项记录 F03 的六个 required field。`主文支持` 表示定位到论文内容；`项目标注` 表示 controlled vocabulary 或声明状态由项目记录承担，不能伪装成作者原文中的字段。

| F03 required field | SAXS 投影 | smFRET 投影 | 主文支持与项目标注 |
| --- | --- | --- | --- |
| `source.native_observable` | `I(q)` 对 `q` | burst-wise / mean `E_FRET` | 两者均由主文直接支持。 |
| `source.estimand` | `R_G,U` / `R_G,L` 和 profile-derived 尺寸或形状量 | 以模型推得、且区别于 `R_E,U` 的 `R_E,L` | 两者有主文支撑；该字段需要 typed project annotation 以保留“原始对象 → 分析或模型 → 报告量”。 |
| `source.time_semantics.kind` | 构象/分子集合平均，非动力学速率测量 | 文中有 ns–ms 运动敏感性与均值效率/分布语义，未定义单一动力学 rate estimand | 主文支持语义；controlled vocabulary 标签需要项目标注。 |
| `source.spatial_support` | 全局分子或链尺度 | 特定标记末端的 donor–acceptor 距离 | 两者均由主文表示。 |
| `source.unit_or_aggregation` | q-indexed profile 与分子/构象加权平均；精确单位在本记录中不完整 | burst-wise efficiency distribution 的均值，再经分布模型映射 | 主文支持聚合语义；本记录不臆造 SI 级数值校准。 |
| `source.native_measurement_declaration_status` | 无作者提供的 status label | 无作者提供的 status label | 必须由项目完成 typed declaration 后标为 `DECLARED`；F03 evaluator 不核验该标注是否忠实于段落。 |

在完整 typed declaration 下，两个来源对象都预期得到本地 `PASS`，路径为 `DIRECT_EVALUATION`，理由为 `SOURCE_NATIVE_MEASUREMENT_DECLARED`。删除任一关键语义项的情景应为 `UNRESOLVED`，路径为 `SOURCE_LOOKUP`；当前 policy 在本 Draft 中没有 lookup executor。这个 PASS 的 ceiling 仅为“来源记录声明了来源原生测量语义”。

F03 evaluator 不独立建立以下事实：项目标注是否逐段忠实于论文、SAXS 的可靠性或不确定性、染料模型或 `R_0` 是否正确、两个来源是否可比、是否代表同一 ensemble、是否已验证，或任何 H1 科学结论。

## 主要差异与处置

| 类型 | 观察到的差异 | 结论 |
| --- | --- | --- |
| `ANNOTATION_TRUTH_NOT_ESTABLISHED` | 主论文没有 `native_measurement_declaration_status` 字段。完整状态由项目标注提供，而 F03 contract 用 `DECLARED` 决定本地 PASS。 | 这是标注真实性的人工来源审阅边界。没有观察到一次实际的 unsafe false PASS；一旦标注错误，局部 PASS 仍可能错误地表示“声明完整”。F03 自身的 ceiling 阻止它升级为科学判断。 |
| `NO_PATTERN_DEFECT` | 本来源对可分别填写原始对象、报告量、时间或集合语义、空间支持和聚合方式。 | 当前六字段对这一对 SAXS / smFRET 对象足够，保留现有模式。 |
| `DATA_INSUFFICIENT` | 一个暴露式来源对无法判断每一种经模型变换的报告量都需要独立的 canonical transformation field。 | 不能据此新增字段或收紧 Rule。下一批冻结案例再检验该问题。 |

## 修复选项

1. `KEEP_CURRENT_F03_PATTERN`（推荐，处置 `KEEP`）：维持当前 canonical 模式。本类来源记录的 `estimand` 标注应明确写出“原始对象 → 分析或模型假设 → 报告量”，并保留文献 locator。该写法属于本校准的使用准则，没有实现改动。

2. `DEFER`（处置 `DEFER`）：待三个冻结来源单位重复出现“原始对象和变换后报告量无法稳定区分”的证据后，再决定是否需要来源记录模板提示或显式 transformation field。届时再评估 Rule、binding 与迁移影响。

本轮没有 `NARROW`、`SPLIT`、`MERGE` 或 `REVISE` 的 canonical proposal。

## Pass E：后续回归影响计划

本轮不改代码，也不执行新的 runtime 测试。若将来修改 F03，回归集应包含：

| 案例 | 已有或拟建输入 | 应保留的行为 |
| --- | --- | --- |
| 正例 | `tests/rules_v1/fixtures/f01_f06_behavioral_matrix.json` 中 `F03R01-positive` | 完整且明确的来源测量声明获得 `PASS` / `DIRECT_EVALUATION`。 |
| 缺失证据 | 同一 fixture 中 `F03R01-missing-evidence`，删除 `source.estimand` | `UNRESOLVED` / `SOURCE_LOOKUP`，不得填补缺失字段。 |
| 变换观测量对抗例 | 后续新增：将 `E_FRET` 与 `R_E,L`，或 `I(q)` 与 `R_G` 故意互换或省略中间变换 | 如果没有显式的原始对象、变换/假设和报告量区分，任何 `PASS` 都应被判为 unsafe false PASS 并拒绝。 |

## 结构与冻结检查

本次交付前的结构检查已通过：

- 三个 JSON 产物可解析，目录中恰有授权的四个交付文件。
- 本地 Fuertes 原始 PDF 的 SHA-256 与 manifest 一致；Pass A 文件的当前 SHA-256 同时与 manifest 和 Pass B projection 中的冻结值一致。
- Pass A 文件不含当前 F03 Rule、binding、contract 或 resolution-policy 标识符。
- manifest 列出的五个 F03 模式输入的当前字节哈希均与冻结值一致；两个来源对象都覆盖同一组六个 required field。
- 对技术中文报告做了非严格模式扫描。没有翻案句或句尾伪分析命中；Markdown 表格分隔线被计入连接号密度，属于格式警告，不改变报告含义。

## 本轮允许与禁止的主张

允许：Fuertes 主文支持此处记录的两类来源测量语义；在准确且完整的项目标注下，冻结的 F03 Draft 契约预期将它们判为来源测量声明 PASS；当前样本没有显示 canonical F03 缺陷。

禁止：把这个开发校准称为 held-out evaluation、runtime 验证、来源科学通过、H1 release、可靠性结论、跨模态可比性、方法验证或科学 SUPPORT。不得把 `R_G` 写成原始 SAXS 观测，也不得把 `R_E,L` 写成原始 smFRET 观测或无标签蛋白实际端到端距离。

## 人工审阅请求与停止点

人工审阅应优先检查每个 typed annotation 是否逐段对应 Fuertes 主文，以及后续候选来源是否重复出现 transformation ambiguity。本 Draft PR 在本报告、四个校准文件和既有 F03 fixture 之外停止；不修改 PR #20，不合并，不发布。
