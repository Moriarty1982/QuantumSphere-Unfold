"""k190 (Erkundung, W2 Punkt 3): In welchem Paarungskanal wirkt die Torsions-Vierfermionenkopplung L = -(3/16) kappa j.j (k173),
j^mu = sum_s psi_s^+ sbar^mu psi_s (linkshaendige Weyl-Felder)? Fierz-Umordnung numerisch:
(1) Identitaet sbar^mu_{ab} sbar_mu,cd = c * eps_ac eps_bd (Koeffizient c bestimmen);
(2) fuer zwei Felder psi_1, psi_2: (psi1^+ sbar psi1).(psi2^+ sbar psi2) = c' * (psi1^+ eps psi2^*)(psi2^T eps psi1) pruefen,
    d.h. Paarungskanal Phi = psi2^T eps psi1 (Lorentz-Skalar, Majorana-artig); Vorzeichen von c' entscheidet anziehend/abstossend.
Konvention: Wechselwirkungsenergie H_int = -L_int. Anziehend im Kanal Phi, wenn H_int = -g |Phi|^2 mit g > 0."""
import numpy as np, itertools
I=np.eye(2);sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1]);eta=np.diag([1.,-1,-1,-1])
sbu=[I,-sx,-sy,-sz];sbl=[eta[m,m]*sbu[m] for m in range(4)];eps=np.array([[0,1],[-1,0]])
T=sum(np.einsum('ab,cd->abcd',sbu[m],sbl[m]) for m in range(4))
for c in (2,-2,1,-1):
    if np.allclose(T,c*np.einsum('ac,bd->abcd',eps,eps)): print('sbar^mu_ab sbar_mu cd =',c,'* eps_ac eps_bd')
for c in (2,-2):
    if np.allclose(T,c*np.einsum('ad,bc->abcd',eps,eps)): print('sbar^mu_ab sbar_mu cd =',c,'* eps_ad eps_bc')
# Bilinear-Identitaet mit Grassmann-Vorzeichen: fuer antikommutierende Felder kommt beim Umordnen ein Faktor -1 hinzu.
rng=np.random.default_rng(1)
p1,p2=(rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(2))
lhs=sum((p1.conj()@sbu[m]@p1)*(p2.conj()@sbl[m]@p2) for m in range(4))
Phi=p2@eps@p1
rhs_c=lambda c:c*(p1.conj()@eps@p2.conj())*Phi
for c in (2,-2,1,-1):
    if np.isclose(lhs,rhs_c(c)): print('kommutierend: j1.j2 =',c,'* (psi1^+ eps psi2^*)(psi2^T eps psi1);  (psi1^+ eps psi2^*) = -conj(Phi)?',np.isclose(p1.conj()@eps@p2.conj(),-np.conj(Phi)),' => j1.j2 =',-c,'* |Phi|^2 (kommutierend)')
print('Kontrolle |Phi|^2 =',abs(Phi)**2,' j1.j2 =',lhs.real)
