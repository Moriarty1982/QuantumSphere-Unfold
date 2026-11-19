# OP5: Neutron–Blei-Streuung bei aufgehobener Myonkopplung

19. November 2026. Nicht blinde analytische Erkundung in M. Die [Myonrechnung](OP5_J_Myonmoment.md) schloss das bisherige Referenzregime bei unveränderter Myonkopplung aus. Hier wird die niedrige Energiegrenze einer Mischung mit dem elektromagnetischen Strom geprüft. Wir behalten $A=g_J^2/(4\pi)=0{,}01$ und das nominelle Massenfenster $0{,}179<m_J<1{,}238$ MeV aus der [Stückelberg-Rechnung](OP5_Endliche_J_Reichweite.md) bei. Diese Erkundung prüft die sichtbare Kopplung dieses Fensterbeispiels und keinen Datenvergleich für H96.

## Sichtbare Ladungen beim Lepton-Nullpunkt

Schreibe die physikalischen Vektorkopplungen bei kleinen Impulsen als $g_J Q_J+\eta Q_{\rm em}$. Für die ursprüngliche Ladungszuordnung gilt
$$
g_\mu=g_e=g_J-\eta,\qquad
g_p=3g_J+\eta,\qquad
g_n=3g_J.
$$
Die Wahl $\eta=g_J$ löscht die Vektorkopplung von Elektron und Myon im betrachteten Niedrigenergievertex. Das Proton trägt dann $4g_J$, das Neutron weiterhin $3g_J$. Isotopenkerne mit $Z$ Protonen und $N$ Neutronen koppeln daher kohärent mit $(4Z+3N)g_J$, solange die räumliche Auflösung den Kern nicht auflöst. Für $^{208}\mathrm{Pb}$ sind $(Z,N)=(82,126)$ und die Kernkopplung ist $706g_J$. Die Elektronen tragen in dieser Näherung keine J-Quellladung. Diese Aussage behandelt den gewählten Nullpunkt und berücksichtigt keine impulsabhängigen Restkopplungen aus weiteren Mischungen.

Die [Schleifenuntergrenze](OP5_J_Myonmoment.md) liefert für $m_J<m_\mu$ und bei derselben großzügigen Toleranz $\delta a_\mu\le10^{-8}$ die notwendige Schranke $g_\mu^2/(4\pi)\le12\pi\,10^{-8}$. Damit gilt bei $A=0{,}01$ näherungsweise $|g_\mu/g_J|\le0{,}00615$. Ein Abweichen von der exakten Abstimmung innerhalb dieser Schranke verändert die kohärente Kernladung in Einheiten von $g_J$ höchstens um $82\cdot0{,}00615$. Im Folgenden wird die atomare Elektronenwolke nur am exakten Nullpunkt weggelassen.

## Nichtperturbativer Streuvergleich

