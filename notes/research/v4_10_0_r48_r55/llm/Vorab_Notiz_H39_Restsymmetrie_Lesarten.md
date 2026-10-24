# Vorab-Notiz H39: Jede Teilchenart liest mit einer eigenen Untergruppe der A₄

Festgelegt am 2026-10-24, **vor** der Rechnung. Autor: „was wäre wenn jede teilchenart eine eigene leseart oder mischung bräuchte“, dann „mach das mal“.
Bezug: K77.4/`Dixon.inv_iff` (gemeinsame Symmetrie von Ablage und Triality-Form: A₄ = 12 Vorzeichen-Permutationen der drei Plätze, gerade Permutation, gerade
Zahl von Vorzeichenwechseln), r44 (Dirac-Kopplungen auf den Plätzen; nur für ν^c ist ein Majorana-Term eichinvariant), r46/r47 (Mischung braucht τ-Brechung),
r49 (u und d, ν und e liegen im selben 𝕆-Sektor).

## Regel (vor der Rechnung festgelegt, aus der Struktur)

Eine Lesart einer Teilchenart ist die Untergruppe G ⊂ A₄, unter der ihre Massenkopplung (M M†) invariant bleibt; sie legt die Eigenbasis ganz oder teilweise fest.
- Die 𝕆-Sektoren unterscheiden u von d und ν von e nicht (r49). Eine Regel aus den Sektoren gibt also u und d dieselbe Lesart, ebenso ν und e, und es gäbe keine
  Mischung. Unterscheidend ist in der Struktur nur r44: **Dirac-Kopplungen** (u, d, e) sind zirkulant, also invariant unter G_D = ⟨τ⟩ ≅ ℤ₃ (die zyklische
  Verschiebung, in A₄ enthalten). **Neutrinos** können einen Majorana-Term haben (ν^c ist das einzige Gesamtsingulett) und lesen mit einer anderen Untergruppe G_M.
- Folge der Regel: u und d lesen gleich ⇒ in führender Ordnung V_CKM = 1 (CKM nur aus Korrekturen, also klein). Die PMNS-Matrix ist der Unterschied zwischen G_D
  und G_M. G_M ist von der Struktur nicht festgelegt; gerechnet werden alle Untergruppen von A₄ außer ⟨τ⟩ selbst und außer A₄ (dort wären die Massen entartet).

## Offenlegung und Korrektur

Im Gespräch habe ich für ℤ₃ gegen ℤ₂ eine tribimaximale Mischung ohne Parameter angekündigt. Das ist für A₄ allein falsch: tribimaximal braucht eine zusätzliche,
in A₄ nicht enthaltene Symmetrie (S₄). Vorab analytisch erwartet: G_M = Klein-Gruppe ℤ₂ × ℤ₂ (Vorzeichenwechsel) legt die Basis ganz fest und gibt |U_ij|² = 1/3 für
alle Einträge (sin²θ₁₃ = 1/3, widerlegt). G_M = ℤ₂ legt eine Spalte fest, |U_i2|² = 1/3 ("TM2"), mit einem freien Winkel; daraus sin²θ₁₂ = 1/(3 cos²θ₁₃) ≈ 0.341.

## Daten

NuFIT 6.0, normale Ordnung, 3σ: sin²θ₁₂ ∈ [0.275, 0.345], sin²θ₂₃ ∈ [0.430, 0.596], sin²θ₁₃ ∈ [0.02023, 0.02376].

## Verfahren

Untergruppen von A₄ durch Erzeugen aus Elementen und Paaren. Für jedes G: gemeinsame Eigenräume; eindimensionale legen Spalten fest, ein zweidimensionaler Eigenraum
erlaubt eine Drehung U(2) mit Winkel θ und Phase φ (Gitter 721 × 73). U_e aus ⟨τ⟩ (Fourier-Spalten), Zuordnung der Spalten zu e, μ, τ und zu ν₁, ν₂, ν₃ in allen
6 × 6 Reihenfolgen. sin²θ₁₃ = |U_e3|², sin²θ₁₂ = |U_e2|²/(1 − |U_e3|²), sin²θ₂₃ = |U_μ3|²/(1 − |U_e3|²).

## Hypothesen

- **H39a (Klein):** Mit G_M = ℤ₂ × ℤ₂ liegt keine Zuordnung in den 3σ-Bereichen.
- **H39b (ℤ₂):** Mit G_M = ℤ₂ gibt es eine Zuordnung und (θ, φ) mit allen drei Größen in den 3σ-Bereichen. Mitberichtet: Spannweite von sin²θ₁₂ und sin²θ₂₃ unter
  allen (θ, φ), die sin²θ₁₃ treffen (Schärfe der zwei verbleibenden Vorhersagen).
- **H39c (andere ℤ₃):** Mit G_M = eine der drei anderen ℤ₃-Untergruppen liegt keine Zuordnung in den 3σ-Bereichen.
- **H39d (Quarks):** Mit derselben Lesart für u und d ist V_CKM in führender Ordnung die Einheitsmatrix (bis auf Spaltenzuordnung); die gemessenen CKM-Winkel
  sind klein, verträglich mit Korrekturen. (Qualitativ; zählt nur zusammen mit H39b.)

## Entscheidungskriterium (verbindlich)

- H39b bestätigt und die Spannweiten aus H39b schmal (sin²θ₁₂ innerhalb einer Breite von 0.02, sin²θ₂₃ innerhalb 0.1) ⇒ Die Lesart-Regel (Dirac ℤ₃, Majorana ℤ₂)
  erklärt qualitativ, warum Leptonen stark und Quarks schwach mischen, und legt sin²θ₁₂ ≈ 0.34 fest. Breite Spannweiten ⇒ Anpassung mit einem Winkel.
- H39b widerlegt ⇒ Keine Untergruppen-Lesart aus A₄ erklärt die PMNS-Mischung.
- H39a und H39c sind vorab erwartet (Prüfung).

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
