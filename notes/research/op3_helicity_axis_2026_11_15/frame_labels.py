"""Drei Vorzeichen eines Feldes, Frame-Abbildungen als Kleinsche Vierergruppe, und keine Feldabbildung,
die die Achsen der invarianten Kugel zyklisch vertauscht (Erkundung, nicht blind).

Vorzeichen: a = sign Re s, b = sign Im s (reelle Felder), c = sign(|s+| - |s-|) (Helizitaet, zweigfrei).
"""
import numpy as np

rng = np.random.default_rng(1511)
R = lambda E, B: (-B, E)
T = lambda E, B: (E, -B)
JB = lambda E, B: (B, E)
maps = {"R": R, "T": T, "J_B": JB}

def s(E, B): z = E + 1j * B; return np.dot(z, z)
def spm(E, B): p, m = E + 1j * B, E - 1j * B; return np.dot(p, p), np.dot(m, m)

# (1) Tabelle: welche Vorzeichen kippt jede Abbildung?
print("(1) Vorzeichen (Re s, Im s, Helizitaet): + bleibt, - kippt")
for name, f in maps.items():
    ra, rb, rc = set(), set(), set()
    for _ in range(200):
        E, B = rng.normal(size=3), rng.normal(size=3)                       # reell: Re s, Im s
        s0, s1 = s(E, B), s(*f(E, B))
        ra.add(np.sign(s0.real) * np.sign(s1.real)); rb.add(np.sign(s0.imag) * np.sign(s1.imag))
        E, B = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
        h0 = np.subtract(*map(abs, spm(E, B))); h1 = np.subtract(*map(abs, spm(*f(E, B))))
        rc.add(np.sign(h0) * np.sign(h1))
    fmt = lambda r: "+" if r == {1.0} else ("-" if r == {-1.0} else str(r))
    print(f"    {name:4s}: Re s {fmt(ra)}, Im s {fmt(rb)}, Helizitaet {fmt(rc)}")

# (2) Eigenzustaende: der Pol, dessen Vorzeichen eine Abbildung erhaelt, ist ihr Eigenzustand (als Feldstrahl)
e1 = np.array([1, 0, 0.])
poles = {"T":   [("Materie", e1, 0 * e1), ("Tachyon", 0 * e1, e1)],
         "J_B": [("Seite +", e1 / np.sqrt(2), e1 / np.sqrt(2)), ("Seite -", e1 / np.sqrt(2), -e1 / np.sqrt(2))],
         "R":   [("selbstdual", 1j * e1, e1), ("antiselbstdual", -1j * e1, e1)]}
def same_ray(F, G):
    v, w = np.concatenate(F), np.concatenate(G)
    lam = np.vdot(v, w) / np.vdot(v, v); return np.linalg.norm(w - lam * v) < 1e-12, lam
for name, lst in poles.items():
    for lab, E, B in lst:
        ok, lam = same_ray((E, B), maps[name](E, B))
        others = [n for n in maps if n != name and same_ray((E, B), maps[n](E, B))[0]]
        print(f"(2) {lab:15s}: Eigenzustand von {name}: {ok} (Eigenwert {np.round(lam, 3)}); auch von {others or 'keiner anderen'}")

# (3) Lineare Abbildungen A der Indexebene (E,B) -> (aE+bB, cE+dB), geschrieben in der Basis F+, F-.
#     Sie sind auf chi nur wohldefiniert, wenn s+', s-' allein von s+, s- abhaengen. Test: zwei Felder mit gleichen
#     s+, s-, aber verschiedenem F+.F- (F- mit einer komplexen Drehung gegen F+ verdreht).
def cplx_rot(theta, axis):
    K = np.array([[0, -axis[2], axis[1]], [axis[2], 0, -axis[0]], [-axis[1], axis[0], 0]])
    w, V = np.linalg.eig(K); return (V @ np.diag(np.exp(theta * w)) @ np.linalg.inv(V))
def from_F(Fp, Fm): return (Fp + Fm) / 2, (Fp - Fm) / (2j)
def induced_ok(Ap):
    Fp, Fm = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
    O = cplx_rot(0.7 + 0.4j, np.array([0.3, -0.5, 0.8]))
    out = []
    for G in (Fm, O @ Fm):
        Gp, Gm = Ap[0, 0] * Fp + Ap[0, 1] * G, Ap[1, 0] * Fp + Ap[1, 1] * G
        out.append((np.dot(Gp, Gp), np.dot(Gm, Gm)))
    same_in = abs(np.dot(O @ Fm, O @ Fm) - np.dot(Fm, Fm)) < 1e-9
    return same_in and np.allclose(out[0], out[1])
cases = {"diagonal": np.diag([1.3 - 0.2j, 0.4 + 0.9j]), "vertauschend": np.array([[0, 0.7j], [1.1, 0]]),
         "nicht diagonal (Beispiel)": np.array([[1, -1j], [1, 1j]]) / np.sqrt(2),
         "allgemein": rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))}
for name, Ap in cases.items():
    print(f"(3) {name:32s}: auf chi wohldefiniert: {induced_ok(Ap)}")
gen = sum(induced_ok(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))) for _ in range(200))
print(f"    200 zufaellige A: wohldefiniert {gen}/200")
print("    Diagonale A: chi -> (a sqrt s+, d sqrt s-), Pole bleiben Pole; vertauschende A tauschen die Pole.")
print("    -> keine lineare Feldabbildung bringt die Helizitaetsachse auf den Aequator; kein Dreierzyklus der Achsen.")
