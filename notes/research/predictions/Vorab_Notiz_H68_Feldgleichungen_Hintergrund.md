# Vorab-Notiz H68: Erfüllt der Hintergrund A, h kovariante Feldgleichungen mit den drei Spinorblöcken als Quelle?

**Geschrieben und committet am 4. November 2026 vor der Rechnung. Status: vorregistriert.**

## Vorwissen geprüft
Gesucht wurde in `analysis/OP5_*`, `llm/Ergebnis_*`, `llm/Erkundung_*`, `llm/Vorab_Notiz_*` und `notes/research/predictions/` nach „Yang–Mills / Klein–Gordon / Yukawa / Maxwell / backreaction / self-consistent / Rückwirkung / Hintergrund“.
- `Erkundung_Fierz_Hintergrund.md` (k168): Alle drei Blöcke liegen im regulären Dirac-Sektor (β ≈ 0), strömen mit v = ±x/t, Spins entlang φ̂ = e_y. Der Vorschlag für H68 stammt von dort.
- `OP5_Boosted_Triad_And_Coframe_Feedback.md`: Ein anderer Ansatz (geboostete Triade, feste Verbindung ω = dx/t) ist als selbstkonsistente Lösung verworfen, weil der induzierte Koframe die Stromerhaltung bricht. Der gegebene Hintergrund A = M(t) dφ ist dort nicht geprüft.
- `OP5_Flat_Reference_Clock_And_Signals.md` §4: Ebene Wellen können keinen Koframe vom Rang 4 erzeugen. Betrifft nicht die Frage hier.
- `OP5_Massive_Affine_Branch.md`: Yukawa-Term mit Referenzvolumen in einem anderen Elternmodell; kein Test des gegebenen h.
- „Bereits beantwortet“ (Anleitung OP5): Die Herkunft von A, h ist ausdrücklich offen. Eine Prüfung von Feldgleichungen für A oder h mit Quellen aus Ψ liegt nicht vor.

## Was vorab analytisch bekannt ist (offen gelegt)
- A = M(t) dφ mit M(t) = (3/(2 cos 2θ))(cos θ·λ₄ − sin θ·λ₆), θ = ½ arcsin(t/2). Daraus F = M′(t) dt∧dφ; die Werte von A und F erzeugen die Algebra 𝔨 = span(λ₂, λ₄, λ₆) ≅ su(2), denn [λ₄, λ₆] = iλ₂. Y₃ ist λ₂ und liegt in 𝔨.
- In der vollen su(3) scheitert die Gleichung trivial: Die linke Seite liegt in 𝔨, die Quelle hat aber eine λ₃-Dichte |Ψ₀|² − |Ψ₁|² ≠ 0 (k168: 5,97 gegen 0,43). Der Test wird deshalb auf 𝔨 beschränkt; die Stromanteile außerhalb von 𝔨 werden nur berichtet.
- Im flachen Fall verlangt ν = t eine λ₂-Ladungsdichte ∝ [M, M′]/ρ², ν = φ einen Azimutstrom ∝ M″/ρ², sonst nichts.

## Messung (k169, Erkundungswerte nur aus dieser Rechnung)
Abgeschnittene Potenzreihen (k138) um den Keim, reparierter 4-Jet, Gleichungen bis Grad 2 (15 Taylor-Koeffizienten je Komponente).
- Metrik: g_μν = η_ab E^a_μ E^b_ν mit dem Koframe des Modells E^a_μ = Re(Ψ†Q_a D_μΨ), V = E⁻¹, √|g| = |det E|. Das ist die Metrik, in der F die Dirac-Gleichung ist.
- Konvention D = ∂ + iA: F_μν = ∂_μA_ν − ∂_νA_μ + i[A_μ, A_ν], L^ν = (1/√|g|)∂_μ(√|g| F^{μν}) + i[A_μ, F^{μν}].
- Farbstrom: j^ν_b = V^ν_a Ψ†(λ_b ⊗ K_a)Ψ = Ψ̄γ^ν(λ_b⊗1)Ψ; Komponente der linken Seite L^ν_b = tr(λ_b L^ν).
- Skalarquelle: s = Ψ†(Y⊗β)Ψ = Ψ̄(Y⊗1)Ψ (Ableitung des Yukawa-Terms nach h); □_g h = (1/√|g|)∂_μ(√|g| g^{μν}∂_ν h).
- Konstanten durch kleinste Quadrate über alle Koeffizienten; relatives Residuum r = ‖LHS − κ·Quelle‖/‖LHS‖.

## Hypothese H68
- **H68a (Yang–Mills):** L^ν_b = κ_A j^ν_b für b ∈ {2, 4, 6}, ν = 0…3, mit einem κ_A ≠ 0.
- **H68b (Klein–Gordon, masselos):** □_g h = κ_h s mit einem κ_h ≠ 0.
- **H68c (Klein–Gordon, massiv, nur wenn H68b scheitert):** □_g h + m² h = κ_h s mit zwei Konstanten.

## Kontrollen (Gültigkeit)
- Bianchi/Ladungserhaltung: (1/√|g|)∂_ν(√|g| L^ν) + i[A_ν, L^ν] = 0 identisch bis Grad 1, relativ ≤ 1e-9.
- Flaches □h aus den Reihen gegen sympy exakt, ≤ 1e-12.
- Keimresiduum R ≤ 1e-10 (wie r71).

## Entscheidung (je Teil)
| Ergebnis | Bedingung |
|---|---|
| bestätigt | r ≤ 1e-6 über alle Grade 0–2 und Konstante ≠ 0 |
| widerlegt | r ≥ 1e-2 |
| unentschieden | dazwischen; berichtet werden r je Grad |
| ungültig | eine Kontrolle verfehlt |

Zusätzlich berichtet (Erkundung, ohne Kriterium): dieselben Größen in der flachen Metrik η der Koordinaten (t, x, y, z) und die Stromanteile außerhalb von 𝔨. Grenze: Die höheren Jets hängen von der ϑ-Eichung ab (s = Ψ†K₂Ψ); bei einem Scheitern wird Grad 0 getrennt ausgewiesen.
