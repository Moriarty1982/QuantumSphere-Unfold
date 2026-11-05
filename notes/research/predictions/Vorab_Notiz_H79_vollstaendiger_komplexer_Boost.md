# Vorab-Notiz H79: Zweite Lesart mit vollständigem komplexem Boost (Spinor und Argument)

**Stand:** 5. November 2026, vor der Rechnung festgelegt. **Nicht blind:** Die Erwartungen folgen analytisch (Boost-Identität, Translations- und Spiegelungsinvarianz des Integrals); die Rechnung (sympy) macht sie nachprüfbar. Autor 21:17: alle drei Wege (Koordinatenabbildung, Variante 1, I1) möglich; begonnen wird mit dem günstigsten.

## Vorwissen geprüft
- H78 / k194: Mit ψ_T(x) = −iσ_zψ(x + δ) (nur Spinor gedreht, Argument nur verschoben) wird der Weyl-Operator anisotrop, quer zu n das γ-fache; ausgeschlossen.
- k174: Λ(iπ) = diag(−1, 1, 1, −1), Spinor exp(−(iπ/2)σ_n) = −iσ_n, Λ(iπ) = −R_n(π). Das ist der komplexe Boost mit Rapidität iπ (γ = cosh 2η ↦ −γ, F3).
- r81.6(b): Tachyon-Abbildung R = σ_y und Zeitumkehr T = σ_z fallen auf dem Dublett nur auf der Kompensatorachse zusammen; r51/r81: nicht verwechseln. Hier wirkt Λ(iπ) auf die Raumzeit-Koordinaten, nicht auf das Dublett; im flachen Raum fällt die Spiegelung des Arguments aus dem Wirkungsintegral heraus.
- Bestandsaufnahme der Wirkungsansätze: offene Stelle „welche Adjungierte“; r81 Entscheidung 2 (reelle Wirkung mit Dirac-Adjungierter, komplexe Lesart K parallel).
- H77: Lesart B; Kriterium K3 (Energie des Bildes entgegengesetzt).

## Aufbau
ψ_T(x) = S·ψ(Λx + δ) mit S = −iσ_z, Λ = Λ(iπ), L_T = −(Bild von ψ†)·σ̄^μ i∂_μ ψ_T (F3), Gewichte a, b.
- **H (hermitesch):** Bild von ψ† ist ψ†(Λx + δ)·S†.
- **K (holomorph):** Bild von ψ† ist ψ†(Λx + δ)·S (Fortsetzung der Identität S(θ)σ̄^μS(θ) = Λ(θ)^μ_ν σ̄^ν von reellem θ auf θ = iπ).
- Skalar: φ_T(x) = φ(Λx + δ), Lesart B.

## Hypothesen und Kriterien
- **H79a (holomorph):** S σ̄^μ S = Λ(iπ)^μ_ν σ̄^ν exakt. Damit ist L_T(x) = −L_M(Λx + δ), und die Wirkung ist (a − b)·S_M: isotrop (ω² = k²), für a > b Energie nach unten beschränkt (nach Dirac-See), keine T-Quanten, Energie des Bildes entgegengesetzt (K3 erfüllt).
- **H79b (hermitesch):** S†σ̄^μS = R^μ_ν σ̄^ν mit RΛ = −1; damit L_T(x) = +L_M(Λx + δ), Wirkung (a + b)·S_M: isotrop, aber der Beitrag des Bildes hat das Vorzeichen der Materie (K3 verletzt).
- **H79c (Skalar):** wie H78a, (a − b)·½X − (a + b)·V, weil X unter Λ invariant ist.
- **Bestätigt**, wenn die symbolische Rechnung die Identitäten und die Dispersion exakt liefert und die numerische Probe (Wirkung mit und ohne Spiegelung und Verschiebung des Arguments, periodisches Gitter) unter 10⁻¹² bleibt.

## Folge, vorab festgelegt
- Gilt H79a, ist Variante 2 mit vollständigem Boost und holomorpher Abbildung der Adjungierten isotrop, stabil (a > b), ohne Zerfall aus H76; Fermionen und Skalare haben dieselbe Kinetik-Gewichtung a − b. Die Wahl „holomorph“ ist dann eine Festlegung, die zur komplexen Lesart K passt, und als solche dem Autor vorzulegen.
- Massenterme (Dirac, Majorana) und FRW sind hier nicht geprüft.

Skript: `llm/k195_komplexer_boost.py` (nach dem Commit dieser Notiz).
