# Vorab-Notiz H41: Senkt die Maske als Korrektur die TM2-Vorhersage für θ₁₂ auf den JUNO-Wert?

Festgelegt am 2026-10-24, **vor** der Rechnung. Autor: „weiter“ (offen nach r55 und r56: Korrekturen aus der Maske zur Lesart aus r55, mit wenigen Einstellungen statt
freier Schichten). Bezug: r55/H39 (Dirac ℤ₃, Majorana ℤ₂ ⇒ TM2, sin²θ₁₂ = 1/(3cos²θ₁₃) ≈ 0.341, 3.6σ über JUNO), r47 (Maske W_l = diag(0, 0, −3)), r52/r54
(Form S für Dirac-Sektoren), r56 (Kalibrierung lehrt nur mit Kompression).

## Modell (Leptonen; die Quarks sind mit einem gemeinsamen ε in Form S schon in H36c widerlegt und hier nicht Gegenstand)

- Geladene Leptonen (Dirac): zirkulantes C_e (τ-invariant, führende Lesart ℤ₃), Korrektur Form S: M_e = D_e C_e D_e⁻¹, D_e = exp(ε_e W_l); Massen exakt angepasst
  (Zweige wie H38, ε_e auf 0, 0.01, …, 2).
- Neutrinos (Majorana): führende Lesart ℤ₂ = ⟨s⟩ mit s ∈ {diag(1,−1,−1), diag(−1,1,−1), diag(−1,−1,1)} (wegen der Maske nicht mehr gleichwertig, alle drei
  gerechnet): M₀ = Q_φ diag(μ) Q_φᵀ, Q_φ Drehung um φ im (−1)-Eigenraum von s, φ auf 0°, 2°, …, 178°. Korrektur in Form K, weil ein Majorana-Term mit D von beiden
  Seiten transformiert: M_ν = D_ν M₀ D_ν, D_ν = exp(ε_ν W_l). |μ| an die Massen angepasst (m₁ ∈ {0, 0.001, 0.003} eV, DESI), alle Zuordnungen der festen Spalte
  zu ν₁, ν₂, ν₃ und alle Vorzeichen von μ.
- **Variante A:** ε_ν = 0 (nur Korrektur der geladenen Leptonen). Einstellungen: φ, ε_e (zwei für drei Winkel).
- **Variante B:** ε_ν = ε_e = ε (eine Maskenstärke für die Leptonen). Einstellungen: φ, ε (zwei für drei Winkel), ε auf 0, 0.02, …, 1.5.

## Daten

NuFIT 6.0 normale Ordnung 3σ (wie H34) und JUNO 2025: sin²θ₁₂ = 0.3092 ± 0.0087 (arXiv:2511.14593), hier als 2σ-Bereich [0.2918, 0.3266].

## Hypothesen

- **H41a (Variante A):** Es gibt (s, φ, ε_e, Zuordnung) mit sin²θ₁₃, sin²θ₂₃ in den NuFIT-3σ-Bereichen und sin²θ₁₂ im JUNO-2σ-Bereich.
- **H41b (Variante B):** dasselbe für Variante B.
- **H41c (Schärfe):** Für eine Variante, die trifft, liegt sin²θ₂₃ unter allen Fällen mit θ₁₂ (JUNO 2σ) und θ₁₃ (3σ) in einem Bereich der Breite < 0.05 (eine Vorhersage).

## Entscheidungskriterium (verbindlich)

- H41a oder H41b bestätigt ⇒ Die Maske als Korrektur der Lesart aus r55 bringt θ₁₂ auf den JUNO-Wert; mit H41c bestätigt ist θ₂₃ vorhergesagt (Bereich festhalten).
- Beide widerlegt ⇒ Die Maske kann die TM2-Spannung mit JUNO nicht auflösen; die Lesart aus r55 bleibt in θ₁₂ unter Druck.
- Treffer ohne H41c ⇒ Anpassung mit zwei Einstellungen, keine Vorhersage.

## Offenlegung

Nicht vorab gerechnet. Allgemein bekannt ist nur, dass Korrekturen der geladenen Leptonen TM2-Werte von θ₁₂ verschieben können; in welche Richtung hier, ist offen.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
