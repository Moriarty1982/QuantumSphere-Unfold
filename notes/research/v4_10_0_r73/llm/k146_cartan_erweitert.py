"""k146: Test H56 (Vorab-Notiz Commit 4ed4c3e). Cartan-Test des Symbols g'' = g' geschnitten mit den fortgesetzten vier
Bedingungen sigma_k (k144). Aufruf: python k146_cartan_erweitert.py <state-sufficiency-Ordner> [pmax]"""
import sys,math,numpy as np
from pathlib import Path
here=Path(__file__).parent;D=Path(sys.argv[1]);pmax=int(sys.argv[2]) if len(sys.argv)>2 else 8
sys.path.insert(0,str(here));import k138_tps_d as T
g={'__file__':str(D/'balanced_spencer_check.py')}
exec((D/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{D}')"),g)
matrix,idx=g['matrix'],g['idx'];wg=np.load(here/'k136_eichdaten.npy')[1]
def rank_gap(s):
    if len(s)==0: return 0,np.inf,1.0
    s=s/s[0];m=int(np.sum(s>1e-14));t=np.r_[s[:m],1e-16] if m==len(s) else s[:m+1]
    k=int(np.argmax(np.log(t[:-1]/t[1:])));return k+1,t[k],t[k+1]
def iota(p,e):
    ci=idx(p);ri=idx(p-1);look={a:n for n,a in enumerate(ci)};M=np.zeros((len(ri)*24,len(ci)*24))
    for rn,b in enumerate(ri):
        for mu in range(4):
            if e[mu]==0: continue
            cn=look[tuple(sorted((*b,mu)))];M[rn*24:(rn+1)*24,cn*24:(cn+1)*24]+=e[mu]*math.sqrt(b.count(mu)+1)*np.eye(24)
    return M
unit=lambda mu:np.eye(4)[mu]
# sigma_k in idx(6)-Reihenfolge
w=np.load(here/'k144_p1'/'w.npy');n5=len([a for a in T.monos(5) if sum(a)==5])*24
c6=[a for a in T.monos(6) if sum(a)==6];look6={a:n for n,a in enumerate(idx(6))}
def to_idx(v6):
    out=np.zeros((len(idx(6))*24,)+v6.shape[1:])
    for n,a in enumerate(c6): out[look6[tuple(sorted(m for m in range(4) for _ in range(a[m])))]*24:][:24]=v6[n*24:(n+1)*24]
    return out
sig=to_idx(w[n5:])
def rows_sigma(p):
    if p<6: return np.zeros((0,len(idx(p))*24))
    R=[]
    for gam in idx(p-6):
        Dm=np.eye(len(idx(p))*24);q=p
        for mu in gam: Dm=iota(q,unit(mu))@Dm;q-=1
        R.append(sig.T@Dm)
    return np.vstack(R)
gaps=[]
def kernel(p,ext=True):
    X=matrix(p)[1];X=X/np.maximum(np.linalg.norm(X,axis=1),1e-300)[:,None];X=np.vstack([X,np.kron(np.eye(len(idx(p))),wg[None,:])])
    if ext and p>=6: Rs=rows_sigma(p);Rs=Rs/np.linalg.norm(Rs,axis=1)[:,None];X=np.vstack([X,Rs])
    _,s,Vt=np.linalg.svd(X,full_matrices=True);r,a,b=rank_gap(s);gaps.append(a/b);print(f'   Rang Symbol p={p}: Luecke {a:.1e}|{b:.1e} (Verh. {a/b:.0e})',flush=True);return Vt[r:].T
# Gueltigkeit: G6 (echter Keim) gegen g'_6 (gespeichertes Symbol)
G6=np.load(here/'k144_p1'/'G6.npy');G=np.linalg.qr(to_idx(G6[n5:]))[0];K6=kernel(6,ext=False)
sn=np.linalg.svd(G-K6@(K6.T@G),compute_uv=False);print(f"Hauptwinkel G6 (echt) gegen g'_6 (gespeichert): max sin = {sn.max():.1e}  (dim {G.shape[1]} / {K6.shape[1]})",flush=True)
kern={};
for p in range(6,pmax+2): kern[p]=kernel(p);print(f"dim g''_{p} = {kern[p].shape[1]}   (dim g'_{p} = {[481,606,745,898,1065][p-6]})",flush=True)
for seed in (1,2,3):
    Eb=np.linalg.qr(np.random.default_rng(seed).normal(size=(4,4)))[0].T
    for p in range(6,pmax+1):
        N=kern[p];dk=[N.shape[1]];wk=[];rows=np.zeros((0,N.shape[0]))
        for k in range(1,4):
            rows=np.vstack([rows,iota(p,Eb[k-1])]);r,a,b=rank_gap(np.linalg.svd(rows@N,compute_uv=False));gaps.append(a/b);dk.append(N.shape[1]-r);wk.append(a/b)
        S=sum(dk);d1=kern[p+1].shape[1];flag='GLEICH (involutiv)' if S==d1 else ('kleiner (nicht involutiv)' if d1<S else 'VERLETZT')
        print(f"seed {seed} p={p}: dim g''^(k) = {dk}, Summe {S}, dim g''_{p+1} = {d1} -> {flag}; Luecken {[f'{x:.0e}' for x in wk]}",flush=True)
print(f'kleinstes Lueckenverhaeltnis: {min(gaps):.0e}')
