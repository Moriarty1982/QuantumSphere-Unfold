# Ergebnis H134: Mit der Frame-Korrektur ist die TM1-Klasse mit JUNO verträglich, aber ohne Vorhersage

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H134_Frame_Rapiditaet_TM1_JUNO.md` (Commit a0ab92e, vor der Rechnung; teilweise nicht blind, Daten bekannt).
Skripte `notes/research/hilbert_shift_felder_2026_11_24/frame_h134/k263_test_h134.py` (Ausgaben `k263_out.txt`, `k263_out_fein.txt`), `k263b_kontrolle.wl`
(`k263b_out.txt`), `k263c_trefferpunkt.py` (`k263c_out.txt`). Status: H134a bestätigt, H134b widerlegt, H134c bestätigt.**

Anlass: Einwand des Autors zum Befund „TM1/H8 nach JUNO disfavorisiert“ (k262): „benutzt juno die idee mit den frames?“, „wir sitzen doch in dem verschobenen frame“.

Werkzeuge: Python (numpy, scipy), Regel und Funktionen unverändert aus k100 (H45). Wolfram Language für die unabhängige Auswertung eines Trefferpunkts und für ε = 0.
Qiskit nicht eingesetzt (keine Schaltung).

## Zur Frage selbst
- JUNO benutzt keine Frames. sin²θ₁₂ ist dort aus der Überlebenswahrscheinlichkeit von Reaktor-Antineutrinos im Labor bestimmt.
- Der Einwand trifft die andere Seite des Vergleichs: k262 und H131 haben eine algebraische Spalte ohne erklärte Abbildung neben eine Messung im Materie-Frame gestellt.
- Frame-Abbildungen, die mit der Gruppe vertauschen (z ↦ iz, z ↦ z̄, HC-Schatten z ↦ z + μ z̄ mit μ = β_sym²), können eine von der Restsymmetrie festgelegte Spalte
  nicht verschieben (Vorab-Notiz, Offenlegung 2). Wirksam ist nur eine Abbildung, die die Plätze unterscheidet. Im Repo ist das die Maske D = exp(ε W_l) mit
  ε = artanh β_sym = 0,6174 (r57, H41, H45). Sie war bisher nur auf TM2 angewandt.

## Kontrollen
| Kontrolle | Messwert | |
|---|---|---|
| (i) ε = 0 | Auf dem Raster der Vorab-Notiz (2°) **kein** Fall mit θ₁₃ in 3σ: das Fenster in φ ist etwa 1,3° breit. Auf 0,5° (nachträglich): 192 Fälle, sin²θ₁₂ ∈ [0,3181; 0,3191], sin²θ₂₃ = 0,500000, \|sin δ\| = 1,000000, kein Treffer im JUNO-2σ-Bereich | auf 2° nicht auswertbar, auf 0,5° erfüllt |
| (ii) Übernahme des Codes | TM2-Lesart, Variante A, Bereiche von k100: 120 Treffer, sin²θ₂₃ ∈ [0,4913; 0,4975] (wie H45) | erfüllt |
| (iii) Massen der geladenen Leptonen | größter relativer Rest 3,5·10⁻¹³, 24 Zweige je ε | erfüllt |
| (iv) Wolfram | Trefferpunkt: sin²θ₁₂ = 0,3089342468, sin²θ₂₃ = 0,5470933659, sin²θ₁₃ = 0,0213245516, sin δ = 0,5755814801, gleich wie Python; Massenverhältnisse stimmen; ε = 0: 0,3196 und 0,3171 | erfüllt |

**Abweichungen von der Vorab-Notiz, offen gesagt:** (1) Kontrolle (i) ist auf dem festgelegten 2°-Raster leer, also dort weder erfüllt noch verletzt. Deshalb ist ein
zweiter Lauf mit 0,5° dazugekommen; er ist nachträglich. Die Entscheidungen fallen auf beiden Rastern gleich aus, maßgeblich bleibt 2°. (2) Der erste Lauf wurde nach zehn
Minuten vom Werkzeug beendet; danach wurde Variante B auf vier Kerne verteilt, ohne Änderung der Regel. (3) Der Trefferpunkt für Wolfram (k263c) ist nachträglich
herausgezogen; Wolfram prüft die Auswertung der Matrizen, nicht die Anpassung.

## Ergebnis (ε = artanh β_sym, Klasse TM1, Raster 2°)
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H134a | Variante A: 0 Treffer. **Variante B: 56 Treffer** (32 davon im JUNO-1σ-Bereich); sin²θ₁₂ ∈ [0,2920; 0,3139], sin²θ₂₃ ∈ [0,5403; 0,5634], \|sin δ\| ∈ [0,523; 0,705] | mindestens ein Treffer in A oder B | **bestätigt** |
| H134b | bei θ₁₃ (3σ) und θ₁₂ (JUNO 2σ): sin²θ₂₃ ∈ [0,133; 0,768] (Breite 0,635), \|sin δ\| ∈ [0,002; 0,934] (Breite 0,932) | Breiten < 0,05 und < 0,3 | **widerlegt** |
| H134c | Variante B: nächster Wert 0,3036 (Abstand 0,0000). Variante A: nächster Wert 0,3480 (Abstand 0,0444, also weiter weg als ohne Korrektur) | Abstand < 0,0136 | **bestätigt** (nur durch B) |

Auf dem Raster 0,5°: Variante A 0 Treffer, Variante B 264 Treffer (120 in 1σ), sin²θ₂₃ ∈ [0,5355; 0,5831], |sin δ| ∈ [0,487; 0,827]; Entscheidungen gleich.

## Was daneben herauskam (ohne Kriterium)
- **Die Korrektur nur der geladenen Leptonen (Variante A) hilft nicht**, sie verschlechtert θ₁₂ (≥ 0,346). Treffer gibt es nur, wenn die Maske auch auf die Neutrinos
  wirkt (Variante B).
- **Der Hopf-Wert trifft auch** (Variante B: 64 Treffer auf 2°, 272 auf 0,5°). Anders als in H45 trennt die TM1-Klasse die beiden Werte von ε nicht.
- **Die Klasse mit θ₁₃ = 0 trifft auf dem feinen Raster ebenfalls** (24 Treffer, |sin δ| ≈ 0,99). Die Maske ist stark (Faktor e^{−3ε} = 0,157 auf Platz 3); nach der
  Korrektur ist die Ausgangsklasse kaum noch zu erkennen.
- **θ₂₃ liegt in allen Treffern im oberen Oktanten** (0,536 bis 0,583). Die TM2-Lesart mit derselben Korrektur gibt [0,491; 0,498] (H45, Vorhersage H46). Die beiden
  Lesarten unterscheiden sich also am Oktanten; die Treffer hier lägen außerhalb von H46 und zum großen Teil über der Grenze von H42 (≤ 0,54).
- Von θ₂₃ = 45° und |sin δ| = 1 aus k262 bleibt nach der Korrektur nichts Scharfes.

## Lesart
- **Der Einwand des Autors trägt.** „TM1 nach JUNO disfavorisiert“ gilt für die unkorrigierte Spalte. Mit der im Repo erklärten Frame-Abbildung und festem ε = η gibt es
  Parameterpunkte, die θ₁₂, θ₁₃ und θ₂₃ zugleich treffen. Der Satz aus k262 ist entsprechend einzuschränken.
- **Es ist Verträglichkeit, keine Vorhersage.** φ ist frei, dazu kommen diskrete Wahlen (welche ℤ₂, Zweig, Zuordnung, Vorzeichen, m₁): 56 Treffer unter 298 752 Fällen,
  von denen 24 568 θ₁₃ treffen. θ₂₃ und δ sind unter der Bedingung an θ₁₂ und θ₁₃ nicht scharf. Dass auch der Hopf-Wert und die andere Klasse treffen, zeigt, dass der
  Treffer wenig über die Ausgangsstruktur sagt.
- **Was der Frame hier ist:** die Maske aus r47/r57 mit ε = Rapidität (H45), eine Lesart ohne Herleitung aus einer Wirkung. μ = β_sym² aus k297 geht über den HC-Schatten
  nicht ein (er vertauscht mit der Gruppe); β_sym geht nur über ε = artanh β_sym ein und ist eingesetzt (OP1 offen).
- OP3 und OP4 bleiben offen, kein Guard ist berührt. H9, H42, H46 unverändert. Vorzeichen und Feldgleichung nicht berührt.
- **Mögliche nächste Frage (nur mit neuer Vorab-Notiz):** ob die Algebra die freie Drehung φ festlegt (etwa über die Massenform K aus H128 auf dem Realteil).
  Erst dann würde aus der Verträglichkeit eine Vorhersage für θ₂₃ und δ, die sich am Oktanten von H46 unterscheiden ließe.
