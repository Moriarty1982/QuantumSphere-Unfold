"""k117: gemeinsamer quadratischer Faktor q der vier Quartiken; Signatur; Bezug zum Symbol J(xi); Kofaktoren d_k."""
import sys,math,itertools,numpy as np
from pathlib import Path
SRC=Path(sys.argv[1])
src=(SRC/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{SRC}')")
g={'__file__':'x'};exec(src,g);idx,J=g['idx'],g['J']
coef=np.load('quartiken.npy');g4=idx(4);g2=idx(2)
mono=lambda a,xi: np.prod([xi[m]**a.count(m) for m in range(4)])
ev=lambda c,xi,base: sum(c[i]*mono(a,xi) for i,a in enumerate(base))
rng=np.random.default_rng(11);pts=[]
while len(pts)<40:
    a,b=rng.normal(size=4),rng.normal(size=4);ts=np.linspace(-2,2,5)
    P=[np.polyfit(ts,[ev(c,a+t*b,g4) for t in ts],4) for c in coef]
    for t in np.roots(P[0]):
        if abs(t.imag)>1e-9: continue
        xi=(a+t.real*b);xi/=np.linalg.norm(xi)
        if max(abs(ev(c,xi,g4)) for c in coef)<1e-12: pts.append(xi)
M=np.array([[mono(a,x) for a in g2] for x in pts]);_,sv,Vt=np.linalg.svd(M);q=Vt[-1]
print('Quadrik-Fit, letzte Singulaerwerte:',np.array2string(sv[-3:],precision=2))
Q=np.zeros((4,4))
for i,a in enumerate(g2):
    if a[0]==a[1]: Q[a[0],a[0]]=q[i]
    else: Q[a[0],a[1]]=Q[a[1],a[0]]=q[i]/2
ew=np.linalg.eigvalsh(Q);print('Eigenwerte der Quadrik:',np.array2string(ew/abs(ew).max(),precision=4),'-> Signatur',(int(sum(ew>0)),int(sum(ew<0))))
# Symbol J(xi): Rang generisch vs auf q=0
Jx=lambda xi: sum(xi[m]*J[:,m*24:(m+1)*24] for m in range(4))
gen=[np.linalg.svd(Jx(rng.normal(size=4)),compute_uv=False) for _ in range(3)]
print('J(xi) generisch, kleinste Singulaerwerte:',[np.array2string(s[-6:],precision=1) for s in gen[:1]])
print('J(xi) auf q=0,  kleinste Singulaerwerte:',[np.array2string(np.linalg.svd(Jx(x),compute_uv=False)[-6:],precision=1) for x in pts[:2]])
# Kofaktoren d_k: c_k = q * d_k
mult=np.zeros((len(g4),len(g2)))
for j,b in enumerate(g2):
    for i,a in enumerate(g2):
        mult[g4.index(tuple(sorted(a+b))),j]+=q[i]
D=[np.linalg.lstsq(mult,c,rcond=None) for c in coef]
print('Divisionsrest |c - q d|/|c|:',[f'{np.linalg.norm(mult@d[0]-c)/np.linalg.norm(c):.1e}' for d,c in zip(D,coef)])
d=np.array([x[0] for x in D]);np.save('kofaktoren.npy',d);np.save('quadrik.npy',Q)
# gemeinsame Struktur der d_k? Rang des Raums {d_k}, gemeinsame Nullstellen auf Geraden
print('Rang der Kofaktoren:',np.linalg.matrix_rank(d,1e-8))
for trial in range(2):
    a,b=rng.normal(size=4),rng.normal(size=4);ts=np.linspace(-2,2,3)
    P=[np.polyfit(ts,[ev(c,a+t*b,g2) for t in ts],2) for c in d]
    print(' Gerade: Nullst. d_1',np.round(np.roots(P[0]),4),'; d_1/q gleiche Nullst.?',np.round(np.roots(np.polyfit(ts,[ (a+t*b)@Q@(a+t*b) for t in ts],2)),4))
# Lichtkegel des Coframes? Vergleiche Q mit Tensor aus Daten: Kandidat g^{mu nu}= E^{-1}eta E^{-T}
np.set_printoptions(precision=4,suppress=True);print('Q (normiert):\n',Q/abs(Q).max())
