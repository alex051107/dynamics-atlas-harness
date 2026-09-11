from pathlib import Path
import numpy as np,json,csv
root=Path(__file__).resolve().parents[1];core=np.array([r-1 for r in list(range(1,30))+list(range(68,116))+list(range(168,215))]);domains={'NMP':np.arange(29,67),'LID':np.arange(117,160)};results={}
for state in ['open','closed']:
 a=np.loadtxt(root/f'derived/{state}_ca_raw.tsv');box=a[:,2:5];raw=a[:,8:].reshape(len(a),214,3);headers=np.loadtxt(root/f'derived/{state}_native_xtc_headers.tsv');inc=np.diff(raw,axis=1);inc-=box[:,None,:]*np.round(inc/box[:,None,:]);whole=np.concatenate([raw[:,:1,:],raw[:,:1,:]+np.cumsum(inc,axis=1)],axis=1)
 best={'distance_A':0};breaches=0
 for i,xyz in enumerate(whole):
  for domain,ix in domains.items():
   delta=xyz[ix,None,:]-xyz[core][None,:,:];delta-=box[i]*np.round(delta/box[i]);dist=np.linalg.norm(delta,axis=-1);breaches+=int(np.any(dist>box[i].min()/2))
   if dist.max()>best['distance_A']:
    j,k=np.unravel_index(dist.argmax(),dist.shape);best={'frame':i,'time_ps':float(headers[i,1]),'domain':domain,'residue1':int(ix[j]+1),'residue2':int(core[k]+1),'distance_A':float(dist[j,k]),'minimum_image_delta_A':delta[j,k].tolist(),'box_A':box[i].tolist(),'half_min_box_A':float(box[i].min()/2)}
 mapping={int(x['resid']):int(x['index'])+1 for x in csv.DictReader((root/f'derived/{state}_atom_mapping.tsv').open(),delimiter='\t')}
 best['gromacs_atom1']=mapping[best['residue1']];best['gromacs_atom2']=mapping[best['residue2']];results[state]={'worst_minimum_image_pair':best,'breach_frame_domain_count':breaches,'interpretation':'Euclidean vector length can exceed half box while each minimum-image component stays within half its cell edge; half-box radial bound is not a universal validity test.'}
(root/'outputs/HALF_BOX_GATE_DIAGNOSIS.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
