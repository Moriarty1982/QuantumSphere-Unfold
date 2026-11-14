# Erkundung: Die Rechtswirkung von H_n ist eine Familiensymmetrie auf ganz C⊗S

14. November 2026. Autor: „(c) zweite Familie“ (Punkt (c) der Übergabe: die zweite Familienstruktur mit neutralem
Qubit). Erkundung ohne Vorab-Notiz, kein Datenvergleich, keine H-Nummer, kein MMA-Beleg, keine Änderung an Guards.
Einordnung T5/T7/T8, OP3. Skript `op3_family_su2_right_action_2026_11_14.py`, Ausgabe `..._out.txt`.

**Blindheit:** Vor der Rechnung war offen, ob die Rechtsmultiplikation auf dem farbigen Teil eine Darstellung bleibt
(S ist nicht assoziativ); das Ergebnis dort (Punkt 2) war nicht vorhergesagt. Die Punkte 4 bis 6 folgen aus bekannter
Gruppentheorie und sind nicht blind.

## Vorwissen geprüft
- `op3_neutral_su2_octant_2026_11_13.md`: Eine neutrale SU(2) wirkt nach Schur nur auf den Generationsindex. In der
  Platz-U(3) gibt es zwei Einbettungen (SO(3) mit Generationen als Vektor und ohne Spinor; SU(2) als 2 + 1 mit
  Spinor). Im Dixon-Raum fehlt der Platz. Gefordert war am Ende ein neutrales Qubit mit einem Element der Ordnung 3.
- `op3_sedenion_charge_2026_11_13.md`: Q_*, N = ker Q_*, Kommutant der Dimension 10.
- `predictions/Ergebnis_H103_...`, Nachtrag: N ist ein Rechtsmodul über H_n, Pauli-Tripel i R_e7, i R_e15, i R_e8.
- `op3_hurwitz_2t_neutral_qubit_2026_11_14.md`: 2T von rechts auf N; ψ und 2T sind verschiedene Dreierstrukturen.
- `op3_sedenion_generations_estar_2026_11_14.md`: zwei vollständige Generationen, ψ ist kein Generationsschritt.
- `op3_generation_carrier_review_2026_11_13.md`: Es fehlt ein nativer Mehrfachraum gleicher Quantenzahlen.
- K28: S = (1,1) ⊕ (1,sgn) ⊕ (7,2) unter G_2 × S_3.
- Nicht gefunden: eine Prüfung der Rechtswirkung von H_n außerhalb von N.

## Suchrichtung (rückwärts)
Ziel ist eine Familienstruktur mit neutralem Qubit. Notwendig sind:
1. eine Wirkung, die mit Farbe und Ladung vertauscht (Schur: sie wirkt dann nur auf den Mehrfachraum);
2. ein Dublett darunter im neutralen Sektor;
3. ein Element der Ordnung 3 mit einem Bezug unter dem magischen Winkel.

Auf N erfüllt die Rechtswirkung von H_n alle drei. Als Familienstruktur taugt sie nur, wenn sie auf allen Teilchenarten
wirkt. Geprüft wird also genau das, statt weitere Träger zu simulieren.

## Ergebnis

**1. R_u vertauscht auf ganz C⊗S mit Farbe und Ladung.** Für u ∈ {e_7, e_8, e_15} ist der Kommutator mit su(3)_c
und mit Q_* null (≤ 3·10⁻¹⁴). Der Grund für die Farbe: su(3)_c besteht aus Derivationen, die e_7, e_8 und e_15
festhalten. Die Linksmultiplikationen L_e7 und L_e15 vertauschen dagegen nicht mit Q_*. R_u mischt den neutralen und
den farbigen Teil nicht.

**2. Auf jedem der beiden Teile gelten die Quaternionen-Relationen, aber mit entgegengesetzter Orientierung.**
R² = −1 und die Antikommutatoren sind exakt null, auf beiden Teilen. Auf dem neutralen Teil gilt R_x R_y = R_(yx)
(Rechtsmodul, wie bekannt). Auf dem farbigen Teil gilt R_x R_y = R_(xy). Folgen:
- Die R_g der 24 Hurwitz-Einheiten sind auf ganz S als Menge **nicht** abgeschlossen.
- Die von R_e7, R_e8, R_e15 erzeugte Lie-Algebra hat die Dimension 6: su(2) auf den Leptonen ⊕ su(2) auf den Quarks.
- Mit der Quaternionen-Konjugation auf dem farbigen Teil, T_g = R_g (neutral) + R_ḡ (farbig), entsteht eine treue
  Darstellung von 2T auf ganz S (Ordnungen 1:1, 2:1, 3:8, 4:6, 6:8), die mit su(3)_c und Q_* vertauscht.

