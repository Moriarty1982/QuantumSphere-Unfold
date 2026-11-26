# Vorab-Notiz H156: Verlangt die Algebra gleiche Massenterme μ_A² = μ_B²?

**26.11.2026, vor jeder Rechnung committet.** Anlass: nach H155 (Skala als Setzung) und Autor „merge und push“, mit dem Auftrag, weiterzumachen mit der Frage, ob die
Algebra μ_A² = μ_B² verlangt. In H155 war das die einzige verbliebene Setzung für K = ⅔ (neben der Skala). Vorzeichen werden nicht gesetzt. Vergeben: H156, Skripte k339
(Python) und k339b (Wolfram). Qiskit nicht vorgesehen. Kein HDL/MMA-Vergleich.

## Vorwissen geprüft
- H155 (k338): mit μ_A² = μ_B², λ_A = λ_B liegt das Minimum bei θ = π/4; das Laufen mit n_B = 2 stört erst in zweiter Ordnung.
- H149a: ReΨ² = cos 2θ = φ² − |y|²; Tausch J: ψ ↦ Uψ̄, J² = 1, Fixpunkt π/4. H149c: ∂_θV|π/4 ∝ (2a − 2c + μ₀² − μ₁²), der tauschungerade Teil.
- k297: Der Tausch ist Rechtsmultiplikation mit der Einheit (μ → 1/μ), also der Wechsel Materie-Frame ↔ Tachyon-Frame (r23).
- H154b: die U(1) aus exp(αU) erhält V nur bei voller Norm (κ = 2λ), dort kein Koide-Kondensat (H150).

## Vorüberlegung (vor der Rechnung)
Quadratische Terme in Ψ, die die Algebra bereitstellt: die Norm N(Ψ) = φ² + |y|² und Re(Ψ²) = φ² − |y|² (tauschungerade); dazu (ReΨ)² = φ² = (N + ReΨ²)/2. Also
μ_A²A + μ_B²B = ½(μ_A² + μ_B²)N + ½(μ_A² − μ_B²)ReΨ². Gleiche Massen heißt: kein ReΨ²-Term. Die Frage ist, welche Symmetrie ReΨ² verbietet und was sie sonst noch erzwingt.

## Hypothesen und Kriterien
- **H156a (nicht blind, analytisch):** Die Automorphismen der Algebra (Konjugation in ℂ = {1, U}; für 𝕆 die Gruppe G₂, die den Realteil festhält) lassen ReΨ² und N
  beide invariant, verlangen also μ_A² = μ_B² nicht. *Kriterium:* symbolisch (Invarianz beider Formen unter Konjugation und einer G₂-Stichprobe).
- **H156b (gewertet):** Invariantentheorie in der Ebene {1, U} = (φ, y) für vier Kandidatengruppen, jeweils quadratische und quartische Invarianten:
  (i) SO(2) aus exp(αU); (ii) Z₄ aus Linksmultiplikation mit U; (iii) Z₂ aus J allein; (iv) D₄ = ⟨Linksmultiplikation mit U, Konjugation⟩.
  Vorhersage: (i) erzwingt μ_A² = μ_B² und κ = 2λ (kein Koide); (ii) erzwingt μ_A² = μ_B² und λ_A = λ_B, lässt aber einen tauschungeraden Quartikterm φy(φ² − y²) zu,
  der θ von π/4 schiebt; (iii) und (iv) erzwingen genau die Form aus H155 (gleiche Massen, gleiche λ, κ frei). *Kriterium:* Dimension und Basis der Invarianten;
  „geeignet“ heißt: erzwingt μ_A² = μ_B² und λ_A = λ_B, lässt κ frei und lässt keinen Term zu, der θ von π/4 schiebt.
- **H156c (gewertet):** Dynamik. Ist die Tauschlinie (μ_A² = μ_B², λ_A = λ_B) im Fluss ins Infrarote anziehend? Linearisierte Raten der tauschungeraden Abweichungen für
  n_B = 1 (Linie invariant) und n_B = 2 (Linie nicht invariant). *Kriterium:* Vorzeichen der Raten auf λ ∈ {0,05; 0,1; 0,2}, κ/λ ∈ {−1; −0,5; 0,5; 1}. Vorhersage:
  für n_B = 1 relativ anziehend, solange |κ| < 6λ (die relative Abweichung r = δλ/λ fällt wie dr/dt ∝ r(2κ² − 72λ²)/λ); für n_B = 2 erzeugt der Fluss die Abweichung
  selbst, die Linie ist dann kein Attraktor.
- **H156d (nicht blind, Lesart):** Ob J eine Symmetrie der Algebra ist. J = Konjugation gefolgt von Linksmultiplikation mit U ist eine Isometrie der Norm, aber kein
  Automorphismus (J(1)·J(1) = U² = −1 ≠ J(1) = U). *Kriterium:* symbolisch. Folgerung vorab: μ_A² = μ_B² folgt genau dann, wenn J als Symmetrie gefordert wird, und das
  ist nach k297 die Gleichberechtigung von Materie-Frame und Tachyon-Frame. Das wäre ein Postulat, keine Folgerung aus der Multiplikation.

## Grenzen
- Rechnung in der Ebene {1, U} (zwei reelle Felder) und im Modell (φ, y₁, y₂) wie H150–H155; die volle Wirkung von Linksmultiplikationen in 𝕆 bzw. 𝕊 führt aus dem
  Drei-Felder-Raum heraus und wird nur benannt.
- Eine Schleife, logarithmisches Laufen.
- OP3 offen; kein Vorzeichen gesetzt; kein Guard wird berührt.
