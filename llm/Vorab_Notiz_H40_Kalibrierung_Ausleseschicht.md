# Vorab-Notiz H40: Kalibrierung der Ausleseschicht und Suche nach Struktur in den Einstellungen

Festgelegt am 2026-10-24, **vor** der Rechnung. Autor: „wenn der kern theoretisch hält und ich eigentlich nur einen ausleselayer über die struktur lege, …
wie man diese filterebene einstellen müsste, so dass sie reale ergebnisse produziert? dann könnte man über die einstellungen versuchen zu begreifen wo das
herkommen könnte“, dann „mach das“. Bezug: r54/H38 (Form S, ein ε je Sektor, passt CKM und PMNS), `thm:master-field-equation` (Ω = m₀ + α P̂M₁₆P̂ + β𝒯 + γℋ_C,
effektive Koeffizienten), r55/H39.

## Die Filterebene (minimal, fest)

Je Sektor X ∈ {u, d, e, ν}: zirkulantes hermitesches C_X = a_X·1 + b_X P + b̄_X P² (Brannen-Form, P zyklische Verschiebung), Maskenstärke ε_X,
Form S: M_X = D C_X D⁻¹, D = exp(ε_X W_X), W_q = diag(0, −2, −1), W_l = diag(0, 0, −3). Dirac-Neutrinos, m₁ ∈ {0, 0.001, 0.003} eV (DESI).

**Zählung:** 4 × (a, |b|, θ, ε) = 16 Einstellungen (+ m₁). Messgrößen: 9 geladene Massen, 2 Δm², 3 CKM-Beträge, 3 PMNS-Winkel = 17 (+ CKM- und PMNS-Phase,
hier nicht verwendet). Kompression also gering: 17 Größen aus 16 Einstellungen; je Familie bleibt eine Vorhersage (H38: nicht scharf).

## Kalibrierung

Zulässig sind genau die Kombinationen aus H38c/d (Verfahren und Daten unverändert: CKM alle drei innerhalb ±20 %, PMNS alle drei im 3σ-Bereich). Für jede
zulässige Kombination werden die Einstellungen abgelesen: ε_X und aus den Eigenwerten λ_X von C_X die Brannen-Größen |b|/|a| und θ (reduziert auf [0, π/3],
weil Permutation und Spiegelung der Eigenwerte θ um 2π/3 bzw. zu −θ verschieben).

## Größen und Kandidatenwerte (vorab festgelegt)

16 Größen: ε_u, ε_d, ε_e, ε_ν, ε_u/ε_d, ε_e/ε_ν, ε_d/ε_e, ε_u/ε_ν, und je Sektor |b|/|a| und θ.
Für jede Größe: Bereich [min, max] über alle zulässigen Kombinationen.
14 Kandidatenwerte aus Struktur und Korpus: 1/3, 1/2, 2/3, 3/4, 1, 1/√3, 1/√2, √3, 2/9, π/6, π/9, β_sym² = 0.3017, β_sym = 0.5493, γ_L = 1.864.
Ein **Treffer** ist ein Paar (Größe, Kandidat) mit Kandidat im Bereich der Größe.

## Gegenprobe (vorab festgelegt)

10 000 Zufallssätze von je 14 Werten, log-gleichverteilt in [0.2, 2] (Spanne der Kandidaten); für jeden Satz dieselbe Trefferzählung. p = Anteil der Zufallssätze mit
mindestens so vielen Treffern wie die Kandidaten.

## Hypothesen

- **H40a (Struktur in den Einstellungen):** Die Kandidaten treffen mehr als zufällige Werte, p < 0.01.
- **H40b (Gleichheit):** Mindestens eine der vier ε-Verhältnisse enthält 1 in ihrem Bereich (zwei Sektoren mit gleicher Maskenstärke).

## Entscheidungskriterium (verbindlich)

- H40a bestätigt ⇒ Die Einstellungen der Filterebene zeigen Struktur aus dem Korpus; die getroffenen Werte werden festgehalten und sind Gegenstand eines eigenen Tests.
- H40a widerlegt ⇒ Die Einstellungen, soweit die Daten sie festlegen, zeigen keine Struktur über Zufall hinaus; die Filterebene ist dann (noch) Beschreibung.
- H40b ist ein Teilbefund und zählt nur mit H40a.
- **Lesarten nach der Rechnung (kein Kriterium):** Zuordnung zu den Koeffizienten der Master-Gleichung (m₀ ↔ a, β ↔ |b|, γ ↔ ε) und Lesart von D als Verformung
  der komplexen Struktur mit Dilatation K = exp(ε·Spannweite(W)) und Beltrami-Betrag |μ| = (K − 1)/(K + 1). Beides wird nur berichtet.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
