"""k141 (Erkundung): Spencer-Kohomologie H^{k,2} des theta-geeichten Symbols g' und des ungeeichten Symbols g.
Aufruf: python k141_spencer_geeicht.py <state-sufficiency-Ordner> <k136_eichdaten.npy> [k...]
H^{k,2} = dim ker(delta: g_k x L2 -> S^{k-1} x L3) - rang(delta: g_{k+1} x L1 -> S^k x L2), ausgeglichene Basis."""
import sys,math,itertools,numpy as np
from pathlib import Path
D=Path(sys.argv[1]);wg=np.load(sys.argv[2])[1];ks=[int(k) for k in sys.argv[3:]] or [4,5]
g={'__file__':str(D/'balanced_spencer_check.py')}
exec((D/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{D}')"),g)
matrix,idx=g['matrix'],g['idx']
def rank_gap(s):
    s=s/s[0];m=int(np.sum(s>1e-14));t=np.r_[s[:m],1e-16] if m==len(s) else s[:m+1]
    k=int(np.argmax(np.log(t[:-1]/t[1:])));return k+1,t[k]/t[k+1]
def kernel(p,gauge):
    X=matrix(p)[1];X=X/np.maximum(np.linalg.norm(X,axis=1),1e-300)[:,None]
    if gauge: X=np.vstack([X,np.kron(np.eye(len(idx(p))),wg[None,:])])
    _,s,Vt=np.linalg.svd(X,full_matrices=True);r,q=rank_gap(s);return Vt[r:].T,q
def iota(p,mu):  # d/dx_mu: S^p x R24 -> S^{p-1} x R24, ausgeglichene Basis
    ci=idx(p);ri=idx(p-1);look={a:n for n,a in enumerate(ci)};M=np.zeros((len(ri)*24,len(ci)*24))
    for rn,b in enumerate(ri):
        cn=look[tuple(sorted((*b,mu)))];M[rn*24:(rn+1)*24,cn*24:(cn+1)*24]=math.sqrt(b.count(mu)+1)*np.eye(24)
    return M
def forms(j): return list(itertools.combinations(range(4),j))
def delta(p,j,N):
    """delta auf (Basis N von g_p) x Lambda^j -> S^{p-1} x R24 x Lambda^{j+1}."""
    Fj=forms(j);Fj1=forms(j+1);fi={f:n for n,f in enumerate(Fj1)};I=[iota(p,mu)@N for mu in range(4)]
    h=I[0].shape[0];out=np.zeros((h*len(Fj1),N.shape[1]*len(Fj)))
    for c,f in enumerate(Fj):
        for mu in range(4):
            if mu in f: continue
            new=tuple(sorted((mu,)+f));sign=(-1)**sum(1 for x in f if x<mu);r=fi[new]
            out[r*h:(r+1)*h,c*N.shape[1]:(c+1)*N.shape[1]]+=sign*I[mu]
    return out
for gauge in (False,True):
    for k in ks:
        Nk,q1=kernel(k,gauge);Nk1,q2=kernel(k+1,gauge)
        d2=delta(k,2,Nk);s=np.linalg.svd(d2,compute_uv=False);r2,q3=rank_gap(s);ker2=d2.shape[1]-r2
        d1=delta(k+1,1,Nk1);s=np.linalg.svd(d1,compute_uv=False);r1,q4=rank_gap(s)
        print(f"{'geeicht ' if gauge else 'ungeeicht'} H^({k},2) = {ker2-r1}   (dim g_{k} = {Nk.shape[1]}, dim g_{k+1} = {Nk1.shape[1]}, ker = {ker2}, Bild = {r1}; Luecken {min(q1,q2,q3,q4):.0e})",flush=True)
