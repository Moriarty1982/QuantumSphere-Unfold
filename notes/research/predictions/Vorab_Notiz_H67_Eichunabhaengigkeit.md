# Vorab-Notiz H67: Sind Zahl und Lage der vier versteckten Bedingungen eichunabhängig?

**Geschrieben und committet am 4. November 2026 vor der Rechnung. Status: vorregistriert.**

## Vorwissen geprüft
Gesucht wurde in r72 (`k136_eichung.py`, Runde r72.1), r73, r77, r78 und predictions nach „Eichung / gauge / K2 / transversal“.
- r72.1(b): Die Eichung s = Ψ†K₂Ψ wurde gewählt, weil sie am Keim am stärksten transversal ist: |ds·v|/|ds| = 0.45.
- Transversal sind am Keim auch:
  - Ψ†Ψ = j⁰ (0.077),
  - j³ = Ψ†K₃Ψ (0.165),
  - Ψ†Q₃Ψ (0.256),
  - Ψ†(I⊗β)Ψ (0.023, ein Lorentz-Skalar),
  - j¹ (0.029).
  Nachgerechnet am 4.11. mit dem unveränderten Teil 2 von k136.
- r72.1(c): Auf Symbolebene ergibt jede transversale algebraische Eichung dasselbe g'_p ≅ g_p/(S^p ⊗ v). Das Symbol ist also eichunabhängig. Ob das auch für die versteckten Bedingungen gilt, hängt von den Termen niedrigerer Ordnung ab und ist nicht geprüft.
- H65(b): K₂ erhält nur so(1,2); Ψ†(I⊗β)Ψ ist lorentzinvariant.

## Messung (k167 = k159 mit wählbarer Eichung, auf GitHub-Runnern)
Gerechnet wird wie in H59 mit q = 6, je ein Job pro Eichmatrix M ∈ {K₂ (Kontrolle), K₀, K₃, Q₃, I⊗β}:
- Die Eichreihe ist w = 2(Re MΨ, Im MΨ), genommen aus den Taylor-Koeffizienten des Keims, sodass der Keim die Eichung von selbst erfüllt.
- Bestimmt wird die Faser F₆ = dim N₆ − Rang C.
- Danach folgen in float die Polarisationen im Faserraum: 100 Nullrichtungen auf q und 30 Richtungen außerhalb.

## Hypothese H67
Für alle vier Alternativen gilt:
- dim N₆ = 501 und Rang C = 24, also F₆ = 477 (20 Ω-Prolongationen und 4 Bedingungen);
- 6 Polarisationen auf dem Kegel und keine außerhalb.

Zahl und Lage der vier Bedingungen sind dann eichunabhängig, auch für die kovariante Eichung Ψ̄Ψ.

## Gültigkeit
- Die Kontrolle K₂ gibt 477 wie in H59.
- Die Gram-Lücke ist ≥ 1e20, die Newton-Residuen sind ≤ 1e-30.
- Bei den Polarisationen ist die Lücke ≥ 1e5.

## Entscheidung
| Ergebnis | Bedingung |
|---|---|
| bestätigt | alle vier Alternativen gültig mit 477 und 6 |
| widerlegt | eine gültige Alternative mit F₆ ≠ 477 oder Polarisationen ≠ 6. Die Bedingungen hängen dann von der Eichung ab; gemeldet wird je Eichung |
| ungültig | Kontrolle verfehlt; Alternativen mit ungültigen Lücken werden einzeln als ungültig gemeldet und zählen nicht |
