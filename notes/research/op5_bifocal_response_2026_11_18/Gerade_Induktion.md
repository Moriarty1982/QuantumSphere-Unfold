# OP5: Vollständige Schaleninduktion für alle geraden Formgrade

Analytischer Beweis mit exakter Kontrolle nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/3b0b29c0d6bac7c08dacbfafdcf621491aa645b8/notes/research/op5_bifocal_response_2026_11_18/Gerade_Induktion_Vorab.md). Fortsetzung von [Gerade_Resolvente.md](Gerade_Resolvente.md) und [Schaleninduktion.md](Schaleninduktion.md). Intrinsisches masseloses Kugelmodell, positive Dirac-Schalen vollständig besetzt, flächenerhaltende Variation. Alle Koeffizienten beziehen sich auf die quadratische Antwort bei festem endlichem L.

## Exaktes Produkt für die skalare Resolvente

Schreibe λ_m=m(m+1), d=k−1 und a=|d−ℓ|, b=d+ℓ. Die Bahndrehimpulse im Legendre-Produkt sind S={a,a+2,…,b}. Definiere Z={a+1,a+3,…,b−1}. Die skalare Resolvente besitzt die geschlossene Form

    R(x)=Σ_{m∈S} w_m/(x−λ_m)
        = ∏_{z∈Z}(x−λ_z) / ∏_{m∈S}(x−λ_m),
    w_m=(2m+1) [3j(d,ℓ,m;0,0,0)]².

Zur Herleitung setze N=(b−a)/2, m=a+2i und t=(b+m)/2. Die [3j-Fakultätendarstellung](https://dlmf.nist.gov/34.3) gibt mit C_j=(2j)!/(j!)²

    w_m = (2m+1) C_i C_{a+i} C_{N−i}/[(2t+1)C_t].

Die Produktresiduen und diese Gewichte haben denselben Quotienten am nächsten Pol:

    w_{m+2}/w_m =
        [(2i+1)(N−i)]/[(i+1)(2N−2i−1)]
        × [(m+b+2)(m+a+1)(2m+5)]/[(m+a+2)(m+b+3)(2m+1)].

Für die Produktresiduen erhält man diesen Quotienten durch Zerlegung λ_m−λ_j=(m−j)(m+j+1) und Kürzen der jeweils um zwei verschobenen Produkte. Für die w_m folgt er aus C_{j+1}/C_j=2(2j+1)/(j+1). Beide Residuensummen sind eins. Für die w_m folgt das aus dem Legendre-Produkt bei t=1 in der Winkelvariablen. Für das rationale Produkt folgt es aus dem Leitglied 1/x. Damit sind alle Residuen identisch, und die rationalen Funktionen stimmen überein. Bei N=0 folgt die Aussage direkt aus dem einzelnen Pol. Die Produktidentität selbst verlangt keine gerade Parität von ℓ.

## Schranke am Pol d für gerade ℓ

In dem noch offenen Bereich ℓ≤2k−2 schreibe ℓ=2q mit d≥q≥1. Dann liegt d im Träger S, und J=2w_d/(2d+1)>0. Setze D=2d+1, s=min(q,d−q). Die Pole relativ zu d haben die geraden Offsets −2s,−2s+2,…,2q. Die Nullstellen dazwischen haben die ungeraden Offsets. Aus der logarithmischen Ableitung des Produkts nach Entfernung des Pols erhält man

    I/J = D [ Σ_{z∈Z} 1/(λ_d−λ_z)
                    − Σ_{m∈S, m≠d} 1/(λ_d−λ_m) ].

Für einen Offset n≠0 ist D/(λ_d−λ_(d+n))=−1/n+1/(D+n). Paare nun positive und negative Seiten. In den Beiträgen aus −1/n heben sich die ersten s Paare auf. Übrig bleibt −Σ_{j=s+1}^q [1/(2j−1)−1/(2j)]. Aus 1/(D+n) sind die positiven Offset-Paare nichtnegativ. Die negativen Offset-Paare liefern −Σ_{j=1}^s [1/(D−2j)−1/(D−2j+1)]. Jeder Unterschied 1/x−1/(x+1) ist durch den größeren Unterschied 1/x−1/(x+2) nach oben beschränkt. Die beiden Summen teleskopieren daher in der Schranke

    −I/J ≤ 1/(2s+1) − 1/(2q+1) + 1/(D−2s) − 1/D.

Nach Gerade_Resolvente.md ist
     
    A_{k,ℓ}=k²(c I+h J)/(2ℓ+1),
    c=(2(d−q)+1)(d+q+1)>0,
    h/c=1/k+(4k−1)/(2c)−1/D.

* Falls d≥2q, gilt s=q und D−2s≥k. Die Schranke für −I/J ist höchstens 1/k−1/D, strikt kleiner als h/c.
* Falls q≤d<2q, gilt s=d−q und D−2s=2q+1. Die Schranke für −I/J ist 1/(2s+1)−1/D. Weil d+q+1≤2d+1 und 4k−1=4d+3, gilt (4k−1)/(2c)>1/(2s+1). Also liegt die Schranke wieder strikt unter h/c.

Somit ist c I+h J>0 im gesamten verbleibenden geraden Bereich. Für ℓ≥2k war A_{k,ℓ}>0 bereits durch den Übergangsabstand bewiesen.

## Vollständige Induktion und Kontrolle der Geltung

Für alle geraden ℓ≥2 und alle k≥1 ist jetzt A_{k,ℓ}>0 bewiesen. Zusammen mit dem [ungeraden Beweis](Legendre_Induktion.md) folgt per B_{L+1,ℓ}=B_{L,ℓ}+A_{L+1,ℓ}: Für jede volle positive Schalenanzahl L≥1 und jeden Formgrad ℓ≥2 ist B_{L,ℓ}>0. Bei ungeraden Graden bleiben die bereits bewiesenen exakt verschwindenden späteren Inkremente bestehen. Wegen der Rotationssymmetrie ist die intrinsische quadratische Form auf allen flächenerhaltenden Formmoden modulo Translation positiv in dem betrachteten Modell. Die Störungsrechnung garantiert für sich weder dynamische Stabilität noch ein nichtlineares Minimum in einem unbegrenzten Funktionenraum.

Die [exakte Produktkontrolle](gerade_induktion_produkt.py) verglich in rationaler Arithmetik 800 Paare (d,ℓ) für 0≤d≤49 und gerade 2≤ℓ≤32, jeweils mitsamt sämtlichen Residuen. Bei 664 Paaren mit d∈S prüfte sie außerdem den regulären Teil und die beiden Ungleichungen. Alle Prüfungen stimmen. Die geschlossene Produktformel für die Höhe des ungeraden Plateaus und H96 bleiben offen.
