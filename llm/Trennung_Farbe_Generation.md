# Trennung von Farbe und Generation

Stand 2026-10-20. Modellbau, kein Datenvergleich, keine Vorhersage. Skript: `k28_sedenion_generationen.py`
(Oktonionen und Sedenionen in der Cayley–Dickson-Konvention des Companion, r04).

## Problem (K25.2)

`thm:three-generations` legt die Generationen auf e₄, e₅, e₆, das Triplett unter SU(3) ⊂ G₂, und gibt jeder
Generation einen Farbindex. Dasselbe Triplett trägt also Farbe und Generation. Gesucht ist eine Struktur, in der
(a) die Farbe in G₂ bleibt, (b) die Generationen von einer Symmetrie gezählt werden, die mit G₂ vertauscht, und
(c) 3 Farben × 3 Generationen = 9 unabhängige farbige Zustände entstehen.

## Weg A: Sedenionen, Aut(𝕊) = G₂ × S₃ (nachgerechnet)

Die Triolen-Hierarchie des Companion reicht bereits bis zu den Sedenionen (K6.2). Nach Gillard und Gresnigt
(arXiv:2306.13098) ist Aut(𝕊) = G₂ × S₃, mit ψ (Ordnung 3: Drehung um 120° in den sieben Ebenen (eᵢ, eᵢ₊₈)) und
ε (Ordnung 2: a + b·e₈ ↦ a − b·e₈).

| Prüfung (M) | Ergebnis |
|---|---|
| ψ, ε Automorphismen in der Companion-Konvention | ja |
| ψ³ = 1, ε² = 1, εψε = ψ⁻¹ (S₃) | ja |
| ψ, ε vertauschen mit G₂ (alle 1344 diskreten und zufällige kontinuierliche Elemente) | ja |
| Farbalgebra = Stabilisator von e₇ in g₂ | Dimension 8 = su(3) |
| Triolen-Relation 1 + ψ + ψ² = 0 auf den 14 Ebenenrichtungen | ja |
| ψᵏ(𝕆), k = 0, 1, 2: Unteralgebren, paarweise Schnitt ℝ, Summe 15-dimensional | ja |
| **Rang der 9 Zustände ψᵏ(e_c), c = 4, 5, 6** | **6, nicht 9** |
| Zerlegung (Spuren tr ψ = −5, tr ε = 0) | 𝕊 = 1 ⊕ sgn ⊕ 7·(Standard) |

Folgerung: Unter G₂ × S₃ ist 𝕊 = (1,1) ⊕ (1,sgn) ⊕ (7,2). Farbige Zustände tragen nur das S₃-**Dublett**, nie das
Singulett. Die drei Kopien jedes Farbzustands sind linear abhängig, weil die Triolen-Relation selbst
(z₁ + z₂ + z₃ = 0) sie verbindet. Weg A trennt Farbe und Generation sauber, liefert aber nur **zwei** unabhängige
farbige Generationen. Das entspricht der von Gillard und Gresnigt berichteten linearen Abhängigkeit.

## Weg B: Triality-Form auf 𝕆 ⊕ 𝕆 ⊕ 𝕆 (nachgerechnet)

Die trilineare Form t(x, y, z) = Re((xy)z) (Baez 2002) ist
- invariant unter der zyklischen Vertauschung (x, y, z) → (y, z, x), einer Triole ℤ₃,
- invariant unter (x, y, z) → (x̄, z̄, ȳ); beides zusammen erzeugt S₃,
- invariant unter G₂, das auf alle drei Kopien gleich wirkt und deshalb mit S₃ vertauscht.

Drei Kopien des Farbtripletts (e₄, e₅, e₆) in 𝕆 ⊕ 𝕆 ⊕ 𝕆: **Rang 9**, also 3 Farben × 3 Generationen unabhängig.
Generationen sind die drei Triality-Plätze, Farbe ist SU(3) ⊂ G₂ in jedem Platz. Auf den imaginären (farbigen)
Anteilen wirkt die Spiegelung mit Konjugation, also mit Vorzeichen; die Generationendarstellung ist dort
sgn ⊕ Standard, weiterhin dreidimensional.

Das passt zum Companion: Abschnitt 3 ordnet S₂ ≅ S⁸ = 𝕆P¹ („oktonionischer Spinor“) drei Generationen zu, und
Spin(8)-Triality ist die Struktur dieser oktonionischen Ebene (G₂ ist die von Triality festgehaltene Untergruppe).

## Empfehlung (V)

**Weg B.** Ersetzt in `thm:three-generations`: Generationenindex = Triality-Platz, Farbindex = SU(3)-Triplett
e₄, e₅, e₆ in jedem Platz. Weg A bleibt als Alternative dokumentiert, scheitert aber an der Generationenzahl.

## Folgen für frühere Ergebnisse

- **r12/r13-Flavour-Analyse:** Δ(96) ⊂ SU(3) liegt nach der Trennung in der Farbgruppe und kann keine
  Flavour-Symmetrie sein. Die Theoremlets r12.2–r12.4 bleiben als Mathematik richtig, verlieren aber ihre
  Lesart als Mischungssymmetrie. Damit entfällt die Grundlage für TM1/TM2 und für die Cayley–Dickson-CP aus r12
  (H4, H8 waren nach JUNO 2026 ohnehin disfavorisiert).
- **Mischung aus der Generationen-S₃:** ℤ₃ (Triole) für die geladenen Leptonen und eine Transposition als ℤ₂ für
  die Neutrinos erhalten die Spalte (0, ½, ½), also θ₁₃ = 0, ausgeschlossen. Das ist dasselbe Ergebnis wie das
  Minimalitätskriterium in H6. Reale Mischung braucht eine weitere Brechung; aus S₃ allein folgt keine Vorhersage.
- **Koide:** Die Triolen-Form v = t(1,1,1) + √2·Re(c(1, ω, ω²)) ist genau die Zerlegung des Generationenraums
  unter S₃ in Singulett-Richtung und Dublett. K = 2/3 bleibt die Gleich-Norm-Bedingung zwischen beiden
  (r10, v4.9) und ist weiter nicht hergeleitet.
- **Quarks:** Mit Weg B gibt es Platz für 3 × 3 farbige Zustände. Die Schemaabhängigkeit der Quark-Werte (K25.1)
  bleibt.
