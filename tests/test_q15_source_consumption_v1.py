import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zlib

from dynamics_atlas_harness import q15_apbs_comparison_v1 as q


class SourceConsumptionTests(unittest.TestCase):
    def test_lengths_and_same_length_mutation(self):
        data=b'100,100,200'
        member={'expanded_bytes':len(data),'crc32':f'{zlib.crc32(data):08x}'}
        q.validate_member_bytes(data,member)
        with self.assertRaisesRegex(ValueError,'LENGTH'):
            q.validate_member_bytes(data+b'0',member)
        with self.assertRaisesRegex(ValueError,'CRC'):
            q.validate_member_bytes(b'150,100,150',member)

    def test_actual_main_cli_rejects_changed_admitted_file(self):
        repo=Path(__file__).resolve().parents[1]
        spec=importlib.util.spec_from_file_location('q15_main_cli',repo/'scripts/run_q15_apbs_comparison_v1.py')
        cli=importlib.util.module_from_spec(spec);spec.loader.exec_module(cli)
        text=('METADATA\nreductionMode,0\nminPhotPerBurst,50\nminNeighbors,15\n'
              'arrivalWindow,0.0005\ntimeResolution,1.25e-8\nDATA\n'
              'Epr,Sraw,Len,F_Aexc_Aem,F_Dexc_Dem,F_Dexc_Aem,F_Aexc_Dem,Tau,BurstStart,BurstEnd,bvaSigEpr,sigEpr,nWindows\n'
              '0.5,0.5,400,200,100,100,0,0.001,0,0.001,0,0,1\n')
        data=text.encode()
        with tempfile.TemporaryDirectory() as tmp:
            task=Path(tmp); first=None
            for source,pair in [('q15_apbs_intake_v1','175_228'),('q15_normal_control_intake_v1','55_175')]:
                results=[]
                for condition in ['apo','1mM_SA']:
                    for rep,count in [('repetion_1',12),('repetion_2',12),('repetion_3',11)]:
                        for index in range(count):
                            name=f'Figure3/{pair}_{condition}/{rep}/{index:03d}_apbs_alex.csv'
                            path=task/'outputs'/source/'source_members'/name
                            path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
                            first=first or path
                            results.append({'status':'LOCAL_HEADER_CENTRAL_CRC_LENGTH_MATCH','path':str(path),
                                            'member':{'name':name,'expanded_bytes':len(data),'crc32':f'{zlib.crc32(data):08x}'}})
                (task/'outputs'/source/'member_intake_receipt.json').write_text(json.dumps({'results':results}))
            out=task/'valid'
            with patch.object(sys,'argv',['runner','--task-root',str(task),'--output',str(out)]), patch('builtins.print'):
                cli.main()
            report=json.loads((out/'report.json').read_text())
            self.assertEqual(report['raw_events'],140)
            self.assertEqual(report['selected_events'],140)
            changed=data.replace(b',200,100,100,0,',b',150,150,100,0,')
            self.assertEqual(len(changed),len(data));self.assertNotEqual(changed,data)
            first.write_bytes(changed)
            with patch.object(sys,'argv',['runner','--task-root',str(task),'--output',str(task/'changed')]), \
                    patch.object(q,'correct',side_effect=AssertionError('Changed bytes reached science calculation')):
                with self.assertRaisesRegex(ValueError,'SOURCE_MEMBER_CRC_MISMATCH'):
                    cli.main()
            self.assertFalse((task/'changed/report.json').exists())


if __name__=='__main__':unittest.main()
