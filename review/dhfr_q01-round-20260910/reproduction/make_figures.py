from pathlib import Path
import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
r=Path(__file__).resolve().parents[1];o=r/'outputs/report';o.mkdir(exist_ok=True)
x=json.loads((r/'outputs/mic_diagnostic/ligand_comparison.json').read_text());lookup={(a['variant'],a['atom_pair']):a for a in x}
fig,axs=plt.subplots(1,2,figsize=(10,4),sharey=True)
for ax,v,title in zip(axs,['wt','l28r'],['Wild type','L28R']):
 rows=[lookup[v,a] for a in ['r18_O_O3P','r20_N_O3P','r22_O_O3P']];pos=np.arange(3)
 ax.bar(pos-.18,[a['TMP_mean_A'] for a in rows],.36,label='TMP',color='#243b64');ax.bar(pos+.18,[a['4DTMP_mean_A'] for a in rows],.36,label="4′-DTMP",color='#21918c');ax.set_xticks(pos,['N18-O','M20-N','W22-O']);ax.set_title(title);ax.set_ylim(0,13);ax.set_xlabel('Protein atom paired with ligand O3P');ax.legend(frameon=False)
 for i,a in enumerate(rows):
  for shift,k in [(-.18,'TMP_mean_A'),(.18,'4DTMP_mean_A')]:ax.text(i+shift,a[k]+.2,f'{a[k]:.2f}',ha='center',fontsize=9)
axs[0].set_ylabel('Mean minimum-image distance (Å)');fig.suptitle('Deposited trajectories: frames 11–1000, one trajectory per condition');fig.tight_layout();fig.savefig(o/'loop_distances.png',dpi=180);plt.close(fig)
fig,ax=plt.subplots(figsize=(9,4));rows=[a for a in x if a['variant']=='l28r' and a['atom_pair'].startswith('r28_')];pos=np.arange(len(rows));ax.barh(pos,[a['delta_4DTMP_minus_TMP_A'] for a in rows],color=['#21918c' if a['delta_4DTMP_minus_TMP_A']<0 else '#ca6b44' for a in rows]);ax.set_yticks(pos,[a['atom_pair'].replace('r28_','R28-').replace('_','–') for a in rows]);ax.axvline(0,color='#243b64',lw=.8);ax.set_xlabel('4′-DTMP minus TMP mean distance (Å); negative = closer');ax.set_title('R28 effect depends on the ligand oxygen');fig.tight_layout();fig.savefig(o/'r28_changes.png',dpi=180);plt.close(fig)
fig,ax=plt.subplots(figsize=(9,3.7));a=np.genfromtxt(r/'derived/tmpp-wt_distances.tsv',names=True,delimiter='\t');b=np.genfromtxt(r/'derived_mic/tmpp-wt_distances.tsv',names=True,delimiter='\t');ax.plot(a['frame_index'],a['r20_N_O3P'],color='#c0c3c7',label='Stored-coordinate distance');ax.plot(b['frame_index'],b['r20_N_O3P'],color='#243b64',label='Nearest periodic image',lw=1);ax.set(xlabel='Frame index (nominal ns; deposit-based mapping)',ylabel='M20-N–O3P distance (Å)',title='WT–TMP: coordinate wrapping changes the apparent separation');ax.legend(frameon=False);fig.tight_layout();fig.savefig(o/'periodic_diagnostic.png',dpi=180)
print('Three source-linked figures created')
