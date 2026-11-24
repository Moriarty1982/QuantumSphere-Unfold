# r13 neu gelesen: Ist der S₃-Zyklus doch ein Generationsschritt? (Erkundung k255, nicht blind, 24.11.2026)

**Ergebnis in einem Satz:** Das r13-Ergebnis („Zyklus unter der Ladung nur Phase“) ist nicht allgemein zwingend. Es gilt in der Eigenbasis
des Zyklus und unter einer gemeinsamen Ladung auf ℂ⊗𝕊. In der Basis der drei Oktonionen-Kopien ist derselbe Operator eine echte
Vertauschung dreier orthonormaler Zustände. Diese liegen je in einer Kopie unter dem magischen Winkel zur reellen Eins, und die
Koide-Beziehung K = ⅔ folgt dort exakt, wenn der Zustand die Form exp(uπ/4) hat. **Die Grenze bleibt:** Die drei Kopien können in ℂ⊗𝕊 keine
gemeinsamen Ladungen tragen. Ihre Kopienladungen vertauschen nicht, und ihr Mittel ist ½·𝟙. Die Sedenionen liefern also das
Generations-*Etikett* und die Mischgeometrie, nicht den Teilcheninhalt dreier Generationen.

Auftrag des Autors (24.11.2026): „prüfen wir das weiter, sieh dir r13 nochmal mit dem jetzigen wissen an“; Anschluss an k253/k254.
**Erkundung, nicht blind:** Die Darstellungstheorie (Permutationsdarstellung von S₃ = 1 ⊕ 2, diskrete Fourier-Transformation,
Brannen-Form) ist Standard. Keine H-Nummer. Vergeben: Skripte **k255** (k255, k255b, k255c, k255d).

Werkzeuge: Python (numpy) für die Sedenion-Rechnungen (k255, k255c, k255d); Wolfram Language exakt für Generationsbasis und Koide (k255b).
Qiskit nicht eingesetzt (kein Messablauf).

## Vorwissen geprüft
- r13 und Notizen: `op3_sedenion_reference_2026_11_13.md`, `op3_sedenion_charge_2026_11_13.md` (Bedingungen N1–N3, Q_* mit Ladungsachse
  e₈ einzig im farbneutralen Block; „keine Fortsetzung mit Q|_O = Q8 vertauscht mit ψ“; Bezug unter dem magischen Winkel nicht nativ),
  `op3_sedenion_generations_estar_2026_11_14.md` (zwei Generationen; ψ-Sektoren sind keine Generationen; ψ ist Phase).
