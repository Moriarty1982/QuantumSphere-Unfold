"""k403c (zu H195c): Woher kommt der l_k^2-Zaehler? Grad-Leiter der F4-invarianten Kruemmungen und
Fit der Zaehler-Familien ueber dem hergeleiteten Nenner (l_i+l_j)^2.
Aufruf: python k403c_zaehler_grad.py > k403c_out.txt
"""
import numpy as np, sympy as sp
l = np.sort([1 + np.sqrt(2) * np.cos(2 / 9 + 2 * np.pi * k / 3) for k in range(3)])
mu = np.array([7.04e-6, 3.56e-3, 0.967]);   su = np.array([0.15e-6, 0.06e-3, 0.004])
md = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd = np.array([0.02e-5, 0.04e-4, 0.009e-2])
PRS = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]; PERM_B = [2, 1, 0]
lk = np.array([l[k] for (i, j, k) in PRS])[PERM_B]
z = np.array([(l[i] + l[j]) ** 2 for (i, j, k) in PRS])[PERM_B]

# --- Grad-Leiter: ab welchem Potentialgrad erscheint l_k^2 in der F4-Kruemmung? ---
lksym = sp.symbols('l_k'); e1, e2 = sp.symbols('e1 e2')
def hcomp(m):
    H = [sp.Integer(1), e1]
    for k in range(2, m + 1): H.append(sp.expand(e1 * H[k - 1] - e2 * H[k - 2]))
    return H[m]
print("F4-invariantes Potential v=x^n -> Kruemmung der Mode (i,j) auf dem Vakuum (Tr=3, e2=3/2):")
first_quad = None
for n in range(2, 7):
    cur = sp.expand((2 * n * hcomp(n - 2)).subs({e1: 3 - lksym, e2: sp.Rational(3, 2) - lksym * (3 - lksym)}))
    deg = sp.Poly(cur, lksym).degree()
    print(f"  n={n}: {cur}   (Grad in l_k: {deg})")
    if first_quad is None and cur.coeff(lksym, 2) != 0:
        first_quad = n
print(f"  -> l_k^2 erscheint zuerst bei Potentialgrad n = {first_quad} (ein Quintik-Term).")

# --- Fit der Zaehler-Familien ueber dem hergeleiteten Nenner z=(l_i+l_j)^2 ---
def fitN(m, s, basis):
    A = np.stack([b / s for b in basis], axis=1); co, *_ = np.linalg.lstsq(A, m / s, rcond=None)
    pred = sum(c * b for c, b in zip(co, basis)); return np.sum(((pred - m) / s) ** 2), co
fam = {
    "{1, l_k}      (Potentialgrad <= 4)": [1.0 / z, lk / z],
    "{l_k, l_k^2}  (H188, braucht Grad 5)": [lk / z, lk ** 2 / z],
    "{1, l_k, l_k^2} (Grad 5, 3 Param)":   [1.0 / z, lk / z, lk ** 2 / z],
}
print("\nFit ueber dem hergeleiteten Nenner (l_i+l_j)^2:")
for nm, basis in fam.items():
    cu, _ = fitN(mu, su, basis); cd, _ = fitN(md, sd, basis)
    npar = len(basis); dof = 3 - npar
    print(f"  Zaehler {nm:36s}: Up chi2={cu:8.2f}  Down chi2={cd:8.2f}  ({npar} Param, {dof} dof)")

print("\nLesart:")
print("  - Nenner (l_i+l_j)^2: hergeleitet (Peirce + W^2-Norm).")
print("  - Zaehler {1,l_k} (Potentialgrad <=4): von den Daten verworfen (Up ~ 10^4 chi2).")
print("  - l_k^2 erscheint erst bei Potentialgrad 5; damit ist der H188-Zaehler feldgleichungs-")
print("    FAEHIG, aber nicht eindeutig vorhergesagt: die Koeffizienten (inkl. fehlender Konstante)")
print("    bleiben frei. {1,l_k,l_k^2} trifft exakt (0 dof), ist aber reiner Fit.")
