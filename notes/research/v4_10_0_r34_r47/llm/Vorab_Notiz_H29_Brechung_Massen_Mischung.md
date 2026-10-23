# Vorab-Notiz H29: Verbindungen zwischen den Chiralitätshälften (Higgs, Massenterme) und Massen und Mischung über die Triality-Plätze

Festgelegt am 2026-10-23, **vor** der Rechnung. Autor: „versuche das mal“. Bezug: r41–r43 (Aufteilung D, C_ch = ½(1 + iL_{e₇}), Inhalt einer
Generation), r37/r38 (Triality τ, Spiegelung ρ = Frame-Triole), v4.8.0-r10 (Koide-Form = Skalar + symmetrische Triole), H11/H16–H18
(natürliche Potentiale: höchstens zwei Massen), `sec:millennium-hc` (MM-Matrix mit mehreren HC).

## Rahmen

V = ℂ⊗ℍ⊗𝕆 ≅ ℂ³² wie in r42 (T = komplexe Konjugation). Ein **Verbinder** ist eine Abbildung V → V, die mit der Farbe und mit der
Linkswirkung von ℍ (Lorentz-Drehungen L_q) vertauscht: linear (X) oder antilinear (Φ = X ∘ T). Ein antilinearer Verbinder antivertauscht dann
mit den Boosts iL_q, bildet also links- auf rechtshändig ab: die Operatorform eines Massenterms. Eichwirkung eines hermiteschen Erzeugers G:
linear X ↦ GX − XG, antilinear X ↦ GX + X·Ḡ. Blöcke nach C = C_ch: „Bild ← Kern“ usw.
Massen über die Plätze: Kopplungsmatrix M (3 × 3) auf den Triality-Plätzen; P = zyklische Verschiebung τ, R = Transposition ρ (fester Platz 1).

## Offenlegung

Dass Yukawa-Kopplungen der Standardmodell-Fermionen ein Dublett mit Y/2 = ±½ verlangen, ist bekannte Gruppentheorie; H29b ist für die
antilinearen Verbinder daher erwartet. Ebenso bekannt: Hermitesche ℤ₃-Zirkulanten haben Eigenwerte a + 2|b|cos(θ + 2πk/3) (Brannen-Form),
S₃-symmetrische Zirkulanten (b = c) haben ein entartetes Paar, und gleichzeitig zirkulante Matrizen werden von derselben Fourier-Matrix
diagonalisiert. Nicht vorab gerechnet sind die Dimensionen der Verbinder-Räume und die Ladungen der linearen Blöcke.

## Hypothesen

- **H29a (Räume):** Die linearen wie die antilinearen Verbinder bilden je einen 24-dimensionalen komplexen Raum (Kommutant von Farbe auf ℂ⊗𝕆,
  Dimension 6, mal Rechtsmultiplikation auf ℍ, Dimension 4).
- **H29b (antilinear, Higgs):** Der antilineare Block „Bild ← Kern“ hat Dimension 8 und zerfällt unter SU(2)′ × U(1)_Y genau in Dubletts mit
  Y/2 = +½ und Y/2 = −½ (je 4 Dimensionen; Lepton- und Quark-Teil): die Quantenzahlen von H und H̃. Er enthält Lepton- **und** Quark-Teil.
- **H29c (linear, keine Massenterme):** Der lineare Block „Bild ← Kern“ ist nur im Lepton-Sektor von null verschieden (Quark-Teil Dimension 0,
  da 3 und 3̄ nicht linear verflochten werden) und trägt keine reinen Higgs-Quantenzahlen: unter seinen Hyperladungen kommt |Y/2| = 3/2 vor.
- **H29d (eichinvariant):** Eichinvariante antilineare Verbinder (von allen Erzeugern annulliert) gibt es nur im Block „Kern ← Kern“, und dort
  nur auf Q_em = 0 (Majorana-Term für ν^c); keinen im Block „Bild ← Kern“.
- **H29e (Massen und Mischung über die Plätze):** (i) Mit τ- und ρ-Symmetrie (S₃) hat jede hermitesche M höchstens zwei verschiedene Eigenwerte.
  (ii) Mit τ-Symmetrie allein (ℤ₃) sind die Eigenwerte generisch drei verschiedene und genau von der Brannen-Form a + 2|b|cos(θ + 2πk/3);
  Koide K = 2/3 genau für |b| = a/√2. (iii) Sind die Kopplungen für up und down beide τ-symmetrisch, so ist |V| = |U_u†U_d| eine
  Permutationsmatrix: keine Mischung. Mischung verlangt Brechung von τ selbst.

## Entscheidungskriterium (verbindlich)

Jede Hypothese bestätigt oder widerlegt nach der wörtlichen Aussage (Toleranz 10⁻⁹; H29e an 200 Zufallsmatrizen). Einordnung vorab:
- H29b, c bestätigt ⇒ In der Operatorsprache der MM-Matrix sind Massenterme **antilinear**: Sie enthalten den Frame-Wechsel T. Lineare
  Nebendiagonal-Blöcke einer farbverträglichen MM-Matrix liefern keine Massen. Lesart: Masse ist eine Kopplung zwischen Materie- und
  Tachyon-Frame, wie die Federkopplung in `thm:spring` der Originalarbeit. Die Higgs-Quantenzahlen tragen genau diese Kopplungen.
- H29e bestätigt ⇒ Die Massenaufspaltung verlangt die Brechung der Spiegelung ρ (der Frame-Triole) auf den Plätzen, die Mischung die Brechung
  der Triality τ. Woher diese Brechungen kommen, ist damit nicht gesagt.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
