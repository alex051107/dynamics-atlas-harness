"""Q09 competing shared/local explanations; bounded two-DA pilot on real counts."""
import hashlib,json
from pathlib import Path
import numpy as np
from . import q09_forward_adequacy_v1 as q
from .q09_shared_ibh_v1 import SharedIBH
from .q09_fluorescence_v1 import poisson_deviance

RULE_ID='Q09R02_CASE_SHARED_POPULATION_COMPARISON_V1'
OPERATOR_ID='q09_shared_local_comparison_v1'
CONFIG={'version':'q09-state-comparison/v1','variants':['19-119','19-132'],'profile_pi':[.2,.35,.5,.65,.8],
 'orientations':[0,1],'donor_components':2,'donor_order_scope':'Existing IBH conditional baseline only; shared across compared models, not imported PQ donor3',
 'instrument':'unchanged originalIBH17HanningLin mask10percent;tailmedianIRF;scatter0;nonperiodic;14.1psbinintegrals',
 'K3_second_weights':[.2,.5,.3],'max_optimizer_calls':13,'claim_ceiling':'Conditional competing-model evidence for2of33variants; no proteinstate-number verdict'}
DONOR_BOUNDS=[(.05,10.)]*2+[(0.,1.),(1e-12,.05),(-5.,5.)]
LOCAL_BOUNDS=DONOR_BOUNDS+2*[(10.,120.),(10.,120.),(0.,1.),(0.,1.),(1e-12,.05),(-5.,5.)]
FIXED_BOUNDS=DONOR_BOUNDS+2*[(10.,120.),(10.,120.),(0.,1.),(1e-12,.05),(-5.,5.)]
SHARED_BOUNDS=FIXED_BOUNDS+[(0.,1.)]
K3_BOUNDS=DONOR_BOUNDS+2*([(10.,120.)]*3+[(0.,1.),(1e-12,.05),(-5.,5.)])+[(0.,1.)]*2


def identity(d):
    expected={'D0_shared','19-119_DA','19-132_DA'}
    if set(d.records)!=expected:raise ValueError('EXACT_SHARED_GROUP_ROLES_REQUIRED')
    h=hashlib.sha256(json.dumps({'audit':d.audit,'config':CONFIG},sort_keys=True).encode())
    for role in sorted(expected):
        for key in ['y','irf','Lin','mask']:
            a=d.records[role][key];h.update((role+':'+key).encode());h.update(str(a.shape).encode());h.update(a.dtype.str.encode());h.update(a.tobytes())
    for name in ['dt','t','r','qweights','rates','transfer_exp']:
        a=np.asarray(getattr(d,name));h.update(name.encode());h.update(a.tobytes())
    return h.hexdigest()


def load_inputs(root):
    if hashlib.md5((Path(root)/'eTCSPC_wildtype.zip').read_bytes()).hexdigest()!='177132ce5bb9fefde871bafe8c92cbfd':raise ValueError('AUTHOR_ARCHIVE_IDENTITY_MISMATCH')
    d=SharedIBH(root)
    baseline=json.loads((q.REPO/'research/paper_result_reproduction_screen_v1/q09_shared_ibh_v1/joint_runs.json').read_text())
    candidates=[]
    for r in baseline:
        rec=dict(r,objective=r['scaled_objective']);q.verify_fit(rec,LOCAL_BOUNDS,lambda p:d.deviance(p)/d.total)
        if r['numerical_status']=='PASS':candidates.append(rec)
    d.baseline=min(candidates,key=lambda r:r['objective']);d.input_id=identity(d)
    return d


def verify_data(d):
    if identity(d)!=d.input_id:raise ValueError('SHARED_GROUP_INPUT_CHANGED')
    observed_total=sum(float(v['y'][v['mask']].sum()) for v in d.records.values())
    if d.total!=observed_total:raise ValueError('CACHED_TOTAL_DIFFERS_FROM_BOUND_OBSERVATIONS')
    q.verify_fit(d.baseline,LOCAL_BOUNDS,lambda p:d.deviance(p)/d.total)


