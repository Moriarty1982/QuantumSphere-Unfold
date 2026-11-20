# OP5 — Kompensation des massiven und masselosen Außenfelds

20. November 2026. Analytische Erkundung im Materieframe M. Vorausgesetzt sind die lineare retardierte Gravitation und der separate lineare massive Vermittler bei vorgegebener Masse $m>0$. Die symmetrische erhaltene Quelle wird als vollständige Änderung beider Kanäle vorgeschrieben. Vor der Schaltung ist die Störung null.

## Vorwissen geprüft

Die [dynamische Kompensation](OP5_J_Dynamische_Kompensation.md) benutzt den kompakten erhaltenen Hilfstensor $S$. Die [masselose Antwort](OP5_J_Antriebsenergie_und_Gravitation.md) zeigt, warum beim bisherigen nichtverschwindenden Quadrupol der ruhenden Profile ein gewöhnliches Außenfeld übrig bleibt. Der [Kontrollkontrast](OP5_J_Kontrollkontrast.md) bestimmt die Achsenauslese. Die [Spannungsbilanz](OP5_J_Spannungsbilanz.md) gibt den Zusammenhang mit dem Moment der vollständigen Energiedichte. Rückwärts wird jetzt eine Quelle verlangt, die beide linearen Außenfelder unverändert lässt und in der Strahlgeometrie einen nichtverschwindenden OP5-Kontrast trägt. Der Zusammenhang im [Gesamtbild](../../../wiki/Gesamtbild.md) liegt vor der realen Mess- und Dichteabbildung für H96. Ein Antrieb für I3 wird hier nicht hergeleitet.

## Eine gemeinsame Quelle für beide Pole

Sei $D=\partial_t^2-\Delta$ und $\mathcal L_{\rm dyn}=1+D/m^2$. Wähle den kompakten erhaltenen Hilfstensor $S$ aus der transversalen Konstruktion mit $S^{00}=\psi$, $S^{z\mu}=S^{\mu z}=0$ und $\int\psi(t,\mathbf b,z)d^2b=0$ für jede Querebene. Wähle jetzt
$$
\delta T=\frac{D}{m^2}\mathcal L_{\rm dyn}S.
$$
Beide Operatoren kommutieren mit der Divergenz. Bei verschwindenden früheren Daten gilt durch Anwendung der jeweiligen retardierten Inversen
$$
D_{\rm ret}^{-1}\delta T=\frac{\mathcal L_{\rm dyn}S}{m^2},
\qquad
\mathcal L_{\rm dyn,ret}^{-1}\delta T=\frac{D S}{m^2}.
$$
Beide Antworten sind kompakt. Spurspiegelung im masselosen Kanal und die lokalen Spur- und Ableitungsterme des massiven Zählers erhalten diese Eigenschaft. Deshalb verschwinden in beiden Modellen die Feldstörungen in den unveränderten äußeren Apparaturregionen auch während der Schaltung. Diese Folgerung gilt für die präparierte vollständige Quelle bei der eingesetzten Masse.

## Der Achsenkontrast bleibt möglich

Für einen ungestörten axialen Nullstrahl mit $t=t_0+z$ ist die direkte Nullkontraktion der massiven gefilterten Quelle $D\psi/m^2$. Die Spurprojektion liefert bei der Integration wieder nur den verschwindenden Randterm, da ihre zusätzliche Nullkontraktion eine zweite Ableitung entlang der Strecke ist. Auch der Unterschied $\partial_t^2-\partial_z^2$ in $D\psi$ hat hier eine reine Randwirkung
$$
(\partial_t^2-\partial_z^2)\psi(t_0+z,0,z)
=\frac{d}{dz}\left[(\partial_t-\partial_z)\psi\right](t_0+z,0,z).
$$
Damit bleibt der geometrische Ausbreitungskontrast
$$
-\frac{1}{m^2}\int_0^L(\Delta_\perp\psi)(t_0+z,0,z)\,dz .
$$
Der Kontrast erfordert eine transversale Krümmung der kompakten Antwort. Unter gleicher minimaler Metrikkopplung und identischer Strahlgeometrie ist der lineare masselose Ausbreitungsbeitrag beiden Signalen gemeinsam. Ein tatsächlich messbarer differentieller massiver Beitrag erfordert weiterhin einen von null verschiedenen Kopplungsunterschied.

