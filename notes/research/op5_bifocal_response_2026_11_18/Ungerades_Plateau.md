# OP5: Geschlossene Höhe der ungeraden Dirac-Schalenplateaus

Analytischer Beweis im intrinsischen masselosen Kugelmodell mit vollständig besetzten positiven Dirac-Schalen und festgehaltener Fläche. Es gilt die Normierung ΔE = (g/R) δ² B_(L,ℓ) + O(δ³) für das Profil P_ℓ. Die frühere [Produktvermutung](Wigner_Induktion.md) gilt für jedes ungerade ℓ≥3:

    B_(L,ℓ) = (ℓ−1)ℓ(ℓ+1)(ℓ+2)/[64(2ℓ+1)] · [(ℓ−1)!!/ℓ!!]²,
    L ≥ (ℓ−1)/2.

## Produktresolvente vor der Plateauschwelle

Setze ℓ=2n+1, d=k−1 und λ_m=m(m+1). Für 1≤k≤n+1 hat das Legendre-Produkt P_d P_ℓ die orbitalen Grade m=ℓ−d, ℓ−d+2, …, ℓ+d. Sie sind alle größer als d und haben entgegengesetzte Parität. Ist w_m das zugehörige Gaunt-Gewicht, liefert das [Legendre-Moment](Legendre_Induktion.md)

    J_(d,ℓ) = ∫ P_d(t)P_ℓ(t)Q_d(t) dt
             = Σ_m 2w_m/(λ_m−λ_d) = −2R(λ_d).

Die Integration läuft von −1 bis 1. In der [Produktresolvente](Gerade_Induktion.md) stehen im Nenner die Grade m=ℓ−d+2i, i=0,…,d, und im Zähler die dazwischenliegenden Grade z=ℓ−d+2i+1, i=0,…,d−1. Zerlege jeden Term durch λ_m−λ_d=(m−d)(m+d+1). Die beiden Nennerprodukte laufen dann in Zweierschritten von 2(n−d)+1 bis 2n+1 und von 2n+2 bis 2(n+d+1). Die Zählerprodukte laufen von 2(n−d+1) bis 2n und von 2n+3 bis 2(n+d)+1. Das Verhältnis ist

    −R(λ_d) = r² b_k,
    r = (2n)!!/(2n+1)!!,
    b_k = a_(n+1−k) a_(n+k),   a_j = binom(2j,j)/4^j.

Die leeren Produkte bei d=0 sind eins. Der Vorfaktor aus dem ungeraden Legendre-Beweis faktorisiert. Damit lautet das Inkrement

    A_(k,ℓ) = r²/(2ℓ+1) · k² p(k) b_k,
    p(k) = (ℓ+1−2k)(ℓ+2k).

Für k=n+1 gilt p(k)=0. Nach dem ungeraden Induktionsbeweis sind auch alle späteren Inkremente null.

## Teleskopsumme

Erweitere b_k auf −n≤k≤n+1 und setze b_(n+2)=0. Mit q(k)=p(1−k) gilt

    q(k+1)b_(k+1)=p(k)b_k     (1≤k≤n+1).

Für k≤n folgt dies aus a_(j+1)/a_j=(2j+1)/(2j+2), am rechten Rand aus p(n+1)=0. Die diskrete Stammfunktion findet sich durch einen kubischen Ansatz für G(k) und Koeffizientenvergleich:

    G(k) = (k−1)[8k²−ℓ(ℓ+1)]/64,
    C = (ℓ−1)ℓ(ℓ+1)(ℓ+2)/64,
    p(k)G(k+1)−q(k)G(k) = k²p(k)/2−C.

Die letzte Identität folgt durch Ausmultiplizieren. Definiere H_k=q(k)G(k)b_k. Dann hat (k²p(k)/2−C)b_k die Stammfunktion H_(k+1)−H_k. Beide Randwerte verschwinden, H_1 wegen G(1)=0 und H_(n+2) wegen b_(n+2)=0.

Die Binomialreihe Σ_(j≥0) a_j x^j=(1−x)^(-1/2) quadriert sich zu (1−x)^(-1). Daher ist Σ_(k=−n)^(n+1) b_k=1, der Koeffizient bei x^(2n+1). Unter k ↦ 1−k haben die beiden Hälften gleiche Gewichte und keinen Fixpunkt. Also ist Σ_(k=1)^(n+1) b_k=1/2. Summation der Stammfunktion ergibt

    Σ_(k=1)^(n+1) k² p(k)b_k = 2 C · (1/2) = C.

Multiplikation mit r²/(2ℓ+1) liefert die behauptete Plateauhöhe.

## Exakte Kontrolle und Geltung

[Kriterium vor der Gegenrechnung](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/9f01a2dc21159700e96c5e97cb07fedd514ac9af/notes/research/op5_bifocal_response_2026_11_18/Ungerades_Plateau_Vorab.md). Die [Kontrolle](ungerades_plateau_kontrolle.py) bestätigt die Polynomidentität symbolisch und vergleicht 252 Inkremente für ungerade 3≤ℓ≤43 in rationaler Arithmetik mit der vorhandenen Spin-Wigner-Routine. Alle 21 Plateaus und die jeweils erste verschwindende Schale stimmen exakt. Die Rechnung ist nicht blind.

Das Ergebnis quantifiziert die quadratische Formantwort. Für den Übergang zu OP5 fehlen weiter die native Kopplung an die Formantwort und eine physikalische Ausleseabbildung. Nichtlineare und dynamische Stabilität sowie H96 bleiben offen.
