"""Archive actual frozen inputs and outputs only after blind scores are sealed."""
from pathlib import Path
import json,tarfile,gzip,shutil,hashlib,datetime
r=Path(__file__).resolve().parents[1];repo=Path.cwd()/'dynamics-atlas-harness-luna-runtime-v1';dest=repo/'review/four-layer-20260910';assert(r/'blind/SCORE_SEAL.json').exists();assert(r/'outputs/UNBLINDING.json').exists()
archives=dest/'archives';archives.mkdir(exist_ok=True);manifest=[]
for name in ['E1a','E1b','ADK_plain','E2','E3','E4']:
 e=r/name
 if name!='E1a':assert not json.loads((e/'runtime/readiness.json').read_text()).get('approved_for_development')
 files=([e/'FREEZE.json',e/'E1_PLANTED_DEFECTS.json',e/'E1a_RESULTS.json']if name=='E1a'else[e/'FREEZE.json',e/'DESIGN.json'])
 for top in (['reference','packets']if name=='E1a'else['cases','runtime','runs','outputs']):
  for p in(e/top).rglob('*'):
   if p.is_symlink()or not p.is_file()or '__pycache__'in p.parts or p.suffix in ['.lock','.pyc']:continue
   if top=='runs' and len(p.relative_to(e/'runs').parts)>2 and p.relative_to(e/'runs').parts[1]=='source':continue # mounted source duplicates frozen case; preserve actual work files
   files.append(p)
 archive=archives/f'{name}_frozen_evidence.tar.gz'
 with archive.open('wb')as raw,gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0)as gz,tarfile.open(fileobj=gz,mode='w')as tar:
  for p in sorted(set(files)):
   info=tar.gettarinfo(str(p),arcname=f'{name}/{p.relative_to(e)}');info.uid=info.gid=0;info.uname=info.gname='';info.mtime=0
   with p.open('rb')as f:tar.addfile(info,f)
 manifest.append({'experiment':name,'archive':str(archive.relative_to(dest)),'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'files':len(set(files))})
 assert archive.stat().st_size<95000000,'Archive too large for ordinary Git publication'
for top in ['outputs','scripts','method_cards']:
 for p in(r/top).rglob('*'):
  if p.is_file()and'__pycache__'not in p.parts and p.suffix not in ['.pyc']:
   q=dest/top/p.relative_to(r/top);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
shutil.copytree(r/'blind',dest/'blind',dirs_exist_ok=True)
(dest/'ARCHIVE_MANIFEST.json').write_text(json.dumps({'created':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archives':manifest,'scope':'Frozen analysis packets, runtime, original submissions, tool logs, receipts and costs; raw trajectory downloads remain at cited source URLs.'},indent=2));print('Exported',len(manifest),'evidence archives;',sum(x['bytes']for x in manifest),'bytes')
