from pathlib import Path
import numpy as np,json,csv,subprocess,datetime
from scipy.spatial.distance import cdist
r=Path(__file__).resolve().parents[1];groups={'CORE':np.array(list(range(0,29))+list(range(67,115))+list(range(167,214))),'NMP':np.arange(29,67),'LID':np.arange(117,160)};results={}
for state in ['open','closed']:
 a=np.loadtxt(r/f'derived/{state}_ca_raw.tsv');x=a[:,8:].reshape(-1,214,3);maps=list(csv.DictReader((r/f'derived/{state}_atom_mapping.tsv').open(),delimiter='\t'));extremes={}
 pairs=[('CORE','CORE'),('NMP','NMP'),('LID','LID'),('CORE','NMP'),('CORE','LID'),('NMP','LID')]
 for ga,gb in pairs:
  best=(-1,None,None,None)
  for k,xyz in enumerate(x):
   mat=cdist(xyz[groups[ga]],xyz[groups[gb]]);ij=np.unravel_index(mat.argmax(),mat.shape);v=float(mat[ij]);
   if v>best[0]:best=(v,k,int(groups[ga][ij[0]]),int(groups[gb][ij[1]]))
  extremes[ga+'_'+gb]={'max_A':best[0],'frame':best[1],'residues':[best[2]+1,best[3]+1]}
 spec={'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rule':'globalmaximum pair in each within-domain and interdomain block, before gmx call; allframes for each selected pair','extremes':extremes};(r/f'outputs/EXTREME_PAIR_SPEC_{state}.json').write_text(json.dumps(spec,indent=2));rp=[q['residues']for q in extremes.values()];nums=[int(maps[i-1]['index'])+1 for pair in rp for i in pair];select=' plus '.join('atomnr '+str(i)for i in nums);out=r/f'outputs/gmx_extremes_{state}.xvg';cmd=['gmx','distance','-s',str(r/f'inputs/ORADD_{state}_state.gro'),'-f',str(r/f'inputs/ORADD_{state}_state_traj.xtc'),'-nopbc','-normpbc','-select',select,'-oall',str(out)];p=subprocess.run(cmd,capture_output=True,text=True);(r/f'outputs/gmx_extremes_{state}.log').write_text(p.stdout+p.stderr);assert p.returncode==0
 vals=np.array([list(map(float,l.split()))for l in out.read_text().splitlines()if l and l[0]not in '#@']);local=np.column_stack([np.linalg.norm(x[:,i-1]-x[:,j-1],axis=1)for i,j in rp]);assert len(vals)==len(x);err=float(abs(vals[:,1:]*10-local).max());assert err<=.01
 results[state]={'status':'PASS','max_abs_error_A':err,'frames':len(x),'pairs':extremes}
(r/'outputs/EXTREME_PAIR_CROSSCHECK.json').write_text(json.dumps(results,indent=2));print({s:v['max_abs_error_A']for s,v in results.items()})
