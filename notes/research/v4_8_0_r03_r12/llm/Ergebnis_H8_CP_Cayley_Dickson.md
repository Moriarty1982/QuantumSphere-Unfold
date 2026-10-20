# Ergebnis H8: Cayley–Dickson-Involution als CP-Symmetrie der Neutrinos

Vorab-Notiz: `Vorab_Notiz_H8_CP_Cayley_Dickson.md`, Commit f6734ab (2026-10-20 03:50 UTC), vor der Rechnung.
Skript: `k26_test_h8.py`. Verfahren und Kriterium unverändert.

## Struktur (M)

- Lösungsraum der Massenmatrix (hᵀ m h = m, m reell wegen X = −1): Dimension 4 für jede Restspiegelung.
- 2000 Zufallsstichproben je Typ: **sin²θ₂₃ = 0,5000 exakt**; für TM1 und TM2 **δ_CP ∈ {90°, 270°}** exakt.
  (Für die θ₁₃ = 0-Spiegelung ist δ_CP nicht definiert.) Die Erwartung aus der Notiz (μ-τ-Spiegelung) ist bestätigt.
- Mit TM1: sin²θ₁₂ = 0,3182 (aus θ₁₃), sin²θ₂₃ = ½, δ_CP = 270° oder 90°. Alle drei TM1-Involutionen und beide
  μ-τ-Zuordnungen geben dasselbe.

## Datenvergleich (NuFIT 6.0, IC24 + SK, NO, Gauß-Näherung)

| | Wert | Beitrag zu χ² |
|---|---|---|
| sin²θ₁₂ | 0,3182 | 0,73 |
| sin²θ₁₃ | 0,02217 (angepasst) | 0,00 |
| sin²θ₂₃ | 0,5000 | 3,11 |
| δ_CP | 270° (90° deutlich schlechter) | 4,98 |
| **χ²_min** | | **8,82 bei 3 FG** |

## Urteil nach dem festgelegten Kriterium

7,81 ≤ 8,82 < 11,34: **Spannung** (weder verträglich auf 95 % noch disfavorisiert auf 99 %).

## Einordnung (ehrlich)

- Gewinn: Die Cayley–Dickson-Involution ist im Modell schon vorhanden (Verdopplungsvorschrift der Oktonionen) und
  macht ohne zusätzliche Annahme zwei scharfe Vorhersagen: θ₂₃ maximal und δ_CP = 270°. Mit TM1 zusammen sind alle
  vier Mischungsgrößen bis auf θ₁₃ festgelegt.
- Kosten: Die Wahl zwischen 90° und 270° trifft der Datenvergleich (zwei diskrete Zweige). Die μ-τ-Spiegelung selbst
  ist aus der Literatur bekannt; neu ist nur, dass sie hier aus der Cayley–Dickson-Struktur folgt.
- Die Spannung kommt aus θ₂₃ (NuFIT bevorzugt 0,470) und δ_CP (212°). Beide Verteilungen sind breit und nicht
  gaußförmig, maximale Mischung liegt im 2σ-Bereich. Die Gauß-Näherung überzeichnet die Spannung eher.
- **Prüfbar bald:** JUNO, DUNE und Hyper-K messen θ₂₃ und δ_CP. Weicht θ₂₃ deutlich von 45° ab oder liegt δ_CP
  klar außerhalb von etwa 270°, ist H8 widerlegt.
- m_ββ mit den H2-Massen und reellen Majorana-Paritäten: 3,56 meV für die H3-Paritäten (−1, +1, +1),
  1,34–4,05 meV über alle Paritäten. Weiter unterhalb der Reichweite geplanter Experimente.

## Status

[P] H8 in Spannung (χ² = 8,8 bei 3 FG). Festgeschrieben: sin²θ₂₃ = 0,5, δ_CP = 270°, sin²θ₁₂ = 0,318 (mit TM1).
Guards unberührt.
