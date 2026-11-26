"""k355 (H164): Ist beta_sym im Modell der Ueberlapp zweier Auslesen?
K-a Paar mit Ueberlapp beta als Identitaet;  K-b Boost-Identitaeten;  K-c Mischung der zwei Auslesen;  K-d Bilder unter dem Boost.
sympy fuer die Identitaeten, Qiskit quantum_info fuer Zustaende, Ueberlappe, Dichtematrizen.
Aufruf: python k355_test_h164.py > k355_out.txt
"""
import itertools
import numpy as np
import sympy as sp
from qiskit.quantum_info import Statevector, DensityMatrix, Pauli

BETA = 0.5493482
b = sp.symbols("beta", positive=True)   # 0 < beta < 1; sqrt(1 - beta^2) wird unten als reell behandelt
def norm(v):
    n = sp.sqrt(sum(sp.Abs(c)**2 for c in v)).subs(c_**2, 1 - b**2); return [sp.simplify(c / n) for c in v]
c_ = sp.symbols("c", positive=True)   # c = sqrt(1 - beta^2)
base = {"N": [1, 0], "S": [0, 1], "K1": [c_, b], "k_alpha": [1, b], "h": [1, b**2], "E": [1, 1]}
states = {}
for name, v in base.items():
    states[name] = norm(v)
    if name not in ("N", "S", "E"): states[name + "~Tausch"] = norm(v[::-1])
    if name not in ("N", "S"): states[name + "~Tach"] = norm([v[0], sp.I * v[1]])
num = lambda e: complex(sp.N(sp.sympify(e).subs(c_, sp.sqrt(1 - b**2)).subs(b, BETA)))

print("== K-a  Paare benannter Zustaende mit Ueberlapp beta ==")
print(f"  {len(states)} Zustaende, {len(states)*(len(states)-1)//2} Paare;  beta_sym = {BETA}, theta_H = {np.degrees(2*np.arcsin(BETA)):.4f} Grad, pi - theta_H = {180-np.degrees(2*np.arcsin(BETA)):.4f} Grad")
ident, near = [], []
for (n1, s1), (n2, s2) in itertools.combinations(states.items(), 2):
    ov = sp.conjugate(s1[0]) * s2[0] + sp.conjugate(s1[1]) * s2[1]
    ov2 = sp.simplify(sp.expand(ov * sp.conjugate(ov)).subs(c_, sp.sqrt(1 - b**2)))
    val = abs(complex(sp.N(ov2.subs(b, BETA))))**0.5
    q = Statevector([num(c) for c in s1]).inner(Statevector([num(c) for c in s2]))   # Qiskit-Kontrolle
    assert abs(abs(q) - val) < 1e-12
    is_id = sp.simplify(ov2 - b**2) == 0
    if is_id: ident.append((n1, n2, val))
    elif abs(val - BETA) / BETA < 0.01: near.append((n1, n2, val, ov2))
print("  Identitaet |<psi1|psi2>| = beta (symbolisch):")
for n1, n2, val in ident: print(f"    ({n1}, {n2}): {val:.7f}")
print("  nur Zahlentreffer innerhalb 1 % (keine Identitaet):")
for n1, n2, val, ov2 in near: print(f"    ({n1}, {n2}): {val:.7f}  Abweichung {100*(val-BETA)/BETA:+.2f} %;  Ueberlapp^2 = {sp.simplify(ov2)}")
if not near: print("    keine")

print("\n== K-b  Boost-Identitaeten (sympy) ==")
eps = sp.atanh(b); gL = (1 + b**2) / (1 - b**2)
thH = 2 * sp.asin(b); th = sp.pi - thH
print("  (i)   cos(theta/2) - beta mit theta = pi - theta_H:", sp.simplify(sp.cos(th / 2) - b), ";  Rapiditaet = artanh(beta) = eps der Maske (H45), Zahl:", f"{float(eps.subs(b, BETA)):.6f}")
e_ = sp.symbols("e", positive=True); tb = sp.tanh(e_)   # beta = tanh(e), damit 0 < beta < 1 eingebaut ist
vrel = 2 * tb / (1 + tb**2); gLe = (1 + tb**2) / (1 - tb**2)
r2 = sp.simplify((1 / (1 - vrel**2) - gLe**2).rewrite(sp.exp))
print("  (ii)  Frames mit +beta und -beta: relative Geschwindigkeit 2 beta/(1 + beta^2); 1/(1 - v^2) - gamma_L^2 =", r2, f";  gamma_L = {float(gL.subs(b, BETA)):.5f}")
r3 = sp.simplify((1 / sp.cosh(2 * e_) - 1 / gLe).rewrite(sp.exp))
print("  (iii) sech(2 eps) - 1/gamma_L =", r3)
print("  invariante Masse des Paars: M/(2E) = sin(theta/2) = cos(theta_H/2) = sqrt(1 - beta^2) =", f"{np.sqrt(1-BETA**2):.6f}", "= 1/gamma(beta)")

