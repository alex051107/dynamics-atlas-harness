"""Q09 all33 conditional comparison using60 unique records and native grids.

No model-selection p value or scientific PASS. Same Q09R02 obligation, larger
explicit evidence set; original author fitted targets never loaded.
"""
from pathlib import Path
import hashlib, json, time, zipfile
import numpy as np
from scipy.optimize import minimize
from scipy.special import ndtr
from numpy.polynomial.legendre import leggauss
from .q09_fluorescence_v1 import PQPair, expected_counts, linearization_reference, poisson_deviance
from .q09_shared_ibh_v1 import read_ibh
from . import q09_forward_adequacy_v1 as q
from .q09_state_comparison_v1 import RULE_ID

OPERATOR_ID='q09_all33_conditional_comparison_v1'
STRUCTURE_OPERATOR_ID='q09_author_forward_structure_comparison_v1'
CONFIG={'version':'q09-all33/v1','models':['local2','shared2','shared3'],
 'donor_order':'3 only22-127;2 other26referencegroups;explicit exploratory hypothesis,NOTadequacyPASS',
 'sigma_A':6.,'distance_bounds_A':[10.,120.],'scatter':0.,'periodic':False,
 'IRF':'original per-recordtail256validmedian subtractclip',
 'window':'IBH17HanningLin>10percentpositiveMedian;PQallnativebinsLin1',
 'local_seconds':60,'global_seconds':120,'maxiter':1500,'shared2_starts':[.35,.65],
 'shared3_starts':['zero_weight_shared2','nonzero_.2_.5_.3'],
 'local_physical_gradient_tolerance':1e-6,'shared_physical_gradient_tolerance':1e-6,
 'claim_ceiling':'Conditional candidate comparison; no absolute adequacy or proteinstateverdict'}
ROOT=q.REPO/'research/paper_result_reproduction_screen_v1'

class Native(PQPair):
    def __init__(self,n,dt,quadrature=256):
        self.dt=dt;self.t=np.arange(n)*dt
        nodes,w=leggauss(quadrature);self.r=(nodes+1)*90;self.qweights=w*90
        self.rates=.224*(2/3)*(56.4/self.r)**6
        self.transfer_exp=np.exp(-self.t[:,None]*self.rates)

class Group:
    def __init__(self,ref,owners,records,donors):
        self.ref=ref;self.owners=owners;self.records=records;self.donors=donors
    @property
    def total(self):return sum(float(r['y'][r['mask']].sum()) for r in self.records.values())
    @property
    def donor_size(self):return 2*self.donors+1
    def bounds(self,kind):
        d=self.donors;b=[(.05,10.)]*d+[(0.,1.)]*(d-1)+[(1e-12,.05),(-5.,5.)]
        per=[(10.,120.)]*(3 if kind=='shared3' else 2)
        if kind=='local2':per+=[(0.,1.)]
        return b+(per+[(0.,1.),(1e-12,.05),(-5.,5.)])*len(self.owners)
    def initial(self):
        out=[1.,4.,.3,.001,0.] if self.donors==2 else [1.,4.,.5,.3,.6,.001,0.]
        return out+[35.,65.,.5,.2,.001,0.]*len(self.owners)
    def predict(self,p,kind,pop=None):
        n=self.donors;tau=p[:n];a=[p[n],1-p[n]] if n==2 else q.amplitudes(*p[n:n+2])
        offset=self.donor_size;bg,shift=p[offset-2:offset];out={}
        r=self.records[self.ref];intrinsic=r['kernel'].intrinsic_donor(tau,a)
        out[self.ref]=expected_counts(intrinsic,r['irf'],r['Lin'],r['mask'],float(r['y'][r['mask']].sum()),shift_bins=shift,background_fraction=bg)
        step=6 if kind in ('local2','shared3') else 5
        for i,v in enumerate(self.owners):
            pp=p[offset+step*i:offset+step*(i+1)];nr=3 if kind=='shared3' else 2
            means=pp[:nr];weights=([pp[nr],1-pp[nr]] if kind=='local2' else pop)
            f0,bg,shift=pp[-3:];r=self.records[v]
            _,intrinsic=r['kernel'].intrinsic_pair(tau,a,means,weights,f0)
            out[v]=expected_counts(intrinsic,r['irf'],r['Lin'],r['mask'],float(r['y'][r['mask']].sum()),shift_bins=shift,background_fraction=bg)
        return out
    def contributions(self,p,kind,pop=None):
        pred=self.predict(p,kind,pop)
        return {k:poisson_deviance(r['y'][r['mask']],pred[k][r['mask']]) for k,r in self.records.items()}
    def deviance(self,p,kind,pop=None):return sum(self.contributions(p,kind,pop).values())
    def from_local(self,p,kind):
        out=list(p[:self.donor_size])
        for i in range(len(self.owners)):
            row=p[self.donor_size+6*i:self.donor_size+6*(i+1)]
            out+=list(row[:2])+([(row[0]+row[1])/2] if kind=='shared3' else [])+list(row[-3:])
        return out

