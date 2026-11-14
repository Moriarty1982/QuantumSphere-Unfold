# OP3: Herkunft der Slot-Fourier-Operation – eine engere notwendige Bedingung

14. November 2026, Codex. Analytische Erkundung, nicht blind; Anschluss an
`op3_slot_fourier_2t_2026_11_14.md`. Einordnung T5/T7/T8, OP3.
Keine H-/k-Nummer, kein neuer MMA-Beleg, keine Änderung von OPs oder Guards.
Das bekannte Ziel wird nicht als Vorhersage behandelt.

## Vorwissen geprüft und Suchrichtung

Gelesen: aktuelle Übergabe nach PR #122, Gesamtbild nach r13,
`op3_triality_carrier_gate_2026_11_12.md`,
`op3_tau_doublet_axis_2026_11_14.md` und die Fourier-Erkundung vom 14.11.
Die Suchabgleiche in Forschungsnotizen, predictions, v4_10_0-Runden und
analysis betreffen Fourier, Heisenberg, Slotposition/-phase und nichtmonomiale
Operationen. Die vorhandene Fourier-Erkundung benennt F ausdrücklich als
Annahme; die Trägerprüfung unterscheidet gemeinsame G2- von voller
Spin(8)-Wirkung. Diese Unterscheidung bleibt erhalten.

Ein schreibgeschützter QAM-Leseserver ist in dieser Sitzung nicht verfügbar.
Die lokale Ersatzabfrage gemäß mcp/README.md wurde ausgeführt:

```
python -X utf8 -m qam.tools.readout_db --read-only find --limit 3 -- Fourier
python -X utf8 -m qam.tools.readout_db --read-only find --limit 3 -- Heisenberg
```

Beide Abfragen endeten mit Code 0 ohne Treffer. Das betrifft nur den lokalen
Index build/qam.sqlite3; dessen Vollständigkeit gegenüber den neu geholten
Quellen ist nicht bestätigt. Es ist kein Ausschluss sämtlicher QAM-Routen.
Mangels Treffer wurde kein Beleg- oder Prämissenhash als Nachweis verwendet.

Rückwärtsfrage: Welche zusätzliche Operation müsste die bisherige
Permutationsstruktur verlassen, damit gerade die angenommene Fourier-Matrix
als aktive Operation entsteht? Zuerst diese notwendige Bedingung klären,
bevor weitere Träger oder Massenparameter untersucht werden.

## 1. Selbst die lineare Permutationsalgebra reicht nicht

Auf dem ausdrücklich gewählten skalaren Slotraum C³ sei

$$\tau(x,y,z)=(y,z,x),\quad P(x,y,z)=(x,z,y),\quad
s=(1,1,1)^T/\sqrt3,\quad Q_s=ss^\dagger.$$

P bezeichnet hier nur den linearen Slotteil von rho, nicht die gesamte
native Operation mit Konjugation. Wir erlauben für die folgende Schranke
sogar beliebige komplexe Linearkombinationen aller sechs Permutationsmatrizen.
Für jede solche Matrix A gilt

$$A s=c s,\qquad [A,Q_s]=0.$$

Begründung: Jede Permutation fixiert s und erhält sein orthogonales
Komplement. Dasselbe gilt für Summen und Produkte. Damit kann auch eine
unitäre Operation aus dieser Algebra s nur um eine Phase ändern. Das
Argument schließt ebenso eine durch einen hermiteschen Generator aus
dieser Algebra erzeugte Zeitentwicklung ein.

Die Fourier-Konvention der vorausgehenden Erkundung lautet hingegen

$$\omega=e^{2\pi i/3},\qquad
F_{jk}=\omega^{jk}/\sqrt3\quad(j,k=0,1,2),\qquad F s=e_0.$$

e_0 ist nicht proportional zu s. Folglich liegt F nicht in der komplexen
Permutationsalgebra. Als exaktes Kontrollmaß gilt

$$\|[F,Q_s]s\|=\|e_0-s/\sqrt3\|=\sqrt{2/3}>0.$$

Das ist stärker als die frühere Schranke für monomiale Gruppenprodukte:
Auch kohärente Summen allein aus tau und P liefern F nicht. Ihre gemeinsame
Zerlegung ist der tau-feste Singulettzustand s plus sein zweidimensionales
Komplement. Die gerade P-Ebene der Fourier-Erkundung ist eine andere
Zerlegung. Beide dürfen nicht identifiziert werden.

**Geltungsgrenze:** Kein Ausschluss beliebiger Operatoren auf O³. Insbesondere
werden verschiedenartige slotweise Spin(8)-Wirkungen, neue Kopplungen und
Antilinearität nicht zu komplex-linearen 3×3-Permutationen erklärt. Sie
müssten erst auf einem gemeinsamen physikalischen Slotraum dargestellt
werden. Auch P als eigenständige native lineare Operation ist hier nicht
bewiesen.

