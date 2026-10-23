# Ergebnis H21: Die Doppelbelegung kommt daher, dass die Triole selbst eine Farbdrehung ist

Vorab-Notiz: `Vorab_Notiz_H21_Herkunft_Doppelbelegung.md`, Commit 516ab15 (2026-10-23 19:03 MESZ), vor der Rechnung.
Skript `k77_test_h21.py`, Ausgabe `k77_out.txt`. Kriterium unverändert.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H21a Automorphismus | **bestätigt** | σ: e₄ → e₅ → e₆ → e₄, e₇ fest, e₁ → −e₃, e₂ → −e₁, e₃ → e₂ ist ein Automorphismus, σ³ = 1. Unter allen 48 Vorzeichen-Fortsetzungen auf e₁, e₂, e₃ ist es der **einzige**. Also σ ∈ Stab(e₇) = SU(3) |
| H21b Farbdrehung | **bestätigt** | σ ist J-linear; auf ℂ³ mit Basis e₄, e₅, e₆ die zyklische Permutationsmatrix, det 1, Eigenwerte 1, ω, ω̄, nicht im Zentrum (Abstand 1). Vertauscht mit Q und mit T, R, J_B (frame-frei) |
| H21c Triole = Farbzustand | **bestätigt** | Die 120°-Triole Σ ω^k e_{k+4} (z₀ + z₁ + z₂ = 0) ist Eigenvektor von σ zum Eigenwert ω̄; unter P₋ liegt sie im Farb-Triplett Q = 2/3 |
| H21d reelle Untergruppe | **bestätigt** | Die Untergruppe von Stab(e₇), die span_ℝ(e₄, e₅, e₆) erhält, ist dreidimensional und wirkt als SO(3); σ liegt darin |
| H21e Trennung | **bestätigt** (Kontrolle) | Die Generationen-ℤ₃ auf Im ℍ der Dixon-Ablage vertauscht mit σ ⊗ 1 und ganz Stab(e₇) |

## Einordnung: woher die Doppelbelegung kommt

1. **Ein Objekt, zwei Lesarten.** Die triolische Grundstruktur des Companion (drei Kerne, 120° phasenverschoben, z₁ + z₂ + z₃ = 0)
   und ihre zyklische Symmetrie sind in 𝕆 genau die Farbdrehung σ, ein Element der Weyl-Gruppe von SU(3)_c.
   - `thm:octonion-SU3` liest die Kerne als Farben. Das ist mit H21c konsistent: Die Triole ist ein Farbzustand.
   - `thm:three-generations` liest dieselbe zyklische Symmetrie (Fano e₄ → e₅ → e₆) als Generationen-Symmetrie. Damit sind
     Farbe und Generation **dasselbe Objekt**, nicht nur dieselben Einheiten.
2. **Kein Frame-Effekt**, wie in r35 vermutet: σ ist reell, wirkt nur auf 𝕆 und vertauscht mit T, R, J_B. Es gibt hier nichts
   zu unterscheiden. Es ist eine Identifikation zweier Rollen.
3. **Auch die reelle Lesart ist Farbe.** Jede Generationen-Symmetrie auf dem reellen Spann von e₄, e₅, e₆, etwa die A₄- und
   Δ(96)-Gruppen der Flavour-Analyse von v4.8.0-r12, liegt in SO(3) ⊂ SU(3)_c. Ihre Brechung bräche die Farbe. Das macht die
   Folgerung (i) aus v4.8.0-r13 strukturell zwingend.
4. **Folgerung für die Trennung:** Die drei Generationen brauchen eine **zweite** Dreierstruktur außerhalb von 𝕆. Zwei Kandidaten
   sind im Companion vorhanden: die drei Triality-Plätze von 𝕆³ (v4.8.0-r14) und Im ℍ der Dixon-Ablage (v4.9.0-r33). Beide
   vertauschen mit der Farbe (H21e).
   - Nach H21 ist das nicht nur eine bequeme Wahl, sondern **nötig**: Innerhalb von 𝕆 mit festem e₇ gibt es keine
     Generationen-ℤ₃, die nicht Farbe wäre.
   - Genauer gilt das für Symmetrien, die e₇ festhalten. Eine ℤ₃, die e₇ bewegt, bräche die Farbgruppe selbst.
5. **Offen (Autorabsicht):** Ob die triolische Grundstruktur ursprünglich die Farbe oder die Generationen meinte. Nach H21 kann sie
   in 𝕆 nur eines davon sein. Die Bestandsaufnahme (Test 2, Spin(8)-Triality) entscheidet, ob die Triality-Plätze die Drei
   tragen.
