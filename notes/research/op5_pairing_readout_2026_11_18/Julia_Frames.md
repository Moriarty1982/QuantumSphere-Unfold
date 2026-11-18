# Kristall–Julia-Auslesung in Konvention F

Analytische Erkundung mit numerischer Kontrolle. [Vorab-Notiz](Julia_Vorab.md), Commit 48107ad259ccac0783d5c1aa2eb9319d355f4283.

Historischer Anhang C: F_c(w)=1/conj(w²+c), c=−1+iγ. Behalte den gemeinsamen Kristallträger. M und T sind getrennt typisierte Randkarten. Setze für die Kontrolle bedingt R(w)=iw als induzierte Koordinatenabbildung. P braucht eine eigene Abbildung oder einen unabhängig begründeten Grenzübergang; γ=0 ist das Referenzpanel im selben Chart.

## M–T-Kontrolle

F_T=R F_c R⁻¹ erfüllt F_T(w)=−i/conj(w²−c). Induktiv gilt R⁻¹F_Tⁿ(Rw)=F_cⁿ(w); die Identität reicht als rationale/antirationale Abbildung auch über Pole auf der Riemannschen Sphäre. Alle identisch definierten Masken und Diagnosen sind auf dem zurücktransportierten Raster gleich. Das umfasst Tunnelbreite, Randintensität und Öffnungswinkel, sofern deren Auswertung vollständig aus den identischen Daten und derselben Kalibrierung erfolgt. Die drei historischen Maße wurden nicht separat rekonstruiert.

Numerische Kontrolle: 128×128 Startpunkte mit Koordinaten (j−63,5)/40 und (k−63,5)/40, j,k=0,…,127. Pro Startpunkt 32 Iterationen; nach jedem Schritt das Bit |w|>1 speichern. M startet bei w, T bei Rw. Für γ=0, 0,000075, 0,000179 und 0,000338 jeweils 0 unterschiedliche 32-Bit-Folgen von 16 384. Negativkontrolle: Die Formel F_c unverändert auf Rw anzuwenden erzeugt jeweils 15 176, 14 592, 14 416 und 14 368 abweichende Folgen. Dieser Effekt ist durch die unterlassene Transformation erzeugt.

## Versuch zur OP5-Schließung

Auf einem gemeinsamen Raster sei h_M das M-Bild und h_T^→M das zurücktransportierte T-Bild. Bei der geprüften reinen Transportregel gilt h_M=h_T^→M punktweise. Die Differenz verschwindet vor jeder Aggregation. Das historische η_f=1/3−β_f² ist ebenfalls gerade unter Vorzeichenwechsel von β_f und kann keinen ungeraden Kanal auszeichnen.

Setzt man verschiedene positive Antwortgewichte A und B auf dasselbe Profil h, ergibt die integrierte Differenz über die integrierte Summe (A−B)/(A+B), sofern das Profil ein nichtnulliges Integral besitzt. Der Randfaktor kürzt sich; die Gewichte und ihre Bedeutung werden damit nicht bestimmt. Die Konstruktion liefert keinen Stress-Energie-Tensor, keine Ableitung der Druckregel p=−2B und keine Bedingung für die Erhaltungsgröße C in k193. Der Photonensektor kann ohne eigene Randkarte kein unabhängiges drittes Datum liefern. Damit ist diese Route als reine Koordinatenübertragung ausgeschöpft. Für einen weitergehenden Kandidaten müsste die Zell-Dynamik eine vom Rücktransport verschiedene physikalische Sondenantwort oder eine gravitative Quellenabbildung liefern. OP5, H96 und die Kern-Guards bleiben offen.
