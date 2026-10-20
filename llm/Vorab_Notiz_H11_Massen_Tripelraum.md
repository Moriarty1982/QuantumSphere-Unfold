# Vorab-Notiz H11: Massen aus einer natürlichen Funktion auf dem Tripel-Raum

Festgelegt am 2026-10-20, **vor** der numerischen Prüfung und vor dem Vergleich mit Massen. Bezug: K30/K31 (r15).

## Rahmen

Tripel (a, b, c) ∈ 𝕆³ (Generationen = Triality-Plätze, Farbe = SU(3) ⊂ G₂ in jedem Platz). Massen-Ablesung
(verbindlich): **√m_k ∝ n_k = |Platz k|**, also m_k ∝ n_k². Die Koide-Zahl ist K = Σn_k²/(Σn_k)².

Invarianten unter G₂ (diagonal) × S₃ bis Grad 4: S = Σn_k², Q = Σn_k⁴, t = Re((ab)c) mit |t| ≤ n₁n₂n₃ = P.

## Hypothesen (V)

- **H11a (Haupt):** Massen sind die Platznormen an den kritischen Punkten der Triality-Form t bei fester Gesamtnorm S.
- **H11b:** Massen sind die Platznormen an den Minima des allgemeinsten G₂ × S₃-invarianten Potentials bis Grad 4,
  V = αS + βS² + γQ − κt (α, β, γ, κ reell, V nach unten beschränkt).

## Offenlegung (Vorüberlegung vor der Notiz)

- H11a: Lagrange-Bedingungen ergeben |bc| = λ|a| usw., also entweder gleiche Normen (K = 1/3) oder zwei verschwindende
  Plätze (K = 1). Erwartung: keine Hierarchie.
- H11b: An einem kritischen Punkt mit n_k ≠ 0 gilt für jedes k dieselbe Gleichung
  (2α + 4βS)·x_k + 4γ·x_k² = κP mit x_k = n_k², quadratisch in x_k. Erwartung: höchstens **zwei** verschiedene Normen,
  also immer ein entartetes Paar oder ein leerer Platz.
- Bekannt: Die geladenen Leptonen haben drei verschiedene Massen.

## Verfahren (verbindlich)

- H11a: kritische Punkte von t auf {S = 3} numerisch (viele Startpunkte, Gradientenverfahren mit Nebenbedingung),
  Normmuster und K berichten.
- H11b: Gitter über (β, γ, κ) bei α = −1 (bei α ≥ 0 liegt das Minimum bei 0), nur beschränkte Fälle; Minimierung von
  vielen Startpunkten über n ∈ ℝ³₊ mit t = +P (für κ > 0 optimal; κ < 0 durch Vorzeichenwahl gleichwertig). Für jedes
  globale Minimum: Zahl der verschiedenen Normen (Toleranz 10⁻⁶ relativ), K.

## Entscheidungskriterium (verbindlich)

- H11a/H11b gelten als **widerlegt**, wenn kein kritischer Punkt bzw. kein Minimum drei verschiedene, von null
  verschiedene Normen hat (dann sind die Leptonmassen nicht darstellbar).
- Gibt es solche Minima, wird geprüft, ob die Lepton-Verhältnisse √(m_e/m_τ), √(m_μ/m_τ) erreichbar sind und wie viele
  Parameter dafür angepasst werden müssen. Werden dafür zwei oder mehr Parameter benötigt, gilt das als **keine
  Vorhersage**.
- Zusätzlich wird berichtet, welcher Grad an Invarianten mindestens nötig wäre.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
