"""H6, Kriterium C: Ist die Vorzeichen-Symmetrie (4 Elemente in Stab(+e7)) das Bild einer Vierergruppe des Bestands?  (Erkundung, nicht blind:
die beiden Antworten (1), (2) stehen analytisch vorher fest.)

Aufbau wie k23/k24 (Oktonionen nach r04, e4 = l, e7 = e3 l).  Pfad zu k23 relativ zum Repo.
(1) Frame-Abbildungen unter phi (v4.9.0-r51.1(c), r16.2(b)): (E, B) -> span(1, e7), (1, +-i) -> 1 +- i e7.  Wirkung auf span(1, e7) vergleichen.
(2) Familien-su(2) (r13.4): rechte Multiplikationen R_e7, R_e8, R_e15 auf den Sedenionen (Cayley-Dickson-Verdopplung derselben Regel).
    Fortsetzung der Vorzeichen-Elemente (a, b) -> (g a, g b); Automorphie und Vertauschbarkeit pruefen.
(3) Lage: L_e7-linear (komplexe Struktur der Farbe bzw. des Tripletts) und Wirkung auf den drei Linien durch e7.
"""
import numpy as np, contextlib, io, os, sys
root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
k23dir = os.path.join(root, "research", "v4_8_0_r03_r12", "llm") if os.path.isdir(os.path.join(root, "research")) else os.path.join(root, "v4_8_0_r03_r12", "llm")
here = k23dir
with contextlib.redirect_stdout(io.StringIO()):
    __file__ = os.path.join(k23dir, "k23_test_h6.py")
    exec(open(__file__).read())
rng = np.random.default_rng(5)
K8 = [np.eye(8)] + [np.block([[np.eye(1), np.zeros((1, 7))], [np.zeros((7, 1)), M]]) for M in kernel]
print(f"Vorzeichen-Kern: {len(K8)} Elemente; Diagonalen (e1..e7): " + "; ".join(str(np.diag(M).astype(int)[1:].tolist()) for M in K8[1:]))
dev = max(np.max(abs(K @ omul(x, y) - omul(K @ x, K @ y))) for K in K8 for x, y in [rng.normal(size=(2, 8))] * 1 for _ in range(1))
for K in K8:
    for _ in range(50):
        x, y = rng.normal(size=8), rng.normal(size=8)
        dev = max(dev, np.max(abs(K @ omul(x, y) - omul(K @ x, K @ y))))
print(f"Automorphismen von O: max. Abweichung {dev:.1e}")

# (1) Frame-Abbildungen auf (E, B) ~ (1, e7)
F = {"R": np.array([[0, -1], [1, 0]]), "T": np.array([[1, 0], [0, -1]]), "J_B": np.array([[0, 1], [1, 0]])}
idx = [0, 7]
restr = [K[np.ix_(idx, idx)] for K in K8]
print("(1) Einschraenkung der Vorzeichen-Elemente auf span(1, e7):", ["Identitaet" if np.allclose(r, np.eye(2)) else r.tolist() for r in restr])
print("    Frame-Abbildungen dort:", {k: v.tolist() for k, v in F.items()}, "-> keine ist die Identitaet: Gleichsetzung unter phi unmoeglich")

# (2) Sedenionen durch Verdopplung derselben Regel
oc = lambda a: a * np.r_[1, -np.ones(7)]
def smul(x, y):
    p, q, r, s = x[:8], x[8:], y[:8], y[8:]
    return np.concatenate([omul(p, r) - omul(oc(s), q), omul(s, p) + omul(q, oc(r))])
E16 = np.eye(16)
e7s, e8s = E16[7], E16[8]
e15s = smul(e7s, e8s)
print(f"    e7 e8 = {'+' if e15s[np.argmax(abs(e15s))] > 0 else '-'}e{int(np.argmax(abs(e15s)))}")
def Rmat(xv): return np.array([smul(E16[i], xv) for i in range(16)]).T
dA = dC = 0.0
for K in K8:
    K16 = np.block([[K, np.zeros((8, 8))], [np.zeros((8, 8)), K]])
    for _ in range(50):
        x, y = rng.normal(size=16), rng.normal(size=16)
        dA = max(dA, np.max(abs(K16 @ smul(x, y) - smul(K16 @ x, K16 @ y))))
    for xv in (e7s, e8s, e15s):
        Rm = Rmat(xv); dC = max(dC, np.max(abs(K16 @ Rm - Rm @ K16)))
print(f"(2) Fortsetzung auf S ist Automorphismus (max. Abweichung {dA:.1e}) und vertauscht mit R_e7, R_e8, R_e15 (max. {dC:.1e})")
print("    -> auf jedem Dublett der Familien-su(2) hoechstens ein Skalar, kein Pauli-Tripel")

# (3) Lage: L_e7-linear?  Wirkung auf den Linien durch e7
Le7 = np.array([omul(E[7], E[i]) for i in range(8)]).T
dL = max(np.max(abs(K @ Le7 - Le7 @ K)) for K in K8)
lines7 = [l for l in tri if 7 in l]
print(f"(3) vertauscht mit L_e7 (komplex-linear bzgl. der e7-Struktur): max. Abweichung {dL:.1e}; Linien durch e7: {lines7}")
for K in K8[1:]:
    d = np.diag(K)
    print("    Element:", ", ".join(f"Linie {tuple(u for u in l if u != 7)}: {'-1' if d[[u for u in l if u != 7][0]] < 0 else '+1'}" for l in lines7))
print("    -> Vorzeichenwechsel auf genau zwei der drei Linien (Determinante +1): die Kleinsche Gruppe im Torus von Stab(e7) = SU(3)")
