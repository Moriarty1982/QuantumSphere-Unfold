# Vorab H244 (k461): Folgt die Belegung (2/3, 1/6, 1/6) von Baum und v₀ aus der Kopien-Regel H242?

**Datum:** 2026-11-28, vor der Rechnung committet. **Anlass:** Marc (20:55): „ja“ zum Vorschlag aus H243.

## Vorwissen geprüft
- **H243/k460:** In der Ladungsbasis (T-Eigenbasis t_k) hat der Baum N̂(π/6) die Klassenanteile (2/3, 1/6, 1/6), ebenso die feste Spalte
  v₀ = (1,0,1)/√2. Die θ₁₃-Richtungen sind rein geladen (0, ½, ½).
- **H242/k458:** Kopien-Belegungen (g₁, g₂, g₃) ∈ ℤ₃³ schließen genau bei g₁+g₂+g₃ ≡ 0 (mod 3), das sind 9 von 27.
- **H173:** TM1-Baum bei δ_ν = π/6 mit b = 0, c = −√(3/2). **H205:** v₀ ist Eigenvektor für jedes b, c.
- **k262:** ℤ₃-Träger, Majorana ⇒ TM1.

## Größen (gesetzt)
- Mit e₂ ↦ −e₂ wird T zur zyklischen Permutation; die Ladungsbasis ist dann die diskrete Fourier-Basis. Kopie j ↔ Flavour-Position j
  (Lesart, Generationen sind nach H242 nicht gezeigt).
- **Belegungsvektor:** z = (z₀, z₁, z₂) mit z_j ∈ {0} ∪ {ω^g}, normiert (Kopie leer oder mit ℤ₃-Phase besetzt). 63 nicht leere Muster.
- **Schluss einer Belegung:** Summe der g über die besetzten Kopien ≡ 0 (mod 3), wie H242. Zusätzlich die phaseninvariante Fassung
  „schließt nach einer gemeinsamen Drehung g ↦ g + h“.
- Klassenanteile W_k = |⟨t_k, z⟩|².

## Hypothese
Die Belegung (2/3, 1/6, 1/6) folgt aus der Kopien-Regel: genau die schließenden Belegungen tragen sie, und der Baum erreicht sie nur bei δ_ν = π/6.

## Kriterien
- **A (nicht blind, vorab analytisch überlegt):** Jede schließende Vollbelegung (alle drei besetzt) ist rein: Anteil 1 in einer Klasse. Ihr
  Mittel über die 9 Belegungen ist (1/3, 1/3, 1/3). Erwartet: weder eine einzelne noch das Mittel gibt (2/3, 1/6, 1/6).
- **B (teilweise nicht blind):** Menge M der Muster mit W = (2/3, 1/6, 1/6) in dieser Reihenfolge gegen die Menge S der schließenden Muster.
  Vorab überlegt: Zweierbelegungen mit gleicher Phase geben diese Anteile. Das Ergebnis der Rechnung über alle 63 Muster ist nicht vorab
  festgestellt. **B gilt**, wenn M = S (beide Fassungen werden berichtet, gewertet wird die H242-Fassung).
- **C (blind):** W₀(N̂(δ_ν)) für δ_ν ∈ [0, π/3] auf dem Zweig b ≥ 0 (b reell). **C gilt**, wenn W₀ = 2/3 (auf 10⁻¹⁰) nur bei δ_ν = π/6 erreicht wird.
- **Urteil:**
  - **trägt:** B und C.
  - **trägt teilweise:** genau eines.
  - **widerlegt:** keines.
- **Nur Bericht:** W₀(c) als geschlossene Formel; Anteile von Mustern mit ℤ₆-Phasen (Vorzeichen), etwa (1,0,−1).

## Werkzeuge
Python k461, Wolfram k461b (exakt: Muster, W₀(c), C). Qiskit nicht einschlägig.
