"""k138: abgeschnittene Potenzreihen beliebigen Grades fuer das OP5-Vergleichsmodell (Verallgemeinerung von k135_tps).
Hintergrund (Verbindung, h) ueber Komposition univariater Reihen statt symbolischer Ableitungen.
Rseries(psi, D): psi Monomkoeffizienten bis Grad D+1, Rueckgabe R = (F, G, dg) bis Grad D, Form (nM(D), 32)."""
import itertools,json,math,numpy as np,sympy as s
from functools import lru_cache
from pathlib import Path

@lru_cache(None)
def monos(D): return [a for d in range(D+1) for a in sorted({tuple(c.count(m) for m in range(4)) for c in itertools.combinations_with_replacement(range(4),d)},reverse=True)]
@lru_cache(None)
def index(D): return {a:i for i,a in enumerate(monos(D))}
@lru_cache(None)
def pairs(D):
    M=monos(D);I=index(D);P=[(i,j,I[tuple(x+y for x,y in zip(a,b))]) for i,a in enumerate(M) for j,b in enumerate(M) if sum(a)+sum(b)<=D]
    return tuple(np.array(v) for v in zip(*P))
def deg(D): return np.array([sum(a) for a in monos(D)])
def mul(a,b,D,op=np.multiply):
    i,j,k=pairs(D);v=op(a[i],b[j]);out=np.zeros((len(monos(D)),)+v.shape[1:],dtype=v.dtype);np.add.at(out,k,v);return out
mm=lambda A,B:np.matmul(A,B)
mv=lambda A,v:np.einsum('...ij,...j->...i',A,v)
def deriv(c,mu,D):
    """c: Reihe bis Grad D+1 -> d/dx_mu bis Grad D."""
    I1=index(D+1);out=np.zeros((len(monos(D)),)+c.shape[1:],dtype=c.dtype)
    for n,a in enumerate(monos(D)):
        b=list(a);b[mu]+=1;out[n]=(a[mu]+1)*c[I1[tuple(b)]]
    return out
def trunc(c,D): return c[:len(monos(D))]
def coord(p,D):
    X=[];I=index(D)
    for mu in range(4):
        c=np.zeros(len(monos(D)));c[0]=p[mu]
        if D>=1: e=[0]*4;e[mu]=1;c[I[tuple(e)]]=1.0
        X.append(c)
    return X
def compose(f,u,c,D):
    """f: sympy-Ausdruck in u; c: Skalarreihe; f(c) bis Grad D."""
    c0=float(np.real(c[0]));dl=c.copy();dl[0]=0
    der=[float(s.N(s.diff(f,u,k).subs(u,c0),30))/math.factorial(k) for k in range(D+1)]
    out=np.zeros_like(c,dtype=float);pw=np.zeros_like(out);pw[0]=1.0
    for k in range(D+1):
        out=out+der[k]*pw;pw=mul(pw,dl,D)
    return out
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]);Z2=np.zeros((2,2))
al=[np.block([[Z2,q],[q,Z2]]) for q in (sx,sy,sz)];beta=np.diag([1,1,-1,-1.])
S3=np.array([[0,.5,0],[.5,0,0],[0,0,0]]);Y3=np.array([[0,-1j,0],[1j,0,0],[0,0,0]]);Z3=np.diag([1,-1,0.])
Km=[np.kron(np.eye(3),m) for m in [np.eye(4)]+al];Qm=[np.kron(S3,m) for m in [np.eye(4)]+al];Ym=np.kron(Y3,beta);Zm=np.kron(Z3,beta)
Ha=[-1j*Km[0]]+[1j*k for k in Km[1:]]
class Background:
    """Verbindung A_k = G spin_k (x) I4 und h bis Grad D+1; conn, h bis Grad D, dc, dh bis Grad D."""
    def __init__(self,p,D):
        E=D+1;u=s.symbols('u');t,x,y,z=coord(p,E);m=lambda a,b:mul(a,b,E)
        rho=compose(s.sqrt(u),u,m(x,x)+m(y,y),E);irho=compose(1/s.sqrt(u),u,m(x,x)+m(y,y),E)
        it=compose(1/u,u,t,E);q=m(m(x,x)+m(y,y)+m(z,z),m(it,it));gam=compose((1-u)**s.Rational(-1,2),u,q,E)
        th=s.asin(u/2)/2
        cc=compose(s.cos(th),u,t,E);dd=compose(s.sin(th),u,t,E);iDel=compose(1/s.cos(2*th),u,t,E)
        pp=1.5*m(cc,iDel);qq=-1.5*m(dd,iDel)          # ohne 1/rho
        spin=[-m(y,irho),m(x,irho),np.zeros_like(x)]
        # G*spin_k: Eintraege pp/rho*spin_k, qq/rho*spin_k
        conn=[np.zeros((len(monos(E)),12,12))]
        for k in range(3):
            a=m(m(pp,irho),spin[k]);b=m(m(qq,irho),spin[k]);G=np.zeros((len(monos(E)),3,3))
            G[:,0,2]=G[:,2,0]=a;G[:,1,2]=G[:,2,1]=b
            conn.append(np.einsum('nij,rs->nirjs',G,np.eye(4)).reshape(-1,12,12))
        h=m(gam,iDel)
        self.D=D;self.conn=[trunc(c,D).astype(complex) for c in conn];self.dc=[[deriv(conn[nu],mu,D).astype(complex) for nu in range(4)] for mu in range(4)]
        self.h=trunc(h,D);self.dh=[deriv(h,mu,D) for mu in range(4)]
