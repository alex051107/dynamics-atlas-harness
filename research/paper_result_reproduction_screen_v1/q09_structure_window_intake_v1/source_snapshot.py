from pathlib import Path
import json,importlib.util
import numpy as np
from dynamics_atlas_harness.q09_fluorescence_v1 import linearization_reference
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'outputs/q09_structure_window_intake_v1';OUT.mkdir(exist_ok=False)
mapping=json.loads((ROOT/'outputs/q09_method_admission_v1/dataset_mapping.json').read_text());sources=json.loads((ROOT/'inputs/q09_structures/source_manifest.json').read_text())
site_ids=sorted({int(n) for v in mapping for n in v['variant'].split('-')});structures=[]
for src in sources:
 lines=(ROOT/'inputs/q09_structures'/(src['PDB']+'.pdb')).read_text().splitlines();chains={};alternates=[]
 for l in lines:
  if l.startswith('ATOM  '):
   chain=l[21];number=int(l[22:26]);insertion=l[26];res=l[17:20];name=l[12:16].strip();alt=l[16]
   if alt not in (' ','A'):alternates.append({'chain':chain,'residue':number,'atom':name,'alt':alt});continue
   chains.setdefault(chain,{}).setdefault((number,insertion),{'resname':res,'atoms':[]})['atoms'].append(name)
 chain_summaries=[]
 for chain,residues in chains.items():
  sites=[]
  for i in site_ids:
   matches=[{'insertion':key[1],**value} for key,value in residues.items() if key[0]==i]
   sites.append({'site':i,'matches':matches,'has_unique_CA_CB':len(matches)==1 and all(k in matches[0]['atoms'] for k in ('CA','CB'))})
  chain_summaries.append({'chain':chain,'residue_count':len(residues),'minimum_residue':min(k[0] for k in residues),'maximum_residue':max(k[0] for k in residues),'label_sites':sites})
 structures.append({'source':src,'headers':[l for l in lines if l.startswith(('HEADER','TITLE ','COMPND','REMARK   2'))], 'chains':chain_summaries,'nonA_alternate_atoms':alternates,'dye_label_attachment_defined':False})
windows=[]
def counts(path):
 text=path.read_text();body=text.split('Chan\tData\n')[1];a=np.array([list(map(float,l.split())) for l in body.splitlines() if l.strip()]);return a[:,1]
for variant in ['55-119','60-119']:
 base=ROOT/'inputs/q09_author/unpacked/eTCSPC'/variant;y=counts(base/(variant+'_D0.txt'));raw=counts(base/'Linearization_D0.txt');lin=linearization_reference(raw);threshold=.1*np.median(lin[lin>0]);mask=lin>threshold
 ix=np.flatnonzero(~mask);segments=np.split(ix,np.flatnonzero(np.diff(ix)!=1)+1)
 windows.append({'variant':variant,'role':'D0','raw_photons':int(y.sum()),'excluded_photons':int(y[~mask].sum()),'excluded_fraction':float(y[~mask].sum()/y.sum()),'Lin_threshold':float(threshold),
    'segments':[{'first_bin0':int(g[0]),'last_bin0':int(g[-1]),'time_ns':[float(g[0]*.0141),float(g[-1]*.0141)],'sample_photons':int(y[g].sum()),'raw_Lin_photons':int(raw[g].sum()),'maximum_sample_bin':int(y[g].max())} for g in segments if len(g)],
    'interpretation':'Observed nonzero sample counts in channels where fixed calibration-response mask excludes fit;no automatic source error or background-only verdict;do not retune mask by desiredfit'})
programs={name:importlib.util.find_spec(name) is not None for name in ['fps','mdtraj_fps','chisurf','mdtraj','MDAnalysis','labellib']}
method={'source_article':'https://www.nature.com/articles/s41467-020-14886-w','program_source':'https://github.com/Fluorescence-Tools/mdtraj_fps',
 'coordinate_references':{'172L':'open','148L':'closed'},'labeling':'pAcF donor/Alexa488 and Cys acceptor/Alexa647; actual anchor mutation and atomic attachment need source-matched method admission',
 'reported_dye_geometry_A':{'Alexa488':{'linker_length':20,'linker_width':4.5,'radii':[5,4.5,1.5]},'Alexa647':{'linker_length':22,'linker_width':4.5,'radii':[11,3,3.5]}},
 'ACV_contact_layer_A':3,'contact_population':'site-specific residual/fundamental anisotropy; values and mapping not yet admitted',
 'observable':'Compare source-defined mean pairwise dye distance for eTCSPC;not CA distance,not distance ofmean dye positions,not automaticallyefficiency-equivalentdistance',
 'problems':['No installed source-matched AV/ACV executable or dependencies','ExactoriginalFPSversion/attachmentatom mutations/grid/residue/siteanisotropy mapping not fully admitted','Two-column currentMD mixes geometry/density equations;returntoPDF beforeencodingequation'],
 'first_structure_FRET_predictions':0,'installed_programs':programs,'dependencies_installed':False}
for name,obj in [('structures.json',structures),('window_exclusions.json',windows),('dye_forward_method_admission.json',method)]:
 (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
(OUT/'source_snapshot.py').write_text(Path(__file__).read_text())
print(json.dumps({'structures':[{'id':s['source']['PDB'],'chains':[(c['chain'],c['residue_count'],all(x['has_unique_CA_CB'] for x in c['label_sites'])) for c in s['chains']]} for s in structures],'windows':windows,'programs':programs},indent=2))
