"""Calibration-only response audit; no fluorescence fitting or corrected IRF."""
from pathlib import Path
import json
import zipfile
import numpy as np
from scipy.stats import chi2

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'inputs/q09_author'
OUT=ROOT/'outputs/q09_irf_regions_v1'


def constant_rate_interval(total,bins):
    # Exact central count interval assuming independent equal-mean Poisson bins.
    lower=0. if total==0 else .5*chi2.ppf(.025,2*total)
    upper=.5*chi2.ppf(.975,2*(total+1))
    return [float(lower/bins),float(upper/bins)]


def describe(t,y,indices):
    values=y[indices];total=int(values.sum());n=len(values)
    blocks=[{'first_bin':int(ix[0]),'last_bin':int(ix[-1]),'count':int(y[ix].sum()),'mean':float(y[ix].mean()),'bins':len(ix)} for ix in np.array_split(indices,8)]
    block_expected=[len(ix)*values.mean() for ix in np.array_split(indices,8)]
    Y=np.array([b['count'] for b in blocks],float);M=np.array(block_expected);positive=Y>0
    terms=M-Y
    if total:terms[positive]+=Y[positive]*np.log(Y[positive]/M[positive])
    return {'first_bin':int(indices[0]),'last_bin':int(indices[-1]),'first_time_ns':float(t[indices[0]]),'last_time_ns':float(t[indices[-1]]),
            'bins':n,'count':total,'mean_counts_per_bin':float(values.mean()),'sample_variance':float(values.var(ddof=1)),
            'zero_fraction':float(np.mean(values==0)),'expected_zero_fraction_under_constant_Poisson':float(np.exp(-values.mean())),
            'conditional_Poisson_mean_95_interval':constant_rate_interval(total,n),'blocks':blocks,
            'eight_block_deviance_descriptive_only':float(2*terms.sum()),
            'assumption':'ConstantPoissonrateintervalonly;regionmaycontaintrueresponse;notproofpurebackground'}


def main():
    OUT.mkdir(exist_ok=False)
    report={'status':'CALIBRATION_ONLY_FIXED_REGION_AUDIT','method':'Predeclared time/edge regions;noDA-drivenselection or IRF mutation','roles':{},'fits':0,'Rules_run':False}
    with zipfile.ZipFile(BASE/'eTCSPC_wildtype.zip') as archive:
        for role in ('D0','DA'):
            name='IRF_'+role+'.dat';path=BASE/'unpacked/eTCSPC/22-127'/name
            assert path.read_bytes()==archive.read('eTCSPC/22-127/'+name)
            a=np.loadtxt(path);t,y=a.T;assert len(y)==6100 and np.all(y>=0) and np.all(y==np.floor(y))
            regions={'first256':np.arange(256),'last256':np.arange(len(y)-256,len(y)),
                     'first512':np.arange(512),'last512':np.arange(len(y)-512,len(y)),
                     'nominal_pulse_3_to_7ns':np.flatnonzero((t>=3)&(t<7)),
                     'postpulse_7_to_15ns':np.flatnonzero((t>=7)&(t<15)),
                     'late_15_to_30ns':np.flatnonzero((t>=15)&(t<30)),
                     'late_30_to_46_752ns':np.flatnonzero((t>=30)&(t<46.752))}
            records={name:describe(t,y,ix) for name,ix in regions.items()}
            # Existing two edge regions are one predeclared conditional rate estimate.
            edges=np.concatenate([regions['first256'],regions['last256']]);pool=describe(t,y,edges)
            lo,hi=pool['conditional_Poisson_mean_95_interval'];nominal=regions['nominal_pulse_3_to_7ns'];outside=np.setdiff1d(np.arange(len(y)),nominal)
            region_excess={}
            for name in ['postpulse_7_to_15ns','late_15_to_30ns','late_30_to_46_752ns']:
                ix=regions[name];count=float(y[ix].sum());region_excess[name]={'observed_count':count,'expected_if_pooled_edge_rate':[lo*len(ix),hi*len(ix)],'excess_over_upper_edge_rate':count-hi*len(ix),'interpretation':'Conditionalcontrastnot formal intervalfor netresponse;overlapping/multiple regionsnotindependenttests'}
            report['roles'][role]={'source':'eTCSPC/22-127/IRF_'+role+'.dat',
                'total_photons':int(y.sum()),'peak_bin':int(np.argmax(y)),'peak_time_ns':float(t[np.argmax(y)]),
                'regions':records,'pooled_first_last256':pool,'nominal_pulse_photons':int(y[nominal].sum()),'outside_nominal_pulse_photons':int(y[outside].sum()),
                'constant_background_count_range_over_full6100bins':[lo*len(y),hi*len(y)],
                'constant_background_fraction_range':[lo*len(y)/y.sum(),hi*len(y)/y.sum()],
                'conditional_late_region_contrasts':region_excess}
    report['claim_ceiling']='Descriptivecalibrationstructure andconditionalconstant-rateintervals;no netIRF truth,backgroundsubtraction,uncertaintypropagationorstate-numberverdict'
    (OUT/'audit.json').write_text(json.dumps(report,indent=2)+'\n');(OUT/'source_snapshot.py').write_text(Path(__file__).read_text())
    print(json.dumps({role:{'peak_ns':v['peak_time_ns'],'pooled_edge_rate':v['pooled_first_last256']['mean_counts_per_bin'],'edge_rate_interval':v['pooled_first_last256']['conditional_Poisson_mean_95_interval'],'region_means':{k:w['mean_counts_per_bin'] for k,w in v['regions'].items()},'conditional_late_contrasts':v['conditional_late_region_contrasts']} for role,v in report['roles'].items()},indent=2))

if __name__=='__main__':main()
