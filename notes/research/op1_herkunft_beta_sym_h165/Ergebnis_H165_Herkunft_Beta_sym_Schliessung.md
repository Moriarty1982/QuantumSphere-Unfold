# Ergebnis H165: Die Überlapp-Schließung erzwingt den Hopf-Wert 1/√3, nicht β_sym; der Wert 0,5494 entsteht erst aus Casimir-Spektrum und Ein-Bit-Einheit

**Stand:** 2026-11-26. Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H165_Herkunft_Beta_sym_Schliessung.md` (Commit e81f649, vor dem ersten Skriptlauf).
**Überwiegend nicht blind** (in der Vorab-Notiz offengelegt). Skripte: `k356_test_h165.py` (mpmath, sympy, Qiskit 2.6.2 `quantum_info`), `k356b_gegenprobe.wl`
(Wolfram, unabhängig). Ausgaben: `k356_out.txt`, `k356b_out.txt`. Beide stimmen in allen Zahlen überein. Kein HDL/MMA-Vergleich (kein RUN_TAPE-Ablauf).
Kein Guard berührt. Sichtung der früheren Versuche: `Sichtung_Herleitungsversuche.md`.

## Frage des Autors
Woher kann 0,5493 kommen, und wieso müsste genau das folgen?

## Antwort in drei Sätzen
1. **Woher:** β_sym ist durch eine einzige Gleichung festgelegt. γ_L ist die Wurzel von Σ_{k≥1} 2^(1 − γ_L·√(k(k+2)/3)) = 1, und β = √((γ_L−1)/(γ_L+1)).
   Das gibt γ_L = 1,8646997646 und **β = 0,5494056410** (der Wert 0,5493482 im Bestand kommt aus gerundeten Eingaben, r64.6b).
2. **Was hineingeht:** drei Zutaten. (i) Gewicht 2 für jeden Spin (m = ±j, zwei Auslesen), (ii) die Fläche √(j(j+1)), (iii) die Einheit „ein Bit bei j = ½“ für T.
   Lässt man (ii) weg und nimmt j + ½, wird γ_L = 2 und β = 1/√3 exakt (k245).
3. **Wieso es folgen müsste:** Das ist nicht gezeigt. Keiner der 37 gesichteten Versuche und keiner der hier geprüften Kandidaten leitet die drei Zutaten her.
   Die Zwei-Auslesen-Lesart aus H161/H164 liefert von sich aus eine Schließungsbedingung, aber die erzwingt den Hopf-Wert, nicht den gemessenen.

## Urteil nach den vorab festgelegten Kriterien
| Kriterium | Vorhersage | Ergebnis |
|---|---|---|
| K-a Ziel (nicht blind) | bestätigt | **bestätigt:** eine Wurzel, gleich γ_M/γ_T auf 39 Stellen; Hopf-Variante exakt 2 |
| K-b Schließung mit Überlappen trifft 0,549406 | widerlegt | **widerlegt:** ⅓; 1/√3; 0,7598; 0,5240; 0,6886 (nächster 4,6 % daneben) |
| K-c Zahlenkandidaten, Identität auf 10⁻⁸ | keine Identität | **keine Identität**; 3 von 13 Vergleichen innerhalb 10⁻³ |
| K-d Kegel (Identität, nicht blind) | bestätigt | **bestätigt** |
| Gesamt | widerlegt | **widerlegt** |

## Befunde
1. **Das Ziel (K-a).** Z(g) = Σ 2^(1 − g·c_k) fällt monoton; Z = 1 hat die eine Wurzel 1,86469976460937256352785741676 = γ_M/γ_T (Differenz numerisch null bei
   40 Stellen). Mit c_k = (k+1)/2 ist die Summe 2x²/(1−x) mit x = 2^(−g/2), die Wurzel x = ½, also g = 2 (symbolisch).
   Die Formulierung von K-a in der Vorab-Notiz war an dieser Stelle verstümmelt; gemeint und gerechnet ist c_k = (k+1)/2.
2. **Die Überlapp-Schließung erzwingt den Hopf-Wert (K-b).** Für das Paar (K₁, S) aus H164 ist |⟨j; K₁|j; S⟩| = β^{2j} (Qiskit, 2j = 1 … 6). Die Summe der
   Übergangswahrscheinlichkeiten über alle Spins mit Gewicht 2 ist Σ_j 2β^{4j} = 2β²/(1−β²), und sie ist genau dann 1, wenn β² = ⅓. Die anderen vier Varianten
   treffen den gemessenen Wert auch nicht; nötig wäre die Potenz p = 1,8343, keine natürliche Zahl.
3. **Nachträglich gefunden (nicht in der Vorab-Notiz):** Σ_{j≥½} 2·|⟨j; K₁|j; S⟩|² = γ_L − 1 gilt als Identität für jedes β (Wolfram: symbolischer Nullrest).
   Also **γ_L = 1 + Σ_{j≥½} 2β^{4j}**: γ_L ist in der Lesart C das Gesamtgewicht der Übergänge zwischen den zwei Auslesen über alle Spins, wenn j = 0 mit Gewicht 1
   mitzählt. Beim gemessenen Wert ist die Summe 0,8647 statt 1. Die Bedingung „Summe = 1“ ist dasselbe wie γ_L = 2. Das ist eine Umformung von
   γ_L = (1+β²)/(1−β²), keine Herleitung, aber sie sagt, was der Hopf-Wert in dieser Lesart bedeutet: Die Übergänge aller Spins j ≥ ½ wiegen zusammen genau so viel
   wie der Spin 0.
4. **Zahlenkandidaten (K-c).** Keine Identität. Innerhalb 10⁻³ liegen drei Vergleiche, die zwei Sachverhalte sind:
   - 2^(1−γ_L) = 0,549161 gegen β = 0,549406 (−4,5·10⁻⁴): der Anteil der j = ½-Durchstoßpunkte in der M-Zählung ist fast der Überlapp der zwei Auslesen. Die
     selbstkonsistente Gleichung 2^(1−g) = √((g−1)/(g+1)) hat die Wurzel g = 1,864293, β = 0,549315 (−2,2·10⁻⁴ in γ_L). Beides sind feste Zahlen; sie sind verschieden.
   - 1/⟨c⟩ = 0,658150 gegen artanh(1/√3) = 0,658479 (−5,0·10⁻⁴).
   Beide waren vor dem Lauf bekannt oder überschlagen (nicht blind). Von den blinden Vergleichen (Nr. 2 ausgenommen, das Nr. 1 umformt) traf keiner: ⟨k⟩ = 1,8432,
   ⟨√(j/(j+1))⟩ = 0,6560, ⟨1/c⟩ = 0,7775, p₁/(1−p₁) = 1,2181, ⟨c⟩ = 1,5194. Eine Zufallswahrscheinlichkeit gebe ich dafür nicht an, weil die Kandidaten nicht zufällig gewählt sind; als Identität sind beide ausgeschlossen.
   Sie werden als **unerklärte Zahlentreffer** geführt, nicht als Stütze.
5. **Kegel (K-d).** Der Hopf-Wert ist der Kosinus des Kegelwinkels eines Spins ½ im Vektormodell, j/√(j(j+1)) = 1/√3, und der doppelte Kegelwinkel ist der
   Tetraederwinkel arccos(−⅓) = 109,47° aus der Erkundung zu H164. Der Faktor √3 in c_k und in γ_T = ln 2/(π√3) ist dieselbe Zahl.

## Was das bedeutet
- Die Hopf-Lücke ist jetzt von zwei Seiten dieselbe Aussage: In der Zählung entsteht 1/√3 mit j + ½ (k245), in der Zwei-Auslesen-Lesart mit den Überlappen
  kohärenter Zustände, die nur 2j kennen und keinen Casimir. Der gemessene Wert verlangt in beiden Bildern die Fläche √(j(j+1)).
- Eine Herleitung von β_sym müsste deshalb genau eines leisten: begründen, warum das Gewicht eines Spins 2^(−γ_L·c_k) mit der Casimir-Fläche ist und nicht die
  Übergangswahrscheinlichkeit β^{4j}. Am Spin ½ sind die beiden Gewichte 0,549161 und 0,603693.
- **Bilanz der Setzungen (Regel aus AGENTS.md, weil OP1 wiederholt „trägt teilweise“ ergab):** Das Ziel selbst ist eine gesetzte Eingabe. β_sym ist als Verhältnis
  zweier Literaturwerte definiert (F11), und die Frage „warum 0,5494“ entsteht nur in der Zerlegung „M zählt alle Spins, T nur j = ½“. Gesetzt sind: die
  U(1)-Zählung mit Gewicht 2, das Casimir-Spektrum, die Ein-Bit-Einheit, die Zuordnung der zwei Regeln zu den Frames. Hergeleitet ist: die Umrechnung
  γ_L ↔ β (`thm:symmetric-frame`), die Identitäten aus H164 und die aus Befund 3. Die offene Wahl ist seit r63 nicht gewandert; sie heißt weiter „Zählregel“.
  Die Weggabelung für den Autor: die Zählregel als Postulat annehmen (wie am 26.11. die Frame-Gleichberechtigung) und β_sym als daraus exakt berechnete Zahl
  führen, oder weiter nach einer Herleitung der Regel suchen.

## Grenzen
Geprüft sind nur Schließungen mit kohärenten Zuständen in der gesetzten Lesart C. Die Sichtung der 37 Versuche stammt aus einer Durchsicht durch einen Subagenten;
gegengelesen sind nur Stichproben. Kein Datenvergleich. β_sym bleibt Eingabe; OP1 bis OP5 bleiben offen.
