"""Wechselnde Walze (Erkundung, analytisch, numerisch bestaetigt; kein Zielwert).

Bestand: Kicks bei jedem Durchgang von arg s durch triole u J_B(triole), also alle 30 Grad Dualitaetswinkel, sechs je Schlag (r13.1, r14.1);
wirksame Umkehrwalze in der Walzenstellung alpha: R_alpha^{-1} J_B R_alpha (r02.5); auf chi: J_B = sigma_y, R_alpha dreht um die Helizitaetsachse
um -2 alpha (op1_u1_check).
(1) Folge der wirksamen Umkehrwalzen M_k fuer alpha_k = 30 k Grad: Achsen auf chi.
(2) Produkte aufeinanderfolgender Walzen: Drehwinkel und Achse; Vergleich mit dem Zeitzyklus r16.9 (Drittel der Periode = 120 Grad um die
    Helizitaetsachse).
(3) Bahn der Zyklusachse z_c und der Oktant-Ecken unter der Kick-Folge (Transport-Lesart: jede Walze bildet ab).
"""
import numpy as np

X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex)


def rotz(phi):
    return np.cos(phi / 2) * np.eye(2) - 1j * np.sin(phi / 2) * Z


def R_dual(a):
    return rotz(-2 * a)


def bloch_map(U):
    P = [X, Y, Z]
    return np.array([[0.5 * np.real(np.trace(P[i] @ U @ P[j] @ U.conj().T)) for j in range(3)] for i in range(3)])


def axis_angle(M):
    w, V = np.linalg.eig(M)
    ax = np.real(V[:, np.argmin(np.abs(w - 1))]); ax /= np.linalg.norm(ax)
    ang = np.degrees(np.arccos(np.clip((np.trace(M) - 1) / 2, -1, 1)))
    return ax, ang


Ms = []
for k in range(6):
    a = np.radians(30 * k)
    M = bloch_map(R_dual(-a) @ Y @ R_dual(a)); Ms.append(M)
    ax, ang = axis_angle(M)
    print(f"(1) Kick {k}: alpha = {30*k:3d} Grad, Halbdrehung ({ang:.0f} Grad) um Achse {np.round(ax, 4)} (Winkel in der Aequatorebene "
          f"{np.degrees(np.arctan2(ax[1], ax[0])) % 180:.0f} Grad)")
for k in range(5):
    P = Ms[k + 1] @ Ms[k]
    ax, ang = axis_angle(P)
    print(f"(2) M_{k+1} M_{k}: Drehung um {np.round(ax, 4)} um {ang:.1f} Grad")
P3 = Ms[2] @ Ms[1] @ Ms[0]
print(f"    M2 M1 M0: det {np.linalg.det(P3):+.0f}, Achse/Winkel {[np.round(x, 4) for x in axis_angle(P3)]}")
zc = np.ones(3) / np.sqrt(3)
p = zc.copy(); orbit = [p]
for k in range(12):
    p = Ms[k % 6] @ p; orbit.append(p)
print("(3) Bahn von z_c unter der Kick-Folge:", [np.round(q * np.sqrt(3), 3).tolist() for q in orbit[:7]])
oct_c = {tuple(s) for s in [(a, b, c) for a in (1, -1) for b in (1, -1) for c in (1, -1)]}
hits = [tuple(np.round(q * np.sqrt(3)).astype(int)) in oct_c and np.allclose(np.abs(q * np.sqrt(3)), 1, atol=1e-9) for q in orbit[:7]]
print("    alle Bahnpunkte Oktantenmitten (+-1, +-1, +-1)/sqrt3:", all(hits))
print("    Abstand des naechsten Bahnpunkts zu -z_c (Grad):", round(min(np.degrees(np.arccos(np.clip(q @ -zc, -1, 1))) for q in orbit[1:7]), 3))

# (4) Vergleich: Viertelraster (r14.1(b): 45 Grad in arg s, also 22.5 Grad Dualitaetswinkel)
Q = []
for k in range(4):
    a = np.radians(22.5 * k)
    M = bloch_map(R_dual(-a) @ Y @ R_dual(a)); Q.append(M)
    ax, ang = axis_angle(M)
    print(f"(4) Viertelraster Kick {k}: alpha = {22.5*k:5.1f} Grad, Achse {np.round(ax, 4)}, z_c -> {np.round(M @ zc * np.sqrt(3), 3).tolist()}")
ax, ang = axis_angle(Q[1] @ Q[0])
print(f"    Produkt aufeinanderfolgender Walzen im Viertelraster: Drehung um {np.round(ax, 4)} um {ang:.1f} Grad")
