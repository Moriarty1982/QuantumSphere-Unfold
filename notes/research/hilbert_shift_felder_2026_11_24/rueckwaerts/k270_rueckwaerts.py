"""k270 (Erkundung, nicht blind, 24.11.2026): Feldkonfigurationen des HS-Turms rueckwaerts.
Start oben (bekannte Physik: SU(3) Farbe, Ladungen einer Generation, Anomaliefreiheit, Chiralitaet),
dann je Stufe: Welche Konfiguration der Stufe darunter ist notwendig, was ist erzwungen, was gesetzt?

A  HS(3): Stabilisatoren in G2 = Der(O) fuer 0, 1, 2, 3 festgehaltene Einheiten.
B  HS(3)->HS(n): Leiterzahl N_c je Stufe (antikommutierende L_e, eine Einheit fest) und J = iL_u = +-(-1)^N.
C  Anomalien einer Generation mit Turm-Ladungen k/N_c fuer allgemeines N_c (exakt, sympy).
D  HS(1): Der Projektor C = (1 + iL_u)/2 schneidet aus der Ellipse a e^{iwt} + b e^{-iwt} genau einen Kreisanteil.
E  Drehsinn-Bit: Ist u -> -u auf HS(1), HS(2), HS(3) durch einen Automorphismus erreichbar? Links/rechts?
Konvention wie k253: (a,b)(c,d) = (ac - d* b, d a + b c*). Aufruf: python3 k270_rueckwaerts.py
"""
import itertools
import numpy as np
import sympy as sp

rng = np.random.default_rng(270)


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def mul(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])


def table(N):
    E = np.eye(N); C = np.zeros((N, N, N))
    for i in range(N):
        for j in range(N):
            C[i, j] = mul(E[i], E[j])
    return C


def Lmat(C, i):  # (L_{e_i} x)_k = sum_j C[i,j,k] x_j
    return C[i].T


def Rmat(C, i):
    return C[:, i, :].T


def der_basis(C, fixed=()):
    N = C.shape[0]; rows = []
    for i in range(N):
        for j in range(N):
            for m in range(N):
                r = np.zeros(N * N)
                for k in range(N):
                    if C[i, j, k]:
                        r[m * N + k] += C[i, j, k]
                for p in range(N):
                    if C[p, j, m]:
                        r[p * N + i] -= C[p, j, m]
                    if C[i, p, m]:
                        r[p * N + j] -= C[i, p, m]
                if r.any():
                    rows.append(r)
    for f in fixed:
        v = np.zeros(N); v[f] = 1.0
        for m in range(N):
            r = np.zeros(N * N)
            for p in range(N):
                r[m * N + p] = v[p]
            rows.append(r)
    A = np.array(rows)
    _, s, vt = np.linalg.svd(A)
    null = vt[(s > 1e-9).sum():]
    return [v.reshape(N, N) for v in null]  # D[m,p]: (D e_p)_m


print("=" * 78)
print("A  HS(3): Was muss das Oktonion-Feld festhalten, damit genau SU(3) bleibt?")
C8 = table(8)
E8 = np.eye(8)
# Quaternion-Unteralgebra: e1,e2,e3 (e1 e2 = e3?)
print("   e1*e2 =", np.round(mul(E8[1], E8[2]), 3), "  e1*e4 =", np.round(mul(E8[1], E8[4]), 3))
cases = [("nichts", ()), ("eine Einheit u = e7", (7,)), ("zwei Einheiten e7, e1", (7, 1)),
         ("assoziatives Tripel e1,e2,e3 (Quaternionen)", (1, 2, 3)),
         ("nicht-assoziatives Tripel e1,e2,e4", (1, 2, 4))]
for name, fx in cases:
    B = der_basis(C8, fx)
    # Kompaktheit: Spurform tr(XY) auf der 8-dim. Darstellung
    if B:
        G = np.array([[np.trace(X @ Y) for Y in B] for X in B])
        ev = np.linalg.eigvalsh(G)
        sig = f"Spurform: {int((ev < -1e-9).sum())} neg, {int((ev > 1e-9).sum())} pos"
    else:
        sig = ""
    print(f"   fest: {name:45s} dim Stab = {len(B):2d}  {sig}")
