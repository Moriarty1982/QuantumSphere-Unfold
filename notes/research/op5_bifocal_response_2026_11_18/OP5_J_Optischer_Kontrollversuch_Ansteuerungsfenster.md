# OP5 – Optischer Kontrollversuch, kohärente Endpunktreferenz und Ansteuerungsfenster

21. November 2026. Analytische Erkundungen im Materieframe M. Die [Endpunktphase und Materialgrenze](OP5_J_Endpunktphase_Laststandard_Materialhub.md) motiviert eine unabhängig prüfbare gewöhnliche Messkette, eine gemeinsame komplexe Zeit- und Phasenreferenz sowie ein symbolisches Materialfenster. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört dies zur lokalen Auslese. I3 benötigt eine eigenständige kosmologische Bestandsdynamik.

## Rein optischer Kontrollversuch mit eigener Durchgangsreferenz

Der Versuch verwendet ausschließlich den gewöhnlich zugänglichen A-Port auf beiden Seiten eines passiven optischen Prüfkörpers. Prüfkörper und Leerkörper werden an denselben markierten Ebenen in beiden Schaltstellungen gemessen. Je Zustand und je Frequenz werden der komplexe Rücklauf $x=a_R/a_L$ und der komplexe Ausgang $y=b_R/a_L$ beobachtet. Für einen feststehenden linearen Prüfkörper ist $y=t+rx$. Die [Zweilastrechnung](OP5_J_Durchgang_Parallelpruefung.md) schätzt den Interzept $t$ aus zwei verschiedenen **gemessenen** Rückwellen. Eine zusätzliche Messung mit unabhängig kalibriertem Direktdurchgang und kontrollierter Abschlussreflexion liefert einen Vergleichswert $t_0$ für genau diese physische Ebene. Ihre Unsicherheit muss bereits Anschlussänderung, Abschlussfehler und Gaintransfer enthalten. Ein Referenzwert aus derselben Zweilastgleichung wäre keine unabhängige Kontrolle.

Ein praktikabler mathematischer Prüfplan ist, die zwei Lastzustände um $x=0$ zu legen und die beobachteten Rohwerte getrennt vom Standard für $t_0$ zu protokollieren. Bei abgeglichenen $x=\pm a$ liest $y(a)+y(-a)-2y(0)$ die gerade Abweichung vom affinen Modell. Die Differenz zweier antisymmetrischer Steigungen bei $a$ und $2a$ liest bei einer polynomiellen lokalen Abweichung bis Grad vier den kubischen Anteil $3c_3a^2$. Eine affine Schaltänderung $h_0+h_1 x$ verschwindet in beiden Kontrasten. Erst die unabhängig bekannte Durchgangsreferenz kann den Interzeptfehler $h_0$ begrenzen. Die Lastpunkte müssen gemessen oder in einer eigenen Fehlerhülle eingeschlossen werden. Bei Fehler höchstens $2\cdot10^{-8}$ in jedem auf den Sollwert korrigierten $y$ ist die deterministische Rauschgrenze des Dreipunkt-Kontrasts $8\cdot10^{-8}$.

Im bisherigen skalaren Zahlenrahmen sei der Interzeptfehler aus den zwei Lasten höchstens $2{,}001\cdot10^{-8}$. Sei die unabhängige Direktreferenz auf $3\cdot10^{-8}$ kalibriert und die beobachtete Differenz höchstens $4\cdot10^{-8}$. Dann sind die beiden physischen Direktwerte je Zustand bis auf höchstens $9{,}001\cdot10^{-8}$ miteinander verträglich. Werden alle vier erforderlichen Zustände bei jedem Bandende so geprüft und liegen die Nennerbeträge über $0{,}99$, ist der Fehler im komplexen Log-Kreuzquotienten unter $3{,}637\cdot10^{-7}$. Diese Grenze ist ein Prüfbudget für vermessene Daten, kein vorausgesagtes Bestehen. Der Versuch kann gerichteten A-Gain, gewöhnliche Echo-Kopplung und den A-Transfer zwischen Leerkörper und Marker prüfen. Eine real propagierende J-Mode oder die J-Normierung lässt sich mit dieser Anordnung nicht messen.

## Eine gemeinsame kohärente Quelle und ihr Restdelay

Für jede Frequenz können Signal und Pilot aus demselben Master geteilt und simultan komplex an derselben relevanten Ebene verglichen werden. Daraus kürzt sich der gemeinsame Quellphasor. Ein Faktor, der je Zustand und Frequenz unterschiedlich auf die Mess- und Pilotpfade wirkt, bleibt im Quotienten. Sei $d_\pm$ die Differenz des verbleibenden Delays zwischen beiden Aufbauten jeweils am Frequenzende $f_\pm$. Dann gilt exakt
$$
2\pi(f_+d_+-f_-d_-)=2\pi[\Delta f\,\bar d+f_0(d_+-d_-)].
$$
Unveränderte gewöhnliche Leitungswege können herausfallen. Eine gemeinsame Taktquelle macht eine verbleibende Zustands- oder Frequenzabhängigkeit der Referenzebenen nicht beobachtbar.

Bei der bisherigen isolierten Phasenzuteilung $2{,}5\cdot10^{-9}$ rad ergibt sich für achromatisches $\bar d$ über 100 MHz höchstens $3{,}979\cdot10^{-18}$ s. Wenn nur der chromatische Term das Budget belegt, entspricht seine Grenze einer vakuumäquivalenten Wegänderung von etwa $1{,}369$ fm bei $0{,}360329$ eV. Beide Werte betreffen unkompensierte **Differenzen**, nicht die Länge eines gemeinsamen optischen Pfads. Ein Vierfachquotient hat im Allgemeinen vier Beiträge zur Messphase und weitere Gain- und Transferanteile. Die Einzelwerte sind keine gemeinsame Geräteanforderung.

