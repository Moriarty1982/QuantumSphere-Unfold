# Koide-Zweig – Quellenabgleich und mathematische Selbstprüfung

11. November 2026. Fokussierte Selbstprüfung durch Codex. Die folgende Bewertung gilt dem ersten Unterabschnitt von sources/research/parts/koide-and-kernel.tex mit SHA256 63fe03eb53ec883292ac09935f65fc04bb4a9f6e7a32870743471cdc294336c7. Sie ist eine dokumentierte mathematische Prüfung mit deklarierten Reviews im Store. Eine unabhängige Begutachtung oder Formalisierung in einem Beweisassistenten wurde hier nicht durchgeführt.

## Quellen und Vorbefunde

Geprüft wurden der aktuelle Originaltext mit vier Propositionen und Beweisen, analysis/Koide_Zero_Kernel_Proof_Audit.md sowie analysis/HC_Lepton_Readout_Identification.md. Der spätere Koide-Überlagerungszweig ist von diesen vier Aussagen zu unterscheiden. Die Suche im QAM-Claimregister findet dazu bedingte Überlagerungsformeln; diese wurden für den vorliegenden Beweisabgleich nicht als MMA-Belege verwendet.

Der Import enthält jede Proposition mit ihrer LaTeX-Umgebung. Die kuratierte Fassung enthält deren inneren Aussageblock einschließlich Label. Für die Zuordnung muss nach Entfernen allein des äußeren proposition-Headers und -Endes exakte Textgleichheit bis auf äußeren Leerraum und Zeilenendkonvention gelten. Diese dokumentarische Übereinstimmung ist eine eigene same-source-as-Beziehung. Sie identifiziert keine unterschiedlichen physikalischen Frames.

## Aussagekarten und Urteile

### K1 – Koide als Gleichnormbedingung

Label v480:koide-equal-norm. Für einen von null verschiedenen Vektor nichtnegativer reeller Hauptwurzeln x in R³ seien A der positive Mittelwert, u=A(1,1,1) und d=x−u. Zu prüfen ist K=1/3+||d||²/(9A²) und die Äquivalenz von K=2/3 mit ||d||²=||u||².

Urteil **proved as written** unter den ausdrücklich genannten Definitionsvoraussetzungen. Die Summenbedingung gibt u·d=0. Daher ist ||x||²=3A²+||d||² und die Nennerquadratsumme 9A²>0. Division und Umstellung ergeben beide Aussagen. Der Nullvektor ist ausgeschlossen; einzelne verschwindende Komponenten sind erlaubt. Die Formel behauptet keine dynamische Auswahl des Normverhältnisses.

### K2 – Bedingte HC-förmige Realisierung

Label v480:koide-hc-mixing. Auf dem deklarierten reellen Wurzelraum sei e normiert symmetrisch, J_m orthogonal und involutiv, C_m=(I+J_m)/2, und x=alpha C_m e nichtnull und komponentenweise nichtnegativ mit alpha>0. Zu prüfen sind h=e·J_m e>−1 und K=2/[3(1+h)].

Urteil **proved as written** unter diesen Hypothesen. Orthogonalität und Involutivität geben J_m*=J_m und machen C_m zum orthogonalen Projektor. Deshalb sind ||C_m e||²=e·C_m e=(1+h)/2>0 und die Summe der Wurzelkomponenten alpha sqrt(3)(1+h)/2. Ihr Verhältnis liefert K. Der Fall h=−1 würde den ausgeschlossenen Nullausgang erzeugen. J_m=I ergibt h=1 und K=1/3. Koide folgt genau bei h=0. Dass der native HC gerade diese Darstellung und diesen Wert liefert, bleibt eine eigene Verpflichtung.

### K3 – Radius und Phase

Label v480:koide-radius-phase. Jeder zulässige Wurzelvektor besitzt die angegebene Kosinusdarstellung mit A>0 und r≥0. Zu prüfen sind K=1/3+r²/6 und die Äquivalenz von Koide mit r=sqrt(2).

Urteil **proved as written**. Die Kosinus- und Sinusvektoren bilden die zweidimensionale Nullsummenebene orthogonal mit Normquadrat 3/2 auf. Die Darstellung von d/A liefert ||d||²=(3/2)A²r². K1 ergibt die Formel. Bei r=0 ist die Phase beliebig. Für r>0 muss der dargestellte Vektor weiterhin nichtnegative Komponenten haben. Freie Wahl von A und theta innerhalb dieser Zulässigkeit wird durch die Koide-Bedingung nicht aufgehoben.

