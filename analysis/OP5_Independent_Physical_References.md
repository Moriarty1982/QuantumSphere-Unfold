# OP5: unabhängige physische Beiträge statt mehrfacher Frame-Auslesung

Checkpoint `OP5-INDEPENDENT-PHYSICAL-REFERENCES-2026-10-26`.
Git-Basis `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Auftrag: Die im Paper verwendeten Paarungen auf tatsächliche zusätzliche
physische Eingaben prüfen und für einen zulässigen Fall eine gemeinsame
Referenz herleiten. Lokale analytische Notiz; keine Manuskriptänderung.

## 1. Ergebnis

Nicht alle Partnerbilder sind zusätzliche physische Beiträge. Die
Dualitätsabbildung eines Feldes liefert denselben Energie-Impuls-Tensor;
die HS(5)-Verdopplung bezeichnet zunächst zwei Informationsrollen. Das
Ancilla-Modell enthält dagegen ausdrücklich ein zusätzliches Teilsystem,
setzt aber dessen Präparation voraus. Die triadischen Probe-Moden sind
getrennte gekoppelte Feldkomponenten; ihre gemeinsame physische
Energie-Impuls-Zuordnung ist in den geprüften Passagen nicht ausgewertet.

Ein klar positiver bedingter Fall ist vollständig lösbar: Zwei positive,
nichtparallele lokale Nullströme bestimmen einen eindeutigen zukünftigen
Beobachter ohne Energiefluss. Dafür braucht man weder einen ausgezeichneten
Photon-Frame noch willkürlich gleiche Gewichte. Der Beobachter folgt aus
den tatsächlich gelieferten Energiedichten und Richtungen.

Diese Referenz ist ein Raumzeit-Beobachter, kein bereits bestimmter
interner P_C7. Die Verbindung zum nativen M16-/Projektorproblem bleibt
eine eigene, genau benannte Abbildung.

## 2. Drei verschiedene Bedeutungen von Unabhängigkeit

Zu unterscheiden sind:

1. **Verschiedene Beschreibungen:** Ein einzelner Zustand oder Tensor wird
   transformiert und erneut ausgelesen. Derselbe physische Inhalt wird
   dadurch nicht zweimal zur Gesamtenergie addiert.
2. **Zusätzliches physisches Teilsystem:** Ein zweiter Träger oder ein
   Messgerät wird tatsächlich präpariert. Er besitzt eigene Freiheitsgrade,
   Energie und gegebenenfalls Kopplungsenergie. Seine Präparation kann
   trotzdem deterministisch vom ersten System abhängen.
3. **Zusätzliche Information für die Referenzwahl:** Der zweite Beitrag
   verändert die relevante Tensor-/Operatorstruktur so, dass vorherige
   Mehrdeutigkeiten aufgehoben werden. Eine physisch zusätzliche Kopie
   mit proportionalem Stress muss diese Bedingung nicht erfüllen.

Statistische Unabhängigkeit ist nochmals eine eigene Bedingung. Ein
Produktzustand nimmt sie für den angegebenen Anfangszeitpunkt an; sie
folgt weder aus verschiedenen Namen noch aus einem Frame-Wechsel.

## 3. Quellenabgleich der tatsächlich verwendeten Paarungen

| Paarung | Was die Quelle liefert | Was für einen neuen physischen Beitrag fehlt |
|---|---|---|
| z und iz; gegenüberliegende Diskpunkte | `v490-post-release-layers.tex`, r28-Korrektur: explizite Dualitätsabbildung | Als Darstellungsrelation kein zweiter Energieträger; selbst eine separat realisierte Kopie hat denselben lokalen Stress und liefert keine neue Flussrichtung. |
| z und J_B z | r04.1/r03: bestimmtes reelles Gegenbild mit umgekehrtem Poyntingfluss | Eine physische zweite Quelle und die Regeln für inkohärente Addition oder kohärente Überlagerung werden durch die Abbildung allein nicht erzeugt. |
| rho tensor sigma_y rho sigma_y | r28.1(c): System und zusätzliches Ancilla im Produktzustand, dann Austausch | Präparation, volle Energiebilanz und physische Feld-/Raumzeitzuordnung der Ancilla sind Zusatzdaten. Kein bloßer passiver Frame-Wechsel. |
| Frisches Reservoir nach jedem Schritt | r28.2(c): ausdrücklich nachgeliefertes Reservoir | Versorgung, Quellen und Rückwirkung müssen mitgeführt werden; seine Wirkung ist nicht kostenloser Energieausgleich. |
| Psi_1,Psi_2,Psi_perp | `v470/10_sphaera_and_physics.tex`, `prop:triadic-two-probe`: getrennte gekoppelte Komponenten | Zulässige gemeinsame Anfangsdaten, Adjungierte und Energie-Impuls aus einer gemeinsamen konsistenten Wirkung müssen ausgewertet werden; Wechselwirkungsstress darf nicht verschwinden. |
| Psi_ART,Psi_QFT und gemischte Bilineare | `v470/13_hc_hypotheses.tex`, „Probe-tensor readout“ und Meta-Generator-Hypothese | Ein explizit erzeugter gemeinsamer Tensor und Nachweis, dass zwei Regime nicht denselben Inhalt doppelt zählen. |
| HS(5) Front/Back | `v470/32_atlas_and_op_promotion.tex`, „HS(5) two-sided duplication“ | Die Rollen Readout/Frame/Sprache und Struktur/Wirkung/Feld sind noch keine zwei berechneten Energieträger; ein gemeinsamer physischer Vergleich fehlt. |

Das ist eine Typ- und Eingabenprüfung der benannten Passagen. Sie behauptet
nicht, dass gekoppelte Moden wegen gemeinsamer Ontologie keine verschiedenen
Freiheitsgrade haben könnten. Ebenso beweist eine Tensorprodukt-Schreibweise
allein keine native Präparationsvorschrift für ein beliebiges unbekanntes
Eingangssystem.

Wichtig: Aus D(rho) ALLEIN folgt weder gleicher noch entgegengesetzter
physischer Stress, weil rho Energie und Richtung bereits reduziert hat.
Die Gleichheit des Maxwell-Stress gilt für die ausdrücklich festgelegte
Feldrealisierung z_dev=i z_sys. Andere physische Realisierungen desselben
reduzierten Ancilla-Zustands benötigen eigene Feld- und Energiedaten.

## 4. Vollständig lösbarer Fall: zwei lokale positive Nullströme

Erklärte zusätzliche physische Voraussetzungen: gegebene lokale
Lorentzmetrik mit Signatur (-+++), c=1, zukünftige Nullrichtungen k,l,
k und l nicht parallel, positive Dichtekoeffizienten a,b. Die hier
betrachtete Materie ist ein additiver inkohärenter Zwei-Strom-Sektor ohne
zusätzlichen Wechselwirkungsstress:

    T^{mu nu}=a k^mu k^nu+b l^mu l^nu,
    k²=l²=0,    chi=-k.l>0.

Diese Voraussetzungen sind keine Herleitung nativer Tachyonen. Die
Ströme sind zukünftige positive Nullströme, keine spacelike Bahnen.
Ein zusätzlicher Wechselwirkungstensor müsste die folgende Eigenanalyse
entsprechend verändern.

Definiere

    V=sqrt(a) k+sqrt(b) l,
    N=sqrt(2 sqrt(a b) chi),
    U=V/N,    epsilon=sqrt(a b) chi.

Dann ist U ein zukünftiger normierter zeitartiger Beobachter. Denn

    V²=-2 sqrt(a b) chi,    U²=-1.

Direkte Anwendung des gemischten Tensors ergibt

    T^mu{}_nu V^nu
      =-a sqrt(b) chi k^mu-b sqrt(a) chi l^mu
      =-epsilon V^mu.

Also gilt T^mu{}_nu U^nu=-epsilon U^mu und die vom Beobachter U
gemessene Energiedichte ist epsilon>0. Sein räumlicher Energiefluss
verschwindet exakt.

## 5. Eindeutigkeit und Kovarianz

Der zweite normierte Vektor

    Z=(sqrt(a) k-sqrt(b) l)/N

erfüllt Z²=1, U.Z=0 und T Z=+epsilon Z. Auf dem zweidimensionalen
orthogonalen Komplement von span(k,l) verschwindet T. Die vier
gemischten Eigenwerte sind daher

    -epsilon, +epsilon, 0, 0.

Weil epsilon>0 ist der negative Eigenwert einfach, und sein Eigenraum
ist die zeitartige Gerade U. Die Forderung „zukünftig und normiert“
wählt genau einen Beobachter aus. Ein möglicher Eigenvektor im
Null-Eigenraum ist räumlich; er liefert keine weitere zeitartige
Nullfluss-Referenz.

Unter einer gemeinsamen eigentlichen zukünftigen Lorentztransformation
transformiert U als Vektor. Die Formel ist auch unabhängig von der
Normierung der beiden Nullstrahlen: k->c k, a->a/c² mit c>0 lässt
sqrt(a)k unverändert, entsprechend für l. Gleiche Gewichte werden nicht
vorausgesetzt. Die physische Summe T bestimmt die Gewichtung.

Für parallele zukünftige Richtungen ist chi=0. Dann bleibt ein einzelner
Nullstrahl und es gibt keinen zeitartigen Ruhebeobachter. Dasselbe gilt,
wenn einer der positiven Beiträge verschwindet. Der Grenzübergang kann
singulär sein; die Formel wird dort nicht durch Division durch null
fortgesetzt. Bei negativen Koeffizienten gilt der Satz nicht.

## 6. Explizite Referenz im gegebenen Beobachterrahmen

Normiere k=(1,n_1), l=(1,n_2) mit |n_1|=|n_2|=1. Dann sind a,b die
lokalen Energiedichten in diesem Rahmen. Die Geschwindigkeit der
gefundenen Referenz ist

    v_U=(sqrt(a)n_1+sqrt(b)n_2)/(sqrt(a)+sqrt(b)).

Bei nichtparallelen Richtungen und a,b>0 ist |v_U|<1. Für exakt
gegenläufige Ströme n_1=e_z,n_2=-e_z folgt

    v_U=(sqrt(a)-sqrt(b))/(sqrt(a)+sqrt(b)),
    eta_U=(1/4) log(a/b),
    epsilon=2 sqrt(a b).

Kontrollfall a=4,b=1: v_U=1/3 und epsilon=4. Das sind keine an das
Paper angepassten Werte, sondern ein vollständig deklarierter Beispieltest.
Der gegenüberliegende Spezialfall wurde schon in
`OP5_Neutral_Frame_Candidates.md` behandelt. Neu ist hier die gemeinsame
Quelleneinordnung und die ausgeschriebene allgemeine nichtkollineare
Existenz-/Eindeutigkeitsprüfung, nicht die Behauptung eines neuen
physikalischen Ruheframe-Verfahrens.

Lokale Strahldichten sind von vollständigen Paketimpulsen zu unterscheiden.
Für zwei gegenläufige Pakete mit Energien E_+,E_- liefert der normierte
Gesamtvierimpuls stattdessen eta_COM=(1/2)log(E_+/E_-). Man darf diese
Paketgewichte nicht ohne Volumen-/Dichteabbildung in die lokale
Tensorformel einsetzen. Genau diese Unterscheidung war im früheren
Neutral-Frame-Audit bereits festgehalten.

## 7. Was diese Konstruktion für P_C7 liefert und was nicht

Aus U entsteht ein kovarianter zeitartiger Raumzeitprojektor

    (P_time)^mu{}_nu=-U^mu U_nu,
    P_time²=P_time,

sowie der räumliche Projektor h=I+U U_flat. Beide sind Tensoren auf
dem Raumzeit-Tangentialraum mit Lorentzmetrik. Sie sind nicht der positive
interne Meta-Septum-Projektor auf dem 16-Moden-Träger. Eine Gleichsetzung
wäre ein Typfehler. Es müsste eine native Abbildung angegeben werden,
die die gemeinsame Raumzeitreferenz mit der internen Operatorfamilie
M16, T und dem Taktgeber verknüpft.

Damit ist ein möglicher neutraler Beobachter aus tatsächlichen physischen
Beiträgen hergeleitet. Die Herleitung braucht aber zwei entsprechende
Stromdaten, die in den bisherigen Frame-Paaren nicht automatisch vorliegen.
Ein rein darstellungsbezogenes Dualitätspaar ist kein Ersatz dafür.

Auch diese Referenz macht positive Strahlungsenergie nicht zu Vakuum:
Der Zwei-Strom-Tensor hat Spur null. Ein reiner Vakuumtensor -rho_Lambda g
hätte Spur -4 rho_Lambda. Der vorliegende nichtverschwindende positive
Tensor wird daher in keinem Beobachterframe zu einem reinen
kosmologischen Vakuumtensor. Dieses Hindernis war schon im vorigen
Neutral-Frame-Audit festgehalten und wird nicht als neue OP5-Lösung verkauft.

## 8. Präziser verbleibender Arbeitsauftrag im Paper

Die konkrete native Kandidatenroute ist die triadische Probe-Gleichung:
Dort sind getrennte gekoppelte Komponenten wenigstens ausdrücklich
vorhanden. Vor der Referenzwahl müssten deren gemeinsamer physischer
Energie-Impuls-Tensor einschließlich Wechselwirkung, zulässige Zustandsdaten
und Projektion aus der Wirkung ausgewertet werden. Erst dann entscheidet
die Eigenstruktur, ob sie zwei unterscheidbare positive Flüsse, eine
entartete Familie oder gar keinen zeitartigen Nullfluss-Beobachter liefern.

Das Ancilla-/Reservoirmodell bietet eine andere Route mit explizit
zusätzlichen Teilsystemen, benötigt aber Präparations- und Energiebilanzdaten.
Die HS(5)-Rollenverdopplung allein liefert diese Daten nicht. Eine Auswahl
zwischen diesen physischen Realisierungen wird hier nicht durch bloßes
Umbenennen eines Frames vorweggenommen.

## 9. Validierung und Grenzen

Die Algebra wurde exakt durch Nullvektorkontraktionen, die beiden
Eigenvektoren U,Z, Normierung und die Strahlnormierungsfreiheit geprüft.
Der positive und der entartete Fall sind getrennt. Keine numerischen
Fits, keine vorgegebenen nativen Energien und keine gemeinsame
M16/P_C7-Realisierung werden behauptet.

Die unabhängige Prüfung von Quelleneinordnung und Zwei-Strom-Satz steht in
`OP5_Independent_Contributions_Independent.md`. Die Quellenfingerprints
und lokalen Eingaben werden im begleitenden Provenienz-Snapshot gepinnt.
Die unabhängige Notiz wurde vollständig gelesen; Zwei-Strom-Eigenwerte,
Reskalierung, Entartungen, Druck und die Quellenqualifikation für D(rho)
wurden mit dieser Ableitung abgeglichen.
OP5 bleibt offen; die physische Referenzkonstruktion ist nun bedingt
vollständig, ihre native Eingabe und ihr interner Projektorübergang fehlen.
