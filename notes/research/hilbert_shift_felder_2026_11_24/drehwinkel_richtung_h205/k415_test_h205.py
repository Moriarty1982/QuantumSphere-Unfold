"""k415 (Test H205): Ist die Richtung der theta13-Korrektur geometrisch erzwungen?
Prueft exakt die k373-Beobachtung: die Achsenvektoren der A-ungeraden antisymmetrischen
Generatoren K1,K2 (Ladungsrichtung) liegen in der Ebene senkrecht zur festen Baum-Spalte
v0=(1,0,1)/sqrt2, und (K1+K2)/sqrt2 halbiert die beiden uebrigen Baum-Richtungen (45 Grad).
Maschinerie (Nhat, T, eig_sorted) aus k370/k371.
Aufruf aus diesem Ordner: python3 k415_test_h205.py > k415_out.txt
"""
import numpy as np

# ---- Maschinerie aus k370 (Nhat, T, eig_sorted) ----
src = open("../mischung_h174/k370_test_h174.py").read().split('print("== Kontrolle')[0]
ns = {}; exec(src, ns)
Nhat, eig_sorted, T = ns["Nhat"], ns["eig_sorted"], ns["T"]
r2 = np.sqrt(2)

def E(i, j):
    M = np.zeros((3, 3)); M[i, j] = 1; return M

# A-ungerade antisymmetrische (Ladungs-)Generatoren wie in k371 (DIRS["K-1"], DIRS["K-2"]):
# K = i * (reelle antisymmetrische Matrix A).  Wir arbeiten mit A (der reelle Teil / i).
A1 = (E(0, 2) - E(2, 0))                                   # zu K-1
A2 = (-E(0, 1) + E(1, 0) + E(1, 2) - E(2, 1)) / r2         # zu K-2

def axis(A):
    """Dualvektor a zu reeller antisymmetrischer Matrix A:  A_ij = eps_ijk a_k."""
    return np.array([A[2, 1], A[0, 2], A[1, 0]])

a1, a2 = axis(A1), axis(A2)

print("=" * 76)
print("H205  Achsenvektoren der A-ungeraden antisymmetrischen Generatoren")
print("=" * 76)
print(f"  axis(K1) a1 = {a1}")
print(f"  axis(K2) a2 = {a2}   (|a2| = {np.linalg.norm(a2):.6f})")

# ---- Baum-Richtungen: Eigenvektoren von Nhat bei delta_nu = pi/6 (b=0) ----
v, U = eig_sorted(Nhat(np.pi / 6, 1))
print("\n  Neutrino-Baum-Eigenvektoren bei delta_nu = pi/6 (Eigenwerte |.|-sortiert):")
for k in range(3):
    print(f"    EW {v[k]:+.6f}:  {np.round(U[:, k], 6)}")
# feste Spalte v0 = (1,0,1)/sqrt2 identifizieren
v0 = np.array([1.0, 0.0, 1.0]) / r2
ov = [abs(abs(U[:, k] @ v0) - 1) < 1e-9 for k in range(3)]
print(f"  Feste Spalte v0 = (1,0,1)/sqrt2 ist Baum-Eigenvektor Nr. {ov.index(True) if any(ov) else '—'}")
# die beiden uebrigen Baum-Richtungen
rest = [U[:, k] for k in range(3) if not ov[k]]
u_p, u_m = rest[0], rest[1]
print(f"  uebrige Baum-Richtungen: u+ = {np.round(u_p,6)},  u- = {np.round(u_m,6)}")

print("\n" + "=" * 76)
print("H205 (a)  Orthogonalitaet: liegen a1, a2 in der Ebene senkrecht zu v0?")
print("=" * 76)
print(f"  a1 . v0 = {a1 @ v0:+.3e}")
print(f"  a2 . v0 = {a2 @ v0:+.3e}")
ortho = max(abs(a1 @ v0), abs(a2 @ v0))
print(f"  max |a . v0| = {ortho:.2e}  -> {'EXAKT orthogonal' if ortho < 1e-12 else 'NICHT orthogonal'}")

print("\n" + "=" * 76)
print("H205 (5)  Strukturgrund: spannt {a1,a2} genau die Ebene senkrecht zu v0 auf?")
print("=" * 76)
# Rang von [a1,a2] und Projektion von v0 auf diesen Spann (soll 0)
M = np.vstack([a1, a2])
rank = np.linalg.matrix_rank(M, tol=1e-9)
# orthonormale Basis der Ebene senkrecht zu v0:
e1 = np.array([0.0, 1.0, 0.0]); e2 = np.cross(v0, e1)
plane = np.vstack([e1, e2 / np.linalg.norm(e2)])
# v0-Komponente in span{a1,a2}
P = M.T @ np.linalg.pinv(M @ M.T) @ M            # Projektor auf span{a1,a2}
v0_in_span = np.linalg.norm(P @ v0)
span_perp = np.linalg.norm(plane @ a1) , np.linalg.norm(plane @ a2)
# Liegt die ganze Ebene senkrecht zu v0 in span{a1,a2}? (Rang 2 + beide Ebenenbasisvektoren drin)
reco = np.linalg.norm((np.eye(3) - P) @ plane[0]) + np.linalg.norm((np.eye(3) - P) @ plane[1])
print(f"  Rang[{{a1,a2}}] = {rank}")
print(f"  ||Projektion von v0 auf span{{a1,a2}}|| = {v0_in_span:.2e} (soll 0)")
print(f"  ||(1-P)(Ebenenbasis)|| = {reco:.2e} (soll 0: Ebene⊥v0 ⊆ span{{a1,a2}})")
struktur = (rank == 2) and (v0_in_span < 1e-12) and (reco < 1e-12)
print(f"  -> span{{a1,a2}} = Ebene senkrecht zu v0 (exakt)? {'JA' if struktur else 'NEIN'}")
print("     D.h. die A-ungeraden antisymmetrischen Generatoren sind genau die Rotationen")
print("     mit Achse senkrecht zu v0 (die v0 kippen = theta13 oeffnen).")

