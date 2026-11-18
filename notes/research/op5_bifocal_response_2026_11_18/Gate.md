# Selbstschließende Grenzfläche: Restladung, Leckage und Energie

Analytische Erkundung mit numerischer Kontrolle nach [Vorab-Notiz](Gate_Vorab.md), Commit 9688a4ddd23c2222772d4bccad6198932f9b06ca. Phänomenologische dissipative Ruhesystem-Zelle, kein aus W2 hergeleiteter Schalter und kein Casimir-Spektrum.

Mit Q̇=−2F und ṡ=ηF gilt Q(s)=Q₀−2(s−s₀)/η. Für E=Q²/(2χ)+Ks²/2 und A=2Q/χ−ηKs folgt Ė=−AF. Die gewählte Antwort F=G(s)A mit G≥0 macht Ė=−G A²≤0. Diese Energie ist die explizite Zellenergie; die abgegebene Energie wäre in einem vollständigen System dem Empfänger zuzurechnen.

Bei A(s₀)>0 verschwindet der Antrieb bei s_eq=(2Q₀/χ+4s₀/(ηχ))/(4/(ηχ)+ηK). Bei perfekter Sperre ε=0 läuft s gegen min(s_eq,s_c). Wenn s_eq>s_c, schließt die Schnittstelle asymptotisch, obwohl noch ein positiver Antrieb besteht; Q_end=Q₀−2(s_c−s₀)/η. Liegt s_eq unter s_c, stoppt der Strom am energetischen Ausgleich bei offenem Kanal. Bei Gleichheit fallen beide Grenzen zusammen. In der geschlossenen Kurve legt die Barriere fest, wie viel Ladung übergeht, nicht einen universellen Endwert. Der Endwert enthält die Anfangsdaten.

Bei ε>0 gibt es keine perfekte Sperre. Asymptotisch erreicht das System s_eq und Q_eq=χηKs_eq/2. Oberhalb der Schaltschwelle ist die Relaxationsrate G₀ ε(4/χ+η²K); ein kleiner Leckstrom kann also einen langen Zwischenzustand liefern. Er entfernt den Unterschied zwischen dem eingefrorenen Wert und dem energetischen Gleichgewicht, nicht zwingend jede Restladung.

Beispiel mit χ=K=η=G₀=s_c=1, s₀=0. RK4 auf der exakten Bilanzgeraden bis t=200 mit dt=0,01:
| Q₀ | ε | s_end | Q_end | E_end | Ausgang des Modells |
|---:|---:|---:|---:|---:|---|
| 4 | 0 | 1 | 2 | 2,5 | Sperre trotz nichtnulligem Antrieb |
| 2 | 0 | 0,8 | 0,4 | 0,4 | energetischer Ausgleich bei offener Barriere |
| 4 | 0,05 | 1,6 | 0,8 | 1,6 | Leckage bis zum energetischen Ausgleich |

Bei geschlossener Wand kostet ihr Zustand Ks_c²/2 je Modellzelle; außerdem ist die hier gewählte Speicherenergie quadratisch in Q. Ohne Volumenabhängigkeit, kovarianten Tensor und Herkunft der Schalterparameter lässt sich daraus kein kosmologischer Druck ableiten. Die ideale Sperre wird über G eingesetzt. Eine Casimir-artige Korrektur würde ein zusätzlich berechnetes Spektrum und einen Referenzzustand verlangen und ist in den Zahlen nicht enthalten. OP5 und H96 bleiben offen.
