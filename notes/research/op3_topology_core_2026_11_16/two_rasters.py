"""Zwei Walzenraster strukturell vergleichen (Erkundung, analytisch; keine Zahl wird mit einem Zielwert verglichen).

Triolenraster (r14): wirksame Walzen bei alpha = 30 k Grad; Viertelraster (r14.1(b)): alpha = 22.5 k Grad.  Auf chi als Bloch-Drehungen.
(1) erzeugte Gruppen (Ordnung), gemeinsame Elemente.
(2) Liegen sie in der Symmetriegruppe O des Oktanten (Wuerfelgruppe, 24 Drehungen)?  Enthalten sie die Frame-Abbildungen {1, R, T, J_B}?
(3) Dreierachsen: Drittelzyklus des Triolenrasters (Helizitaetsachse) gegen die Symmetrieachse des Oktanten (1,1,1); Winkel zwischen ihnen.
(4) Ist der Oktant (Ecken x, y, z) eine Bahn des Drittelzyklus?  Ist eine Bahn des Drittelzyklus mit Ueberlappung 1/2 ein Oktant?
"""
import itertools
import numpy as np

X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex)


def rotz(phi):
    return np.cos(phi / 2) * np.eye(2) - 1j * np.sin(phi / 2) * Z


def bloch_map(U):
    P = [X, Y, Z]
    return np.array([[0.5 * np.real(np.trace(P[i] @ U @ P[j] @ U.conj().T)) for j in range(3)] for i in range(3)])


def walzen(step_deg, n):
    return [bloch_map(rotz(2 * np.radians(step_deg * k)) @ Y @ rotz(-2 * np.radians(step_deg * k))) for k in range(n)]


def closure(gens):
    G = [np.eye(3)]
    frontier = [np.eye(3)]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                m = h @ g
                if not any(np.allclose(m, x, atol=1e-9) for x in G):
                    G.append(m); new.append(m)
        frontier = new
    return G


def member(m, G):
    return any(np.allclose(m, x, atol=1e-9) for x in G)


TRI = closure(walzen(30, 6)); QUA = closure(walzen(22.5, 8))
common = [g for g in TRI if member(g, QUA)]
print(f"(1) Triolenraster erzeugt eine Gruppe der Ordnung {len(TRI)}, Viertelraster eine der Ordnung {len(QUA)}; gemeinsam: {len(common)} Elemente")
both = closure(walzen(30, 6) + walzen(22.5, 8))
print(f"    beide zusammen: Ordnung {len(both)}")
# Wuerfelgruppe O: alle Permutationsmatrizen mit Vorzeichen und det +1
O = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3))
        for i, j in enumerate(perm): M[i, j] = signs[i]
        if np.isclose(np.linalg.det(M), 1): O.append(M)
print(f"(2) |O| = {len(O)}; Viertelraster in O: {all(member(g, O) for g in QUA)}; Triolenraster in O: {all(member(g, O) for g in TRI)}")
frames = {"1": np.eye(3), "R (sigma_z)": bloch_map(Z), "T (sigma_x)": bloch_map(X), "J_B (sigma_y)": bloch_map(Y)}
print("    Frame-Abbildungen im Viertelraster:", {k: member(v, QUA) for k, v in frames.items()})
print("    Frame-Abbildungen im Triolenraster:", {k: member(v, TRI) for k, v in frames.items()})
print("    gemeinsame Elemente sind:", ["1" if np.allclose(g, np.eye(3)) else ("J_B" if np.allclose(g, frames["J_B (sigma_y)"]) else "anderes") for g in common])
zc = np.ones(3) / np.sqrt(3); ez = np.array([0, 0, 1.0])
print(f"(3) Winkel zwischen der Dreierachse des Triolenrasters (Helizitaetsachse) und der Oktantenachse (1,1,1): "
      f"{np.degrees(np.arccos(ez @ zc)):.4f} Grad (magischer Winkel arccos(1/sqrt3) = {np.degrees(np.arccos(1/np.sqrt(3))):.4f})")
C3 = closure([bloch_map(rotz(2 * np.pi / 3))])
octant = [np.array(v, float) for v in ([0, 0, 1], [1, 0, 0], [0, 1, 0])]
is_orbit = any(all(any(np.allclose(g @ octant[0], v) for g in C3) for v in octant) for _ in [0])
print(f"(4) Ist der Oktant eine Bahn des Drittelzyklus um die Helizitaetsachse? {is_orbit}"
      f"  (die z-Ecke ist Fixpunkt: {np.allclose(C3[1] @ octant[0], octant[0])})")
th = np.arccos(1 / np.sqrt(3))
orb = [np.array([np.sin(th) * np.cos(2 * np.pi * k / 3), np.sin(th) * np.sin(2 * np.pi * k / 3), np.cos(th)]) for k in range(3)]
G = np.array([[a @ b for b in orb] for a in orb])
print(f"    Bahn des Drittelzyklus mit Kegelwinkel 54.74 Grad (Ueberlappung 1/2): paarweise orthogonale Bloch-Vektoren: {np.allclose(G - np.eye(3), 0, atol=1e-12)}"
      " -> ein Oktant, aber um die Helizitaetsachse gedreht, nicht der Oktant der Frame-Abbildungen")
