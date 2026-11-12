# Drei elastische Strings bei fester Gesamtlänge

12.11.2026. Autorenidee aus dem Chat; analytische Erkundung, nicht blind.
Einordnung T8/T13. Zusatzannahmen des folgenden Vergleichsmodells sind
keine nativen Companion-Gesetze. Vorwissen: OP3-Torus-/Gram-/Frame-Notizen,
bekannte Massendreiecksgrenze und inverse Messwertdiagnose; Suchabgleich
in Forschungsnotizen/predictions. Kein neuer H-Test oder Massenfit.

## Präzisierung des Versuchs

Der äußere String hat feste Länge L>0. Die drei inneren Endlängen sind
ell_i≥0 mit sum ell_i=L. Wir behandeln sie zunächst als unabhängig
verteilbare Längen. Ihre Realisierbarkeit durch konkrete Toruswege,
Wicklungen und bewegliche Endpunkte ist eine separate offene Pflicht.
Die Endbedingung wird für die Gleichgewichtsprüfung als Nebenbedingung
benutzt; ein dynamischer Mechanismus, der sie erst erreicht, fehlt.

Zusätzliche Ausleseannahme: sqrt(m_i)=c ell_i, c>0. Deshalb
K=sum ell_i²/L². Die Gleichheit K=2/3 ist das bekannte Ziel, keine
blind getestete Vorhersage.

## Gleiche Strings

Ein einfaches elastisches Vergleichsmodell mit Null-Ruhelänge ist
E=(1/2) sum k_i ell_i², k_i>0. Minimierung unter der Längenbedingung
ergibt k_i ell_i=lambda und damit

ell_i=L (1/k_i)/(sum_j 1/k_j).

Die positive definite Hesse-Matrix diag(k_i) macht diesen inneren
stationären Punkt zum eindeutigen globalen Minimum auf dem Simplex.
Für gleiche k_i gilt ell_i=L/3 und K=1/3. Es gibt in diesem Modell
keine spontane ungleiche Aufteilung. Konstante identische Zugspannung
liefert dagegen E=T sum ell_i=TL und wählt überhaupt keine Aufteilung.

## Exaktes 2/3-Beispiel

Lasse zwei Strings gleiche Steifigkeit k haben und den dritten k/q.
Dann lauten die Längenverhältnisse q:1:1 und

K=(q²+2)/(q+2)².

K=2/3 verlangt q²−8q−2=0. Die positive Lösung ist
q=4+3 sqrt(2), ungefähr 8.24. Somit

ell_1/L=(1+sqrt(2))/3,
ell_2/L=ell_3/L=(2−sqrt(2))/6.

Direkte Kontrolle: Die Anteile summieren sich zu eins und ihre
Quadratsumme ist 2/3. Das Gleichgewicht ist stabil im angegebenen
Längenmodell. Alle drei tatsächlichen Zugkräfte k_i ell_i sind gleich;
die Längen unterscheiden sich wegen der unterschiedlichen Steifigkeiten.
Maximale zulässige Spannungen müssten jeweils mindestens lambda betragen.
Es werden keine Materialwerte oder Maximalspannungen behauptet.

Dies erzeugt zwei gleiche Massen und daher nicht das gemessene
Leptonspektrum. Der benötigte Steifigkeitsfaktor wurde aus dem Ziel
rückgerechnet. Er ist keine Erklärung dafür, warum die Natur 2/3 wählt.

## Was geometrisch dafür aufgegeben werden muss

Jede positive Aufteilung mit K>1/2 hat mindestens einen Anteil größer
als L/2: Andernfalls wäre sum ell_i²≤(L/2)sum ell_i=L²/2.
Damit können die drei Längen nicht die Seiten eines gewöhnlichen
geschlossenen geraden Dreiecks sein. Auch drei kürzeste paarweise
Verbindungen in derselben geodätischen Metrik erfüllen die
Dreiecksungleichung und scheiden aus.

Ein Torusmodell müsste deshalb zusätzliche festgelegte Wege/Wicklungen,
Führungen oder eine andere Netzverknüpfung benutzen. Bloß die Sehnen durch
kürzeste Oberflächenwege zu ersetzen genügt nicht. Die drei Längen als
freie Variablen zu behandeln ist genau die zusätzliche Freiheit dieses
Vergleichsmodells; ein eingebettetes mechanisches Gleichgewicht ist damit
noch nicht bewiesen.

## Ergebnis

Mit ungleichen Elastizitäten lässt sich ein stabiles 2/3-Längengleichgewicht
konstruieren. Identische quadratische Stringenergien liefern 1/3.
Die feste Gesamtlänge allein liefert 2/3 nicht. Nächste konkrete Pflicht
ist eine Netzgeometrie mit festgelegten Wicklungsklassen und unabhängig
begründeten elastischen Eigenschaften; sonst ist der Faktor 4+3sqrt(2)
nur eine andere Schreibweise des eingesetzten Zielwerts.

Keine numerische Rechnung nötig: Lagrange-Bedingung, positive Hesse-Matrix
und Einsetzen der exakten Wurzel sind die vollständige Selbstprüfung.
Keine neuen MMA-Belege, H-/k-Nummern oder Änderungen von OPs/Guards.
Die frühere I1-Stringidee wird durch diesen rein geometrischen Vergleich
nicht als physikalische Mehrsystem-Wirkung aktiviert.
