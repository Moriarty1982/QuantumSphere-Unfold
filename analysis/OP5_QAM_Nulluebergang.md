# OP5 mit QAM: vom Detektor-Null zur exakten Null

Arbeitsstand vom 12. Oktober 2026. Ein eng begrenzter mathematischer Testfall,
keine neue globale Closure-Behauptung und keine erneute MEALS-Bewertung.

## Ergebnis

Die im Companion angegebene skalare C5-Folge erreicht bei Schritt 20 die
Detektorschwelle, aber keine exakte Null. Der QAM-Readout kann diesen Unterschied
explizit speichern. Die Gleichheit zweier Detektorwerte liefert nach den
vorhandenen QAM-Regeln keine Closure-Klassen-Gleichheit ihrer Ausgangszustaende.

Der fehlende Schritt ist eine **Null-Reflexion auf einer konkret bestimmten
Zustandsmenge**. Fuer den unveraenderten Schwellen-Readout und einen Zielbegriff,
der Phi = 0 verlangt, ist diese Reflexion auf der endlichen C5-Folge sogar falsch.
Ein weiterer endlicher Kontraktionsschritt kann das nicht reparieren.

## Quellen und Reichweite

Gelesene Basis:
`Quantum_Sphaera_Companion_v4_7_0_source (1) (1).tex`
(lokale v4.7.0-Quellkopie; identifiziert durch den folgenden SHA256).

SHA256: `019E7A35ADB3E299B1EED7E5310397D922D18575FE8A5122C3B448CF1A383329`.

Die folgenden Zeilenangaben beziehen sich auf diese Quelldatei:

| Grundlage | Fundstelle |
| --- | --- |
| Primitive QAM-Praedikate und getaggte Codes | ab Zeile 2837 |
| QAM admissible transport | ab Zeile 2936 |
| QAM-coded readout und closure-compatible readout | ab Zeile 2996 bzw. 3012 |
| Prospective kernel bridge datum | ab Zeile 2710; Label `def:qam-kernel-bridge-datum` |
| MML-Instruktionen und MMA-Zertifikatsregister | ab Zeile 13729 |
| Endlich positive C5-Folge | r11, Label `lem:v470-r11-finite-positive-guard` |
| C5-Abschluss am Punkt infinity | r13, Label `def:v470-r13-bounded-collar-completion-topology` |
| Komprimierter Endpunkt r55--r80 | ab Zeile 62649 |
| Effektives Detektor-Null und Status-Reklassifikation | r81--r84, ab Zeile 62706 |

Die lokalen Repository-Quellen stammen laut `sources/README.md` aus einer
v3.35.0-Synchronisierung. Diese Notiz behandelt deshalb die externe v4.7.0-Basis
und wird nicht ungeprueft in den aelteren aktiven LaTeX-Kern eingebaut.
Die Aussagen der Quelle werden hier als Forschungsinhalt untersucht.

OP5 wird nur ueber seinen dokumentierten skalaren C5-/Detektor-Testfall betrachtet.
Dieser Test ist kein Ersatz fuer die gesamte OP5-Architektur. Die Rekurrenz wird
aus dem Text uebernommen; ihre Ableitung aus konkreten MM/HC-Operatoren wird in
dieser Notiz nicht bewiesen. Der komprimierte r55--r80-Block verweist fuer seine
Detailbeweise auf einen separaten Quellbestand, der hier nicht geprueft wurde.

## 1. QAM-Objekte und explizite Bedeutungen

Wir verwenden die vorhandenen Tags, ohne einen zweiten QAM-Kalkuel einzufuehren.
Alle Graphen unten bestehen aus Paaren von Codes; Observable sind als
ZF-codierbare Daten dargestellt.

| Rolle | QAM-Code | Bedeutung im Testfall |
| --- | --- | --- |
| Lokale Zustandsmenge | L = <1, ell, S> | S enthaelt die getaggten endlichen Collar-Zustaende |
| Zustand | s_n = <0, a_n> | a_n = (ell, n, Phi_n, gamma_n); gamma_n speichert die lokalen Guards |
| Rekurrenzoperator | o_T = <2, ell, ell, G_T> | G_T enthaelt (s_n, s_(n+1)) mit Phi_(n+1) = 3 Phi_n / 4 |
| Detektor-Readout | r_theta = <3, ell, W_det, R_theta> | R_theta liest den Schwellenstatus aus |
| Exakter skalarer Readout | r_Phi = <3, ell, W_Phi, R_Phi> | R_Phi liest Phi_n ohne Schwellenbildung aus |
| Witness-Code | w = <6, u> | u speichert Aussage, Voraussetzungen und Begruendung |

Die Zusatzdaten im Payload sind eine Instanziierung der vorhandenen State-Codes.
Sie werden nicht als bereits im Companion vorhandene neue Definition ausgegeben.
Ein Tag `QWitness(w)` erkennt nur den Objekttyp; die Wahrheit der gespeicherten
Aussage braucht weiterhin einen Beweis.

Die C5-Daten des Textes sind

