import copy
import unittest
from dynamics_atlas_harness.q15_dye_evidence_v2 import histogram_direction, summarize_dye_evidence
from dynamics_atlas_harness import q15_cross_modal_evidence_v1 as q
from test_q15_cross_modal_evidence_v1 import inputs, admitted


def sources():
    hist = dict(role='PUBLISHED_MEASURED_HISTOGRAM_BARS_NOT_FITTED_CURVES',
        variant='HiSiaP175/228', dye_pair='TMR/Cy5', frames={c:[0,100,0,50] for c in ['apo','holo']},
        bins={c:[dict(left_pt=x,right_pt=x+1,height_pt=20)] for c,x in [('apo',20),('holo',70)]})
    results = {}
    for name, ratio in [('175_AF555',.6),('58_AF555',1.05),('175_TMR',.99)]:
        results[name] = {}
        for c, late in [('apo',.2),('holo',.2*ratio)]:
            results[name][c] = {'windows': {
                'early': dict(delay_ns=[2.,4.],mean_peak_normalized_intensity=.5),
                'late': dict(delay_ns=[6.,8.],mean_peak_normalized_intensity=late,
                    intensity_weighted_anisotropy=.1 if name=='175_TMR' else .25)}}
    return dict(histogram=hist,dye_summary=dict(status='SOURCE_LABELLED_DYE_POSITION_OBSERVATIONS',results=results),
        concordance=dict(status='NUMERIC_WORKBOOK_CSV_MATCH_WITH_PDF_CY5_VISUAL_DISCREPANCY'))


class DyeTests(unittest.TestCase):
    def test_histogram_reverse_overlap_and_missing_change_text(self):
        s=sources()['histogram']
        self.assertEqual(histogram_direction(s)['direction'],'RIGHT')
        s['bins']['apo'],s['bins']['holo']=s['bins']['holo'],s['bins']['apo']
        r=histogram_direction(s)
        self.assertEqual(r['direction'],'LEFT');self.assertNotIn('向右',r['sentence'])
        s['bins']['holo']=copy.deepcopy(s['bins']['apo'])
        self.assertEqual(histogram_direction(s)['direction'],'GEOMETRIC_DIRECTION_UNRESOLVED')
        s['bins']['holo']=[]
        self.assertEqual(histogram_direction(s)['direction'],'SOURCE_INSUFFICIENT')

    def test_relations_follow_both_bound_directions(self):
        args=inputs();e=q.synthesize_manual_evidence(*args);s=sources()
        d=summarize_dye_evidence(s,e);self.assertEqual(d['Alexa_relation'],'OPPOSITE')
        s['histogram']['bins']['apo'],s['histogram']['bins']['holo']=s['histogram']['bins']['holo'],s['histogram']['bins']['apo']
        d=summarize_dye_evidence(s,e)
        self.assertEqual(d['Alexa_relation'],'SAME');self.assertEqual(d['DEER_relation'],'TENSION')
        self.assertNotIn('向右',d['histogram_answer'])
        row=next(r for r in e['rows'] if r['pair']=='175_228');row['observed_E_effect']=.1
        self.assertEqual(summarize_dye_evidence(s,e)['Alexa_relation'],'OPPOSITE')

    def test_same_instance_off_tampered_evidence_and_prior_source_guard(self):
        args=inputs();kw=admitted(args);e=q.synthesize_manual_evidence(*args);s=sources()
        receipt=dict(main_input_id='x',sources={k:dict(canonical_sha256=q.canonical_digest(v)) for k,v in s.items()})
        d=summarize_dye_evidence(s,e)
        more=dict(dye_sources=s,dye_receipt=receipt,dye_evidence=d)
        before=q.evaluate(args[0],e,**kw);after=q.evaluate(args[0],e,**kw,**more)
        self.assertEqual(before['rule_instance_id'],after['rule_instance_id'])
        self.assertFalse(after['full_question_answer'])
        self.assertNotIn('question_answer_candidate',q.evaluate(args[0],e,False,**kw,**more))
        d['histogram_answer']='Unique mechanism proven'
        with self.assertRaisesRegex(ValueError,'BOUND_NUMBERS'):q.evaluate(args[0],e,**kw,**more)
        more['dye_evidence']=summarize_dye_evidence(s,e)
        s['histogram']['bins']['holo'][0]['left_pt']+=.1
        more['dye_evidence']=summarize_dye_evidence(s,e)
        with self.assertRaisesRegex(ValueError,'PREVIOUSLY_ADMITTED'):q.evaluate(args[0],e,**kw,**more)

    def test_probe_conclusion_follows_numeric_change(self):
        s=sources();e=q.synthesize_manual_evidence(*inputs())
        d=summarize_dye_evidence(s,e);self.assertTrue(d['replacement_donor_reduces_observed_concern'])
        s['dye_summary']['results']['175_TMR']['holo']['windows']['late']['mean_peak_normalized_intensity']=.001
        d=summarize_dye_evidence(s,e);self.assertFalse(d['replacement_donor_reduces_observed_concern'])
        self.assertIn('没有显示更小',d['probe_answer'])


if __name__=='__main__':unittest.main()
