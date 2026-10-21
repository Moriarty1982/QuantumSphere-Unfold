# Vorab-Notiz H12: Zuordnung der Messwerte zu den Kreuztermen bei gebrochener J-Symmetrie

Festgelegt am 2026-10-21, **vor** der Berechnung des genauen Vorhersagewerts. Bezug: K36/K37 (v4.8.0-r18), H9.

## Rahmen

Drei Frames in Rapiditäten: Materie bei η₊, Photon bei 0, Tachyon bei −η_s. Unter J-Symmetrie ist η₊ = η_s = η
(r18.1); H12 lässt beide getrennt. Kreuzterme η_a − η_b, Geschwindigkeit tanh, Lorentzfaktor cosh.

## Hypothese (V)

**H12:** Die drei Größen sind folgenden Kreuztermen zugeordnet (verbindlich):

- **R1** γ_L = γ_BI/γ_string = 1,86444 ist der Materie–Tachyon-Term: cosh(η₊ + η_s) = γ_L
  (so liest thm:symmetric-frame γ_L selbst).
- **R2** Die Kaskade startet im Tachyon-Stratum S⁸ und benutzt den tachyonseitigen Nachbarterm (−0):
  Ω_M = tanh²η_s. Daten: Planck 2018 (TT,TE,EE+lowE+lensing+BAO), Ω_M = 0,3111 ± 0,0056 — der Wert, den
  rem:omega-bsym verwendet.
- **R3** Der solare Mischungswinkel ist eine Messgröße des Materie-Frames und benutzt den beobachterseitigen
  Nachbarterm (+0): |U_e2|² = tanh²η₊, also sin²θ₁₂ = tanh²η₊ / cos²θ₁₃, mit sin²θ₁₃ = 0,02215 ± 0,00057
  (NuFIT 6.0, wie H9).

R1 und R2 legen η₊ und η_s fest (null Freiheitsgrade). R3 macht daraus eine Vorhersage für sin²θ₁₂, die sich
von H9 (symmetrisch, sin²θ₁₂ = β_sym²/cos²θ₁₃ = 0,30862) unterscheidet.

## Offenlegung (vor dem Festschreiben bekannt)

1. **Größenordnung bekannt.** Aus rem:omega-bsym ist bekannt, dass √Ω_M = 0,5578 über β_sym = 0,5493 liegt. Daraus
   folgt ohne Rechnung, dass η₊ unter η_s liegt und die H12-Vorhersage etwas **unter** H9. Dass η₊ < η_s mit der
   Drift-Richtung von prop:H0-tension zusammenpasst, ist deshalb **kein Befund**. Der genaue Wert ist nicht
   berechnet.
2. **Nachträgliche Grundlage.** R3 übernimmt die Relation |U_e2|² = β² aus H9, die selbst nachträglich gefunden wurde
   (K17.4). H12 ist eine Variante derselben Relation, keine unabhängige Idee.
3. **Zwei Versuche auf dieselbe Messung.** H9 und H12 zielen auf dieselbe künftige JUNO-Zahl. Ein Treffer einer der
   beiden ist deshalb weniger wert als ein einzelner vorab festgelegter Treffer. Das Kriterium unten ist deshalb
   vergleichend.
4. **Datenwahl R2.** Mit Planck 2018 ohne BAO (Ω_M = 0,3153 ± 0,0073) verschöbe sich die Vorhersage. Festgelegt ist
   der Wert mit BAO, weil das Dokument ihn benutzt; die Alternative wird mit berichtet, entscheidet aber nicht.
5. **Heutige Daten.** JUNO 2026 (sin²θ₁₂ = 0,3036 ± 0,0064) ist gelesen. Der Vergleich damit wird berichtet und
   **zählt nicht**.
6. **Ungeklärte Modellwahl.** Warum die Kaskade den tachyonseitigen und der Mischungswinkel den beobachterseitigen Term
   benutzt, ist motiviert (Startstratum S⁸, Messung im Materie-Frame), nicht hergeleitet.

## Verfahren (verbindlich)

1. η_s = artanh √Ω_M; η₊ = arcosh γ_L − η_s.
2. Vorhersage P₁₂ = tanh²η₊ / (1 − sin²θ₁₃); Unsicherheit σ_P aus Ω_M und sin²θ₁₃ (lineare Fehlerfortpflanzung).
3. Berichtet werden: η₊, η_s, β₊ = tanh η₊, β_s = tanh η_s, P₁₂ ± σ_P, die Variante ohne BAO, der (nicht zählende)
   Abstand zu JUNO 2026 und der Abstand P₁₂ − 0,30862 zu H9.
4. Skript `llm/k33_test_h12.py`, erst nach dem Commit dieser Notiz.

## Was getestet wird (verbindlich)

Dieselbe Messung wie bei H9: die **nächste** JUNO-Veröffentlichung von sin²θ₁₂ mit 1σ-Fehler ≤ 0,004, ersatzweise ein
globaler Fit, der sie enthält. Ältere Daten zählen nicht.

## Entscheidungskriterium (verbindlich)

Mit dem neuen Messwert x ± σ_x und σ = √(σ_x² + σ_P²):

- z₁₂ = (P₁₂ − x)/σ. |z₁₂| ≥ 3: **H12 widerlegt**. 2 ≤ |z₁₂| < 3: Spannung.
- Vergleich mit H9: Δχ² = z₉² − z₁₂² (z₉ wie in H9).
  - Δχ² ≥ 4 und |z₁₂| < 2: **H12 gegenüber H9 bevorzugt** (Stütze für die getrennten Offsets).
  - Δχ² ≤ −4 und |z₉| < 2: **H9 bevorzugt** (Stütze für die symmetrische Lesart).
  - sonst: **nicht entschieden**.
- Ist der Abstand |P₁₂ − 0,30862| kleiner als 2σ, kann die Messung H9 und H12 grundsätzlich nicht trennen; das wird
  dann als Ergebnis festgehalten, nicht als Test.

Wird H12 widerlegt, fällt nur die Kombination R1–R3; die Drei-Frame-Typisierung aus r18 bleibt davon unberührt.
Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
