# Vorab-Notiz H20: Woher kommt der Fehler in der Farb- und ν_R-Zuordnung? (innerer gegen äußeren Frame)

Festgelegt am 2026-10-23, **vor** der Rechnung. Anlass: H19c (v4.9.0-r34, K80.3) hat die wörtliche Zuordnung von
`thm:octonion-SU3` / `thm:three-generations` widerlegt. Autorhinweis: Wenn es wieder nur der feste Frame war, muss
unterschieden werden.

## Wortlaut (gelesen vor der Notiz)

- `thm:octonion-SU3`: „𝕆 = ℂ ⊕ ℂ³ unter SU(3), Singulett plus Triplett; das Triplett trägt die drei Kerne als Farben.“
- `thm:three-generations`, Beweis: „Im(𝕆) = ℂ ⊕ ℂ³: Singulett e₇ und Triplett (e₄, e₅, e₆). Das Anti-Triplett (e₁, e₂, e₃)
  trägt die konjugierte Farbdarstellung.“ Tabelle: Gen_i ↔ e_{i+3}, ν_R ↔ e₇.
- `thm:SM`: U(1) aus dem komplexen Skalar it, „Elektromagnetismus“.

## Vermutung (V)

Der Companion rechnet im **inneren Frame**: komplexe Struktur J = L_{e₇} auf 𝕆 selbst (ohne den ℂ-Faktor). H19 rechnet im
**äußeren Frame**: i = ℂ-Faktor der Dixon-Ablage. Die beiden Einheiten sind verschiedene Objekte; der Fehler könnte darin liegen,
dass sie nicht unterschieden werden.

## Rahmen

Konventionen wie H19 (k22/k69, α_a, N, Q = N/3, Stab(e₇), T: i ↦ −i). J = L_{e₇} (reell, J² = −1). P_±(x) = ½(x ∓ i·Jx) für
x ∈ 𝕆, als Abbildung 𝕆 → ℂ⊗𝕆.

## Hypothesen

- **H20a (innerer Frame, `thm:octonion-SU3`):** Jedes Element von Stab(e₇) ist J-linear. (𝕆, J) ≅ ℂ⁴ zerfällt in
  span_ℝ(1, e₇) (Stab wirkt trivial) und e₇^⊥ (irreduzibel als komplexe 3-dim. Darstellung), und e₄, e₅, e₆ ist eine
  **komplexe Basis** von (e₇^⊥, J).
- **H20b (Anti-Triplett-Satz, wörtlich):** span(e₁, e₂, e₃) trägt die zu (e₄, e₅, e₆) konjugierte Darstellung — im inneren
  Frame (als eigener J-invarianter Unterraum mit konjugierter Darstellung) **oder** im äußeren Frame (span_ℂ(e₁, e₂, e₃) als
  Stab-invarianter Unterraum bzw. Q-Eigenraum). Bestätigt, wenn eines davon zutrifft.
- **H20c (Brücke):** P₊ und P₋ sind Stab(e₇)-äquivariant, injektiv und erfüllen P_±J = ±i·P_±. Jede bildet e₇^⊥ auf eines der
  beiden Q-Tripletts und span(1, e₇) auf eines der beiden Q-Singuletts ab, P₊ und P₋ auf verschiedene; die Bilder von e₄, e₅, e₆
  sind eine Basis des Tripletts, das Bild von e₇ liegt im Singulett. T vertauscht P₊ und P₋.
- **H20d (U(1) von `thm:SM`):** Q liegt in span_ℝ{1, i·L_{e₇}, i·R_{e₇}} (R = Rechtsmultiplikation), braucht also beide
  Einheiten; die Phase e^{iθ} des komplexen Skalars allein wirkt auf allen vier Ladungssektoren gleich.

## Entscheidungskriterium (verbindlich)

Jede Hypothese bestätigt oder widerlegt nach der wörtlichen Aussage (Toleranz 10⁻¹⁰). Einordnung vorab:
- H20a und H20c bestätigt ⇒ Die H19c-Widerlegung der Triplett-Basis und von e₇ ↔ ν_R ist ein **Frame-Unterschied**: im inneren
  Frame richtig, im äußeren über P_± übersetzbar, aber erst dort mit Ladungen. Die Wahl P₊ gegen P₋ ist dann eine Frame-Wahl.
- H20b widerlegt ⇒ Der Anti-Triplett-Satz ist ein echter Fehler, und zwar eine **Vermischung** beider Frames: Konjugierte
  Darstellungen gibt es erst mit der äußeren Einheit.
- Unabhängig davon bleibt die Doppelbelegung Gen_i ↔ e_{i+3} (Farbe = Generation, v4.8.0-r13); sie ist kein Frame-Problem.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
