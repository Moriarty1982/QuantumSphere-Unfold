# Vorab-Notiz H167: Skala als Setzung. Welche Terme legen die Phase δ fest, was bewirkt die Ladungsmischung, und wo tritt die Skala ein?

**Stand:** 26.11.2026, vor der Rechnung festgelegt. **Überwiegend nicht blind:** a, b, c stehen analytisch fest und sind von Hand überschlagen; für d2 ist
eine Zahl überschlagen (≈ 0,08). Blind ist nur d1. Anlass: Autor, 26.11.2026, 18:17 UTC: „man kann ja zuerst setzen und dann schauen was sich daraus ergibt,
vielleicht finden wir dann einen grund wieso es skalenfrei sei muss“. **Die Skala ist hier eine Setzung.** Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4.
Vergeben: H167, k362 (geprüft: frei; k360, k361 gehören zu H162).

## Vorwissen geprüft
- **H166** (`../delta_h166/`): δ ist der σ-ungerade Dipol; Ziel unter J ist δ* = 0,2222220471; offen ist Dipol gegen Quadrupol.
- **k282** (`../rueckwaerts/k282/README.md`): zwei quadratische Terme. Tr(W∘σW) = |d|² + 2[(1 − c²)(|s|² − |v|²) − 4c s·v] (Konjugation σ) und der Spin-1-Term
  d_v(1 + c²)|v|² (trennt Spin 1 von Spin 2). Für c = 0 fallen sie zusammen. Vorzeichen frei.
- **k278** (`../rueckwaerts/k278/README.md`): Ladungsmischung a (hier c), Eintrag (−a + i)v; „Prüfen, ob r42 die Ladungsmischung a festlegt“ ist dort offen;
  der Projektor ½(1 + iL_e₇) aus r42 gäbe a = 1.
- **H128** (`../kollaps_h128/`): Die algebraweite Massenform trennt Spin 1 und Spin 2 im Verhältnis 9/10 (u = e₇); Vorzeichen offen bis zur Feldgleichung.
- **H155, H157, H158** (`../generationszahl_h138/`): Skala als Setzung; unter J nur gerade Ordnungen; J-erlaubt bei Ordnung 2 nur die Norm, bei Ordnung 4
  zusätzlich φ²r² cos 2δ und sin 2δ, bei Ordnung 6 cos δ, cos 3δ. H158e: c dreht nur die Phase; H158d nachträglich: Ordnung 4 mit σ gibt δ = 0 oder π/2.
- **H101, H103, r12** (`../../predictions/`): Oktant δ = π/12, masseloses Elektron; kein Mechanismus hebt es, ohne K zu brechen.
- **Feldgleichung** (`../feldgleichung/README.md`): rekursiver Ansatz, Vorzeichen frei; H150: skalenfrei gibt es das Koide-Kondensat nur für κ < 0.
- Suche nach „cos 2(δ − χ)“, „Spin-1-Term“ zusammen mit „Oktant“ in `notes/`, `wiki/`: kein Vorbefund, dass der Spin-1-Term mit c = 1 den Oktanten gibt.

**Suchrichtung:** rückwärts von H166: gesucht ist ein σ-ungerader Beitrag. Die Algebra hat ihn schon, sobald c ≠ 0 ist: Der Spin-1-Term ist dann gegen
die Konjugation σ verdreht. **Werkzeugwahl:** Python (sympy, numpy/scipy), Wolfram unabhängig für die symbolischen Teile und die Zahlen. Qiskit nicht geeignet.

## Aufbau (k362, `k362_test_h167.py`; Gegenprobe `k362b_gegenprobe.wl`)
Zirkulantensektor W = a + zS + z̄S², z = r e^{iδ} = (1 + ic)(s + iv), χ = arctan c. Ebenen-Lesart des Postulats J wie H157/H158: A = a, B = √2 r, Tausch A ↔ B.
- Konjugationsterm: T_σ = Re z² = r² cos 2δ. Spin-1-Term: T_v = (1 + c²)v² = r² sin²(δ − χ), also bis auf Konstante −½ r² cos 2(δ − χ).
- Potential mit gesetzter Skala: V = V₀(A, B) + α·T_σ·f + α′·(−cos 2(δ − χ))·r²·f, mit f = 1 (quadratisch, Skala m²) oder f = A² (Ordnung 4, J-symmetrisch).
- Ordnung 6 (nur mit Skala Λ): (A³B³/Λ²)(β₃ cos 3δ + β₁ cos δ).