def reduce_local(p):return list(p[:5])+list(p[5:7])+list(p[8:11])+list(p[11:13])+list(p[14:17])
def expand_fixed(p,pi):return list(p[:5])+list(p[5:7])+[pi]+list(p[7:10])+list(p[10:12])+[pi]+list(p[12:15])
def shared2_counts(d,p):return d.joint_counts(expand_fixed(p[:15],p[15]))


def k3_counts(d,p):
    t1,t2,a,bg0,s0=p[:5];pop=q.amplitudes(*p[-2:]);donor=d.intrinsic_donor([t1,t2],[a,1-a]);out={'D0_shared':d.counts('D0_shared',donor,bg0,s0)}
    for i,role in enumerate(['19-119_DA','19-132_DA']):
        R1,R2,R3,f0,bg,shift=p[5+6*i:11+6*i]
        _,da=d.intrinsic_pair([t1,t2],[a,1-a],[R1,R2,R3],pop,f0)
        out[role]=d.counts(role,da,bg,shift)
    return out


def loss(d,p,kind):
    pred=shared2_counts(d,p) if kind=='shared2' else k3_counts(d,p)
    return sum(poisson_deviance(v['y'][v['mask']],pred[k][v['mask']]) for k,v in d.records.items())/d.total


def embed_k3(p):
    out=list(p[:5])
    for start in (5,10):
        R1,R2,f0,bg,shift=p[start:start+5];out+=[R1,R2,(R1+R2)/2,f0,bg,shift]
    return out+[p[15],1.]


def embed_local_k3(p):
    """Exact feasible embedding for TWO variants, identical component kernels.

    Includes coincident distances/zero weights. Not an optimizer PASS and not
    the nesting relation of the general33-variant comparison.
    """
    a,b=p[7],p[13]
    if not (0<=a<=1 and 0<=b<=1):raise ValueError('INVALID_LOCAL_POPULATIONS')
    if a<=b:
        weights=[a,b-a,1-b];ar=[p[5],p[6],p[6]];br=[p[11],p[11],p[12]]
    else:
        weights=[b,a-b,1-a];ar=[p[5],p[5],p[6]];br=[p[11],p[12],p[12]]
    u=weights[0];v=weights[1]/(1-u) if u<1 else 0.
    return list(p[:5])+ar+list(p[8:11])+br+list(p[14:17])+[u,v]


def equivalent_local_counterexample(d):
    # Synthetic known mean; no fitting and no author parameter values.
    t=[1.,4.];a=[.3,.7];pi=[.2,.5,.3];results=[]
    for role,local,R in [('19-119_DA',[.2,.8],[35.,65.,65.]),('19-132_DA',[.7,.3],[35.,35.,65.])]:
        _,two=d.intrinsic_pair(t,a,[35.,65.],local,.1);_,three=d.intrinsic_pair(t,a,R,pi,.1)
        a2=d.counts(role,two,.001,.2);a3=d.counts(role,three,.001,.2)
        results.append(float(np.max(abs(a2-a3))/np.max(a2)))
    if max(results)>1e-12:raise ValueError('COALESCENCE_COUNTEREXAMPLE_NOT_EQUIVALENT')
    return {'synthetic_known_mean':True,'max_relative_count_differences':results,'judgment':'EQUIVALENT_LOCAL_K2_EXPLANATION_EXISTS; sharedK3fit alone cannot establish3protein states'}


def request(d,g):return q.digest({'rule':RULE_ID,'graph':g,'input':d.input_id,'baseline':d.baseline,'config':CONFIG})


