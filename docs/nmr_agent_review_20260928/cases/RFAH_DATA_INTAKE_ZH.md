# RfaH 2025（Cai et al., PNAS 2025）作者存档数据入库说明

存档位置：`<local-work>/rfah_raw_sealed/archive/`（只读核查，未移动/未改动任何文件，未运行任何 MATLAB 程序）。
论文全文来源：`<workspace>/literature/workflow_papers_20260920/metadata/RFAH2025.html`（Materials and Methods / Experimental Procedures 部分）。

## 总述

存档是作者本人的 MATLAB 全局拟合工作区，对应论文中 RfaH 分离 C 端结构域（RfaH<sup>CTD</sup>）的
15N-CEST + 15N-CPMG 交换动力学分析。顶层 7 个目录对应作者README.docx写明的 7 个递进/并列拟合步骤：

1. `cest-2-state_major` — 仅主态（A 态）15N-CEST，2-state 模型单独拟合。
2. `15N_CEST_major+minor` — 主态+次态（可观测的 B 态）15N-CEST 联合拟合，2-state 模型；内嵌
   `cest-2-state_minor` 子目录做次态单独拟合。
3. `majotr_3stateCPMG-2state-CEST` — 主态 15N-CPMG（3-state 模型）+ 主态 15N-CEST（2-state 模型）联合拟合。
4. `minor_4state_cpmg(branched)_2state_cest` / `minor_4state_cpmg(linrar)_2state_cest` — 次态 15N-CPMG
   （4-state 模型，两种拓扑：branched / linear）+ 主态 15N-CEST（2-state 模型）联合拟合。
5. `5state_together_branched_2state_CEST` / `5state_together_linear_2state_CEST` — 次态 15N-CPMG（5-state
   模型，两种拓扑）+ CEST 联合拟合，是文中最完整的全局模型（对应摘要中的 A、A′、B、B′、B″ 五态网络）。

每个目录内部结构一致：`DATA*`/`CS_data` 子目录放实测数据，顶层 `.m`/`.asv` 是拟合程序，`outputs/`
及顶层散落的 `fit_vals_*`、`D_omega*`、`R2_fit*`、`Omega.txt`、`params_global_fit.txt`、`*.mat` 是拟合中间量
或结果。文件用途判断依据是 `setup_*.m` / `calc_*.m` / `*Fit*.m` / `opt_*.m` 里的 `load()` 调用和保存
（`save`/`fopen`+`fprintf`）语句，而非文件名猜测；具体出处见下表。md5/cmp 比对确认了同名文件在多个目录间是否为同一份原始数据副本（见第三节）。

---

## 一、最小实测数据集合

以下每类只列一份代表性路径；同 md5 的重复副本见第三节，不重复列出。

### 1. 15N-CEST 实测数据（主态 A，10/15/25 Hz 三个 B1 场）

| 文件路径 | 内容 | 列/单位 | 残基映射 | 出处 |
|---|---|---|---|---|
| `majotr_3stateCPMG-2state-CEST/DATA_cest/data_10Hz.txt`（同 `data_15Hz.txt`/`data_25Hz.txt`） | CEST 归一化峰强度矩阵（I_sat/I_ref） | 每行一个残基，每列一个饱和频率偏置点；10/15/25 Hz 分别 231/153/93 列，无量纲 | 行序与同目录 `Res.txt` 一一对应 | `setup_cpmg_data.m` L126–148（`load DATA_cest/data_10Hz.txt; data_1=data_10Hz;`）；论文 *15N-CEST Experiments*：600 MHz、231/153/93 张谱与代码列数精确一致 |
| `.../DATA_cest/cwsat_10Hz`（同 `cwsat_15Hz`/`cwsat_25Hz`） | CEST 饱和频率偏置表，相对 15N 载波（118 ppm） | 单列，单位 Hz；10Hz场：−1130~1170步10（231点）；15Hz场：−1135~1170步15（153点）；25Hz场：−1145~1155步25（93点） | 与 data_*Hz.txt 列序对应 | `setup_cpmg_data.m` L129/138/147（`fqlist_1=cwsat_10Hz'+N15_CARRIER_HZ`）；论文同一段落 |
| `.../DATA_cest/Res.txt` | 残基编号列表（47 个残基） | 单列，残基序号（整数） | 定义上表所有矩阵的行序 | `setup_cpmg_data.m` L105–106 |
| `.../DATA_cest/15N_major.txt` | 主态 15N 化学位移 | 列1=残基号，列2=化学位移(ppm) | 与 Res.txt 同序 | `setup_cpmg_data.m` L108–110（`cs(:,2)=cs(:,2)*B0_FIELD` 换算为 Hz） |
| `.../DATA_cest/R1_major.txt`、`.../DATA_cest/R2_major.txt`（原始，见 `cest-2-state_major/DATA/R1_major.txt` 等） | 实测 R1、R2 弛豫速率（单指数拟合得到，视为一手实验读数） | 列1=残基号，列2=速率(s⁻¹)，列3=误差(s⁻¹) | 与 Res.txt 匹配后合并进 R12_list.txt | `cest-2-state_major/DATA/R1_R2.m` L4–7（`load R2_major.txt; R2=R2_major; load R1_major.txt; R1=R1_major`），该脚本把 R1/R2/D_omega/CEST 数据按残基号交叉匹配后另存为 `Res.txt`/`R12_list.txt`/`data_*Hz.txt`（L93–98），`DATA_cest/` 下的同名文件即为该脚本处理后的结果 |

