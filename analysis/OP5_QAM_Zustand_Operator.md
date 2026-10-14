# OP5: QAM-Zustand, Restoperator und Guard-Erhaltung

Arbeitsstand vom 12. Oktober 2026. Fortsetzung von
[OP5_QAM_Nulluebergang.md](OP5_QAM_Nulluebergang.md).
Gleiche v4.7.0-Quellbasis und gleicher SHA256 wie dort.

## Befund an der nativen Schnittstelle

Die Herkunft des C5-Tests ist jetzt bis r02--r09 zurueckverfolgt:

| Quellblock / Label | Inhalt | Noch zu konkretisieren |
| --- | --- | --- |
| r02, `def:v470-r02-extmix-candidate` | C5 als MM/HC-Fit-Term mit Links-/Rechts-Typ und fuenf Residualslots | Auswertung dieser Slots aus einem Witness |
| r04, `def:v470-r04-c5-lowering-score` | Phi als Summe dreier quadrierter Restnormen | Normraeume, Normalisierung und konkrete Restfunktionen |
| r04/r05, finite witness ledger | Werte 1, 3/4, 9/16 mit Guard-Eintraegen | Konstruktion der Witness-Pakete und ihrer Guard-Auswertung |
| r08, `def:v470-r08-c5-update-candidate` | Scalar update Phi -> 3 Phi / 4 | Lift auf den Witness und seine Restobjekte |
| r09, `def:v470-r09-bounded-c5-operator-domain` | deklarierter bounded collar domain | Mengen- und Typdefinition sowie Invarianz unter dem Lift |
| r09, `lem:v470-r09-c5-finite-stage-admissibility` | beanspruchte Wiederholbarkeit | Zustandsabbildung, die Leakage-/Scope-Pruefung wirklich erhaelt |

Die r09-Formulierung beschreibt den Definitionsbereich zunaechst als Menge
von Stufen n, setzt dann aber Phi_n in diesen Bereich ein. Die folgende
Formalisierung trennt Stufen, Witness-Zustaende und skalare Readouts.

Ein kleinerer Score beweist nicht, dass ein aktualisierter Witness im selben
zulaessigen Bereich liegt. Die bisherige Begruendung von r09 ist fuer einen
nativen Zustandsoperator deshalb ergaenzungsbeduerftig. Das arithmetische
Induktionsargument ist korrekt, sobald dieser Operator und seine Invarianz
vorliegen.

## 1. Native Daten und QAM-Codes

Sei W eine explizit festzulegende Menge von lokalen C5-Witness-Paketen.
Wir verlangen definierte Restfunktionen

\[
\rho_{\rm bd}:W\to H_{\rm bd},\quad
\rho_{\rm ext}:W\to H_{\rm ext},\quad
\rho_{\rm mix}:W\to H_{\rm mix},
\]

in normierten Raeumen und setzen

\[
R(w)=(\rho_{\rm bd}(w),\rho_{\rm ext}(w),\rho_{\rm mix}(w)),\qquad
\Phi(w)=\|R(w)\|_\oplus^2
=\sum_j\|\rho_j(w)\|^2.
\]

Dies instanziiert die Form des r04-Scores. Alle Summanden werden als
dimensionslos normalisiert vorausgesetzt. Eine positiv definite Norm ist
notwendig; eine unbestimmte physikalische Metrik waere kein Ersatz dafuer.

Das r02-Paket hat ausserdem die Slots rho_leak und rho_fit. Diese werden im
State-Payload mitgefuehrt, aber nicht stillschweigend dem dreiteiligen r04-Score
gleichgesetzt. Eine Identifikation oder Eliminierung braucht einen eigenen
Nachweis.

Sei K4 der jeweils festgehaltene C4-Status und K6 der festgehaltene C6-Blocker.
Ein Witness-Zustand hat die Daten

\[
x=(w,K4,K6,\sigma^L,\sigma^R,\rho_{\rm leak},\rho_{\rm fit},\text{scope}).
\]

Der QAM-Code ist s_x=<0,x>. Sein Layer-Code ist <1,ell,S_A>, wobei
S_A={s_x:x in A} die Codes der unabhaengig definierten zulaessigen Menge A sind.
Die Stufennummer n gehoert zur Laufhistorie und darf nicht mit dem Witness oder
dem Score verwechselt werden.

Ein normativer Guard wird getrennt vom gespeicherten Guardbericht geprueft.
Wir verwenden gemeinsam die Pruefungen aus r04 und r05:

