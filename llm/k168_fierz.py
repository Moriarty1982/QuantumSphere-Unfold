"""k168 (Erkundung, Route 1 der Literaturnotiz): Fierz-/polare Groessen der drei Spinorbloecke am Keim.
Phi = u^+ beta u, Theta = u^+ beta i gamma5 u, J^a = u^+ beta gamma^a u, K^a = u^+ beta gamma^a gamma5 u (Dirac-Basis wie k127).
Prueft Fierz-Identitaeten, Yvon-Takabayasi-Winkel, Geschwindigkeit/Spinachse je Block, Kreuzstrom (S3) und Lage zu e_y (Eichachse)
und zur Azimutrichtung phi-hat des Hintergrunds. Aufruf: python k168_fierz.py <Keim-Ordner>"""
import sys,json,numpy as np
from pathlib import Path
D=Path(sys.argv[1]);f70=json.loads((D/'precision-first-jet-70.json').read_text())
p=[float(eval(v.replace('/','/'))) if '/' not in v else float(v.split('/')[0])/float(v.split('/')[1]) for v in f70['point']]
psi=np.array([complex(float(a),float(b)) for a,b in f70['psi']]).reshape(3,4)
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]);Z2=np.zeros((2,2));I2=np.eye(2)
al=[np.block([[Z2,q],[q,Z2]]) for q in (sx,sy,sz)];be=np.diag([1,1,-1,-1.]);g5=np.block([[Z2,I2],[I2,Z2]])
gam=[be]+[be@a for a in al];eta=np.diag([1,-1,-1,-1.])
bil=lambda u,v,M:(u.conj()@be@M@v)
print('Punkt (t,x,y,z) =',p,' phi-hat =',np.round([-p[2]/np.hypot(p[1],p[2]),p[1]/np.hypot(p[1],p[2]),0],3))
for n,u in enumerate(psi):
    Phi=bil(u,u,np.eye(4)).real;Th=bil(u,u,1j*g5).real;J=np.array([bil(u,u,g).real for g in gam]);K=np.array([bil(u,u,g@g5).real for g in gam])
    rho2=np.hypot(Phi,Th);J2=J@eta@J;K2=K@eta@K
    if rho2<1e-12*max(1,np.abs(J).max()): print(f'Block {n}: singulaer (Phi=Theta=0), |J|={np.linalg.norm(J):.3e}');continue
    print(f'Block {n}: |u|^2={np.vdot(u,u).real:.4f}  phi^2={rho2:.4f}  beta={np.degrees(np.arctan2(Th,Phi)):.2f} Grad | Fierz J^2-(Phi^2+Th^2)={J2-rho2**2:.1e}, K^2+J^2={K2+J2:.1e}, J.K={J@eta@K:.1e}')
    print(f'    u^a = J/phi^2 = {np.round(J/rho2,4)}  s^a = K/phi^2 = {np.round(K/rho2,4)}')
# Kreuzstrom (S3 koppelt Block 0 und 1): j_S^a = Re(A^+ K^a B), K^a=(1,alpha)
Ka=[np.eye(4)]+al;A,B=psi[0],psi[1];jS=np.array([np.real(A.conj()@k@B) for k in Ka])
print('Kreuzstrom j_S^a =',np.round(jS,4),' Norm^2 (eta) =',round(float(jS@eta@jS),5))
