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

W1 liefert nach Torsionselimination einen konkreten Stromquadratik-Term. Im isotropen M-Ruhesystem gilt für den ungewichteten Gesamtstrom j²=(n₊+n₋)²≥Q_J²; interne Gegenladungen löschen ihn nicht aus. Bei Umverteilung einer festen Gesamtbesetzung reagiert der Term aber gar nicht auf Q_J, während einseitige Neubesetzung einen Q_J²-Anteil erzeugt. Die Auswahl des Dichtepfads, die gesamte Energieantwort und eine M/T-Randabbildung sind offen. [W1-Prüfung](../notes/research/op5_bifocal_response_2026_11_18/W1_Strom.md).

Die W1-Maxwell-Gleichung begrenzt auch den Pfad mit fester Gesamtbesetzung. Ohne Gegenquelle ist homogene J-Ladung mit exakter Isotropie unvereinbar. Eine periodische räumliche Ladungsmode mit Mittelwert null ist mit dem Gaußgesetz vereinbar, trägt aber schon bei minimaler Feldenergie einen positiven quadratischen Maxwell-Beitrag. [Gauß-Prüfung](../notes/research/op5_bifocal_response_2026_11_18/W1_Gauss.md).

Die diagonale klassische W1-Wirkung hat auch **eichneutrale interne Differenzströme**: Eine Differenz zweier gleich geladenen Komponenten kann sich zwischen Zuständen ändern, ohne den Eichstrom oder den Torsionsstrom zu ändern. Ihre getrennte Erhaltung liefert keine Erzeugungsdynamik. W2-Yukawa-Terme beschränken die erlaubten Phasengeneratoren; die native Randabbildung und der gesamte Tensor bleiben offen. [W1/W2-Prüfung](../notes/research/op5_bifocal_response_2026_11_18/W1_Neutral.md).

Unter der klassischen Dirac-Yukawa-Lesart von W2 überlebt B−L. Die Richtung 3(B−L) ist bei einer Generation einschließlich ν^c zum W1-J-Generator orthogonal; eine entlang dieser Richtung gewählte Umverteilung ändert die globale Ladung bei unveränderter W1-Eichquelle und Gesamtbesetzung. Ein zusätzlicher Majorana-Term bricht diese stetige Symmetrie. Der benötigte Vorzeichenwechsel unter einer nativen M/T-Fermionabbildung, der Randdipol und der Energietensor bleiben offen. [W2-Ladungsprüfung](../notes/research/op5_bifocal_response_2026_11_18/W2_Ladung.md).

Der Quellenabgleich löst die Vorzeichenfrage für den bisherigen W2-Kandidaten: In r51 kommutiert die native Tachyon-Abbildung R ausdrücklich mit B−L. Den älteren Vorzeichenwechsel ordnet r51 der Port-/Zeitumkehr zu. Auch die getrennte r84.2-Spinorlesart ändert die interne Ladungsdichte nach Rücktransport nicht. Damit fällt die direkte Identifikation mit einem M↔T-ungeraden Dipol in diesen Realisierungen aus. Eine eigenständige Grenzflächenabbildung bleibt offen. [Frame-Prüfung](../notes/research/op5_bifocal_response_2026_11_18/W2_Frame.md).

## Grenzflächenpolarisation als physikalisches Modell

Zwei getrennte Träger einer globalen Ladung können eine orientierte Besetzungsdifferenz bilden. Ihr räumlicher Dipol ist proportional zu Abstand mal Ladungsdifferenz. Eine radiale lineare Sondenantwort liest den ersten Kosinuskoeffizienten bei kleiner Trennung proportional dazu aus. Der Überschuss ist bei geschlossenen Außenrändern nur dann konstant, wenn netto kein Ladungsfluss die Schnittstelle quert. Trennung, Randbedingung und Sondenwirkung sind bislang Modellannahmen. [Grenzflächenrechnung](../notes/research/op5_bifocal_response_2026_11_18/Grenzflaeche.md).

Die einfache ebene statische W2-Higgsgrenze zwischen h=0 und dem gebrochenen Minimum existiert im quellenfreien radialen Ansatz nicht: Das erste Integral verlangt gleiche Potentialwerte an beiden Enden. Eine zusätzlich bereitgestellte halbunendliche Massenbarriere reflektiert Subgap-Moden. Ein neutraler massiver Skalar liefert einen expliziten Dipolkern, ist aber eine neue Kopplung und erzeugt einen eigenen quadratischen Energiebeitrag. [Herleitung](../notes/research/op5_bifocal_response_2026_11_18/Grenze_W2.md).

Die beiden Vorzeichen eines reell eingeschränkten W2-Higgsfelds sind im komplexen Dublett durch einen durchgehenden Weg von Minima verbunden. Ein zusätzlicher reeller Ordnungsparameter mit diskreter Symmetrie hat dagegen eine explizite Kinkwand mit positiver Spannung. Eine vorzeichenwechselnde Dirac-Masse kann dort eine gebundene Mode ohne Normalstrom tragen. Dies ist keine allgemeine Abschirmung zweier Reservoirs und folgt nicht aus W2 allein. [Wand und Fermionmode](../notes/research/op5_bifocal_response_2026_11_18/Domaene.md).

## Selbstschließende Grenzfläche

Ein dissipatives Modell, in dem der Fluss den Wandzustand verändert, kann einen Überschuss trotz verbleibenden Antriebs sperren. Der Endwert hängt von Anfangsüberschuss und Schaltschwelle ab. Eine endliche Leckage löst die Sperre auf und führt auf den energetischen Ausgleich; dieser kann eine andere, nichtverschwindende Restladung tragen. Die Wand- und Speicherenergie sind explizit, ein kosmologischer Druck und eine Casimir-Korrektur folgen noch nicht. [Modell und Rechnung](../notes/research/op5_bifocal_response_2026_11_18/Gate.md).

Die ideale Casimir-Wechselwirkung kann im Modell mit elastischem Spalt eine mechanische Schaltschwelle liefern: Bei d/d₀=4/5 verschwindet das stabile offene Minimum. Daraus folgt noch keine Transportsperre. Der reine Casimir-Beitrag skaliert bei gleichmäßiger Dilatation als ρ_C∝a⁻⁴ mit p_C=ρ_C/3 für die isotrope Dilatationsantwort. Das ist kein druckloser Überschuss und keine kosmologische Herleitung. [Casimir-Rechnung](../notes/research/op5_bifocal_response_2026_11_18/Casimir.md).
