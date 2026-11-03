"""k152: Symbolraeume aus ebenen Wellen xi^p (x) u auf dem Lichtkegel (konsistente Daten wie k148).
Aufruf: python k152_wellen.py <Ordner> <modus: pruef | sigma> [pmin pmax] [anzahl_richtungen]
pruef: ohne sigma, Vergleich mit g'_p; sigma: mit den vier Bedingungen."""
import sys,math,numpy as np
from pathlib import Path
here=Path(__file__).parent;mode=sys.argv[2];pmin,pmax=(int(sys.argv[3]),int(sys.argv[4])) if len(sys.argv)>4 else (2,8)
nd=int(sys.argv[5]) if len(sys.argv)>5 else 400;sys.argv=sys.argv[:2]+['6']
src=open(here/'k148_konsistent.py').read().split("print('Gueltigkeit")[0];exec(src)
Jm=g['J'];fac=lambda a:math.prod(math.factorial(k) for k in a)
# Koframe am Keim fuer den Lichtkegel q
bg0=T.Background(p,0);I5=T.index(5);ps=psi[0];jj=[psi[I5[tuple(1 if k==m else 0 for k in range(4))]] for m in range(4)]
cov=[jj[m]+1j*bg0.conn[m][0]@ps for m in range(4)];Ef=np.array([[np.real(ps.conj()@T.Qm[a]@cov[m]) for m in range(4)] for a in range(4)]);V=np.linalg.inv(Ef)
eta=np.diag([1,-1,-1,-1.]);q=lambda x:(V.T@x)@eta@(V.T@x)
def wavevec(x,pp):  # Faktoren x^alpha/sqrt(alpha!) in idx(pp)-Reihenfolge
    return np.array([math.prod(x[m] for m in a)/math.sqrt(fac(tuple(a.count(k) for k in range(4)))) for a in idx(pp)])
def cond_rows(x):
    Jx=sum(x[m]*Jm[:,m*24:(m+1)*24] for m in range(4))
    th_x=np.einsum('a,aik->ik',wavevec(x,3),theta.reshape(-1,24,theta.shape[1])).T          # theta(xi) (1 x 24)
    rows=[Jx,th_x,wg[None,:]]
    if mode=='sigma': rows.append(np.einsum('a,aik->ik',wavevec(x,6),sig.reshape(-1,24,4)).T)   # sigma_k(xi) (4 x 24)
    return np.vstack([r/np.maximum(np.linalg.norm(r,axis=1),1e-300)[:,None] for r in rows])
rng=np.random.default_rng(7);dirs=[]
while len(dirs)<nd:
    sp=rng.normal(size=3);f=lambda t:q(np.r_[t,sp]);a=(f(1)+f(-1)-2*f(0))/2;b=(f(1)-f(-1))/2;c=f(0)
    for t in np.roots([a,b,c]):
        if abs(t.imag)<1e-12: x=np.r_[t.real,sp];dirs.append(x/np.linalg.norm(x))
kerns=[];kd=[]
for x in dirs:
    _,s,Vt=np.linalg.svd(cond_rows(x));s=s/s[0];k=int(np.sum(s<1e-9));kd.append(k);kerns.append(Vt[-k:] if k else np.zeros((0,24)))
print(f'{mode}: {len(dirs)} Nullrichtungen; Kerndimension je Richtung: {sorted(set(kd))} (Haeufigkeit {[kd.count(v) for v in sorted(set(kd))]})',flush=True)
for pp in range(pmin,pmax+1):
    W=np.vstack([np.kron(wavevec(x,pp),Uk) for x,Uk in zip(dirs,kerns) if len(Uk)])   # Wellen als Zeilen
    W/=np.linalg.norm(W,axis=1)[:,None];s=np.linalg.svd(W,compute_uv=False);r,a,b=rank_gap(s);t=s/s[0]
    print(f'   p={pp}: Spann der Wellen dim {r} (aus {W.shape[0]} Wellen; Luecke {a:.1e}|{b:.1e}, Verh. {a/b:.0e}); Werte um den Rang {np.array2string(t[r-3:r+2],precision=2)}',flush=True)
