"""Erkundung (12.11.2026): rho-ungerade Platzkopplung aus der Trialitaetsform.

Nicht blind, kein Hypothesentest. Prueft die Aussagen der Notiz
op3_rho_odd_coupling_2026_11_12.md am Oktonionenfaktor von Modell I (r45):
Chiralitaet C = (1 + i L_e7)/2 auf jedem Platz, t(x,y,z) = Re((xy)z).
Aufruf: python op3_rho_odd_coupling_2026_11_12.py
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "v4_10_0_r32_r33", "llm"))
from k69_test_h17 import omul  # Konvention r04  # noqa: E402

E = np.eye(8)
rng = np.random.default_rng(20261112)


def cm(x, y):
    """Komplex-bilineare Fortsetzung des Oktonionenprodukts."""
    return (omul(x.real, y.real) - omul(x.imag, y.imag)
            + 1j * (omul(x.real, y.imag) + omul(x.imag, y.real)))


def T(x, y, z):
    return cm(cm(x, y), z)[0]


L7 = np.array([omul(E[7], E[j]) for j in range(8)]).T
R7 = np.array([omul(E[j], E[7]) for j in range(8)]).T
C = 0.5 * (np.eye(8) + 1j * L7)
Q8 = 0.5 * np.eye(8) - (1j / 6) * L7 - (1j / 3) * R7
w, V = np.linalg.eig(Q8)


def sector(q, proj):
    u, s, _ = np.linalg.svd(proj @ V[:, abs(w - q) < 1e-8], full_matrices=False)
    return [u[:, c] * np.sqrt(2) for c in range(u.shape[1]) if s[c] > 1e-8]


lep = sector(0, C)[0]                  # Lepton-Anteil im Bild von C (Q8 = 0)
quarks = sector(2 / 3, C)              # Farbtriplett im Bild von C (Q8 = 2/3)
cplx = lambda n: rng.normal(size=n) + 1j * rng.normal(size=n)


def lepton_plane():
    """Auf span_C(1, e7): t symmetrisch, kein Beitrag von h ausserhalb, sesquilinear null."""
    asym = out = 0.0
    for _ in range(500):
        a, b, c, d = cplx(4)
        x, y, h = a * E[0] + b * E[7], c * E[0] + d * E[7], cplx(8)
        asym = max(asym, abs(T(x, y, h) - T(y, x, h)))
        hperp = h.copy(); hperp[[0, 7]] = 0
        out = max(out, abs(T(x, y, hperp)))
    ses = max(abs(T(lep, lep.conj(), h)) + abs(T(lep.conj(), lep, h)) for h in (cplx(8) for _ in range(200)))
    return asym, out, ses, T(lep, lep, lep)


def quark_coupling():
    """alpha = T(u, conj w, h), beta = T(conj w, u, h) fuer reelles h = h0 + h7 e7."""
    err = off = 0.0
    for _ in range(300):
        h0, h7 = rng.normal(size=2)
        h = (h0 * E[0] + h7 * E[7]).astype(complex)
        al = np.array([[T(u, v.conj(), h) for v in quarks] for u in quarks])
        be = np.array([[T(v.conj(), u, h) for v in quarks] for u in quarks])
        err = max(err, abs(al - (-2 * (h0 - 1j * h7)) * np.eye(3)).max(),
                  abs(be - (-2 * (h0 + 1j * h7)) * np.eye(3)).max())
        mix = max(abs(T(lep, v.conj(), h)) + abs(T(v, lep.conj(), h)) for v in quarks)
        off = max(off, mix)
    return err, off


def chiral_h():
    out = {}
    for name, h in (("1+ie7", E[0] + 1j * E[7]), ("1-ie7", E[0] - 1j * E[7])):
        u = quarks[0]
        out[name] = (T(u, u.conj(), h), T(u.conj(), u, h))
    return out


def slot_matrix(a, h0, h7):
    """Platzmatrix a + alpha P + beta P^2 und ihre Brannen-Daten (Quarks)."""
    P = np.roll(np.eye(3), 1, axis=1)
    al, be = -2 * (h0 - 1j * h7), -2 * (h0 + 1j * h7)
    M = a * np.eye(3) + al * P + be * P @ P
    herm = abs(M - M.conj().T).max()
    ev = np.sort(np.linalg.eigvalsh(M))
    th = np.angle(al)
    br = np.sort([a + 2 * abs(al) * np.cos(th + 2 * np.pi * k / 3) for k in range(3)])
    return herm, abs(ev - br).max(), ev


def epsilon_part():
    """Alle drei Eintraege im Farbtriplett des Bildes: total antisymmetrisch."""
    q = quarks
    sym = max(abs(T(q[i], q[j], q[k]) + T(q[j], q[i], q[k])) for i in range(3) for j in range(3) for k in range(3))
    return sym, abs(T(q[0], q[1], q[2]))


if __name__ == "__main__":
    asym, out, ses, lll = lepton_plane()
    print(f"Lepton-Ebene: Antisymmetrie {asym:.1e}; h ausserhalb der Ebene traegt {out:.1e} bei;")
    print(f"  sesquilineare Kopplung T(l, conj l, h) fuer beliebiges h: {ses:.1e}; T(l,l,l) = {lll.real:.3f}")
    err, off = quark_coupling()
    print(f"Quarks, h = h0 + h7 e7 reell: alpha = -2(h0 - i h7), beta = -2(h0 + i h7), Fehler {err:.1e};"
          f" Lepton-Quark-Mischung {off:.1e}")
    for name, (al, be) in chiral_h().items():
        print(f"  chirales h = {name}: alpha = {al:.3f}, beta = {be:.3f}")
    herm, dev, ev = slot_matrix(3.0, 0.6, 0.25)
    print(f"Platzmatrix a=3, h0=0.6, h7=0.25: hermitesch {herm:.1e}, Brannen-Form {dev:.1e}, Eigenwerte {np.round(ev, 4)}")
    herm, dev, ev = slot_matrix(3.0, 0.6, 0.0)
    print(f"  mit h7 = 0: Eigenwerte {np.round(ev, 4)} (zwei gleich)")
    sym, eps = epsilon_part()
    print(f"Drei Farbtripletts: symmetrischer Anteil {sym:.1e}, |T(q1,q2,q3)| = {eps:.3f}")