Ein explizites Profil mit genügend stetigen Ableitungen ist
$$
\psi=A s(t)\left[1-\frac{(z-z_0)^2}{\ell^2}\right]_+^6
\left(g_a(\mathbf b)-\tfrac14g_{2a}(\mathbf b)\right),\qquad
g_a(\mathbf b)=\left[1-\frac{|\mathbf b|^2}{a^2}\right]_+^6 .
$$
Hier ist $[x]_+=\max(x,0)$, der Längsträger liegt zwischen den Endpunkten, und $A,\ell,a>0$. Wegen der Flächenskalierung ist das Querintegral null. Auf einem Plateau mit $s=1$ beträgt die transversale Laplace-Wirkung auf den reinen Querfaktor $-45/(2a^2)$. Die Längsnorm ist $2048\ell/3003$. Der Achsenkontrast beträgt daher $15360 A\ell/(1001a^2m^2)>0$, bis auf den Kopplungsfaktor. Eine quer verschobene kompakte Quelle, deren Antwortträger den Strahl verfehlt, liefert im Modell eine äußere und axiale Nullkontrolle.

## Welche Forderung aufgegeben wird

Für das gewählte Profil sei $\int x^2\psi\,d^3x=\int y^2\psi\,d^3x=-Qs(t)$ mit $Q>0$, während das Längsmoment null ist. Weil $\int\psi=0$, trägt der räumliche Laplace-Term bei diesen zweiten Momenten nichts bei. Dasselbe gilt bei wiederholter Anwendung. Für die physische Zielquelle folgt
$$
\int x^2\delta T^{00}\,d^3x=-Q\left(\frac{\ddot s}{m^2}+\frac{s^{(4)}}{m^4}\right),
\qquad
\int\delta T^{xx}\,d^3x=-\frac{Q}{2}\left(\frac{s^{(4)}}{m^2}+\frac{s^{(6)}}{m^4}\right).
$$
Analog gilt dies in $y$, während der Längsbeitrag verschwindet. Auf den Plateaus verschwindet das zweite räumliche Moment der Quelle in allen Richtungen. Allgemeiner ist die statische $\delta T^{00}$ ein Laplace-Bild einer kompakten Funktion. Ihre Integrale gegen harmonische Polynome sind deshalb null. Die vorige Bedingung eines fest vorgeschriebenen von null verschiedenen Plateauquadrupols ist mit dieser doppelten Kompensation unvereinbar. Das frühere Paar- und Ringmodell kann daher nicht direkt als Ansteuerung übernommen werden. Für eine glatte Schaltung bleiben höhere Zeitableitungen im integrierten Stress zu erfüllen.

## Wolfram-Ausgabe

Das [Prüfskript](op5_j_zweifache_aussenfeldkompensation.wl) kontrolliert beide Operatoridentitäten, Profilintegrale, Achsenkrümmung und das resultierende Dichtemoment. Es ist eine klassische Feldrechnung.

~~~text
Massless inverse residual: 0
Massive inverse residual: 0
Transverse integral: 0
Axial integral on unit half-length: 2048/3003
Transverse Laplacian on axis: -45/(2*a^2)
Static axial contrast factor (times A ell / (a^2 m^2)): 15360/1001
Boundary derivatives (orders 0 to 5): {0, 0, 0, 0, 0, 0}
Transverse density moment: -((mom*Derivative[2][s][t])/m^2) - (mom*Derivative[4][s][t])/m^4
~~~

Der separate Rückgabewert des letzten `Print` war `Out[1]= Null`. Die physische Erzeugung dieser Gesamtquelle, ihre Kopplung an eine reale Apparatur und H96 bleiben offen.
