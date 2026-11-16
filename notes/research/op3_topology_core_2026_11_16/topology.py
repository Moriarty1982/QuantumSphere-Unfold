"""Topologische Analyse des Kern-Bildes (Erkundung, analytisch, numerisch bestaetigt; keine Zielwerte ausgewertet).

(1) Umkehrwalze Theta = i sigma_y K: bildet den koharenten Zustand bei n auf den bei -n ab (bis auf Phase), Theta^2 = -1.
(2) Theta als Symmetrie der Verbindung: Bargmann-Phase des Antipodendreiecks = -Phase des Dreiecks (natuerliche Hopf-Verbindung);
    mit der Orientierungsumkehr der Antipodenabbildung heisst das: Flussdichte F(-n) = F(n).
(3) Borsuk-Ulam: Auf dem trivialen Buendel gibt es keine Struktur Theta mit Theta^2 = -1 ueber der Antipodenabbildung
    (sie braeuchte eine ungerade stetige Abbildung S^2 -> S^1).  Numerisch: Kandidaten f(n) = exp(i k . n)-artige Felder verletzen f(-n) = -f(n).
(4) Rationalitaet: Fluss eines Oktanten = (1/8) * 2 pi; Verhaeltnis phi/(2 pi) fuer pi/4 und fuer 2/3.
"""
import numpy as np

sy = np.array([[0, -1j], [1j, 0]])


def coh(n):
    n = np.asarray(n, float) / np.linalg.norm(n)
    th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def theta(v):
    return 1j * sy @ np.conj(v)


def phase(g):
    return np.angle(np.vdot(g[0], g[1]) * np.vdot(g[1], g[2]) * np.vdot(g[2], g[0]))


rng = np.random.default_rng(4)
ok1 = ok2 = True
for _ in range(300):
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    v = theta(coh(n)); w = coh(-n)
    ok1 &= abs(abs(np.vdot(w, v)) - 1) < 1e-12
    ok1 &= np.allclose(theta(theta(coh(n))), -coh(n))
    tri = rng.normal(size=(3, 3)); tri /= np.linalg.norm(tri, axis=1)[:, None]
    p = phase([coh(t) for t in tri]); pa = phase([coh(-t) for t in tri])
    ok2 &= abs(p + pa) < 1e-10 or abs(abs(p + pa) - 2 * np.pi) < 1e-10
print(f"(1) Theta bildet n auf -n ab und Theta^2 = -1 (300 Punkte): {ok1}")
print(f"(2) Phase(Antipodendreieck) = -Phase(Dreieck) (300 Dreiecke): {ok2}  -> mit Orientierungsumkehr: F(-n) = F(n)")
# (3) ungerade Abbildung S^2 -> S^1 existiert nicht: Pruefe, dass f(n) = exp(i a.n) (gerade/ungerade Mischung) nie f(-n) = -f(n) ueberall erfuellt
bad = []
for _ in range(200):
    a = rng.normal(size=3) * 3
    pts = rng.normal(size=(500, 3)); pts /= np.linalg.norm(pts, axis=1)[:, None]
    f = np.exp(1j * pts @ a); fm = np.exp(-1j * pts @ a)
    bad.append(np.max(np.abs(f + fm)))
print(f"(3) Borsuk-Ulam-Probe: max |f(n) + f(-n)| bei 200 Kandidaten stets > 0 (Minimum {min(bad):.3f}); "
      "allgemein folgt es aus Borsuk-Ulam (jede stetige Abbildung S^2 -> R^2 hat ein Antipodenpaar mit gleichem Wert).")
print(f"(4) Oktant: pi/4 / (2 pi) = {np.pi/4/(2*np.pi):.6f} = 1/8;  2/3 / (2 pi) = {2/3/(2*np.pi):.6f} (= 1/(3 pi), irrational)")
