"""k153: hochgenaue Linearisierung L = A^mu(x) d_mu + B(x) am reparierten Keim (mpmath, punktweise Feldgleichung).
A(x) = dR/d(d Psi), B(x) = dR/dPsi entlang des Keimpolynoms (Grad <= 5, 70 Stellen); Taylor-Koeffizienten in x per
symmetrischen Differenzen. Aufruf: python k153_hp_linear.py <Ordner> <schritt>
schritte: pruef (Grad 0 gegen k142) | punkt <i> (ein Stuetzpunkt der x-Schablone) | taylor (aus allen Stuetzpunkten)"""
import sys,json,itertools,math,pickle,numpy as np,mpmath as mp,sympy as s
from pathlib import Path
here=Path(__file__).parent;D=Path(sys.argv[1]);step=sys.argv[2];mp.mp.dps=160
W=here/'hp_work2';W.mkdir(exist_ok=True)
# --- Hintergrund symbolisch, mpmath-Auswertung
t,x,y,z=s.symbols('t x y z',real=True);X=(t,x,y,z);NN=16
rho=s.sqrt(x**2+y**2);gam=1/s.sqrt(1-(x**2+y**2+z**2)/t**2);th=s.asin(8*t/NN)/2;c,d_,Del=s.cos(th),s.sin(th),s.cos(2*th)
pp=3*c/(2*rho*Del);qq=-3*d_/(2*rho*Del);Gm=s.Matrix([[0,0,pp],[0,0,qq],[pp,qq,0]]);spin=[-y/rho,x/rho,s.Integer(0)];hm=16*gam/(NN*Del)
connS=[s.zeros(3)]+[Gm*sp for sp in spin]
fconn=s.lambdify(X,connS,'mpmath');fdc=s.lambdify(X,[[M.diff(v) for M in connS] for v in X],'mpmath')
fh=s.lambdify(X,hm,'mpmath');fdh=s.lambdify(X,[hm.diff(v) for v in X],'mpmath')
O=lambda a:np.array(a,dtype=object)
sx=O([[0,1],[1,0]]);sy=O([[0,-1j],[1j,0]]);sz=O([[1,0],[0,-1]]);Z2=O([[0,0],[0,0]])
blk=lambda a,b,c_,d:np.block([[a,b],[c_,d]])
al=[blk(Z2,q,q,Z2) for q in (sx,sy,sz)];beta=O(np.diag([1,1,-1,-1]))
S3=O([[0,mp.mpf(1)/2,0],[mp.mpf(1)/2,0,0],[0,0,0]]);Y3=O([[0,-1j,0],[1j,0,0],[0,0,0]]);Z3=O(np.diag([1,-1,0]))
I3=O(np.eye(3,dtype=int));I4=O(np.eye(4,dtype=int))
K=[np.kron(I3,m) for m in [I4]+al];Q=[np.kron(S3,m) for m in [I4]+al];Y=np.kron(Y3,beta);Zm=np.kron(Z3,beta)
def mpc_arr(a): return np.vectorize(lambda v:mp.mpc(v),otypes=[object])(a)
K=[mpc_arr(k) for k in K];Q=[mpc_arr(q) for q in Q];Y=mpc_arr(Y);Zm=mpc_arr(Zm)
Hb=[-1j*K[0]]+[1j*k for k in K[1:]]
re=np.vectorize(lambda v:mp.re(v),otypes=[object]);im=np.vectorize(lambda v:mp.im(v),otypes=[object]);cj=np.vectorize(lambda v:mp.conj(v),otypes=[object])
def kron4(M):
    rows=[[M[i,k] for k in range(3)] for i in range(3)] if hasattr(M,'rows') else M
    return np.kron(mpc_arr(O(rows)),I4)
