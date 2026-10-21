"""k35: Rechnung zur Vorab-Notiz H13 (Commit 645295f), Verfahren 1-4 der Notiz."""
import numpy as np

ETA_H = np.arctanh(1/np.sqrt(3))
F_PLUS, S_F = 0.9436, 0.0083                       # K39
eta_metric = np.diag([-1.0, 1, 1, 1])

def boost(w):
    """reiner Boost, der ein ruhendes Objekt auf Geschwindigkeit w bringt (passiv: Koordinaten des bewegten Frames)."""
    b = np.linalg.norm(w)
    if b < 1e-15:
        return np.eye(4)
    g = 1/np.sqrt(1-b*b); n = w/b
    L = np.eye(4)
    L[0, 0] = g; L[0, 1:] = L[1:, 0] = -g*b*n
    L[1:, 1:] += (g-1)*np.outer(n, n)
    return L

def four_vel(v):
    g = 1/np.sqrt(1-v@v); return np.concatenate(([g], g*v))

n = [np.array([np.cos(2*np.pi*k/3), np.sin(2*np.pi*k/3), 0.0]) for k in range(3)]
v = [np.tanh(ETA_H)*nk for nk in n]

# Frame-Abbildungen Labor -> Ruhesystem von Frame k; Uebergang k -> k+1 als reiner Boost in Koordinaten von k
L = [boost(v[0])]
for k in range(3):
    u_next = four_vel(v[(k+1) % 3])
    u_in_k = L[-1] @ u_next                         # 4-Geschwindigkeit des naechsten Frames, gesehen aus k
    w = u_in_k[1:]/u_in_k[0]                        # Relativgeschwindigkeit in Koordinaten von k
    L.append(boost(w) @ L[-1])
H = L[-1] @ np.linalg.inv(L[0])                     # Holonomie in Koordinaten von Frame 0

boostanteil = max(abs(H[0, 1:]).max(), abs(H[1:, 0]).max(), abs(H[0, 0]-1))
R = H[1:, 1:]
delta = np.arccos(np.clip((np.trace(R)-1)/2, -1, 1))
print("eta_H = %.6f, Geschwindigkeit je Frame %.6f" % (ETA_H, np.tanh(ETA_H)))
print("Boostanteil der Holonomie (soll 0): %.2e;  Orthogonalitaet: %.2e" % (boostanteil, abs(R@R.T-np.eye(3)).max()))
print("Wigner-Winkel delta = %.6f rad = %.4f Grad" % (delta, np.degrees(delta)))

# Gegenprobe: Flaeche des hyperbolischen Dreiecks mit Ecken u_k
u = [four_vel(vk) for vk in v]
ch = -(u[0] @ eta_metric @ u[1])                   # cosh der Seitenlaenge
cosA = ch/(1+ch)
area = np.pi - 3*np.arccos(cosA)
print("Gegenprobe: Seitenlaenge %.6f, Innenwinkel %.4f Grad, Flaeche (Defekt) %.6f rad" % (np.arccosh(ch), np.degrees(np.arccos(cosA)), area))

f13 = np.cos(delta)
z = (f13-F_PLUS)/S_F
print()
print("f13 = cos(delta) = %.5f  gegen f(+) = %.4f +- %.4f  ->  z = %+.1f" % (f13, F_PLUS, S_F, z))
print("Urteil nach Notiz:", "verträglich" if abs(z) < 2 else "Spannung" if abs(z) < 3 else "widerlegt (fuer diese Konstruktion)")
