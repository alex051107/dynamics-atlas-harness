"""Narrow original-Figure4c vector correspondence; no fitted author quantities."""
from pathlib import Path
import json, re, math, statistics, xml.etree.ElementTree as ET

TASK=Path(__file__).resolve().parents[1]


def main():
    out=TASK/'outputs/q15_cy5_vector_concordance_v1'
    if (out/'report.json').exists():raise ValueError('PRESERVE_EXISTING_RESULT')
    out.mkdir(exist_ok=True)
    root=ET.parse(TASK/'outputs/q15_tmr_histogram_intake_v1/source_figure4.local.svg')
    paths=root.findall('.//{http://www.w3.org/2000/svg}path')
    number=r'[-+]?(?:\d*\.\d+|\d+)(?:[eE][-+]?\d+)?'
    def points(index):
        node=paths[index];tokens=re.findall('[MLC]|'+number,node.attrib['d'])
        residual=re.sub('[MLC]|'+number,'',node.attrib['d']).strip()
        assert not residual, residual
        result=[];i=0;current=None
        while i<len(tokens):
            command=tokens[i];i+=1
            if command in ['M','L']:
                current=tuple(map(float,tokens[i:i+2]));i+=2;result.append((*current,'vertex'))
            elif command=='C':
                values=list(map(float,tokens[i:i+6]));i+=6
                p0=current;p1=values[:2];p2=values[2:4];p3=values[4:6]
                # Include exact vertical extrema of cubic, not its control points.
                aa=3*(-p0[1]+3*p1[1]-3*p2[1]+p3[1])
                bb=6*(p0[1]-2*p1[1]+p2[1]);cc=3*(p1[1]-p0[1])
                roots=[]
                if abs(aa)<1e-14:
                    if abs(bb)>1e-14:roots=[-cc/bb]
                elif bb*bb-4*aa*cc>=0:
                    dd=math.sqrt(bb*bb-4*aa*cc);roots=[(-bb+dd)/(2*aa),(-bb-dd)/(2*aa)]
                for t in roots:
                    if 0<t<1:
                        v=[(1-t)**3*p0[j]+3*(1-t)**2*t*p1[j]+3*(1-t)*t*t*p2[j]+t**3*p3[j]for j in [0,1]]
                        result.append((*v,'cubic_extremum'))
                current=tuple(p3);result.append((*current,'vertex'))
            else:raise ValueError(command)
        a,b,c,d,e,f=map(float,re.findall(number,node.attrib['transform']));assert b==c==0
        return [[a*x+e,d*y+f,kind]for x,y,kind in result]
    aframe=points(1926);iframe=points(2034)
    axlo,axhi=min(v[0]for v in aframe),max(v[0]for v in aframe)
    ixlo,ixhi=min(v[0]for v in iframe),max(v[0]for v in iframe)
    yzero=points(1957)[0][1];y04=points(1977)[0][1];yscale=(yzero-y04)/.4
    source=json.loads((TASK/'outputs/q15_dye_response_v1/curves.local.json').read_text())
    results={};derived={}
    for cond,aniso_id,intensity_id in [('apo',1914,2032),('holo',1922,2033)]:
        ai=points(aniso_id);ip=[v for v in points(intensity_id)if ixlo<=v[0]<=ixhi]
        peak=min(ip,key=lambda v:v[1]);peak_t=-2+22*(peak[0]-ixlo)/(ixhi-ixlo)
        ac=[[-2+22*(x-axlo)/(axhi-axlo)-peak_t,(yzero-y)/yscale]for x,y,kind in ai]
        src=source['175_Cy5_'+cond];rows={}
        for label,lo,hi in [('early',2.,4.),('late',6.,8.)]:
            pv=[r for t,r in ac if lo<=t<=hi];sv=[r for t,r,I in src if lo-1e-9<=t<=hi+1e-9]
            assert len(pv)>100 and len(sv)==126
            rows[label]=dict(postpeak_window_ns=[lo,hi],PDF_points=len(pv),source_points=len(sv),
                PDF_mean_anisotropy=statistics.mean(pv),deposited_mean_anisotropy=statistics.mean(sv),
                difference=statistics.mean(pv)-statistics.mean(sv))
        results[cond]=dict(PDF_peak_display_time_ns=peak_t,peak_kind=peak[2],windows=rows,
            aniso_svg_path=aniso_id,intensity_svg_path=intensity_id)
        derived[cond]=ac
    report=dict(status='PDF_AND_DEPOSITED_CY5_ANISOTROPY_NUMERIC_DISCREPANCY',
        source='OriginalPeter2022PDFphysical7Figure4c Cy5 blackapo/redholo',
        axis=dict(time_limits=[-2,20],aniso_frame_x=[axlo,axhi],intensity_frame_x=[ixlo,ixhi],
            aniso_zero_y=yzero,aniso_04_y=y04,aniso_points_per_unit=yscale,
            source_registration='Each ownintensitypeak; no fittedlifetime orparameteralignment'),results=results,
        limits=['Only central2-4/6-8ns windows inside identified continuouspaths used',
            'SVGpointquantization andpanelregistration remain; no confidenceinterval',
            'No identificationofwhichcarrieriswrong orwhy; noautomaticrelabeling',
            'Unweighted windowmeans compared here, not earlier intensityweightedsummary; no absolutebrightness assumption'],
        Rules_extra=0,scientific_full_question_answer=False)
    (out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    (out/'aniso_coordinates.local.json').write_text(json.dumps(derived)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
