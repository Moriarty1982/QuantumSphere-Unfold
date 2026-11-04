# Vorab-Notiz H65: Kovarianz von R auf Werteebene und Eichung

**Geschrieben und committet am 4. November 2026 vor der Rechnung. Status: vorregistriert.**

## Vorwissen geprüft
Gesucht wurde nach „covarian / kovarian / Frame_Covariance / ϑ-Eichung / K2“ in `analysis/OP5_*`, r71–r77 und predictions.
- `OP5_Frame_Covariance_Independent.md` und `OP5_Frame_Recheck.md` (25.10.) betreffen den spektralen Frame-Übergang, nicht R.
- H64 (r77) zeigt Kovarianz nur auf Symbolebene erster Ordnung.
- Ω und die vier Bedingungen sind bisher numerisch als Linkskern-Bedingungen bestimmt. Es gibt keine geschlossene Formel, die man direkt transformieren könnte.

## Idee
Ω wird aus R allein abgeleitet (r71, eichinvariant). Die vier Bedingungen kommen aus R zusammen mit der Eichung Ψ†K₂Ψ = S (r72, r73). Abgeleitete Integrabilitätsbedingungen eines kovarianten Systems sind selbst kovariant. Deshalb genügt es zu prüfen:
- (a) ob R auch auf Werteebene kovariant ist, mit allen Termen niedrigerer Ordnung;
- (b) unter welchen inneren Lorentz-Transformationen die Eichung erhalten bleibt.

## Messung (k165)
- **(a)** An 5 zufälligen Datensätzen außerhalb der Lösungsmenge werden ψ, j, A, ∂A, h und ∂h gewählt. Sie werden mit zufälligem M ∈ GL(4) und S ∈ Spin(1,3) transformiert wie in H64. Die Zeilentransformation C wird aus dem Symbol bestimmt (pinv mit rcond 1e-6). Gemessen wird ‖R' − C R‖/‖R'‖ mit R' = R(Lj, Sψ, bg'), blockweise für F, G und dg.

  Ist C nicht bei allen Datensätzen gleich, wird das gemeldet. Der Test verlangt nur je Datensatz ein C, das aus dem Symbol desselben Datensatzes kommt.
- **(b)** Gesucht sind die Generatoren X ∈ so(1,3) in der Spin-Darstellung mit Re(ψ†K₂Xψ) = 0 für alle ψ. Das ist die infinitesimale Invarianz von ψ†K₂ψ. Gemeldet wird die Dimension dieser Unteralgebra und welche Generatoren sie bilden.

## Hypothese H65
- (a) Alle Residuen sind ≤ 1e-8 (positive Kontrolle M = 1, S = 1: ≤ 1e-12).
- (b) Die erhaltende Unteralgebra ist 3-dimensional: Drehung um y sowie Boosts entlang x und z, also so(1,2), der Stabilisator von e_y. Die Eichung ist damit eine nicht kovariante Eichfixierung, die eine Raumrichtung auszeichnet.

## Entscheidung
| Ergebnis | Bedingung |
|---|---|
| bestätigt | (a) und (b) gelten |
| widerlegt | (a) ein Residuum ≥ 1e-5, oder (b) eine Dimension ≠ 3 bzw. eine andere Unteralgebra |
| ungültig | die positive Kontrolle verfehlt, oder ein Residuum liegt zwischen 1e-8 und 1e-5 |

## Lesart bei Bestätigung
Ω ist kovariant. Die vier Bedingungen sind nur unter dem Stabilisator der Eichung kovariant. Ihr Bestand ist eichabhängig, ihre Zahl auf dem Kegel womöglich nicht; das wäre ein eigener Test.

## Nachtrag vom 4. November 2026, nach Lauf 1 und vor Lauf 2
**Lauf 1 ist ungültig.** Die positive Kontrolle verfehlte für F die Schranke 1e-12: Sie ergab 0.24. Die Ursache liegt im Verfahren. An Daten außerhalb der Lösungsmenge liegt R nicht im Bild des Symbols J, und C = J'L·J⁺ bestimmt C auf diesem Komplement nicht.

Werte von Lauf 1:
- (a): F 0.09 bis 0.24, G 7e-10 bis 2e-4, dg ≤ 1e-9;
- (b): Dimension 3 mit Drehung y, Boost x, Boost z, wie vorhergesagt.

**Lauf 2, nicht blind.** C wird nicht mehr aus dem Symbol bestimmt, sondern aus den Werten. Für ein festes (M, S) werden 80 zufällige Datensätze transformiert, und es gilt C = R'·R⁺ über alle Datensätze. Das ist zulässig, weil eine echte Zeilentransformation nur von (M, S) abhängt und nicht von den Daten. Das Residuum ist dann das größte relative ‖R' − CR‖/‖R'‖ über 20 weitere Datensätze, die nicht zur Bestimmung von C dienten. Zwei Paare (M, S) werden geprüft. Alle Schranken bleiben unverändert; (b) wird nicht wiederholt.
