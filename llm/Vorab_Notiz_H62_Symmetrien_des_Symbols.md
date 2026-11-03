# Vorab-Notiz H62: enthält die Symmetrie-Algebra des Symbols eine Lorentz-Algebra?

**Geschrieben und committet am 3. November 2026 vor der Rechnung. Status: vorregistriert.** Bekannt sind der Lichtkegel q(ξ) = ξᵀQξ (k160) und, nach H61, dass die naive Spin-Zuordnung I₃ ⊗ Spin½ nicht trägt. Die Symmetrien des Symbols selbst sind noch nicht gerechnet.

## Messung (k162)
Gesucht ist die Stabilisator-Algebra 𝔰_p = {(A, B) ∈ gl(4) × gl(24) : X_{A,B} g''_p ⊂ g''_p}.
- Die Wirkung ist X_{A,B} = ρ_p(A) ⊗ 1 + 1 ⊗ B.
- ρ_p ist die von ξ ↦ Aξ induzierte Wirkung auf den Komponenten ξ^α/√α! der ebenen Wellen.
- Die Bedingung lautet (1 − Π)XΠ = 0. Sie ist linear in den 592 Unbekannten und wird zur Gram-Matrix 592 × 592 verdichtet.
- Gerechnet wird bei p = 6 (hochgenaue Basis), p = 7 und p = 8.
- Gemeldet werden dim 𝔰_p, dim des B-Anteils mit A = 0 (innere Symmetrien), die Projektion π_A(𝔰_p) und deren Schnitt mit so(Q) = {A : AᵀQ + QA = 0} (6-dimensional).
- Triviale Elemente sind (0, 1) und (1, 0) (Skalierung).

## Hypothese H62
π_A(𝔰_p) ⊇ so(Q), also dim(π_A(𝔰_p) ∩ so(Q)) = 6, bei p = 6, 7 und 8.

## Gültigkeit
- Die Gram-Eigenwerte haben am Kern eine Lücke ≥ 1e6.
- dim 𝔰_p ist für p = 6, 7, 8 gleich.

## Entscheidung
| Ergebnis | Bedingung |
|---|---|
| bestätigt | Schnitt = 6 bei allen drei p |
| widerlegt | Schnitt < 6 bei einem gültigen p |
| ungültig | Kriterien der Gültigkeit verletzt |

## Teil (b) bei Bestätigung (Verfahren vorab festgelegt, Wert ohne Vorhersage)
- Zu jeder Drehung A_n ∈ so(Q), die eine Nullrichtung ξ festhält, wird ein B_n aus 𝔰_8 bestimmt (bis auf innere Symmetrien).
- Gemeldet werden die Eigenwerte von B_n auf dem Polarisationsraum P(ξ), also die Helizitäten.
- Wenn die inneren Symmetrien P(ξ) nicht erhalten oder die Eigenwerte von der Wahl abhängen, wird das berichtet statt eines Spinwerts.
