# Integrierte Transmission an der gekrümmten Kontaktlinie

Analytische Erkundung mit numerischer Kontrolle nach [Vorab-Notiz](Kontaktstreifen_Vorab.md), Commit 47402e57e7c8610b4658c1a4686f73c4afbe7c36. Lokale Kanalnäherung mit gleichen masselosen Leitungen, fester Barrierenmasse m und konstanter Einfallsdichte quer zur Kontaktlinie. Keine kohärente Streuung zwischen Kanälen und kein Kontaktmodell.

Für die lokale Spaltweite h(y)=d+y²/(2R) und κ=√(m²−ω²)>0 gilt T(h)=[1+(m²/κ²)sinh²(κh)]⁻¹. Der auf die konstante Einfallsdichte normierte Durchlass pro Linienlänge ist G(d)/L=∫ T(h(y))dy. T ist für h>0 streng fallend. Daher steigt der Gesamtwert auf jeder festen positiven Querbreite bei fallendem d strikt an. Der formale Grenzwert bei d→0 ist positiv. Auch auf der ganzen idealisierten Querrichtung ist er endlich und positiv, da T einen gaußartig abfallenden Schwanz in y hat. Ein kleiner Bereich, in dem h/d nahe eins ist, bedeutet daher nicht, dass der transportaktive Bereich verschwindet.

Für κd≫1 ist T(h)≈4κ² exp(−2κh)/m². Auf der idealisierten ganzen Linie ergibt sich G/L≈(4κ²/m²)√(πR/κ) exp(−2κd). Die wirksame Querbreite in diesem Tunnelgrenzfall folgt aus der Zerfallslänge der Barriere und aus R. Sie verkleinert sich bei festem R nicht proportional zu √d. Das Regime darf nicht bis zum Nahkontakt extrapoliert werden.

Kontrolle mit m=1, ω=1/2 und R=100, auf |y|≤20 mit 4096 Mittelpunktintervallen: Bei d=1, 7/9, 1/10, 0 sind die mittleren Transmissionswerte 0,219563; 0,302502; 0,632441; 0,674984. d₀=1 dient der Normierung der separat angesetzten mechanischen Schwelle. Der letzte Wert ist ein formaler Grenzwert der lokalen Kanalnäherung, kein Wert für realen Kontakt.

Damit scheidet auch die geometrische Verengung des Kontaktstreifens allein als Sperre im geprüften Modell aus. Für OP5 müsste eine physikalische Schnittstellenregel z.B. die Barrierenmasse, Zufluss- oder Kopplungsstruktur ändern oder die integrierte Restwirkung aus Ausfrieren.md begründen. Die Kanalrechnung liefert keine native Kopplung, keinen gravitativen Tensor und keinen H96-Wert.