class GlobalData:
    def __init__(self,input_root,manifest_root=ROOT/'q09_global_ownership_v1'):
        base=Path(input_root);self.mapping=json.loads((Path(manifest_root)/'records.json').read_text())
        ownership=json.loads((Path(manifest_root)/'reference_ownership.json').read_text())
        if len(self.mapping)!=66 or len(ownership)!=27:raise ValueError('FULL33_OWNERSHIP_REQUIRED')
        records={};kernels={};checked=set();seen={}
        with zipfile.ZipFile(base/'eTCSPC_wildtype.zip') as z:
            def path(relative):
                f=base/'unpacked/eTCSPC'/relative
                if relative not in checked:
                    if f.read_bytes()!=z.read('eTCSPC/'+relative):raise ValueError('SOURCE_BYTE_MISMATCH')
                    checked.add(relative)
                return f
            for row in self.mapping:
                src=row['source'];path(row['metadata'])
                if src['instrument']=='IBH':
                    y,_=read_ibh(path(src['decay']));irf,_=read_ibh(path(src['irf']));rawlin,_=read_ibh(path(src['linearization']))
                    lin=linearization_reference(rawlin);mask=lin>.1*np.median(lin[lin>0]);dt=.0141
                elif src['instrument']=='PQ':
                    ytable=np.loadtxt(path(src['decay']));htable=np.loadtxt(path(src['irf']));dt=.008
                    if ytable.shape!=htable.shape or ytable.shape[1]!=2 or not np.array_equal(ytable[:,0],htable[:,0]) or not np.allclose(ytable[:,0],np.arange(len(ytable))*dt,rtol=0,atol=1e-10):raise ValueError('PQ_NATIVE_AXIS_MISMATCH')
                    y=ytable[:,1];irf=htable[:,1];lin=np.ones_like(y);mask=np.ones(len(y),bool)
                else:raise ValueError('UNKNOWN_INSTRUMENT')
                if np.any(y<0) or not np.all(y==np.floor(y)) or np.any(irf<0) or not np.all(irf==np.floor(irf)):raise ValueError('INVALID_SOURCE_COUNTS')
                irf=np.maximum(irf-float(np.median(irf[np.flatnonzero(mask)[-256:]])),0)
                key=row['decay_record'];kernelkey=(len(y),dt)
                if kernelkey not in kernels:kernels[kernelkey]=Native(*kernelkey)
                r={'y':y,'irf':irf,'Lin':lin,'mask':mask,'kernel':kernels[kernelkey]}
                if key in records:
                    if any(not np.array_equal(r[k],records[key][k]) for k in ('y','irf','Lin','mask')) or records[key]['kernel'].dt!=dt:raise ValueError('SHARED_REFERENCE_METHOD_CONFLICT')
                else:records[key]=r
                seen[(row['variant'],row['role'])]=key
        self.groups=[]
        for owner in ownership:
            ref=owner['record_id'];variants=owner['owners']
            if any(seen[(v,'D0')]!=ref for v in variants):raise ValueError('REFERENCE_OWNER_MISMATCH')
            rs={ref:records[ref],**{v:records[seen[(v,'DA')]] for v in variants}}
            self.groups.append(Group(ref,variants,rs,3 if variants==['22-127'] else 2))
        self.audit={'variants':sorted({v for g in self.groups for v in g.owners}),'reference_groups':len(self.groups),'unique_records':len(records),'checked_source_files':len(checked),'raw_photons':int(sum(r['y'].sum() for r in records.values())),'fit_photons':int(self.total),'donor_components':{g.ref:g.donors for g in self.groups},'source_mapping':self.mapping,'reference_exchangeability':'CONDITIONAL_UNKNOWN','independent_biological_replicates':'NOT_ESTABLISHED','calibration_uncertainty':'NOT_PROPAGATED_IN_THIS_CONDITIONAL_BATCH'}
        if len(self.audit['variants'])!=33 or len(records)!=60 or self.audit['raw_photons']!=1579507556:raise ValueError('FULL33_SOURCE_ACCOUNTING_MISMATCH')
        self.input_id=self.identity()
    @property
    def total(self):return sum(g.total for g in self.groups)
    def identity(self):
        h=hashlib.sha256(json.dumps({'mapping':self.mapping,'config':CONFIG},sort_keys=True).encode())
        for g in self.groups:
            h.update(json.dumps([g.ref,g.owners,g.donors]).encode())
            for role,r in g.records.items():
                for key in ('y','irf','Lin','mask'):
                    a=r[key];h.update((role+':'+key).encode());h.update(str(a.shape).encode());h.update(a.dtype.str.encode());h.update(a.tobytes())
                h.update(str(r['kernel'].dt).encode())
                for key in ('t','r','qweights','rates','transfer_exp'):
                    arr=getattr(r['kernel'],key);h.update(key.encode());h.update(arr.tobytes())
        return h.hexdigest()
    def verify(self):
        if self.identity()!=self.input_id:raise ValueError('GLOBAL_INPUT_MUTATED')

