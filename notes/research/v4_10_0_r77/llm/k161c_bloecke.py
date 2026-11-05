"""k161c (Erkundung): Gewicht des Polarisationsraums P(xi) auf den drei Bloecken von Psi (je 4 komplexe = 8 reelle Komponenten)."""
import sys,math,numpy as np
from pathlib import Path
here=Path(__file__).parent;exec(open(here/'k161_spin.py').read().split("p=8;B=basis[p]")[0])
p=8;B=basis[p];wts=[];invs=[]
idx=[[4*b+s for s in range(4)]+[12+4*b+s for s in range(4)] for b in range(3)]
for x in nullrichtungen(100):
    W=wave(x,p);R=W-B@(B.T@W);_,s,Vt=np.linalg.svd(R);P=Vt[-6:].T;Pr=P@P.T
    wts.append([np.trace(Pr[np.ix_(i,i)]) for i in idx])
    sv=[np.linalg.svd(P[i],compute_uv=False) for i in idx];invs.append([int(np.sum(v>1e-6)) for v in sv])
print('Spur des Projektors je Block (Median, Summe 6):',np.array2string(np.median(wts,axis=0),precision=3),' Streuung',np.array2string(np.std(wts,axis=0),precision=3))
print('Rang von P eingeschraenkt auf Block (Median):',np.median(invs,axis=0))
