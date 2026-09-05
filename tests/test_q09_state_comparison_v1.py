import copy,json
import unittest
from unittest.mock import patch
import numpy as np
from test_q09_forward_adequacy_v1 import synthetic,graph
from dynamics_atlas_harness.q09_shared_ibh_v1 import SharedIBH
from dynamics_atlas_harness import q09_state_comparison_v1 as s


def data():
    base=synthetic();d=SharedIBH.__new__(SharedIBH)
    for name in ('dt','t','r','qweights','rates','transfer_exp'):setattr(d,name,getattr(base,name))
    d.records={k:{'y':base.y['D0' if k=='D0_shared' else 'DA'].copy(),'irf':base.irf['DA'].copy(),'Lin':base.lin.copy(),'mask':base.mask.copy()} for k in ['D0_shared','19-119_DA','19-132_DA']}
    d.audit={'synthetic_expected_means_only':True};d.total=sum(v['y'].sum() for v in d.records.values());d.input_id=s.identity(d);return d

class ComparisonTests(unittest.TestCase):
    def test_sharedK3_can_exactly_represent_different_localK2_populations(self):
        d=data();r=s.equivalent_local_counterexample(d)
        self.assertLess(max(r['max_relative_count_differences']),1e-12)
        self.assertIn('EQUIVALENT_LOCAL_K2_EXPLANATION_EXISTS',r['judgment'])

    def test_sharedK2_embeds_localK2_and_zero_weightK3(self):
        d=data();p=[1.,4.,.3,.001,.2,35.,65.,.1,.001,.2,40.,70.,.2,.001,.3,.35]
        local=s.expand_fixed(p[:15],p[-1]);np.testing.assert_array_equal(s.reduce_local(local),p[:15])
        original=d.joint_counts(local);three=s.k3_counts(d,s.embed_k3(p))
        for role in original:np.testing.assert_allclose(original[role],three[role],rtol=1e-12,atol=1e-12)
        self.assertAlmostEqual(s.loss(d,p,'shared2'),s.loss(d,s.embed_k3(p),'shared3'),places=12)

    def test_shared_group_input_keys_are_bound(self):
        d=data();original=d.input_id;d.records=dict(reversed(list(d.records.items())));self.assertEqual(s.identity(d),original)
        old=d.records;d.records={'D0_shared':old['19-119_DA'],'19-119_DA':old['D0_shared'],'19-132_DA':old['19-132_DA']}
        self.assertNotEqual(s.identity(d),original)
        d.records['extra']=d.records['D0_shared']
        with self.assertRaises(ValueError):s.identity(d)

    def expected_evidence(self):
        d=data();p=[1.,4.,.3,.001,.2,35.,65.,.1,.001,.2,40.,70.,.2,.001,.3,.35]
        for k,mu in s.shared2_counts(d,p).items():d.records[k]['y']=mu
        d.input_id=s.identity(d);local=s.expand_fixed(p[:15],p[-1])
        def fit(params,bounds,fun,initial):
            return {'initial':list(initial),'parameters':list(params),'objective':float(fun(params)),'optimizer_success':True,'numerical_status':'PASS','projected_gradient_inf':float(max(abs(s.q.gradient_at(params,bounds,fun)))),'fixture':'SYNTHETIC_EXPECTED_MEAN_NOT_OPTIMIZER_RUN'}
        d.baseline=fit(local,s.LOCAL_BOUNDS,lambda x:d.deviance(x)/d.total,local);g=graph();rid=s.request(d,g)
        e={'schema':s.CONFIG['version'],'operator_id':s.OPERATOR_ID,'request_id':rid,'input_id':d.input_id,'config':s.CONFIG,'baseline':d.baseline,'profile_runs':[],'shared2_refinement':None,'K3_runs':[],'counterexample':s.equivalent_local_counterexample(d)}
        for pi in s.CONFIG['profile_pi']:
            for ori in s.CONFIG['orientations']:
                initial=s.reduce_local(local)
                if ori:initial[10:12]=initial[10:12][::-1]
                f={'initial':initial,'numerical_status':'TIME_BUDGET_STOP'}
                if pi==.35 and ori==0:f=fit(p[:15],s.FIXED_BOUNDS,lambda x:d.deviance(s.expand_fixed(x,pi))/d.total,initial)
                e['profile_runs'].append({'pi':pi,'orientation':ori,'fit':f})
        e['shared2_refinement']=fit(p,s.SHARED_BOUNDS,lambda x:s.loss(d,x,'shared2'),p)
        emb=s.embed_k3(p);e['K3_runs']=[fit(emb,s.K3_BOUNDS,lambda x:s.loss(d,x,'shared3'),emb),{'initial':emb[:-2]+[.2,.625],'numerical_status':'TIME_BUDGET_STOP'}]
        return d,g,e

    def test_positive_numeric_reassessment_and_reject_mutations(self):
        d,g,e=self.expected_evidence()
        with patch.object(s.q,'optimize',side_effect=AssertionError('No replay optimization')):r=s.evaluate(g,d,e)
        self.assertIn('BOUND_SHARED_LOCAL_COMPARISON_RECOMPUTED',r['reason_codes'])
        self.assertFalse(r['complete_question_answer']);self.assertEqual(r['comparison']['protein_state_number'],'UNRESOLVED')
        json.dumps(r)  # NumPy bool regression at final serialization boundary.
        for kind in ['seed','gradient','counterexample','input']:
            bad=copy.deepcopy(e)
            if kind=='seed':bad['profile_runs'][0]['pi']=.99
            if kind=='gradient':bad['shared2_refinement']['projected_gradient_inf']=.9
            if kind=='counterexample':bad['counterexample']['max_relative_count_differences'][0]=.9
            if kind=='input':bad['input_id']='wrong'
            self.assertEqual(s.evaluate(g,d,bad)['reason_codes'],['COMPARISON_EVIDENCE_REJECTED'],kind)

    def test_rule_off_does_not_call_comparison(self):
        d=data();g=graph();r=s.evaluate(g,d,enabled=False)
        with patch.object(s,'run') as run:self.assertIsNone(s.dispatch(r,d,g));run.assert_not_called()

if __name__=='__main__':unittest.main()
