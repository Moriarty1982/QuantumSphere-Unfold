"""k163 (H63): Stabilisator {(A,B,C): sum_mu A_{mu nu} X_mu + X_nu B - C X_nu = 0} fuer X = F, F+G, F+G+dg aus J (32 x 96).
Aufruf: python k163_lorentz_F.py <Keim-Ordner>   (braucht k160_qmat.npy)"""
import sys,numpy as np
from pathlib import Path
here=Path(__file__).parent;J=np.load(Path(sys.argv[1])/'completion-omega-witness.npz')['completed_first_symbol'];Qc=np.load(here/'k160_qmat.npy')
L=np.zeros((16,16))
for mu in range(4):
    for nu in range(4):
        E=np.zeros((4,4));E[mu,nu]=1;L[:,4*mu+nu]=(E.T@Qc+Qc@E).ravel()
_,sl,Vl=np.linalg.svd(L);soQ=Vl[-6:];print('so(Q): Luecke',f'{sl[-7]/sl[0]:.1e}|{sl[-6]/sl[0]:.1e}')
def stab(r):
    X=[J[:r,m*24:(m+1)*24] for m in range(4)];nu_=16+576+r*r;cols=[]
    for mu in range(4):
        for nu in range(4):
            v=np.zeros((4,r,24));v[nu]=X[mu];cols.append(v.ravel())          # A_{mu nu}
    for i in range(24):
        for j in range(24):
            v=np.zeros((4,r,24))
            for nu in range(4): v[nu][:,j]=X[nu][:,i]                      # (X_nu B)[:,j] = X_nu[:,i] B_ij
            cols.append(v.ravel())
    for i in range(r):
        for k in range(r):
            v=np.zeros((4,r,24))
            for nu in range(4): v[nu][i,:]=-X[nu][k,:]                      # -(C X_nu)[i,:] = -C_ik X_nu[k,:]
            cols.append(v.ravel())
    M=np.array(cols).T;M=M/np.linalg.norm(M,axis=0)[None,:]
    _,s,Vt=np.linalg.svd(M);s=np.r_[s,np.zeros(M.shape[1]-len(s))]/s[0];lg=np.log10(np.maximum(s,1e-300))
    k=int(np.argmax(lg[:-1]-lg[1:]))+1;K=Vt[k:]      # Kern
    SA=K[:,:16];sa=np.linalg.svd(SA,compute_uv=False);rA=int(np.sum(sa/sa[0]>1e-6))
    UA=np.linalg.svd(SA)[2][:rA];c=np.linalg.svd(UA@soQ.T,compute_uv=False)   # Kosinusse der Hauptwinkel
    inter=int(np.sum(c>1-1e-8))
    print(f'Zeilen {r}: dim Stab {K.shape[0]} (Luecke {s[k-1]:.1e}|{s[k]:.1e}, Verh. {s[k-1]/max(s[k],1e-300):.0e}); dim pi_A {rA}; '
          f'Schnitt mit so(Q) {inter}; Kosinusse {np.array2string(np.sort(c)[::-1],precision=10)}',flush=True)
    return K
for r in (24,28,32): stab(r)
