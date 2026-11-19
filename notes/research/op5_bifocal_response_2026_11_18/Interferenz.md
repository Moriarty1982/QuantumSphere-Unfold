# Interferenz mit einer gebundenen Wandmode

Analytische Erkundung mit numerischer Kontrolle. [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/ff203eddc8e388a28ebca6380de1746c1619706f/notes/research/op5_bifocal_response_2026_11_18/Interferenz_Vorab.md). Die Geometrie im [Kontaktstreifen](Kontaktstreifen.md) erhöhte die Transmission bei kleinerem Spalt. Hier erhält der Leitungsplatz 0 stattdessen einen kohärenten Seitenzweig mit einer gebundenen Mode. Die zusätzliche Kopplung ist eine Modellannahme. Der Modelltyp ist als [Fano-Resonanz in diskreten Leitungen](https://doi.org/10.1103/PhysRevE.72.056611) bekannt.

## Exakte Streuung

Die Leitung hat Hopping −J mit J>0. Die Wandmode hat Energie E₀ und reelle Kopplung g≠0 (Wahl ihrer Phase). Für ihre Amplitude b gilt (E−E₀)b=gψ₀. Einsetzen in die Gleichung am Leitungsplatz 0 ergibt den lokalen Term V(E)ψ₀ mit V(E)=g²/(E−E₀). Für E=−2J cos k und 0<k<π lauten die Streuansätze links exp(ikn)+r exp(−ikn) und rechts t exp(ikn). Die Nachbargleichungen geben ψ₀=1+r=t. Die Gleichung bei n=0 liefert (2iJ sin k−V)t=2iJ sin k. Ein- und Auslaufgeschwindigkeit sind gleich. Damit gilt

    T(E) = 4 J² sin²(k) (E−E₀)² / [4 J² sin²(k) (E−E₀)² + g⁴].

Liegt E₀ im offenen Band, verlangt die ursprüngliche Seitengleichung bei E=E₀ unmittelbar ψ₀=0 und damit t=0 sowie r=−1. Bei jeder anderen Energie im offenen Band gilt T>0.

## Endliches Energiefenster

Für x=E−E₀ klein und γ=g²/(2J sin k₀), wobei E₀=−2J cos k₀, ist T(E₀+x)=x²/γ²+O(x³). Im gleichmäßig gewichteten symmetrischen Fenster E₀±Δ vollständig innerhalb des offenen Bandes ergibt die Taylorentwicklung

    mittleres T = Δ²/(3γ²) + O(Δ⁴).

Für J=g=1 und E₀=0 ergibt sich T(E)=E²(4−E²)/[1+E²(4−E²)] und γ=1/2. Die zusammengesetzte Mittelpunktregel auf der positiven Fensterhälfte (Symmetrie) mit 8.192 Teilintervallen ergab:

| Δ | mittleres T | mittleres T / Δ² |
|---:|---:|---:|
| 0.2 | 0.048475387 | 1.211885 |
| 0.1 | 0.013003291 | 1.300329 |
| 0.05 | 0.003312243 | 1.324897 |

Bei 4.096 Teilintervallen änderten sich die Mittel um weniger als 4,4·10⁻¹⁰. Der Quotient nähert sich dem analytischen Wert 4/3.

## Folgerung für OP5

Die Seitenmode kann den Durchlass bei einer exakt abgestimmten Energie vollständig unterdrücken. Für jedes Energiefenster positiver Breite im Leitungsband bleibt der Mittelwert positiv. Dasselbe gilt bei einer nichtnegativen integrierbaren Energiegewichtung mit positivem Gesamtgewicht innerhalb des offenen Bandes. Ein Nullzustand der Kinkwand allein liefert weder die Matrixelemente der seitlichen Kopplung noch eine auf die Resonanz konzentrierte Einspeisung. Eine native Begründung aus W2 oder durch OP2 und der OP5-Guard H96 bleiben offen.
