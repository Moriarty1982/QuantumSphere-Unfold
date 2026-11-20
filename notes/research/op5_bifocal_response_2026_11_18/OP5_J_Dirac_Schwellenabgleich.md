# OP5 — Dirac-Schwellenvergleich für den sichtbaren Krümmungsterm

20. November 2026. Analytische Erkundung im Materieframe M. Betrachtet werden zwei kanonisch normierte abelsche Felder und freie schwere Dirac-Arten. Diese koppeln minimal an dieselbe effektive Metrikstörung des massiven Hintergrunds. Es wird nur ihr Ein-Schleifen-Beitrag im niederenergetischen Vergleich bestimmt. Diese Metrikkopplung ist eine zusätzliche Modellannahme.

## Vorwissen geprüft

Der [sichtbare Krümmungsterm](OP5_J_Sichtbarer_Kruemmungsterm.md) gibt den axialen Testwellenkontrast bei eingesetzten Koeffizienten. Der [J-Eichkanal](W2_J_Eichkanal.md) hat in der verwendeten Dirac-Lesart dieselbe J-Teilchenladung für alle vier Arten. Die [neutralen Ströme](W2_Neutralstroeme.md) geben die elektrische Ladungstabelle in einer zusätzlichen elektroschwachen Referenz. W1/W2 enthalten in diesem Abgleich keine unabhängig ausgeschriebene Photondynamik mit den nötigen gemeinsamen Vermittlerkopplungen. Rückwärts wird zuerst der von Ladungs- und Massendaten bestimmte Teil des sichtbaren Koeffizienten gesucht. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese vor H96. Die Populationsdynamik für I3 bleibt getrennt.

## Der Ein-Schleifen-Beitrag ist eine Matrix

Eine Dirac-Art $i$ der Masse $m_i>0$ sieht bei Vektorladungen $(q_{iJ},q_{iA})$ die Feldstärke $\mathcal F_i=q_{iJ}F_J+q_{iA}F_A$. In der quadratischen Ein-Schleifen-Wirkung tritt damit für jedes Krümmungsinvariant die Ladungsmatrix $q_iq_i^{\mathsf T}$ auf. Für einen gemeinsamen effektiven Metrikhintergrund ist der gegenüber der Ein-Arten-Rechnung verbleibende Faktor die Matrix
$$
\mathsf G=\sum_i\frac{n_i}{m_i^2}\,q_iq_i^{\mathsf T},
$$
wobei $n_i$ die Multiplizität identischer Arten bezeichnet. Die Rechnung setzt Frequenzen und Hintergrundimpulse klein gegenüber den integrierten Massen und eine kanonische flache kinetische Normierung an der Vergleichsschwelle voraus. Beiträge aus weiteren Arten, Wechselwirkungen und lokalen Ausgangsoperatoren sind eigene Eingaben.