print("   Lesart: 14 = G2, 8 = SU(3), 3 = SU(2) (Stab eines Quaternion-Blocks), 0 = nichts.")
print("   SU(3) ungebrochen <=> genau eine Einheit fest. Zwei feste Einheiten erzwingen die dritte (e7 e1)")

print("=" * 78)
print("B  Leiterzahl je Stufe und J = iL_u als Paritaet (-1)^N")


def max_anticomm(C):
    N = C.shape[0]
    L = [Lmat(C, i) for i in range(1, N)]
    best = []
    # greedy over orderings (wie k254), reicht fuer untere Schranke; RH-Zahl ist Obergrenze
    for start in range(len(L)):
        S = [start]
        for j in range(len(L)):
            if j in S:
                continue
            if all(np.abs(L[j] @ L[k] + L[k] @ L[j]).max() < 1e-9 for k in S):
                S.append(j)
        if len(S) > len(best):
            best = S
    return [b + 1 for b in best]


for n in range(1, 6):
    N = 2 ** n
    Cn = table(N)
    S = max_anticomm(Cn)
    m = len(S)
    Nc = (m - 1) // 2
    print(f"   n={n} dim={N:2d}: antikommutierende L_e: {m:2d} -> eine Einheit fest, Leitern N_c = {Nc}"
          + ("   (ungerader Rest: eine Achse ohne Partner)" if (m - 1) % 2 else ""))

# Fock-Struktur auf C (x) O explizit (Konvention H19: u = e7, Leitern a = 4,5,6, alpha_a = 1/2 (L_a + i L_{e7 e_a}))
L = {i: Lmat(C8, i) for i in range(1, 8)}
I8 = np.eye(8)


def Lof(v):
    return sum(v[i] * L[i] for i in range(1, 8) if abs(v[i]) > 1e-12)


alphas = []
for a in (4, 5, 6):
    e7ea = mul(E8[7], E8[a])
    alphas.append(0.5 * (L[a] + 1j * Lof(e7ea)))
Nop = sum(al.conj().T @ al for al in alphas)
J = 1j * L[7]
P = np.diag([1.0])
par = None
ev, V = np.linalg.eigh((Nop + Nop.conj().T) / 2)
print("   C(x)O: Eigenwerte N =", np.round(ev, 6))
# Paritaet (-1)^N gegen J = iL_e7
from scipy.linalg import expm
parity = expm(1j * np.pi * Nop)
for sgn in (+1, -1):
    print(f"   |J - ({sgn:+d})(-1)^N| = {np.abs(J - sgn * parity).max():.1e}")
print("   -> J = iL_u ist (bis aufs Vorzeichen) die Fock-Paritaet: C = (1+J)/2 waehlt die geraden oder ungeraden Sektoren.")

print("=" * 78)
print("C  Anomalien mit Turm-Ladungen fuer allgemeines N_c (exakt)")
# Setting wie r43: Sektoren k=0..Nc, Ladung Q=k/Nc, Darstellung Lambda^k von SU(Nc) (Dim binom(Nc,k)),
# H-Faktor: Dublett-Index T3 = +-1/2 fuer jeden Sektor. C = Projektor auf eine Paritaet (gerade k).
# Links (Bild von C): schwaches Dublett, Y/2 = Q + s. Rechts: Singuletts, Y/2 = Q + s + T3.
# Alle Felder als linkshaendige Weyl-Felder gezaehlt (rechte Sektoren als ladungskonjugierte, wie r43: dort tragen
# die rechten Sektoren schon die konjugierten Quantenzahlen, Bild 1/3 und 1 -> d^c, u^c, e^c, nu^c).
s = sp.symbols('s')


