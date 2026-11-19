# OP5: Können gleichnamige J-Ladungen den Fokusabstand halten?

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im statischen Materie-Ruhesystem. Die [vorige Kraftrechnung](W2_Fokusabstand.md) behandelte ladungskonjugierte Wolken. Hier dürfen die Besetzungen der beiden Foki unabhängig gewählt werden. Grundlagen sind die [J-Quellgewichte](W2_J_Eichkanal.md), die [Higgsquelle](W2_Higgsquelle.md) und die [radialen Außenamplituden](W2_Fokusprofile.md). Geprüft werden der ausgeschriebene W1-Maxwell-Term und der lineare radiale Higgsanteil von W2 auf flachem Hintergrund, ohne festgehaltene Randgeometrie, weitere Eichfelder oder Gravitation.

## Eine abstoßende J-Quelle ist mit einem B−L-Dipol vereinbar

Für die getrennten radialen Wolken seien $R>2b$ der Abstand und $b$ eine feste obere Schranke ihrer Radien. Die gewöhnlichen J-Ladungen $Q_1,Q_2$ dürfen dasselbe Vorzeichen haben. Das schließt einen B−L-Dipol selbst bei insgesamt verschwindendem B−L nicht aus. Als Belegungsbeispiel setze für die Summen der signierten Quark- und Leptonpopulationen $(N_q,N_\ell)$ am ersten Fokus $(N,0)$ und am zweiten $(N/2,N/2)$ mit $N>0$. Beide haben J-Ladung $N$, während die B−L-Ladungen $+N/3$ und $-N/3$ sind. Die Quarksumme zählt alle Farben. Das Beispiel ist eine Besetzungswahl und keine Lösung der stationären Materiegleichungen. Auf $\mathbb R^3$ ist der entsprechende Coulomb-Ausläufer mit endlicher Feldenergie vereinbar. Eine periodische Zelle ohne Randfluss würde den gesamten J-Überschuss verbieten und eine weitere Quelle verlangen.

## Der stationäre Abstand ist eine Energiebarriere

Bei festgehaltenen Profilen hat jede Wolke eine nichtnegative skalare Quelle für den Higgsradius bei $v>0$. Sie hängt von der Summe der Teilchen- und Antiteilchenbesetzungen ab. Ihre Paarenergie ist deshalb attraktiv. Zusammen mit dem J-Maxwell-Term ergibt das bis zur geprüften Ordnung

$$
E(R)=E_0+\frac{A}{R}-\frac{B e^{-mR}}R,\qquad
A=\frac{g_J^2Q_1Q_2}{4\pi},\qquad
B=\frac{a_m[S_1]a_m[S_2]}{4\pi Z_h}\ge0,\qquad m=m_h>0.
$$

$E_0$ enthält die bei festen Profilen abstandsunabhängigen Terme, $a_m$ ist das radiale Yukawa-Gewicht und $Z_h$ die Norm des Higgsgradiententerms. Für gleichnamige Ladungen ist $A>0$. Setze $H(R)=(1+mR)e^{-mR}$. Dann ist die nach außen positive Kraft

$$
F(R)=-\partial_R E=\frac{A-BH(R)}{R^2},\qquad H'(R)=-m^2R e^{-mR}<0.
$$

Für $B>0$ existiert genau eine Nullstelle im getrennten Bereich $R>2b$, falls $0<A/B<H(2b)$. Bei Gleichheit liegt sie auf der ausgeschlossenen Kontaktgrenze. Unterhalb der inneren Nullstelle überwiegt die Higgsanziehung, oberhalb die Coulombabstoßung. Die Krümmung dort ist

$$
E''(R_*)=\frac{B H'(R_*)}{R_*^2}
       =-\frac{B m^2e^{-mR_*}}{R_*}<0.
$$

Die Kräftebilanz ist ein striktes Maximum. Wenn $A\le0$ und mindestens ein Kanal aktiv ist, ist die Kraft überall anziehend. Bei $B=0$ und $A\ne0$ hat sie überall dasselbe Vorzeichen. In allen wirksamen Fällen fehlt ein stabiles getrenntes Minimum. Ohne beide Wechselwirkungen bleibt der Abstand frei.

Das Vorzeichen am stationären Punkt schließt auch ein gemeinsames lokales Minimum variabler radialer Profile und des Abstands aus, sofern man am betreffenden Profil den Abstand in beide Richtungen variieren darf. Schon die zulässige Variation bei festem Profil sieht die negative Krümmung. Für einen glatten lokal minimierenden Profilzweig mit positiv definitem Profil-Hessian verringert der Schur-Komplement-Term die effektive Abstandskrümmung zusätzlich. Diese Aussagen setzen einen offenen Bereich ohne geometrische Kontaktzwänge voraus.

## Welche Zusatzwirkung könnte den Mechanismus ändern?

Eine konstante Zugkraft $T$ (Energie je Längeneinheit) liefert im einfachen geraden Modell den Term $TR$ mit $T>0$. Diese ergänzende Dynamik ist eine Kontrolle und in W2 hier nicht hergeleitet. Für reine Coulombabstoßung $A>0$ und $B=0$ folgt exakt $R_*=\sqrt{A/T}$ mit $E''(R_*)=2A/R_*^3>0$, sofern $R_*>2b$. Bei $B>0$ ist die ursprüngliche Kraft für hinreichend großes $R$ positiv und streng fallend, denn ihr asymptotischer Leitterm ist $A/R^2$. Wählt man $L>2b$ in diesem Bereich und $0<T<F(L)$, existiert auf $R>L$ genau eine stabile Nullstelle von $F(R)-T$. Der Abstand ist damit ein Resultat des zusätzlich angesetzten mechanischen Gesetzes. Eine Stringverbindung aus I1 wäre erst nach Herleitung ihrer Kopplung zur Fokusladung, ihrer effektiven Spannung und ihrer Einordnung in Konvention F ein Kandidat für diese Rolle. Die Rechnung führt keine solche Verbindung ein.

## Konsequenz

Eine abstoßende Kraft kann im ausgeschriebenen J-Kanal vorhanden sein und der Zustand kann einen neutralen B−L-Dipol tragen. Die Kombination aus masseloser Abstoßung und kurzreichweitiger Higgsanziehung liefert hier jedoch kein stabiles Gleichgewicht. Ein aus der Wirkung bestimmter Zug- oder anderer Rückstellterm könnte den Befund ändern. I3 bleibt an eine eigenständige Überschussdynamik gebunden. Native Randwirkung und H96 bleiben offen.
