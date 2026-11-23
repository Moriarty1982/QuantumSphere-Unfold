# Zufallsabschätzung der Treffer von γ_L (Erkundung, nicht blind, 18.11.2026)

**Ergebnis in einem Satz:** Unter der vorab festgelegten Zählung ist der Dreifachtreffer von DL/ABCK (sin²θ₁₂, cot θ_W, Ω_m) **mit Zufall verträglich**,
sobald man mitzählt, dass das Paar aus 36 Zählregel-Paaren gewählt ist (erwartet 0,64–0,81 gleich gute Paare). Nur wenn das Paar ohne Blick auf die Daten
feststünde, läge die Zufallswahrscheinlichkeit bei etwa 2 %.

Auftrag des Autors: „Ja, Zufallsabschätzung“ (offener Vorschlag 3). Verfahren vor der Rechnung festgelegt: `Methoden_Notiz.md` (Commit 8557ed7).
Skript `k235_chance_estimate.py`, Ausgabe `run/k235_stdout.txt`; Nachtrag `k235_nachtrag.py`, `run/k235_nachtrag_stdout.txt` (nachträglich).
Keine H-Nummer, kein Test der Theorie, nur eine Aussage über die Zählung.

## Teil A: belegte Auswahl je Treffer
| Treffer | belegte Auswahl | p (Zufall) |
|---|---|---|
| Ω_M = β² | 26 Lesarten, Trefferbereich 0,049 (Λ-Kreuzungen) | 0,73 |
| \|U_e2\|² = β² (H9) | rund 10 Konstanten, Fensterbreite 0,013 | 0,12 |
| cot θ_W = γ_L (H15) | 3 Dokumentkonstanten, 1σ | 0,17 |
| Φ_e = π/4 − γ_M/2 (H102) | Scan mit 154 Versuchen, 0,34 erwartet | 0,29 |

Erwartete Zufallstreffer bei diesen vier Suchen: Σp = 1,31; beobachtet 4. P(4 von 4) = 0,0044, P(mindestens 3) = 0,070. Wie vorab gesagt, ist das eine
**Untergrenze** der Zufallswahrscheinlichkeit: Nicht gezählte Suchen fehlen (35 widerlegte Tests in der Sichtung vom 17.11.), die Treffer sind nach dem
Sehen ausgewählt, und die beiden ersten prüfen dieselbe Zahl gegen zwei Messgrößen um 0,30.

## Teil B: fester Zielkatalog (16 Ziele, 8 Formen, 2σ)
| Größe | Wert |
|---|---|
| Treffer von DL/ABCK (γ_L = 1,8647) | 3: sin²θ₁₂ durch β² (−1,05σ), cot θ_W durch γ_L (−0,58σ), Ω_m durch β² (+0,51σ) |
| Trefferzahlen der 36 Paare | 0: 11, 1: 21, 2: 3, 3: 1 (nur DL/ABCK) |
| P(n ≥ 3), γ_L gleichverteilt auf [1,006; 3,51] | 0,0226; 36 · P = **0,81** |
| P(n ≥ 3), log-gleichverteilt | 0,0179; 36 · P = **0,64** |
| mittlere Trefferzahl eines zufälligen γ_L | 0,9–1,0 (P(n ≥ 1) 0,74–0,81) |

Nach der vorab festgelegten Lesart (36 · P über 0,3) ist das **mit Zufall verträglich**. Dass unter 36 Paaren genau eines drei Treffer hat, entspricht der
Erwartung von 0,6–0,8 solcher Paare. Die meisten Treffer zufälliger Werte fallen auf die breiten Ziele sin²θ₂₃ (52 %), Ω_m (21 %) und sin²θ₁₂ (18 %);
die genauen Ziele (sin²θ_W MS-bar, m_μ/m_τ, Ω_b h²) trifft fast nie ein Wert.

## Nachtrag (nachträglich, nach dem Sehen der Ausgabe)
- Die beiden Ziele um 0,30 hängen stark zusammen: Trifft β² sin²θ₁₂, trifft es in 73 % der Fälle auch Ω_m. Zwei der drei Treffer sind also fast einer.
- Ohne Ω_m im Katalog: P(n ≥ 2) = 0,049, 36 · P = 1,8. Dann ist der Befund klar zufallsverträglich.
- Der einzige Treffer an einem genauen Ziel ist cot θ_W (Fensteranteil 0,9 %); er trägt das Gewicht von H98, wie dort schon gesagt.

## Lesart
- **Die Treffer allein belegen „eine Zahl“ nicht.** Bei freier Wahl des Zählregel-Paars ist ein Paar mit drei Treffern zu erwarten. Das Gewicht hängt
  daran, ob die Wahl DL für M und ABCK für T ohne Blick auf die Daten begründet wird; das ist OP1 (warum Gewicht 2, warum diese Zuordnung).
- **Ehrlicher Stand für Außenwirkung (I6, bis 23.11. als I5 geführt):** Mit heutigen Daten keine Signifikanz; tragfähig sind nur die vorab festgelegten Vorhersagen (H9, H15, H96,
  H102, H112). Ein vorab festgelegter Treffer an einem genauen Ziel (etwa H15 mit σ(m_W) ≲ 1 MeV) wöge mehr als alle nachträglichen zusammen.
- Die Zählung hängt an Katalog und Formen; ein anderer Katalog gäbe andere Zahlen, aber dieselbe Größenordnung, solange er breite Ziele um 0,3 enthält.
- OP1, OP4, OP5 offen.
