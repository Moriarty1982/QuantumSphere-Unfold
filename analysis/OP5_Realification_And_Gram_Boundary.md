# OP5: Realifizierung geschlossen, Informationsgrenze des Zustandsreadouts

Checkpoint `OP5-REALIFICATION-GRAM-BOUNDARY-2026-10-26`.
Git-Basis `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Lokale analytische Fortsetzung; keine Manuskriptänderung oder OP5-Schließung.

## 1. Korrektur des vorherigen Befunds

Die Übersetzung zwischen J_B=iK auf dem komplexen Feld und dem reellen
Doublet-Spaltentausch ist **nicht** fehlend. Sie steht ausdrücklich in
`sources/research/parts/v490-post-release-layers.tex`, r04.1,
`subsec:v490-r04-doublet`. Unsere vorige Vergleichsnotiz hatte diese
vorhandene Passage nicht berücksichtigt und die konkrete Lücke zu weit
formuliert. Der allgemeine Typunterschied bleibt mathematisch richtig,
wird hier aber durch eine angegebene Realifizierung erklärt.

Offen bleibt die weitere Verbindung zur vollständigen M16, P_C7 und den
HS(5)-Seiten. Außerdem ist der anschließende Gram-/Zustandsreadout nicht
invertierbar. An dieser Stelle lassen sich jetzt konkrete Grenzen für
Frame-Wechsel und Frame-Mischung nachweisen.

## 2. Exaktes Wörterbuch ohne zusätzliche Frame-Annahme

Für z=E+iB mit reellen räumlichen Vektoren E,B setze

    R(z)=F=[E | B] in R^(3x2),
    R_alpha=[[cos alpha,-sin alpha],[sin alpha,cos alpha]].

Die Abbildung R ist eine reelllineare Bijektion von C³ (als reellem Raum)
nach R^(3x2). Sie ist keine komplexlineare Abbildung in einen bereits
vorgegebenen anderen komplexen Raum. Direkte Substitution ergibt

    R(exp(i alpha)z)=F R_alpha^T,
    R(bar z)=F sigma_z,
    R(i bar z)=F sigma_x,
    R(-z)=-F.

Die originale Multiplikation mit i ist auf F die komplexe Struktur
I_0:F -> F R_(pi/2)^T mit I_0²=-I. Der Spaltentausch anticommutes mit
I_0; genau darin bleibt die ursprüngliche Antilinearität erhalten.

Der ursprüngliche HC-Ausdruck C(z)=(z+i bar z)/2 wird zu

    R(C(z))=F C_+,    C_+=(I+sigma_x)/2.

Sein Bild hat E=B. Das Partnerbild hat E=-B. Beide sind reelle
Unterräume; Multiplikation mit dem originalen i vertauscht sie. Sie sind
keine komplexen Unterräume des ursprünglichen C³. Ihre Komplexifizierung
oder eine Verwendung als abstrakte komplexe Zwei-Port-Hilberträume ist
eine zusätzliche Konstruktion, keine unveränderte Rückübersetzung.

Damit sind die beiden J_B-Schreibweisen konsistent. Ein wechselndes
Linearitätslabel allein ist hier kein nachgewiesener falscher Frame.

## 3. Konsequenz für die Doublet-Portgewichtung

Die Quelle r05.1 lässt auf den reellen Portkoordinaten

    M_port=a I+b sigma_x

zu. Auf dem ursprünglichen komplexen Feld ist dieselbe reelllineare
Operation

    z -> a z+b i bar z.

Für reelles b!=0 ist sie nicht komplexlinear in der ursprünglichen
komplexen Struktur. Würde man zusätzlich komplexlinearen Transport in
genau dieser Struktur fordern, bliebe in dieser realen 2x2-Familie nur
b=0, also skalare Gewichtung.

Das widerspricht r05 nicht: Dort werden ausdrücklich reale Matrizen
klassifiziert und die volle M16 gerade nicht identifiziert. Es begrenzt
aber die Übertragung der Portgewichtung auf einen komplexen Hamilton-
oder M16-Operator. Eine solche Übertragung braucht die tatsächlich
verwendete komplexe Struktur und den gemeinsamen Träger.

## 4. Zweiter Übergang: F -> G -> rho verliert Information

Die Quelle r04.2 setzt

    G=F^T F=[[|E|²,E.B],[E.B,|B|²]],
    u=Tr(G)/2,    s=z.z,
    rho=G/Tr(G) für F!=0.

G ist positiv semidefinit und enthält drei reelle Werte. F hat sechs
reelle Komponenten. Alle räumlichen orthogonalen Linkstransformationen
F->O F lassen G unverändert. Insbesondere verschwinden absolute räumliche
Orientierung und Richtung des Poyntingvektors aus G. Die Normierung zu rho
entfernt zusätzlich die Gesamtintensität u. Beim verschwindenden Feld F=0 ist rho
nicht definiert.

Für einen einzelnen reellen Feldwert gilt tatsächlich

    det G=|E cross B|²,
    rho=I/2 iff |E|=|B| und E.B=0 (bei F!=0).

Das ist die Bedingung für ein nichtverschwindendes lichtartiges Feld im elektromagnetischen
Modell, nicht die Behauptung verschwindender Feldenergie. Die Quelle
selbst hält in r04 fest, dass F die Flussrichtung zusätzlich trägt, die
G nicht sieht.

## 5. Exakter Gegencheck: rho bestimmt keinen allgemeinen Boost

In den üblichen Einheiten c=1 betrachte zwei Felder

    E=(2,0,0),    B_+=(0,1,0),    B_-=(0,-1,0).

Beide besitzen dasselbe G=diag(4,1), dieselbe Energiegröße u=5/2 und
rho=diag(4/5,1/5). Ihre Flüsse sind jedoch S_+=(0,0,2) und S_-=(0,0,-2).

Für denselben passiven Boost mit v=(0,0,1/3) benutze die Konvention

    E'_perp=gamma(E+v cross B),
    B'_perp=gamma(B-v cross E),    gamma²=9/8.

Direktes Einsetzen liefert

    G'_+=diag(25/8,1/8),    u'_+=13/8,
    G'_-=diag(49/8,25/8),   u'_-=37/8,
    rho'_+=diag(25/26,1/26),
    rho'_-=diag(49/74,25/74).

In beiden Fällen bleibt |E'|²-|B'|²=3 erhalten, wie erforderlich.
Gleiche Eingangsrho und sogar gleiches G liefern also unter demselben
gerichteten Boost verschiedene Ausgangsrho. Es gibt keine allgemein
wohldefinierte Boost-Abbildung nur auf dem gesamten reduzierten rho-Disk,
die diese beiden Fälle ohne zusätzliche Orientierungsdaten reproduziert.

Das ist keine Verletzung der Kovarianz: Bei gemeinsamer Rotation von Feld
UND Beobachter transformiert das ganze Experiment konsistent. Das
Gegenbeispiel hält den Beobachterboost fest und zeigt den vorangegangenen
Informationsverlust der Reduktion. Die Quelle r04.1 sagt bereits, dass
Boosts nicht als bloße rechte Doublet-Matrix wirken.

Für rechte reine Portoperationen F->F L ist der reduzierte Readout dagegen
geschlossen: G'=L^T G L und rho'=L^T rho L/Tr(L^T rho L), sofern der
Nenner nicht null ist. Daraus folgt nicht dieselbe Eigenschaft für Boosts.

## 6. Exakter Gegencheck: eine neutrale Mischung ist nicht ein einzelnes lichtartiges Feld

Betrachte ein gleichgewichtetes Ensemble zweier statischer Feldwerte:

    F_1=[e_x | 0],    F_2=[0 | e_x].

Für beide ist u=1/2 und E cross B=0. Gemittelt erhält man

    G_ensemble=(G_1+G_2)/2=I/2,
    rho_ensemble=I/2,    mittlerer Fluss=0.

Ein einzelner Feldwert

    F_null=[e_x/sqrt(2) | e_y/sqrt(2)]

hat genau dasselbe G=I/2 und dieselbe Intensität u=1/2, aber

    E cross B=e_z/2.

Der Einzelwert ist null und trägt gerichteten Fluss; das Ensemble ist
eine Mischung zweier nichtnuller Feldwerte mit verschwindendem mittleren
Fluss. Insbesondere ist sqrt(det G_ensemble)=1/2 nicht der Betrag des
gemittelten Flusses, der hier null ist. Die Einzelwert-Identität darf
nicht nach einer statistischen Mittelung unverändert eingesetzt werden.

Somit kann rho=I/2 aus verschiedenen physischen Konstruktionen entstehen.
Die Bezeichnung „Photon“ für die Mitte der Einzelwert-Disk macht eine
gemittelte Zustandsmatrix nicht automatisch zu einem einzelnen
propagierenden Photonfeld mit dessen Energie-Impuls-Tensor. Auch ist
ein klassischer Feld-Gramreadout nicht ohne weitere Quantisierung eine
vollständige Einphoton-Dichtematrix.

Dies begrenzt die früheren Qubit-Relaxationsmodelle: Ihre Annäherung an
rho=I/2 ist ein bewiesener Zustandsmodell-Befund unter ihren Annahmen,
keine bereits hergeleitete Entstehung eines physischen Photonfelds oder
eines Vakuumzustands. Dafür fehlen die Lift-Dynamik und volle Feldbilanz.

## 7. Welche Information für einen neuen Referenzsektor bleiben muss

Die sichere Reihenfolge ist jetzt konkreter:

1. Vollständigen Feld-/Trägerzustand samt komplexer Struktur und
   physischer Vergleichsabbildung bestimmen.
2. Alle relevanten Frame-Abbildungen auf diesem Träger auswerten.
3. Erst danach Gramreadout, Mischung, Projektion und Normierung durchführen;
   die beim Lift benötigten Orientierungs-, Intensitäts- und
   Ensemble-/Korrelationsdaten gesondert behalten.
4. Einen relationalen P_C7 auf dem gemeinsamen Träger bestimmen und seine
   Closure und Transportverträglichkeit prüfen.

Die ursprüngliche Vermutung erhält damit eine überprüfbare Form:
Nicht der konsistent realifizierte J_B ist hier das Problem. Problematisch
wäre die Behandlung eines schon reduzierten Zustandsreadouts als vollständige
Frame- oder Feldinformation. Genau diese Übertragung darf bei M16/P_C7
nicht ohne konkrete Liftabbildung erfolgen. Eine tatsächliche solche
fehlerhafte Berechnung des nativen P_C7 ist weiterhin nicht nachgewiesen,
weil seine gemeinsame numerische Darstellung nicht vorliegt.

## 8. Validierung, Quellenstatus und offene Verpflichtung

Alle Formeln wurden analytisch durch direkte Real-/Imaginärzerlegung,
Gramprodukte, die angegebenen rationalen Boostwerte und die beiden
Ensemble-Feldwerte geprüft. Keine numerischen Experimente oder neuen
Parameterfits. Die unabhängige Prüfung steht in
`OP5_Realification_Gram_Independent.md`.

Quelle: `sources/research/parts/v490-post-release-layers.tex`, r03.3–4,
r04.1–3, r05.1, r28-Korrektur und r40-Modell. Der Realifizierungsbefund
bestätigt die vorhandene r04-Passage; er ist keine neue native Konstruktion.

Die Verbindung zur vollständigen M16/P_C7, dem unabhängigen Taktgeber,
den HS(5)-Seiten, positiver physischer Probe-Norm und rückgekoppelter
Feld-/Gravitationsdynamik bleibt offen. Der Fortschritt besteht in einer
geschlossenen lokalen Darstellungsbrücke und einer konkret bewiesenen
Grenze der folgenden Informationsreduktion, nicht in einer Lambda-Lösung.
