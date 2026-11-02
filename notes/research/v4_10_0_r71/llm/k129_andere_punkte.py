import sys,numpy as np
exec(open('k128_schale.py').read().split("rng=np.random.default_rng(5)")[0])
rng=np.random.default_rng(9)
cases=[('z=0, anderes Psi',[1,0.6,0,0],psi0*np.exp(0.3j)+0.2*(rng.normal(size=12)+1j*rng.normal(size=12))),
       ('z=0, anderer Punkt',[1.1,0.5,0.1,0],psi0),
       ('z=0.05',[1,0.6,0,0.05],psi0),('z=0.2',[1,0.6,0,0.2],psi0),('z=-0.3, y=0.2',[1.1,0.5,0.2,-0.3],psi0)]
for label,p,psi in cases:
    jv,res=project(j0.copy(),psi,p)
    if res>1e-9: print(f'{label:22s} keine Loesung gefunden (Residuum {res:.1e})');continue
    cov=R(jv,psi,p)[1];J=symbol(jv,psi,p)
    vals=[max(np.linalg.norm(J[24:,m*24:(m+1)*24]@rv(cov[n])) for m in range(4)) for n in range(4)]
    print(f'{label:22s} Residuum {res:.1e} | G,dg auf D_t,D_x,D_y,D_z Psi:',' '.join(f'{v:.1e}' for v in vals))
