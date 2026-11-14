# Erkundung: Generationsstruktur unter der e_8-Ladung Q_*

14. November 2026. Autor: „weiter“; gewählt wurde Punkt (b) der Übergabe: ob Q_* auf den Fermionzuständen die
bekannten Ladungen gibt. Das ist eine notwendige Bedingung, bevor weiter am Bezugszustand gearbeitet wird
(Suchrichtung). Erkundung, nicht blind: Das Ergebnis folgt aus der Zerlegung in `op3_sedenion_charge_2026_11_13.md`,
Punkt 1. Es gibt keinen Datenvergleich, keine H-Nummer und keine Änderung an Guards. Einordnung T5/T8, OP3. Skript
`op3_sedenion_generations_estar_2026_11_14.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- `op3_sedenion_charge_2026_11_13.md`: Q_* = P_0(1/2 − (i/2) L_e8)P_0 + 2/3 P_3 + 1/3 P_3̄ mit dem Spektrum 0 (2),
  1/3 (6), 2/3 (6), 1 (2); N = ker Q_* = span(1 + i e_8, e_7 − i e_15).
- Nachtrag zu H103 (`predictions/Ergebnis_H103_...`): Auf N wirkt die Rechtsmultiplikation mit H_n als Pauli-Tripel.
- K28 / `Trennung_Farbe_Generation.md`: S = (1,1) ⊕ (1,sgn) ⊕ (7,2) unter G_2 × S_3. Weg A hat nur zwei farbige
  Generationen.
- k85: Q8 = Q_S|_O gibt auf C⊗O genau eine Generation (ν, 3 d̄, 3 u, e⁺).

## Ergebnis

**1. Gemeinsame Zerlegung.** C⊗S zerfällt unter (Q_*, Farbtyp, ψ-Eigenwert) in acht Stücke:

| Teilchen | ψ = 1 | ψ = ω | ψ = ω̄ |
|---|---|---|---|
| ν (Q = 0, Singulett) | 1 | 1 | – |
| e⁺ (Q = 1, Singulett) | 1 | – | 1 |
| u (Q = 2/3, 3) | – | 3 | 3 |
| d̄ (Q = 1/3, 3̄) | – | 3 | 3 |

Insgesamt sind das 16 Zustände, genau **zwei vollständige Generationen**. Der Ladungsinhalt stimmt.

**2. Die ψ-Sektoren sind keine Generationen.**
- Der Sektor ψ = 1 enthält nur Leptonen (ν, e⁺), Ladungssumme 1.
- Der Sektor ω enthält ν, u und d̄, Ladungssumme 3.
- Der Sektor ω̄ enthält e⁺, u und d̄, Ladungssumme 4.

Eine Generation hat die Ladungssumme 4. Die komplexe Konjugation paart (Q, ω) mit (1 − Q, ω̄), wie es für Teilchen
und Antiteilchen sein muss.

**3. ψ ist unter Q_* kein Generationsschritt.** ψ vertauscht mit Q_* und mit su(3)_c, lässt also jedes Stück der
Tabelle in sich. Zwei vollständige Generationen G_1 ⊕ G_2 lassen sich als Summen solcher Stücke bilden, sogar auf
mehrere Weisen (je ein ν, ein e⁺, ein u-Triplett und ein d̄-Triplett). Jede solche Zerlegung ist ψ-invariant. ψ wirkt
dann **innerhalb** jeder Generation als Phase, nicht als Vertauschung der Generationen. Eine Ordnung-3-Vertauschung
von zwei Generationen gibt es ohnehin nicht. Das ist die Einschränkung aus K28 in neuer Form.

**4. Das neutrale Qubit ist der Flavourraum der zwei Neutrinos.** Jede Generation enthält genau ein ν. Die beiden
neutralen Zustände 1 + i e_8 (ψ = 1) und e_7 − i e_15 (ψ = ω) liegen deshalb in verschiedenen Generationen. N ist also
der Raum der zwei Neutrino-Flavours, und ψ = diag(1, ω) ist eine relative Phase zwischen ihnen. Der Bezug unter dem
magischen Winkel wäre eine Mischung dieser zwei Neutrinos. Das passt zur Erwartung „sichtbar nur im Neutrino-Block“,
gibt aber nur zwei Flavours statt drei.

## Bewertung
- **Bestanden:** Q_* gibt auf C⊗S den Ladungsinhalt zweier vollständiger Generationen.
- **Nicht bestanden:** Die Lesart von ψ als Generationsschritt. Unter Q_* ist ψ eine flavourdiagonale Phase. Das
  Oktanten-Tripel im neutralen Qubit entsteht aus der Bahn eines gemischten Neutrinozustands unter dieser Phase,
  nicht aus drei Generationen.
- Dass es nur zwei Generationen sind, stammt aus Weg A (K28) und ist unverändert. Der dritte Neutrino-Flavour fehlt in
  den Sedenionen.
- **Offen:**
  - ob der Qubit-Oktant (drei Zustände in C²) sinnvoll als Zwei-Flavour-Phänomen zu lesen ist;
  - wie die dritte Generation hinzukommt (Weg B, Triality auf O ⊕ O ⊕ O).
- OP3/OP4 bleiben offen. OP1–OP5, C5 und C6/T2 sind unverändert. H100 und H102 bleiben unberührt.
- Zurückgestellte Ideen: Keiner der Auslöser I1–I5 trifft zu.