print("\n== K-c  gleichgewichtete Mischung der zwei Auslesen (Qiskit DensityMatrix) ==")
def bloch(rho): return np.real([rho.expectation_value(Pauli(p)) for p in "XYZ"])
K1 = Statevector([np.sqrt(1 - BETA**2), BETA]); S = Statevector([0, 1]); N = Statevector([1, 0])
rho = DensityMatrix(0.5 * (DensityMatrix(K1).data + DensityMatrix(S).data)); bl = bloch(rho)
print(f"  Bloch-Vektor {np.round(bl, 6)}, Laenge {np.linalg.norm(bl):.6f}  (beta = {BETA}; Materie-Zustand: 1/gamma_L = {(1-BETA**2)/(1+BETA**2):.6f})")
print(f"  Besetzungen im Eigensystem {np.round(np.sort(np.linalg.eigvalsh(rho.data))[::-1], 6)}; Materie-Zustand (1, beta^2)/(1 + beta^2) = [{1/(1+BETA**2):.6f} {BETA**2/(1+BETA**2):.6f}]")
ka = Statevector(np.array([1, BETA]) / np.sqrt(1 + BETA**2)); rk = DensityMatrix(np.diag(np.diag(DensityMatrix(ka).data)))
print(f"  zum Vergleich der dephasierte Kickzustand (1, beta): Besetzungen {np.round(np.real(np.diag(rk.data)), 6)}, Bloch-Laenge {np.linalg.norm(bloch(rk)):.6f}")
x = sp.symbols("x", positive=True); root = sp.nsolve(x**3 + x**2 + x - 1, 0.5)
print(f"  Laenge beta = 1/gamma_L nur fuer beta^3 + beta^2 + beta - 1 = 0: beta = {float(root):.6f} (gemessen {BETA}, Hopf {1/np.sqrt(3):.6f})")

print("\n== K-d  Bilder unter dem Boost, der K1 und S auf Gegenpunkte legt ==")
def spinor(n):   # Bloch-Vektor -> Spinor
    th_, ph_ = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0]); return np.array([np.cos(th_ / 2), np.exp(1j * ph_) * np.sin(th_ / 2)])
def bvec(psi):
    psi = psi / np.linalg.norm(psi); sv = Statevector(psi); return np.real([sv.expectation_value(Pauli(p)) for p in "XYZ"])
def boost_matrix(u, beta):   # SL(2,C): Richtungen laengs u werden auseinandergezogen (Aberration cos' = (cos - beta)/(1 - beta cos))
    eta = np.arctanh(beta); sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
    su = sum(u[i] * sig[i] for i in range(3)); return np.cosh(eta / 2) * np.eye(2) - np.sinh(eta / 2) * su
def ang(n1, n2): return np.degrees(np.arccos(np.clip(n1 @ n2, -1, 1)))
def bilder(beta):
    thH_ = 2 * np.arcsin(beta); pts = {"N": np.array([0, 0, 1.0]), "S": np.array([0, 0, -1.0]), "K1": np.array([np.sin(thH_), 0, np.cos(thH_)]),
           "E+x": np.array([1.0, 0, 0]), "E-x": np.array([-1.0, 0, 0]), "E+y": np.array([0, 1.0, 0])}
    u = pts["K1"] + pts["S"]; u /= np.linalg.norm(u); A = boost_matrix(u, beta)
    return pts, {k: bvec(A @ spinor(v)) for k, v in pts.items()}, A
