import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from types import SimpleNamespace

from dynamics_atlas_harness.nmr_agent.agent import Agent, RunConfig
from dynamics_atlas_harness.nmr_agent.reference_comparison import compare
from dynamics_atlas_harness.nmr_agent import exchange


class ReviewRepairs(unittest.TestCase):
    def test_reference_pair_uses_common_residues_and_preserves_sign(self):
        r = compare({'A1':0, 'A2':0, 'A3':0, 'A4':0},
                    {'A1':1, 'A2':2, 'A3':3, 'A4':10},
                    {'positive':{'A1':1,'A2':2,'A3':3,'A4':10},
                     'negative':{'A1':-1,'A2':-2,'A3':-3}}, ['A1','A2','A3','A4'])
        self.assertEqual(r['common_residues'], ['A1','A2','A3'])
        self.assertAlmostEqual(r['references']['negative']['pearson_r'], -1)
        self.assertEqual(r['references']['positive']['rmsd_ppm'], 0)
        self.assertEqual(r['references']['positive']['n'], r['references']['negative']['n'])

    def test_opposite_sign_is_explicitly_fitted(self):
        calls=[]
        def fit(*args, **kw):
            bounds=kw['dw_bounds']['A1'];calls.append(bounds)
            return SimpleNamespace(params={'dwN[A1]':0.01 if bounds[0]==0 else -0.01}, chi2=1.)
        e=SimpleNamespace(profiles={'A1':object()})
        with patch.object(exchange,'fit_two_state',side_effect=fit):
            r=exchange.cest_sign_scan(e,['A1'],{},400,.1,{'A1':120})['A1']
        self.assertIn((0.,25.), calls);self.assertIn((-25.,0.), calls)
        self.assertFalse(r['determined'])

    def test_result_retrieval_policy_and_path_boundary(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);ws=root/'ws';ws.mkdir();run=root/'run'
            (ws/'TASK.md').write_text('Neutral test')
            (ws/'large.txt').write_text('a'*12000+'critical contradictory evidence')
            (ws/'tool_policy.json').write_text(json.dumps({'allow_network_bmrb':False,
                'allowed_tools':['read_text','read_result','get_research_state','python']}))
            a=Agent(ws,run,RunConfig(arm='C'))
            data,err=a._execute('python',{'code':"print('x'*15000+'END_EVIDENCE')"})
            self.assertFalse(err);self.assertEqual(data['returncode'],0,data)
            oid=data['observation_id'];offset=0;parts=[]
            while True:
                page,_=a._execute('read_result',{'observation_id':oid,'offset':offset})
                parts.append(page['text']);offset=page['next_offset']
                if offset is None:break
            self.assertIn('END_EVIDENCE',''.join(parts))
            _,err=a._execute('bmrb_entry',{'entry_id':'123'})
            self.assertTrue(err)
            with self.assertRaises(PermissionError):a.tools._v('../outside')
            _,err=a._execute('read_text',{'path':'../secret'})
            self.assertTrue(err)
            a.log.close();a.calls.close()


if __name__=='__main__':unittest.main()
