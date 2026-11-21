# OP5 – Passive Lasten, Dispersionsauflösung und Krümmungsschwellen

21. November 2026. Analytische Erkundungen im Materieframe M. Die [Last- und Phasenrechnung](OP5_J_Lastvariation_Laufphase.md) liefert das Dreieck der Rücklaufamplituden, den Phasenanker und den gemeinsamen minimalen Hauptteil. Hier werden erreichbare Lasten, die zum Dispersionsvergleich nötige Auflösung und die Nichtproportionalität der [Dirac-Schwellenmatrix](OP5_J_Dirac_Schwellenabgleich.md) geprüft. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 erfordert eine eigenständige kosmologische Bestandsdynamik.

## Erreichbare Rückwellen mit passiven Lasten

Am rechten Referenzport sei $u$ die auslaufende Welle bei abgeglichener Last, $R$ der Reflexionsblock des Markers und $\Gamma$ die Lastmatrix. Die Rückwelle erfüllt $x=\Gamma(u+Rx)$. Bei $\|R\|\le r<1$ und passiver Last $\|\Gamma\|\le1$ ist die Lösung eindeutig und $\|x\|\le\|u\|/(1-r)$. Für einen vorgegebenen Zielvektor $x$ setze $v=u+Rx$.

- Bei beliebiger modenumwandelnder passiver Last ist die notwendige und hinreichende Bedingung $\|x\|\le\|v\|$. Für $v\ne0$ realisiert die Rang-eins-Abbildung $\Gamma=xv^\dagger/\|v\|^2$ den Zielvektor als Kontraktion. Für $v=0$ bleibt nur $x=0$. Die Konstruktion garantiert Passivität auf Ebene der Streumatrix. Physische Realisierbarkeit, Reziprozität und Bandabgleich sind weitere Eigenschaften.
- Bei einer diagonal wirkenden Last gilt stattdessen komponentenweise $|x_i|\le|v_i|$. Insbesondere folgt $|x_J|\le |u_J|+r\|u\|/(1-r)$. Am abgeglichenen Port lautet der differentielle Zusammenhang $dx=d\Gamma\,u$. Diagonale Lasten können dort nur Moden variieren, die in $u$ vorhanden sind. Ein unabhängiger Mischkoeffizient der Last kann dagegen auch einen J-Anteil aus $u_A$ erzeugen.

Im bisherigen homogenen Vergleich verwende am rechten Port dieselben Reflexionsgrenzen wie links, $r\le3{,}512\cdot10^{-6}$, und $|u_J|\le0{,}00317$, $\|u\|\le1$. Dann kann eine diagonale Last höchstens $|x_J|<0{,}003174$ liefern. Für das frühere gleichseitige Dreieck mit Radius $0{,}02$ wären $|x_J|\simeq0{,}01732$ erforderlich. Diese konkrete Lastgeometrie scheidet ohne Mischung aus. Ein schmales affines Dreieck bleibt möglich, falls $u_J$ und die erreichbaren Stellungen separat belegt sind. Für Achsenskalierungen $a_A=0{,}02$, $a_J=0{,}003$ und denselben Vorwärtsfehlern von $10^{-8}$ liefert die vorangegangene Konditionsrechnung einen Interzeptfehler unter $2{,}001\cdot10^{-8}$. Das ist ein bedingtes Rechenbeispiel für gemessene Zielpunkte.

Für beliebige passive Mischung liegt der gesamte Ball $\|x\|\le\|u\|/(1+r)$ in der theoretisch erreichbaren Menge, weil $\|v\|\ge\|u\|-r\|x\|$. Kommt der benötigte Modenumwandler als Last nicht infrage, kann eine kalibrierte kohärente Einspeisung von rechts dieselben Zielpunkte an der Portebene herstellen. In beiden Fällen muss die A/J-Portkondition unabhängig belegt werden.

## Auflösung und Phasenanker für J

Sei $g(E)=k_J-k_A$ und $\delta=2\arcsin(10^{-4})+2\cdot10^{-6}$ rad der illustrative Fehler einer entfalteten differentiellen Phase pro Frequenz. Über den Abstand $d$ erzeugt der massive Vergleich zwischen den Bandenden den Betrag $S=d|g(E_+)-g(E_-)|$. Die beiden Phasenfehler summieren sich auf $2\delta$. Ein am Modellwert zentrierter Messbefund könnte einen konstanten Wellenzahlversatz bei $S>2\delta$ ausschließen. Die Fehlerintervalle beider Modelle sind unabhängig von der Fehlerrealisierung bei $S>4\delta$ getrennt.