def R(jv,psi,p):
    """punktweise (F, G, dg) wie k127, in mpmath. jv: 96 reell, psi: 12 komplex, p: Punkt."""
    conn=[kron4(M) for M in fconn(*p)];dc=[[kron4(M) for M in row] for row in fdc(*p)]
    h=fh(*p);dh=fdh(*p)
    j=[O([mp.mpc(jv[m*24+k],jv[m*24+12+k]) for k in range(12)]) for m in range(4)]
    cov=[j[m]+1j*(conn[m]@psi) for m in range(4)]
    E=mp.matrix(4,4)
    for a in range(4):
        for m in range(4): E[a,m]=mp.re(cj(psi)@(Q[a]@cov[m]))
    V=E**-1;Vn=np.array([[V[i,k] for k in range(4)] for i in range(4)],dtype=object)
    A=[[mp.re(v) for v in (cj(psi)@q)]+[-mp.im(v) for v in (cj(psi)@q)] for q in Q]
    F=sum(1j*Vn[m,a]*(K[a]@cov[m]) for m in range(4) for a in range(4))-h*(Y@psi)
    G=[mp.mpf(0)]*4;C=[mp.mpf(0)]*4
    for mu in range(4):
        dv=[1j*(dc[mu][nu]@psi+conn[nu]@j[mu]) for nu in range(4)]
        dE=mp.matrix(4,4)
        for a in range(4):
            for nu in range(4): dE[a,nu]=mp.re(cj(j[mu])@(Q[a]@cov[nu])+cj(psi)@(Q[a]@dv[nu]))
        dVm=-(V*dE*V);dV=np.array([[dVm[i,k] for k in range(4)] for i in range(4)],dtype=object)
        b=sum(1j*(K[a]@(dV[nu,a]*cov[nu]+Vn[nu,a]*dv[nu])) for nu in range(4) for a in range(4))-dh[mu]*(Y@psi)-h*(Y@j[mu])
        rb=list(re(b))+list(im(b))
        km=[sum(A[a2][k]*sum(Vn[mu,a]*_hb(a,k,rb) for a in range(4)) for k in range(24)) for a2 in range(4)]
        for a2 in range(4): G[a2]+=km[a2]
        C[mu]=-mp.mpf(1)/2*dh[mu]*mp.re(cj(psi)@(Zm@psi))-h*mp.re(cj(psi)@(Zm@j[mu]))
    return list(re(F))+list(im(F))+G+C
_HBR=None
def _hb(a,k,rb):
    """(realmat(Hb[a]) @ rb)[k]"""
    global _HBR
    if _HBR is None:
        _HBR=[]
        for H in Hb:
            Hr=np.empty((24,24),dtype=object);Hr[:12,:12]=re(H);Hr[:12,12:]=-im(H);Hr[12:,:12]=im(H);Hr[12:,12:]=re(H);_HBR.append(Hr)
    return sum(_HBR[a][k,l]*rb[l] for l in range(24))
# --- Keim (70 Stellen) als Polynom
rd=lambda f:json.loads((D/f).read_text())
f70=rd('precision-first-jet-70.json');root=rd('precision-completed-root-result.json');sec=rd('precision-second-jet-result.json');om=rd('precision-omega-repair-result.json');fi=rd('precision-fifth-gate-repair-result.json')
P0=[mp.mpf(s.Rational(v).p)/s.Rational(v).q for v in f70['point']]
coef={(0,0,0,0):O([mp.mpc(a,b) for a,b in f70['psi']])}
for dg,packed in [(1,root['first_derivatives_real_packed']),(2,sec['second_coefficients_real_packed']),(3,om['third_coefficients_real_packed']),(4,fi['fourth_coefficients_real_packed']),(5,fi['fifth_coefficients_real_packed'])]:
    for i,cc in enumerate(itertools.combinations_with_replacement(range(4),dg)):
        a=tuple(cc.count(m) for m in range(4));coef[a]=O([mp.mpc(packed[i*24+k],packed[i*24+12+k]) for k in range(12)])
def jet(dx,maxdeg=5):
    """Psi und d_mu Psi am Punkt P0+dx aus dem Keimpolynom."""
    ps=O([mp.mpc(0)]*12);dps=[O([mp.mpc(0)]*12) for _ in range(4)]
    for a,cv in coef.items():
        if sum(a)>maxdeg: continue
        ps=ps+cv*mp.fprod(dx[m]**a[m] for m in range(4))
        for mu in range(4):
            if a[mu]==0: continue
            b=list(a);b[mu]-=1;dps[mu]=dps[mu]+cv*a[mu]*mp.fprod(dx[m]**b[m] for m in range(4))
    jv=[];[jv.extend(list(re(d))+list(im(d))) for d in dps]
    return ps,jv