### 2. 15N-CPMG 实测数据（600/900 MHz 两场，主态）

| 文件路径 | 内容 | 列/单位 | 残基映射 | 出处 |
|---|---|---|---|---|
| `majotr_3stateCPMG-2state-CEST/R2eff_600_major.txt`、`R2eff_900_major.txt` | 实测有效 R2（CPMG 弛豫色散谱） | 每行一残基，19 列，对应 νCPMG=17,33,50,67,83,100,117,133,150,167,200,250,333,417,500,583,667,833,1000 Hz，单位 s⁻¹ | 行序=同目录 `Res_major.txt`（48残基，脚本加载后删除第36行→47） | `setup_cpmg_data.m` L88–91（`R2eff_H=load('R2eff_900_major.txt'); R2eff_H(36,:)=[];`）；论文 *15N CPMG Relaxation Dispersion Measurements*：CT=60 ms、19 个 νCPMG 值与代码 `ncyc=[1 2 3 4 5 6 7 8 9 10 12 15 20 25 30 35 40 50 60]; fullCT=0.06` 换算结果逐一对应 |
| `.../sigma_H_major.txt`（900 MHz）、`sigma_L_major.txt`（600 MHz） | R2eff 实测不确定度 | 同上矩阵形状，单位 s⁻¹ | 同上 | `setup_cpmg_data.m` L92–95 |
| `.../int_mcab600_major.txt`、`.../int_neo900_major.txt` | 更底层的 CPMG 原始峰强度（未经 R2eff 换算） | 列1=残基号，其后每列一个 νCPMG 点的峰强度（含500Hz重复点，对应论文"21个数据集=19个νCPMG+1个500Hz重复点+参考"） | 列1为残基号 | 不被存档内任何 `.m` 脚本 `load()`；论文正文提及重复点与参考谱但换算脚本未包含在本存档中（见第四节"尚不确定"） |
| `5state_together_branched_2state_CEST/CPMGfield.txt` | νCPMG 场强列表 | 单列，19 个值，单位 Hz | — | `setup_cpmg_data.m` L24–33 用 `ncyc./fullCT` 现算，CPMGfield.txt 是同一列表的落盘副本，数值与论文一致 |

### 3. 15N-CPMG 实测数据（次态 B，4 个含次态-CPMG的目录中一致）

| 文件路径 | 内容 | 说明 |
|---|---|---|
| `minor_4state_cpmg(linrar)_2state_cest/R2eff_600_minor.txt`、`R2eff_900_minor.txt` | 次态 CPMG 有效 R2 | 结构同主态版本 |
| `.../sigma_H_minor.txt`、`sigma_L_minor.txt` | 次态 R2eff 误差 | 同上 |
| `.../int_mcab600_minor.txt`、`.../int_neo900_minor.txt` | 次态原始峰强度 | 同主态，未被脚本加载 |
| `.../Res_minor.txt` | 次态残基编号表 | 见第三节：与部分目录中 `Res_major.txt` 内容巧合相同（同一批被测残基） |

### 4. 15N-CEST 实测数据（次态 B，仅 `15N_CEST_major+minor` 目录）

