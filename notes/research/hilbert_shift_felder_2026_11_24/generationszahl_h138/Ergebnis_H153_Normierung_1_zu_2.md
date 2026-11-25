# Ergebnis H153: Eine Normierung wählt nur die Startlinie; nur die Einschränkung auf die Unteralgebra {1, U} gibt K = ⅔ exakt

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H153_Normierung_1_zu_2.md` (Commit fd4c7f3). Skripte `k336_normierung.py` (`k336_out.txt`), `k336b_gegenprobe.wl`
(`k336b_out.txt`, Wolfram). Status: H153a, c, d bestätigt; H153b bestätigt bis auf eine Teilvorhersage (N1 und N2 geben dasselbe K, nicht verschiedene).**

Anlass: Autor „erst die normierung“. Gelesen als: Gibt es eine aus der Algebra begründete 1:2-Normierung, die den skalenfreien Fluss (H150/H151) auf K = ⅔ zieht, die
Startabhängigkeit beseitigt, π/4 stabil hält, und wirkt sie auf δ? Werkzeuge: Python (sympy für die β-Funktionen und die Kovarianz, scipy für den Fluss), Wolfram unabhängig
(β über direkte Koeffizienten mit Restprüfung, Kovarianz, Fluss mit WorkingPrecision 30). Alle gemeinsamen Werte stimmen auf zehn Stellen. Qiskit nicht eingesetzt
(keine Schaltungsfrage).

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H153a | β mit B̂ = s\|y\|² minus konjugierter Fluss S⁻¹β(Sĝ): Nullrest (Python und Wolfram); GW-Bedingung κ + 2√(λ_Aλ_B) = 0 hat in den Hut-Kopplungen dieselbe Form; K am GW-Punkt hängt nur am physikalischen λ_A/λ_B | exakt | **bestätigt** (nicht blind) |
| H153b | N1: K 0,6780 … 0,9776, Std 0,114; N2: identisch mit N1; N3: K 0,5602 … 0,6778, Std 0,046; 3σ-Treffer 0/24 je Normierung; \|θ − π/4\| < 0,01: 8/24, 8/24, 12/24 | Std < 10⁻³; Treffer; θ stabil | **bestätigt**: keine startunabhängig, keine trifft, θ nicht stabil. Teilvorhersage „verschiedene Mittelwerte“ für N1/N2 falsch (Erklärung unten) |
| H153c | N4 (n_A = n_B = 1), 24 Starts: max \|K − ⅔\| = 0 (Python), < 10⁻²⁹ (Wolfram); θ = π/4 exakt; ⅔ liegt 0,81σ vom Messwert | alle innerhalb 10⁻⁹ | **bestätigt**; aber Setzung über die Freiheitsgrade |
| H153d | mit ξ ≠ 0 (Ansatz H152): δ auf 0 oder π/3 in 12/12 je Normierung (N1, N2, N3) | δ ∈ {0, π/3} | **bestätigt** |

## Lesart
- **Eine Normierung ist eine Umparametrisierung.** Wer A und B anders normiert (je Komponente, nach der Spur der Auslesung 1/3 : 2/3, über drei statt zwei Kopien),
  rechnet denselben Fluss in anderen Koordinaten (Nullrest in H153a). Sie ändert nur, welche Startwerte „symmetrisch“ heißen. Weil die Einschleifen-β-Funktionen homogen vom
  Grad 2 sind, zählt dabei nur der Startstrahl: Eine Gesamtskala ändert nur τ, nicht K. Deshalb sind N1 (a = 1, b = 2) und N2 (a = ⅓, b = ⅔) gleich: beide haben b/a = 2.
  Das war vor der Rechnung nicht bedacht (nachträglich erklärt).
- **K hängt dann nur an κ̂/λ und an b/a.** Für N1/N2 liegt K immer über ⅔ (0,678 … 0,978), für N3 schneidet es ⅔ zwischen κ̂/λ = −0,5 (K = 0,66624) und −0,2. ⅔ wäre
  also mit N3 erreichbar, aber nur über einen gewählten Startwert, also ein Fit. Für κ̂ → 0⁻ laufen alle drei auf denselben Grenzwert 1/3 + √10/9 aus H151.
- **Nur eine Änderung der Freiheitsgrade hilft.** Läuft die Schleife nur über die von Ψ erzeugte Unteralgebra {1, U} ≅ ℂ (eine Komponente je Seite), ist der Tausch J eine
  exakte Symmetrie des Flusses (β_λA − β_λB = 0 bei λ_A = λ_B), und jeder symmetrische Start mit κ < 0 endet bei θ = π/4 und K = ⅔, unabhängig von λ und κ. Das ist kein
  Fit, aber eine Setzung: Es legt fest, dass die zweite Richtung der Kopien-Ebene nicht in der Schleife läuft, und friert damit δ ein. Ob die Algebra das erzwingt, ist die
  offene Frage. Sie ist dieselbe wie in H151 („Komponentenzahl ist eine Lesart“), jetzt scharf gestellt.
- **δ bleibt unberührt.** Alle Normierungen gewichten nur die Normen A und B um; die Z₃-Struktur der Ebene sieht sie nicht. Mit ξ ≠ 0 landet δ weiter auf 0 oder π/3.

## Grenzen
- Eine Schleife, ohne Eichfelder. Die vier Kandidaten sind die aus der Vorab-Notiz; weitere Normierungen mit derselben Art (i) ändern nach H153a nichts Grundsätzliches.
- N4 ist eine Setzung über die Freiheitsgrade, keine Herleitung; sie wird hier nicht als Lösung von OP3 geführt.
- Wolfram: Ein erster Lauf mit SolveAlways lieferte im Fall B = s|y|² keine vollständige Lösung; ersetzt durch direkte Koeffizienten mit Restprüfung (in `k336b_out.txt` vermerkt).
- OP3 offen; kein Vorzeichen gesetzt; kein Guard berührt.
- Vergeben: H153, k336. Nächste frei: H154, k337.
