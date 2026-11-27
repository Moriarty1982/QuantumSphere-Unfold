# H200 / k410 — Chirale/holomorphe Feldgleichung

Prüft, ob Chiralität unter der Ladungs-U(1) (H198: P_up = ½(1+iL_U)) ein Strukturprinzip der
Feldgleichung sein kann.

**Verdikt: teilweise.** Globale Holomorphie verworfen (macht Down masselos, 77–181σ). Strikt
D = B (gradselektive Chiralität) trifft das Muster, ist aber bei ~9σ ausgeschlossen (χ² 320,7
vs. 7,91 frei; D/B = 1,0085, ~0,9-%-Rest über RG-Budget). Chiralität ist dominant, approximativ,
gradselektiv.

## Dateien
- `Vorab_H200_chirale_Feldgleichung.md` — Vorab-Notiz mit Entscheidungskriterien (vor der Rechnung committet).
- `k410_test_h200.py` / `k410_out.txt` — numpy: Operator-Kontrolle + drei Modell-Fits.
- `k410b_kontrolle.wl` / `k410b_out.txt` — Wolfram: unabhängige Kontrolle der drei Fits (exakt gleich).
- `Ergebnis_H200_chirale_Feldgleichung.md` — Ergebnis, Einordnung, Grenzen.

## Kette
H196 (Up/Down-Ort = Ladungsvorzeichen) → H197 (keine Symmetrie erzwingt D=B) → H198 (P_up =
Chiralität der Ladung) → H199 (D=B kein Laufeffekt) → **H200 (Chiralität nicht global, nicht
exakt — gradselektiv und dominant)**. Offen: warum gerade die Quintik chiral, und woher der
~0,9-%-ladungsblinde Rest.
