import sys,numpy as np,itertools
from pathlib import Path
SRC=Path(sys.argv[1])
src=(SRC/'balanced_spencer_check.py').read_text().split('def run_variant')[0].replace("Path(__file__).resolve().parent",f"Path(r'{SRC}')")
g={'__file__':'x'};exec(src,g);idx=g['idx']
d=np.load('kofaktoren.npy');Q=np.load('quadrik.npy');g2=idx(2)
def mat(c):
    M=np.zeros((4,4))
    for i,a in enumerate(g2):
        if a[0]==a[1]: M[a[0],a[0]]=c[i]
        else: M[a[0],a[1]]=M[a[1],a[0]]=c[i]/2
    return M
Ms=[mat(c) for c in d]
print('Rang der Kofaktor-Matrizen:',[np.linalg.matrix_rank(M,1e-8*abs(M).max()) for M in Ms])
print('Eigenwerte (normiert):');[print('  ',np.array2string(np.linalg.eigvalsh(M)/abs(np.linalg.eigvalsh(M)).max(),precision=3)) for M in Ms]
# gemeinsamer Linearfaktor?  Ist ein Vektor v mit M_k v gemeinsam im Bild... Test: Bilder aller M_k zusammen
img=np.hstack(Ms);print('Rang gemeinsames Bild:',np.linalg.matrix_rank(img,1e-8*abs(img).max()))
# Liegen die d_k in Q * (Linearformen)?  Nein, Grad passt nicht; teste ob span{d_k} + Q Kegelstruktur: d_k = Q-Spur-freie Teile?
# Pencil: d(lambda) = sum lambda_k d_k; enthaelt der Raum Q selbst?
X=np.array([[*c] for c in d]);qv=np.array([Q[a[0],a[1]]*(1 if a[0]==a[1] else 2) for a in g2])
res=np.linalg.lstsq(X.T,qv,rcond=None);print('q im Raum der d_k? Rest',np.linalg.norm(X.T@res[0]-qv)/np.linalg.norm(qv))
# Rang-1-Elemente im Raum (d = l*m)?  minimiere sigma_3 ueber Pencil grob
rng=np.random.default_rng(0);best=1
for _ in range(20000):
    lam=rng.normal(size=4);M=sum(l*m for l,m in zip(lam,Ms));s=np.abs(np.linalg.eigvalsh(M));s.sort();best=min(best,s[1]/s[-1])
print('kleinstes sigma2/sigma_max im Pencil (Zufallssuche):',f'{best:.2e}')