Im fermionischen Drummond–Hathrell-Vergleich treten neben $R_{\mu\alpha\nu\beta}F^{\mu\alpha}F^{\nu\beta}$ auch Ricci-, Skalarkrümmungs- und Maxwell-Gleichungsterme auf. Für die zitierte Konvention sind die Ricci- und Riemann-Faktoren $13/360$ bzw. $-1/360$ in Einheiten $\alpha_{\rm em}/\pi$ vor Ausklammern der inversen Fermionmasse. Die Ladungsabhängigkeit $\alpha_{\rm em}=q^2/(4\pi)$ geht bei zwei Feldern in $\mathsf G/(4\pi)$ über. [Shore, lokale effektive Photonenwirkung](https://doi.org/10.1016/S0550-3213(02)00833-7)

Im kompakten freien Testwellenvergleich ändert der Skalarkrümmungsterm in erster Ordnung nur die Maxwell-Norm. Der Maxwell-Gleichungsterm trägt auf dem ungestörten freien Zweig nicht zur linearen Dispersionskorrektur bei. An geladenen Rändern muss ein solcher Eliminationsschritt mit den Quell- und Detektortermen gemeinsam durchgeführt werden. Der Ricci-Term trägt in der geometrischen Optik mit $R_{nn}$ bei, der Riemann-Term mit $4R(n,e,n,e)$, da beide antisymmetrischen Feldstärken je zwei gleiche Kontraktionen liefern. Auf der rotationssymmetrischen Achse gilt $R_{nn}=2R(n,e,n,e)$. Der axiale Schleifenbeitrag enthält daher den kombinierten Faktor
$$
2(13/360)+4(-1/360)=11/180.
$$
In der zitierten Krümmungskonvention lautet die Laufzeitmatrix des fermionischen Beitrags folglich
$$
\delta\boldsymbol\tau_{\rm Schleife}
=\frac{11}{720\pi^2}\mathsf G\int R(n,e,n,e)\,dz .
$$
Eine zusätzliche Norm des effektiven Metrikhintergrunds gehört in die Gezeitenkontraktion. Dieser Vergleich übernimmt die Krümmungskonvention der Wilson-Koeffizienten durchgängig. Die reine Riemann-Kopplung der Vorrechnung und der volle Dirac-Schleifenvergleich sind als zwei verschiedene Wirkungsansätze zu lesen.

## Ein-Generationen-Kontrolle und Signalmischung

Setze die Ladungspaare $(g_J,eQ_i)$ für $(u,d,\nu,e^-)$ mit Farben $(3,3,1,1)$ und schreibe $w_i=m_i^{-2}$. Dann gilt
$$
\mathsf G=
\begin{pmatrix}
g_J^2(3w_u+3w_d+w_\nu+w_e) & eg_J(2w_u-w_d-w_e)\\
eg_J(2w_u-w_d-w_e) & e^2(4w_u+w_d+3w_e)/3
\end{pmatrix}.
$$
Bei formal gleichen Schwellen fällt der gemischte Eintrag heraus und die Diagonale ist proportional zu $(8g_J^2,8e^2/3)$. Das folgt aus der Summe der elektrischen Ladungen mit Farbfaktoren. Verschiedene Schwellen erhalten diese Kürzung nur, falls $2w_u=w_d+w_e$ gilt. Insbesondere hat der einzelne geladene Leptonbeitrag Rang eins bei nichtverschwindenden Ladungen. Seine unverschobene Kombination ist proportional zu $(e,g_J)$, seine verschobene zu $(g_J,-e)$. Eine reine J- oder A-Einspeisung kann bei nichtverschwindender Mischung beide Ausbreitungsmoden anregen. Die beobachtbaren Signale hängen deshalb von den Projektionen der tatsächlichen Sende- und Empfangsports ab.

Die Matrix ist eine analytische Kontrolle mit freien schweren Arten. Insbesondere ist sie keine numerische Behandlung eingeschlossener Quarks. Eine zu leichte oder masselose J-geladene Art lässt sich in der vorausgesetzten lokalen Schwellenentwicklung nicht so eliminieren. Auch die flache kinetische Mischung und mögliche unabhängige Krümmungsparameter müssen beim physischen Vergleich mitgeführt werden.

## Wolfram-Ausgabe

Das [Prüfskript](op5_j_dirac_schwellenabgleich.wl) kontrolliert die Ladungsalgebra, den kombinierten axialen Faktor und die transparente Richtung der Ein-Arten-Kontrolle. Es führt kein Schleifenintegral aus. Für diese algebraische Schwellenrechnung ist keine Quantenschaltung definiert.

~~~text
Axial spinor Wilson multiplier (in units alpha/pi): 11/180
One-generation charge matrix: {{gj^2*(3*wd + we + wn + 3*wu), -(ea*gj*(wd + we - 2*wu))}, {-(ea*gj*(wd + we - 2*wu)), (ea^2*(wd + 3*we + 4*wu))/3}}
Degenerate threshold matrix: {{8*gj^2, 0}, {0, (8*ea^2)/3}}
Single-electron determinant: 0
Single-electron transparent direction residual: {0, 0}
~~~

Der separate Rückgabewert des letzten `Print` war `Out[1]= Null`. Native Metrikkopplung des massiven Vermittlers, vollständige Schwellenrechnung, geladene Empfangsports und H96 bleiben offen.
