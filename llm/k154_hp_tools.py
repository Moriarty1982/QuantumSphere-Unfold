"""k154: Werkzeuge fuer die hochgenaue Rechnung (python-flint, 60 Stellen) auf Basis der Linearisierung aus k153.
Blockaufbau der Fortsetzungssysteme aus den 32x24-Koeffizientenmatrizen von A, B (Taylor bis Grad 2) und der Eichreihe."""
import math,pickle,itertools,numpy as np,flint,mpmath as _mp
_mp.mp.dps=160   # wichtig: sonst schreibt str(mpf) nur 15 Stellen (Fehler bis 3.11.2026, 18 Uhr)
from pathlib import Path
import os
flint.ctx.dps=int(os.environ.get('QS_DPS','60'))
here=Path(__file__).parent;W=here/os.environ.get('QS_HPWORK','hp_work')
arb,arb_mat=flint.arb,flint.arb_mat
def mon(d): return [a for a in sorted({tuple(c.count(m) for m in range(4)) for c in itertools.combinations_with_replacement(range(4),d)},reverse=True)]
fac=lambda a:math.prod(math.factorial(k) for k in a)
def to_arb_mat(M): return arb_mat([[arb(_mp.nstr(v,120) if isinstance(v,(_mp.mpf,_mp.mpc)) else str(v)) for v in row] for row in M])
def load():
    mons,Ac,Bc=pickle.load(open(W/'AB_taylor2.pkl','rb'));Ix={a:i for i,a in enumerate(mons)}
    A={(mu,a):to_arb_mat(Ac[mu,Ix[a]]) for mu in range(4) for a in mons};B={a:to_arb_mat(Bc[Ix[a]]) for a in mons}
    return mons,A,B
def gauge_series(D,dmax=2):
    """w_gamma (1 x 24, arb) aus dem 70-stelligen Keim: d(Re Psi^+ K2 Psi) = 2 (Re K2Psi, Im K2Psi)."""
    import json
    rd=lambda f:json.loads((Path(D)/f).read_text())
    f70=rd('precision-first-jet-70.json');root=rd('precision-completed-root-result.json');sec=rd('precision-second-jet-result.json')
    co={(0,0,0,0):[(a,b) for a,b in f70['psi']]}
    for dg,packed in [(1,root['first_derivatives_real_packed']),(2,sec['second_coefficients_real_packed'])]:
        for i,cc in enumerate(itertools.combinations_with_replacement(range(4),dg)):
            co[tuple(cc.count(m) for m in range(4))]=[(packed[i*24+k],packed[i*24+12+k]) for k in range(12)]
    # K2 = I3 (x) alpha_y, alpha_y = [[0, sy],[sy, 0]], sy = [[0,-i],[i,0]]
    def K2psi(v):
        re=[arb(a) for a,b in v];im=[arb(b) for a,b in v];ore=[arb(0)]*12;oim=[arb(0)]*12
        for blk in range(3):
            o=4*blk  # alpha_y auf (p0,p1,p2,p3): (sy p2, sy p3 ; sy p0, sy p1) mit sy(u,v) = (-i v, i u)
            for (dst,src) in ((0,2),(2,0)):
                u_r,u_i=re[o+src],im[o+src];v_r,v_i=re[o+src+1],im[o+src+1]
                ore[o+dst],oim[o+dst]=v_i,-v_r          # -i v
                ore[o+dst+1],oim[o+dst+1]=-u_i,u_r      #  i u
        return ore,oim
    w={}
    for a,v in co.items():
        if sum(a)>dmax: continue
        r,i=K2psi(v);w[a]=arb_mat([[2*x for x in r]+[2*x for x in i]])
    return w
def Rblock(A,B,k,m,dmax=2):
    """Block der R-Zeilen vom Grad k auf die Spalten c_m (ausgeglichen: c = b/sqrt(alpha!)) als arb_mat, oder None."""
    if m>k+1 or k+1-m>dmax: return None
    rows,cols=mon(k),mon(m);M=arb_mat(32*len(rows),24*len(cols))
    for r,bt in enumerate(rows):
        for c,al in enumerate(cols):
            d=[x-y for x,y in zip(bt,al)];blk=None
            if all(v>=0 for v in d) and sum(d)<=dmax: blk=B[tuple(d)]
            for mu in range(4):
                if al[mu]==0: continue
                g=list(d);g[mu]+=1
                if all(v>=0 for v in g) and sum(g)<=dmax:
                    t=A[(mu,tuple(g))]*al[mu];blk=t if blk is None else blk+t
            if blk is None: continue
            sc=1/arb(fac(al)).sqrt()
            for i in range(32):
                for j in range(24): M[32*r+i,24*c+j]=blk[i,j]*sc
    return M