print("\n" + "=" * 76)
print("H205 (b)  Halbierung: liegt (a1+a2)/sqrt2 mittig (45 Grad) zwischen u+ und u-?")
print("=" * 76)
def ang(x, y):
    c = abs(x @ y) / (np.linalg.norm(x) * np.linalg.norm(y))
    return np.degrees(np.arccos(min(c, 1.0)))
bis = (a1 + a2) / r2
# a1,a2 sind selbst (bis auf Vorzeichen/Norm) die beiden uebrigen Baum-Richtungen -> teste direkt
print(f"  a1 vs u+/u-: {ang(a1,u_p):.3f} / {ang(a1,u_m):.3f} Grad")
print(f"  a2 vs u+/u-: {ang(a2,u_p):.3f} / {ang(a2,u_m):.3f} Grad")
print(f"  (a1+a2)/sqrt2 vs u+ : {ang(bis,u_p):.4f} Grad")
print(f"  (a1+a2)/sqrt2 vs u- : {ang(bis,u_m):.4f} Grad")
diff = abs(ang(bis, u_p) - ang(bis, u_m))
print(f"  |Winkeldifferenz| = {diff:.2e} Grad  -> {'EXAKTE Halbierung' if diff < 1e-9 else 'keine exakte Halbierung'}")
print(f"  a1 . a2 = {a1 @ a2:+.2e} (orthogonal?) ; |a1|={np.linalg.norm(a1):.4f} |a2|={np.linalg.norm(a2):.4f}")

print("\n" + "=" * 76)
print("H205 (6)  Allgemeinheit: gilt (a) auch fuer v0 bei einem Versatz (b != 0)?")
print("=" * 76)
for x in (0.0, 0.0395773407, 0.0649):
    vv, UU = eig_sorted(Nhat(np.pi / 6 - x, 1))
    # feste Spalte: die, die bei x->0 nach (1,0,1)/sqrt2 geht = groesster EW-Zweig hier EW-Index via Ueberlapp
    k0 = int(np.argmax([abs(UU[:, k] @ v0) for k in range(3)]))
    vx = UU[:, k0]
    print(f"  x={x:.5f}: feste Spalte≈{np.round(vx,4)}  a1.vx={a1@vx:+.2e}  a2.vx={a2@vx:+.2e}")
print("  (bei x=0 exakt 0; bei x!=0 zeigt sich, ob die Orthogonalitaet an v0=(1,0,1)/sqrt2 haengt)")

print("\n" + "=" * 76)
print("H205 Entscheidung (Vorab-Kriterien)")
print("=" * 76)
K1 = (ortho < 1e-12) and struktur
print(f"  K1 (Richtung strukturell hergeleitet): (a) exakt orthogonal = {ortho<1e-12}, "
      f"Strukturgrund (5) = {struktur}  -> {'JA' if K1 else 'NEIN'}")
print(f"  (b) 45-Grad-Halbierung exakt = {diff<1e-9}")
print("\n  FAZIT H205:")
if K1:
    print("  - Die k373-Beobachtung ist EXAKT und strukturell erzwungen, kein Zufall:")
    print("    Die A-ungeraden antisymmetrischen (Ladungs-)Generatoren K1,K2 sind genau die")
    print("    Rotationen mit Achse senkrecht zu v0=(1,0,1)/sqrt2; ihre Achsen a1,a2 sind (bis auf")
    print("    Norm/Vorzeichen) selbst die beiden uebrigen Baum-Richtungen, daher halbiert")
    print("    (a1+a2)/sqrt2 sie exakt (45 Grad).")
    print("  - Damit ist die RICHTUNGSKLASSE der theta13-Korrektur im Ladungssektor geometrisch")
    print("    festgelegt (Ebene senkrecht zu v0). Frei bleiben: Winkel IN der Ebene, Staerke, Vorzeichen.")
    print("  - ABER (H175): die Daten verlangen den Ladungssektor nicht (erlaubter Raum 5-dim,")
    print("    symmetrische Terme bewegen theta12). K1 ist eine STRUKTURELLE Auszeichnung der")
    print("    Ladungsrichtung, keine Datenauszeichnung; H168-Spannung und Staerke bleiben offen.")
    print("  - Teilweise nicht blind: DASS die Zahlen ~45 Grad/senkrecht sind, war aus k373 bekannt;")
    print("    neu ist der exakte Nachweis UND der Strukturgrund (A-Symmetrie => Achse senkrecht v0).")
else:
    print("  - Die Beobachtung ist nicht exakt erzwungen; die Richtung bleibt frei (wie die")
    print("    Quark-Kopplungen nach H202/H204).")
