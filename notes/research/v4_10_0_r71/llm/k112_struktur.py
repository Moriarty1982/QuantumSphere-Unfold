"""k112: Sind die zusaetzlichen Dimensionen ab Grad 7 strukturell (wertunabhaengig) oder datenbedingt?
Vergleich: echte Daten J,theta gegen zufaellige J,theta gleicher Form, und gegen J echt + theta zufaellig."""
import sys,numpy as np
from pathlib import Path
SRC=Path(sys.argv[1])
src=(SRC/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{SRC}')")
def dims(J,theta,ps,label):
    g={'__file__':'x'};exec(src,g);g['J']=J;g['theta']=theta
    out=[]
    for p in ps:
        X=g['matrix'](p)[1];X=X/np.maximum(np.linalg.norm(X,axis=1),1e-300)[:,None]
        s=np.linalg.svd(X,compute_uv=False);n=X.shape[1];r=int(sum(s>s[0]*1e-9))
        out.append((p,n-r,f'{s[r-1]:.1e}|{s[r]:.1e}' if r<len(s) else f'{s[r-1]:.1e}|-'))
    print(label,out,flush=True)
w=np.load(SRC/'completion-omega-witness.npz');J0=w['completed_first_symbol'];th0=w['theta_normalized']
rng=np.random.default_rng(1)
ps=[2,3,4,5,6,7]
dims(J0,th0,ps,'echt           ')
dims(J0,rng.normal(size=480),ps,'J echt, theta zufaellig')
dims(J0,np.zeros(480),[2,3,4,5,6],'J echt, ohne Omega   ')
# J zufaellig, aber mit derselben 4-dim gemeinsamen Rechtskern-Struktur? zuerst ganz generisch:
dims(rng.normal(size=J0.shape),rng.normal(size=480),[2,3,4,5],'alles zufaellig      ')
