from pathlib import Path
import json,csv,collections
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parents[1];O=B/'outputs';F=O/'report/figures';F.mkdir(exist_ok=True)
def read(n):return list(csv.DictReader((B/'inputs'/n).open(),delimiter='\t'))
frames=read('frame_state_assignments.tsv');anatomy=read('trajectory_time_anatomy.tsv');by=collections.defaultdict(list)
for x in frames:by[x['trajectory']].append(x)
meta={x['trajectory']:x['seed_lineage'] for x in anatomy};arrays={};diff=0
for tr,rows in by.items():
 vo=np.loadtxt(B/'inputs'/tr/'open_contact_violation.dat');vc=np.loadtxt(B/'inputs'/tr/'closed_contact_violation.dat');tm=np.array([float(x['time_ns']) for x in rows]);g=np.array([float(x['geometry_delta_A']) for x in rows]);m=np.array([float(x['contact_margin_A']) for x in rows]);assert vo.shape[0]==vc.shape[0]==1001
 assert np.array_equal(vo[:,0],np.arange(1,1002)) and np.array_equal(vc[:,0],vo[:,0]) and np.array_equal(tm,np.arange(20,1021))
 err=np.max(np.abs(m-(vc[:,2]-vo[:,2])));diff=max(diff,float(err));assert err<1e-8
 arrays[tr]=(tm,vo[:,1],vc[:,1],(g>0)&(m>0))
p95=float(np.quantile(np.concatenate([a[1] for tr,a in arrays.items() if meta[tr]=='open_seeded']),.95))
def first_run(mask,start=0):
 count=0
 for i in range(start,len(mask)):
  count=count+1 if mask[i] else 0
  if count==50:return i-49
 return None
def partition(tr,k):
 x=next(x for x in anatomy if x['trajectory']==tr and int(x['persistence_saved_frames'])==k)
 return 'FIRST_OPEN' if x['first_persistent_direction']=='OPEN_CONSENSUS' else ('CLOSED_THEN_OPEN' if x['opposite_direction_departure_candidate']=='True' else ('ONLY_CLOSED' if x['first_persistent_direction']=='CLOSED_CONSENSUS' else 'NONE'))
per=[];perframe=[];sensitivity={};classes=['OPEN_NOE','CLOSED_NOE','BOTH_FAR','BOTH_NEAR']
for tau in [.5,1.,2.]:
 results=[]
 for tr,(tm,vo,vc,direction) in arrays.items():
  cls=np.where((vo<=tau)&(vc>tau),'OPEN_NOE',np.where((vc<=tau)&(vo>tau),'CLOSED_NOE',np.where((vo>tau)&(vc>tau),'BOTH_FAR','BOTH_NEAR')))
  cond={c:float(np.mean(cls[direction]==c)) if direction.any() else None for c in classes}
  judgment='NOT_APPLICABLE' if not direction.any() else ('AGREEMENT' if cond['OPEN_NOE']>=.8 else ('RELATIVE_ONLY' if cond['BOTH_FAR']>=.5 else 'PARTIAL'))
  entry=first_run(vo<=p95);leave=first_run(vo>p95,entry+50) if entry is not None else None
  row=dict(trajectory=tr,seed_lineage=meta[tr],partition_5=partition(tr,5),partition_50=partition(tr,50),open_direction_fraction=float(direction.mean()),judgment=judgment,first_reference_entry_ns=None if entry is None else float(tm[entry]),subsequent_reference_exit_ns=None if leave is None else float(tm[leave]),first100_Vopen_mean=float(vo[:100].mean()),last100_Vopen_mean=float(vo[-100:].mean()),first100_Vclosed_mean=float(vc[:100].mean()),last100_Vclosed_mean=float(vc[-100:].mean()))
  row.update({c+'_fraction':float(np.mean(cls==c)) for c in classes});row.update({'within_direction_'+c:v for c,v in cond.items()});results.append(row)
  if tau==1.:
   for i in range(len(tm)):perframe.append(dict(trajectory=tr,time_ns=tm[i],V_open_A=vo[i],V_closed_A=vc[i],open_direction=bool(direction[i]),native_class=cls[i]))
 sensitivity[str(tau)]={group:dict(collections.Counter(x['judgment'] for x in results if x['seed_lineage']==group)) for group in ['closed_seeded','open_seeded']}
 if tau==1.:per=results