### K4 – Zyklische lineare Symmetriesperre

Label v480:koide-equivariant-obstruction. Sei P die zyklische Permutation auf R³ und T reell linear mit TP=PT. Zu prüfen ist, dass T die symmetrische Linie erhält.

Urteil **proved as written**. Für Pu=u gilt P(Tu)=T(Pu)=Tu. Der Fixraum der zyklischen Permutation besteht genau aus konstanten Tripeln. Der Nullausgang bleibt zulässig für das Lemma, erzeugt aber keine Hierarchie. Dieses Resultat benötigt weder Hauptwurzelpositivität noch eine positive Massenskala. Die bisher kuratierte Abhängigkeit dieser Aussage vom vollständigen positiven Wurzel-Setup ist deshalb als unnötige Voraussetzung zu entfernen. Die eigene reelle lineare Zyklusdefinition genügt.

## Abhängigkeiten und geprüfte Verpflichtungen

| Aussage | Tatsächliche lokale Voraussetzungen | Beweiszuordnung | Urteil |
|---|---|---|---|
| K1 | Nichtnegative nichtnullige Hauptwurzeln und orthogonale Mittelwertzerlegung | Originalbeweis zu K1 | proved as written |
| K2 | Wurzeldomäne, e, orthogonale reelle Involution, nichtnulliger positiver Ausgang | Originalbeweis zu K2 | proved as written |
| K3 | Wurzeldomäne, Basis der Nullsummenebene und K1 | Originalbeweis zu K3 | proved as written |
| K4 | Reelle zyklische Permutation, Linearität und Kommutation | Originalbeweis zu K4 | proved as written |

Die Zuordnung von statement zu Originalbeweis und die genannten Voraussetzungen sind Gegenstand der Selbstprüfung. Die Paketressource amsthm ist eine technische Exportabhängigkeit. Die Erläuterungen mit historischen Zahlenvergleichen werden nicht als neu geprüfte numerische Vorhersagen bewertet.

## Getrennte offene physikalische Anschlussstellen

1. **Natives Wurzelwörterbuch**. Eine unabhängig bestimmte Auslesung muss native Zustände auf die drei physikalischen Hauptmassenwurzeln abbilden, einschließlich Positivität, Nichtnulligkeit und gemeinsamer Generationenbasis.
2. **Auswahlgesetz**. Die native Dynamik oder ein unabhängiges Prinzip muss die Gleichnormbedingung beziehungsweise h=0 liefern. Projektor- und Involutionsaxiome allein tun dies nicht.
3. **Phase und Skala**. Bei Koide-Radius bleiben A und die zulässige Phase frei. Ihre Auswahl und eine physikalische Massenskala müssen zusätzlich folgen.
4. **Hierarchiemechanismus**. Soll eine Hierarchie aus einem symmetrischen Eingang entstehen, muss der Mechanismus die Voraussetzungen der linearen Zyklussperre gezielt verlassen, etwa durch eine unabhängig begründete asymmetrische Quelle oder Kopplung.

Die zwei früheren breiten nativen Guards bleiben offen. Die vier genaueren Pflichten präzisieren sie. Eine mathematisch korrekte Identität erfüllt diese nativen Pflichten nicht automatisch.

Die generische Import-Prüfpflicht kann für die vier einzelnen Aussageblöcke nach Quellen-, Frame-, Voraussetzungen-, Beweis- und Ressourcenabgleich als bearbeitet protokolliert werden. Das Review verweist dabei auf die kuratierte Interpretation und die weiter offenen nativen Guards. Der unveränderliche ursprüngliche Importstatus bleibt als Herkunft erhalten.

## Verifikation und Geltungsgrenze

Ausgeführt wurde python -m unittest discover -s scripts/qsc_audit/tests -p test_koide_and_kernel.py. Alle 35 vorhandenen Tests waren erfolgreich. Die Tests ergänzen die vier rekonstruierten Argumente; sie ersetzen deren allgemeine Beweise nicht. Es wurden keine neuen realen Massendaten erhoben und keine externe Quelle für einen tragenden Satz benötigt. Der Store soll deklarierte Review-Provenienz anzeigen und diese nicht mit einem automatischen MMA-Zertifikat verwechseln.
