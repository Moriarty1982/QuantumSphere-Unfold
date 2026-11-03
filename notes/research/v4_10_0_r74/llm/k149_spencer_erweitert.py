"""k149 (Erkundung): Spencer-Kohomologie H^{k,2} des erweiterten Symbols g'' (konsistente Daten wie k148).
Obergrenze fuer weitere versteckte Bedingungen. Aufruf: python k149_spencer_erweitert.py <Ordner> [k ...]"""
import sys,itertools,numpy as np
from pathlib import Path
here=Path(__file__).parent;ks=[int(k) for k in sys.argv[2:]] or [5,6,7];sys.argv=sys.argv[:2]+['6']
src=open(here/'k148_konsistent.py').read().split("print('Gueltigkeit")[0];exec(src)
def forms(j): return list(itertools.combinations(range(4),j))
def delta(pp,j,N):
    Fj=forms(j);Fj1=forms(j+1);fi={f:n for n,f in enumerate(Fj1)};I=[iota(pp,np.eye(4)[mu])@N for mu in range(4)]
    h=I[0].shape[0];out=np.zeros((h*len(Fj1),N.shape[1]*len(Fj)))
    for c,f in enumerate(Fj):
        for mu in range(4):
            if mu in f: continue
            new=tuple(sorted((mu,)+f));sign=(-1)**sum(1 for x in f if x<mu);r=fi[new]
            out[r*h:(r+1)*h,c*N.shape[1]:(c+1)*N.shape[1]]+=sign*I[mu]
    return out
for with_sigma in (False,True):
    for k in ks:
        Nk=kernel(k,with_sigma);Nk1=kernel(k+1,with_sigma)
        d2=delta(k,2,Nk);r2,a2,b2=rank_gap(np.linalg.svd(d2,compute_uv=False));ker2=d2.shape[1]-r2
        d1=delta(k+1,1,Nk1);r1,a1,b1=rank_gap(np.linalg.svd(d1,compute_uv=False))
        print(f"{'g erweitert' if with_sigma else 'g geeicht  '} H^({k},2) = {ker2-r1}  (ker {ker2}, Bild {r1}; Luecken delta {a2/b2:.0e}, {a1/b1:.0e})",flush=True)
