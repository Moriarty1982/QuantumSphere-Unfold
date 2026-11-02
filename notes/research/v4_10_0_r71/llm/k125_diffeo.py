"""k125: Symbol J(xi) auf den Diffeomorphismus-Richtungen B c (B = real gepackte D_mu Psi)."""
import json,sys,numpy as np
from pathlib import Path
exec(open('k121_rahmen.py').read().split("print('det E")[0])
SRC=Path(sys.argv[1]);w=np.load(SRC/'completion-omega-witness.npz');J=w['completed_first_symbol']
Jx=lambda xi: sum(xi[m]*J[:,m*24:(m+1)*24] for m in range(4))
B=np.column_stack([np.r_[c.real,c.imag] for c in cov])
rng=np.random.default_rng(1);xi=rng.normal(size=4)
M=Jx(xi)@B;np.set_printoptions(precision=3,suppress=True)
print('|F-Zeilen auf B| =',np.linalg.norm(M[:24]),' |G-Zeilen| =',np.linalg.norm(M[24:28]),' |dg-Zeilen| =',np.linalg.norm(M[28:]))
print('Rang von J(xi)B generisch:',np.linalg.svd(M,compute_uv=False))
Pl=np.load('ebenen.npy');planes=[np.linalg.svd(np.hstack([Pl[k].real,Pl[k].imag]))[0][:,:2] for k in range(2)]
for k in range(2):
    xi=planes[k]@rng.normal(size=2);print(f'auf Ebene {k}: Singulaerwerte von J(xi)B',np.linalg.svd(Jx(xi)@B,compute_uv=False))
# Struktur der G- und dg-Bloecke: N^mu = J_mu-Block (Zeilen 24..31) @ B
N=[J[24:,m*24:(m+1)*24]@B for m in range(4)]
print('dg-Block (Zeilen 28..31) fuer xi=e_mu:');[print('  mu',m,'\n',N[m][4:]) for m in range(4)]
print('G-Block (Zeilen 24..27) fuer xi=e_mu:');[print('  mu',m,'\n',N[m][:4]) for m in range(4)]
np.save('N.npy',np.array(N))
