# Methoden-Notiz: Gleiche Gewichte beider Zeitorientierungen aus dem Gegenstrom des OP5-Keims? (Erkundung, vor der Rechnung festgelegt)

22. November 2026. Auftrag des Autors: „weiter“ nach Runde v4.10.0-r40. Keine H-Nummer.
**Nicht blind:** Die Tabelle in k168 gibt die Dichten der drei Blöcke auf zwei Stellen (5,97 + 0,43 gegen 6,38); das Gewicht p ≈ 0,501 ist
damit vor der Rechnung ungefähr bekannt. Neu sind die genauen Werte, die Prüfung des Zeitumkehrbilds und die Unterscheidung von der Spiegelung.

## Rückwärtssuche
Ziel aus r40.4: Der Austausch gewichtet beide relativen Zeitorientierungen seiner Enden gleich, p = ½ (dann w = 2p − 1 = 0 und N_m).
Notwendig sind zwei Anteile, die lokale Zeitumkehrbilder voneinander sind, mit gleichem Gewicht. Kandidaten im Bestand:
- (a) Gegenstrom am OP5-Keim (k168): Blöcke 0 und 1 laufen mit +x/t, Spin +e_y; Block 2 läuft mit −x/t, Spin −e_y.
- (b) Paar-Konnektor aus Materie und Tachyonbild (r34): Die Tachyon-Abbildung ist keine Zeitumkehr; r40.4 zeigt, dass sie nicht aufhebt.
  Ausgeschlossen.
- (c) String zwischen M und T unter G2 (T vor, M nach dem Urknall): vollständig umgekehrte Orientierung gäbe p = 0, den Lorentz-Fall
  2(x − a)²; trägt nur, wenn die Brücke beide Orientierungen gleich trägt. Hier nicht gerechnet.
Gerechnet wird (a).

## Vorwissen geprüft
- k168 (`../v4_10_0_r80/llm/Erkundung_Fierz_Hintergrund.md`, Skript `k168_fierz.py`): Fierz-Größen der drei Blöcke am Keim
  (t, x, y, z) = (1, 0,6, 0, 0); β ≈ 0; Gegenstrom; Spins entlang φ̂ = e_y.
- Counterflow-Serie (`analysis/OP5_Counterflow_*`, `OP5_Boosted_Triad_*`): Hintergrund als geboostete Triade.
- r40: w = 2p − 1 (r40.4); J_0i zeitungerade, J_00 und J_ij gerade (r40.3); H118: Zeitumkehr kehrt die Oktant-Orientierung um.
- Zurückgestellte Ideen: I1 (String M–T) betrifft Kandidat (c), nicht diese Rechnung.

## Werkzeug
Python mit mpmath (40 Stellen) auf dem 70-stelligen Keim `analysis/op5-field-slices/state-sufficiency-2026-10-30/precision-first-jet-70.json`
(Ordner als Argument), für Fierz-Größen und Gewichte. Wolfram Language exakt für den Austausch unter Spiegelung statt Zeitumkehr. Qiskit nicht
geeignet (kein Schaltkreis). Skripte `counterflow_weights.py`, `reflection_average.wl`; Ausgaben in `run/`.

## Fragen
1. **Zeitumkehrbild:** Ist Block 2 das lokale Zeitumkehrbild von Block 0 (und 1)? Vergleich der normierten Fierz-Größen
   (Φ, Θ, J^a, K^a) von Block 2 mit dem Bild von Block 0 unter Zeitumkehr (J^i, K^i, Θ wechseln das Vorzeichen); Abweichung angeben.
2. **Gewichte:** p = Gewicht(Blöcke 0 + 1)/Gewicht(alle) mit drei Gewichtsmaßen: φ², J⁰ = ψ†ψ, J^a-Norm. Daraus w = 2p − 1 und die relative
   Abweichung des Zählers von N_m, max über x, a ≥ 0 von |2w a x|/(3N_m).
3. **Zeitumkehr oder Spiegelung:** Für diese Vektoren (J entlang x, K entlang y) gibt die Spiegelung x ↦ −x dasselbe Fierz-Muster. Austausch
   mit Mittel über einen an x ↦ −x gespiegelten Vertex (Gewicht ½) gegen N_m, exakt (Wolfram), bei Wellenvektor in allgemeiner Richtung.

## Raster (vorab)
- **trägt:** Block 2 ist das Zeitumkehrbild auf 1e-6, |w| ≤ 0,01 mit jedem Gewichtsmaß, und die Spiegelung ist als Lesart ausgeschlossen,
  weil sie N_m nicht gibt, während die Zeitumkehr es gibt.
- **trägt teilweise:** Block 2 ist das Zeitumkehrbild und die Gewichte sind nahezu gleich, aber eine der beiden anderen Bedingungen fehlt,
  etwa |w| > 0,01, abhängiges Gewichtsmaß oder Zeitumkehr und Spiegelung nicht unterscheidbar.
- **trägt nicht:** Block 2 ist kein Zeitumkehrbild (Abweichung > 1e-3) oder die Gewichte sind deutlich verschieden (|w| > 0,1).

Die Zuordnung, dass die Enden des Vermittleraustauschs in den Strömen der Blöcke ausgelesen werden, ist in jedem Fall eine Lesart; das wird
im Ergebnis gesagt. Frames: Keim im Materie-Frame M, Rahmen und Achse wie r36–r40. OP5 bleibt offen.
