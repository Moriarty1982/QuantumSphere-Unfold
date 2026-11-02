"""k121: Coframe E am Keim; q und die zwei Ebenen in Rahmenkomponenten eta_a = V^mu_a xi_mu."""
import json,sys,numpy as np,sympy as s
from pathlib import Path
D=Path(sys.argv[1])
t,x,y,z=s.symbols('t x y z',real=True);N=16;I=s.I
rho=s.sqrt(x**2+y**2);vv=s.Matrix([x,y,z])/t;gam=1/s.sqrt(1-vv.dot(vv))
th=s.asin(8*t/N)/2;c,d_,Del=s.cos(th),s.sin(th),s.cos(2*th)
pp=3*c/(2*rho*Del);qq=-3*d_/(2*rho*Del);Gm=s.Matrix([[0,0,pp],[0,0,qq],[pp,qq,0]]);spin=[-y/rho,x/rho,0]
f70=json.loads((D/'precision-first-jet-70.json').read_text());root=json.loads((D/'precision-completed-root-result.json').read_text())
p0={k:s.Rational(v) for k,v in zip((t,x,y,z),f70['point'])}
psi=np.array([complex(float(a),float(b)) for a,b in f70['psi']])
fd=[float(v) for v in root['first_derivatives_real_packed']];dpsi=[np.array(fd[m*24:m*24+12])+1j*np.array(fd[m*24+12:m*24+24]) for m in range(4)]
G=np.array(Gm.subs(p0).evalf(),dtype=float);sp_=[float(s.N(v.subs(p0))) if v!=0 else 0. for v in spin]
A=[np.zeros((12,12))]+[np.kron(G*sp_[k],np.eye(4)) for k in range(3)]
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]);Z2=np.zeros((2,2))
al=[np.block([[Z2,p],[p,Z2]]) for p in (sx,sy,sz)];beta=np.diag([1,1,-1,-1])
S3=np.array([[0,.5,0],[.5,0,0],[0,0,0]]);Qm=[np.kron(S3,m) for m in [np.eye(4)]+al];Km=[np.kron(np.eye(3),m) for m in [np.eye(4)]+al]
cov=[dpsi[m]+1j*A[m]@psi for m in range(4)]
E=np.array([[np.real(psi.conj()@Qm[a]@cov[m]) for m in range(4)] for a in range(4)]);V=np.linalg.inv(E)
print('det E =',np.linalg.det(E));np.set_printoptions(precision=4,suppress=True)
Qq=np.load('quadrik.npy');Pl=np.load('ebenen.npy')
# q im Rahmen: xi = E^T eta  (eta_a = V^mu_a xi_mu  <=> xi = E^T eta)
Qf=E@Qq@E.T;Qf/=Qf[0,0];print('q in Rahmenkomponenten (normiert auf [0,0]):\n',Qf)
eta=np.diag([1,-1,-1,-1]);print('Abstand zu Minkowski diag(1,-1,-1,-1):',np.linalg.norm(Qf-eta))
np.save('E.npy',E)
for k in range(2):
    B=np.linalg.svd(np.hstack([Pl[k].real,Pl[k].imag]))[0][:,:2]   # reelle Basis der Ebene (xi-Koordinaten)
    Bf=V.T@B;Bf=np.linalg.qr(Bf)[0]                                 # Ebene in Rahmenkomponenten eta
    print(f'Ebene {k} im Rahmen (Spalten, Komponenten eta_0..eta_3):\n',Bf)
    ann=np.linalg.svd(Bf.T)[2][2:].T;print(f'  Querrichtungen (Annihilator, Rahmenvektoren e_0..e_3):\n',ann)
# Zustandsgroessen im Rahmen: Strom j^a, Spin
gam0=beta;gamma=[beta]+[beta@a for a in al];g5=np.block([[Z2,np.eye(2)],[np.eye(2),Z2]])
P3=psi.reshape(3,4)
for n in range(3):
    u=P3[n]
    if np.linalg.norm(u)<1e-12: continue
    ub=u.conj()@beta
    j=np.array([np.real(ub@gamma[a]@u) for a in range(4)]);ax=np.array([np.real(ub@gamma[a]@g5@u) for a in range(4)])
    print(f'Farbkomponente {n}: |u|={np.linalg.norm(u):.3f}  Strom j^a={j}  Axialstrom s^a={ax}')
