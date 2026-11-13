# Erkundung: Ladung auf die Sedenionen anders als über e_7 fortsetzen

13. November 2026, abends. Autorenauftrag: „Sedenionen-Ladung“ (Wahl aus der Übergabe: Fortsetzung der Ladung auf
die Sedenionen anders als über e_7). Erkundung, nicht blind: Das Ergebnis stand nach der Rückwärtssuche analytisch fest
und wurde danach numerisch bestätigt. Es gibt weder einen Datenvergleich noch eine H-Nummer oder einen MMA-Beleg, und
offene Guards ändern sich nicht. Einordnung T5/T8, OP3. Skript `op3_sedenion_charge_2026_11_13.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- `op3_sedenion_reference_2026_11_13.md`:
  - Die farbneutrale Quaternionenalgebra H_n = span(1, e_7, e_8, e_15) ist bekannt.
  - ψ dreht dort um 120° um e_8. Die Diagonale (e_7 + e_8 + e_15)/√3 liefert das Oktanten-Tripel.
  - Nachtrag: **Keine Fortsetzung mit Q|_O = Q8 vertauscht mit ψ.** Die über e_7 fortgesetzte Ladung Q_S macht den
    Träger geladen.
- k85 (`Q8 = 1/2 − (i/6) L_e7 − (i/3) R_e7`).
- K28 / `Trennung_Farbe_Generation.md`:
  - Aut(S) = G_2 × S_3.
  - S = (1,1) ⊕ (1,sgn) ⊕ (7,2).
  - Weg A hat nur zwei farbige Generationen.
- `op3_neutral_su2_octant_2026_11_13.md`: Reelle Zustände geben nur K = 1/2. Für das Oktanten-Tripel fehlte ein Bezug
  unter dem magischen Winkel.
- Übergabe, Profil der fehlenden Struktur: Gesucht ist ein farb- und ladungsneutrales Qubit, auf dem der Zyklus mit
  Ordnung 3 wirkt, dazu ein Bezug unter arccos(1/√3).

## Suchrichtung (rückwärts)
Statt eine weitere Fortsetzung zu raten, wurden die notwendigen Bedingungen an Q festgelegt. Danach wurde die
Lösungsmenge bestimmt.
- **N1** [Q, ψ] = 0, damit der Generationsschritt die Ladung nicht ändert.
- **N2** [Q, su(3)_c] = 0. Farbe ist dabei der Stabilisator von e_7 in g_2, diagonal auf S.
- **N3** Q ist hermitesch und erfüllt Q̄ = 1 − Q (Teilchen gegen Antiteilchen wie bei Q8). Das Spektrum liegt in
  {0, 1/3, 2/3, 1}, und das Farbtriplett 3 hat 2/3, 3̄ hat 1/3.

Die Bedingung Q|_O = Q8 aus dem Nachtrag wird ausdrücklich **aufgegeben**.

## Ergebnis

**1. Kommutant.** Der Kommutant von ψ und su(3)_c hat die komplexe Dimension 10. Der farbneutrale Block
span(1, e_7, e_8, e_15) trägt dazu gl(2) ⊕ 1 ⊕ 1 bei, mit den ψ-Eigenwerten 1, 1, ω, ω̄. Der farbige Teil trägt vier
Sektoren bei (3 oder 3̄, ω oder ω̄).

**2. Der farbige Teil ist eindeutig.** N3 legt dort 2/3 auf 3 und 1/3 auf 3̄ fest, unabhängig vom ψ-Sektor. Das ist
die Isotypie-Zerlegung, und sie stimmt mit Q8 auf den farbigen Richtungen von O überein.

**3. Der farbneutrale Teil ist bis auf zwei Vorzeichen eindeutig, und zwar über e_8.**
- Aus N3 folgt Q = 1/2 + iA mit A reell antisymmetrisch.
- Aus N1 folgt A = b·K + a·J. Dabei dreht K die Ebene (1, e_8) und J die Ebene (e_7, e_15).
- Leptonladungen {0, 1} erzwingen |a| = |b| = 1/2.
- Auf dem Block ist L_e8 = K − J und R_e8 = K + J. Damit gilt:
  **Q_\* = P_0 (1/2 − (i/2) L_e8) P_0 + 2/3 P_3 + 1/3 P_3̄** (oder mit R_e8).
- Q_\* erfüllt N1–N3 numerisch, und das Spektrum ist 0 (2), 1/3 (6), 2/3 (6), 1 (2).
- Die Ladungsachse der farbneutralen Leptonen ist damit **e_8, die einzige ψ-feste imaginäre Richtung.** L_e8 vertauscht
  mit ganz G_2 und mit ψ.
- Nebenbefund: Das ψ-Mittel der e_7-Ladung ist die Konstante 1/2, weil L linear ist und e_7 + ψe_7 + ψ²e_7 = 0 gilt.

**4. Es entsteht ein farb- und ladungsneutrales Qubit.** Es ist N = ker Q_\* = span(v_1, v_ω) mit
- v_1 = 1 + i e_8, ψ-fest,
- v_ω = e_7 − i e_15, mit dem ψ-Eigenwert ω.

ψ wirkt auf N als diag(1, ω), projektiv also als Drehung der Ordnung 3. Das ist der erste native Träger, der die
ersten beiden Punkte des Profils erfüllt: farbneutral und ladungsneutral, mit dem Zyklus als Element der Ordnung 3.

**5. Der Bezugszustand ist nicht nativ.** Das Oktanten-Tripel verlangt in N einen Bezug mit cos θ = ±1/√3 zur ψ-Achse.
- Für ein reelles x = a + b e_7 + c e_8 + d e_15 ist der Bloch-Winkel der Projektion auf N
  cos θ = (a² + c² − b² − d²)/(a² + b² + c² + d²). Bei rationalen Koeffizienten ist das rational, 1/√3 wird also nicht
  erreicht.
- Die frühere Diagonale (e_7 + e_8 + e_15)/√3 gibt cos θ = −1/3, ρ² = 1/3, K = 5/9 und die Phase π/2.
- Die Hurwitz-Einheiten (±1 ± e_7 ± e_8 ± e_15)/2 geben cos θ = 0, also K = 1/2.
- Erst ein von Hand gesetzter Bezug gibt das Oktanten-Tripel (ρ² = 1/2, K = 2/3, Phase π/4). Er braucht das
  Amplitudenverhältnis tan(θ/2) = 2 sin(π/12).

**6. Preis der Konstruktion.**
- Q_\* lässt O nicht invariant und stimmt auf span(1, e_7) nicht mit Q8 überein. Das ist mit dem Nachtrag verträglich,
  der genau diese Unmöglichkeit zeigt.
- ε (a + b e_8 ↦ a − b e_8) vertauscht mit dem farbigen Teil. Auf dem farbneutralen Block gilt aber ε Q_\* ε = 1 − Q_\*,
  ε wirkt dort also wie eine Ladungskonjugation. Die Ladung bricht S_3 zu ℤ_3.
- Weg A behält die Einschränkung aus K28 (nur zwei farbige Generationen).

## Bewertung
- **Positiv:** Mit der Ladungsachse e_8 statt e_7 haben die Sedenionen ein farb- und ladungsneutrales Qubit, auf dem der
  Generationszyklus mit Ordnung 3 wirkt. Unter N1–N3 ist das im farbneutralen Block die einzige Möglichkeit, bis auf
  zwei Vorzeichen. Damit fällt das Hindernis aus `op3_sedenion_reference` (Ladung) weg, sofern man Q|_O = Q8 aufgibt.
- **Offen:** Der Bezug unter dem magischen Winkel bleibt nicht nativ. Die Lücke hat sich verschoben: Gefragt ist jetzt
  ein Bezugszustand in N, nicht mehr ein neutraler Träger. Er braucht ein irrationales Gewichtsverhältnis 2 sin(π/12).
- **Nicht gezeigt:**
  - warum nur die Neutrinos (Majorana-Block) diesen Träger sehen;
  - wie sich die Aufgabe von Q|_O = Q8 mit der Ladung des Companion auf O verträgt (die erste Generation ist dann
    nicht O);
  - wie ε als Ladungskonjugation zu C im Companion passt.
- Die Wahl von e_8 als Ladungsachse ist eine Annahme. Der Companion definiert auf S keine Ladung.
- OP3/OP4 bleiben offen. OP1–OP5, C5 und C6/T2 sind unverändert. H100 und H102 bleiben unberührt.
- Zurückgestellte Ideen: Keiner der Auslöser I1–I5 trifft zu.
