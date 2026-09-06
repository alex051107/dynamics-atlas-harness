from pathlib import Path
import urllib.request,json,struct,datetime
p=Path('autoresearch/tasks/dynamics_atlas_paper_result_reproduction_screen_20260904');out=p/'outputs/q02_cpmg_inventory_v1';out.mkdir(exist_ok=False)
url='https://bmrbig.org/deposition/released/44/HSP90-NTD-CPMG_WT_293K.zip';size=213907264;receipts=[]
def fetch(start,end):
 request=urllib.request.Request(url,headers={'Range':f'bytes={start}-{end}','Accept-Encoding':'identity','If-Range':'"1657112476.128644-213907264-2093228031"'})
 with urllib.request.urlopen(request,timeout=45) as response:
  record={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':response.url,'request_range':[start,end],'status':response.status,'headers':dict(response.headers)}
  receipts.append(record)
  if response.status!=206 or response.headers.get('Content-Range')!=f'bytes {start}-{end}/{size}':
   raise ValueError('EXACT_RANGE_RESPONSE_REQUIRED')
  data=response.read(end-start+2)
  if len(data)!=end-start+1:raise ValueError('RANGE_LENGTH_MISMATCH')
  return data
try:
 tail=fetch(size-65536,size-1);(out/'tail.bin').write_bytes(tail)
 index=tail.rfind(b'PK\x05\x06')
 if index<0:raise ValueError('END_DIRECTORY_NOT_IN_BOUNDED_TAIL')
 _,disk,cd_disk,ndisk,nall,cdsize,cdoffset,comment=struct.unpack_from('<IHHHHIIH',tail,index)
 if disk or cd_disk or ndisk!=nall or cdoffset==0xffffffff or cdsize>196608:raise ValueError('UNSUPPORTED_OR_OVERSIZE_DIRECTORY')
 central=tail[cdoffset-(size-65536):cdoffset-(size-65536)+cdsize] if cdoffset>=size-65536 else fetch(cdoffset,cdoffset+cdsize-1)
 (out/'central_directory.bin').write_bytes(central);members=[];i=0
 while i<len(central):
  values=struct.unpack_from('<IHHHHHHIIIHHHHHII',central,i)
  signature,vmade,vneed,flag,method,tm,dt,crc,cs,us,nl,el,cl,disk,inta,exta,offset=values
  if signature!=0x02014b50:raise ValueError('CENTRAL_SIGNATURE')
  name=central[i+46:i+46+nl].decode('utf-8' if flag&2048 else 'cp437')
  members.append({'name':name,'flags':flag,'compression':method,'crc32':f'{crc:08x}','compressed_bytes':cs,'expanded_bytes':us,'local_header_offset':offset})
  i+=46+nl+el+cl
 if len(members)!=nall:raise ValueError('CENTRAL_ENTRY_COUNT')
 (out/'members.json').write_text(json.dumps(members,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'entries':len(members),'directory_bytes':cdsize,'folders':[m['name']for m in members if m['name'].endswith('/')]},ensure_ascii=False,indent=2)[:7000])
 status='DIRECTORY_RECEIVED_ONLY_NO_SCIENTIFIC_PAYLOAD'
except Exception as exc:
 status='SOURCE_DIRECTORY_REQUEST_FAILED';receipts.append({'error_type':type(exc).__name__,'error':str(exc)});print(status,type(exc).__name__,str(exc))
finally:
 (out/'receipt.json').write_text(json.dumps({'status':status,'source_archive_declared_size':size,'source_archive_declared_md5':None,'whole_archive_verified':False,'HTTP':receipts},indent=2)+'\n')
