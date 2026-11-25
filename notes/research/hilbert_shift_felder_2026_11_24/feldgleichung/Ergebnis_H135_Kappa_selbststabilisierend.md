# Ergebnis H135: κ ≈ 1,2 ist in den geprüften Lesarten kein selbststabilisierender Punkt

**Stand:** 2026-11-25. Test nach Vorab-Notiz `notes/research/predictions/Vorab_Notiz_H135_Kappa_selbststabilisierend.md` (Commit cbfbb9f, vor dem ersten
Lauf). **Teilweise nicht blind:** K-a stand vorab fest, K-b war offen.
Anlass: Frage des Autors zum Zahlentreffer aus k303, ob das System bei diesem Wert selbststabilisierend sein könnte.
Skripte: `k304_test_h135.py` (Python: numpy, sympy, scipy), Ausgabe `k304_out.txt`; Gegenprobe `k304b_gegenprobe.wl` (Wolfram Language), Ausgabe
`k304b_out.txt`. Qiskit nicht eingesetzt (keine Schaltung). Kein Guard berührt. OP1 bis OP5 bleiben offen.

## Gesamturteil
**H135 widerlegt**, in beiden vorab festgelegten Lesarten.

| Kriterium | Vorhersage | Ergebnis |
|---|---|---|
| K-a (Fluss) | widerlegt (nicht blind) | **widerlegt** |
| K-b (Vakuumtiefe) | widerlegt (Vermutung) | **widerlegt**: F(κ) wächst monoton, kein inneres Maximum |

## 1. Fluss (K-a)
- Der Ein-Schleifen-Fluss nur mit Skalaren ist homogen vom Grad 2 (Nullrest geprüft). Feste Werte ungleich null gibt es nicht, nur feste Verhältnisse.
- Von κ(v) = 1,204 aus wächst κ zu großen Skalen (1,41 bei 670 GeV, 2,84 bei 4,9 TeV, Pol bei 1,4·10⁴ GeV). Zu kleinen Skalen sinkt es erst auf 1,04
  und steigt dann wieder; λ_A und λ_C werden negativ, bei 0,1 GeV überschreitet eine Kopplung 4π.
- Benachbarte Startwerte (1,0 / 1,2 / 1,4) laufen nicht auf einen gemeinsamen Wert zu. Ihre Spanne schrumpft kurz von 0,40 auf 0,34 und wächst dann in
  beide Richtungen (0,73 bei t = −5, 3,1 bei t = +3). Es gibt keinen Einzugsbereich.

## 2. Vakuumtiefe (K-b)
Skalenfreies Ein-Schleifen-Potential V = φ⁴[A + B·ln(φ²/Λ²)], Tiefe bei fester Skala Λ proportional zu F(κ) = B·exp(−2A/B).
- Ohne Eichfelder und Top ist F für jedes κ gleich e³/(16π²) = 0,1272 (symbolisch). Die Abhängigkeit von κ kommt allein von W, Z und Top.
- Mit ihnen steigt F von 0 bei κ = 0,416 monoton gegen diesen Grenzwert: 10,5 % bei κ = 0,6, 57,7 % bei κ* = 1,204, 89,8 % bei κ = π, 98,6 % bei κ = 10.
  Die Steigung wechselt auf (0,416, 40] nie das Vorzeichen (Gitter und Nullstellensuche, beide Werkzeuge).
- Bei κ* ist d ln F/d ln κ = 0,96. Dort ist nichts Besonderes. Wäre κ beweglich, liefe es zu immer größeren Werten, bis die Beschreibung endet.
- Bei festem v statt festem Λ ist die Tiefe m_s²v²/16 und wächst ebenfalls monoton.

Nachträglich bemerkt (kein Kriterium): v/Λ hat ein flaches Maximum bei κ ≈ 0,8 (1,05), und m_S/Λ läuft gegen √e = 1,649.

## 3. Häufigkeit (ohne Kriterium)
- Ein Vakuum gibt es für jedes κ zwischen 0,416 und der Unitaritätsgrenze π. Bei gleichverteiltem κ sind das 87 %, bei log-gleichverteiltem (ab 0,01) 35 %.
- m_h reicht dabei von 0 bis 345 GeV. Zwischen 120 und 130 GeV landen 2,7 % (κ von 1,16 bis 1,24).

Der Gedanke des Autors trägt also in einer Hinsicht: Das System „startet“ bei den meisten κ, dafür muss kein besonderer Wert getroffen werden. Er
erklärt in dieser Form aber nicht, warum gerade κ ≈ 1,2 vorliegt. Die 125 GeV wären dann ein Wert unter vielen möglichen.

## Was fehlt
Selbststabilisierung braucht eine Rückwirkung: κ müsste von etwas abhängen, das seinerseits auf κ antwortet. Der Zahlentreffer κ = 1/cos 2θ legt nahe,
dass das der HC-Winkel θ sein müsste. In Lesart S-a (H133) gibt es diese Rückwirkung nicht, weil der Anhang nur an A = A₁ + B koppelt und θ nicht sieht.
Sie entsteht erst, wenn der HC die SU(2) bricht und der Anhang an Vorstufe und HS(2)-Anhang verschieden koppelt (κ₁·A₁·C + κ₂·B·C). Dann verschiebt die
Schleife des HS(3)-Anhangs den Winkel θ, und man kann fragen, ob κ_eff = 1/cos 2θ ein fester Punkt dieser Schleife ist. Das ist nicht gerechnet.

## Grenzen
Eine Schleife. In L2 laufen g, g′, y_t zwischen Λ und v nicht mit. Der Vergleich bei fester Skala Λ ist eine Lesart. Ob κ im Turm überhaupt beweglich ist,
ist nicht gezeigt; die Lesarten L1 und L2 habe ich gewählt. Andere Formen von Selbststabilisierung (etwa über θ, siehe oben, oder über eine Dynamik
jenseits einer Schleife) sind damit nicht ausgeschlossen. Massen und v aus dem Gedächtnis wie in k300.