| 文件路径 | 内容 |
|---|---|
| `15N_CEST_major+minor/DATA_minor/data_10Hz_minor.mat`（对应 `.../cest-2-state_minor/DATA_minor/data_10Hz.txt` 等文本版） | 次态 CEST 强度矩阵，结构同主态 data_*Hz.txt |
| `.../DATA_minor/R12_list.txt`（`.txt` 版在 `cest-2-state_minor/DATA_minor/`） | 次态 R1/R2 合并表 |
| `.../DATA_minor/cs_list.txt` | 次态化学位移表 |

### 5. 化学位移交叉验证数据（仅 `minor_4state_cpmg(linrar/branched)_2state_cest/CS_data/`）

| 文件路径 | 内容 | 说明 |
|---|---|---|
| `CS_data/N_major.txt` | 主态构象 15N 化学位移（实测，独立于CEST/CPMG拟合） | `delta_corr_plot.m` L2 |
| `CS_data/N_minor.txt` | 次态构象 15N 化学位移（残基号做了 −200 偏移，来自一个用于隔离次态构象的独立构建/样品） | `delta_corr_plot.m` L3, L9（`Res_mi=N_minor(:,1)-200`） |
| `CS_data/N_fl.txt` | 全长 RfaH 的 15N 化学位移 | 用变量名 `random` 装载但函数内注释为 "full length shifts" 的对照 |
| `CS_data/N15.txt` | 野生型 CTD 的 15N 化学位移 | `delta_corr_plot.m` L5 |

这组文件只用于 `delta_corr_plot.m` 里的散点图交叉验证（比较 CEST/CPMG 拟合得到的 Δω 与直接测得的化学位移差），**不进入**核心 CEST/CPMG 全局拟合流程，但本身是实测数据，应保留。

---

## 二、实验参数（程序 + 论文双重确认）

- **15N 载波**：118.074 ppm（`setup_CEST.m` L17：`N15_CARRIER_PPM = 118.074`）；论文写"118 ppm"，一致。
- **主磁场换算**：`B0_FIELD = 60.815 MHz`（15N Larmor，对应 ¹H 600 MHz 谱仪）；CPMG 高场 `B0field = 90.2 MHz`（对应 ¹H 900 MHz）、低场 `low_field = 60.8 MHz`（对应 600 MHz）（`setup_cpmg_data.m` L24–26）；论文：CEST 在 600 MHz 采集，CPMG 在 600/900 MHz 两场采集，一致。
- **CEST 饱和时间**：0.600 s（`calc_CEST.m` L19：`SAT_LENGTH = 0.600`）；论文："exchange time T_CEST set to 600 ms"，一致。
- **CEST 三个 B1 场强**：10、15、25 Hz，各 231/153/93 张谱（增量分别为10/15/25Hz）；论文精确给出同样数字，代码 cwsat_*Hz 文件行数与之逐一对应。
- **CPMG 恒定时长 (CT)**：60 ms（`setup_cpmg_data.m` L27：`fullCT=0.06`）；论文："The relaxation period was set to 60 ms"，一致。
- **νCPMG 列表**：17,33,50,67,83,100,117,133,150,167,200,250,333,417,500,583,667,833,1000 Hz（由 `ncyc=[1 2 3 4 5 6 7 8 9 10 12 15 20 25 30 35 40 50 60]` 与 `fullCT=0.06` 相除取整得到）；论文给出完全相同的 19 个数值，并说明 500 Hz 处有重复点用于误差估计（对应 `int_*.txt` 里比 R2eff 多出的一列）。
- **温度**：25 °C（仅见于论文 *NMR Experiments*："All NMR data were recorded at 25 °C on Bruker 500, 600, 700, and 900 MHz NMR spectrometers…"）。**存档内 MATLAB 程序未记录温度值**，无法从代码侧交叉验证，只能视为论文单一来源（见第四节）。
- **样品**：1.0 mM 同位素标记 RfaH<sup>CTD</sup>，95%/5% (v/v) H₂O/D₂O，25 mM 磷酸钾缓冲液，pH 6.5，0.5 mM EDTA（论文同段落）。
- **主/次态区分**：论文摘要给出 A（~76–77%，主态即"major"）、B（~23%，NMR 可直接观测的次态即"minor"）、A′（~0.35%）、B′（~0.3%）、B″（~0.05%）五个态；`major`/`minor` 后缀文件名直接对应 A/B 两个可观测态，A′/B′/B″ 只在 CPMG 弛豫色散中以化学位移差（Δω，如 `D_omega_cpmg.txt`、程序变量 `wCA`/`wBA`/`wBC`/`wBD`）体现，没有独立的强度数据文件。
- **残基编号方式**：所有实测矩阵按 `Res.txt`/`Res_major.txt`/`Res_minor.txt`/`Res_data.txt` 给出的残基号顺序逐行排列；不同拟合步骤之间残基集合会因数据完整性筛选而略有出入（例如 `cest-2-state_major/DATA`为48个残基，而下游 6 个联合拟合目录统一筛选为 47 个残基，缺失的是残基123，见第三节）。

