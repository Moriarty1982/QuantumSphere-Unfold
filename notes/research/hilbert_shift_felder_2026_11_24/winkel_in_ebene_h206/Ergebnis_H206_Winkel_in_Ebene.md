# Ergebnis H206 (k416): Die Richtung in der Ebene ⊥ v₀ ist strukturell erzwungen (K₂), löst aber θ₁₂ nicht

**Datum:** 2026-11-27. **Werkzeuge:** numpy (Richtungs-Scan, PMNS, Fits), **Wolfram Language** exakt (Massen-Erhaltung in der zirkulanten Eigenbasis, Eindeutigkeit). Beide einig.
**Vorab:** `Vorab_H206_Winkel_in_Ebene.md` (vor der Rechnung committet). **Teilweise nicht blind** (K₂ als θ₁₃-Gruppe aus k372 1. Ordnung bekannt).

## Frage
Nach H205 (Ebene ⊥ v₀ fest, (K₁+K₂)/√2 die 45°-Halbierende): Welche Richtung **in** der Ebene ist strukturell erzwungen, und was sagt sie voraus?

## Befund: die Richtung ist eindeutig erzwungen (K₂) — ein strukturelles Teilresultat, aber kein θ₁₂-Erfolg

**(A) Eindeutige massenerhaltende Richtung = K₂ (exakt).** Parametrisiert man die Korrektur als D(ψ) = cos ψ·K₁ + sin ψ·K₂ in der Ebene ⊥ v₀, so verschwindet die Massen-Eigenwert-Verschiebung erster Ordnung **genau** für K₂ (ψ = 90°). In der zirkulanten Eigenbasis (T-Eigenwerte 1, ω, ω²) ist (Wolfram exakt) diag(K₂) = {0, 0, 0}, diag(K₁) = {0, −1/√3, +1/√3} ≠ 0. Die Bedingung cos ψ·diag(K₁) = 0 erzwingt cos ψ = 0 ⇒ **ψ = 90° eindeutig**. Die Massen-Erhaltung legt die Richtung in der Ebene also exakt auf K₂ fest (numpy: ‖Shift‖ = 1,4·10⁻¹⁶ für K₂ gegen 0,82 für K₁).

**(B) Was K₂ vorhersagt.** Mit D = K₂ allein, Stärke κ:
- **θ₂₃ = 45° und |sin δ_CP| = 1 in erster Ordnung** (bei κ = 0 exakt; sie driften nur zweiter Ordnung: bei der physikalischen Stärke κ* sin²θ₂₃ = 0,4939 (+1,4σ), sin δ = 0,9998). Also **nahezu maximales θ₂₃ und nahezu maximale CP-Verletzung** als robuste Vorhersage.
- **θ₁₃ wird getroffen:** κ* mit sin²θ₁₃ = 0,02248 ⇒ κ* = 0,0436.
- **θ₁₂ bleibt zu hoch:** sin²θ₁₂ = 0,3195 (+2,5σ gegen NuFIT 0,3036) — das bekannte TM1-Problem. Koide ρ bleibt bei 1,000 (Masse erhalten).

**(C) Gegenüberstellung mit der angepassten Halbierenden (H176).** (K₁+K₂)/√2 ist **nicht** massenerhaltend (diag ≠ 0; Koide ρ fällt auf 0,985). Sie senkt sin²θ₁₂ auf 0,2979 (−0,9σ, trifft), **bricht dafür** θ₂₃ (0,4941) und vor allem |sin δ_CP| (0,964 statt 1). Sie ist also ein an die Daten (θ₁₂) angepasster, nicht-struktureller Zusatz, der die Massen-Erhaltung und die maximale CP-Verletzung opfert.

## Lesart
- **Hergeleitet:** die Korrektur-**Richtung in der Ebene** ist durch Massen-Erhaltung **eindeutig** auf K₂ festgelegt (exakt). Zusammen mit H205 (Ebene ⊥ v₀) ist die θ₁₃-Richtung damit **vollständig strukturell bestimmt** (nur Stärke und Vorzeichen frei).
- **Vorhersage der Struktur:** nahezu maximales θ₂₃ und maximale CP-Verletzung (|sin δ_CP| ≈ 1), θ₁₃ frei über die Stärke einstellbar.
- **Was nicht trägt:** sin²θ₁₂ bleibt bei der struktur-erhaltenden Richtung zu hoch (TM1-Problem, +2,5σ). Es strukturell zu senken erfordert eine **nicht** massenerhaltende Richtung (K₁-Anteil), die die Massen und die maximale CP-Verletzung bricht — also eine gesetzte/angepasste Zutat, keine hergeleitete.
- **Kein Datensieg:** die reine Struktur-Richtung K₂ trifft die Daten nicht vollständig (θ₁₂); die Daten verlangen nach H175 ohnehin nicht den Ladungssektor.

## Bilanz der Setzungen (Strang 3, nach H205/H206 — zwei Runden „trägt teilweise")
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H173 | Ein-Feld-Form, Brannen-Spektrum | TM1-Baum (θ₂₃=45°, \|sinδ\|=1, sin²θ₁₂=⅓) | ein freier Winkel θ₁₃ (Stärke/Versatz) |
| H205 | — | feste Spalte v₀ baumunabhängig; θ₁₃-Korrektur ⊥ v₀ (Ebene) | Winkel in der Ebene, Stärke, Vorzeichen |
| H206 | — | Winkel in der Ebene = K₂ (massenerhaltend, eindeutig); θ₂₃≈45°, \|sinδ\|≈1 Vorhersage | **Stärke** (θ₁₃) frei; **θ₁₂ ungelöst** (TM1-Problem) |

**Ziel-Prüfung (AGENTS-Regel):** Die θ₁₃-Richtung ist jetzt vollständig hergeleitet (H205+H206). Es bleiben zwei getrennte offene Stellen: (i) die **Stärke** (= Versatz x; H168-Spannung, 5,7σ zwischen Neutrino- und Lepton-Versatz, H176); (ii) **sin²θ₁₂ zu hoch** (TM1-Problem) — strukturell nur durch Aufgabe der Massen-Erhaltung senkbar. Diese zwei sind die nächsten Weggabeln; dem Autor vorgelegt.

## Ehrlichkeit (teilweise nicht blind)
**Nicht blind:** dass K₂ die θ₁₃-/massenerhaltende Richtung ist (k372, 1. Ordnung). **Blind/neu:** der exakte Nachweis der **Eindeutigkeit** (Wolfram: diag(K₂)=0, diag(K₁)≠0 ⇒ ψ=90° einzig), die Parameterfreiheit erster Ordnung von θ₂₃=45°/|sin δ|=1, die exakte Gegenüberstellung mit der nicht-massenerhaltenden Halbierenden, und die ehrliche Trennung (Richtung hergeleitet; θ₁₂ ungelöst). OP4 bleibt offen.

## Dateien
- `Vorab_H206_Winkel_in_Ebene.md` — Vorab-Notiz (vor der Rechnung).
- `k416_test_h206.py`, `k416_out.txt` — numpy-Rechnung und Ausgabe.
- `k416b_kontrolle.wl`, `k416b_out.txt` — Wolfram-Gegenkontrolle (exakt).
