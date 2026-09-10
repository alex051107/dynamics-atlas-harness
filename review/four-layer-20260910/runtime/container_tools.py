"""Container-only tools. No model credential or host project mount."""
import json,os,subprocess,sys,base64
from pathlib import Path

def dispatch(a):
    kind=a['kind']
    if kind=='python':
        r=subprocess.run([sys.executable,'-c',a['code']],cwd='/work',capture_output=True,text=True,timeout=85)
        return {'returncode':r.returncode,'stdout':r.stdout[:24000],'stderr':r.stderr[:8000]}
    p=Path(a.get('path','/source')).resolve()
    if not any(p==b or b in p.parents for b in [Path('/source'),Path('/work'),Path('/tools')]):
        raise ValueError('Tool path outside public workspace')
    if kind=='list':return {'files':[str(x) for x in sorted(p.rglob('*')) if x.is_file()][:1500]}
    if kind=='read':
        lines=p.read_text(errors='replace').splitlines();start=max(1,int(a.get('start_line',1)));n=min(180,int(a.get('lines',100)))
        return {'total_lines':len(lines),'text':'\n'.join(f'{i+1}: {s}' for i,s in enumerate(lines[start-1:start-1+n],start-1))}
    if kind=='search':
        q=a['query'].lower();files=[p] if p.is_file() else list(p.rglob('*'));out=[]
        for f in files:
            if not f.is_file() or f.suffix.lower() not in ['.md','.txt','.py','.rst','.csv','.json']:continue
            for i,s in enumerate(f.read_text(errors='replace').splitlines()):
                if q in s.lower():out.append({'file':str(f),'line':i+1,'text':s[:500]})
                if len(out)>=80:return out
        return out
    if kind=='image':
        if p.suffix.lower()=='.pdf':
            import fitz
            d=fitz.open(p);pg=d.load_page(int(a.get('page',0)));pix=pg.get_pixmap(matrix=fitz.Matrix(1.4,1.4));raw=pix.tobytes('png')
        else:
            from PIL import Image
            import io
            im=Image.open(p);im.thumbnail((1600,1600));b=io.BytesIO();im.save(b,format='PNG');raw=b.getvalue()
        return {'image_base64':base64.b64encode(raw).decode(),'mime':'image/png','source':str(p),'page':a.get('page')}
    raise ValueError('Unknown tool kind')
if __name__=='__main__':
    try: print(json.dumps(dispatch(json.load(sys.stdin)),ensure_ascii=False))
    except Exception as e: print(json.dumps({'error':type(e).__name__,'message':str(e)}))
