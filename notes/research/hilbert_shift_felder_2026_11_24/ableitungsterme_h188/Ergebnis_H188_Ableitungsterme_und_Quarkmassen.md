# Ergebnis H188: K₁ bis K₄ wirken bei kleinen Schwingungen nicht; eine kinetische Normierung trifft die Massen nur so oft wie der Zufall

**Stand:** 27.11.2026. Vorab-Notiz `Vorab_Notiz_H188_Ableitungsterme_und_Quarkmassen.md` (Commit bb9da71, vor der Rechnung). Skripte
`k391_test_h188.py` (`k391_out.txt`), `k391c_nachtrag.py` (`k391c_out.txt`, nachträglich) und `k391b_gegenprobe.wl` (`k391b_out.txt`).

Werkzeuge: Python (numpy, sympy): Ordnung von K₁ bis K₄ in der Störung exakt (ganzzahlige Richtungen auf H₃(𝕆), Polynom in ε durch Interpolation),
Suche über die Funktionsmenge R aus H187 mit linearer Fehlerfortpflanzung, Zufallskontrolle mit 2000 erfundenen Datensätzen. Wolfram Language:
H188a symbolisch an allgemeinen 3×3-Matrizen, Nachtrag mit 30 Stellen. Qiskit nicht eingesetzt. Warnungen in Wolfram: nur Hinweise der
Auswerteumgebung.

**Ergebnis in einem Satz:** Die Ableitungsterme K₁ bis K₄ ändern die kleinen Schwingungen um ein ruhendes Vakuum nicht; eine vom Vakuum abhängige
kinetische Normierung mit einer Potentialfunktion trifft die Quarkmassen nicht, mit zwei Potentialfunktionen trifft sie beide Sektoren, aber das
tut sie auch bei 63 % erfundener Datensätze.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H188a | K₁, K₂, K₄ beginnen bei ε⁴, K₃ bei ε⁶; Koeffizienten ε⁰ bis ε³ exakt null (Python auf H₃(𝕆), Wolfram symbolisch) | zweite Variation exakt null | **bestätigt** (nicht blind) |
| H188b | ein Quotient f/z je Sektor: bester Abstand Up 29σ, Down 15σ; kein Quotient unter 3σ | beide Sektoren < 3σ | **widerlegt** |
| H188c | (a·f + b·g)/z: beide Sektoren unter 3σ bei X = m, Zuordnung A (Up 1,05σ, Down 1,59σ) und B (Up 2,05σ, Down 1,76σ) | Treffer und Zufallsquote < 5 % | **ohne Urteil** (Zufallsquote 63,4 %) |
| Kontrolle | 2000 erfundene Datensätze: Treffer mit einem Quotienten 0,00 %, mit einem Tripel 63,40 % | Bericht | – |

Verglichen: 72 Quotienten und 324 Tripel je Sektor, je 3 Lesarten (X = √m, m, m²) und 2 Zuordnungen der Generationen. Viele Tripel sind linear
abhängige Schreibweisen derselben Form (zum Beispiel l_k(l_i + l_j) = Tr(W₀)·l_k − l_k²).

## H188a: Warum K₁ bis K₄ nichts beitragen
Alle vier Bausteine (k290) sind aus X_μ = ∂_μW gebaut und mindestens vierter Ordnung in X. Um ein ruhendes, homogenes Vakuum ist ∂_μW₀ = 0, also
X_μ = ε ∂_μδW. Damit beginnen sie bei ε⁴ und fehlen in der Bewegungsgleichung der kleinen Schwingungen, die nur die Ordnung ε² sieht. Das gilt
unabhängig von den Koeffizienten.

Gegenstück (nachträglich, nur Ordnungsabzählung, keine Lösung der Feldgleichung): Hat der Hintergrund selbst eine Ableitung (X_t = B₀ ≠ 0, etwa
die rotierende Lösung ψ̇ = uωψ aus k253), dann tragen K₁, K₂ und K₄ in der Ordnung ε² bei; für K₁ ist der Koeffizient exakt
N(B₀)N(∂_xδW) − ⟨B₀, ∂_xδW⟩² (Wolfram). Die Ableitungsterme können die Massen also nur über ein bewegtes Vakuum erreichen.

## H188b, c: kinetische Form aus dem Vakuum
Bestes Ergebnis je Lesart und Zuordnung (Abstand in σ; „Tripel“ = zwei Potentialfunktionen über einer kinetischen):

| Lesart, Zuordnung | Up: Quotient | Up: Tripel | Down: Quotient | Down: Tripel |
|---|---|---|---|---|
| √m, A | 29σ | 1,69σ | 69σ | 3,56σ |
| √m, B | 29σ | 0,41σ | 73σ | 8,5σ |
| m, A | 34σ | **1,05σ** | 48σ | **1,59σ** |
| m, B | 34σ | **2,05σ** | 15σ | **1,76σ** |
| m², A | > 10⁶σ | 9,2σ | 158σ | 2,03σ |
| m², B | > 10⁶σ | 120σ | 466σ | 79σ |

