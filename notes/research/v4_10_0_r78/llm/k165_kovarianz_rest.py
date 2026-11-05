"""k165 (H65): (a) Kovarianz von R auf Werteebene an zufaelligen Daten ausserhalb der Loesungsmenge; (b) Stabilisator der Eichung psi^+ K2 psi in so(1,3).
Aufruf: python k165_kovarianz_rest.py <Keim-Ordner> <Pfad zu k127_symbol_frei.py> <Pfad zu k164_kovarianz.py>"""
import sys,numpy as np,scipy.linalg as sl
D,P127,P164=sys.argv[1:4];src=open(P164).read().split("bg0=(")[0];sys.argv=[P164,D,P127];exec(src)
sig=[sx,sy,sz];Sig=[np.block([[s_,Z2],[Z2,s_]]) for s_ in sig]
gen=[-0.5j*S_ for S_ in Sig]+[0.5*a for a in al]          # Drehungen x,y,z; Boosts x,y,z
spinor=lambda c:sl.expm(sum(c[k]*gen[k] for k in range(6)))
rng=np.random.default_rng(65)
def rand_bg():
    cm=lambda:(lambda X:X-X.T)(rng.normal(size=(3,3)))   # reelle antisymmetrische Farbmatrizen wie G*spin
    conn=[np.kron(cm().astype(complex),np.eye(4)) for _ in range(4)];dc=[[np.kron(cm().astype(complex),np.eye(4)) for _ in range(4)] for _ in range(4)]
    return conn,dc,float(rng.uniform(0.5,2)),rng.normal(size=4)
def tf(M,S4,psi,jv,bg):
    Mi=np.linalg.inv(M);S=np.kron(np.eye(3),S4);conn,dc,h,dh=bg
    conn2=[sum(Mi[n,m]*conn[n] for n in range(4)) for m in range(4)]
    dc2=[[sum(Mi[a,mu]*Mi[b,nu]*dc[a][b] for a in range(4) for b in range(4)) for nu in range(4)] for mu in range(4)]
    def Lj(v):
        j=[v[m*24:m*24+12]+1j*v[m*24+12:m*24+24] for m in range(4)];return np.concatenate([rv(sum(Mi[n,m]*S@j[n] for n in range(4))) for m in range(4)])
    L=np.column_stack([Lj(np.eye(96)[k]) for k in range(96)]);return S@psi,L@jv,(conn2,dc2,h,Mi.T@dh),L
blocks=(('F',slice(0,24)),('G',slice(24,28)),('dg',slice(28,32)))
def test(M,S4,psi,jv,bg):
    J=symb(jv,psi,bg);p2,j2,bg2,L=tf(M,S4,psi,jv,bg);J2=symb(j2,p2,bg2);C=(J2@L)@np.linalg.pinv(J,rcond=1e-6)
    R1=Rb(jv,psi,bg);R2=Rb(j2,p2,bg2);out={}
    for n,r in blocks: out[n]=np.linalg.norm(R2[r]-(C@R1)[r])/max(np.linalg.norm(R2[r]),1e-300)
    return out
fmt=lambda d:'  '.join(f'{k} {v:.1e}' for k,v in d.items())
for i in range(5):
    psi=rng.normal(size=12)+1j*rng.normal(size=12);jv=rng.normal(size=96);bg=rand_bg()
    if i==0: print('Kontrolle positiv:',fmt(test(np.eye(4),np.eye(4),psi,jv,bg)))
    M=np.eye(4)+0.3*rng.normal(size=(4,4));S4=spinor(0.6*rng.normal(size=6))
    print(f'Datensatz {i}:',fmt(test(M,S4,psi,jv,bg)),flush=True)
# (b) Stabilisator der Eichung: Re(psi^+ K2 X psi) = 0 fuer alle psi  <=>  K2 X + X^+ K2 = 0 (hermitesch-antisymmetrisch)
K2=np.kron(np.eye(3),al[1]);Xs=[np.kron(np.eye(3),g) for g in gen]
Mb=np.column_stack([(K2@X+X.conj().T@K2).ravel() for X in Xs]);Mb=np.vstack([Mb.real,Mb.imag])
_,s,Vt=np.linalg.svd(Mb);s=s/s[0];k=int(np.sum(s<1e-12));print('(b) Singulaerwerte:',np.array2string(s,precision=2),' -> Dimension',k)
names=['Drehung x','Drehung y','Drehung z','Boost x','Boost y','Boost z']
for v in Vt[6-k:]: print('    Generator:',' + '.join(f'{c:.2f} {n}' for c,n in zip(v,names) if abs(c)>1e-8))
