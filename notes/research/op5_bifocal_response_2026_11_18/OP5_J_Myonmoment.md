# OP5: Myon-Magnetmoment und kalter Einfang mit endlicher J-Reichweite

19. November 2026. Nicht blinde analytische Erkundung in M. Die [Stückelberg-Erweiterung](OP5_Endliche_J_Reichweite.md) erhält die J-Kopplung gewöhnlicher geladener Dirac-Leptonen. Die [Wasserstoffrechnung](OP5_J_Wasserstoffspektrum.md) fand eine Spannung für das nominelle Singulett-Bindungsfenster. Hier prüfen wir dieselbe Kraft unabhängig von der Protonstruktur mit der magnetischen Anomalie des Myons. Wir nehmen am Myon die physikalische Vektorkopplung $g_\mu=g_J$ an. Weitere neue Beiträge, die diese Korrektur kompensieren könnten, werden in diesem Vergleich nicht angesetzt.

## Positiver Beitrag der massiven Vektorkraft

Sei $a_\mu=(g_\mu^{\rm mag}-2)/2$ das dimensionslose anomale magnetische Moment, wobei $g_\mu^{\rm mag}$ den magnetischen Faktor und $g_J$ ausschließlich die Eichkopplung bezeichnet. Der zusätzliche Ein-Schleifen-Beitrag eines massiven Vektorbosons an einem Dirac-Strom ist
$$
\delta a_\mu=\frac{A}{2\pi}F(r),\qquad
r=\frac{m_J}{m_\mu},\qquad A=\frac{g_J^2}{4\pi},
\qquad F(r)=\int_0^1\frac{2z(1-z)^2}{(1-z)^2+r^2 z}\,dz .
$$
Das ist der übliche abelsche Vektorvertex mit seiner physikalischen Kopplung. Für $r=0$ ist $F=1$. [Pospelov, Neutralvektor und anomales magnetisches Moment](https://arxiv.org/abs/0811.1030)

Für $0\le z\le1$ gilt $(1-z)^2+z\le1$. Der Nenner ist daher höchstens $\max(1,r^2)$. Der Zähler integriert sich zu $1/6$. Somit folgt für jede positive Vektormasse die strikte positive Untergrenze
$$
\delta a_\mu\ge\frac{A}{12\pi\,\max(1,r^2)}.
$$
Sie genügt zum Ausschluss einer Untermenge des Vergleichs ohne numerische Schleifenintegration.

Als Referenz gibt die PDG-Übersicht für 2025 $a_\mu^{\rm exp}=(116592071{,}5\pm14{,}5)\times10^{-11}$ und $a_\mu^{\rm SM}=(116592033\pm62)\times10^{-11}$ an. Ihre Differenz ist etwa $3{,}85\times10^{-10}$. Die kombinierte nominelle Unsicherheit ist rund $6{,}4\times10^{-10}$. Für eine grobe Modellbedingung erlauben wir einen deutlich größeren positiven Zusatz von bis zu $10^{-8}$. Diese Toleranz wird hier als Rechenannahme benutzt und ist kein publiziertes Konfidenzintervall. [PDG 2025, Abschnitt 10.3.3 zum Myonmoment](https://ccwww.kek.jp/pdg/2025/reviews/rpp2025-rev-standard-model.pdf)

Bei $A=0{,}01$ und $m_J=1$ MeV ergibt direkte Simpson-Integration mit $m_\mu\simeq105{,}658$ MeV den Beitrag $\delta a_\mu\simeq1{,}547\times10^{-3}$. Er übersteigt sogar das gesamte gemessene Moment $a_\mu^{\rm exp}\simeq1{,}166\times10^{-3}$. Dies ist derselbe Punkt, an dem die nominelle Einfangschwelle und die Bindung zuvor zusammenpassten.

## Zwei notwendige Bedingungen aus dem gebundenen Sektor

Sei $M$ die Masse je eines der beiden gleich schweren Singuletts. In der statischen Yukawa-Näherung ist die Bindung $B_Y$ durch ihren Coulomb-Wert nach oben beschränkt:
$$
B_Y\le MA^2/4 .
$$
Damit bei verschwindender Einlaufenergie ein reelles J-Quant abgegeben werden kann, ist $m_J\le MA^2/4$ notwendig. Das ist eine Bedingung für kalten Einfang über diesen Kanal. Sie erfasst keine heiße Produktion, Dreikörperreaktion oder Abstrahlung eines anderen Teilchens.

Die niedrigste erreichbare ungerade Anregungsschwelle liegt höchstens bei der Ionisationsenergie $B_Y$, da der ungerade Kontinuumssektor bei der freien Schwelle beginnt. Will man den gesamten inelastischen J-Ladungskanal bis zu einer Referenzenergie $K_{\max}$ kinematisch schließen, ist daher ebenfalls $MA^2/4\ge K_{\max}$ notwendig. Das ist eine konservative Bedingung und keine hinreichende Garantie für die tatsächliche Lücke.

Für das vorige Beispiel $M=50$ GeV und $K_{\max}\simeq196$ keV folgt $A\gtrsim3{,}96\times10^{-3}$. Betrachte den ausdrücklich gewählten schwach gekoppelten Bereich $A\le0{,}1$. Dann begrenzt der kalte Einfang die J-Masse auf $m_J\le125$ MeV, also $r\le1{,}184$. Die analytische Schleifenuntergrenze liefert im ganzen so eingegrenzten Bereich
$$
\delta a_\mu\gtrsim7{,}5\times10^{-5}.
$$
Dies übersteigt die großzügige Toleranz um mehr als drei Größenordnungen. Hier werden im nichtrelativistischen Singulettmodell nur notwendige Schwellenbedingungen benutzt. Eine genauere Einfangrate oder ein genauerer Yukawa-Eigenwert kann diese drei Anforderungen für denselben Massenbereich und unveränderte Myonkopplung nicht in Einklang bringen.

## Welche Modelländerung die Schranke berührt

Für $A>12\pi\times10^{-8}$ erzwingt die Toleranz in diesem Vergleich schon $m_J\ge m_\mu\sqrt{A/(12\pi\,10^{-8})}$. Zusammen mit der kalten Schwelle erhält man den allgemeinen notwendigen Massenmaßstab
$$
M\ge\frac{4m_\mu}{\sqrt{12\pi\,10^{-8}}}A^{-3/2}.
$$
Bei $A=0{,}01$ bedeutet dies $m_J\gtrsim17{,}2$ GeV und $M\gtrsim6{,}9\times10^5$ GeV je Konstituent. Die Ungleichung ist keine Existenz- oder Verträglichkeitsaussage für so schwere Materie. Sie macht sichtbar, welche Größenänderung die bisher gewählten Annahmen mindestens erfordern würden.

Die Gleichheit $g_\mu=g_J$ ist eine physikalische Annahme, die sich in einer erweiterten Eichwirkung ändern lässt. Eine Beimischung des elektromagnetischen Stroms der Form $g_JJ+\epsilon e Q_{\rm em}$ kann bei niedrigen Energien die Myonkopplung verringern. Bei den ursprünglichen Ladungen verschiebt sie die Protonkopplung entgegengesetzt, lässt die Neutronkopplung $3g_J$ unverändert und belässt die Summe von Proton- und Elektronkopplung bei $4g_J$. Ein solcher geänderter Vergleich müsste daher die Kern- und Atomtests neu rechnen. Unabhängig davon bleiben eine vollständige kosmologische Dynamik und H96 offen.
