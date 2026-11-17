"""Vorschau (kein Test): wo liegen die wartenden OP4-Vorhersagen gegen die neuesten verfuegbaren Werte?
NuFIT 6.1 (Datenstand Nov. 2025, vor den Festlegungen; zaehlt nicht als Pruefung), normale Ordnung, Tabelle v61.tbl-parameters.pdf:
  sin^2 theta12 = 0,3088 +0,0067 -0,0066;  sin^2 theta23 = 0,470 +0,017 -0,014 (mit und ohne SK-atm gleich);  sin^2 theta13 = 0,02248.
JUNO 29.09.2026 (arXiv:2609.37895): sin^2 theta12 = 0,3036 +- 0,0064.
2-sigma-Intervalle hier naeherungsweise als Bestwert +- 2 x (einseitiger 1-sigma-Fehler); die Kriterien verlangen das von den Autoren angegebene Intervall.
"""
import numpy as np

t23, up, dn = 0.470, 0.017, 0.014
i1 = (t23 - dn, t23 + up); i2 = (t23 - 2 * dn, t23 + 2 * up)
print(f"NuFIT 6.1 sin^2 t23: 1sigma [{i1[0]:.3f}; {i1[1]:.3f}], 2sigma ~ [{i2[0]:.3f}; {i2[1]:.3f}], Breite 2sigma {i2[1]-i2[0]:.3f}")
# H42: widerlegt, wenn 2sigma ganz ueber 0,54; bestaetigt, wenn ganz unter 0,54
h42 = "bestaetigt" if i2[1] < 0.54 else ("widerlegt" if i2[0] > 0.54 else "unentschieden")
print(f"H42 (<= 0,54): bei diesen Werten {h42}")
# H46: widerlegt, wenn 2sigma [0,49; 0,50] nicht beruehrt; bestaetigt, wenn 1sigma beruehrt und 2sigma-Breite < 0,06
touch2 = i2[1] >= 0.49 and i2[0] <= 0.50; touch1 = i1[1] >= 0.49 and i1[0] <= 0.50
h46 = "widerlegt" if not touch2 else ("bestaetigt" if touch1 and (i2[1] - i2[0]) < 0.06 else "unentschieden")
print(f"H46 ([0,49; 0,50]): 2sigma beruehrt {touch2}, 1sigma beruehrt {touch1} -> {h46}; Abstand Bestwert zu 0,49: {(0.49-t23)/up:.2f} sigma")
s12, s12u, s12d = 0.3088, 0.0067, 0.0066
juno, sj = 0.3036, 0.0064
for name, pred, sp in (("H9 (beta_sym^2/cos^2 t13)", 0.30185 / (1 - 0.02248), 0.0), ("H12 (Drei-Frame)", 0.2991, 0.0057), ("TM1 (H4)", 0.3182, 0.0)):
    zN = (pred - s12) / np.hypot(s12u if pred > s12 else s12d, sp)
    zJ = (pred - juno) / np.hypot(sj, sp)
    print(f"{name:28s} Vorhersage {pred:.4f}: gegen NuFIT 6.1 {zN:+.2f} sigma, gegen JUNO 2026 {zJ:+.2f} sigma")
print("H9-Kriterium verlangt eine JUNO-Messung mit sigma <= 0,004; JUNO 2026 hat 0,0064.")
