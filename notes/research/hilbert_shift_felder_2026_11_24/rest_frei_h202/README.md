# H202 / k412 — Ist der ~0,9-%-Rest (D/B−1) frei?

Schritt (2) nach H201: Folgt D/B = 1,0085 aus den Grad-4/Grad-5-Strukturkoeffizienten, oder ist
es ein freier Eingabewert?

**Verdikt: D/B frei.** Die Abbildung (Kopplungen) → (A, B, C, D) hat Rang 4 (numpy + Wolfram); jede
Invariant-Basis mit ≤ 3 Kopplungen ist verworfen (bestes χ² = 8 312 gegen 7,91 bei 4). Minimal
nötig: 2 gerade + 2 ungerade Invarianten = 4 Kopplungen = 4 Koeffizienten. Der ~0,9-%-Rest ist ein
Eingabewert.

**Abschluss des Strangs:** Weder Grad (H201), Symmetrie (H197), Holomorphie (H200) noch minimale
Invariant-Zahl (H202) legen D/B fest. Alle Bausteine identifiziert (2 gerade Grad 3&5, 2 ungerade
Grad-4-H186-Formen, exakte Strukturkoeffizienten), Kopplungen frei. Nächster Schritt braucht eine
neue Eingabe — dem Autor als Weggabelung vorgelegt (Lepton-Kopplung / Elter-Darstellung / ruhen).

## Dateien
- `Vorab_H202_Rest_frei.md` — Vorab mit Kriterien (vor der Rechnung committet).
- `k412_test_h202.py` / `k412_out.txt` — numpy: Rang + Basis-Enumeration.
- `k412b_kontrolle.wl` / `k412b_out.txt` — Wolfram: Rang-Kontrolle (exakt gleich).
- `Ergebnis_H202_Rest_frei.md` — Ergebnis, Strang-Bilanz, Weggabelung.
