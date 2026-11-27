# H195: Die H188-Form aus der Feldgleichung

Test, **teilweise**. Herleitung der H188-Form m ∝ (a·l_k + b·l_k²)/(l_i+l_j)² aus der zweiten Variation um das Leptonvakuum.

- `Vorab_Notiz_H195_H188_Form_aus_der_Feldgleichung.md` — Vorab (Kopie; Original unter `notes/research/predictions/`), Commit a5f2f6d.
- `k403a_peirce_check.py` — Peirce-Eigenwert ½(l_i+l_j) und kinetische Normen N₀,N₁,N₂ über die H₃(𝕆)-Algebra (verifiziert).
- `k403_test_h195.py` / `k403_out.txt` — Fit der hergeleiteten Form (A+B l_k)/z, Vergleich mit H188, Nenner-Varianten, Kontrolle.
- `k403c_zaehler_grad.py` / `k403c_out.txt` — Grad-Leiter der F₄-Krümmungen; l_k² erst ab Potentialgrad 5; Zähler-Familien-Fit.
- `k403b_out.txt` — Wolfram-Gegenprobe (Grad-Leiter, Norm-Identität), bestätigt Python/sympy.
- `Ergebnis_H195_H188_Form_aus_der_Feldgleichung.md` — Befund.

**Kurz:** Der **Nenner (l_i+l_j)²** ist hergeleitet — aus dem Peirce-Eigenwert W₀∘X = ½(l_i+l_j)X und einer W²-gewichteten
kinetischen Norm (N₂ = ¼(l_i+l_j)²N₀, exakt). Der **Zähler** ist es nicht: F₄-Krümmungen geben auf dem Vakuum ein Polynom in l_k,
dessen l_k² erst ab Potentialgrad 5 erscheint; die einfache Form (A+B l_k, Grad ≤4) verwerfen die Daten (Up 93σ), die H188-Form
(l_k²) braucht Grad 5 und hat freie Koeffizienten. Feldgleichungs-kompatibel, nicht vorhergesagt. Up/Down-Split (b/a) nicht erklärt.
Aufruf: `python k403_test_h195.py > k403_out.txt`.
