# H206 / k416 — Winkel in der Ebene ⊥ v₀: strukturell erzwungen?

**Verdikt: Richtung in der Ebene eindeutig erzwungen (K₂, massenerhaltend) — aber θ₁₂ bleibt ungelöst.**

Fortsetzung des Winkel-Strangs (Autor „weiter und push" nach H205).

- In der Ebene ⊥ v₀ (H205) ist **K₂ die eindeutige massenerhaltende Richtung**: in der zirkulanten Eigenbasis (T-EW 1, ω, ω²) ist diag(K₂) = {0,0,0}, diag(K₁) = {0,−1/√3,+1/√3} ≠ 0 (Wolfram exakt) ⇒ Massen-Erhaltung erzwingt ψ = 90° (K₂). Zusammen mit H205 ist die θ₁₃-**Richtung vollständig strukturell bestimmt** (nur Stärke/Vorzeichen frei).
- **Vorhersage der Struktur-Richtung K₂:** nahezu maximales θ₂₃ und maximale CP-Verletzung (|sin δ| ≈ 1, erste Ordnung exakt), θ₁₃ über die Stärke einstellbar. **Aber** sin²θ₁₂ = 0,320 zu hoch (+2,5σ, TM1-Problem).
- Die in H176 angepasste Halbierende (K₁+K₂)/√2 senkt θ₁₂ (trifft), **bricht** dafür Massen (Koide 1,0→0,985) und |sin δ| (→0,964) — nicht strukturell, sondern gefittet.
- **Bilanz:** θ₁₃-Richtung hergeleitet (H205+H206); offen bleiben Stärke (H168-Spannung) und θ₁₂ (TM1). Teilweise nicht blind.

**Werkzeuge:** numpy (k416), Wolfram exakt (k416b) — einig.

**Dateien:** `Vorab_H206_Winkel_in_Ebene.md`, `k416_test_h206.py` (+ `k416_out.txt`), `k416b_kontrolle.wl` (+ `k416b_out.txt`), `Ergebnis_H206_Winkel_in_Ebene.md`.
