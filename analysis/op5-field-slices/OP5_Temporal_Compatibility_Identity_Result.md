# OP5: explizite vier zeitliche Verträglichkeitsbedingungen

29.10.2026. Festgehaltenes Vergleichsmodell und gemischtes Feld, keine regionale Evolutionslösung.

## Identität

Reell gepackt:24 Komponenten der Spinorgleichung F,24 zeitliche Variablen. A ist die4x24-Abbildung von einer Zeitjetänderung auf delta E_0, B die24x4-Matrix der kovarianten Jets. AB=E. H ist die reelle Darstellung des eingefrorenen zeitlichen Dirac-Operators i P0. Bei raumartiger Zeitscheibe ist H invertierbar. P=I-B E^{-1}A entfernt die vier punktweisen Scherrichtungen.

Auf ker(A) ist die Coframe konstant, daher J=H; auf Bild(B) gilt J=0. Somit gilt exakt J=HP. Folglich ist L=A H^{-1} eine explizite vollständige4x24-Matrix linker Kompatibilitätszeilen: LJ=0, RangL4. Das ist eine strukturelle Formel, keine Identifikation nur anhand numerischer Ränge.

Bei festen Feldwerten, räumlichen Jets und vorgegebener Zeitcoframe lautet die Gleichung F=H d0+b. A d0=E_0 im bisherigen zeitlich verbindungsfreien Vergleich. Die vier Bedingungen sind daher C=L F=E_0+A H^{-1}b=0. Sie lassen sich ohne Wahl neuer Zeitjets aus den übrigen Daten bestimmen.

Stärker als bloße Linearisierung: Jede Zeitänderung mit A delta d0=0 lässt E exakt unverändert; F ändert sich exakt um H delta d0. Daher sind C=0 notwendig und hinreichend für eine punktweise Nullstellung durch Zeitjetänderung bei festem E_0. Falls erfüllt, ist delta d0=-H^{-1}F die eindeutige Korrektur in dieser Fixierung. Dies behauptet weder konsistente räumliche Anfangsdaten noch Fortpflanzung über ein Gebiet.

## Bekannte skalare Bedingung und drei verbleibende Kombinationen

Die Zeile ell=(-Im(SPsi),Re(SPsi)) liefert ell F=4-h Psi†ZbetaPsi/2. Sie liegt im Zeilenraum von L. Damit ist eine Kombination der vier Bedingungen bereits die bekannte skalare Zustandsbedingung. Drei weitere unabhängige Kombinationen bleiben; eine physikalische Benennung als Energie-/Impulsbedingungen ist nicht hergeleitet. Ihre konkrete Basis ist nicht eindeutig.

## Kontrollen

Drei Punkte wie im vorherigen Gauge-Test. J numerisch per zentralem Differenzschritt1e-5, H/A/B analytisch aus den Werten. Relativer Fehler J-HP ungefähr5.1e-11; Differenz der analytischen und numerischen linken Raumprojektoren unter6.6e-10. ell-Rekonstruktionsfehler aus L unter6.8e-15. L überall Rang4. Die bekannte skalare Kombination ist unter1.7e-15 erfüllt, die übrigen Komponenten von LF bleiben im Näherungsfeld nichtnull.

Nach orthogonaler Projektion auf den linken Raum beträgt die mit Zeitänderung bei fester Coframe nicht korrigierbare Restnorm am Zentrum2.977e-5, am Randpunkt1.841e-4, am inneren Punkt3.899e-5. Dies sind lokale Werte dieses Kandidaten, keine unvermeidlichen Fehleruntergrenzen für andere räumliche Daten oder eine andere physikalische Modellwahl.

## Konsequenz

Jetzt ist explizit bekannt, welche zusätzlichen räumlichen Verträglichkeitsdaten die bisherige skalare Normierung nicht erfüllt. Nächste sinnvolle Rechnung: den drei verbleibenden Kombinationen im Feldansatz gezielt nachgehen und prüfen, ob ihre Erhaltung aus einer gemeinsamen Dynamik folgt. Ihre bloße Verwendung als numerische Zusatzstrafe ersetzt keine Fortpflanzungsidentität. Die punktweise Coframe-Festlegung ist weiterhin nicht als globale native Eichsymmetrie bewiesen.

Artefakte OP5_Temporal_Compatibility_Identity_Check.py/.json. Vorläuferdaten und bestehende Torch/NumPy-Auswertung nötig. Lokal gespeichert, nicht committed. Keine neue physikalische Feldgleichung postuliert, OP5 offen.
