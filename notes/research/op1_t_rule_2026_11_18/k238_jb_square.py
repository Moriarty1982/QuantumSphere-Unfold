"""k238: OP1, T-Regel, Kandidat "J_B waehlt die Dubletts mit J_B^2 = -1" (Erkundung, nicht blind, Ausgang analytisch).

(a) Unter (A): J_B = exp(-i pi J_k) auf Spin j. Quadrat = exp(-2 pi i J_k) = (-1)^{2j}.
(b) Ohne (A), als Dualitaetsdrehung um pi/2 auf dem Extremdublett |j, +-j> (Helizitaet +-j):
    (b1) Erzeuger sign(Helizitaet) (Maxwell-artig: selbstdual * e^{i theta}): Phase i^{+-1}, Quadrat -1 fuer jedes j;
    (b2) Erzeuger Helizitaet selbst: Phase e^{+-i j pi/2}, Quadrat e^{+-i j pi} = (-1)^{2j} fuer halbzahlige j, +1/-1 je nach j.
Gesucht: Welche j erfuellen "Quadrat = -1"? Nur j = 1/2 waere der Kandidat.
"""
import numpy as np
from scipy.linalg import expm


def J(j):
    m = np.arange(j, -j - 1, -1.0)
    jp = np.diag(np.sqrt(j * (j + 1) - m[1:] * (m[1:] + 1)), 1)
    return (jp + jp.T) / 2, (jp - jp.T) / (2j), np.diag(m)


rows = []
for j in np.arange(0.5, 5.01, 0.5):
    Jx, Jy, Jz = J(j)
    a = all(np.allclose(expm(-1j * np.pi * Jk) @ expm(-1j * np.pi * Jk), -np.eye(len(Jz))) for Jk in (Jx, Jy, Jz))
    b1 = True  # i^2 = -1 und (-i)^2 = -1 fuer jedes j
    ph = np.exp(1j * j * np.pi / 2), np.exp(-1j * j * np.pi / 2)
    b2 = all(np.isclose(p * p, -1) for p in ph)
    rows.append((j, a, b1, b2))
print(" j    (a) exp(-i pi J_k)^2=-1   (b1) sign-Erzeuger   (b2) Helizitaets-Erzeuger")
for j, a, b1, b2 in rows:
    print(f"{j:4.1f}  {str(a):>22s}   {str(b1):>18s}   {str(b2):>22s}")
for lab, idx in (("(a)", 1), ("(b1)", 2), ("(b2)", 3)):
    sel = [r[0] for r in rows if r[idx]]
    print(f"{lab}: Quadrat = -1 fuer j = {sel}")
