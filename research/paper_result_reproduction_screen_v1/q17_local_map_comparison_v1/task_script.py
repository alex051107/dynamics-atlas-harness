"""Conditional local map comparison on actual deposited data, CPU only."""
from pathlib import Path
import json, gzip, struct, time, math, re
import numpy as np
from scipy.spatial import cKDTree
from scipy.stats import spearmanr

TASK=Path(__file__).resolve().parents[1]
A={'C':[.0893,.2563,.7570,1.0487,.3575],'O':[.0974,.2921,.6910,.6990,.2039],
   'N':[.1022,.3219,.7982,.8197,.1715],'S':[.2497,.5628,1.3899,2.1865,.7715]}
B={'C':[.2465,1.7100,6.4094,18.6113,50.2523],'O':[.2067,1.3815,4.6943,12.7105,32.4726],
   'N':[.2451,1.7481,6.1925,17.3894,48.1431],'S':[.2681,1.6711,7.0267,19.5377,50.3888]}
PROTEIN=set('ALA ARG ASN ASP CYS GLN GLU GLY HIS HSD ILE LEU LYS MET PHE PRO SER THR TRP TYR VAL'.split())


def atoms(path):
    result=[]
    for line in path.read_text().splitlines():
        if line.startswith(('ATOM  ','HETATM')):
            res=line[17:20].strip();name=line[12:16].strip()
            result.append(dict(chain=line[21],resid=int(line[22:26]),resname='HIS'if res=='HSD'else res,
                name='CD1'if res=='ILE'and name=='CD'else name,element=line[76:78].strip(),
                xyz=np.array([float(line[i:i+8])for i in [30,38,46]]),bfactor=float(line[60:66]),protein=res in PROTEIN))
    return result


def correlation(a,b):
    if len(a)<20 or np.std(a)==0 or np.std(b)==0:return None
    return float(np.corrcoef(a,b)[0,1])