class Joint:
    def __init__(self,data,kind):
        self.data=data;self.kind=kind;self.slices=[];self.bounds=[]
        for g in data.groups:
            b=g.bounds(kind);self.slices.append(slice(len(self.bounds),len(self.bounds)+len(b)));self.bounds+=b
        self.nlocal=len(self.bounds);self.bounds += [(0.,1.)]*(2 if kind=='shared3' else 1)
        self.lo=np.array([b[0] for b in self.bounds]);self.span=np.array([b[1]-b[0] for b in self.bounds]);self.cache={}
    def population(self,p):return q.amplitudes(*p[-2:]) if self.kind=='shared3' else [p[-1],1-p[-1]]
    def group_loss(self,i,p):
        key=(i,tuple(p[self.slices[i]]),tuple(p[self.nlocal:]))
        if key not in self.cache:
            if len(self.cache)>2000:self.cache.clear()
            self.cache[key]=self.data.groups[i].deviance(p[self.slices[i]],self.kind,self.population(p))
        return self.cache[key]
    def objective(self,p):return sum(self.group_loss(i,p) for i in range(len(self.slices)))/self.data.total
    def jac_scaled(self,z,check_time=lambda:None):
        grad=np.zeros(len(z));p=self.lo+self.span*z
        for j in range(len(z)):
            check_time();h=1e-5*max(abs(z[j]),.001);a=z.copy();b=z.copy();a[j]=min(1,z[j]+h);b[j]=max(0,z[j]-h)
            pa=self.lo+self.span*a;pb=self.lo+self.span*b
            if j<self.nlocal:
                i=next(i for i,sl in enumerate(self.slices) if sl.start<=j<sl.stop)
                diff=self.group_loss(i,pa)-self.group_loss(i,pb)
            else:diff=sum(self.group_loss(i,pa)-self.group_loss(i,pb) for i in range(len(self.slices)))
            grad[j]=diff/(a[j]-b[j])/self.data.total
        return grad
    def stationary(self,p):
        grad=self.jac_scaled((np.array(p)-self.lo)/self.span)/self.span
        for i,(lo,hi) in enumerate(self.bounds):
            if (p[i]<=lo+1e-7 and grad[i]>0) or (p[i]>=hi-1e-7 and grad[i]<0):grad[i]=0
        local={g.ref:float(np.max(abs(grad[sl]))*self.data.total/g.total) for g,sl in zip(self.data.groups,self.slices)}
        return {'group_scaled_physical_gradient':local,'shared_physical_gradient':float(max(abs(grad[self.nlocal:]))),'global_scaled_physical_gradient':float(max(abs(grad)))}

