# OP5: Gemeinsames Wigner-Gewicht und Kandidat für das ungerade Plateau

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/d511097b45f9d192141179e6125c9d5240793be0/notes/research/op5_bifocal_response_2026_11_18/Wigner_Induktion_Vorab.md). Fortsetzung von [Schaleninduktion.md](Schaleninduktion.md) und [Ungerade_Induktion.md](Ungerade_Induktion.md). Intrinsischer masseloser Diracoperator auf der runden Kugel, flächenerhaltende Variation mit Profil P_ℓ und vollständig gefüllte positive Schalen.

## Eine Übergangsformel für alle Grade

Schreibe k für die positive Anfangsschale, n für den Betrag der Endschale, j=k−1/2 und j′=n−1/2. Die beiden Chiralitätskomponenten eines normierten Spinors mit nichtverschwindender Eigenenergie tragen gleiche Norm und haben Spin-Gewichte ±1/2. In einer spin-gewichteten Basis ist die Multiplikation mit P_ℓ diagonal in diesen beiden Komponenten. Die [spin-gewichtete Gaunt-Regel](https://academic.oup.com/mnras/article/547/2/stag331/8488767) gibt für jede normierte Komponente den Faktor √[(2k)(2n)] mal einem 3j-Symbol für die magnetischen Zahlen und einem 3j-Symbol für die Spin-Gewichte. Die beiden Spin-Gewichtssymbole haben wegen Vorzeichenumkehr dieselbe Betragsquadrate. Für jedes n sind die beiden Dirac-Endzustände die zwei gleichgewichteten Kombinationen der Chiralitätskomponenten. Die Summe der Betragsquadrate über diese beiden Endsignaturen ist daher die Übergangsstärke einer normierten einzelnen Komponente. Kugelparität weist die gesamte Stärke einem Vorzeichen zu: Das positive Band hat Orbitalparität (−1)^(n−1), das negative (−1)^n. Somit ist nur ν=s_n n mit s_n=(−1)^(ℓ+n−k) möglich. Die [3j-Orthogonalität](https://dlmf.nist.gov/34.3) ergibt bei Summe über die magnetischen Zahlen den Faktor 1/(2ℓ+1). Es folgt

    T_{k,s_n n} = (2k)/(2ℓ+1) p_n,
    p_n = (2n) [ 3j(j,ℓ,j′; −1/2,0,1/2) ]²,
    max(1,k−ℓ,ℓ+1−k) ≤ n ≤ k+ℓ.

Die p_n sind nichtnegative Clebsch-Gordan-Gewichte und summieren sich zu eins. 176 Inkremente (2≤ℓ≤12, 1≤k≤16) aus der exakten Formel wurden mit der unabhängigen orbitalen Legendre-Rekursion verglichen. Die maximale absolute Abweichung war 1,0·10⁻¹³.

## Die noch zu beweisende Identität für ungerade Grade

Für ungerades ℓ ist s_n n niemals das positive Band k. Der Diagonalterm entfällt. Die universelle Formel des vorherigen Induktionsversuchs wird damit zu

    A_{k,ℓ} = [2k³/(2ℓ+1)] [ 1/(2k) + Σ_n p_n/(k−s_n n) ].

Um die algebraische Aufhebung für beliebiges ungerades ℓ abzuschließen, genügt jetzt die gemeinsame Identität Σ_n p_n/(k−s_n n)=−1/(2k) für k≥(ℓ+1)/2. Unterhalb dieser Grenze ist A_{k,ℓ}>0 bereits allgemein bewiesen, da dann ℓ≥2k gilt. Die Umschreibung der Übergangsgewichte ist bewiesen. Die Gleichheit des gewichteten Mittelwerts ist der offene Schritt.

## Kandidat für den Plateauwert

Aus den ersten exakt ausgerechneten Plateaus ergibt sich als Kandidat für ungerades ℓ≥3

    B_plateau(ℓ) = [(ℓ−1)ℓ(ℓ+1)(ℓ+2)/(64(2ℓ+1))]
                    × [ (ℓ−1)!! / ℓ!! ]².

Die Doppel-Fakultät multipliziert Faktoren derselben Parität herunter bis 1 oder 2. Die Formel wurde an den aus ℓ≤25 bekannten Werten erkannt und danach mit exakter rationaler Wigner-Rechnung für sämtliche ungeraden Grade 27 bis 43 bestätigt. Insgesamt stimmen die aus den jeweils ersten (ℓ−1)/2 Inkrementen gebildeten endlichen Summen bei allen 21 ungeraden Graden von 3 bis 43 exakt überein. Für ℓ≤25 wurden außerdem pro Grad die späteren Schalen k=(ℓ+1)/2, k+1 zu dieser Schwelle, ℓ, ℓ+1 und 2ℓ+1 exakt auf Null geprüft. Das [Skript](wigner_schalen.py) reproduziert diese Prüfungen. Für beliebige Grade ist die Produktformel ein Kandidat. Die endlichen Summen sind von der unbewiesenen allgemeinen Aufhebung späterer Schalen zu unterscheiden. H96 bleibt offen.
