"""k135: Test H50 (Vorab-Notiz ea36f39). Reagiert Omega in niedriger Ordnung auf Verschiebungen von Psi entlang der theta-Richtung?"""
import sys,time,json,numpy as np
from pathlib import Path
from k135_tps import *
D=Path(sys.argv[1]);p0,psi4=load_germ(D);bg=Background(p0)
def pack(ps4): return np.concatenate([np.r_[ps4[i].real,ps4[i].imag] for i in range(70)])
def unpack(v): return np.array([v[i*24:i*24+12]+1j*v[i*24+12:i*24+24] for i in range(70)])
u0=pack(psi4);e=1e-3;t0=time.time()
import os
if os.path.exists('k135_jac5.npy'): Jac=np.load('k135_jac5.npy')
else:
    Jac=np.zeros((35*32,70*24))
    for k in range(70*24):
        du=np.zeros_like(u0);du[k]=e
        f=lambda h: Rseries(unpack(u0+h*du),bg).ravel()
        Jac[:,k]=(-f(2)+8*f(1)-8*f(-1)+f(-2))/(12*e)
    np.save('k135_jac5.npy',Jac)
print('Jacobi (5-Punkt)',round(time.time()-t0),'s',flush=True)
deg=lambda i: sum(M3[i]) if i<35 else 4
rows=lambda ds: [r*32+q for r in range(35) for q in range(32) if sum(M3[r]) in ds]
cols=lambda ds: [c*24+q for c in range(70) for q in range(24) if sum(M4[c]) in ds]
R3,Rlow=rows([3]),rows([0,1,2]);C4,Clow=cols([4]),cols([0,1,2,3])
M4s=Jac[np.ix_(R3,C4)];U,sv,_=np.linalg.svd(M4s);gaps=sv[400:639]/sv[401:640];r4=int(400+np.argmax(gaps)+1);L=U[:,r4:]
print('M4 Spektrum um die Grenze:',np.array2string(sv[r4-3:r4+3],precision=2))
print('Grad-4-Symbol: Rang',r4,'Linkskern',L.shape[1],'Luecke',f'{sv[r4-1]:.1e}|{sv[r4]:.1e}')
g=L.T@Jac[np.ix_(R3,Clow)]                       # Gradienten der Linkskern-Paarungen nach Jets <=3
Al=Jac[np.ix_(Rlow,Clow)];Ua,sa,Vat=np.linalg.svd(Al);ra=int(sum(sa>sa[0]*1e-9));Row=Vat[:ra];Ker=Vat[ra:].T
print('A_low: Rang',ra,'Kern',Ker.shape[1],'Luecke',f'{sa[ra-1]:.1e}|{sa[ra]:.1e}')
gp=g-(g@Row.T)@Row
ug,sg,vgt=np.linalg.svd(gp);print('projizierte Gradienten, Singulaerwerte:',np.array2string(sg[:4],precision=2))
valid_rank=sg[1]<sg[0]*1e-3;dOm=vgt[0]
# Vergleich Grad-3-Anteil mit gespeichertem theta (modulo Grad-3-Symbolzeilen)
th=np.load(D/'completion-omega-witness.npz')['theta_normalized']
c3=[i for i,a in enumerate(M4) if sum(a)==3];top=np.concatenate([dOm[ (I3[M4[i]])*24:(I3[M4[i]])*24+24] for i in c3])
import itertools
order3=[tuple(c.count(m) for m in range(4)) for c in itertools.combinations_with_replacement(range(4),3)]
thm=np.concatenate([th[order3.index(M4[i])*24:order3.index(M4[i])*24+24] for i in c3])
S3=Jac[np.ix_(rows([2]),[c*24+q for c in c3 for q in range(24)])]
def resid(B,v): return np.linalg.norm(v-B@np.linalg.lstsq(B,v,rcond=1e-10)[0])/np.linalg.norm(v)
with_th=resid(np.column_stack([S3.T,thm]),top);without=resid(S3.T,top)
print(f'Grad-3-Anteil von dOmega: Rest mit theta {with_th:.1e}, ohne theta {without:.1e}')
valid_theta=with_th<1e-3*max(without,1e-30) and without>1e-3
# Testvektoren
def field(cvec_expr):
    return [taylor(s.sympify(ce),p0,3) if ce!=0 else np.zeros(35,dtype=complex) for ce in cvec_expr]
fields={'theta':field([0,-z*x/rho,-z*y/rho,rho]),'d_t':field([1,0,0,0]),'d_x':field([0,1,0,0]),'d_y':field([0,0,1,0])}
dpsi=[d4to3(psi4,m) for m in range(4)]
res={}
for name,cf in fields.items():
    cd=sum(mul(cf[m],dpsi[m],lambda a,b:a*b) for m in range(4))
    rs=[]
    for i,a in enumerate(M3):
        f=np.zeros(35,dtype=complex);f[i]=1;dv=mul(f,cd,lambda a_,b_:a_*b_)
        v=np.concatenate([np.r_[dv[I3[M4[k]]].real,dv[I3[M4[k]]].imag] for k in range(35)])
        pk=Ker@(Ker.T@v);nk=np.linalg.norm(pk)
        rs.append(abs(dOm@v)/nk if nk>1e-9*np.linalg.norm(v) else 0.)
    res[name]=rs;print(f'{name:6s} max_f r = {max(rs):.2e}   je Grad von f:',[f'{max(r for r,a in zip(rs,M3) if sum(a)==d):.1e}' for d in range(4)],flush=True)
ctrl_ok=all(max(res[n])>=1e-2 for n in ('d_t','d_x','d_y'));rt=max(res['theta'])
print('Gueltigkeit: Rang1',valid_rank,'| theta-Abgleich',valid_theta,'| Kontrollen',ctrl_ok)
verdict='UNENTSCHIEDEN'
if valid_rank and valid_theta and ctrl_ok:
    verdict='BESTAETIGT (zweite Klasse)' if rt>=1e-3 else 'WIDERLEGT (erste Klasse bis Ordnung 3)' if rt<=1e-6 else 'UNENTSCHIEDEN'
print('Kriterium:',verdict)
json.dump({'rank_M4':r4,'left_kernel':L.shape[1],'rank_Alow':ra,'proj_sv':sg[:4].tolist(),'theta_check':[with_th,without],'r':{k:v for k,v in res.items()},'verdict':verdict},open('k135_out.json','w'),indent=1)
