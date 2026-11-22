# Optische Materialmode als Vermittler des OP5-Falls: trägt teilweise (Erkundung, nicht blind, 22.11.2026)

**Ergebnis in einem Satz:** Die optische Mode einer einachsig präparierten Zweikomponenten-Probe liefert für den Higgs-Radialmodus einen
gerichteten, massiven Vermittlerterm mit Lücke ω₀² und Gewicht μ(Y₁/ρ₁ − Y₂/ρ₂)², der nur vom Querimpuls a_⊥ abhängt. Die
Ausbreitungsgeschwindigkeit r_m wird dafür nicht gebraucht. Der Zähler ist aber a_⊥ statt ⅔a_⊥² wie im Vergleichsmodell: Das Material
gibt die Form f = Δ_⊥H/m² der induzierten Quelle, nicht die Rückwirkung g_m²Δ_⊥f. **Nach dem vorab festgelegten Raster: trägt teilweise.**

Auftrag des Autors: „Weg A: Material“. Verfahren vorab: `Methoden_Notiz.md` (Commit a86479e0). Skript `material_mediator.wl`, Ausgabe
`run/material_mediator.txt`, Wolfram exakt. Keine H-Nummer.

## Ergebnis
| Schritt | Befund |
|---|---|
| (1) isotrop | Effektiver Operator 2(m_H² + q − x) + q Yᵀ M⁻¹ Y. Optischer Pol bei ω₀² = k(ρ₁+ρ₂)/(ρ₁ρ₂), Residuum q·μ(Y₁/ρ₁ − Y₂/ρ₂)² mit μ = ρ₁ρ₂/(ρ₁+ρ₂); akustischer Pol mit Residuum q(Y₁+Y₂)²/(ρ₁+ρ₂). Isotrop, also kein gerichteter Term. |
| (2) r_m | Statisch g_m²N_m/d_m = ⅔g_m²a_⊥²/m² − ⅔g_m²r_m a_⊥² q/m⁴ + …: Das führende Glied, aus dem r32.4 den Kontrast gewinnt, hängt nicht von r_m ab. Die Unterluminalität (V2) wird für den führenden Kontrast nicht gebraucht. |
| (3) einachsig | Paarfeder längs der Achse starr, quer k_⊥: Längs bleibt nur der akustische Pol, quer der optische mit Residuum a_⊥·μ(Y₁/ρ₁ − Y₂/ρ₂)². Der Term hängt nur von a_⊥ ab: gerichtet. |
| (4) Form | Statisch induzierte Quelle −a_⊥μ(Y₁/ρ₁ − Y₂/ρ₂)²/ω₀² · η, also die Form Δ_⊥η/ω₀² von f in r32.4 mit m² ↔ ω₀². Im Vergleichsmodell steht im Operator g_m²Δ_⊥f, eine Potenz a_⊥ mehr. |
| Kopplung | Mit Y_a = f_aρ_a/v (f_a Higgs-Anteil der Ruhemasse) wird das Gewicht μ(f₁ − f₂)²/v²: Es koppelt nur, wenn die beiden Komponenten verschieden große Higgs-Anteile ihrer Masse haben. |

## Lesart
- Weg A trägt den gerichteten Kontrast in der Form, nicht in der Potenz. Ein Material mit Dichtekopplung kann den Zähler a_⊥² nicht liefern;
  dafür bräuchte es eine Kopplung an zweite Ableitungen der Verschiebung, die gegenüber der Dichtekopplung um (Gitterabstand × Impuls)²
  unterdrückt wäre (Abschätzung, nicht gerechnet).
- Gewonnen ist: Masse = optische Lücke, Richtung = einachsige Präparation, Kopplung = Unterschied der Higgs-Massenanteile. Alle drei sind
  Eigenschaften der Probe und lassen sich unabhängig variieren; die Unterluminalität ist für das führende Glied entbehrlich.
- Ehrlich offen: welche Potenz die OP5-Auslese tatsächlich misst (r32.4 liest f aus, nicht die Rückwirkung auf H), und die Größe von
  f₁ − f₂ (keine Zahlen eingesetzt). OP5 und H96 bleiben offen.
