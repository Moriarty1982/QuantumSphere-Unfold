# Fokusvertauschung und der Kreisgrenzfall

Analytische Erkundung gemäß [Vorab-Notiz](Symmetrie_Vorab.md), Commit b8af20ed2d4dbfb88cfca88e24b036f7bd79f35f. Ergänzt Steifigkeit.md. Das Modell hat feste Ruhelänge und positive Umfangssteifigkeit.

Sei w der vorzeichenbehaftete halbe Brennpunktabstand. Fokustausch w↦−w lässt den Abstandsmonitor exakt invariant. Am Kreis w=0, b=a, liefert die Taylorrechnung mit kleiner Halbachsenantwort v:
G(t)=2 sin²t·[v+w²/(2a)]+O(v², v w², w⁴).
Die zweite Potenz der hier ungestörten Fokuskoordinate bedeutet: Austauschparität erzwingt keine verschwindende Energiekrümmung von sich aus, aber die Energie ist die Summe quadrierter Residuen, und diese beginnen nach Minimierung bei Ordnung w². Zum Vergleich liegt bei getrennten Foki w=c+u bereits die lineare Störung 2cu in w²−c²=2cu+u². Der Fokustausch bildet dort auf den Ausgang bei −c ab, nicht auf u↦−u innerhalb desselben Ausgangs.

Mit A=⟨(2 sin²t)²⟩=3/2 und S=κπ² folgt am Kreis:
v*(w)=−A w²/[2a(A+S)]+O(w⁴),
E_min(w)=AS w⁴/[8a²(A+S)]+O(w⁶).
Die lokale Minimumsfamilie ist glatt in w², da der v-Hessian am Ausgang A+S>0 ist. Für a=1, κ=1: v*/w²→−0,0659654 und E_min/w⁴→0,1627630. Direkte Minimierung der nichtlinearen Energie auf 512 Punkten für w=0,04; 0,02; 0,01; 0,005 ergibt für den zweiten Quotienten 0,1627583; 0,1627618; 0,1627627; 0,1627629.

Für OP5: Falls die physikalische Eigenladungsdichte Q den signierten Abstand lokal linear anregt, beginnt dieser Modellbeitrag zum Druck erst in vierter Ordnung (p=Qρ'−ρ). Würde Q dagegen linear die austauschgerade Größe w² anregen, wäre die Energie wieder quadratisch in Q. Auch eine unabhängige direkte Energie ∝w² ist mit Austauschparität verträglich und wurde hier nicht angesetzt. Weder die Quellenabbildung noch das Fehlen solcher Terme und auch keine native Identifikation des Kreisgrenzfalls sind gezeigt. OP5 und H96 bleiben offen.