- K28 (𝕊 = (1,1) ⊕ (1,sgn) ⊕ (7,2)); k85 (Q8 = ½ − (i/6)L_e7 − (i/3)R_e7, eine Generation auf ℂ⊗𝕆).
- k254 (S₃ exakt, drei Oktonionen-Kopien, Bott-Periode), k253 (Berry-Phase −Ω/2 bei HS(2)), k246 (größter Formzyklus = halbe Drehung),
  H123 (Bargmann 1/4 + i/4, Phase π/4), H125 Stufe A (Projektdateien und PR #278: Leptonen nur mit det −1, Quarks nur mit det +1).
- Wiki Gesamtbild: Koide K = ⅔ als mittlere quadratische Überlappung ρ² = ½ (r12).

## Ergebnisse
1. **Warum r13 eine Phase fand (k255).** Die 120°-Drehung ψ hält e₈ fest und vertauscht mit L_{e₈} exakt. Die r13-Ladungsachse e₈ liegt im
   S₃-invarianten Teil. Jede Ladung über e₈ vertauscht deshalb mit ψ, und ψ kann nur Phasen zwischen Ladungssektoren geben.
2. **Dieselbe Abbildung als Vertauschung (k255, k255b).** ψ bildet die Kopien zyklisch aufeinander ab (P₀ → P₁₂₀ → P₂₄₀, Fehler 10⁻¹⁶).
   Für jede imaginäre Oktonion-Richtung w trägt V_w = span{1, w⊗f₁, w⊗f₂} die Permutationsdarstellung 1 ⊕ 2 von S₃. Darin bilden
   g_k = 1/√3 + √(2/3)·w⊗f_k (f_k bei 0°, 120°, 240°) eine **Orthonormalbasis** (Gram = 𝟙, Wolfram exakt), mit ψg_k = g_{k+1}. Jedes g_k liegt
   in der Kopie O_k (Abstand 10⁻¹⁶, k255c) und **unter dem magischen Winkel** zur reellen Eins (cos² = ⅓, 54,7356°). In der Eigenbasis ist
   derselbe ψ diag(1, ω, ω̄), also genau die Phase aus r13. **Ob ψ „Schritt“ oder „Phase“ ist, entscheidet die Wahl der Basis.**
   Der fehlende „Bezug unter dem magischen Winkel“ aus r13 ist hier nativ: Es sind die Generationszustände selbst.
3. **Koide exakt (k255b).** Ein Zustand Ψ = α·1 + β·w⊗n(δ) hat in dieser Basis die Amplituden c_k = (α + √2 β cos(δ − 2πk/3))/√3, also
   K = (α² + β²)/(3α²). **K = ⅔ genau für β = α**, dann ist c_k ∝ 1 + √2 cos(δ − 2πk/3) (Brannen-Form). Normiert heißt β = α:
   Ψ = (1 + u)/√2 = exp(uπ/4), also eine Achteldrehung von der Eins weg, Realteil und Imaginärteil gleich schwer. Das ist ρ² = ½ aus r12,
   und π/4 ist die Phase des Oktant-Tripels (H123). Der Winkel δ ist die Richtung von u in der Kopienebene.
4. **δ ist nicht festgelegt (k255).** Nur bei θ = 0°, 60°, 120°, … ist O_θ = span{1, cos θ e_i + sin θ e_{i+8}} eine Unteralgebra (Abweichung
   10⁻¹⁶; sonst 0,5 bis 1,0). Die Symmetrie erlaubt nur 120°-Schritte von δ. Der Koide-Wert δ ≈ 2/9 müsste aus Dynamik oder Holonomie kommen
   und ist nicht hergeleitet. Die Holonomie k246 (−π) und die Berry-Phase −Ω/2 legen ihn ohne weitere Setzung nicht fest.
5. **Die Spiegelungen sind ladungsumkehrend (k255c).** Die drei Spiegelungen von S₃ (det M = −1, e₈ ↦ −e₈) kehren L_{e₈} exakt um, die
   Drehungen lassen es fest. S₃ = ℤ₃ (Generationszyklus) ⋊ ℤ₂ (Umkehr der Ladungsachse). Das passt zur Struktur von H125 (Leptonen det −1,
   Quarks det +1). Ob die ℤ₂ das relative CP-Vorzeichen ist, ist nicht gerechnet; Stufe A von H125 bleibt maßgeblich.
6. **Die Grenze: Ladungen der Kopien (k255d).** Q_S (k85-Form über e₇) gibt auf ℂ⊗O₀ genau eine Generation (0, ⅓³, ⅔³, 1). Die Kopienladungen
   Q^(k) = ψ^k Q_S ψ^{-k} vertauschen aber nicht miteinander ([Q⁽⁰⁾, Q⁽¹⁾] = 0,24), und ihr Mittel ist exakt ½·𝟙. Damit hat es keine Ladungsstruktur
   mehr. In ℂ⊗𝕊 (16 komplexe Zustände) passen drei Generationen (24) ohnehin nicht. Die drei Kopien überlappen: Sie sind ein straffer Rahmen
   (Σ P_Im = 3/2·𝟙, Hauptwinkel 60°).
7. **Lecks und Kopplung zwischen Kopien (k255).** Elemente w⊗n vom Rang 1 (jede Richtung n) sind nie Nullteiler (kleinster Singulärwert
   = |a|). Nullteiler sind „verschränkt“ (Rang 2 in 7 ⊗ ℝ², z. B. e₁ + e₁₀). Die Lecks liegen also zwischen den Kopien, nicht in ihnen.
   Ein Produkt aus Kopie 0 und Kopie 120 fällt überwiegend in die dritte Kopie (Projektionsanteil 0,87) mit Rest auf e₈ (0,10) und ℝ (0,03).
   Der Assoziator über drei Kopien ist groß (1,67): Die Kopplung zwischen Generationen ist nicht-assoziativ.

## Bewertung
- **r13 bleibt richtig, aber nicht zwingend.** Unter einer gemeinsamen Ladung auf ℂ⊗𝕊 (N1–N3, Achse e₈) ist ψ eine Phase. Liest man die
  Kopien als Generationen, ist ψ ein Schritt, der Bezug unter dem magischen Winkel ist nativ, und Koide folgt aus Ψ = exp(uπ/4).
- **Was diese Lesart nicht leistet:** gemeinsame Ladungen für drei Generationen in ℂ⊗𝕊 und den Wert von δ. Für den Teilcheninhalt braucht es
  drei orthogonale Träger. Das sind ℂ⊗(𝕆 ⊕ 𝕆 ⊕ 𝕆) (Weg B, Trialität) oder das Kopienregister höherer Stufen (HS(5) Vorder/Rück, k254
  Bott-Periode). Die Sedenionen würden dann die Mischgeometrie zwischen diesen Trägern festlegen.
- Prüfbar wäre (nur mit Vorab-Notiz, dann H-Nummer): ob die Mischgeometrie der Kopien (straffer Rahmen, Hauptwinkel 60°, nicht-assoziative
  Kopplung in die dritte Kopie) eine Mischungsmatrix vorhersagt, die nicht schon aus Koide folgt.
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert; kein Guard berührt. H125 unberührt (Stufe A eigenständig).
- Zurückgestellte Ideen: I1 (β_sym als Verhältnis zweier Zählungen) berührt am Rand (Verhältnis β/α = 1 bei Koide); kein neuer Auslöser.

## Dateien
`k255_kopien_generationen.py` (`k255_out.txt`), `k255b_generationen_koide.wl` (`k255b_out.txt`), `k255c_spiegelung_ladung.py`
(`k255c_out.txt`), `k255d_kopienladung.py` (`k255d_out.txt`). Aufruf aus diesem Ordner; die Skripte lesen `../k253_cayley_dickson_turm.py`.
