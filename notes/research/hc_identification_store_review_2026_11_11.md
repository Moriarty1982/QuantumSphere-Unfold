# HC-Identifikationszweig – mathematische Selbstprüfung und Store-Abgleich

11. November 2026. Selbstprüfung durch Codex am Original sources/research/parts/hc-mass-identification.tex, SHA256 4a2cecf409f75355ea3c49e8191993a4cb4019d8c997eb0a64e4674a62301f4c. Die fünf Propositionen werden unter ihren angegebenen Hypothesen bewertet. Keine unabhängige Begutachtung und kein formales Beweisassistentenzertifikat.

## Quellen und Domänen

Gelesen wurden die fünf Originalbeweise, die vorausgehende Koide-Bedingung und analysis/HC_Lepton_Readout_Identification.md. Ausgangsrahmen ist eine ausdrücklich reelle Hilbert-Realisierung mit orthogonaler Involution J und C=(I+J)/2. Die native komplexe beziehungsweise antiunitäre Lesart ist damit nicht automatisch identifiziert. Der Wurzelraum ist euklidisches R³ mit e=(1,1,1)/sqrt(3).

Die kuratierten Aussageblöcke werden wörtlich mit den inneren Propositionstexten des Gesamtimports abgeglichen. Quellenübereinstimmung, mathematische Beweiszuordnung, technische Ressourcen und physikalische Anschlussstellen sind eigene Beziehungen.

## H1 – Normkontrollierter Abstieg

Label v480:hc-mass-descent. Für reelles Hilbert-H, orthogonale Involution J und beschränkte Coisometrie B nach R³ mit BB*=I ist die J-Invarianz von ker B hinreichend für J_m=BJB*, dessen Selbstadjungiertheit und Involutivität sowie BC=C_m B. Das Intertwining BJ=J_m B erfordert umgekehrt einen invarianten Kern und bestimmt J_m eindeutig.

Urteil **proved as written**. B*B ist die orthogonale Projektion E auf (ker B) senkrecht. J ist selbstadjungiert und erhält wegen der Kerninvarianz beide orthogonalen Teilräume; folglich JE=EJ. Daher ist J_m²=BJEJB*=BEB*=I. Die Identität J_m B=BJE=BJ folgt, weil B J auf ker B verschwindet. Mittelung liefert die Projektoridentität. Für die Umkehrung genügt Bk=0; Surjektivität liefert Eindeutigkeit. Der Beweis funktioniert auch für unendlichdimensionales H, da die beteiligten Operatoren beschränkt sind.

Dies ist ein bedingtes Transferresultat. Weder die Existenz des physikalisch richtigen B noch ein natives Saatobjekt oder eine Massenauslesung folgt aus dem Satz.

## H2 – Verlust des ungeraden Eingangs

Label v480:hc-mass-odd-obstruction. Für Jf=−f ist Cf=0, daher verschwinden BCf und jedes F(Cf) mit F(0)=0. Für einen J-fixen Seed mit Bf₀=e und gültigem abgestiegenem linearem Intertwining wird der nichtnullige Wurzelausgang symmetrisch und hat K=1/3.

Urteil **proved as written** unter der im Text genannten abgestiegenen Route für den zweiten Teil. Der erste Teil ist direkt C f=(f+Jf)/2. Im zweiten Teil gilt J_m e=BJf₀=e und C_m e=e. Ein affiner Offset, ein Residualreadout oder eine zusätzliche Kopplung liegt außerhalb der ausgeschlossenen reinen Ausleseroute. Die Abhängigkeit des zweiten Teils von H1 muss im Argumentbaum ausdrücklich erhalten bleiben.

## H3 – Äquivariante Auslesung eines fixen Eingangs

Label v480:hc-mass-equivariant-obstruction. Auf einem unter U erhaltenen Zustandsbereich sei F(Uf)=P F(f) für die zyklische Permutation P der drei Wurzelkoordinaten. Ist Uf₀=f₀, so ist F(f₀) ein konstantes Tripel und bei nichtnulligen nichtnegativen Hauptwurzeln K=1/3.

Urteil **proved as written**. P F(f₀)=F(f₀), und der Fixraum des Dreizyklus besteht aus konstanten Tripeln. Linearität von F wird nicht benötigt. Die Generationssymmetrie U ist von der Involution J zu unterscheiden. Eine nichtlineare, aber weiterhin äquivariante Auslesung umgeht diese Sperre am fixen Eingang nicht.

## H4 – Normgrenze der geschlossenen Triole

Label v480:hc-mass-triole-bound. In einem normierten Raum gelte z₀+z₁+z₂=0 bei mindestens einem nichtnulligen Eintrag. Unter dem zusätzlichen Massengesetz m_i=kappa ||z_i||² mit gemeinsamem positivem kappa ist 1/3≤K≤1/2.

