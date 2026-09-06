"""Thirteen source-grounded donor-order comparisons, fixed unique D0 ownership."""
import datetime,functools,json,time
from pathlib import Path
from unittest.mock import patch
import numpy as np
from dynamics_atlas_harness import q09_global_comparison_v1 as a
W=Path(__file__).resolve().parents[4];T=Path(__file__).resolve().parents[1];O=T/'outputs/q09_donor_order_groups_v2'
METHOD={'version':'q09-source-donor-groups/v2','IRF_shift':'padded_linear_v2','source_orders':'SI21Table2a componentpresence only','models':['donor2_FRET2_fixed_reference','donor3_FRET2_conditional'],'unique_D0_likelihood':True,'seconds_per_fit':30,'fits_per_changed_group':2,'max_fits':26,'maxiter':1500,'gradient_tolerance':1e-6,'new_donor_seed':[.2,1.5,4.,.2,.5],'author_fitted_values_used':False,'protein_state_number':'NOT_INFERRED'}
def save(n,v):(O/n).write_text(json.dumps(v,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
def main():
    O.mkdir(exist_ok=False);start=time.monotonic();d=a.GlobalData(T/'inputs/q09_author');old=json.loads((a.ROOT/'q09_global_comparison_v1/evidence.json').read_text());source=json.loads((a.ROOT/'q09_deposited_structure_intake_v1/donor_order_source_audit.json').read_text());selected=[x for x in source['groups'] if x['mismatch_variants']];assert len(selected)==13
    newcounts=functools.partial(a.expected_counts,shift_policy='padded_linear_v2')
    e={'method':METHOD,'source_input_id':d.input_id,'source_orders':source,'request_id':a.q.digest({'source':d.input_id,'method':METHOD,'source_orders':source}),'groups':{},'fits':0}
    save('method.json',METHOD)
    with patch.object(a,'expected_counts',newcounts),patch.dict(a.CONFIG,local_seconds=30):
        for ref in selected:
            gr=next(x for x in d.groups if x.ref==ref['reference']);assert gr.donors==2
            p=old['local_runs'][gr.ref]['parameters'];gr3=a.Group(gr.ref,list(gr.owners),gr.records,3)
            embedded=[p[0],p[1],(p[0]+p[1])/2,p[2],1.,p[3],p[4]]+p[5:]
            v2=gr.predict(p,'local2');v3=gr3.predict(embedded,'local2');max_rel={role:float(np.max(abs(v3[role]-v2[role]))/np.max(v2[role])) for role in v2}
            row={'reference':gr.ref,'owners':gr.owners,'source':ref,'old_donor2_parameters':p,'old_donor2_padded_deviance':gr.deviance(p,'local2'),'old_donor2_padded_gradient':float(max(abs(a.q.gradient_at(p,gr.bounds('local2'),lambda x:gr.deviance(x,'local2')/gr.total)))),'embedding_max_relative_prediction_delta':max_rel,'runs':[]}
            e['groups'][gr.ref]=row;save('evidence.json',e)
            if max(max_rel.values())>1e-12:
                row['status']='EMBEDDING_REJECTED_NO_FIT';save('evidence.json',e);continue
            seeds=[embedded,[.2,1.5,4.,.2,.5]+p[3:5]+p[5:]]
            for seed in seeds:
                fit=a.optimize_local(gr3,seed);row['runs'].append(fit);e['fits']+=1;save('evidence.json',e);print(gr.ref,fit['numerical_status'],fit['objective']*gr.total,flush=True)
            best=min(row['runs'],key=lambda x:x['objective']);row['best_D']=best['objective']*gr.total;row['best_status']=best['numerical_status'];row['contributions']=gr3.contributions(best['parameters'],'local2');row['status']='CONDITIONAL_SOURCE_ORDER_COMPARISON_WITH_LIMITS';save('evidence.json',e)
    summary={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'SOURCE_ORDER_GROUP_BATCH_COMPLETED','groups':len(e['groups']),'fits':e['fits'],'elapsed_seconds':time.monotonic()-start,'PASS':sum(r['numerical_status']=='PASS' for g in e['groups'].values() for r in g['runs']),'STOP':sum(r['numerical_status']!='PASS' for g in e['groups'].values() for r in g['runs']),'results':[{k:g[k] for k in ['reference','owners','old_donor2_padded_deviance','best_D','best_status']} for g in e['groups'].values() if 'best_D'in g],'D0_24_source_shared_configuration':'UNKNOWN;sameD0 observedonce;joint2vs3isourconditionalchoice','full_question_answer':False,'rules_controlled':False,'claim_ceiling':'Method-groundedconditionalreferencegroup fits;not3proteinstates orfull33globalrecovery'};save('receipt.json',summary);print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
