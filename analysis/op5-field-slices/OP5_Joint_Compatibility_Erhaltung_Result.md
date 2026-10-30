# OP5: direkte Kompatibilität und Erhaltung gemeinsam

30.10.2026. Drei Kontrollpunkte, festes Vergleichsmodell, keine regionale Feldlösung.

Wolfram Language bestätigte symbolisch dg=-(q dh+h dq)/2 für g=4-hq/2 und lieferte h am Zentrum und8/h mit60 Stellen. Zusätzlich wurde die logarithmische Ableitung des tatsächlichen Hintergrunds h=[(1-r²/t²)(1-t²/4)]^-1/2 abgefragt. Die vollständigen numerischen Punkt- und Prolongationssysteme wurden lokal gelöst, nicht Wolfram zugeschrieben.

Zum direkten Kompatibilitätssystem kommen nun alle vier Bedingungen dg_mu=-(partial_mu h)Psi†ZbetaPsi/2-h Re(Psi†Zbeta partial_mu Psi)=0 hinzu. Feldwerte und gewählte zeitliche Coframe bleiben gleich, sieben reelle räumliche Jetkomponenten werden ausgewählt und direkt bestimmt; zeitliche Jets jeweils aus der Gleichung abgeleitet. Drei dominante Kompatibilitätskombinationen und vier Erhaltungsbedingungen werden gemeinsam per7x7-Newton-System gelöst, aber alle acht ursprünglichen Komponenten unabhängig kontrolliert. Die kleine achte Singulärzahl abseits der Nullstelle wird nicht als Beweis einer achten unabhängigen Bedingung am Lösungsort interpretiert.

An Zentrum/Rand/Innenpunkt: Norm des vollständigen Kompatibilitäts-/Erhaltungsvektors9.60e-15,1.27e-15,4.68e-15. Vollständiger Spinorgleichungsrest8.13e-15,1.57e-15,1.92e-15. Änderungen räumlicher Jets etwa6.00e-5,6.60e-4,9.35e-5. Coframes regulär, g^{00}=-.468,-.533,-.435. Diese Werte sind Rundungsniveau, keine physikalische Skala; siehe den unabhängigen Präzisionstest.

Erneute erste Prolongation bei festgehaltenen reparierten Werten/Jets, einschließlich Coframe- und Hintergrundableitungen: Ohne Zweitjetsymmetrie Rest bei Schritt1e-5 ungefähr1.62e-9,1.51e-9,1.55e-9. Bei Schritt1e-4 ungefähr1.5e-7 und bei1e-6 ungefähr1e-9, konsistent mit Differenzenfehler und Rundung. Der frühere größere unsymmetrische Quellenrest ist damit numerisch beseitigt.

Mit der notwendigen Symmetrie gemischter zweiter Ableitungen bleibt Rang88 und stabiler Rest .000878953, .02363114, .00949256. Dieser Rest kann nicht als Rundungsniveau eingeordnet werden. Damit ist die verbleibende Einschränkung in dieser Datenfamilie der symmetrischen Feldfortsetzung zugeordnet; sie beweist keine allgemeine Unlösbarkeit des Vergleichsmodells oder des nativen Papers.

Fortschritt ist eine Ursachenabgrenzung: punktweise Gleichungen und skalare Erhaltung können gleichzeitig direkt erfüllt werden, der darüber hinaus verbleibende Fortsetzungsrest hängt an der Gleichheit gemischter Ableitungen. Die jetzt gewählten ersten Jets sind weiterhin frei reparierte Daten, keine Ableitungen eines bereits angegebenen gemeinsamen Feldes. Ob die symmetrische Quelle durch andere kompatible erste Jets verschwindet, ist offen.

Nächster diskriminierender Schritt: vollständige linke Eliminationsbedingungen des symmetrischen Zweitjetsystems als zusätzliche Bedingungen an die noch freien ersten Jets bestimmen und gemeinsam lösen, dabei keine fremden physikalischen Quellterme ergänzen. Zeitcoframe-Festlegung und native Wirkung sind weiterhin gesondert zu begründen.

Artefakte OP5_Joint_Compatibility_Erhaltung_Check.py/.json; OP5_Joint_Compatibility_Lower_Data.json; OP5_Joint_Compatibility_Second_Jet_Check.py/.json. Lokale Vorläufer/Evaluatoren erforderlich. Lokal gespeichert, nicht committed; Paper-Grafik unverändert, OP5 offen.
