"""k127: eigener Aufbau des vervollstaendigten Symbols J = dR/d(erste Ableitungen) fuer beliebige Punkte und Feldwerte.
Test: verschwinden G- und dg-Zeilen auf der Richtung D_z Psi (freie z-Verschiebung) auch abseits von z=0 und abseits von Loesungen?"""
import json,sys,numpy as np,sympy as s
from pathlib import Path
D=Path(sys.argv[1]);w=np.load(D/'completion-omega-witness.npz')
t,x,y,z=s.symbols('t x y z',real=True);X=(t,x,y,z);N=16
rho=s.sqrt(x**2+y**2);gam=1/s.sqrt(1-(x**2+y**2+z**2)/t**2);th=s.asin(8*t/N)/2;c,d_,Del=s.cos(th),s.sin(th),s.cos(2*th)
pp=3*c/(2*rho*Del);qq=-3*d_/(2*rho*Del);Gm=s.Matrix([[0,0,pp],[0,0,qq],[pp,qq,0]]);spin=[-y/rho,x/rho,s.Integer(0)];hm=16*gam/(N*Del)
connS=[s.zeros(3)]+[Gm*sp for sp in spin]
fconn=s.lambdify(X,connS,'numpy');fdc=s.lambdify(X,[[M.diff(v) for M in connS] for v in X],'numpy')
fh=s.lambdify(X,hm,'numpy');fdh=s.lambdify(X,[hm.diff(v) for v in X],'numpy')
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]);Z2=np.zeros((2,2))
al=[np.block([[Z2,p],[p,Z2]]) for p in (sx,sy,sz)];beta=np.diag([1,1,-1,-1.])
S3=np.array([[0,.5,0],[.5,0,0],[0,0,0]]);Y3=np.array([[0,-1j,0],[1j,0,0],[0,0,0]]);Z3=np.diag([1,-1,0.])
K=[np.kron(np.eye(3),m) for m in [np.eye(4)]+al];Q=[np.kron(S3,m) for m in [np.eye(4)]+al];Y=np.kron(Y3,beta);Zm=np.kron(Z3,beta)
def realmat(M): return np.block([[M.real,-M.imag],[M.imag,M.real]])
rv=lambda v: np.r_[v.real,v.imag]
Hb=[realmat(-1j*K[0])]+[realmat(1j*k) for k in K[1:]]
def R(jv,psi,p):
    conn=[np.kron(np.array(M,dtype=complex),np.eye(4)) for M in fconn(*p)];dc=[[np.kron(np.array(M,dtype=complex),np.eye(4)) for M in row] for row in fdc(*p)]
    h=fh(*p);dh=fdh(*p)
    j=[jv[m*24:m*24+12]+1j*jv[m*24+12:m*24+24] for m in range(4)]
    cov=[j[m]+1j*conn[m]@psi for m in range(4)]
    E=np.array([[np.real(psi.conj()@Q[a]@cov[m]) for m in range(4)] for a in range(4)]);V=np.linalg.inv(E)
    A=np.array([np.r_[np.real(psi.conj()@q),-np.imag(psi.conj()@q)] for q in Q])
    F=sum(1j*V[m,a]*K[a]@cov[m] for m in range(4) for a in range(4))-h*Y@psi
    G=np.zeros(4);C=np.zeros(4)
    for mu in range(4):
        dv=[1j*(dc[mu][nu]@psi+conn[nu]@j[mu]) for nu in range(4)]
        dE=np.array([[np.real(j[mu].conj()@Q[a]@cov[nu]+psi.conj()@Q[a]@dv[nu]) for nu in range(4)] for a in range(4)]);dV=-V@dE@V
        b=sum(1j*K[a]@(dV[nu,a]*cov[nu]+V[nu,a]*dv[nu]) for nu in range(4) for a in range(4))-dh[mu]*Y@psi-h*Y@j[mu]
        km=A@sum(V[mu,a]*Hb[a] for a in range(4));G+=km@rv(b)
        C[mu]=-.5*dh[mu]*np.real(psi.conj()@Zm@psi)-h*np.real(psi.conj()@Zm@j[mu])
    return np.r_[rv(F),G,C],cov
def symbol(jv,psi,p,e=1e-6):
    return np.column_stack([(R(jv+e*np.eye(96)[k],psi,p)[0]-R(jv-e*np.eye(96)[k],psi,p)[0])/(2*e) for k in range(96)])
f70=json.loads((D/'precision-first-jet-70.json').read_text());root=json.loads((D/'precision-completed-root-result.json').read_text())
p0=[float(s.Rational(v)) for v in f70['point']];psi0=np.array([complex(float(a),float(b)) for a,b in f70['psi']]);j0=np.array([float(v) for v in root['first_derivatives_real_packed']])
J0=symbol(j0,psi0,p0);print('Abgleich mit gespeichertem J: max|Diff| =',np.max(abs(J0-w['completed_first_symbol'])),' |J| ~',np.max(abs(J0)))
rng=np.random.default_rng(0)
def ztest(jv,psi,p,label):
    J=symbol(jv,psi,p);cov=R(jv,psi,p)[1];vz=rv(cov[3])
    N=[J[24:,m*24:(m+1)*24]@vz for m in range(4)];Nall=[J[24:,m*24:(m+1)*24]@rv(cov[n]) for m in range(4) for n in range(4)]
    print(f'{label:42s} |G,dg auf D_z Psi| = {max(np.linalg.norm(v) for v in N):.2e}   (Vergleich andere Richtungen ~ {np.median([np.linalg.norm(v) for v in Nall]):.2e})')
ztest(j0,psi0,p0,'Keim, echte Daten')
ztest(j0+0.3*rng.normal(size=96),psi0,p0,'Keim-Punkt, gestoerte Ableitungen')
ztest(rng.normal(size=96),psi0+0.5*(rng.normal(size=12)+1j*rng.normal(size=12)),p0,'Keim-Punkt, zufaelliges Feld')
for p in ([1,0.6,0,0.2],[1.2,0.4,0.25,-0.3],[0.9,0.3,-0.2,0.35]):
    ztest(j0+0.3*rng.normal(size=96),psi0+0.3*(rng.normal(size=12)+1j*rng.normal(size=12)),p,f'Punkt {p}, zufaellig')