def herm(a,M,b,D): return mul(np.conj(a),mv(M,b),D,lambda u,w:(u*w).sum(-1))
def Rseries(psiD1,bg):
    D=bg.D;n=len(monos(D));M=lambda a,b,op=np.multiply:mul(a,b,D,op)
    psi=trunc(psiD1,D);j=[deriv(psiD1,m,D) for m in range(4)]
    cov=[j[m]+1j*M(bg.conn[m],psi,mv) for m in range(4)]
    E=np.zeros((n,4,4))
    for a in range(4):
        for m in range(4): E[:,a,m]=herm(psi,Qm[a],cov[m],D).real
    V0=np.linalg.inv(E[0]);Nn=E.copy();Nn[0]=0
    V=np.zeros_like(E);V[0]=V0;term=V.copy()
    for k in range(D):
        term=-np.einsum('ij,njk->nik',V0,M(Nn,term,mm));V=V+term
    sm=lambda sc,vec:M(sc,vec,lambda u,w:u[...,None]*w)
    F=sum(1j*sm(V[:,m,a],mv(Km[a],cov[m])) for m in range(4) for a in range(4))-sm(bg.h,mv(Ym,psi))
    G=np.zeros((n,4));C=np.zeros((n,4))
    for mu in range(4):
        dv=[1j*(M(bg.dc[mu][nu],psi,mv)+M(bg.conn[nu],j[mu],mv)) for nu in range(4)]
        dE=np.zeros((n,4,4))
        for a in range(4):
            for nu in range(4): dE[:,a,nu]=(herm(j[mu],Qm[a],cov[nu],D)+herm(psi,Qm[a],dv[nu],D)).real
        dV=-M(M(V,dE,mm),V,mm)
        b=sum(1j*(sm(dV[:,nu,a],mv(Km[a],cov[nu]))+sm(V[:,nu,a],mv(Km[a],dv[nu]))) for nu in range(4) for a in range(4))
        b=b-sm(bg.dh[mu],mv(Ym,psi))-sm(bg.h,mv(Ym,j[mu]))
        for a2 in range(4):
            G[:,a2]+=sum(M(V[:,mu,a],herm(psi,Qm[a2],mv(Ha[a],b),D)) for a in range(4)).real
        C[:,mu]=(-.5*M(bg.dh[mu],herm(psi,Zm,psi,D))-M(bg.h,herm(psi,Zm,j[mu],D))).real
    return np.concatenate([F.real,F.imag,G,C],axis=1)
def load_germ(Dir,D,fourth='fifth'):
    """Keim bis Grad min(D,5) als (nM(D),12) komplex; fourth='omega' nimmt den alten (nicht reparierten) Grad 4 ohne Grad 5."""
    Dir=Path(Dir);rd=lambda f:json.loads((Dir/f).read_text())
    f70=rd('precision-first-jet-70.json');root=rd('precision-completed-root-result.json');sec=rd('precision-second-jet-result.json')
    om=rd('precision-omega-repair-result.json');fi=rd('precision-fifth-gate-repair-result.json')
    psi=np.zeros((len(monos(D)),12),dtype=complex);I=index(D);psi[0]=[complex(float(a),float(b)) for a,b in f70['psi']]
    lv=[(1,root['first_derivatives_real_packed']),(2,sec['second_coefficients_real_packed']),(3,om['third_coefficients_real_packed'])]
    lv+=[(4,fi['fourth_coefficients_real_packed']),(5,fi['fifth_coefficients_real_packed'])] if fourth=='fifth' else [(4,om['fourth_coefficients_real_packed'])]
    for dg,packed in lv:
        if dg>D: continue
        vals=[float(v) for v in packed]
        for i,c in enumerate(itertools.combinations_with_replacement(range(4),dg)):
            a=tuple(c.count(m) for m in range(4));psi[I[a]]=np.array(vals[i*24:i*24+12])+1j*np.array(vals[i*24+12:i*24+24])
    return [float(s.Rational(v)) for v in f70['point']],psi
