# OP5 – Optischer Nullport, gekoppelte Rückläufe und Achsensäule

21. November 2026. Analytische Erkundungen im Materieframe M. Die [Standards- und Kontrollprüfung](OP5_J_Standards_Echophasen_Weylkontrolle.md) benötigt eine physisch bekannte Kreuzkalibrierung, beobachtbare Mehrwege und eine vom massiven Laufzeitbeitrag getrennte gewöhnliche Messgröße für $b_4$. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 benötigt eine eigenständige kosmologische Bestandsdynamik.

## Elektrische Null mit H und HCl

Ein bereits als rein A- oder rein J-diagonal bekannter Materialstandard ist unter der relativen diagonalen Portumskalierung invariant. Auch zwei solche Standards setzen keine bekannte Kreuzamplitude. Ein gekreuzter Standard braucht mindestens einen unabhängig bekannten von null verschiedenen A/J-Eintrag.

Die zwei modellierten [H/HCl-Feldrichtungen](OP5_J_HCl_Vektoranschluss.md) liefern einen bedingten Weg zu einer J-Einspeiserichtung. Schreibe in der diagonal-kinetischen Vergleichsbasis $v_H=a_H(1,r_H)^{\mathsf T}$ und $v_C=a_C(1,r_C)^{\mathsf T}$ in Reihenfolge $(A,J)$. Werden die getrennt adressierten Antriebe nach ihrer komplexen elektrischen Antwort normiert, hat die Kombination $a_C v_H-a_H v_C$ genau verschwindende A-Amplitude und J-Amplitude $a_Ha_C(r_H-r_C)$. Sind die normierten Beiträge um $\delta_H,\delta_C$ falsch gewichtet, bleibt $|\delta_H-\delta_C|\le2\eta$ elektrisch übrig für $|\delta_H|,|\delta_C|\le\eta$. Die J-Amplitude wird höchstens um $\eta(|r_H|+|r_C|)$ kleiner. Eine hinreichende Bedingung für ein A/J-Leckverhältnis höchstens $p$ ist folglich
$$
\eta\le\frac{p\,|r_H-r_C|}{2+p(|r_H|+|r_C|)}.
$$
Für die bisherige illustrative Kopplung $|g_J/e|=10^{-3}$ und $p=4\cdot10^{-4}$ ergibt sich in beiden HCl-Vorzeichenfällen $|r_H-r_C|\simeq0{,}002537$ und eine komplexe optische Gainanforderung von rund $5{,}07\cdot10^{-7}$ je normiertem Beitrag. Erforderlich sind elektrische Kalibrierung, identische kohärente A-Portmoden und die zugehörigen physischen J-Moden. Die Schranke modelliert nur die Gewichtungsfehler. Profiländerungen, Übersprechen, weitere Anregung und eine andere flache Kinetik gehen gesondert ein.

Die A-Null legt die absolute J-Amplitude nicht fest. Die Differenz $r_H-r_C$ hängt vom unkalibrierten $g_J$ sowie von Moden und kinetischer Normierung ab. Ohne belegten J-Durchgang oder einen anderen unabhängigen J-Standard kann auch eine ausgezeichnete A-Null kein bekanntes $C_{AJ}$ für die Kreuzkalibrierung herstellen. Ein optisch abgeglichener H/HCl-Nullport ist daher ein Richtungskandidat unter den Modellannahmen. Der myonische Vergleich liefert ebenfalls eine modellierte zweite Dipolrichtung, jedoch keinen kalibrierten gemeinsamen freien J-Kanal bei dieser optischen Frequenz. [Myonischer Vergleich](OP5_J_Myonischer_Anschluss.md)

## Zwei unabhängig phasenmarkierte Echo-Pfade

Für zwei gekoppelte markierte Rundläufe betrachte
$$
G(z,w)=C(I-U-zA-wB)^{-1}D.
$$
$U$ sammelt unmarkierte lineare Rückläufe. Setze $L=(I-U)^{-1}$, $a=\|LA\|$, $b=\|LB\|$ und $a+b<1$. Bei unabhängiger komplexer Mittelung über $z,w\in\{1,-1\}$ bleiben genau die Wörter mit gerader Zahl beider markierter Faktoren erhalten. Die gemischten Zweierwörter $AB,BA$ entfallen auch wenn sie nicht kommutieren. Die Wörter $A^2$ und $B^2$ bleiben, gemischte Wörter beginnen bei zwei Faktoren von jeder Art. Das Direktglied $CLD$ enthält weiterhin die unmarkierten Rückläufe.

Vom Direktglied abgezogen ist die Norm des markierten Rests höchstens $\|C\|\|LD\|\mathcal M(a,b)$, mit
$$
\mathcal M(a,b)=
\frac{1-a^2-b^2}{[1-(a+b)^2][1-(a-b)^2]}-1.
$$
Das ist die über beide Vorzeichen gemittelte skalare Majorante der nichtkommutierenden Reihe. Wenn beide Markierungen nur gemeinsam geschaltet werden, überlebt jedes Wort gerader Gesamtlänge einschließlich $AB$ und $BA$. Bei unveränderten Direktfaktoren und idealen Phasenstellungen liefert die getrennte Schaltung die engere Grenze.

