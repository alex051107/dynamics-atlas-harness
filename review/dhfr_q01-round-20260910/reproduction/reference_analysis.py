import csv,json
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parents[1]; rows=[]; values={}
for p in sorted((root/'derived').glob('*_distances.tsv')):
 sys=p.stem.replace('_distances','');x=np.genfromtxt(p,names=True,delimiter='\t');assert len(x)==1001
 assert np.array_equal(x['frame_index'],np.arange(1001))
 for col in x.dtype.names[1:]:
  v=x[col][11:];assert np.all(np.isfinite(v)) and np.all(v>0)
  row={'system':sys,'atom_pair':col,'n_frames':len(v),'mean_A':float(v.mean()),'sd_A':float(v.std(ddof=0)),'min_A':float(v.min()),'max_A':float(v.max()),'full_mean_A':float(x[col].mean())};rows.append(row);values[sys,col]=row
out=root/'outputs';(out/'reference_statistics.json').write_text(json.dumps(rows,indent=2))
with (out/'distance_summary.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
comparisons=[]
for variant in ['wt','l28r']:
 for col in sorted({c for s,c in values if s=='tmpp-'+variant}):
  t=values['tmpp-'+variant,col];d=values['d4tmpp-'+variant,col];comparisons.append({'variant':variant,'atom_pair':col,'TMP_mean_A':t['mean_A'],'4DTMP_mean_A':d['mean_A'],'delta_4DTMP_minus_TMP_A':d['mean_A']-t['mean_A']})
(out/'ligand_comparison.json').write_text(json.dumps(comparisons,indent=2))
print(json.dumps([r for r in comparisons if r['atom_pair'] in ['r18_O_O3P','r20_N_O3P','r22_O_O3P'] or r['atom_pair'].startswith('r28_')],indent=2))
