# OP5 – Stärke und Übersprechen der HCl/H-Anschlüsse

20. November 2026. Analytische Erkundung im Materieframe M. Der [H³⁵Cl-Vektorübergang](OP5_J_HCl_Vektoranschluss.md) liefert bei 0,360329 eV zusammen mit einem getrennten H-Anschluss zwei unabhängige Feldrichtungen. Hier wird rückwärts von einer geforderten Mindestantwort gerechnet. Gefragt ist, wann die Rohsignale beider Anschlüsse groß genug bleiben, um die zwei Feldanteile im linearen Modell zu trennen.

## Vorwissen geprüft

Die Projekteinstufung folgt dem [Gesamtbild](../../../wiki/Gesamtbild.md), insbesondere der Trennung von lokaler Auslese, nativer Dynamik und H96. Die [fixierten Isotopenanschlüsse](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Fixierte_Isotopenanschluesse.md) untersuchen normierte Richtungen, der [myonische Vergleich](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Myonischer_Anschluss.md) auch die Unterdrückung der elektrischen Antwort. Der [A/B-Vergleich](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Sende_Empfangsports.md) setzt stabile Anschlussmatrizen voraus. Die neue Rechnung setzt vor dieser Auswertung an und bestimmt die kleinste Singulärzahl bei ungleichen Verstärkungen und komplexem Übersprechen. Die Suche nach diesen Stichworten in Vorab-Notizen, OP5-Notizen, Wiki und analysis ergab für die HCl/H-Paarung keine frühere Rechnung. Für die bei I3 fehlende kosmologische Populationsdynamik wäre eine eigene Wirkung mit Bestandsentwicklung erforderlich.

## Anschlussmatrix

Die beiden Feldkoordinaten werden in die kanonische Basis gebracht. Am Sender seien $v_H,v_C$ die normierten Feldrichtungen des H-Anschlusses beziehungsweise der HCl-Linie, $a,b\ge 0$ ihre Amplituden bei gleich normierten Ansteuergrößen und $\rho=v_H^\dagger v_C$. Normen für Feld, Ansteuerung und Detektion sind festzulegen, etwa durch gleiche Bezugsamplituden oder durch die Rauschskalierung der Kanäle. Definiere $s=\sqrt{1-|\rho|^2}$. Die Sendeantwort bei einer festen Energie ist
$$
F=[v_H,v_C]\begin{pmatrix}a&0\\0&b\end{pmatrix}S,\qquad
S=\begin{pmatrix}1&u\\v&1\end{pmatrix}.
$$
Zeilen von $S$ bezeichnen die beiden Volumina, Spalten die beiden Antriebe. $u,v$ sind komplexe relative Überlappungen. Direkte Antworten sind in $a,b$ und den Richtungsphasen enthalten. Dasselbe Modell kann am Empfänger mit separat kalibrierten Verstärkungen und Übersprechtermen für die adjungierte Empfangsmatrix benutzt werden.

Für $T=\operatorname{tr}(F^\dagger F)$ und $D=\det(F^\dagger F)$ gilt
$$
T=a^2(1+|u|^2)+b^2(1+|v|^2)+2ab\,\mathrm{Re}[\rho(v+\bar u)],
\qquad
D=a^2b^2s^2|1-uv|^2.
$$
Falls $F\ne0$, ergibt sich
$$
\sigma_{\min}(F)^2=\frac{2D}{T+\sqrt{T^2-4D}}.
$$
Die Formel zeigt getrennt, wie ein schwacher Anschluss, fast parallele Feldrichtungen oder fast proportionale Antriebe den kleinsten Signalgewinn verringern. Bei $\delta=\max(|u|,|v|)<1$ liefert $\|S-I\|_2=\delta$ die Schranke $\sigma_{\min}(F)\ge(1-\delta)\sigma_{\min}(F|_{S=I})$. Bei festen Überlappungen und festem Winkel ist der Grenzwert für $b\to\infty$ gleich $a s|1-uv|/\sqrt{1+|v|^2}$. Dazu in der Formel $D/b^2$ konstant halten und $T/b^2\to 1+|v|^2$ verwenden.

## Mindestantwort und Frequenzfenster

