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
