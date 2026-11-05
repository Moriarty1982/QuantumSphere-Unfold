"""k157: die vier Bedingungen hochgenau. Fester Jet bis Grad 5, Faser der 6-Jets mit den Gleichungen bis Grad 7.
Elimination c8, dann c7 (Linkskerne: float-SVD, Newton in arb, 60 Stellen). Auf dem Kern N6 von [R5; G6] werden die
abgeleiteten Bedingungen in fortgesetztes Omega (theta aus k155) und den Rest (sigma) getrennt.
Aufruf: python k157_hp_bedingungen.py <Ordner>"""
import sys,time,math,pickle,numpy as np,flint
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent));from k154_hp_tools import *
t0=time.time();D=sys.argv[1];mons,A,B=load();w=gauge_series(D)
log=lambda *a:print(f'[{time.time()-t0:5.0f} s]',*a,flush=True)
def blk(kind,k,m): return Rblock(A,B,k,m) if kind=='R' else Gblock(w,k,m)
def vstack_arb(mats):
    n=mats[0].ncols();T=arb_mat(sum(M.nrows() for M in mats),n);r0=0
    for M in mats:
        for i in range(M.nrows()):
            for j in range(n): T[r0+i,j]=M[i,j]
        r0+=M.nrows()
    return T
def leftnull(Tblocks):
    """Linkskern von vstack(Tblocks): float-SVD, Newton mit Residuum X^T T in arb."""
    Tf=np.vstack([tofloat(M) for M in Tblocks]);rs=np.linalg.norm(Tf,axis=1);rs[rs==0]=1;Tf=Tf/rs[:,None]   # Zeilen auf Norm 1
    U,s,Vt=np.linalg.svd(Tf.T,full_matrices=True);t=s/s[0]
    m=int(np.sum(t>1e-15));tt=np.r_[t[:m],1e-17] if m==len(t) else t[:m+1];r=int(np.argmax(np.log(tt[:-1]/tt[1:])))+1
    X=Vt[r:].T/rs[:,None];Ur,Sr,Vr=U[:,:r],s[:r],Vt[:r].T;Xa=arb_mat(X.tolist());offs=np.cumsum([0]+[M.nrows() for M in Tblocks])
    hist=[]
    for it in range(8):
        Res=None
        for M,a,b in zip(Tblocks,offs[:-1],offs[1:]):
            Xs=arb_mat([[Xa[i,j] for j in range(Xa.ncols())] for i in range(a,b)]);P=Xs.transpose()*M;Res=P if Res is None else Res+P
        rf=tofloat(Res).T;nr=np.max(abs(rf))/s[0];hist.append(nr)
        if nr<1e-62: break
        Xa=Xa-arb_mat(((Vr@((Ur.T@rf)/Sr[:,None]))/rs[:,None]).tolist())
    return Xa,r,(t[r-1],t[r] if r<len(t) else 0),hist,offs
def apply_left(L,offs,blocks):
    """L^T vstack(blocks) blockweise."""
    out=None
    for M,a,b in zip(blocks,offs[:-1],offs[1:]):
        Ls=arb_mat([[L[i,j] for j in range(L.ncols())] for i in range(a,b)]);P=Ls.transpose()*M;out=P if out is None else out+P
    return out
# --- Stufe 1: c8
R7_8,G8_8=blk('R',7,8),blk('G',8,8);log('Bloecke c8 gebaut',R7_8.nrows(),R7_8.ncols())
L8,r8,g8,h8,o8=leftnull([R7_8,G8_8]);log(f'c8: Rang {r8} (Luecke {g8[0]:.1e}|{g8[1]:.1e}), Linkskern {L8.ncols()}, Residuen {[f"{x:.0e}" for x in h8]}')
del R7_8,G8_8
D7_7=apply_left(L8,o8,[blk('R',7,7),blk('G',8,7)]);D7_6=apply_left(L8,o8,[blk('R',7,6),blk('G',8,6)]);log('abgeleitete Zeilen D7',D7_7.nrows())
pickle.dump([[[M[i,j].mid().str(65,radius=False) for j in range(M.ncols())] for i in range(M.nrows())] for M in (D7_7,D7_6)],open(W/'k157_D7.pkl','wb'));log('D7 gespeichert')
# --- Stufe 2: c7
L7,r7,g7,h7,o7=leftnull([blk('R',6,7),blk('G',7,7),D7_7]);log(f'c7: Rang {r7} (Luecke {g7[0]:.1e}|{g7[1]:.1e}), Linkskern {L7.ncols()}, Residuen {[f"{x:.0e}" for x in h7]}')
D6=apply_left(L7,o7,[blk('R',6,6),blk('G',7,6),D7_6]);log('abgeleitete Zeilen D6',D6.nrows())
# --- Stufe 3: Faser c6
R5_6,G6_6=blk('R',5,6),blk('G',6,6);Tf=np.vstack([tofloat(R5_6),tofloat(G6_6)]);U,s,Vt=np.linalg.svd(Tf,full_matrices=True);t=s/s[0]
m=int(np.sum(t>1e-15));tt=np.r_[t[:m],1e-17] if m==len(t) else t[:m+1];r=int(np.argmax(np.log(tt[:-1]/tt[1:])))+1
N=Vt[r:].T;Ur,Sr,Vr=U[:,:r],s[:r],Vt[:r].T;Na=arb_mat(N.tolist());T6=vstack_arb([R5_6,G6_6])
for it in range(6):
    rf=tofloat(T6*Na);nr=np.max(abs(rf))/s[0]
    if nr<1e-62: break
    Na=Na-arb_mat((Vr@((Ur.T@rf)/Sr[:,None])).tolist())
log(f'Kern von [R5; G6]: dim {Na.ncols()} (Residuum {nr:.0e})')
C=D6*Na;cn_=np.linalg.norm(tofloat(D6),axis=1);cn_[cn_==0]=1;C=arb_mat([[C[i,j]/cn_[i] for j in range(C.ncols())] for i in range(C.nrows())]);Gm=C.transpose()*C;ev=np.array([abs(float(v.real.mid())) for v in flint.acb_mat(Gm).eig(algorithm='approx')]);ev=np.sort(ev)[::-1];ev=ev/ev[0]
log('Gram der abgeleiteten Bedingungen auf dem Kern, groesste 30 (relativ):');print(np.array2string(ev[:30],precision=1),flush=True)
pickle.dump({'N6':[[N[i,j] for j in range(N.shape[1])] for i in range(N.shape[0])]},open(W/'k157_N6_float.pkl','wb'))
# Zwischenstand sichern (Strings, 60 Stellen)
def dump(M,f): pickle.dump([[M[i,j].mid().str(60,radius=False) for j in range(M.ncols())] for i in range(M.nrows())],open(W/f,'wb'))
dump(C,'k157_C.pkl');dump(Na,'k157_N6.pkl');log('gespeichert')
