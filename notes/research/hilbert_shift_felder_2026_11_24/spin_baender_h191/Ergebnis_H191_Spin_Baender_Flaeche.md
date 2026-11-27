# H191: Entsteht in einer Schleife über Bänder verschiedener Spins die Casimir-Fläche √(j(j+1))? (Test, k397, 27.11.2026)

**Status:** Test mit Vorab-Notiz (`notes/research/predictions/Vorab_Notiz_H191_Spin_Baender_Flaeche.md`, committet vor der Rechnung). H191a ist
nicht blind (Kontrolle), H191d ein Bericht. **Werkzeuge:** Python auf der Maschine `qam/examples/coprocessor/stufe2/` (Bausteine gegen Qiskit
geprüft), Wolfram für das Zielprofil und eine Runde exakt. Gerechnet am 27.11.2026.

## Idee des Tests
Die Zählregel (r67) gewichtet Band k (Spin j = k/2) mit 2^(−γ a_k), a_k = √(k(k+2)/3). Für die stationäre Verteilung p_k einer Schleife heißt
das: das γ- und skalenfreie Profil r_k := ln(p_k/p_{k+1}) / d_∞ muss, damit „Casimir“ herauskommt, gleich √3 (a_{k+1} − a_k) sein (1,0964; 1,0446;
1,0260; 1,0171 für k = 1..4), und für die glatte Fläche j + ½ gleich 1. Die Fläche a_k wird nicht eingegeben; sie wird aus den Gewichten abgelesen.

## Maschine
Eine Runde auf dem Band: `ROT alpha` (Drehung um 2α), `HC` (S_x messen, verwerfen), `ADD mu` (ein Qubit |+⟩ ankoppeln, Gesamtspin messen:
k → k±1 nach Clebsch-Gordan), `DROP lam` (ein Qubit abgeben: k → k−1). Start Band 1, |+⟩. Gitter: α ∈ {π/6, π/4, π/3}, (μ, λ) ∈ {(0,25; 0,5),
(0,5; 1,0), (0,2; 0,6), (0,4; 0,6)}; zwölf Punkte; stationär bis 10⁻¹².

## Ergebnis

**H191a (nicht blind, bestätigt).** Für α = 0 bleibt der Zustand voll entlang x polarisiert, `ADD` führt immer nach oben, und die Verteilung ist
exakt geometrisch: |r_k − 1| ≤ 10⁻¹⁴ an allen vier (μ, λ). Das ist die glatte Fläche j + ½ als Vergleichsfall der Maschine, und zugleich eine
Prüfung, dass die Bausteine stimmen (Wolfram: eine Runde exakt, Maschine gleich).

**H191b (Casimir-Profil): widerlegt.** 0 von 12 Gitterpunkten im Fenster ±0,015. Der Abstand des Profils zum Casimir-Profil liegt an allen
nicht entarteten Punkten zwischen 0,23 und 0,35.

**H191c (glattes Profil): widerlegt.** 0 von 12 Gitterpunkten. Abstand zum glatten Profil 0,14 bis 0,25.

**H191d (Bericht).** Jeder nicht entartete Punkt hat einen geometrischen Schwanz (d_k konvergiert), aber d_∞ hängt von α und (μ, λ) ab
(1,67 bis 2,65), und das Profil r_k steigt von unten gegen 1 (r_1 zwischen 0,75 und 0,88), also **von der falschen Seite**: Das Casimir-Profil
liegt über 1, die Maschine bleibt darunter. Der Abfall von r_k − 1 geht wie 1/k, während das Casimir-Profil wie 1/(2k²) gegen 1 geht (Wolfram).

**Fehler im Gitter, offen benannt:** Die vier Punkte mit λ = 1,0 sind entartet (jedes Qubit wird sofort wieder abgegeben, alles Gewicht bleibt auf
Band 0). Sie können kein Fenster erfüllen und sind in der Zählung als „entartet“ ausgewiesen; die Aussage stützt sich auf die acht gültigen Punkte,
die alle weit außerhalb beider Fenster liegen.

## Lesart
Die Schleife erzeugt zwar einen Turm besetzter Bänder mit geometrischem Schwanz, aber das Gewichtsprofil ist das der Clebsch-Gordan-Faktoren
(Korrekturen in 1/k), nicht das der Casimir-Fläche (1/k²). Die Fläche √(j(j+1)) steht in der Maschine als Eigenwert von S² zur Verfügung, aber die
**Dynamik** benutzt sie nicht als Gewicht der Bänder. Die Erwartung aus der Vorab-Notiz (beide widerlegt) trifft zu. Damit bleibt die Herkunft der
Casimir-Fläche und von β_sym offen (OP1); dieser Weg ist erledigt.

## Bilanz der Setzungen
| Größe | Status |
|---|---|
| Rundenschritte, Bezugsband |+⟩, kollektiver HC, Auf-/Abbau um ein Qubit | gesetzt (vorab) |
| Gitter, Schwelle 0,015, Bänder für d_∞ | gesetzt (vorab) |
| Zielprofile (Casimir, glatt) | aus r67 und k245 |
| Fläche a_k | **nicht** eingegeben; aus p_k abgelesen |
| Ergebnis (Profil von unten gegen 1, Abfall 1/k) | hergeleitet/gemessen |

## Grenzen
Ein Qubit Auf- und Abbau je Runde; andere Übergangsregeln (mehrere Qubits, andere Bezugszustände) nicht geprüft. Kein Bezug zu Messdaten.
Nächste frei: H192, k400 (k398, k399 vergeben).
