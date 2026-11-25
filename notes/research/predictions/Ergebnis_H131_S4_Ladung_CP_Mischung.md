# Ergebnis H131: Eine einzige Klasse, aber mit δ = 0 oder 180°: TM2 ohne CP-Verletzung, θ₂₃ nicht maximal

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H131_S4_Ladung_CP_Mischung.md` (Commit 875e6d4, 10:36 UTC, vor der Rechnung; teilweise nicht blind).
Skripte `notes/research/hilbert_shift_felder_2026_11_24/mischung_h131/k261_test_h131.py` (Ausgabe `k261_out.txt`), `k261b_exakt.wl` (`k261b_out.txt`),
`k261c_theta23.py` (`k261c_out.txt`, nachträglich). Status: H131a bestätigt, H131b widerlegt.**

Werkzeuge: Python (numpy) für die Gruppe aus k260, die Lösungsräume der Restsymmetrien und 200 Stichproben je Kombination; Wolfram Language exakt für die CP-Abbildungen
und die allgemeine Majorana-Matrix. Qiskit nicht eingesetzt (keine Schaltung).

## Kontrollen
| Kontrolle | Messwert | |
|---|---|---|
| (i) Gruppe | 24 Elemente erhalten das Triplett (Rest 10⁻¹⁵); 12 linear (Ordnungen 1, 2, 3 in den Anzahlen 1, 3, 8), 12 antilinear; unter gemischter Verknüpfung abgeschlossen | erfüllt |
| (ii) ohne CP | trimaximale Spalte in allen 24 Kombinationen (T, S), Abweichung 2·10⁻¹³; J frei (bis 0,096), keine Zeilengleichheit | erfüllt |
| (iii) Entartung | X mit XX* = S (6 der 12): zwei Neutrinomassen exakt gleich (Wolfram), 48 Kombinationen nicht gewertet | ausgewiesen |
| (iv) Wolfram exakt | für XX* = 1 ist m_ν in der Basis der geladenen Leptonen reell; für XX* = S Eigenwerte {a², e² + e₂² + f₂², e² + e₂² + f₂²} | erfüllt |

Alle 24 Matrizen sind reell und ganzzahlig (vorzeichenbehaftete Permutationen), die antilinearen haben Determinante −1. 24 Paare (S, X) scheiden aus, weil X nicht mit S vertauscht.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H131a | 48 gewertete Kombinationen, **eine** Klasse: Spalte trimaximal (Rest 2·10⁻¹¹), J = 0, Zeilen verschieden | genau eine Klasse | **bestätigt** |
| H131b | in dieser Klasse \|J\| < 10⁻¹⁰ in allen Stichproben; kleinste Zeilendifferenz 0,29 | J ≢ 0 und zwei gleiche Zeilen | **widerlegt** |

## Warum es so ausgeht
- Die antilinearen Elemente sind Platzvertauschungen mit Vorzeichen, verbunden mit der Konjugation der Ladung. In der Basis, in der die ℤ₃ der geladenen Leptonen diagonal
  ist, werden die zulässigen X zu reellen symmetrischen Matrizen (±(2/3, −1/3)-Muster), und die Majorana-Matrix wird reell. Die Mischungsmatrix ist dann reell bis auf Phasen.
- Die sechs antilinearen Elemente der Ordnung 4 (XX* = S) erzwingen zwei gleiche Neutrinomassen und scheiden aus.
- Die μτ-Spiegelung (θ₂₃ = 45°, |sin δ| = 1), die H8 aus der Cayley–Dickson-Involution gelesen hatte, entsteht aus dieser Gruppe nicht.

## Lesart
- **Was die Struktur aus k260 festlegt, wenn man ℤ₃ für geladene Leptonen und ℤ₂ mit CP für Majorana-Neutrinos ansetzt:** TM2 mit δ = 0 oder 180°. Nachträglich gerechnet
  (k261c, Stichprobe stimmt mit der Formel auf 10⁻¹⁵ überein): bei sin²θ₁₃ = 0,022 ist sin²θ₁₂ = 0,341 und **sin²θ₂₃ = 0,395 oder 0,605**. Es bleibt ein diskretes Vorzeichen,
  kein freier Winkel.
- **Gegen die Daten spricht das eher, als dass es stützt.** Die Spalte ist nach H39 bereits 3,6σ von JUNO entfernt (vorab offengelegt). θ₂₃ liegt in beiden Fällen deutlich
  von 45° weg; der Wert 0,605 widerspricht der eigenen offenen Vorhersage H42 (≤ 0,54), beide widersprechen H46 ([0,49; 0,50]). Ein Vergleich mit aktuellen globalen Fits für
  θ₂₃ und δ ist hier nicht gerechnet (keine Datentabelle im Repo herangezogen).
- **Was daraus folgt:** Die Lesart „Kopie k auf Platz k, ℤ₃ und ℤ₂ wie H39, CP aus der Ladung“ ist scharf und damit prüfbar, und sie steht schlecht da. Das trifft die
  Setzungen dieser Lesart (Offenlegung 4 der Vorab-Notiz), nicht H128 und H130. Mit H8 (δ = 270°, θ₂₃ maximal) ist sie nicht vereinbar; beide können nicht zugleich gelten.
- Nicht berührt: Vorzeichen der Massenterme und Feldgleichung. OP3 und OP4 bleiben offen, kein Guard ist berührt.
- **Mögliche nächste Frage (nur mit neuer Vorab-Notiz):** Welche der Setzungen trägt die Spannung? Kandidaten sind die Zuordnung ℤ₂ zu den Neutrinos (statt einer
  Restsymmetrie, die TM1 hält, wie in k256 und k280) und die Annahme „Kopie k auf Platz k“.
