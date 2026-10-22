# Vorab-Notiz H12: Massen aus invarianten Potentialen bis Grad 6 auf dem Tripel-Raum

Festgelegt am 2026-10-22, **vor** der numerischen Prüfung und vor dem Vergleich mit Massen. Bezug: H11 (K32, r16).

## Rahmen (wie H11)

Tripel (a, b, c) ∈ 𝕆³, Generationen = Triality-Plätze, Farbe = SU(3) ⊂ G₂ je Platz. Ablesung (verbindlich):
√m_k ∝ n_k = |Platz k|, x_k = n_k². K = Σn_k²/(Σn_k)². Wie in H11 nur Funktionen der Normen und von
t = Re((ab)c) mit |t| ≤ P = n₁n₂n₃; bei den betrachteten Vorzeichen ist t = P im Minimum optimal.

Leptonen (PDG-Polmassen): √m/√m_τ = (0,016959; 0,243848; 1), K = 0,666664, also
x_e : x_μ : x_τ = 2,876·10⁻⁴ : 0,05946 : 1.

## Minimale Erweiterung (festgelegt)

Die Kandidaten vom Grad 5–6 sind S³, S·Q, H = Σn_k⁶, P², S·P. Nur H erzeugt einen Term x_k³ in der
Bedingung an die kritischen Punkte (die anderen ändern nur Koeffizienten, die für alle k gleich sind). Daher:

  **V₆ = −S + βS² + γQ − κP + δH**, mit δ > 0 (dann nach unten beschränkt), κ ≥ 0.

## Offenlegung (Vorüberlegung vor der Notiz, nur analytisch)

An einem kritischen Punkt mit allen n_k ≠ 0 gilt für jedes k dieselbe kubische Gleichung
6δ·x³ + 4γ·x² + (−2 + 4βS)·x − κP = 0. Haben die x_k drei verschiedene Werte, sind sie genau die drei Wurzeln,
und Vieta ergibt S = −2γ/(3δ) (also γ < 0), e₂ = Σx_ix_j = (−2 + 4βS)/(6δ), P = κ/(6δ).
Folge: Jedes Tripel mit drei verschiedenen positiven x_k ist kritischer Punkt einer Parameterfamilie; für
zwei Verhältnisse plus Skala bleiben bei vier Parametern zwei Parameter frei. **Kritisch** ist das Tripel damit
immer erreichbar, offen ist nur, ob es ein **Minimum** (lokal, global) ist. Erwartung: Wenn ja, dann als Anpassung.
Außerdem: K = 2/3 verlangt Σn_k, das kein Polynom in den Oktonionen-Koordinaten ist; polynomiale Potentiale
sehen K nicht direkt. Erwartung: K = 2/3 ist unter V₆ nicht ausgezeichnet.

## Hypothesen (V)

- **H12a (Existenz):** V₆ hat für einen Teil der Parameter ein globales Minimum mit drei verschiedenen, von null
  verschiedenen Normen.
- **H12b (Leptonen erreichbar):** Es gibt Parameter, für die das Lepton-Tripel (Verhältnisse oben, Skala frei)
  das **globale** Minimum von V₆ ist.
- **H12c (Vorhersage):** Unter einer festen Parameterverteilung ist K = 2/3 bei den Minima mit drei verschiedenen
  Normen ausgezeichnet.

## Verfahren (verbindlich)

- Minimierung über n ∈ ℝ³ mit P = n₁n₂n₃ (Vorzeichen frei, wie k30), 40 Startpunkte, BFGS. „Verschieden“:
  relative Toleranz 10⁻⁴ (nach H11 festgelegt); Kontrolle über die kubische Gleichung.
- Verteilung für H12a/H12c: β ~ U(0, 3), γ ~ U(−2, 1), κ ~ U(0, 3), δ ~ U(0,01; 2), N = 2000, Seed 31.
- H12b: Für das Lepton-Tripel die zweiparametrige Familie aus Vieta (freie Skala s und freies β; γ, κ, δ daraus)
  auf einem Gitter abtasten: s ∈ {10⁻², …, 10²} (logarithmisch, 41 Werte), β ∈ [−5, 5] (41 Werte); je Punkt
  Bedingung δ > 0, κ ≥ 0, Hessematrix positiv definit (lokales Minimum), dann globale Suche mit 200 Startpunkten
  (global, wenn kein Punkt um mehr als 10⁻⁹·|V| tiefer liegt).

## Entscheidungskriterium (verbindlich)

- H12a **bestätigt**, wenn mindestens ein Parameterpunkt der Verteilung ein solches globales Minimum hat;
  berichtet wird der Anteil.
- H12b **bestätigt**, wenn mindestens ein Gitterpunkt das Lepton-Tripel als globales Minimum hat; dann wird die
  Dimension der Lösungsmenge berichtet. Werden zwei oder mehr Parameter dafür angepasst (Erwartung), gilt das als
  **Anpassung, keine Vorhersage**. Hat kein Gitterpunkt ein solches Minimum, ist H12b **widerlegt** (dann trägt V₆
  die Lepton-Hierarchie nicht).
- H12c **bestätigt** nur, wenn unter den Minima mit drei verschiedenen Normen mindestens 50 % |K − 2/3| < 0,01
  erfüllen; sonst **widerlegt**. Zusätzlich berichtet: Verteilung von K und Anteil mit x_min/x_max < 10⁻³.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
