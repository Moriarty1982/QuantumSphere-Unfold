# Beide Felder als ein Element: die Algebra legt das Vorzeichen nicht fest, sie hebt die Ausrichtung ganz auf (Erkundung k281, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Fasst man das Spin-1-Feld und das Spin-2-Feld als Teile **eines** Elements W der Albert-Algebra auf, dann füllen sie zusammen den ganzen
spurfreien Teil von H₃(ℂ), das Potential ist SU(3)-invariant, und das Vakuum ist eine ganze Bahn (ℂP²) ohne Restgruppe. Weder das Vorzeichen aus k280 noch der Winkel 45°
noch die ℤ₃-Ausrichtung aus k278 sind dann festgelegt.

Auftrag: Autor („dann mach das“), gedacht als blinder Test H128 („legt die Algebra das Vorzeichen fest?“). **Nicht blind, daher Erkundung:** Beim Festlegen des Prinzips für
die Vorab-Notiz zeigte sich, dass 3 + 5 = 8 Dimensionen genau die spurfreien hermiteschen 3×3-Matrizen sind. Damit steht das Ergebnis ohne Rechnung fest.
**H128 bleibt frei.** Skripte **k281, k281b**.

Werkzeuge: Python (numpy, scipy) mit der Albert-Algebra aus k276 (Abgleich, Maxima aus Zufallsstarts, Hesse-Matrix). Wolfram Language exakt für die Determinante der
Feldabbildung und die Höhe des ℤ₃-Vakuums (k281b). Qiskit nicht eingesetzt.

## Vorwissen geprüft
k278 (ein Feld, Spin 1, ℤ₃), k279 (ein Feld, Spin 2, Kreise), k280 (Kopplung, 45°, Spalte je nach Vorzeichen), r60 (farbneutraler Teil H₃(ℂ) = 1 ⊕ 3 ⊕ 5, Familien-SO(3) ⊂ SU(3)),
r42 (Projektor ½(1 + iL_e₇)), H39.

## Ergebnisse
1. **Ein Element (k281 A, k281b):** W = Z_v(a) + Z_S(b) hat die Nebendiagonale wₖ = (1 + ib)sₖ + (−a + i)vₖ. Die Abbildung (sₖ, vₖ) → wₖ hat Determinante **1 + ab**.
   Für ab ≠ −1 ist jede spurfreie hermitesche 3×3-Matrix ein W. Jedes Potential V = f(Tr W², N(W)) ist dann unter W → UWU⁺ mit U ∈ SU(3) invariant.
2. **Vakuum (k281 B):** Die Maxima von N auf der Schale sind die Bahn W = (3ψψ⁺ − 1)/√6. Numerisch erreichen 60 von 60 Starts je (a, b) die Höhe 1/√54 mit Eigenwerten
   (2, −1, −1)/√6, an lauter verschiedenen Punkten: Restgruppe in A₄ trivial in 180 von 180 Läufen, Spin-1-Anteil zwischen 0,01 und 1,08, größte Mischungsspalte zwischen 0,35 und 0,99.
3. **Die Zwei-Feld-Vakua aus k280 (k281 C)** liegen bei passendem Mischungsverhältnis auf dieser Bahn, und zwar für **beide** Vorzeichen. Sie sind nicht ausgezeichnet.
4. **Das ℤ₃-Vakuum aus k278 (k281 D, k281b)** hat im vollen Raum die Höhe |3a − a³|/(1 + a²)^{3/2} · 1/√54. Das ist kleiner als 1/√54, außer bei **a = ±1/√3**. Sonst ist es ein
   Sattel mit drei instabilen Richtungen.

## Bewertung
- **Die Frage aus k280 ist beantwortet, aber anders als erhofft:** Das Ein-Element-Prinzip legt zwar alle Kopplungen fest, macht das Potential aber zu symmetrisch. Die
  Ausrichtungen aus k278 bis k280 (ℤ₃, ℤ₂, 45°, TM1-Spalte) entstehen allein dadurch, dass die Felder **von Hand auf Teilräume eingeschränkt** wurden (nur Spin 1, nur Spin 2,
  kleine Kopplung). Das ist eine Setzung und kein Ergebnis der Algebra.
- **Was gebraucht wird:** ein Grund, der Spin 1 und Spin 2 trennt, also ein Term, der unter der Familien-SO(3) oder A₄ invariant ist, aber nicht unter SU(3). Der einfachste ist
  eine getrennte Masse für die beiden Anteile (μ₁² ≠ μ₂²). Er liegt außerhalb der Albert-Invarianten eines Elements.
- **Ausnahme a = ±1/√3:** Dort ist das ℤ₃-Vakuum auch im vollen Raum ein Minimum. Das ist die Phase, bei der der kubische Term in k278 maximal ist. Ob sie ausgezeichnet ist,
  ist offen (r42 legt a = 1 nahe, dort ist es ein Sattel).
- Weiter gesetzt: die Plätze als Generationen, alle Skalen. OP3 und OP4 bleiben offen, kein Guard ist berührt.

## Mögliche nächste Schritte
- **Getrennte Massen μ₁² ≠ μ₂²** als kleinste Brechung von SU(3) auf SO(3): Welche Punkte der Bahn überleben? Hier könnte ein blinder Test H128 liegen, wenn sich das Ergebnis
  nicht vorab ablesen lässt.
- **Bilanz der Setzungen** für k277 bis k281, bevor weitergerechnet wird: was hergeleitet ist (A₄, Spin 3, xyz als Norm, No-go) und was gesetzt (Teilräume, Kopplungen).

## Dateien
`k281_ein_element_beide_felder.py`, `k281_out.txt` (Python), `k281b_exakt.wl`, `k281b_out.txt` (Wolfram). Aufruf aus diesem Ordner, benutzt `../h127/k276_test_h127.py`.
