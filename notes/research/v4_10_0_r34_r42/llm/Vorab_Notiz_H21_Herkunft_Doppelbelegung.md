# Vorab-Notiz H21: Woher kommt die Doppelbelegung von Farbe und Generation?

Festgelegt am 2026-10-23, **vor** der Rechnung. Bezug: v4.8.0-r13 (Doppelbelegung festgestellt), r14 (Trennung vorgeschlagen),
v4.9.0-r33 (Dixon-Ablage), r35 (innere Einheit J = L_{e₇}; Doppelbelegung dort als kein Frame-Effekt eingestuft).

## Gelesen vor der Notiz (Fundstellen)

- Triolische Struktur: drei Kerne K₁, K₂, K₃ mit z₁ + z₂ + z₃ = 0, um 120° phasenverschoben (Grundstruktur der Sphaera).
- `thm:octonion-SU3`: „Das Triplett ℂ³ trägt die drei Kerne (K₁, K₂, K₃) als die drei Farben.“ Ebenso im Beweis der
  Spektralaussage („The three kernels realize the three colors of ℂ³“).
- `thm:three-generations`: Gen_i ↔ e_{i+3}; Beweis: „Die Fano-Struktur gibt die zyklische Symmetrie e₄ → e₅ → e₆.“
- Koide/Brannen-Form der Generationen mit Phasen θ + 2πk/3.
- Bekannt (r13): [e₄, e₅, e₆] = −2e₇, (e₄, e₅, e₆) ist keine Fano-Linie (e₄e₅ = e₁).

## Vermutung (V)

Die Doppelbelegung stammt daher, dass **eine** Dreierstruktur, die Triole mit ihrer zyklischen ℤ₃ und den 120°-Phasen, zweimal
gelesen wurde: als Farbe (Kerne = Farben) und als Generation (zyklisches e₄ → e₅ → e₆, Brannen-Phasen). Ist die zyklische
Vertauschung ein Automorphismus, der e₇ festhält, so liegt sie in SU(3) = Stab(e₇): Sie ist dann eine **Farbdrehung**, und
jede daraus gebaute Generationen-Symmetrie wäre eine Farbsymmetrie.

## Rahmen

Konventionen wie H19/H20 (k69-Multiplikation, J = L_{e₇}, Q, P_±, Stab(e₇)). ω = e^{2πi/3}.
Kandidat σ: σ(e₀) = e₀, σ(e₇) = e₇, σ: e₄ → e₅ → e₆ → e₄, auf e₁, e₂, e₃ J-linear fortgesetzt (aus J e₄ = −e₃, J e₅ = −e₂,
J e₆ = e₁: σ(e₃) = e₂, σ(e₂) = −e₁, σ(e₁) = −e₃). Zusätzlich werden alle vorzeichenbehafteten Permutationen geprüft, die e₇
festhalten und e₄ → e₅ → e₆ → e₄ zyklisch vertauschen.

## Hypothesen

- **H21a (Automorphismus):** Es gibt ein σ der genannten Art, das ein Automorphismus von 𝕆 ist; damit σ ∈ Stab(e₇) = SU(3).
- **H21b (Farbdrehung, nicht Zentrum):** Auf (e₇^⊥, J) mit komplexer Basis e₄, e₅, e₆ ist σ die zyklische Permutationsmatrix
  (Determinante 1, Eigenwerte 1, ω, ω̄), also ein Element der Weyl-Gruppe von SU(3) und nicht im Zentrum. σ vertauscht mit Q
  und mit den Frame-Abbildungen T, R, J_B (frame-frei).
- **H21c (Triole = Farbzustand):** Die 120°-Triole der Kerne, z_k = ω^k auf e_{k+4} (k = 0, 1, 2) mit komplexen
  Koeffizienten bezüglich J, also Σ z_k e_{k+4} mit z₀ + z₁ + z₂ = 0, ist Eigenvektor von σ zum Eigenwert ω oder ω̄. Die
  zyklische Verschiebung der Kerne ist also die Farbdrehung σ, gesehen als 120°-Phase. Unter P₋ liegt die Triole im
  Farb-Triplett Q = 2/3.
- **H21d (reelle Untergruppe):** Die Untergruppe von Stab(e₇), die den reellen Spann von e₄, e₅, e₆ erhält, hat die Dimension
  3 und wirkt darauf als SO(3). Eine Generationen-Symmetrie auf dem reellen Spann (wie die Flavour-Gruppen von v4.8.0-r12) wäre
  damit eine Untergruppe der Farbgruppe.
- **H21e (Trennung möglich):** In der Dixon-Ablage (Im ℍ)⊗ℂ⊗𝕆 (v4.9.0-r33) vertauscht die Generationen-ℤ₃ (zyklisch auf Im ℍ,
  von rechts) mit σ ⊗ 1 und mit ganz Stab(e₇). Das folgt aus der Tensorstruktur und ist nur Kontrolle.

## Entscheidungskriterium (verbindlich)

Jede Hypothese bestätigt oder widerlegt nach der wörtlichen Aussage (Toleranz 10⁻¹⁰). Einordnung vorab:
- H21a bis H21c bestätigt ⇒ Die Doppelbelegung ist **kein Frame-Effekt, sondern eine Identifikation**: Die zyklische Symmetrie
  der Triole, die der Companion als Generationen-Symmetrie liest, ist eine Farbdrehung. Die Kerne als Farben und die Triole als
  Generationen sind dasselbe Objekt. Die Trennung verlangt eine **zweite** Dreierstruktur außerhalb von 𝕆.
- H21a widerlegt ⇒ Die zyklische Vertauschung ist keine Symmetrie von 𝕆. Die Begründung „Fano-Struktur gibt e₄ → e₅ → e₆“
  trägt dann nicht, und die Doppelbelegung käme nur aus der Benennung.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
