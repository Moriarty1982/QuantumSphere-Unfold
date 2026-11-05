# Erkundung: Bezugszustände bei gemeinsamer Rapidität (Autorhinweis „Grenzwert statt Extremwerte“, k182)

**5. November 2026. Status: Erkundung mit analytischer Herleitung und numerischer Prüfung, ohne Kriterium.**

## Anlass
In H73 standen die Moden bei η = 0 (Ruhe, Schwelle), die Gewichte kamen aber von η_sym (x = tanh²η_sym). Das ist inkonsistent. Der Autor fragt, was bei einem Grenzwert statt der Extremwerte herauskommt.

## Konsistente Familie
- Materie (V1): k = m sinh η, ω = m cosh η, Gewicht p₊ = 1/(1 + t²).
- Tachyon (V2, λ = +1) als Fortsetzung η → η + iπ/2: k = m cosh η, ω = m sinh η, Gewicht p₋ = t²/(1 + t²), mit t = tanh η.
- Isotrop gemittelt, Feldnorm. Pro Mode gilt ρ_B = ω, p_B = k²/(3ω); ρ_A = −ω²/k, p_A = −k/3 (aus k179/k181).
- Grenzfall η → 0: Ruhe und Schwelle, die Extremwerte aus H73.

## Ergebnis (analytisch, numerisch auf ≤ 2e-15 bestätigt)
| Lesart | ρ | p | w |
|---|---|---|---|
| Materie-Frame-Gewichte (p₊ auf Materie) | m / cosh η | **0 exakt** | **0 (Staub)** |
| Tachyon-Frame-Gewichte (vertauscht) | **0 exakt** | −m / (3 cosh η) | reine Spannung |
| Summe beider Lesarten | m / cosh η | −m / (3 cosh η) | −⅓ |

Herleitung des Materie-Falls: p ∝ p₊·sinh²η/(3cosh η) − p₋·cosh η/3 = sinh²η/(3cosh η)·(p₊ − p₋·cosh²η/sinh²η) = 0, weil p₋/p₊ = tanh²η.

## Lesart
- **Mit konsistenter Rapidität ist die M–T-Mischung im Materie-Frame druckloser Staub**, und zwar für jedes η, nicht nur im Grenzfall. Ihre Energiedichte ist m/cosh η. Bei η_sym = 0,6174 ist das 0,836 m.
- Im Tachyon-Frame gelesen hat dieselbe Mischung keine Energie, nur Spannung.
- Ein Λ-artiger Term (w = −1) entsteht in keiner der drei Lesarten. Das H73-Ergebnis w = −β²/3 war ein Artefakt der Mischung inkonsistenter Rapiditäten.
- Möglicher Bezug, nur als Lesart: Druckloser Staub aus einer Materie–Tachyon-Mischung hätte die Zustandsgleichung kalter dunkler Materie. Das passt zum Spiegelteilchen-Gedanken des Autors (H71, Lesart 3) und zu Ω_M = β² (r67), ist aber nicht geprüft.
- Die Summe beider Lesarten hat w = −⅓, die Zustandsgleichung von Strings bzw. Krümmung. Ob eine solche Summe physikalisch Sinn hat, ist offen. Auslöser 3 von I1 (String/LQG) liegt nahe; als Hinweis vermerkt.