\[
g(x)=(\Lambda_5^{\rm new}(x),A_4^{\rm abs}(x),
L_4^{\rm new}(x),U_6^{\rm all}(x)).
\]

Falls eine Pruefung von Vor- und Nachzustand abhaengt, ist sie als g(x,Fx)
zu definieren. In A sind die erforderlichen Pruefungen Null; das ist eine
Eigenschaft der ausgewerteten Objekte, keine frei beschreibbare Flag-Liste.

## 2. Bedingter nativer Lift-Satz

**Voraussetzungen.** Eine konkrete Witness-Abbildung F:A -> A und eine
Restabbildung T auf dem direkten Summenraum sind gegeben. Es ist bewiesen:

\[
R(Fx)=T R(x),\qquad
\|T R(x)\|_\oplus^2=\tfrac34\|R(x)\|_\oplus^2.
\]

Hier bedeutet R(x) die Auswertung am Witness w des Zustands x. Ausserdem
bleiben K4, K6, Sidedness und Scope unter F erhalten, und die echten
Leakage-/Absorptionspruefungen sind nach dem Schritt weiterhin Null.
Diese Aussagen muessen aus der Definition von F bewiesen werden.

**Folgerung.** Fuer x_0 in A mit Phi(x_0)=1 ist x_n=F^n(x_0) fuer jedes
endliche n definiert und zulaessig. Es gilt

\[
\Phi(x_n)=(3/4)^n,
\qquad g(x_n)=0,
\qquad K4(x_n)=K4(x_0),\quad K6(x_n)=K6(x_0).
\]

**Beweis.** F:A -> A liefert die Invarianz und Iterierbarkeit. Die
Kommutationsgleichung R(Fx)=TR(x) und die Normgleichung liefern die
Score-Rekurrenz. Induktion liefert die geschlossene Formel. Die nachgewiesene
Erhaltung der Guard-Pruefungen und Ledgerkoordinaten wird ebenfalls induktiv
fortgesetzt. Kein Schritt setzt eine positive Restnorm gleich Null.

Bei lediglich `||TR(x)||^2 <= 3 Phi(x)/4` folgt nur eine obere Schranke.
Eine solche Variante liefert ab Schritt 20 ebenfalls Schwellenkleinheit,
aber keine Positivitaet aller endlichen Reste: T koennte eine Nullrichtung haben.

## 3. Uebertragung in QAM ohne zirkulaere Zulassung

Mit dem bewiesenen F ist

\[
o_F=\langle2,\ell,\ell,G_F\rangle,\qquad
G_F=\{(s_x,s_{Fx}):x\in A\}
\]

ein funktionaler QOp-Graph. Der exakte und der Detektor-Readout lauten

\[
r_\Phi=\langle3,\ell,\mathbb R_{\ge0},
\{(s_x,\Phi(x)):x\in A\}\rangle,
\]

\[
r_\theta=\langle3,\ell,\{0_{\rm det},1_{\rm det}\},
\{(s_x,D_\theta(\Phi(x))):x\in A\}\rangle.
\]

Alle Zielwerte sind als ZF-Daten codiert zu verstehen. Die Graphen erfuellen
QOp beziehungsweise QReadout und die entsprechenden QRead-Aussagen.

Fuer QAdmTransport fehlt daneben ein unabhaengiger nativer Satz:
F erhaelt die im Companion gemeinte Closure-Klasse. Falls C(x) diese Klasse
bezeichnet, muss C(Fx)=C(x) bewiesen sein und die Uebersetzung muss
`C(x)=C(y) => QClEq(s_x,s_y)` legitimieren. Dann erst ist o_F als
QAdmTransport einsetzbar. Guard-Erhaltung allein ersetzt diesen Satz nicht.

Phi und D_theta(Phi) muessen fuer die blosse Auswertung nicht
closure-compatible sein. Ob sie ueber ein J durch die native Klasse
faktorisieren, ist eine weitere getrennte Frage. Exakte Restgroesse kann sich
unter einem Closure-Klassen-erhaltenden Operator durchaus aendern.

## 4. Vollstaendig berechenbarer Residual-Lift

Ein konkretes Modell fuer die verlangte Score-Rekurrenz ist

\[
E=\mathbb R^3,\qquad
T=\frac{\sqrt3}{2}I,\qquad
R_0=(1,0,0),\qquad
R_n=T^nR_0.
\]

Dann gilt exakt

\[
\|TR\|^2=\tfrac34\|R\|^2,
\qquad \|R_n\|^2=(3/4)^n.
\]

