# H201 / k411 — Grad-Selektion der chiralen Quintik

Prüft, ob die Chiralität der l_k²-Quintik (H200) ein *Grad-Selektions-Prinzip* ist (nur der
Top-Grad chiral) oder eine gradübergreifende Koinzidenz.

**Verdikt: nein zur Grad-Selektion.** B (gerades l_k²) erscheint erst bei Feldgrad 5, D (ungerades
l_k²) schon bei Grad 4 — verschiedene Grade, also kann „Top-Grad = chiral" keine Ordnung sein.
Der lineare Term ist unabhängig ladungsgespalten (C/A = −2,056; C = 0 bei 91σ ausgeschlossen). Das
saubere Grad-Selektions-Modell (C = 0, D = B) ist mit χ² = 11 206 verworfen. Die Quintik-Chiralität
(D ≈ B) ist eine Near-Equality zwischen einer Grad-4-ungeraden und einer Grad-5-geraden Kopplung.

## Dateien
- `Vorab_H201_Grad_Selektion.md` — Vorab-Notiz mit Kriterien (vor der Rechnung committet).
- `k411_test_h201.py` / `k411_out.txt` — sympy-Grad-Zerlegung + numpy-Fits.
- `k411b_kontrolle.wl` / `k411b_out.txt` — Wolfram: unabhängige Kontrolle der Grad-Zerlegung (exakt gleich).
- `Ergebnis_H201_Grad_Selektion.md` — Ergebnis, Grad-Karte, Einordnung, Grenzen.

## Kette
… H198 (P_up = Chiralität) → H199 (kein Laufeffekt) → H200 (Chiralität gradselektiv, approximativ)
→ **H201 (keine Grad-Ordnung: D≈B ist gradübergreifend, Grad 4 vs 5; linearer Term unabhängig
ladungsgespalten)**. Offen → Schritt (2): folgt der ~0,9-%-Rest D/B−1 aus den Grad-4/Grad-5-
Koeffizienten, oder bleibt er frei?
