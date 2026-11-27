# Ergebnis H207 (k417): Die H168-Spannung war ein Richtungs-Artefakt — die Stärke ist (fast) der gemeinsame Versatz

**Datum:** 2026-11-27. **Werkzeuge:** numpy (κ-Fit, Kandidatenvergleich, gemeinsamer Versatz). Keine exakte Identität ⇒ Wolfram nicht einschlägig; Qiskit nicht einschlägig.
**Vorab:** `Vorab_H207_Staerke_Versatz.md` (vor der Rechnung committet). **Teilweise nicht blind** (κ* ≈ Versatz aus H206-Zahlen erkennbar).

## Frage
Nach H205/H206 ist die θ₁₃-**Richtung** strukturell fest (K₂). Ist die **Stärke** κ ein struktureller Versatz, und löst sich die H168-Spannung (H176: 5,7σ) mit der jetzt festgelegten Richtung?

## Befund: die H168-Spannung war weitgehend ein Artefakt der angepassten Richtung

**(1) Mit der Struktur-Richtung K₂ fällt die Mischungs-Spannung von 5,7σ auf ~1,5σ.** Der gemeinsame Versatz x (Neutrino-Spektrum **und** κ = tan x), der θ₁₃ trifft, ist **x\* = 0,0409** — nur **1,5σ** vom Lepton-Versatz x_lepton = 0,039577 entfernt (σ_x = 0,00091). H176 fand mit der **angepassten Halbierenden** (K₁+K₂)/√2 noch x = 0,04478, also 5,7σ. Die große Spannung war also ein Artefakt der nicht-strukturellen Richtung; die massenerhaltende Richtung K₂ (H206) löst sie weitgehend.

**(2) Der reine H168-Versatz (x = x_lepton überall, null Parameter) trifft alles außer θ₁₂.** Setzt man **einen** Versatz x = x_lepton für Neutrino-Spektrum **und** Stärke κ = tan(x_lepton) in K₂-Richtung:

| Größe | Wert | z |
|---|---|---|
| sin²θ₁₃ | 0,02164 | **−1,5σ** ✓ |
| sin²θ₂₃ | 0,49445 | +1,4σ ✓ |
| sin δ_CP | +0,9998 | nahezu maximal ✓ |
| sin²θ₁₂ | 0,31983 | **+2,5σ** ✗ (TM1-Problem) |

Mit **null** freien Parametern liegen θ₁₃, θ₂₃ und δ_CP innerhalb ~1,5σ; nur θ₁₂ ist zu hoch.

**(3) Kein einzelner Kandidat trifft θ₁₃ exakt, aber x_lepton am besten.** Mit Neutrino-Spektrum bei x_ν (R) ist κ*(θ₁₃) = 0,0363 ± 0,0027; die Kandidaten: x_lepton → θ₁₃ +1,2σ (nächster), tan(x_ν)/x_ν → +2,7σ, ε = artanh β_sym = 0,618 unbrauchbar (Massen nicht erreichbar). Der ursprüngliche K1-Kandidat **x_ν trifft nicht** (2,7σ); **x_lepton** ist der nahe Wert (1,2σ).

## Lesart (ehrliche Einordnung)
- **Aufgelöst:** Die von H176 berichtete 5,7σ-Spannung zwischen Mischungs-Versatz und Lepton-Versatz ist **kein echtes Problem** — sie entstand durch die angepasste Halbierende. Mit der strukturellen Richtung K₂ ist die Mischungs-Stärke mit dem gemeinsamen Versatz verträglich (~1,5σ). Die Stärke ist also **kein wild freier Parameter**, sondern (fast) der gemeinsame Versatz; θ₁₃ ist mit null Parametern aus x_lepton auf −1,5σ **vorhergesagt**.
- **Verbleibende echte Spannung (verschoben, nicht beseitigt):** Das Neutrino-Spektrum braucht für R den Versatz x_ν = 0,043359, die geladenen Leptonen geben x_lepton = 0,039577; die Differenz ist **(x_ν − x_lepton)/σ_x = 4,2σ**. Das ist die genuine H168-Rest-Spannung — zwischen **Neutrino-R-Versatz und Lepton-Versatz**, unabhängig von der Mischungsrichtung. H207 verschiebt die Spannung von der Mischung (gelöst) auf die beiden Sektor-Versätze (R vs. Masse).
- **Weiterhin offen:** sin²θ₁₂ = 0,320 (+2,5σ, TM1-Problem, aus H206) — der strukturell hartnäckigste Punkt; strukturell nur durch Aufgabe der Massen-Erhaltung senkbar (H206).
- **Kein Datensieg, aber bessere Lage:** Mit der Struktur (H205/H206) und dem gemeinsamen Versatz sind θ₁₃, θ₂₃, δ_CP mit null Parametern innerhalb ~1,5σ; die Mischung ist damit viel weniger „gefittet" als in H176. Die Daten verlangen den Ladungssektor nach H175 trotzdem nicht.

## Stand Mischungswinkel (Strang 3, nach H207)
- **Hergeleitet/vorhergesagt:** TM1-Baum (H173); feste Spalte v₀ (H205); θ₁₃-Richtung = K₂ (H206); mit dem gemeinsamen Versatz x_lepton sind θ₁₃ (−1,5σ), θ₂₃ (+1,4σ), |sin δ| ≈ 1 **null-parametrige** Vorhersagen (H207).
- **Offen:** (i) sin²θ₁₂ zu hoch (+2,5σ, TM1); (ii) der 4,2σ-Abstand zwischen Neutrino-R-Versatz (0,0434) und Lepton-Versatz (0,0396). OP4 bleibt offen.

## Ehrlichkeit (teilweise nicht blind)
Dass κ* nahe einem der Versätze liegt, war aus H206 erkennbar. **Blind/neu:** welcher Versatz (x_lepton, nicht x_ν), die quantitative Auflösung der 5,7σ-Spannung auf 1,5σ durch die Struktur-Richtung, die null-parametrige H168-Vorhersage (θ₁₃ −1,5σ), und die Verschiebung der Rest-Spannung auf die Sektor-Versätze (4,2σ) und θ₁₂.

## Dateien
- `Vorab_H207_Staerke_Versatz.md` — Vorab-Notiz (vor der Rechnung).
- `k417_test_h207.py`, `k417_out.txt` — numpy-Rechnung und Ausgabe.
