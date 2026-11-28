# Ergebnis H240 (k456): Zwei RAIDZ2, anders zusammengeschaltet?

**Datum:** 2026-11-28. **Vorab:** `Vorab_H240_RAIDZ2_Verschaltung.md`, Commit abcfa98, vor der Rechnung. **Rechnung:** `k456_test_h240.py` → `k456_out.txt`;
Gegenprobe `k456b_gegenprobe.wl` → `k456b_out.txt` (exakt). **Urteil: trägt teilweise.** Es gibt eine feste, für alle Nullteiler gleiche Verschaltung,
aber sie besteht nicht aus zwei RAIDZ2. Sie ist ein ungeschützter 8er-Block neben 4 Spiegelpaaren.

## Methode
Ein linearer Code zerfällt genau dann über eine Aufteilung der Platten, wenn sein Matroid unzusammenhängend ist. Die Zusammenhangskomponenten
(berechnet über die Fundamentalkreise der Paritätsprüfmatrix) sind die feinste Zerlegung. Damit sind alle Direktsummen-Verschaltungen auf einmal
erfasst: getrennt, verschränkt quer zur Wand, 4 × RAID5. Je Komponente werden [Länge n, Daten k, Mindestabstand d] angegeben; die Ausfalltoleranz ist d − 1.

## Befunde
- **A1 (nicht blind):** RAID1 über zwei RAIDZ2 (Kapazität 6/16) und der volle 4×4-Produktcode (9/16) scheiden an der Kapazität aus; C_x hat 12/16.
- **A2 (blind), Standardkoordinaten:**
  - Alle 84 Basis-Nullteiler: 8 × [1,1,1] + 4 × [2,1,2], also 8 ungeschützte Platten und 4 Spiegelpaare.
  - Alle 200 allgemeinen Nullteiler: 2 × [1,1,1] + 1 × [14,10,5], also e₀ und e₈ ungeschützt; die übrigen 14 Platten bilden einen einzigen MDS-Block mit 4
    Paritäten, der jeden Ausfall von bis zu 4 Platten verkraftet.
  - Zwei [8,6,3] (zweimal RAIDZ2) oder vier [4,3,2] (4 × RAID5) kommen nicht vor.
- **A3:** Jeder Nullteiler-Code hat ungeschützte Platten. Verschachtelte Verschaltungen, die jede Platte schützen (V4), scheiden deshalb aus.
- **B (Vorhersage nicht blind, numerisch bestätigt):** Der gebaute Rahmen g ist ein Automorphismus von 𝕆 (Abweichung 1,4·10⁻¹⁵) und diagonal von 𝕊
  (1,1·10⁻¹⁴). In G₂-angepassten Koordinaten haben alle 200 allgemeinen Nullteiler dieselbe Zerlegung wie (e₁ + e₁₀)/√2:
  8 × [1,1,1] + 4 × [2,1,2].
- **B2 (blind, Python und Wolfram exakt):** L_x ist blockdiagonal.
  - Auf dem 8-dim. Block ℍ_x ⊕ ℍ_x·e₈ mit ℍ_x = span{1, a, b, ab} ist L_x invertierbar: Alles geht durch, ohne Schutz (wie RAID0).
  - Auf dem 8-dim. Komplement hat L_x Rang 4, und dort liegt der ganze Kern: Die Hälfte bleibt, wie bei 4 Spiegelpaaren (RAID1).
- **Zufallskontrolle:** Alle 200 zufälligen [16,12]-Codes sind zusammenhängend und MDS, also 1 × [16,12,5].

## Lesart
„Zwei Gruppen zu 8“ gibt es tatsächlich, aber nicht an der Wand e₈ und nicht als zwei RAIDZ2. Ein Nullteiler teilt 𝕊 in einen Quaternion-Block
ℍ_x ⊕ ℍ_x·e₈ (8 Platten, Klartext) und dessen Komplement (8 Platten, 4 Spiegelpaare). Kapazität 8 + 4 = 12. Gegen Ausfälle schützt diese Verschaltung
schlechter als ein Zufallscode, weil der Klartext-Block ungeschützt ist. Die Lage des Blocks hängt vom Nullteiler ab (ℍ_x wird von a und b erzeugt), die Form
ist für alle gleich.

## Korrektur zu H239 (append-only)
Das Ergebnis von H239 nannte den Code allgemeiner Nullteiler „deutlich schwächer als ein zufälliger Code“. Genauer: Alle nicht rekonstruierbaren
Ausfallmengen aus k455c (2, 29, 196, 819) enthalten e₀ oder e₈. Ohne diese beiden Platten ist der Code in Standardkoordinaten MDS ([14,10,5]).
Schwächer ist er nur wegen der zwei ungeschützten Platten 1 und e₈.

## Hergeleitet, gesetzt, offen
- **Hergeleitet:** die Komponenten in beiden Koordinatensystemen; die Blockzerlegung ℍ_x ⊕ ℍ_x·e₈ (invertierbar) und das Komplement (Rang 4, mit Kern).
- **Gesetzt:** die Übersetzung aus H239 (Code = Bild der Linksmultiplikation, Platte = Koordinate) und die Liste der Verschaltungen.
- **Nicht blind:** die Gleichheit in angepassten Koordinaten (folgt aus der Transitivität von G₂ auf orthonormalen Paaren und G₂ ⊂ Aut(𝕊)).
- **Offen:** Die Standardkoordinaten sind nicht G₂-invariant; der [14,10,5]-Block ist dort generisch und kein Strukturbefund. Ob die Blockzerlegung
  physikalisch etwas bedeutet (etwa ℍ_x als Ladungs- oder Spinanteil), ist nicht untersucht.

## Werkzeuge und Grenzen
Python (Matroid-Komponenten, Mindestabstand bis Gewicht 6, G₂-Rahmen, Zufallskontrolle) und Wolfram (exakt: Blockzerlegung an einem rationalen Nullteiler).
Qiskit nicht einschlägig. Nicht lineare oder nicht über Koordinaten definierte Verschaltungen (etwa Reed–Solomon über anderen Körpern) wurden nicht geprüft.
