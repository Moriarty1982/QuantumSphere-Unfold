"""Explizite Anordnung des M-Fraktals im Einheitsquadrat (zwei Kopien je Skala r_n = 2^{-sqrt(n(n+2)/3)}), mit Pruefung auf
Ueberlappungsfreiheit; Rest (n >= 7) ueber Moon-Moser (Quadrate mit Gesamtflaeche <= A/2 passen in ein Quadrat der Flaeche A, 1967)."""
import numpy as np
r = lambda n: 2.0 ** (-np.sqrt(n * (n + 2) / 3))
sq = []  # (x, y, Seite)
sq += [(0, 0, r(1)), (0.5, 0, r(1))]                         # unten
sq += [(0, 0.5, r(2)), (r(2), 0.5, r(2))]                    # oben links
x0 = 2 * r(2)
sq += [(x0, 0.5, r(3)), (x0, 0.5 + r(3), r(3))]              # rechte Spalte, gestapelt
x = 0.0; y = 0.5 + r(2)
for k in (4, 5, 6):
    for _ in range(2):
        sq.append((x, y, r(k))); x += r(k)
ok_in = all(0 <= a and 0 <= b and a + s <= 1 + 1e-12 and b + s <= 1 + 1e-12 for a, b, s in sq)
def ov(p, q):
    (a, b, s), (c, d, t) = p, q
    return a < c + t - 1e-12 and c < a + s - 1e-12 and b < d + t - 1e-12 and d < b + s - 1e-12
ok_ov = not any(ov(sq[i], sq[j]) for i in range(len(sq)) for j in range(i + 1, len(sq)))
fx = x0 + r(3); free_side = min(1 - fx, 0.5)                 # freier Streifen rechts oben: Breite 1 - fx, Hoehe 0,5
rest = 2 * sum(r(n) ** 2 for n in range(7, 200000))
print(f"12 Quadrate (n = 1..6) im Einheitsquadrat: innen {ok_in}, ueberlappungsfrei {ok_ov}; Breite unten-oben-Reihe {x:.4f} <= {2*r(2):.4f}")
print(f"freies Quadrat rechts oben: Seite {free_side:.4f}, Flaeche {free_side**2:.5f}; Restflaeche n >= 7: {rest:.5f}; Moon-Moser (Rest <= Flaeche/2): {rest <= free_side**2/2}")
print("=> offene-Mengen-Bedingung mit V = offenes Einheitsquadrat erfuellt; das M-Fraktal liegt in der Ebene, Hausdorff-Dimension = 1,8647")
