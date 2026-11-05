"""k170 (Erkundung, Wirkung W1): punktweise Identitaet fuer den Imaginaerteil der nicht symmetrisierten Dirac-Lagrangedichte
mit unabhaengiger Lorentz-Verbindung omega und U(1)-Potential A:
  Im(Psibar i gamma^mu D_mu Psi) = 1/2 (d_mu j^mu + omega_a^a_b j^b),  j^a = Psibar gamma^a Psi,
D = d + (1/8) omega_{mu ab}[gamma^a,gamma^b] + i q A. Zufallswerte, flacher Tetraden-Punkt (Identitaet algebraisch in e).
Zweitens: das U(1)-Potential faellt aus Im L heraus; drittens: symmetrisierte Kinetik ist reell."""
import numpy as np
rng=np.random.default_rng(1)
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]);Z=np.zeros((2,2));I2=np.eye(2)
be=np.block([[I2,Z],[Z,-I2]]).astype(complex);al=[np.block([[Z,s],[s,Z]]) for s in (sx,sy,sz)]
g=[be]+[be@a for a in al];eta=np.diag([1.,-1,-1,-1])
worst=[0,0,0]
for trial in range(200):
    psi=rng.normal(size=4)+1j*rng.normal(size=4);dpsi=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
    w=rng.normal(size=(4,4,4));w=w-w.transpose(0,2,1)          # omega_{mu a b}, antisymmetrisch in ab (Indizes unten)
    A=rng.normal(size=4);q=rng.normal()
    Gam=[sum(w[m,a,b]*(g[a]@g[b]-g[b]@g[a]) for a in range(4) for b in range(4))/8 for m in range(4)]
    bar=lambda v:v.conj()@be
    D=[dpsi[m]+Gam[m]@psi+1j*q*A[m]*psi for m in range(4)]
    gup=[sum(eta[m,n]*g[n] for n in range(4)) for m in range(4)]   # gamma^mu (oben) = eta^{mu nu} gamma_nu? hier gamma^a schon oben
    L=sum(bar(psi)@(1j*g[m]@D[m]) for m in range(4))
    j=np.array([(bar(psi)@g[a]@psi).real for a in range(4)])
    divj=sum(2*np.real(bar(psi)@g[m]@dpsi[m]) for m in range(4))
    # omega_a^a_b j^b = sum_a eta^{aa} omega_{a a b} j^b  (erster Index = Raumzeitindex mu=a)
    tr=sum(eta[a,a]*w[a,a,b]*j[b] for a in range(4) for b in range(4))   # omega_{a}{}^{a}{}_{b} j^b = eta^{ac} omega_{acb} j^b
    r1=abs(L.imag-0.5*(divj+tr));r1m=abs(L.imag-0.5*(divj-tr))
    # symmetrisiert: 1/2(L + conj-Partner) = Re L
    Ls=0.5*(L+np.conj(L))
    worst=[max(worst[0],min(r1,r1m)),max(worst[1],abs(Ls.imag)),worst[2]]
    sign='+' if r1<r1m else '-'
    # A-Unabhaengigkeit: Im L mit A=0
    D0=[dpsi[m]+Gam[m]@psi for m in range(4)];L0=sum(bar(psi)@(1j*g[m]@D0[m]) for m in range(4))
    worst[2]=max(worst[2],abs(L.imag-L0.imag))
print('Identitaet Im L = 1/2(div j',sign,'omega-Spur j): max Residuum',f'{worst[0]:.1e}')
print('symmetrisiert reell: max |Im|',f'{worst[1]:.1e}','| A faellt aus Im L heraus: max',f'{worst[2]:.1e}')
