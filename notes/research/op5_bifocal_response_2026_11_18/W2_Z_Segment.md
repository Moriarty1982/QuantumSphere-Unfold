# OP5: Kann ein kurzes Segment die Z-String-Instabilität unterdrücken?

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im statischen Materie-Ruhesystem. Die [Z-String-Prüfung](W2_Z_Strang.md) dokumentiert eine negative transversale Mode des unendlichen bosonischen Standardmodell-Wirbels und die magnetische Endpunktanziehung. Die [Kräftebilanz](W2_Gleichnamige_Foki.md) beschreibt ein mögliches Minimum des Fokusabstands. Hier wird die negative Mode auf ein endliches Segment projiziert. Das ist ein Kontrollmodell, keine Lösung für die Nambu-Endzonen.

## Projektion auf die negative Mode

Im idealisierten translationsinvarianten Inneren habe eine normierte physische Transversalmode den Eigenwert $-\mu^2$ mit $\mu>0$. Ihre Amplitude entlang der Achse sei $f(x)$ auf $0\le x\le R$. Die eindimensionale quadratische Energie nach kanonischer Normierung ist

$$
\mathcal Q[f]=\int_0^R \big(|f'|^2-\mu^2|f|^2\big)\,dx
+h\left(|f(0)|^2+|f(R)|^2\right),\qquad h\ge0.
$$

Der Endterm setzt eine symmetrische lokale Steifigkeit $h$ an. $h=0$ bedeutet freie Enden für die projizierte Mode; festgeklemmte Enden sind der Dirichlet-Grenzfall $h\to\infty$. Ein solcher Wert folgt bisher weder aus den Nambu-Endpunkten noch aus W2.

Variation ergibt $f'(0)=h f(0)$ und $f'(R)=-h f(R)$. Für $h>0$ ist die niedrigste Eigenfunktion positiv und aufgrund der Spiegelung symmetrisch. Daher ist sie proportional zu $\cos[k_0(x-R/2)]$ mit

$$
k_0\tan(k_0R/2)=h,\qquad 0<k_0R<\pi,\qquad
\lambda_0=k_0^2-\mu^2.
$$

Das linke Glied ist auf diesem Ast streng steigend. Strikte Positivität der betrachteten Mode verlangt für endliches $h$

$$
R<R_{\rm crit}(h)=\frac{2}{\mu}\arctan\!\left(\frac{h}{\mu}\right).
$$

Bei Gleichheit bleibt eine Nullmode und die quadratische Prüfung entscheidet ihre nichtlineare Stabilität nicht. Für freie Enden gilt $k_0=0$, also $\lambda_0=-\mu^2$ bei jeder Länge. Selbst starre Enden erlauben strikte Positivität nur für $R<\pi/\mu$.

## Ein langer instabiler Innenabschnitt genügt

Innerhalb des effektiven eindimensionalen Modells ist die Dirichlet-Grenze zugleich eine notwendige Grenze für jeden Endterm, der nur von den Amplituden an den Enden abhängt und bei verschwindender Endamplitude null ist. Die Testfunktion $\sin(\pi x/R)$ hat dort keine Randenergie und gibt den Rayleigh-Quotienten $(\pi/R)^2-\mu^2$. Für $R>\pi/\mu$ ist er negativ.

Eine lokale Variante braucht kein separates Endmodell. Gibt es im Inneren ein Teilintervall der Länge $L$, auf dem für dieselbe Transversalmode das quadratische Funktional von oben durch $\int (c^2|f'|^2-\mu_{\rm in}^2|f|^2)\,dx$ beschränkt ist, dann genügt $L>\pi c/\mu_{\rm in}$ für einen negativen Testwert. Hier sind $c>0$ eine obere Schranke der longitudinalen Gradientensteifigkeit in der gewählten Normierung und $\mu_{\rm in}>0$ eine untere Schranke des Instabilitätsmaßes. Die Sinusfunktion auf dem Teilintervall wird außerhalb null fortgesetzt. Im $H^1$-Formraum ist dies zulässig; bei Bedarf kann sie glatt approximiert werden. Die Behauptung setzt voraus, dass das projizierte Testprofil die physischen Nebenbedingungen erfüllt und die angegebene Formschranke wirklich gilt. Die vorige Z-String-Notiz liefert noch keine solche Schranke für einen endlichen Nambu-Strang.

## Vergleich mit dem mechanischen Abstand

Für die führende Abstandsdynamik $TR+A_{\rm eff}/R$ mit $T>0$ und $A_{\rm eff}>0$ ist $R_*=\sqrt{A_{\rm eff}/T}$. Wenn im idealisierten Modell die Länge des homogenen Segments gleich dem Fokusabstand ist, müssen zusätzlich zu seinem Abstandsminimum

$$
R_*<R_{\rm crit}(h),\qquad
0<\frac{A_{\rm eff}\mu^2}{T}<4\arctan^2(h/\mu)\le\pi^2
$$

gelten, damit diese eine Mode strikt positiv wird. Das Langstreckenpotential setzt zugleich voraus, dass $R_*$ gegenüber der Endzonen- und Kerngröße hinreichend groß ist. Liegt die für diese Näherung benötigte Mindestlänge schon bei $\pi/\mu$ oder darüber, gibt es in diesem Modell keinen gemeinsamen Geltungsbereich. Eine numerische Entscheidung für W2 bräuchte den aus der Instabilität bestimmten Wert $\mu$, die Endantwort und die Gültigkeitslänge, alle aus demselben Hintergrund. Die Positivität dieser einen Mode würde für sich die übrigen Moden und die gekoppelte Endpunktdynamik offenlassen.

I1 müsste daher neben Spannung und Randbindung auch eine nachweislich ausreichende Endantwort oder eine Änderung der negativen Innenmode liefern. I3 bleibt an eigenständige Überschussdynamik gebunden. Native Randwirkung und H96 bleiben offen.