def evaluate(g,d,e=None,enabled=True):
    r={'rule_instance_id':q.rule_instance_id(RULE_ID,'CASE',g['case']['case_id']),'status':'UNRESOLVED','obligations':[],'complete_question_answer':False,'reason_codes':[]}
    if not enabled or g['case']['case_id']!='q09_t4l_state_number_20260905' or g['case']['requested_claim_level']!='STATE_NUMBER_AND_STRUCTURE_CONSISTENCY':r.update(status='NOT_APPLICABLE');return r
    registry=json.loads((q.REPO/'registries/rules_v1/q09_state_comparison_rule_v1.json').read_text())
    if registry['rule_id']!=RULE_ID or registry['operator_id']!=OPERATOR_ID or registry['scientific_pass_enabled']:raise ValueError('UNSUPPORTED_STATE_COMPARISON_RULE')
    q._validate_graph(g);verify_data(d);rid=request(d,g);r['request_id']=rid
    obligation={'operator_id':OPERATOR_ID,'request_id':rid,'input_id':d.input_id,'rule_instance_id':r['rule_instance_id']}
    if e is None:r.update(obligations=[obligation],reason_codes=['SHARED_LOCAL_AND_STRUCTURE_COMPETING_EVIDENCE_REQUIRED']);return r
    try:result=verify_evidence(d,e,rid)
    except (ValueError,KeyError,TypeError,IndexError) as err:r.update(obligations=[obligation],reason_codes=['COMPARISON_EVIDENCE_REJECTED'],rejection_reason=str(err));return r
    if result['status'] in ('NUMERICAL_STOP','NUMERICAL_COMPARISON_INCOMPLETE'):
        r.update(reason_codes=['BOUND_SHARED_LOCAL_COMPARISON_RECOMPUTED','SOLVER_COMPARISON_INCOMPLETE','STRUCTURE_FORWARD_EVIDENCE_REQUIRED'],comparison=result);return r
    r.update(reason_codes=['BOUND_SHARED_LOCAL_COMPARISON_RECOMPUTED','LOCAL_POPULATION_ALTERNATIVE_MUST_BE_RETAINED','STRUCTURE_FORWARD_EVIDENCE_REQUIRED'],comparison=result)
    return r


def run(d,rid,checkpoint=None):
    verify_data(d);base=d.baseline['parameters'];e={'schema':CONFIG['version'],'operator_id':OPERATOR_ID,'request_id':rid,'input_id':d.input_id,'config':CONFIG,
      'baseline':d.baseline,'profile_runs':[],'shared2_refinement':None,'K3_runs':[],'counterexample':equivalent_local_counterexample(d)}
    def record():
        if checkpoint:checkpoint(e)
    for pi in CONFIG['profile_pi']:
        for orientation in CONFIG['orientations']:
            initial=reduce_local(base)
            if orientation:initial[10:12]=initial[10:12][::-1]
            fit=q.optimize(initial,FIXED_BOUNDS,lambda p:d.deviance(expand_fixed(p,pi))/d.total,'SHARED_K2_FIXED_PI')
            e['profile_runs'].append({'pi':pi,'orientation':orientation,'fit':fit});record()
    ok=[x for x in e['profile_runs'] if x['fit']['numerical_status']=='PASS']
    if not ok:return e
    best=min(ok,key=lambda x:x['fit']['objective']);start=best['fit']['parameters']+[best['pi']]
    e['shared2_refinement']=q.optimize(start,SHARED_BOUNDS,lambda p:loss(d,p,'shared2'),'SHARED_K2_FREE_PI');record()
    r=e['shared2_refinement'];p=r['parameters'] if r['numerical_status']=='PASS' else start
    for seed in (0,1):
        initial=embed_k3(p)
        if seed:initial[-2:]=[.2,.625]
        fit=q.optimize(initial,K3_BOUNDS,lambda p:loss(d,p,'shared3'),'SHARED_K3');e['K3_runs'].append(fit);record()
    return e


