import pandas as pd, numpy as np, os
files=['tmpp-wt','d4tmpp-wt','tmpp-l28r','d4tmpp-l28r']
D={x:pd.read_csv('/source/data/'+x+'_distances.tsv',sep='\t').query('frame_index>=11') for x in files}
# print selected means/fractions
for g in ['wt','l28r']:
 print('\nGEN',g)
 for r in ['r18_O','r20_N','r22_O','r49_O','r52_NH1','r52_NH2'] + (['r28_NE','r28_NH1','r28_NH2'] if g=='l28r' else []):
  print(r,end=': ')
  for x in [('tmpp-'+g),('d4tmpp-'+g)]:
   cols=[c for c in D[x] if c.startswith(r+'_')]
   vals=D[x][cols].to_numpy().ravel(); print(x.split('-')[0], 'mean %.2f minpair %s frac<6 %.1f%% frac<3.2 %.1f%%'%(vals.mean(), ','.join(f'{c.split("_")[-1]}={D[x][c].mean():.2f}' for c in cols),100*(vals<6).mean(),100*(vals<3.2).mean()),end='; ')
  print()
# exact pair means and fraction changes for M20 and R28
for x in files:
 print('\n',x)
 for c in D[x].columns[1:]:
  if c.startswith('r20_') or c.startswith('r28_'): print(c, 'mean',round(D[x][c].mean(),3),'sd',round(D[x][c].std(),3),'lt6',round((D[x][c]<6).mean()*100,1),'lt3.2',round((D[x][c]<3.2).mean()*100,1))