\[
\Phi_0=1,\qquad \Phi_{n+1}=\frac34\Phi_n,
\qquad \Phi_n=\left(\frac34\right)^n,\qquad \theta=\frac1{256}.
\]

Fuer diesen Test instanziieren wir den Schwellen-Readout vollstaendig:

\[
D_\theta(x)=
\begin{cases}
0_{\rm det},&0\le x\le\theta,\\
1_{\rm det},&x>\theta.
\end{cases}
\]

Die Binaercodierung oberhalb der Schwelle ist nur eine minimale Modellwahl.
Fuer den Null-Uebergang wird ausschliesslich die untere Nullfaser benutzt.

## 2. Zulassige Schritte und ihr tatsaechlicher Ertrag

1. **Rekurrenz auswerten.** Der Graph G_T berechnet s_(n+1) aus s_n, soweit
   Payload und Guards definiert sind. Damit ist er ein funktionaler QOp-Graph.
   `QAdmTransport(o_T,s_n,s_(n+1))` folgt daraus allein noch nicht: Die native
   Closure-Klassen-Erhaltung muss separat nachgewiesen werden.
2. **Detektor lesen.** `QRead(r_theta,s_n,D_theta(Phi_n))` folgt aus dem
   expliziten Readout-Graphen. Dies ist ein Observable und kein neuer Zustand
   derselben Closure-Klasse.
3. **Schritt 20 zertifizieren.** Die genaue Rechnung liefert
   `0 < Phi_20 <= theta`. Deshalb darf das Zertifikatsregister einen lokalen
   Schwellen-Witness aufnehmen.
4. **Terminaldaten zurueckgeben.** Der Witness traegt den Scope
   `local/collar/detector`; ein globales Zertifikat wird nicht erzeugt.
5. **Exakte Null anfordern.** Eine Behauptung `Phi_20 = 0` wird durch den
   exakten Readout widerlegt. Eine weitergehende globale Closure-Aussage
   braucht zusaetzlich ihre eigene native Definition und einen Bridge-Witness.

Diese Liste ist ein Auswertungsprotokoll in der vorhandenen Objekt- und
Zertifikatsdisziplin. Sie wird nicht als bereits bewiesenes Programm des
speziellen MML-HC/OP-Instruktionsalphabets ausgegeben: Fuer eine solche
Einbettung muessten dessen konkrete Eingabe- und Ausgabetypen nachgewiesen werden.

## 3. Exakter Gegenbeleg zur direkten Null-Promotion

Mit ganzzahliger Arithmetik erhalten wir:

\[
\Phi_{19}=\frac{1162261467}{274877906944}>\frac1{256},
\qquad
0<\Phi_{20}=\frac{3486784401}{1099511627776}<\frac1{256}.
\]

Die Folge ist streng fallend. Schritt 20 ist daher der erste endliche Schritt
mit Detektor-Null. Zugleich gilt fuer jedes endliche n: Phi_n > 0.

Schon auf dem skalaren Testtraeger gilt

\[
D_\theta(0)=D_\theta(\Phi_{20})=0_{\rm det},
\qquad 0\ne\Phi_{20}.
\]

Die Nullfaser ist das ganze Intervall [0, theta], nicht nur {0}. Deshalb gibt
es keine Rekonstruktion des exakten Skalarwerts aus dem Detektorwert, die auf
diesem Intervall gleichzeitig 0 und Phi_20 korrekt zurueckliefert.
Dies widerlegt die allgemeine Regel `Detektor-Null => exakte skalare Null`.
Es ist kein Gegenbeweis gegen jede moegliche globale Theorie des Companion.

## 4. Die QAM-Regel hat eine Richtung

Der vorhandene Kalkuel verlangt

\[
\operatorname{QAdmTransport}(o,s,t)
\Longrightarrow \operatorname{QClEq}(s,t).
\]

Bei einem closure-compatible Readout folgt daraus nur

\[
\operatorname{QClEq}(s,t)
\Longrightarrow J_r(w_s)=J_r(w_t).
\]

Die Umkehrung ist nicht Bestandteil dieser Definition. Weder gleiche rohe
Readouts noch gleiche J_r-Bilder beweisen QClEq. Insbesondere kann eine
Faktorisierung Information verlieren; eine konstante J_r-Abbildung erfuellt
die Kompatibilitaetsbedingung sogar ohne Trennleistung.

Auch die im Kernel-Bridge-Datum so bezeichnete closure reflection hat die
Richtung `QClEq => gleiche Kernel-Normalform`. Sie liefert ohne weiteren Satz
keine Rueckrichtung von gleichem Detektorwert zu QClEq oder physikalischer Null.

Ein reines Schwellenmodell koennte eine Detektor-Aequivalenz definieren.
Diese waere eine andere Relation als die nachzuweisende native Closure-Klasse.
Ausserdem erhaelt die Kontraktion selbst diese Detektor-Aequivalenz nicht auf
dem ganzen skalaren Traeger: x=theta+theta/4 und y=2 theta sind beide oberhalb
der Schwelle; 3x/4 ist darunter, 3y/4 bleibt darueber. Eine Quotienten-Dynamik
benoetigt daher ebenfalls einen Wohl-definiertheitsbeweis.

