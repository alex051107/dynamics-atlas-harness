"""Conditional two-DA/one-reference IBH group; no protein state-number verdict."""
from pathlib import Path
import json
import re
import zipfile
import numpy as np
from numpy.polynomial.legendre import leggauss
from q09_forward_v1 import linearization_reference, expected_counts, poisson_deviance
from q09_pq_joint_v1 import PQPair

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT/'inputs/q09_author'
OUT = ROOT/'outputs/q09_shared_ibh_v1'


def read_ibh(path):
    content=path.read_text()
    body=content.split('Chan\tData\n',1)[1]
    pairs=np.array([[int(v) for v in row.split()] for row in body.splitlines() if row.strip()])
    if pairs.shape!=(4096,2) or not np.array_equal(pairs[:,0],np.arange(1,4097)) or np.any(pairs[:,1]<0):
        raise ValueError('IBH_CHANNEL_OR_COUNT_MISMATCH')
    return pairs[:,1].astype(float),content.split('Chan\tData\n',1)[0]


class SharedIBH:
    # Same exact exponential-bin integration, different source/role admission.
    intrinsic_donor=PQPair.intrinsic_donor
    intrinsic_pair=PQPair.intrinsic_pair
    def __init__(self,quadrature=256):
        variants=('19-119','19-132');self.dt=.0141;self.t=np.arange(4096)*self.dt
        self.audit={'variants':list(variants),'source_files':[],'metadata':{},'byte_equal_across_variants':{}}
        self.payload={}; records={}
        with zipfile.ZipFile(BASE/'eTCSPC_wildtype.zip') as archive:
            for variant in variants:
                directory=BASE/'unpacked/eTCSPC'/variant
                names=[variant+'.yml',variant+'_D0.txt',variant+'_DA.txt','IRF_D0.txt','IRF_DA.txt','Linearization_D0.txt','Linearization_DA.txt']
                for name in names:
                    relative='eTCSPC/'+variant+'/'+name
                    payload=(directory/name).read_bytes()
                    if payload!=archive.read(relative):raise ValueError('EXTRACTED_BYTES_DIFFER_FROM_FROZEN_ZIP')
                    self.payload[(variant,name)]=payload
                    self.audit['source_files'].append(relative)
                metadata=(directory/(variant+'.yml')).read_text()
                if metadata.count('Setup ID: IBH TCSPC')!=6 or 'Resolution [ps]: 14.1' not in metadata:raise ValueError('UNEXPECTED_IBH_METADATA')
                for name in names[1:]:
                    if 'Filename: ./'+name not in metadata:raise ValueError('METADATA_ROLE_REFERENCE_MISSING')
                self.audit['metadata'][variant]={'sample_name':re.search(r'Name: (T4[^\n]+)',metadata)[1],
                    'sample_descriptions':[v.strip() for v in metadata.splitlines() if 'PBS pH' in v],
                    'resolution_ps':14.1,'channel_origin':'stored channel1 mapped to relative time0','native_dt_authority':'metadata resolution and sequential channel axis',
                    'donor_exchangeability':'NOT_ESTABLISHED_BY_IDENTICAL_BYTES'}
                for role in ('D0','DA'):
                    y,header=read_ibh(directory/(variant+'_'+role+'.txt'))
                    raw_irf,_=read_ibh(directory/('IRF_'+role+'.txt'))
                    raw_lin,_=read_ibh(directory/('Linearization_'+role+'.txt'))
                    lin=linearization_reference(raw_lin);mask=lin>.1*np.median(lin[lin>0])
                    indices=np.flatnonzero(mask)
                    baseline=float(np.median(raw_irf[indices[-256:]]))
                    records[(variant,role)]={'y':y,'header':header,'irf':np.maximum(raw_irf-baseline,0),'Lin':lin,'mask':mask,'irf_baseline':baseline,'raw_irf':raw_irf,'raw_Lin':raw_lin}
        for role in ('D0','DA'):
            for component in ('decay','IRF','Linearization'):
                names=[v+'_'+role+'.txt' if component=='decay' else component+'_'+role+'.txt' for v in variants]
                equal=self.payload[(variants[0],names[0])]==self.payload[(variants[1],names[1])]
                self.audit['byte_equal_across_variants'][role+'_'+component]=equal
        if not all(self.audit['byte_equal_across_variants']['D0_'+k] for k in ('decay','IRF','Linearization')):
            raise ValueError('SHARED_DONOR_RECORD_INSTRUMENT_OR_LIN_NOT_IDENTICAL')
        if self.audit['byte_equal_across_variants']['DA_decay']:raise ValueError('DA_UNEXPECTED_DUPLICATE')
        self.records={'D0_shared':records[('19-119','D0')],**{v+'_DA':records[(v,'DA')] for v in variants}}
        self.audit['record_treatment']='One observed D0 record contributes once;two distinct DA records both retained. Applying one latent donor response to two mutant samples is explicitly conditional,not proven.'
        self.audit['original_donor_descriptions_preserved']=True
        self.audit['records']={k:{'raw_photons':int(v['y'].sum()),'fit_photons':int(v['y'][v['mask']].sum()),'excluded_photons':int(v['y'][~v['mask']].sum()),'fit_bins':int(v['mask'].sum()),'irf_baseline':v['irf_baseline'],'original_header':v['header']} for k,v in self.records.items()}
        nodes,weights=leggauss(quadrature);self.r=(nodes+1)*90;self.qweights=weights*90
        self.rates=.224*(2/3)*(56.4/self.r)**6
        self.transfer_exp=np.exp(-self.t[:,None]*self.rates)
        self.total=sum(v['y'][v['mask']].sum() for v in self.records.values())

    def counts(self,key,intrinsic,bg,shift):
        d=self.records[key]
        return expected_counts(intrinsic,d['irf'],d['Lin'],d['mask'],float(d['y'][d['mask']].sum()),shift_bins=shift,background_fraction=bg)

    def joint_counts(self,p):
        # shared donor tau1,tau2,amplitude,bg0,shift0; six local DA params each.
        t1,t2,a,bg0,s0=p[:5]
        donor=self.intrinsic_donor([t1,t2],[a,1-a])
        result={'D0_shared':self.counts('D0_shared',donor,bg0,s0)}
        for index,variant in enumerate(('19-119','19-132')):
            r1,r2,x,f0,bg,shift=p[5+6*index:11+6*index]
            _,da=self.intrinsic_pair([t1,t2],[a,1-a],[r1,r2],[x,1-x],f0)
            result[variant+'_DA']=self.counts(variant+'_DA',da,bg,shift)
        return result

    def channel_deviance(self,p):
        predictions=self.joint_counts(p)
        return {k:poisson_deviance(d['y'][d['mask']],predictions[k][d['mask']]) for k,d in self.records.items()}

    def deviance(self,p):return sum(self.channel_deviance(p).values())


