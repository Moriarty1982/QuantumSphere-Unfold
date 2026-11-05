"""k172 (Erkundung, W1): Weyl-Form von k170. Linkshaendiger 2-Spinor, sigma-bar^a = (1, -sigma_i), Spin-Verbindung
Gamma_mu = (1/8) omega_{mu ab}(sigma^a sigmabar^b - sigma^b sigmabar^a). Prueft Im(i psi^+ sigmabar^mu D_mu psi) = 1/2(div j + omega_a^a_b j^b),
j^a = psi^+ sigmabar^a psi, j^0 = psi^+ psi >= 0."""
import numpy as np
rng=np.random.default_rng(2);I=np.eye(2);sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1])
s=[I,sx,sy,sz];sb=[I,-sx,-sy,-sz];eta=np.diag([1.,-1,-1,-1]);worst=0
for _ in range(200):
    p=rng.normal(size=2)+1j*rng.normal(size=2);dp=rng.normal(size=(4,2))+1j*rng.normal(size=(4,2))
    w=rng.normal(size=(4,4,4));w=w-w.transpose(0,2,1);A=rng.normal(size=4)
    G=[sum(w[m,a,b]*(s[a]@sb[b]-s[b]@sb[a]) for a in range(4) for b in range(4))/8 for m in range(4)]
    D=[dp[m]+G[m]@p+1j*A[m]*p for m in range(4)]
    L=sum(p.conj()@(1j*sb[m]@D[m]) for m in range(4))
    j=np.array([(p.conj()@sb[a]@p).real for a in range(4)]);div=sum(2*np.real(p.conj()@sb[m]@dp[m]) for m in range(4))
    tr=sum(eta[a,a]*w[a,a,b]*j[b] for a in range(4) for b in range(4))
    worst=max(worst,min(abs(L.imag-0.5*(div+tr)),abs(L.imag-0.5*(div-tr))));sg='+' if abs(L.imag-0.5*(div+tr))<1e-9 else '-'
print('Weyl: Im L = 1/2(div j',sg,'omega-Spur j), max Residuum',f'{worst:.1e}','; j^0 = |psi|^2 >= 0')
