"""k169 (H68): Erfuellt der Hintergrund A = M(t) dphi, h(t,r) kovariante Feldgleichungen mit den Spinorbloecken als Quelle?
Yang-Mills auf k = span(l2,l4,l6) in der Koframe-Metrik g = E^T eta E, Quelle j^nu_b = V^nu_a Psi^+(l_b (x) K_a)Psi;
Klein-Gordon fuer h mit Quelle s = Psi^+(Y (x) beta)Psi. Reihen bis Grad 2 um den Keim (k138, reparierter 4-Jet).
Aufruf: python k169_feldgleichungen.py <Keim-Ordner> [json-Ausgabe]"""
import sys,json,itertools,numpy as np,sympy as s
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import k138_tps_d as T
D=2;DE=D+1          # Gleichungen bis Grad 2, Koframe bis Grad 3
p,psi=T.load_germ(sys.argv[1],DE+1)
bg=T.Background(p,DE)
n=lambda d:len(T.monos(d))
M=lambda a,b,op=np.multiply,d=DE:T.mul(a,b,d,op)
mm=T.mm
# --- Kontrolle: Keimresiduum
R=T.Rseries(T.trunc(psi,3),T.Background(p,2));resR=float(np.abs(R).max())
# --- Koframe E bis Grad 3
ps=T.trunc(psi,DE);j=[T.deriv(psi,m,DE) for m in range(4)]
cov=[j[m]+1j*M(bg.conn[m],ps,T.mv) for m in range(4)]
E=np.zeros((n(DE),4,4))
for a in range(4):
    for m in range(4): E[:,a,m]=T.herm(ps,T.Qm[a],cov[m],DE).real
def inv(Ms,d):
    V0=np.linalg.inv(Ms[0]);Nn=Ms.copy();Nn[0]=0;V=np.zeros_like(Ms);V[0]=V0;term=V.copy()
    for k in range(d):
        term=-np.einsum('ij,njk->nik',V0,T.mul(Nn,term,d,mm));V=V+term
    return V
def det4(Ms,d):
    out=np.zeros(Ms.shape[0])
    for perm in itertools.permutations(range(4)):
        sg=np.linalg.det(np.eye(4)[list(perm)]);t=Ms[:,0,perm[0]]
        for r in range(1,4): t=T.mul(t,Ms[:,r,perm[r]],d)
        out=out+sg*t
    return out
eta=np.diag([1.,-1,-1,-1])
u=s.symbols('u')
def geometry(flat):
    if flat:
        gi=np.zeros((n(DE),4,4));gi[0]=eta;sq=np.zeros(n(DE));sq[0]=1.0;isq=sq.copy();V=None
    else:
        V=inv(E,DE)                                  # V[mu,a] = V^mu_a
        gi=np.einsum('nma,ab,kb->nmk',V,eta,V) if False else None
        Vt=np.transpose(V,(0,2,1))
        gi=M(M(V,np.broadcast_to(eta,V.shape)*(np.arange(n(DE))==0)[:,None,None],mm),Vt,mm)
        dt=det4(E,DE);sgn=np.sign(dt[0])
        sq=T.compose(s.sqrt(u),u,sgn*dt,DE);isq=T.compose(1/s.sqrt(u),u,sgn*dt,DE)
    return V,gi,sq,isq