def Gblock(w,k,m,dmax=2):
    if m>k or k-m>dmax: return None
    rows,cols=mon(k),mon(m);M=arb_mat(len(rows),24*len(cols))
    for r,bt in enumerate(rows):
        for c,al in enumerate(cols):
            d=tuple(x-y for x,y in zip(bt,al))
            if all(v>=0 for v in d) and sum(d)<=dmax:
                sc=1/arb(fac(al)).sqrt()
                for j in range(24): M[r,24*c+j]=w[d][0,j]*sc
    return M
def tofloat(M): return np.array([[float(x.mid()) for x in row] for row in M.tolist()])
def stack(blocks):
    """blocks: Liste von Zeilen, jede Zeile Liste von arb_mat oder (nrows, ncols)-Tupel fuer Nullbloecke."""
    rows=[];
    for rb in blocks:
        h=next(b.nrows() for b in rb if isinstance(b,arb_mat))
        mats=[b if isinstance(b,arb_mat) else arb_mat(h,b) for b in rb];R=arb_mat(h,sum(m.ncols() for m in mats))
        c0=0
        for mm in mats:
            for i in range(h):
                for j in range(mm.ncols()): R[i,c0+j]=mm[i,j]
            c0+=mm.ncols()
        rows.append(R)
    n=rows[0].ncols();T=arb_mat(sum(r.nrows() for r in rows),n);r0=0
    for R in rows:
        for i in range(R.nrows()):
            for j in range(n): T[r0+i,j]=R[i,j]
        r0+=R.nrows()
    return T
def null_refine(T,side="right",iters=10,tol=1e-45):
    """Kern (rechts: T x = 0; links: y^T T = 0) hochgenau: Start aus float-SVD, Newton-Korrektur mit float-Pseudoinverse,
    Residuen in arb. Rueckgabe: (Basis als arb_mat, float-Singulaerwerte, Rang, Residuenverlauf)."""
    Tf=tofloat(T);M=Tf if side=='right' else Tf.T;U,s,Vt=np.linalg.svd(M,full_matrices=True);t=s/s[0]
    m=int(np.sum(t>1e-15));tt=np.r_[t[:m],1e-17] if m==len(t) else t[:m+1];r=int(np.argmax(np.log(tt[:-1]/tt[1:])))+1
    X=Vt[r:].T;Ur,Sr,Vr=U[:,:r],s[:r],Vt[:r].T   # M = U S V^T; Kern von M: V[:, r:]
    Mh=T if side=='right' else T.transpose();Xh=arb_mat(X.tolist());hist=[];split=None
    for it in range(iters):
        Res=Mh*Xh;rf=tofloat(Res);nr=np.max(abs(rf));hist.append(nr)
        if nr<tol: break
        if it==6 and split is None:
            # Fast-Kern trennen: hochgenaue Gram-Matrix der Residuen, Eigenwerte; echte Kernrichtungen haben ~0
            Gm=Res.transpose()*Res;vals,vecs=flint.acb_mat(Gm).eig(algorithm='approx',right=True)
            ev=np.array([abs(float(v.real.mid())) for v in vals]);o=np.argsort(ev);evs=ev[o]
            le=np.log10(np.maximum(evs,1e-200));gaps=le[1:]-le[:-1];j=int(np.argmax(gaps)) if len(gaps) else -1
            keep=list(o[:j+1]) if (j>=0 and gaps[j]>10) else list(o)   # nur bei Luecke > 10 Dekaden trennen
            print(f'      Gram-Trennung: {len(o)-len(keep)} Richtungen mit Eigenwert >= {10**le[j+1] if j>=0 and gaps[j]>10 else 0:.1e} entfernt (Luecke {10**gaps[j] if j>=0 else 0:.0e})',flush=True)
            split=(len(o)-len(keep),evs)
            if len(keep)<len(o):
                Vk=arb_mat([[vecs[i,k].real for k in keep] for i in range(vecs.nrows())]);Xh=Xh*Vk;continue
        dX=Vr@((Ur.T@rf)/Sr[:,None]);Xh=Xh-arb_mat(dX.tolist())
    return Xh,s,r,hist