def verify_evidence(d,e,rid):
    verify_data(d)
    if e['schema']!=CONFIG['version'] or e['operator_id']!=OPERATOR_ID or e['request_id']!=rid or e['input_id']!=d.input_id or e['config']!=CONFIG or e['baseline']!=d.baseline:raise ValueError('COMPARISON_BINDING_MISMATCH')
    if e['counterexample']!=equivalent_local_counterexample(d):raise ValueError('COUNTEREXAMPLE_NOT_RECOMPUTED')
    if len(e['profile_runs'])!=10:raise ValueError('INCOMPLETE_SHARED_PI_PROFILE')
    checks=[];accepted=[]
    for item,(pi,ori) in zip(e['profile_runs'],[(p,o) for p in CONFIG['profile_pi'] for o in CONFIG['orientations']]):
        initial=reduce_local(d.baseline['parameters'])
        if ori:initial[10:12]=initial[10:12][::-1]
        if item['pi']!=pi or item['orientation']!=ori or item['fit']['initial']!=initial:raise ValueError('UNDECLARED_PROFILE_START')
        check=q.verify_fit(item['fit'],FIXED_BOUNDS,lambda p:d.deviance(expand_fixed(p,pi))/d.total);checks.append({'pi':pi,'orientation':ori,**check})
        if check['status']=='VERIFIED':accepted.append(item)
    result={'profile_checks':checks,'localK2_baseline_deviance':d.baseline['objective']*d.total,'sharedK2_deviance':None,'sharedK3_deviance':None,'counterexample':e['counterexample'],'protein_state_number':'UNRESOLVED'}
    if not accepted:
        if e['shared2_refinement'] is not None or e['K3_runs']:raise ValueError('DEPENDENT_MODEL_WITHOUT_ACCEPTED_PROFILE')
        result['status']='NUMERICAL_STOP';return result
    best=min(accepted,key=lambda x:x['fit']['objective']);start=best['fit']['parameters']+[best['pi']];r=e['shared2_refinement']
    if r['initial']!=start:raise ValueError('UNDECLARED_FREE_PI_START')
    check=q.verify_fit(r,SHARED_BOUNDS,lambda p:loss(d,p,'shared2'));result['shared2_refinement_check']=check
    p=r['parameters'] if check['status']=='VERIFIED' else start
    result['sharedK2_deviance']=loss(d,p,'shared2')*d.total
    embedded=embed_k3(p);a=shared2_counts(d,p);b=k3_counts(d,embedded)
    for role in a:np.testing.assert_allclose(a[role],b[role],rtol=1e-12,atol=1e-9)
    result['K3_zero_weight_embedding_deviance']=loss(d,embedded,'shared3')*d.total
    if len(e['K3_runs'])!=2:raise ValueError('INCOMPLETE_K3_STARTS')
    kc=[]
    for i,fit in enumerate(e['K3_runs']):
        initial=embed_k3(p)
        if i:initial[-2:]=[.2,.625]
        if fit['initial']!=initial:raise ValueError('UNDECLARED_K3_START')
        ck=q.verify_fit(fit,K3_BOUNDS,lambda p:loss(d,p,'shared3'));kc.append(ck)
    result['K3_checks']=kc;valid=[x['objective'] for x in kc if x['status']=='VERIFIED']
    if valid:result['sharedK3_deviance']=min(valid)*d.total
    local_embedding=embed_local_k3(d.baseline['parameters'])
    local_counts=d.joint_counts(d.baseline['parameters']);embedded_counts=k3_counts(d,local_embedding)
    for role in local_counts:np.testing.assert_allclose(local_counts[role],embedded_counts[role],rtol=1e-12,atol=1e-9)
    result['localK2_exact_K3_candidate']={'kind':'EXACT_FEASIBLE_NOT_OPTIMIZER_PASS','parameters':local_embedding,'deviance':loss(d,local_embedding,'shared3')*d.total}
    result['search_stops']={'fixed_profile':sum(c['status']!='VERIFIED' for c in checks),'shared2_refinement':check['status']!='VERIFIED','K3':sum(c['status']!='VERIFIED' for c in kc)}
    tol=1e-5
    result['local2_nested_order_observed']=bool(result['localK2_baseline_deviance']<=result['sharedK2_deviance']+tol)
    result['K3_nested_order_observed']=bool(valid) and bool(result['sharedK3_deviance']<=result['sharedK2_deviance']+tol)
    result['K3_local2_nested_order_observed']=bool(valid) and bool(result['sharedK3_deviance']<=result['localK2_exact_K3_candidate']['deviance']+tol)
    completed=result['local2_nested_order_observed'] and result['K3_nested_order_observed'] and result['K3_local2_nested_order_observed'] and not any(result['search_stops'].values())
    result['status']='CONDITIONAL_COMPETING_EXPLANATIONS_RETAINED' if completed else 'NUMERICAL_COMPARISON_INCOMPLETE'
    return result


def dispatch(r,d,g,checkpoint=None):
    if not r['obligations']:return None
    if r!=evaluate(g,d):raise ValueError('INVALID_STATE_COMPARISON_OBLIGATION')
    return run(d,r['request_id'],checkpoint)
