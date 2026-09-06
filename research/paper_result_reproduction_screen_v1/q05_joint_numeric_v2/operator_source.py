"""Narrow, versioned common-ensemble rule and Gaussian BME calculation.

Conditional reconstruction of deposited Q05 matrices. No author final weights,
post-fit predictions or scientific acceptance thresholds are consumed.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.optimize import minimize
from scipy.special import logsumexp

from .rules_prototype_v1 import rule_instance_id

RULE_ID = "Q05R01_CASE_COMMON_ENSEMBLE_NUMERIC_V1"
OPERATOR_ID = "q05_common_weight_bme_v1"
CHANNELS = ("saxs", "amide", "methyl")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    allow_nan=False).encode()).hexdigest()


def validate_config(config):
    fixed = {"theta": 6.0, "noe_power": 3, "prior": "UNIFORM",
             "saxs_scale": "AS_DEPOSITED_NO_SCALE_OFFSET",
             "error_model": "GAUSSIAN_FIRST_ORDER_NOE_PROPAGATION",
             "loss": "HALF_SUM_FIXED_ROWS", "duplicate_policy": "PRESERVE_ALL_ROWS",
             "channel_weights": {k: 1.0 for k in CHANNELS},
             "original_joint_configuration": "UNKNOWN",
             "mode": "CONDITIONAL_RECONSTRUCTION",
             "maxiter": 2000, "max_seconds": 120,
             "projected_gradient_tolerance": 1e-6,
             "relative_primal_dual_gap_tolerance": 1e-6}
    if config != fixed:
        raise ValueError("UNSUPPORTED_OR_INCOMPLETE_METHOD_CONFIGURATION")


def _parsed_id(data):
    return digest({k: data[k].tolist() if isinstance(data[k], np.ndarray) else data[k]
                   for k in ('A','b','sigma','channel','labels','frame_ids','input_id','method_config')})


def seal_data(data, config):
    # Runtime calls this only after source admission; tests use synthetic data explicitly.
    data['method_config'] = json.loads(json.dumps(config))
    data['parsed_id'] = _parsed_id(data)
    for k in ('A','b','sigma','channel'):
        data[k].flags.writeable = False
    return data


def verify_data(data, config):
    validate_config(config)
    if data['method_config'] != config or data['parsed_id'] != _parsed_id(data):
        raise ValueError('ADMITTED_PARSED_INPUT_CHANGED')


def _check_author_payloads(payloads, paths, root):
    repo = Path(__file__).resolve().parents[2]
    base = repo/'research/paper_result_reproduction_screen_v1'
    manifest = json.loads((base/'q05_review_evidence/inputs/q05_author/manifest.json').read_text())
    extra = json.loads((base/'q05_input_authority_supplement_v1.json').read_text())
    if extra['author_commit'] != manifest['commit']:
        raise ValueError('AUTHORITY_COMMIT_MISMATCH')
    expected = {x['relative_path'].removeprefix('inputs/q05_author/'):x['git_blob_sha']
                for x in manifest['files'] if 'git_blob_sha' in x}
    for x in (extra['raw_saxs'],extra['q_labels']):
        expected[x['relative_path']] = x['git_blob_sha']
    for key, payload in payloads.items():
        relative = str(paths[key].relative_to(root))
        actual = hashlib.sha1(b'blob '+str(len(payload)).encode()+b'\0'+payload).hexdigest()
        if actual != expected.get(relative):
            raise ValueError('AUTHOR_SOURCE_IDENTITY_MISMATCH:'+relative)
    return manifest['commit']


def load_inputs(root: Path, config):
    validate_config(config)
    method = root / "BME_reweight/inputs_and_method"
    paths = {k: method / name for k, name in {
        "saxs": "simulation_SAXS.dat", "amide": "simulation_HN2_NOE.dat",
        "methyl": "simulation_methyl_NOE.dat"}.items()}
    paths.update(q=method / "SAXS_q_labels_from_author_stats.dat",
                 experiment=root / "SAXS_and_SANS/Delta_H5_no_tag_Static_SAXS_30C_RB_subtracted.dat",
                 amide_exp=method / "exp_HN2_NOE.dat", methyl_exp=method / "exp_methyl_NOE.dat")
    # Read each immutable payload once; parse and fingerprint the same bytes.
    import io
    payloads = {k: p.read_bytes() for k, p in paths.items()}
    admitted_commit = _check_author_payloads(payloads, paths, root)
    hashes = {str(paths[k].relative_to(root)): hashlib.sha256(v).hexdigest()
              for k, v in payloads.items()}
    sims = {k: np.loadtxt(io.BytesIO(payloads[k])) for k in CHANNELS}
    ids = sims["saxs"][:, 0]
    if len(np.unique(ids)) != len(ids) or not np.all(np.isfinite(ids)):
        raise ValueError("INVALID_FRAME_IDENTITIES")
    for k, a in sims.items():
        if not np.array_equal(a[:, 0], ids):
            raise ValueError("FRAME_ORDER_MISMATCH:" + k)
        if not np.all(np.isfinite(a)) or not np.all(a[:, 1:] > 0):
            raise ValueError("INVALID_PREDICTION_MATRIX:" + k)
    obs = np.loadtxt(io.BytesIO(payloads["experiment"]), skiprows=1)
    q = np.loadtxt(io.BytesIO(payloads["q"]))
    indices = []
    for value in q:
        found = np.flatnonzero(np.isclose(obs[:, 0], value, rtol=0, atol=1e-10))
        if len(found) != 1:
            raise ValueError("SAXS_Q_NOT_UNIQUE")
        indices.append(int(found[0]))
    if len(set(indices)) != len(indices) or len(indices) != sims["saxs"].shape[1]-1:
        raise ValueError("SAXS_COLUMN_IDENTITY_MISMATCH")
    obs = obs[indices]
    A, b, sigma = [sims['saxs'][:, 1:]], [obs[:, 1]], [obs[:, 2]]
    channel = ['saxs'] * len(obs)
    labels = ['q=' + repr(float(v)) for v in q]
    for k in ('amide', 'methyl'):
        rows = [line.split() for line in payloads[k+'_exp'].decode().splitlines()
                if line.strip() and not line.lstrip().startswith('#')]
        if len(rows) != sims[k].shape[1]-1 or not all(len(v)==5 and v[-1]=='UPPER' for v in rows):
            raise ValueError('NOE_COLUMN_OR_BOUND_MISMATCH:'+k)
        u = np.array([float(v[2]) for v in rows]); e = np.array([float(v[3]) for v in rows])
        if not np.all(u>0) or not np.all(e>0):
            raise ValueError('INVALID_NOE_BOUND_OR_ERROR')
        A.append(sims[k][:, 1:]**-3); b.append(u**-3); sigma.append(3*e/u**4)
        channel.extend([k]*len(rows))
        # Row position preserves intentional or unexplained duplicates.
        labels.extend(f'{i}:{v[0]}--{v[1]}' for i,v in enumerate(rows))
    data = {'A':np.hstack(A), 'b':np.concatenate(b), 'sigma':np.concatenate(sigma),
            'channel':np.array(channel), 'labels':labels, 'frame_ids':ids.tolist()}
    if not np.all(np.isfinite(data['b'])) or not np.all(np.isfinite(data['sigma'])) or not np.all(data['sigma']>0):
        raise ValueError('INVALID_OBSERVATION_OR_ERROR')
    identity = {'files':hashes, 'config':config, 'frame_ids':data['frame_ids'],
                'labels':labels, 'channel':channel,
                'source_commit':admitted_commit,
                'source_identity_status':'MATCHED_PREEXISTING_AUTHOR_MANIFEST_AND_VERIFIED_SUPPLEMENT',
                'column_mapping':'Deposited positional NOE columns; q matched to author grid metadata; coordinate mapping unverified'}
    data['input_identity'] = identity
    data['input_id'] = digest(identity)
    return seal_data(data, config)


def score(data, weights):
    A,b,sigma = data['A'],data['b'],data['sigma']
    pred = weights @ A
    signed = (pred-b)/sigma
    residual = np.where(data['channel']=='saxs', signed, np.minimum(signed,0))
    losses = {}
    for k in dict.fromkeys(data['channel'].tolist()):
        mask = data['channel']==k; r = residual[mask]; total=float(r@r)
        losses[k] = {'rows':int(mask.sum()), 'squared_loss_sum':total,
                     'fixed_row_mean':total/int(mask.sum()),
                     'nonzero_residual_count':int(np.count_nonzero(r)),
                     'max_absolute_residual':float(np.max(abs(r)))}
    return {'prediction':pred.tolist(), 'signed_standardized_residual':signed.tolist(),
            'objective_residual':residual.tolist(), 'channels':losses}


def solve_joint(data, config):
    """One shared vector, same Gaussian dual as the audited local v0 core."""
    verify_data(data, config)
    A,b,sig = data['A'],data['b'],data['sigma']; n,m=A.shape
    w0=np.full(n,1/n); theta=config['theta']; start=time.monotonic()
    center=w0@A; scale=(np.sqrt(np.average((A-center)**2,axis=0,weights=w0))+sig)/2
    X=(A-center)/scale; y=(b-center)/scale; s=sig/scale; logw0=np.log(w0)
    lower=data['channel']!='saxs'
    def fun(lam):
        if time.monotonic()-start>config['max_seconds']:
            raise TimeoutError('OPTIMIZER_TIME_BUDGET')
        v=logw0-X@lam; z=logsumexp(v); w=np.exp(v-z)
        return ((z+lam@y+0.5*theta*np.sum((s*lam)**2))/theta,
                (y-X.T@w+theta*s*s*lam)/theta)
    opt=minimize(fun,np.zeros(m),method='L-BFGS-B',jac=True,
                 bounds=[(None,0) if x else (None,None) for x in lower],
                 options={'maxiter':config['maxiter'],'ftol':1e-14,'gtol':1e-8,'maxls':40})
    lam=opt.x; value,grad=fun(lam)
    w=np.exp(logw0-X@lam-logsumexp(logw0-X@lam))
    baseline=score(data,w0); fitted=score(data,w)
    positive=w>0; kl=float(np.sum(w[positive]*np.log(w[positive]/w0[positive])))
    primal=0.5*sum(v['squared_loss_sum'] for v in fitted['channels'].values())+theta*kl
    dual=-theta**2*value
    # Projected gradient mapping for lambda <= 0 on transformed lower bounds.
    projected=lam-grad; projected[lower]=np.minimum(projected[lower],0)
    pg=float(np.max(abs(lam-projected))); gap=float(primal-dual)
    gap_tol=config['relative_primal_dual_gap_tolerance']*max(1,abs(primal))
    ok=(opt.success and pg<=config['projected_gradient_tolerance']
        and -gap_tol<=gap<=gap_tol and np.all(np.isfinite(w))
        and abs(w.sum()-1)<1e-10 and np.all(w>=0))
    weights=w.tolist(); wid=digest({'frame_ids':data['frame_ids'],'weights':weights})
    return {'schema_version':'q05-joint-numeric-evidence/v2', 'input_id':data['input_id'],
            'dual_multipliers':lam.tolist(),'operator_id':OPERATOR_ID,'config':config,'frame_ids':data['frame_ids'],
            'labels':data['labels'],'weights':weights,'weight_id':wid,
            'channel_weight_ids':{k:wid for k in fitted['channels']},
            'baseline':baseline,'fitted':fitted,
            'optimization':{'success':bool(opt.success),'message':str(opt.message),
                            'iterations':int(opt.nit),'projected_gradient_inf':pg,
                            'primal':float(primal),'dual_lower_bound':float(dual),
                            'primal_dual_gap':gap,'gap_tolerance':gap_tol,
                            'numerical_conditions_satisfied':bool(ok)},
            'concentration':{'relative_entropy':-kl,'entropy_effective_fraction':float(np.exp(-kl)),
                             'weight_ess_not_independent_samples':float(1/(w@w)),
                             'max_weight':float(w.max())},
            'elapsed_seconds':time.monotonic()-start,
            'scientific_compatibility':'UNRESOLVED_NO_JUSTIFIED_ACCEPTANCE_CRITERION',
            'fit_targets':list(CHANNELS), 'independent_validation':'NOT_CLAIMED'}


def verify_numeric_evidence(data, config, evidence, request_id):
    """Recompute the numerical certificate, without optimizing or trusting summaries."""
    verify_data(data, config)
    if (evidence.get('schema_version') != 'q05-joint-numeric-evidence/v2'
        or evidence.get('operator_id') != OPERATOR_ID or evidence.get('config') != config
        or evidence.get('request_id') != request_id or evidence.get('input_id') != data['input_id']
        or evidence.get('frame_ids') != data['frame_ids'] or evidence.get('labels') != data['labels']):
        raise ValueError('EVIDENCE_CONTEXT_MISMATCH')
    n,m=data['A'].shape; w=np.asarray(evidence['weights'],dtype=float)
    lam=np.asarray(evidence['dual_multipliers'],dtype=float)
    if (w.shape!=(n,) or lam.shape!=(m,) or not np.all(np.isfinite(w))
        or not np.all(np.isfinite(lam)) or np.any(w<0) or abs(w.sum()-1)>1e-10):
        raise ValueError('INVALID_NUMERICAL_CERTIFICATE')
    wid=digest({'frame_ids':data['frame_ids'],'weights':evidence['weights']})
    if (evidence.get('weight_id')!=wid or set(evidence.get('channel_weight_ids',{}))!=set(CHANNELS)
        or any(x!=wid for x in evidence['channel_weight_ids'].values())):
        raise ValueError('SHARED_WEIGHT_IDENTITY_MISMATCH')
    w0=np.full(n,1/n);A,b,sig=data['A'],data['b'],data['sigma'];theta=config['theta']
    center=w0@A;scale=(np.sqrt(np.average((A-center)**2,axis=0,weights=w0))+sig)/2
    X=(A-center)/scale;y=(b-center)/scale;s=sig/scale
    z=logsumexp(np.log(w0)-X@lam);w_dual=np.exp(np.log(w0)-X@lam-z)
    if not np.allclose(w,w_dual,rtol=1e-8,atol=1e-12):
        raise ValueError('WEIGHTS_DO_NOT_MATCH_DUAL_CERTIFICATE')
    lower=data['channel']!='saxs'
    if np.any(lam[lower]>1e-12):raise ValueError('DUAL_BOUND_VIOLATION')
    baseline=score(data,w0);fitted=score(data,w)
    def compare(actual,expected):
        if isinstance(expected,dict):
            if not isinstance(actual,dict) or set(actual)!=set(expected):raise ValueError('EVIDENCE_STRUCTURE_MISMATCH')
            for key,value in expected.items():compare(actual[key],value)
        else:
            a=np.asarray(actual,dtype=float);b=np.asarray(expected,dtype=float)
            if a.shape!=b.shape or not np.all(np.isfinite(a)) or not np.allclose(a,b,rtol=1e-8,atol=1e-10):
                raise ValueError('EVIDENCE_NUMBERS_INCONSISTENT')
    compare(evidence['baseline'],baseline);compare(evidence['fitted'],fitted)
    positive=w>0;kl=float(np.sum(w[positive]*np.log(w[positive]/w0[positive])))
    primal=.5*sum(x['squared_loss_sum'] for x in fitted['channels'].values())+theta*kl
    dual=-theta*(z+lam@y+.5*theta*np.sum((s*lam)**2))
    grad=(y-X.T@w+theta*s*s*lam)/theta
    projected=lam-grad;projected[lower]=np.minimum(projected[lower],0)
    pg=float(np.max(abs(lam-projected)));gap=float(primal-dual)
    tol=config['relative_primal_dual_gap_tolerance']*max(1,abs(primal))
    calculated={'projected_gradient_inf':pg,'primal':primal,'dual_lower_bound':dual,
                'primal_dual_gap':gap,'gap_tolerance':tol}
    optimization=evidence['optimization']
    for key,value in calculated.items():compare(optimization[key],value)
    numerical_ok=(optimization.get('success') is True and pg<=config['projected_gradient_tolerance'] and -tol<=gap<=tol)
    if optimization.get('numerical_conditions_satisfied') is not bool(numerical_ok):
        raise ValueError('NUMERICAL_STATUS_CONTRADICTS_CERTIFICATE')
    concentration={'relative_entropy':-kl,'entropy_effective_fraction':float(np.exp(-kl)),
                   'weight_ess_not_independent_samples':float(1/(w@w)),'max_weight':float(w.max())}
    compare(evidence['concentration'],concentration)
    return {'baseline':baseline,'fitted':fitted,'numerical_ok':bool(numerical_ok),'weight_id':wid}


def _validate_q05_graph(graph,rule):
    repo=Path(__file__).resolve().parents[2]
    packet=json.loads((repo/'evidence/paper_blind_exposed_v1/public/q05_public_fact_packet_v1.json').read_text())
    authority=packet['platform_authority_envelope']['rules_projection_authority']
    if graph['case']['scientific_claim']!=authority['case']['scientific_claim']:
        raise ValueError('Q05_CLAIM_MISMATCH')
    sources=graph.get('evidence_items',[])
    if len(sources)!=3 or {x['source_id']:x['evidence_role'] for x in sources}!=authority['source_evidence_roles']:
        raise ValueError('Q05_SOURCE_SET_MISMATCH')
    keys=('comparison_id','left_source_id','right_source_id','relation_type')
    observed=[tuple(x.get(k) for k in keys) for x in graph.get('comparisons',[])]
    expected=[tuple(x[k] for k in keys) for x in authority['comparisons']]
    if sorted(observed)!=sorted(expected):raise ValueError('Q05_COMPARISON_SET_MISMATCH')


def evaluate_joint_rule(case_graph, data, evidence=None, *, enabled=True):
    """Reevaluate against admitted numerical data, not an identity string alone."""
    case_id=case_graph['case']['case_id'];instance=rule_instance_id(RULE_ID,'CASE',case_id)
    result={'rule_instance_id':instance,'runtime_subrule_id':RULE_ID,'target':{'kind':'CASE','id':case_id},
            'status':'UNRESOLVED','reason_codes':[],'obligations':[],
            'scientific_compatibility':'UNRESOLVED','complete_question_answer':False}
    registry=Path(__file__).resolve().parents[2]/'registries/rules_v1/q05_joint_numeric_rule_v1.json'
    rule=json.loads(registry.read_text())
    if rule['rule_id']!=RULE_ID or rule['operator_id']!=OPERATOR_ID or rule['scientific_pass_enabled']:
        raise ValueError('UNSUPPORTED_JOINT_RULE_VERSION')
    joint=(case_id==rule['case_id'] and any(e.get('relation_type')==rule['trigger_relation'] for e in case_graph.get('comparisons',[])))
    if not enabled or not joint:
        result.update(status='NOT_APPLICABLE',reason_codes=['RULE_DISABLED' if not enabled else 'NO_JOINT_CLAIM']);return result
    _validate_q05_graph(case_graph,rule)
    if data is None:result['reason_codes']=['TYPED_METHOD_INPUT_REQUIRED'];return result
    verify_data(data,data['method_config'])
    request_id=digest({'rule_instance_id':instance,'graph':case_graph,'input_id':data['input_id'],
                       'parsed_id':data['parsed_id'],'method':data['method_config']})
    if evidence is None:
        result['reason_codes']=['COMMON_WEIGHT_NUMERIC_EVIDENCE_REQUIRED']
        result['obligations']=[{'rule_instance_id':instance,'operator_id':OPERATOR_ID,'request_id':request_id,
                                'input_id':data['input_id'],'purpose':'CONDITIONAL_COMMON_WEIGHT_MAIN_CALCULATION'}]
        return result
    try:
        checked=verify_numeric_evidence(data,data['method_config'],evidence,request_id)
    except (ValueError,TypeError,KeyError,OverflowError) as exc:
        result['reason_codes']=['NUMERIC_EVIDENCE_REJECTED'];result['rejection_reason']=str(exc);return result
    if not checked['numerical_ok']:
        result['reason_codes']=['NUMERICAL_OPTIMALITY_NOT_ESTABLISHED'];return result
    comparison={}
    for k in CHANNELS:
        old=checked['baseline']['channels'][k]['squared_loss_sum'];new=checked['fitted']['channels'][k]['squared_loss_sum']
        tol=1e-10*max(1,abs(old),abs(new))
        comparison[k]='DECREASED' if new<old-tol else 'INCREASED' if new>old+tol else 'UNCHANGED'
    result.update(reason_codes=['COMMON_WEIGHT_NUMERIC_EVIDENCE_AVAILABLE','ABSOLUTE_COMPATIBILITY_CRITERION_UNRESOLVED'],
                  relative_fit_change=comparison,evidence_weight_id=checked['weight_id'],request_id=request_id,
                  conditional_calculation='COMPLETE',claim_ceiling='Verified per-channel changes under stated method; no absolute compatibility or shape support')
    return result


def dispatch_obligation(rule_result, data, config, case_graph):
    obligations=rule_result['obligations']
    if not obligations:return None
    verify_data(data,config)
    expected=evaluate_joint_rule(case_graph,data)
    if rule_result!=expected or expected['status']!='UNRESOLVED' or len(obligations)!=1:
        raise ValueError('INVALID_NUMERIC_OBLIGATION')
    evidence=solve_joint(data,config)
    evidence['request_id']=obligations[0]['request_id']
    return evidence
