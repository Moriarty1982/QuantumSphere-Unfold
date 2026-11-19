# OP5: Pauli-Grenze der Wandbeladung

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/e5e75b0c8ee23c05bd6a9ab4429eab5f218d3ca9/notes/research/op5_bifocal_response_2026_11_18/Pauli_Beladung_Vorab.md). Verwendet wird der Einfang unter Emission genau einer masselosen Translationswelle aus [Wandeinfang.md](Wandeinfang.md). Annahmen: lokal ebene ruhende Wand, ein einfallendes Fermion der äußeren Ruhemasse M, leerer skalarer Endkanal und ein bei schneller tangentialer Relaxation näherungsweise gefüllter Fermikreis bis k_F. Die Relaxation selbst wird nicht hergeleitet. Bei einer großen Kugel ist die ebene Kinematik eine lokale Dünnwandnäherung.

## Schräger Einfall

Sei P der Betrag des einfallenden Tangentialimpulses, E²=M²+p_n²+P² und k die Tangentialenergie des gebundenen Endfermions. Die emittierte Wandwelle trägt E−k. Tangentialimpulserhaltung erfordert, dass die beiden Vektoren der Längen k und E−k einen Summenvektor der Länge P bilden können. Die Dreiecksungleichung ergibt

    (E−P)/2 ≤ k ≤ (E+P)/2.

Für P=0 ist k=E/2. Bei beliebiger Richtung ist für gegebenes E der größte erreichbare Wert als Grenzwert bei streifendem Einfall mit p_n→0 gegeben:

    k_max(E) = [E+√(E²−M²)]/2.

Die Grenzrichtung selbst hat keinen einfallenden Normalfluss. Ein freier Endzustand für nichtverschwindenden Normalfluss ist nur erreichbar, wenn k_max(E)>k_F. Für k_F>M/2 ist die erforderliche Einfallsenergie daher strikt größer als

    E_min(k_F) = k_F + M²/(4k_F),
    E_min−M = (2k_F−M)²/(4k_F).

Senkrechter Einfall verlangt stattdessen E>2k_F. Das sind kinematische Schwellen, keine Winkelmittelung eines Matrixelements. Ein beliebig kaltes Reservoir mit E→M erreicht nur die Umgebung von k=M/2. Ein Reservoir mit hochenergetischem Ausläufer kann weiter beladen, soweit Einfangmatrixelement und Fluss ausreichen. Ohne Relaxation kann der Einfang schmale Impulsbereiche füllen; die Grenze für einen bereits gefüllten Kreis ist dann keine Vorhersage für die tatsächliche Besetzung.

## Vergleich mit dem radialen Druckausgleich

Nach [Wandladung.md](Wandladung.md) gilt für g entartete Wandzweige und nackte Spannung σ am radialen Minimum k_*=(12πσ/g)^(1/3). Gegen direkte Emission bei Ruhe muss im Modell k_*<M gelten. Kalter fortgesetzter Einfang bis zum Gleichgewicht bei dessen Fläche ist kinematisch ohne hochenergetischen Ausläufer nur im Bereich k_*≤M/2 möglich; für Abstand von der Sättigungsgrenze ist die strikte Form k_*<M/2 relevant. Das entspricht σ<g M³/(96π). Im Bereich M/2<k_*<M sind die Träger zwar nach diesem Kriterium gebunden, aber kalte Einfälle können eine schon weit gefüllte Wand dort nicht weiter beladen.

Dieser Vergleich schließt eine frühere Beladung bei größerer Fläche nicht aus. Für festes N gilt k_F∝A^(−1/2). Bei erhaltener Ladung kann Kontraktion k_F nach dem Einfang steigern. Wenn ein kalter Fluss die notwendige Ladung bei einer größeren Kugelfläche gerade bis M/2 speichert, gilt für Beladungsradius und späteren Gleichgewichtsradius R_load/R_*=2k_*/M. Bei noch niedrigerer Anfangskante müsste die Beladungsfläche entsprechend größer sein. Dies entscheidet weder Einfangzeit noch Formstabilität.

## Prüfung des lösbaren Kinks

Schreibe y für die Yukawa-Kopplung, damit g nur die Zahl der Wandzweige bezeichnet. Für χ=v tanh(x/ℓ), M=yv und Mℓ=1 ist σ=4v²/(3ℓ)=4v²M/3. Damit

    k_*/M = [16π/(g y²)]^(1/3).

Das Emissionskriterium verlangt g y²>16π. Die strengere kalte Direktbeladung am Gleichgewichtsradius verlangt g y²>128π. Bei einer einzelnen Dirac-Sorte (g=1) entspricht das y>√(128π)≈20,1; im exakt lösbaren Profil gilt außerdem λ=2y². Die Konstruktion liefert bei wenigen Wandzweigen somit keine perturbativ abgesicherte kalte Direktbeladung. Viele Zweige, ein anderes Profil oder die Beladung bei größerer Fläche ändern die Voraussetzungen; ihre Realisierbarkeit wurde hier nicht geprüft.

## OP5

Das Ergebnis trennt drei Bedingungen: ein von null verschiedenes Einfangsmatrixelement, ausreichend freie Endzustände und Energie unter der Emissionsschwelle nach der Bildung. Die vorhandene Wandrechnung gibt hierfür Schranken, aber keine Bildungsrate, native W2-Kopplung oder H96-Quote. Die I3-Lesart bliebe erst nach einer unabhängig begründeten Materiekomponente prüfbar.
