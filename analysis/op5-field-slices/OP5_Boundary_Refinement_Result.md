# OP5: erste randbetonte Anpassung

Korrektur vom29.10.2026 nach Kontrolle des Folgevergleichs: Die zusätzliche Punktmenge wurde nur an die berichtete Trainingsmetrik übergeben; die wiederverwendete Residualfunktion behielt ihre ursprünglichen337 Punkte. Die Aussage, Randpunkte hätten diesen Optimierungsschritt beeinflusst, ist deshalb zurückgenommen. Die gespeicherten Felder und ihre unabhängigen Kontrollfehler bleiben gültige Auswertungen, belegen aber nur weitere Optimierung auf der alten Punktmenge. Der korrigierte Randversuch wird in OP5_Boundary_Fair_Result.md dokumentiert. Der folgende ursprüngliche Text bleibt als nachvollziehbare Historie erhalten.

29.10.2026. Gleicher quadratischer Feldansatz und gleiche Region Radius .01, keine zusätzliche Physik.

Zu337 bisherigen Trainingspunkten kamen64 Zufallspunkte auf Randflächen (seed291039) und16 Eckpunkte. Die Eckpunkte sind bereits im ursprünglichen Trainingsgitter enthalten und werden dadurch doppelt gewichtet:417 Einträge,401 verschiedene Punkte. Die64 neuen Punkte liegen konstruktionsbedingt auf vier der acht Randflächen (t negativ, x positiv, y negativ, z positiv); der Test ist keine gleichmäßige Randflächenanpassung. Die separat geprüften Randpunkte decken alle acht Flächen gleichmäßig ab. Diese Asymmetrie muss bei Fortsetzung korrigiert oder als eigene Wahl begründet werden.

Drei akzeptierte gedämpfte Gauss-Newton-Schritte, alle720 Parameter frei, gleiche notwendigen Feldbedingungen und Geometriekontrollen. Die höhere Trainings-RMS gegenüber dem früheren Trainingssatz ist wegen der geänderten Punktgewichtung nicht unmittelbar als Rückschritt zu interpretieren.

Vorher/nachher auf exakt denselben unangetasteten Kontrollpunkten seed291041:1024 gleichmäßig auf acht Flächen verteilte Randpunkte, RMS .000180886 -> .000170686, Maximum .000420864 -> .000396820.4096 Innenpunkte, RMS .000130328 -> .000122473, Maximum .000417416 -> .000391289. Alle Stichproben-Coframes invertierbar, g^{00} negativ; auf Randkontrollen kleinste |detE|12.9883, größtes g^{00}=-.398674.

Ergebnis: bescheidene Verbesserung sowohl am Rand als auch im Inneren. Kein Nachweis, dass die Randgewichtung mehr bringt als drei weitere Schritte auf der alten Punktmenge; ein solcher Parallelvergleich wurde nicht durchgeführt. Rand-RMS bleibt höher. Keine uniforme Fehlerkontrolle, keine exakte regionale Lösung und kein nativer OP5-Abschluss.

Nächste saubere Fragestellung: gleichmäßige Flächenabdeckung ohne unbeabsichtigte Dopplung gegen gleiches Rechenbudget mit alter Punktmenge vergleichen. Keine weitere Parametervermehrung allein aufgrund der größeren Randreste.

Artefakte OP5_Boundary_Refinement_Check.py/.json und OP5_Boundary_Refinement_Validation.py/.json, mit gespeicherten Vorläuferdaten und Evaluatoren. Lokal gespeichert, nicht committed; Paper-Grafik unverändert.
