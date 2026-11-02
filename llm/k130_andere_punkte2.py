import sys,numpy as np
exec(open('k127_symbol_frei.py').read().split("rng=np.random.default_rng(0)")[0])
def Rfull(u,p):
    psi=u[96:108]+1j*u[108:120];return R(u[:96],psi,p)[0]
def jac(u,p,e=1e-7): return np.column_stack([(Rfull(u+e*np.eye(120)[k],p)-Rfull(u-e*np.eye(120)[k],p))/(2*e) for k in range(120)])
def solve(u,p):
    for it in range(60):
        r=Rfull(u,p)
        if np.max(abs(r))<1e-12: break
        u=u-np.linalg.lstsq(jac(u,p),r,rcond=1e-10)[0]
    return u,np.max(abs(Rfull(u,p)))
u0=np.r_[j0,psi0.real,psi0.imag]
print('Keim:',np.max(abs(Rfull(u0,p0))))
for label,p in [('z=0, Nachbarpunkt',[1.02,0.6,0.03,0]),('z=0.02',[1,0.6,0,0.02]),('z=0.1',[1,0.6,0,0.1]),('z=0.1, y=0.05',[1.03,0.58,0.05,0.1]),('z=-0.2',[1,0.6,0,-0.2])]:
    # Fortsetzung in kleinen Schritten vom Keim aus
    u=u0.copy();ok=True
    for lam in np.linspace(0,1,11)[1:]:
        q=[a+lam*(b-a) for a,b in zip(p0,p)];u,res=solve(u,q)
        if res>1e-9: ok=False;break
    if not ok: print(f'{label:20s} Fortsetzung bricht ab bei lam={lam:.1f} (Residuum {res:.1e})');continue
    psi=u[96:108]+1j*u[108:120];jv=u[:96];cov=R(jv,psi,p)[1];J=symbol(jv,psi,p)
    vals=[max(np.linalg.norm(J[24:,m*24:(m+1)*24]@rv(cov[n])) for m in range(4)) for n in range(4)]
    print(f'{label:20s} Residuum {res:.1e} | G,dg auf D_t,D_x,D_y,D_z Psi:',' '.join(f'{v:.1e}' for v in vals))