| Vergleich bei unverändertem Fehler | Zentrierter Messbefund | Garantiert getrennte Fehlerintervalle |
| --- | ---: | ---: |
| Nötige freie Basis bei 100 MHz | rund $1{,}92743$ m | rund $3{,}85486$ m |
| Nötige Bandbreite bei 1 cm | rund $19{,}2743$ GHz | rund $38{,}5486$ GHz |

Der frühere 1-cm-Phasenanker hat eine Wellenzahlunsicherheit von etwa $0{,}0202\ {\rm m}^{-1}$. Für einen weiteren Abstand von 4 m ist $dW+\delta\simeq0{,}081<\pi$, sodass derselbe Anker den Zweig weiterhin eindeutig auswählt. Die Rechnung trennt den Phasenzweig von der Fehlerauflösung. Für eine 4-m-Strecke sind die angenommenen komplexen Fehlerschranken, Mehrwegkontrolle und kohärente J/A-Referenz noch nachzuweisen. Die breitere Frequenzvariante setzt dieselbe Portkalibrierung über das neue Band voraus.

## Nichtproportionalität der Krümmungsschwelle

Für schwere, lokal integrierbare Dirac-Arten mit reellen Vektorladungen setze $G=\sum_i w_iq_iq_i^{\mathsf T}$, $w_i=n_i/m_i^2>0$, mit $q_i=(q_{A,i},q_{J,i})$. Relativ zur positiv definiten flachen Kinetik $K$ ist die Nichtproportionalität äquivalent zu
$$
[\operatorname{tr}(K^{-1}G)]^2-4\det(K^{-1}G)>0.
$$
Das ist dieselbe basisunabhängige Eigenwertlücke wie in der Kinetikprüfung. Sie kennzeichnet den Matrixfaktor der Schwelle. Eine Laufphase braucht zusätzlich eine wirksame Krümmungsprojektion und zugängliche Moden.

Ein einzelner geladener Elektronbeitrag mit $q_e=(-e,g_J)$ hat Rang eins und kann zu keinem positiv definiten $K$ proportional sein. Für Elektron und eine lokal integrierbare neutrale Art $q_\nu=(0,g_J)$ wäre Proportionalität nur möglich bei
$$
K_{AJ}/K_{AA}=-g_J/e,\qquad
K_{JJ}/K_{AA}=(g_J/e)^2(1+w_\nu/w_e).
$$
Für diagonales $K$ und $g_J\ne0$ ist diese Zweiergruppe folglich nichtproportional. Für die vollständige Summe reicht das Rang-eins-Argument allein nicht. Ein formaler Vergleich gleich gewichteter EW-Arten pro Farbfreiheitsgrad mit $u,d,\nu,e$ und $g_J/e=1/\sqrt3$ ergibt relativ zu $K=I$ eine proportionale Matrix. Das ist ein algebraisches Gegenbeispiel zur Verallgemeinerung, keine physische Schwellenrechnung.

Eine hinreichende robuste Grenze folgt nach Normierung mit $K$. Der Elektronenanteil habe die Eigenwertlücke $s>0$. Liegt der zusätzliche normierte Beitrag in Operatornorm höchstens $\varepsilon$ von einem beliebigen skalaren Vielfachen der Identität entfernt, bleibt die gesamte Eigenwertlücke mindestens $s-2\varepsilon$. Positivität der zusätzlichen Beiträge allein liefert diese Kontrolle nicht.

Die W1/W2-Dirac-Lesart sichert im Modell die gemeinsame J-Ladung der aufgeführten Teilchen und das J-neutrale Higgs. Die elektrischen Ladungen gehören zur zusätzlichen EW-Referenz. [J-Eichkanal](W2_J_Eichkanal.md) · [Neutralströme](W2_Neutralstroeme.md) Für die native Gesamtsumme fehlen die physische A/J-Kinetik, die schweren Zustände samt Kopplung an den Vermittler und die gültige Schwellenbeschreibung. Eine zu leichte Art gehört nicht in die lokale Schweremassenentwicklung. Konfinierte Quarks dürfen für den betrachteten niederenergetischen Kanal nicht als freie Schwellen addiert werden. Die freie J-Ausbreitung und die native Krümmungskopplung bleiben offen.

## Rechenkontrolle

Wolfram prüfte die passive Zielabbildung, die Lastgrenzen, die beiden Dispersionsschwellen, den 4-m-Phasenanker, die Rang-eins-Schwelle, die Zweier-Ausrichtung und das proportionale Gegenbeispiel. Qiskit wurde erwogen. Die Prüfung betrifft klassische Streumatrizen, Phasen und lokale effektive Koeffizienten.

[Wolfram-Skript](op5_j_passive_last_dispersion.wl) · [Tatsächliche Ausgabe](op5_j_passive_last_dispersion.txt) · [Laufmanifest](op5_j_passive_last_dispersion.json)