Außerhalb des Kerns wird bei den MeV-Mediatormassen zunächst der Punktkernvergleich benutzt. Zwei positive Vektorladungen stoßen sich ab. Die Wechselwirkung eines Neutrons mit $^{208}\mathrm{Pb}$ ist
$$
V(r)=2118 A\,\frac{e^{-m_J r}}{r}.
$$
Die Reichweite liegt im Fenster bei mindestens $159$ fm. Die Born-Reihe am Modellpunkt ist keine kontrollierte Näherung: Der dimensionslose Parameter $2\mu_{nT}\,2118 A/m_J$ beträgt schon am oberen Ende mehrere Zehntausend. Zum Vergleich gibt es schwach gekoppelte Analysen von Neutron–Blei-Daten, die ein zusätzliches Yukawa-Potential an die Streuung anpassen. Ihre perturbativen Kopplungsgrenzen werden hier nicht auf den starken Punkt fortgeschrieben. [Knapen, Lin und Zurek, Abschnitt zu Neutron–Blei-Streuung](https://escholarship.org/content/qt9xn2n1hc/qt9xn2n1hc.pdf?t=p6b547)

Für das äußere, reelle $s$-Wellen-Problem bei Nullenergie verwende die reduzierte Radialfunktion $u$ und $y=u/u'$. In natürlichen Einheiten gilt
$$
u''=2\mu_{nT}V u,\qquad y'=1-2\mu_{nT}V y^2,\qquad
a_s=\lim_{r\to\infty}(r-y(r)).
$$
Eine analytische Untergrenze ist auch ohne Integration erhältlich. Setze den inneren Radius bei $r_0=20$ fm und zunächst eine Randbedingung $y(r_0)\ge0$ an, einschließlich der harten Wand und des Grenzfalls $u'=0$. Sie umfasst reguläre, gleichsinnig ansteigende Lösungen am Rand, jedoch keine beliebige nukleare Randbedingung. Auf $[r_0,R]$ mit $R=1000$ fm gilt über das ganze Fenster $V(r)\ge V_0=V(R;m_J=1{,}238\,{\rm MeV})\simeq7{,}88$ keV. Der Vergleich der Riccati-Gleichungen liefert
$$
y(R)\le\frac{\coth[\kappa(R-r_0)]}{\kappa},
\qquad \kappa=\sqrt{2\mu_{nT}V_0}.
$$
Die rechte Seite ist die Lösung für konstantes $V_0$ und $y(r_0)\to+\infty$. Jenseits von $R$ gilt $(r-y)'=2\mu_{nT} V y^2\ge0$. Damit folgt $a_s\ge R-\kappa^{-1}\coth[\kappa(R-r_0)]\simeq948{,}6$ fm. Verwendet ist $\mu_{nT}\simeq0{,}935$ GeV und $\hbar c\simeq0{,}197327$ GeV fm für die Umrechnung. Die Schranke ist nichtperturbativ innerhalb des äußeren Modells und verwendet nur den repulsiven Fernanteil und die angegebene Randklasse.

Als numerische Kontrolle wurde $y'=1-[2\mu_{nT}V/(\hbar c)^2]y^2$ ab $r_0=20$ fm mit $y(r_0)=0$ bis $45\hbar c/m_J$ integriert. Runge–Kutta vierter Ordnung mit Schritten von $0{,}05$ und $0{,}025$ fm ergab stabil:

| $m_J$ in MeV | $a_s$ in fm |
| ---: | ---: |
| 0,179 | 12036,75 |
| 1,000 | 1841,83 |
| 1,238 | 1456,60 |

## Einordnung der Daten

NIST tabelliert die gebundene kohärente Neutronenstreulänge von $^{208}\mathrm{Pb}$ mit $9{,}50$ fm und den kohärenten Streuquerschnitt mit $11{,}34$ barn. Der kinematische Faktor zwischen gebundener und freier Streulänge beträgt für Blei nur etwa $1{,}005$. Gegenüber dem reinen repulsiven Vergleich unterscheiden sich die Streulängen also um mindestens zwei Größenordnungen. Die Differenz kann in der geprüften Randklasse nicht durch Wahl eines anderen inneren nichtnegativen Randparameters absorbiert werden. [NIST, Neutronenstreulängen und Wirkungsquerschnitte](https://www.ncnr.nist.gov/resources/n-lengths/list.html)

Für eine umfassende Aussage ist die wirkliche nukleare Streuamplitude einzusetzen. Negative oder komplexe logarithmische Randdaten und resonante Abhängigkeit von der Neutronenenergie werden durch den analytischen Vergleich nicht behandelt. Auch eine unabhängige zusätzliche Kraft mit kompensierendem längerem Verlauf wäre ein anderes Modell. Das Ergebnis zeigt die Größenordnung und das Vorzeichenproblem der elektromagnetischen Abstimmung im bisherigen Parameterfenster. Es ist keine neue experimentelle Ausschlusskurve, und es setzt H96 nicht auf geschlossen.
