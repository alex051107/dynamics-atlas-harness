from pathlib import Path
import json,csv,shutil,hashlib,datetime,copy
w=Path.cwd();r=Path(__file__).resolve().parents[1];s=r.parent;adk=w/'autoresearch/tasks/dynamics_atlas_adk_plain_agent_v2_20260910';dh=w/'autoresearch/tasks/dynamics_atlas_adk_plain_agent_v1_20260910';hs=w/'autoresearch/tasks/dynamics_atlas_hsp90_first_round_v3_20260910/cases/HSP90_Q01/common'
base=r/'E1a';(base/'reference').mkdir(parents=True,exist_ok=True);(base/'packets').mkdir(exist_ok=True)
for name,files,unit,timecol,role,pool in [('HSP90',[hs/'frame_state_assignments.tsv'],'Angstrom','time_ns','fitted_reference_reused_for_diagnostic','Henot2022 refinedNMRseed40'),('DHFR',sorted((dh/'derived_mic').glob('*_distances.tsv')),'Angstrom','frame_index','simulation_diagnostic_with_external_experiment_context','Cetin2023 4conditions n1each'),('ADK',sorted((adk/'derived').glob('*_domain_distances.tsv')),'Angstrom','time_ns','simulation_diagnostic_with_experiment_context','Zenodo5583119 twoinitialstates')]:
 ref=base/'reference'/name;p=base/'packets'/('clean_'+name);(ref/'data').mkdir(parents=True,exist_ok=True);(p/'data').mkdir(parents=True,exist_ok=True);tables=[]
 for f in files:
  shutil.copy2(f,ref/'data'/f.name);shutil.copy2(f,p/'data'/f.name);rows=list(csv.DictReader(f.open(),delimiter='\t'));tables.append({'file':'data/'+f.name,'rows':len(rows),'time_column':timecol,'unit':unit,'condition':f.stem,'statistical_unit':'trajectory','independent_replicates':1,'time_group':'trajectory'if name=='HSP90'else None,'candidate_pool':pool})
 meta={'system':name,'tables':tables,'evidence_role':role,'candidate_pool':pool,'source_authority':('Henot2022 Methods lines549–557 and628; refined NMR seeds are not independent of NOE reference'if name=='HSP90'else'Cetin2023 deposited filenames PSF identity and independent VMD PBC validation'if name=='DHFR'else'Oradd2021 Zenodo5583119; native header and whole-chain admission'),'physical_representation':('project scalar/residual; no MIC decision'if name=='HSP90'else'nearest-periodic-ligand atom to specified protein atom; prior VMD independent reference'if name=='DHFR'else'whole contiguous intramolecular CA; no MIC'),'reference_tolerance_A':.0001 if name=='DHFR'else .01}
 (ref/'SOURCE_AUTHORITY.json').write_text(json.dumps(meta,indent=2));(p/'DECLARED_METADATA.json').write_text(json.dumps(meta,indent=2))
 if name=='DHFR':shutil.copy2(dh/'outputs/PBC_VALIDATION.json',ref/'PHYSICAL_SOURCE_CHECK.json')
 if name=='ADK':shutil.copy2(adk/'outputs/FOUR_STANDARD_PHYSICAL_ADMISSION.json',ref/'PHYSICAL_SOURCE_CHECK.json')
mutations=[]
for num,source in [(1,'DHFR'),(2,'ADK'),(3,'ADK'),(4,'ADK'),(5,'DHFR'),(6,'HSP90')]:
 dest=base/'packets'/f'defect_{num}';shutil.copytree(base/'packets'/('clean_'+source),dest,dirs_exist_ok=True);mp=dest/'DECLARED_METADATA.json';meta=json.loads(mp.read_text());f=dest/meta['tables'][0]['file'];description=''
 if num==1:
  for q in (dest/'data').glob('*.tsv'):shutil.copy2(dh/'cases/DHFR_Q01/common/data'/q.name,q)
  description='Original wrapped-coordinate protein-ligand distance arrays replace corrected arrays; raw original preserved'
 elif num==2:meta['tables'][0]['unit']='nm';description='Only declared unit changed Angstrom to nm; numerical array unchanged'
 elif num==3:
  lines=f.read_text().splitlines();f.write_text('\n'.join(lines[:-20])+'\n');description='Remove last20saved rows; declared/source count unchanged'
 elif num==4:
  lines=f.read_text().splitlines();rows=[x.split('\t')for x in lines];ix=rows[0].index('time_ns');rows[11][ix],rows[12][ix]=rows[12][ix],rows[11][ix];f.write_text('\n'.join('\t'.join(x)for x in rows)+'\n');description='Exchange adjacent timestamps only, rows11 and12; coordinate-derived values unchanged'
 elif num==5:meta['tables'][0]['condition'],meta['tables'][1]['condition']=meta['tables'][1]['condition'],meta['tables'][0]['condition'];description='Swap two condition labels, arrays unchanged'
 elif num==6:meta['evidence_role']='independent_validation';description='Label fitted/reused NMR reference as independent validation; authority remains source Methods'
 mp.write_text(json.dumps(meta,indent=2));mutations.append({'packet':dest.name,'source':source,'single_mutation':description,'expected_defect':True})
plan={'freeze_time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'clean':['clean_HSP90','clean_DHFR','clean_ADK'],'defects':mutations,'success':'>=5/6 defects including realperiodic01;0/3 falsepositives','scope':'Consistency with independently curated source authority and validated numerical reference; not autonomous literature interpretation','hidden_reference_not_in_agent_workspace':True}
(base/'E1_PLANTED_DEFECTS.json').write_text(json.dumps(plan,indent=2));print('3clean6defect prepared; no checker outcomes read')