def optimize_local(g,initial):
    bounds=g.bounds('local2');lo=np.array([b[0] for b in bounds]);span=np.array([b[1]-b[0] for b in bounds]);start=time.monotonic();best={'parameters':list(initial),'objective':g.deviance(initial,'local2')/g.total};calls=0
    def fun(z):
        nonlocal calls
        if time.monotonic()-start>CONFIG['local_seconds']:raise TimeoutError('LOCAL_TIME_BUDGET')
        calls+=1;p=lo+span*z;v=g.deviance(p,'local2')/g.total
        if v<best['objective']:best.update(parameters=p.tolist(),objective=float(v))
        return v
    def jac(z):
        out=[]
        for i in range(len(z)):
            h=1e-5*max(abs(z[i]),.001);a=z.copy();b=z.copy();a[i]=min(1,z[i]+h);b[i]=max(0,z[i]-h);out.append((fun(a)-fun(b))/(a[i]-b[i]))
        return np.array(out)
    success=False;message='';nit=None
    try:
        fit=minimize(fun,(np.array(initial)-lo)/span,jac=jac,method='L-BFGS-B',bounds=[(0,1)]*len(lo),options={'maxiter':CONFIG['maxiter'],'ftol':1e-15,'gtol':1e-11,'maxfun':20000});success=bool(fit.success);message=str(fit.message);nit=int(fit.nit)
    except TimeoutError as e:message=str(e)
    pg=float(max(abs(q.gradient_at(best['parameters'],bounds,lambda p:g.deviance(p,'local2')/g.total))))
    return dict(best,initial=initial,optimizer_success=success,iterations=nit,evaluations=calls,message=message,projected_gradient_inf=pg,numerical_status='PASS' if success and pg<=1e-6 else 'NUMERICAL_STOP_WITH_FEASIBLE_POINT',elapsed_seconds=time.monotonic()-start,kind='ACTUAL_OPTIMIZER')

def optimize_global(j,initial):
    start=time.monotonic();best={'parameters':list(initial),'objective':float(j.objective(initial))};calls=0
    def timer():
        if time.monotonic()-start>CONFIG['global_seconds']:raise TimeoutError('GLOBAL_TIME_BUDGET')
    def fun(z):
        nonlocal calls
        timer();calls+=1;p=j.lo+j.span*z;v=j.objective(p)
        if v<best['objective']:best.update(parameters=p.tolist(),objective=float(v))
        return v
    success=False;nit=None
    try:
        fit=minimize(fun,(np.array(initial)-j.lo)/j.span,jac=lambda z:j.jac_scaled(z,timer),method='L-BFGS-B',bounds=[(0,1)]*len(initial),options={'maxiter':CONFIG['maxiter'],'maxfun':20000,'ftol':1e-15,'gtol':1e-11});success=bool(fit.success);message=str(fit.message);nit=int(fit.nit)
    except TimeoutError as e:message=str(e)
    ck=j.stationary(best['parameters']);ok=max(ck['group_scaled_physical_gradient'].values())<=1e-6 and ck['shared_physical_gradient']<=1e-6
    return dict(best,initial=initial,optimizer_success=success,iterations=nit,evaluations=calls,message=message,convergence=ck,numerical_status='PASS' if success and ok else 'NUMERICAL_STOP_WITH_FEASIBLE_POINT',elapsed_seconds=time.monotonic()-start,kind='ACTUAL_OPTIMIZER')

