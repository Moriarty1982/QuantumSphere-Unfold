# OP5: größerer Partnersektor und die native HS(5)-Verdopplung

Checkpoint `OP5-HS5-PAIRED-SECTOR-2026-10-26`.
Git-Basis `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Lokale analytische Fortsetzung; kein Manuskript- oder Veröffentlichungsstand.

## 1. Neuer Quellenbefund

Die größere Partnersektor-Variante hat bereits eine native Anschlussstelle:
`sources/research/parts/v470/32_atlas_and_op_promotion.tex`, Abschnitte
„HS(4) meta-septum leakage target“ und „HS(5) two-sided duplication“.
Die Quelle setzt

    H_5=(H_4)_front direct_sum (H_4)_back,
    P_5=diag(P_front,P_back),    dim H_4=16 Kanäle.

Die Frontseite trägt dort Readout-/Frame-/Sprachinformation, die Rückseite
Struktur-/Wirkungs-/Feldinformation. Die Quelle definiert ein Cross-Side-
Register mit den Querblöcken relativ zu P_5. Ein Transfer zwischen Front
und Back ist damit nicht generell verboten: Verboten ist unkontrollierter
Transfer zwischen dem zugelassenen Sektor und seinem Komplement.

Das sind keine schon hergeleiteten Materie-/Tachyon-Seiten. Ebenso liefert
dieser Abschnitt keinen konkreten positiven unitären Vergleich zwischen
beiden Seiten und keinen numerischen Rang von P_C7. P_C7 wird in HS(4)
mit P²=P als geerbter Sektor eingeführt. Der Index 7 wird nicht ohne
weiteren Beweis als Rang auf diesem Träger verwendet.

## 2. Aus der Quelle abgeleiteter exakter Blocktest

Zusätzliche Voraussetzungen für die folgenden Aussagen: endliche positive
Hilberträume, orthogonale P_f,P_b und eine gemeinsame Adjungierte.
Setze Q_s=I-P_s und einen allgemeinen Zweitseitenoperator

    T_5=[[A,B],[C,D]].

Die Kommutatorbedingung [T_5,P_5]=0 ist exakt äquivalent zu

    [A,P_f]=0,    [D,P_b]=0,
    B P_b=P_f B,    C P_f=P_b C.

Die letzten Gleichungen sind Intertwiner-Bedingungen: Zugelassene Daten
werden von einer Seite in zugelassene Daten der anderen Seite übertragen;
das Komplement ebenfalls in das Komplement. Für hermitesches T_5 mit
C=B† und orthogonalen P_s sind die beiden Querbedingungen adjungiert.
Für einen nichtselbstadjungierten T_5 müssen beide Richtungen geprüft werden.

Der in der Quelle „Cross-Side“ genannte vollständige Register enthält
bei wörtlicher Auswertung auch die beiden seiteneigenen Closure-Tests.
Sind diese schon separat bewiesen, bleiben genau die Intertwiner-Bedingungen
zwischen den Seiten als neue Verpflichtungen übrig.

Auch ohne Orthogonalität sind die Blockkommutatorgleichungen algebraisch
gültig; Positivität, Normen und die unten verwendeten Spektralprojektoren
werden aber nicht aus bloßer Idempotenz gefolgert.

## 3. Eine kovariante Partneranhebung statt eines Projektormittels

Gegeben seien P auf einer positiven 16-dimensionalen Referenzseite und
ein zusätzlich physisch begründeter unitärer Vergleich W zur Rückseite.
Definiere

    P_b=W P W†,
    P_pair=diag(P,W P W†),
    X=[[0,W†],[W,0]].

Dann sind X=X†, X²=I, P_pair=P_pair†=P_pair² und

    [P_pair,X]=0,    rank P_pair=2 rank P.

Die mathematische Vergrößerung enthält also beide Partner, statt sie zu
einem nichtidempotenten Mittel zusammenzudrücken. Unter unabhängigen
unitären Basiswechseln U_f,U_b transformiert der Vergleich als

    W'=U_b W U_f†,
    P_pair'=diag(U_f,U_b) P_pair diag(U_f,U_b)†.

Die Auswahl benötigt damit keinen festgehaltenen Koordinatenframe.
W selbst und die physische Bedeutung beider Seiten werden durch diese
Kovarianz allerdings nicht bestimmt. Sie dürfen nicht passend zum
gewünschten Ergebnis frei als nativ hergeleitet ausgegeben werden.

Sind beide seitlichen Projektoren bereits physisch vorgegeben, darf die
Relation P_b=W P W† nicht bloß passend gesetzt werden. Für ein gegebenes W
ist der größte austauschverträgliche Unterraum innerhalb beider gewählten
Seiten durch K=ran(P_f) intersect W†ran(P_b) bestimmt. Der zugehörige
gepaarte Projektor ist diag(P_K,W P_K W†), hat Rang 2 dim(K) und kann
auch null sein. Das beschränkt die Partneranhebung bei festgehaltenen
Eingaben und verhindert eine zirkuläre Anpassung des Rückseitenprojektors.

## 4. Beide Austauschports innerhalb desselben Closure-Sektors

Die Austauschports von X sind

    C_+^side=(I+X)/2,    C_-^side=(I-X)/2.

Beide haben auf H_5 Rang 16. Sie kommutieren mit P_pair und

    rank(P_pair C_+^side)=rank(P_pair C_-^side)=rank P.

Beweis: In den beiden X-Eigenräumen haben die Vektoren die Form
(v,+Wv)/sqrt(2) beziehungsweise (v,-Wv)/sqrt(2). P_pair wählt darin
jeweils genau v in ran(P). Bei rank P>0 und <16 sind P_pair und die
Side-Ports somit verschiedene Projektoren mit verschiedenen Aufgaben.
Für P=0 bzw. I gelten die entsprechenden trivialen Grenzfälle.

Das schafft eine genaue Alternative zur bisherigen Gleichsetzung eines
einzelnen Ports mit dem gesamten physischen Sektor. Ein ungerader Rang
auf der ursprünglichen Seite wäre hier nicht ausgeschlossen; nur sein
gepaarter Gesamtrang ist gerade. Eine Rangvorgabe muss aus der tatsächlichen
nativen Darstellung stammen, nicht aus dem Namen C7.

## 5. Nichttriviale Partnerdynamik ist mit Closure vereinbar

Für einen internen hermiteschen H mit [H,P]=0 und reelles g setze

    H_pair=diag(H,W H W†)+g X.

Alle Terme kommutieren mit P_pair. Der volle zugelassene Partnersektor
bleibt erhalten, obwohl g X kohärenten Transfer zwischen Front und Back
erzeugt. Zum Beispiel entwickelt sich ein anfänglicher Frontzustand
(v,0), v in ran(P), zu

    (cos(g t) exp(-iHt)v,
     -i sin(g t) W exp(-iHt)v).

Die Frontwahrscheinlichkeit ist cos²(g t), die Backwahrscheinlichkeit
sin²(g t). Bei einem einzelnen passenden Zeitpunkt kann ein ausgeglichener
Readout auftreten; ohne zusätzliche Auswahlmechanik ist dies keine
Relaxation zu einem dauerhaft neutralen Zustand. Die gesamte Norm und
die Energie des konstanten hermiteschen H_pair bleiben erhalten.

Dieser Generator ist eine zusätzliche transparente Testrealisierung
des Quellen-Blockmusters. Die Quelle bestimmt weder W noch g und beweist
damit auch nicht diese physische Zeitentwicklung.

## 6. Der ursprüngliche Closure-Defekt verschwindet dadurch nicht

Der kritischere Gegencheck lässt die alte M-Matrix ausdrücklich unverändert.
Für beliebiges M und reelles g bilde

    M_pair=diag(M,W M W†)+g X.

Weil [X,P_pair]=0, gilt mit K=[M,P]

    [M_pair,P_pair]=diag(K,W K W†).

Bei denselben nichtnegativen Closure-Koeffizienten rho,sigma ist deshalb
für das minimale Funktional exakt

    H_C,pair=diag(H_C(M,P), W H_C(M,P) W†).

Folglich

    H_C,pair=0  iff  H_C(M,P)=0,
    Tr H_C,pair=2 Tr H_C(M,P).

Für rho+sigma>0 entspricht dies auch K=0; für beide Koeffizienten null
ist das Closure-Funktional ohne Aussage über K. Die Norm des positiven
Closure-Operators bleibt bei der Verdopplung in der Operatornorm gleich;
eine größere Zahl von Kopien ist keine physische Verstärkung der Dichte.
Die doppelte Spur zählt zunächst doppelte interne Kanäle. Bei normierter
gleichgewichteter Seitenmischung bleibt der entsprechende mittlere
Erwartungswert gleich. Eine physische Energie- oder Volumennormierung
ist damit nicht hergeleitet.

Das ist ein wichtiger negativer Test: Die Anhebung repariert eine
zu enge Ein-Port-Beschreibung, beseitigt aber keinen echten ursprünglichen
M/P-Defekt. Ein solcher Defekt müsste auf jeder Seite oder durch eine
begründet anders gewählte relationale Closure behoben werden.

## 7. Neutralität und Eindeutigkeit bleiben separate Fragen

In den durch W identifizierten Seitenkoordinaten ist

    P_pair=I_2 tensor P,
    rho_neutral=(I_2/2) tensor rho_internal

für einen normierten inneren Zustand rho_internal auf ran(P) seitenneutral.
P_pair ist ein Projektor; rho_neutral ist eine Dichtematrix. Das sind
verschiedene Objekte. Austausch allein erlaubt auch seitliche Kohärenzen;
für eine eindeutig maximierte Seitenmischung braucht es zusätzliche
Invarianz- oder Präparationsbedingungen. Beispielsweise erzwingt Invarianz
unter zwei nichtparallelen Pauli-Seitenkonjugationen den Faktor I_2/2,
während die interne Dichtematrix dadurch noch frei bleibt.

Ebenso bestimmt die Seitenalgebra den inneren Projektor P nicht:
Jeder mit der vollen Pauli-Seitenalgebra kommutierende Operator ist
I_2 tensor Y. Das folgt aus den vier Pauli-Koeffizienten einer allgemeinen
2x2-Blockmatrix; die drei nichtskalaren Koeffizienten müssen verschwinden.
Als orthogonale Projektoren bleiben daher genau I_2 tensor Q mit beliebigem
orthogonalem inneren Q. Das Partnerprinzip begründet die doppelte Struktur,
nicht den noch fehlenden internen P_C7.

## 8. Was jetzt physikalisch präziser ist

Die native Quelle gestattet bereits zugelassenen Transfer innerhalb eines
größeren zweiseitigen Sektors. Das frühere Bild „ein Port physisch, Partner
außerhalb“ ist folglich keine notwendige Lesart der gesamten Architektur.
Die mathematische Partneranhebung zeigt konkret, wie beide Ports und ihre
Kopplung mit einem einzigen idempotenten physischen Projektor vereinbar sind.

Die verbleibenden nativen Verpflichtungen sind enger benennbar:

1. Welcher physische Vergleich W verbindet die beiden Quellseiten, und
   sind dies überhaupt Materie-/Tachyon-Frames oder andere Informationslagen?
2. Welche gemeinsame innere Operatorfamilie bestimmt P_C7 samt Rang?
3. Erfüllen die tatsächlichen Querblöcke die vier Intertwiner-Bedingungen?
4. Wie sind positive Adjungierte, Zeitskala und Feldrückwirkung bestimmt?

Die Anhebung erfindet keine Werte für diese Eingaben. Sie lässt einen
skalaren Energieoffset weiterhin frei und liefert keine kosmologische
Vakuumenergie. OP5 bleibt offen. Die Partnerstruktur ist jetzt an eine
tatsächliche Passage des Papers angeschlossen, ihr physischer Inhalt und
ihre vollständige Dynamik sind noch zu evaluieren.

## 9. Prüfung und Provenienz

Alle neuen Formeln wurden durch explizite 2x2-Blockmultiplikation,
Adjunktion, Eigenraumdarstellung von X und Exponentiation zweier
kommutierender Hamiltonanteile analytisch geprüft. Der Kontrollfall mit
unverändertem nichtgeschlossenem M verhindert ein verdecktes Wegmitteln
des alten Defekts. Keine numerischen Experimente oder native Fits.

Die unabhängig geprüften Querblockbedingungen und Quellenabgrenzungen
stehen in `OP5_HS5_Partner_Lift_Independent.md`. Die vorangehende
Auswahlprüfung steht in `OP5_Dynamics_And_Symmetry_Selection.md`.
Die unabhängige Notiz wurde vollständig gelesen und die Blockbedingungen,
Austauschränge und der Zusatzfall nichtkompatibler Projektoren abgeglichen.
