"""Conditional Q05 geometry preparation; no trajectory reader or scientific verdict.

Equal-atom-weight N/CA/C is an explicit GROMACS-style backbone assumption.
All coordinates supplied to these functions must already be in Angstrom.
"""
from pathlib import Path
import numpy as np

AA=frozenset('ALA ARG ASN ASP CYS GLN GLU GLY HIS ILE LEU LYS MET PHE PRO SER THR TRP TYR VAL HSD HSE HSP'.split())
AXIS_RTOL=1e-6
AXIS_ATOL_A2=1e-10


def selected_backbone(pdb_path: Path):
    selected=[];excluded=[];index=-1
    for line in pdb_path.read_text().splitlines():
        if line[:6].strip() not in ('ATOM','HETATM'):continue
        index+=1
        atom=line[12:16].strip();resname=line[17:20].strip();chain=line[21:22]
        if resname not in AA or atom not in ('N','CA','C'):continue
        if line[16:17].strip() or line[26:27].strip():raise ValueError('AMBIGUOUS_ALTLOC_OR_INSERTION_CODE')
        resid=int(line[22:26])
        entry={'coordinate_index_zero_based':index,'pdb_serial':int(line[6:11]),
               'chain':chain,'pdb_residue_number':resid,'residue_name':resname,'atom_name':atom,
               'coordinates_A':[float(line[30:38]),float(line[38:46]),float(line[46:54])]}
        (excluded if 55<=resid<=63 else selected).append(entry)
    identities=[(v['chain'],v['pdb_residue_number'],v['atom_name']) for v in selected]
    if len(set(identities))!=len(identities):raise ValueError('DUPLICATE_ATOM_IDENTITY')
    return selected,excluded


def _coordinates(value):
    a=np.asarray(value,dtype=float)
    if a.ndim!=2 or a.shape[1]!=3 or len(a)<3 or not np.all(np.isfinite(a)):
        raise ValueError('FINITE_N_BY_3_COORDINATES_REQUIRED')
    return a-a.mean(axis=0)


def align_fixed_reference(coordinates_A,reference_A):
    x=_coordinates(coordinates_A);y=_coordinates(reference_A)
    if x.shape!=y.shape:raise ValueError('ATOM_ORDER_OR_COUNT_MISMATCH')
    if np.linalg.matrix_rank(y)<2:raise ValueError('REFERENCE_FRAME_DEGENERATE')
    u,_,vt=np.linalg.svd(x.T@y)
    correction=np.eye(3);correction[-1,-1]=np.linalg.det(u@vt)
    return x@(u@correction@vt)


def frame_geometry(coordinates_A,reference_A=None):
    x=_coordinates(coordinates_A)
    if reference_A is not None:x=align_fixed_reference(x,reference_A)
    tensor=x.T@x/len(x)
    values,vectors=np.linalg.eigh(tensor)
    if values[-1]<=0:raise ValueError('ZERO_EXTENT_STRUCTURE')
    gap=float(values[-1]-values[-2])
    numeric_degenerate=bool(np.isclose(values[-1],values[-2],rtol=AXIS_RTOL,atol=AXIS_ATOL_A2))
    axis=None
    if not numeric_degenerate:
        vector=vectors[:,-1]
        if vector[np.argmax(abs(vector))]<0:vector=-vector
        axis=vector.tolist()
    return {'gyration_tensor_A2':tensor.tolist(),'eigenvalues_A2_ascending':values.tolist(),
            'acylindricity_A2':gap,'sqrt_acylindricity_A':float(np.sqrt(max(0,gap))),
            'relative_inplane_eigengap':gap/float(values[-1]),'axis_unoriented':axis,
            'axis_status':'NUMERICALLY_DEGENERATE' if numeric_degenerate else 'NUMERICALLY_DEFINED_UNCERTAINTY_NOT_VALIDATED',
            'reference':'FIXED_LABELLED_PROTEIN_REFERENCE' if reference_A is not None else 'SUPPLIED_COORDINATE_FRAME',
            'atomic_weighting':'EQUAL_ATOM_WEIGHTS','scientific_axis_switch_verdict':'NOT_EMITTED'}


def axis_angle_degrees(first,second):
    if first is None or second is None:return None
    a=np.asarray(first);b=np.asarray(second)
    return float(np.degrees(np.arccos(np.clip(abs(a@b),0,1))))
