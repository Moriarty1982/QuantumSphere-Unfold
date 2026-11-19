# OP5: Vollständige Schaleninduktion für alle ungeraden Formgrade

Analytischer Beweis mit exakter Kontrolle nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/0ec241c56ac3b53c7f080c042385973b78b41231/notes/research/op5_bifocal_response_2026_11_18/Legendre_Induktion_Vorab.md). Fortsetzung von [Wigner_Induktion.md](Wigner_Induktion.md) und [Schaleninduktion.md](Schaleninduktion.md). Intrinsischer Diracoperator auf der Einheitskugel, Anfangsschale k>0 und Profil u=P_ℓ mit ungeradem ℓ. Für Kugelradius R kommt in der Energie der Faktor 1/R hinzu.

## Resolvente im entgegengesetzten Paritätsraum

Schreibe D=σ·L+1, d=k−1 und t=x·y für Punkte x,y der Einheitskugel. Die positive Anfangsschale P_k besitzt orbitalen Grad d und Parität (−1)^d. Multiplikation mit ungeradem u führt in den entgegengesetzten Orbitalparitätsraum. Auf diesem Raum ist k−D invertierbar. Für die orbitale Quantenzahl l hat σ·L die möglichen Eigenwerte l und −l−1. Somit gilt

    (k−D)⁻¹ = (k+σ·L) [d(d+1)−L²]⁻¹

auf dem entgegengesetzten Paritätsraum. Hier bezeichnet L² das Quadrat des Drehimpulsoperators. Der skalare inverse Operator, auf Null auf dem Raum gleicher Parität ergänzt, hat Kugelkern −Q_d(t)/(4π). Dabei ist Q_d die reelle Legendre-Funktion zweiter Art im Intervall, normiert durch

    Q_d(t) = (1/2) PV ∫_{−1}^1 P_d(s)/(t−s) ds.

Die Normierung folgt aus der [Legendre-Integralformel](https://dlmf.nist.gov/14.12), oder aus Q₀(t)=atanh(t) und der Rekursion. Zur Prüfung des Kerns: Q_d hat Parität (−1)^(d+1), und die Legendre-Differentialgleichung mit ihrem Wronskian am Rand gibt ∫_{−1}^1 P_l Q_d dt=2/[l(l+1)−d(d+1)] bei entgegengesetzter Parität. Der Additionssatz liefert damit den genannten Multiplikator. Die Randwerte von (1−t²)Q_d′ sind 1 bei t=1 und (−1)^d bei t=−1.

Der positive Projektor P_k hat Kugelkern (k+σ·L_x)P_d(t)/(4π). Der Resolventenkern entsteht entsprechend aus −(k+σ·L_x)Q_d(t)/(4π). Weil L_x P_d(t)=−i(x×y)P_d′(t), ergibt die Spinorspur des Produkts der Kerne an (x,y) und (y,x)

    −2/(4π)² [k² P_d Q_d + (1−t²)P_d′ Q_d′].

Der erste Kugelkern ist glatt. Die Logarithmen und die erste Ableitung des Resolventenkerns sind im Winkelintegral integrierbar. Der Funk-Hecke-Satz und ∫_{S²} u² dΩ=4π/(2ℓ+1) geben für die gewichtete Kehrwertsumme der Übergangsstärken

    S = Σ_ν T_{k,ν}/(k−ν)
      = −1/(2ℓ+1) ∫_{−1}^1 P_ℓ(t)
                  [k² P_d Q_d + (1−t²)P_d′Q_d′] dt.

## Der entscheidende Randterm und die Polynommomente

Setze F=P_d Q_d und J_{d,ℓ}=∫_{−1}^1 P_ℓ F dt. Die Legendre-Differentialgleichungen beider Faktoren geben

    k² P_d Q_d + (1−t²)P_d′Q_d′
        = k(2k−1) F + [(1−t²) F′]′/2.

Partielle Integration gegen P_ℓ liefert für ungerades ℓ einen Randbeitrag genau eins: (1−t²)F′ geht an beiden Enden gegen eins, P_ℓ hat die Randwerte +1 und −1, und (1−t²)P_ℓ′ F verschwindet. Damit

    S = −[1 + (k(2k−1)−ℓ(ℓ+1)/2) J_{d,ℓ}]/(2ℓ+1),
    A_{k,ℓ} = −k²/(2ℓ+1) [k(2k−1)−ℓ(ℓ+1)/2] J_{d,ℓ}.

Um J auszuwerten, symmetrisiere die Hauptwertformel. Mit demselben symmetrischen Ausschluss der Diagonale in beiden Integralen gilt

    J_{d,ℓ} = (1/4) ∫∫ P_d(t)P_d(s)
                         [P_ℓ(t)−P_ℓ(s)]/(t−s) dt ds.

Der Differenzenquotient ist ein Polynom vom Gesamtgrad ℓ−1. Bei ℓ≤2d−1 enthält jedes seiner Monome in mindestens einer Variable einen Exponenten kleiner d. Wegen der Orthogonalität von P_d verschwinden alle diese Momente. Also J_{d,ℓ}=0 für ungerade ℓ≤2d−1. Im Grenzfall ℓ=2d+1=2k−1 verschwindet der Vorfaktor k(2k−1)−ℓ(ℓ+1)/2 direkt. Folglich gilt

    A_{k,ℓ}=0 für jedes ungerade ℓ≤2k−1,
    Σ_n p_n/(k−s_n n)=−1/(2k) im selben Bereich.

## Vollständiger Induktionsschritt für ungerade Grade

Für jeden ungeraden ℓ≥3 sind die ersten (ℓ−1)/2 Inkremente strikt positiv nach dem bereits bewiesenen Bereich ℓ≥2k. Alle folgenden sind exakt null nach diesem Nachweis. Mit B_{1,ℓ}>0 und B_{L+1,ℓ}=B_{L,ℓ}+A_{L+1,ℓ} folgt B_{L,ℓ}>0 für jede endliche Anzahl L voller Schalen und jedes ungerade ℓ≥3. Das Plateau beginnt bei L=(ℓ−1)/2. Für ℓ=1 verschwinden alle Inkremente, entsprechend der Translationskontrolle.

Die [exakte Legendre-Kontrolle](legendre_schalen_kontrolle.py) wertet den Differenzenquotienten mit rationalen Momenten aus. Für 1≤k≤20 und ungerade 1≤ℓ≤21 stimmten 220 Werte exakt mit der unabhängigen Wigner-Rechnung überein, einschließlich der Schritte vor dem Plateau. Der allgemeine Beweis der Produktformel für die Plateauhöhe und die allgemeinen geraden Grade bleiben offen. H96 bleibt offen.
