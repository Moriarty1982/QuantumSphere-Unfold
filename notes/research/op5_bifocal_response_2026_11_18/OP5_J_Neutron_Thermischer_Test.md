# OP5: Neutron–Blei bei thermischer Energie und innere Randpole

19. November 2026. Nicht blinde analytische Erkundung in M. Die [inverse Nullenergie-Rechnung](OP5_J_Neutron_Randabstimmung.md) verlangt am elektromagnetischen Lepton-Nullpunkt eine stark abgestimmte Kernrandbedingung. Wir vergleichen zusätzlich bei endlicher thermischer Energie, ohne die effektive-Reichweiten-Entwicklung bis dorthin fortzusetzen. Betrachtet wird dieselbe statische äußere Schrödinger-Gleichung. Der Kern ist für die Schlussfolgerung reell, lokal, energieunabhängig und einkanalig. Sein inneres Potential wird ansonsten offen gelassen.

## Eingangsintervalle

Für die Nullenergie-Streulänge verwenden wir wie zuvor $9\le a\le10$ fm. Dieses Intervall enthält die gebundene kohärente NIST-Angabe $9{,}50$ fm samt Umrechnung zur freien Streulänge. Die Nukleardatenauswertung JENDL-5 gibt für Blei-208 bei der Laborenergie $E_{\rm lab}=0{,}0253$ eV einen elastischen Querschnitt von $11{,}46$ barn. Der Wert stammt aus einer evaluierten Bibliothek bei 300 K. Wir behandeln beide Zahlen als konventionelle Bedingungen für den Modellvergleich, ohne sie als statistisch unabhängige Rohmessungen zu verwenden. Die Anwendung auf den reellen Streuoperator setzt voraus, dass der evaluierte thermische Wert den elastischen freien Kernquerschnitt in dieser Größenordnung repräsentiert. [NIST, Streulängen](https://www.ncnr.nist.gov/resources/n-lengths/list.html), [JAEA, JENDL-5 für Blei-208](https://wwwndc.jaea.go.jp/jendl/j5/elm/Table/z082/T208.html)

Für $r\ge r_0=20$ fm gilt im [bisherigen Modell](OP5_J_Neutron_Blei.md) $u_k''=(W-k^2)u_k$ mit
$$
W(r)=\frac{2\mu_{nT}}{(\hbar c)^2}\,2118 A\,\frac{\hbar c}{r}e^{-m_Jr/(\hbar c)} .
$$
Die Eingaben sind $A=0{,}01$, $\mu_{nT}=0{,}935$ GeV und $0{,}179<m_J<1{,}238$ MeV. Mit der kleinen Umrechnung von Labor- in Schwerpunktsenergie hat der thermische Wellenvektor $3{,}47\times10^{-5}<k<3{,}50\times10^{-5}$ fm$^{-1}$. Da alle Beiträge der Partialwellen zum elastischen Integralquerschnitt nichtnegativ sind, gilt $4\pi\sin^2\delta_0/k^2\le\sigma_{\rm el}$. Die JENDL-Zahl ergibt $\sqrt{\sigma_{\rm el}/(4\pi)}<9{,}56$ fm. Wir können die Phase modulo $\pi$ daher mit $|\delta_0|/k<10$ fm wählen und die äußere Lösung durch $u_k(r)\sim\sin(kr+\delta_0)/k$ normieren. Das Vorzeichen der Phase wird nicht vorausgesetzt.

## Positivität der äußeren Lösung bei thermischer Energie

Wähle den Abgleichradius $R=35000$ fm und $b=0{,}0009071$ fm$^{-1}$ als untere Schranke für $m_J/(\hbar c)$. Für $r\ge R$ gilt mit nach oben gerundetem Wert $W(r)\le9{,}34\times10^{-17}e^{-b(r-R)}$ fm$^{-2}$. Das asymptotische Integralproblem ist
$$
u_k(r)=\frac{\sin(kr+\delta_0)}{k}
+\int_r^\infty \frac{\sin[k(t-r)]}{k}W(t)u_k(t)\,dt .
$$
Die Iteration des Volterra-Kerns beschränkt die Abweichungen in $k u_k(R)$ und $u_k'(R)$ von der freien Lösung durch $e^D-1$, wobei $D=\int_R^\infty W(t)\,dt/k<3{,}0\times10^{-9}$. Beim freien Rückwärtstransport dieser Randabweichungen auf $[r_0,R]$ ist die absolute Abweichung der Wellenfunktion kleiner als $2(e^D-1)/k<2\times10^{-4}$ fm. Dort ist $0<kr+\delta_0<\pi/2$, und der freie Anteil bleibt einschließlich dieses Fehlers positiv. Er liegt für $100\le r\le200$ fm über $80$ fm.

Auf demselben Intervall bis $R$ ist der rückwärts laufende Volterra-Kern $\sin[k(t-r)]/k$ nichtnegativ, da $0\le k(t-r)<1{,}23$. Der positive freie Rückwärtstransport ist daher eine Untergrenze von $u_k$. Insbesondere gilt $u_k(100\,{\rm fm})>80$ fm. Die abgeleitete Integralgleichung enthält $-\int_r^R\cos[k(t-r)]W(t)u_k(t)\,dt$. Sein Anteil auf $[100,200]$ fm zeigt $u_k'(100\,{\rm fm})<0$, denn dort sind der Cosinus größer als $0{,}99$ und $W>0{,}286$ fm$^{-2}$. Der Betrag der Ableitung des freien Rückwärtstransports ist kleiner als $1{,}001$. Auf $[20,100]$ fm gilt $W-k^2>(1{,}03\,{\rm fm}^{-1})^2$. Ein elementarer Rückwärtsvergleich liefert damit
$$
u_k(r)\ge80\,{\rm fm}\,\cosh[1{,}03\,{\rm fm}^{-1}(100\,{\rm fm}-r)] .
$$

## Abgleich der beiden Energien

Die frühere Nullenergielösung $u_0$, normiert durch $u_0(r)\sim r-a$, erfüllt auf $[20,100]$ fm dieselbe Cosinus-hyperbolicus-Schranke mit Vorfaktor $90$ fm. Beide Lösungen sind auf $[r_0,R]$ positiv. Für ihren Wronskian folgt direkt aus den Differentialgleichungen
$$
u_0(r_0)u_k(r_0)[L_{\rm außen}(k^2)-L_{\rm außen}(0)]
=(u_0u_k'-u_0'u_k)(R)
+k^2\int_{r_0}^{R}u_0u_k\,dr,\qquad L=u'/u .
$$
Der Randterm am großen Radius hat Betrag unter $2\times10^5$ fm. Dazu genügen $|u_k(R)|<3\times10^4$ fm, $|u_k'(R)|<1{,}001$, $|u_0(R)|<2R$ und $|u_0'(R)|<2$. Die beiden Nullenergieschranken folgen aus der Volterra-Gleichung am Außenrand mit dem gewichteten Normparameter $W(R)[1/b^2+2/(b^3(R-10\,{\rm fm}))]<1{,}3\times10^{-10}$ und der daraus folgenden Ableitungsschranke. Das positive Integral liefert bereits über $[20,21]$ fm, multipliziert mit $k^2$, mehr als $10^{64}$ fm. Damit gilt im ganzen angegebenen Fenster strikt
$$
L_{\rm außen}(k^2)>L_{\rm außen}(0).
$$
Die astronomische Differenz der beiden Terme dient nur zum Nachweis des Vorzeichens. Der Wronskian muss zur Gewinnung des Randunterschieds noch durch $u_0(r_0)u_k(r_0)$ geteilt werden.

Für die reguläre Lösung eines reellen, lokalen und energieunabhängigen inneren Einkanaloperators gilt zwischen seinen Randpolen dagegen
$$
\frac{dL_{\rm innen}}{d(k^2)}
=-\frac{\int_0^{r_0} u_{\rm innen}(r;k^2)^2\,dr}{u_{\rm innen}(r_0;k^2)^2}<0.
$$
Diese Identität folgt durch Differenzieren der inneren Schrödinger-Gleichung nach $k^2$ und Auswerten des Wronskians. Die reguläre Randbedingung am Ursprung lässt den dortigen Wronskian verschwinden. Bei glattem Anschluss müssen die logarithmischen Ableitungen an beiden Energien übereinstimmen. Die beiden Vergleichswerte können daher nur getroffen werden, wenn $u_{\rm innen}(r_0;\tilde k^2)=0$ für mindestens ein $0<\tilde k^2<k^2$. Das entspricht einem Dirichlet-Eigenwert des abgeschnittenen inneren Problems in einem Intervall schmaler als $25{,}3$ meV über der Schwelle. Es ist eine notwendige Bedingung und kein Nachweis einer beobachtbaren Resonanz des vollen Streuproblems.

Damit ist eine glatte polfreie Kernkorrektur in diesem Einkanalmodell mit den beiden Referenzwerten unvereinbar. Ein absichtlich eingebauter innerer Pol, komplexe oder energieabhängige optische Potentiale und gekoppelte Kanäle werden dadurch nicht allgemein ausgeschlossen. Die Beobachtungsprüfung von H96 bleibt separat offen.