Die Zufallskontrolle zeigt, dass die Treffer in H188c nichts unterscheiden: Mit 324 Tripeln, 6 Kombinationen und einer Vorhersage je Sektor
treffen 63 % der erfundenen Datensätze ebenfalls beide Sektoren. In H187c (ohne kinetische Funktion) waren es 2,45 %.

## Nachträgliche Beobachtung (kein Test, k391c)
Unter den Treffern gibt es genau eine Form, die **beide Sektoren mit denselben Funktionen** trifft (drei linear abhängige Schreibweisen):

m ∝ (a·l_k + b·l_k²) / (l_i + l_j)², Zuordnung B (leichteste Generation beim Paar (μ, τ)), Lesart X = m.

| Sektor | a | b | b/a | Abstände (Gen. 1, 2, 3) | χ² (1 Freiheitsgrad) |
|---|---|---|---|---|---|
| Up | −5,71·10⁻⁴ | 3,31·10⁻² | −57,9 | −0,09σ, +2,13σ, −0,53σ | 4,8 |
| Down | 1,65·10⁻³ | −1,41·10⁻⁴ | −0,085 | −1,12σ, +1,35σ, −0,11σ | 3,1 |

Down liegt nahe an l_k/(l_i + l_j)², Up nahe an l_k²/(l_i + l_j)²; allein treffen beide nicht (15σ und 34σ), erst mit dem jeweils anderen Glied.
Dass irgendeine gemeinsame Form beide Sektoren trifft, kommt bei 4,2 % der erfundenen Datensätze vor. Das ist nachträglich gefunden, die Form war
vorab nicht ausgezeichnet, und je Sektor sind zwei Zahlen angepasst. Es ist kein Befund, sondern ein Kandidat, der nur mit einer neuen Vorab-Notiz
und einer unabhängigen Vorhersage (etwa einer Beziehung zwischen b/a für Up und Down oder einer Herleitung der Form) geprüft werden kann.

## Lesart
- **Die Ableitungsterme der Feldgleichung sind für diese Frage nicht der fehlende Baustein**, solange das Vakuum ruht. Das ist eine Aussage über
  Ordnungen und hängt an keiner Zahl.
- **Eine kinetische Normierung macht die Lesart flexibler, nicht schärfer.** Sobald ein Nenner aus dem Vakuum erlaubt ist, treffen zwei
  Potentialfunktionen fast jede Hierarchie. Die Massen bleiben damit frei.
- **Was bleibt:** die nachträgliche gemeinsame Form (oben) und das bewegte Vakuum, bei dem K₁, K₂, K₄ in zweiter Ordnung wirken.

## Bilanz der Setzungen
| | gesetzt | hergeleitet | offene Wahl wandert nach |
|---|---|---|---|
| Träger, Vakuum, Symmetrie | wie H185 bis H187; Vakuum ruhend und homogen | – | ob das Vakuum ruht |
| Ableitungsterme | K₁ bis K₄ aus k290 | kein Beitrag in zweiter Ordnung (exakt) | – |
| Kinetische Form | Funktionsmenge R (Grad ≤ 2), je Sektor eigene Koeffizienten | ein Quotient trifft nicht; Tripel treffen so oft wie der Zufall | welche kinetische Form und welche Koeffizienten |
| Massen | Lesart (3), Zuordnung (2) | – | welche Abbildung gilt |

Zur Regel „Bilanz der Setzungen“: H184 bis H188 betreffen dieselbe offene Voraussetzung. Die offene Wahl ist mit H188 nicht kleiner geworden,
sondern um die kinetische Form größer. Die in H187 vorgelegte Weggabelung besteht weiter; neu ist, dass der Weg „Ableitungsterme“ nur über ein
bewegtes Vakuum offen bleibt.

## Grenzen
Nur ruhendes, homogenes Vakuum; die rotierende Lösung ist nicht gerechnet (nur Ordnungsabzählung). Kinetische Formen höheren Grades und
Mischungen mehrerer kinetischer Funktionen nicht verglichen. Positivität der kinetischen Form nicht verlangt (l_i l_j − ½ l_k² wechselt das
Vorzeichen); in der gemeinsamen Form ist der Nenner positiv, die Koeffizienten a, b haben je Sektor entgegengesetztes Vorzeichen (angepasst, nicht
gesetzt). Massen bei M_Z ohne Laufen. H188a in Wolfram an Matrizen statt Oktonionen (K₃ dort identisch null; K₃ in Python auf H₃(𝕆)). OP3 und OP4
bleiben offen.

## Nächster Schritt (Vorschlag, Entscheidung beim Autor)
Entweder das bewegte Vakuum rechnen (rotierende Lösung, dort wirken K₁, K₂, K₄ in zweiter Ordnung; neue Vorab-Notiz) oder die Lesart wechseln
(Quarks auf anderer HS-Stufe oder als getrennte Felder). Die gemeinsame Form kann als eigener Vorab-Test mitlaufen, wenn sich eine unabhängige
Vorhersage angeben lässt. Vergeben: H188, k391. Nächste frei: H189, k392.
