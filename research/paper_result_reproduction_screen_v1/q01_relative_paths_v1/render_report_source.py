from pathlib import Path
import json,csv,datetime
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
w=Path.cwd();t=w/'autoresearch/tasks/dynamics_atlas_paper_result_reproduction_screen_20260904';a=t/'outputs/q01_path_comparison_v1';o=t/'outputs/q01_relative_paths_v1'
r=json.loads((o/'numerical_report.json').read_text());maps=json.loads((a/'trajectory_mapping.json').read_text());rows=list(csv.DictReader((o/'full_preference_paths.tsv').open(),delimiter='\t'));assert len(rows)==40040
by={m['name']:[] for m in maps}
for row in rows:by[row['trajectory']].append(row)
maxbond=0
for m in maps:
 d=np.load(a/'trajectories'/m['name']/'coordinates.npz');xyz=d['xyz_nm'];keys=[tuple(k) for k in m['mapping']['atom_keys']];ix={k:i for i,k in enumerate(keys)}
 for residue in range(40,220):
  maxbond=max(maxbond,float(np.linalg.norm(xyz[:,ix[(residue,'C')]]-xyz[:,ix[(residue+1,'N')]],axis=1).max()))
 assert len(by[m['name']])==1001 and [float(x['time_ns']) for x in by[m['name']]]==list(range(20,1021))
assert maxbond<.2,maxbond
# Canonical rows include each method and all predeclared persistence values.
assert len(r['rows'])==80 and all(set(x['paths'])=={'5','20','50'} for x in r['rows'])
changes=sum(x['frame_preference_changes'] for x in r['method_changes']);rr=json.loads((o/'receipt.json').read_text());assert rr['same_instance_as_parent'] and rr['on_operator_calls']==1 and rr['off_operator_calls']==0
fig,axs=plt.subplots(2,2,figsize=(15,11),gridspec_kw={'width_ratios':[1,1]},layout='constrained')
for row,seed in enumerate(['open','closed']):
 names=[m['name'] for m in maps if m['seed']==seed]
 geometry=np.array([[float(x['geometry_margin_A']) for x in by[n]] for n in names])
 im=axs[row,0].imshow(geometry,aspect='auto',origin='upper',extent=[20,1020,20.5,.5],cmap='coolwarm',vmin=-12,vmax=12)
 labels=np.array([[{'open':0,'conflict':1,'closed':2}[x['SI_preference']] for x in by[n]] for n in names])
 axs[row,1].imshow(labels,aspect='auto',origin='upper',extent=[20,1020,20.5,.5],cmap=ListedColormap(['#b94f46','#e1ded7','#477ca9']),vmin=0,vmax=2)
 for ax in axs[row]:ax.set_yticks(range(1,21));ax.set_ylabel(seed+'-seeded trajectory');ax.set_xlabel('Saved trajectory time (ns)')
 axs[row,0].set_title('Closed-reference RMSD minus open-reference RMSD')
 axs[row,1].set_title('Geometry + SI-contact relative preference')