HJ=mp.mpf('1e-55')
def AB(dx):
    """A (4 x 32 x 24) und B (32 x 24) am Punkt P0+dx; symmetrische Differenzen in den Jet-Variablen."""
    ps,jv=jet(dx);p=[P0[m]+dx[m] for m in range(4)]
    A=np.empty((4,32,24),dtype=object);B=np.empty((32,24),dtype=object)
    for k in range(96):
        jp=list(jv);jm=list(jv);jp[k]+=HJ;jm[k]-=HJ;col=[(u-v)/(2*HJ) for u,v in zip(R(jp,ps,p),R(jm,ps,p))];A[k//24,:,k%24]=col
    for k in range(24):
        e=O([mp.mpc(0)]*12);e[k%12]=mp.mpc(1) if k<12 else mp.mpc(0,1)
        col=[(u-v)/(2*HJ) for u,v in zip(R(jv,ps+HJ*e,p),R(jv,ps-HJ*e,p))];B[:,k]=col
    return A,B
# x-Schablone fuer Taylor bis Grad 3: Punkte h*v mit v in {-2..2}^4, |v|_1 <= 3
HX=mp.mpf('1e-25')
STENCIL=sorted({v for v in itertools.product(range(-2,3),repeat=4) if sum(abs(a) for a in v)<=2})   # Stufe 1: Taylor bis Grad 2
if step=='pruef':
    import time;t0=time.time();A0,B0=AB([mp.mpf(0)]*4);print('A,B am Keim in',f'{time.time()-t0:.0f} s')
    d2=np.load(here/'k142_lin2.npz');Af=np.array(A0.tolist(),dtype=float);Bf=np.array(B0.tolist(),dtype=float)
    print('max|A(0) - k142| =',f"{np.max(abs(Af-d2['A'][:,0])):.1e}",' max|B(0) - k142| =',f"{np.max(abs(Bf-d2['B'].mean(0)[0])):.1e}",' |A|',f'{np.max(abs(Af)):.1e}')
    pickle.dump((A0,B0),open(W/'AB_000.pkl','wb'))
elif step=='punkt':
    i=int(sys.argv[3]);v=STENCIL[i];A,B=AB([HX*v[m] for m in range(4)]);pickle.dump((v,A,B),open(W/f'AB_pt{i:03d}.pkl','wb'));print('Punkt',i,v,'fertig')
elif step=='anzahl': print(len(STENCIL))
elif step=='taylor':
    # Taylor-Koeffizienten bis Grad 2 aus den Stuetzpunkten: Kleinste Quadrate in mpmath (symmetrische Schablone)
    mons=[a for d in range(3) for a in sorted({tuple(c.count(m) for m in range(4)) for c in itertools.combinations_with_replacement(range(4),d)},reverse=True)]
    pts=[pickle.load(open(W/f'AB_pt{i:03d}.pkl','rb')) for i in range(len(STENCIL))]
    M=mp.matrix([[mp.fprod((HX*v[m])**a[m] for m in range(4)) for a in mons] for v,_,_ in pts]);Mp=(M.T*M)**-1*M.T
    Avals=[[mp.matrix([[pt[1][mu,r,c] for pt in pts]]).T for r in range(32) for c in range(24)] for mu in range(4)]
    Ac=np.empty((4,len(mons),32,24),dtype=object);Bc=np.empty((len(mons),32,24),dtype=object)
    for mu in range(4):
        for r in range(32):
            for c_ in range(24):
                col=Mp*mp.matrix([pt[1][mu,r,c_] for pt in pts]);Ac[mu,:,r,c_]=[col[i] for i in range(len(mons))]
    for r in range(32):
        for c_ in range(24):
            col=Mp*mp.matrix([pt[2][r,c_] for pt in pts]);Bc[:,r,c_]=[col[i] for i in range(len(mons))]
    pickle.dump((mons,Ac,Bc),open(W/'AB_taylor2.pkl','wb'))
    d2=np.load(here/'k142_lin2.npz');print('Abgleich mit k142 (float): A',f"{np.max(abs(np.array(Ac.tolist(),dtype=float)-d2['A'][:,:len(mons)])):.1e}",' B',f"{np.max(abs(np.array(Bc.tolist(),dtype=float)-d2['B'].mean(0)[:len(mons)])):.1e}")