Der Faktor sqrt(3)/2 auf den Restobjekten ist wesentlich: Multiplikation der
Reste selbst mit 3/4 wuerde den quadrierten Score mit 9/16 multiplizieren.

Auf dem Einheitsball E_1 ist T invariant, da ||TR|| <= ||R|| <= 1.
Ein Modellzustand besteht aus R und festgehaltenen Ledger-/Scope-Daten;
F_mod skaliert nur R. Seine Projektionen auf K4, K6 und Scope bleiben exakt
unveraendert. Das beweist Erhaltung dieser **Modellregister**. Es beweist nicht
die Abwesenheit physikalischer Leakage in einem noch unbekannten MM/HC-Lift.

Dieses Modell realisiert die Rekurrenz auf Restobjekten. Seine Gleichsetzung
mit den nativen Witness-Funktionen R(w) ist ausdruecklich offen.
Eine Beispiel-Klasse im Modell koennte durch die Rest-Richtung fuer R != 0
und eine separate Nullklasse definiert werden; T erhaelt diese Klassen.
Das ist eine konsistente Illustration, keine neue Definition der nativen
QClEq-Relation des Companion.

## 5. Warum Score-Kontraktion den Bereich nicht alleine erhaelt

Gegenmodell: E=R^2, A ist der Abschnitt der x-Achse im Einheitsball, und
T=sqrt(3)/2 mal einer Drehung um 90 Grad. Es gilt fuer jedes R die richtige
Normrekurrenz. Trotzdem liegt T(1,0)=(0,sqrt(3)/2) nicht in A.

Damit ist die Schlussregel `Score wird kleiner => Witness bleibt zulaessig`
ohne einen Invarianzbeweis falsch. Guards, die von Richtung, Sidedness oder
Operator-Kommutatoren abhaengen, koennen durch eine Normschranke allein
nicht kontrolliert werden.

## 6. Detektorschwelle und Abschluss im Restmodell

Bei n=20 gilt ||R_20||^2 <= 1/256, also ||R_20|| <= 1/16.
Der Score-Schwellwert 1/256 ist deshalb nicht derselbe wie der
Restnorm-Schwellwert 1/16. Fuer alle endlichen n ist R_n != 0.

Im vollstaendigen Raum R^3 konvergiert R_n gegen R_infinity=0.
Der lokale Modellabschluss ist damit ein wirklicher Grenzzustand und nicht
nur ein nachtraeglich angehaengter skalarer Nullwert. Der exakte
Rest-Readout ist stetig. Der Schwellen-Readout ist am Grenzpunkt ebenfalls
stetig, wenn sein Ziel diskret ist, da eine Umgebung von Null konstant Null
liest; an der Schwelle selbst ist er unstetig.

Ob die native Witness-Menge einen entsprechenden Grenzzustand enthaelt,
ob ihre Guards grenzwertstabil sind und ob dort die native Closure gilt,
ist durch dieses Modell nicht entschieden. C6/all-readout bleibt separat.

## 7. Konkreter Anschluss an das Paper

Die naechste native Aufgabe ist jetzt genau spezifiziert:

1. Den Witness W und die drei r04-Restfunktionen aus den MM/HC-Fit-Objekten
   definieren; die beiden weiteren r02-Slots separat erklaeren.
2. Einen Witness-Operator F angeben und R(Fw)=TR(w) beweisen. Ein reiner
   Tabellenwert oder ein Operator auf Phi reicht dafuer nicht.
3. Den bounded collar als Zustandsmenge definieren und F(A) subset A mit den
   echten Guard-Pruefungen zeigen.
4. Native Closure-Klassen-Erhaltung separat nachweisen, dann QAdmTransport
   einsetzen und den lokalen Schwellen-Witness in QAM speichern.

Die bedingte Rekurrenz ist nun formal durchgearbeitet; ein expliziter nativer
MM/HC-Witness-Operator ist in den untersuchten r02--r09-Definitionen noch nicht
auskonstruiert. Der positive Ertrag ist ein pruefbarer Lift-Vertrag mit einem
vollstaendig berechenbaren Restmodell und einem Gegenbeleg gegen die bislang
zu kurze Invarianzbegruendung.

## Verifikation

Eine beigefuegte eigenstaendige LaTeX-Notiz stellt den Lift-Satz und das
Restmodell als zitierbare Arbeitsfassung dar. Die ganzzahligen Scorewerte
und ihre Schwellenvergleiche sind unveraendert; die zusaetzlichen Modell-
Identitaeten folgen aus T^*T=3I/4. Keine dieser Pruefungen verifiziert die
noch offene native Witness-Abbildung.
