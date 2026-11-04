# Ergebnis H68: Der Hintergrund A, h erfüllt keine Feldgleichungen mit den Spinorblöcken als Quelle

**4. November 2026. Vorab-Notiz `Vorab_Notiz_H68_Feldgleichungen_Hintergrund.md` (Commit 4d10b0f). Skript `k169_feldgleichungen.py`, Ausgabe `k169_out.json`. Status: H68a und H68b widerlegt, H68c widerlegt.**

## Kontrollen (alle gültig)
- Bianchi/Ladungserhaltung der linken Seite bis Grad 1: relativ 1,2e-14 (Koframe-Metrik), 4,4e-16 (flach).
- Flaches □h aus den Reihen −6,344838895781823 gegen sympy exakt −6,344838895781825.
- Keimresiduum R ≤ 2,8e-13.

## Ergebnis in der Koframe-Metrik g = Eᵀ η E (Kriterium)
| Teil | Konstante (Fit) | relatives Residuum r | Entscheidung |
|---|---|---|---|
| H68a Yang–Mills auf 𝔨 = span(λ₂, λ₄, λ₆) | κ_A = 0,668 (Grad 0 allein 22,4; Grad 1: 0,118; Grad 2: 0,682) | 0,955 (je Grad 0,965 / 0,963 / 0,954) | widerlegt |
| H68b Klein–Gordon masselos | κ_h = −3,13 | 0,995 | widerlegt |
| H68c Klein–Gordon massiv | m² = −28,4, κ_h = −3,30 | 0,826 | widerlegt |

## Warum es scheitert
- **Die Quellen sind am Keim um rund drei Größenordnungen zu klein.** Die 𝔨-Ströme haben Komponenten ≈ 1e-3; die linke Seite ist O(0,1–0,4) in der Koframe-Metrik und O(3–5) flach. Ebenso die Skalarquelle: s = Ψ†(Y⊗β)Ψ = 0,002 gegen □_g h = 6,91 (flach −6,34).
- **Auch die Richtungen passen nicht.** Bei Grad 0 hat die linke Seite in jedem Generator eine andere Komponentenverteilung als der Strom; die Fits je Grad geben κ zwischen 0,12 und 22.
- **Die Spinorströme liegen fast ganz außerhalb von 𝔨:** Normen der Reihen bis Grad 2 in der Koframe-Metrik λ₀ 525, λ₈ 504, λ₅ 180, λ₃ 160, λ₇ 116, λ₁ 77, gegen ≈ 0,01 in 𝔨. Die Blöcke sind gegenüber den nichtdiagonalen Generatoren λ₂, λ₄, λ₆ praktisch inkohärent.

## Flache Metrik (Erkundung)
- Die analytische Struktur bestätigt sich: L hat nur die Komponenten (ν = t, λ₂) = 4,81 und (ν = φ̂ = y, λ₄, λ₆) = −2,82, 2,48.
- Fits: Yang–Mills r = 0,9997, Klein–Gordon masselos r = 1,000, massiv r = 0,28 (m² = 26,1, κ_h = 0,098; zwei Konstanten an 15 Koeffizienten, kein Kriterium).

## Lesart
- Der vorgegebene Hintergrund ist **nicht** von den drei Spinorblöcken über Yang–Mills und Klein–Gordon mit einer Kopplung erzeugt, weder in der Koframe- noch in der flachen Metrik. Er bleibt eine Vorgabe von außen.
- Die Grenze der Vorab-Notiz greift nicht: Schon Grad 0 (eichunabhängig von den höheren Jets) scheitert mit r = 0,965.
- Offen bleibt, ob eine andere Quelle passt, etwa die diagonalen Farbströme (λ₃, λ₈), die die Blöcke tatsächlich tragen. Das verlangt aber einen Zusammenhang mit diagonalen Anteilen und damit einen anderen Hintergrund. Nicht nachträglich anpassen; nur mit neuer Vorab-Notiz.
