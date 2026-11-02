"""Abgeschnittene Potenzreihen in 4 Variablen (Monom-Taylorkoeffizienten) fuer das OP5-Vergleichsmodell."""
import itertools,json,math,numpy as np,sympy as s
from pathlib import Path
def monos(D): return [a for d in range(D+1) for a in sorted({tuple(c.count(m) for m in range(4)) for c in itertools.combinations_with_replacement(range(4),d)},reverse=True)]
M3=monos(3);M4=monos(4);I3={a:i for i,a in enumerate(M3)};I4={a:i for i,a in enumerate(M4)}
PAIRS=[(i,j,I3[tuple(x+y for x,y in zip(a,b))]) for i,a in enumerate(M3) for j,b in enumerate(M3) if sum(a)+sum(b)<=3]
def mul(a,b,op=np.multiply):
    out=None
    for i,j,k in PAIRS:
        v=op(a[i],b[j])
        if out is None: out=np.zeros((35,)+np.shape(v),dtype=complex)
        out[k]+=v
    return out
def d4to3(c4,mu):  # Ableitung einer Grad-4-Reihe -> Grad 3
    out=np.zeros((35,)+c4.shape[1:],dtype=complex)
    for i,a in enumerate(M3):
        b=list(a);b[mu]+=1;out[i]=(a[mu]+1)*c4[I4[tuple(b)]]
    return out
def trunc(c4): return c4[[I4[a] for a in M3]]
t,x,y,z=s.symbols('t x y z',real=True);X=(t,x,y,z);N=16
rho=s.sqrt(x**2+y**2);gam=1/s.sqrt(1-(x**2+y**2+z**2)/t**2);th=s.asin(8*t/N)/2;cc,dd,Del=s.cos(th),s.sin(th),s.cos(2*th)
pp=3*cc/(2*rho*Del);qq=-3*dd/(2*rho*Del);Gm=s.Matrix([[0,0,pp],[0,0,qq],[pp,qq,0]]);spin=[-y/rho,x/rho,s.Integer(0)];hm=16*gam/(N*Del)
def taylor(expr,p,D):
    out=np.zeros(len(monos(D)),dtype=complex);cache={(0,0,0,0):expr}
    for i,a in enumerate(monos(D)):
        if a not in cache:
            mu=next(m for m in range(4) if a[m]>0);b=list(a);b[mu]-=1;cache[a]=s.diff(cache[tuple(b)],X[mu])
        out[i]=complex(s.N(cache[a].subs(dict(zip(X,p))),20))/math.prod(math.factorial(k) for k in a)
    return out
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]);Z2=np.zeros((2,2))
al=[np.block([[Z2,q],[q,Z2]]) for q in (sx,sy,sz)];beta=np.diag([1,1,-1,-1.])
S3=np.array([[0,.5,0],[.5,0,0],[0,0,0]]);Y3=np.array([[0,-1j,0],[1j,0,0],[0,0,0]]);Z3=np.diag([1,-1,0.])
Km=[np.kron(np.eye(3),m) for m in [np.eye(4)]+al];Qm=[np.kron(S3,m) for m in [np.eye(4)]+al];Ym=np.kron(Y3,beta);Zm=np.kron(Z3,beta)
Ha=[-1j*Km[0]]+[1j*k for k in Km[1:]]
class Background:
    def __init__(self,p):
        conn4=[np.zeros((70,12,12),dtype=complex)]
        for k in range(3):
            C=np.zeros((70,12,12),dtype=complex)
            for i in range(3):
                for j in range(3):
                    if Gm[i,j]!=0 and spin[k]!=0:
                        tc=taylor(Gm[i,j]*spin[k],p,4)
                        for r in range(4): C[:,4*i+r,4*j+r]=tc
            conn4.append(C)
        h4=taylor(hm,p,4)
        self.conn=[trunc(c) for c in conn4];self.dc=[[d4to3(conn4[nu],mu) for nu in range(4)] for mu in range(4)]
        self.h=trunc(h4);self.dh=[d4to3(h4,mu) for mu in range(4)]
def conjT(v): return np.conj(v)   # x reell: Koeffizienten konjugieren
def herm(a,M,b):  # a^dagger M b  als Skalarreihe
    return mul(conjT(a),np.einsum('ij,kj->ki',M,b) if b.ndim==2 else None,lambda u,w: u@w)