---

## 三、副本比对结果（md5 + 行数/内容 diff）

以下按数据类别汇总；同一 md5 视为逐字节相同副本。

| 数据类别 | 相同的目录集合 | md5 结果 | 结论 |
|---|---|---|---|
| CEST 饱和偏置表 `cwsat_10Hz/15Hz/25Hz` | 全部 8 个含 CEST 数据的目录（含 `cest-2-state_major` 及 6 个联合拟合目录及 `15N_CEST_major+minor` 系列） | 逐目录 md5 完全一致 | 真正恒定的实验参数，全存档统一，无需多份保留 |
| CEST 强度数据 `data_10/15/25Hz.txt`、`R12.txt`/`R12_list.txt`、`R2_major.txt`、`R1_major.txt`、`15N_major.txt`、`Res.txt`、`Res_data.txt`、`sigma_1/2/3.txt` | 分两代：(a) `cest-2-state_major/DATA/*`（48 残基，md5 各不相同于(b)）；(b) `majotr_3stateCPMG-2state-CEST/DATA_cest/*`、`minor_4state_cpmg(branched)_.../DATA_cest/*`、`minor_4state_cpmg(linrar)_.../DATA_cest/*`、`5state_together_branched_.../DATA_cest/*`、`5state_together_linear_.../DATA_cest/*` 五个目录（47 残基，md5 互相完全一致） | (a) 与 (b) 不同；(b) 内部 5 份完全相同 | (b) 是逐字节复制、被所有下游联合拟合目录复用的"权威版"主态 CEST 数据；(a) 是更早、多1个残基（残基123，`diff Res.txt` 确认）的独立版本，两者都是真实数据但代表不同筛选阶段，**最小集合建议以 (b) 为准**，(a) 作为历史版本单独说明 |
| CPMG 主态数据 `R2eff_600/900_major.txt`、`sigma_H/L_major.txt`、`int_mcab600/neo900_major.txt`、`Res_major.txt` | `majotr_3stateCPMG-2state-CEST`、`5state_together_branched_2state_CEST`、`5state_together_linear_2state_CEST`（3 目录） | 三者 md5 完全一致 | 主态 CPMG 数据在 3、5 态各拓扑变体间未被修改，一份即可 |
| CPMG 次态数据 `R2eff_600/900_minor.txt`、`sigma_H/L_minor.txt`、`int_mcab600/neo900_minor.txt`、`CPMGfield.txt` | `minor_4state_cpmg(branched)_2state_cest`、`minor_4state_cpmg(linrar)_2state_cest`、`5state_together_branched_2state_CEST`、`5state_together_linear_2state_CEST`（4 目录） | 四者 md5 完全一致 | 次态 CPMG 数据在 4、5 态各拓扑变体间未被修改，一份即可 |
| `Res_minor.txt` | `5state_together_branched/linear`两目录一致（hash A）；`minor_4state_cpmg(branched)/(linrar)`两目录一致（hash B，且与 `15N_CEST_major+minor/DATA_major/Res_major.txt` 相同） | 两组各自一致，A≠B | 数值巧合相同（同一批残基编号序列），不代表主/次态混淆，但需要在重命名时逐一核对，不能只凭文件名判断 |
| **异常：`15N_CEST_major+minor/cest-2-state_minor/DATA-old/*`** | 该子目录下 `data_10Hz.txt`、`15N_major.txt`、`R1_major.txt`、`R2_major.txt`、`R12.txt`、`data_25Hz.txt` 等的 md5 与 `cest-2-state_major/DATA/*`（**主态**数据）完全相同，而不是与同级 `DATA/`、`DATA_minor/`（正确的次态数据，md5 一致）相同 | 见上 | `DATA-old` 很可能是从主态分析目录整体复制、后续切换到次态分析时未更新内容的**残留旧目录**，其内容其实是主态数据被误留在"次态"路径下。构建解题工作区或引用此目录时必须排除 `DATA-old`，只用同目录下的 `DATA/` 与 `DATA_minor/` |

