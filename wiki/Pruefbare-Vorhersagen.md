# Prüfbare Vorhersagen nach Experiment

**Stand:** 28.11.2026. Diese Seite ordnet die offenen, festgeschriebenen Vorhersagen nach den Experimenten, die sie prüfen. Die verbindlichen Kriterien
stehen in den Vorab-Notizen und auf [Vorhersagen und Tests](Vorhersagen-und-Tests). Die Empfindlichkeiten der Experimente sind **Richtwerte aus der
Literatur** (Planungsangaben der Kollaborationen), im Repo nicht nachgerechnet. Ehrlicher Status: OP1 bis OP5 bleiben offen. φ = 0,0396 ist eine gemessene
Eingabe, die Vorhersagen hängen an den Setzungen der jeweiligen Notiz (K = ⅔, Brannen-Form H99, Zweigvorzeichen und andere).

**Verbindliches Register:** Companion-Runde v4.10.0-r75 (Stand 28.11.2026, gilt für Version v5.6.0, veröffentlicht 28.11.2026, DOI 10.5281/zenodo.24632437) mit der Einstufung jeder Abhängigkeit. Regel des Autors: Jede öffentliche Version hält ihre Vorhersagen datiert fest; Korrekturen nur in einer neuen Version mit Begründung, nie Nachjustieren nach einer Messung; als Test zählt die vor der Messung festgeschriebene Version.

## Auf einen Blick
| Größe | Vorhersage | heute | prüft | was sie trennt |
|---|---|---|---|---|
| Massenordnung | normal (umgekehrt im Modell −16σ, H213) | normal leicht bevorzugt | JUNO, DUNE, Hyper-K, Kosmologie | umgekehrte Ordnung mit 3σ widerlegt H227 und H176 |
| Σm_ν | **59,30 ± 0,24 meV** (H227) | < 64,2 meV (DESI DR2 + CMB, 95 %) | DESI DR3, Euclid, CMB-S4 (σ ≈ 15–20 meV) | Σm < 58 meV widerlegt; der Abstand zum Minimum der normalen Ordnung (≈ 58,7 meV) ist kleiner als jede geplante Messung |
| m₁, m₂, m₃ | 0,379 / 8,81 / 50,11 meV (H227) | — | indirekt über Σm | — |
| m_β | 8,87 ± 0,04 meV (H227) | < 450 meV (KATRIN) | KATRIN (≈ 300 meV), Project 8 (Ziel ≈ 40 meV) | Ein Nachweis oberhalb ≈ 40 meV widerlegt |
| m_ββ | 1,3 bis 4,0 meV (H227; 3,49 meV in der Brannen-Lesart) | < 28–122 meV (KamLAND-Zen) | LEGEND-1000, nEXO (≈ 9–20 meV) | Vorhersage: **kein Signal** in der nächsten Generation; ein Signal oberhalb ≈ 10 meV widerlegt |
| R = Δm²₂₁/Δm²₃₁ | 0,030839 (H99/H100 A) | 0,030016 ± 0,000457 (+1,8σ) | nächster NuFIT-Fit, JUNO | H100: Varianten A, B, C trennen |
| sin²θ₂₃ | 0,494–0,495 (H176, H207); ≤ 0,54 (H42); [0,49; 0,50] (H46) | 0,470 mit SK, 0,561 ohne | DUNE, Hyper-K, globale Fits | 0,45 oder 0,55 mit Fehler 0,01 widerlegt H176 und H46 |
| sin²θ₁₂ | drei Lesarten, siehe unten | 0,3036 ± 0,0064 | **JUNO** (Ziel σ ≈ 0,002) | JUNO trennt die drei Lesarten |
| sin²θ₁₃ | 0,0223 (H176); 0,0216 ohne Parameter (H207) | 0,02248 ± 0,00056 | Reaktoren, globale Fits | 3σ-Kriterium in H176 |
| δ_CP | \|sin δ\| ≈ 1 (H176: ±77,7°), sin δ < 0 (H125), zusammen ≈ 282° | NuFIT (normal) um 212° ± 34°, nicht gaußisch | DUNE, Hyper-K (σ ≈ 10–20°) | \|sin δ\| < 0,8 mit 3σ widerlegt H176; sin δ > 0 mit 3σ widerlegt H125 |
| Ω_m | 0,30185 = β_sym² (H96) | DESI/Planck um 0,30–0,31 | DESI DR3 (BAO allein), Euclid | Abweichung > 2σ |
| m_W | 80,3615 ± 0,0018 GeV (H15) | PDG 2026: 80,3625 ± 0,0077 | nächste Weltmittelung | Kriterium in der Vorab-Notiz |
| m_τ | 1776,969 MeV (Koide, H227) gegen 1777,134 MeV (H102) | 1776,93 ± 0,09 | Belle II, BESIII, später STCF | trennt erst bei σ ≲ 0,05 MeV |