**3. Jede Teilchenart ist ein Dublett.** Auf ν, e⁺, u und d̄ hat der Casimir-Operator den Wert 3/4, also Spin 1/2;
i R_e8 und i R_e7 haben die Eigenwerte ±1. Die zwei Generationen von C⊗S sind damit ein Dublett einer nativen,
farb- und ladungsneutralen Familien-su(2), getrennt für Leptonen und Quarks.

**4. ψ ist eine Drehung dieser Familien-su(2).** Es gilt ψ R_u ψ⁻¹ = R_(ψu), und ψ dreht Im H_n um die Achse e_8 um
120° (e_8 fest). ψ normalisiert also die Familien-su(2), aber nicht 2T (wie schon auf N).

**5. Oktant mit den ursprünglichen Rollen.** Nimmt man als Zyklus eine Hurwitz-Einheit h der Ordnung 3 oder 6 und als
Bezug einen ψ-Eigenzustand von N (1 + i e_8 oder e_7 − i e_15), gibt die Bahn ρ² = 1/2, K = 2/3, Phase π/4, Rang 2.
Die Konjugation mit h vertauscht die Achsen zyklisch: e_7 → e_15 → e_8 → e_7. Das ist das Oktantenbild in seiner
ersten Form (`op3_neutral_su2_octant`, Nachtrag Punkt 1). Der Bezug ist dann ein Ladungs- und ψ-Eigenzustand und
braucht keine Auswahl; ausgewählt werden muss stattdessen h.

**6. Majorana-Bilinear.** N ⊗ N zerfällt unter der Familien-su(2) in den symmetrischen Teil mit Spin 1 (Vektor) und
den antisymmetrischen mit Spin 0. Ein Majorana-Massenterm ist in den Familienindizes symmetrisch und enthält deshalb
kein Singulett: Er trägt immer eine Richtung in (komplexifiziertem) Im H_n. Ein Dirac-Term (2̄ ⊗ 2 = 1 ⊕ 3) darf
familienblind sein.

## Bewertung
- **Einschränkung zuerst:** Dass es auf zwei Generationen je Teilchenart eine U(2) gibt, die mit Farbe und Ladung
  vertauscht, folgt schon aus Schur. Neu ist nur die Realisierung: Eine einzige native Operation, die
  Rechtsmultiplikation mit H_n, liefert diese su(2) auf allen vier Teilchenarten, mit ψ als Drehung um die
  Ladungsachse und den Hurwitz-Einheiten als 2T.
- **Antwort auf (c):** Die Sedenionen mit der Ladungsachse e_8 enthalten eine zweite Familienstruktur. Sie ist vom
  Typ „SU(2) als 2 (+ 1)“ aus der Einbettungstabelle: Die Generationen sind ein Dublett, keine drei Achsen. Der Vektor
  mit drei Achsen tritt nur als Im H_n auf, also in den Erzeugern und im symmetrischen Bilinear.
- **Nicht erfüllt aus dem Profil:**
  - „nur im Majorana-Block“: Das Dublett tragen alle Teilchenarten, auch e⁺. Punkt 6 gibt nur einen schwächeren
    Unterschied (Majorana ohne Singulett, Dirac mit).
  - drei Generationen: Es bleiben zwei (K28). Ein Singulett als dritte Generation ist nicht gefunden.
  - drei Massen: Ein symmetrisches 2×2-Bilinear hat zwei Singulärwerte. Der Rang-2-Oktant gibt keine drei Massen.
- **Offen:**
  - ob die entgegengesetzte Orientierung auf Leptonen und Quarks eine Bedeutung hat oder nur die Konjugation ḡ ist;
  - was eine Hurwitz-Einheit als Zyklus auszeichnet (Punkt 5) und ob ψ oder h der physikalische Schritt ist;
  - die Ladungsachse e_8 selbst (CT-003, placeholder, drei Guards). Alles hier erbt diese Guards.
- Das Ziel war bekannt; Koide 2/3 und die Phase sind **nicht** hergeleitet. OP3/OP4 bleiben offen. OP1–OP5, C5 und
  C6/T2 sind unverändert. H100 und H102 bleiben unberührt.
- Zurückgestellte Ideen: Keiner der Auslöser I1–I5 trifft zu.

## Mögliche nächste Schritte (Autorentscheidung)
- Die dritte Generation als Singulett suchen: Gibt es neben C⊗S einen nativen Träger einer Generation, auf dem die
  Familien-su(2) trivial wirkt (etwa C⊗O mit Q8, k85)? Das wäre 2 + 1.
- Den Majorana-Vektor ausrechnen: Welche Richtung in Im H_n trägt der einzige eichinvariante Paarkanal ν^c ν^c
  (r82.4) im Familien-Dublett?
- Die Linie ablegen, bis H100 oder H102 entschieden sind.
