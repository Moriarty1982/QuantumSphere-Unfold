# Signierte Brennpunktstörung als Dipolauslesung

Analytische Erkundung mit numerischer Kontrolle gemäß [Vorab-Notiz](Dipol_Vorab.md), Commit 9c87c803cd452b32dbedc4325c5f41cec9b89daf. Entlang einer orientierten Chartachse liegen die bezeichneten Foki bei ±w, der Rand bei (a cos t,b_eff sin t). Setze D=d_-−d_+.

Aus der Differenz der quadrierten Abstände folgt D(t)=4aw cos t/(d_-+d_+). D ist gegenpunktungerade, sein gleichgewichtiger Mittelwert ist exakt null. Sein RMS ist bei w↦−w gleich und trägt kein Vorzeichen. Die dimensionslose Dipolkoordinate q=⟨D cos t⟩/a ist dagegen unter Fokustausch ungerade, sofern die Bezugsachse und das Raster festgehalten werden.

Auf der exakten Reparaturellipse mit d_-+d_+=2a gilt D=2w cos t, also q=w/a und RMS(D)=√2 |w|. Auf der steifen minimierten Familie um den Kreis ist d_-+d_+=2a+O(w²); damit q=w/a+O(w³) und die Zuordnung ist lokal invertierbar. Der Leitterm der Energie aus Symmetrie.md wird damit AS a² q⁴/[8(A+S)] + O(q⁶), A=3/2, S=κπ². Ein expliziter Energieanteil proportional zu q² bleibt mit Austauschparität verträglich.

Kontrolle der steifen Familie auf 512 Winkelpunkten, a=κ=1: |w|=0,04, 0,02, 0,01 ergibt q/w=0,9998263, 0,9999566, 0,9999891. E_min/q⁴=0,1628714, 0,1627901, 0,1627698 konvergiert zum analytischen Wert 0,1627630. Bei Vorzeichenwechsel wechselt q das Vorzeichen, die Energie bleibt gleich. Der Mittelwert von D blieb unter 7·10⁻¹⁸ im Betrag.

OP5: Das Modell besitzt eine explizite signierte geometrische Koordinate und der quartische Term übersteht den Koordinatenwechsel. Der Dipol ist auf eine orientierte Bezugsachse bezogen, kein isotroper Mittelwert. Ohne eine aus M/T/P hergeleitete Achse, eine Quellenabbildung und einen Erhaltungssatz ist q keine kosmologische Ladungsdichte. OP5 und H96 bleiben offen.
