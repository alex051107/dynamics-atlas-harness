from pathlib import Path
import json,csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
p=Path('autoresearch/tasks/dynamics_atlas_paper_result_reproduction_screen_20260904');o=p/'outputs/q01_absolute_paths_v1';r=json.loads((o/'numerical_report.json').read_text());rows=sorted(r['rows'],key=lambda x:(x['seed_group']!='open',x['trajectory']));names=[x['trajectory']for x in rows];blue='#277DA8';orange='#C86B28'
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
fig,ax=plt.subplots(3,2,figsize=(13,15),gridspec_kw={'height_ratios':[1.25,1,1]});fig.subplots_adjust(top=.91,bottom=.07,hspace=.38,wspace=.35)
fig.suptitle('Q01 | Absolute structural motion across all 40 HSP90 paths',fontsize=18,x=.065,ha='left',y=.975)
fig.text(.065,.945,'20 open-seeded + 20 closed-seeded paths · 20–1020 ns · same core alignment and backbone atoms',fontsize=11)
disp=[];md=[]
for name in names:
 with np.load(o/(name+'.npz'),allow_pickle=False)as z:disp.append(z['displacement_from_20ns_A']);md.append(z['nearest_open_MD_lid_rmsd_A'])
for a,matrix,title,cmap,vmax in [(ax[0,0],disp,'A  Lid displacement from analysis start','magma',22),(ax[0,1],md,'B  Distance to nearest open MD reference','viridis',20)]:
 im=a.imshow(matrix,aspect='auto',origin='upper',extent=[20,1020,40.5,.5],vmin=0,vmax=vmax,cmap=cmap);a.axhline(20.5,color='white',lw=1.5);a.set_title(title,loc='left');a.set_xlabel('Time (ns)');a.set_yticks([1,10,20,21,30,40],['GS01','GS10','GS20','ES01','ES10','ES20']);fig.colorbar(im,ax=a,pad=.02,label='Core-aligned lid RMSD (Å)')
a=ax[1,0]
for j,seed in enumerate(['open','closed']):
 vals=[x['absolute_metrics']['lid_displacement_from_20ns_A']['first20_to_last20']['after_median']for x in rows if x['seed_group']==seed];jitter=np.linspace(-.18,.18,len(vals));a.scatter(j+jitter,vals,color=[blue,orange][j],s=30,alpha=.85);q25,med,q75=np.quantile(vals,[.25,.5,.75]);a.plot([j-.25,j+.25],[med,med],color='black',lw=2);a.vlines(j,q25,q75,color='black',lw=3)
a.set_xticks([0,1],['Open seeds (n=20)','Closed seeds (n=20)']);a.set_ylabel('Terminal 20-sample median displacement (Å)');a.set_title('C  Whole trajectories are the comparison units',loc='left');a.text(.03,.97,'Group medians: 3.77 Å vs 9.71 Å\nConditional median difference: 5.94 Å',transform=a.transAxes,va='top',fontsize=9)
a=ax[1,1];a.axhline(0,color='.7',lw=.8);a.axvline(0,color='.7',lw=.8)
for x in rows:
 m=x['absolute_metrics'];xx=m['open_reference_lid_rmsd_A']['first20_to_last20']['delta'];yy=m['closed_reference_lid_rmsd_A']['first20_to_last20']['delta'];candidate=x['methods']['deposited_uniform']['unchanged_relative_path']['category']=='SUSTAINED_OPPOSITE_REFERENCE_PREFERENCE';a.scatter(xx,yy,c=blue if x['seed_group']=='open'else orange,s=45 if candidate else 25,edgecolors='black'if candidate else'none',linewidths=.7)
 if x['trajectory'].split('_')[1]in ['ES05','ES17','ES07','ES01']:a.annotate(x['trajectory'].split('_')[1],(xx,yy),xytext=(5,3),textcoords='offset points',fontsize=8)
a.set_ylim(-4,17);a.set_title('D  Absolute direction, all 40 trajectories',loc='left');a.set_xlabel('Change in distance to open NMR reference (Å)');a.set_ylabel('Change in distance to closed NMR reference (Å)');a.text(.03,.97,'Upper-left: closer to open, farther from closed\nOutlined points: original 9 relative candidates',transform=a.transAxes,va='top',fontsize=8)
a=ax[2,0];es17=[x for x in rows if '_ES17_'in x['trajectory']][0];data={m:[]for m in ['deposited_uniform','SI_per_contact']}
with(o/'full_absolute_paths.tsv').open()as f:
 for line in csv.DictReader(f,delimiter='\t'):
  if line['trajectory']==es17['trajectory'] and 605<=float(line['time_ns'])<=646:data[line['method']].append(line)
for method,ls in [('deposited_uniform','-'),('SI_per_contact','--')]:
 series=data[method];t=[float(x['time_ns'])for x in series]
 for k,color,label in [('open_contact_normalized_direction',blue,'Open-specific channel'),('closed_contact_normalized_direction',orange,'Closed-specific channel')]:a.plot(t,[float(x[k])for x in series],ls=ls,color=color,lw=1.5,label=label if ls=='-'else None)
a.set_ylim(-.23,.37);a.axhline(0,color='black',lw=.7);a.set_title('E  ES17: opposing contact-channel directions',loc='left');a.set_xlabel('Time in first sustained relative event (ns)');a.set_ylabel('Reference-normalized contact direction');a.legend(fontsize=8,loc='center right');a.text(.02,.04,'Solid: uniform · Dashed: SI\nInternal disagreement: 41/42 vs 42/42 samples',transform=a.transAxes,fontsize=8)
a=ax[2,1];candidates=[x for x in rows if x['methods']['deposited_uniform']['unchanged_relative_path']['category']=='SUSTAINED_OPPOSITE_REFERENCE_PREFERENCE'];labels=[x['trajectory'].split('_')[1]for x in candidates];vals=[x['absolute_metrics']['nearest_open_MD_lid_rmsd_A']['first20_to_last20']['after_median']for x in candidates];a.axvspan(r['open_MD_leave_whole_trajectory_out_geometry_A']['q05'],r['open_MD_leave_whole_trajectory_out_geometry_A']['q95'],color=blue,alpha=.14,label='Open-run LOO geometry: 5th–95th percentiles');a.barh(labels,vals,color=orange,alpha=.85,height=.58);a.invert_yaxis();a.set_xlabel('Terminal median distance to open MD references (Å)');a.set_title('F  Candidate paths span different MD proximity',loc='left');a.legend(fontsize=7,loc='lower right')
fig.text(.065,.025,'MD references: 11 fixed samples per open run; exclude the whole query run for open LOO. The shaded range is descriptive, not a state boundary.\nRelative labels are unchanged. Contact disagreement limits complete-state interpretation. No new MD, GROMACS extraction, or optimization.',fontsize=8,color='.3')
fig.savefig(o/'absolute_paths_summary.png',dpi=180);fig.savefig(o/'absolute_paths_summary.pdf');plt.close(fig)
(p/'scripts/render_q01_absolute_paths_v1.py').write_text(Path('/tmp/q01_plot42.py').read_text());print('PNG/PDF rendered')
