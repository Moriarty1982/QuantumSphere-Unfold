# Erkundung (Korrektur): Photon-Gewichte verhindern die Gravitonen-Erzeugung am Urknall nicht. Sie unterdrücken nur lange Wellen, die Energie sitzt bei k ~ 1/Δ

**6. November 2026. Status: Erkundung, numerisch, ohne Kriterium.** Nachprüfung der Begründung zur Autorentscheidung „Photon-Gewichte für die Gravitation“ (`Erkundung_Gravitonen_Urknall.md`). Code `k214_erzeugung_photongewichte.py`, Ausgabe `k214_out.txt`. Der Autor sagte „Weiterrechnen“.

## Was korrigiert wird
In `Erkundung_Gravitonen_Urknall.md` und in der Entscheidung steht: „Mit Photon-Gewichten erzeugt der Übergang keine Gravitonen (r85.5)“. Das gilt nur im scharfen Grenzfall kΔ → 0. Am glatten Übergang mischen auch bei a = b die beiden Frequenzen für kΔ ~ 1, und die Energie der Erzeugung wird gerade dort bestimmt.

## Rechnung
tanh-Profil, Δ = 2, beide Drehsinne gemittelt. Als Maß der Beimischung dient n_mix(k) = min(|C|², |D|²)/(b/a). Im scharfen Grenzfall ist das bei Materie-Gewichten n₀ = 0,404 und bei Photon-Gewichten 0. Weil der Übergang bei kΔ ~ 1 nicht unitär ist (H94), ist das Maß dort eine Wahl. Energieintegral I = ∫₀^{8} x³·n_mix(x) dx mit x = kΔ, in Einheiten Δ⁻⁴.

| Gewichte | n_mix(kΔ = 0,02) | größtes n_mix | I |
|---|---|---|---|
| Materie (β_sym) | 0,405 | 0,56 bei kΔ = 0,27 | 0,091 |
| Photon (a = b) | 0,0014 | 0,49 bei kΔ = 0,47 | 0,066 |

Bei beiden Gewichten liegt das Maximum des Integranden bei kΔ ≈ 0,76. Kontrolle: Wronski-Determinante ≤ 10⁻¹¹ (wie k210). Bei Photon-Gewichten läuft die Norm ebenfalls von +1 (lange Wellen) nach −1 (kurze Wellen), mit |N| < 1 dazwischen (Nullstelle bei kΔ ≈ 0,49).

## Folge
- Photon-Gewichte senken die Gravitonen-Energie nur um etwa 27 %. Mit den Bosonen des Standardmodells (Materie-Gewichte) wird ΔN_eff ≈ 2,6 statt 3,6, und das ist weiter weit über der Grenze ≈ 0,3.
- **Die Begründung der Entscheidung trägt also nicht.** Das N_eff-Problem kommt von der Erzeugung bei k ~ 1/Δ ≳ M_P, also oberhalb der Planck-Skala, und zwar für jedes Gewicht, solange die Gravitation am Urknall das Vorzeichen ihres Gewichts wechselt (−b → a).
- **Mögliche Auswege:**
  - (i) Die Gravitation wechselt am Urknall ihr Gewicht gar nicht (kein Übergang im Gravitationsterm). Das ist eine wörtlichere Lesart von r64 („Gravitation frame-unabhängig“) und eine Ausnahme von der zweiten Lesart für den Einstein–Cartan-Term.
  - (ii) Die Erzeugung oberhalb der Planck-Skala ist nicht physikalisch (die effektive Beschreibung bricht dort zusammen). Dann ist ΔN_eff unbestimmt, und Δ ≲ ℓ_P ist mit Vorsicht zu lesen.
  - (iii) Sehr viele zusätzliche Bosonen mit Materie-Gewichten (g_B ≳ 200–300).
- Für die übrigen Bosonen gilt dasselbe: Auch ihre Erzeugung (r04.5) wird bei k ~ 1/Δ bestimmt. Die dort genannte Energiedichte ist nur eine Größenordnung.
