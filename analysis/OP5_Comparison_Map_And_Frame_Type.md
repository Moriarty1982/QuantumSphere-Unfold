# OP5: Welche Vergleichsabbildung verbindet die Partnerseiten?

Checkpoint `OP5-COMPARISON-MAP-TYPE-2026-10-26`.
Git-Basis `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Lokale Fortsetzung der HS(5)-Partnersektorprüfung; keine Manuskriptänderung.

**Korrektur durch die Fortsetzung:** `OP5_Realification_And_Gram_Boundary.md`
berücksichtigt die schon vorhandene explizite Brücke aus r04.1:
z=E+iB -> F=[E|B], iK -> rechter Spaltentausch sigma_x.
Die frühere Einordnung dieser konkreten Übersetzung als fehlend war zu
weitgehend. Die allgemeinen linearen/antilinearen Rechnungen unten bleiben
gültig; offen sind die volle M16/P_C7-/HS(5)-Einbettung und die physische
Vergleichszuordnung, nicht die lokale r04-Realifizierung.

## 1. Ergebnis des Quellenabgleichs

Der Vergleich zwischen den beiden Seiten ist nicht bereits als unitäres W
festgelegt. Die Quelle erlaubt explizite Vergleichstensoren und Selektoren.
Der spätere r40-Test zeigt ausdrücklich, dass bilineare und hermitesche
Vergleiche verschiedene Frame-Eigenschaften haben und antilineare
Frame-Abbildungen Werte konjugieren können.

Damit ist eine wichtige Grenze des vorigen Partner-Modells lokalisiert:
Seine positive, komplexlineare und unitäre Identifikation W war eine
zusätzliche Annahme. Sie ist nicht die bereits ausgerechnete native
Vergleichsabbildung. Diese Annahme muss entweder physikalisch begründet
oder durch eine korrekt typisierte andere Vergleichsstruktur ersetzt werden.

## 2. Primäre Quellen und Typen

`sources/research/parts/v470/07_qam_infrastructure.tex`,
`def:two-sided-structural-tensor-interface` und
`def:two-sided-admissible-contractions`: Die Vorder-/Rückindizes trennen
Rollen. Gleichartige Indizes werden nur mit einem ausdrücklich angegebenen
Vergleichstensor oder Selektor verglichen. Dieser Notationsblock wird
selbst als konservative Grammatik und nicht als neues Tensor- oder
Closure-Kalkül bezeichnet.

`sources/research/parts/v470/32_atlas_and_op_promotion.tex`, HS(5):
Der 32-Kanal-Träger verdoppelt den 16-Kanal-Träger und verlangt deklarierte
Vergleiche. Das liefert noch keine ausgewertete physische Zuordnung W.

`sources/research/parts/v490-post-release-layers.tex`,
`sec:v490-r40-two-sided-frames`, insbesondere Modell und r40.1(b),(c):
Die Frontabbildung X->iX ist komplexlinear, T ist Konjugation, J_B deren
Komposition. Bilineare Vergleiche wechseln unter i das Vorzeichen;
hermitesche Vergleiche nicht. Die Quelle nennt die Notation frame-kovariant,
nicht allgemein frame-invariant, und hält eine vorgeschlagene Frame-Klausel
als Autorenentscheidung fest. Es wird hier keine nachträgliche Annahme
gemacht, dass diese Klausel bereits alle gemeinsamen Operatoren bestimmt.

Insbesondere ist ein bilinearer Tensor G ein Vergleich in Richtung eines
Dualraums und nicht allein schon ein Transport V_front -> V_back. Auch
ein Selektor oder eine Ähnlichkeitszahl ist kein invertierbarer Transport.
Eine Rückübersetzung in W erfordert identifizierte Träger und Metriken.

## 3. Bilineare Neutralität ist nicht positive Normneutralität

Bei reell symmetrischem G setze in der angegebenen Darstellung

    q(X)=X^T G X,    h(X)=X† G X.

Dann gilt exakt

    q(iX)=-q(X),    h(iX)=h(X),
    q(bar X)=bar q(X),    h(bar X)=h(X).

Für die Norminterpretation von h ist zusätzlich G>0 erforderlich;
reelle Symmetrie allein reicht dafür nicht. Bereits mit G=I und
X=(1,i)^T ist q(X)=0, aber h(X)=2. Die Bilinearform kann also trotz
nichtverschwindender positiver Größe null sein.

Eine derartige Aufhebung kann eine strukturelle Vergleichsbedingung
erfüllen. Sie ist ohne weitere Dynamik- und Wirkungsidentifikation weder
verschwindende Energie noch verschwundene positive Closure-Last. Falls
eine frühe physische Deutung q wie h benutzt hat, wäre genau diese
Vertauschung zu korrigieren. Für den tatsächlichen P_C7 muss dies an
seiner konkreten Definition geprüft werden; der vorliegende Befund
beweist nicht, dass er schon so berechnet wurde.

## 4. Wann aus einem linearen Vergleich ein eindeutiges unitäres W folgt

Nehme zusätzlich zwei gleichdimensionale positive Hilberträume und eine
konkrete invertierbare komplexlineare Vergleichsmatrix L an. Dann ist
ihre Polarzerlegung durch

    S=(L†L)^(1/2)>0,    W=L S^(-1),    L=W S

eindeutig; W ist unitär. Das ist eine Ableitung aus gelieferten L und
Metriken, keine freie Wahl von W. Für singuläres L erhält man auf seinem
Träger nur eine partielle Isometrie; eine globale unitäre Ergänzung ist
im Allgemeinen nicht eindeutig. Bei verschiedenen Dimensionen kann die
Quadrat-Matrix-Konstruktion nicht einfach übernommen werden.

Sind orthogonale P_f,P_b vorhanden und L P_f=P_b L, dann folgt durch
Adjunktion P_f L†=L† P_b. Daraus ergibt sich

    [L†L,P_f]=0,    [S,P_f]=0,    W P_f=P_b W.

Ein bereits kompatibler invertierbarer linearer Vergleich liefert also
auch einen kompatiblen unitären Polar-Anteil. Ein nichtkompatibler L wird
dadurch nicht automatisch kompatibel. Ist S physische Verstärkung oder
Filterung, darf es zudem nicht als bloße Normierung entfernt werden:
Der Ersatz L->W wäre dann eine Änderung des Prozesses. Die gemeinsame
positive Adjungierte und die Rolle von S müssen vorher feststehen.

Die Quelle liefert im geprüften HS(5)-Abschnitt kein solches konkretes L.
Darum ist diese Konstruktion eine bedingte Methode zur Bestimmung von W,
keine bereits ausgeführte native Polarzerlegung.

## 5. Ein punktweises W muss auch zur Verbindung passen

Sei W(x) unitär und D_mu^s=partial_mu+i A_mu^s mit hermiteschem A_mu^s
auf den beiden Seiten. Die Forderung, dass W den Transport verknüpft,
lautet für beliebiges f

    D_mu^b(W f)=W D_mu^f f.

Ausmultiplizieren liefert die notwendige und hinreichende lokale Gleichung

    partial_mu W+i A_mu^b W-i W A_mu^f=0,
    A_mu^b=W A_mu^f W†+i(partial_mu W)W†.

Kommutiert man zwei solche Ableitungen, folgt die zusätzliche notwendige
Krümmungsbedingung

    F_mu nu^b W=W F_mu nu^f.

Ein flacher und ein nichtflacher Hintergrund können daher nicht durch
einen solchen parallelen unitären Vergleich identifiziert werden. Umgekehrt
beweist eine punktweise passende Krümmung noch keine gemeinsame glatte
globale Vergleichsabbildung; Wegtransport und globale Bedingungen bleiben.

Mit P_b=W P_f W† überträgt ein solcher Vergleich auch kovariante
Projektorparallelität: nabla_mu^b P_b=W(nabla_mu^f P_f)W†. Damit lassen
sich die Bedingungen des vorherigen nativen Projektortests gemeinsam
formulieren. Ein frei punktweise gewähltes W ohne Ableitungsprüfung reicht
dafür nicht.

Für eine vollständige Verbindung mit weiteren nichtunitären HC-Anteilen
muss die Intertwiner-Gleichung mit der vollständigen B_mu statt nur iA_mu
geprüft werden; die obige positive unitäre Teilrechnung ersetzt das nicht.

## 6. Antilineare Frame-Zuordnung: anderer Typ, andere Zeitgleichung

Bei einem antiunitären Vergleich W=U K, mit K komplexer Konjugation in
einer ausdrücklich angegebenen Basis, ist P_b=W P_f W^(-1) weiterhin
ein komplexlinearer orthogonaler Projektor. Auch ein Kommutator transformiert
konsistent: [W M W^(-1),W P W^(-1)]=W[M,P]W^(-1). Nullität wird dadurch
nicht repariert oder erzeugt.

Aber die bisherige HS(5)-Austauschabbildung

    X(v,w)=(W^(-1)w,Wv)

ist dann selbst antilinear. Sie erfüllt X²=I, doch (I+X)/2 und (I-X)/2
sind nur reelllineare Projektoren, keine komplexlinearen orthogonalen
Quantenprojektoren auf dem unveränderten komplexen Träger. Zum Beispiel
ist (z+bar z)/2=Re z nicht komplexlinear. Eine Realifizierung oder ein
geänderter Träger ist möglich, muss aber ausdrücklich konstruiert werden.

Auch die Vorwärtszeit-Dynamik ändert ihren Typ. Für i dot f=H_f f und
b(t)=U(t)bar f(t) folgt durch direkte Ableitung

    i dot b=H_b b,
    H_b=i dot U U†-U H_f^* U†.

Der Stern bei H_f^* bedeutet hier eintragsweise komplexe Konjugation,
nicht die mit dagger bezeichnete hermitesche Adjungierte.

Bei konstantem U entsteht das Minuszeichen vor dem konjugierten
Generator. Für eine tatsächliche Zeitumkehr b(t)=U bar f(-t) mit
konstantem U gilt dagegen H_b(t)=U H_f(-t)^* U†. Eine antilineare
Frame-Zuordnung bei gleicher Zeit ist also nicht schon dieselbe Behauptung
wie physische Zeitumkehr. Die Transformation eines Energieobservablen
ist zusätzlich von der eines zeitabhängigen Darstellungsgenerators zu
unterscheiden.

Damit lassen sich r40-Konjugation, unitärer Partnerlift und unveränderte
Vorwärtsdynamik nicht ohne weitere Vorschrift gleichsetzen. Das ist eine
konkrete Typ- und Vorzeichenpflicht für die Frame-Hypothese.

## 7. Welche der Optionen lässt die Quelle derzeit zu?

| Gelieferte Vergleichsstruktur | Was daraus folgt | Was zusätzlich fehlt |
|---|---|---|
| Bilinearer Tensor G | Frame-sensitiver Vergleich, ggf. Vorzeichenwechsel | Kein automatisches positives Skalarprodukt oder W |
| Hermitesches G | Phasenblinder Vergleich; bei G>0 positive Norm | Kein automatisch ausgewählter Sektor oder Transport |
| Invertierbares lineares L plus positive Metriken | Eindeutiger unitärer Polar-Anteil | Physische Rolle des positiven Faktors; Projektor- und Transportverträglichkeit |
| Antiunitäres W | Konsistente antiunitäre Zuordnung von Zuständen und Operatoren | Angepasste Austausch-/Zeitformulierung; keine ungeänderten komplexlinearen Side-Projektoren |
| Selektor oder Rollenetikett | Zulässigkeit bestimmter Vergleiche | Keine Matrixelemente oder physische Dynamik |

Keine Zeile allein liefert den gesamten nativen Übergang. In den
geprüften Quellen wird kein einzelnes W mit sämtlichen benötigten
Eigenschaften ausgewertet. Die linearen und antilinearen r40-Abbildungen
leben auf einer konkret beschriebenen Dixon-Frontstruktur; ihre Nutzung
als W zwischen den zwei HS(4)-Kopien erfordert noch eine Einbettung.
Ebenso darf X->iX auf diesem Träger nicht ohne Darstellungstransport
mit der sigma_y-Konjugation des Zustandsdoublets gleichgesetzt werden.

Eine besonders konkrete Typunterscheidung betrifft den gleichen Namen J_B:
r40 schreibt J_B=iK antilinear auf dem komplexen Faktor; das frühere
Doublet verwendet J_B=sigma_x komplexlinear. Eine komplexlineare
Basisänderung kann die Linearitätsart nicht ändern. Eine gemeinsame
Deutung benötigt daher eine Realifizierung bzw. explizite Abbildung der
verschiedenen Träger. Genau diese lokale Realifizierung ist in r04.1
bereits angegeben, wie die nachfolgende Prüfung ausdrücklich festhält.
Die Typdifferenz ist dort konsistent aufgelöst; die vollständige
M16/P_C7-/HS(5)-Abbildung ist damit noch nicht bestimmt.

## 8. Geänderter Forschungsstand

Die Partnersektor-Variante bleibt möglich. Ihre wichtigste zusätzliche
Eingabe ist jetzt genauer bestimmt: Art, positive Metrik, Matrixelemente
und Transportgesetz des Vergleichs müssen gemeinsam angegeben werden.
Die physische Unterscheidung zwischen bilinearer und hermitescher
Neutralität muss VOR einer Closure- oder Energieinterpretation erfolgen.

Das erhärtet den ursprünglichen Prüfauftrag: Ein unmarkierter Wechsel
des Vergleichstyps kann Probleme in spätere Frame-Aussagen mitnehmen.
Die Quelle r40 kennt genau diese Unterscheidung bereits. Sie wird hier
als notwendiger Teil des M16-/P_C7-Audits integriert, nicht als neue
Behauptung eines schon nachgewiesenen falschen P_C7 ausgegeben.

Ein neuer beliebiger Mischframe würde diese Eingabe ersetzen statt sie
herzuleiten. Bevor weiter eine bestimmte neutrale Referenz berechnet wird,
muss daher der physische Typ des Vergleichs feststehen. Kein absoluter
Energieoffset und keine kosmologische Konstante wurden hier bestimmt.

## 9. Validierung

Analytische Prüfung durch Substitution in q,h, Polarzerlegung mit expliziten
Invertierbarkeitsbedingungen, Ableitung der Verbindungs- und
Krümmungsidentität sowie direkte komplexe Konjugation der Schrödingergleichung.
Keine numerischen Stichproben und kein native Fit. Die unabhängige
Antilinearitätsprüfung steht in `OP5_Antilinear_Comparison_Independent.md`.
Sie wurde gelesen und hinsichtlich beider Zeitvorzeichen, der reelllinearen
Graphsektoren, positiven Closure-Kovarianz und der J_B-Typdifferenz
abgeglichen. Eine antilineare Vorzeichenänderung des Darstellungsgenerators
ist insbesondere keine hergeleitete negative gravitative Energie.
