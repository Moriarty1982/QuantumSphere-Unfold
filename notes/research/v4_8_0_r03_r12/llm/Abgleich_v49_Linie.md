# Abgleich: lokale Linie v4.8.0-r03–r12 und GitHub-Linie v4.9.0-Kandidat

Stand 2026-10-20. GitHub `main` bei 651b624 (19.10.2026), Teile in `sources/research/parts/`, Änderungsübersicht
`analysis/V490_Research_Candidate.md`. Beide Linien gehen vom veröffentlichten v4.8.0 aus und haben sich
unabhängig entwickelt. Die v4.9-Linie wurde hier nur gelesen, nicht verändert.

## Inhalt der v4.9-Linie (kurz)

Schwerpunkt ist eine neutrale Cartan-Wirkung mit endlichen Kompatibilitäts- und Quellgesetzen (Rang-40-Inverse,
Normalquellen, Restkontrollen), dazu HC-Dynamik, Massenidentifikation, Generationenkopplung, Koide und Kern,
Kopplungsskalen. Ausdrücklich nicht behauptet: native Einstein-Emergenz, physikalische Kopplung oder Skala,
Frame-Zuordnung, OP5-Abschluss.

## Übereinstimmungen

| Thema | v4.9 | lokale Linie | Bewertung |
|---|---|---|---|
| Koide | K = 2/3 ⇔ gleiche Normen von Symmetrie- und Nullsummenanteil; zyklische Symmetrie legt das Verhältnis nicht fest (`v480:koide-equal-norm`, `v480:koide-equivariant-obstruction`) | r10: K = 2/3 ⇔ \|c\| = t; Lesart B ist Kinematik, Dynamik fehlt | gleich (Normierung r_v4.9 = √2 · r_lokal) |
| Phasenkammern | positive Wurzelmatrix genau für \|θ − 2πj/3\| ≤ π/12; nahe der Grenze ein parametrisch leichtes Teilchen (`v480:generation-phase-chambers`) | K14.4: Grenzphase π/12, 25 % des Kreises positiv; alle geladenen Gruppen knapp innerhalb | **unabhängig gleich gefunden** |
| Phasen-Ansatz θ = π − √2 arcsin β | numerisch und strukturell verworfen | r09/r11: Phasenformeln widerlegt | gleich |
| Θ-Summe | als offene Verpflichtung geführt (`premise-audit`) | r05: Θ-Summen-Vermutung widerlegt (−0,1097 statt 0,893) | lokal schärfer; v4.9 könnte r05 übernehmen |
| Riemann / GUE | Riemann-Takt nicht als Satz behauptet, R_GUE nicht identifiziert | r04: Riemann-Arbeit keine Beweisquelle; r05: GUE empirisch | gleich |
| β_sym | γ_string exakt, γ_BI = 0,2375 → β = 0,5493482…; Neukalibrierung von γ_BI abgelehnt | H9 nutzt dieselben Werte (β = 0,549348) | gleich |

## Spannungen

1. **Vorzeichen der Wurzeln (H2, H3).** v4.9 verlangt nicht-negative Wurzeln für das physikalische K: „Taking
   absolute values of signed roots does not preserve the displayed ratio“. H2 setzt dagegen ein negatives v_k an
   (Koide mit Vorzeichen). Mathematisch kein Widerspruch: H2 hat selbst offengelegt, dass mit nicht-negativen
   Wurzeln K ≤ 0,585 bleibt; für die H2-Massen ist das nicht-negative K = 0,525. Begrifflich aber ein Unterschied:
   **H2 testet „Koide mit Vorzeichen“**, das außerhalb des positiven Bereichs der v4.9-Linie liegt. Das muss in
   H2/H3 so benannt werden.
2. **Farbe und Generation.** Beide Linien übernehmen das Dixon-Wörterbuch Gen_i ≅ (ℂ⊗ℍ)⊗e_{i+3}. v4.9 merkt an,
   dass die Faktorisierung im nativen Träger nicht bewiesen ist, behandelt aber die Farbe nicht. Der Befund K25.2
   (dasselbe Triplett trägt Farbe und Generation) betrifft beide Linien.
3. **Flavour-Gruppe.** Die lokale Δ(96)-Analyse (r12) hat in v4.9 kein Gegenstück. Sie wäre dort nur unter der
   Annahme „Triplett = Generationen“ einzuordnen (K25.2).

## Empfehlungen

- Für die v4.9-Linie: r04 (Entkopplung von der Riemann-Arbeit) und r05 (Θ-Summen-Vermutung widerlegt) übernehmen
  oder zitieren; K25.2 als offene Modellverpflichtung aufnehmen.
- Für die lokale Linie: H2 und H3 ausdrücklich als „Koide mit Vorzeichen, außerhalb des positiven Bereichs“
  kennzeichnen; die Phasenkammern von v4.9 als unabhängige Bestätigung von K14.4 zitieren.
- Zusammenführung: über den offenen Entwurf-PR #19. Ein Merge berührt keine Datei der v4.9-Linie.