Urteil **proved as written**. Für r_i=||z_i|| und s=sum r_i>0 gibt die Dreiecksungleichung r_i≤s/2. Summation von r_i²≤(s/2)r_i liefert die Obergrenze. Die skalare Cauchy–Schwarz-Ungleichung auf den drei reellen Normwerten liefert die Untergrenze. Ein inneres Produkt auf dem ursprünglichen Raum wird nicht benötigt. Die Obergrenze ist etwa für (v,−v,0) erreicht. Die Sperre gilt für das ausdrücklich angesetzte gemeinsame Normgesetz; sie schließt andere Kopplungen nicht aus.

## H5 – Anpassungsfreiheit der HC-Form

Label v480:hc-mass-fit-freedom. Für jedes nichtnullige nichtnegative x in R³ existieren eine orthogonale Involution J_x und alpha_x>0 mit x=alpha_x(I+J_x)e/2.

Urteil **proved as written** mit dem vorher festgelegten normierten e. C_x=xx^T/||x||² ist eine orthogonale Rang-eins-Projektion. J_x=2C_x−I ist eine orthogonale Involution. Wegen s=sum x_i>0 gilt C_x e=sx/(sqrt(3)||x||²); die angegebene Wahl alpha_x=sqrt(3)||x||²/s ergibt x. Verschwindende einzelne Komponenten sind zulässig. Die freie Anpassung nach Kenntnis von x ist gerade kein unabhängiges Spektralgesetz.

## Argumentbaum und Anschluss an Koide

| Aussage | Erforderliche lokale Daten | Beweiszuordnung |
|---|---|---|
| H1 | Reelles Hilbert-HC, Coisometrie und invariantes ker B | Originalbeweis H1 |
| H2 | HC-Zerlegung, F(0)=0; für den fixen Teil zusätzlich H1 und Bf₀=e | Originalbeweis H2 |
| H3 | Admittierter Bereich, U/P-Äquivarianz, fixer Eingang; für K nichtnegative Hauptwurzeln | Originalbeweis H3 |
| H4 | Normierter Raum, geschlossene Triole, gemeinsamer positiver Norm-Massenfaktor | Originalbeweis H4 |
| H5 | Euklidischer Hauptwurzelraum, e und x≠0 | Originalbeweis H5 |

H1 spezialisiert den Zusammenhang mit der bedingten Koide-HC-Realisierung. Erst wenn ein unabhängiger Seed Bf₀=e und das physikalische Gesetz x=alpha B C f₀ mit positiver nichtnulliger Auslesung geliefert werden, ergibt h=<B*e,J B*e>=0 das Koide-Kriterium. Diese Verbindung ist als bedingte Spezialisierung mit ihren zusätzlichen Hypothesen zu registrieren. Sie bestätigt keine native B-Konstruktion.

Der Residualansatz des Quelltexts ist ausdrücklich eine zusätzliche effektive Möglichkeit. Er setzt D_beta, Generationenzustände, eine positive Massenskala und zulässige Domänen voraus. Die vorliegende Prüfung leitet diese Daten nicht her.

## Präzise offene Pflichten

1. Native scalar-field interpretation. Die reelle Hilbert-Realisierung und das J-Intertwining müssen mit der tatsächlich gewählten nativen unitären beziehungsweise antiunitären Lesart verbunden werden.
2. Native readout and seed. B, seine Coisometrie/Kerninvarianz, f₀ sowie das positive nichtnullige Wurzelgesetz müssen unabhängig geliefert werden.
3. Native residual generation coupling. Falls die Residualroute verwendet wird, müssen D_beta und die zugelassenen Generationenzustände mit ihren Domänen konstruiert werden.
4. Selection and mass scale. Die native Kopplung muss Koide-Normgesetz, zulässige Phase und absolute Skala liefern. Ein nach den Zielmassen gewählter Operator erfüllt diese Pflicht nicht.

Diese Pflichten ergänzen die offenen Koide-Guards. Die mathematischen Ausschlusssätze schließen nur die angegebenen direkten Routen.

## Reproduzierte Prüfungen und Provenienz

python -m unittest discover -s scripts/qsc_audit/tests -p test_hc_mass_identification.py war mit 18 erfolgreichen Tests abgeschlossen. Sie prüfen endliche algebraische Beispiele und Grenzen der Identifikation. Die fünf allgemeinen Urteile beruhen zusätzlich auf der oben rekonstruierten Selbstprüfung. Keine neuen empirischen Daten, keine Aktivierung von OP3 oder anderen OPs.
