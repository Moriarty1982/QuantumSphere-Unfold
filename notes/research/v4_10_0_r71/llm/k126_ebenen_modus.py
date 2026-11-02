import json,sys,numpy as np
from pathlib import Path
exec(open('k121_rahmen.py').read().split("print('det E")[0])
N=np.load('N.npy');Pl=np.load('ebenen.npy');planes=[np.linalg.svd(np.hstack([Pl[k].real,Pl[k].imag]))[0][:,:2] for k in range(2)]
np.set_printoptions(precision=4,suppress=True)
Mx=lambda xi: sum(xi[m]*N[m] for m in range(4))   # 8x4: G (4) + dg (4) auf Diffeo-Richtungen c
wv=N[0][4,:];print('dg-Kovektor w =',wv,' (Gradient von g entlang der Feldableitungen)')
print('D_z Psi =',np.round(cov[3],3)[:4],'... |D_z Psi| =',np.linalg.norm(cov[3]))
rng=np.random.default_rng(3)
for k in range(2):
    for _ in range(2):
        xi=planes[k]@rng.normal(size=2);u,s,vt=np.linalg.svd(Mx(xi));K=vt[2:].T
        # Extra-Kernrichtung orthogonal zu e_z
        c=K[:,np.argmin(abs(K[3,:]))] if abs(K[3,0])>1e-9 or abs(K[3,1])>1e-9 else K[:,0]
        c=K@np.linalg.svd(K[3:4,:])[2][-1];c/=np.linalg.norm(c)
        print(f'Ebene {k}: xi={np.round(xi/np.linalg.norm(xi),3)}  Extra-Modus c={np.round(c,4)}  xi.c={xi@c/np.linalg.norm(xi):.2e}  w.c={wv@c:.2e}')
# Ist die Extra-Richtung fest (unabhaengig von xi in der Ebene)?  Ebenen-Annihilatoren:
for k in range(2):
    ann=np.linalg.svd(planes[k].T)[2][2:].T;print(f'Annihilator von Ebene {k} (Vektoren):\n',ann.T)
# Struktur von G auf (t,x,y): G(xi) c = sum_mu xi_mu N^mu_G c ; schreibe als Tensor T[r, mu, nu] und pruefe Symmetrie in (mu,nu)
T=np.array([N[m][:4,:3] for m in range(4)])  # mu, r, nu
print('G-Tensor: |Antisymm. in (mu,nu) fuer nu<3| / |T| ~ Lie-Ableitung-Struktur?')
for r in range(4):
    Mr=T[:3,r,:];print('  Zeile',r,' sym/antisym Anteil:',np.round([np.linalg.norm(Mr+Mr.T)/2,np.linalg.norm(Mr-Mr.T)/2],3))
