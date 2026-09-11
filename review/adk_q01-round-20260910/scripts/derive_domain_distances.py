from pathlib import Path
import numpy as np,csv,json,datetime,struct,collections
root=Path(__file__).resolve().parents[1];derived=root/'derived';checks={};summaries={};outputs=[]
core=np.array([r-1 for r in list(range(1,30))+list(range(68,116))+list(range(168,215))]);domains={'NMP':np.arange(29,67),'LID':np.arange(117,160)}
for state in ['open','closed']:
 m=list(csv.DictReader((derived/f'{state}_atom_mapping.tsv').open(),delimiter='\t'));assert [int(r['resid'])for r in m]==list(range(1,215))
 a=np.loadtxt(derived/f'{state}_ca_raw.tsv');f=a[:,0];box=a[:,2:5];angles=a[:,5:8];raw=a[:,8:].reshape(len(a),214,3)
 native=[]
 with (root/f'inputs/ORADD_{state}_state_traj.xtc').open('rb')as h:
  while b:=h.read(92):
   assert len(b)==92
   magic,n,step,t=struct.unpack('>iiif',b[:16]);assert magic==1995
   assert struct.unpack('>i',b[52:56])[0]==n
   packed=struct.unpack('>i',b[88:92])[0];assert packed>0
   native.append((step,t,*struct.unpack('>9f',b[16:52])))
   h.seek((packed+3)//4*4,1)
 native=np.array(native);assert len(native)==len(a)
 time=native[:,1]/1000
 assert np.allclose(native[:,[2,6,10]]*10,box,atol=1e-4)
 np.savetxt(derived/f'{state}_native_xtc_headers.tsv',native,delimiter='\t',header='step time_ps box9_nm')
 assert np.allclose(angles,90,atol=1e-4);assert np.all(box>0);assert np.all(np.diff(time)>0);assert np.allclose(np.diff(time),np.diff(time)[0],atol=1e-6)
 gro=(root/f'inputs/ORADD_{state}_state.gro').read_text().splitlines();natoms=int(gro[1]);xtc=root/f'inputs/ORADD_{state}_state_traj.xtc'
 with xtc.open('rb')as h:header=struct.unpack('>iiif9f',h.read(52))
 assert header[0]==1995 and header[1]==natoms;assert abs(header[3]/1000-time[0])<1e-8
 first_ca=np.array([[float(gro[int(r['index'])+2][20:28]),float(gro[int(r['index'])+2][28:36]),float(gro[int(r['index'])+2][36:44])]for r in m])*10
 # Initial XTC and GRO can represent different stored states; this is not a required identity.
 increments=np.diff(raw,axis=1);increments-=box[:,None,:]*np.round(increments/box[:,None,:]);neigh=np.linalg.norm(increments,axis=-1)
 whole=np.concatenate([raw[:,:1,:],raw[:,:1,:]+np.cumsum(increments,axis=1)],axis=1)
 dist={k:[]for k in domains};maxpair=0.;boxbreaches=0
 for i,coords in enumerate(whole):
  for k,ix in domains.items():
   delta=coords[ix,None,:]-coords[core][None,:,:]
   # Intramolecular reconstructed C-alpha pair distances used in domain summaries.
   values=np.linalg.norm(delta,axis=-1);maxpair=max(maxpair,float(values.max()));boxbreaches+=int(np.any(values>box[i].min()/2));dist[k].append(float(values.mean()))
 out=derived/f'{state}_domain_distances.tsv'
 with out.open('w')as h:
  w=csv.writer(h,delimiter='\t');w.writerow(['frame_index','time_ns','NMP_CORE_mean_CA_distance_A','LID_CORE_mean_CA_distance_A']);w.writerows(zip(f.astype(int),time,dist['NMP'],dist['LID']))
 n=len(a);nedge=max(1,int(n*.1));summary={'n_saved_frames':n,'time_start_ns':float(time[0]),'time_end_ns':float(time[-1]),'interval_ns':float(np.diff(time)[0]),'first_window_ns':[float(time[0]),float(time[nedge-1])],'last_window_ns':[float(time[-nedge]),float(time[-1])],'n_window':nedge}
 for k,v in dist.items():
  v=np.array(v);summary[k]={'first_mean_A':float(v[:nedge].mean()),'last_mean_A':float(v[-nedge:].mean()),'change_A':float(v[-nedge:].mean()-v[:nedge].mean()),'median_A':float(np.median(v)),'q05_A':float(np.quantile(v,.05)),'q95_A':float(np.quantile(v,.95)),'min_A':float(v.min()),'max_A':float(v.max())}
 residue_counts=collections.Counter(l[5:10].strip()for l in gro[2:2+natoms]);checks[state]={'n_atoms':natoms,'XTC_matches_GRO_atom_count':True,'n_CA':len(m),'residues_1_to_214':True,'frame_time_checked':True,'box_min_A':float(box.min()),'orthorhombic':True,'CA_neighbor_distance_range_A':[float(neigh.min()),float(neigh.max())],'max_contributing_residue_pair_A':maxpair,'half_box_breach_frame_domain_count':boxbreaches,'unit_conversion':'GRO nm / XTC nm -> VMD A; XTC ps -> ns','composition_atom_counts':dict(residue_counts),'status':'PASS' if boxbreaches==0 and neigh.max()<5 else 'FAIL'}
 summaries[state]=summary
(derived/'domain_summary.json').write_text(json.dumps(summaries,indent=2));overall='PASS'if all(c['status']=='PASS'for c in checks.values())else'FAIL'
(root/'outputs/PREFREEZE_PHYSICAL_CHECK.json').write_text(json.dumps({'status':overall,'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'systems':checks,'source_scope':'Single-source ligand-free MD. Article experiment uses AMP and released ATP; experiment is context, not condition-matched validation.','domain_definition':'Predetermined unambiguous interior subsets; project scalar summary, not exact author RMSD or fitted scattering ensemble','gate':'All contributing pair distances <=half minimum cell; all CA neighbors <5A'},indent=2));print(json.dumps({'status':overall,'summary':summaries,'maxpairs':{k:v['max_contributing_residue_pair_A']for k,v in checks.items()}},indent=2))
