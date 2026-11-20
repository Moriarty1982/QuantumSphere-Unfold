# OP5: Tomographie bei unbekannter Vermittlerreichweite

20. November 2026. Analytische Erkundung in M. Die [transversale Massenauslese](OP5_J_Transversale_Massenmodulation.md) liefert für eine Strahlrichtung eine mit der Yukawa-Reichweite geglättete Säulendichte. Wir prüfen, ob ideale Durchstrahlung aus allen Richtungen die dreidimensionale D-Dichte und die Vermittlermasse zugleich bestimmt. Vorausgesetzt sind das statische schwache Modell im flachen Raum, ein bekannter Phasenbezug, geradlinige vollständige Strahlwege und eine bekannte oder separat abgezogene Apparaturantwort. Es erfolgt kein H96-Datenvergleich.

## Was vollständige Strahldaten bestimmen

Verwende eine nichtnegative integrierbare Dichte $\rho$, $m>0$ und den normierten Yukawa-Kern $G_m(\mathbf r)=m^2 e^{-m|\mathbf r|}/(4\pi|\mathbf r|)$. Bezeichne mit $C_\Delta=(g_J-g_A)g_D/m^2$ den differentiellen, als räumlich konstant angenommenen Koeffizienten. Im idealen Vergleich ist die Laufzeit entlang des Strahls mit Richtung $\mathbf e$ und transversaler Koordinate $\mathbf b$ das Linienintegral von
$$
U(\mathbf x)=C_\Delta(G_m*\rho)(\mathbf x).
$$
Für reine Profiländerungen werden $\rho$ und $U$ durch ihre jeweiligen Differenzen ersetzt. Die zweidimensionale Fourier-Transformierte einer solchen Strahlprojektion ist $\widehat U(\mathbf q)$ auf der Ebene $\mathbf q\cdot\mathbf e=0$. Die Aussage folgt durch Zusammenfassen der transversalen Integration mit der Linienintegration. Alle Richtungen bestimmen damit idealerweise $U$, einschließlich der entsprechenden aus den Projektionen bestimmbaren Gesamtnormierung. [Fourier-Schnittprinzip, SIAM-Kapitel zur Radon-Transformation](https://epubs.siam.org/doi/10.1137/9780898717792.ch6)

Ist $m$ bekannt und $C_\Delta\ne0$ kalibriert, kann die Dichte formal über
$$
\rho=C_\Delta^{-1}(1-\Delta/m^2)U,\qquad
\widehat\rho(\mathbf q)=C_\Delta^{-1}(1+q^2/m^2)\widehat U(\mathbf q)
$$
zurückgerechnet werden. Hohe Ortsfrequenzen verstärken dabei Rekonstruktionsfehler. Bei unbekanntem $C_\Delta$ bleibt unabhängig davon die Skalierung $\rho\mapsto s\rho$, $C_\Delta\mapsto C_\Delta/s$ mit $s>0$.

## Nichtnegative Gegenfamilie mit gleicher Gesamtmasse

Selbst bei bekanntem $C_\Delta$ bestimmen die Strahldaten den Vermittler nur unter Zusatzannahmen. Wähle für eine beliebige andere Masse $m'\ge m$ den Faktor $a=m^2/m'^2$ und definiere
$$
\rho'=a\rho+(1-a)G_m*\rho .
$$
Mit $0<a\le1$ ist $\rho'$ nichtnegativ und hat wegen der Kernnorm eins dieselbe Gesamtmasse wie $\rho$. In Fourier-Darstellung gilt
$$
\widehat{\rho'}(\mathbf q)
=\frac{m^2+a q^2}{m^2+q^2}\widehat\rho(\mathbf q),
\qquad
\frac{m'^2}{m'^2+q^2}\widehat{\rho'}(\mathbf q)
=\frac{m^2}{m^2+q^2}\widehat\rho(\mathbf q).
$$
Somit sind $U$ und sämtliche Strahlprojektionen für das Paar $(m,\rho)$ und für $(m',\rho')$ exakt gleich. Die vier Impulse $q\in\{0,0{,}3,2,7\}$ bestätigten das für $m=2,m'=5$ bis auf Rundung. Die Konstanz von $C_\Delta$ beim Massenwechsel verlangt in der mikroskopischen Parametrisierung ein geändertes Produkt der beiden unbekannten Kopplungen, da $C_\Delta$ dort den Faktor $1/m^2$ enthält. Sind Masse und mikroskopisches Kopplungsprodukt unabhängig verknüpft, kann diese Gegenfamilie dadurch eingeschränkt werden.

Der Einwand gilt bereits für absolute positive Dichten. Werden in zwei Zuständen nur Laufzeitdifferenzen bei gleicher Gesamtmasse aufgenommen, kann dieselbe positive Transformation auf beide Zustandsdichten angewandt werden. Die Gesamtmassen bleiben dann erhalten und ihre Differenzprojektion bleibt gleich. Mehr Blickrichtungen oder eine bekannte Gesamtmasse reichen daher in dieser Dichteklasse für die getrennte Rekonstruktion von Profil und Reichweite nicht aus. Bei bekannten absoluten Daten und bekannter Gesamtmasse kann man dagegen $C_\Delta$ über $\int U=C_\Delta\int\rho$ bestimmen.

## Zwei Auswege mit zusätzlicher Information

Erstens: Ist die Quelle kompakt getragen und ein Außenbereich mit $\rho=0$ bekannt, erfüllt das gemessene $U$ dort $\Delta U=m^2U$. Auf einem offenen Teilbereich mit $U\ne0$ folgt dadurch $m^2=\Delta U/U$. Die Gegenfamilie fällt für $m'>m$ aus dieser Klasse, denn für eine nichttriviale positive Ausgangsdichte ist $G_m*\rho$ überall positiv. Bei zwei positiven kompakten Quellen mit identischem $U$ genügt sogar ihr gemeinsamer Außenbereich für die Eindeutigkeit der Masse. Bei bloßen Differenzdaten kann das Außenfeld dagegen verschwinden; dann liefert dieser Quotient dort keine Kalibrierung. Bei realen Daten erschweren der exponentielle Abfall und die zweite Ableitung den Vergleich.

Zweitens: Ist die räumliche Struktur einer Kalibrierungsdichte separat bekannt, genügen ideal zwei ihrer nichtverschwindenden Fourier-Modi mit verschiedenen Beträgen. Aus $Q_i=\widehat U(\mathbf q_i)/\widehat\rho(\mathbf q_i)$ ergibt sich
$$
R=Q_1/Q_2=\frac{m^2+q_2^2}{m^2+q_1^2},\qquad
m^2=\frac{q_2^2-Rq_1^2}{R-1}.
$$
Anschließend kann ein Modus $C_\Delta$ festlegen. Als algebraische Kontrolle liefert $m=2$ mit $q_1=1$ und $q_2=3$ das Verhältnis $2{,}6$ und die rekonstruierte Masse zum Quadrat $4$. Bei $R$ nahe eins wäre die Rückrechnung empfindlich. Weder ein garantiertes D-Vakuum noch eine unabhängig bekannte Kalibrierungsdichte ist bisher aus W1/W2 hergeleitet.

Die ideale Tomographie bestimmt somit den gefalteten Antwortkörper. Die Trennung von Dichte und Reichweite benötigt zusätzliche räumliche oder mikroskopische Information. Reale J-Observablen, der kosmologische Übergang zu allen Materiebeiträgen und H96 bleiben offen.
