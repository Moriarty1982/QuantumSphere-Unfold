"""k162 (H62): Stabilisator-Algebra s_p = {(A,B) in gl(4) x gl(24): X_{A,B} g''_p in g''_p}, p = 6,7,8.
X = rho_p(A) (x) 1 + 1 (x) B; rho_p aus xi -> A xi auf den Komponenten xi^alpha/sqrt(alpha!).
Aufruf: QS_DPS=70 QS_HPWORK=hp_work2 python k162_symmetrien.py   (braucht k160_qmat.npy)"""
import sys,math,time,pickle,numpy as np
from pathlib import Path
here=Path(__file__).parent;sys.argv=[str(here/'k158_cartan_hp.py'),'7']
exec(open(here/'k158_cartan_hp.py').read().split('for seed in (1,2,3):')[0])
Qc=np.load(here/'k160_qmat.npy');t0=time.time()
def rho(p,mu,nu):
    ms=mon(p);look={a:i for i,a in enumerate(ms)};R=np.zeros((len(ms),len(ms)))
    for i,a in enumerate(ms):
        if a[mu]==0: continue
        b=list(a);b[mu]-=1;b[nu]+=1;b=tuple(b);R[i,look[b]]+=a[mu]*math.sqrt(fac(b)/fac(a))
    return R
def gram(p,s=12):
    Qb=basis[p];n,d=Qb.shape;m=n//24;Q3=Qb.reshape(m,24,d);rh=[rho(p,mu,nu) for mu in range(4) for nu in range(4)];G=np.zeros((592,592))
    for c0 in range(0,d,s):
        c=slice(c0,min(d,c0+s));Qs=Q3[:,:,c];k=Qs.shape[2];Y=np.zeros((m,24,k,592))
        for g,R in enumerate(rh): Y[...,g]=np.einsum('ab,bjd->ajd',R,Qs)
        for i in range(24):
            for j in range(24): Y[:,i,:,16+24*i+j]=Qs[:,j,:]
        Y=Y.reshape(n,k*592);Y=Y-Qb@(Qb.T@Y);Y=Y.reshape(n*k,592)   # M = (1 - Pi) X Q ohne Ausloeschung
        G+=Y.T@Y
    return G
# so(Q): A^T Q + Q A = 0
L=np.zeros((16,16))
for mu in range(4):
    for nu in range(4):
        E=np.zeros((4,4));E[mu,nu]=1;L[:,4*mu+nu]=(E.T@Qc+Qc@E).ravel()
_,sl,Vl=np.linalg.svd(L);soQ=Vl[-6:];print('so(Q): kleinste Singulaerwerte',np.array2string(sl[-7:]/sl[0],precision=1))
out={}
for p in (6,7,8):
    G=gram(p);np.save(here/f'k162_G{p}.npy',G);w,U=np.linalg.eigh(G);w=np.abs(w)/np.abs(w).max();o=np.argsort(w);w,U=w[o],U[:,o];lg=np.log10(np.maximum(w,1e-300))
    j=int(np.argmax(lg[1:]-lg[:-1]))+1   # Anzahl kleiner Werte
    S=U[:,:j].T;SA=S[:,:16];sa=np.linalg.svd(SA,compute_uv=False);rA=int(np.sum(sa/sa[0]>1e-6)) if sa[0]>0 else 0
    SB0=int(j-rA)
    rk=np.linalg.svd(np.vstack([SA,soQ]),compute_uv=False);rAll=int(np.sum(rk/rk[0]>1e-6));inter=rA+6-rAll
    out[p]=dict(dim=j,luecke=(float(w[j-1]),float(w[j])),dimA=rA,innere=SB0,schnitt=inter,S=S)
    print(f'[{time.time()-t0:4.0f} s] p={p}: dim s_p {j} (Luecke {w[j-1]:.1e}|{w[j]:.1e}, Verh. {w[j]/max(w[j-1],1e-300):.0e}); dim pi_A {rA}; innere (A=0) {SB0}; Schnitt mit so(Q) {inter}',flush=True)
    print('     Gram-Werte um die Luecke:',np.array2string(w[max(0,j-4):j+6],precision=1),flush=True)
pickle.dump({p:out[p]['S'] for p in out},open(here/'k162_stab.pkl','wb'))