---

## 四、必须封存清单（作者拟合结果 / 中间量 / 程序 / 会泄露结论的名称）

### 拟合结果与中间量（禁止当作实测数据使用）

- 所有 `outputs/` 目录下的文件：`fit_vals_1/2/3`、`fit_vals_H`、`fit_vals_L`、`fit_vals_H_major`、`fit_vals_H_minor`、`fit_vals_L_major`、`fit_vals_L_minor`、`D_omega.txt`（outputs内的）、`R2_fit.txt`（outputs内的）、`branched_of_D_omega.txt`、`params_global_fit.txt`、`jac_cpmgFitRes.mat` —— 均由 `setup_CEST.m`（L199–237, `save fit_vals_* ... -ascii`）或 `opt_all_*state.m` 系列在拟合迭代中/收敛后写出，是模拟曲线或拟合参数，不是实测。
- 顶层散落的中间量：`Omega.txt`、`delta_Omega.txt`（`setup_CEST.m` L185–186, `fopen('Omega.txt','w')`）、`R2A.txt`/`R2A_major.mat`/`R2A_minor.mat`、`R2B.txt`/`R2B_major.mat`/`R2B_minor.mat`、`Io_fit.txt`（拟合值，区别于全为1.0的初始猜测`Io_list.txt`，已用`head`核实）、`D_omega_init.txt`、`D_omega_fit.txt`、`D_omega_minor.txt`、`D_omega_major.txt`、`D_omega_m.txt`、`D_omegaA/B/C_save.txt`、`D_omega_all.txt`、`R2_fit.txt`（顶层，被`setup_cpmg_data.m` L38 当作上一步拟合结果重新加载，用来定义残基集合和初值——本身就是被复用的拟合输出）、`R2_fit_minor.txt`、`R2_init.txt`、`R2A_H.txt`/`R2A_L.txt`（CPMG 拟合初值/结果）、`fitted_global_parameter.txt`、`cs_om_tbl.txt`、`screen_output.txt`、`jac_CEST.mat`、`ci`（confidence interval 变量转储）。
- 各级 `README.docx`：逐条写明了每个目录对应的模型设定（几态、拓扑），内容本身即结论描述，不应随数据一起进入解题工作区。

### 程序文件

- 全部 `*.m`、`*.asv`（如 `CEST_fit.m`、`calc_CEST.m`、`setup_CEST.m`、`cest_opt.m`/`cest_opt_all.m`、`setup_cpmg_data.m`、`R2_newcpmg_*.m`、`cpmgFit_*_2field.m`、`opt_all_*state.m`、`CPMGplot.m`、`plot_CEST.m`、`simulate_CEST.m` 等）——按任务要求不运行，仅作为"数据 vs 拟合"判断依据保留在封存区，不进入解题工作区。

### 会泄露论文结论的目录名 / 文件名 / 变量名（构建解题工作区时必须改名）

- 顶层 7 个目录名全部暴露态数和拓扑：
  - `cest-2-state_major` → 暴露"2态"
  - `15N_CEST_major+minor` → 暴露 major/minor 两态标签
  - `majotr_3stateCPMG-2state-CEST` → 暴露"3态"
  - `minor_4state_cpmg(branched)_2state_cest` / `minor_4state_cpmg(linrar)_2state_cest` → 暴露"4态" + branched/linear 拓扑
  - `5state_together_branched_2state_CEST` / `5state_together_linear_2state_CEST` → 暴露"5态" + 拓扑（对应论文摘要 A/A′/B/B′/B″ 五态网络及"linear model"/"branched model"两种B″连接方式）
