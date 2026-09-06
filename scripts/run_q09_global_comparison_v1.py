from pathlib import Path
import argparse,json
from dynamics_atlas_harness import q09_global_comparison_v1 as a

def main():
    p=argparse.ArgumentParser();p.add_argument('--input-root',required=True,type=Path);p.add_argument('--graph',required=True,type=Path);p.add_argument('--output-dir',required=True,type=Path);args=p.parse_args();args.output_dir.mkdir(exist_ok=False)
    def save(n,obj):(args.output_dir/n).write_text(json.dumps(obj,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    d=a.GlobalData(args.input_root);g=json.loads(args.graph.read_text());save('source_admission.json',d.audit);save('case_graph.json',g)
    # New group-native loader must reproduce both already-computed source fits.
    reuse={gr.ref:a.reuse_local(gr) for gr in d.groups if gr.owners in (['19-119','19-132'],['22-127'])};save('reused_native_parity.json',reuse)
    before=a.evaluate(g,d);off=a.evaluate(g,d,enabled=False);save('rule_before.json',before);save('rule_off.json',off)
    assert a.dispatch(off,d,g,None) is None
    def checkpoint(e):
        save('evidence.json',e)
        latest=list(e['local_runs'].items())[-1] if e['local_runs'] else None
        print(json.dumps({'local_groups':len(e['local_runs']),'shared2':len(e['shared2_runs']),'shared3':len(e['shared3_runs']),'latest_local':None if latest is None else {'group':latest[0],'status':latest[1]['numerical_status'],'seconds':latest[1].get('elapsed_seconds'),'D_per_photon':latest[1]['objective']}},ensure_ascii=False),flush=True)
    e=a.dispatch(before,d,g,checkpoint);save('evidence.json',e);after=a.evaluate(g,d,e);save('rule_after.json',after)
    save('receipt.json',{'on_calls':1,'off_calls':0,'optimizer_calls':sum(r['kind']=='ACTUAL_OPTIMIZER' for r in e['local_runs'].values())+len(e['shared2_runs'])+len(e['shared3_runs']),'same_instance':before['rule_instance_id']==after['rule_instance_id'],'full_question_answer':False,'reason_codes':after['reason_codes']})
    print(json.dumps({'finished':True,'reason_codes':after['reason_codes'],'status':after.get('comparison',{}).get('numerical_status'),'rejection':after.get('rejection_reason')},ensure_ascii=False),flush=True)
if __name__=='__main__':main()
