"""k249: Anziehender Zyklus der Julia-Abbildung F_c(w) = 1/conj(w^2 + c), c = -1 + i*gamma (historischer Anhang C).
Erkundung 24.11.2026, nicht blind. Berichtet Periode und vorzeichenbehaftete Flaeche des Zyklus sowie den Einfanganteil
von Startpunkten innen (|w| < 3) und aussen (|w| ~ 1000). gamma = 0 hat den Zyklus -1 -> inf -> 0 auf der Achse (Flaeche 0);
dort meldet die numerische Suche keinen endlichen Zyklus.
Aufruf: python3 k249_julia_zyklus.py
"""
import warnings
import numpy as np

warnings.filterwarnings("ignore")
rng = np.random.default_rng(24112026)


def F(w, c):
    return 1 / np.conj(w * w + c)


def cycle(c):
    w = 0.1 + 0.1j
    for _ in range(5000):
        w = F(w, c)
    orb = [w]
    for _ in range(12):
        w = F(w, c)
        orb.append(w)
    p = next((k + 1 for k in range(12) if abs(orb[k + 1] - orb[0]) < 1e-9), None)
    if p is None or not np.isfinite(orb[0]):
        return None, None
    cyc = orb[:p]
    area = 0.5 * sum(cyc[i].real * cyc[(i + 1) % p].imag - cyc[(i + 1) % p].real * cyc[i].imag for i in range(p))
    return cyc, area


for g in [0.0, 0.05, -0.05, 0.237533]:
    c = -1 + 1j * g
    cyc, area = cycle(c)
    if cyc is None:
        print(f"gamma={g}: kein endlicher Zyklus gefunden (Zyklus ueber unendlich)")
        continue
    x = np.linspace(-3, 3, 301)
    inner = (x[:, None] + 1j * x[None, :]).ravel()
    th = rng.uniform(0, 2 * np.pi, 2000)
    outer = 1000 * np.exp(1j * th) * (1 + 0.5 * rng.random(2000))
    res = []
    for W in (inner, outer):
        Z = W.copy()
        for _ in range(3000):
            Z = F(Z, c)
        d = np.min(np.abs(Z[:, None] - np.array(cyc)[None, :]), axis=1)
        res.append(np.mean(d < 1e-6))
    print(f"gamma={g}: Periode {len(cyc)}, Flaeche {area:+.6f}, Einfang innen {res[0]:.4f}, aussen {res[1]:.4f}")