- 内部程序/变量名同样暴露态数与状态标签，需要连带处理：`R2_newcpmg_3state.m`/`_3stateB.m`/`_3stateC.m`、`R2_newcpmg_5state_majorA/B/E.m`、`R2_newcpmg_5state_minorA/B/C/D.m`、`opt_all_3state.m`/`opt_all_4state.m`/`opt_all_5state.m`、`cpmgFit_3state_2field.m`/`cpmgFit_4state_2field.m`/`cpmgFit_5state_2field.m` —— 文件名里的数字与 A/B/C/D/E 后缀对应论文里的状态标签（A、A′、B、B′、B″）。
- 数据文件名里的 `major`/`minor` 字样（`Res_major.txt`、`Res_minor.txt`、`R1_major.txt`、`data_10Hz_minor.mat`、`15N_major.txt` 等）直接对应论文 A（主态，可观测基态）与 B（次态，23%占据的可观测激发态）标签，构建解题工作区时应替换为中性名（如 `dataset_1`/`dataset_2` 或 `high_pop_state`/`low_pop_state` 之类不预设结论的命名，具体命名策略由后续任务决定）。

---

## 五、尚不确定清单

- **int_mcab600_*.txt / int_neo900_*.txt 到 R2eff_*.txt 的换算方式未知**：这两组文件是比 R2eff 更底层的原始峰强度（含500Hz重复点），但存档内没有任何 `.m` 脚本 `load()` 它们，换算公式（参考强度 I0 的选取、R2eff = f(强度比, CT) 的具体实现）不在本存档内，无法在不运行外部工具的前提下确认。
- **D_omega.txt / D_omega_init.txt 的原始来源未知**：`cest-2-state_major/setup_CEST.m` L134–135 把它当作初始猜测值加载，并允许在拟合中 ±700 Hz 浮动，不清楚这个初始值本身是否来自独立测量（类似 `CS_data/` 里对次态可见峰的直接 HSQC 比对）还是作者根据 CEST dip 位置目测估计；论文正文未逐条说明。
- **`B2.txt`（`majotr_3stateCPMG-2state-CEST` 顶层）用途不明**：162 行，大部分为0，中段（约残基108起）有一段非零小数值，但目录内任何 `.m` 脚本都未 `load()` 此文件，无法确认它是弃用的中间量还是未被当前脚本调用的额外实测量。
- **`sigma_1.txt`/`sigma_2.txt`/`sigma_3.txt`（各 `DATA`/`DATA_cest` 目录下）是孤立文件**：程序实际使用的 CEST 强度不确定度是硬编码常数（`setup_CEST.m` L40/71/80 及 `setup_cpmg_data.m` L128/137/146 里的 `0.02`、`0.02`、`0.025`），从未 `load()` 这三个文件；它们的数值来源、是否为更早版本遗留不明确。
- **温度、缓冲液等实验条件仅见于论文正文，代码侧无法交叉验证**：25 °C、pH 6.5、25 mM KPi、0.5 mM EDTA 等条件只在 `RFAH2025.html` 的 Materials and Methods 中出现，MATLAB 程序未记录，因此这些数值只有论文单一信源，没有存档内的第二来源可比对。
- **哪一份 R2eff/int_ 数据对应论文最终发表图表未标注版本号**：branched/linear、3/4/5-state 各变体间虽然原始数据字节相同，但存档内没有日期戳或版本标记能确认"最终正式结果"对应哪一次拟合运行；本次未逐一核对文件 mtime，只能依据目录结构与README.docx描述做逻辑推断。

---

## 主会话补记（2026-09-26）

- 正控输入由 `<local-work>/rfah_pc/make_chemex_inputs.py` 从 `majotr_3stateCPMG-2state-CEST` 的最小实测集生成（47 残基，主态峰；CEST 误差按作者程序常数 0.02/0.02/0.025；CPMG 由 R2eff 换算为等价强度；删除第 36 行同作者程序）。磁场按作者程序取 ¹⁵N 60.815 MHz 与 90.2 MHz；后者对应 ¹H 约 890 MHz，与论文所写 900 MHz 有约 1% 差，正控按作者实际计算复现，解题工作区需另行决定并注明。
- 解题工作区构建时额外封存：`CS_data/N_minor.txt`（B 态直接实测位移，属于 A5 划分中的答案）；所有 `D_omega*`（来源不明，视为作者估计）；`15N_CEST_major+minor/cest-2-state_minor/DATA-old`（误留的主态数据）。
