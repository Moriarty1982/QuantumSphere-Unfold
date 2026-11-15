"""Auslesungen eines Objekts: Eigenzustaende der Frame-Abbildungen, paarweise nicht orthogonal (Erkundung, nicht blind).

Auf der invarianten Kugel chi = (sqrt s+, sqrt s-) (invariant_doublet.py, frame_labels.py):
(1) Die Frame-Abbildungen wirken als 2x2-Matrizen; ihre Eigenzustaende sind genau die sechs Pole.
(2) Alle Teilmengen der sechs Pole ohne orthogonales Paar: maximale Groesse, Anzahl, Ueberlappungen, K, Phase.
(3) Bahnen der drei Frame-Abbildungen auf den maximalen Tripeln.
"""
import itertools
import numpy as np

e1 = np.array([1, 0, 0.])
poles = {"Materie": (e1, 0 * e1), "Tachyon": (0 * e1, e1),
         "Seite+": (e1 / np.sqrt(2), e1 / np.sqrt(2)), "Seite-": (e1 / np.sqrt(2), -e1 / np.sqrt(2)),
         "selbstdual": (1j * e1, e1), "antiselbstdual": (-1j * e1, e1)}
maps = {"R": lambda E, B: (-B, E), "T": lambda E, B: (E, -B), "J_B": lambda E, B: (B, E)}


def chi(E, B):
    p, m = E + 1j * B, E - 1j * B
    sp, sm = np.dot(p, p), np.dot(m, m)
    rp = np.sqrt(sp + 0j)
    rm = np.conj(rp) if abs(sm - np.conj(sp)) < 1e-12 else np.sqrt(sm + 0j)   # vertraegliche Wahl fuer reelle Felder
    v = np.array([rp, rm]); return v / np.linalg.norm(v)


C = {k: chi(*f) for k, f in poles.items()}

# (1) Auf chi wirken R, T, J_B als halbe Drehungen um die Achsen z (Helizitaet), x (Re s), y (Im s), d.h. als
#     sigma_z, sigma_x, sigma_y bis auf Phase. Konsistenz mit der Feldwirkung an den sechs Polen und an 200 reellen Feldern.
PAULI = {"R": np.diag([1, -1]).astype(complex), "T": np.array([[0, 1], [1, 0]], complex),
         "J_B": np.array([[0, -1j], [1j, 0]])}
rng = np.random.default_rng(16)
print("(1) Frame-Abbildungen auf chi und ihre Eigenzustaende")
for name, f in maps.items():
    M = PAULI[name]
    tests = list(poles.values()) + [(rng.normal(size=3), rng.normal(size=3)) for _ in range(200)]
    cons = max(1 - abs(np.vdot(M @ chi(E, B), chi(*f(E, B)))) for E, B in tests)
    w, V = np.linalg.eigh(M)
    eig = [k for j in range(2) for k in poles if abs(abs(np.vdot(V[:, j], C[k])) - 1) < 1e-9]
    print(f"    {name:4s} = sigma_{ {'R': 'z', 'T': 'x', 'J_B': 'y'}[name] }: Abweichung von der Feldwirkung {cons:.1e};"
          f" Eigenzustaende (genau zwei Strahlen) = {eig}")

# (2) Teilmengen ohne orthogonales Paar
names = list(poles)
ov = {(a, b): abs(np.vdot(C[a], C[b])) ** 2 for a in names for b in names}
good = [S for r in range(1, 7) for S in itertools.combinations(names, r)
        if all(ov[(a, b)] > 1e-9 for a, b in itertools.combinations(S, 2))]
mx = max(len(S) for S in good)
tri = [S for S in good if len(S) == mx]
print(f"\n(2) Teilmengen ohne orthogonales Paar: {len(good)}; groesste Groesse {mx}; Anzahl maximaler Mengen {len(tri)}")
for S in tri:
    v = [C[k] for k in S]
    G = np.array([[abs(np.vdot(a, b)) for b in v] for a in v])
    ph = np.angle(np.vdot(v[0], v[1]) * np.vdot(v[1], v[2]) * np.vdot(v[2], v[0]))
    print(f"    {S}: Ueberlappungen^2 {sorted({round(ov[(a, b)], 6) for a, b in itertools.combinations(S, 2)})},"
          f" K = {np.trace(G @ G) / np.trace(G) ** 2:.6f}, Phase/pi = {ph / np.pi:+.3f}")

# (3) Bahnen der Frame-Abbildungen auf den maximalen Tripeln
def image(S, f):
    out = []
    for k in S:
        c = chi(*f(*poles[k])); out.append(next(n for n in names if abs(abs(np.vdot(c, C[n])) - 1) < 1e-9))
    return tuple(sorted(out))
tri_s = [tuple(sorted(S)) for S in tri]
orbits, seen = [], set()
for S in tri_s:
    if S in seen: continue
    orb, front = {S}, [S]
    while front:
        X = front.pop()
        for f in maps.values():
            Y = image(X, f)
            if Y not in orb: orb.add(Y); front.append(Y)
    seen |= orb; orbits.append(orb)
print(f"\n(3) Bahnen der Frame-Abbildungen auf den {len(tri_s)} Tripeln: {len(orbits)} Bahnen, Groessen {[len(o) for o in orbits]}")
AX = {"Materie": 0, "Tachyon": 0, "Seite+": 1, "Seite-": 1, "selbstdual": 2, "antiselbstdual": 2}
def phase_ordered(S):
    v = [C[k] for k in sorted(S, key=lambda k: AX[k])]   # Reihenfolge x-Pol, y-Pol, z-Pol
    return round(np.angle(np.vdot(v[0], v[1]) * np.vdot(v[1], v[2]) * np.vdot(v[2], v[0])) / np.pi, 3)
for o in orbits:
    print(f"    Bahn {sorted(o)}: Phasen/pi (Ecken nach Achsen geordnet) {sorted({phase_ordered(S) for S in o})}")
