"""k161b (Erkundung nach H61): Ist P(xi) eine reelle Form des masselosen Dirac-Polarisationsraums?
Pruefe dim(P+JP), Winkel P vs JP, und ob P+JP = ker(xi_a gamma^a) (realifiziert, drei Spinoren; +-Vorzeichen beider Konventionen)."""
import sys,math,numpy as np
from pathlib import Path
here=Path(__file__).parent;src=open(here/'k161_spin.py').read().split("p=8;B=basis[p]")[0];exec(src)
be=np.diag([1,1,-1,-1.]);al=[np.block([[Z2,s],[s,Z2]]) for s in (sx,sy,sz)];gam=[be]+[be@a for a in al]
p=8;B=basis[p];out=[]
for x in nullrichtungen(100):
    W=wave(x,p);R=W-B@(B.T@W);_,s,Vt=np.linalg.svd(R);P=Vt[-6:].T
    PJ=np.hstack([P,Jm@P]);sPJ=np.linalg.svd(PJ,compute_uv=False);dimPJ=int(np.sum(sPJ/sPJ[0]>1e-6))
    cosmax=np.linalg.svd(P.T@Jm@P,compute_uv=False)[0]          # 0: P senkrecht JP (total reell)
    xh=V.T@x;r=[]
    for sg in (1,-1):   # Konventionen xi_a gamma^a mit eta-Hebung bzw. ohne
        xa=xh*np.array([1,sg,sg,sg]);D=real(np.kron(np.eye(3),sum(xa[a]*gam[a] for a in range(4))))
        Ud,sd,Vd=np.linalg.svd(D);kd=int(np.sum(sd/sd[0]<1e-8));K=Vd[-kd:].T
        Qp,_=np.linalg.qr(PJ);ang=np.linalg.svd(K.T@Qp,compute_uv=False)  # Hauptwinkel-Kosinusse
        r.append((kd,float(np.linalg.norm(D@P)/np.linalg.norm(D)),float(ang.min()) if kd else 0))
    out.append((dimPJ,cosmax,r))
print('dim(P+JP):',sorted(set(o[0] for o in out)),' max cos(P,JP) Median',f"{np.median([o[1] for o in out]):.1e}")
for i,sg in enumerate(('eta-gehoben','ungehoben')):
    print(f"Dirac {sg}: dim ker {sorted(set(o[2][i][0] for o in out))}, |D P|/|D| Median {np.median([o[2][i][1] for o in out]):.1e}, kleinster Kosinus(ker, P+JP) Median {np.median([o[2][i][2] for o in out]):.3f}")