def anomalies(Nc, parity_even=True):
    TrY = 0; TrY3 = 0; A2 = 0; A3 = 0
    reps = []
    for k in range(Nc + 1):
        dim = sp.binomial(Nc, k)
        Tk = sp.Rational(1, 2) * sp.binomial(Nc - 2, k - 1) if (Nc >= 2 and 1 <= k <= Nc - 1) else 0  # Dynkin-Index Lambda^k
        Q = sp.Rational(k, Nc) if Nc else 0
        left = (k % 2 == 0) == parity_even
        reps.append((k, int(dim), 'L' if left else 'R'))
        if left:
            y = Q + s                      # Y/2 fuer beide Dublett-Komponenten
            TrY += 2 * dim * y
            TrY3 += 2 * dim * y ** 3
            A2 += dim * y                  # SU(2)^2 U(1): Summe ueber Dubletts (Index 1/2 je Dublett, Faktor weggelassen)
            A3 += 2 * Tk * y               # SU(Nc)^2 U(1)
        else:
            for t3 in (sp.Rational(1, 2), -sp.Rational(1, 2)):
                y = Q + s + t3
                TrY += dim * y
                TrY3 += dim * y ** 3
                A3 += Tk * y
    return [sp.simplify(TrY), sp.simplify(TrY3), sp.simplify(A2), sp.simplify(A3)], reps


for Nc in (0, 1, 2, 3, 4, 5, 7):
    an, reps = anomalies(Nc)
    sols = sp.solve(an[0], s)
    out = []
    for sol in sols:
        vals = [sp.nsimplify(sp.simplify(a.subs(s, sol))) for a in an]
        out.append((sol, vals))
    fundamental_only = all(r[1] in (1, Nc) for r in reps)
    ndoublets = sum(r[1] for r in reps if r[2] == 'L')
    print(f"   N_c={Nc}: Sektoren (k, dim, Seite) = {reps}")
    print(f"          nur Singuletts/Fundamentale: {fundamental_only};  schwache Dubletts: {ndoublets}"
          f" ({'gerade' if ndoublets % 2 == 0 else 'UNGERADE -> globale SU(2)-Anomalie (Witten)'})")
    for sol, vals in out:
        print(f"          Tr Y = 0 -> s = {sol};  (Tr Y, Tr Y^3, SU(2)^2U(1), SU(Nc)^2U(1)) = {vals}")

# Standardmodell-Formel fuer allgemeines N_c gegen Turm-Ladung des u-Quarks
Ncs = sp.symbols('N_c', positive=True)
print("   SM mit N_c Farben (Anomaliefreiheit): Q_u = 1/2 + 1/(2N_c); Turm: u im Sektor N_c-1 -> Q_u = (N_c-1)/N_c")
print("   Loesung von 1/2 + 1/(2N_c) = (N_c-1)/N_c:", sp.solve(sp.Eq(sp.Rational(1, 2) + 1 / (2 * Ncs), (Ncs - 1) / Ncs), Ncs))

print("=" * 78)
print("D  HS(1): C = (1 + iL_u)/2 auf der komplexifizierten Ellipse")
C2 = table(2)
Lu = Lmat(C2, 1)          # Multiplikation mit u = i_HS(1) auf R^2
Cp = 0.5 * (np.eye(2) + 1j * Lu)
Cm = 0.5 * (np.eye(2) - 1j * Lu)
print(f"   C+^2 - C+ = {np.abs(Cp @ Cp - Cp).max():.1e},  C+ C- = {np.abs(Cp @ Cm).max():.1e},  Rang C+ = {np.linalg.matrix_rank(Cp)}")
w = 1.0
for a, b in [(1.0, 1.0), (1.0, 0.5), (1.0, 0.0), (0.0, 1.0)]:
    ts = np.linspace(0, 2 * np.pi, 7)[:-1]
    # Bahn psi(t) = a e^{u w t} + b e^{-u w t} als Vektor in R^2 = (Re, Im), komplexifiziert mit der Zeitphase
    # Komplexe Zeitdarstellung: psi(t) = Re[ Z e^{i w t} ] mit Z in C (x) R^2; zerlege Z nach C+-.
    Z = a * np.array([1, -1j]) + b * np.array([1, 1j])      # e^{+uwt}: (cos, sin) = Re[(1,-i)e^{iwt}]; e^{-uwt}: Re[(1,i)e^{iwt}]
    wp = np.linalg.norm(Cp @ Z) ** 2; wm = np.linalg.norm(Cm @ Z) ** 2
    area = np.pi * (a ** 2 - b ** 2)
    print(f"   a={a:.1f} b={b:.1f}: Gewicht im C+-Bild {wp:.3f}, im C--Bild {wm:.3f}, Differenz/2 = {(wp - wm) / 2:+.3f}, Flaeche/pi = {area / np.pi:+.3f}")