def reuse_local(g):
    if g.owners==['19-119','19-132']:
        runs=json.loads((ROOT/'q09_shared_ibh_v1/joint_runs.json').read_text());r=min((r for r in runs if r['numerical_status']=='PASS'),key=lambda r:r['scaled_objective']);p=r['parameters'];objective=r['scaled_objective'];source='q09_shared_ibh_v1/joint_runs.json'
    elif g.owners==['22-127']:
        ev=json.loads((ROOT/'q09_role_bound_readmission_v2/forward/evidence.json').read_text())
        runs=ev['joint_runs'];r=min((r for r in runs if r['numerical_status']=='PASS'),key=lambda r:r['objective']);old=r['parameters'];p=old[:5]+old[9:11]+old[5:9]+old[11:13];objective=r['objective'];source='q09_role_bound_readmission_v2/forward/evidence.json'
    else:return None
    actual=g.deviance(p,'local2')/g.total
    if not np.isclose(actual,objective,rtol=1e-9,atol=1e-11):raise ValueError('REUSED_LOCAL_NATIVE_KERNEL_OR_MAPPING_MISMATCH')
    pg=float(max(abs(q.gradient_at(p,g.bounds('local2'),lambda x:g.deviance(x,'local2')/g.total))))
    if pg>1e-6:raise ValueError('REUSED_LOCAL_GRADIENT_FAILED')
    return {'parameters':p,'objective':actual,'kind':'REUSED_VERIFIED_NO_OPTIMIZATION','source':source,'projected_gradient_inf':pg,'numerical_status':'PASS'}

def run(data,request_id,save):
    data.verify();e={'schema':CONFIG['version'],'operator_id':OPERATOR_ID,'request_id':request_id,'input_id':data.input_id,'config':CONFIG,'local_runs':{},'shared2_runs':[],'shared3_runs':[]}
    for g in data.groups:
        r=reuse_local(g)
        if r is None:r=optimize_local(g,g.initial())
        e['local_runs'][g.ref]=r;save(e)
    for pi in CONFIG['shared2_starts']:
        initial=sum((g.from_local(e['local_runs'][g.ref]['parameters'],'shared2') for g in data.groups),[])+[pi]
        e['shared2_runs'].append(optimize_global(Joint(data,'shared2'),initial));save(e)
    best=min(e['shared2_runs'],key=lambda r:r['objective']);j2=Joint(data,'shared2')
    for seed in (0,1):
        initial=[]
        for g,sl in zip(data.groups,j2.slices):
            p=best['parameters'][sl];initial+=p[:g.donor_size]
            for i in range(len(g.owners)):
                row=p[g.donor_size+5*i:g.donor_size+5*(i+1)];initial+=row[:2]+[(row[0]+row[1])/2]+row[-3:]
        initial += [best['parameters'][-1],1.] if seed==0 else [.2,.625]
        e['shared3_runs'].append(optimize_global(Joint(data,'shared3'),initial));save(e)
    return e

def request(data,g):return q.digest({'input':data.input_id,'graph':g,'config':CONFIG,'rule':RULE_ID,'operator':OPERATOR_ID})

