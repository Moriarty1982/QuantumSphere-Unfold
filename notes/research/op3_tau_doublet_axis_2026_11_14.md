# Erkundung: Keine zweizählige Achse unter dem magischen Winkel auf dem τ-Dublett von O³

14. November 2026. Autor: „Ja, Lücke prüfen“. Geprüft wird die in
`op3_third_generation_singlet_2026_11_14.md` benannte Lücke: ob die Trialität (r37) oder das A_4 aus r55 auf dem
τ-Dublett von Weg B eine zweizählige Achse außerhalb des Äquators liefert. Rückwärtssuche. Erkundung, nicht blind (die
Aussagen folgen aus der Gestalt der Operationen und sind nur nachgerechnet), kein Datenvergleich, keine H-Nummer, kein
MMA-Beleg, keine Änderung an Guards. Einordnung T5/T7/T8, OP3. Skript `op3_tau_doublet_axis_2026_11_14.py`, Ausgabe
`..._out.txt`.

## Vorwissen geprüft
- `op3_third_generation_singlet_2026_11_14.md`: τ-symmetrisches 2 + 1 in O³; S_3 gibt nur 90°.
- `op3_triality_carrier_gate_2026_11_12.md`: Slotoperationen τ und ρ; diagonale Automorphismen; Spin(8) wirkt nach r37
  auf den drei Slots als verschiedene Darstellungstypen, je innerhalb eines Slots.
- `op3_neutral_su2_octant_2026_11_13.md`: Der Zentralisator der Farb-su(3) in so(8) ist zweidimensional und abelsch;
  A_4 hat keine Spinor-Darstellung, 2T schon.
- r55 (über `op3_selection_principle_2026_11_13.md` und `op3_generation_carrier_review_2026_11_13.md`): A_4 als
  gemeinsame Platzsymmetrie, Klein-Gruppe als Vorzeichenwechsel, ℤ₃ als Zyklus.
- `op3_hurwitz_2t_neutral_qubit_2026_11_14.md`: 2T in Weg A aus den Hurwitz-Einheiten.

**Nicht neu gerechnet:** Die Trialitätsabbildungen selbst. Benutzt wird nur, dass Spin(8) innerhalb jedes Slots wirkt.

## Bedingung (rückwärts)
Der Slotraum einer Teilchenart ist C³ (Schur). Das Dublett sind die Fourier-Moden (ω, ω̄), das Singulett ist die
symmetrische Mode. Gesucht ist ein Element g, das diese Zerlegung erhält und auf dem Dublett eine Drehung um 180° ist,
deren Achse mit der τ-Achse den Winkel arccos(1/√3) bildet. Zusammen mit τ erzeugt ein solches g auf dem Dublett die
Gruppe 2T (nachgerechnet, Ordnung 24).

## Ergebnis

**1. Monomiale Operationen geben nur 0° und 90°.** Eine monomiale Slotoperation ist eine Permutation mal Phasen je
Slot. Dazu gehören τ, der Slotteil von ρ, die Vorzeichenwechsel von A_4 und alle Phasen, die innerhalb eines Slots
wirken. Mit Phasen aus den 12. Einheitswurzeln sind das 10 368 Elemente. Davon erhalten 72 die Zerlegung 2 + 1, und auf
dem Dublett wirken sie so:
- 12 als Eins,
- 24 als Drehung um 120° um die τ-Achse,
- 36 als Drehung um 180° um eine Achse senkrecht zur τ-Achse.

Der magische Winkel kommt nicht vor. Grund: Eine monomiale Matrix hält die symmetrische Mode nur fest, wenn ihre
Phasen gleich sind. Übrig bleibt dann eine Permutation mal Zahl, also S_3.

**2. A_4 erhält die Zerlegung 2 + 1 nicht.** Von den vier Vorzeichenwechseln hält nur die Eins die symmetrische Mode
fest; diag(1, −1, −1) gibt ⟨sym|·|sym⟩ = −1/3. Unter A_4 sind die drei Slots eine irreduzible Darstellung (der
Vektor). Das τ-Dublett ist kein A_4-invarianter Raum, also wirkt A_4 gar nicht auf ihm.

**3. Die Trialität ändert daran nichts.** Spin(8) wirkt innerhalb jedes Slots, und der Teil, der mit der Farbe
vertauscht, ist abelsch. Auf dem Slotraum einer Teilchenart sind das Phasen je Slot, also wieder monomiale
Operationen. Die äußeren Automorphismen sind die Permutationen.

**4. Das gesuchte Element ist nicht monomial.** Für drei Azimute der Achse hat g im Slotraum acht oder neun von neun
Einträgen ungleich null, mit Beträgen wie 1/3, √2/3, 1/√3, 2/3 und √(2/3). Es überlagert die drei Slots kohärent.

**5. Gegenprobe Weg A.** Auf dem Slotpaar S = O ⊕ O e_8 sind R_e7, R_e8 und R_e15 monomial: R_e7 bleibt in den
Slots, R_e8 und R_e15 vertauschen sie. Die Hurwitz-Einheit R_h ist nicht monomial; sie ist die Summe
(1 + R_e7 + R_e8 + R_e15)/2. In Weg A entsteht 2T also, weil das Dublett ein Paar von Slots ist: Dort bilden
monomiale Operationen schon die Quaternionengruppe, und die Algebra erlaubt ihre halbzahlige Summe.

## Bewertung
- **Die Lücke wird von den vorhandenen Operationen nicht geschlossen.** Weder S_3 noch A_4 (r55) noch die
  slotweise Trialität (r37) liefern auf dem τ-Dublett eine Achse unter dem magischen Winkel.
- **Struktureller Grund:** Die Quaternionengruppe braucht ein Dublett aus zwei Slots (Weg A). Der Slotzyklus τ
  braucht drei Slots und macht das Dublett zum Fourier-Paar (Weg B). Auf dem Fourier-Paar sind monomiale Operationen
  nur eine Diedergruppe. Beide Forderungen zugleich verlangen eine Operation, die Slots addiert, also eine
  Algebrastruktur auf O³, in der die Summe von Slotoperationen selbst eine Operation ist.
- **Was das für die Linie heißt:** Mit dem jetzigen Bestand ist das Profil (drei Generationen, Zyklus der Ordnung 3
  auf einem neutralen Qubit, Bezug unter dem magischen Winkel) nicht erfüllbar. Jeder der beiden Wege erfüllt einen
  Teil. Das ist die vierte Variante mit derselben offenen Voraussetzung; nach der Suchrichtungs-Regel ist hier
  anzuhalten.
- Nicht ausgeschlossen: eine neue Struktur auf O³, etwa die Jordan-Algebra der hermiteschen 3×3-Matrizen über O mit
  F_4. Sie ist im Companion nicht angelegt und wurde nicht geprüft. Aus Vorwissen, ungeprüft: Dort drehen reelle
  Operationen die Slots als Vektor; reelle Operationen geben auf dem Fourier-Paar ebenfalls nur 0° und 90°.
- Koide 2/3 und die Phase sind **nicht** hergeleitet. OP3/OP4 bleiben offen. OP1–OP5, C5 und C6/T2 sind unverändert.
  H100 und H102 bleiben unberührt.
- Zurückgestellte Ideen: Keiner der Auslöser I1–I5 trifft zu.

## Mögliche nächste Schritte (Autorentscheidung)
- Die Linie ablegen, bis H100 oder H102 entschieden sind (Empfehlung).
- Statusvermerk in einer neuen Runde: Profil der fehlenden Struktur mit den vier Befunden vom 14.11.
