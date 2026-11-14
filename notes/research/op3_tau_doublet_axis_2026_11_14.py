"""Erkundung (14.11.2026, nicht blind): Gibt es auf dem tau-Dublett von O^3 eine zweizaehlige Achse unter dem
magischen Winkel? Rueckwaertssuche: erst die Bedingung, dann die vorhandenen Operationen dagegen.

Slotraum einer Teilchenart: C^3 (Schur). tau = Zyklus. Dublett = Fourier-Moden (omega, omegabar), Singulett = sym.
(1) Monomiale Slotoperationen (Permutation mal Slot-Phasen aus den 12. Einheitswurzeln; enthaelt S3, die Klein-Gruppe
    von A4 und Slot-Phasen aus e7): welche erhalten 2 + 1, und welche Achsen haben sie auf dem Dublett?
(2) A4 (Vorzeichenwechsel und Zyklus): erhaelt es die Zerlegung 2 + 1?
(3) Das gesuchte Element g: zweizaehlig, Achse unter cos = 1/sqrt3 zur tau-Achse. Gestalt im Slotraum; <tau, g>.
(4) Gegenprobe Weg A: R_e7, R_e8, R_e15 auf dem Slotpaar S = O + O e8 sind monomial; R_h ist es nicht.
Aufruf: python op3_tau_doublet_axis_2026_11_14.py
"""
import importlib.util
import itertools
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("fs", os.path.join(HERE, "op3_family_su2_right_action_2026_11_14.py"))
fs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fs)

W = np.exp(2j * np.pi / 3)
CYC = np.zeros((3, 3)); CYC[0, 1] = CYC[1, 2] = CYC[2, 0] = 1                    # tau(x, y, z) = (y, z, x)
F = np.array([[1, 1, 1], [1, W, W ** 2], [1, W ** 2, W]]).T / np.sqrt(3)         # Spalten: sym, Mode a, Mode b
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1])]


def split_ok(M):
    """Erhaelt M die Zerlegung sym + Dublett?"""
    Mm = F.conj().T @ M @ F
    return np.linalg.norm(Mm[0, 1:]) < 1e-9 and np.linalg.norm(Mm[1:, 0]) < 1e-9


def doublet(M):
    return (F.conj().T @ M @ F)[1:, 1:]


def axis_cos(U, zaxis):
    """|cos| zwischen der Bloch-Drehachse von U und zaxis; None fuer Vielfache der Eins; dazu Drehwinkel in Grad."""
    V = U / np.sqrt(np.linalg.det(U))
    n = np.array([np.imag(np.trace(V @ s)) / 2 for s in SIG])
    nn = np.linalg.norm(n)
    if nn < 1e-9:
        return None, 0.0
    ang = 2 * np.degrees(np.arccos(np.clip(abs(np.real(np.trace(V)) / 2), 0, 1)))
    return abs(n @ zaxis) / nn, ang