fig.colorbar(im,ax=axs[:,0],label='Angstrom: positive = nearer open reference')
fig.suptitle('Q01: full paths of all 40 trajectories\nRelative preference is not membership in an NMR reference state',fontsize=15)
from matplotlib.patches import Patch
axs[0,1].legend(handles=[Patch(color='#b94f46',label='open preference'),Patch(color='#e1ded7',label='conflict'),Patch(color='#477ca9',label='closed preference')],loc='upper center',bbox_to_anchor=(.5,1.14),ncol=3,fontsize=9)
fig.savefig(o/'full40_paths.png',dpi=160);fig.savefig(o/'full40_paths.pdf');plt.close(fig)
validation={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','full_path_rows':len(rows),'trajectory_method_records':len(r['rows']),'frames_each':1001,'max_backbone_adjacent_C_N_nm':maxbond,'threshold_method_frame_preference_changes':changes,'same_instance':True,'category_changes_20frames':sum(x['category_changes']['20'] for x in r['method_changes']),'gmx_calls_repeated':0,'optimizer_calls':0}
(o/'artifact_check.json').write_text(json.dumps(validation,indent=2)+'\n')
(a/'REPORT_ZH.md').write_text('''# Q01 完整轨迹与状态参照范围检查

40条原始XTC均由现有GROMACS读取，1001个20–1020ns时间点/条。每次读取同时产生N、CA、C、O主链坐标、甲基氢坐标与盒矩阵。所有24接触使用同一坐标产生统一阈值和SI逐接触阈值评分。每条与作者存档pseudo-COM评分对照，最大差0.00500167Å，低于预登记0.011Å。全部主链相邻C–N距离检查通过，坐标没有人为拼接或换成Cα。

SI页4–5明确排除O04/O10/O15/O23/O24；19open+5closed是原MD指标子集。作者脚本的backbone语义与四原子选择已按源代码核准，详见source_method_review.md。

第一项规则控制的比较使用NMR construction范围：每态自身20模型留一最近lidRMSD最大值作为几何范围，每方法/态自身接触评分最大值作为接触范围，要求两者同时支持。参照自身20/20符合，但全部40轨迹在分析起点不在该范围。两套方法都不能据此判定起始态/离开；不能把全体未分类称为“稳定的轨迹结论”。早期过宽的状态措辞被纠正，原数值和修正前回执均保存。两方法仅改变3条轨迹共16帧的范围支持标签。

这暴露了方法-问题错配：NMR范围支持与相对方向不是同一问题。随后同一规则消费此数值证据，要求相对参照路径对照；后续结果在../q01_relative_paths_v1/，原范围缺口保留。

实际首项on1/off0、40次gmx、0优化；完整20题原基线仍不变。数值派发前保存rules_before.json，数值报告重算后返回同一实例。人工ES01canary没有追认为过去Rulesextra。当前是显式Q01 CASE规则开发，不冒充全20题通用能力。
''')
(o/'REPORT_ZH.md').write_text(f'''# Q01 已得到完整40条轨迹的有界方向性结果

在这些已发表的种子和模拟条件下，开放构象启动的20条轨迹均保持对开放参照的相对偏好；闭合构象启动的20条中，9条出现至少20个连续采样点的开放参照偏好，1条持续失去闭合偏好但两种几何指标没有一致转向，10条未出现持续偏好丢失。这个有限时间方向性在两套来源接触阈值下保持一致。

这里“偏好”要求core对齐后的lid主链RMSD和接触指标同时更偏向同一参照。两个接触分数按NMR开放/闭合集合的均值差分别归一化，然后取等权投影，避免直接比较19接触与5接触的未校准平均。正向表示更近开放参照；这不是概率。冻结方法见frozen_policy.json，40模型用于construction归一化，非独立实验或heldout。

| 连续采样点 | 开放种子：未持续丢失开放偏好 | 闭合种子：持续开放偏好 | 闭合种子：持续冲突 | 闭合种子：未持续丢失闭合偏好 |
|---|---:|---:|---:|---:|
|5（采样跨度4ns）|20|10|1|9|
|20（跨度19ns；主判据）|20|9|1|10|
|50（跨度49ns）|20|8|2|10|

两套接触定义在全部三项持续性条件下都给出相同的轨迹类别。逐帧偏好有{changes}个差异，主类别变化0/40；阈值改变评分的幅度不等于科学结论增益。完整时间路径保存在full_preference_paths.tsv，图见full40_paths.png。时间点不是独立重复，统计单位保留为轨迹；不估计平衡人口或跃迁速率。

![Full paths](full40_paths.png)

前一方法把NMR参照范围当作起始状态要求，导致40/40起点不被覆盖，不能回答原方向问题。本次作为已暴露的开发修订，保留范围外事实，仅比较相对方向；没有放大参照范围，也没有用作者轨迹标签、结果人数或阈值目标初始化。原方法失败在../q01_path_comparison_v1/。该结果支持比“真实进入开放态”更窄的相对方向判断；精确原文分组/亚稳性解释及领域最终判定仍未完成，因此完整题数尚不加一。

同一RuleInstance在已验证的全体初始范围缺口后实际产生一项新义务：on1/off0，复用全部40条坐标衍生结果，gmx新调用0、优化0。EvidenceResult逐项重算后，状态从方法不能回答起始态，变为“两套方法下相对方向稳定”；保留原范围缺口。它证明这项窄Rules能组织必要方法跟进和消费数值结果，没有证明相对专家正确流程的准确率增益。

核验：5项主路径检查（首次语法错误修复后通过）、2项跟进检查通过；40轨迹源评分、完整时间轴与数值回放通过。相邻C–N最大距离{maxbond:.6f}nm。记录位于artifact_check.json。保留旧结果，未重复轨迹读取。Pro审阅将在同一PR发布后进行。
''')
print(json.dumps(validation,indent=2))