def check():
    OUT.mkdir(exist_ok=False)
    data=SharedIBH();fine=SharedIBH(512)
    p=[1.1,3.88,.097,.0018,.58,35.,65.,.5,.1,.001,0.,65.,35.,.5,.1,.001,0.]
    predictions=data.joint_counts(p);reference=fine.joint_counts(p)
    for k,d in data.records.items():
        np.testing.assert_allclose(predictions[k],reference[k],rtol=1e-8,atol=1e-7)
        np.testing.assert_allclose(predictions[k][d['mask']].sum(),d['y'][d['mask']].sum(),rtol=1e-12)
        assert np.all(predictions[k][d['mask']]>0)
    loss=data.channel_deviance(p);assert len(loss)==3
    np.testing.assert_allclose(data.deviance(p),sum(loss.values()),rtol=0,atol=0)
    # Explicit duplicate-reference counterfactual is accounting-only,never the baseline.
    duplicated=sum(loss.values())+loss['D0_shared']
    np.testing.assert_allclose(duplicated-data.deviance(p),loss['D0_shared'],rtol=1e-12)
    report={'status':'CONDITIONAL_SHARED_IBH_INPUT_AND_FORWARD_PASS','audit':data.audit,
            'checks':['14consumedZIPmembers byte-equal;metadata filenames,instrument,14.1ps and1..4096channel axes','D0/IRF/Lin identical;DA both distinct','exactnativebin forward256vs512','fullmodelLin finalmaskedcountnormalization','oneD0plusbothDA likelihood accounting'],
            'fixed_probe_channel_deviance':loss,'double_counted_reference_counterfactual_delta':duplicated-data.deviance(p),
            'scientific_gate':'Conditional shared reference model allowed;actualdonor exchangeability and acquisition provenance remainunknown',
            'fits':0,'Rules_run':False}
    (OUT/'input_forward_check.json').write_text(json.dumps(report,indent=2)+'\n')
    (OUT/'group_source.py').write_text(Path(__file__).read_text())
    (OUT/'binned_source.py').write_text((ROOT/'scripts/q09_pq_joint_v1.py').read_text())
    (OUT/'instrument_source.py').write_text((ROOT/'scripts/q09_forward_v1.py').read_text())
    print(json.dumps(report,indent=2))

if __name__=='__main__':check()
