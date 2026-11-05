"""k163b (Erkundung nach H63): Ist pi_A(Stab F) = R*1 + so(Q') fuer eine eigene quadratische Form Q'? Vergleich Q' mit Q und Rangabfall von F(xi)."""
import sys,numpy as np
from pathlib import Path
here=Path(__file__).parent;exec(open(here/'k163_lorentz_F.py').read().split('for r in (24,28,32)')[0])
K=stab(24);SA=K[:,:16];UA=np.linalg.svd(SA)[2][:7];As=[u.reshape(4,4) for u in UA]
A0=[a-np.trace(a)/4*np.eye(4) for a in As]
sym=[(i,j) for i in range(4) for j in range(i,4)];Mq=np.zeros((16*len(A0),10))
for k,(i,j) in enumerate(sym):
    S=np.zeros((4,4));S[i,j]=S[j,i]=1
    Mq[:,k]=np.concatenate([(a.T@S+S@a).ravel() for a in A0])
_,s,Vt=np.linalg.svd(Mq);print('Q\'-Bedingung: kleinste Singulaerwerte',np.array2string(s[-3:]/s[0],precision=2))
q=Vt[-1];Qp=np.zeros((4,4))
for k,(i,j) in enumerate(sym): Qp[i,j]=Qp[j,i]=q[k]
ev=np.linalg.eigvalsh(Qp);Qp=Qp*np.sign(-np.prod(ev)) if False else Qp;print('Eigenwerte Q\' (normiert):',np.array2string(np.sort(ev)/np.max(abs(ev)),precision=4))
nQ=lambda M:M/np.linalg.norm(M);cosQ=abs(np.sum(nQ(Qp)*nQ(Qc)));print(f"Kosinus(Q', Q) = {cosQ:.6f}")
# traceless-Anteil wirklich in so(Q')?
res=max(np.linalg.norm(a.T@Qp+Qp@a)/np.linalg.norm(a) for a in A0);print(f"max |A0^T Q' + Q' A0|/|A0| = {res:.1e}")
F=[J[:24,m*24:(m+1)*24] for m in range(4)];rng=np.random.default_rng(3)
def drop(xi): s=np.linalg.svd(sum(xi[m]*F[m] for m in range(4)),compute_uv=False);return int(np.sum(s/s[0]<1e-9))
def null_of(Qm):
    while True:
        sp=rng.normal(size=3);a=Qm[0,0];b=2*Qm[0,1:]@sp;c=sp@Qm[1:,1:]@sp;d=b*b-4*a*c
        if d>=0: return np.r_[(-b+np.sqrt(d))/(2*a),sp]
print('Rangabfall von F(xi): auf Q\'-Kegel',[drop(null_of(Qp)) for _ in range(5)],' auf Q-Kegel',[drop(null_of(Qc)) for _ in range(5)],' generisch',[drop(rng.normal(size=4)) for _ in range(3)])
np.save(here/'k163_Qp.npy',Qp)
