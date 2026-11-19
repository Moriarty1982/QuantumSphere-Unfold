# OP5: Teilweise gefüllte Schalen unter quadrupolarer Abplattung

Analytische Erkundung mit Kontrollintegration nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/19ffcf7389912788f1336b120955d005580fdef0/notes/research/op5_bifocal_response_2026_11_18/Schalenverformung_Vorab.md). Fortsetzung von [Dirac_Schalen.md](Dirac_Schalen.md) und [Profilrelaxation.md](Profilrelaxation.md). Intrinsischer masseloser Dirac-Operator auf einer eingebetteten Kugel mit festgehaltener Fläche und fermionischer Grundzustandsbesetzung bei fester Teilchenzahl. Die Fermionen dürfen sich bei der Verformung im betrachteten Schalenraum neu verteilen. Daraus folgt keine Aussage über Umverteilungszeiten oder einen vollständigen mikroskopischen Wandoperator.

## Störungsmatrix im Schalenraum

Schreibe die radiale Fläche als r(θ,φ)=R[1+δu(θ,φ)+O(δ²)], u=P₂(cos θ)=(3 cos²θ−1)/2. Die durch die Einbettung induzierte Metrik lautet in erster Ordnung g_δ=(1+2δu)g₀+O(δ²). Weil ∫u dΩ=0, kann die Fläche durch eine Reskalierung mit Faktor 1+O(δ²) exakt konstant gehalten werden. Die erste Störungsmatrix bleibt davon unberührt.

In zwei Dimensionen ist der bezüglich des unveränderten L²-Maßes dargestellte konforme Dirac-Operator D_δ=e^(−δu/2) D₀ e^(−δu/2)+O(δ²). Dies folgt aus der [konformen Transformationsregel](https://epub.uni-regensburg.de/25547/1/MP176.pdf) und der unitären Anpassung des Flächenmaßes. Für den Projektor P_k auf das positive Eigenband k/R gilt damit

    P_k D′ P_k = −(k/R) P_k u P_k.

Hier ist k=1,2,… die Schalenenergie in Einheiten 1/R. Für D₀=(σ·L+1)/R hat ihr positiver Teil Gesamtdrehimpuls j=k−1/2 und Bahndrehimpuls l=k−1. Axialsymmetrie macht P_k u P_k diagonal in der magnetischen Quantenzahl m. Die Clebsch-Gordan-Gewichte für die Beiträge Y_{l,m−1/2} und Y_{l,m+1/2} sind (j+m)/(2j) und (j−m)/(2j). Zusammen mit

    ⟨Y_{l,a},P₂ Y_{l,a}⟩ = [l(l+1)−3a²]/[(2l−1)(2l+3)]

ergibt sich für k≥2

    λ′_{k,m} = −(k/R) [j(j+1)−3m²]/[4 j(j+1)].

Bei k=1 verschwindet die erste Korrektur, da l=0. Im positiven Band k≥2 sind die Steigungen nicht konstant, und ihre Summe ist null, weil Σ_m m²=j(j+1)(2j+1)/3.

## Explizite zweite Schale

Für k=2, j=3/2 gilt ⟨u⟩=+1/5 bei |m|=1/2 und −1/5 bei |m|=3/2. Die beiden Doppelniveaus sind damit

    λ_|m|=1/2 = 2/R − 2δ/(5R) + O(δ²),
    λ_|m|=3/2 = 2/R + 2δ/(5R) + O(δ²).

Kontrollintegration mit 32.768 Mittelpunktintervallen in x=cos θ ergab die orbitalen Momente 0,3999999977 für Y₁₀ und −0,1999999995 für Y₁₁, daraus 0,1999999986 für |m|=1/2. Für eine Dirac-Sorte und n=1,2,3 Fermionen in der zweiten Schale ergibt die Wahl der jeweils niedrigsten Zustände den Gesamtgewinn

    ΔE_F(δ) = −[2/(5R)] min(n,4−n) |δ| + O(δ²).

Tiefer liegende voll besetzte Schalen haben keine lineare Gesamtverschiebung. Bei endlicher Gesamtzahl gelten diese Aussagen für hinreichend kleine Störungen, damit die ausgeschiedenen Nachbarschalen durch ihre Lücke getrennt bleiben.

## Folge für die Kugelform

Für jede teilweise gefüllte Schale k≥2 hat die Summe der niedrigsten n Steigungen einer nichtkonstanten spurfreien Folge ein strikt negatives Vorzeichen. Für δ<0 wählt man entsprechend die größten Steigungen der ursprünglichen Folge. Dieses Argument gilt auch bei mehreren gleichartigen entarteten Dirac-Sorten, sofern die gesamte Teilbelegung energetisch neu geordnet werden darf. Beim Wechsel des Vorzeichens der Störung kann sich das besetzte Muster ändern. Für höhere Schalen haben die beiden einseitigen Steigungen im Allgemeinen verschiedene Beträge.

Damit ist die runde Kugel im gerechneten intrinsischen Grundzustandsmodell bei offener Schale k≥2 kein lokales Energieminimum. Der separat hergeleitete positive lokale Biegeterm beginnt quadratisch in δ und kann einen negativen linearen Term im additiven Modell bei beliebig kleiner Störung nicht ausgleichen. Für eine geschlossene Schale ist nur der lineare Term null. Zur Stabilität muss dort die zweite Spektralvariation bestimmt werden. Eine eingefrorene oder durch andere Wirkungen bereits aufgespaltene Besetzung erfordert eine andere Rechnung. Aussagen über Fragmentation zwischen zwei runden Endzuständen bleiben davon logisch getrennt. OP5/H96 bleiben offen.
