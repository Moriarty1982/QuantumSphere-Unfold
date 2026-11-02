import sys,math,itertools,numpy as np
from pathlib import Path
SRC=Path(sys.argv[1])
src=(SRC/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{SRC}')")
g={'__file__':'x'};exec(src,g);idx,fac,J,theta=g['idx'],g['fac'],g['J'],g['theta']
b3=idx(3)
Jx=lambda xi: sum(xi[m]*J[:,m*24:(m+1)*24] for m in range(4))
def thx(th,xi): return sum(th[i*24:(i+1)*24]*np.prod([xi[m]**a.count(m) for m in range(4)])/fac(a) for i,a in enumerate(b3))
rng=np.random.default_rng(8);thr=rng.normal(size=480)
print('Test: Ist Omega blind fuer die freie Richtung k(xi) (Kern von J(xi))?')
for _ in range(4):
    xi=rng.normal(size=4);u,s,vt=np.linalg.svd(Jx(xi));k=vt[-1]
    te=thx(theta,xi);tr=thx(thr,xi)
    print(f'  sigma_min J={s[-1]:.1e} | echt: |theta.k|/|theta|={abs(te@k)/np.linalg.norm(te):.1e} | zufaellig: {abs(tr@k)/np.linalg.norm(tr):.1e}')
P=np.load('ebenen.npy');Q=np.load('quadrik.npy')
print('Singulaerwerte von J(xi) (die kleinsten 6):')
for lab,xi in [('generisch',rng.normal(size=4))]+[(f'Ebene {k}',np.real(np.linalg.svd(np.hstack([P[k].real,P[k].imag]))[0][:,:2]@rng.normal(size=2))) for k in (0,1) for _ in range(2)]:
    print(f'  {lab:10s}',np.array2string(np.linalg.svd(Jx(xi),compute_uv=False)[-6:],precision=2),' q=',f'{xi@Q@xi/np.dot(xi,xi):.2f}')
