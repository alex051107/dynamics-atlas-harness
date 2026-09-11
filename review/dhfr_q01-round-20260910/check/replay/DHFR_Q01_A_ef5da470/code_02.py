import pandas as pd, numpy as np, glob, os
files=glob.glob('/source/data/*distances.tsv')
# selected all columns stats means sd and fraction thresholds
for f in sorted(files):
 d=pd.read_csv(f,sep='\t').set_index('frame_index').loc[11:1000]
 print('\n',os.path.basename(f),'n',len(d))
 for c in d.columns:
  print(f'{c}: mean {d[c].mean():.3f} sd {d[c].std(ddof=1):.3f} med {d[c].median():.3f} p<6 {np.mean(d[c]<6):.3f} p<3.2 {np.mean(d[c]<3.2):.3f}')
# differences for key M20, N18,W22 and R28, paired framewise d4-tmp
for res in ['r18_O','r20_N','r22_O']:
 print('\nDELTA',res)
 for c in [x for x in pd.read_csv(files[0],sep='\t').columns if x.startswith(res)]:
  vals=[]
  for sys in ['wt','l28r']:
   a=pd.read_csv(f'/source/data/tmpp-{sys}_distances.tsv',sep='\t').set_index('frame_index').loc[11:1000,c]
   b=pd.read_csv(f'/source/data/d4tmpp-{sys}_distances.tsv',sep='\t').set_index('frame_index').loc[11:1000,c]
   vals.append((sys,b.mean()-a.mean(),np.mean(b<6)-np.mean(a<6)))
  print(c, vals)
print('\nR28 delta L28R d4-tmp')
for c in [x for x in pd.read_csv('/source/data/tmpp-l28r_distances.tsv',sep='\t').columns if x.startswith('r28')]:
 a=pd.read_csv('/source/data/tmpp-l28r_distances.tsv',sep='\t').set_index('frame_index').loc[11:1000,c];b=pd.read_csv('/source/data/d4tmpp-l28r_distances.tsv',sep='\t').set_index('frame_index').loc[11:1000,c]
 print(c, 'TMP %.3f %.3f %.3f'%(a.mean(),np.mean(a<6),np.mean(a<3.2)), 'D4 %.3f %.3f %.3f'%(b.mean(),np.mean(b<6),np.mean(b<3.2)), 'delta %.3f'%(b.mean()-a.mean()))