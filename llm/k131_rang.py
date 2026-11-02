import sys,numpy as np
exec(open('k130_andere_punkte2.py').read().split("u0=np.r_")[0])
u0=np.r_[j0,psi0.real,psi0.imag];rng=np.random.default_rng(2)
for label,p in [('z=0 (Keim)',p0),('z=0, Nachbarpunkt',[1.02,0.6,0.03,0]),('z=0.02',[1,0.6,0,0.02]),('z=0.1',[1,0.6,0,0.1]),('z=-0.2',[1,0.6,0,-0.2])]:
    u=u0.copy()
    for lam in np.linspace(0,1,11)[1:]:
        u,res=solve(u,[a+lam*(b-a) for a,b in zip(p0,p)])
    psi=u[96:108]+1j*u[108:120];J=symbol(u[:96],psi,p)
    sv=[np.linalg.svd(sum(xi[m]*J[:,m*24:(m+1)*24] for m in range(4)),compute_uv=False)[-3:] for xi in rng.normal(size=(3,4))]
    print(f'{label:20s} kleinste Singulaerwerte von J(xi), 3 zufaellige xi:',' | '.join(np.array2string(s,precision=1) for s in sv))
