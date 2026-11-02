import sys,numpy as np,time
from pathlib import Path
SRC=Path(sys.argv[1])
src=(SRC/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{SRC}')")
g={'__file__':'x'};exec(src,g);th0=g['theta'].copy()
rng=np.random.default_rng(3);thr=rng.normal(size=480)
for label,th,ps in [('echt',th0,[8,9,10]),('zufaellig',thr,[8,9])]:
    g['theta']=th
    for p in ps:
        t=time.time();X=g['matrix'](p)[1];X=X/np.maximum(np.linalg.norm(X,axis=1),1e-300)[:,None]
        s=np.linalg.svd(X,compute_uv=False);n=X.shape[1];r=int(sum(s>s[0]*1e-9))
        print(label,p,'dim',n-r,'Grenze',f'{s[r-2]:.1e} {s[r-1]:.1e} | {s[r]:.1e}','t',round(time.time()-t),flush=True)
