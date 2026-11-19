# OP5: Endliche J-Reichweite, Bindung und Einfangschwelle

19. November 2026. Analytische Erkundung in M zur [ungeschirmten J-Kraft](OP5_Singulettpaar_J_Reichweite.md) und zum [radiativen Einfang](OP5_Strahlungseinfang.md). Wir fragen, ob Fernkraftunterdrückung, Bindung und eine große Ladungsanregungslücke kinematisch zugleich möglich sind. Die Vergleichsfeldliste und die J-Ladungen gewöhnlicher Materie bleiben erhalten. Wir wählen eine zusätzliche abelsche Stückelberg-Masse $m_J>0$. Diese Eingabe stammt nicht aus der ursprünglichen W1/W2-Wirkung.

## Abelsche Masse und Vergleich der Spektren

Der Term $\tfrac12(m_JJ_\mu-\partial_\mu s)(m_JJ^\mu-\partial^\mu s)$ ist invariant unter $J_\mu\mapsto J_\mu+\partial_\mu\chi$ und $s\mapsto s+m_J\chi$, bei der üblichen gleichzeitigen Transformation der geladenen Felder. Der neue Skalar ist eine Stückelberg-Koordinate, keine zusätzliche chirale Materie. Die bereits angenommene Anomalieaufhebung ist weiterhin nötig. Der statische Austausch für erhaltene Ströme liefert das Yukawa-Potential. [Ruegg und Ruiz-Altaba, Überblick zum Stückelberg-Mechanismus](https://arxiv.org/abs/hep-th/0304245)

Für zwei gleich schwere, entgegengesetzt J-geladene Singuletts mit Konstituentenmasse $M$ und reduzierter Masse $\mu=M/2$ gilt in Einheiten $\hbar=c=1$
$$
H_Y=\frac{\mathbf p^2}{2\mu}-\frac{A e^{-m_J r}}{r},\qquad A=\frac{g_J^2}{4\pi}.
$$
Schreibe $H_C$ für den Coulomb-Grenzfall. Der Potentialunterschied erfüllt punktweise
$$
0\le H_Y-H_C=\frac{A(1-e^{-m_J r})}{r}\le A m_J .
$$
Deshalb liegt die Grundenergie zwischen $-\mu A^2/2$ und $-\mu A^2/2+A m_J$. Letztere Schranke folgt schon durch Auswerten im Coulomb-Grundzustand. Ist sie negativ, liegt der Grundzustand unter der Aufbruchsschwelle null. Für seine Bindungsenergie $B_Y$ gilt dann
$$
\mu A^2/2-A m_J\le B_Y\le\mu A^2/2.
$$
Auf dem ungeraden Unterraum liegt die spektrale Unterkante von $H_Y$ mindestens bei der Coulomb-$2p$-Energie $-\mu A^2/8$. Der Abstand vom Grundzustand zur niedrigsten ungeraden Energie, gegebenenfalls zum Kontinuum, ist damit mindestens
$$
\Delta_{\rm odd}\ge \frac38\mu A^2-A m_J.
$$
Das zentrale Yukawa-Potential erhält die Parität. Beim gleich schweren Paar bleibt der Ladungsoperator $2i\sin(\mathbf q\cdot\mathbf r/2)$ ungerade und sein elastisches Matrixelement im geraden Grundzustand null. Die untere Schranke schließt angeregte Endzustände dieses Operators aus, wenn sie größer als die verfügbare Relativenergie ist. Magnetische, spinabhängige und mehrfache Austauschterme sind davon getrennt.

## Fernkraft und Emission im selben Parameterbeispiel

Für zwei gewöhnliche, J-ungeschirmte Wasserstoffatome mit Ladung $+4$ ist bei Abstand $R$ die führende Punktladungs-Fernkraft im Vergleich zur Gravitation
$$
\left|\frac{\mathcal F_J}{\mathcal F_G}\right|
=\frac{16A}{Gm_H^2}(1+m_J R)e^{-m_J R}.
$$
Die Punktformel beschreibt den Fernbereich außerhalb der gewöhnlichen Ladungsverteilungen. Bei kurzer Reichweite und Abständen in der Größenordnung der Atomgröße ist für ausgedehnte Ladungsprofile eine eigene Faltung nötig. Wir verwenden $R=1$ Å daher als nominelle Distanz für zwei punktförmige Träger der Ladung $+4$. Der Wert ist weder ein Labormesspunkt noch eine Schranke für reale Wasserstoffatome.

Übernehme $M=50$ GeV je Singulett, $A=0{,}01$ und als Rückstoßvergleich eine Zielmasse von $122$ GeV bei höchstens $800$ km/s. Die verfügbare Relativenergie beträgt $196$ keV. Für die nominellen Punktladungen wird $\lvert\mathcal F_J/\mathcal F_G\rvert<1$ bei $m_J>0{,}179$ MeV erfüllt. Das folgt aus $(1+x)e^{-x}<Gm_H^2/(16A)$ für $x=m_JR$, hier $x>90{,}71$. Die untere Schranke für den Abstand zum ungeraden Sektor liegt für $m_J<74{,}2$ MeV oberhalb von $196$ keV. Jeder endliche Abstand muss im konkreten Materiemodell geprüft werden.

Bei Einfang mit relativer Einlaufenergie $K$ in den Grundzustand ist für ein freies massives J-Quant mindestens $K+B_Y\ge m_J$ nötig. Das ist im Schwerpunktsystem zugleich die Massenschwelle; oberhalb liegt positiver Endphasenraum einschließlich Rückstoß vor. Beim Grenzfall $K\to0$ genügt nach der Bindungsuntergrenze
$$
m_J<\frac{\mu A^2}{2(1+A)}=1{,}238\,{\rm MeV}.
$$
Damit schneiden sich die hinreichenden Bedingungen im nominellen Punktmodell, etwa bei $m_J=1$ MeV. Dort gilt $B_Y\ge1{,}24$ MeV und $\Delta_{\rm odd}\ge0{,}9275$ MeV. Die Coulomb-Bindungsenergie, die zugleich obere Schranke ist, beträgt $1{,}25$ MeV. Bei $m_J=10$ MeV bleiben Fernkraftunterdrückung und Anregungslücke erhalten. Die kalte Emission eines einzelnen reellen J-Quantums ist dann geschlossen, da selbst $B_Y\le1{,}25$ MeV ist. In beiden Fällen wäre eine Einfangrate aus dem Yukawa-Kontinuum mit einem massiven Vektorfeld gesondert zu bestimmen. Die Massenschwelle allein berechnet sie nicht.

## Gewöhnliche Materie auf kurzen Distanzen

Bei $m_J=1$ MeV beträgt die Reichweite rund $197$ fm und die modellierte zusätzliche Nukleonabstoßung für punktförmige Nukleonen mit J-Ladung $+3$ bei $r=1$ fm rund
$$
+\frac{9A e^{-m_Jr}}{r}\ \simeq\ +17{,}7\,{\rm MeV}.
$$
Die Punktnukleon-Näherung bei $1$ fm dient der Größenordnung; nukleare Formfaktoren und starke Kerndynamik sind dort mitzubehandeln. Zudem verschiebt die J-Abstoßung zwischen Proton und Elektron im ungestörten Wasserstoff-$1s$-Zustand die Energie in erster Störungsordnung um
$$
\delta E_{1s}^{(1)}=3A\!\int|\psi_{1s}(\mathbf r)|^2\frac{e^{-m_Jr}}r\,d^3r
=\frac{12A}{a_H(2+m_Ja_H)^2},\qquad a_H=(\mu_{pe}\alpha)^{-1}.
$$
Beim selben Punktbeispiel ergibt das etwa $+6{,}1\times10^{-3}$ eV. Das ist ein Diagnostikwert und noch kein Vergleich mit Spektrallinien, Protonradiusdaten oder einem Fit der gewöhnlichen Kräfte. Die starke exponentielle Unterdrückung bei großen Abständen kann daher nicht als Verträglichkeit mit gewöhnlicher Materie gelesen werden. Die Kurzstreckenprüfung, die Einfangrate, der kosmologische Bestand und H96 bleiben offen.
