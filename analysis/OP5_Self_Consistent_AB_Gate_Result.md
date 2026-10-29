# OP5: selbstkonsistente transversale Prüfung und räumliche relative Phase
28.10.2026. Folgt auf OP5_Mixing_Coframe_Feedback_Result.md. Kein OP5-Abschluss.

## Unveränderte Ausgangsdaten
Vergleichsfelder und Kopplungen aus dem Repository-Checkpoint 337d9cb, N=16, zwei bekannte Punkte. Der induzierte Vergleichsoperator bleibt der zuvor ausdrücklich gewählte Operator mit internen Verbindungs-Einformen in Koordinatenkomponenten. Gemeinsame Spinverbindung ist weiterhin kein gelöstes Feld; sie fällt aus der transversalen A/B-Bedingung bei proportionalen Feldwerten heraus. Die Zahlen zur vollständigen Restgleichung verwenden den bisherigen flachen Vergleichsoperator.

## Reduktion der Rückkopplung
E=I+a r^T, a=Delta j_u/2, r=q-q0, q0=(theta_t,0,0,0).
Für die hier tangentiale interne Verbindung s=(0,-y/rho,x/rho,0) gilt a·s=0, weil der räumliche Strom radial ist. Damit bleibt neben P^mu q_mu=q0_0 I auch P^mu s_mu=alpha_s unverändert.

Setze b0=q0_0 u-h beta u-i(dp-cq)alpha_s w.
Mit lediglich zeitlicher relativer Phasenrate lambda lautet die notwendige Gleichung b0+i lambda P^0 u=0.
Eine notwendige Relaxation erlaubt beliebige reelle l_a statt l_a=lambda (E^-1)^0_a:
b0+i sum_a l_a K^a u=0.

Die reelle 8x4-Matrix besitzt an beiden Punkten Rang vier. Least-Squares-Reste liegen unter 1e-29. Die eindeutigen Koeffizienten sind:
P1: l ungefähr (0,0,0,-2.020725942).
P2: l ungefähr (0,0.154173761,0.077086880,-2.321926075).
Minkowski-Normen (-+++): +4.083333333 bzw. +5.421052632.
Daher lassen sie sich nicht durch einen zeitartigen alten Zeitkovektor mit reeller zeitlicher Phasenrate darstellen. Dies erklärt die Schwierigkeit der vorherigen zeitlichen Phasenreparatur. Die Rang- und Vorzeichenaussagen sind numerische Diagnostik an zwei Punkten, keine globale Behauptung.

## Andere Realisierung: volle räumliche Phasenableitungen
Wir behalten stattdessen q=q0 und E=I und ändern nur die relativen Phasenjets:
delta(partial_mu A)=-i d u l_mu,
delta(partial_mu B)=+i c u l_mu,
delta(partial_mu C)=0.
Hier entspricht l_mu=cd partial_mu(phi_B-phi_A) am Anfangswert. Es ist nicht direkt der Phasendifferenzgradient. Die gemeinsame gewichtete Phasenänderung ist in dieser Wahl null.

Die direkte Änderung der reellen Cross-Coframe ist
Re[i(c²-d²)/2 (u† K^a u)l_mu]=0.
Das ist eine algebraische Identität am proportionalen Feldwert. Die numerische Implementierung prüft alle 16 Coframe-Einträge direkt. Daher bleibt der alte flache Frame in dieser lokalen Reparatur unverändert; die Geometrie wird nicht erst nachträglich ausgetauscht.

Auch individuelle Vektor-/Axialströme reagieren am Punkt nicht auf reine Phasenableitungen. Interne Kopplungen werden festgehalten; dies ist keine gemeinsame Eichtransformation von Feldern UND Verbindung. Relative Phasen können bei festem Kopplungsoperator physikalisch relevante Gleichungsbeiträge erzeugen.

## Vollständige Restkontrolle im Vergleichsoperator
Der transversale Rest c R_B-d R_A verschwindet an beiden Punkten bis unter 2e-30 in quadratischer Norm. Die gemeinsame Kombination c R_A+d R_B und R_C bleiben unverändert, was direkt geprüft wurde.

| Quadratische volle Restnorm | P1 | P2 |
|---|---:|---:|
| vorher | 102.2777778 | 157.3617634 |
| nach Phasenjet-Korrektur | 69.6111111 | 113.9933423 |
| entfernt | 32.6666667 | 43.3684211 |

Das sind etwa 31.94 % und 27.56 % Reduktion. Keine einzelne vollständige Speziesgleichung ist damit gelöst: Restnormen A/B/C danach etwa (6.5552,1.7565,4.8534) bzw. (7.8975,2.1161,6.8662).

## Beweisgrenze
Diese Prüfung repariert eine notwendige transversale Gleichung geometrieverträglich am ersten Jet. Sie ändert die räumlichen Anfangsdaten. Sie beweist weder Erhaltung alter Anfangsdaten noch regionale Feldexistenz.

Insbesondere wurden passende Phasenableitungen an zwei getrennten Punkten gefunden. Es ist noch nicht nachgewiesen, dass eine zusammenhängende Phasenfunktion die benötigten Ableitungen in einer Umgebung besitzt. Eine nichttriviale Phase kann in einer Umgebung auch die endlichen Cross-Ströme und das Auslesegesetz ändern. Dass ihre erste Variation an einem Punkt verschwindet, garantiert keine global unveränderte Geometrie. Eine aus den Feldern induzierte Levi-Civita- oder andere Spinverbindung verlangt weitere Geometrieableitungen und bleibt offen.

Nächster Schritt: gemeinsamen A/B-Rest und C-Rest getrennt diagnostizieren und die Integrabilität des erforderlichen relativen Phasengradienten prüfen. Keine freien Potentiale nachträglich anpassen, um die verbleibenden Reste zu verbergen.

Reproduktion: OP5_Self_Consistent_AB_Gate_Check.py/.json. Analytische Ausgangsfelder bei 30 Dezimalstellen, anschließend reelle NumPy-Least-Squares mit rcond=1e-12; Rang, Singulärwerte, vollständige Restnormen und direkte Coframe-Variation geprüft. Lokaler Arbeitsstand, nicht committed.
