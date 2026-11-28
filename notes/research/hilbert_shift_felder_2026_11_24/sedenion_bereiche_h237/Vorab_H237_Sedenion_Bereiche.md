# Vorab H237 (k453): Tragen die wellenfähigen Richtungen in 𝕊 die drei Oktonion-Kopien? Welche Bereiche von 𝕊 lassen stabile Felder zu?

**Datum:** 2026-11-28, vor der Rechnung committet. **Anlass:** k452 hat gezeigt, dass die Feldgleichung erster Ordnung D = ∂₀ + Σ eᵢ∂ᵢ nur bis 𝕆
eine Wurzel der Wellengleichung ist. Marc gab den vorgeschlagenen Test frei und ergänzte (17:42): „es könnte in den sedenionen noch bereiche geben,
die stabile felder zulassen“. 𝕊 wird also nicht pauschal ausgeschlossen, sondern kartiert.

## Vorwissen geprüft
- **k452:** Für D über ganz 𝕊 ist die Clifford-Bedingung LᵢLⱼ + LⱼLᵢ = −2δᵢⱼ verletzt (Abweichung 2). S¹⁵ trägt höchstens ρ(16) − 1 = 8 Felder.
- **k407:** Die größte antikommutierende Menge von Basis-Linksmultiplikationen in HS(4) hat 8 Elemente.
- **H138 (k321):** In 𝕊 gibt es genau drei G₂-stabile unitale Oktonion-Kopien O_v = span{1} ⊕ {(v₀a, v₁a) : a ∈ Im 𝕆} mit v = (1, 0) und
  (−½, ±√3/2). Alle drei sind oktonionisch, also alternativ und normmultiplikativ, und paarweise nicht orthogonal.
- **H139:** Nullteiler entsprechen einem flachen Kopienprofil.
- **H140–H143:** Ob die Kopien Generationen sind, ist offen.
- **k254:** Der endliche Anteil von Aut(𝕊) ist S₃ und vertauscht die drei Kopien.
- **Literatur (Bezug, nicht nachgeprüft):** Unter den 8-dimensionalen Basis-Unteralgebren von 𝕊 gibt es Oktonionen und „Quasi-Oktonionen“
  (Cawagas). Die Nullteiler der Norm 1 bilden eine Mannigfaltigkeit, die zu G₂ homöomorph ist (Moreno).

## Größen (gesetzt)
- Produkt wie k253/k321 (g = −1 an jeder Wand). Lᵤ ist die Linksmultiplikation mit u.
- Für einen Richtungsraum U ⊂ Im 𝕊 mit Orthonormalbasis uₐ ist K_ab = L_a L_b + L_b L_a + 2δ_ab·1 (16×16).
- Wellendefekt: δ(U) = maxₐᵦ ‖K_ab‖.
- **Stabiler Bereich:** W(U) = ∩ₐᵦ ker K_ab. Das sind die Feldwerte, für die D̄D = Δ mit Richtungen aus U gilt.
- Nicht blind: Für eine Kopie V gilt V ⊂ W(Im V), weil V alternativ ist. Also ist dim W ≥ 8.

## Teil A (blind): die drei Kopien
Für jede Kopie V_k (k = 1, 2, 3) werden δ(Im V_k) und dim W(Im V_k) berechnet.
- **trägt:** δ = 0 für alle drei. Dann quadriert sich die Feldgleichung jeder Kopie auf ganz 𝕊; die Kopien sind wellenfähige Bereiche auf ganz 𝕊.
- **trägt teilweise:** δ = 0 für eine oder zwei Kopien, oder für alle δ ≠ 0, aber dim W > 8 für mindestens eine Kopie. Dann ist der stabile Bereich
  größer als die Kopie selbst.
- **widerlegt:** δ ≠ 0 und dim W = 8 für alle drei. Felder einer Kopie sind dann nur innerhalb der Kopie stabil.

## Teil B (Kartierung, nur Bericht, blind gerechnet)
- **B1:** Alle von Basiseinheiten aufgespannten Unteralgebren der Dimension 2, 4 und 8 zählen, jeweils mit den Eigenschaften: alternativ,
  Nullteiler, Norm multiplikativ.
- **B2:** Für jede 8-dimensionale Basis-Unteralgebra δ und dim W ihres Imaginärteils.
- **B3:** Für ganz Im 𝕊 (15 Richtungen) dim W(Im 𝕊).
- **B4:** Maximale Clifford-Mengen aus Basiseinheiten (paarweise antikommutierend, Lᵢ² = −1 auf ganz 𝕊): Größe, Anzahl, und ob eine Menge die
  Imaginärteile einer Kopie enthält.
- **B5:** Stichprobe allgemeiner (nicht basisgebundener) Richtungen: größtes zufällig gefundenes U mit δ(U) = 0 im Vergleich zu 8.

## Werkzeuge
Python k453 und Wolfram k453b (unabhängig: δ und dim W für die drei Kopien, Zahl der 8-dimensionalen Basis-Unteralgebren). Qiskit ist nicht einschlägig.
