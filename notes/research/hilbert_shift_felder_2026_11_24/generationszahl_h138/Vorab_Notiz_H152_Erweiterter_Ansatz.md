# Vorab-Notiz H152: Der abgeschnittene Ansatz, erweitert um alle zulässigen Viertordnungs-Terme und die HS(3)-Rückwirkung

**25.11.2026, vor jeder Rechnung committet.** Anlass: Autor „probiere erst den abgeschnittenen ansatz“. Lesart (mit dem Koordinator): Der skalenfreie Fluss aus H150/H151
ist nach dem einen Kopplungsterm κ abgeschnitten; er wird um die fehlenden Terme erweitert. Die 1:2-Normierung kommt später als eigener Test. Falls „abgeschnitten“ die
Abschneidung Λ (Skala als Setzung) meinte: Das ist in H150b schon gerechnet (θ → cos 2θ = c_L/f²); dann wird nachgefragt. Vergeben: H152, Skripte k335 (Python) und
k335b (Wolfram). Qiskit nicht vorgesehen. Kein HDL/MMA-Vergleich.

## Vorwissen geprüft
- H150/H151 (k333/k334): V = λ_A A² + κAB + λ_B B² mit A = φ² (HS(0)-Einheit), B = |y|² (Kopien-Ebene, 2 Komponenten); Koide-Kondensat nur für κ < 0; mit 1 gegen 2
  Komponenten K am GW-Punkt startabhängig 0,6667 … 0,6778, Grenzwert 1/3 + √10/9; der Fluss ist O(2)-invariant und lässt δ frei.
- H149: δ sieht nur die kubische Norm N(W) = c₀c₁c₂ über cos 3δ; ohne Anpassung nur δ = 0, π/3 (entartet) oder π/12 (N(W) = 0).
- H133 (k302): HS(3)-Anhang koppelt über einen Term κ_C·A·C an vier entartete Felder C (Higgs-artig).
- H11/H16: Potentiale in den Slot-Normen bis Grad sechs ohne Minimum mit drei verschiedenen Normen.

## Der erweiterte Ansatz (vorab festgelegt)
Felder: φ (1 Komponente), y = (y₁, y₂) Kopien-Ebene, C (4 Komponenten, Rückwirkung von HS(3)). Symmetrie: Z₃ ⋊ Z₂ der drei Kopien (statt O(2)) und O(4) auf C.
Skalenfrei heißt: nur Terme vierter Ordnung. Die zulässigen Invarianten vierter Ordnung sind dann genau
φ⁴, φ²B, B², **φ·C₃(y)** mit C₃ = y₁³ − 3y₁y₂² (= Re(y₁ + iy₂)³), sowie φ²|C|², B|C|², |C|⁴.
Der neue Term ξ·φ·C₃ ist die skalenfreie Form der kubischen Norm: φ·N(W) enthält φ⁴, φ²B und φC₃. Die Rechnung prüft, dass die Liste vollständig ist und dass ½Tr(∂²V)²
in ihr schließt.

## Hypothesen und Kriterien
- **H152a (gewertet):** Die Liste der Z₃-invarianten Terme vierter Ordnung ist vollständig, und die Einschleifen-β-Funktionen schließen in ihr. *Kriterium:* symbolischer
  Nullrest. Vorhersage: bestätigt.
- **H152b (gewertet, offen):** Startwertabhängigkeit. Es wird ein Gitter gerechnet: λ_A = λ_B = λ ∈ {0,1; 0,2; 0,3}, κ/λ ∈ {−1,5; −1,0; −0,5; −0,2}, ξ/λ ∈ {−0,4; −0,2; −0,1;
  0,1; 0,2; 0,4}, κ_C ∈ {0; 0,2} (mit κ_BC = 0, λ_C = 0,2). Ins Infrarote integriert bis zum ersten τ, an dem das Minimum von V auf der Einheitskugel null wird
  (Gildener–Weinberg). Dort Richtung, Amplituden c_k, K und δ. *Kriterium:* „fester Punkt“, wenn die Streuung von K über das Gitter < 10⁻³ ist; sonst „startabhängig“.
  Vorhersage: startabhängig.
- **H152c (gewertet):** δ am GW-Punkt. Vorhersage: δ landet auf 0 oder π/3 (zwei gleiche Massen) bzw. bei ξ = 0 bleibt es frei; kein Gitterpunkt gibt drei verschiedene Massen
  mit δ innerhalb 1 % von 2/9. *Kriterium:* Anteil der Punkte mit drei verschiedenen Massen und |δ/0,22222 − 1| < 1 %. Bestätigt bei 0.
- **H152d (gewertet):** K am GW-Punkt gegen den Messwert 0,666661 ± 0,000007. *Kriterium:* Anteil der Punkte innerhalb 3σ. Vorhersage: kein Punkt (außer zufällig);
  weil das Gitter grob ist, wird zusätzlich berichtet, ob K = ⅔ im Bereich der erreichten Werte liegt (dann wäre es mit einem gewählten Startwert erreichbar, also ein Fit).
- **H152e (gewertet):** π/4 stabil? Polwinkel θ am GW-Punkt. *Kriterium:* Anteil mit |θ − π/4| < 0,01. Vorhersage: der ξ-Term verschiebt θ zusätzlich (er ist ungerade
  in φ), also eher weniger Punkte nahe π/4 als in H150d.

## Grenzen
- Eine Schleife, ohne Eichfelder und ohne die Zusatzterme K₁–K₄. Die Ankopplung von C nur über φ²|C|² ist eine Lesart von H133.
- Vorzeichen werden nicht gesetzt: ξ und κ_C laufen über beide Vorzeichen; κ < 0 ist die Klasse, in der nach H150 überhaupt ein Koide-Kondensat entsteht.
- OP3 offen; kein Guard wird berührt.