Ohne Übersprechen gilt $\sigma_{\min}\le a s$. Das sieht man an einer normierten linken Feldrichtung senkrecht zu $v_C$, auf die der H-Anschluss den Betrag $as$ projiziert. Der Grenzwert wird für sehr großes $b$ erreicht. Ein höherer HCl-Peak allein kann diese Grenze bei gegebener H-Referenz nicht anheben.

Sei $t>0$ die geforderte kleinste Singulärzahl am betrachteten Ende. Für $0<t<a s$ ist im Fall $S=I$ die Bedingung $\sigma_{\min}\ge t$ äquivalent zu
$$
b^2\ge b_{\mathrm{req}}^2
=\frac{t^2(a^2-t^2)}{a^2s^2-t^2}.
$$
Denn die erste Diagonale von $F^\dagger F-t^2 I$ ist $a^2-t^2>0$, und seine Determinante ist $b^2(a^2s^2-t^2)-t^2(a^2-t^2)$. Für nichtorthogonale Richtungen ist bei endlichem $b$ stets $\sigma_{\min}<as$. Im orthogonalen Sonderfall gilt $\sigma_{\min}=\min(a,b)$, und $t=a$ ist bei $b\ge a$ möglich.

Im Einlinienmodell setze $b(\Delta)=b_0/\sqrt{1+(\Delta/\gamma)^2}$ mit Energieverstimmung $\Delta=E-E_0$ und Lorentz-Halbbreite $\gamma$ in Energieeinheiten. Bei über das Fenster konstanten Richtungen, H-Gewinn und direkten geometrischen Faktoren ist das zuschreibbare Halbfenster ohne Übersprechen
$$
|\Delta|\le\gamma\sqrt{(b_0/b_{\mathrm{req}})^2-1},
$$
sofern $b_0\ge b_{\mathrm{req}}$. Bei lediglich beschränktem Übersprechen liefert der Ersatz $t\mapsto t/(1-\delta)$ ein hinreichendes Fenster, sofern der erhöhte Zielwert unter $as$ liegt. Für Senden und Empfangen ist der Schnitt der jeweiligen Fenster relevant. Das Modell verwendet eine isolierte kohärente Lorentz-Linie. Es erfasst keine Doppler- oder Hyperfeinstruktur, Sättigung, Strahlungstransport oder Profiländerungen. Außerdem muss das gemeinsame Fenster oberhalb einer etwaigen J-Ruheenergie liegen.

Für den A/B-Vergleich sei $M_A=LF$ und $P=M_A^{-1}M_B$. Dann gilt $\sigma_{\min}(M_A)\ge\sigma_{\min}(L)\sigma_{\min}(F)$. Bei additiven Matrixfehlern $E_A,E_B$ mit $\|E_X\|_2\le\epsilon_X$ und $\epsilon_A<\sigma_{\min}(M_A)$ erfüllt das gemessene $\widehat P$ die Schranke
$$
\|\widehat P-P\|_2\le
\frac{\epsilon_B+\epsilon_A\|P\|_2}{\sigma_{\min}(M_A)-\epsilon_A}.
$$
Sie folgt aus $\widehat P-P=(M_A+E_A)^{-1}(E_B-E_A P)$. Sie kontrolliert die Matrixrekonstruktion pro Frequenz. Für einen Fehlerbalken auf Eigenphasen oder Laufzeiten braucht es zusätzlich eine ausreichend große Phasentrennung und eine kontrollierte Frequenzauswertung. Profilgebundene Endpunktantworten bleiben Gegenstand der gesonderten A/B-Kontrolle.

## Anhaltspunkt für die Eingangsgrößen

