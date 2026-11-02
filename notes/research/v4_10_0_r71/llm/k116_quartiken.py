"""k116: Die vier zusaetzlichen Beziehungen bei Grad 7. Omega-Anteil -> Quartiken c_k(xi) mit c_k(d) Omega = Folge der J-Gleichungen."""
import sys,math,itertools,numpy as np
from pathlib import Path
SRC=Path(sys.argv[1])
src=(SRC/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{SRC}')")
g={'__file__':'x'};exec(src,g);idx,fac,J,theta=g['idx'],g['fac'],g['J'],g['theta']
p=7;A,B,_,rw,cw=g['matrix'](p);rn=np.linalg.norm(B,axis=1);X=B/rn[:,None]
U,s,Vt=np.linalg.svd(X);r=int(sum(s>s[0]*1e-9));L=U[:,r:]
nJ=len(idx(p-1))*32;Y=L[nJ:,:]                       # Omega-Block (35 Zeilen)
u,sv,_=np.linalg.svd(Y,full_matrices=False);print('Omega-Anteil des Linksnullraums, Singulaerwerte:',np.array2string(sv[:7],precision=2))
k=int(sum(sv>1e-8));Yk=u[:,:k]
gam=idx(3+0)  # placeholder
gam=idx(p-3)
coef=np.array([[Yk[i,j]*rw[nJ+i]/rn[nJ+i]/math.prod(math.factorial(a.count(m)) for m in range(4)) for i,a in enumerate(gam)] for j in range(k)])  # c_k = sum z/gamma! xi^gamma
def ev(c,xi): return sum(c[i]*np.prod([xi[m]**a.count(m) for m in range(4)]) for i,a in enumerate(gam))
np.save('quartiken.npy',coef);print('Anzahl Quartiken',k)
# gemeinsamer Faktor? Schnitt mit zufaelligen Geraden
rng=np.random.default_rng(5)
for trial in range(3):
    a,b=rng.normal(size=4),rng.normal(size=4)
    polys=[]
    for c in coef:
        ts=np.linspace(-2,2,5);vals=[ev(c,a+t*b) for t in ts];polys.append(np.polyfit(ts,vals,4))
    roots=np.roots(polys[0])
    print('Gerade',trial,': Nullstellen von c_1 und |c_2..c_k| dort / |c|:')
    for t in roots:
        xi=a+t*b;sc=np.linalg.norm(xi)**4
        print('   t=',np.round(t,4),' ',[f'{abs(ev(c,xi))/sc:.1e}' for c in coef[1:]])
