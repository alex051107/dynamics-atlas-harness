import copy
import unittest
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from dynamics_atlas_harness import q15_cross_modal_evidence_v1 as q


def inputs():
    main={'input_id':'x','condition_comparisons':{p:{'holo_minus_apo_E':.1 if p=='55_175' else -.1} for p in q.PAIRS}}
    summary={'input_id':'x','diagnostics':{p:{'equal_repetition_mean_effect':r['holo_minus_apo_E'],
              'equal_repetition_median_effect':r['holo_minus_apo_E'],'leave_one_per_condition_effects':[r['holo_minus_apo_E']]*9} for p,r in main['condition_comparisons'].items()}}
    deer={'source_role':'AUTHOR_PROCESSED_DEER_DISTRIBUTION_NOT_RAW_TRACE_REINVERSION',
          'curves':[{'pair':p.replace('_','/'),'condition':s,'mean_source_axis_units':v} for p in q.PAIRS for s,v in [('apo',50),('holo',40)]]}
    forward={'pairs':{p:{k:{'apo':50,'holo':40} for k in ['FRET_sim','PELDOR_sim']} for p in q.PAIRS},
             'system':'HiSiaP','doi':'10.1038/s41467-022-31945-6','source_role':'AUTHOR_COMPUTED_FORWARD_NOT_LOCAL_SIMULATION'}
    return main,summary,deer,forward


def admitted(args):
    sources=dict(zip(['main','summary','deer','forward'],args))
    receipt={'forward_distance_semantics':'FRET_EFFICIENCY_AVERAGED_MODEL_DISTANCE','sources':{k:{'canonical_sha256':q.canonical_digest(v)} for k,v in sources.items()}}
    return dict(admitted_sources=sources,source_receipt=receipt)


class CrossModalTests(unittest.TestCase):
    def test_evidence_off_and_missing_dye_branch(self):
        args=inputs();e=q.synthesize_manual_evidence(*args)
        self.assertEqual(q.evaluate(args[0],e,False)['evidence_applications'],0)
        after=q.evaluate(args[0],e,**admitted(args))
        self.assertEqual(after['new_numerical_operator_calls'],0)
        self.assertFalse(after['full_question_answer'])
        self.assertIn('TMR_CY5_DOUBLE_LABEL_DATA_AND_CALIBRATION',after['remaining_obligations'])
        self.assertEqual({r['pair']:r['fluorescence_relation'] for r in after['partial_claims']},
                         {'55_175':'DIRECTIONAL_AGREEMENT_WITH_REFERENCE_READOUT','175_228':'DIRECTIONAL_TENSION_WITH_REFERENCE_READOUT'})

    def test_direction_counterfacts_change_scientific_relations(self):
        args=inputs();args[2]['curves'][1]['mean_source_axis_units']=60
        e=q.synthesize_manual_evidence(*args)
        self.assertEqual(sum(r['DEER_direction_matches_own_spin_prediction'] for r in e['rows']),1)
        args[1]['diagnostics']['175_228']['leave_one_per_condition_effects'][0]=.01
        e=q.synthesize_manual_evidence(*args)
        row=next(r for r in e['rows'] if r['pair']=='175_228')
        self.assertEqual(row['fluorescence_relation'],'DESCRIPTIVE_DIRECTION_UNRESOLVED')

    def test_unmatched_input_or_probe_cannot_close_rule(self):
        args=inputs();args[1]['input_id']='other'
        with self.assertRaisesRegex(ValueError,'INPUT_MISMATCH'):q.synthesize_manual_evidence(*args)
        args=inputs();e=q.synthesize_manual_evidence(*args);e['rows'][0]['pair']='another'
        with self.assertRaisesRegex(ValueError,'PAIR_BINDING'):q.evaluate(args[0],e)
        args=inputs();args[3]['source_role']='AUTHOR_FITTED_EXPERIMENTAL_TARGET'
        with self.assertRaisesRegex(ValueError,'SOURCE_REQUIRED'):q.synthesize_manual_evidence(*args)

    def test_numeric_label_ceiling_and_missing_content_rejected(self):
        args=inputs();kw=admitted(args);original=q.synthesize_manual_evidence(*args)
        for mutation in ['label','empty','ceiling','hypothesis','number']:
            e=copy.deepcopy(original)
            if mutation=='label':e['rows'][0]['fluorescence_relation']='UNCONDITIONAL_SCIENTIFIC_PASS'
            if mutation=='empty':e['rows']=[{'pair':p} for p in q.PAIRS]
            if mutation=='ceiling':e['limits']=['UNIQUE_MECHANISM_PROVEN']
            if mutation=='hypothesis':e['hypothesis']='Unconditional biological activity'
            if mutation=='number':e['rows'][0]['observed_E_effect']=.8
            with self.subTest(mutation=mutation),self.assertRaisesRegex(ValueError,'NUMERICAL_SYNTHESIS'):
                q.evaluate(args[0],e,**kw)
        self.assertIn('MATCHED_DEER_AND_FORWARD_EVIDENCE',q.evaluate(args[0])['remaining_obligations'])

    def test_new_digest_is_not_previous_source_admission(self):
        args=inputs();kw=admitted(args);args[2]['curves'][0]['mean_source_axis_units']+=1
        e=q.synthesize_manual_evidence(*args)
        with self.assertRaisesRegex(ValueError,'PREVIOUSLY_ADMITTED'):
            q.evaluate(args[0],e,**kw)
        kw=admitted(args);kw['source_receipt']['forward_distance_semantics']='ARITHMETIC_MEAN_DISTANCE'
        with self.assertRaisesRegex(ValueError,'SEMANTICS'):
            q.evaluate(args[0],e,**kw)

    def test_actual_consumer_cli_rejects_changed_previously_admitted_file(self):
        args=inputs();receipt=admitted(args)['source_receipt']
        names=['q15_apbs_comparison_v1/report.json','q15_pro19_verification_v1/report.json','q15_deer_source_audit_v1/report.json','q15_probe_forward_source_facts_v1.json']
        repo=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            task=Path(tmp)
            for name,value in zip(names,args):
                path=task/'outputs'/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value))
            manifest=task/'prior_admission.json';manifest.write_text(json.dumps(receipt))
            cmd=[sys.executable,str(repo/'scripts/consume_q15_cross_modal_evidence_v1.py'),'--task-root',str(task),'--source-receipt',str(manifest),'--output',str(task/'normal')]
            env=dict(os.environ,PYTHONPATH=str(repo/'src'))
            good=subprocess.run(cmd,env=env,capture_output=True,text=True)
            self.assertEqual(good.returncode,0,good.stderr)
            args[2]['curves'][0]['mean_source_axis_units']+=1
            (task/'outputs'/names[2]).write_text(json.dumps(args[2]))
            cmd[-1]=str(task/'mutated');bad=subprocess.run(cmd,env=env,capture_output=True,text=True)
            self.assertNotEqual(bad.returncode,0)
            self.assertIn('SOURCE_NOT_PREVIOUSLY_ADMITTED:deer',bad.stderr)
            self.assertFalse((task/'mutated/after.json').exists())


if __name__=='__main__':unittest.main()
