import sys,numpy as np
src=open('k133_test_h49.py').read().split("u0=np.r_[j0")[0];exec(src)
u0=np.r_[j0,psi0.real,psi0.imag];p=[1,0.6,0,0.1];u=u0.copy()
for lam in np.linspace(0,1,11)[1:]: u,res=solve(u,[a+lam*(b-a) for a,b in zip(p0,p)])
jv=u[:96];psi=u[96:108]+1j*u[108:120];Rp,Rpsi,J=pieces(jv,psi,p)
def kap(b):
    M=np.zeros((128,240))
    for mu in range(4):
        for nu in range(4):
            k=pairs.index(tuple(sorted((mu,nu))));M[mu*32:(mu+1)*32,k*24:(k+1)*24]+=J[:,nu*24:(nu+1)*24]
    U,s,_=np.linalg.svd(M);L=U[:,113:];return np.linalg.norm(L.T@b)/np.linalg.norm(b)
b=np.concatenate([Rp[:,m]+Rpsi@jv[m*24:(m+1)*24] for m in range(4)])
b1=np.concatenate([Rpsi@jv[m*24:(m+1)*24] for m in range(4)])            # expliziter Hintergrund-Gradient weggelassen
b2=np.concatenate([Rp[:,m]+Rpsi@jv[m*24:(m+1)*24] for m in range(4)]);b2[np.arange(4)*32+30]*=1.001  # 1e-3 Fehler in einer Zeile
print(f'echt: {kap(b):.1e} | ohne Hintergrund-Gradient: {kap(b1):.1e} | 0.1% Fehler in einer dg-Zeile: {kap(b2):.1e}')
