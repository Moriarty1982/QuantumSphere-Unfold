# Vorab-Notiz H4: TM1 gegen TM2 — Vergleich 1:1

Festgelegt am 2026-10-20, **vor** dem gemeinsamen Datenvergleich. Baut auf H2 (normale Ordnung) auf.

## Herkunft

Die Triolen-Form t(1,1,1) + √2 Re(c(1,ω,ω²)) ist das Spektrum einer hermiteschen zyklischen Matrix; ihre
Eigenvektoren sind die festen Fourier-Vektoren. Die naive Mischung daraus ist ausgeschlossen (θ₁₃ ≈ 35°).
Zwei Minimalvarianten erhalten je eine Spalte des tribimaximalen Musters:

- **TM2:** zweite Spalte (1,1,1)/√3, die Skalar-Richtung t der Triole.
- **TM1:** erste Spalte (2,−1,−1)/√6, in der Triolen-Ebene.

Beide stammen aus der Literatur (trimaximale Mischung); geprüft wird hier nur der direkte Vergleich.

## Offenlegung vor der Festlegung

Bereits gesehen (Kopfrechnung bzw. Skript im Gespräch, vor dieser Notiz): TM2 gibt sin²θ₁₂ = 0,341, TM1 gibt
0,318 (gemessen 0,308); für TM1 folgt δ_CP ≈ 262° oder 98° bei sin²θ₂₃ = 0,47. Der θ₁₂-Teil des Vergleichs
ist also **nicht blind**. Blind sind: die δ_CP-Vorhersage von TM2, der gemeinsame Fit und das Urteil.

## Hypothese

**H4:** Genau eine der beiden Spalten ist erhalten. Beide Varianten haben gleiche Vorab-Gewichte (1:1) und
keine freien Parameter über die gemessenen θ₁₃, θ₂₃ hinaus; θ₁₂ und cos δ_CP sind jeweils festgelegt.

## Daten (verbindlich)

NuFIT 6.0 (arXiv:2410.05380), Tabelle 1, „IC24 with SK atmospheric data“, normale Ordnung:
sin²θ₁₂ = 0,308 (+0,012/−0,011); sin²θ₁₃ = 0,02215 (+0,00056/−0,00058); sin²θ₂₃ = 0,470 (+0,017/−0,013);
δ_CP = 212° (+26/−41).

## Verfahren (verbindlich)

- Für jedes Muster: Bedingung |U_e1|² = 2/3, |U_μ1|² = 1/6 (TM1) bzw. |U_e2|² = 1/3, |U_μ2|² = 1/3 (TM2).
- χ² über die vier Größen mit Gauß-Näherung und **asymmetrischen** Fehlern (Seite je nach Abweichung);
  θ₁₃ und θ₂₃ werden angepasst, θ₁₂ und δ_CP folgen; beide δ_CP-Zweige, der bessere zählt.
- Δχ² = χ²(TM2) − χ²(TM1). Bayes-Faktor ≈ exp(Δχ²/2), da beide gleich viele Parameter haben.
- Zusätzlich: χ² nur aus θ₁₂ und nur aus δ_CP getrennt ausweisen (der blinde Teil ist δ_CP).
- Vorhersagen für die Zukunft angeben: θ₁₂ (JUNO) und δ_CP-Bereich (DUNE, Hyper-K) je Muster.

Grenze der Methode: Die NuFIT-δ_CP-Verteilung ist nicht gaußförmig; die Gauß-Näherung ist eine Vereinfachung
und wird so benannt.

## Entscheidungskriterium (verbindlich)

- |Δχ²| < 2: unentschieden.
- 2 ≤ |Δχ²| < 6: schwache Bevorzugung.
- |Δχ²| ≥ 6 (Verhältnis etwa 20:1): starke Bevorzugung.
- Ein Muster mit χ²_min > 9 bei 2 Freiheitsgraden (4 Größen, 2 angepasst) gilt zusätzlich für sich als
  disfavorisiert, unabhängig vom Vergleich.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
