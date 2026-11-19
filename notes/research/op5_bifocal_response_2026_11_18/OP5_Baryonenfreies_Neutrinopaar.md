# OP5: Stabilität und Massenbilanz eines baryonenfreien Neutrinopaars

19. November 2026. Analytische Erkundung in M. Die [Baryonenbilanz](OP5_Protonverband_Massenbudget.md) schließt den Protonverband unter der konventionellen Dichtenormierung als Quelle des fehlenden Materieanteils aus. Die [Erweiterung mit entgegengesetzter J-Ladung](OP5_Anomalie_Betazerfall.md) erlaubt ein Paar aus einem gewöhnlichen Dirac-Neutrino $\nu$ und einem Neutrino $\nu'$ der Zusatzgeneration. Die geladenen und neutralen schwachen Ströme der Zusatzgeneration werden hier wie bei einer gewöhnlichen sequentiellen Generation angenommen. Beide Neutrinos haben $B-L=-1$, und ihre J-Ladungen sind $+1$ und $-1$. Wir prüfen die Ladungs- und Massenschwellen und behalten die [vorgesehene Prüfung von H96](../predictions/Vorab_Notiz_H96_Omega_M_beta2.md) separat.

## Bedingter Schutz der Konstituenten

Wähle generationserhaltende Dirac-Yukawa-Matrizen und erhalte $B-L$ separat im ursprünglichen und im zusätzlichen Sektor. In der gewählten renormierbaren Feldliste erhalten die geladenen schwachen Ströme sowie J- und Higgsvertex diese zwei Vektorladungen. Die beiden Ströme haben in dieser Feldliste auch keine gemischte Anomalie mit den dynamischen Eichfeldern. Für eine linkshändige Generation lauten die Gewichte $3(B-L)$ auf $(Q,u^c,d^c,L,e^c,\nu^c)$ gleich $(1,-1,-1,-3,3,3)$. Die Spur für $SU(2)^2(B-L)$ ist proportional zu $3\cdot1-3=0$, jene für $SU(3)^2(B-L)$ zu $2-1-1=0$. Multiplizitätsgewichtet verschwinden ebenfalls die Spuren $(B-L)Y^2$, $(B-L)J^2$, $(B-L)YJ$ und die gemischt gravitative Spur. Das Umkehren der J-Ladung lässt diese Nullwerte bestehen. Die Kontrolle benutzt die explizite Ladungstabelle der [Eicherweiterung](OP5_Anomalie_Betazerfall.md). Die getrennte Erhaltung ist eine Modellwahl und schränkt zusätzliche Operatoren ein.

Das Paar hat die getrennten Ladungen $(-1,-1)$ und Gesamtladungen $Q_J=Q_{\rm em}=B=0$. Die vollständige Annihilation in Feldquanten ist daher ausgeschlossen. Eine Umwandlung in zwei Neutrinos desselben Sektors verletzt die getrennten Vektorladungen und trägt zudem eine von null verschiedene J-Ladung. Eine geladene schwache Umwandlung in rein leptonische Zwei-Körper-Endzustände mit denselben beiden Vektorladungen muss in beiden Sektoren je ein Lepton belassen. Ein Austausch eines Neutrinos gegen ein geladenes Lepton ergäbe elektrische Ladung $-1$ bzw. $-2$. Ein solcher Kanal verlangt daher weitere Teilchen. Eine hinreichende Spektralvoraussetzung ist, dass es im betrachteten Gesamtladungssektor keine tiefere Teilchenschwelle gibt, etwa durch leichtere mehrfach besetzte Konstituenten oder durch andere zusammengesetzte Zustände. Die Ladungsrechnung allein entscheidet diese Voraussetzung nicht.

