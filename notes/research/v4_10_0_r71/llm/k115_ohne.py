import sys,numpy as np
from pathlib import Path
SRC=Path(sys.argv[1])
src=(SRC/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{SRC}')")
g={'__file__':'x'};exec(src,g);g['theta']=np.zeros(480)
for p in [7,8]:
    X=g['matrix'](p)[1];keep=np.linalg.norm(X,axis=1)>0;X=X[keep];X=X/np.linalg.norm(X,axis=1)[:,None]
    s=np.linalg.svd(X,compute_uv=False);r=int(sum(s>s[0]*1e-9));print('ohne Omega',p,X.shape[1]-r,f'{s[r-1]:.1e}|{s[r]:.1e}',flush=True)