Der zuvor betrachtete J-Lastwechsel $x=\gamma T^2$ besitzt ein anderes Budget. Wenn die kompensierte Auswertung bei genau bekanntem $x$ den Produktfehler $\epsilon_0$ hätte und $\widehat x=x(1+e_x)$ verwendet wird, ist der Gesamtfehler höchstens $(\epsilon_0+|P||e_x|)/(1-|e_x|)$. Mit $|P|=9\cdot10^{-6}$, $\epsilon_0=1{,}4125\cdot10^{-7}$ und Ziel $1{,}791\cdot10^{-7}$ ist $|e_x|\le0{,}0041234$ hinreichend. Wenn allein die Einwegphase von $T$ fehlerhaft ist, bedeutet das $|\delta\arg T|\le0{,}0020617$ rad. Der A-Kontrollversuch und die hypothetische J-Last benötigen also getrennte, jeweils belegte Phasenvergleiche.

## Symbolisches Ansteuerungsfenster für den gewöhnlichen Abzug

Im [Achsensäulenvergleich](OP5_J_Optischer_Nullport_Echo_Achsensaeule.md) sei der gewöhnliche abzuziehende Beitrag $S=K\Phi_0$. Bei festem Signalprofil und Skalierung des separaten Kontrollprofils bleibt $S$ im linearen Vergleich fest und die Transfernormierung $K$ ändert sich entsprechend. Bezeichne $\beta=(E_{b_4}-E_{\rm Modell})/|S|$ als verbleibende relative Reserve, $\rho_K$ als relativen komplexen Transferfehler und $\eta_\Phi$ als absolute Unsicherheit des gewöhnlichen Kontrollpotentials. Dann ist für eine robuste Fehlergarantie hinreichend
$$
\rho_K+(1+\rho_K)\eta_\Phi/|\Phi_0|\le\beta.
$$
Für positive $\eta_\Phi$ und $\beta>\rho_K$ folgt der Mindestbetrag $(1+\rho_K)\eta_\Phi/(\beta-\rho_K)$. Die Unsicherheit $\eta_\Phi$ schließt Außenreferenz und Längsendterme ein und muss für die skalierte Kontrollfahrt gültig sein.

Die [mechanischen Mindestgrenzen](OP5_J_Endpunktphase_Laststandard_Materialhub.md) liefern die notwendigen Höchstwerte des möglichen Kontrollpotentials. Mit den dort ausgewiesenen Faktoren $C_u,C_\epsilon,C_\sigma,C_F$ sind dies
$$
|\Phi_0|\le \min\left(
\frac{G|D_\rho|\ell_z R_c U_{\max}}{C_u},
\frac{G|D_\rho|\ell_z R_c^2\epsilon_{\max}}{C_\epsilon},
\frac{G R_c^2\sigma_{\max}}{C_\sigma},
\frac{G|D_\rho|R_c^3\bar F_{\max}}{(\lambda+2\mu)C_F}
\right).
$$
Der letzte Wert gilt für die elastische Stützung. Eine kompatible spannungsfreie Endlage kann diese statische Kraftgrenze entfallen lassen. Hub, Dehnung und Dichte bleiben erforderlich. Bei Verformungsgrenzen für beide Komponenten sind beispielsweise $U_{\max}=\min(U_1,cU_2)$ und die entsprechenden kleineren Dehnungs- und Beschleunigungsgrenzen zu verwenden. Ein leeres Fenster schließt die robuste Garantie unter diesen Eingängen aus. Ein nichtleeres Fenster ist zunächst nur ein notwendiger Abgleich. Die exakten Profilnormen und Aktorgrenzen könnten weiter einschränken.

Bei einem skalaren Schaltverlauf zwischen ruhenden Endlagen gilt $\sup|s''|\ge4/T^2$ für eine Umschaltdauer $T$, denn $|s'(t)|\le \sup|s''|\min(t,T-t)$. Damit ist für zulässige Beschleunigung $A_{\max}$ und erforderlichen geometrischen Hub $U_{\rm req}$ mindestens $T\ge2\sqrt{U_{\rm req}/A_{\max}}$ nötig. Bei spannungsfreien Endlagen entfallen diese kinematischen und dynamischen Bedingungen nicht. [Umschaltung und Ruhelagen](OP5_J_Umschaltung_Ruhelagen.md)

Es wurden keine Antriebs- oder Werkstoffwerte eingesetzt. Abgleich mit tatsächlich zugänglichen, getrennt kalibrierten gewöhnlichen Messungen, freie J-Ausbreitung, HCl/H-Portkondition, native Vermittlermetrik und H96 bleiben offen.

## Rechenkontrolle

Wolfram bestätigte die Lastabschluss-Identitäten, die Delayzerlegung, die J-Last-Fehlerhülle und die Schaltzeitrelation. Qiskit wurde für diese klassischen Streu- und Materialrechnungen erwogen.

[Wolfram-Skript](op5_j_optischer_kontrollversuch_ansteuerungsfenster.wl) · [Tatsächliche Ausgabe](op5_j_optischer_kontrollversuch_ansteuerungsfenster.txt) · [Laufmanifest](op5_j_optischer_kontrollversuch_ansteuerungsfenster.json)
