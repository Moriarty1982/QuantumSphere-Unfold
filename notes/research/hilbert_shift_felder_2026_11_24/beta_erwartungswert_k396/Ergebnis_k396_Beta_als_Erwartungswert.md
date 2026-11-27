# k396: Kann β_sym ein Erwartungswert sein, der leicht von ½ abweicht? (Erkundung, 27.11.2026)

**Status:** Erkundung ohne Vorab-Notiz, kein Test. Abschnitt 5 ist nachträglich. **Anlass:** Frage des Autors vom 27.11.2026: Ist β_sym vielleicht
einfach ein Erwartungswert, der im Mittel nie auf glatte 0,5 kommt, wie die kleine Abweichung von 50 % bei gekoppelten Rädern der Lorenz-Maschine?
(β_sym − ½ = 0,0494.) **Werkzeuge:** Python, Qiskit (Korrelation zweier Bänder), Wolfram (exakte Werte, erste Ordnung).

## Vorwissen geprüft

r67 (Zählregel als Postulat: Σ_{k≥1} 2^(1 − γ a_k) = 1 mit a_k = √(k(k+2)/3), k = 2j; γ_L = 1,8646997646, β_sym = 0,5494056410; mit der Fläche
j + ½ käme γ = 2, β = 1/√3). r70 (HC als Messung, b_C = 1/γ_L für den Materie-Frame). k395 (Schleife L3, Fixpunkt b = ½). 37 frühere
Herleitungsversuche für die Casimir-Fläche und H165 (widerlegt) laut Projektstand; ein Ansatz „Erwartungswert nahe ½“ war nicht darunter.

## 1 Welche Größe liegt glatt bei ½?

| Größe | glatt (Fläche j + ½, zugleich Fixpunkt der Schleife L3) | Zählregel (Casimir) | Abstand |
|---|---|---|---|
| b_C = 1/γ, Erwartungswert ⟨σ_x⟩ der HC-Messung | 0,5 | 0,5362794 | +0,0363 |
| p₁ = 2^(1−γ), Anteil der Spin-½-Durchstoßpunkte | 0,5 | 0,5491607 | +0,0492 |
| β = √((γ−1)/(γ+1)) | 0,5773503 | 0,5494056 | −0,0279 |
| x = β² | 0,3333333 | 0,3018466 | −0,0315 |
| p₊ = (1 + 1/γ)/2 | 0,75 | 0,7681397 | +0,0181 |

Befund: Die Vermutung trifft, aber eine Größe weiter. Glatt ½ sind der Erwartungswert der HC-Messung 1/γ und der Anteil p₁. β selbst hat den
glatten Wert 1/√3 und liegt 0,028 darunter.

## 2 Die Abweichung von ½ ist ein Mittelwert (innerhalb der Zählregel hergeleitet)

Im glatten Fall sind die Spins verteilt wie p_k = 2^(−k) (½, ¼, ⅛, …). Die Casimir-Fläche ist für j = ½ gleich der glatten (beide 1 Bit) und
für höhere Spins größer: Überschuss 0; 0,133; 0,236; 0,328; 0,416; 0,5 für k = 1 bis 6. In erster Ordnung gilt

δγ = −γ ⟨δa⟩/⟨a⟩ = −2 · 0,114450/1,5 = −0,1526, also 1/γ − ½ ≈ +0,03815; voll gerechnet +0,03628 (Wolfram: 0,03814986 und 0,03627936).

Die Abweichung von ½ ist also der mittlere Flächenüberschuss der höheren Spins, gewichtet mit ihrer Häufigkeit. Spin ½ allein gäbe exakt ½.
Schrittweise: Casimir nur bis k = 2 gibt 1/γ = 0,5103, bis k = 4 0,5258, bis k = 10 0,5359, alle 0,5363. Das ist keine neue Herleitung von
β_sym; es ist die Zählregel, anders gelesen. Sie sagt aber, **was** die „Restkorrelation“ sein müsste: der Beitrag der Bänder mit j ≥ 1
(zusammen 45 % der Durchstoßpunkte).

## 3 Schleife L3 mit kleinen Störungen: welche Eingabe zieht wohin?

Ungestört liegt der Fixpunkt bei ½ (k395). Ziel wäre 1/γ_L = 0,53628.

| Störung | Richtung | trifft 1/γ_L bei |
|---|---|---|
| Reservoir unrein (Polarisation 1 − ε) | nach unten (0,497 bei ε = 0,01) | nie |
| HC-Messung nur mit Stärke η < 1 | nach unten (0,484 bei η = 0,9) | nie |
| Reservoir enthält Anteil m der letzten Ausgabe (Gedächtnis) | m > 0 nach unten, m < 0 nach oben | m = −0,2404 |
| Drehwinkel-Regel tan²α = x(1 + κ) | κ < 0 nach oben | κ = −0,2384 |
| Stärke-Regel x = (1 − b)/(1 + b)·(1 + λ) | λ > 0 nach oben | λ = +0,3129 |