pts, img, A = bilder(BETA); alpha = np.degrees(np.arctan(BETA)); thHd = np.degrees(2 * np.arcsin(BETA))
print(f"  det A = {np.linalg.det(A).real:.12f};  Winkel K1'-S' = {ang(img['K1'], img['S']):.6f} Grad (Gegenpunkte);  Ueberlapp danach {abs(np.vdot(A @ spinor(pts['K1']), A @ spinor(pts['S']))):.1e}")
print(f"  Bezugswinkel: theta_H = {thHd:.4f}, 2 alpha = {2*alpha:.4f}, 4 alpha = {4*alpha:.4f}, pi - theta_H = {180-thHd:.4f}, pi - 2 alpha = {180-2*alpha:.4f}  (tan alpha = beta, cos 2 alpha = 1/gamma_L)")
cands = lambda be: {"theta_H": np.degrees(2*np.arcsin(be)), "2 alpha": 2*np.degrees(np.arctan(be)), "4 alpha": 4*np.degrees(np.arctan(be)), "pi - theta_H": 180-np.degrees(2*np.arcsin(be)),
                    "pi - 2 alpha": 180-2*np.degrees(np.arctan(be)), "pi - 4 alpha": 180-4*np.degrees(np.arctan(be)), "pi/2": 90.0, "pi": 180.0, "0": 0.0}
tests = (BETA, 1 / np.sqrt(3), 0.3, 0.71, 0.123)
for k1, k2 in itertools.combinations(pts, 2):
    hits = None
    for be in tests:
        p_, i_, _ = bilder(be); a = ang(i_[k1], i_[k2]); h = {n for n, v in cands(be).items() if abs(a - v) < 1e-8}
        hits = h if hits is None else hits & h
    print(f"    {k1:>3}'-{k2:<3}': vorher {ang(pts[k1], pts[k2]):9.4f}, nachher {ang(img[k1], img[k2]):9.4f} Grad;  Identitaet (5 Werte von beta): {', '.join(sorted(hits)) if hits else 'keine der benannten'}")
proj = img["K1"] @ img["N"]
print(f"  Projektion von K1' auf die Achse N': {proj:.6f};  1/gamma_L = {(1-BETA**2)/(1+BETA**2):.6f}  => K1', um die Achse N' dephasiert, hat die Bloch-Laenge des Materie-Zustands")
psiK = A @ spinor(pts["K1"]); psiN = A @ spinor(pts["N"]); psiN /= np.linalg.norm(psiN); psiK /= np.linalg.norm(psiK)
psiNp = np.array([-np.conj(psiN[1]), np.conj(psiN[0])])
print(f"  Besetzungen von K1' in der Basis (N', Gegenpunkt von N'): {abs(np.vdot(psiN, psiK))**2:.6f}, {abs(np.vdot(psiNp, psiK))**2:.6f};  Materie-Zustand: {1/(1+BETA**2):.6f}, {BETA**2/(1+BETA**2):.6f}")

print("\n== Erkundung ohne Kriterium ==")
bh = 1 / np.sqrt(3)
print(f"  Hopf-Wert beta = 1/sqrt(3): theta = pi - theta_H = {180-np.degrees(2*np.arcsin(bh)):.4f} Grad = arccos(-1/3) = {np.degrees(np.arccos(-1/3)):.4f} (Tetraederwinkel); 2 alpha = 60, gamma_L = 2")
tet = [np.array([0, 0, 1.0])] + [np.array([np.sqrt(8) / 3 * np.cos(p), np.sqrt(8) / 3 * np.sin(p), -1 / 3]) for p in (0, 2 * np.pi / 3, 4 * np.pi / 3)]
ovs = [abs(Statevector(spinor(tet[i])).inner(Statevector(spinor(tet[j])))) for i, j in itertools.combinations(range(4), 2)]
print(f"    vier Tetraeder-Zustaende: paarweiser Ueberlapp min {min(ovs):.6f}, max {max(ovs):.6f} (1/sqrt(3) = {bh:.6f}); Summe der Projektoren = {np.round(sum(DensityMatrix(Statevector(spinor(t))).data for t in tet).real, 6).tolist()} (= 2 mal Eins: vollstaendige Messung)")
print(f"    vier paarweise gleichwinklige Richtungen gibt es nur bei cos = -1/3; beim gemessenen beta (cos = {2*BETA**2-1:.4f}, {180-thHd:.2f} Grad) hoechstens drei")
