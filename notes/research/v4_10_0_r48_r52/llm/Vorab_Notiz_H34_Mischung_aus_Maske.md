# Vorab-Notiz H34: Erklärt die Maske aus r47 mit einem gemeinsamen ε die CKM- und PMNS-Mischung?

Festgelegt am 2026-10-24, **vor** der Rechnung. Autor: „mach den test, dann sehen wir was raus kommt“. Bezug: r47 (Modellannahme und Masken
W_q = diag(0, −2, −1), W_l = diag(0, 0, −3), Leptonen in der Generationen-Basis √3 stärker), r46 (Mischung ∝ Gewicht, unterdrückt durch Massenabstände).

## Modell (die Annahme von r47, nicht hergeleitet)

Für X ∈ {u, d, e, ν}: M_X = C_X + ε (W_X C_X + C_X W_X), C_X hermitesch und ℤ₃-zirkulant, C_X = F diag(λ_X) F† mit reellen λ_X
(F Fourier-Matrix der Generationen). W_u = W_d = W_q, W_e = W_ν = W_l. **Ein gemeinsames ε ≥ 0** für alle vier. Neutrinos als Dirac-Teilchen
wie die geladenen Fermionen. Die Massen sind die Beträge der Eigenwerte von M_X; die Mischung ist V = U_u† U_d bzw. U = U_e† U_ν, Spalten
nach aufsteigender Masse geordnet. Nur Massenverhältnisse gehen ein.

## Daten (fest)

- Massen bei μ = M_Z (Huang, Zhou, arXiv:2009.04851, „Full SM“): m_u = 1.23 MeV, m_c = 0.620 GeV, m_t = 168.26 GeV; m_d = 2.67 MeV,
  m_s = 53.16 MeV, m_b = 2.839 GeV; m_e = 0.48307 MeV, m_μ = 101.766 MeV, m_τ = 1728.56 MeV.
- Neutrinos (NuFIT 6.0, normale Ordnung, IC19 ohne SK-atm): Δm²₂₁ = 7.49·10⁻⁵ eV², Δm²₃₁ = 2.534·10⁻³ eV²; m₁ ∈ {0, 0.001, 0.003, 0.01,
  0.02, 0.05, 0.1} eV.
- CKM (PDG 2024): |V_us| = 0.2250, |V_cb| = 0.0418, |V_ub| = 0.00373.
- PMNS (NuFIT 6.0, wie oben, 3σ): sin²θ₁₂ ∈ [0.275, 0.345], sin²θ₂₃ ∈ [0.430, 0.596], sin²θ₁₃ ∈ [0.02023, 0.02376].

## Verfahren (fest)

Für jeden Sektor werden die Zweige der Lösungen λ_X(ε) mit |eig M_X| = Zielmassen verfolgt: Start bei ε = 0 in allen 48 Zuordnungen
(Permutation der Massen auf die Fourier-Moden × Vorzeichen; λ ↦ −λ ist dieselbe Lösung, bleiben 24), Fortsetzung in Schritten von 0.005
bis ε = 3, Lösen mit relativer Toleranz 10⁻⁹; ein Zweig endet, wo keine Lösung mehr gefunden wird. |V_us| = |V₁₂|, |V_cb| = |V₂₃|,
|V_ub| = |V₁₃|; sin²θ₁₃ = |U₁₃|², sin²θ₁₂ = |U₁₂|²/(1 − |U₁₃|²), sin²θ₂₃ = |U₂₃|²/(1 − |U₁₃|²).

## Hypothesen

- **H34a (CKM):** Es gibt ein ε und Zweige für u und d, bei denen |V_us|, |V_cb|, |V_ub| alle drei innerhalb ±20 % der Daten liegen.
  Mitberichtet wird, welcher Anteil aller (ε, Zweigpaar)-Kombinationen das erfüllt (Freiheit durch die Zweigwahl).
- **H34b (gemeinsames ε):** Bei einem ε, das H34a erfüllt, gibt es ein m₁ aus der Liste und Zweige für e und ν, bei denen alle drei
  PMNS-Größen in den 3σ-Bereichen liegen.
- **H34c (Richtung):** Bei jedem ε, das H34a erfüllt, ist für alle m₁ und alle Lepton-Zweige der größte PMNS-Winkel größer als θ₁₂^CKM.

## Entscheidungskriterium (verbindlich)

- H34a widerlegt ⇒ Die Maske mit der Störungsannahme von r47 erklärt schon die Quark-Mischung nicht.
- H34a bestätigt, H34b widerlegt ⇒ Quark-Mischung möglich, ein gemeinsames ε für Quarks und Leptonen widerlegt.
- H34a und H34b bestätigt ⇒ Mit einem Parameter ε sind beide Mischungen verträglich. Die passenden m₁ gelten dann als Vorhersage für die
  leichteste Neutrinomasse, zu prüfen gegen spätere Messungen. Ist der Anteil passender Kombinationen in H34a groß, zählt das als schwacher Befund.
- H34c ist qualitativ und zählt nur zusammen mit H34a.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
