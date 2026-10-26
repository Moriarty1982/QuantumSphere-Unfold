# OP5: kovarianter ergänzter Readout und die Grenze einer neutralen Referenz

Checkpoint `OP5-COVARIANT-READOUT-COMPLETION-2026-10-26`.
Git-Basis `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Lokale analytische Fortsetzung der Realifizierungs-/Gramprüfung.
Keine Manuskriptänderung oder Lösung der nativen gravitativen Feldgleichung.

## 1. Ergebnis

Im klassischen elektromagnetischen Reading-B-Modell lässt sich der
reduzierte Readout ergänzen: Der vollständige Energie-Impuls-Tensor T und
das komplexe Feldinvariant s bestimmen den Gramreadout für jeden angegebenen
Lorentz-Beobachter. Der vorherige Richtungsverlust lässt sich damit für
diese Aufgabe beheben, ohne willkürlich einen neuen Frame anzusetzen.

Die ergänzten Daten wählen aber noch keinen eindeutigen neutralen
Beobachter. Insbesondere erhält die native korrigierte Gegenabbildung
z->iz den Energie-Impuls-Tensor vollständig. Zwei entgegengesetzte
Diskpunkte sind daher nicht automatisch gegenläufige Energieströme.

Alle Aussagen betreffen den ausdrücklich angegebenen klassischen
Vergleichssektor. Sie identifizieren weder eine native M16 noch P_C7,
ein Quantenmessinstrument oder eine Vakuumenergiedichte.

## 2. Festgelegte Größen und Konventionen

Reelle dreidimensionale Felder E,B in einem lokalen orthonormalen
Beobachterrahmen, z=E+iB, c=1 und positive Standard-Maxwell-Normierung.
Signatur (-+++). Setze

    u=(|E|²+|B|²)/2,    S=E cross B,
    s=z.z=|E|²-|B|²+2i E.B,
    T^{00}=u,    T^{0i}=T^{i0}=S_i,
    T^{ij}=u delta_ij-E_i E_j-B_i B_j.

T ist der hier als Modellannahme verwendete klassische Maxwell-Tensor;
seine Identifikation mit der nativen gravitativen Quelle wird nicht
vorausgesetzt. s ist unter den hier betrachteten eigentlichen,
zeit-orientierungserhaltenden Lorentztransformationen invariant.
Raumspiegelungen und andere orientierungsumkehrende Abbildungen sind
gesondert zu behandeln, insbesondere beim Imaginärteil von s.

Die Lorentzmetrik und Orientierung sind hier Eingaben der lokalen
Vergleichsrechnung, keine aus den internen Zustandsdaten abgeleitete
Raumzeitgeometrie.

Der Quellenanschluss ist `v490-post-release-layers.tex`, r03.3–4 und
r04.1–3 für E,B,u,S,s und den Gramreadout sowie r28 für z->iz. Es wird
keine zusätzliche volle native Einstein-Maxwell-Gleichung eingeführt.

## 3. Exakte Ergänzung: (T,s) statt rho allein

Für den zukünftigen Einheitsbeobachter n mit g(n,n)=-1 ist

    u_n=T^{mu nu} n_mu n_nu,
    G_n=[[u_n+Re(s)/2, Im(s)/2],
         [Im(s)/2, u_n-Re(s)/2]],
    rho_n=G_n/(2u_n)  für u_n>0.

Beweis: Im jeweiligen Beobachterrahmen ist T^{00}=u_n; die reelle und
imaginäre Komponente des invarianten s bestimmen E_n²-B_n² und 2E_n.B_n.
Zusammen mit E_n²+B_n²=2u_n sind genau die drei Einträge von G_n bestimmt.

Für einen vorgegebenen passiven Boost mit Matrix Lambda gilt T'=Lambda
T Lambda^T und s'=s. Daraus folgt G' und rho' eindeutig. Für v in einer
gegebenen räumlichen Richtung lautet insbesondere

    u'=gamma²(u-2 v_i S_i+v_i v_j T^{ij}).

Damit werden die beiden vorherigen Gegenbeispiele korrekt unterschieden:
Die gleiche ursprüngliche rho hatte dort unterschiedliche gerichtete S.
T alleine enthält s nicht vollständig: Eine Dualitätsrotation lässt T
gleich und rotiert s. Deshalb muss für den Gramreadout auch s bzw. die
entsprechende interne Vergleichsinformation erhalten bleiben.

Dies ist eine hinreichende Ergänzung, keine bewiesene minimalparametrische
Repräsentation. Die Daten müssen von zulässigen Einzelwerten oder einem
deklarierten Ensemble stammen; beliebige unabhängig gewählte T,s werden
nicht als physisch zulässiger Einzel-Feldwert ausgegeben. Auch bestimmen
T,s nicht eine eindeutige Feldamplitude oder alle Quanteninformationen.

## 4. Mittelung vor Normierung ist jetzt eindeutig formulierbar

Für ein angegebenes statistisches Ensemble mit Gewichten w_j>=0,
sum w_j=1, auf einem gemeinsamen lokalen Beobachterträger setze

    T_bar=sum_j w_j T_j,    s_bar=sum_j w_j s_j,
    G_bar=sum_j w_j G_j.

Die Formeln aus Abschnitt 3 sind linear vor der Normierung und gelten
deshalb für den gemittelten Gramreadout auch nach einem gemeinsamen Boost.
Der normierte Gesamtreadout ist

    rho_bar=G_bar/Tr G_bar
           =sum_j [w_j u_j/(sum_k w_k u_k)] rho_j.

Er ist im Allgemeinen NICHT sum_j w_j rho_j. Gewichte statistischer
Feldkonfigurationen und Intensitätsgewichte normierter Readouts dürfen
nicht verwechselt werden. Wenn die u_j im Vergleichsrahmen gleich sind,
fallen sie dort zusammen; nach einem gemeinsamen gerichteten Boost muss
dies nicht mehr gelten.

Die Einzel-Feldbeziehung det G=|S|² darf für G_bar nicht mit S_bar
gleichgesetzt werden. Ebenso garantiert s_bar=0 nicht, dass T_bar ein
einziger nuller Strahlungstensor ist. Kohärente Feldüberlagerung ist ein
anderes Experiment: Für E_total=sum E_j und B_total=sum B_j entstehen
Kreuzterme, die durch eine bloße Liste gemittelter Einzel-Tensoren nicht
bestimmt sind. Die Art der Mischung ist daher Teil der Eingabe.

## 5. Die korrigierte Gegenabbildung ist kein Gegenstrom

Die source-native Dualitätsabbildung z->iz bedeutet

    E_D=-B,    B_D=E,    s_D=-s.

Direkt folgt

    u_D=u,
    S_D=(-B) cross E=E cross B=S,
    E_D E_D^T+B_D B_D^T=EE^T+BB^T,
    T_D=T.

Gleichgewichtete statistische Mischung des Feldes mit diesem Partner
liefert daher

    s_bar=0,    G_bar=u I,    rho_bar=I/2,
    T_bar=T,    S_bar=S.

Der Readout wird neutral, der gesamte ursprüngliche Energiefluss bleibt
aber erhalten. Das ist ein direkter Gegencheck gegen die Gleichsetzung
„gegenüberliegende Diskpunkte -> gegenläufige physische Ströme“.

Beispiel: E=2e_x, B=e_y hat u=5/2, S=2e_z und s=3. Sein Dualitätspartner
hat s=-3, aber denselben T und denselben S. Die gleichgewichtete Mischung
hat rho=I/2 und dennoch |S_bar|/u_bar=4/5 statt des Einzel-Nullfeldwerts 1.
Es entsteht damit kein einzelner Lichtstrahl, dessen Flussbetrag gleich
der Energiedichte wäre.

Die ältere andere Involution J_B:(E,B)->(B,E) kehrt S tatsächlich um,
erhält u und den räumlichen Spannungstensor und sendet s->-bar s. Sie
neutralisiert jedoch nicht allgemein beide Blochkoordinaten. Auch hier
sind Disk-Neutralität und Impulsneutralität verschiedene Anforderungen.

## 6. Warum der ergänzte Tensor keinen eindeutigen neutralen Frame liefert

Ein Nullfluss-Beobachter müsste die zeitartige Eigenvektorbedingung

    T^mu{}_nu n^nu=-epsilon n^mu,
    g(n,n)=-1,    n zukunftsgerichtet

erfüllen. Ein eindeutiger solcher Eigenvektor wäre eine physisch begründete
Landau-Referenz. Existenz und Eindeutigkeit sind aber gesondert zu prüfen.

Schon ein reines elektrisches Feld entlang z mit u>0 hat

    T^{mu nu}=diag(u,u,u,-u),
    T^mu{}_nu=diag(-u,u,u,-u).

Alle Beobachter n=(cosh eta,0,0,sinh eta) sind normierte zukünftige
Eigenvektoren zum Eigenwert -u. Sie sehen keinen Energiefluss. Es gibt
also eine ganze eindimensionale Beobachterfamilie statt einer eindeutigen
Ruhe-Referenz. Dieses explizite Gegenbeispiel reicht, um eine universelle
Eindeutigkeit aus T allein zu widerlegen. Ein nichtverschwindendes nulles
Feld hat dagegen einen reinen Nullstrahl-Tensor und keinen zeitartigen
Nullfluss-Beobachter.

Da z und iz dasselbe T besitzen, kann ihre Mischung diese Entartung
nicht aufheben. Sie liefern für die Impulsreferenz keine zwei unabhängigen
physikalischen Informationen. Eine echte zusätzliche nichtkollineare
Stromquelle oder ein weiterer physischer Träger könnte mehr festlegen;
das wäre zusätzliche Dynamik und nicht bloß ein anderes Disklabel.

Für wirklich zwei unabhängige positive gegenläufige Strahlungsströme
war eine Nullfluss-Referenz bereits in `OP5_Neutral_Frame_Candidates.md`
angegeben. Dieses Resultat ist von der vorliegenden Dualitätspaarung
zu unterscheiden; es wird hier nicht als neue Lösung wiederholt.

## 7. Ein engerer Auswahlauftrag für M16 und P_C7

Die Frage „mindestens zwei Referenzen“ muss nun drei Dinge festlegen:

1. Sind es unabhängige physische Träger oder nur zwei Darstellungen
   desselben Tensors? Das Dualitätspaar liefert den zweiten Fall.
2. Soll die Referenz eine statistische Auslese neutralisieren, einen
   Energiefluss ausgleichen oder einen invarianten Operatorsektor wählen?
   Diese drei Kriterien sind nicht äquivalent.
3. Welche Feld-/Trägerdaten bleiben bis zur Bestimmung des Projektors
   erhalten? Für die hier betrachteten Lorentz-Gramreadouts reichen T,s;
   für M16-/Taktgeber-/Seed-Matrixelemente ist weiterhin die gemeinsame
   Operatorrealisierung nötig.

Damit steht eine konkrete verbesserte Eingabe für die Frame-Prüfung zur
Verfügung, aber kein automatisch ausgewählter P_C7. Ein Projektor aus
einer vorausgesetzten neutralen rho würde diese jetzt explizit getrennten
physischen Unterschiede nicht erfassen.

## 8. Prüfung und offene Grenzen

Analytisch geprüft: die Rekonstruktion von G aus u_n,s, die gemeinsame
Lorentztransformation, Intensitätsgewichtung, volle Dualitätsinvarianz
des Maxwell-Tensors und die entartete Nullfluss-Eigenfamilie. Keine
numerischen Experimente, keine native Parameteranpassung.

Unabhängige Gegenprüfung: `OP5_Duality_Stress_Independent.md`.
Diese wurde vollständig gelesen; die zehn Stresskomponenten,
Dualitäts-/J_B-Wirkung, der konkrete Mischkontrollfall und die
Beobachter-Eigenbedingungen stimmen mit der vorliegenden Ableitung überein.
Die vorige Informationsgrenze steht in `OP5_Realification_And_Gram_Boundary.md`.
Die klassische Maxwell-Normierung ist eine erklärte Modellvoraussetzung,
kein Ersatz für die aus der nativen Wirkung zu bestimmende Gravitation.
Energieoffset, gemeinsame M16/P_C7-Darstellung, physische Auswahlregel,
positive Probe-Norm und Feldrückwirkung bleiben offen. OP5 bleibt offen.
