# Ausfrieren: endliche Transmission, endlicher Ladungsaustausch

Analytische Erkundung nach [Vorab-Notiz](Ausfrieren_Vorab.md), Commit 912aa32fff24f6251e9b7505ddb50d301576382e. Mitbewegte Ladung Q, fester mitbewegter Gleichgewichtswert Q_eq, effektive Rate Γ(t)≥0 je Eigenzeit. Kein neuer Satz über die native Grenzfläche.

Der Ansatz Q̇=−Γ(t)(Q−Q_eq) ist exakt lösbar: Q(t)−Q_eq=(Q₀−Q_eq)exp[−∫_(t₀)^t Γ(t')dt']. Für Q₀≠Q_eq bleibt ein von null verschiedener Abstand genau dann, wenn die gesamte Restwirkung ∫_(t₀)^∞ Γ dt endlich ist. Das bedeutet asymptotische Speicherung, nicht exakt verschwindenden Fluss zu einem endlichen Zeitpunkt. Ein kleiner konstanter Quotient Γ/H=ε>0 genügt bei unbeschränkt wachsendem a nicht, weil das Integral ε ln(a/a₀) divergiert.

Für Γ=Γ₀(a/a₀)^(-n), Γ₀>0: Bei a/a₀=(t/t₀)^p mit p>0 ist das Integral endlich genau bei pn>1, Wert Γ₀t₀/(pn−1); bei pn=1 logarithmisch divergent. Bei a/a₀=exp[H(t−t₀)] mit H>0 ist es für n>0 endlich, Wert Γ₀/(nH). Beispiel im reinen Potenzmodell mit n=3: bei p=2/3 ist die Restwirkung Γ₀t₀, bei p=1/2 ist sie 2Γ₀t₀. Eine positive Transmission aus Transmission.md bestimmt Γ nicht; die Rate hängt zusätzlich vom Zustrom und von der Kopplung ab.

Nachtrag zum Vorwissen: H48 (notes/research/v4_10_0_h48/Ergebnis_H48_Einfrieren_beta.md) untersucht eine andere M/T-Observable und enthält den einschlägigen Vorbefund. Das dortige Einfrieren trat in allen gerechneten Läufen auf, aber die Auswahl eines universellen Werts war widerlegt. Die hier geprüfte skalare Grenzflächenrate macht die Abhängigkeit von Anfangswert und Geschichte explizit; sie ist keine Wiederholung von H48 mit geändertem Ergebnis.

Für OP5: Endliche Restwirkung kann eine perfekte Sperre als Voraussetzung zur Speicherung ersetzen. Das Modell liefert weder den heutigen H96-Wert noch die Lage der relevanten Epoche oder einen drucklosen Tensor. Ein weiterer Fit der Rate wäre ohne native Ankopplung und definierte Quelle nicht aussagekräftig. OP5 und H96 bleiben offen.
