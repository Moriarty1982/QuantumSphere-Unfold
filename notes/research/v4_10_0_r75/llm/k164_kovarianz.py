"""k164 (H64): Kovarianz der Konstruktion R (k127) unter linearer Koordinatenaenderung M und innerer Lorentz-Transformation S.
Aufruf: python k164_kovarianz.py <Keim-Ordner> <Pfad zu k127_symbol_frei.py>"""
import sys,json,numpy as np,scipy.linalg as sl
from pathlib import Path
D=Path(sys.argv[1]);src=open(sys.argv[2]).read().split("J0=symbol(j0,psi0,p0)")[0];sys.argv=[sys.argv[2],str(D)];exec(src)
def Rb(jv,psi,bg):
    conn,dc,h,dh=bg;j=[jv[m*24:m*24+12]+1j*jv[m*24+12:m*24+24] for m in range(4)]
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
    return np.r_[rv(F),G,C]
def symb(jv,psi,bg,e=1e-5): return np.column_stack([(Rb(jv+e*np.eye(96)[k],psi,bg)-Rb(jv-e*np.eye(96)[k],psi,bg))/(2*e) for k in range(96)])
bg0=([np.kron(np.array(M,dtype=complex),np.eye(4)) for M in fconn(*p0)],[[np.kron(np.array(M,dtype=complex),np.eye(4)) for M in row] for row in fdc(*p0)],fh(*p0),np.array(fdh(*p0),dtype=float))
J0=symb(j0,psi0,bg0);print('Abgleich mit gespeichertem J:',f"{np.max(abs(J0-w['completed_first_symbol']))/np.max(abs(J0)):.1e}")
sig=[sx,sy,sz];Sig=[np.block([[s_,Z2],[Z2,s_]]) for s_ in sig]
def spinor(rot,boost): return sl.expm(sum(-0.5j*rot[k]*Sig[k]+0.5*boost[k]*al[k] for k in range(3)))
def transform(M,S4,tbg=True):
    Mi=np.linalg.inv(M);S=np.kron(np.eye(3),S4)          # d'_m = sum_n Mi[n,m] d_n
    conn,dc,h,dh=bg0
    if tbg:
        conn2=[sum(Mi[n,m]*conn[n] for n in range(4)) for m in range(4)]
        dc2=[[sum(Mi[a,mu]*Mi[b,nu]*dc[a][b] for a in range(4) for b in range(4)) for nu in range(4)] for mu in range(4)]
        dh2=Mi.T@dh
    else: conn2,dc2,dh2=conn,dc,dh
    def Lj(jv):
        j=[jv[m*24:m*24+12]+1j*jv[m*24+12:m*24+24] for m in range(4)];j2=[sum(Mi[n,m]*S@j[n] for n in range(4)) for m in range(4)]
        return np.concatenate([rv(v) for v in j2])
    L=np.column_stack([Lj(np.eye(96)[k]) for k in range(96)])
    return S@psi0,(conn2,dc2,h,dh2),L
def res(M,S4,tbg=True):
    psi2,bg2,L=transform(M,S4,tbg);J2=symb(L@j0,psi2,bg2);T=J2@L
    out={}
    for name,rows in (('F',slice(0,24)),('G',slice(24,28)),('dg',slice(28,32))):
        X=T[rows];C=X@np.linalg.pinv(J0,rcond=RC);out[name]=np.linalg.norm(X-C@J0)/np.linalg.norm(X)
    return out
RC=float(__import__('os').environ.get('QS_RCOND','1e-15'));_sv=np.linalg.svd(J0,compute_uv=False)/np.linalg.svd(J0,compute_uv=False)[0];print('Singulaerwerte J0 (relativ), kleinste 3:',np.array2string(_sv[-3:],precision=1),' rcond',RC)
rng=np.random.default_rng(64);M=np.eye(4)+0.3*rng.normal(size=(4,4));S4=spinor(0.7*rng.normal(size=3),0.5*rng.normal(size=3))
fmt=lambda d:'  '.join(f'{k} {v:.1e}' for k,v in d.items())
print('Kontrolle positiv (M=1,S=1):',fmt(res(np.eye(4),np.eye(4))))
print('Kontrolle negativ (a ohne Hintergrund):',fmt(res(M,np.eye(4),tbg=False)))
print('(a) Koordinaten M:',fmt(res(M,np.eye(4))))
print('(b) innere Lorentz S:',fmt(res(np.eye(4),S4)))
print('(c) beides:',fmt(res(M,S4)))
print('Zusatz: S nur Drehung:',fmt(res(np.eye(4),spinor(0.7*rng.normal(size=3),np.zeros(3)))),' | S nur Boost:',fmt(res(np.eye(4),spinor(np.zeros(3),0.5*rng.normal(size=3)))))
print('Zusatz: Rang J0 =',np.linalg.matrix_rank(J0,1e-8*np.linalg.norm(J0)))
