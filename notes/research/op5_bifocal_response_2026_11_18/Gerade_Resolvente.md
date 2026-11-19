# OP5: Skalare Reduktion der geraden Schaleninkremente

Analytische Erkundung mit exakter Kontrolle nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/c6e5a286cad1255ebe5b0fa676c638c39fc7303e/notes/research/op5_bifocal_response_2026_11_18/Gerade_Resolvente_Vorab.md). Fortsetzung von [Legendre_Induktion.md](Legendre_Induktion.md). Intrinsischer Kugel-Diracoperator D=σ·L+1, positive Anfangsschale k und runde Einheitskugel. Flächenerhaltendes Profil u=P_ℓ mit geradem ℓ≥2. Setze d=k−1, λ_l=l(l+1), Δ=2ℓ+1 und c=k(2k−1)−λ_ℓ/2.

## Der reduzierte Resolvent

Der gleiche Paritätsraum enthält beim Bahndrehimpuls d sowohl die ausgeschlossene positive Schale k als auch die negative Endschale −d, sofern d>0. Für Bahndrehimpuls m≠d bleibt der Resolvent (k+σ·L)/(λ_d−λ_m). Setze im skalaren Teil den Bahndrehimpuls d ganz aus und ergänze anschließend den negativen Anteil mit Projektor (d−σ·L)/(2d+1) innerhalb des orbitalen d-Raums. Sein Resolventenfaktor ist 1/(2d+1). Für d=0 ist dieser Projektor null. Diese Trennung vermeidet eine Singularität oder einen irrtümlichen Verlust der negativen Eigenzustände.

Definiere die rein skalaren Momente aus der [Gaunt-Formel](https://dlmf.nist.gov/34.3):

    J_m = ∫_{−1}^1 P_ℓ P_d P_m dt = 2 [3j(d,ℓ,m;0,0,0)]²,
    J = J_d,
    I = Σ_{m≠d} (2m+1) J_m/(λ_d−λ_m).

Die Summe ist endlich, weil |d−ℓ|≤m≤d+ℓ und m−d gerade sein muss. Die Expansion von P_ℓ P_d an t=1 gibt Σ_m (2m+1)J_m=2.

## Spur ohne Spinor-Übergangsgewichte

Wie bei der ungeraden Resolvente liefert der Projektorkern (k+σ·L)P_d/(4π) zusammen mit dem orbitalen Kern zu m≠d den Winkelterm k² P_d P_m+(1−t²)P_d′P_m′. Für jede dieser Polynomfunktionen ergibt partielle Integration

    ∫ P_ℓ (1−t²) P_d′P_m′ dt = (λ_d+λ_m−λ_ℓ) J_m/2.

Die Normsumme der J_m vereinfacht den zusätzlichen Anteil. Damit ist die gewichtete Kehrwertsumme aus Bahndrehimpulsen m≠d gleich [c I−1+(2k−1)J/2]/Δ. Der verbleibende negative Endraum mit m=d liefert λ_ℓ J/[2Δ(2k−1)]. Derselbe Spuransatz für den Übergang zurück in den positiven Eigenraum ergibt T_{k,k}=cJ/Δ. Zusammen mit dem Diagonalterm der Störungsrechnung folgt die exakte Formel

    A_{k,ℓ} = (k²/Δ) [ c I + h J ],
    h = (2k−1)/2 + λ_ℓ/[2(2k−1)] + c/k.

Insbesondere sind alle Spinor-Wigner-Zahlen durch gewöhnliche Legendre-Produktgewichte ersetzt. Bei ℓ≤2k−2 sind sowohl J als auch c strikt positiv, und der noch ausstehende Induktionsschritt hat die Form I/J≥−h/c. Für ℓ≥2k gilt J=0 und Positivität war bereits in Schaleninduktion.md gezeigt.

## Vergleich und offene Ungleichung

Die [Rechenkontrolle](gerade_resolvente_kontrolle.py) verglich 330 Werte (gerade 2≤ℓ≤22, 1≤k≤30) in rationaler Arithmetik mit der unabhängigen Spin-Wigner-Rechnung. Alle stimmen exakt überein. In allen 264 Fällen mit J>0 war I/J negativ. Beispiele am ersten erlaubten Rückübergang sind I/J=−9/20 bei k=2, ℓ=2 und −275/504 bei k=3, ℓ=4.

Somit lässt sich der positive Induktionsschritt nicht aus der Nichtnegativität des skalaren Lösungsanteils begründen. Die noch zu beweisende untere Schranke für I/J enthält jetzt jedoch nur skalare, explizit faktorielle Gewichte. Der allgemeine gerade Fall und H96 bleiben offen.
