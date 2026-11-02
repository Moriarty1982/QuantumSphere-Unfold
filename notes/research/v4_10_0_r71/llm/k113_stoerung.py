"""k113: Liegt theta auf einem Sonderort? Stoere theta zufaellig um eps und verfolge die kleinsten Singulaerwerte bei Grad 6,7."""
import sys,numpy as np
from pathlib import Path
SRC=Path(sys.argv[1])
src=(SRC/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{SRC}')")
g={'__file__':'x'};exec(src,g)
th0=g['theta'].copy();rng=np.random.default_rng(7);d=rng.normal(size=480);d/=np.linalg.norm(d)
for eps in [0,1e-12,1e-10,1e-8,1e-6,1e-4]:
    g['theta']=th0+eps*np.linalg.norm(th0)*d
    row=[]
    for p,exp in [(6,565),(7,722)]:
        X=g['matrix'](p)[1];X=X/np.maximum(np.linalg.norm(X,axis=1),1e-300)[:,None]
        s=np.linalg.svd(X,compute_uv=False);r=X.shape[1]-exp
        row.append(f'p={p}: '+' '.join(f'{v:.1e}' for v in s[r-6:r+1]))
    print(f'eps={eps:.0e} | '+' || '.join(row),flush=True)
