"""Fixed-parameter admission of previously computed manual background descendants."""
import argparse,json,time,datetime
from pathlib import Path
import numpy as np
from dynamics_atlas_harness import q09_global_comparison_v1 as a
from dynamics_atlas_harness import q09_targeted_continuation_v1 as c
from dynamics_atlas_harness.q09_cached_group_v2 import CachedGroup


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--task-root',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();t=args.task_root.resolve();out=args.output.resolve();out.mkdir(parents=True,exist_ok=False)
    def read(path):return json.loads(path.read_text())
    def save(name,value):(out/name).write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    parent=t/'outputs/q09_targeted_continuation_v1';previous=read(parent/'rules_after.json');anchor=read(parent/'evidence_result.json');c.verify_saved_history(previous,anchor)
    original=read(parent/'verified_report.json');canary=read(t/'outputs/q09_background_profile_canary_v1/result.json');data=a.GlobalData(t/'inputs/q09_author')
    if canary['source_report_id']!=a.q.digest(original) or canary['input_id']!=data.input_id or previous['method_evidence']['input_id']!=data.input_id:raise ValueError('BACKGROUND_SOURCE_CHANGED')
    if canary['policy']['source_method']!='padded_linear_v2;mix beforeLin and finalmasknormalization' or canary['policy']['background_bounds']!=[1e-12,.05] or canary['scalar_root_calls']!=9:raise ValueError('BACKGROUND_METHOD_CHANGED')
    if len(canary['points'])!=3:raise ValueError('BACKGROUND_BATCH_CHANGED')
    request={'base_result_id':a.q.digest(previous),'input_id':data.input_id,'rule_instance_id':previous['rule_instance_id'],'canary_report_id':a.q.digest(canary),'provenance':'MANUAL_BACKGROUND_DERIVED_FIXED_POINT_VERIFIED'}
    report=dict(request,request_id=a.q.digest(request),optimizer_calls=0,new_rules_extra=0,runs=[]);started=time.monotonic();current=c.current_groups(previous)
    for point in canary['points']:
        source=[r for r in original['runs']if r['reference']==point['reference'] and r['parent_candidate_id']==point['parent_candidate_id']]
        if len(source)!=1:raise ValueError('BACKGROUND_SOURCE_CANDIDATE_AMBIGUOUS')
        source=source[0];parent_id=source['checked']['candidate_id'];parents=[r for r in current[point['reference']]['candidates']if r['candidate_id']==parent_id]
        if len(parents)!=1 or parents[0]['parameters']!=point['parameters_before']:raise ValueError('BACKGROUND_PARENT_CHANGED')
        group0=next(g for g in data.groups if g.ref==point['reference']);g=CachedGroup(group0.ref,group0.owners,group0.records,3)
        pars=np.asarray(point['parameters_after_background_only']);old=np.asarray(point['parameters_before']);low,high=np.asarray(g.bounds('local2')).T
        if pars.shape!=low.shape or not np.isfinite(pars).all() or np.any(pars<low) or np.any(pars>high):raise ValueError('BACKGROUND_POINT_BOUNDS')
        indices=[5]+[11+6*i for i in range(len(g.owners))]
        changed=np.flatnonzero(pars!=old).tolist()
        if not set(changed)<=set(indices) or [r['parameter_index']for r in point['role_updates']]!=indices:raise ValueError('NON_BACKGROUND_PARAMETER_CHANGED')
        objective=lambda x:g.deviance(x,'local2')/g.total
        value=float(objective(pars));gradient=float(np.max(np.abs(a.q.gradient_at(pars,g.bounds('local2'),objective))))
        if not np.isclose(value,point['objective_after'],atol=1e-11,rtol=1e-8) or not np.isclose(gradient,point['projected_gradient_inf'],atol=1e-8,rtol=.001):raise ValueError('BACKGROUND_FIXED_POINT_REPLAY_FAILED')
        checked={'objective':value,'deviance':value*g.total,'projected_gradient_inf':gradient,'parameters':pars.tolist(),'numerical_status':'PASS'if gradient<=1e-6 else 'NUMERICAL_STOP_WITH_FEASIBLE_POINT','provenance':request['provenance'],'full_fit_optimizer_executed':False,'original_manual_background_roots':len(indices)}
        checked['candidate_id']=a.q.digest(checked)
        report['runs'].append({'reference':g.ref,'parent_candidate_id':parent_id,'source_continuation_parent_id':point['parent_candidate_id'],'checked':checked})
    evidence={k:report[k]for k in ['request_id','input_id','rule_instance_id','base_result_id']};evidence['report_id']=a.q.digest(report)
    checks=[];verify=lambda e:(checks.append(e)or report)
    off=c.consume_manual_derived(previous,evidence,verify,enabled=False)
    if checks:raise ValueError('OFF_CONSUMED_MANUAL_EVIDENCE')
    after=c.consume_manual_derived(previous,evidence,verify);evidence=c.evidence_anchor(after,evidence);c.verify_saved_history(after,evidence)
    save('rules_before.json',previous);save('rules_off.json',off);save('rules_after.json',after);save('verified_report.json',report);save('evidence_result.json',evidence);save('next_request.json',c.request(after))
    receipt={'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'fixed_points_verified':len(report['runs']),'optimizer_calls':0,'new_scalar_roots':0,'new_rules_extra':0,'manual_evidence_on_calls':len(checks),'manual_evidence_off_calls':0,'same_rule_instance':after['rule_instance_id']==previous['rule_instance_id'],'elapsed_seconds':time.monotonic()-started,'remaining_selected':[x['reference']for x in c.request(after)['selected']],'complete_question_answer':False};save('receipt.json',receipt);print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()
