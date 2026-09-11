from pathlib import Path
import urllib.request,json,subprocess,hashlib,datetime
root=Path(__file__).resolve().parents[1];dest=root/'inputs';dest.mkdir(exist_ok=True)
with urllib.request.urlopen('https://zenodo.org/api/records/5583119',timeout=60)as r:meta=json.load(r)
(dest/'zenodo_metadata.json').write_text(json.dumps(meta,indent=2));files=meta['files'];assert len(files)==4 and sum(f['size']for f in files)<=1500000000
records=[]
for f in files:
 p=dest/f['key'];tmp=p.with_suffix(p.suffix+'.part')
 if not p.exists():
  for attempt in range(1,4):
   cmd=['curl','--fail','--location','--silent','--show-error','--max-time','600','--continue-at','-','--output',str(tmp),f['links']['self']]
   q=subprocess.run(cmd,capture_output=True,text=True)
   if q.returncode==0 and tmp.stat().st_size==f['size']:tmp.rename(p);break
   print(json.dumps({'file':f['key'],'attempt':attempt,'status':'retryable_download_failure','bytes':tmp.stat().st_size if tmp.exists()else 0,'stderr':q.stderr[-200:]}),flush=True)
  assert p.exists(),f'Download failed after three attempts: {p.name}'
 assert p.stat().st_size==f['size'];sha=hashlib.sha256();md=hashlib.md5()
 with p.open('rb')as h:
  for b in iter(lambda:h.read(8*1024*1024),b''):sha.update(b);md.update(b)
 assert 'md5:'+md.hexdigest()==f['checksum']
 records.append({'name':p.name,'bytes':p.stat().st_size,'sha256':sha.hexdigest(),'zenodo_checksum':f['checksum'],'url':f['links']['self'],'license':meta['metadata']['license'],'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
 (root/'outputs/DOWNLOAD_MANIFEST.json').write_text(json.dumps({'record':5583119,'files':records,'total_bytes':sum(r['bytes']for r in records),'complete':len(records)==4},indent=2));print(json.dumps({'file':p.name,'verified':True,'bytes':p.stat().st_size}),flush=True)
