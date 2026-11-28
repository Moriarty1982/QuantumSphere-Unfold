# Vorab H238 (k454): Zeichnet eine Energie auf dem Kreis der wellenfähigen Richtungsräume genau die drei Kopien aus? Sind die Kopien die Generationen?

**Datum:** 2026-11-28, vor der Rechnung committet. **Anlass:** H237 (k453c, nachträglich) zeigte, dass die Feldgleichung einen ganzen Kreis
wellenfähiger Richtungsräume U_θ = {cos θ·eᵢ + sin θ·e₈₊ᵢ : i = 1…7} zulässt und dass die Dreizahl nur aus der Abgeschlossenheit als Algebra kommt.
Marc: „weiter“. Gesucht ist eine physikalische Größe statt reiner Algebra.

## Vorwissen geprüft
- **H138 (k321):** Unitale, G₂-stabile Oktonion-Kopien gibt es genau bei Im((t₁ + i t₂)³) = 0, also sin 3θ = 0. Das sind drei Kopien bis auf das
  Vorzeichen von v. Die **Lage** der Nullstellen ist damit bekannt (nicht blind).
- **H237:** δ = 0 auf ganz 𝕊 für jedes θ. Mit e₈ gibt es 8 Richtungen.
- **H148, k255, r13:** Koide K = ⅔ gilt genau bei der Amplitude √2 bzw. dem Mischwinkel π/4. Die Brannen-Form ist
  √m_k = μ(1 + √2 cos(δ + 2πk/3)).
- **H221–H236:** Der Lepton-Versatz φ ist nicht herleitbar. δ_Im = 0,2222220, δ_Re = 0,48399 (H225).
- **H140–H143:** Ob die Kopien Generationen sind, ist offen.
- **Zählpostulat r67:** Gewicht 2 je Spin (nur als möglicher Bezug, nicht gewertet).

## Teil A (Form und Nicht-Entartung blind, Lage der Nullstellen nicht blind): Leck-Energie
Ein Feld mit Werten in span{1, U_θ} wechselwirkt quadratisch mit sich selbst über das Produkt. Was aus dem eigenen Raum herausfällt, ist Leck. Die
Leck-Energie ist L(θ) = Σₐ,ᵦ ‖P⊥_θ(uₐuᵦ)‖², wobei P⊥_θ auf das Komplement von span{1, U_θ} projiziert.
- **trägt:** L(θ) = A·sin²(3θ) exakt (Restabweichung < 10⁻¹⁰ auf 360 Winkeln). L hat genau drei Minimumsklassen (θ mod π), alle nicht entartet
  (L″ > 0), und keine weiteren Minima.
- **trägt teilweise:** Die Minima liegen genau bei den Kopien, aber die Form weicht ab, oder es gibt zusätzliche Minima.
- **widerlegt:** Die Minima liegen nicht bei den Kopien, oder sie sind entartet.

## Teil B (nicht blind, Identität; nur Lesart): Brannen-Form als Überlapp mit den Kopien
Die Kopien werden mit Vorzeichen so gewählt, dass sie bei θ_k = 0°, 120° und 240° liegen. Der Überlapp eines Richtungsraums U_θ mit Kopie k ist
⟨U_θ, U_θk⟩ = cos(θ − θ_k). Das Feld F = 1 + w·(Einheitsrichtung bei θ) hat die Amplituden a_k = 1 + w·cos(θ − θ_k) auf den drei Kopien.
- Es wird nachgerechnet, dass K = Σa_k² / (Σa_k)² = ⅔ genau bei w = √2 gilt, für jedes θ. Mit θ = −δ ist das die Brannen-Form.
- Nur Bericht: w² = |Im F|²/|Re F|² = 2.

## Teil C (blind): Liegen die gemessenen Brannen-Phasen in Minima der Leck-Energie?
L(δ)/max L wird für δ_Im = 0,2222220 und δ_Re = 0,48399 berechnet (θ = ±δ).
- **Kriterium C:** Liegen beide Phasen innerhalb 1 % von max L in einem Minimum (L/max < 0,01), heißt das „Phasen im Minimum“. Sonst „Phasen
  abseits“; dann braucht die Lage auf dem Kreis eine weitere Größe, wie φ bisher.

## Urteil
Das Urteil richtet sich nach Teil A. B ist eine Lesart, C ein Zusatzbefund. Kopien = Generationen wird **nicht** als gezeigt gewertet, auch wenn B passt.

## Werkzeuge
Python k454, Wolfram k454b (symbolisch L(θ), unabhängig). Qiskit ist nicht einschlägig.