def evaluate(g,data,e=None,enabled=True,structure_evidence=None):
    instance=q.rule_instance_id(RULE_ID,'CASE',g['case']['case_id'])
    out={'rule_instance_id':instance,'status':'UNRESOLVED','obligations':[],'reason_codes':[],'complete_question_answer':False}
    if not enabled:out['status']='NOT_APPLICABLE';return out
    q._validate_graph(g);data.verify()
    if g['case']['case_id']!='q09_t4l_state_number_20260905' or g['case']['requested_claim_level']!='STATE_NUMBER_AND_STRUCTURE_CONSISTENCY':raise ValueError('CLAIM_NOT_APPLICABLE')
    registry=json.loads((q.REPO/'registries/rules_v1/q09_state_comparison_rule_v1.json').read_text())
    if registry['global_operator_id']!=OPERATOR_ID or registry['scientific_pass_enabled']:raise ValueError('UNSUPPORTED_GLOBAL_COMPARISON')
    rid=request(data,g);out['request_id']=rid
    obligation={'operator_id':OPERATOR_ID,'request_id':rid,'input_id':data.input_id,'rule_instance_id':instance,'variants':data.audit['variants']}
    if e is None:out.update(obligations=[obligation],reason_codes=['ALL33_SAME_RECORD_COMPARISON_REQUIRED']);return out
    try:report=verify(data,e,rid)
    except (ValueError,KeyError,TypeError) as err:out.update(obligations=[obligation],reason_codes=['COMPARISON_EVIDENCE_REJECTED'],rejection_reason=str(err));return out
    out['comparison']=report;out['reason_codes']=['BOUND_ALL33_COMPARISON_RECOMPUTED']
    if report['numerical_status']!='COMPLETE_LOCAL_SEARCH_BUDGET':out['reason_codes'].append('SOLVER_COMPARISON_INCOMPLETE')
    else:out['reason_codes'].append('MODEL_SELECTION_CALIBRATION_REQUIRED')
    out['reason_codes'].append('DONOR_AND_INSTRUMENT_ADEQUACY_NOT_ESTABLISHED')
    if structure_evidence is None:
        out['reason_codes'].append('STRUCTURE_FORWARD_EVIDENCE_REQUIRED')
        out['obligations']=[{'operator_id':STRUCTURE_OPERATOR_ID,'rule_instance_id':instance,'input_id':data.input_id,'comparison_evidence_id':q.digest(e),'purpose':'Compare own conditional mean distances with source-attributed author forward predictions'}]
    else:
        try:
            expected=structure_comparison(data,e,report)
            if structure_evidence!=expected:raise ValueError('STRUCTURE_COMPARISON_NOT_RECOMPUTED')
            out['structure_comparison']=expected;out['reason_codes'].append('AUTHOR_FORWARD_STRUCTURE_COMPARISON_ASSESSED_WITH_LIMITS')
        except (ValueError,KeyError,TypeError) as error:
            out['reason_codes'].append('STRUCTURE_EVIDENCE_REJECTED');out['structure_rejection']=str(error)
    return out

