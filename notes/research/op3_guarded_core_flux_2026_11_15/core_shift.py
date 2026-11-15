"""Erkundung (nicht blind): bewachter Kern als Kappe auf der Bloch-Kugel, die Fluss ausschliesst statt ihn zu tragen.
Spin-1/2-Berry-Phase: Flussdichte 1/2 pro Steradiant, Gesamtfluss 2 pi (Chern-Zahl fest).
Szenario A: ausgeschlossener Fluss verlaesst das Dreieck ganz (z. B. ueber das Loch im S^3 bzw. zum Gegenpol).
Szenario B: ausgeschlossener Fluss verteilt sich gleichmaessig auf den Rest der Kugel (Minimum der Feldenergie in 2D).
Der Kern (Raumwinkel Omega) wandert auf einem Grosskreis von ausserhalb des Oktanten bis zur Zyklusachse."""
import json, math
import numpy as np
rng = np.random.default_rng(1511)
G = 0.2375330
pts = rng.normal(size=(2_000_000, 3)); pts /= np.linalg.norm(pts, axis=1)[:, None]
in_oct = (pts > 0).all(axis=1)
def cap_fraction_inside(center, omega):
    a = math.acos(1 - omega / (2 * math.pi))
    in_cap = pts @ center > math.cos(a)
    return (in_cap & in_oct).sum() / max(in_cap.sum(), 1)
c0 = np.array([1, 1, -1]) / math.sqrt(3); c1 = np.ones(3) / math.sqrt(3)
ang = math.acos(c0 @ c1); axis = np.cross(c0, c1); axis /= np.linalg.norm(axis)
def rot(t):
    th = t * ang; v = c0
    return v * math.cos(th) + np.cross(axis, v) * math.sin(th) + axis * (axis @ v) * (1 - math.cos(th))
rows = []
for t in np.linspace(0, 1, 41):
    c = rot(t); f = cap_fraction_inside(c, G)
    phiA = math.pi / 4 - (G / 2) * f
    phiB = (math.pi / 2 - f * G) * 2 * math.pi / (4 * math.pi - G)
    rows.append(dict(t=round(float(t), 3), deg_from_axis=round(math.degrees((1 - t) * ang), 2), f=round(float(f), 4),
                     phiA=round(phiA, 6), phiB=round(phiB, 6)))
need_B = (math.pi ** 2 - 8 * math.pi / 3) / (2 * math.pi - 2 / 3)
out = dict(gamma_M=G, scenario_A_at_axis=rows[-1]["phiA"], scenario_B_at_axis=rows[-1]["phiB"], target=2 / 3,
           Omega_needed_B_inside=need_B, ratio_to_gamma=need_B / G, rows=rows)
json.dump(out, open("run/core_shift.json", "w", encoding="utf-8"), indent=1)
print("Kern auf der Zyklusachse: phi_A =", out["scenario_A_at_axis"], " phi_B =", out["scenario_B_at_axis"], " Ziel 2/3 =", round(2/3, 6))
print("Szenario B braucht Omega =", round(need_B, 6), "sr =", round(need_B / G, 4), "* gamma_M")
for r in rows[::5]:
    print(r)