## 5. Praezise Form des fehlenden Bridge-Satzes

Sei A eine konkret angegebene Menge zulaessiger QAM-Zustaende. Sei Z_exact(s)
eine unabhaengig definierte native Zielaussage, etwa `Phi(s)=0` fuer den
skalaren Test. Dann ist die gewuenschte Detektor-Promotion genau die Bedingung

\[
\{s\in A:D_\theta(\Phi(s))=0_{\rm det}\}
\subseteq
\{s\in A:Z_{\rm exact}(s)\}.
\]

Das ist die notwendige und hinreichende Null-Reflexion auf A; ein Beweis muss
die linke Menge und den unabhaengigen Zielbegriff tatsaechlich untersuchen.
Fuer A mit s_20 und Z_exact(s) := [Phi(s)=0] scheitert sie am Gegenbeleg oben.

Eine staerkere, hinreichende QAM-Bridge haette folgende getrennte Lasten:

1. Ein Referenzzustand z ist nativ als exakt geschlossen bewiesen.
2. Gleiche Null-Readout-Bilder implizieren auf A tatsaechlich QClEq(s,z).
3. QClEq erhaelt den unabhaengigen exakten Zielbegriff.
4. Falls der Zielbegriff global/all-readout ist, sind Zustandsbereich,
   Readout-Abdeckung und deren Transport ebenfalls bewiesen.

Dann folgt Z_exact(s) durch 2 und 3 aus 1. Die Schwierigkeit liegt in diesen
Voraussetzungen, nicht im letzten logischen Schritt. Sie duerfen nicht durch
Definition von QClEq oder Z_exact aus dem Detektorstatus vorweggenommen werden.

## 6. Zwei tragfaehige Fortsetzungen

**Effektive OP5-Linie.** Der bereits erreichte Satz lautet

\[
n\ge20\Longrightarrow D_{1/256}(\Phi_n)=0_{\rm det}.
\]

Er ist exakt als Schwellen-Aussage und lokal im Scope. Das offene Arbeitsziel
ist seine Bindung an die nativen OP5-Objekte: Welcher MM/HC-Zustand erzeugt Phi,
welcher Operator realisiert die Rekurrenz, und welche Guards bleiben dabei
erhalten? Diese Bindung ist mehr als eine weitere Status-Reklassifikation.

**Abschluss-Linie.** r13 definiert bereits den skalaren Abschlusswert
`widehat(Phi)(infinity)=0`. Fuer einen Abschluss des nativen Zustands braucht
man jedoch eine Topologie fuer s_n, einen zulaessigen Grenzzustand s_infinity,
Konvergenz s_n -> s_infinity und eine geeignete stetige Restfunktion.
Wenn deren Nullmenge exakt lokale Closure charakterisiert, folgt daraus lokale
Closure am Grenzzustand. Globale Closure verlangt darueber hinaus einen
separaten Nachweis fuer die gesamte beanspruchte Readout-Familie.
Ein skalarer Grenzwert allein stellt diese Daten nicht bereit.

Eine dritte Moeglichkeit, endliche exakte Null, braucht einen anderen
mathematischen Mechanismus als die unveraenderte positive 3/4-Kontraktion.
Schwellenbildung oder die Benennung einer neuen Nullklasse leisten das nicht.

## Naechster konkreter Arbeitsschritt

Fortsetzung ausgearbeitet in
[OP5_QAM_Zustand_Operator.md](OP5_QAM_Zustand_Operator.md), mit eigenstaendiger
LaTeX-Arbeitsfassung [OP5_QAM_Residual_Lift.tex](OP5_QAM_Residual_Lift.tex).
Sie fuehrt den Score auf die r04-Restnormen zurueck, beweist den bedingten
Witness-Lift und trennt das berechenbare Restmodell vom noch offenen nativen
MM/HC-Operator.

Zuerst den nativen OP5-Zustand und seine Restfunktion Phi ausdruecklich in
QState/QOp/QReadout uebertragen und die Rekurrenz samt Guard-Erhaltung daran
beweisen. Dann entscheiden, ob das Forschungsziel effektive Closure oder ein
nativer Grenzzustand ist. Die Null-Promotion bleibt bis zu einem passenden
Bridge-Witness gesperrt; der bereits vorhandene lokale Schwellen-Witness bleibt
als eigenstaendiges positives Ergebnis erhalten.

## Pruefung

Die Werte fuer n=19 und n=20 sowie ihr Vergleich mit 1/256 wurden am
12. Oktober 2026 mit beliebig grossen Ganzzahlen nachgerechnet, ohne
Gleitkomma-Rundung. Die Aussagen fuer alle endlichen n folgen aus Positivitaet
und strenger Monotonie der geometrischen Folge. Die Modell-Gegenbelege zeigen
die Informationsverluste der Schwellenbildung; die native MM/HC-Rekurrenz und
eine globale Bridge sind damit nicht verifiziert.
