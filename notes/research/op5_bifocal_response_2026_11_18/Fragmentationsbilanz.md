# OP5: Gemeinsame Fragmentationsbilanz von Schalen und Krümmung

Analytische Erkundung mit numerischer Kontrolle nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/9baae3304384b1cc0573e026639d8abe37bc3140/notes/research/op5_bifocal_response_2026_11_18/Fragmentationsbilanz_Vorab.md). Additiver Dünnwand-Kontrollansatz für weit getrennte runde Kugeln mit großen einzelnen Teilchenzahlen. Die intrinsische Energie aus [Dirac_Schalen.md](Dirac_Schalen.md), das lokale fermionische Hauptsymbol aus [Normalmoden_Biegung.md](Normalmoden_Biegung.md) und der starre skalare Anteil aus [Wandform.md](Wandform.md) werden gemeinsam ausgewertet. Andere Beiträge derselben Ordnung werden dadurch nicht bestimmt.

## Kugelzuschlag aus extrinsischer Krümmung

Für eine Kugel gilt ∫(2H)² dA=16π und ∫K dA=4π. Bei Fermienergie pro Fläche ε_F ist daher

    C_ext = 4π(2κ_F + κ_G,F + κ_G,χ)
          = 4π[ ε_F (μ₂−(6/5)J k_*²) + κ_G,χ ].

Dabei stammt κ_G,χ aus dem zweiten Normalmoment der ebenen skalaren Energiedichte. Beim lösbaren Tanh-Profil mit Mℓ=1 gilt

    μ₂ = π²/(12M²),
    κ_G,χ = (σ/M²)(π²/12−1/2).

Für die zweite Gleichung ist das normierte zweite Moment von sech⁴ u gleich π²/12−1/2. Es folgt aus der zweiten Ableitung der normierten Fouriertransformierten |Γ(2+it/2)|²/Γ(2)² bei t=0. Die Kontrollintegration ergab 0,322467033424115 für das dimensionslose Moment.

Am führenden radialen Gleichgewicht ist ε_F=2σ, k_*³=12πσ/g und die Kontinuumsenergie pro Teilchen μ₀=k_*. Schreibe r=k_*/M und j=M⁴J≈0,711747742502. Damit

    C_ext/(g μ₀) = r²/3 [π²/4−1/2 − (12/5)j r²] ≔ C(r).

Diese Korrektur ist von Ordnung N⁰ und bei festem r für jede große Kugel dieselbe. Ihre führende Bewertung am ungestörten radialen Minimum ist konsistent: Eine relative Verschiebung des Minimums durch einen glatten Term von Ordnung N⁰ ist von Ordnung 1/N und ändert die führende Korrektur nicht. Die Nutzung des lokalen extrinsischen Terms zusammen mit der diskreten intrinsischen Besetzung ist eine Modellannahme auf führender Ordnung.

## Vergleich mit dem Schalengewinn

Für große N lautet die intrinsische Schalenkorrektur pro Kugel in Einheiten g μ₀

    c(η) = 1/3−(2η−1)²/4,   1/12≤c(η)≤1/3,

wobei η den relativen Füllstand der letzten Schale bezeichnet. Die für zwei Tochterkugeln verfügbare Energie ist daher

    Δ/(g μ₀) = c(η_Mutter)−c(η_Tochter1)−c(η_Tochter2)−C(r)+o(1).

Der maximale asymptotische Schalengewinn ist durch 1/3−2·(1/12)=1/6 begrenzt, unabhängig vom Teilungsverhältnis bei zwei jeweils großen Töchtern. C(r)>1/6 ist deshalb hinreichend, um die energetische Aufspaltung für alle Füllungen in dieser Ordnung zu verhindern. Bei Gleichheit müssen die Restterme aufgelöst werden. Die Lösung C(r)>1/6 im gebundenen Bereich 0<r<1 ist näherungsweise

    0,615294 < r < 0,879293.

Das Maximum von C liegt bei r≈0,758862 und beträgt etwa 0,188828. Unterhalb der hinreichenden Schranke reicht der Schalenfüllstand allein nicht zur Entscheidung.

## Numerische Kontrolle an gleich großen Tochterkugeln

Für dieselben 300 Partitionen wie in Dirac_Schalen.md wurde der exakte intrinsische Energieunterschied mit dem führenden konstanten Extrinsikzuschlag verrechnet. Die Tabelle zählt positive Δ. Bei g=1 war der größte intrinsische Gewinn im Raster Δ_intr/μ₀≈0,166666666648.

| r | C(r) | positive Δ unter 300 Partitionen |
|---:|---:|---:|
| 0.55 | 0.146276 | 87 |
| 0.65 | 0.175435 | 0 |
| 0.70 | 0.184630 | 0 |
| 0.75 | 0.188727 | 0 |
| 0.90 | 0.157616 | 59 |
| 0.95 | 0.128081 | 119 |

Die 300 Partitionen sind eine rechnerische Kontrolle der gewählten Folge. Sie liefern keine Häufigkeit realer Zerfälle. Für kleine Kugeln ist der konstante Dünnwandzuschlag keine kontrollierte Näherung.

## Einordnung

Das additive Modell weist für einen Bereich des Bindungsparameters nach, dass die berechnete extrinsische Krümmungsenergie den maximalen intrinsischen Schalengewinn überwiegt. Ein Teil dieses Bereichs liegt zugleich unter der konservativen Emissionskante r=3^(−1/3) aus Wandkontraktion.md, allerdings unter den dort festgelegten Anfangsbedingungen. Weder Formstabilität noch dynamischer Zerfall folgen aus dem Vergleich zweier Endzustände. Profilrelaxation und weitere mikroskopische Terme können den Extrinsikzuschlag verschieben. Die [Rechnung von Ogure et al.](https://arxiv.org/abs/hep-ph/0212332) behandelt eine verwandte vollständiger entwickelte Fragmentationsbilanz. OP5/H96 bleiben offen.
