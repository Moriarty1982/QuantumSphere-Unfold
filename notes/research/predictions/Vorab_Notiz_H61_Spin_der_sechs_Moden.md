# Vorab-Notiz H61: Spin und Chiralität der 6 masselosen Moden

**Geschrieben und committet am 3. November 2026 vor der Rechnung. Status: vorregistriert.** Bekannt ist nur H60 (6 reelle Polarisationen je Nullrichtung). Spin, Chiralität und komplexe Struktur des Polarisationsraums sind noch nicht gerechnet.

## Annahme (Rahmen)
- Die 24 reellen Komponenten sind (Re, Im) von Ψ ∈ C³ ⊗ C⁴.
- Ψ besteht aus drei Dirac-Spinoren in der Dirac-Basis, denn α_k = [[0, σ_k], [σ_k, 0]] wie in k138.
- Die Lorentz-Wirkung im rekonstruierten Koframe ist I₃ ⊗ (Spin-½-Darstellung) mit
  - Σ_k = I₃ ⊗ diag(σ_k, σ_k),
  - γ₅ = I₃ ⊗ [[0, 1], [1, 0]],
  - der komplexen Struktur J (Multiplikation mit i).
- Der Koframe entsteht aus Q_a = S₃ ⊗ (1, α_a); das gilt nur innerhalb des Vergleichsmodells.

## Messung (k161)
Für 200 Nullrichtungen ξ wird der Polarisationsraum P(ξ) ⊂ R²⁴ aus g''_8 bestimmt (6-dimensional, wie in k160). Dazu kommen:
- ξ̂ = Vᵀξ mit ξ̂_0 > 0,
- der Impuls k^i = −ξ̂_i und die Richtung n = k/|k|,
- die Helizität h = n·Σ/2.

Bestimmt werden die Invarianzresiduen r_X = ‖(1 − Π_P) X Π_P‖ für X = J, γ₅, h sowie die Eigenwerte von Π_P X Π_P auf P.

## Hypothese H61 (Weyl-Typ)
- P ist invariant unter J, γ₅ und h.
- γ₅ hat auf P ein einziges Vorzeichen (alle sechs Eigenwerte gleich, +1 oder −1).
- h ist auf P konstant ±½, mit festem Vorzeichen über alle zeitorientierten Nullrichtungen.

Lesart bei Bestätigung: drei Weyl-Moden gleicher Chiralität. Das globale Vorzeichen von h hängt von der Konvention der ebenen Welle ab und wird nicht gedeutet.

## Entscheidung (Median über die Richtungen)
| Ergebnis | Bedingung |
|---|---|
| bestätigt | alle r_X ≤ 1e-6, γ₅ einheitlich auf P und h einheitlich ±½ |
| widerlegt | ein r_X ≥ 1e-3, oder γ₅ bzw. h hat auf P gemischte Vorzeichen bzw. Werte |
| ungültig | ein r_X liegt zwischen 1e-6 und 1e-3 |

Bei Widerlegung werden die gemessenen Strukturen beschrieben, zum Beispiel Majorana-artig (nicht J-invariant) oder gemischte Chiralität.