# Farbteil der Verbindung (3x3) bis Grad 3, Ableitungen bis Grad 3
A=[c[:,0::4,0::4] for c in bg.conn];dA=[[bg.dc[mu][nu][:,0::4,0::4] for nu in range(4)] for mu in range(4)]
com=lambda X,Y,d=DE:T.mul(X,Y,d,mm)-T.mul(Y,X,d,mm)
Fl=[[dA[m][k]-dA[k][m]+1j*com(A[m],A[k]) for k in range(4)] for m in range(4)]   # F_{mu nu} Grad 3
l=np.zeros((9,3,3),dtype=complex)
l[2][0,1]=-1j;l[2][1,0]=1j;l[4][0,2]=l[4][2,0]=1;l[6][1,2]=l[6][2,1]=1
l[1][0,1]=l[1][1,0]=1;l[3]=np.diag([1,-1,0]);l[5][0,2]=-1j;l[5][2,0]=1j;l[7][1,2]=-1j;l[7][2,1]=1j;l[8]=np.diag([1,1,-2])/np.sqrt(3);l[0]=np.eye(3)*np.sqrt(2/3)
tr=lambda b,X:np.einsum('ij,nji->n',l[b],X)
k4=[np.eye(4)]+T.al
def run(flat):
    V,gi,sq,isq=geometry(flat)
    # F^{mu nu} und X^{mu nu} = sqrt|g| F^{mu nu}
    Fu=[[sum(M(M(gi[:,m,a],gi[:,k,b]),Fl[a][b],lambda x,y:x[...,None,None]*y) for a in range(4) for b in range(4)) for k in range(4)] for m in range(4)]
    X=[[M(sq,Fu[m][k],lambda x,y:x[...,None,None]*y) for k in range(4)] for m in range(4)]
    sL=[sum(T.deriv(X[m][k],m,D) for m in range(4))+1j*T.trunc(M(sq,sum(com(A[m],Fu[m][k]) for m in range(4)),lambda x,y:x[...,None,None]*y),D) for k in range(4)]   # sqrt|g| L^nu, Grad 2
    L=[T.mul(T.trunc(isq,D),sL[k],D,lambda x,y:x[...,None,None]*y) for k in range(4)]
    # Bianchi-Kontrolle bis Grad 1
    bi=sum(T.deriv(sL[k],k,D-1) for k in range(4))+1j*sum(T.trunc(com(T.trunc(A[k],D),sL[k],D),D-1) for k in range(4))
    bia=float(np.abs(bi).max()/max(np.abs(T.trunc(sL[0],D-1)).max(),1e-300))
    # Stroeme j^nu_b (Grad 2)
    cur={}
    for b in range(9):
        ja=np.stack([T.herm(ps,np.kron(l[b],k4[a]),ps,DE).real for a in range(4)],-1)   # Psi^+(l_b x K_a)Psi
        if flat: jn=ja@eta*0+ja      # flache Basis: j^mu = j^a (Koordinaten = Bezugsframe)
        else: jn=np.stack([sum(M(V[:,mu,a],ja[:,a]) for a in range(4)) for mu in range(4)],-1)
        cur[b]=T.trunc(jn,D)
    Lb={b:np.stack([tr(b,L[k]).real for k in range(4)],-1) for b in range(9)}
    imL=max(float(np.abs(np.stack([tr(b,L[k]).imag for k in range(4)])).max()) for b in range(9))
    # Fit Yang-Mills auf k
    lhs=np.concatenate([Lb[b].ravel() for b in (2,4,6)]);rhs=np.concatenate([cur[b].ravel() for b in (2,4,6)])
    kap=float(lhs@rhs/(rhs@rhs));rA=float(np.linalg.norm(lhs-kap*rhs)/np.linalg.norm(lhs))
    degs=T.deg(D);perdeg={}
    for d in range(D+1):
        sel=degs==d;lh=np.concatenate([Lb[b][sel].ravel() for b in (2,4,6)]);rh=np.concatenate([cur[b][sel].ravel() for b in (2,4,6)])
        kd=float(lh@rh/(rh@rh));perdeg[d]=dict(kappa=kd,r=float(np.linalg.norm(lh-kd*rh)/np.linalg.norm(lh)),r_global=float(np.linalg.norm(lh-kap*rh)/np.linalg.norm(lh)))
    # Grad 0 Komponentenweise
    g0={f'l{b}':dict(L=[float(v) for v in Lb[b][0]],j=[float(v) for v in cur[b][0]]) for b in range(9)}
    # Klein-Gordon
    h=bg.h;dh=bg.dh            # h Grad 3, dh Grad 3
    Pi=[M(sq,sum(M(gi[:,m,k],dh[k]) for k in range(4))) for m in range(4)]
    box=T.mul(T.trunc(isq,D),sum(T.deriv(Pi[m],m,D) for m in range(4)),D)
    sY=T.trunc(T.herm(ps,T.Ym,ps,DE).real,D);hh=T.trunc(h,D)
    kh=float(box@sY/(sY@sY));rB=float(np.linalg.norm(box-kh*sY)/np.linalg.norm(box))
    Aq=np.stack([hh,sY],1);sol,*_=np.linalg.lstsq(Aq,box,rcond=None);rC=float(np.linalg.norm(box-Aq@sol)/np.linalg.norm(box))
    kgdeg={d:dict(box=[float(v) for v in box[degs==d]],s=[float(v) for v in sY[degs==d]]) for d in range(D+1)}
    return dict(bianchi_rel=bia,imag_L=imL,YM=dict(kappa=kap,r=rA,per_degree=perdeg,norm_L=float(np.linalg.norm(lhs)),norm_j=float(np.linalg.norm(rhs))),
                outside_k={f'l{b}':float(np.linalg.norm(cur[b])) for b in (0,1,3,5,7,8)},grad0=g0,
                KG0=dict(kappa=kh,r=rB),KG1=dict(m2=-float(sol[0]),kappa=float(sol[1]),r=rC),KG_terms=kgdeg)
# Kontrolle flaches Box h exakt
t,x,y,z=s.symbols('t x y z',real=True);rho=s.sqrt(x**2+y**2);th=s.asin(t/2)/2
hm=1/s.sqrt(1-(x**2+y**2+z**2)/t**2)/s.cos(2*th);sub=dict(zip((t,x,y,z),[s.nsimplify(v) for v in p]))
boxex=float(s.N((s.diff(hm,t,2)-s.diff(hm,x,2)-s.diff(hm,y,2)-s.diff(hm,z,2)).subs(sub),30))
out=dict(point=p,germ_residual=resR,induced=run(False),flat=run(True),box_h_flat_exact=boxex)
out['box_h_flat_series']=out['flat']['KG_terms'][0]['box'][0]
txt=json.dumps(out,indent=1);(Path(sys.argv[2]) if len(sys.argv)>2 else Path('k169_out.json')).write_text(txt)
for k in ('induced','flat'):
    o=out[k];print(k,'bianchi',f"{o['bianchi_rel']:.1e}",'imL',f"{o['imag_L']:.1e}",'| YM kappa',f"{o['YM']['kappa']:.6g}",'r',f"{o['YM']['r']:.3e}",
      '| per Grad',{d:(round(v['kappa'],5),f"{v['r']:.2e}") for d,v in o['YM']['per_degree'].items()})
    print('   KG0 kappa',f"{o['KG0']['kappa']:.6g}",'r',f"{o['KG0']['r']:.3e}",'| KG1 m2',f"{o['KG1']['m2']:.6g}",'kappa',f"{o['KG1']['kappa']:.6g}",'r',f"{o['KG1']['r']:.3e}")
    print('   ausserhalb k |j|:',{a:f'{v:.3g}' for a,v in o['outside_k'].items()})
print('Keimresiduum',f"{resR:.1e}",' Box h flach exakt',boxex,' Reihe',out['box_h_flat_series'])
