# Ergebnis H190: Eine Drehung in den Generationen erzeugt eine Hierarchie, aber nicht die der Quarks

**Stand:** 27.11.2026. Vorab-Notiz `Vorab_Notiz_H190_Drehung_in_den_Generationen.md` (Commit d918623, vor der Rechnung). Skripte
`k393_test_h190.py` (`k393_out.txt`) und `k393b_gegenprobe.wl` (`k393b_out.txt`).

Werkzeuge: Python (numpy, scipy): Derivation D_T im vollen Modell ℂ ⊗ H₃(𝕆) auf den 36 Farbrichtungen, Eigenwertproblem zweiter Ordnung, Suche
über die Drehrate auf einem dichten Raster (189 582 zulässige Punkte, auch dicht an den Schwellen) mit Nachverfeinerung, Zufallskontrolle mit
2000 erfundenen Datensätzen. Wolfram Language: Formel der gekoppelten Frequenzen exakt, eine Stichprobe gegen die Daten (stimmt überein).
Qiskit nicht eingesetzt. Warnungen in Wolfram: nur Hinweise der Auswerteumgebung; zwei Aufrufe scheiterten zuerst an „Service Unavailable“.

**Ergebnis in einem Satz:** Dreht sich das Vakuum in der Ebene zweier Generationen, koppelt das zwei der drei Farbschwingungen gyroskopisch und
kann eine Frequenz beliebig klein machen; mit einer Krümmungsfunktion und einer Drehrate je Sektor trifft das Down allein (2,5σ), Up nie
(bester Abstand 7,1σ), und keine gemeinsame Form trifft beide.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H190a | D_T ist Derivation (Rest 2·10⁻¹⁵), vertauscht mit i und Ladung, lässt die Schwingung zum Paar (p, q) fest, dreht die zwei anderen (D² = −1); Frequenzen gegen die Formel 1,5·10⁻¹³ | Abweichung < 10⁻⁸ | **bestätigt** (nicht blind) |
| H190b | Down trifft einmal (2,47σ, Ω² = m); Up nie: bester Abstand 7,1σ (Ω² = √m), 24σ (Ω² = m), 171σ (Ω² = m²) | beide Sektoren < 3σ bei derselben Lesart | **widerlegt** |
| H190c | gemeinsame Form: bester Fall Up 7,1σ und Down 24,7σ | beide Sektoren < 3σ | **widerlegt** |
| Kontrolle | 2000 erfundene Datensätze: je Sektor frei 25,95 % Treffer; gemeinsame Form 3,25 % | Bericht | – |

Verglichen: 54 Kombinationen (9 Funktionen, 2 Vorzeichen, 3 Ebenen) je Sektor und Lesart, 3 Lesarten. 29 Kombinationen haben keinen zulässigen
Punkt (negative Krümmung lässt sich durch die Drehung nicht für alle drei Schwingungen stabilisieren).

## H190a: der Mechanismus (ohne Daten)
T sei in der Eigenbasis des Vakuums die Drehung in der Ebene der Eigenrichtungen p, q, und D_T(W) = TW − WT. Dann gilt im vollen Modell:

- D_T ist eine Derivation der Albert-Algebra, bewegt das Vakuum und vertauscht mit Farbe, mit der Multiplikation mit i und mit der Ladung.
- Die Farbschwingung zum Paar (p, q) bleibt fest. Die zwei anderen (zu den Paaren (p, k) und (q, k)) werden ineinander gedreht.
- Um W(t) = exp(ωt·D_T)W₀ lautet die Bewegungsgleichung δ̈ + 2ωDδ̇ + ω²D²δ + Hδ = 0. Mit den Krümmungen h_a, h_b der zwei gekoppelten und h_c der
  freien Schwingung sind die Frequenzquadrate

  h_c und Ω²_± = ½(h_a + h_b) + ω² ± √(¼(h_a − h_b)² + 2ω²(h_a + h_b)), mit Ω²_+·Ω²_− = (h_a − ω²)(h_b − ω²).

- Für beide Ladungen ist das gleich. Erreicht ω² eine der Krümmungen, geht eine Frequenz gegen null: Die Drehung kann also aus zwei ähnlichen
  Krümmungen ein sehr ungleiches Paar machen. Für h_a = h_b ergibt sich (√h ∓ ω)², der Fall aus H189b.

