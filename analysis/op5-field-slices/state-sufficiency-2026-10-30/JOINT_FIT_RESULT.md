# OP5: Erste und zweite Ableitungen gemeinsam angepasst

30.10.2026, Ausgangsrevision f98b29b. Numerischer Test im bestehenden OP5-Vergleichsmodell, keine regionale Lösung oder physikalische Zertifizierung.

## Vertrag und Ergebnis

Festgehalten: drei gespeicherte Feldwerte, Hintergrundverbindung und ihre tatsächlichen Ableitungen, Kopplung und ihre Ableitungen, Massenterm, Koordinaten und die vier Werte der zeitlichen Coframe am jeweiligen Punkt. Keine Ableitung dieser Fixierung wird vorgeschrieben. Variabel: alle 96 reellen ersten Spinorableitungen und 240 reelle symmetrische zweite Ableitungen. Gemischte zweite Ableitungen teilen konstruktiv dieselbe Variable. Die unveränderten vorherigen Daten dienen als Fehlkontrolle.

Gleichzeitig minimiert werden die vollständige Feldgleichung (24 reelle Zeilen), alle vier totalen ersten Ableitungen dieser Gleichung (96 Zeilen) und die punktweise zeitliche Coframe-Fixierung (4 Zeilen). Ein gedämpfter Minimum-Norm-Schritt passt beide Ableitungsordnungen an; er erzwingt die Bedingungen bis zur beobachteten numerischen Genauigkeit, nicht als zertifizierte exakte Gleichheiten. Keine Gewichtung versteckt einen Restblock.

| Kontrollpunkt | Fortsetzungsrest vorher | nachher, automatische Differentiation | voller Feldrest | Änderung erster Ableitungen |
|---|---:|---:|---:|---:|
| Zentrum | 8.7895e-4 | 9.2638e-14 | 3.0613e-14 | 0.001655 |
| Rand | 2.3631e-2 | 1.3308e-14 | 2.2903e-15 | 0.043665 |
| Innen | 9.4926e-3 | 1.4469e-14 | 2.8837e-15 | 0.017025 |

Je Punkt zwei bzw. drei akzeptierte Schritte. Determinanten bleiben 13.63, 13.86 und 13.52; inverse Metrikkomponente g00 bleibt -0.468, -0.538 und -0.433. Zweitjetnormen liegen bei 7.08, 6.90 und 7.18, ohne beobachtetes Aufblähen. Die zeitliche Coframe-Fixierung bleibt unter 1.5e-14 verletzt. Normen gehören zu den bisherigen gepackten Koordinaten, sind keine physikalischen Skalen.

## Kontrollen

- Vollständige inverse Coframe wird mitdifferenziert. Hintergrundwerte werden für die automatische Differentiation lokal mit ihren exakten symbolischen ersten Ableitungen eingesetzt; das ist für die hier getestete erste Prolongation ausreichend, für die nächste Ordnung nicht.
- Getrennte NumPy-Auswertung auf einem gemeinsamen quadratischen Taylorfeld kontrolliert die Feldgleichung und ihre Richtungsableitungen. Zentraldifferenzen bei h=1e-4,1e-5,1e-6 ergeben Fortsetzungsnormen etwa 6e-7, 6e-9, 3e-9 bis 4.5e-9. Der Abfall und die anschließende Rundungsgrenze stützen die AD-Werte; die AD-Rundungswerte sind keine unabhängige Zertifizierung auf 14 Stellen.
- Separat geprüft: g=4-h Psi†ZbetaPsi/2 und alle vier dg. Zustandsreste unter 1e-15, Ableitungsnormen unter 3.4e-14.
- Getrennte Agentenprüfung des konkreten Codes fand keinen blockierenden Packungs- oder Kettenregelfehler und bestätigte g,dg mit den ursprünglichen symbolischen Hintergrundableitungen. Sie ist eine zusätzliche Implementierungsprüfung, kein unabhängiger mathematischer Existenzbeweis.
- Quelldateien und Ausgangsdaten gehasht; unverändert während des Laufs. Das maschinenlesbare Manifest besteht die Evidenzvalidierung.

## Bedeutung

Die frühere Nichtverträglichkeit der eingefrorenen ersten Jets ist an der getesteten zweiten Ordnung beseitigt. Ein gemeinsames Anpassen der unteren Daten und ihrer Fortsetzung findet numerisch verträgliche endliche Zweitjets an allen drei Punkten, ohne neue Felder oder geänderte Kopplungen. Daraus folgt weder, dass die vorherigen Daten falsch ausgewertet wurden, noch dass diese drei neuen Keime zu demselben regionalen Lösungsfeld gehören.

Die Blockade kann in die nächste Ordnung wandern. Als nächster diskriminierender Test sind vollständig symmetrische dritte Jets mit zweiten Hintergrundableitungen erforderlich; zuerst bei festgehaltenen neuen unteren Daten. Zusätzlich bleiben gemeinsame Anfangsdaten, Fortpflanzung der Zwangsbedingungen, regionaler Existenznachweis und die native physikalische Identifikation offen. OP5 ist nicht geschlossen.

## Artefakte

`joint_fit.py` (Befehl: `python joint_fit.py`), `joint-fit-result.json`, `verify_joint.py` (Befehl: `python verify_joint.py`), `joint-fit-scalar-controls.json`, `joint-fit-manifest.json`, archivierte Eingaben unter `joint-inputs/`, `independent-review.md`. Python/NumPy/Torch/SymPy; keine SciPy-Abhängigkeit. Der Auswertungscode liest die bestehenden Originaldateien aus dem Repository; keine Repository-Datei wurde verändert, kein Commit/Push ausgeführt.
