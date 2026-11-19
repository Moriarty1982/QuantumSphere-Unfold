# OP5: Exakte Schalenantwort für Formgrad vier

Analytische Erkundung und numerische Kontrolle nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/b791379386c05db8c65d11e53018f8cf71140694/notes/research/op5_bifocal_response_2026_11_18/GradVier_Schalen_Vorab.md). Fortsetzung von [Oktupol_Schalen.md](Oktupol_Schalen.md) und [Hoehere_Formmoden.md](Hoehere_Formmoden.md). Positive Dirac-Schalen bis L vollständig besetzt, intrinsisches masseloses Kugelmodell und flächenerhaltendes Profil u=P₄(cos θ).

## Orbitale Übergänge

Sei k die positive Anfangsschale, l=k−1 ihr Bahndrehimpuls und a die orbitale magnetische Quantenzahl. Schreibe C_{l,a} für den Koeffizienten der cos-θ-Rekursion aus der Oktupolrechnung. Abseits der unteren Randfälle setze d(l)=C_{l,a}²+C_{l+1,a}². Aus P₄(x)=(35x⁴−30x²+3)/8 entstehen die orbitalen Koeffizienten

    O₀ = [35(d(l)² + C_{l,a}² C_{l−1,a}² + C_{l+1,a}² C_{l+2,a}²) − 30d(l)+3]/8,
    O₂ = C_{l+1,a} C_{l+2,a} [35(d(l)+d(l+2))−30]/8,
    O₄ = (35/8) C_{l+1,a} C_{l+2,a} C_{l+3,a} C_{l+4,a}.

Nicht vorhandene orbitale Zustände werden im Rekursionsschritt ausgelassen. Für jeden der beiden Spinanteile ist a=m∓1/2 einzusetzen. Mit den Spinadditionsvektoren aus Oktupol_Schalen.md quadriert man die jeweiligen Matrixelemente und summiert über m. Symmetrische Momente lassen sich durch Σ_{m=−k+1/2}^{k−1/2} m^d = [B_{d+1}(k+1/2)−B_{d+1}(−k+1/2)]/(d+1) bilden, mit den Bernoulli-Polynomen B_d. Die algebraisch erhaltenen positiven Stärken für gleiche oder höhere Schalen und die negativen Stärken zu größeren Beträgen lauten

    T_{k,k} = k(k−2)(k−1)(k+1)(k+2) / [2(2k−3)(2k−1)(2k+1)(2k+3)],
    T_{k,k+2} = 5k(k−1)(k+1)(k+2)(k+3) / [9(2k−1)(2k+1)(2k+3)(2k+5)],
    T_{k,k+4} = 35k(k+1)(k+2)(k+3)(k+4) / [36(2k+1)(2k+3)(2k+5)(2k+7)],
    T_{k,−(k+1)} = 5k(k−1)(k+1)(k+2) / [(2k−3)(2k−1)(2k+1)(2k+3)(2k+5)],
    T_{k,−(k+3)} = 35k(k+1)(k+2)(k+3) / [9(2k−1)(2k+1)(2k+3)(2k+5)(2k+7)].

Weitere Übergänge folgen aus Selbstadjungiertheit der Multiplikation mit u und der Chiralität, die D→−D konjugiert und mit u kommutiert. Die übrigen Übergänge fehlen nach Drehimpuls und Parität.

## Positiver Beitrag jeder vollen Schale

Einsetzen in die Spurformel aus Hoehere_Formmoden.md ergibt als Koeffizient pro Schale

    A_{k,4} = k²(48k⁸−280k⁶+599k⁴−385k²+108)
              / [4(2k−3)²(2k−1)²(2k+1)²(2k+3)²].

Für k=1,2,3,4 ist die Formel auch direkt mit den tatsächlich vorhandenen Schalen geprüft. Die ersten Werte sind 1/10, 8/35, 1733/4410 und 190768/266805. Für k≥2 setze z=k²−4≥0. Das Zählerpolynom nach Abtrennen von k² lautet dann

    48 z⁴+488 z³+1847 z²+3255 z+2520,

also A_{k,4}>0. Der Wert bei k=1 ist ebenfalls positiv. Damit folgt für jede endliche Zahl vollständig besetzter Schalen ΔE_intr=(g/R)δ² Σ_{k≤L} A_{k,4}+O(δ³)>0 in hinreichend kleiner nichtverschwindender Verformung. Der Koeffizient der Summe wächst asymptotisch wie L³/64. Diese asymptotische Aussage gilt für den Koeffizienten, ohne eine in L uniforme Störungsgrenze zu behaupten.

Die unabhängige Legendre-Rekursion für L=1,…,64 stimmte mit der exakten Schalenformel bis auf 5,1·10⁻¹² in der Summe überein. Bei L=64 lautet die Summe 4190,1966485381. Der positive lokale Biegeterm aus Profilrelaxation.md verstärkt die Antwort, solange seine Dünnwandnäherung anwendbar ist. Für die Formgrade 2, 3 und 4 liegt damit ein analytisches Vorzeichen vor. Ein allgemeiner Beweis für alle höheren Grade, dynamische Stabilität und H96 bleiben offen.
