# OP5: dynamische Erhaltung der A/B-Proportionalität
28.10.2026. Fortsetzung der chiralen Coframe-Prüfung. Vergleichsmodell des Checkpoints 337d9cb, N=16. Keine native OP5-Lösung.

## Festgelegtes Problem
Startwerte A=c u, B=d u, C=w, c=cos(theta), d=sin(theta), p=kc, q=-kd. Originale flache Dirac-Dynamik, ursprüngliche Kopplungen und Feldwerte. Ausgangschart theta=asin(t/2)/2, daher räumlicher theta-Gradient null. Zunächst sämtliche räumlichen Ableitungen festgehalten. Unbekannte zeitliche Ableitungen werden von der ursprünglichen Hamilton-Gleichung vorgegeben. Kein neuer Potentialfit.

## Exakte notwendige Bedingung
Mit alpha_s=sum spin_i alpha_i und h=hm gilt
b=c dot(B)-d dot(A) = -(alpha·grad theta)u+h beta u+i(dp-cq)alpha_s w.
Eine reell proportionale Familie verlangt b=dot(theta)u.
Gemeinsame Änderungen von u, einschließlich gemeinsamem chiralen Winkel, fallen aus dieser Kombination heraus. Sie können diese notwendige Bedingung nicht reparieren.

Der komplex-proportionale Vergleich lässt b=lambda u mit komplexem lambda zu; dies erlaubt zusätzlich relative Phase, aber keinen neuen Spinorzustand. Die unabhängige algebraische Gegenprüfung bestätigte Vorzeichen und Tangentialbedingung.

## Numerische Kontrollen
Analytische Ausgangsableitungen bei 30 Stellen ausgewertet, anschließend reelle NumPy-Least-Squares-Systeme mit rcond=1e-12. Reell/Imaginärteile werden gestapelt. Singulärwerte und unprojizierte Restnormen der jeweiligen Gate-Gleichung sind in JSON gespeichert.

Quadratische Restnormen in der bisherigen Vergleichsnormierung:
| Freigegebene Größen | P1=(1,.6,0,0) | P2=(1,.4,.2,.2) |
|---|---:|---:|
| Nur reelle zeitliche Mischrate | 32.6666667 | 43.3684211 |
| Komplexe zeitliche Proportionalitätsrate | 32.6666667 | 42.1684211 |
| Zusätzlich drei räumliche theta-Ableitungen, reell | unter 5e-30 | 1.2 |
| Räumliche theta-Ableitungen und relative Phasenrate | unter 5e-30 | unter 8e-30 |

Die ersten beiden Zeilen behalten die räumlichen Daten bei. Ihre positiven Reste zeigen: Selbst komplexe Proportionalität wird am bisherigen Anfangsfeld von dieser Dynamik nicht erhalten.

Die letzten beiden Zeilen ändern die räumlichen Anfangsableitungen ausdrücklich. Sie sind neue lokale Jet-Kandidaten, keine Entwicklung der alten Anfangsdaten. Gemeinsame räumliche Ableitungen von u fallen aus der transversalen Gleichung heraus.

## Attribution des verbleibenden Fehlers
Bei freiem reellem theta-Gradienten ist die Gleichung
(theta_t I+sum theta_i alpha_i)u=h beta u+i(dp-cq)alpha_s w.
Alle vier Matrizen links sind hermitesch. Daher ist Im(u† RHS)=0 notwendig. Der Vektor iu steht im reellen Skalarprodukt senkrecht auf allen vier Fitspalten.

Die untere Schranke für die quadratische Restnorm lautet
[Im(u† RHS)]²/(u†u).
Sie ist an P1 null und an P2 1.2 und stimmt dort mit dem gesamten numerischen Rest überein. Eine zusätzliche Spalte iu beseitigt diesen Rest an beiden Punkten. Deren Koeffizient ist an P2 etwa -0.3872983. Er ist die imaginäre transversale Rate; bei A=c exp(i phi_A)u, B=d exp(i phi_B)u entspricht er cd*(dot phi_B-dot phi_A), nicht unmittelbar der Phasendifferenzrate.

## Rückwirkung auf die Geometrie
Die freigegebenen räumlichen Mischableitungen sind geometrisch nicht kostenlos. Am unveränderten proportionalen Feldwert und bei unveränderter Verbindung ergibt ihre Änderung
delta E_mu^a = (cos(2 theta)/2) (u†K^a u) delta(partial_mu theta).
Dies folgt direkt aus der Cross-Coframe-Definition. Der alte flache Operator ist deshalb für diese neuen Jets noch nicht selbstkonsistent bestätigt. Die vorherige Invarianz unter dem gemeinsamen chiralen Winkel gilt nicht als Invarianz unter beliebigen theta-Ableitungsänderungen.

Ebenso ist die finite Coframe-Eigenschaft bei unabhängigen relativen A/B-Phasen erneut zu prüfen. Eine erfolgreiche transversale Projektion ersetzt weder die übrigen Spinorgleichungen noch die Rückkopplung der Verbindung/Geometrie.

## Ergebnis und nächster Schritt
Der gemeinsame chirale Winkel allein kann die dynamische Proportionalitätslücke nicht schließen. Die Lücke wurde präziser zerlegt: bei festen räumlichen Daten ein echter Spinorrichtungsfehler; nach Freigabe räumlicher Mischung an P2 zusätzlich eine relative Phasenrichtung. Der erweiterte lokale Gate-Fit ist möglich, aber ändert die Geometrie.

Nächster Schritt: Coframe aus diesen geänderten Jets neu auswerten und die vollständige Dirac-Gleichung im daraus folgenden Operator prüfen. Alternativ vollständig unabhängige A/B-Felder zulassen und die bisherigen geometrischen Nebenbedingungen neu herleiten. Kein universelles No-go für andere Anfangsdaten oder andere Kopplungen.

Dateien: OP5_AB_Proportional_Dynamics_Check.py und .json. Der Skriptimport verweist auf den bestehenden Repository-Evaluator; bei einer späteren Übernahme ins Repository ist er auf einen Nachbarpfad umzustellen. Lokal gespeichert, noch nicht committed.
