# Vorab-Notiz H206 (k416): Ist die Korrekturrichtung IN der Ebene ⊥ v₀ strukturell erzwungen?

**Datum:** 2026-11-27. **Strang:** Lepton-Mischung (Strang 3). **Auslöser:** Autor, 27.11., „weiter und push" (nach H205). Fortsetzung des Winkel-Strangs: nächster offener Freiheitsgrad nach H205 ist der **Winkel innerhalb** der Ebene ⊥ v₀ (welche Mischung aus K₁, K₂) sowie die Stärke. Einordnung: `wiki/Gesamtbild.md` T8, OP4.

## Frage
H205 zeigte: die θ₁₃-Korrektur im Ladungssektor liegt exakt in der Ebene ⊥ v₀ = (1,0,1)/√2; (K₁+K₂)/√2 ist die 45°-Halbierende. Offen blieb: welche Richtung **in** dieser Ebene. k372 beobachtete (erste Ordnung): von den Ladungs-Generatoren bewegt **K₂ allein** θ₁₃ und lässt dabei die Massenstruktur unberührt **und** hält sin δ_CP = 1; **K₁** dagegen bewegt θ₁₂ und ändert Koide-Wert und Phase.

**H206:** Ist die Korrekturrichtung in der Ebene ⊥ v₀ **strukturell** erzwungen — nämlich auf die eindeutige Richtung, die (a) die Massen-Eigenwerte und (b) |sin δ_CP| = 1 und θ₂₃ = 45° erhält (vermutlich K₂) — und was sagt diese erzwungene Richtung voraus? Oder ist der Winkel in der Ebene frei, sodass die angepasste Halbierende (K₁+K₂)/√2 aus H176 nötig ist?

## Was gerechnet wird (k416)
Maschinerie aus k371 (DIRS, obs/chi2, N̂, Polmassen). Parametrisiere die Korrektur als D(ψ) = cos ψ·K₁ + sin ψ·K₂ in der Ebene span{K₁, K₂} (= Ebene ⊥ v₀, H205). Numerisch (numpy) und für die Struktur-Aussagen exakt (Wolfram):
1. **Massen-/sinδ-Erhaltung:** Für welche ψ lässt D(ψ) die drei Massen-Eigenwerte (erste Ordnung) und sin δ_CP = 1, θ₂₃ = 45° exakt? Ist diese Richtung eindeutig (= K₂, ψ = 90°)?
2. **Vorhersage der erzwungenen Richtung:** Mit D = K₂ (reine Struktur-Richtung), Stärke κ: sind θ₂₃ = 45° und |sin δ_CP| = 1 **parameterfrei** (für alle κ) exakt? θ₁₃(κ), θ₁₂(κ). Pinne κ an sin²θ₁₃ (Daten) → Vorhersage sin²θ₁₂ und sin²θ₂₃; vergleiche mit NuFIT/JUNO.
3. **Gegenüberstellung:** dieselben Vorhersagen für die Halbierende (K₁+K₂)/√2 (H176); um wie viel weicht θ₂₃ von 45° und |sin δ| von 1 ab, und was kostet/bringt das bei θ₁₂?

## Entscheidungskriterien (vorab)
- **K1 (Richtung in der Ebene strukturell erzwungen):** Es gibt genau eine Richtung ψ* in der Ebene (bis auf Vorzeichen), die Massen-Eigenwerte **und** sin δ = 1, θ₂₃ = 45° erhält (exakt, Wolfram), und das ist K₂. Dann ist die Korrektur-Richtung **vollständig** festgelegt (nur Stärke und Vorzeichen frei), und θ₂₃ = 45°, |sin δ_CP| = 1 sind **parameterfreie Vorhersagen**. Ob sie die Daten trifft (θ₁₂!) ist dann eine separate Aussage.
- **K2 (Winkel in der Ebene frei):** Kein eindeutiges ψ* erhält Massen + sin δ = 1; mehrere Richtungen sind strukturell gleichwertig, oder die Erhaltung legt ψ nicht fest. Dann bleibt der Winkel in der Ebene frei (wie die Stärke).

## Erwartung (ehrlich)
Voraussichtlich **K1 für die Struktur-Richtung K₂** (k372 erste Ordnung deutet darauf), aber: die erzwungene Richtung K₂ allein lässt sin²θ₁₂ zu hoch (TM1-Problem, H175b: +2,5σ). D. h. die **Struktur** sagt maximales θ₂₃ und maximale CP-Verletzung (|sin δ| = 1) voraus und trifft θ₁₃, verfehlt aber θ₁₂; die in H176 angepasste Halbierende bricht θ₂₃/sin δ leicht, um θ₁₂ zu senken. **Nicht blind** ist, dass K₂ die θ₁₃-Gruppe ist (k372 erste Ordnung); **blind/neu** ist der exakte Nachweis der Eindeutigkeit und Parameterfreiheit (θ₂₃ = 45°, |sin δ| = 1 für alle κ) sowie die exakte Gegenüberstellung mit der Halbierenden. Selbst bei K1 bleiben Stärke, Vorzeichen und die θ₁₂-Spannung offen; die Daten verlangen die reine Struktur-Richtung nach H175 nicht.

## Vorwissen geprüft
- `drehwinkel_richtung_h205/` (H205): Ebene ⊥ v₀ exakt; v₀ Eigenvektor von N̂ für alle δ_ν.
- `mischung_h175/` (H175, k371–k373): zwei Gruppen (θ₁₃ vs θ₁₂); K₂ erhält Masse+sinδ=1 (erste Ordnung); (K₁+K₂)/√2 angepasst; K₂ allein χ²=8,1 (θ₁₂ +2,5σ).
- `mischung_h173/` (H173): TM1-Baum; sin²θ₁₂ wie TM1 zu hoch gegen JUNO.
- k262/k262b (Träger, A), H99 (Brannen), H168 (Versatz), H125 (sin δ_PMNS < 0).

## Werkzeuge
numpy (D(ψ), Eigenwerte, PMNS, Fits) und **Wolfram Language** exakt (Eindeutigkeit der struktur-erhaltenden Richtung; θ₂₃ = 45°, |sin δ| = 1 parameterfrei). Qiskit nicht einschlägig.
