"""Check delivery structure; never treat this as scientific validation."""
import argparse,json,re,zipfile
from pathlib import Path
import xml.etree.ElementTree as E

def check(root,profile):
    names={'progress':('DYNAMICS_ATLAS_PROGRESS_REPORT_20260912_ZH','DYNAMICS_ATLAS_PROGRESS_REPORT_20260912',8,20,6),'round':('DYNAMICS_ATLAS_HSP90_Q01_DEEP_READER_ZH','DYNAMICS_ATLAS_HSP90_Q01_COLLABORATOR_REPORT',10,25,5),'science':('DEEP_READER_ZH','COLLABORATOR_REPORT',6,1,5)}
    reader,deck,minslides,minclaims,minheads=names[profile]; failures=[]
    required=[reader+'.md',reader+'.html',deck+'.pptx','claim_source_map.jsonl','REPORT_INDEX.md']
    if profile!='progress':required+=['ROUND_BRIEF_ZH.md','ROUND_BRIEF_ZH.html','review_report.md']
    for name in required:
        if not (root/name).is_file() or not (root/name).stat().st_size:failures.append('missing/empty: '+name)
    if failures:return {'pass':False,'failures':failures}
    nheads=len(re.findall(r'<h2(?:\s|>)',(root/(reader+'.html')).read_text()))
    if nheads<minheads:failures.append(f'headings {nheads} < {minheads}')
    rows=[json.loads(x) for x in (root/'claim_source_map.jsonl').read_text().splitlines() if x.strip()]
    if len(rows)<minclaims:failures.append(f'claims {len(rows)} < {minclaims}')
    with zipfile.ZipFile(root/(deck+'.pptx')) as z:
        slides=[x for x in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml',x)]
        if len(slides)<minslides:failures.append(f'slides {len(slides)} < {minslides}')
        for slide in slides:
            i=re.search(r'(\d+)\.xml',slide).group(1);notes=f'ppt/notesSlides/notesSlide{i}.xml'
            if notes not in z.namelist():failures.append(f'no notes slide {i}');continue
            texts=E.fromstring(z.read(notes)).findall('.//{http://schemas.openxmlformats.org/drawingml/2006/main}t')
            if len(''.join(x.text or '' for x in texts).strip())<15:failures.append(f'empty notes slide {i}')
    return {'pass':not failures,'profile':profile,'headings':nheads,'slides':len(slides),'claims':len(rows),'failures':failures,'scope':'artifact presence and structure only; content requires source audit'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--profile',choices=['progress','round','science'],default='round');a=p.parse_args();r=check(a.root,a.profile);print(json.dumps(r,ensure_ascii=False,indent=2));raise SystemExit(0 if r['pass'] else 1)
