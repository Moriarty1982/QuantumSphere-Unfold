"""k133: Test H49 (Vorab-Notiz e2d3394). Vertraeglichkeit der zweiten Ableitungen fuer R=(F,G,dg) am Aequator vs. abseits."""
import sys,json,numpy as np
exec(open('k130_andere_punkte2.py').read().split("u0=np.r_")[0])
def pieces(jv,psi,p,e=1e-6):
    f=lambda jj,ps,pp: R(jj,ps,pp)[0]
    Rp=np.column_stack([(f(jv,psi,np.add(p,e*np.eye(4)[m]))-f(jv,psi,np.subtract(p,e*np.eye(4)[m])))/(2*e) for m in range(4)])
    Rpsi=np.column_stack([(f(jv,psi+e*(np.eye(12)[k] if k<12 else 1j*np.eye(12)[k-12]),p)-f(jv,psi-e*(np.eye(12)[k] if k<12 else 1j*np.eye(12)[k-12]),p))/(2*e) for k in range(24)])
    return Rp,Rpsi,symbol(jv,psi,p,e)
pairs=[(a,b) for a in range(4) for b in range(a,4)]
def kappa(jv,psi,p):
    Rp,Rpsi,J=pieces(jv,psi,p)
    M=np.zeros((128,240));b=np.zeros(128)
    for mu in range(4):
        b[mu*32:(mu+1)*32]=Rp[:,mu]+Rpsi@jv[mu*24:(mu+1)*24]
        for nu in range(4):
            k=pairs.index(tuple(sorted((mu,nu))));M[mu*32:(mu+1)*32,k*24:(k+1)*24]+=J[:,nu*24:(nu+1)*24]
    U,s,_=np.linalg.svd(M);gaps=s[:-1]/s[1:];r=int(np.argmax(gaps[100:125])+101)   # Rang an der groessten Luecke
    L=U[:,r:];kap=np.linalg.norm(L.T@b)/np.linalg.norm(b)
    return kap,r,s[r-1],s[r] if r<len(s) else 0,np.linalg.norm(b)
u0=np.r_[j0,psi0.real,psi0.imag];out=[]
def run(label,p,start=None,kind='Test'):
    u=(start if start is not None else u0).copy()
    for lam in np.linspace(0,1,11)[1:]: u,res=solve(u,[a+lam*(b-a) for a,b in zip(p0,p)])
    psi=u[96:108]+1j*u[108:120];k,r,sl,sn,nb=kappa(u[:96],psi,p)
    row=dict(label=label,kind=kind,point=list(map(float,p)),R_residual=float(res),rank=r,gap=f'{sl:.1e}|{sn:.1e}',kappa=float(k),rhs_norm=float(nb))
    out.append(row);print(f'{kind:9s} {label:28s} Residuum {res:.0e} Rang {r} Luecke {sl:.1e}|{sn:.1e}  kappa = {k:.2e}',flush=True)
    return u
run('Keim',p0,kind='Kontrolle')
run('Nachbar z=0',[1.02,0.6,0.03,0],kind='Kontrolle')
Kn=np.linalg.svd(J0)[2][31:].T;rng=np.random.default_rng(5)
for i,step in enumerate([0.2,0.5]):
    # andere Loesungen am Keimpunkt (psi fest, wie k128), dann ganze Loesung nachziehen
    jv=j0+step*Kn@rng.normal(size=Kn.shape[1])/np.sqrt(Kn.shape[1]);u=np.r_[jv,psi0.real,psi0.imag];u,res=solve(u,p0)
    psi=u[96:108]+1j*u[108:120];k,r,sl,sn,nb=kappa(u[:96],psi,p0)
    out.append(dict(label=f'Keimpunkt, andere Loesung {i+1}',kind='Kontrolle',point=list(map(float,p0)),R_residual=float(res),rank=r,kappa=float(k)))
    print(f'Kontrolle Keimpunkt, andere Loesung {i+1:<9d} Residuum {res:.0e} Rang {r} Luecke {sl:.1e}|{sn:.1e}  kappa = {k:.2e}',flush=True)
for zz in [0.02,0.05,0.1,0.2]: run(f'z={zz}',[1,0.6,0,zz])
run('(1.03,0.58,0.05,0.1)',[1.03,0.58,0.05,0.1])
json.dump(out,open('k133_out.json','w'),indent=1)
ctrl=max(r['kappa'] for r in out if r['kind']=='Kontrolle');test=[r['kappa'] for r in out if r['kind']=='Test' and abs(r['point'][3])>=0.05]
print('max Kontrolle',f'{ctrl:.2e}','| Tests |z|>=0.05:',[f'{v:.2e}' for v in test])
if ctrl<=1e-6 and all(v>=max(100*ctrl,1e-5) for v in test): print('Kriterium: BESTAETIGT')
elif all(v<10*ctrl for v in test): print('Kriterium: WIDERLEGT')
else: print('Kriterium: UNENTSCHIEDEN')
