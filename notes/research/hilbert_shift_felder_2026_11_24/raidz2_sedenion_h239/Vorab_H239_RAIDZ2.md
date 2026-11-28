# Vorab H239 (k455): Ist die Struktur von 𝕊 im Grunde zweimal RAIDZ2?

**Datum:** 2026-11-28, vor der Rechnung committet. **Anlass:** Marc (18:03): „prüfe bitte ob das evtl. quasi zwei raidz2 sein könnten“, im Anschluss an
H237/H238 (8 wellenfähige Richtungen je Kopie, Wand e₈, Nullteiler).

## Vorwissen geprüft
- Im Repo kommt RAIDZ nicht vor (`git grep -i raidz` leer). Der ZFS-Baustein des Coprozessors (PR #401) ist Hardware, keine Algebra-Aussage.
- **H237/k453:** Jede der drei Kopien hat mit e₈ eine volle Clifford-Menge aus 8 Richtungen. Der Kern aller 15 Richtungen ist span{1, e₈}.
- **H238/k454:** Die Leck-Energie ist L(θ) = 42·sin²3θ.
- **H139:** Nullteiler entsprechen einem flachen Kopienprofil.
- **Literatur (Bezug, nicht nachgeprüft):** Der Annihilator eines Nullteilers von 𝕊 ist 4-dimensional (Moreno); Nullteiler-Diagonalen e_i ± e_j mit
  i ∈ 1…7, j ∈ 9…15, j ≠ i+8 („assessors“, 42 Paare, 7 Box-Kites, de Marrais).

## Übersetzung (gesetzt)
RAIDZ2 mit 8 Platten: 6 Daten, 2 Parität, zwei beliebige Ausfälle verkraftbar. Als linearer Code ist das ein [8, 6]-Code mit Mindestabstand 3 (MDS).
„Zweimal RAIDZ2“ heißt: ein [16, 12]-Code, der in zwei unabhängige Gruppen zu je 8 Koordinaten zerfällt.
- Ein Nullteiler x vernichtet beim Multiplizieren einen Teil des Inhalts. Der gespeicherte Inhalt ist der Code C_x = Bild(L_x) ⊂ ℝ¹⁶, die Ausfallrichtungen
  sind K_x = Kern(L_x). Koordinaten sind die Basiseinheiten e₀…e₁₅; die natürliche Gruppengrenze ist die Wand e₈ (untere Hälfte 𝕆, obere Hälfte).
- Nullteiler-Stichproben: (Z1) alle 84 Basis-Diagonalen (e_i ± e_j)/√2; (Z2) 200 allgemeine Nullteiler, zufällig, x = (a, b)/√2 mit a, b ∈ Im 𝕆
  Einheitsvektoren und a ⟂ b (vorher wird geprüft, dass L_x singulär ist; nicht singuläre werden gezählt und verworfen).

## Kriterien
- **D1 (nicht blind, Literatur):** Rang L_x = 12 für alle Nullteiler. Das entspricht der Kapazität 12/16 = 6/8 von zweimal RAIDZ2.
- **D2 (blind), Spaltung:** C_x = (C_x ∩ unten) ⊕ (C_x ∩ oben) mit 6 + 6. Für Z1 zusätzlich alle 6435 Aufteilungen der 16 Koordinaten in 8 + 8.
- **D3 (blind), Paritätsprofil:** In jeder Gruppe einer gefundenen Spaltung ist jeder Ausfall von 2 Koordinaten rekonstruierbar (Rang der Einschränkung
  auf die übrigen 6 ist 6), aber nicht jeder Ausfall von 3.
- **Zufallskontrolle:** 2000 zufällige 12-dimensionale Unterräume von ℝ¹⁶ und 2000 zufällige 12-dim. Bilder von Rang-12-Matrizen mit derselben
  Kerngröße: Anteil mit 6+6-Spaltung an der Wand und Anteil mit dem Profil aus D3.

## Urteil
- **trägt:** D1, D2 an der Wand e₈ für alle Nullteiler aus Z1 und Z2, D3 in beiden Gruppen, und die Zufallskontrolle spaltet nie.
- **trägt teilweise:** Spaltung nur für Z1 oder nur an einer anderen Aufteilung als der Wand, oder D3 verfehlt.
- **widerlegt:** Keine 8+8-Spaltung. Dann bleibt von RAIDZ2 nur die Zahl 12/16, die schon aus der Literatur folgt.

## Nur Bericht
- dim(K_x ∩ unten), dim(K_x ∩ oben) und die Ränge der Projektionen von K_x auf die Hälften.
- Für jede Kopie V_k aus H138: dim(K_x ∩ V_k).

## Werkzeuge
Python k455 (Hauptrechnung), Wolfram k455b (exakt für Basis-Nullteiler: Rang, Spaltung an der Wand). Qiskit nicht einschlägig.
