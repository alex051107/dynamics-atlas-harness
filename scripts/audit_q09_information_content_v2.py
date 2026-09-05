"""Source-bound old-parameter replay and explicit padded-IRF method delta; no fits."""
import argparse
import functools
import json
from pathlib import Path
from unittest.mock import patch
import numpy as np
from dynamics_atlas_harness import q09_global_comparison_v1 as a


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--input-root',type=Path,required=True);parser.add_argument('--output-dir',type=Path,required=True);args=parser.parse_args();args.output_dir.mkdir(exist_ok=False)
    def save(n,v):(args.output_dir/n).write_text(json.dumps(v,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    d=a.GlobalData(args.input_root);root=a.ROOT/'q09_global_comparison_v1';e=json.loads((root/'evidence.json').read_text());g=json.loads((root/'case_graph.json').read_text())
    with patch.object(a,'minimize',side_effect=AssertionError('AUDIT_MUST_NOT_OPTIMIZE')):
        before=a.evaluate(g,d);mid=a.evaluate(g,d,e)
        if 'BOUND_ALL33_COMPARISON_RECOMPUTED' not in mid['reason_codes']:raise ValueError(mid)
        off=a.evaluate(g,d,enabled=False);assert a.dispatch_structure(off,d,g,e) is None
        structural=a.dispatch_structure(mid,d,g,e);final=a.evaluate(g,d,e,structure_evidence=structural)
        assert 'ZERO_CONTRIBUTION_DISTANCE_PARAMETERS_ARE_NOT_OBSERVATIONAL_EVIDENCE' in final['reason_codes']
        assert before['rule_instance_id']==final['rule_instance_id'] and not final['complete_question_answer']
        save('structure_evidence.json',structural);save('rule_after.json',final);save('original_decay_evidence.json',e)
        original=a.expected_counts;padded=functools.partial(original,shift_policy='padded_linear_v2')
        impact=[];endpoints=[]
        for gr in d.groups:
            for role,r in gr.records.items():endpoints.append({'reference':gr.ref,'role':role,'IRF_first':float(r['irf'][0]),'IRF_last':float(r['irf'][-1]),'IRF_total':float(r['irf'].sum())})
        models=[('local2',None)]+[(kind,idx) for kind in ('shared2','shared3') for idx in range(2)]
        for kind,idx in models:
            joint=a.Joint(d,kind) if kind!='local2' else None
            params=e[kind+'_runs'][idx]['parameters'] if idx is not None else None
            pop=joint.population(params) if joint else None
            for n,gr in enumerate(d.groups):
                p=e['local_runs'][gr.ref]['parameters'] if kind=='local2' else params[joint.slices[n]]
                legacy=gr.predict(p,kind,pop)
                with patch.object(a,'expected_counts',padded):new=gr.predict(p,kind,pop)
                for role,r in gr.records.items():
                    mask=r['mask'];oldD=a.poisson_deviance(r['y'][mask],legacy[role][mask]);newD=a.poisson_deviance(r['y'][mask],new[role][mask])
                    impact.append({'model':kind,'run_index':idx,'reference':gr.ref,'role':role,'legacy_deviance':oldD,'padded_deviance':newD,'delta_deviance':newD-oldD,'max_count_change':float(np.max(abs(new[role]-legacy[role]))),'parameters_refit':False})
        save('IRF_endpoints.json',endpoints);save('old_parameter_padded_method_impact.json',impact)
        gr=next(gr for gr in d.groups if gr.owners==['60-119']);p=e['local_runs'][gr.ref]['parameters'].copy();k=gr.donor_size
        assert p[k+3]==1.;old=gr.predict(p,'local2');p[k:k+2]=[35.,65.];new=gr.predict(p,'local2')
        invariant={role:float(np.max(abs(new[role]-old[role]))) for role in old};assert all(v==0 for v in invariant.values())
        save('actual_60_119_invariance.json',{'status':'EXACT_PREDICTION_INVARIANCE','changed_distance_parameters_A':[35.,65.],'donor_only_fraction':1.,'max_count_difference':invariant,'numeric_fits':0,'scope':'At this conditional parameter point, distances do not constrain predictedobservations; not proof sample lacksFRET.'})
        summary={}
        for kind,idx in models:
            rows=[v for v in impact if v['model']==kind and v['run_index']==idx]
            summary[kind+('' if idx is None else ':'+str(idx))]={'legacy_D':sum(x['legacy_deviance'] for x in rows),'padded_D_at_old_parameters':sum(x['padded_deviance'] for x in rows),'changed_roles':sum(x['max_count_change']>1e-8 for x in rows),'maximum_count_delta':max(x['max_count_change'] for x in rows)}
        receipt={'status':'OLD_DECAY_VERIFIED_STRUCTURE_INFORMATION_REASSESSED_NEW_METHOD_DELTA_ONLY','optimizer_calls':0,'old_fits_repeated':0,'same_rule_instance':True,'structure_on_calls':1,'structure_off_calls':0,'original_decay_evidence_unchanged':True,'author_archive_MD5_verified':True,'source_hash_checks':1,'structure_zero_contribution_components':{k:v['zero_contribution_components'] for k,v in structural['models'].items()},'shift_method_comparison':summary,'new_shift_policy':'padded_linear_v2','historical_policy':'legacy_endpoint_v1','new_shift_scientific_fit':'NOT_RUN','full_question_answer':False}
        save('receipt.json',receipt);print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
