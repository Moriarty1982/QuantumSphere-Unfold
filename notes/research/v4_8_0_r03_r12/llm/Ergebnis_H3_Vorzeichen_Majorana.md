# Ergebnis H3: Triolen-Vorzeichen als Majorana-CP-Parität

Vorab-Notiz: `Vorab_Notiz_H3_Vorzeichen_Majorana.md`, Commit e3b140e (2026-10-20 01:34 UTC), vor der Rechnung.
Skript: `k17_test_h3.py`. Daten und Kriterium unverändert.

## Ergebnisse

H2-Massen (NO): m = (0,364; 8,662; 50,131) meV, Paritäten η = (−1, +1, +1).

| Größe | H3 (η₁ = −1) | Vergleich η₁ = +1 |
|---|---|---|
| m_ββ bei δ_CP = 212° | 3,02 meV | 3,49 meV |
| m_ββ, voller δ_CP-Bereich | 1,25–3,47 meV | 1,75–3,97 meV |
| m_ββ, Monte Carlo | 2,74 ± 0,70 meV (95 %: 1,27–3,58) | 3,21 ± 0,71 meV |
| 95 %-Obergrenze, δ_CP gleichverteilt | 3,50 meV (Maximum 3,84) | — |

m_β = 8,85 ± 0,10 meV (folgt aus H2, unabhängig vom Vorzeichen).

## Urteil nach dem festgelegten Kriterium

- Heute **verträglich**: m_ββ liegt eine Größenordnung unter der KamLAND-Zen-Grenze (28–122 meV).
- Festgeschriebene Widerlegung: ein bestätigtes 0νββ-Signal mit m_ββ über **3,5 meV** (nach Kernmatrixelement-
  Spanne) oder ein Nachweis von Dirac-Neutrinos.
- **Das Vorzeichen selbst ist nicht prüfbar.** Es verschiebt m_ββ um rund 0,5 meV, weniger als die Streuung durch
  δ_CP (±0,7 meV).

## Einordnung (ehrlich)

- Die geplanten Experimente (LEGEND-1000, nEXO) erreichen etwa 5–20 meV. H3 sagt für sie **kein Signal** voraus.
  Ein Signal dort würde H2 + H3 widerlegen; ausbleibende Signale bestätigen H3 nicht, weil jede normale Ordnung
  mit fast masselosem m₁ einen ähnlich kleinen Wert gibt.
- m_β = 8,9 meV liegt unter dem Ziel von Project 8 (etwa 40 meV); KATRIN (Endgrenze etwa 0,3 eV) erst recht.
- Die Zuordnung „e₃ < 0 ⇔ Majorana“ ist bei den geladenen Fermionen durch Ladungserhaltung trivial erfüllt und
  daher kein Beleg.
- Nebenbefund: Das MC-Suchfenster in k15 hatte bei NO rund 28 % der Ziehungen verworfen. Korrigiert
  (Fenster je Ordnung); die H2-Werte bleiben unverändert (Σ = 0,05916 ± 0,00023 eV).

## Status

[P] H3 verträglich, auf absehbare Zeit nicht prüfbar. Vorhersage m_ββ ≤ 3,5 meV festgeschrieben.
Guards unberührt.
