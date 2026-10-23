# Vorab-Notiz H17: Massen aus Potentialen mit Realteil-Invarianten auf dem Tripel-Raum

Festgelegt am 2026-10-22, **vor** der numerischen Prüfung und vor dem Vergleich mit Massen. Bezug: H11 (K32),
H16 (K70, v4.9.0-r26). Nummer H17 unter der Annahme, dass lokal nach H16 keine weitere Notiz angelegt wurde (der Rechner
war beim Festlegen nicht erreichbar; die Notiz wurde im Container committet und dem Autor vor der Rechnung geschickt).

## Rahmen

Tripel (a, b, c) ∈ 𝕆³; a_k = r_k + v_k mit Realteil r_k und Imaginärteil v_k ∈ ℝ⁷. G₂ wirkt diagonal nur auf die v_k,
also sind die r_k einzeln G₂-invariant. S₃ = ⟨zyklisch, (a,b,c) → (ā,c̄,b̄)⟩ lässt Realteile, Normen und
t = Re((ab)c) invariant. Ablesung (verbindlich, wie H11/H16): √m_k ∝ n_k = |a_k|, K = Σn_k²/(Σn_k)².

Neue Invarianten bis Grad 2: L = Σr_k, R₂ = Σr_k², L². Festgelegte Familie (H11-Potential plus alle Realteil-Invarianten
bis Grad 2):

  **V_R = −S + βS² + γQ − κt − μL − νR₂ − λL²**, S = Σn_k², Q = Σn_k⁴.

Nach unten beschränkt genau dann, wenn β > 0 und β + γ > 0.

## Offenlegung (Vorüberlegung vor der Notiz, nur analytisch)

- Auf der reellen Achse (a_k = n_k ≥ 0, t = P) wird V_R zu −(1+ν)S + βS² + γQ − κP − μL − λL², und L = Σn_k ist genau
  die Summe der Normen, die K braucht. Die Bedingung an kritische Punkte ist für jedes k dieselbe **quartische** Gleichung
  4γn⁴ + (4βS − 2(1+ν))n² − (μ + 2λL)n − κP = 0 ohne n³-Term, also ist die vierte Wurzel −L. Drei verschiedene Normen
  sind damit schon bei Grad 4 möglich; das e₂-Hindernis aus r26.1 entfällt, weil Q in den Elementarsymmetrischen der n_k
  den Term 2e₂² enthält.
- Vieta für ein Ziel-Tripel: κ = 4γL, μ + 2λL = 4γ(P − L·e₂), β aus e₂ − L² = (4βS − 2(1+ν))/(4γ). Für die Leptonen
  ist P − L·e₂ < 0. Ohne ν ist das Tripel instabil gegen Drehen des τ-Platzes aus der reellen Achse
  (Bedingung κP + 2νn_k² > |μ + 2λL|·n_k verletzt). Mit ν groß genug erwartet: lokales Minimum, also **Anpassung**
  mit mindestens zwei freien Parametern, keine Vorhersage.
- Liegen die Minima auf der reellen Achse, bleibt G₂ ungebrochen (Farbgruppe nicht ausgezeichnet); das wird berichtet.
- Erwartung H17c: K = 2/3 nicht ausgezeichnet.

## Hypothesen (V)

- **H17a (Existenz):** Unter der festen Verteilung haben globale Minima von V_R drei verschiedene, von null verschiedene
  Normen (Anteil wird berichtet).
- **H17b (Leptonen):** Für einige Parameter ist das Lepton-Tripel (√m/√m_τ = 0,016959; 0,243848; 1) das globale
  Minimum von V_R auf 𝕆³.
- **H17c (Vorhersage):** Unter den Minima mit drei verschiedenen Normen ist K = 2/3 ausgezeichnet.

## Verfahren (verbindlich)

- Minimierung über alle 24 reellen Koordinaten (keine Annahme über die Lage), BFGS mit analytischem Gradienten
  (∂t/∂a = conj(bc), ∂t/∂b = conj(ca), ∂t/∂c = conj(ab)), 20 Startpunkte. „Verschieden“ und „≠ 0“: relative Toleranz 10⁻⁴.
- Verteilung (H17a/c), N = 2000, Seed 41: β ~ U(0,1; 3), γ ~ U(−1, 2) (verworfen, wenn β + γ ≤ 0,05), κ ~ U(0, 3),
  μ ~ U(−2, 2), ν ~ U(−1, 2), λ ~ U(−1, 1). Berichtet: Muster, Anteil drei verschiedene, K-Verteilung, Anteil
  |K − 2/3| < 0,01, Anteil x_min/x_max < 10⁻³, Anteil der Minima auf der reellen Achse (|v_k| < 10⁻⁴·n_max).
- H17b: Vieta-Familie auf der reellen Achse mit freien s ∈ logspace(−2, 2, 21), γ ∈ {0,1; 0,3; 1; 3},
  ν ∈ {0; 0,5; 1; 2; 5; 10; 30}, λ ∈ {−1; 0; 1}; β, κ, μ daraus. Je Punkt: Beschränktheit, κ ≥ 0, Hessematrix in allen
  24 Richtungen positiv semidefinit bis auf die G₂-Nullrichtungen (kleinster Eigenwert ≥ −10⁻⁸·größter), dann globale
  Suche mit 100 Startpunkten (global, wenn nichts um mehr als 10⁻⁹·|V| tiefer liegt).

## Entscheidungskriterium (verbindlich)

- H17a **bestätigt**, wenn mindestens ein Parameterpunkt der Verteilung ein solches globales Minimum hat, sonst widerlegt.
- H17b **bestätigt**, wenn mindestens ein Gitterpunkt das Lepton-Tripel als globales Minimum hat, sonst widerlegt.
  Werden dafür zwei oder mehr Parameter angepasst, gilt das als **Anpassung, keine Vorhersage**.
- H17c **bestätigt** nur, wenn mindestens 50 % der Minima mit drei verschiedenen Normen |K − 2/3| < 0,01 erfüllen;
  sonst widerlegt.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
