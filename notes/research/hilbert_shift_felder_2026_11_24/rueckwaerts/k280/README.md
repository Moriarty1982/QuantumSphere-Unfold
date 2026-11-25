# Kopplung der beiden Felder: der Winkel wird 45°, die ℤ₂ geht in erster Ordnung verloren (Erkundung k280, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Koppelt man das Spin-1-Feld (ℤ₃-Vakuum, k278) an das Spin-2-Feld (flache Kreise, k279), dann wählt jede der drei niedrigsten
gemischten Invarianten denselben Punkt der flachen Richtung, den **Blockwinkel 45°** (Achse u = (1, ±1, 0)/√2). Dieselbe Kopplung bricht aber die ℤ₂ des zweiten
Felds schon in erster Ordnung. Eine gemeinsame Restgruppe gibt es nicht.

Auftrag: Autor („rechne erstmal“). **Nicht blind:** Die Vorprüfung in Wolfram (k280b) zeigte vor der Rechnung, dass alle drei Kopplungen auf dem Kreis ∝ sin 2θ sind.
Damit steht der Winkel fest, und es ist eine Erkundung. H128 bleibt frei. Skripte **k280, k280b**.

Werkzeuge: Wolfram Language exakt für die gemischten Invarianten, ihre Form auf dem Kreis und die Mischungsspalte (k280b). Python (numpy, scipy) für den Abgleich
mit der Albert-Algebra aus k276 und das volle Minimum aus Zufallsstarts (k280). Qiskit nicht eingesetzt (keine Schaltung).

## Vorwissen geprüft
k278 (ein Feld, ℤ₃), k279 (Spin 2, drei Kreise, ℤ₂ generisch, V₄ an Punkten), r60 (A₄, Spin 3), H39 (ℤ₃ für Dirac-Sektoren, ℤ₂ → TM2 für Neutrinos, V₄ → trimaximal widerlegt),
k256/H8 (TM1 über K∘S₀), Literatur (Altarelli–Feruglio: Fehlausrichtung durch Kopplung von φ_T und φ_S ist das bekannte Ausrichtungsproblem).

## Ergebnisse
1. **Gemischte Invarianten (k280 A, k280b):** I₁₁ = Tr(Z_v∘Z_S) = **2(b − a)·Σvₖsₖ**. Schon die Bilinearform mischt das Spin-1-Feld mit der Nebendiagonale des
   Spin-2-Felds (beide sind A₄-Tripletts); sie verschwindet nur für a = b. I₂₁ und I₁₂ stehen in `k280b_out.txt`. Algebra gegen 3×3-Matrizen: 10⁻¹⁴.
2. **Auf der flachen Richtung (k280 B, k280b):** Mit v = v₀(1,1,1) und u = (cos θ, sin θ, 0) gilt exakt I₁₁ = √6(b − a)v₀·sin θ cos θ/√(1 + b²),
   I₂₁ = √6(a² + 2ab − 1)v₀²·sin θ cos θ/√(1 + b²), I₁₂ = (b − a)v₀·sin θ cos θ/√(1 + b²). Alle drei ∝ sin 2θ. Extrema bei **θ = π/4 und 3π/4**, also weder am V₄-Punkt
   (θ = 0) noch irgendwo dazwischen. Dort hat der 2×2-Block gleiche Diagonale, das ist maximale Mischung zweier Plätze.
3. **Volles Minimum (k280 C):** V = V₁ + V₂ + ε·I₁₁ mit a = 1, b = 0,5. Für ε = 0 ist der Winkel frei (Einzelfelder ℤ₃ und ℤ₂). Für jedes ε ≠ 0 liegt der Blockwinkel
   bei 45,00° (40/40 Starts je ε). Zugleich wachsen die kleinen Nebendiagonalen linear: |s_klein/s_groß| = 0,0013; 0,013; 0,037; 0,11 für ε = 10⁻³; 10⁻²; 0,03; 0,1.
   Auch das erste Feld verlässt (1,1,1) in erster Ordnung. Restgruppen: beide Felder einzeln und gemeinsam trivial.
4. **Lesart als Mischung (k280 D, Setzung):** Nimmt man den reellen Teil von Z_S als Massenmatrix des zweiten Sektors und den ersten Sektor ℤ₃-diagonal, dann ist die
   einzige festgelegte Spalte die der Achse u: **(2/3, 1/6, 1/6)** für u = (1, 1, 0)/√2 oder **(0, 1/2, 1/2)** für u = (1, −1, 0)/√2. Das sind die erste und die
   dritte Spalte der tribimaximalen Matrix. Welche auftritt, hängt am Vorzeichen von ε(b − a)κ₁c_N(a)κ₂. Die beiden anderen Eigenwerte sind entartet (2, −1, −1).

## Bewertung
- **Die flache Richtung wird aufgehoben, und zwar eindeutig.** Der freie Winkel aus k279 ist kein Mischungsparameter, sondern wird von der Kopplung auf 45° gesetzt,
  unabhängig davon, welche der drei Kopplungen wirkt und wie stark. V₄ (trimaximal, widerlegt) wird nicht gewählt.
- **(2/3, 1/6, 1/6) ist die TM1-Spalte.** Das ist die Struktur, die k256/H8 auf anderem Weg (K∘S₀) fand, und sie verträgt sich mit den Daten. Die Alternative
  (0, 1/2, 1/2) hat θ₁₃ = 0 und ist allein widerlegt. Das Vorzeichen entscheidet, und es ist hier frei. Eine Vorhersage ist das deshalb nicht.
- **Das Ausrichtungsproblem tritt genau wie in der Literatur auf:** ℤ₃ und ℤ₂ haben in A₄ nur die Eins gemeinsam, und die Kopplung, die den Winkel festlegt, verschiebt
  beide Vakua in erster Ordnung in ε. Die Spalte wandert dabei (0,668; 0,675; 0,691; 0,739 statt 2/3 für die genannten ε). Ohne einen Grund für kleines ε ist
  die TM1-Struktur nur genähert.
- **Grenzen:** Die Mischungslesart setzt die Massenmatrix gleich dem reellen Teil von Z_S. Mit der komplexen Phase χ des Eintrags ist die Spalte
  ((1 + cos χ)/3, …), also phasenabhängig (k280b). Zwei entartete Eigenwerte lassen zwei Spalten offen. Weiter gesetzt: die Felder, die Plätze als Generationen,
  a, b und alle Skalen. OP3 und OP4 bleiben offen, kein Guard ist berührt.

## Mögliche nächste Schritte
- **Blinder Test H128 wäre jetzt formulierbar:** Vorzeichen und Größe von ε aus der Algebra (etwa a = b erzwingt I₁₁ = 0, dann entscheidet a² + 2ab − 1 = 3a² − 1) und daraus,
  welche der beiden Spalten auftritt.
- **Aufspaltung der Entartung (2, −1, −1):** Erst sie legt die beiden anderen Spalten fest.

## Dateien
`k280_kopplung.py`, `k280_out.txt` (Python), `k280b_kopplung_exakt.wl`, `k280b_out.txt` (Wolfram). Aufruf aus diesem Ordner, benutzt `../h127/k276_test_h127.py`.
