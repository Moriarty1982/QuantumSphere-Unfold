# Erkundung k376: Quarks einzeln justiert. K ≠ ⅔ verlangt einen Bruch von J, nicht der Dreiersymmetrie

**Stand:** 26.11.2026. **Erkundung, nicht blind** (keine Vorab-Notiz; alle Zahlen standen seit H1/H172/k374/k375 fest). Anlass: Autor, 26.11.2026
(„für jedes einzelne Teil erstmal das System justieren … welche Konfiguration jeweils gesetzt sein muss und wie die zusammenhängen“).
Skripte k376 (Python, 10⁵ Ziehungen, Seed 20261126) und k376b (Wolfram, exakte Identitäten). Qiskit nicht eingesetzt (keine Schaltung).

**Ergebnis in einem Satz:** Die Abweichung der Quarks von K = ⅔ lässt sich nicht billig durch einen Bruch der Dreiersymmetrie erzeugen (exakt nötige Stärke
√(9K − 6) = 0,85 bzw. 1,41, fünf- bis neunmal mehr als die ganze CKM-Matrix braucht); sparsam geht es nur über die zirkulante Stellgröße ρ selbst, also über
einen Bruch des Frame-Tauschs J.

## 1. Konfiguration als Winkel
K = (1 + ρ²)/3 mit ρ = tan θ. K = ⅔ ist θ = 45°, der Fixpunkt von J (H149).

| Sektor | K | θ | θ − 45° | δ |
|---|---|---|---|---|
| e | 0,66666 | 45,000° | 0 | 0,22222 |
| d (M_Z) | 0,7478 ± 0,0011 | 48,11° ± 0,04° | +3,11° | 0,1001 |
| u (M_Z) | 0,8876 ± 0,0008 | 52,21° ± 0,02° | +7,21° | 0,0518 |

An der Planck-Skala (k375): d +2,67°, u +7,37°.

## 2. Zwei Wege zu K ≠ ⅔
- **Weg A (zirkulant):** ρ ≠ 1. Die Dreiersymmetrie bleibt, J ist gebrochen. Nur K bewegt sich; δ und die Mischung bleiben unberührt. Nötig ρ − 1 = 0,115 (d)
  und 0,290 (u).
- **Weg B (J im Baumwert, Dreiersymmetrie gebrochen):** M = Ĉ(ρ = 1, δ₀) + B. Der brechende Teil B hat in der Fourier-Basis Diagonale null (k376b, Nullrest),
  deshalb gilt **exakt** ‖B‖² = Σμ² − Σλ₀² = 3(ρ² − 1) = 9K − 6, unabhängig von δ₀ und von der Drehung. Das gibt ‖B‖ = 0,854 (d) und 1,410 (u).
  Für die ganze CKM-Matrix reichen 0,157 bis 0,166 (k374). Weg B verlangt außerdem Drehungen von 10° bis 27° je Sektor (CKM: 13° / 2,4° / 0,2°), die sich
  zwischen Up und Down fast vollständig aufheben müssten. Mit δ₀ = π/12 gibt es gar keine Lösung (Schur-Horn-Bedingung verletzt).

**Lesart:** Die Quarks brauchen zwei getrennte Eingaben. Erstens einen J-Bruch (θ − 45° = 3,1° und 7,2°), der die Dreiersymmetrie nicht berührt. Zweitens
einen kleinen Bruch der Dreiersymmetrie (0,16) für die Mischung. Bei den Leptonen fehlt die erste Eingabe (J exakt), die zweite ist halb so groß (0,075).

## 3. Hängen J-Bruch und δ zusammen? (nachträglich, Zahlenvergleich, kein Test)
- (θ − 45°)_u/(θ − 45°)_d = 2,31 bei M_Z, 2,76 an der Planck-Skala. δ_d/δ_u = 1,93 bzw. 2,23. Größerer J-Bruch geht mit kleinerer Phase einher; das Produkt
  (θ − 45°)·δ ist 0,0054 (d) und 0,0065 (u), also nicht gleich (20 % Unterschied bei Fehlern von 1 bis 2 %).
- K_d liegt bei M_Z 2,0σ unter ¾, K_u 1,5σ unter 8/9. Beides hält dem Laufen nicht stand (−12,9σ bzw. +6,6σ an der Planck-Skala), und bei Fehler 0,001
  trifft ein beliebiger Wert mit etwa 50 % einen Bruch mit Nenner bis 12 auf 2σ. **Kein Befund.**

## Übersicht: was je Teil gesetzt sein muss
| Eingabe | ν | e | d | u | Status |
|---|---|---|---|---|---|
| J-Bruch θ − 45° | 0 (gesetzt) | 0 (gemessen, 10⁻⁵) | 3,1° | 7,2° | Quarks: gemessen, unerklärt |
| Phase δ | 0,480 | 0,2222 | 0,100 | 0,052 | gemessen bzw. angepasst (ν); Halbierung widerlegt (H177) |
| Bruch der Dreiersymmetrie | zusammen 0,075 | | zusammen 0,16 | | Stärke und Richtung angepasst (k374, H176) |

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| k374 | Brannen-Form je Sektor | CKM-Baumwert 𝟙; Zählung je Algebra | (K, δ) je Sektor, Brechung |
| H177 | Ein-Schleifen-Laufen | Quarkzahlen fast skalenstarr | Halbierung keine Regel |
| k376 | nichts Neues | ‖B‖² = 9K − 6 exakt; K ≠ ⅔ ist ein J-Bruch, kein Bruch der Dreiersymmetrie | Warum ist J bei Quarks gebrochen und bei Leptonen nicht? |

Die offene Frage ist damit schärfer: Gesucht ist eine Eingabe, die den Frame-Tausch J bricht, die Dreiersymmetrie erhält und nur bei Quarks wirkt.
Kandidat aus dem Projekt ist die Farbe (H127, H125). Das ist eine Frage an den Autor, kein Ergebnis.

## Grenzen
Die Drehwinkel für Weg B sind die besten aus 200 Starts, kein bewiesenes Minimum; die Norm ist exakt. Yukawa-Werte bei M_Z aus k14/k367. Der Vergleich
mit 0,157 nutzt dieselbe Normierung (mittlere Diagonale 1) wie k374. Kein Vorzeichen gesetzt; kein Guard berührt; OP3 und OP4 offen.
Vergeben: k376. Nächste frei: H178, k377.
