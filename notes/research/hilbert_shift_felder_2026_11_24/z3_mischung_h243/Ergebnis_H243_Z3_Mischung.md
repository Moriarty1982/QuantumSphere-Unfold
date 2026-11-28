# Ergebnis H243 (k460): ℤ₃-Ladung an der Mischung

**Datum:** 2026-11-28. **Vorab:** `Vorab_H243_Z3_Mischung.md` (Commit d5f4315, vor der Rechnung). **Urteil: trägt teilweise.**
Die θ₁₃ erzeugenden Richtungen sind rein ℤ₃-geladen (A2 in führender Ordnung, A3). Der TM1-Baum ist aber nicht ℤ₃-geschlossen (A1 fällt).
Damit ist θ₁₃ keine ℤ₃-Brechung eines geschlossenen Baums. Die ℤ₃-Regel ordnet nur, welche Richtungen θ₁₃ tragen können.

## Rechnung
- Python `k460_test_h243.py` → `k460_out.txt` (Maschinerie k370/k371 unverändert).
- Wolfram `k460b_gegenprobe.wl` → `k460b_out.txt`, exakt. Alle Anteile sind exakte Brüche und stimmen mit Python überein.
  Warnungen: nur Symbol::undefined2 (lokale Namen).
- Qiskit nicht einschlägig.

## Befunde
Die Klassenanteile [W₀, W₁, W₂] sind Frobenius-Anteile in der T-Eigenbasis t_k (Eigenwert ω^k).

| Größe | Regel | W₀, W₁, W₂ | Kriterium |
|---|---|---|---|
| N̂(π/6), Baum, exakt [[1,0,−√(3/2)],[0,1,0],[−√(3/2),0,1]] | Majorana (i+j) | 2/3, 1/6, 1/6 | **A1 fällt** (verlangt W₀ = 1) |
| b-Richtung (führend, b ∝ √x) | Majorana | 0, 1/2, 1/2 | **A2 gilt** (führende Ordnung) |
| c-Richtung (dc/dδ_ν = −1/√2, Ordnung x) | Majorana | 1/3, 1/3, 1/3 | gemischt |
| N̂(π/6−x) − N̂(π/6), voller Versatz | Majorana | 0,0039, 0,498, 0,498 | fast rein geladen |
| K₂ (θ₁₃-Richtung, massenerhaltend) | Dirac (j−i) | 0, 1/2, 1/2 | **A3 gilt** (nicht blind) |
| K₁ | Dirac | 1/3, 1/3, 1/3 | Bericht |
| S+b, S−q | Dirac | 0, 1/2, 1/2 | Bericht |
| S+c, S+d | Dirac | 1/3, 1/3, 1/3 | Bericht |
| S−p, K+ | Dirac | 2/3, 1/6, 1/6 | Bericht |

- **Zur Lesart von A2:** Die Vorab nennt ∂N̂/∂δ_ν bei π/6. Weil b ∝ √(π/6 − δ_ν), divergiert die Ableitung dort. Gewertet ist deshalb die führende
  Versatzrichtung (b-Richtung). Der Anteil der Ordnung x (c-Richtung) ist gemischt. Der volle Versatz hat W₀ = 0,0039, nicht ≤ 10⁻¹². Das ändert
  das Urteil nicht, weil A1 ohnehin fällt.
- **Gegenprobe mit der Konjugations-Regel (j−i) für Majorana:** gleiche Werte (W₀ = 2/3, 0, 1/3 für Baum, b, c).
- **Spalte v₀ = (1,0,1)/√2:** Gewichte 2/3, 1/6, 1/6, also gemischt (exakt).
- **Klasse-0-Projektion des Baums:** zurück in der Flavourbasis ergibt sie [[1, 1/√6, −1/√6], [1/√6, 1, 1/√6], [−1/√6, 1/√6, 1]].
  Die Mischung daraus hat s₁₂ = 0, s₂₃ = ½, s₁₃ = 0; der Baum selbst hat s₁₂ = 1/3. Der Wert sin²θ₁₂ = 1/3 kommt also aus dem geladenen Teil des Baums.
- **Zufallskontrolle:**
  - symmetrisch: W₀ ≥ 1 − 10⁻⁶ in 0/10 000, mittleres W₀ 0,334;
  - antisymmetrisch: W₀ ≤ 10⁻⁶ in 12/10 000 (0,0012, knapp über der für „trägt“ genannten Schwelle 10⁻³), mittleres W₀ 0,336.
  - Rein geladene Richtungen sind in Zufallsmatrizen selten. Dass K₂ und b rein geladen sind, ist daher eine echte Struktur und kein Zufall.

## Hergeleitet, gesetzt, nicht blind, nachträglich
- **Hergeleitet (exakt):** Klassenanteile oben; b(π/6) = 0; b-Richtung, K₂, S+b, S−q rein geladen; Baum W₀ = 2/3.
- **Gesetzt:**
  - Ladungsbasis = T-Eigenbasis.
  - Majorana-Regel (i+j) aus H242 ohne Konjugation, Dirac-Regel (j−i).
  - W₀ als Maß.
- **Nicht blind:** A3. Unter der Dirac-Regel ist Klasse 0 genau die Diagonale in der Ladungsbasis, und diag K₂ = 0 steht schon in H206.
- **Nachträglich:**
  - Die θ₁₃-erzeugenden Richtungen (b, K₂, S+b, S−q) fallen alle in dieselbe Klasse „rein geladen“. Ebenso fällt die massenerhaltende Richtung mit
    der rein geladenen zusammen.
  - θ₁₂ = 1/3 sitzt im geladenen Teil des Baums.
  - Mögliche Lesart, nicht getestet: TM1 ist ein Baum mit Vakuum in einer gemischten Kopien-Belegung, und θ₁₃ ist eine reine Ladungsanregung.

## Folgen
- OP4 (Mischung) bleibt offen. Kein Urteil H205–H213 und kein Befund H221–H242 kippt.
- φ-Ruheregel unberührt: H243 betrifft die Richtung, nicht die Stärke φ.
- Möglicher nächster Test: Ob eine Vakuum-Belegung g mit Gewichten (2/3, 1/6, 1/6), wie bei v₀ und dem Baum, aus der Kopien-Regel H242 folgt. Dann
  wäre der Baum selbst ℤ₃-bestimmt.