Lesart: Unvollkommenheiten (unreines Band, schwache Messung, Gedächtnis mit positivem Vorzeichen) ziehen den Wert **unter** ½. Für einen Wert
über ½ braucht es eine Gegenkopplung (m < 0) oder eine geänderte Regel. Jede Zeile ist eine Zahl für eine Zahl: angepasst, nichts hergeleitet.
Für m gilt exakt (2b − 1)(b + 1) = m(b − 1).

## 4 Restkorrelation gekoppelter Bänder (Lorenz-artig, Qiskit)

- Für unabhängige Bänder multiplizieren sich die Erwartungswerte: ⟨X⊗X⟩ = b₁b₂ (für b = ½: 0,25, also 62,5 % gleiche Ausgänge). Das ist die Regel
  hinter Tuttes Angriff: kleine Abweichungen von 50 % überleben die Summe zweier Bänder.
- Zwei gleiche Schleifen L3, deren Bänder je Runde teilweise getauscht werden (Kopplung 0; 0,1; 0,3), bleiben beide bei ½, und ⟨X⊗X⟩ bleibt ¼.
  Der Tausch gleicher Zustände erzeugt keine Restkorrelation.

Befund: Eine Abweichung von ½ braucht ein Band, das **anders** ist. In der Zählregel sind das die höheren Spins mit ihrer größeren Fläche
(Abschnitt 2). Ein Mechanismus, der das aus einer Schleife über Bänder verschiedener Spins erzeugt, ist nicht gebaut.

## 5 Nachträgliche Beobachtung (kein Test)

p₁ = 2^(1−γ_L) = 0,5491607 und β_sym = 0,5494056 unterscheiden sich um 0,000245 (0,045 %). Im glatten Fall sind die zwei Größen nicht gleich
(0,5 gegen 0,577); entlang der Verbindung von glatter zu Casimir-Fläche schneiden sie sich bei t = 1,0034, also fast genau an der Casimir-Fläche
(t = 1). Exakt gleich wären sie bei γ = 1,8642932 (β = 0,5493155); die Zählregel gibt 1,8646998. Beide Werte liegen im 2σ-Fenster aus m_W
(β ∈ [0,54907; 0,54978], k358), die Daten trennen sie nicht.

In Worten hieße das: β_sym ist (fast) der Anteil der Spin-½-Durchstoßpunkte, also selbst eine Wahrscheinlichkeit nahe ½. Durchgesehen wurden
13 einfache Kenngrößen der Spinverteilung (alle in `k396_out.txt`); die nächstbeste liegt 0,0069 entfernt. Grobe Zufallsabschätzung: 0,3 % bis
0,6 %. Selten, aber nachträglich gefunden, und exakt gleich sind die Zahlen nicht. Ob dahinter eine Beziehung steht (β = p₁ als zweite Gleichung
neben der Zählregel wäre überbestimmt und stimmt nur auf 4·10⁻⁴), ist offen.

## Antwort auf die Frage

- Ja in diesem Sinn: Der Erwartungswert der HC-Messung, 1/γ_L = 0,536, ist „½ plus eine kleine systematische Abweichung“, und die Abweichung ist
  ein Mittelwert über die höheren Spins. ½ ist der Wert, den die selbstjustierende Schleife von allein findet.
- Nein in dem Sinn, dass damit etwas hergeleitet wäre: Die Abweichung kommt genau aus der Casimir-Fläche, deren Grund weiter offen ist. Die
  Frage „warum 0,549 und nicht 0,577“ wird zu „warum zählen höhere Spins mit √(j(j+1)) statt j + ½“. Das ist dieselbe offene Frage wie in r67.
- Neu ist die Richtung: eine Schleife über Bänder verschiedener Spins, in der die höheren Spins als seltene, andersartige Bänder die Abweichung
  erzeugen. Das wäre ein Test mit Vorab-Notiz wert (Kriterium: kommt √(j(j+1)) heraus oder j + ½, ohne dass die Fläche eingegeben wird).

## Bilanz der Setzungen

| Größe | Status |
|---|---|
| Zählregel mit Casimir-Fläche | Postulat (r67) |
| 1/γ − ½ = Mittelwert des Flächenüberschusses (erste Ordnung 0,0381, voll 0,0363) | hergeleitet innerhalb des Postulats |
| Störgrößen m, κ, λ der Schleife | angepasst |
| ⟨X⊗X⟩ = b₁b₂; gleiche gekoppelte Schleifen bleiben bei ½ | hergeleitet im Modell |
| p₁ ≈ β_sym auf 0,045 % | nachträglich beobachtet, ungeklärt |

## Grenzen

Kein Test. Die Schleife ist das Ein-Qubit-Modell aus k395. OP1 (Herkunft von β_sym) bleibt offen.
