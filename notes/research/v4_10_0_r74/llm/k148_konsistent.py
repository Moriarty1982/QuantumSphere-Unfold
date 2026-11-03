"""k148: Test H58 (Vorab-Notiz Commit 99675a5). Symbol aus konsistenten Daten am reparierten Keim:
J = A(0) aus k142_lin2, theta neu (K3 gegen K4 wie k144), sigma aus k144; Cartan-Test.
Aufruf: python k148_konsistent.py <state-sufficiency-Ordner> [pmax]"""
import sys,math,numpy as np
from pathlib import Path
here=Path(__file__).parent;D=sys.argv[1];pmax=int(sys.argv[2]) if len(sys.argv)>2 else 8
_argv=sys.argv;sys.argv=[sys.argv[0],D,'none'];__file__=str(here/'k140_fortsetzung_exakt.py')
exec(open(__file__).read().split('p,psi=T.load_germ')[0]);sys.argv=_argv
p,psi=T.load_germ(D,5);d2=np.load(here/'k142_lin2.npz');A2,B2=d2['A'],d2['B'].mean(0);_AB['AB']=(A2,B2)
g={'__file__':str(Path(D)/'balanced_spencer_check.py')}
exec((Path(D)/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{D}')"),g)
idx=g['idx'];g['J']=np.hstack([A2[m,0] for m in range(4)]);g['theta']=np.zeros(480);matrix=g['matrix'];wg=np.load(here/'k136_eichdaten.npy')[1]
Jold=np.load(Path(D)/'completion-omega-witness.npz')['completed_first_symbol'];print('max|J(neu) - J(gespeichert)| =',f"{np.max(abs(g['J']-Jold)):.1e}")
fac=lambda a:math.prod(math.factorial(k) for k in a)
def balanced_kernel(Dfix,N,deg):
    """Projektion von ker F^Dfix_N auf die Koeffizienten vom Grad deg, ausgeglichene Koordinaten, Reihenfolge T.monos."""
    E,rhs,degc=build(psi,p,Dfix,N,wseries(psi,max(N-Dfix-1,0)));cn=np.linalg.norm(E,axis=0);cn[cn==0]=1;E/=cn;E/=np.maximum(np.linalg.norm(E,axis=1),1e-300)[:,None]
    _,s,Vt=np.linalg.svd(E,full_matrices=True);r,a,b=rank_gap(s);Z=(Vt[r:].T)/cn[:,None];sel=degc==deg
    cols=[al for al in T.monos(N) if Dfix<sum(al)<=N and sum(al)==deg];sf=np.repeat([math.sqrt(fac(al)) for al in cols],24)
    K=Z[sel]*sf[:,None];U,sk,_=np.linalg.svd(K,full_matrices=False);rk,ak,bk=rank_gap(sk)
    print(f'  F^{Dfix}_{N}: Rang {r} (Verh. {a/b:.0e}); Projektion auf Grad {deg}: dim {rk} (Verh. {ak/bk:.0e})',flush=True);return U[:,:rk],cols
K3,cols3=balanced_kernel(2,3,3);K4,_=balanced_kernel(2,4,3)
C=K3.T@K4;U,s,_=np.linalg.svd(C,full_matrices=True);print('  dim K3 - dim K4 =',K3.shape[1]-K4.shape[1],'; K4 in K3, Rest',f'{np.linalg.norm(K4-K3@(K3.T@K4)):.1e}')
th=K3@U[:,K4.shape[1]:];look3={a:n for n,a in enumerate(idx(3))}
theta=np.zeros((len(idx(3))*24,th.shape[1]))
for n,al in enumerate(cols3): theta[look3[tuple(sorted(m for m in range(4) for _ in range(al[m])))]*24:][:24]=th[n*24:(n+1)*24]
# sigma (k144) in idx(6)-Reihenfolge
w=np.load(here/'k144_p1'/'w.npy');n5=len([a for a in T.monos(5) if sum(a)==5])*24;c6=[a for a in T.monos(6) if sum(a)==6];look6={a:n for n,a in enumerate(idx(6))}
sig=np.zeros((len(idx(6))*24,4))
for n,a in enumerate(c6): sig[look6[tuple(sorted(m for m in range(4) for _ in range(a[m])))]*24:][:24]=w[n5+n*24:n5+(n+1)*24]
def iota(pp,e):
    ci=idx(pp);ri=idx(pp-1);look={a:n for n,a in enumerate(ci)};M=np.zeros((len(ri)*24,len(ci)*24))
    for rn,b in enumerate(ri):
        for mu in range(4):
            if e[mu]==0: continue
            cn=look[tuple(sorted((*b,mu)))];M[rn*24:(rn+1)*24,cn*24:(cn+1)*24]+=e[mu]*math.sqrt(b.count(mu)+1)*np.eye(24)
    return M
def prolong(cov,q,pp):
    if pp<q: return np.zeros((0,len(idx(pp))*24))
    R=[]
    for gam in idx(pp-q):
        Dm=np.eye(len(idx(pp))*24);k=pp
        for mu in gam: Dm=iota(k,np.eye(4)[mu])@Dm;k-=1
        R.append(cov.T@Dm)
    return np.vstack(R)
gaps=[]
def kernel(pp,with_sigma):
    X=matrix(pp)[1];X=X[np.linalg.norm(X,axis=1)>0];X=X/np.linalg.norm(X,axis=1)[:,None]
    parts=[X,np.kron(np.eye(len(idx(pp))),wg[None,:])]
    for cov,q in ([(theta,3)]+([(sig,6)] if with_sigma else [])):
        R=prolong(cov,q,pp)
        if len(R): parts.append(R/np.linalg.norm(R,axis=1)[:,None])
    _,s,Vt=np.linalg.svd(np.vstack(parts),full_matrices=True);r,a,b=rank_gap(s);gaps.append(a/b)
    print(f"   p={pp} {'mit' if with_sigma else 'ohne'} sigma: dim {Vt.shape[0]-r} (Luecke {a:.1e}|{b:.1e}, Verh. {a/b:.0e})",flush=True);return Vt[r:].T
print('Gueltigkeit: g\'_p ohne sigma (soll 117, 188, 273, 371, 481, 606, 745, 898)')
for pp in range(2,pmax+2): kernel(pp,False)
kern={pp:kernel(pp,True) for pp in range(6,pmax+2)}
for seed in (1,2,3):
    Eb=np.linalg.qr(np.random.default_rng(seed).normal(size=(4,4)))[0].T
    for pp in range(6,pmax+1):
        N=kern[pp];dk=[N.shape[1]];wk=[];rows=np.zeros((0,N.shape[0]))
        for k in range(1,4):
            rows=np.vstack([rows,iota(pp,Eb[k-1])]);r,a,b=rank_gap(np.linalg.svd(rows@N,compute_uv=False));gaps.append(a/b);wk.append(a/b);dk.append(N.shape[1]-r)
        S=sum(dk);d1=kern[pp+1].shape[1];flag='GLEICH (involutiv)' if S==d1 else ('kleiner (nicht involutiv)' if d1<S else 'VERLETZT')
        print(f"seed {seed} p={pp}: dim g''^(k) = {dk}, Summe {S}, dim g''_{pp+1} = {d1} -> {flag}; Luecken {[f'{x:.0e}' for x in wk]}",flush=True)
print(f'kleinstes Lueckenverhaeltnis: {min(gaps):.0e}')