for name,rows in [('per_frame_native_class.tsv',perframe),('per_trajectory_crosswalk.tsv',per)]:
 with (O/name).open('w') as f:a=csv.DictWriter(f,list(rows[0]),delimiter='\t');a.writeheader();a.writerows(rows)
control=sensitivity['1.0']['open_seeded'].get('AGREEMENT',0)>=18
summary=dict(frame_rows=len(perframe),trajectory_rows=len(per),tau_primary_A=1.,p95_open_A=p95,max_margin_alignment_error=diff,positive_control_pass=control,sensitivity=sensitivity,reference_entry_counts={g:sum(x['first_reference_entry_ns'] is not None for x in per if x['seed_lineage']==g) for g in ['closed_seeded','open_seeded']},claim_ceiling='Same-source decomposition, not independent experimental validation; tau is a project tolerance',interpretation_status='CONTINUE' if control else 'STOP_CONTROL_FAILED')
(O/'group_summary.json').write_text(json.dumps(summary,indent=2))
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
fig,axs=plt.subplots(3,1,figsize=(10,8),sharex=True)
for ax,short in zip(axs,['ES15','ES03','ES01']):
 tr=next(t for t in arrays if '_'+short+'_' in t);tm,vo,vc,direction=arrays[tr];ax.plot(tm,vo,label='Open NOE violation',color='#087E8B');ax.plot(tm,vc,label='Closed NOE violation',color='#CA683F');ax.axhline(1,color='gray',ls=':',label='Project tolerance 1 A');ax.fill_between(tm,0,1,where=direction,transform=ax.get_xaxis_transform(),alpha=.12,color='#087E8B');ax.set(title=short,ylabel='Mean violation (A)')
axs[0].legend(ncol=3,fontsize=8);axs[-1].set_xlabel('Time (ns)');fig.tight_layout();fig.savefig(F/'native_examples.png',dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(7,5));markers={'FIRST_OPEN':'o','CLOSED_THEN_OPEN':'s','ONLY_CLOSED':'^','NONE':'x'}
for x in per:ax.scatter(x['open_direction_fraction'],x['OPEN_NOE_fraction'],marker=markers[x['partition_5']],c='#087E8B' if x['seed_lineage']=='open_seeded' else '#CA683F',s=48,alpha=.7)
ax.plot([0,1],[0,1],ls=':',c='gray');ax.set(xlabel='Fraction with open direction',ylabel='Fraction OPEN_NOE (tau = 1 A)',title='Relative direction versus absolute tolerance');fig.tight_layout();fig.savefig(F/'native_scatter.png',dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(8,4));groups=['FIRST_OPEN','CLOSED_THEN_OPEN','ONLY_CLOSED'];mat=np.array([[np.mean([x[c+'_fraction'] for x in per if x['seed_lineage']=='closed_seeded' and x['partition_5']==g]) for c in classes] for g in groups]);im=ax.imshow(mat,vmin=0,vmax=1,cmap='Blues');ax.set_xticks(range(4),classes);ax.set_yticks(range(3),groups)
for i in range(3):
 for j in range(4):ax.text(j,i,f'{mat[i,j]:.2f}',ha='center',va='center',color='white' if mat[i,j]>.5 else 'black')
fig.colorbar(im,ax=ax,label='Mean trajectory fraction');fig.tight_layout();fig.savefig(F/'native_heatmap.png',dpi=220);plt.close(fig)
print(json.dumps(summary,indent=2))
