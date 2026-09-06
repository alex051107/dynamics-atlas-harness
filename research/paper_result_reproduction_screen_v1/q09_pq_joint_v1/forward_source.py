"""22-127 native PQ pair, conditional binned latent model and exact ZIP binding."""
from pathlib import Path
import json
import zipfile
import numpy as np
from scipy.special import ndtr
from numpy.polynomial.legendre import leggauss
from q09_forward_v1 import expected_counts, poisson_deviance

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT/'inputs/q09_author'


def bin_factor(rate, dt):
    x = np.asarray(rate)*dt
    return -np.expm1(-x)/x


class PQPair:
    def __init__(self, quadrature=256):
        self.name='22-127'
        directory=BASE/'unpacked/eTCSPC'/self.name
        filenames=[self.name+'.yml',self.name+'_D0.dat',self.name+'_DA.dat','IRF_D0.dat','IRF_DA.dat']
        with zipfile.ZipFile(BASE/'eTCSPC_wildtype.zip') as archive:
            for name in filenames:
                if (directory/name).read_bytes()!=archive.read('eTCSPC/'+self.name+'/'+name):
                    raise ValueError('EXTRACTED_BYTES_DIFFER_FROM_FROZEN_ZIP')
        metadata=(directory/(self.name+'.yml')).read_text()
        if metadata.count('Setup ID: PQ TCSPC')!=4 or 'Resolution [ps]: 8' not in metadata:
            raise ValueError('UNEXPECTED_INSTRUMENT_METADATA')
        self.y={};self.irf={};self.irf_baseline={}
        self.dt=.008
        for role in ('D0','DA'):
            curve=np.loadtxt(directory/(self.name+'_'+role+'.dat'))
            response=np.loadtxt(directory/('IRF_'+role+'.dat'))
            if curve.shape!=response.shape or curve.shape[1]!=2 or not np.array_equal(curve[:,0],response[:,0]):
                raise ValueError('IRF_AND_COUNT_AXIS_MISMATCH')
            if not np.allclose(np.diff(curve[:,0]),self.dt,rtol=0,atol=1e-10) or curve[0,0]!=0:
                raise ValueError('PHYSICAL_TIME_AXIS_MISMATCH')
            if not np.all(np.isfinite(curve)) or not np.all(np.isfinite(response)) or np.any(curve[:,1]<0) or np.any(response[:,1]<0):
                raise ValueError('INVALID_RAW_COUNTS')
            if not np.all(curve[:,1]==np.floor(curve[:,1])) or not np.all(response[:,1]==np.floor(response[:,1])):
                raise ValueError('NONINTEGER_RAW_COUNTS')
            self.t=curve[:,0];self.y[role]=curve[:,1]
            self.irf_baseline[role]=float(np.median(response[-256:,1]))
            self.irf[role]=np.maximum(response[:,1]-self.irf_baseline[role],0)
        self.lin=np.ones_like(self.t);self.mask=np.ones_like(self.t,dtype=bool)
        nodes,factors=leggauss(quadrature)
        self.r=(nodes+1)*90.;self.qweights=factors*90.
        self.rates=.224*(2/3)*(56.4/self.r)**6
        self.transfer_exp=np.exp(-self.t[:,None]*self.rates)

    def intrinsic_donor(self,taus,amplitudes):
        alpha=1/np.asarray(taus)
        return (np.exp(-self.t[:,None]*alpha)*bin_factor(alpha,self.dt))@np.asarray(amplitudes)

    def intrinsic_pair(self,taus,amplitudes,means,populations,f0):
        density=np.zeros_like(self.r)
        for mean,population in zip(means,populations):
            density+=population*np.exp(-.5*((self.r-mean)/6.)**2)/(6*np.sqrt(2*np.pi)*ndtr(mean/6))
        density*=self.qweights
        quenched=np.zeros_like(self.t)
        for tau,amplitude in zip(taus,amplitudes):
            alpha=1/tau
            # Exact integral of each total-rate exponential over native time bin.
            quenched+=amplitude*np.exp(-self.t*alpha)*(self.transfer_exp@(density*bin_factor(alpha+self.rates,self.dt)))
        donor=self.intrinsic_donor(taus,amplitudes)
        return donor, f0*donor+(1-f0)*quenched

    def counts(self,role,intrinsic,bg,shift):
        return expected_counts(intrinsic,self.irf[role],self.lin,self.mask,float(self.y[role].sum()),shift_bins=shift,background_fraction=bg)

    def joint_counts(self,p):
        tau1,tau2,a,r1,r2,x,f0,bg0,shift0,bga,shifta=p
        d0,da=self.intrinsic_pair([tau1,tau2],[a,1-a],[r1,r2],[x,1-x],f0)
        return {'D0':self.counts('D0',d0,bg0,shift0),'DA':self.counts('DA',da,bga,shifta)}

    def deviance(self,p):
        values=self.joint_counts(p)
        return sum(poisson_deviance(self.y[role],values[role]) for role in ('D0','DA'))


def check():
    out=ROOT/'outputs/q09_pq_joint_v1';out.mkdir(exist_ok=False)
    data=PQPair(256);fine=PQPair(512)
    maximum=0.
    for means in ([20.,50.],[40.,65.],[90.,120.]):
        for taus in ([.05,4.],[1.,3.8]):
            d0,da=data.intrinsic_pair(taus,[.1,.9],means,[.4,.6],.1)
            ref0,refa=fine.intrinsic_pair(taus,[.1,.9],means,[.4,.6],.1)
            maximum=max(maximum,float(np.max(abs(da-refa))))
            np.testing.assert_allclose(da,refa,rtol=1e-8,atol=1e-10)
    d0,da=data.intrinsic_pair([1.,4.],[.2,.8],[40.,60.],[.5,.5],1.)
    np.testing.assert_allclose(d0,da,atol=0,rtol=0)
    # Analytic average of one exponential over the first bin.
    np.testing.assert_allclose(data.intrinsic_donor([4.],[1.])[0],4/.008*(1-np.exp(-.008/4)),rtol=1e-12)
    p=[1.,4.,.1,40.,65.,.5,.1,.001,0.,.001,0.]
    predictions=data.joint_counts(p)
    for role in ('D0','DA'):
        assert np.all(predictions[role]>0)
        np.testing.assert_allclose(predictions[role].sum(),data.y[role].sum(),rtol=1e-12)
    record={'status':'PQ_MAPPING_AND_BINNED_FORWARD_CHECK_PASS','variant':data.name,'bins_per_role':len(data.t),'dt_ns':data.dt,
            'counts':{k:int(v.sum()) for k,v in data.y.items()},'irf_baseline':data.irf_baseline,
            'source_binding':'all5consumedfiles byte-equal original frozenZIP;metadataPQ8ps matches nativeaxes',
            'quadrature_256_512_max_absolute_difference':maximum,'checks':['ZIPbinding_and_metadata_time','positive_distance_quadrature_convergence','exact_exponential_bin_average','f0equals1_DAequalsD0_beforeIRF','separateIRFs_and_final_count_normalization'],
            'conditional_limits':['Histogram IRF convolution assumes within-bin phase represented by fittedshift','IRFbackgroundmedianlast256;scatter0;allbinswindow;no nuisance sensitivity completed'],
            'fits':0}
    (out/'forward_validation.json').write_text(json.dumps(record,indent=2)+'\n')
    (out/'forward_source.py').write_text(Path(__file__).read_text())
    print(json.dumps(record,indent=2))


if __name__=='__main__':check()
