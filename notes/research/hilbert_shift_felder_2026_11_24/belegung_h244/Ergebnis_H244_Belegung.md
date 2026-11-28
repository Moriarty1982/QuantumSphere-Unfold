# Ergebnis H244 (k461): Folgt die Belegung (2/3, 1/6, 1/6) aus der Kopien-Regel H242?

**Datum:** 2026-11-28. **Vorab:** `Vorab_H244_Belegung.md` (Commit b2f0677, vor der Rechnung). **Urteil: trägt teilweise.**
- B fällt: Die Belegung folgt **nicht** aus der Schlussregel g₁+g₂+g₃ ≡ 0.
- C gilt: Der Baum erreicht sie nur bei δ_ν = π/6.

Der Kern der Hypothese trägt damit nicht. Was bleibt, ist eine ℤ₃-Lesart des Punkts π/6, keine neue Herleitung.

## Rechnung
- Python `k461_test_h244.py` → `k461_out.txt` (Maschinerie k370 unverändert).
- Wolfram `k461b_gegenprobe.wl` → `k461b_out.txt`, exakt, mit unabhängig angesetzter Ladungsbasis. Beide Rechnungen stimmen überein.
- Qiskit ist nicht einschlägig.

## Befunde
- **A (nicht blind):**
  - Jede schließende Vollbelegung ist rein, also (1,0,0), (0,1,0) oder (0,0,1).
  - Das Mittel über die 9 schließenden ist (1/3, 1/3, 1/3), ebenso das Mittel über alle 27.
  - Keine davon gibt (2/3, 1/6, 1/6). Das war erwartet.
- **B (fällt):**
  - Von 63 Mustern tragen genau 9 die Anteile (2/3, 1/6, 1/6): das sind **zwei besetzte Kopien mit gleicher Phase** (g, g), an jeder der drei Stellen.
  - Die Schlussregel trifft davon nur (0, 0): |M ∩ S| = 3 von |S| = 21.
  - Die phaseninvariante Fassung enthält M (M ⊂ S_inv), ist aber mit 45 Mustern viel größer.
  - Grund: Die Anteile hängen nur von der relativen Phase ab, der Schluss dagegen von der absoluten.
- **Klassen nach Besetzung (exakt):**
  - Eine Kopie besetzt gibt (1/3, 1/3, 1/3).
  - Zwei Kopien geben je eine Permutation von (2/3, 1/6, 1/6). Klasse 0 bekommt 2/3 genau bei gleicher Phase.
  - Drei Kopien geben entweder rein (9 Muster) oder (1/3, 1/3, 1/3) (18 Muster).
  - Nur Bericht: zwei Kopien mit **entgegengesetztem Vorzeichen** (ℤ₆-Phase, außerhalb ℤ₃), etwa (1, 0, −1), geben (0, ½, ½). Das ist genau
    das Muster der θ₁₃-Richtungen aus H243.
- **C (gilt, blind):**
  - Allgemein gilt W₀(b, c) = (9 + 2c²)/(9 + 12b² + 6c²). W₀ = 2/3 liegt auf der Ellipse c² + 4b² = 3/2.
  - Der Baum ist nur für δ_ν ∈ [0, π/6] reell; dort gilt b² = cos δ(cos δ − √3 sin δ)/2 und c = −√2 sin(δ + π/6).
  - Auf dieser Kurve steigt W₀ streng von 5/9 (δ = 0) über 11/18 (π/12) bis 2/3 am Rand δ = π/6, wo b = 0.
  - Die einzige Nullstelle von W₀ − 2/3 ist π/6 (Wolfram Reduce).
  - Jenseits von π/6 wäre b² < 0. Dort klemmt `Nhat` b auf 0, deshalb sind die Werte für δ > π/6 in k461_out kein gültiger Baum.

## Hergeleitet, gesetzt, nicht blind, nachträglich
- **Hergeleitet (exakt):**
  - die Klassenanteile aller 63 Muster;
  - W₀(b, c) und die Ellipse;
  - W₀ entlang des Baums und die einzige Nullstelle π/6.
- **Gesetzt:**
  - Ladungsbasis; Kopie j ↔ Flavour-Position j nach e₂ ↦ −e₂;
  - Belegungen mit ℤ₃-Phasen;
  - Schlussregel H242 auf die besetzten Kopien übertragen.
- **Nicht blind:** A, und in B die Zweierbelegungen mit gleicher Phase (beide vorab überlegt).
- **Nachträglich:**
  - Mögliche Lesart: Der TM1-Baum ist der Punkt, an dem die Ladungsbelegung des Baums gleich der seiner festen Spalte v₀ wird, nämlich „zwei Kopien in Phase“.
    Die θ₁₃-Richtungen sind „zwei Kopien gegenphasig“.
  - Das ist eine Umformulierung von H173 (π/6 war dort schon hergeleitet), kein neuer Grund.
  - Gegenphase braucht ℤ₆ statt ℤ₃.

## Folgen
- OP4 bleibt offen. Kein früheres Urteil kippt; die φ-Ruheregel ist unberührt.
- Die Kopien-Schlussregel H242 legt die Mischung nicht fest; sie ist gegen eine gemeinsame Phase nicht invariant, die Klassenanteile schon.
- Möglicher nächster Schritt, nur falls Marc will: ob eine ℤ₆-Fassung (Vorzeichen als halbe Kopien-Drehung) Baum und θ₁₃ in einer Regel fasst.