Mit $a=b=q$ ist $\mathcal M=2q^2/(1-4q^2)$. Sind acht skalare Rohphasen zu budgetieren und ist das Verhältnis $\|C\|\|LD\|/|CLD|$ eins, genügt für einen Gesamtfehler von $6\cdot10^{-6}$ rad bei idealen Markierungen $q\le6{,}1237\cdot10^{-4}$. Die Phase eines Rohwertes relativ zum Direktglied lässt sich dann über die Fehlerscheibe mit $\arcsin\mathcal M$ begrenzen. Bei größerem Faktor oder kleinen Direktwerten verkleinert sich die Grenze. Unmarkierte und in beiden Zählungen gerade Pfade bleiben mit dem Signal vermischt. Mehr phasenstabile Wiederholungen lösen dieses Identifikationsproblem erst mit einer unabhängigen Pfadmodulation oder Transfergrenze.

## Gewöhnliches Achsenpotential aus der Säulendichte

Für die gewöhnliche statische Poisson-Metrik definiere $\sigma(r)=\int\delta\rho(r,z)\,dz$ und $\bar\Phi(r)=\int\Phi(r,z)\,dz$ für ein radialsymmetrisches Kontrollprofil. Bei verschwindenden Längsendtermen gilt
$$
\frac1r\partial_r(r\partial_r\bar\Phi)=4\pi G\sigma.
$$
Bei kompakter Säule bis $R_c$, verschwindendem Querintegral und einer kalibrierten Außennull ergibt Integration von der Außenreferenz zur Achse
$$
\bar\Phi(0)=-4\pi G\int_0^{R_c}r\,\sigma(r)\log(R_c/r)\,dr.
$$
Ein absoluter punktweiser Säulendichtefehler höchstens $\epsilon_\sigma$ führt zu höchstens $\pi G R_c^2\epsilon_\sigma$ Fehler im Achsenpotential. Hinzu kommen die Außennull und, bei endlichem Längsfenster, der Beitrag der Differenz der longitudinalen Gradienten an den Fensterrändern. Für einen punktweisen Betrag dieses Endterms bis $\epsilon_{\rm end}$ genügt $R_c^2\epsilon_{\rm end}/4$. Bei nicht exakt rotationssymmetrischen Störquellen genügen die azimutal gemittelten Dichte- und Randwerte, weil der Winkel-Laplace-Term sich wegmittelt und der Achsenwert regulär ist. Alternativ kann eine unabhängig gewöhnlich-selektiv bestimmte radiale Beschleunigung von der Achse bis zur Außenreferenz integriert werden. Ihre gleichmäßige Unsicherheit multipliziert sich mit höchstens der Integrationslänge. Die kompensierende Übergangs- und Annulusregion muss in der Dichteintegration erfasst werden. Die konstante gewöhnliche $b_4$-Potentialkomponente im Kern des $s^4$-Profils ist im Kern selbst in der Säulendichte unsichtbar.

Der [Binnenfeldvergleich](OP5_J_Binnenfeld_Messweg.md) erlaubt einen direkten Transfer vom gewöhnlichen Achsenpotential des $s^4$-Kontrollprofils zum entarteten gewöhnlichen Weyl-Term des Signalprofils. Für denselben $R$ und denselben gewöhnlichen Kopplungsfaktor gilt
$$
W^{(b_4)}_S(s)=\frac{A_Ha\,P_z^S\kappa R^4s}{128c_4P_z^C}\bar\Phi_C(0).
$$
Dabei ist $W$ die radiale minus tangentiale Gezeitenantwort geteilt durch zwei und integriert entlang der Strecke. Die Formel eliminiert den gemeinsamen gewöhnlichen Vorfaktor und $b_4$. Für prognostizierten Faktor $\widehat K$ einschließlich der gewöhnlichen Geräteantwort und Fehler $\eta_K$ ist der Fehler des subtrahierten Beitrags höchstens
$$
|\widehat K|\eta_\Phi+\eta_K(|\widehat{\bar\Phi}_C(0)|+\eta_\Phi),
$$
zuzüglich Profil- und Übertragungsresten. Die gewöhnliche Säulendichte oder der gewöhnliche radiale Gradient müssen unabhängig vom nativen massiven Signal bestimmt werden. Die erforderliche tatsächlich selektive Messung und die Übertragbarkeit des gewöhnlichen Modells bleiben offen. Dasselbe gilt für freie J-Ausbreitung, native effektive Metrik, Portkondition und H96.

## Rechenkontrolle

Wolfram prüfte die optische Null und ihre Fehlertoleranz, die Echo-Majorante, den logarithmischen Poisson-Kern und den $b_4$-Transfer. Qiskit wurde für diese klassischen komplexen und symbolischen Prüfungen erwogen.

[Wolfram-Skript](op5_j_optischer_nullport_echo_achsensaeule.wl) · [Tatsächliche Ausgabe](op5_j_optischer_nullport_echo_achsensaeule.txt) · [Laufmanifest](op5_j_optischer_nullport_echo_achsensaeule.json)