def Rseries(psi4,bg):
    """psi4: (70,12) komplex Monomkoeffizienten bis Grad 4. Rueckgabe (35,32) reelle Koeffizienten von R=(F,G,dg)."""
    psi=trunc(psi4);j=[d4to3(psi4,m) for m in range(4)]
    cov=[j[m]+1j*mul(bg.conn[m],psi,lambda A,v:A@v) for m in range(4)]
    E=np.zeros((35,4,4),dtype=complex)
    for a in range(4):
        for m in range(4): E[:,a,m]=herm(psi,Qm[a],cov[m]).real
    E0=E[0].real;V0=np.linalg.inv(E0);Nn=E.copy();Nn[0]=0
    V=np.zeros_like(E);V[0]=V0;term=V.copy()
    for k in range(3):
        term=-mul(mul(np.broadcast_to(V0,(35,4,4)).copy()*(np.arange(35)==0)[:,None,None],Nn,lambda A,B:A@B),term,lambda A,B:A@B);V=V+term
    smul=lambda sc,vec: mul(sc,vec,lambda u,w:u*w)
    F=sum(1j*smul(V[:,m,a],np.einsum('ij,kj->ki',Km[a],cov[m])) for m in range(4) for a in range(4))-smul(bg.h,np.einsum('ij,kj->ki',Ym,psi))
    G=np.zeros((35,4),dtype=complex);C=np.zeros((35,4),dtype=complex)
    for mu in range(4):
        dv=[1j*(mul(bg.dc[mu][nu],psi,lambda A,v:A@v)+mul(bg.conn[nu],j[mu],lambda A,v:A@v)) for nu in range(4)]
        dE=np.zeros((35,4,4),dtype=complex)
        for a in range(4):
            for nu in range(4): dE[:,a,nu]=(herm(j[mu],Qm[a],cov[nu])+herm(psi,Qm[a],dv[nu])).real
        dV=-mul(mul(V,dE,lambda A,B:A@B),V,lambda A,B:A@B)
        b=sum(1j*(smul(dV[:,nu,a],np.einsum('ij,kj->ki',Km[a],cov[nu]))+smul(V[:,nu,a],np.einsum('ij,kj->ki',Km[a],dv[nu]))) for nu in range(4) for a in range(4))
        b=b-smul(bg.dh[mu],np.einsum('ij,kj->ki',Ym,psi))-smul(bg.h,np.einsum('ij,kj->ki',Ym,j[mu]))
        for a2 in range(4):
            G[:,a2]+=sum(smul(V[:,mu,a],herm(psi,Qm[a2],np.einsum('ij,kj->ki',Ha[a],b))) for a in range(4)).real
        C[:,mu]=(-.5*smul(bg.dh[mu],herm(psi,Zm,psi))-smul(bg.h,herm(psi,Zm,j[mu]))).real
    return np.concatenate([F.real,F.imag,G.real,C.real],axis=1)
def load_germ(D):
    import mpmath as mp
    f70=json.loads((D/'precision-first-jet-70.json').read_text());root=json.loads((D/'precision-completed-root-result.json').read_text())
    second=json.loads((D/'precision-second-jet-result.json').read_text());omega=json.loads((D/'precision-omega-repair-result.json').read_text())
    fifth=json.loads((D/'precision-fifth-gate-repair-result.json').read_text())
    psi4=np.zeros((70,12),dtype=complex);psi4[I4[(0,0,0,0)]]=[complex(float(a),float(b)) for a,b in f70['psi']]
    for deg,packed in [(1,root['first_derivatives_real_packed']),(2,second['second_coefficients_real_packed']),(3,omega['third_coefficients_real_packed']),(4,fifth['fourth_coefficients_real_packed'])]:
        vals=[float(v) for v in packed]
        for i,c in enumerate(itertools.combinations_with_replacement(range(4),deg)):
            a=tuple(c.count(m) for m in range(4));psi4[I4[a]]=np.array(vals[i*24:i*24+12])+1j*np.array(vals[i*24+12:i*24+24])
    return [float(s.Rational(v)) for v in f70['point']],psi4
