# Erkundung: nativer Bezugszustand für das Oktanten-Tripel in den Sedenionen

13. November 2026, spät. Autorenauftrag: „Bezugszustand suchen“. Anlass: In der farbneutralen Sedenion-Ebene (e_7, e_15)
wirkt der Generationszyklus als Element der Ordnung 3, aber reelle Zustände geben nur K = 1/2; gefehlt hat ein Bezug
unter dem magischen Winkel (`op3_neutral_su2_octant_2026_11_13.md`, Prüfung Punkt 3). Erkundung, nicht blind, kein
Datenvergleich. Keine H-Nummer, kein MMA-Beleg, keine Änderung offener Guards. Einordnung T5/T8, OP3.
Skript `op3_sedenion_reference_2026_11_13.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- r13 (Sedenionen S = O ⊕ O e_8, ψ dreht die sieben Ebenen (e_i, e_{i+8}) um 2π/3, Aut(S) = G_2 × S_3, Gillard–Gresnigt).
- r55 (A_4 als Platzsymmetrie), Hurwitz-Einheit und binäre Tetraedergruppe (Prüfung Punkt 3), Hopf-Notiz (magischer
  Winkel = orthonormale Platzrichtungen).

## Ergebnis

**1. Was der Bezug sein muss.** Im Oktanten liegen die zweizähligen Achsen (Koordinatenachsen) unter dem magischen
Winkel 54,74° zur dreizähligen Achse (Raumdiagonale); der Bezug ist ein Eigenzustand einer zweizähligen Achse. Das
leistet A_4 (mit Klein-Gruppe), nicht S_3: In der Diedergruppe D_3 stehen die zweizähligen Achsen senkrecht zur
dreizähligen. Deshalb gab die Ebene (e_7, e_15) allein nur K = 1/2.

**2. Die Sedenionen haben eine farbneutrale Quaternionenalgebra.** H_n = span(1, e_7, e_8, e_15) ist assoziativ,
e_7 e_8 = e_15, e_15² = −1 (numerisch); es ist die Cayley-Dickson-Verdopplung von span(1, e_7). Alle vier Einheiten
werden von der Farb-SU(3) festgehalten (e_7 als Stabilisatorachse, e_8 von G_2 fest, e_15 = e_7 e_8).

**3. Der Zyklus ψ ist dort eine Drehung um 120° um e_8.** ψ ist ein Automorphismus von S (Fehler 10⁻¹⁴), hält e_8 fest und
dreht (e_7, e_15) um 120°.

**4. Der Bezug ist nativ: die Raumdiagonale des farbneutralen Dreibeins.** f = (e_7 + e_8 + e_15)/√3 steht genau unter
dem magischen Winkel zu e_8 (cos = 1/√3). Ihre Bahn unter ψ ist orthonormal, und als Qubits (Spinoren von H_n) gelesen
gibt sie ρ² = 1/2, **K = 2/3** und die Bargmann-Phase **π/4**. Das ist das Oktanten-Tripel, aus nativen Bausteinen:
der Zyklus ψ aus r13, die farbneutrale Quaternionenalgebra H_n und deren Raumdiagonale.

**5. Das Hindernis ist jetzt die Ladung.** ψ vertauscht nicht mit L_e7: Er dreht e_7 nach e_15. Und L_e7 dreht die Ebene
(e_8, e_15) in sich, diese Richtungen tragen also die zu J = L_e7 gehörende Ladung. Wenn die elektrische Ladung im
Companion an e_7 hängt (J = L_e7), ist dieser Träger nicht Q_em-verträglich. Eine Ladung ist auf den Sedenionen im
Companion allerdings nicht definiert; die Prüfung gilt unter der Annahme, dass sie über L_e7 fortgesetzt wird.

## Bewertung
- Der gesuchte Bezugszustand existiert nativ: die Raumdiagonale von (e_7, e_8, e_15). Mit ihm liefern die Sedenionen
  das Oktanten-Tripel farbneutral, mit genau den Werten von H99 (Überlappung 1/2, Rang 2, Phase π/4).
- Offen und wahrscheinlich hinderlich: die Ladung. Mit J = L_e7 trägt der Träger Ladung; ein farb- und
  ladungsneutraler Ort ist damit weiter nicht gefunden. Ob die Ladung auf den Sedenionen anders fortzusetzen ist, ist
  die nächste Frage.
- Nicht gezeigt: warum nur die Neutrinos diesen Träger sehen; wie der Sedenion-Anteil an den Platzüberlappungen
  hängt. Nachträglich, mit bekanntem Ziel.
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert; H100 unberührt.

## Nachtrag: Ladung auf die Sedenionen fortgesetzt (13.11., spät, Autor: „Ladung fortsetzen“)

Vorwissen: k85 (`k85_test_h29.py`) definiert die Ladung auf O als Q8 = 1/2 − (i/6) L_e7 − (i/3) R_e7 (Eigenwerte 0, 1/3,
2/3, 1), Q_em = Isospin + Q − 1/2. Skript, Abschnitte „Ladung auf die Sedenionen fortsetzen“ und „Alternative“.

**1. Natürliche Fortsetzung.** Q_S = 1/2 − (i/6) L_e7 − (i/3) R_e7 mit sedenionischer Multiplikation stimmt auf O mit Q8
überein, vertauscht aber nicht mit ψ.

**2. Keine Fortsetzung vertauscht mit ψ.** Gesucht wurde jedes Q auf S, das auf O gleich Q8 ist und mit ψ vertauscht
(lineares Gleichungssystem für alle übrigen Einträge). Kleinster Restfehler 0,75: **nicht lösbar.** Grund: ψ dreht die
Ladungsachse e_7 nach −e_7/2 + (√3/2) e_15; die einzige ψ-feste imaginäre Richtung ist e_8. Der Generationsschritt ψ
der Sedenionen ist also mit der Ladung des Companion in keiner Fortsetzung verträglich.

**3. Ladungsverträgliche Alternative.** Die Konjugation mit dem symmetrischen Punkt a = exp(2πe_7/3) aus r15, auf S
fortgesetzt, hält e_7 fest, vertauscht mit Q_S und dreht (e_8, e_15) um 120°. Die Raumdiagonale (e_7 + e_8 + e_15)/√3
steht auch zu e_7 unter dem magischen Winkel, ihre Bahn ist orthonormal: wieder das Oktanten-Tripel. Aber:
- Diese Konjugation ist auf S **kein Automorphismus** (Fehler 21; auf O war sie einer).
- Unter Q_S tragen die komplexifizierten Richtungen von span(1, e_7, e_8, e_15) die Ladungen 0, 1, 1/3, 2/3; die
  Richtungen e_8, e_15 sind quarkartig geladen. Der Träger ist also nicht ladungsneutral, und der Bezugszustand mischt
  Ladungen.

**Bewertung.** Mit der Ladung des Companion gibt es in den Sedenionen keinen farb- und ladungsneutralen Träger des
Oktanten-Tripels: Der Automorphismus ψ verletzt die Ladung in jeder Fortsetzung; die ladungsverträgliche Drehung um e_7
ist kein Automorphismus und läuft durch geladene Richtungen. Die Fortsetzung Q_S ist dabei eine Annahme (im Companion
ist auf S keine Ladung definiert); das Ergebnis 2 gilt für jede Fortsetzung, die auf O die bekannte Ladung behält.
Die Suche nach einem nativen Träger ist damit auch in den Sedenionen negativ. OP3/OP4 offen; H100 unberührt.
