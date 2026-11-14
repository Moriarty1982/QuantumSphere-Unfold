# Erkundung: Der Majorana-Vektor auf dem neutralen Qubit N

14. November 2026. Autor: „Erst weiterrechnen“. Gewählt wurde der zweite Folgeschritt aus
`op3_family_su2_right_action_2026_11_14.md`, in der Form, die im Sedenionen-Rahmen rechenbar ist: welche symmetrischen
Bilinearformen auf N nativ sind und welche Richtung sie tragen. Der Paarkanal ν^c ν^c aus r82.4 lebt in C⊗H⊗O und ist
hier **nicht** gerechnet; eine Abbildung zwischen beiden Rahmen fehlt. Erkundung, nicht blind (Punkt 3 ist
Darstellungstheorie von Spin 1), kein Datenvergleich, keine H-Nummer, keine Änderung an Guards. Einordnung T8, OP3.
Skript `op3_majorana_vector_n_2026_11_14.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- `op3_family_su2_right_action_2026_11_14.md`, Punkt 6: Das symmetrische Bilinear von N ist der Vektor in Im H_n.
- `op3_eta_form_search_2026_11_13.md`: Majorana gegen Dirac als Unterschied der Sektoren (Hyperladungs-Regel,
  nachträglich); für einen symmetrischen Block ist ein Fluss nicht wie bei einer hermiteschen Matrix definiert.
- r55 (über `op3_selection_principle_2026_11_13.md`): Majorana-Auslesung ℤ₂, Dirac-Auslesung ℤ₃ in A_4.
- `op3_neutral_su2_octant_2026_11_13.md`, Feldsuche Punkt 2: ν^c-Paarung mit Spins entlang x, y, z gibt (0; 1,22; 1,22).
- Nicht gefunden: eine Einteilung der symmetrischen Formen auf N nach den nativen Symmetrien.

## Ergebnis
Eine symmetrische Form wird als M = (m·σ)ε mit m ∈ C³ geschrieben; die Achsen sind e_7, e_15, e_8. Ihre zwei
Singulärwerte sind die zwei Massen.

**1. Die native Bilinearform verschwindet auf N.** Das reelle Skalarprodukt von S, komplex-bilinear fortgesetzt, ist
auf N null: N ist isotrop. Ein Majorana-Term braucht also einen Operator dazwischen.

**2. Kurze native Wörter geben nur entartete Massen.** Von 42 Formen xᵀWy mit W aus L_a, R_a (a = e_7, e_8, e_15,
Länge 1 und 2) haben 12 einen symmetrischen Teil. Alle tragen eine reelle Richtung: vier entlang e_8, acht senkrecht
dazu. Keine liegt auf einer Raumdiagonale, keine ist ein Nullvektor. Die Massen sind jedes Mal (1, 1).

**3. Reelle Richtung heißt zwei gleiche Massen, Nullvektor heißt eine Masse.** Unter M → UᵀMU:

| Element | feste Form | Massen | Richtung |
|---|---|---|---|
| ψ (Ordnung 3, Achse e_8) | nur M₁₁ | (1, 0) | Nullvektor senkrecht zu e_8 |
| R_e8 (zweizählig) | Achse e_8 | (1, 1) | reell |
| R_e7 (zweizählig) | Achse e_7 | (1, 1) | reell |
| R_h (dreizählig) | Raumdiagonale | (1, 1) | reell, cos zu e_8 = 1/√3 |

Die Form entlang e_8 ist unter ψ nicht fest, sondern bekommt den Faktor ω, weil ψ auf N die Determinante ω hat. Die
beiden anderen Eigenformen von R_h (Eigenwerte ω, ω̄) sind Nullvektoren mit einer Masse.

**4. ψ-Invarianz gibt genau ein massives Neutrino.** Die einzige ψ-feste Form ist M₁₁: Nur der ψ-invariante Zustand
1 + i e_8 bekommt eine Masse, e_7 − i e_15 bleibt masselos. Invarianz unter einer Hurwitz-Einheit gibt dagegen zwei
gleiche Massen.

**5. Koide liegt dazwischen und wird nicht festgelegt.** Mit einer dritten Masse null ist K = 1 für eine Masse und
K = 1/2 für zwei gleiche. Die Mischung cos t · M_ψ + sin t · M_h durchläuft alle Werte dazwischen; 2/3 wird bei einem
freien Mischwinkel erreicht. Das ist eine Anpassung, keine Vorhersage.

## Bewertung
- Der Majorana-Vektor ist im Sedenionen-Rahmen durch die Symmetrien nicht festgelegt. Jede einzelne native Symmetrie
  wählt ein entartetes oder ein einmassiges Spektrum; beide sind als Neutrinospektrum falsch (zwei Massendifferenzen
  sind gemessen).
- Der Befund aus r55 hat hier ein Gegenstück: Eine ℤ₂-feste Majorana-Form ist eine Achse (e_7, e_15 oder e_8) mit
  entarteten Massen. Das ist eine Parallele, kein Abgleich mit r55.
- Drei Massen aus zwei Flavours gibt es nicht. Der Rang-2-Oktant aus der Vornotiz ist eine Gram-Matrix dreier
  Zustände, kein Massenterm dieses Dubletts.
- Die Linie „neutrales Qubit der Sedenionen“ liefert damit Träger, Zyklus, Bezug und Familien-su(2), aber weder die
  dritte Generation noch ein Spektrum. Alles erbt die Guards von CT-003.
- Koide 2/3 und die Phase sind **nicht** hergeleitet. OP3/OP4 bleiben offen. OP1–OP5, C5 und C6/T2 sind unverändert.
  H100 und H102 bleiben unberührt.
- Suchrichtung: Das war die dritte Variante mit derselben offenen Voraussetzung (dritte Generation). Weitere
  Rechnungen auf N sind erst sinnvoll, wenn diese Voraussetzung geklärt ist.
- Zurückgestellte Ideen: Keiner der Auslöser I1–I5 trifft zu.

## Mögliche nächste Schritte (Autorentscheidung)
- Die dritte Generation direkt angehen: Welche native Struktur enthält C⊗S (Dublett) und eine weitere Generation
  (Singulett) zugleich? Ohne Kandidaten ist das eine Rückwärtssuche über die Bedingungen, keine Simulation.
- Die Linie ablegen, bis H100 oder H102 entschieden sind.
