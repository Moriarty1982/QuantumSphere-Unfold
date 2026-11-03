"""k158: Cartan-Test des erweiterten Symbols aus dem hochgenauen Unterraum g''_6 (k157: g''_6 = N6 . ker C).
g''_{p+1} = Fortsetzung von g''_p (iota_mu v in g''_p fuer alle mu). Basis von g''_6 hochgenau bestimmt, danach float.
Aufruf: QS_DPS=70 QS_HPWORK=hp_work2 python k158_cartan_hp.py [pmax]"""
import sys,math,pickle,numpy as np,flint
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent));from k154_hp_tools import *
pmax=int(sys.argv[1]) if len(sys.argv)>1 else 8
ld=lambda f:arb_mat([[arb(x) for x in row] for row in pickle.load(open(W/f,'rb'))])
N6=ld('k157_N6.pkl');C=ld('k157_C.pkl');print('N6',N6.nrows(),N6.ncols(),' C',C.nrows(),C.ncols(),flush=True)
# ker C hochgenau (rechts): float-SVD + Newton
Cf=tofloat(C);U,s,Vt=np.linalg.svd(Cf,full_matrices=True);t=s/s[0];r=int(np.sum(t>1e-30)) if False else None
gl=np.r_[t,0];print('Singulaerwerte von C (relativ), kleinste 6 echte:',np.array2string(t[-6:],precision=2),flush=True)
# Rang 24 (aus k157, Luecke 1e58 im Gram); Newton auf dem Kern
r=24;K=Vt[r:].T;Ur,Sr,Vr=U[:,:r],s[:r],Vt[:r].T;Ka=arb_mat(K.tolist())
for it in range(8):
    rf=tofloat(C*Ka);nr=np.max(abs(rf))/s[0]
    if nr<1e-60: break
    Ka=Ka-arb_mat((Vr@((Ur.T@rf)/Sr[:,None])).tolist())
print(f'ker C: dim {Ka.ncols()}, Residuum {nr:.0e}',flush=True)
G6=tofloat(N6*Ka);Q6,_=np.linalg.qr(G6);print('g\'\'_6: dim',Q6.shape[1],flush=True)
mon_=lambda d:mon(d)
def iota(p,e):
    ci=mon(p);ri=mon(p-1);look={a:n for n,a in enumerate(ci)};M=np.zeros((len(ri)*24,len(ci)*24))
    for rn,b in enumerate(ri):
        for mu in range(4):
            if e[mu]==0: continue
            bb=list(b);bb[mu]+=1;cn=look[tuple(bb)];M[rn*24:(rn+1)*24,cn*24:(cn+1)*24]+=e[mu]*math.sqrt(b[mu]+1)*np.eye(24)
    return M
def rank_gap(s):
    if len(s)==0 or s[0]==0: return 0,np.inf,1.0
    s=s/s[0];m=int(np.sum(s>1e-15));t=np.r_[s[:m],1e-17] if m==len(s) else s[:m+1];k=int(np.argmax(np.log(t[:-1]/t[1:])));return k+1,t[k],t[k+1]
basis={6:Q6};gaps=[]
for p in range(7,pmax+2):
    Pc=np.eye(basis[p-1].shape[0])-basis[p-1]@basis[p-1].T
    X=np.vstack([Pc@iota(p,np.eye(4)[mu]) for mu in range(4)])
    _,s,Vt=np.linalg.svd(X,full_matrices=False);r,a,b=rank_gap(s);basis[p]=Vt[r:].T;gaps.append(a/b)
    print(f"g''_{p}: dim {basis[p].shape[1]} (Luecke {a:.1e}|{b:.1e}, Verh. {a/b:.0e})",flush=True)
for seed in (1,2,3):
    Eb=np.linalg.qr(np.random.default_rng(seed).normal(size=(4,4)))[0].T
    for p in range(6,pmax+1):
        Nb=basis[p];dk=[Nb.shape[1]];wk=[];rows=np.zeros((0,Nb.shape[0]))
        for k in range(1,4):
            rows=np.vstack([rows,iota(p,Eb[k-1])]);r,a,b=rank_gap(np.linalg.svd(rows@Nb,compute_uv=False));wk.append(a/b);dk.append(Nb.shape[1]-r)
        S=sum(dk);d1=basis[p+1].shape[1];flag='GLEICH (involutiv)' if S==d1 else ('kleiner (nicht involutiv)' if d1<S else 'VERLETZT')
        print(f"seed {seed} p={p}: dim g''^(k) = {dk}, Summe {S}, dim g''_{p+1} = {d1} -> {flag}; Luecken {[f'{x:.0e}' for x in wk]}",flush=True)
