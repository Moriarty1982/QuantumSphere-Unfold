"""k137: Cartan-Test des theta-geeichten, Omega-erweiterten OP5-Symbols (Test H51, Vorab-Notiz Commit 10693a0).
Aufruf: python k137_cartan_test.py <state-sufficiency-Ordner> [pmin] [pmax]
Ausgeglichene Basis (Spalten mit sqrt(alpha!)): Kontraktion iota(e) hat dann Eintraege e_mu*sqrt(beta_mu+1)."""
import sys,math,numpy as np
from pathlib import Path
D=Path(sys.argv[1]);pmin=int(sys.argv[2]) if len(sys.argv)>2 else 4;pmax=int(sys.argv[3]) if len(sys.argv)>3 else 7
g={'__file__':str(D/'balanced_spencer_check.py')}
exec((D/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{D}')"),g)
matrix,idx=g['matrix'],g['idx']
wg=np.load(Path(__file__).with_name('k136_eichdaten.npy'))[1]
def rankgap(X):
    s=np.linalg.svd(X,compute_uv=False)
    if len(s)==0 or s[0]==0: return 0,np.inf,1.0
    s=s/s[0];m=int(np.sum(s>1e-14));t=np.r_[s[:m],1e-16] if m==len(s) else s[:m+1]
    k=int(np.argmax(np.log(t[:-1]/np.maximum(t[1:],1e-300))));return k+1,t[k],t[k+1]
def system(p):
    B=matrix(p)[1];B=B/np.maximum(np.linalg.norm(B,axis=1),1e-300)[:,None]
    return np.vstack([B,np.kron(np.eye(len(idx(p))),wg[None,:])])
def kernel(p):
    X=system(p);U,s,Vt=np.linalg.svd(X,full_matrices=True);s=s/s[0]
    r,a,b=rankgap(X);return Vt[r:].T,a,b
def iota(p,e):  # S^p x R24 -> S^{p-1} x R24, ausgeglichene Basis
    ci=idx(p);ri=idx(p-1);look={a:n for n,a in enumerate(ci)};M=np.zeros((len(ri)*24,len(ci)*24))
    for rn,beta in enumerate(ri):
        for mu in range(4):
            if e[mu]==0: continue
            cn=look[tuple(sorted((*beta,mu)))];M[rn*24:(rn+1)*24,cn*24:(cn+1)*24]+=e[mu]*math.sqrt(beta.count(mu)+1)*np.eye(24)
    return M
dimg={};kern={}
for p in range(pmin,pmax+2):
    N,a,b=kernel(p);kern[p]=N;dimg[p]=N.shape[1];print(f"dim g'_{p} = {dimg[p]}  (Luecke {a:.1e}|{b:.1e}, Verhaeltnis {a/b:.0e})",flush=True)
for seed in (1,2,3):
    E=np.linalg.qr(np.random.default_rng(seed).normal(size=(4,4)))[0].T
    for p in range(pmin,pmax+1):
        N=kern[p];dk=[dimg[p]];worst=np.inf;rows=np.zeros((0,N.shape[0]))
        for k in range(1,4):
            rows=np.vstack([rows,iota(p,E[k-1])]);X=rows@N
            r,a,b=rankgap(X);dk.append(N.shape[1]-r);worst=min(worst,a/b)
        S=sum(dk);flag='GLEICH (involutiv)' if S==dimg[p+1] else ('kleiner (nicht involutiv)' if dimg[p+1]<S else 'VERLETZT')
        print(f"seed {seed} p={p}: dim g'^(k) k=0..3 = {dk}, Summe {S}, dim g'_{p+1} = {dimg[p+1]} -> {flag}; min. Lueckenverhaeltnis {worst:.0e}",flush=True)
