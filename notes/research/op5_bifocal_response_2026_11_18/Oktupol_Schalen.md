# OP5: Exakte oktupolare Antwort aller vollständigen Schalen

Analytische Erkundung mit Kontrolle nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/fd967a30d114a3e2f5cf3bc04aa2c5a18257bd6d/notes/research/op5_bifocal_response_2026_11_18/Oktupol_Schalen_Vorab.md). Fortsetzung von [Hoehere_Formmoden.md](Hoehere_Formmoden.md). Intrinsischer masseloser Kugel-Diracoperator, feste Fläche 4πR², vollständig gefüllte positive Schalen bis L. Die Verformung besitzt das axiale Profil u=P₃(cos θ) und die kleine dimensionslose Amplitude δ.

## Endliche Übergänge

In der positiven Schale k gilt l=k−1 und j=k−1/2. Setze C_{l,a}=√[(l²−a²)/(4l²−1)] mit null für einen unzulässigen Rekursionsschritt. Aus P₃(x)=(5x³−3x)/2 folgen die zwei orbitalen Aufwärtsmatrixelemente

    O₁(l,a) = (C_{l+1,a}/2)[5(C_{l,a}²+C_{l+1,a}²+C_{l+2,a}²)−3],
    O₃(l,a) = (5/2) C_{l+1,a} C_{l+2,a} C_{l+3,a}.

Für l'=l+d definiere den positiven Clebsch-Gordan-Vektor w_{l,m}=(√[(l+1/2+m)/(2l+1)], √[(l+1/2−m)/(2l+1)]). Der negative Vektor ist w_{l,m} um 90 Grad in diesem Komponentenpaar gedreht. Das Spinormatrixelement ist das Skalarprodukt des Endvektors mit diag[O_d(l,m−1/2),O_d(l,m+1/2)] w_{l,m}. Quadrieren und Summieren von m=−k+1/2 bis k−1/2 liefert für die zur Energie beitragenden Aufwärtsstärken

    a(k) = T_{k,k+1}    = 3k(k−1)(k+1)(k+2)/[7(2k−1)(2k+1)(2k+3)],
    c(k) = T_{k,k+3}    = 5k(k+1)(k+2)(k+3)/[7(2k+1)(2k+3)(2k+5)],
    b(k) = T_{k,−(k+2)} = 15k(k+1)(k+2)/[7(2k−1)(2k+1)(2k+3)(2k+5)].

In dieser Summe sind die quadrierten Spinorbeiträge rationale Polynome in m. Die Radikale des Mischprodukts haben paarweise identische Faktoren. Die Auswertung benötigt nur gerade Momente bis zum sechsten Grad. Die positiven Abwärtsstärken folgen durch Selbstadjungiertheit von u, die negativen durch die zusätzliche Chiralität, die D→−D konjugiert und mit u kommutiert. Positive Übergänge k→k sind wegen orbitaler Parität null. Bei negativen Zwischenzuständen sind nach Parität und Drehimpuls nur ν=−(k±2) und ν=−k möglich. Der Term ν=−k trägt den Faktor k+ν=0 und fällt aus der Energie heraus.

## Exaktes Aufheben ab der zweiten Schale

Setze F_k(ν,T)=k(k+ν)T/[2(k−ν)] wie in [Geschlossene_Schalen.md](Geschlossene_Schalen.md). Dann gilt

    A_{k,3} = 2k²/7
              + F_k(k+1,a(k)) + F_k(k−1,a(k−1))
              + F_k(k+3,c(k)) + F_k(k−3,c(k−3))
              + F_k(−k−2,b(k)) + F_k(2−k,b(k−2)).

Für k≥4 vereinfacht sich die rationale Summe identisch zu null. Für k=1,2,3 werden nicht vorhandene Schalen weggelassen. Das gibt A_{1,3}=5/42 und A_{2,3}=A_{3,3}=0. Somit erhält man für jede endliche Anzahl voller Schalen

    B_{L,3}=Σ_{k=1}^L A_{k,3}=5/42,    L≥1,
    ΔE_intr=(5g/(42R)) δ²+O(δ³).

Die unabhängige Auswertung der Legendre-Rekursion aus Hoehere_Formmoden.md reproduzierte 5/42 für L=1,…,64 mit maximaler absoluter Abweichung 6,2·10⁻¹².

## Konsequenz

Das Oktupolprofil ist im gerechneten intrinsischen Modell für jede volle Schalenanzahl positiv in zweiter Ordnung. Jede zusätzlich vollständig gefüllte Schale ab k=2 trägt in dieser Richtung exakt null zum quadratischen Koeffizienten bei. Der zuvor berechnete lokale positive Biegeterm kommt hinzu, soweit die Dünnwandnäherung anwendbar ist. Andere höhere Formgrade, teilweise gefüllte Schalen und die dynamische Fragmentation sind damit nicht entschieden. H96 bleibt offen.
