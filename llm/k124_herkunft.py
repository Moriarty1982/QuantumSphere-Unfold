import json,sys,itertools,numpy as np
from pathlib import Path
exec(open('k121_rahmen.py').read().split("print('det E")[0])
Pl=np.load('ebenen.npy');SRC=Path(sys.argv[1])
planes=[np.linalg.svd(np.hstack([Pl[k].real,Pl[k].imag]))[0][:,:2] for k in range(2)]   # Kovektor-Ebenen, xi-Koordinaten
def angle(A,B):
    A=np.linalg.qr(A)[0];B=np.linalg.qr(B)[0];c=np.linalg.svd(A.T@B,compute_uv=False);return np.degrees(np.arccos(np.clip(c.min(),-1,1)))
Ei=np.array([[np.imag(psi.conj()@Qm[a]@cov[m]) for m in range(4)] for a in range(4)])
Ek=np.array([[np.real(psi.conj()@Km[a]@cov[m]) for m in range(4)] for a in range(4)])
Eki=np.array([[np.imag(psi.conj()@Km[a]@cov[m]) for m in range(4)] for a in range(4)])
np.set_printoptions(precision=3,suppress=True)
for name,Mx in [('Im Q',Ei),('Re K',Ek),('Im K',Eki)]:
    print(name,'Rang',np.linalg.matrix_rank(Mx,1e-9*abs(Mx).max()))
    for lab,L in [('V Mx (auf xi rechts)',None)]:
        pass
    # lineare Abbildung auf Kovektoren: xi -> E^T^{-1} Mx^T xi  (beide sind a x mu; Kovektor xi_mu, Rahmenkomponenten eta = V^T xi)
    T=Mx.T@np.linalg.inv(E.T)            # xi -> Mx^T (E^T)^{-1} xi
    ev,evec=np.linalg.eig(T);print('   Eigenwerte',np.round(ev,4))
    # reelle invariante Ebenen aus komplexen Paaren bzw. Paaren reeller Eigenvektoren
    cand=[]
    for i,j in itertools.combinations(range(4),2):
        B=np.column_stack([evec[:,i],evec[:,j]])
        R=np.hstack([B.real,B.imag]);u,s,_=np.linalg.svd(R)
        if s[2]<1e-8*s[0]: cand.append(((i,j),u[:,:2]))
    for (i,j),B in cand:
        print(f'   invariante Ebene ({i},{j}): Winkel zu Ebene0 {angle(B,planes[0]):.3f}, zu Ebene1 {angle(B,planes[1]):.3f}')