Für den einzelnen polarisierten R(0)-Übergang ist $|d_C|=0{,}0719426\,\mathrm D/\sqrt{3}=0{,}01634155\,e a_0$. In atomaren Einheiten hat H bei unendlicher Kernmasse die statische elektrische Polarisierbarkeit $9/2$. Dazu löst $-(r+r^2/2)\cos\vartheta\,\psi_{1s}$ die erste Störung der Wellenfunktion für den Operator $+z$. Ihr Dipolintegral ergibt $9/2$. Die H-Referenz weicht bei der Linienenergie im verlustfreien Coulomb-Modell um höchstens rund $0{,}125\,\%$ vom statischen Wert ab. [Linienstärke, Tabelle 2](https://doi.org/10.1016/j.jqsrt.2011.03.014) · [CODATA-Einheiten](https://physics.nist.gov/cuu/pdf/RevModPhys.97.025002.pdf)

Für kleine Signale und direkt elektrisch angesprochene Volumina ergibt der resonante Term pro Molekül im Betrag $|d_C|^2/\sqrt{\Delta^2+\gamma^2}$ in konsistenten Einheiten. Der Gegenrotator und die übrigen Übergänge sind als Untergrund weggelassen. Vor Populations- und Geometriefaktoren beträgt das Verhältnis der rein elektrischen HCl- zur H-Polarisierbarkeit etwa
$$
\frac{1{,}61482\times10^{-3}\,\mathrm{eV}}
{\sqrt{\Delta^2+\gamma^2}}.
$$
Für die tatsächliche Anschlussamplitude $b/a$ müssen die effektiven Atom- und Molekülzahlen in den lokalen Moden, die HCl-Besetzungsdifferenz des gewählten Übergangs und die jeweiligen direkten Geometriefaktoren multipliziert werden. Im diagonal-kinetischen Vergleich kommt für die Norm des jeweils abgestrahlten Zweifeldvektors der Faktor $\sqrt{1+r_C^2}/\sqrt{1+r_H^2}$ hinzu, mit $r_i=D_{J,i}/D_{A,i}$. Diese Darstellung fasst Linienbreite, Besetzung und räumliches Übersprechen als unabhängig einzusetzende Parameter. Ihre Werte für eine Apparatur bleiben offen.

Für $K=I$ verwendet die Zahlenschätzung aus der vorigen Notiz $r_H=-0{,}997807(g_J/e)$ und $r_C=1{,}53875(g_J/e)$ oder $-3{,}53491(g_J/e)$ für die beiden Vorzeichen der radialen Matrixelemente. Bei $|g_J/e|=1$ beträgt $s$ rund 0,978 beziehungsweise 0,489. Für einen illustrativen Zielwert $t/a=0{,}1$ wäre dann ohne Übersprechen $b/a\ge0{,}102$ bzw. $0{,}208$ nötig. Bei $|g_J/e|=10^{-3}$ ist bereits die Obergrenze $s$ in beiden Fällen rund $0{,}00254$. Stärkere Resonanz kann hier selbst bei idealer Geometrie keine Mindestantwort von 10 % der H-Referenz erzeugen. Die beiden Kopplungsverhältnisse und die Zielantwort sind Rechenbeispiele. Für ein konkretes Experiment müsste die Schwelle aus Signal- und Rauschkalibrierung folgen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_hcl_anschlusskondition.wl) · [Tatsächliche Print-Ausgabe und Rückgabewert](op5_j_hcl_anschlusskondition.txt) · [Laufmanifest](op5_j_hcl_anschlusskondition.json)

Die symbolische Kontrolle prüft Spur und Determinante bei komplexem Übersprechen, die verschobene Gram-Determinante und die radiale H-Störung. Ein Beispiel mit komplexem Übersprechen überprüft die geschlossene Singulärzahlformel zusätzlich über eine direkte SVD bei 50-stelliger Eingabe. Die Grenzfälle orthogonaler gleichstarker Richtungen, singulären Übersprechens und fehlender zweiter Amplitude sind separat gerechnet. Die Gültigkeit außerhalb der numerischen Beispiele folgt aus den Algebraformeln. Lokal reproduzierbar mit `wolframscript -file op5_j_hcl_anschlusskondition.wl` im Notizordner, ausgeführt wurde der Wolfram-Kernel über den Connector. Qiskit wurde erwogen. Die Rechnung betrifft eine im Allgemeinen verlustbehaftete lineare Antwort, deren unbestimmte Eingangsgrößen durch eine Zustandsvektorschaltung nicht bestimmt werden.

Freie J-Ausbreitung im betrachteten Band, native Kopplung, kohärente experimentelle Anschlussstärken, A/B-Endpunktkontrolle und H96 bleiben offen.