def verify(data,e,rid):
    data.verify()
    if any(e[k]!=v for k,v in [('schema',CONFIG['version']),('operator_id',OPERATOR_ID),('request_id',rid),('input_id',data.input_id),('config',CONFIG)]):raise ValueError('GLOBAL_EVIDENCE_BINDING_MISMATCH')
    if set(e['local_runs'])!={g.ref for g in data.groups} or len(e['shared2_runs'])!=2 or len(e['shared3_runs'])!=2:raise ValueError('ALL33_CANDIDATES_INCOMPLETE')
    def fitcheck(r,bounds,fun,convergence):
        p=np.asarray(r['parameters']);lo=np.array([b[0] for b in bounds]);hi=np.array([b[1] for b in bounds])
        if p.shape!=lo.shape or not np.all(np.isfinite(p)) or np.any(p<lo) or np.any(p>hi):raise ValueError('GLOBAL_PARAMETER_BOUNDS')
        actual=float(fun(p))
        if not np.isclose(actual,r['objective'],atol=1e-11,rtol=1e-8):raise ValueError('GLOBAL_OBJECTIVE_MISMATCH')
        ck=convergence(p)
        if r['numerical_status']=='PASS' and (not ck or (r.get('kind')=='ACTUAL_OPTIMIZER' and r.get('optimizer_success') is not True)):raise ValueError('GLOBAL_FALSE_NUMERIC_PASS')
        if r['numerical_status'] not in ('PASS','NUMERICAL_STOP_WITH_FEASIBLE_POINT'):raise ValueError('UNSUPPORTED_NUMERIC_STATUS')
        return actual
    local=0;local_contributions={};stops=[]
    for gr in data.groups:
        r=e['local_runs'][gr.ref]
        reused=reuse_local(gr)
        if reused is not None:
            if r!=reused:raise ValueError('REUSED_LOCAL_EVIDENCE_CHANGED')
        elif r.get('initial')!=gr.initial() or r.get('kind')!='ACTUAL_OPTIMIZER':raise ValueError('UNDECLARED_LOCAL_START')
        fun=lambda p:gr.deviance(p,'local2')/gr.total
        local+=fitcheck(r,gr.bounds('local2'),fun,lambda p:max(abs(q.gradient_at(p,gr.bounds('local2'),fun)))<=1e-6)*gr.total
        local_contributions[gr.ref]=gr.contributions(r['parameters'],'local2')
        if r['numerical_status']!='PASS':stops.append('local2:'+gr.ref)
    results={};bestparams={}
    for kind in ('shared2','shared3'):
        j=Joint(data,kind);valid=[]
        for i,r in enumerate(e[kind+'_runs']):
            initial=global_initial(data,e,kind,i)
            if r.get('initial')!=initial or r.get('kind')!='ACTUAL_OPTIMIZER':raise ValueError('UNDECLARED_GLOBAL_START')
            def conv(p):
                ck=j.stationary(p)
                return max(ck['group_scaled_physical_gradient'].values())<=1e-6 and ck['shared_physical_gradient']<=1e-6
            val=fitcheck(r,j.bounds,j.objective,conv);valid.append((val,r))
            if r['numerical_status']!='PASS':stops.append(kind+':'+str(i))
        val,r=min(valid,key=lambda x:x[0]);bestparams[kind]=r['parameters']
        results[kind]={'deviance':val*data.total,'population':j.population(r['parameters']),'contributions':{gr.ref:gr.contributions(r['parameters'][sl],kind,j.population(r['parameters'])) for gr,sl in zip(data.groups,j.slices)},'selected_kind':'BEST_FEASIBLE_WITH_RECORDED_STOPS','bound_hits':[i for i,(v,b) in enumerate(zip(r['parameters'],j.bounds)) if min(abs(v-b[0]),abs(v-b[1]))<1e-5]}
    results['local2']={'deviance':local,'contributions':local_contributions}
    ordering={'local2_le_shared2':bool(local<=results['shared2']['deviance']+1e-5),'shared3_le_shared2':bool(results['shared3']['deviance']<=results['shared2']['deviance']+1e-5)}
    return {'models':results,'numerical_stops':stops,'nested_feasible_order':ordering,'numerical_status':'COMPLETE_LOCAL_SEARCH_BUDGET' if not stops and all(ordering.values()) else 'NUMERICAL_COMPARISON_INCOMPLETE','observed_records':60,'variants':33,'total_photons':data.total,'protein_state_number':'UNRESOLVED','local2_to_shared3_relation':'No automatic two-variant nesting claim for33variants','best_parameters':bestparams}

def dispatch(before,data,g,save):
    if not before['obligations']:return None
    if before!=evaluate(g,data):raise ValueError('INVALID_ALL33_OBLIGATION')
    return run(data,before['request_id'],save)


