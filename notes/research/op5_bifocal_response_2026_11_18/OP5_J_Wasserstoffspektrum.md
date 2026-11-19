# OP5: Wasserstoff-Spektralkombination für die endliche J-Reichweite

19. November 2026. Nicht blinde analytische Erkundung in M. Die [Stückelberg-Erkundung](OP5_Endliche_J_Reichweite.md) fand für $A=0{,}01$ und $M=50$ GeV je Konstituent ein nominelles Fenster $0{,}179<m_J<1{,}238$ MeV mit Fernkraftunterdrückung und energetisch möglicher kalter J-Abstrahlung im Singulettmodell. Hier wird derselbe vorgegebene J-Vertex an bekannten Übergängen des gewöhnlichen elektronischen Wasserstoffs geprüft. Das ist ein Vergleich für die zusätzliche Wechselwirkung und kein Datenvergleich nach dem vorregistrierten Kriterium von [H96](../predictions/Vorab_Notiz_H96_Omega_M_beta2.md).

## Drei gemessene Frequenzen

Bezeichne mit $\nu_{12}=(E_{2S}-E_{1S})/h$ den $1S_{1/2}\to2S_{1/2}$-Übergang, mit $\nu_{28}=(E_{8D}-E_{2S})/h$ den $2S_{1/2}\to8D_{5/2}$-Übergang und mit $\nu_L=(E_{2S}-E_{2P})/h$ die positive $2S_{1/2}-2P_{1/2}$-Lamb-Aufspaltung. Für die Kombination
$$
\mathcal C=-\nu_{12}+\frac{16}{5}\nu_{28}-\frac{19}{5}\nu_L
=\frac{E_{1S}-8 E_{2S}+\frac{16}{5}E_{8D}+\frac{19}{5}E_{2P}}h
$$
verschwinden die nichtrelativistischen Rydberg-Energien proportional zu $1/n^2$ und die führende gewöhnliche Protonradius-Kontaktenergie proportional zu $\delta_{\ell0}/n^3$. Die beiden Nullen folgen aus $1-8/4+(16/5)/64+(19/5)/4=0$ und $1-8/8=0$. Die vollständige Standardrechnung enthält weiterhin relativistische, QED-, Rückstoß- und höhere Protonstrukturbeiträge. Die Kombination selbst hat daher eine große Standardvorhersage und muss mit dieser verglichen werden.

Verwendet sind die CODATA-2022-Einträge A7, A23 und A29 aus Tabelle XI. In der hier definierten positiven Frequenzkonvention lauten die Werte:

| Eingang | Frequenz in kHz | Berichtete Standardunsicherheit in kHz |
| --- | ---: | ---: |
| $\nu_{12}$ | 2 466 061 413 187,018 | 0,011 |
| $\nu_{28}$ | 770 649 561 570,9 | 2,0 |
| $\nu_L$ | 1 057 829,8 | 3,2 |

Sie ergeben $\mathcal C_{\rm obs}\simeq13\,164{,}087$ MHz. Für eine konservative Vergleichsskala kann man die gesamte finale CODATA-Anpassung mit $\chi^2=44{,}2$ benutzen. Mit der vollständigen Eingangskovarianz $\Sigma$ gilt für jedes Eingangsresiduum $|r_i|\le\sqrt{\chi^2}\sqrt{\Sigma_{ii}}$ durch Cauchy–Schwarz. Die Diagonalunsicherheiten der drei Frequenzen sind im finalen Fit um Faktor $1{,}7$ vergrößert. Die Dreiecksungleichung liefert
$$
|\mathcal C_{\rm obs}-\mathcal C_{\rm CODATA}|
\le1{,}7\sqrt{44{,}2}
\left(0{,}011+\tfrac{16}{5}\,2{,}0+\tfrac{19}{5}\,3{,}2\right){\rm kHz}
\simeq0{,}210\,{\rm MHz}.
$$
Die Schranke folgt aus dem bereits veröffentlichten Fit. Sie ist kein neues Konfidenzintervall und benötigt keine Unabhängigkeit der Frequenzdaten. [CODATA 2022, Tabelle XI und Abschnitt XV](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958143)

## J-Korrektur erster Ordnung

Proton und Elektron tragen J-Ladungen $+3$ und $+1$. Im statischen Punktproton-Vergleich ist die Zusatzenergie positiv und proportional zu $3A e^{-m_Jr}/r$. Wir benutzen nichtrelativistische Coulomb-Wellenfunktionen mit elektronischem Bohr-Radius $a=(\mu_{pe}\alpha)^{-1}$. Sei $x=m_Ja$ und $I_{n\ell}=\langle e^{-m_Jr}/r\rangle_{n\ell}$. Integration der normierten Coulomb-Radialfunktionen ergibt
$$
I_{1S}=\frac{4}{a(x+2)^2},\qquad
I_{2S}=\frac{4x^2+2}{8a(x+1)^4},\qquad
I_{2P}=\frac{1}{4a(x+1)^4}.
$$
Daher ist
$$
I_{1S}-8 I_{2S}=\frac{6x^2+8x-4}{a(x+1)^4(x+2)^2}.
$$
Der führende Kontaktterm fällt heraus, und der erste verbleibende Beitrag geht für große $x$ wie $x^{-4}$. Die vollständige lineare Verschiebung ist
$$
h\,\delta\mathcal C^{(1)}=3A\left(I_{1S}-8 I_{2S}+\tfrac{16}{5}I_{8D}+\tfrac{19}{5}I_{2P}\right).
$$
Da beide letzten Integrale positiv sind, genügt für eine einseitige Schranke schon der erste Unterschied. Im Fenster gilt näherungsweise $x_{\min}=48{,}0$ und $x_{\max}=332{,}2$. Aus
$$
I_{1S}-8 I_{2S}\ \ge\ \frac{6}{a x_{\max}^4(1+1/x_{\min})^4(1+2/x_{\min})^2}
$$
folgt für das gesamte Fenster $\delta\mathcal C^{(1)}>11$ MHz. Bei $m_J=1$ MeV ergeben allein $1S$, $2S$ und $2P$ zusammen $35{,}4$ MHz in dieser Kombination. Der $8D$-Beitrag erhöht den Wert. Die Rechnung benutzt $a^{-1}\simeq3727$ eV und $h\simeq4{,}13567\times10^{-15}$ eV s. Der Radialausdruck ergibt sich aus Integralen der Form $\int_0^\infty y^n e^{-b y}\,dy=n!/b^{n+1}$; die rationale Differenz vermeidet numerische Subtraktion zweier großer Kontaktterme.

## Geltungsbereich der Spannung

Die vorzeichenfeste lineare Zusatzverschiebung im gesamten nominellen Fenster ist mehr als fünfzigmal größer als die konservative Residualskala des veröffentlichten Standardfits. Führende Verschiebungen von Rydberg-Konstante und Protonradius können sie in dieser Kombination nicht absorbieren. Diese Aussage gilt für die gewählten Punktladungen und den linearen nichtrelativistischen Zusatzterm. Ein vollständiger Ausschlussfit für die Eichwirkung müsste relativistische und radiative J-Beiträge, höhere Ordnungen, Protonstruktur, weitere gleichzeitig veränderte Eingaben und die Kovarianzen neu mitführen. Das ist besonders relevant für eine Kombination, in der der größte kurzreichweitige Beitrag bereits fortfällt. Die Berechnung liefert eine quantitative Spannung für das bisherige Parameterbeispiel. Sie schließt weder jede andere Wahl von $A,M,m_J$ noch H96 ab.
