# Ergebnis H238 (k454): Leck-Energie auf dem Kreis der wellenfähigen Richtungsräume

**Datum:** 2026-11-28. **Vorab:** `Vorab_H238_Kreis_Energie.md`, Commit c49ea83, vor der Rechnung. **Rechnung:** `k454_test_h238.py` → `k454_out.txt`;
Gegenprobe `k454b_gegenprobe.wl` → `k454b_out.txt` (symbolisch, exakt). **Urteil: trägt** (Teil A). Kopien = Generationen ist **nicht** gezeigt.

## Frage
H237 zeigte: Die Feldgleichung lässt einen ganzen Kreis wellenfähiger Richtungsräume U_θ = {cos θ·eᵢ + sin θ·e₈₊ᵢ} zu. Die Dreizahl kam nur aus der
Abgeschlossenheit als Algebra. Gesucht war eine physikalische Größe, die genau drei Punkte auszeichnet.

## Teil A (Form und Nicht-Entartung blind, Lage der Nullstellen aus H138 bekannt): trägt
Leck-Energie eines quadratisch selbstwechselwirkenden Feldes in span{1, U_θ}: L(θ) = Σₐᵦ ‖P⊥_θ(uₐuᵦ)‖².
- **L(θ) = 42·sin²(3θ) exakt.** Python: Restabweichung 9,2·10⁻¹⁴ auf 360 Winkeln, nur die Fourier-Moden 0 und 6. Wolfram: symbolischer Nullrest 0.
- Genau drei Minimumsklassen (θ mod π) bei 0°, 60°, 120°, das sind die drei G₂-Kopien aus H138 (mit v → −v bei 0°, 120°, 240°). L = 0 dort.
- Alle nicht entartet: L″ = 756 = 18·42 an allen drei Kopien (Wolfram exakt). Keine weiteren Minima.
- Lesart: Zwischen den Kopien fällt ein Teil des Produkts aus dem eigenen Raum heraus; nur an den drei Kopien ist das Feld energetisch geschlossen.
  Die Dreizahl ist damit nicht mehr nur Algebra, sondern Minimum einer Energie auf dem Kreis, den die Feldgleichung offen lässt.

## Teil B (nicht blind, Identität): Brannen-Form als Überlapp
- Überlapp ⟨U_θ, U_θk⟩ = cos(θ − θ_k) exakt. Für F = 1 + w·(Richtung bei θ) sind die Amplituden auf den Kopien a_k = 1 + w·cos(θ − θ_k).
- K = Σa_k²/(Σa_k)² = (2 + w²)/6 für jedes θ (Wolfram exakt). Also K = ⅔ genau bei w = √2. Mit θ = −δ ist das die Brannen-Form.
- Nur Bericht, nicht gewertet: w² = |Im F|²/|Re F|² = 2. Ein Bezug zur Zählregel r67 (Gewicht 2 je Spin) liegt nahe, ist aber nicht hergeleitet.

## Teil C (blind): Phasen abseits der Minima
- δ_Im = 0,2222220: L/max = sin²(3δ) = 0,382381 (12,73° auf dem Kreis).
- δ_Re = 0,48399: L/max = 0,985947 (27,73°).
- Kriterium (< 0,01) verfehlt: Die gemessenen Phasen liegen nicht in Minima. Die Lage auf dem Kreis braucht weiter eine eigene Größe, wie φ bisher.

## Nachträglich (nicht gewertet)
- Die Baumlagen der Phasen sind π/12 (Im-Sektor) und π/6 (Re-Sektor, TM1-Baum H173). Dort ist L/max = ½ bzw. 1, also genau die Mitte und das Maximum
  der Leck-Energie. Die gemessenen Phasen liegen um den gemeinsamen Versatz φ ≈ 2,27° daneben. Ob diese Lagen (Mitte, Maximum) eine Bedeutung haben,
  ist offen und wäre ein eigener Test mit Vorab-Notiz.

## Hergeleitet, gesetzt, offen
- **Hergeleitet:** L(θ) = 42 sin²3θ; drei nicht entartete Minima genau an den Kopien; K(w) = (2 + w²)/6 unabhängig von θ.
- **Gesetzt:** Die Energie selbst (quadratische Selbstwechselwirkung, Leck als Projektion auf das Komplement von span{1, U_θ}); Feldwert in span{1, U_θ}.
- **Bekannt vorab:** Lage der Nullstellen (H138, sin 3θ = 0).
- **Offen:** ob die Kopien die Generationen sind (H140–H143); die Lage der Brannen-Phasen auf dem Kreis (φ, Teil C); der Grund für w = √2.

## Werkzeuge und Grenzen
Python (numerisch, 360 Winkel, Fourier) und Wolfram (symbolisch, exakt; Hinweis „undefined2“ betrifft nur lokale Namen). Qiskit nicht einschlägig.
Die Energie ist eine natürliche, aber gewählte Größe; eine andere Wechselwirkung könnte andere Gewichte geben. Das Ergebnis zeichnet die drei Kopien
energetisch aus, es identifiziert sie nicht mit den drei Generationen.
