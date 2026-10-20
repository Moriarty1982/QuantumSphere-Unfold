# Vorab-Notiz H8: Cayley–Dickson-Involution als CP-Symmetrie der Neutrinos

Festgelegt am 2026-10-20, **vor** der Rechnung der Mischungsparameter und vor dem Datenvergleich.
Bezug: K20.2 (`k25_test_h7.py`).

## Ausgangslage (M, schon gerechnet)

Die Cayley–Dickson-Involution p + qℓ ↦ p − qℓ (e₁, e₂, e₃ fest, e₄…e₇ negiert) wirkt auf dem Generationen-Triplett
(e₄, e₅, e₆) antilinear als z ↦ X z̄ mit **X = −1**, also als gewöhnliche CP-Transformation in der Basis, in der
der vorzeichenfreie Triolen-Lift die reine zyklische Vertauschung ist. Sie kommutiert mit der Triole und mit allen
TM1- und θ₁₃ = 0-Involutionen (K20.2).

## Hypothese (V)

**H8:** Die Majorana-Massenmatrix der Neutrinos ist invariant unter einer Restspiegelung h (TM1-Lift) und unter der
CP-Transformation X: hᵀ m h = m und Xᵀ m X = m*. Die geladenen Leptonen sind diagonal in der Eigenbasis der Triole
(Elektron = Eigenwert-1-Richtung).

## Offenlegung vor der Rechnung

Erwartung aus der Literatur (μ-τ-Spiegelungssymmetrie, Harrison–Scott; Grimus–Lavoura): Gewöhnliche CP in einer
Basis, in der die geladenen Leptonen durch eine zyklische ℤ₃ diagonalisiert werden, wird in der Massenbasis zur
μ-τ-Spiegelung. Diese erzwingt **sin²θ₂₃ = ½ und δ_CP = 90° oder 270°**, Majorana-Phasen 0 oder π. Mit TM1
zusammen bleibt dann nur ein freier Mischungsparameter (über θ₁₃ festgelegt). Gemessen sind sin²θ₂₃ = 0,470 und
δ_CP = 212° (beide nicht genau). Diese Erwartung wird nachgerechnet, nicht vorausgesetzt.

## Verfahren (verbindlich)

- Allgemeinste symmetrische 3×3-Matrix m mit hᵀ m h = m und Xᵀ m X = m* (lineare Nebenbedingungen); zufällige
  Stichproben aus dem Lösungsraum; Diagonalisierung, U = U_ℓ† U_ν; Winkel und δ_CP über |U|² und die
  Jarlskog-Invariante, Majorana-Phasen aus U.
- Für alle drei TM1-Involutionen und den vorzeichenfreien Triolen-Lift; zum Vergleich auch die θ₁₃ = 0- und
  TM2-Involutionen.
- Zuordnung μ ↔ τ (Reihenfolge der zwei komplexen Eigenrichtungen der Triole) beide Varianten berichten.
- Datenvergleich danach: χ² wie in H4 (NuFIT 6.0, IC24 + SK, NO, Gauß-Näherung, asymmetrische Fehler); der einzige
  freie Winkel wird angepasst.

## Entscheidungskriterium (verbindlich)

- Freiheitsgrade: 4 Messgrößen, 1 angepasster Winkel → 3 FG. **Verträglich** bei χ²_min < 7,81 (95 %),
  **disfavorisiert** bei χ²_min ≥ 11,34 (99 %), dazwischen „Spannung“.
- Die festgelegten Werte sin²θ₂₃ und δ_CP werden als Vorhersage für JUNO/DUNE/Hyper-K festgeschrieben.
- Zusätzlich (nicht entscheidend): m_ββ mit den H2-Massen und den von H8 erzwungenen Majorana-Phasen.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
