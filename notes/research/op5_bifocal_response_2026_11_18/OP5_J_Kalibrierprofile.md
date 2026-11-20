# OP5: Kalibrierprofile der statischen J–Gravitations-Antwort

20. November 2026. Die Profile beziehen sich auf den [partiellen Kreuzspektrumsquotienten](OP5_J_Gravitative_Reichweitenkalibrierung.md) und lassen sich direkt in den [Ausschlusstest mit gemeinsamen Fehlern](OP5_J_Minimax_Polreduktion.md#gemeinsame-kalibrierfehler) einsetzen. Sie sind aus der Messabbildung hergeleitet. Amplituden aus echten J-, Gravitations- und Tracerkarten liegen in den geprüften Projektquellen nicht vor.

## Vorwissen geprüft

Das [Gesamtbild](../../../wiki/Gesamtbild.md) führt H96 als offenen Vergleich des heutigen Materieanteils. Die [H96-Vorabnotiz](../predictions/Vorab_Notiz_H96_Omega_M_beta2.md) fixiert einen veröffentlichten $\Omega_M$-Wert und das zugehörige $2\sigma$-Kriterium. Die hier kalibrierte lokale Antwort ist ein vorgelagerter OP5-Messschritt. Der [Gravitationsabgleich](OP5_J_Gravitationsabgleich.md) setzt gemeinsame räumliche Karten und eine überprüfte Tracerprojektion voraus. Die [Tomographie](OP5_J_Tomographische_Mehrdeutigkeit.md) liefert unter ihren Voraussetzungen einen idealisierten Antwortkörper. Für den Übergang zu $\Omega_M$ braucht man zusätzlich den absoluten J-Mittelwert, die übrigen Materiebeiträge und die kritische Dichte. Die H96-Vorabfestlegung gilt unverändert.

## Antwort, Konvention und Profile

Setze $x=q^2$, mit zwei J-Karten $U_1,U_2$, Gravitationskarte $G$ und Tracer $B$, alle auf derselben räumlichen Auflösung und demselben Schnitt. Mit $P_{AB}=\langle\delta\widetilde A\,\delta\widetilde B^*\rangle$ sei
$$
X=P_{1G}-P_{1B}P_{BG}/P_{BB},\qquad
Y=P_{12}-P_{1B}P_{B2}/P_{BB},\qquad y=Y/X.
$$
$Y$ ist das partielle Split-Kreuzspektrum. Die Verwendung setzt die im Gravitationsabgleich genannten Unkorreliertheiten der Split-Fehler voraus. Der Rechner verarbeitet reelle, auf gemeinsamen Phasenbezug geprüfte Spektren. Ein unkontrollierter Imaginärteil verlangt seinen eigenen Kalibriernachweis.

Ein normiertes Profil $b_\alpha$ ist die Änderung in $y$ pro gemeinsamer Amplitude $\eta_\alpha$ bei $\eta_\alpha=0$. Alle Bins verwenden für ein Profil denselben Koeffizienten. Die Spalte „Kalibrierung“ gibt an, welche unabhängige Messung oder Variation zur Amplitudengrenze gehört.

| Gemeinsamer Fehler | Profil in $y$ | Kalibrierung |
| --- | --- | --- |
| Relative Verstärkung von $U_2$ | $+y$ pro relativer Gainänderung | Einspeisung und Wiedergewinnung einer Referenzamplitude im zweiten Split |
| Relative Verstärkung von $G$ | $-y$ pro relativer Gainänderung | Unabhängiges Massen- oder Transfernormal der Gravitationskarte |
| Relative Verstärkung von $U_1$ oder $B$ | $0$ exakt bei gemeinsamer reeller, von null verschiedener Multiplikation im Bin | Gleichheit der Multiplikation in allen beteiligten Spektren prüfen |
| Differentieller Transfer $U_2/G$ | $y h(x)$ für eine relative Transferänderung $h(x)$ | Transferkurve aus Einspeisung und Wiedergewinnung auf den tatsächlich genutzten Skalen |
| Differenz der gaußförmigen Filtervarianzen $s_2-s_G$ | $-xy/2$ pro Varianzeinheit, bei Transfer $\exp(-s x/2)$ | Unabhängige Breitenkalibrierung und Prüfung dieses Filtermodells |
| Restmaterie in $G$ | $-y\,P_{1\epsilon\cdot B}/X$ pro Einheit eines gemessenen Residualtemplates $\epsilon$ | Separater Materietracer oder Kontrollkarte nach Projektion auf $B$ |
| Zusätzlicher Anteil $s(x)B$ in $G$ | $0$ exakt, wenn er pro Bin tatsächlich proportional zu demselben Tracer ist | Konsistenz der Tracerkarten und der gemeinsamen Filterung |
| Störung der Form von $B$ | $(\delta Y-y\,\delta X)/X$ | Kreuzspektren mit einer kontrolliert variierten Tracerkarte neu bestimmen |
| Gemeinsame Skalenabweichung $q\mapsto(1+\eta)q$ | $2x\,y'(x)$ | Externe Skalenkalibrierung und aus Rebinning oder unabhängigem Transfermodell bestimmte Ableitung |

Bei den Gain- und Transferprofilen bleiben die übrigen Karten jeweils fest. Die Formel der Gaußzeile verwendet die Transferkonvention direkt auf Kartenebene. Ein bereits dekonvolvierter Transfer ist mit der tatsächlich verbleibenden Änderung anzusetzen. Für endliche reine Gains gilt exakt $y'=y\,g_2/g_G$. Die exakten Kürzungen gelten für binweise gemeinsame Faktoren. Modenmischung innerhalb eines Bins wird über neu berechnete Spektren eingebracht. Eine Änderung des Tracers durch Signalbeimischung oder sein additives Rauschen ist eine Formstörung und fällt nicht unter die Gain-Kürzung. Offset und Drift, die erst additiv entstehen *nachdem* $y$ gebildet wurde, fallen bis zum gewählten Kontaktgrad aus der Prüfmatrix heraus.

## Rechner und einheitliche Fehlerschranke

Der [Profilrechner](op5_j_kalibrierprofile.py) verarbeitet sechs reelle Rohspektren pro Bin. Der Tracernenner lässt sich algebraisch kürzen:
$$
y=N/D,\qquad
N=P_{12}P_{BB}-P_{1B}P_{B2},\qquad
D=P_{1G}P_{BB}-P_{1B}P_{BG}.
$$
Jeder benannte Eingangsmode beschreibt die **durch seine Kalibriergrenze bereits skalierte** affine Änderung $\Delta_\alpha P$ der Rohspektren. Die restliche gemeinsame Amplitude läuft dann in $[-1,1]$. Die erste Variation liefert
$$
b_\alpha=\frac{\delta_\alpha N-y\,\delta_\alpha D}{D}.
$$
Affine Änderungen der Rohspektren ergeben wegen der Produkte quadratische Beiträge $R_N,R_D$. Der Rechner begrenzt sie durch Summen von Beträgen. Mit $\ell=\sum_\alpha\eta_\alpha b_\alpha$ und der gesamten Nenneränderung $\Delta D$ gilt exakt
$$
y'-y-\ell=\frac{R_N-y R_D-\ell\,\Delta D}{D+\Delta D}.
$$
Aus $|\ell|\le\sum_\alpha|b_\alpha|$ folgt die ausgegebene obere Schranke für den nichtlinearen Rest. Der Rechner prüft $P_{BB}>0$ und hält $D$ über die ganze Eingabebox von null fern. Andernfalls meldet er den betroffenen Bin. Für nichtaffine Änderungen der **Eingabespektren** muss ihre Abweichung von der verwendeten Box zusätzlich eingeschlossen werden, etwa durch separate Fehlerprofile mit einer unabhängig validierten Hülle. Eine Folge von Zentraldifferenzen allein belegt eine solche Hülle nicht.

Der Aufruf ist `python op5_j_kalibrierprofile.py kalibrierung.json`. Die Ausgabe gibt $y_j$, jede gemeinsame Profilspalte $b_{\alpha,j}$ und die Resthalbbreite $R_j$ als exakte Bruchstrings aus. Im Ausschlusstest zur tatsächlichen Kalibrieramplitude eins werden die Profilspalten gekoppelt übernommen. Die unabhängigen Halbbreiten sind dann $\sigma_j^{\rm Messung}+R_j$ zuzüglich separat begrenzter Eingabereste. Bei Änderung der Eingabeamplituden wird der nichtlineare Rest neu berechnet.

Ein synthetischer Bin demonstriert das Format. Für mehrere Bins sind dieselben Modenamen zu verwenden. Ein Nullbeitrag wird als leeres Objekt angegeben. Fehlende Spektren **innerhalb einer Mode** bedeuten null.

~~~json
{
  "bins": [{
    "x": "1",
    "spectra": {
      "p_12": "13/10", "p_1g": "5", "p_1b": "1",
      "p_b2": "1", "p_bg": "2", "p_bb": "2"
    },
    "modes": {
      "j2_gain": {"p_12": "13/1000", "p_b2": "1/100"},
      "g_gain": {"p_1g": "1/10", "p_bg": "1/25"},
      "g_tracer_leakage": {"p_1g": "1/20", "p_bg": "1/10"},
      "tracer_shape": {
        "p_1b": "1/50", "p_b2": "-1/100", "p_bg": "1/50", "p_bb": "1/50"
      }
    }
  }]
}
~~~

Der Bin ergibt $y=1/5$, die Profilwerte $1/500$, $-1/250$, $0$ und $1/1000$ sowie den Restbetrag $16717/38969000$ als Obergrenze. Die Rechnung wurde mit exakten Brüchen am kartesischen Testgitter $\{-1,0,1\}^4$ geprüft. Die algebraische Schranke gilt für die ganze Box. Tests prüfen auch die Ablehnung von Bins bei möglicher Null des Tracer- oder Quotientennenners.

Die vorhandenen Projektquellen definieren das Verfahren und die Schlüsselgrößen. Für zahlenmäßige Messprofile fehlen binweise reelle Kreuzspektren der gemeinsamen Karten sowie extern bestimmte Grenzen der Gain-, Transfer-, Tracer- und Skalenvariationen. Der synthetische Bin dient dem Rechentest. H96 erhält dadurch keinen neuen Vergleichswert.
