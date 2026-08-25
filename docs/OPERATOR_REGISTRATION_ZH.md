# Registered operator 设计

## Skill 与 operator 的关系

Installed skill 回答“专家通常怎样做这类分析”。Registered operator 回答“这次运行允许执行哪个固定实现”。两者不能画等号。

例如 `molecular-dynamics` skill 提供 OpenMM、MDAnalysis、RMSD、RMSF 和 contacts 的程序性模板；本机 runtime probe 却没有找到 MDAnalysis/OpenMM/MDTraj。正确状态是 `REGISTERED_BLOCKED`，而不是“已经接入 MDAnalysis”。

## OperatorSpec 最小字段

| 字段 | 目的 |
|---|---|
| `operator_id`, `version` | 稳定调用身份 |
| `skill_ref` | 为什么选择这个方法/库的程序性来源 |
| `implementation_ref` | 固定脚本、包或 API adapter |
| `runtime` | package/CLI/container 与版本 probe |
| `fixed_inputs` | 不允许模型替换的 source paths |
| `fixed_parameters` | 人工或既有分析冻结的参数 |
| `input_contract`, `output_contract` | 类型与统计单位 |
| `route_match` | 哪类 gap、target、method 可以调用 |
| `claim_ceiling`, `forbidden_claims` | output 不能被升级成什么结论 |
| canary receipt | 当前环境是否真的跑过 |

Registry 是 allowlist。Agent 可以提出 `RUN_OPERATOR`，deterministic resolver 才能依据 gap 与 spec 选择；模型不能传入任意 entrypoint、文件路径或 shell command。

## 当前两个 specs

### `hsp90.directional_time_anatomy.v0`

- 来源：现有 HSP90 time-anatomy v0 脚本；
- runtime：Python standard library；
- inputs：固定的 `frame_state_assignments.tsv` 与 `route_predictions.tsv`；
- parameters：`persistence_saved_frames = [5,20,50]` 和既有 zero-sign rule；
- statistical unit：trajectory，frame runs 只做 within-trajectory 描述；
- output：三张 TSV 和 `results_summary.json`；
- claim ceiling：same-packet descriptive diagnostic；
- 不能声称 rate、equilibrium、population、free energy、complete pathway、mechanism 或 mutation effect。

2026-08-25 canary 为 `SUCCEEDED`。它复用了旧脚本，没有重写科学算法。

### `trajectory.structural_state_projection.v1`

- 来源：installed `molecular-dynamics` skill 与已有 AdK pilot；
- candidate backend：MDAnalysis + NumPy/SciPy/scikit-learn；
- 当前 blocker：MDAnalysis runtime 不可用；新 case 的 trajectory/topology/reference/mapping、MD method profile、metric 和 parameters 未冻结；
- 当前状态：`REGISTERED_BLOCKED`，不会执行。

## NMR package

会议录音确认 Gina 发布过一个 NMR Python package，但转写和本地保存材料没有保留 package 名或链接。它暂时不能进入 registry。拿到链接后按以下顺序处理：

1. 核对官方 source、license、version 和实际 API；
2. 从 skill/docs 提取 candidate capability；
3. 选择一个真实 gap，不做整个 package 的泛化注册；
4. 冻结 input/output/parameter/claim ceiling；
5. runtime probe；
6. 一个最小 canary；
7. canary PASS 后保留 `CANARY_PASS / NOT_ROUTABLE`；只有完整 output schema、exact case/input binding 和 route-specific evaluation contract 都通过后，才能由人工提升为 `ROSTER_PASS / routable=true`。

## 怎样增加下一个 operator

优先级不是“库越多越好”，而是：

1. 先看现有 RunPlan 的 blocked gaps；
2. 选择影响最高且已有 established package/旧分析的一个 gap；
3. 优先复用 installed scientific skill 或项目脚本；
4. 只写 adapter 和 contract，不重写算法；
5. 运行一次 scoped canary；
6. 让 EvidenceResult 回到 Evaluation Contract，再 reevaluate。

当 operator 数量只有个位数时，JSON registry 足够。只有出现大量依赖、兼容性和替代工具关系时，才参考 SciToolAgent 式 tool knowledge graph。
