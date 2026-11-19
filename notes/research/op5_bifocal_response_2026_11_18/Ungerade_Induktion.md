# OP5: Exakte Schaleninduktion für die Formgrade fünf und sieben

Analytische Erkundung mit exakter symbolischer Rechnung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/49e2f7581c6b2323acbf1190a0b8aa3eaf1a9c95/notes/research/op5_bifocal_response_2026_11_18/Ungerade_Induktion_Vorab.md). Fortsetzung von [Schaleninduktion.md](Schaleninduktion.md) und [Oktupol_Schalen.md](Oktupol_Schalen.md). Intrinsisches masseloses Kugelmodell bei konstanter Fläche und vollständig besetzten positiven Dirac-Schalen.

## Exakte Rechnung statt Toleranzentscheidung

Für den ungeraden Formgrad ℓ koppelt P_ℓ vom positiven Band k zu positiven Bandsprüngen der ungeraden Abstände ±1,±3,…,±ℓ. Die negativen Bänder haben nach Drehimpuls und Parität Betragsabstände 0,±2,…,±(ℓ−1). Der Übergang zu −k hat den Energiefaktor k+ν=0. Abwärtsstärken ergeben sich aus Selbstadjungiertheit und für den Wechsel zum negativen Spektrum zusätzlich aus Chiralität.

Für einen Orbitalsprung von l nach l+d zerlegt die Rekursion jeden Pfad in den kürzesten Weg und Paare von Hin- und Rückschritten. Der kürzeste Weg enthält je eine Wurzel aus der cos-θ-Rekursion. Jedes Hin- und Rückpaar trägt das Quadrat eines solchen Koeffizienten. Nach Herausziehen des kürzesten Wegs ist der Rest ein rationales Polynom in der magnetischen Quantenzahl. Nach der Spinaddition gilt das auch für die quadrierten Matrixelemente: Das Mischprodukt beider Spinanteile enthält eine Wurzel aus einer rationalen Quadratzahl. Über ihren Vorzeichenast entscheidet die nichtnegative Standardwahl der einzelnen Wurzeln auf den zulässigen Pfaden. Die Summe über m lässt sich damit exakt durch Bernoulli-Polynome auswerten.

Das [SymPy-Skript](ungerade_schalen_exakt.py) setzt diese Übergangsstärken in

    A_{k,ℓ} = 2k²/(2ℓ+1) + Σ_{ν≠k} [k(k+ν)/(2(k−ν))] T_{k,ν}^{(ℓ)}

ein. Für allgemeines k≥ℓ+1 vereinfacht sich die resultierende rationale Funktion für ℓ=5 und ℓ=7 identisch zu null. Alle Fälle k≤ℓ werden in exakter Arithmetik mit der direkten, bei den tatsächlich vorhandenen orbitalen Zuständen endenden Rekursion berechnet. Es folgt

| Grad ℓ | positive exakte Inkremente ab k=1 | A_{k,ℓ}=0 ab | B_{L,ℓ} auf dem Plateau |
|---:|---|---:|---:|
| 5 | 14/165, 14/55 | k=3 | 56/165 für L≥2 |
| 7 | 9/140, 198/875, 1287/3500 | k=4 | 576/875 für L≥3 |

Die unabhängige numerische Legendre-Rekursion bis L=96 weicht in B_{L,ℓ} um weniger als 1,1·10⁻¹¹ von diesen exakten Folgen ab.

## Folgerung für den Induktionsschritt

Bei ℓ=5 und ℓ=7 ist B_{1,ℓ}>0, und B_{L+1,ℓ}=B_{L,ℓ}+A_{L+1,ℓ} mit A_{L+1,ℓ}≥0 für jede volle Schalenanzahl. Damit ist die Induktion für beide Formgrade abgeschlossen. Insbesondere handelt es sich bei den numerischen Werten nahe null in den späteren Schalen um exakte Aufhebung. Zusammen mit dem Oktupol sind drei ungerade Fälle bewiesen. Für beliebige ungerade ℓ bleibt die symbolische Aufhebung im allgemeinen ℓ-abhängigen Übergangsmuster offen. OP5/H96 bleiben offen.
