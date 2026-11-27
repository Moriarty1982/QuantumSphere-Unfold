# H199 (1b): Entsteht D = B aus dem Lauf der Kopplungen?

Test, **Befund: nein**. Ist D ≈ B ein Laufeffekt von einer hohen Skala?

- `Vorab_Notiz_H199_Lauf_der_Kopplungen.md` — Vorab (Commit a8ac697).
- `k409_test_h199.py` / `k409_out.txt` — 1-Schleifen-SM-RGEs, D/B(μ) von M_Z bis Planck.
- `k409b_out.txt` — Wolfram-Gegenprobe (dominanter Top-Lauf, einig).
- `Ergebnis_H199_Lauf_der_Kopplungen.md` — Befund.

**Kurz:** D/B läuft von 1,0085 (M_Z) bis 1,0123 (Planck) — **0,4 % über 17 Dekaden** — und bleibt überall nahe 1, fern von 0, ⅓,
−1. Der Lauf erzeugt D = B **nicht**; D ≈ B ist skalenstabil. Das stützt H198: D = B ist ein struktureller Zug (Chiralität), kein
dynamischer Laufeffekt. Aufruf: `python k409_test_h199.py > k409_out.txt`.
