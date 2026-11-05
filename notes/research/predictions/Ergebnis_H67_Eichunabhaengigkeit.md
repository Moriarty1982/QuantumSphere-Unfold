# Ergebnis H67: bestätigt. Zahl und Lage der vier Bedingungen sind eichunabhängig

Grundlage ist die Vorab-Notiz H67 (d1f9d54, vor der Rechnung). Gerechnet hat `ci/hp_eich/k167_hp_eichung.py` im GitHub-Lauf 41898162356 vom 4.11.2026: arb mit 70 Stellen, q = 6, je ein Job pro Eichung.

Vor dem Lauf gab es einen Funktionstest mit q = 4 in der Eichung Ibeta: F₄ = 273, 7 Polarisationen. Er gehört nicht zum Test.

| Eichung s = Ψ†MΨ | Transversalität | dim N₆ | Rang C | F₆ | Gram-Lücke | Polarisationen auf dem Kegel (100 Richtungen) | kleinste Lücke | außerhalb: kleinster Singulärwert |
|---|---|---|---|---|---|---|---|---|
| K₂ = I₃⊗α_y (Kontrolle) | 0.45 | 501 | 24 | **477** | 5.0e-13 \| 1.0e-71 | 6 | 3e7 | 5.5e-2 |
| K₀ = 1 (Dichte) | 0.077 | 501 | 24 | **477** | 5.4e-13 \| 1.3e-71 | 6 | 2e7 | 5.5e-2 |
| K₃ = I₃⊗α_z | 0.165 | 501 | 24 | **477** | 2.3e-13 \| 2.1e-71 | 6 | 2e7 | 5.5e-2 |
| Q₃ = S₃⊗α_z | 0.256 | 501 | 24 | **477** | 4.7e-13 \| 1.2e-71 | 6 | 2e7 | 5.5e-2 |
| I₃⊗β (Ψ̄Ψ, Lorentz-Skalar) | 0.023 | 501 | 24 | **477** | 1.8e-15 \| 4.3e-72 | 6 | 9e5 | 5.5e-2 |

Alle Newton-Residuen liegen bei ≤ 1.0e-51, die Gram-Lücken bei ≥ 4e56. Jeder Job brauchte etwa 4 GB und 15 bis 24 Minuten.

## Prüfung der Kriterien
- Die Kontrolle K₂ gibt 477, wie in H59.
- Alle Lücken liegen bei ≥ 1e20, alle Residuen bei ≤ 1e-30.
- Die Lücken der Polarisationen liegen bei ≥ 9e5, also über 1e5.
- Alle vier Alternativen ergeben 477 und 6.

**H67 ist bestätigt.**

## Lesart
- Die vier versteckten Bedingungen auf 6-Jets und ihre Lage auf dem Lichtkegel hängen nicht von der Wahl der Eichung ab. Das gilt auch für die kovariante Eichung Ψ̄Ψ.
- Mit H66, wonach R und Ω kovariant sind, gehören die vier Bedingungen damit zum kovarianten Inhalt des Vergleichssystems und nicht zur nicht-kovarianten Eichfixierung.
- Die Lorentz-Brechung kommt allein vom vorgegebenen Hintergrund (Ψ am Keim, A, h).
- Bei Ψ̄Ψ ist die Transversalität am Keim schwach (0.023). Das zeigt sich in kleineren, aber immer noch eindeutigen Lücken.
