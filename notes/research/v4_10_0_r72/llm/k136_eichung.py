"""k136: theta-Eichung des OP5-Vergleichsmodells (Erkundung).
Aufruf: python k136_eichung.py <analysis/op5-field-slices/state-sufficiency-2026-10-30>
1) Eichrichtung v = gemeinsamer Nullvektor aller J-Bloecke (delta Psi = f v), Abgleich mit Omega.
2) Natuerliche Eichfunktionen s_M = Psi^+ M Psi: Transversalitaet ds.v.
3) Geeichtes Symbol g'_p (Zeilen w x alle Monome vom Grad p): dim g'_p gegen g_p - C(p+3,3)."""
import sys,json,math,itertools,numpy as np
from pathlib import Path
D=Path(sys.argv[1]);pmax=int(sys.argv[2]) if len(sys.argv)>2 else 7
w=np.load(D/'completion-omega-witness.npz');J=w['completed_first_symbol'];theta=w['theta_normalized']
f70=json.loads((D/'precision-first-jet-70.json').read_text())
psi=np.array([complex(float(a),float(b)) for a,b in f70['psi']])
# 1) Eichrichtung
S=np.vstack([J[:,m*24:(m+1)*24] for m in range(4)]);sv=np.linalg.svd(S);v=sv[2][-1]
print('J-Bloecke gestapelt: kleinste Singulaerwerte',np.array2string(sv[1][-3:],precision=2))
print('theta-Bloecke auf v: max',f"{max(abs(theta[b*24:(b+1)*24]@v) for b in range(20)):.1e}",' (|theta| ~',f'{np.max(abs(theta)):.1e})')
vc=v[:12]+1j*v[12:]
# 2) Eichfunktionen
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]);Z2=np.zeros((2,2))
al=[np.block([[Z2,q],[q,Z2]]) for q in (sx,sy,sz)];beta=np.diag([1,1,-1,-1.])
S3=np.array([[0,.5,0],[.5,0,0],[0,0,0]]);Z3=np.diag([1,-1,0.])
K=[np.kron(np.eye(3),m) for m in [np.eye(4)]+al];Q=[np.kron(S3,m) for m in [np.eye(4)]+al]
cands={'Psi^+Psi':np.eye(12),'Psi^+(Z x beta)Psi [g]':np.kron(Z3,beta),'Psi^+(I x beta)Psi':np.kron(np.eye(3),beta)}
for a in range(4): cands[f'j^{a} = Psi^+K_{a}Psi (Strom)']=K[a]
for a in range(4): cands[f'Psi^+Q_{a}Psi']=Q[a]
best=None
for n,M in cands.items():
    gM=M@psi; wv=np.r_[(2*gM).real,(2*gM).imag]  # d(Re Psi^+ M Psi) als reeller 24-Kovektor (fuer hermitesches M)
    r=abs(wv@v)/max(np.linalg.norm(wv),1e-300)
    print(f'  {n:34s} |ds.v|/|ds| = {r:.3e}')
    if 'g]' not in n and (best is None or r>best[0]): best=(r,n,wv)
print('gewaehlt:',best[1])
np.save(Path(sys.argv[0]).with_name('k136_eichdaten.npy'),np.vstack([v,best[2]/np.linalg.norm(best[2])]))
# 3) geeichtes Symbol
g={'__file__':str(D/'balanced_spencer_check.py')}
exec((D/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{D}')"),g)
matrix,idx=g['matrix'],g['idx']
wg=best[2]/np.linalg.norm(best[2])
def dims(A):
    X=A/np.maximum(np.linalg.norm(A,axis=1),1e-300)[:,None];s=np.linalg.svd(X,compute_uv=False)
    s=s/s[0];m=int(np.sum(s>1e-14))  # nur Werte oberhalb des Maschinen-Nullniveaus
    s=np.r_[s[:m],1e-16] if m==len(s) else s[:m+1]
    k=int(np.argmax(np.log(s[:-1]/np.maximum(s[1:],1e-300))));return A.shape[1]-(k+1),s[k],s[k+1]
for p in range(2,pmax+1):
    A=matrix(p)[1];nc=len(idx(p));Wr=np.kron(np.eye(nc),wg[None,:])
    d0,a0,b0=dims(A);d1,a1,b1=dims(np.vstack([A,Wr]))
    print(f'p={p}: g_p={d0} (Luecke {a0:.1e}|{b0:.1e})  g\'_p={d1} (Luecke {a1:.1e}|{b1:.1e})  g_p-C(p+3,3)={d0-math.comb(p+3,3)}',flush=True)