if __name__ == "__main__":
    tm = doublet(CYC.astype(complex))
    nz = np.array([np.imag(np.trace(tm / np.sqrt(np.linalg.det(tm)) @ s)) / 2 for s in SIG])
    zaxis = nz / np.linalg.norm(nz)
    print(f"Kontrolle: tau erhaelt 2 + 1: {split_ok(CYC)}; tau auf dem Dublett = diag{np.round(np.diag(tm), 4).tolist()}, "
          f"Achse {np.round(zaxis, 4).tolist()}")

    print("\n(1) Monomiale Slotoperationen: Permutation mal diag(Phasen), Phasen aus den 12. Einheitswurzeln")
    roots = [np.exp(2j * np.pi * k / 12) for k in range(12)]
    perms = [np.eye(3)[list(p)] for p in itertools.permutations(range(3))]
    total = keep = 0
    stats = {}
    images = set()
    for Pm in perms:
        for ph in itertools.product(roots, repeat=3):
            M = np.diag(ph) @ Pm
            total += 1
            if not split_ok(M):
                continue
            keep += 1
            U = doublet(M)
            V = U / np.sqrt(np.linalg.det(U))
            V = V * np.sign(np.real(V.ravel()[np.argmax(np.abs(V.ravel()))]) or 1)
            images.add(tuple(np.round(np.concatenate([np.abs(V).ravel(), [abs(np.trace(V))]]), 5)))
            c, ang = axis_cos(U, zaxis)
            key = ("Eins" if c is None else f"{ang:.0f} Grad, |cos| = {c:.4f}")
            stats[key] = stats.get(key, 0) + 1
    print(f"    {total} Elemente, davon erhalten {keep} die Zerlegung 2 + 1")
    for k, v in sorted(stats.items()):
        print(f"    Wirkung auf dem Dublett: {k}: {v} Elemente")
    print(f"    magischer Winkel (|cos| = {1 / np.sqrt(3):.4f}) kommt vor: {any('0.5774' in k for k in stats)}")

    print("\n(2) A4 auf den Slots: Klein-Gruppe der Vorzeichenwechsel und der Zyklus")
    klein = [np.diag(s) for s in ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))]
    print(f"    Vorzeichenwechsel, die 2 + 1 erhalten: {sum(split_ok(k) for k in klein)} von 4 (nur die Eins)")
    sym = F[:, 0]
    print(f"    <sym| diag(1,-1,-1) |sym> = {np.real(np.vdot(sym, klein[1] @ sym)):.4f} (Betrag 1 waere noetig)")

    print("\n(3) Das gesuchte Element: g = i (n . sigma) auf dem Dublett, n unter cos = 1/sqrt3 zur tau-Achse")
    perp = np.cross(zaxis, [1.0, 0, 0]); perp /= np.linalg.norm(perp)
    for az in (0.0, np.pi / 4, np.pi / 2):
        e1 = np.cos(az) * perp + np.sin(az) * np.cross(zaxis, perp)
        n = zaxis / np.sqrt(3) + np.sqrt(2 / 3) * e1
        g2 = 1j * sum(n[k] * SIG[k] for k in range(3))
        Mm = np.eye(3, dtype=complex); Mm[1:, 1:] = g2
        G = F @ Mm @ F.conj().T
        nzc = int(np.sum(np.abs(G) > 1e-9))
        mods = sorted({round(float(a), 4) for a in np.abs(G).ravel()})
        # Gruppe aus tau und g auf dem Dublett
        gens = [tm, g2]
        grp = [np.eye(2, dtype=complex)]
        frontier = list(grp)
        while frontier and len(grp) < 200:
            new = []
            for a in frontier:
                for b in gens:
                    c = a @ b
                    if not any(np.allclose(c, x) for x in grp):
                        grp.append(c); new.append(c)
            frontier = new
        print(f"    Azimut {np.degrees(az):5.1f} Grad: g im Slotraum hat {nzc} von 9 Eintraegen ungleich null "
              f"(monomial: 3), Betraege {mods}; Ordnung von <tau, g> auf dem Dublett: {len(grp)}")
    print("    (Ordnung 24: tau und g erzeugen auf dem Dublett die binaere Tetraedergruppe 2T)")

    print("\n(4) Gegenprobe Weg A: Slotpaar S = O + O e8 (Koordinaten 0..7 und 8..15)")
    su, R = fs.su, fs.R
    def slot_blocks(M):
        b = [[np.linalg.norm(M[0:8, 0:8]), np.linalg.norm(M[0:8, 8:16])],
             [np.linalg.norm(M[8:16, 0:8]), np.linalg.norm(M[8:16, 8:16])]]
        return np.round(b, 3).tolist()
    for name, x in (("R_e7", su(7)), ("R_e8", su(8)), ("R_e15", su(15))):
        print(f"    {name:5s}: Blocknormen [[11, 12], [21, 22]] = {slot_blocks(R(x))}")
    h = np.zeros(16); h[[0, 7, 8, 15]] = 0.5
    print(f"    R_h  : Blocknormen = {slot_blocks(R(h))} (Summe mit halbzahligen Koeffizienten, nicht monomial)")
