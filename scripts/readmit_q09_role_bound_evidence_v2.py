"""Re-admit historical Q09 results from source bytes; change bindings, never fits."""
from pathlib import Path
import argparse,copy,hashlib,json
from dynamics_atlas_harness import q09_forward_adequacy_v1 as q
from dynamics_atlas_harness import q09_calibration_sensitivity_v1 as c

def legacy_identity(d):
    h=hashlib.sha256()
    for a in [d.t,*[d.y[k] for k in ('D0','DA')],*[d.irf[k] for k in ('D0','DA')],d.lin,d.mask,d.r,d.qweights,d.rates,d.transfer_exp]:
        h.update(str(a.shape).encode());h.update(a.dtype.str.encode());h.update(a.tobytes())
    h.update(json.dumps({'dt':d.dt,'baseline':d.baseline,'source_identity':d.source_identity},sort_keys=True,allow_nan=False).encode());return h.hexdigest()

def main():
    p=argparse.ArgumentParser();p.add_argument('--input-root',type=Path,required=True);p.add_argument('--old-forward-dir',type=Path,required=True);p.add_argument('--old-calibration',type=Path,required=True);p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args();a.output_dir.mkdir(exist_ok=False)
    # Fixed loader checks original archive and named member bytes before rebinding.
    d=q.load_inputs(a.input_root);g=json.loads((a.old_forward_dir/'case_graph.json').read_text());old=json.loads((a.old_forward_dir/'evidence.json').read_text());cal=json.loads(a.old_calibration.read_text())
    prior=legacy_identity(d);expected=q.digest({'instance':q.rule_instance_id(q.RULE_ID,'CASE',g['case']['case_id']),'graph':g,'input_id':prior,'config':q.CONFIG})
    if old['input_id']!=prior or old['request_id']!=expected or cal['input_id']!=prior or cal['request_id']!=c.request_id(old):raise ValueError('LEGACY_SOURCE_OR_REQUEST_NOT_MATCHED')
    new=copy.deepcopy(old);new['input_id']=d.input_id;new['request_id']=q.evaluate_forward_rule(g,d)['request_id']
    newcal=copy.deepcopy(cal);newcal['input_id']=d.input_id;newcal['request_id']=c.request_id(new)
    after=q.evaluate_forward_rule(g,d,new,calibration_evidence=newcal)
    if 'BOUND_CALIBRATION_SENSITIVITY_RECOMPUTED' not in after['reason_codes']:raise ValueError(after)
    forward=a.output_dir/'forward';forward.mkdir()
    for name,obj in [(forward/'evidence.json',new),(forward/'case_graph.json',g),(a.output_dir/'calibration_evidence.json',newcal),(a.output_dir/'reassessment.json',after),
      (a.output_dir/'receipt.json',{'status':'ROLE_BOUND_SOURCE_READMISSION_AND_NUMERIC_REPLAY_PASS','old_input_id':prior,'new_input_id':d.input_id,'changed_fields_only':['input_id','request_id'],'all_fit_parameters_and_calibration_realizations_preserved':True,'optimizer_calls':0,'local_forward_status':after['local_forward_status'],'full_scientific_answers_added':0})]:name.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
    print(after['local_forward_status'])
if __name__=='__main__':main()