print("   -> HS(0) (a=b): gleiche Gewichte in beiden Bildern. Ladung a^2-b^2 = halbe Gewichtsdifferenz.")
print("      Das Bild von C (eine Generation, r42) ist der reine Kreisanteil b = 0.")

# Auf C (x) O: span_C(1, e7) ist die eingebettete HS(1)-Ebene; C = (1+iL_e7)/2 dort
Ce = 0.5 * (I8 + 1j * L[7])
sub = np.zeros((8, 2)); sub[0, 0] = 1; sub[7, 1] = 1
Cs = sub.T @ Ce @ sub
print(f"   Einschraenkung von C=(1+iL_e7)/2 auf span(1,e7) gleich C+ der HS(1)-Ebene: {np.abs(Cs - Cp).max():.1e}")

print("=" * 78)
print("E  Drehsinn-Bit: u -> -u durch Automorphismus? links <-> rechts?")
# HS(1): Aut_R(C) = {id, conj}; conj ist kein Drehen (det -1 auf R^2), die Identitaetskomponente ist trivial
print("   HS(1) C: Automorphismen {id, conj}; conj hat det", np.linalg.det(np.diag([1, -1])), "-> Bit echt (nicht wegdrehbar)")
C4 = table(4); E4 = np.eye(4)


def qinv(q):
    return conj(q) / np.dot(q, q)


j = E4[2]
img = mul(mul(j, E4[1]), qinv(j))
print("   HS(2) H: j i j^-1 =", np.round(img, 3), " -> i -> -i durch innere Drehung (Weg exp(theta j), theta 0..pi/2)")
for th in (0, np.pi / 4, np.pi / 2):
    q = np.cos(th) * E4[0] + np.sin(th) * E4[2]
    print(f"      theta={th:.3f}: q i q^-1 = {np.round(mul(mul(q, E4[1]), qinv(q)), 3)}")
# links/rechts: Automorphismus phi: phi L_a phi^-1 = L_{phi(a)}; Links-Algebra vertauscht mit Rechts-Algebra
LA = [Lmat(C4, i) for i in range(1, 4)]; RA = [Rmat(C4, i) for i in range(1, 4)]
print(f"   H: [L_a, R_b] max = {max(np.abs(x @ y - y @ x).max() for x in LA for y in RA):.1e} (zwei vertauschende SU(2))")
Rot = None
# zufaelliger Automorphismus von H: Konjugation mit Einheitsquaternion q
q = rng.normal(size=4); q /= np.linalg.norm(q)
Phi = np.column_stack([mul(mul(q, E4[k]), qinv(q)) for k in range(4)])
devL = max(np.abs(Phi @ LA[i] @ np.linalg.inv(Phi) - sum(Phi[m, i + 1] * LA[m - 1] for m in range(1, 4))).max() for i in range(3))
print(f"   H: phi L_a phi^-1 = L_phi(a) (Abw. {devL:.1e}): Automorphismen lassen links links -> Seitenwahl ist ein echtes Bit")
Kq = np.diag([1, -1, -1, -1.0])
devK = max(np.abs(Kq @ LA[i] @ Kq - (-RA[i])).max() for i in range(3))
print(f"   H: Konjugation K: K L_a K = -R_a (Abw. {devK:.1e}): erst die Anti-Automorphie tauscht die Seiten")
# HS(3): (a,b) -> (a,-b) ist Automorphismus von O = H + H l und schickt e7 -> -e7
S = np.diag([1, 1, 1, 1, -1, -1, -1, -1.0])
xs = [rng.normal(size=8) for _ in range(2)]
dev = np.abs(S @ mul(xs[0], xs[1]) - mul(S @ xs[0], S @ xs[1])).max()
print(f"   HS(3) O: (a,b)->(a,-b) Automorphismus (Abw. {dev:.1e}), schickt e7 -> {S[7, 7]:+.0f} e7; G2 zusammenhaengend")
print("   -> Das Drehsinn-Bit von HS(1) wird ab HS(2) wegdrehbar (Konvention); als echtes Bit bleibt links/rechts.")
