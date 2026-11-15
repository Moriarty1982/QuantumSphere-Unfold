"""Nachtrag zu (B3): Hat Helizitaetsneutralitaet (b_y = 0, lineare Polarisation) im Bestand eine ausgezeichnete Rolle?
(Erkundung, nicht blind.)
(1) Frame-Abbildungen auf b_y (r16.2(a)): R erhaelt b_y, T und J_B kehren es um.  Einzige von allen dreien erhaltene
    Helizitaet: b_y = 0.
(2) Fuer eine ebene Welle ist die Helizitaetsbilanz boost-invariant: Beide Helizitaetsanteile erhalten denselben
    Doppler-Faktor; linear bleibt linear.  Fuer allgemeine komplexe Amplituden nicht (r16.2(d)).
"""
import numpy as np

rng = np.random.default_rng(1119)


def b_y(E, B):
    return -2 * np.imag(np.conj(E) @ B) / (np.vdot(E, E).real + np.vdot(B, B).real)


def boost(E, B, v, n):
    n = n / np.linalg.norm(n); g = 1 / np.sqrt(1 - v * v); vv = v * n
    return (g * (E + np.cross(vv, B)) - (g - 1) * np.dot(E, n) * n,
            g * (B - np.cross(vv, E)) - (g - 1) * np.dot(B, n) * n)


maps = {"R": lambda E, B: (-B, E), "T": lambda E, B: (E, -B), "J_B": lambda E, B: (B, E)}
E, B = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
print("(1) b_y =", round(b_y(E, B), 4), "->", {k: round(b_y(*f(E, B)), 4) for k, f in maps.items()})

k = np.array([0, 0, 1.0])
dev_lin = dev_ell = 0.0; gen = []
for _ in range(500):
    v, n = rng.uniform(0.1, 0.95), rng.normal(size=3)
    for pol, store in (((1, 0), "lin"), ((1, 0.4j), "ell")):
        E = np.array([pol[0], pol[1], 0], complex); B = np.cross(k, E)
        b0 = b_y(E, B); b1 = b_y(*boost(E, B, v, n))
        if store == "lin": dev_lin = max(dev_lin, abs(b1))
        else: dev_ell = max(dev_ell, abs(b1 - b0))
    Eg, Bg = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
    gen.append(abs(b_y(*boost(Eg, Bg, v, n)) - b_y(Eg, Bg)))
print(f"(2) ebene Welle linear: |b_y| nach Boost <= {dev_lin:.1e}; elliptisch: |Delta b_y| <= {dev_ell:.1e};"
      f" allgemeine Amplituden: Median |Delta b_y| = {np.median(gen):.3f}")
