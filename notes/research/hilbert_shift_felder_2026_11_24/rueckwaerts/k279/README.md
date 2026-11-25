# Zweites Feld im Spin-2-Teil: ℤ₂ nur als entartetes Vakuum (Erkundung k279, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Ein einzelnes Feld im Spin-2-Teil (reell symmetrisch, spurfrei), gemischt mit seiner Ladungsdrehung (Z_b = S + b·C·S),
hat als Vakuum **keinen isolierten ℤ₂-Punkt**, sondern drei Kreise gleicher Tiefe. Auf ihnen ist die Restgruppe fast überall **ℤ₂**, an drei Punkten je Kreis
die Kleinsche Vierergruppe **V₄**. Ein Ein-Feld-Potential kann zwischen beiden nicht wählen, in keiner Ordnung.

Auftrag: Autor („mach die rechnung bitte“, „weiter“), geplant als blinder Test H128. **Nicht blind, daher Erkundung:** Beim Aufschreiben der Vorab-Notiz
ergab sich die Zerlegung in Punkt 2, aus der das Ergebnis vor der Rechnung folgt. Nach der Regel „nicht blind = offen sagen“ läuft das als Erkundung;
**H128 bleibt frei.** Die ursprünglich erwogene Vorhersage („ℤ₂ für alle b ≠ 0“) wäre nach Wortlaut teilweise eingetreten (ℤ₂ generisch, aber auch bei b = ±√3 nichts,
und nie isoliert). Skripte **k279, k279b**.

Werkzeuge: Python (numpy, scipy) mit der Albert-Algebra aus k276 (Invarianten gegen Formel, Maxima von N aus Zufallsstarts, Stabilisator in A₄).
Wolfram Language exakt für Formeln, Zerlegung, Maximum und die flache Richtung (k279b). Qiskit nicht eingesetzt (keine Schaltung).

## Vorwissen geprüft
k278 (ein Feld im Spin-1-Teil: nur |v|² und xyz, ℤ₃ erzwungen, ℤ₂ braucht ein zweites Feld), r60 (H127: Brechung ist reiner Spin 3; farbneutraler Teil
H₃(ℂ) = 1 ⊕ 3 ⊕ 5 unter der Familien-SO(3)), k277 (N(CX) = −2xyz), H39 (ℤ₂ → TM2 für Neutrinos; Klein → trimaximal, widerlegt), k256/H8 (TM1 über K∘S₀).

## Ergebnisse
1. **Invarianten (k279 A, k279b):** Mit Diagonale a (Σa = 0) und Nebendiagonale s_k(1 + i·b) gilt exakt Tr Z² = |a|² + 2(1 + b²)|s|² und
   **N(Z) = a₁a₂a₃ + 2(1 − 3b²)·s₁s₂s₃ − (1 + b²)·Σ aₖsₖ²**. In der Algebra geprüft auf 3·10⁻¹⁴. Jedes Ein-Feld-Potential ist V = f(Tr Z², N) (Cayley–Hamilton, k278).
2. **Zerlegung (k279 B, k279b):** Mit t = √(1 + b²)·s und γ = (1 − 3b²)/(1 + b²)^{3/2} = cos 3φ (tan φ = b) ist
   **N = ½[(1 + γ)·det(D + T) + (1 − γ)·det(D − T)]**, ein gewichtetes Mittel zweier reeller Determinanten. Für |γ| < 1 ist N also höchstens max det = 1/√54
   (auf der Schale Tr Z² = 1), und das wird genau dort erreicht, wo D + T und D − T beide maximal sind.
3. **Vakuum-Menge (k279 C, D, k279b):** Auf der det-Bahn M = (3uuᵀ − 1)/√6 gilt N − 1/√54 = −3√(3/2)·(1 − γ)·u₁²u₂²u₃². Die Maxima sind die drei Großkreise
   uₖ = 0. Numerisch: 60/60 Starts je b erreichen 1/√54, immer mit einem sₖ = 0, die Achse u streut über den ganzen Kreis. Stabilisator **ℤ₂** in 60, 60, 60, 59, 60
   von 60 Läufen für b = 0,25; 0,5; 1; 2; 4 (der eine Ausreißer bei b = 2 ist Konvergenz, dort ist 1 + γ = 0,016). An u = eₖ ist der Stabilisator V₄.
   N ist entlang des Kreises exakt konstant (Wolfram).
4. **Volle Entartung bei b = 0 und b = ±√3:** Dort ist γ = ±1 und N = det(D ± T), also SO(3)-invariant. Keine Ausrichtung (Stabilisator trivial in 60/60).
   Das ist dieselbe Phase π/3 wie in k278, dort als Maximum des kubischen Terms.

## Bewertung
- **ℤ₂ kommt vor, ist aber nicht festgelegt.** Die ℤ₂ ist die Drehung um die Koordinatenachse senkrecht zum Kreis (Vorzeichenwechsel zweier Plätze), also dieselbe
  Klasse wie die ℤ₂ der Neutrino-Lesart (H39). Das Ein-Feld-Prinzip aus k278 gibt im Spin-2-Teil aber eine **flache Richtung**: Der Winkel auf dem Kreis ist frei,
  und er entscheidet zwischen ℤ₂ und V₄. Die V₄-Punkte sind die diagonalen Felder, und V₄ führt nach H39 auf trimaximale Mischung (widerlegt).
- **Die flache Richtung ist exakt** für jedes Ein-Feld-Potential, weil V nur von Tr Z² und N abhängt. Aufheben kann sie nur etwas außerhalb des Prinzips:
  eine Kopplung an das erste Feld (Spin 1, ℤ₃-Vakuum aus k278), ein Term außerhalb der Albert-Invarianten oder Quantenkorrekturen.
- **Der Winkel auf dem Kreis ist ein freier Parameter.** Ob er mit einem Mischungswinkel zusammenhängt (TM2 hat genau einen freien Winkel), ist eine naheliegende
  Frage, hier aber nicht geprüft. Das wäre ein Kandidat für einen blinden Test H128, wenn sich vorab eine Größe festlegen lässt.
- Weiter gesetzt: das zweite Feld im Spin-2-Teil, die drei Plätze als Generationen, die Ladungsmischung b, alle Skalen. OP3 und OP4 bleiben offen, kein Guard ist berührt.

## Mögliche nächste Schritte
- **Kopplung der beiden Felder:** Spin-1-Feld im ℤ₃-Vakuum (1,1,1) plus Spin-2-Feld; hebt die gemischte Invariante Tr(Z_v ∘ Z_S ∘ …) die flache Richtung auf, und wohin?
- **Winkel und Mischung:** die Massenmatrix aus dem Spin-2-Vakuum entlang des Kreises mit TM2 vergleichen (H39).

## Dateien
`k279_spin2_feld.py`, `k279_out.txt` (Python), `k279b_spin2_exakt.wl`, `k279b_out.txt` (Wolfram). Aufruf aus diesem Ordner, benutzt `../h127/k276_test_h127.py`.
