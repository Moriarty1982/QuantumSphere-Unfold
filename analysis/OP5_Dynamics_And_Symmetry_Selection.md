# OP5: Versuch einer Auswahl durch gemeinsame Dynamik und Symmetrie

Checkpoint `OP5-DYNAMICS-SYMMETRY-SELECTION-2026-10-26`.
Git-Basis `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Auftrag: Die vorgeschlagenen Begründungen tatsächlich prüfen, bevor eine
neue Frame-Mischung als P_C7 eingesetzt wird. Lokale Forschungsnotiz;
keine Manuskriptänderung, Veröffentlichung oder Schließung von OP5.

## 1. Ergebnis

Beide Wege liefern konkrete mathematische Tests. Sie liefern aber aus den
bislang dargestellten nativen Daten noch keinen eindeutig ausgewählten P_C7.
Auf dem vorhandenen Doublet scheitert die Forderung nach einem einzelnen
nichttrivialen, sowohl porttreuen als auch austauschsymmetrischen Projektor.
Die zwei Ports können stattdessen als gleichberechtigte, vertauschte Familie
erhalten bleiben. Ihr neutraler gemischter Zustand ist kein neuer Projektor.

Ein enger positiver Befund gelingt für den früheren reellen Dreimoden-
Rotationskandidaten: Dynamik plus dessen reelle Struktur bestimmen seine
Zweimodenebene bei festem Rang eindeutig. Diese Eindeutigkeit ist bedingt
durch die gewählte Struktur und stabilisiert sich nicht automatisch gegen
weitere native Kopplungen. Sie identifiziert daher noch keinen nativen P_C7.

## 2. Gemeinsame Dynamik: der konkrete Auswahltest

Endlicher positiver interner Hilbertraum, orthogonales P, gemeinsam
angegebene konstante Operatoren A_j. Gesucht wird

    P=P†=P²,    rank P=r,    [P,A_j]=0 für alle j.

Die Kommutatorgleichungen sind zunächst linear in einem unbekannten X.
Man bestimmt also den gemeinsamen Kommutanten

    K={X:[X,A_j]=[X,A_j†]=0 für alle j}

und sucht erst darin hermitesche Idempotente des physisch begründeten Rangs.
Nicht jedes Element von K ist ein Projektor. Wenn K nur die Skalare enthält,
sind 0 und I die einzigen Projektoren. Ist K größer, ist eine eindeutige
Auswahl noch nicht garantiert; bei mehrfach vorkommenden identischen
Darstellungen kann sogar eine kontinuierliche Auswahlfreiheit bleiben.

Die tatsächliche Familie darf nicht frei passend gewählt werden. Sie
enthält die physischen freien Generatoren und die verlangten Symmetrien.
Für den faktorisierten Probe-Ansatz verlangen die bisherigen Ergebnisse
insbesondere kovariant paralleles P und bei beta g_Y!=0 die Bedingung QTP=0.
In einer lokalen Basis mit konstantem P wird die Parallelität zu [A_mu,P]=0.
Die native exakte Millennium-Closure verlangt zusätzlich [M,P]=0.
Für nichtselbstadjungiertes M muss die positive orthogonale Reduktion
berücksichtigt werden, nicht nur eine beliebige einseitige Invarianz.

Ein unabhängiger Pacer R darf nicht ohne physische Entscheidung zusätzlich
in diese freie Generatorfamilie aufgenommen werden: Soll gerade sein
Querblock (I-P)RP einen Mess-/Massendefekt liefern, würde [R,P]=0 diese
Route per Definition beseitigen. Die Rolle als freier Generator oder
als sektorübergreifende Messkopplung ist zu unterscheiden. Das ist bereits
in `native-operator-link.tex`, `v480:native-closure-transfer`, dokumentiert.

Das Fehlen gemeinsamer nativer Einträge von M,P,T und gegebenenfalls R
verhindert derzeit eine tatsächliche 16x16-Kommutantenbestimmung. Bekannte
Eigenwerte allein reichen dafür nicht: Die Quelle beweist bereits die
relative isospektrale Freiheit (`v480:native-isospectral-freedom`).

## 3. Dynamik darf auch keinen kleineren Sektor übriglassen

Ein exakter Zweidimensionen-Test mit zwei hermiteschen Generatoren:

    A_1=sigma_x,    A_2=sigma_z.

Schreibe X=a I+b_x sigma_x+b_y sigma_y+b_z sigma_z mit komplexen
Koeffizienten. [X,sigma_x]=0 erzwingt b_y=b_z=0;
[X,sigma_z]=0 erzwingt danach b_x=0. Der gemeinsame Kommutant ist C I.
Folglich existiert kein gemeinsamer Rang-eins-Projektor.

Allgemeiner gilt für zwei nichtparallele Pauli-Achsen derselbe Schluss.
Bei parallelen Achsen bleiben ihre beiden gemeinsamen Rang-eins-Ports
übrig; das entscheidet noch nicht, welcher davon der physische Sektor ist.

Dieses Beispiel zeigt eine echte Alternative zur erwarteten neutralen
Mitte: Zwei Referenzen können den gesamten Raum gemeinsam benötigen,
anstatt einen kleineren gemeinsamen Sektor auszuwählen. Falls man statt
eines Projektors eine Dichtematrix sucht, ist die einzige mit beiden
Generatoren kommutierende normierte Matrix I/2. Diese Aussage liefert
einen gemeinsamen stationären Zustand, aber noch keinen Mechanismus,
der andere Zustände zu ihm hin entwickelt.

## 4. Symmetrie auf dem nativen Doublet

Quellen: `v490-post-release-layers.tex`, r05.1 und die r28-Korrektur.
Der porttreue Schichttransport hat die Form

    J_B=sigma_x,    C_+=(I+sigma_x)/2,    C_-=(I-sigma_x)/2,
    M=lambda_+ C_+ +lambda_- C_-.

Bei lambda_+!=lambda_- sind seine beiden Rang-eins-Spektralprojektoren
genau C_+,C_-. Die korrigierte gegenüberliegende Frame-Abbildung wirkt
auf Zuständen als D:rho -> sigma_y rho sigma_y und vertauscht diese Ports:

    sigma_y C_+ sigma_y=C_-,    sigma_y C_- sigma_y=C_+.

Fordert man [P,M]=0 und sigma_y P sigma_y=P für EINEN orthogonalen P,
bleiben deshalb nur P=0 und P=I. Bei gleichem Portgewicht M=lambda I
entfällt die erste Einschränkung; dieser entartete Fall muss getrennt
behandelt werden und liefert keine durch M ausgewählte Portaufteilung.

Für die Familie {C_+,C_-} ist die Austauschabbildung dagegen völlig
verträglich: Sie permutiert die Elemente. Das ist Symmetrie der Familie,
keine individuelle Invarianz jedes einzelnen Ports. Unter einem gemeinsamen
unitären Wechsel U transformiert auch die Familie mit U; das ist Kovarianz.
Die drei Forderungen dürfen nicht miteinander verwechselt werden.

Die gleiche Gewichtung ist durch diese Austauschforderung für eine
portdiagonale normierte Dichtematrix begründet:

    rho_p=p C_+ +(1-p)C_-,
    sigma_y rho_p sigma_y=rho_p  iff  p=1/2,
    rho_neutral=I/2.

Die Symmetrie begründet hier einen neutralen Zustand, nicht einen neuen
Rang-eins-P_C7. Sie begründet auch nicht, dass ungleiche Portgewichte in M
selbst eine unveränderte physische Symmetrie besitzen: D M D† vertauscht
lambda_+,lambda_- und ist nur bei Gleichheit wieder derselbe M. Als
Abbildung zwischen Referenzbeschreibungen kann D die ganze Datenfamilie
transformieren; daraus folgt keine Symmetrie eines festgehaltenen
ungleich gewichteten Operators.

## 5. Positiver bedingter Versuch: dynamisch und reell bestimmte Ebene

Betrachte nochmals den vollständig deklarierten Vergleichsgenerator

    H=m I+iA(a),    A(a)f=a cross f,    a reell,    Omega=||a||>0.

Gesucht wird jetzt ein orthogonaler Projektor P auf C³ mit

    [P,H]=0,    P*=P (eintragsweise Konjugation),    rank P=2.

Hier bedeutet P*=P, dass der Sektor unter der zuvor gewählten gewöhnlichen
reellen Struktur erhalten bleibt. Das ist eine zusätzliche Strukturbedingung;
sie wird nicht ohne Beweis mit nativer Tachyon- oder Zeitumkehr identifiziert.

**Exakte Lösung:**

    P=S=I-aa^T/Omega².

Beweis: Ein reeller hermitescher Projektor ist reell symmetrisch. Sein
eindimensionaler orthogonaler Kern wird wegen [P,A]=0 von A erhalten.
Auf einer reellen invarianten Geraden hat eine schiefsymmetrische Matrix
Eigenwert null. Für a!=0 ist ker A genau span(a). Somit ist ker P=span(a)
und P eindeutig S. Umgekehrt erfüllt S alle Bedingungen.

Ohne die Rangforderung bleiben 0, der Achsenprojektor aa^T/Omega²,
S und I als reelle orthogonale kommutierende Projektoren. Ohne die
Reellheitsbedingung gibt es wegen der drei verschiedenen Eigenwerte
m,m+Omega,m-Omega drei unterschiedliche kommutierende Rang-zwei-
Spektralprojektoren. Dynamik allein wählt S also nicht eindeutig aus.

Die Darstellung kann kovariant unter realen orthogonalen Basiswechseln
formuliert werden: A -> O A O^T führt S -> O S O^T. Unter allgemeinen
komplexen unitären Änderungen muss die reelle Struktur als antiunitäre
Abbildung mittransportiert werden; bloß P*=P in der alten Basis festzuhalten
wäre ein zusätzlich bevorzugter Frame.

Dieser Befund erklärt genauer, welche zusätzliche Begründung die frühere
Ebene tatsächlich auswählt: gemeinsamer Generator, begründete reelle
Struktur UND begründeter Rang. Es ist keine aus dem Paper gewonnene
Auswahl von P_C7 oder eine Erklärung der Zahl 7.

## 6. Zweite Kopplung als diskriminierender Test

Soll derselbe reelle Rang-zwei-Projektor zusätzlich mit iA(b) kommutieren,
muss seine Kerngerade auch die Achse b sein. Bei nichtverschwindenden,
nichtparallelen a,b ist das unmöglich. Bei parallelen Achsen bleibt S
erhalten, ohne dass eine neue physikalische Auswahl hinzukommt.

Damit ist der positive Versuch nicht gegen beliebige weitere native
Generatoren abgesichert. Die frühere Closure-Verträglichkeitsprüfung
lieferte für ihren speziellen Ansatz bereits genau eine solche zusätzliche
Störung. Ein einziges erfolgreiches Rotationsmodell beweist keine
gemeinsame native Invarianz.

## 7. Falls nur näherungsweise Closure existiert

Ein mathematisch sauberer, aber noch nicht physikalisch bestimmter Ansatz
wäre bei festgelegtem Rang r und dimensionslos normierten A_j

    F(P)=sum_j w_j ||[A_j,P]||_F²,    w_j>0.

Auf der kompakten endlichen Menge orthogonaler Rang-r-Projektoren existiert
ein Minimum. F=0 gilt genau bei gemeinsamer Reduktion aller A_j; bei F>0
liegt nur eine bestmögliche Näherung für die gewählten Gewichte vor.
Ohne begründeten Rang sind 0,I triviale Minima. Ohne begründete Gewichte,
Normierung, Metrik und Wirkung wäre das lediglich eine Anpassung.
Es wird hier kein Minimum als nativer P_C7 ausgegeben. Insbesondere wäre
die Übernahme der Koordinaten-Frobeniusnorm keine allgemeine Lorentz-
invariante physikalische Auswahlregel.

## 8. Konsequenz und nächster Übergang

Die Versuche unterscheiden jetzt drei Möglichkeiten:

1. Gemeinsame Dynamik liefert nur den ganzen Raum: Dann wäre ein einzelner
   kleinerer geschlossener Frame-Sektor die falsche Forderung.
2. Die Symmetrie erhält eine Familie aus Partnersektoren: Dann kann ihre
   gleichgewichtete Mischung neutral sein, ohne selbst P_C7 zu sein.
3. Ein kleinerer Sektor wird durch Dynamik plus zusätzliche Struktur
   ausgewählt: Dann sind diese Struktur und sein Rang physisch herzuleiten,
   und alle weiteren nativen Kopplungen müssen ihn ebenfalls erhalten.

Am vorhandenen Doublet ist Möglichkeit 2 konkret nachgewiesen. Für den
deklarierten Dreimodenkandidaten ist Möglichkeit 3 bedingt bewiesen.
Eine gemeinsame 16x16-Operatorfamilie für die tatsächliche native Auswahl
ist weiterhin nicht ausgewertet. Das ist die verbleibende Eingabe, keine
durch zusätzliche algebraische Beispiele ersetzbare Rechnung.

Für die Frame-Vermutung bedeutet das: Ein einzelner bevorzugter Port
könnte tatsächlich eine Symmetrie der Partnerfamilie verdecken. Seine
Mischung erklärt dann einen neutralen Zustand, jedoch keine automatische
Reparatur der Closure-Herleitung oder der Vakuumenergie. Eine stationäre
symmetrische Dichtematrix braucht noch eine physische Präparation oder
Auswahldynamik. Energieoffset, Reservoir und gravitative Wirkung bleiben
separate Verpflichtungen. OP5 bleibt offen.

## 9. Belege, Prüfung und unabhängige Gegenprüfung

Alle neuen Ergebnisse sind exakte endliche analytische Ableitungen:
Pauli-Kommutanten, Portvertauschung, Rang-zwei-Kernargument und der
nichtparallele Achsentest. Es wurde kein numerisches Experiment oder
keine native Parameteranpassung durchgeführt.

Primäre Quellen: `sources/research/parts/native-operator-link.tex`,
`sources/research/parts/v470/12_structural_core.tex` (T4) und
`sources/research/parts/v490-post-release-layers.tex` (r05.1, r28).
Die vorherige genealogische Prüfung steht in
`OP5_M16_PC7_Frame_Origin_Audit.md`.

Die unabhängige analytische Prüfung der Doublet-Symmetrie in
`OP5_Symmetry_Sector_Selection_Independent.md` wurde gelesen und mit der
vorliegenden Ableitung abgeglichen. Sie bestätigt die Pauli-Klassifikation
einschließlich des entarteten M, komplexer sigma_y-Eigenprojektoren,
reeller Bereichsbeschränkung, gleichzeitiger Zustandsinvarianz und des
Unterschieds zwischen individueller Invarianz und Permutation einer Familie.
Die drei dort dokumentierten Quellenfingerprints werden zusätzlich im
begleitenden Provenienz-Snapshot mit den aktuellen Dateien abgeglichen.
