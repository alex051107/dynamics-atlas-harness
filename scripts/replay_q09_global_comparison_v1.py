"""Replay real all33 evidence without optimization; optional explicit binding upgrade."""
from pathlib import Path
import argparse,hashlib,json
from unittest.mock import patch
from dynamics_atlas_harness import q09_global_comparison_v1 as a

def legacy_identity(d):
    h=hashlib.sha256(json.dumps({'mapping':d.mapping,'config':a.CONFIG},sort_keys=True).encode())
    for g in d.groups:
        h.update(json.dumps([g.ref,g.owners,g.donors]).encode())
        for role,r in g.records.items():
            for key in ('y','irf','Lin','mask'):
                v=r[key];h.update((role+':'+key).encode());h.update(str(v.shape).encode());h.update(v.dtype.str.encode());h.update(v.tobytes())
            h.update(str(r['kernel'].dt).encode())
    return h.hexdigest()

def main():
    p=argparse.ArgumentParser();p.add_argument('--input-root',required=True,type=Path);p.add_argument('--evidence-dir',required=True,type=Path);p.add_argument('--output-dir',required=True,type=Path);p.add_argument('--readmit-pre-kernel-binding',action='store_true');args=p.parse_args();args.output_dir.mkdir(exist_ok=False)
    def save(n,v):(args.output_dir/n).write_text(json.dumps(v,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    d=a.GlobalData(args.input_root);g=json.loads((args.evidence_dir/'case_graph.json').read_text());e=json.loads((args.evidence_dir/'evidence.json').read_text());old=e['input_id']
    if args.readmit_pre_kernel_binding:
        legacy=legacy_identity(d)
        oldrid=a.q.digest({'input':legacy,'graph':g,'config':a.CONFIG,'rule':a.RULE_ID,'operator':a.OPERATOR_ID})
        if old!=legacy or e['request_id']!=oldrid:raise ValueError('LEGACY_SOURCE_BINDING_NOT_CONFIRMED')
        e=dict(e,input_id=d.input_id,request_id=a.request(d,g))
    before=a.evaluate(g,d)
    with patch.object(a,'minimize',side_effect=AssertionError('Zerooptimizationreplay')):
        r=a.evaluate(g,d,e)
        if 'BOUND_ALL33_COMPARISON_RECOMPUTED' not in r['reason_codes']:raise ValueError(r)
        off=a.evaluate(g,d,enabled=False)
        assert a.dispatch_structure(off,d,g,e) is None
        structural=a.dispatch_structure(r,d,g,e)
        final=a.evaluate(g,d,e,structure_evidence=structural)
        if 'AUTHOR_FORWARD_STRUCTURE_COMPARISON_ASSESSED_WITH_LIMITS' not in final['reason_codes']:raise ValueError(final)
    save('evidence.json',e);save('structure_evidence.json',structural);save('rule_after.json',final)
    save('receipt.json',{'status':'SOURCE_BOUND_NUMERIC_AND_STRUCTURE_REPLAYED','optimizer_calls':0,'same_instance':before['rule_instance_id']==final['rule_instance_id'],'original_input_id':old,'input_id':d.input_id,'changed_evidence_fields':['input_id','request_id'] if args.readmit_pre_kernel_binding else [],'why_readmission':'Before publication strengthen generatednativekernel identity; same sourceobservations/parameters/objectives; originals preserved','local_ACV_runs':0,'full_question_answer':False,'structure_operator_calls':1,'structure_off_calls':0})
    print(json.dumps({'status':final['comparison']['numerical_status'],'reasons':final['reason_codes'],'deviances':{k:v['deviance'] for k,v in final['comparison']['models'].items()},'stops':final['comparison']['numerical_stops']},ensure_ascii=False))
if __name__=='__main__':main()
