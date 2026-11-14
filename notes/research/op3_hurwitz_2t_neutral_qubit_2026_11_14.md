# Erkundung: Die Hurwitz-Einheiten von H_n tragen das neutrale Qubit als 2T-Dublett

14. November 2026. Autor: „weiter“. Erkundung, nicht blind: Das Ergebnis folgt aus der Geometrie der Hurwitz-Einheiten
und dem Pauli-Tripel aus dem Nachtrag zu H103. Es gibt keinen Datenvergleich, keine H-Nummer und keine Änderung an
Guards. Einordnung T5/T8, OP3. Skript `op3_hurwitz_2t_neutral_qubit_2026_11_14.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- **Die Frage aus der Übergabe zu Weg B ist schon beantwortet.** `op3_neutral_su2_octant_2026_11_13.md`, Nachtrag
  Punkt 3: Das Oktanten-Tripel braucht nur ein Element der Ordnung 3 auf einem Qubit (Hurwitz-Einheit, 2T über A_4).
  Ein 2T-Dublett ist aber keine Darstellung der Platz-U(3) oder von A_4, und **das Spinor-Feld bleibt neu**. Der
  neutrale Sektor von Weg B (drei Trialitätsplätze) trägt nur den A_4-Vektor 3. Diese Frage wird nicht neu gestellt.
- `predictions/Ergebnis_H103_...`, Nachtrag: N = ker Q_* ist ein Rechtsmodul über H_n = span(1, e_7, e_8, e_15). Darauf
  ist i R_e7, i R_e15, i R_e8 ein Pauli-Tripel mit e_8 als ψ-Achse. Offen war, was die Raumdiagonale auszeichnet.
- `op3_sedenion_generations_estar_2026_11_14.md`: N ist der Raum zweier Neutrino-Flavours. ψ ist eine Phase innerhalb
  der Generationen.
- `op3_hopf_octant_2026_11_13.md`: Im Hopf-Träger entsteht das Oktanten-Tripel am magischen Winkel zur Ladungsachse.

## Ergebnis

**1. N ist ein natives 2T-Dublett.** Die 24 Hurwitz-Einheiten von H_n sind ±1, ±e_7, ±e_8, ±e_15 und
(±1 ± e_7 ± e_8 ± e_15)/2. Von rechts wirken sie auf N treu und unitär, und sie sind abgeschlossen. Ihre Ordnungen sind
1 (1), 2 (1), 3 (8), 4 (6) und 6 (8): Das ist die binäre Tetraedergruppe 2T. Das projektive Bild hat 12 Elemente,
also A_4. Das Spinor-Feld, das in der Feldsuche als neu galt, gibt es damit auf dem Sedenionen-Weg nativ: als
Rechtswirkung der ganzzahligen Quaternionen von H_n auf das farb- und ladungsneutrale Qubit.

**2. Die ψ-Achse ist eine zweizählige Achse dieses 2T.** Auf der Bloch-Kugel von N liegen:
- die zweizähligen Achsen (±e_7, ±e_15) senkrecht zur ψ-Achse;
- ±e_8 auf der ψ-Achse;
- alle vier dreizähligen Achsen (Raumdiagonalen) unter **|cos| = 1/√3** zur ψ-Achse.

Der magische Winkel ist also der Winkel zwischen einer zweizähligen und einer dreizähligen Achse der nativen Hurwitz-
Gruppe.

**3. Der Bezug ist nativ: ein Eigenzustand einer Hurwitz-Einheit der Ordnung 3.** Für h = (1 + e_7 + e_8 + e_15)/2
geben beide Eigenzustände von R_h unter ψ ρ² = 1/2, K = 2/3 und die Bargmann-Phase π/4. Alle acht Einheiten der
Ordnung 3 liegen unter demselben Winkel und sind in diesem Sinn gleichwertig. Damit ist die offene Frage aus dem
Nachtrag zu H103 beantwortet: Die Raumdiagonale ist die Drehachse einer Hurwitz-Einheit der Ordnung 3. Ausgezeichnet
ist sie durch die ganzzahlige Struktur von H_n, nicht durch eine freie Wahl.

**4. ψ und 2T sind verschiedene Dreierstrukturen.** ψ normalisiert 2T nicht. Von den 24 Hurwitz-Einheiten bildet ψ
nur ±1 und ±e_8 auf Hurwitz-Einheiten ab. Gegenüber dem ursprünglichen Oktantenbild sind die Rollen vertauscht:
- Ursprünglich ist der Zyklus die dreizählige Drehung und der Bezug ein Eigenzustand einer zweizähligen Achse.
- Hier dreht ψ um eine zweizählige Achse, und der Bezug sitzt auf einer dreizähligen.

Der Winkel und damit K und die Phase sind in beiden Fällen gleich.

## Bewertung
- **Positiv:** Auf dem Sedenionen-Weg mit der Ladungsachse e_8 sind jetzt alle drei Bausteine des Oktanten-Tripels
  nativ:
  - der farb- und ladungsneutrale Träger N;
  - der Zyklus ψ der Ordnung 3;
  - der Bezug als Eigenzustand einer Hurwitz-Einheit von H_n (2T, von rechts).

  Das Spinor-Feld, das in der Feldsuche fehlte, ist hier die Rechtswirkung von 2T auf N.
- **Einschränkungen:**
  - ψ ist kein Generationsschritt, und N enthält nur zwei Neutrino-Flavours (Weg A, K28).
  - Die Ladungsachse e_8 und die physikalische Rolle der Rechtswirkung bleiben Annahmen.
  - Offen ist, welche der vier dreizähligen Achsen und welcher Eigenzustand gilt. Für K und |Phase| ist das
    gleichgültig.
- **Nicht gezeigt:** warum nur der Majorana-Block diesen Bezug sieht und wie ein Koide-Spektrum aus zwei Flavours mit
  drei Massen folgen soll.
- Das ist nachträglich und mit bekanntem Ziel; Koide ist **nicht** hergeleitet. OP3/OP4 bleiben offen. OP1–OP5, C5 und
  C6/T2 sind unverändert. H100 und H102 bleiben unberührt.
- Zurückgestellte Ideen: Keiner der Auslöser I1–I5 trifft zu.