## Gegen die sechs Massen
| Lesart | Up: bester Abstand | Down: bester Abstand | beste gemeinsame Form |
|---|---|---|---|
| Ω² = √m | 7,1σ (l_i + l_j, Ebene (0,1), w = 2,138) | 13,1σ | Up 7,1σ, Down 24,7σ |
| Ω² = m | 24,2σ | **2,47σ** (l_k(l_i + l_j), Ebene (1,2), w = 1,636) | Up 28,8σ, Down 17,6σ |
| Ω² = m² | 171σ | 10,8σ | Up 171σ, Down 10,8σ |

(w = ω²/A; Ebenen in der Zählung der Eigenrichtungen 0, 1, 2 nach aufsteigendem Eigenwert.)

Der Treffer für Down liegt 11 % unter der Schwelle w = h, ist also nicht fein abgestimmt; das Spektrum ist 0,0060 : 0,1194 : 6,146. Er ist für
sich kein Befund: Ein Sektor mit einer Vorhersage und 162 Vergleichen wird leicht getroffen, und verlangt waren beide. Erfundene Datensätze
treffen in 26 % der Fälle beide Sektoren; die echten Daten sind für diesen Mechanismus also schwerer als eine typische Hierarchie. Der Grund
ist Up: Dort müssten zwei Verhältnisse von 10⁻⁵ und 10⁻³ zugleich stimmen, die Drehung macht aber nur eine Frequenz klein.

## Lesart
- **Der Mechanismus ist echt, aber er hat nur einen Hebel.** Eine Drehung in einer Ebene macht eine der drei Frequenzen klein. Die Quarks
  brauchen zwei kleine Verhältnisse je Sektor; das zweite müsste das Potential liefern, und das tut keine Funktion aus R.
- **Up und Down werden auch hier nicht getrennt.** Die Kopplung ist für beide Ladungen gleich; ein Unterschied kommt nur über die Krümmungen.
- **Damit ist die Lesart „Quarks als Farbschwingungen um das Leptonvakuum“ in allen bisher benannten Wegen geprüft:** Potential, Ladungsterm,
  Adjunkte, kinetische Normierung, Ableitungsterme, Phasendrehung, Drehung in den Generationen.

## Bilanz der Setzungen
| | gesetzt | hergeleitet | offene Wahl wandert nach |
|---|---|---|---|
| Träger, Vakuumwert, Symmetrie | wie H185 bis H189; Potential invariant unter der SU(3) der Plätze | – | ob es das drehende Vakuum als Lösung gibt |
| Bewegung | Drehung in einer Eigenebene, feste Rate | Kopplung zweier Schwingungen, Formel für Ω²_± | welche Ebene, welche Rate |
| Krümmungen | h = ±A·f, f ∈ R, je Sektor frei | – | Koeffizienten (wie H186, H187) |
| Massen | Lesart (3), Zuordnung nach Größe | Down allein trifft, Up nicht, gemeinsame Form nicht | welche Abbildung gilt |

Zur Regel „Bilanz der Setzungen“: sieben Tests (H184 bis H190) zur selben Voraussetzung. Hergeleitet sind Zahl und Form der Zustände und drei
Mechanismen ohne Daten (Funktionen je Term, Gradientenformen, gyroskopische Kopplung). Die offene Wahl (was die Massen festlegt) ist in keinem
Test kleiner geworden. Dem Autor vorgelegt: die Lesart selbst.

## Grenzen
Nur Drehungen in einer Eigenebene mit einer Rate; allgemeine Erzeuger (zwei Ebenen zugleich, zwei Raten) nicht gerechnet. Solche Drehungen
hätten zwei Hebel und je Sektor keine Vorhersage mehr, solange die Krümmungen frei sind. Kein Nachweis, dass das drehende Vakuum Lösung der
Feldgleichung ist. Suche über w auf einem Raster (Schrittweite unter 1 %, an den Schwellen bis 10⁻¹⁰), bester Abstand nachverfeinert. Massen bei
M_Z ohne Laufen. Die Wirkung von D_T ist nur in Python geprüft. Kein Vorzeichen gesetzt. OP3 und OP4 bleiben offen.

## Nächster Schritt (Vorschlag, Entscheidung beim Autor)
Die Lesart wechseln (Quarks auf anderer HS-Stufe oder als getrennte Felder) oder die Quarkmassen ruhen lassen und zur Feldgleichung der
Leptonen zurückkehren. Offen daneben: die nachträgliche gemeinsame Form aus H188. Vergeben: H190, k393. Nächste frei: H191, k394.
