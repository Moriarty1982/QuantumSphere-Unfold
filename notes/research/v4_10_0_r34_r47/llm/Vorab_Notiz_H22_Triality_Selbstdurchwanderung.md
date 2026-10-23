# Vorab-Notiz H22: Triality als Selbstdurchwanderung, und welche Perioden die Struktur zulässt

Festgelegt am 2026-10-23, **vor** der Rechnung. Bezug: Bestandsaufnahme Test 2 (K79.3), H21/K82 (Generationen brauchen eine
Dreierstruktur außerhalb von 𝕆), v4.8.0-r14.2 (Triality-Form auf 𝕆³, S₃). Autorabsicht (2026-10-23): Die Triole sollte eine andere
Darstellung der Sphäre sein; die fraktale Selbstdurchwanderung transformiert zwischen den Gestalten (Triole, Sphäre, Umgebung), die
Selbstähnlichkeit wählt bei jedem Zoom eine Gestalt. Autorhinweis: nicht auf Periode 3 festlegen.

## Gelesen vor der Notiz (Fundstellen)

- Ein Begriff „time crystal“ / „Zeitkristall“ kommt in Companion, Originalarbeit v3.1.4, Riemann-Paper v4.15, den Release-Archiven
  und den Notizen nicht vor.
- **Originalarbeit v3.1.4, `thm:spring`:** Die Triole ist Materie–Photon–Tachyon, ein Federsystem um das Photon bei z⁻ = 0
  (Materie +β, Tachyon −β = J-Bild), harmonischer Oszillator ω = γ_string √(2/3), Amplituden 1 : 1 : 3; „When matter oscillates,
  the photon follows … and this following motion defines the coordinate system.“ Diese Triole ist das Frame-Tripel M/P/T, kein
  120°-Objekt.
- **Companion `sec:alternating-triolic-orbit-scan`:** Verschiebe-Selektor Σ^i_j = δ^i_{j+1}; zwei Triolen-Regime A, B mit
  Σ(A) = B, Σ² = Regime-erhaltend (Periode 2, Struktur eines diskreten Zeitkristalls).
- **Companion `sec:crystal-fractal-readout-probe`:** Kristall = Kohärenz über Richtungen, Fraktal = Wiederkehr über Skalen.
- **Riemann-Paper, kombinatorische Bahntheorie:** beliebige Selbstabbildung Φ, periodische Punkte, primitive Bahnen beliebiger
  Mindestperiode ℓ(x).
- **Companion `sec:fractal`:** Selbstdurchwanderung = Transport derselben Null-Achsen-Struktur durch die Strata; ℤ/3-Muster
  z₁ + z₂ + z₃ = 0 auf der Null-Achse.

## Rahmen

Oktonionen wie k69. t(x, y, z) = Re((xy)z) auf 𝕆³. Symmetrie-Algebra der Tripel:
𝔤 = {(A, B, C) ∈ so(8)³ : t(Ax, y, z) + t(x, By, z) + t(x, y, Cz) = 0 für alle x, y, z}.
τ: (x, y, z) ↦ (y, z, x); ρ: (x, y, z) ↦ (x̄, z̄, ȳ). Auf dem ℂ-Faktor T (z ↦ z̄), R (z ↦ iz), J_B = R ∘ T.

## Hypothesen

Teil A, Triality (Test 2):
- **H22a:** dim 𝔤 = 28, jede der drei Projektionen 𝔤 → so(8) ist ein Isomorphismus, und die drei so entstehenden
  8-dimensionalen Darstellungen sind paarweise **nicht äquivalent** (kein Verflechtungsoperator ungleich null). t ist also die
  Spin(8)-Triality-Form, die drei Plätze tragen Vektor- und beide Spinor-Darstellungen.
- **H22b:** τ bildet 𝔤 auf sich ab und permutiert die drei Projektionen zyklisch. Wegen H22a ist das ein **äußerer**
  Automorphismus der Ordnung 3: die Triality selbst, als Verschiebung der Plätze.
- **H22c:** Die unter τ festen Elemente {(A, A, A) ∈ 𝔤} bilden eine 14-dimensionale Algebra, gleich den Derivationen von 𝕆 (G₂);
  mit A e₇ = 0 zusätzlich Dimension 8 (SU(3)_c). Lesart: Farbe ist, was die Durchwanderung festlässt; Generation ist, was sie
  vertauscht.
- **H22d (schwach):** Auf 𝕆⁴ ist keine der fünf Klammerungen von Re(x·y·z·w) invariant unter der zyklischen Verschiebung der vier
  Plätze, anders als t auf 𝕆³. *Ausdrücklich schwach:* Zyklische Mittel existieren immer. Die starke Aussage, dass Spin(8) genau
  drei 8-dimensionale irreduzible Darstellungen hat (Out = S₃), ist bekannte Mathematik und wird hier nicht bewiesen, nur über
  H22a verträglich geprüft.

Teil B, Perioden der Selbstdurchwanderung (nicht auf 3 festgelegt):
- **H22e:** Auf ℂ ⊗ 𝕆³ (reell 48-dimensional) erzeugen τ, ρ, T, R eine Gruppe der Ordnung 48 ≅ S₃ × D₄. τ, ρ vertauschen mit T, R,
  und τ, ρ erhalten t. Die vorkommenden Perioden (Elementordnungen) sind genau {1, 2, 3, 4, 6, 12}. Lesart: Die Struktur trägt
  Periode 2 (Orbit-Scan, Frame-Wechsel J_B), 3 (Triality), 4 (Dualitätsdrehung R) und deren Kombinationen, nicht nur 3.

## Entscheidungskriterium (verbindlich)

Jede Hypothese bestätigt oder widerlegt nach der wörtlichen Aussage (Toleranz 10⁻⁹ für Ränge und Abweichungen). Einordnung vorab:
- H22a–c bestätigt ⇒ Die drei Triality-Plätze sind ein Träger der Generationen, der mit der Farbe nicht kollidiert: Die
  Generationen-ℤ₃ ist die (äußere) Triality, die Farbe liegt in ihrer Fixgruppe. Das ist die von H21 verlangte Dreierstruktur
  außerhalb von 𝕆, und sie passt zur Autorlesart „drei Darstellungen derselben Sphäre“. **Nicht** gezeigt ist damit, dass die drei
  Plätze physikalisch Generationen *sind*.
- H22a widerlegt ⇒ t ist nicht die Triality-Form, und die Plätze erklären die Drei nicht.
- H22e bestätigt ⇒ Die Selbstdurchwanderung hat keine ausgezeichnete Periode; welche Periode ein Readout sieht, ist eine Wahl
  (Zoom bzw. Frame). Das Frame-Tripel M/P/T der Originalarbeit ist dabei kein ℤ₃-Objekt, sondern ℤ₂ (M ↔ T) mit Fixpunkt P; es wird
  hier nicht gerechnet, nur festgehalten.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
