"""k241: H121, die Frame-Abbildung J_B am Flaechenoperator (OP1). Vorab-Notiz llm/Vorab_Notiz_H121_JB_Flaechenoperator.md (Commit c35174df).
Aufruf: python k241_h121_jb_area.py   (keine Daten, keine Pfade)"""
import numpy as np
import sympy as sp
from scipy.linalg import expm

# ---- Lorentz-Algebra in der Vektordarstellung ----
def Lgen(i):
    M = sp.zeros(4)
    a, b = [(2, 3), (3, 1), (1, 2)][i]
    M[a, b] = -1; M[b, a] = 1
    return M


def Kgen(i):
    M = sp.zeros(4)
    M[0, i + 1] = 1; M[i + 1, 0] = 1
    return M


L = [Lgen(i) for i in range(3)]; K = [Kgen(i) for i in range(3)]
com = lambda A, B: A * B - B * A
eps = lambda i, j, k: sp.LeviCivita(i, j, k)
okLL = all(com(L[i], L[j]) == sum((eps(i, j, k) * L[k] for k in range(3)), sp.zeros(4)) for i in range(3) for j in range(3))
okLK = all(com(L[i], K[j]) == sum((eps(i, j, k) * K[k] for k in range(3)), sp.zeros(4)) for i in range(3) for j in range(3))
okKK = all(com(K[i], K[j]) == sum((-eps(i, j, k) * L[k] for k in range(3)), sp.zeros(4)) for i in range(3) for j in range(3))
print('(0) Vertauschungsrelationen [L,L] = eps L, [L,K] = eps K, [K,K] = -eps L:', okLL, okLK, okKK)

basis = L + K
names = ['Lx', 'Ly', 'Lz', 'Kx', 'Ky', 'Kz']


def coords(X):
    c = sp.symbols('c0:6')
    sol = sp.solve(list(X - sum((ci * B for ci, B in zip(c, basis)), sp.zeros(4))), c, dict=True)[0]
    return [sp.simplify(sol.get(ci, 0)) for ci in c]


def adjoint(G):
    Gi = sp.simplify(G.inv())
    return sp.Matrix([coords(sp.simplify(G * B * Gi)) for B in basis]).T   # Spalte j = Bild von basis[j]


Kx = K[0]
JB = sp.simplify((sp.I * sp.pi / 2 * Kx).exp())
print('(H121a) J_B = exp(i pi/2 K_x) =', JB.tolist())
AdJ = adjoint(JB)
for j, n in enumerate(names):
    img = ' + '.join(f'({AdJ[i, j]}) {names[i]}' for i in range(6) if AdJ[i, j] != 0)
    print(f'        J_B {n} J_B^-1 = {img}')
JBn = [sp.simplify(JB * B * JB.inv()) for B in basis]
Lp, Kp = JBn[:3], JBn[3:]
ok = (all(sp.simplify(com(Lp[i], Lp[j]) - sum((eps(i, j, k) * Lp[k] for k in range(3)), sp.zeros(4))) == sp.zeros(4) for i in range(3) for j in range(3))
      and all(sp.simplify(com(Kp[i], Kp[j]) + sum((eps(i, j, k) * Lp[k] for k in range(3)), sp.zeros(4))) == sp.zeros(4) for i in range(3) for j in range(3)))
print('        Bilder erfuellen dieselben Vertauschungsrelationen (Automorphismus):', ok)

