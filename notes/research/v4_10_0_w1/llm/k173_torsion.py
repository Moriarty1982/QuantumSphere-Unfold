"""k173 (Erkundung, W1): Cartan-Gleichung (Variation nach omega) fuer symmetrische Dirac- bzw. Weyl-Kinetik in Einstein-Cartan.
Punktweise, flacher Tetraden-Punkt, omega = Kontorsion K (Levi-Civita-Teil 0). Bestimmt
 (1) die Kopplung dL_sym/dK_{abc}: total antisymmetrisch? proportional zu eps_{abcd} j5^d (Dirac) bzw. eps j^d (Weyl)?
 (2) den algebraischen Kruemmungsanteil R(K) = e^mu_a e^nu_b (K_mu^a_c K_nu^cb - K_nu^a_c K_mu^cb) fuer total antisym. K
 (3) die effektive Vier-Fermionen-Kopplung L_eff = c*kappa*(Strom)^2 nach Elimination von K aus (1/2kappa)R + L_sym.
Kontrolle: fuer Dirac |c| = 3/16 (Hehl-Datta, kappa = 8 pi G)."""
import numpy as np, itertools
eta=np.diag([1.,-1,-1,-1]);rng=np.random.default_rng(3)
eps=np.zeros((4,4,4,4))
for p in itertools.permutations(range(4)): eps[p]=np.linalg.det(np.eye(4)[list(p)])
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1]);Z=np.zeros((2,2));I2=np.eye(2)
be=np.block([[I2,Z],[Z,-I2]]).astype(complex);al=[np.block([[Z,s],[s,Z]]) for s in (sx,sy,sz)];gD=[be]+[be@a for a in al]
g5=1j*gD[0]@gD[1]@gD[2]@gD[3]
s=[I2,sx,sy,sz];sb=[I2,-sx,-sy,-sz]
def spin_coupling(kind,psi):
    """C[m,a,b] = dL_sym/d omega_{m a b} (omega antisym in ab, Basis E_{ab}-E_{ba})."""
    C=np.zeros((4,4,4))
    for m in range(4):
        for a in range(4):
            for b in range(4):
                if a==b: continue
                w=np.zeros((4,4,4));w[m,a,b]=1;w[m,b,a]=-1
                if kind=='D':
                    G=sum(w[m,c,d]*(gD[c]@gD[d]-gD[d]@gD[c]) for c in range(4) for d in range(4))/8
                    bar=psi.conj()@be;L=bar@(1j*gD[m]@G@psi)
                else:
                    G=sum(w[m,c,d]*(s[c]@sb[d]-s[d]@sb[c]) for c in range(4) for d in range(4))/8
                    L=psi.conj()@(1j*sb[m]@G@psi)
                C[m,a,b]=L.real/2   # Re L = symmetrisierte Lagrangedichte (Ableitungsterme fehlen, da psi konstant); /2: jedes Paar doppelt gezaehlt
    return C
def lower(T):  # Raumzeitindex m (unten), a,b schon unten -> alles unten: K_{mab}; hier keine Aenderung noetig
    return T
# algebraischer Kruemmungsanteil fuer K_{abc} = eps_{abcd} k^d
def R2(k):
    K=np.einsum('abcd,d->abc',eps,k)                       # K_{m a b} alle unten
    Kmu=np.einsum('mab,bc->mac',K,eta)                       # K_m{}_a{}^c ... wir brauchen K_mu^a_c: a hoch
    Kup=np.einsum('ad,mdc->mac',eta,K)                       # K_m{}^a{}_c
    Kupup=np.einsum('mac,cb->mab',Kup,eta)                   # K_m{}^{ab}
    R=0
    for m in range(4):
        for n in range(4):
            Rab=Kup[m]@Kupup[n]-Kup[n]@Kupup[m]               # (K_m K_n - K_n K_m)^{ab}
            R+=Rab[m,n]                                      # e^mu_a e^nu_b = delta: a=mu, b=nu (oben)
    return R
alpha=R2(np.array([1.,0,0,0]));alpha2=-R2(np.array([0,1.,0,0]))
kr=np.random.default_rng(9).normal(size=4);print('Lorentz-Pruefung R(k)/(k.k) =',R2(kr)/(kr@eta@kr))
print('R(K) = alpha*k.k mit alpha =',round(alpha,6),'(k zeitartig),',round(alpha2,6),'(k raumartig, k.k=-1)')
for kind in ('D','W'):
    psi=(rng.normal(size=4 if kind=='D' else 2)+1j*rng.normal(size=4 if kind=='D' else 2))
    C=spin_coupling(kind,psi)
    tot=np.einsum('abcd,abc->d',eps,C)/6                     # total antisym. Anteil, dualisiert
    Cas=np.einsum('abcd,d->abc',eps,tot)*(-1)                # eps_{abcd}eps^{abce}=-6 delta: Rueckbau (Vorzeichen aus Lorentz-Signatur)
    if kind=='D': cur=np.array([(psi.conj()@be@gD[a]@g5@psi).real for a in range(4)])
    else: cur=np.array([(psi.conj()@sb[a]@psi).real for a in range(4)])
    curl=eta@cur
    # Fit tot_d (Index oben durch eps mit unteren) gegen Strom (unten/oben)
    fit=[np.linalg.lstsq(v[:,None],tot,rcond=None)[0][0] for v in (cur,curl)];res=[np.linalg.norm(tot-f*v)/np.linalg.norm(tot) for f,v in zip(fit,(cur,curl))]
    i=int(np.argmin(res));beta=fit[i]
    nonanti=np.linalg.norm(C-np.einsum('abcd,d->abc',eps,np.linalg.lstsq(np.einsum('abcd->abcd',eps).reshape(64,4),C.ravel(),rcond=None)[0]))/np.linalg.norm(C)
    # L_K = (1/2kappa) alpha k.k + (Kopplung) : sum_{abc} C_{abc} K_{abc} = sum C eps k = (eps:C)_d k^d = 6*tot_d k^d? direkt:
    g_d=np.einsum('abc,abcd->d',C,eps)*1.0                   # dL/dk^d (K_{abc}=eps_{abcd}k^d), Summe ueber a,b,c mit Paar-Konvention
    # Paar-Konvention: C war je Paar (a<b und a>b) halbiert, also Summe ueber alle a,b korrekt
    # stationaer: (alpha/kappa) eta_{de}k^e + g_d = 0  -> k = -kappa/alpha eta g ; L_eff = -kappa/(2alpha) g.eta.g
    Leff_over_kappa=-(g_d@eta@g_d)/(2*alpha)
    J2=cur@eta@cur
    print(f"{'Dirac' if kind=='D' else 'Weyl'}: Kopplung nicht total antisym. Anteil {nonanti:.1e}; prop. zu Strom (Residuum {res[i]:.1e}); "
          f"L_eff = {Leff_over_kappa/J2:+.6f} * kappa * (Strom)^2   [Strom = {'j5' if kind=='D' else 'j'}]")
