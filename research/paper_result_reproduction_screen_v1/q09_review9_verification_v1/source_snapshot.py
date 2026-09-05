"""Independent arithmetic and IRF-region audit; no optimization or scientific cutoff."""
from pathlib import Path
import json,csv
import numpy as np
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'outputs/q09_review9_verification_v1';OUT.mkdir(exist_ok=False)
rows=list(csv.DictReader((ROOT/'outputs/q09_pq_joint_v3/per_bin.csv').open()))
blocks=json.loads((ROOT/'outputs/q09_pq_joint_v3/residual_blocks.json').read_text());result={};vectors=[]
for role in ('D0','DA'):
    y=np.array([float(r[role+'_observed']) for r in rows]);mu=np.array([float(r[role+'_expected']) for r in rows])
    by=[];bm=[]
    for b in blocks:
        ix=slice(b['first_bin'],b['last_bin']+1);Y=float(y[ix].sum());M=float(mu[ix].sum())
        assert Y==b['channels'][role]['observed'];np.testing.assert_allclose(M,b['channels'][role]['expected'],rtol=1e-12)
        by.append(Y);bm.append(M)
    Y=np.array(by);M=np.array(bm);res=(Y-M)/np.sqrt(M);positive=Y>0;terms=M-Y;terms[positive]+=Y[positive]*np.log(Y[positive]/M[positive]);vectors.append(res)
    result[role]={'block_deviance':float(2*terms.sum()),'max_abs_scaled_residual':float(max(abs(res))),'blocks_abs_residual_gt5_descriptive_only':int(sum(abs(res)>5)),'scaled_residuals':res.tolist()}
result['block_residual_correlation_descriptive_only']=float(np.corrcoef(vectors)[0,1]);irfs={}
dir=ROOT/'inputs/q09_author/unpacked/eTCSPC/22-127'
for role in ('D0','DA'):
    a=np.loadtxt(dir/('IRF_'+role+'.dat'));stats={}
    for name,ix in [('first256',slice(0,256)),('last256',slice(-256,None))]:
        v=a[ix,1];stats[name]={'first_time_ns':float(a[ix,0][0]),'last_time_ns':float(a[ix,0][-1]),'bins':len(v),'total':int(v.sum()),'mean':float(v.mean()),'median':float(np.median(v)),'zero_fraction':float(np.mean(v==0)),'interpretation':'Descriptive region;purebackgroundnotproven'}
    irfs[role]={'total_photons':int(a[:,1].sum()),'peak_time_ns':float(a[np.argmax(a[:,1]),0]),'regions':stats}
meta=(dir/'22-127.yml').read_text();assert 'Excitation source repetition rate: 20 MHz' in meta
report={'status':'SOURCE_AND_RESIDUAL_VERIFIED','aggregate_residuals':result,'IRF_audit':irfs,'donor_model_form':{'source':'PublishedSI PDF21 SupplementaryTable2a,visuallyverified','variant':'E22pAcF/D127C','populated_donor_lifetime_terms':3,'table_fit_values_excluded_from_solver':True},'PQ_repetition_ns':50,'scientific_scope':'Structuredbiasobserved;noformalcalibratedgoodnessoffittest,modelcauseorstate-numberverdict','Rules_run':False}
(OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n');(OUT/'source_snapshot.py').write_text(Path(__file__).read_text());print(json.dumps(report,indent=2))
