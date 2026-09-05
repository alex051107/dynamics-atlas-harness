"""All33variant source/likelihood ownership; no fitting and no inferred exchangeability."""
from pathlib import Path
from collections import Counter
import json,zipfile
import numpy as np
from dynamics_atlas_harness.q09_fluorescence_v1 import linearization_reference
ROOT=Path(__file__).resolve().parents[1];SOURCE=ROOT/'inputs/q09_author/unpacked/eTCSPC';OUT=ROOT/'outputs/q09_global_ownership_v1'


def parse(raw,kind,dt):
    lines=raw.decode().splitlines()
    ibh=lines[0].startswith('Item name:')
    if ibh:lines=lines[lines.index('Chan\tData')+1:]
    a=np.array([list(map(float,l.split())) for l in lines if l.strip()]);assert a.shape[1]==2
    if ibh:assert kind=='IBH' and np.array_equal(a[:,0],np.arange(len(a))+1)
    else:assert kind=='PQ' and abs(a[0,0])<1e-12 and np.allclose(np.diff(a[:,0]),dt,rtol=0,atol=1e-10)
    assert np.all(np.isfinite(a)) and np.all(a[:,1]>=0) and np.all(a[:,1]==np.floor(a[:,1]))
    return a[:,1]


def main():
    OUT.mkdir(exist_ok=False)
    mapping=json.loads((ROOT/'outputs/q09_method_admission_v1/dataset_mapping.json').read_text());cache={}
    with zipfile.ZipFile(ROOT/'inputs/q09_author/eTCSPC_wildtype.zip') as z:
        paths=sorted({v['metadata'] for v in mapping}|{d[k] for v in mapping for d in v['datasets'] for k in ['decay','irf','linearization'] if d[k]})
        for name in paths:
            raw=(SOURCE/name).read_bytes();assert raw==z.read('eTCSPC/'+name),name;cache[name]=raw
    # Direct byte identity avoids recomputing historical source hashes.
    pools={k:[] for k in ['DA','D0','IRF','Lin']}
    def own(kind,path):
        if path is None:return None
        for i,g in enumerate(pools[kind]):
            if cache[g[0]]==cache[path]:
                if path not in g:g.append(path)
                return f'{kind}_{i+1:02d}'
        pools[kind].append([path]);return f'{kind}_{len(pools[kind]):02d}'
    rows=[]
    for v in mapping:
        for d in v['datasets']:
            y=parse(cache[d['decay']],d['instrument'],d['bin_width_ns']);h=parse(cache[d['irf']],d['instrument'],d['bin_width_ns']);assert y.shape==h.shape
            if d['linearization']:
                linear=parse(cache[d['linearization']],d['instrument'],d['bin_width_ns']);assert linear.shape==y.shape
                lin=linearization_reference(linear);mask=lin>.1*np.median(lin[lin>0])
            else:mask=np.ones(len(y),bool)
            baseline=float(np.median(h[np.flatnonzero(mask)[-256:]]))
            metadata=cache[v['metadata']].decode().split('Setup parts:',1)[0]
            rows.append({'variant':v['variant'],'role':d['role'],'sample_name':v['sample_name'],'metadata':v['metadata'],
                         'source':d,'decay_record':own(d['role'],d['decay']),'IRF_record':own('IRF',d['irf']),'Lin_record':own('Lin',d['linearization']),
                         'native_bins':len(y),'valid_bins_under_existing_conditional_mask':int(mask.sum()),'valid_first_bin':int(np.flatnonzero(mask)[0]),'valid_last_bin':int(np.flatnonzero(mask)[-1]),
                         'raw_photons':int(y.sum()),'retained_photons':int(y[mask].sum()),'excluded_photons':int(y[~mask].sum()),'IRF_tail_median':baseline,
                         'metadata_measurement_section':metadata,'reference_exchangeability':'UNKNOWN; byteidentity does not establish biological response transfer'})
    byref={}
    for r in rows:
        if r['role']=='D0':byref.setdefault(r['decay_record'],[]).append(r)
    refs=[]
    for key,rs in byref.items():
        methods={(r['IRF_record'],r['Lin_record'],r['source']['instrument'],r['source']['bin_width_ns'],r['valid_first_bin'],r['valid_last_bin']) for r in rs}
        refs.append({'record_id':key,'likelihood_multiplicity':1,'owners':[r['variant'] for r in rs],'source_paths':[r['source']['decay'] for r in rs],
                     'raw_photons':rs[0]['raw_photons'],'retained_photons':rs[0]['retained_photons'],'instrument_method_alternatives':len(methods),
                     'status':'CONDITIONAL_UNIQUE_REFERENCE' if len(methods)==1 else 'SAME_RECORD_CONFLICTING_INSTRUMENT_CONTEXT',
                     'response_transfer_to_distinct_mutants':'UNKNOWN' if len(rs)>1 else 'SINGLE_PAIR_JOINT_DONOR_RESPONSE_ASSUMPTION'})
    assert len(mapping)==33 and len(rows)==66 and len(refs)==27 and len(pools['DA'])==33
    raw_dup=sum(r['raw_photons'] for r in rows);raw_unique=sum(r['raw_photons'] for r in rows if r['role']=='DA')+sum(r['raw_photons'] for r in refs)
    summary={'status':'SOURCE_LIKELIHOOD_OWNERSHIP_CONDITIONAL_NOT_FITTED','variants':33,'role_paths':66,'original_files_compared_to_ZIP':len(paths),
             'DA_likelihood_terms':33,'D0_likelihood_terms':27,'total_unique_likelihood_terms':60,'raw_photons_unique_records':raw_unique,
             'raw_photons_if_66_paths_wrongly_counted_independently':raw_dup,'duplicated_reference_photons':raw_dup-raw_unique,
             'unique_calibration_records':{k:len(pools[k]) for k in ['IRF','Lin']},'role_instruments':dict(Counter(r['source']['instrument'] for r in rows)),
             'reference_context_conflicts':[r for r in refs if r['instrument_method_alternatives']>1],
             'conditional_source_aliases':[{'variant':r['variant'],'role':r['role'],'exception':r['source']['original_irf_reference_exception']} for r in rows if r['source']['original_irf_reference_exception']],
             'nonzero_excluded_sample_photons':[{'variant':r['variant'],'role':r['role'],'excluded_photons':r['excluded_photons']} for r in rows if r['excluded_photons']],
             'shared_reference_groups':[r for r in refs if len(r['owners'])>1],
             'optimizer_calls':0,'Rules_runs':0,'full_scientific_answers':0}
    contract={'source_locator':'Source-matched SI Markdown lines3323-3334, physical page59, previously visuallychecked SI59','models':['K2_local_populations','K2_shared_populations','K3_shared_populations'],
              'comparability':'Same60 unique likelihoodrecords, role-specific bins/calibration/nuisance assumptions anddonororder acrosscomparands;allmodel-specificfailuresretained',
              'common_donor_latent':'One fitted donorresponseperuniqueD0record,sharedconditionallywithitsDAowners before eachindividualIRF convolution;single D0likelihood notonceperowner',
              'local_parameters':['DA distance means','DA donor-only coefficient','per unique observed record background andshift'],
              'population_parameters':'K2localonepervariant;K2sharedonescalar;K3sharedtwosimplexcoordinates. Noauthorfittedfractions.',
              'labels':'No distance sorting toassert proteinstate correspondence; componentpermutations/structuralidentification mustremainexplicit',
              'calibration':'Share eachbyte-identicalIRF/Lin realization acrossallrecordowners,distinctfromlatentdonorresponseexchangeability;calibration sensitivitynotyetpropagatedglobally',
              'remaining_admission':['19-86 crossinstrumentlatentresponse transfer conditional','duplicateD0reference biologicalexchangeability unknown','instrument/model adequacy outside22-127 untested','conditional fitbounds,startsandbudget mustfreeze beforefit','globalpopulationlabel/structuremapping unresolved'],
              'scientific_stop':'No proteinstate supportfrom optimizedlowerloss;needadequacy,conditionalmodelcomparison,identifiability andstructure evidence',
              'not_solver_input':'Authorfinalparameters/populations, localmanualobligations, paperanswer'}
    for name,obj in [('records.json',rows),('reference_ownership.json',refs),('calibration_ownership.json',pools),('summary.json',summary),('conditional_comparison_contract.json',contract)]:
        (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
    (OUT/'source_snapshot.py').write_text(Path(__file__).read_text())
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
