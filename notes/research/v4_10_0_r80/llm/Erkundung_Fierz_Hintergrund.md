# Erkundung: Fierz- und polare Größen des Hintergrunds am Keim (Route 1 der Literaturnotiz)

**4. November 2026. Status: Erkundung, ohne Kriterium.** Das ist der erste Schritt von Route 1 aus `analysis/OP5_Mathematical_Literature_Routes_2026-10-27.md`: vollständige polare bzw. Fierz-Variablen (Fabbri, arXiv:1707.03270) und die Übersetzung der Konventionen. Gerechnet hat `k168_fierz.py` in der Dirac-Basis wie k127, mit γ⁰ = β, γ^i = βα_i, γ₅ = [[0,1],[1,0]].

## Vorwissen geprüft
- Gesucht wurde nach „Fabbri / polar / Takabayasi / Fierz / counterflow“ in `analysis/OP5_*`.
- Die Counterflow-Serie (`OP5_Counterflow_*`, `OP5_Boosted_Triad_*`) baut den Hintergrund als geboostete Triade: A = cos θ·U, B = sin θ·U, C = W, θ = ½ arcsin(8t/N), Gesamtstrom J^a = (8t, −8x/3, −8y/3, −8z/3).
- Die Literaturnotiz empfiehlt die polare Zerlegung als ersten Schritt.
- Eine Fierz-Auswertung des 70-stelligen Keims liegt noch nicht vor.

## Werte am Keim (t, x, y, z) = (1, 0,6, 0, 0); die Azimutrichtung φ̂ = e_y
| Block | φ² | Yvon–Takabayasi-Winkel β | u^a = J/φ² | s^a = K/φ² |
|---|---|---|---|---|
| 0 | 5,97 | −0,02° | γ(1, +0,600, 0, 0), γ = 1,250 | (0, 0, +1, 0) |
| 1 | 0,43 | −0,07° | γ(1, +0,598, 0, 0) | (0, 0, +1, 0) |
| 2 | 6,38 | +0,01° | γ(1, −0,600, 0, 0) | (0, 0, −1, 0) |

- Die Fierz-Identitäten gelten auf 1e-14: J² = Φ² + Θ² = −K² und J·K = 0.
- Der Kreuzstrom j_S = Re(A†K^aB), aus dem der Koframe gebaut wird, ist zeitartig (j_S² = 2,54) und läuft mit +0,6.

## Lesart
- **Alle drei Blöcke liegen im regulären Dirac-Sektor mit β ≈ 0.** Die Pseudoskalardichte verschwindet praktisch.
- **Die Blöcke sind drei Spinorflüssigkeiten in einer Hubble-artigen Strömung v = ±x/t.**
  - Die Blöcke 0 und 1 laufen mit v = +x/t (γ = 1/√(1 − 0,36) = 1,25).
  - Block 2 läuft mit v = −x/t entgegen. Das ist der Counterflow der früheren Serie.
- **Alle Spins zeigen entlang der Azimutrichtung φ̂ = e_y,** bei den Blöcken 0 und 1 parallel, bei Block 2 antiparallel. Dieselbe Richtung zeichnen aus:
  - die Eichung (K₂ = α_y, H65(b): Stabilisator so(1,2) von e_y);
  - der Hintergrund-Zusammenhang A = M(t) dφ.
- Die nicht-kovariante Eichung legt also die Stromkomponente entlang φ̂ fest, die Achse, die auch der Hintergrund auszeichnet.
- Physikalisch ähnelt das einer spinpolarisierten, wirbelartigen relativistischen Strömung. Das ist eine Lesart, keine Herleitung.

## Nächster Schritt (Vorschlag)
Für A und h sind kovariante Feldgleichungen zu suchen, deren Quellen die Ströme der drei Blöcke sind:
- Yang–Mills für den Farbzusammenhang: A ist reell symmetrisch in den Farbindizes (0, 2) und (1, 2), also vom Typ Gell-Mann λ₄, λ₆. Die Quelle wäre Ψ̄γ^μ(T ⊗ 1)Ψ.
- Eine Yukawa- bzw. Klein–Gordon-Gleichung für h mit der Quelle Ψ̄(Y ⊗ β)Ψ.

Getestet wird, ob der vorgegebene Hintergrund diese Gleichungen mit einer einzigen Kopplungskonstanten erfüllt. Das wäre H68, vorab festzulegen.
