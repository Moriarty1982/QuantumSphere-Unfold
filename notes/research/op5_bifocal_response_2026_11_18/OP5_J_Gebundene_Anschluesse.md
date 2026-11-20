# OP5 — Anschlussrichtungen eines elektrisch neutralen gebundenen Paars

20. November 2026. Analytische Erkundung im Materieframe M. Rückwärts gesucht sind getrennt ansteuerbare und auslesbare Stromrichtungen für den [kohärenten A/B-Vergleich](OP5_J_Sende_Empfangsports.md).

## Vorwissen geprüft

Der [J-Eichkanal](W2_J_Eichkanal.md) gibt im Dirac-Modell jedem Quark und dem Elektron dieselbe J-Teilchenladung. Das [Wasserstoffspektrum](OP5_J_Wasserstoffspektrum.md) verwendet daraus bereits die effektiven Punktladungen $+3$ und $+1$ für Proton und Elektron. [Gebundener Tensor](OP5_Gebundener_Tensor.md) unterscheidet die Schwerpunktbewegung von der inneren Dynamik. Die [neutralen Ströme](W2_Neutralstroeme.md) behandeln eine separate elektroschwache Referenz und begründen keine Photon-Portgleichung aus W1/W2. [Endpunktdrift](OP5_J_Endpunktdrift.md) und [doppelte Laufzeitdifferenz](OP5_J_Doppelte_Laufzeitdifferenz.md) geben die Bedingungen zur Trennung von Endpunkt und Strecke. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört die Rechnung zur lokalen OP5-Auslese. Die bei I3 benötigte Entwicklung einer gravitativen Population wird durch sie nicht geliefert.

## Ladung und Dipolstrom

Betrachte einen gebundenen Proton-Elektron-Vergleich in der nichtrelativistischen elektrischen Dipolnäherung. Das Proton ist eine effektive Punktquelle. Die Kopplungen in den beiden Feldrichtungen sind
$$
q_p=(3g_J,e)^{\mathsf T},\qquad q_e=(g_J,-e)^{\mathsf T},\qquad e g_J\ne0.
$$
Bis auf äußere lineare Kräfte sei die innere Bindung translationsinvariant. Eine Schwerpunkt-Halterung wird separat modelliert. Für eine Raumrichtung seien $M=m_p+m_e$, $R=(m_p x_p+m_e x_e)/M$ und $r=x_p-x_e$. Bei festen Ladungen ist der zeitabhängige Dipolstrom das räumliche Integral des Stroms in dieser Richtung:
$$
\binom{D_J}{D_A}=C\binom Rr,\qquad
C=\begin{pmatrix}4g_J & a\\0&e\end{pmatrix},
\qquad a=g_J\,\frac{m_e-3m_p}{M},
\qquad
\binom{\int j_J^x\,d^3x}{\int j_A^x\,d^3x}=C\binom{\dot R}{\dot r}.
$$
Die Stromgleichung folgt aus der Kontinuitätsgleichung bei lokalisierten Quellen. Beim Netto-J-Dipol ist der Ursprung festzuhalten. Eine feste Verschiebung dieses Ursprungs lässt die zeitabhängige Antwort und den Strom unverändert. Schwerpunkttranslation liefert einen reinen J-Dipolstrom. Die innere Polarisation liefert eine Richtung mit elektromagnetischer Komponente. Konstante positiv definite kinetische Mischung multipliziert $C$ von links mit $K^{-1/2}$ und erhält den Rang. Aussagen über den reinen J-Strom beziehen sich auf die ursprünglichen Kopplungskoordinaten.

## Zwei Materiekoordinaten und zwei tatsächliche Zugriffsmöglichkeiten

Setze in linearer Antwort eine trennbare Schwerpunkt- und interne Suszeptibilität $\chi_R(\omega)$ beziehungsweise $\chi_r(\omega)$ voraus. Uniforme Felder in der betrachteten Raumrichtung liefern den Wechselwirkungsterm $-E^{\mathsf T}C(R,r)^{\mathsf T}$ mit $E=(E_J,E_A)^{\mathsf T}$. Für Fourier-Zeitfaktor $e^{-i\omega t}$ gilt
$$
D=C\begin{pmatrix}\chi_R&0\\0&\chi_r\end{pmatrix}C^{\mathsf T}E,\qquad
j_{\rm int}=-i\omega D,\qquad
\det\!\left(\frac{\partial D}{\partial E}\right)
=16g_J^2e^2\chi_R\chi_r.
$$
Diese Aussage gilt bei endlichen Suszeptibilitäten. Außerhalb von Nullstellen kann im Modell bei $\omega\ne0$ ein unabhängiger mechanischer Schwerpunktantrieb zusammen mit einem elektrischen Polarisationsantrieb zwei Stromrichtungen erzeugen. Die generalisierten Kräfte stehen dann in den beiden Koordinaten getrennt zur Verfügung. Ein rein uniformer elektromagnetischer Antrieb derselben neutralen Einheit hat nur eine Stellgröße und liefert keine Schwerpunktkraft in dieser Näherung. Eine mechanische Halterung und ihre Rückleitung gehören bei einer realen Ausführung zur vollständigen Quell- und Feldbilanz.

