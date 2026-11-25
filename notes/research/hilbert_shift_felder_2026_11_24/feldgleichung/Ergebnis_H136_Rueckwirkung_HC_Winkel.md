# Ergebnis H136: Die Rückwirkung über den HC-Winkel hält κ ≈ 1,2 nicht fest

**Stand:** 2026-11-25. Test nach Vorab-Notiz `notes/research/predictions/Vorab_Notiz_H136_Rueckwirkung_HC_Winkel.md` (Commit 50bb7e6, vor dem ersten Lauf).
**Teilweise nicht blind:** K-a stand vorab fest, das Vorzeichen in K-c war überschlagen, K-b war offen.
Skripte: `k305_test_h136.py` (Python: numpy, scipy), Ausgabe `k305_out.txt`; Gegenprobe `k305b_gegenprobe.wl` (Wolfram Language), Ausgabe `k305b_out.txt`.
Qiskit nicht eingesetzt (keine Schaltung). Kein Guard berührt. OP1 bis OP5 bleiben offen.

## Gesamturteil
**H136 widerlegt.**

| Kriterium | Vorhersage | Ergebnis |
|---|---|---|
| K-a (Eichlesart) | widerlegt (nicht blind) | **widerlegt**: mit geeichter SU(2) hängt keine Invariante am Winkel |
| K-b (Schleifen allein halten den Winkel) | offen, Vermutung widerlegt | **widerlegt**: die Lösung ist ein Minimum der Tiefe und braucht κ₂ < 0 |
| K-c (Steigung nach der Regel) | widerlegt | **widerlegt**: −0,77 gegen +1,59, falsches Vorzeichen |

## 1. Eichlesart (K-a)
Auf a = ψ₁ + χ·j gibt es unter SU(2) links mal U(1) rechts eine Invariante vom Grad 2 (A = A₁ + B) und eine vom Grad 4 (A²). A₁ − B, also cos 2θ, ist nicht
invariant (unter L_j wird daraus −4x₀x₂ + 4x₁x₃). Ein ruhender Winkel θ ist dann Eichung (k299), und keine Schleife kann von ihm abhängen. Eine
Rückwirkung über einen ruhenden Winkel gibt es nur, wenn bloß U(1) links und rechts gelten (2 Invarianten vom Grad 2, 3 vom Grad 4).

## 2. Modell U mit HC-Strafe
Mit V = η(B − μ²A₁)² + (κ₁A₁ + κ₂B)·C verschiebt die Schleife des Anhangs den Winkel um Δθ = 0,0098·(κ₂ − κ₁)/η (im Bogenmaß). Für η = 1 und κ₂ − κ₁ = ±0,5 sind
das ±0,28°, für η = 0,1 sind es ±2,8°. Die Rückwirkung existiert in diesem Modell, sie ist klein und hängt an zwei freien Zahlen.

## 3. Schleifen allein (K-b, K-c)
Ohne HC-Strafe (η = 0) müsste die Schleife den Winkel selbst halten. Die zwei Bedingungen (Tiefe F stationär bei θ₀ = 16,79°, κ_eff(θ₀) = κ*) haben genau
eine Lösung: **κ₁ = 1,321, κ₂ = −0,078.**
- κ₂ ist negativ, liegt also außerhalb des zulässigen Bereichs. Für θ > 76° hätte der Anhang ein negatives Massenquadrat.
- Die zweite Ableitung von F nach θ ist dort positiv (+0,0011): θ₀ ist ein **Minimum** der Tiefe. Der Winkel liefe von θ₀ weg, die Tiefe wächst zu größeren
  Winkeln (größtes F im zulässigen Bereich bei 67,5°).
- Die Steigung dκ_eff/dθ ist −0,774. Die Regel κ = 1/cos 2θ verlangt +1,594. Mit der Steigung der Regel (κ₂ − κ₁ = 2,88) ist F bei θ₀ nicht stationär.
- Kontrolle: Hängt die Top-Masse nicht an θ, ist F nur für κ₁ = κ₂ stationär, und dann ist F in θ flach. Dann gibt es gar keine Rückwirkung.

## Bilanz der drei Versuche zum Wert von κ
| Schritt | gefragt | Ergebnis |
|---|---|---|
| H133 (k302) | legt der Turm κ fest? | Form ja (ein Term, vier entartete Felder), Wert nein |
| k303 | welche Regel gäbe 1,2? | keine mit Prinzip; ein Zahlentreffer κ = (γ_L + 1/γ_L)/2 |
| H135 (k304) | hält sich 1,2 selbst? | nein: kein fester Punkt, Tiefe monoton |
| H136 (k305) | hält es sich über den HC-Winkel? | nein: mit SU(2) keine Rückwirkung, ohne SU(2) instabil und falsches Vorzeichen |

Gesetzt war in allen vier Schritten: skalenfreies Bild, eine Schleife, die 125 GeV als Schleifen-Skala, γ_L und μ als eingesetzte Zahlen (OP1). Der
Zahlentreffer bleibt eine unerklärte Auffälligkeit. Mit den hier geprüften Mechanismen lässt er sich nicht stützen.

## Was noch offen ist
Der Winkel ist unter SU(2) nur für eine **drehende** Lösung messbar (Stromverhältnis, k299). Eine Rückwirkung müsste dann über die Drehung laufen, nicht
über ein ruhendes Potential: Der Anhang müsste an den Strom koppeln. Solche Terme haben eine höhere Dimension und bringen eine neue Skala mit; das
verlässt das skalenfreie Bild. Nicht gerechnet.

Zurückgestellte Ideen: Auslöser 1 von I4 (Arbeit am Skalarsektor) trifft zu. I4 ist seit dem 6.11. unter den geltenden Lesarten gescheitert und bietet
hier keinen neuen Ausweg.

## Grenzen
Eine Schleife, g, g′, y_t laufen nicht mit. Modell U ist mit der geeichten SU(2) nicht verträglich. Die Top-Kopplung nur an ψ₁ ist eine Setzung.
Vergleich der Tiefe bei fester Skala Λ wie in H135. Massen und v aus dem Gedächtnis wie in k300. θ₀ eingesetzt (OP1).
