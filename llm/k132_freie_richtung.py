import sys,numpy as np
exec(open('k130_andere_punkte2.py').read().split("u0=np.r_")[0])
u0=np.r_[j0,psi0.real,psi0.imag];rng=np.random.default_rng(2);np.set_printoptions(precision=4,suppress=True)
for label,p in [('z=0 (Keim)',p0),('z=0.1',[1,0.6,0,0.1]),('z=-0.2',[1,0.6,0,-0.2]),('z=0.1,y=0.05,t=1.03',[1.03,0.58,0.05,0.1])]:
    u=u0.copy()
    for lam in np.linspace(0,1,11)[1:]: u,res=solve(u,[a+lam*(b-a) for a,b in zip(p0,p)])
    psi=u[96:108]+1j*u[108:120];jv=u[:96];J=symbol(jv,psi,p);cov=R(jv,psi,p)[1]
    B=np.column_stack([rv(c) for c in cov]);E=np.array([[np.real(psi.conj()@Q[a]@cov[m]) for m in range(4)] for a in range(4)])
    print(label)
    for xi in rng.normal(size=(3,4)):
        k=np.linalg.svd(sum(xi[m]*J[:,m*24:(m+1)*24] for m in range(4)))[2][-1]
        cvec,res_,_,_=np.linalg.lstsq(B,k,rcond=None);inB=np.linalg.norm(B@cvec-k)
        cvec/=np.linalg.norm(cvec)*np.sign(cvec[np.argmax(abs(cvec))])
        print('   in Bild B (Diffeo)? Rest',f'{inB:.1e}','  Richtung c =',cvec,'  xi.c/|xi| =',f'{xi@cvec/np.linalg.norm(xi):.3f}')
    # dg-Kovektor w und Gradient von h, d(gamma): Vergleich
    print('   e^a (Frame-Vektoren V):\n',np.linalg.inv(E).T[:, :].round(3))
