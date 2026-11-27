# Vorab-Notiz H198 (1a): Ist der Up-Typ-Projektor P_up eine bekannte Projektgröße — die Chiralität der Ladungs-U(1)?

**Datum:** 27.11.2026. **Nummern:** H198 (Test), k408 (Rechnung). **Strang:** Quarkmassen; offene Stelle aus H197.
**Anlass:** „probiere beides" des Autors (27.11., 10:55), Richtung 1a: P_up an eine bekannte Projektgröße knüpfen.

## Worum es geht
H197 hat gezeigt: „Down linear" (D = B) verlangt, dass das l_k²-Glied mit dem Up-Typ-Projektor **P_up = 3(Q₀−⅓)** koppelt,
und keine Symmetrie des F4/Ladungs-Rahmens erzeugt P_up. Frage hier: Ist P_up dennoch ein **bekanntes** Objekt des Projekts —
nämlich die chirale (holomorphe) Projektion der Ladungs-U(1)?

## Vermutung, die ich prüfe (teils nicht blind, Algebra)
Aus H182 (k389) ist auf dem Farbblock Q₀ = ½ + (i/6)·L_U, mit L_U = Linksmultiplikation mit der Ladungseinheit U = e₇.
Dann ist Q₀−½ = (i/6)·L_U (die ladungsungerade J-Form, rein imaginär, der **Generator** der Ladungs-U(1)), und

  **P_up = 3(Q₀−⅓) = 3(⅙ + (i/6)L_U) = ½(1 + i·L_U).**

Das ist exakt der **Projektor auf den +i-Eigenraum von L_U**, also auf eine **Chiralität** der Ladungs-U(1). H182 hat diese
U(1) bewusst **nicht gefordert** (H178). P_up wäre damit keine Ad-hoc-Größe, sondern die chirale Projektion einer Symmetrie,
die der Rahmen kennt, aber bisher nicht aufgeprägt hat.

## Teile und Kriterien
- **H198a (nicht blind, Algebra).** Operatoridentität P_up = ½(1 + i·L_U) auf dem Farbblock exakt nachweisen (k389-Konstruktion;
  Wolfram-Gegenprobe). Zeigen: P_up projiziert auf den Up-Typ (Ladung ⅔), P_down = ½(1 − i·L_U) auf Down; P_up² = P_up,
  P_up + P_down = 1, P_up P_down = 0. (Erwartung: trifft, reine Algebra.)
- **H198b (Test — Chiralität erzeugt b_down = 0).** Ein unter der Ladungs-U(1) **holomorpher** (chiraler) Potentialterm benutzt
  nur die +Chiralität, koppelt also nur an den Up-Typ. Konkret: die zweite Variation (Krümmung) eines chiralen Grad-5-Terms auf
  der Up-Mode gegen die Down-Mode. **Kriterium:**
  - **„ja, hergeleitet unter einer benannten Annahme":** P_up = ½(1+iL_U) exakt **und** ein chiraler Grad-5-Invariant erzeugt das
    l_k²-Glied nur für Up (b_down = 0 exakt, b_up ≠ 0), d. h. D = B folgt aus „das Quintik-Glied ist holomorph unter der
    Ladungs-U(1)". Dann ist die freie Zahl D/B auf **eine Symmetrieannahme** (Chiralität) reduziert, und P_up ist mit einem
    bekannten Objekt identifiziert.
  - **„teilweise":** P_up = ½(1+iL_U) exakt, aber der chirale Grad-5-Term legt die übrigen Koeffizienten (A, B, C) nicht fest —
    dann ist P_up benannt und D = B auf Chiralität zurückgeführt, aber keine volle Herleitung der Massen.
  - **„nein":** P_up ist nicht die holomorphe Projektion, oder Chiralität gibt b_down ≠ 0.
- **H198c (Bericht).** Ist die Ladungs-U(1) + Holomorphie des Quintik-Terms verträglich mit dem Rest (F4-invarianter Kinetik,
  dem J-Tausch der Leptonen)? Was bricht die Holomorphie auf, dass die **geraden** Terme (A, B über beide Sektoren) bleiben?

## Erwartung (offen gelegt, teils nicht blind)
Ich erwarte **teilweise**: Die Operatoridentität P_up = ½(1+iL_U) trifft (reine Algebra), damit ist P_up als chirale Projektion
der Ladungs-U(1) benannt — ein echtes Strukturergebnis, das „Down linear" als „der Massen-Quintik ist holomorph unter der
Ladung" liest. Eine **volle** Herleitung (alle Koeffizienten) erwarte ich nicht: Holomorphie ist eine zusätzliche Annahme, die
der F4-Rahmen nicht erzwingt (H178: U(1) nicht gefordert). Ein echter Gegenbefund wäre, wenn Holomorphie b_down ≠ 0 gäbe.

## Werkzeuge
Python (numpy für die Operatoridentität und die chirale Krümmung; sympy für die exakten l_k-Reduktionen); Wolfram Language
exakt für P_up = ½(1+iL_U) und die Projektor-Eigenschaften. Qiskit nicht nötig.

## Vorwissen geprüft
- `.../ladung_h182/` (H182, k389): Q₀ = ½ + (i/6)L_U auf dem Farbblock; J-Form = Q₀−½; U = e₇.
- `.../farbe_h178/` (H178): die Ladungs-U(1) ist nicht gefordert (Winkel frei für Farbanteil).
- `.../symmetrie_db_h197/` (H197): D=B ⇔ P_up = 3(Q₀−⅓); P_up nicht J-kovariant; nötig neue Eingabe.
- `.../feldgleichung_form_h195/` (H195): l_k² ab Grad 5; Nenner (l_i+l_j)².
- Bilanz_Feldgleichung_2026_11_27.md: Gesamtstand.

## Grenzen (vorab)
Dieselbe Zerlegung (ruhendes Vakuum, Krümmung/Norm, Farbblock). Holomorphie/Chiralität unter der Ladungs-U(1) ist eine
**zusätzliche Annahme**, kein Satz des F4-Rahmens; der Befund sagt nur, ob P_up mit ihr identisch ist, nicht ob sie gelten muss.
OP3/OP4 bleiben offen; kein Guard berührt.