Am Empfangsende erzeugt ein einfallendes $E$ die Kräfte $C^{\mathsf T}E$. Sind $R$ und $r$ unabhängig und kohärent messbar, erhält man nach Kalibrierung
$$
E_J=\frac{R}{4g_J\chi_R},\qquad
E_A=\frac{r/\chi_r-a R/(4g_J\chi_R)}{e}.
$$
Reine elektrische Dipolauslese misst nur $D_A=e r$. Ein ideal starr gehaltener Schwerpunkt entspricht $\chi_R=0$. Die verbleibende Antwort ist dann $\chi_r(a,e)^{\mathsf T}(a,e)$ und hat bei nichtverschwindender innerer Suszeptibilität Rang eins. Kleine $\chi_R$ kann die Rückrechnung stark verschlechtern, weil der J-Anteil aus einer kleinen mechanischen Antwort rekonstruiert wird. Die Rechnungen betreffen den elektrischen Dipolterm bei kleinem Verhältnis von Ausdehnung zu Wellenlänge. Finite Feldgradienten, höhere Multipole, Tragstruktur, Hintergrundladung, Reichweite und Kopplung an die am Ende tatsächlich propagierenden Moden sind hier ausgeklammert.

## Ein konkreter Endpunktbeitrag

Für eine bedämpfte Halterung mit $\chi_R(\omega)=1/(\kappa-M_R\omega^2-i\eta\omega)$ seien $\kappa>0$, $M_R>0$ und $\eta\ge0$. $M_R$ ist die effektive bewegte Masse der Halterung mit Last. Ändert der Profilwechsel allein ihre effektive Steifigkeit um $\delta\kappa$ bei unveränderter Strecke und $\kappa+\delta\kappa>0$, dann trägt schon der isolierte Schwerpunkt-Endpunkt bei
$$
\left.\partial_\omega\arg\frac{\chi_{R,B}}{\chi_{R,A}}\right|_{\omega=0}
=\eta\!\left(\frac{1}{\kappa+\delta\kappa}-\frac{1}{\kappa}\right)
=-\frac{\eta\,\delta\kappa}{\kappa(\kappa+\delta\kappa)}.
$$
Dies ist der Grenzwert der Phasensteigung nahe null, während der abgestrahlte Dipolstrom bei null Frequenz verschwindet. Bei nichtverschwindender Frequenz kürzt sich der in beiden Zuständen gleiche Stromfaktor $-i\omega$ im Endpunktquotienten. Das Beispiel liefert eine mögliche profilgebundene Phase. Eine lokale Messung von $\chi_R$ in beiden Profilen könnte genau diesen Beitrag kalibrieren. Die Höhe von $\delta\kappa$ und weitere Endpunktterme müssten separat bestimmt werden.

## Rechenkontrolle

[Wolfram Language](op5_j_gebundene_anschluesse.wl) bestimmt die Strommatrix, ihren Rang und die modellierte Endpunktverschiebung symbolisch. Die tatsächliche Print-Ausgabe lautet

```text
atomic charge = {4 g, 0}
determinant of dipole map = 4*e*g
internal dipole coefficient, simplified = g*(-1 + (4*me)/(me + mp))
determinant of driven response = 16*chiR*chiRrel*e^2*g^2
clamped-center dark residual = {0, 0}
electric drive center force = 0
electric drive relative force per field = e
center loading time shift at zero frequency = -((delta*eta)/(kappa*(delta + kappa)))
```

Der separate Rückgabewert war `Null`. Die Rechnung ist eine symbolische Dipol- und lineare Antwortrechnung. Eine Quantenschaltung oder Zustands- und Messsimulation würde die fehlende mechanische Ansteuerung und Auslese nicht festlegen. Das Modell liefert einen bedingten Kandidaten für beide Enden. Eine kalibrierte gekoppelte Apparatur, ihre Rückwirkung beim Profilwechsel und H96 bleiben offen.
