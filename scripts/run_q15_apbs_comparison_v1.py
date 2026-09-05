"""First main comparison from admitted Q15 APBS counts, not Rules-extra."""
import argparse,csv,io,json,hashlib,time,datetime,collections
from pathlib import Path
import numpy as np
from dynamics_atlas_harness import q15_apbs_comparison_v1 as q


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--task-root',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();t=args.task_root.resolve();out=args.output.resolve();out.mkdir(parents=True,exist_ok=False)
    def save(name,value):(out/name).write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    started=time.monotonic();h=hashlib.sha256();h.update(json.dumps(q.POLICY,sort_keys=True).encode());files=[];groups=collections.defaultdict(list);manifest=[]
    for source in ['q15_apbs_intake_v1','q15_normal_control_intake_v1']:
        receipt=json.loads((t/'outputs'/source/'member_intake_receipt.json').read_text())
        for item in receipt['results']:
            name=item['member']['name']
            if not name.endswith('_apbs_alex.csv'):continue
            if item['status']!='LOCAL_HEADER_CENTRAL_CRC_LENGTH_MATCH':raise ValueError('UNADMITTED_APBS_FILE')
            path=t.parent.parent.parent/Path(item['path'])
            # Source receipts are workspace-relative; use exact known source directory and member name.
            path=t/'outputs'/source/'source_members'/name
            b=path.read_bytes();q.validate_member_bytes(b,item['member']);h.update(name.encode()+b'\0'+len(b).to_bytes(8,'big')+b)
            lines=b.decode().splitlines();i=lines.index('DATA');meta=dict(csv.reader(lines[1:i]));rows=list(csv.DictReader(lines[i+1:]));
            if meta['reductionMode']!='0' or int(meta['minPhotPerBurst'])!=50 or int(meta['minNeighbors'])!=15 or float(meta['arrivalWindow'])!=.0005 or float(meta['timeResolution'])!=1.25e-8:raise ValueError('SOURCE_BURST_POLICY_CHANGED')
            counts=np.array([[float(r[k])for k in ['F_Dexc_Dem','F_Dexc_Aem','F_Aexc_Aem']]for r in rows]);duration=np.array([float(r['Tau'])for r in rows])
            if not np.array_equal(counts.sum(axis=1),np.array([float(r['Len'])for r in rows])):raise ValueError('RAW_LENGTH_IDENTITY')
            rec=q.correct(counts,duration);selected=rec['selected'];eligible=rec['eligible'];parts=name.split('/');pair=parts[1].split('_1mM')[0].split('_apo')[0];condition='holo'if'_1mM_SA'in parts[1]else'apo';rep=parts[2]
            diag={'member':name,'pair':pair,'condition':condition,'repetition':rep,'raw_events':len(rows),'raw_at_least150':int(eligible.sum()),'selected':int(selected.sum()),
                  'eligible_nonpositive_corrected_totals':int(np.sum(eligible&~rec['positive_totals'])),'eligible_nonfinite_ratios':int(np.sum(eligible&~rec['finite_ratios'])),
                  'eligible_negative_corrected_count_events':int(np.sum(eligible&np.any(rec['corrected_counts_DD_DA_AA']<0,axis=1))),
                  'selected_negative_corrected_count_events':int(np.sum(selected&np.any(rec['corrected_counts_DD_DA_AA']<0,axis=1))),
                  'E':q.summarize(rec['E'][selected]),'S':q.summarize(rec['S'][selected])}
            files.append(diag);groups[(pair,condition,rep)].append((rec['E'][selected],rec['S'][selected],diag));manifest.append({'source_receipt':source+'/member_intake_receipt.json','member':item['member']})
    if len(files)!=140 or len(groups)!=12:raise ValueError('EXPECTED_TWO_PAIRS_TWELVE_REPETITIONS')
    repetitions=[];bins=np.linspace(0,1,51)
    for (pair,cond,rep),values in sorted(groups.items()):
        e=np.concatenate([x[0]for x in values]);s=np.concatenate([x[1]for x in values]);hist=np.histogram(e,bins)[0]
        repetitions.append({'pair':pair,'condition':cond,'repetition':rep,'files':len(values),'raw_events':sum(x[2]['raw_events']for x in values),'raw_at_least150':sum(x[2]['raw_at_least150']for x in values),
                            'E':q.summarize(e),'S':q.summarize(s),'E_histogram_edges':bins.tolist(),'E_histogram_counts':hist.tolist(),'E_below_zero':int(np.sum(e<0)),'E_above_one':int(np.sum(e>1))})
        np.savez_compressed(out/(pair+'_'+cond+'_'+rep+'_derived_ES.npz'),E=e,S=s)
    report={'policy':q.POLICY,'input_id':h.hexdigest(),'files':files,'repetitions':repetitions,'condition_comparisons':q.group_difference(repetitions),'raw_events':sum(f['raw_events']for f in files),'raw_at_least150':sum(f['raw_at_least150']for f in files),'selected_events':sum(f['selected']for f in files),
            'method_role':'MAIN_COMPUTATION_NOT_RULES_EXTRA','complete_question_answer':False,'missing_for_original_question':['TMR/Cy5 double-labelled counts and own calibration','DEER/probe-geometry comparison','probe-environment obligations and uncertainty assessment'],'scientific_scope':'Observed corrected fluorescence changes under explicitly reported source-compatible calibration; no protein closure/distance inference'}
    save('source_manifest.json',manifest);save('report.json',report);save('receipt.json',{'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input_id':report['input_id'],'source_files':len(files),'elapsed_seconds':time.monotonic()-started,'full_fit_calls':0,'new_rules_extra':0,'first_main_calculation':True,'whole_archives_downloaded':0,'raw_sources_published':False})
    print(json.dumps({'raw_events':report['raw_events'],'selected_events':report['selected_events'],'condition_comparisons':report['condition_comparisons']},indent=2))


if __name__=='__main__':main()
