# Ergebnis H12: Zuordnung der Messwerte zu den Kreuztermen

Vorab-Notiz `llm/Vorab_Notiz_H12_Drei_Frame_Zuordnung.md` (Commit a593f5d), Skript `llm/k33_test_h12.py`.
Gerechnet am 2026-10-21 nach dem Commit der Notiz, Verfahren 1–3 unverändert.

## Werte

| Größe | Wert |
|---|---|
| arcosh γ_L = η₊ + η_s | 1,23489 |
| η_s (aus Ω_M = 0,3111) | 0,62958, β_s = 0,55776 |
| η₊ | 0,60531, β₊ = 0,54082 |
| symmetrisch zum Vergleich | η = 0,61745, β_sym = 0,54935 |
| **P₁₂ = sin²θ₁₂ (H12)** | **0,29911 ± 0,00571** |
| Variante ohne BAO (entscheidet nicht) | 0,29484 ± 0,00742 |
| H9 | 0,30862 ± 0,00018 |
| Abstand P₁₂ − H9 | −0,00951 |

Die Unsicherheit von P₁₂ stammt fast ganz aus Ω_M: Weil η₊ = arcosh γ_L − η_s, geht ein Fehler in Ω_M praktisch eins
zu eins in die Vorhersage ein (σ_P ≈ σ_Ω).

## Heutige Daten (zählen nicht)

JUNO 2026, sin²θ₁₂ = 0,3036 ± 0,0064: z₁₂ = −0,52, z₉ = +0,78, Δχ² = +0,34. Beide verträglich, keine Trennung.

## Trennbarkeit (nach dem festgelegten Kriterium)

Mit σ_x = 0,004 ist σ = √(σ_x² + σ_P²) = 0,00697, also |P₁₂ − H9| / σ = 1,36 < 2.
**Nach der Notiz kann die künftige JUNO-Messung H9 und H12 grundsätzlich nicht trennen. Das ist das Ergebnis; ein
Test liegt nicht vor.**

Die Grenze setzt nicht JUNO, sondern Planck: Selbst bei fehlerfreier Messung von θ₁₂ bliebe σ = σ_P = 0,0057 und
2σ = 0,0114 > 0,0095. Trennbar würde es erst mit Ω_M auf etwa ±0,0025 genau (bei σ_x = 0,004) oder ±0,0046 (bei
fehlerfreiem θ₁₂). Die Notiz legt den Planck-2018-Wert mit BAO fest; neuere Ω_M-Werte dürfen hier nicht eingesetzt
werden.

## Asymmetrie, offengelegt

Läge der künftige Messwert genau bei 0,299, ergäbe der Vergleichsteil Δχ² = 5,6, weil H9 keine Modellunsicherheit
trägt und dann selbst 2,4σ entfernt wäre. Das ist keine Stütze für H12: Die Trennbarkeitsklausel der Notiz geht vor,
und eine solche Messung wäre nach H9s eigenem Kriterium eine **Spannung für H9**, also H9s Test, nicht H12s. Umgekehrt
kann ein Messwert bei 0,3086 H12 höchstens um Δχ² = 1,9 benachteiligen.

## Urteil

- H12 ist rechnerisch festgelegt: β₊ = 0,5408 < β_sym = 0,5493 < β_s = 0,5578, Vorhersage sin²θ₁₂ = 0,2991 ± 0,0057.
- **Nicht testbar gegen H9** mit der festgelegten Datenlage. Die Notiz schreibt vor, das als Ergebnis festzuhalten.
- Die Reihenfolge β₊ < β_s war vorher bekannt (Offenlegung 1) und zählt nicht.
- H9 bleibt mit seinem eigenen Kriterium unverändert bestehen. Die Drei-Frame-Typisierung aus r18 ist davon nicht
  berührt.