## Die θ₁₂-CP-Korrelation (JUNO und DUNE zusammen)
Im Repo stehen drei Lesarten für sin²θ₁₂. Sie schließen sich gegenseitig aus, deshalb entscheidet JUNO zwischen ihnen:
1. **H9:** sin²θ₁₂ = β_sym²/cos²θ₁₃ = 0,3086 (nachträglich gefunden, nicht blind).
2. **H176** (Ein-Zahl-Kandidat, festgeschrieben): 0,3019, zusammen mit sin²θ₂₃ = 0,4954, sin²θ₁₃ = 0,0223 und δ_CP = ±77,7°.
3. **Strukturlesart H206–H208** (Richtung K₂, ohne angepassten Parameter): Die feste Spalte v₀ gibt |U_e1|² = ⅔ exakt, also nahe TM1:
   sin²θ₁₂ ≈ 0,318 bis 0,3195. Mit einem erlaubten, nicht hergeleiteten Zusatzterm sinkt der Wert auf 0,3155, aber nur bei maximaler CP-Verletzung.
   Das ergibt eine **Korrelation**: Entweder ist sin²θ₁₂ ≳ 0,315 und |sin δ| ≈ 1, oder sin²θ₁₂ liegt nahe 0,304 und |sin δ| ist deutlich kleiner (≈ 0,65).
   Die Korrelation wurde nachträglich gefunden (H208).

Ausgang nach Messung:
- **JUNO bei ≈ 0,318:** Die Strukturlesart trägt, H176 und H9 fallen. DUNE müsste dann |sin δ| ≈ 1 finden.
- **JUNO bei ≈ 0,302:** H176 bleibt verträglich, die Strukturlesart mit maximaler CP fällt. DUNE müsste dann |sin δ| ≈ 0,98 (H176) finden. Eine submaximale CP-Phase würde
  die Strukturlesart ohne Maximalbedingung retten, H176 aber nicht.
- **JUNO bei ≈ 0,309:** H9 trägt, die beiden anderen fallen.

## Neutrinomassen (Kosmologie, Beta-Zerfall, doppelter Beta-Zerfall)
- **Σm_ν = 59,30 ± 0,24 meV** ist die schärfste Zahl. Sie liegt knapp über dem Minimum der normalen Ordnung, weil m₁ = 0,38 meV sehr klein ist. Kosmologie trennt
  diesen Wert in den nächsten Jahren nicht vom Minimum. Sie kann aber die umgekehrte Ordnung (Σm ≳ 100 meV) und jede Messung Σm < 58 meV ausschließen. Hinweis
  (H227): DESI DR2 bevorzugt im ΛCDM-Fit sehr kleine Σm. Erhärtet sich das, gerät jede normale Ordnung mit m₁ ≈ 0 unter Druck, auch diese.
- **m_β = 8,87 meV** liegt weit unter allen geplanten Empfindlichkeiten. Das Bild sagt für KATRIN und Project 8 ein Nullergebnis voraus.
- **m_ββ = 1,3 bis 4,0 meV:** Ein Nullergebnis von LEGEND-1000 und nEXO ist vorhergesagt. Ein Signal würde das Bild widerlegen (oder umgekehrte Ordnung bedeuten).

## Zeitachse (Richtwerte)
| bis | erwartete Daten | betroffene Vorhersagen |
|---|---|---|
| 2027 | neuer NuFIT-Fit, erste JUNO-Präzision für θ₁₂ und Δm²₂₁ | H100 (R), θ₁₂-Lesarten (erste Trennung), H176 |
| 2028–2030 | JUNO nach etwa 6 Jahren (θ₁₂ sub-%, Ordnung ≈ 3σ), DESI DR3, Euclid | θ₁₂-Korrelation, Massenordnung, H96, Σm |
| 2030–2035 | DUNE, Hyper-K (δ_CP, Oktant), CMB-S4, LEGEND-1000 | δ_CP (H176, H125), θ₂₃ (H42, H46), Σm, m_ββ |

## Was eine Widerlegung träfe
- **Umgekehrte Ordnung oder Σm < 58 meV:** Die Leptonenmassen-Bilanz H227 fällt und mit ihr die Brannen-Form für Neutrinos (H99).
- **sin²θ₁₂ fern von 0,302, 0,309 und 0,318 (über 3σ):** Alle drei Mischungslesarten fallen. Die feste Spalte v₀ (exakt hergeleitet) stünde dann gegen die Daten.
- **|sin δ| < 0,8 mit 3σ:** H176 fällt; die Strukturlesart bliebe nur ohne die Bedingung maximaler CP-Verletzung.
- **Ω_m weit neben 0,302:** Die Λ-Auslesung H96 fällt, das berührt die Zählregel (Postulat).

Quellen: Ergebnis-Notizen H227 (`massen_bilanz_h227/`), H176 (`mischung_h176/`), H206–H208 (`theta12_tm1_h208/` und Nachbarordner), H213, sowie die Tabelle
„Offene Vorhersagen“ auf [Vorhersagen und Tests](Vorhersagen-und-Tests). Alle unter `notes/research/hilbert_shift_felder_2026_11_24/`.