Für vorgegebene stabile Konstituenten und den festen Zwei-Körper-Hamiltonoperator ist der Coulomb-Grundzustand unter der Aufbruchsschwelle und besitzt keinen tieferen Zustand für radiativen Zerfall. Mit $m=M_\nu$, $M=M_{\nu'}$, $\mu=mM/(m+M)$ und $A=g_J^2/(4\pi)$ gilt
$$
B_{\rm P}=\frac{\mu A^2}{2}>0,\qquad
a=(\mu A)^{-1},\qquad
M_{\rm P}=M+m-B_{\rm P}.
$$
Die Formeln verwenden schwache J-Kopplung und vernachlässigen kurzreichweitige Wechselwirkungen. Sie bestimmen die Coulomb-Bindung im gegebenen Sektor und keine Zerfallsrate des vollständigen Modells.

## Schwache Neutralströme und der schwere Konstituent

Die linkshändigen Komponenten beider Neutrinos tragen dieselben elektroschwachen Quantenzahlen. Für ein zusätzliches sehr leichtes aktives Neutrino mit Standardstärke wäre deshalb ein weiterer Beitrag zur unsichtbaren Z-Breite zu erwarten. Die Z-Polmessungen sind mit drei solchen leichten Arten verträglich. Der exakt kinematische Weg, den zusätzlichen Zwei-Körper-Kanal $Z\to\nu'\bar\nu'$ zu schließen, ist $M\ge m_Z/2\simeq45{,}6$ GeV. Nahe der Schwelle ist der offene Kanal phasenraumunterdrückt. Die Zahl $m_Z/2$ dient hier als Kriterium für kinematischen Schluss und nicht als aus der Z-Breite allein abgeleitete scharfe Massengrenze. Sie betrifft die Anschlussbedingung, wenn die betrachtete Zusatzgeneration über das beobachtete Standardmodell hinausgeht. [PDG, Zahl leichter Neutrinoarten](https://pdgweb.lbl.gov/2024/listings/rpp2024-list-number-neutrino-types.pdf)

Auch das Paar selbst ist im Modell nicht schwach neutral. Im Coulomb-Grundzustand und in führender nichtrelativistischer Näherung liefert der kohärente Vektoranteil des elastischen Z-Matrixelements, in Einheiten der gemeinsamen Einteilchen-Vektorladung,
$$
\mathcal F_Z(q)= f\!\left(\frac{M}{m+M}q\right)+f\!\left(\frac{m}{m+M}q\right),
\qquad f(k)=(1+a^2k^2/4)^{-2}.
$$
Hier ist $f$ die Fouriertransformierte der normierten Coulomb-$1s$-Dichte und die beiden Faktoren im Argument folgen aus den relativen Schwerpunktkoordinaten. Insbesondere gilt $\mathcal F_Z(0)=2$. Der entsprechende J-Vektoranteil ist eine Differenz und verschwindet bei $q=0$. Diese Rechnung gilt für den angegebenen elastischen Grenzfall und enthält keine vollständige Streu-, Abkühlungs- oder Detektorvorhersage.

## Woher die Masse kommt

Für $m>0$ und $M\gg m$ gilt $B_{\rm P}\le m A^2/2$. Bei einer gebundenen Stückzahl pro Volumen $n_{\rm P}$ dominiert die bereits im Zusatzneutrino vorhandene Ruheenergie:
$$
\rho_{\rm P}=n_{\rm P}(M+m-B_{\rm P}),\qquad
\rho_{\rm P}-n_{\rm P}M\le m n_{\rm P}.
$$
Mit $m\le1$ eV und $M\ge45{,}6$ GeV beträgt der mögliche relative Zuwachs gegenüber demselben Bestand freier Zusatzneutrinos höchstens $2{,}2\times10^{-11}$. Wenn die leichten Neutrinos in der Ausgangsbilanz schon enthalten sind, sinkt die gesamte Ruheenergie dieser beiden Populationen durch die Bindung um $n_{\rm P}B_{\rm P}$. Die Bildung kann ihre Dynamik und Strahlungsbilanz verändern. Sie berechnet keine zusätzliche große Ruhemasse.

Soll die Komponente näherungsweise eine konventionelle kalte Materiedichte $\Omega_c h^2\simeq0{,}120$ liefern, beträgt die nötige Stückzahl einschließlich eines eventuellen Antipaarbestands
$$
n_{\rm P} \simeq \frac{0{,}120}{M+m-B_{\rm P}}\frac{\rho_{\rm crit}}{h^2}.
$$
Der Wert ist eine Referenz zur Größenordnung, kein Test des H96-Ziels. Ohne Herleitung der Erzeugung und des Überlebens der schweren Zusatzneutrinos ist die benötigte Stückzahl ein freier Bestand. Für eine Vorhersage wären danach insbesondere Einfang, Ionisation und die schwache Kopplung an gewöhnliche Materie im selben kosmologischen Modell zu bestimmen. [Planck 2018, kosmologische Parameter](https://arxiv.org/abs/1807.06209)

Das Paar beseitigt die Bindung der Anzahl an den Baryonenvorrat. Die benötigte zusätzliche Materiedichte müsste aber nahezu vollständig aus schon vorhandenen schweren Zusatzneutrinos stammen. Die vollständige Stabilität, ihre Abundanz und H96 bleiben offen.
