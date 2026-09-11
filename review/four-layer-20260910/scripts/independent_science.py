from pathlib import Path
import numpy as np,json,statistics
from scipy.spatial.distance import cdist
w=Path.cwd();r=Path(__file__).resolve().parents[1];a=w/'autoresearch/tasks/dynamics_atlas_adk_plain_agent_v2_20260910';g={'CORE':np.array(list(range(29))+list(range(67,115))+list(range(167,214))),'NMP':np.arange(29,67),'LID':np.arange(117,160)};out={}
for state in ['open','closed']:
 raw=np.loadtxt(a/f'derived/{state}_ca_raw.tsv');xyz=raw[:,8:].reshape(-1,214,3);tab=np.genfromtxt(a/f'derived/{state}_domain_distances.tsv',names=True,delimiter='\t');n=len(tab);k=n//10;checks={}
 for dom in ['NMP','LID']:
  val=np.array([cdist(x[g[dom]],x[g['CORE']]).mean()for x in xyz]);err=float(abs(val-tab[f'{dom}_CORE_mean_CA_distance_A']).max());assert err<1e-10
  first=statistics.fmean(val[:k]);last=statistics.fmean(val[-k:]);checks[dom]={'first_mean_A':first,'last_mean_A':last,'delta_A':last-first,'median_A':float(np.median(val)),'q05_A':float(np.quantile(val,.05)),'q95_A':float(np.quantile(val,.95)),'max_table_difference_A':err}
 out[state]={'frames':n,'window_n':k,'time_ns':[float(tab['time_ns'][0]),float(tab['time_ns'][-1])],'domains':checks}
(r/'outputs/ADK_INDEPENDENT_RECOMPUTE.json').write_text(json.dumps({'status':'PASS','method':'SciPy cdist independent implementation on original extracted CA; statistics.fmean windows; original derives numpy broadcasting','results':out},indent=2));print('ADK independent whole-chain pair means PASS')
