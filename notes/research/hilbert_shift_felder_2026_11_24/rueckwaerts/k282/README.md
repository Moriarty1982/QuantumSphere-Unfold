# Was die SU(3)-Entartung aufhebt: die zwei Abbildungen des Verdopplungsschritts (Erkundung k282, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Die beiden einfachsten Terme, die die Entartung aus k281 aufheben, sind keine freien Zutaten, sondern die zwei Strukturabbildungen des
Schritts ℝ → ℂ: die **Konjugation σ** (e₇ → −e₇) bricht SU(3) auf die Familien-SO(3), die **Einheit C** (Multiplikation mit e₇) bricht weiter auf die Würfelgruppe und
mit Ladungsmischung auf A₄. Ihre Vorzeichen bleiben frei, und sie entscheiden über das Vakuum: ℤ₃, V₄ oder eine flache ℤ₂-Richtung. Ein isoliertes ℤ₂-Vakuum trat nie auf.

Auftrag: Autor („merge dann weiter“; dazu sein Hinweis, der Hilbert-Shift könne die Brechung liefern). **Nicht blind:** Die Bilanz der Setzungen
(`../bilanz/Bilanz_Setzungen_k275_k281.md`) hatte vorab abgeleitet, dass die Spin-1/Spin-2-Masse allein die flache Richtung stehen lässt und der Diagonalterm zwischen V₄ und 45° wählt.
Teil C (Herkunft der Terme) kam nach dem Hinweis des Autors dazu. Die Hilbert-Shift-Idee selbst rechnet ein eigener Thread (ab k283). Skripte **k282, k282b**.

Werkzeuge: Python (numpy, scipy) mit der Albert-Algebra aus k276; Wolfram Language exakt für die quadratischen Formen (k282b). Qiskit nicht eingesetzt.

## Vorwissen geprüft
k281 (SU(3)-Entartung), k278–k280, r60 (C bricht SO(3) → A₄; ungerade Elemente wechseln das Vorzeichen von C), k253 (Turm als Cayley–Dickson-Verdopplung), H39.

## Ergebnisse
1. **Die zwei Terme (k282 A, C, k282b):** Tr((CW)∘(CW)) = Tr W² − |d|² und, für c = 0, Tr(W∘σW) = Tr W² − 4|v|². Der erste trennt Diagonale von Nebendiagonale, der zweite
   Spin 1 von Spin 2. Mit Ladungsmischung c gilt Tr(W∘σW) = |d|² + 2[(1 − c²)(|s|² − |v|²) − 4c·s·v].
2. **Symmetrie (k282 C):** In su(3) erhält Tr W² alles (Dimension 8), dazu Tr(W∘σW) nur so(3) (Dimension 3), dazu Tr((CW)²) nichts Kontinuierliches. Von den 24 Würfeldrehungen
   erhalten bei c = 0 alle die Norm N(W), bei c ≠ 0 nur 12 (A₄).
3. **Vakuum je Vorzeichen (k282 B, 40 Starts je Punkt, c = 0,5 und 1):**

   | Diagonalterm d_d | Spin-1-Term d_v | Restgruppe | flache Richtungen |
   |---|---|---|---|
   | 0 | 0 | keine | 4 (k281) |
   | 0 | + (Spin 1 schwer) | ℤ₂ | 1 (Kreis aus k279, Spin-1-Anteil 0) |
   | 0 | − (Spin 1 leicht) | **ℤ₃** | 0 |
   | + | 0 | keine | 2 |
   | − | 0 | **V₄** | 0 |
   | + | + | **ℤ₃** | 0 (Spin-1-Anteil klein, 0,04 bis 0,13) |
   | − | + | **V₄** | 0 |
   | + | − | **ℤ₃** | 0 |
   | − | − | ℤ₂ | 1 bis 2 (Spin-1-Anteil 1) |

## Bewertung
- **Der Hinweis des Autors trifft in einem genauen Sinn zu:** Der Verdopplungsschritt bringt mehr Dimensionen (H₃(ℝ) mit 6 → H₃(ℂ) mit 9) und für die nackte Algebra mehr Symmetrie
  (SO(3) → SU(3)). Merkt sich das Feld aber, woher es kommt, also σ und C, dann fällt die Symmetrie auf SO(3) und weiter auf A₄. Das ist die Kette aus r60, jetzt für das Potential.
- **σ ist die Ladungskonjugation.** Tr(W∘σW) koppelt das Feld an sein Konjugiertes und ist damit vom Majorana-Typ. Dass ein solcher Term die Familiensymmetrie von SU(3) auf SO(3)
  senkt, ist aus der Flavourphysik bekannt. Hier folgt es aus der Algebra. Das ist eine Lesart und keine Vorhersage.
- **Die Vorzeichen bleiben frei**, und mit ihnen die Restgruppe. ℤ₃ ist robust (vier von acht Vorzeichenfällen), V₄ auch (zwei). ℤ₂ erscheint nur mit flacher Richtung, wie in der
  Bilanz vorab abgeleitet. Die Zwei-Sektoren-Lesart aus H39 (ℤ₃ und ℤ₂) kommt so nicht heraus.
- Korrektur zur Bilanz: Dort stand „d_d > 0 wählt 45°“. Der Blockwinkel ist tatsächlich 45,0°, die Restgruppe dabei aber ℤ₃ oder keine, nicht ℤ₂.
- Weiter gesetzt: die Plätze als Generationen, c, alle Skalen. OP3 und OP4 bleiben offen, kein Guard ist berührt.

## Mögliche nächste Schritte
- **Vorzeichen aus dem Turm** (läuft im parallelen Thread ab k283): Legt die Verdopplungsregel fest, mit welchem Vorzeichen σ und C eintreten? Dann wäre die Restgruppe eine Vorhersage,
  und H128 könnte blind sein, weil die Tabelle oben vorab festliegt.
- **Der nächste Schritt ℂ → ℍ** (H₃(ℍ), Sp(3)): dieselbe Rechnung eine Stufe höher.

## Dateien
`k282_a4_massen.py`, `k282_out.txt` (Python), `k282b_exakt.wl`, `k282b_out.txt` (Wolfram). Aufruf aus diesem Ordner, benutzt `../h127/k276_test_h127.py`.
