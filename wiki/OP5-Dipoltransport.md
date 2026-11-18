# OP5: Dipoltransport und lokale Umlagerung

Arbeitsstand zu PR #190. Die Größen beziehen sich auf das geometrische Randmodell, nicht auf eine bereits hergeleitete kosmologische Ladung.

- Nachbardiffusion erhält den Mittelwert, lässt den Dipol aber abklingen. Ein eigens gewählter Generator mit geschützter erster Winkelharmonischer kann den Dipol erhalten.
- Eine reellwertige Umlagerung auf vier benachbarten Stellen kann Gesamtmenge und beide Dipolmomente exakt erhalten. Die getestete Blockprojektion dämpft höhere Winkelmoden langsam.
- Für ganzzahlige Änderungen in derselben Einheit auf einem 32er-Ring erzwingt exakte Dipolerhaltung gleiche Änderungen an antipodalen Punkten. Die kürzeste zusammenhängende Strecke für einen nichttrivialen Schritt umfasst 18 Plätze. Ein 6er-Ring erlaubt dagegen vier benachbarte Plätze. Damit ist die Einschränkung rasterabhängig.

Die physikalische Zuordnung des Randdipols, das native Übergangsgesetz und H96 bleiben offen.

[Herleitung zur Ganzzahligkeit](../notes/research/op5_bifocal_response_2026_11_18/Ganzzahl.md).

Die antipodale Kopplung reicht auf dem 32er-Ring nicht für beliebige Glättung. Jede ganzzahlige exakte Umlagerung lässt alle Gegenpunktdifferenzen und damit alle ungeraden Winkelmoden unverändert. Neben den beiden Dipolkomponenten bleiben so 14 weitere ungerade Richtungen erhalten. Auf dem 6er-Ring gibt es diese zusätzliche lineare Einschränkung nicht. [Herleitung und Gegenbeispiel](../notes/research/op5_bifocal_response_2026_11_18/Relaxation.md).

## Welche Annahmen verlangt der Companion?

Quellenabgleich vom 18.11.2026. Die [Definition des endlichen Scans](../sources/research/parts/v470/05_orbit_scan.tex#L379) setzt ein gleichmäßiges Winkelraster für die Proben, aber keine Zweierpotenz. Für den separaten zyklischen Paritätstest ist gerade Länge hinreichend. Die Ganzzahlindizes gehören zu den Abtastpunkten; die bifokalen Residuen sind metrische Abstandsdifferenzen, keine Anzahlen gleicher Einheiten. Der [Paritätstest](../sources/research/parts/v470/05_orbit_scan.tex#L464) schützt Indexparität beim Doppelschritt, kein erstes Winkelmoment. Weder die vier Nullregister des lokalen OP5-Geltungsbereichs ([OP5 #12](https://github.com/Moriarty1982/QuantumSphere-Unfold/issues/12)) noch die [H96-Vorab-Notiz](../notes/research/predictions/Vorab_Notiz_H96_Omega_M_beta2.md) fordern eine exakte Erhaltung des Randdipols. H96 benutzt eine diskrete Spin-Summe, liefert aber keine Quantisierung der Randdifferenzen. Der ganzzahlige 32er-Gegenbefund grenzt deshalb eine ergänzende Mikrodynamik ein und ist kein Hindernis für den formulierten OP5-Ansatz selbst. OP5 und H96 bleiben offen.

## Rückwärtssuche nach einer physikalisch erhaltenen Größe

Unter der Maxwell-Abbildung M→T bleibt die Energie gleich. Die passende vorzeichenwechselnde Größe Re S=E²−B² ist dagegen nicht allgemein erhalten, wie ein periodisches stehendes Feld bei konstanter Gesamtenergie exakt zeigt. W1 hat einen erhaltenen internen Eichstrom, dessen Ladungsvorzeichen bisher keine nachgewiesene Zuordnung zum M–T-Randdipol besitzen. Der physikalische Übergang bleibt offen. [Gegenprobe und Quellenabgleich](../notes/research/op5_bifocal_response_2026_11_18/Quelle.md).

Eine modellhafte Paarumwandlung M+T↔p mit neutraler Hilfsmode erhält die M–T-Besetzungsdifferenz genau. Sie bindet die Summe der beiden Phasen relativ zur Hilfsmode. Der sesquilineare Sonden-Kreuzterm hängt dagegen an der Differenz der Phasen und ist unter dieser Erhaltungssymmetrie nicht invariant. Eine neue Auslesung oder eine physikalisch begründete Phasenreferenz bleibt nötig. [Paarprüfung](../notes/research/op5_bifocal_response_2026_11_18/Paarsymmetrie.md).

## Antwort des Dipols auf eine direkte Quelle

Bei einer steifen Dipolkoordinate erzeugt eine lineare Q-q-Kopplung den gewünschten linearen Dipol. Die minimierte Energie bleibt aber quadratisch in Q, sofern die drei quadratischen Koeffizienten nicht gemeinsam ein vollständiges Quadrat bilden. Eine lineare Quelle an der quartisch weichen Kreisgeometrie liefert sogar q∝sgn(Q)|Q|^{1/3} bis auf das Vorzeichen der Kopplung und einen Energieleitterm der Ordnung |Q|^{4/3}. Die Austauschparität allein erzwingt keine der benötigten Relationen. [Herleitung](../notes/research/op5_bifocal_response_2026_11_18/Quellkopplung.md).