def global_initial(data,e,kind,seed):
    if kind=='shared2':
        return sum((g.from_local(e['local_runs'][g.ref]['parameters'],'shared2') for g in data.groups),[])+[CONFIG['shared2_starts'][seed]]
    best=min(e['shared2_runs'],key=lambda r:r['objective']);j2=Joint(data,'shared2');initial=[]
    for g,sl in zip(data.groups,j2.slices):
        p=best['parameters'][sl];initial+=p[:g.donor_size]
        for i in range(len(g.owners)):
            row=p[g.donor_size+5*i:g.donor_size+5*(i+1)];initial+=row[:2]+[(row[0]+row[1])/2]+row[-3:]
    return initial+([best['parameters'][-1],1.] if seed==0 else [.2,.625])


def structure_comparison(data,e,report):
    """Descriptive mean-to-mean comparisons, never a model selection test.

    Preserve all global assignments; no individual variant label sorting.
    Author uncertainties/experimental fitted targets are not read.
    """
    import itertools
    source=json.loads((ROOT/'q09_deposited_structure_intake_v1/author_forward_predictions.json').read_text())
    if set(source['predictions'])!={'172L','148L'} or source['local_ACV_runs']!=0:raise ValueError('STRUCTURE_SOURCE_ROLE_MISMATCH')
    expected_pairs={v.replace('-','_') for v in data.audit['variants']}
    if any(set(row)!=expected_pairs for row in source['predictions'].values()):raise ValueError('STRUCTURE_PAIR_SET_MISMATCH')
    def mean(mu):return float(mu+6*np.exp(-.5*(mu/6)**2)/(np.sqrt(2*np.pi)*ndtr(mu/6)))
    result={'schema':'q09-author-structure-comparison/v1','operator_id':STRUCTURE_OPERATOR_ID,'input_id':data.input_id,'comparison_evidence_id':q.digest(e),'source':source,'claim':'DESCRIPTIVE_CONDITIONAL_MEAN_RESIDUALS_ONLY','local_ACV_runs':0,'uncertainty':'No validated joint fit/forward uncertainty; no standardizedscores,thresholdPASSorproteinstateconclusion','models':{}}
    for kind in ('shared2','shared3'):
        j=Joint(data,kind);p=report['best_parameters'][kind];n=2 if kind=='shared2' else 3;means={}
        for gr,sl in zip(data.groups,j.slices):
            local=p[sl];step=5 if n==2 else 6
            for i,v in enumerate(gr.owners):means[v.replace('-','_')]=[mean(mu) for mu in local[gr.donor_size+step*i:gr.donor_size+step*i+n]]
        assignments=[]
        for perm in itertools.permutations(range(n),2):
            residuals={pdb:{v:means[v][comp]-expected for v,expected in source['predictions'][pdb].items()} for pdb,comp in zip(('172L','148L'),perm)}
            flat=[x for r in residuals.values() for x in r.values()]
            assignments.append({'172L_component':perm[0],'148L_component':perm[1],'residuals_A':residuals,'RMS_A':float(np.sqrt(np.mean(np.square(flat)))),'max_absolute_A':float(max(abs(x) for x in flat))})
        result['models'][kind]={'actual_truncated_distance_means_A':means,'global_assignments':assignments,'fit_search_status':report['numerical_status'],'component_number_is_not_protein_state_identity':True}
    return result


def dispatch_structure(before,data,g,e):
    if not before['obligations']:return None
    if before!=evaluate(g,data,e) or len(before['obligations'])!=1 or before['obligations'][0]['operator_id']!=STRUCTURE_OPERATOR_ID:raise ValueError('INVALID_STRUCTURE_OBLIGATION')
    registry=json.loads((q.REPO/'registries/rules_v1/q09_state_comparison_rule_v1.json').read_text())
    if registry['structure_operator_id']!=STRUCTURE_OPERATOR_ID:raise ValueError('UNREGISTERED_STRUCTURE_OPERATOR')
    return structure_comparison(data,e,before['comparison'])
