"""k119: Erzeugen die vier Quadriken d_k das Ideal zweier windschiefer Geraden? Wo liegen sie relativ zum Kegel q?"""
import sys,numpy as np,itertools,sympy as sp
from pathlib import Path
SRC=Path(sys.argv[1])
src=(SRC/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{SRC}')")
g={'__file__':'x'};exec(src,g);idx=g['idx']
d=np.load('kofaktoren.npy');Q=np.load('quadrik.npy');g2=idx(2)
def mat(c):
    M=np.zeros((4,4))
    for i,a in enumerate(g2):
        M[a[0],a[1]]+=c[i]/(1 if a[0]==a[1] else 2)
        if a[0]!=a[1]: M[a[1],a[0]]+=c[i]/2
    return M
Ms=[mat(c) for c in d]
# Hilbert-Funktion des Ideals I=(d_k): dim I_3, I_4
def deg_span(k):
    rows=[]
    for m in idx(k-2):
        for c in d:
            v={}
            for i,a in enumerate(g2):
                key=tuple(sorted(a+m));v[key]=v.get(key,0)+c[i]
            rows.append([v.get(b,0) for b in idx(k)])
    s=np.linalg.svd(np.array(rows),compute_uv=False);return int(sum(s>s[0]*1e-9)),s
for k in (3,4,5):
    r,s=deg_span(k);print(f'dim I_{k} =',r,' (zwei windschiefe Geraden: ',{3:12,4:25,5:42}[k],')  Grenze',f'{s[r-1]:.1e}|{s[r] if r<len(s) else 0:.1e}')
# Punkte von V(I): Schnitt mit zufaelliger Ebene span(a,b,c); loese d1=d2=0, pruefe d3,d4
rng=np.random.default_rng(2)
def points_on_slice():
    a,b,c=(rng.normal(size=4)+1j*rng.normal(size=4) for _ in range(3))
    x,y=sp.symbols('x y')
    def poly(M):
        v=[x*a[i]+y*b[i]+c[i] for i in range(4)]
        return sp.expand(sum(complex(M[i,j])*v[i]*v[j] for i in range(4) for j in range(4)))
    P=[poly(M) for M in Ms];res=sp.Poly(sp.resultant(P[0],P[1],y),x)
    out=[]
    for xr in np.roots([complex(cf) for cf in res.all_coeffs()]):
        ys=np.roots([complex(cf) for cf in sp.Poly(P[0].subs(x,xr),y).all_coeffs()])
        for yr in ys:
            v=xr*a+yr*b+c;v=v/np.linalg.norm(v)
            if max(abs(v@M@v) for M in Ms)<1e-8: out.append(v)
    return out
pts=[]
for _ in range(4):
    pp=points_on_slice();pts+=pp
print('gemeinsame Nullstellen gefunden:',len(pts))
# Gruppiere in Ebenen: zwei Punkte gehoeren zur selben Ebene, wenn alle d auf ihrer Verbindung verschwinden
def same(u,v): return max(abs((u+0.37*v)@M@(u+0.37*v)) for M in Ms)<1e-7
groups=[]
for v in pts:
    for gr in groups:
        if same(gr[0],v): gr.append(v);break
    else: groups.append([v])
print('Ebenen:',len(groups),[len(gr) for gr in groups])
for k,gr in enumerate(groups):
    B=np.array(gr).T;u,s,vh=np.linalg.svd(B);P=u[:,:2]
    print(f' Ebene {k}: Dimension (Singulaerwerte)',np.array2string(s[:3],precision=2))
    # liegt die Ebene im Kegel q? q(P z)=0 fuer alle z <=> P^T Q P = 0
    print('   |P^T Q P|/|Q| =',f'{np.linalg.norm(P.T@Q@P)/np.linalg.norm(Q):.1e}','  reell?',f'{np.linalg.norm(P.imag) if np.linalg.matrix_rank(np.hstack([P,P.conj()]),1e-8)>2 else 0:.2f}', ' Rang[P, conj P] =',np.linalg.matrix_rank(np.hstack([P,P.conj()]),1e-8))
if len(groups)==2:
    P0=np.linalg.svd(np.array(groups[0]).T)[0][:,:2];P1=np.linalg.svd(np.array(groups[1]).T)[0][:,:2]
    print(' Ebene 1 = konj(Ebene 0)?  Rang[P0, conj P1] =',np.linalg.matrix_rank(np.hstack([P0,P1.conj()]),1e-8))
    print(' windschief? Rang[P0,P1] =',np.linalg.matrix_rank(np.hstack([P0,P1]),1e-8))
