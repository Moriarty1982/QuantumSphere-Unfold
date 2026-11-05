# Vorab-Notiz H63: Ist der dynamische Teil F von J lorentzsymmetrisch?

**Geschrieben und committet am 4. November 2026 vor der Rechnung. Status: vorregistriert.**

Bekannt aus r71, Erkundung:
- Die Ebenen Π_k entstehen im G-Teil (k126).
- F vernichtet die Diffeo-Richtungen (k125).

Die zuerst erwogene Hypothese „Π₁ = span(Strom, Axialstrom)“ ist durch k122 schon verneint und wird nicht erneut getestet.

## Messung (k163)
J = `completed_first_symbol` (32 × 96) aus `completion-omega-witness.npz`. Die Zeilen 0–23 sind F, 24–27 sind G, 28–31 sind dg. Für einen Zeilenblock X wird die Stabilisator-Algebra gesucht:

{(A, B, C) : Σ_μ A_{μν} X_μ + X_ν B − C X_ν = 0 für ν = 0..3}

- A ∈ gl(4) wirkt auf ξ, B ∈ gl(24) auf die Felder, C auf die Gleichungen.
- Das System ist linear und wird über SVD gelöst.
- Gemeldet werden dim(π_A ∩ so(Q)), mit Q aus k160, für X = F, X = F+G und X = F+G+dg.

## Hypothese H63
- (a) X = F: dim(π_A ∩ so(Q)) = 6. Der dynamische Teil ist lorentzsymmetrisch, sobald Spin und Gleichungen mittransformiert werden.
- (b) X = F+G und X = F+G+dg: dim(π_A ∩ so(Q)) ≤ 1. Die Brechung sitzt im G-Teil.

## Gültigkeit
- Die Singulärwert-Lücke am Kern beträgt ≥ 1e6 in allen drei Fällen.
- so(Q) ist 6-dimensional.

## Entscheidung
| Ergebnis | Bedingung |
|---|---|
| bestätigt | (a) und (b) gelten |
| widerlegt | (a) < 6 (dann bricht schon F), oder (b) > 1 |
| ungültig | eine Lücke < 1e6 |

## Lesart bei Bestätigung (a)
Für die Rotationen in so(Q) werden die Kommutatoren der B gemeldet und mit der Spin-½-Wirkung I₃ ⊗ σ^{ab} verglichen (beschreibend, ohne Vorhersage).
