# OP5: Versuch vollständiger Induktion über die Schalenanzahl

Analytische und numerische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/467dca1d555bb99e816e1fb8125d622cb9cdca6d/notes/research/op5_bifocal_response_2026_11_18/Schaleninduktion_Vorab.md). Fortsetzung von [Hoehere_Formmoden.md](Hoehere_Formmoden.md). Festgehaltene Fläche, vollständig besetzte positive Dirac-Schalen und intrinsische quadratische Energie. Für das axiale Profil P_ℓ gilt ΔE=(g/R) δ² B_{L,ℓ}+O(δ³).

## Induktionsanfang und gewünschter Schritt

Für die erste Schale ist

    B_{1,ℓ} = (ℓ−1)(ℓ+2)/[ℓ(ℓ+1)(2ℓ+1)] > 0   (ℓ≥2).

Beim Hinzufügen der nächsten vollen Schale gilt exakt B_{L+1,ℓ}=B_{L,ℓ}+A_{L+1,ℓ}. Eine hinreichende verstärkte Induktionsbehauptung ist A_{k,ℓ}≥0. Sie ist stärker als die Positivität der Gesamtsumme und folgt nicht allein aus der Induktionsannahme für B. Auch strikte Positivität jedes Inkrements wäre zu stark, denn beim Oktupol verschwinden die Inkremente ab k=2 exakt.

Mit T_{k,ν} für die quadrierten Übergangssummen und Σ_ν T_{k,ν}=2k/(2ℓ+1) lässt sich die Spurformel umschreiben zu

    A_{k,ℓ}/k² = 1/(2ℓ+1) + T_{k,k}/k
                   + Σ_{ν≠k} T_{k,ν}/(k−ν).

Denn k(k+ν)/[2(k−ν)]=−k/2+k²/(k−ν), während der Diagonalterm aus der direkten Variation k T_{k,k}/2 lautet. Die Beiträge ν>k sind in der Umschreibung die einzigen negativen. Im allgemeinen Fall ist daher noch zu zeigen, dass die Summe über T_{k,ν}/(ν−k) für ν>k höchstens die Summe der übrigen im Ausdruck stehenden nichtnegativen Terme erreicht.

## Bewiesener Teil des Induktionsschritts

Für ℓ≥2k sind alle erlaubten positiven Endschalen mindestens ν=k+2. Aus dem Dreieck der Gesamtdrehimpulse folgt k+ν≥ℓ+1. Für ℓ>2k reicht das direkt. Bei ℓ=2k muss zusätzlich ν−k gerade sein, weil sich die beiden positiven orbitalen Quantenzahlen nur um eine Zahl der Parität von ℓ unterscheiden. Damit entfällt auch ν=k+1. Es gibt keinen Diagonalterm. Also gilt

    A_{k,ℓ}/k² ≥ 1/(2ℓ+1) − (1/2) Σ_{ν>k} T_{k,ν}
                        + Σ_{ν<0} T_{k,ν}/(k−ν) > 0.

Die nichtstrikte Schranke folgt aus der Normsumme. Striktheit folgt daraus, dass mindestens ein negatives Endband tatsächlich gekuppelt ist: Wähle den obersten Anfangszustand m=k−1/2. Sein einziger nichtverschwindender Spinanteil hat die orbitale Zahl a=k−1. Der höchste Bahndrehimpuls l′=k−1+ℓ entsteht durch den führenden Term von P_ℓ und ℓ aufeinanderfolgende Aufwärtsschritte der cos-θ-Rekursion. Sein Matrixelement ist von null verschieden. Der negative Endspinor bei demselben m hat eine von null verschiedene Projektion auf diesen Spinanteil für ℓ≥2.

Damit ist für jeden Grad ℓ die Induktion bis L≤⌊ℓ/2⌋ exakt durchführbar. Insbesondere ist für jede feste Anzahl L voller Schalen der gesamte intrinsische Koeffizient bei allen ℓ≥2L positiv. Die bereits vollständigen Beweise für ℓ=2,3,4 bleiben unabhängig davon gültig.

## Numerische Prüfung der fehlenden Schritte

[hoehere_formmoden.mjs](hoehere_formmoden.mjs) wertet mit der Option --induction die Inkremente für 1≤k≤96 und 2≤ℓ≤24 aus. Unter 2208 Kombinationen war kein Inkrement kleiner als −10⁻⁸. 1218 waren größer als 10⁻⁸, 990 lagen im Toleranzband. Der kleinste positive Inkrementwert unter den geraden Graden betrug rund 0,0203401. Die betragsmäßig größte negative Rundungszahl betrug 6,8·10⁻¹²; der Normtest wich höchstens 8,6·10⁻¹⁴ ab.

Im Raster sind bei ungeradem ℓ nur die ersten (ℓ−1)/2 Inkremente aufgelöst positiv. Alle folgenden liegen im Toleranzband. Für ℓ=3 ist deren Verschwinden analytisch bewiesen, für höhere ungerade Grade ist es eine Erkundungsbeobachtung. Der numerische Befund ersetzt keinen allgemeinen Beweis im verbleibenden Bereich ℓ<2k. H96 bleibt offen.
