# W2-Higgsgrenze und ein expliziter neutraler Sondenkanal

Analytische Erkundung nach [Vorab-Notiz](Grenze_W2_Vorab.md), Commit 8edb4b4d35a7659a0499ef2f267cd52e7502898c. Statische, flache Modellreduktionen in einem gemeinsamen Ruhesystem. Keine native Identifikation der Seiten mit M/T.

## Die einfache W2-Higgsgrenze scheitert

W2 setzt V(h)=−μ²h²+λh⁴ mit μ²,λ>0 und h=|Φ|. Für statische ebene Profile mit festem Higgswinkel, ohne Eichfelder und Fremdquellen, wähle die Energie (Z/2)h'²+V(h), Z>0 (beim reellen Radius in der notierten W2-Normierung Z=2). Die Gleichung Z h''=V'(h) liefert das erste Integral Z h'²/2−V(h)=konstant. Geht h' auf beiden Seiten gegen null, müssen die beiden asymptotischen Potentialwerte gleich sein. Bei h=0 ist V=0, beim Minimum h=v=μ/√(2λ) ist V=−μ⁴/(4λ). Folglich gibt es keine solche statische ebene Grenzlösung von 0 nach v. Das schließt externe Stabilisierung, andere Felder, andere Randzustände, dynamische Lösungen und gekrümmte Geometrie nicht aus.

Wird eine halbunendliche Massenbarriere unabhängig bereitgestellt, ist die Reflexion unterhalb der Schwelle dagegen herleitbar: Im stationären 1D-Dirac-Teil gilt im konstanten Barrierengebiet k²=ω²−m_B². Für |ω|<|m_B| bleibt nur die ins Unendliche abklingende Lösung. Der stationäre Normalstrom ist ortsunabhängig und tendiert dort gegen null, also verschwindet er überall und ein auf der anderen Seite propagierender Einfall wird vollständig reflektiert. Für eine endliche Barriere folgt kein exakt verschwindender Strom aus diesem Argument. W2 bestimmt hier keine getrennten Zustände beidseits einer gemeinsamen Barriere.

## Explizite Sondenantwort als ergänzendes Feldmodell

Für eine neutrale reelle Sonde σ mit Massenskala m_s>0 setze im statischen Ruhesystem die Funktionalform E[σ;ρ]=∫[(|∇σ|²+m_s²σ²)/2−gσρ] d³x. Die Variation ergibt (−Δ+m_s²)σ=gρ. Außerhalb einer Punktquelle liefert die radiale Gleichung den abklingenden Modus exp(−m_s r)/r; das Integral über eine kleine Kugel fixiert K(r)=exp(−m_s r)/(4πr). Für zwei Quellen Q_M,Q_T bei ±de/2 ist σ=g[Q_M K(|x−de/2|)+Q_T K(|x+de/2|)]. Am Ring r=a folgt für den Kosinuskoeffizienten
g d (Q_M−Q_T)(1+m_s a)exp(−m_s a)/(8π a²)+O(d³).
Vorausgesetzt sind kleine d/a sowie ein glatter Kernel am Messradius und punktförmig angenäherte Quellen. Die statische Kopplung an ρ benutzt ein vorgegebenes Ruhesystem. W2 enthält in der geprüften Form keine solche lineare Ladungsquelle für ein neutrales skalares Messfeld.

Die Sonde liefert ein explizites Feldgesetz für den Dipol, gleichzeitig führt Eliminieren von σ bei glatten Quellen zu −g²〈ρ,K*ρ〉/2 in der vollständigen angesetzten statischen Energie einschließlich Quellkopplung. Das ist ein zusätzlicher quadratischer Beitrag und keine Herleitung eines drucklosen Tensors. Punktquellen dienen hier nur der Fernfeldauslesung; ihre Selbstenergie wird nicht als endlich behauptet. Die einfache native Grenzherleitung scheitert; OP5 und H96 bleiben offen.
