"""k155: Omega (theta) hochgenau am reparierten Keim: zulaessige c3 bei festem 2-Jet mit den Gleichungen vom Grad 2
(K3) gegen bis Grad 3 (K4). theta = die Linearform auf K3, die auf K4 verschwindet. Aufruf: python k155_hp_theta.py <Ordner>"""
import sys,time,numpy as np,flint
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent));from k154_hp_tools import *
t0=time.time();D=sys.argv[1];mons,A,B=load();w=gauge_series(D)
# Probe Eichreihe gegen float
import k138_tps_d as T
_,psi=T.load_germ(D,5);gf=np.einsum('ij,nj->ni',T.Km[2],psi[:len(T.monos(2))]);wf=np.concatenate([2*gf.real,2*gf.imag],axis=1)
print('Eichreihe arb gegen float:',f"{max(np.max(abs(tofloat(w[a])[0]-wf[T.index(2)[a]])) for a in w):.1e}")
n3,n4=24*len(mon(3)),24*len(mon(4))
# Zeilen: R2 (c3), R3 (c3, c4), G3 (c3), G4 (c3, c4)
R2_3=Rblock(A,B,2,3);R3_3=Rblock(A,B,3,3);R3_4=Rblock(A,B,3,4);G3_3=Gblock(w,3,3);G4_3=Gblock(w,4,3);G4_4=Gblock(w,4,4)
# Stufe 1: c4 eliminieren
T4=stack([[R3_4],[G4_4]]);L,s,r,h=null_refine(T4,'left');print(f'c4: Block {T4.nrows()}x{T4.ncols()}, Rang {r}, Linkskern {L.ncols()}, Residuen {[f"{x:.0e}" for x in h]}',flush=True)
Dr=L.transpose()*stack([[R3_3],[G4_3]])     # abgeleitete Zeilen auf c3
# K3: Kern von [R2; G3] auf c3; K4: zusaetzlich die abgeleiteten Zeilen
N3,s3,r3,h3=null_refine(stack([[R2_3],[G3_3]]),'right');print(f'K3: dim {N3.ncols()}, Residuen {[f"{x:.0e}" for x in h3]}')
C=Dr*N3;Cf=tofloat(C);sc=np.linalg.svd(Cf,compute_uv=False);print('abgeleitete Zeilen auf K3: Singulaerwerte',np.array2string(sc[:4]/sc[0],precision=2),'... Anzahl',len(sc))
# theta = Linearform auf K3 (in K3-Koordinaten), hochgenau: groesster Singulaervektor, nachverbessert via Gram-Eigenvektor
G=C.transpose()*C;ev=flint.acb_mat(G).eig(algorithm='approx',right=True)
vals,vecs=ev;vals=[float(v.real.mid()) for v in vals];i=int(np.argmax(vals))
print('Gram-Eigenwerte (groesste 3, relativ):',np.array2string(np.sort(vals)[::-1][:3]/max(vals),precision=2))
v=arb_mat([[vecs[k,i].real] for k in range(vecs.nrows())])
theta=N3*v           # theta als Vektor im c3-Raum (ausgeglichene Koordinaten): Linearform u -> theta^T u auf K3
import pickle;pickle.dump([[str(theta[k,0].mid())] for k in range(theta.nrows())],open(W/'theta_hp.pkl','wb'))
# Abgleich mit k148 (float)
tf=tofloat(theta)[:,0];print(f'theta hochgenau berechnet in {time.time()-t0:.0f} s; Norm {np.linalg.norm(tf):.3f}')