# ---- H121c: induzierte Simplizitaet ----
g = sp.symbols('gamma', positive=True)
# Bild: L'_i = sum_j (c_ij L_j + d_ij K_j), K'_i = sum_j (a_ij L_j + b_ij K_j); mit K = gamma L: K' = (a + g b) L, L' = (c + g d) L
C = AdJ[0:3, 0:3].T; D = AdJ[3:6, 0:3].T   # L'_i aus Spalten i: Koeffizienten von L_j (Zeilen 0..2) und K_j (Zeilen 3..5)
A_ = AdJ[0:3, 3:6].T; B_ = AdJ[3:6, 3:6].T
Lmap = sp.simplify(C + g * D); Kmap = sp.simplify(A_ + g * B_)
Gam = sp.simplify(Kmap * Lmap.inv())
print('(H121c) aus K = gamma L folgt K\' = Gamma\' L\' mit Gamma\' =', Gam.tolist())
gM = sp.Rational(237533, 1000000); gT = sp.log(2) / (sp.pi * sp.sqrt(3)); gL = sp.nsimplify(1.864700)
vals = sorted(set(sp.N(x, 12) for x in Gam.subs(g, gM).diagonal()), key=lambda v: sp.re(v))
print('         eingesetzt gamma_M = 0.237533: Diagonale von Gamma\' =', [sp.N(x, 8) for x in Gam.subs(g, gM).diagonal()])
print('         Vergleich mit gamma_T =', sp.N(gT, 8), 'und gamma_L =', gL)
for v in vals:
    for nm, tgt in (('|gamma\'| gegen gamma_T', abs(v) - gT), ('gamma_M/|gamma\'| gegen gamma_L', gM / abs(v) - gL), ('gamma_M/|gamma\'| gegen gamma_T', gM / abs(v) - gT)):
        ref = gT if 'gamma_T' in nm else gL
        print(f'           gamma\' = {sp.N(v, 8)}: {nm}: relative Abweichung {sp.N(abs(tgt) / ref, 4)}')
# Flaechenquant von T, wenn T mit seinen eigenen Drehungen L' abliest: |L'_quer| = |K_quer| = gamma |L_quer|
print('         Querkomponenten: L\'_y = (', AdJ[:, 1].T.tolist(), ') -> |L\'_quer| = gamma |L_quer| auf K = gamma L')

# ---- H121b: Spektrum unter Konjugation in endlichen Darstellungen ----
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)


def spin(j):
    d = int(round(2 * j + 1)); m = np.arange(j, -j - 1, -1)
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((d, d), complex)
    for k in range(1, d):
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / (2j), Jz]


def rep(j1, j2):
    A = spin(j1); B = spin(j2); I1 = np.eye(len(A[0])); I2 = np.eye(len(B[0]))
    Ja = [np.kron(a, I2) for a in A]; Jb = [np.kron(I1, b) for b in B]
    J = [Ja[i] + Jb[i] for i in range(3)]; Kh = [-1j * (Ja[i] - Jb[i]) for i in range(3)]   # hermitesche Konvention, K = -i(A - B)
    return J, Kh


worst = 0.0
for (j1, j2) in ((0.5, 0), (0.5, 0.5), (1, 0)):
    J, Kh = rep(j1, j2)
    U = expm(-1j * (1j * np.pi / 2) * Kh[0])     # Boost exp(-i r K_x) mit r = i pi/2, nicht unitaer
    Ui = np.linalg.inv(U)
    for nm, O in (('J^2', sum(x @ x for x in J)), ('J_z', J[2])):
        e0 = np.sort_complex(np.linalg.eigvals(O)); e1 = np.sort_complex(np.linalg.eigvals(U @ O @ Ui))
        dev = np.max(np.abs(e0 - e1)); worst = max(worst, dev)
        herm = np.allclose(U @ O @ Ui, (U @ O @ Ui).conj().T)
        print(f'(H121b) ({j1},{j2}) {nm}: Eigenwerte vorher {np.round(e0.real, 6)}, Abweichung nachher {dev:.2e}; Bild hermitesch: {herm}; U unitaer: {np.allclose(U @ U.conj().T, np.eye(len(U)))}')
print(f'        groesste Abweichung der Spektren: {worst:.2e} (Kriterium <= 1e-10)')

# ---- Kontrolle: reeller Boost mit eta_sym ----
eta = sp.atanh(sp.Rational(549406, 1000000))
Gr = sp.simplify((eta * Kx).exp())
Adr = adjoint(Gr)
Cr = Adr[0:3, 0:3].T; Dr = Adr[3:6, 0:3].T; Ar = Adr[0:3, 3:6].T; Br = Adr[3:6, 3:6].T
Gamr = sp.simplify((Ar + g * Br) * (Cr + g * Dr).inv())
print('(Kontrolle) reeller Boost eta_sym: Gamma\' bei gamma_M =', [[sp.N(x, 6) for x in row] for row in Gamr.subs(g, gM).tolist()])
