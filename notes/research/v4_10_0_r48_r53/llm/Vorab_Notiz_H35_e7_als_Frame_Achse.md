# Vorab-Notiz H35: Ist e₇ die Bezugsachse der Frames?

Festgelegt am 2026-10-24, **vor** der Rechnung. Autor: „dann prüfe das mit dem rahmen nach“. Offen geblieben in r49 (Punkt 4): ob e₇ wenigstens als
Bezugsachse der Frames dient. Bezug: Konvention F (r22, korrigiert in r28/K72.1: Tachyon-Abbildung z ↦ iz, ρ ↦ σ_y ρ σ_y), Lean `Frames.lean`
(J_B = σ_x lässt die Ports fest, T = σ_z vertauscht sie), K77.8 (Annahme A_ℂ: ℂ-Faktor = Amplitudenebene z; T: z ↦ z̄, R: z ↦ iz, J_B = R ∘ T),
r35 (innere Einheit J = L_{e₇}, äußere i, P_± J = ±i P_±), r48 (Sektoren).

## Offenlegung (vorab analytisch gesehen)

R ist ℂ-linear und vertauscht mit allem, was auf 𝕆 wirkt; T und J_B sind antilinear. Auf e₇^⊥ ≅ ℂ³ (Triplett unter SU(3)) kann es keine
SU(3)-verträgliche, bezüglich J antilineare Abbildung geben, weil 3 nicht zu 3̄ äquivalent ist. Die Rechnung prüft das.

## Hypothesen

- **H35a (Frames auf ℂ ⊗ 𝕆):** Unter A_ℂ lässt die Tachyon-Abbildung R (z ↦ iz) jeden Sektor fest und vertauscht mit Q, B − L, iL_{e₇}, iR_{e₇} und
  der Farbe. T und J_B bilden den Sektor (ℓ, r) auf (−ℓ, −r) ab.
- **H35b (innere Einheit):** L_{e₇} vertauscht mit Stab_{G₂}(e₇) (eine innere Tachyon-Abbildung z ↦ e₇z existiert auf ganz 𝕆). Der Raum der reell-linearen
  Abbildungen K auf 𝕆 mit K g = g K für alle g in der Lie-Algebra von Stab(e₇) und K L_{e₇} = −L_{e₇} K hat Dimension 2 und verschwindet auf e₇^⊥:
  T und J_B haben im inneren Frame kein farbverträgliches Gegenstück auf dem Triplett.
- **H35c (Frame-Ebene = Singulett-Ebene):** φ(x + iy) = x + y·e₇ bildet die Frame-Ebene auf span(1, e₇) ab und übersetzt z ↦ iz in L_{e₇}, z ↦ z̄ in die
  Oktonion-Konjugation und z ↦ i z̄ in deren Produkt, jeweils auf span(1, e₇).

## Entscheidungskriterium (verbindlich)

Jede Hypothese bestätigt oder widerlegt nach der wörtlichen Aussage (Toleranz 10⁻⁹). Einordnung vorab:
- H35a–c bestätigt ⇒ e₇ ist Bezugsachse der Frames **nur teilweise**: Die Tachyon-Abbildung hat mit L_{e₇} ein inneres, farbverträgliches Gegenstück auf ganz
  𝕆; auf der Singulett-Ebene haben es alle drei Frame-Abbildungen (Frame-Ebene = Ebene des Photon-Kerns). Zeitumkehr T und J_B brauchen die äußere Einheit.
  Folge: Ladungen sind zwischen Materie und Tachyon frame-frei; die Ladungskonjugation ist der Zeitumkehr-Anteil T, nicht die Tachyon-Abbildung. Die
  Frame-Zeilen von r41 und r48, die „T“ als Ladungskonjugation führen, meinen die Zeitumkehr (σ_z), nicht den Tachyon-Frame (σ_y); das wird nachgetragen.
- H35a widerlegt ⇒ die Tachyon-Abbildung wirkt auf die Ladungen, und die Frame-Zeilen bleiben, wie sie sind.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