## Hypothesen und Kriterien
- **H167a (nicht blind, exakt):** Auf festem r ist V_δ = r²[α cos 2δ − α′ cos 2(δ − χ)] = R cos(2δ − 2δ₀); Minima bei δ₀ + π/2 und δ₀ + 3π/2. Sonderfälle:
  α′ = 0 gibt δ ∈ {0, π/6} (gefaltet), für jedes c. α = 0 gibt δ ∈ χ + {0, π/2}; **für c = 1 sind das gefaltet π/12 und π/4, also der Oktant** (det W = 0 bei
  K = ⅔, masseloses Elektron) und sein Partner. Kriterium: symbolische Nullreste, Python und Wolfram.
- **H167b (nicht blind, exakt): Wo die Skala eintritt.** (i) Die quadratischen Terme sind nicht J-symmetrisch; ihre J-symmetrischen Fassungen haben Ordnung 4 und
  sind dimensionslos. Unter J legt also kein Term mit Skala δ fest. (ii) Bis Ordnung 4 ist V gerade in A; die beiden Minima δ₀ + π/2 und δ₀ + 3π/2 sind exakt
  entartet, haben aber verschiedene Spektren. Erst Ordnung 6, also die Skala Λ, wählt zwischen ihnen. Kriterium: symbolisch; numerische Kontrolle am vollen
  V(A, B, δ) mit V₀ = μ²(A² + B²) + λ(A⁴ + B⁴) + κA²B², μ² < 0, λ = 1, κ = 0,5: K = ⅔ auf 10⁻⁹, δ wie in a auf 10⁻⁷.
- **H167c (nicht blind): Elektronmasse als Maß des Konjugationsterms.** Für c = 1 und |α/α′| ≪ 1 gilt nahe dem Oktanten δ − π/12 ∝ α/α′ und m_e/m_τ ∝ (α/α′)².
  Kriterium: Exponent 2,00 ± 0,05 aus einer Anpassung über α/α′ ∈ [10⁻³, 10⁻²].
- **H167d (Zielwert für das Verhältnis):** Für c = 1 die Verhältnisse ρ = α/α′ bestimmen, bei denen ein Minimum gefaltet bei δ* liegt (alle Zweige).
  - **d2 (nicht blind, überschlagen):** Auf dem Oktant-Zweig ist |ρ*| ≈ 0,08. Kriterium: 0,05 < |ρ*| < 0,12.
  - **d1 (blind): Keine native Zahl trifft.** Liste L, vorab: 9/10, 10/9, 1/10, 1/9, 1/19 (aus H128: (10 − 9)/(10 + 9)), 1/2, 2, 1/3, 2/3, 2/9, 1/√2, √2, 1/√3, √3,
    β_sym = 0,5494056410, β_sym², ε₀ = artanh β_sym, γ_M = 0,237533, γ_M/2, 1/(4π), α_em = 1/137,035999, jeweils mit beiden Vorzeichen (42 Kandidaten), gegen alle
    Zielverhältnisse. Treffer, wenn relativ näher als 10⁻⁴. **Vorhersage: kein Treffer.** Zufallserwartung < 0,05.
- **Kontrolle zu c:** Ohne Konjugationsterm (α = 0) verlangt δ* die Mischung c* = tan(δ* + π/6) oder ihren Kehrwert. Gesehen vor der Rechnung:
  c* ≈ 0,92382 liegt nahe cos(π/8) = 0,92388. Das wird nur berichtet (Abstand in δ), nicht als Treffer gezählt.

## Folge, vorab festgelegt
- a und b bestätigt: Der σ-ungerade Beitrag aus H166 ist die Verdrehung χ des Spin-1-Terms gegen die Konjugation. Mit c = 1 (Projektor-Lesart, **offen seit k278,
  hier eine Setzung**) gibt der Spin-1-Term allein den Oktanten. Die Phase wird von dimensionslosen Termen festgelegt; die Skala wählt nur den Zweig. Das wäre ein
  Hinweis, kein Beweis, dass die Phase skalenfrei bestimmt ist.
- c bestätigt: Die Elektronmasse misst das Verhältnis von Konjugations- zu Spin-1-Term. Das ersetzt den Fit R* aus H155 durch einen anderen Parameter ρ*;
  es ist keine Herleitung, solange ρ* nicht folgt.
- d1 ohne Treffer: ρ* bleibt offen. Mit Treffer: eigener Test mit Vorhersage für m_τ nötig.
- Kein Vorzeichen wird gesetzt (beide gerechnet); kein Guard berührt; OP3 und OP4 bleiben offen.