def main():
    started=time.monotonic();out=TASK/'outputs/q17_local_map_comparison_v1';out.mkdir(exist_ok=False)
    cp=TASK/'outputs/q17_coordinate_admission_v1';mp=TASK/'outputs/q17_map_admission_v1'
    original=atoms(cp/'published_7w9w.pdb');refined=atoms(cp/'02-7w9w__3-Model__cc-1.0__conf_EMMIVOX.pdb')
    matrices={}
    for line in (cp/'published_7w9w.pdb').read_text().splitlines():
        if line.startswith('REMARK 350   BIOMT'):
            s=line.split();matrices.setdefault(int(s[3]),{})[int(s[2][-1])-1]=list(map(float,s[4:8]))
    assembly=[];ligands=[]
    for op,chain in [(1,'A'),(2,'B'),(3,'C')]:
        m=np.array([matrices[op][i]for i in range(3)])
        for atom in original:
            copied={**atom,'chain':chain,'xyz':m[:,:3]@atom['xyz']+m[:,3]}
            if atom['protein']:assembly.append(copied)
            elif atom['resname']!='HOH':ligands.append(copied['xyz'])
    ligands.extend(a['xyz']for a in refined if not a['protein'])
    key=lambda a:(a['chain'],a['resid'],a['resname'],a['name'])
    def selected(rows):
        rows=[a for a in rows if a['protein']and a['element']!='H'and a['resid']not in {89,149,279}]
        d={key(a):a for a in rows};assert len(d)==len(rows)
        return d
    old,new=selected(assembly),selected(refined);keys=sorted(old.keys()&new.keys());assert len(keys)>6000
    old,new=[old[k]for k in keys],[new[k]for k in keys]
    positions=[np.array([a['xyz']for a in rows])for rows in [old,new]]
    arrays=[];headers=[]
    for name in ['emd_32377.map.gz','emd_32377_half_map_1.map.gz','emd_32377_half_map_2.map.gz']:
        raw=gzip.open(mp/name,'rb').read();nx,ny,nz,mode=struct.unpack_from('<4i',raw);ns=struct.unpack_from('<i',raw,92)[0]
        assert (nx,ny,nz,mode)==(162,162,162,2)and struct.unpack_from('<3i',raw,64)==(1,2,3)
        spacing=np.array(struct.unpack_from('<3f',raw,40))/np.array(struct.unpack_from('<3i',raw,28))
        origin=np.array(struct.unpack_from('<3f',raw,196));assert not origin.any()
        arrays.append(np.frombuffer(raw,dtype='<f4',offset=1024+ns).reshape(nz,ny,nx))
    xyz=np.concatenate(positions);lo=np.maximum(np.floor((xyz.min(0)-3)/spacing).astype(int),0)
    hi=np.minimum(np.ceil((xyz.max(0)+3)/spacing).astype(int)+1,[nx,ny,nz])
    zz,yy,xx=np.meshgrid(np.arange(lo[2],hi[2]),np.arange(lo[1],hi[1]),np.arange(lo[0],hi[0]),indexing='ij')
    ijk=np.column_stack([xx.ravel(),yy.ravel(),zz.ravel()]);vox=ijk*spacing
    union_dist=cKDTree(xyz).query(vox,workers=1)[0];ligand_dist=cKDTree(ligands).query(vox,workers=1)[0]
    keep=(union_dist<=3)&(ligand_dist>4);ijk,vox=ijk[keep],vox[keep]
    nearest=cKDTree(positions[0]).query(vox,workers=1)[1]
    residue_keys=sorted({k[:3]for k in keys});rindex={k:i for i,k in enumerate(residue_keys)}
    assignment=np.array([rindex[keys[i][:3]]for i in nearest])
    actual=[a[ijk[:,2],ijk[:,1],ijk[:,0]].astype(float)for a in arrays]
    densities=[];parameter=[]
    for rows,xyz in zip([old,new],positions):
        assert all(a['element']in A and a['bfactor']>=0 and math.isfinite(a['bfactor'])for a in rows)
        width=np.array([np.array(B[a['element']])+a['bfactor']/4 for a in rows])
        pref=np.array([A[a['element']]for a in rows])*(np.pi/width)**1.5;inv=np.pi**2/width
        tree=cKDTree(xyz);density=np.zeros(len(vox))
        for start in range(0,len(vox),2000):
            if time.monotonic()-started>120:raise TimeoutError('FROZEN_CPU_BUDGET')
            part=vox[start:start+2000];neighbors=tree.query_ball_point(part,10)
            vi=np.repeat(np.arange(len(part)),[len(x)for x in neighbors]);ai=np.concatenate(neighbors).astype(int)
            dist2=np.sum((xyz[ai]-part[vi])**2,axis=1)
            contribution=np.sum(pref[ai]*np.exp(-inv[ai]*dist2[:,None]),axis=1)
            density[start:start+len(part)]=np.bincount(vi,weights=contribution,minlength=len(part))
        densities.append(density);parameter.append((pref,inv))
    # Independent scalar accumulation at three actual voxels checks array indexing/formula.
    error=0
    for model in [0,1]:
        for index in [0,len(vox)//2,len(vox)-1]:
            expected=0.
            for atom,xyz in enumerate(positions[model]):
                d2=sum(float(x-y)**2 for x,y in zip(xyz,vox[index]))
                if d2<100:
                    expected+=sum(float(parameter[model][0][atom,j])*math.exp(-float(parameter[model][1][atom,j])*d2)for j in range(5))
            error=max(error,abs(expected-densities[model][index]))
    assert error<1e-10
    halfmean=(actual[1]+actual[2])/2;proxy=np.abs(actual[1]-actual[2])/2
    rows=[]
    for index,rkey in enumerate(residue_keys):
        mask=assignment==index;count=int(mask.sum())
        cc0=correlation(densities[0][mask],actual[0][mask]);cc1=correlation(densities[1][mask],actual[0][mask])
        ca=keys.index((*rkey,'CA'))if (*rkey,'CA')in keys else None
        rows.append(dict(chain=rkey[0],resid=rkey[1],resname=rkey[2],voxels=count,
            halfmean_noise_proxy=float(np.median(proxy[mask]))if count else None,
            original_local_CC=cc0,refined_local_CC=cc1,CC_change=cc1-cc0 if cc0 is not None and cc1 is not None else None,
            main_halfmean_CC=correlation(actual[0][mask],halfmean[mask]),
            CA_change_A=float(np.linalg.norm(positions[1][ca]-positions[0][ca]))if ca is not None else None))
    # Collapse the three symmetry copies before descriptive ordering.
    collapsed=[]
    for resid in sorted({r['resid']for r in rows}):
        rr=[r for r in rows if r['resid']==resid and r['CC_change']is not None]
        if len(rr)!=3:continue
        collapsed.append(dict(resid=resid,**{k:float(np.median([r[k]for r in rr]))for k in ['halfmean_noise_proxy','original_local_CC','refined_local_CC','CC_change','CA_change_A']}))
    ranked=sorted(collapsed,key=lambda r:(r['halfmean_noise_proxy'],r['resid']));q=len(ranked)//4
    groups={label:dict(n=len(rr),median_noise=float(np.median([r['halfmean_noise_proxy']for r in rr])),
        median_CC_change=float(np.median([r['CC_change']for r in rr])),median_CA_change_A=float(np.median([r['CA_change_A']for r in rr])),
        residues_with_CC_decrease=sum(r['CC_change']<0 for r in rr))for label,rr in [('low_noise_quartile',ranked[:q]),('high_noise_quartile',ranked[-q:])]}
    report=dict(status='CONDITIONAL_LOCAL_NOISE_AND_MAP_FIT_OBSERVED',common_heavy_atoms=len(keys),voxels=len(vox),residue_copy_rows=len(rows),
        collapsed_residues=len(collapsed),groups=groups,global_mask_CC=dict(original=correlation(densities[0],actual[0]),refined=correlation(densities[1],actual[0]),main_halfmean=correlation(actual[0],halfmean)),
        scalar_formula_maxerror=error,elapsed_seconds=time.monotonic()-started,
        local_noise_CCchange_spearman=float(spearmanr([r['halfmean_noise_proxy']for r in collapsed],[r['CC_change']for r in collapsed]).statistic),
        method='FiveGaussianfixedauthorformfactor; eachdepositedB; 10A cutoff; commonprotein3Aunionmask; ligand4Aexclusion; nearestoriginalheavyatomresidue; median3copies.',
        limits=['Different original/refined Bfactors are partofcomparison, notisolatedcoordinateeffect.',
            'Halfmapproxy is not calibrated mainmap likelihoodvariance; no statistical CI/pvalue.',
            'Mask differs fromauthorCC_mask+; not an exactFig2replication.',
            'No clashes/Hbond/saltgeometry yet; CAchange doesnotmeasurephysicalquality.',
            'Availablemodelcomparison notpure noise-weight intervention; nochannelactivity orcausalclaim.'],
        Rules_extra=0,full_question_answer=False)
    (out/'report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    (out/'residue_results.json').write_text(json.dumps(dict(rows=rows,collapsed=collapsed),indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