## 2. Die Uhr D liefert zusätzliche Information

Die Fourier-Erkundung verwendet zusätzlich

$$D=\operatorname{diag}(1,\omega,\omega^2),\qquad
S=\operatorname{diag}(1,\omega,\omega).$$

Weder D noch S erhält die Gerade C s. Mit D verlässt man also bereits die
oben ausgeschlossene Permutationsalgebra. Die Aussage, dass die neun
Matrizen tau^a D^b alle 3×3-Matrizen aufspannen, zeigt deshalb keine
Herkunft von F aus den Slot-Permutationen allein. D sowie die konkreten
komplexen Koeffizienten der Summe sind zusätzliche Eingaben. Gleiche
Koeffizientenbeträge wählen deren Phasen nicht aus.

## 3. Was eine echte Positions-/Phasenvertauschung festlegen würde

Mit genau den obigen Konventionen gelten

$$F\tau F^\dagger=D^{-1},\qquad F D F^\dagger=\tau.$$

Falls ein unitärer nativer Operator U beide Gleichungen mit U statt F
erfüllt, folgt U = exp(i alpha) F. Denn F^dagger U kommutiert dann mit
tau und D. Wegen der drei verschiedenen D-Eigenwerte ist diese Matrix
diagonal; Vertauschen mit dem Zyklus macht alle drei Diagonaleinträge
gleich. Die Unitarität lässt nur eine Gesamtphase übrig.

Damit ist ein konkretes Herleitungsziel benannt: eine unabhängig begründete
Uhr D und eine aktive Operation, die **beide** geordneten Vertauschungsregeln
liefert. Nur U tau U^dagger = D^-1 reicht nicht: U = F C ist für jede
unitäre, mit tau kommutierende Matrix C eine Lösung. Die relativen Phasen
der drei tau-Eigenräume bleiben dabei frei.

Auch F²=P allein wählt F nicht. Beispielsweise ist

$$U_0=(I+P)/2+i(I-P)/2$$

unitär und erfüllt U_0²=P, wirkt aber auf der geraden P-Ebene als Identität.
Es liefert dort keine ausgezeichnete zweizählige Achse. Eine Auswahl von F
aus Wurzeln der Parität wäre eine weitere Voraussetzung.

## 4. Aktive Operation und Basiswechsel

F kann jederzeit als Basiswechsel von Slotpositionen zu Fourier-Moden
benutzt werden. Dabei werden Zustände, Operatoren und Auslesekarten
gemeinsam transformiert; das erzeugt keine neue physische Kopplung.
Die Konstruktion des Oktanten braucht dagegen F als aktive Operation
relativ zur festgehaltenen Slot-Phase S sowie eine Auswahl des Bezugszustands.
Die Möglichkeit, den Zyklus zu diagonalisieren, begründet diese aktive
Operation nicht.

## Ergebnis und nächste Pflicht

Die offene Herkunft von F lässt sich nicht dadurch erledigen, dass man
Summen der bisherigen Slot-Permutationen zulässt. Es fehlt eine begründete
Operation, welche die gleichmäßige Slotgerade verlassen kann. Das Paar
(tau,D) mit geordneter Positions-/Phasenvertauschung wäre hinreichend, F bis
auf Gesamtphase festzulegen; D und diese Vertauschung sind aber nicht
hergeleitet. Auch die Herkunft von S und die Auswahl des F-Eigenzustands
bleiben offen. Koide und Leptonmassen folgen daraus weiterhin nicht.

Nächster konkreter Schritt: Für die slotweisen Trialitätsoperatoren aus
r37 auf einem gemeinsamen farb- und ladungstypisierten Dreierraum prüfen,
ob eine native Uhr D oder die Phase S überhaupt dargestellt wird.
Dabei die volle Spin(8)-Wirkung nicht stillschweigend auf die gemeinsame
G2-Wirkung reduzieren. Ohne diese Darstellung keine weitere F-Auswahl
oder Massenanpassung. F4 wurde nicht untersucht.

Die Auslöser I1–I5 wurden erneut geprüft; diese begrenzte Slotprüfung
aktiviert keinen neuen Auslöser. CT-001/CT-002 bleiben in ihrer ruhenden
Route, CT-003 wird nicht auf diesen Slotraum übertragen. H100/H102 und
OP1–OP5, C5, C6/T2 behalten ihren bisherigen Status.

Selbstprüfung: Die Schranke folgt aus dem invarianten Projektor Q_s;
die Fourier-Identitäten folgen durch Indexverschiebung modulo 3; die
Eindeutigkeit aus dem gemeinsamen Kommutanten; U_0²=P aus den beiden
orthogonalen Paritätsprojektoren. Keine numerische Rechnung nötig.
