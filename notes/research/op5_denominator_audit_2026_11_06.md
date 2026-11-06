# OP5-Neuaufbau: Welche Grundgesamtheit steckt im Verhältnis?

**6. November 2026. Begrenzte Quellenprüfung, nicht blinde algebraische Einordnung.** Basis `b11683f`. Selbstprüfung durch Codex; keine neue Rechnung, keine neue H-/k-Nummer, keine unabhängige Wiederholung früherer numerischer oder literaturbezogener Checks.

## 1. Urteil

**Die Ableitung des kosmologischen Anteils aus den verglichenen Verhältnissen ist unvollständig.** Die kleinste fehlende Verbindung ist eine physikalisch begründete Abbildung zwischen Register-/Kaskaden-/Zählgrößen und dem heutigen Materieanteil relativ zur kritischen Dichte. Die algebraische Gleichheit ausgewählter Zahlen erfüllt diese Verpflichtung nicht.

Dabei ist bereits die Behauptung, die Markov-Kaskade leite den Wert β² her, zu präzisieren: r31 nimmt β² als Verzweigungseingabe und untersucht deren Stabilität. Der Wert wird dort nicht aus den übrigen Übergängen berechnet.

## 2. Vorwissen geprüft

- `notes/research/v4_9_0_r17_r19/rounds/v490_r17_round.tex`, r17.1: Eigenwertverhältnis, nicht kleinerer Eigenanteil.
- `notes/research/v4_10_0_r26_r31/rounds/v490_r31_round.tex`, Ausgangskette und r31.1: β² als Eingang; stationäre Besetzungen und aus S8 austretende Flussanteile.
- `notes/research/v4_10_0_r63_r64/rounds/v490_r63_round.tex`, r63.1 und Lesart: Lösungen zweier Zählgleichungen; zusätzliche Zuordnung zu Frames und offener Spiegel-Floor.
- Gleicher Ordner, `v490_r67_round.tex`, r67.2 und Lesart Punkt 3: Umformung zu (γ_M−γ_T)/(γ_M+γ_T); Brücke zum Energiebudget und Epoche ausdrücklich offen.
- Gleicher Ordner, `v490_r68_round.tex` und `README.md`: spätere Zählprüfung und Unterschied der Zählannahmen. Die dazu zitierte externe Literatur wurde hier nicht erneut verifiziert.
- `sources/research/parts/v480-post-release-layers.tex`, r03 F11: Herkunft als zwei Bestimmungen desselben Parameters.
- `notes/research/v4_10_0_r05/Fundstellen_Dynamik_Lambda_Auslesung.md`, `Vorschlag_Bruecke_Kaskade_Friedmann.md`: fehlende Zeit-/Dichtebrücke und ausdrücklich zusätzlich vorgeschlagener dynamischer Ansatz.
- `notes/research/predictions/Vorab_Notiz_H96_Omega_M_beta2.md`, `Ergebnis_H97_Bruecke_DESI_DR2.md`: bestehende empirische Hypothese und gescheiterte konkrete dynamische Brücke.

Einordnung: T6 und T9, nicht neuer Nachweis der Quelle–Rückweg-Schließung. I1-Auslöser 3 ist durch γ_BI/γ_string berührt: eine unabhängig begründete String-/LQG-Verbindung bleibt als zurückgestellte Idee relevant, wird hier aber nicht vorausgesetzt. I3 ist berührt, seine geprüften Formen sind gescheitert. Keine Reaktivierung oder neue Wirkungs-/Kondensatwahl.

## 3. Vier verschiedene Nenner

| Verhältnis | Zähler | Nenner / Bezugsgröße | Tatsächliche Aussage |
|---|---|---|---|
| q = λ₋/λ₊ | kleinerer Register-Eigenwert | größerer Eigenwert | Verhältnis zweier Eigengewichte, kein Anteil an ihrer Summe |
| f₄/(f₄+f₂) im r31-Modell | Übergangsfluss S8→S4 | gesamter direkter Ausfluss aus S8 nach S4 oder S2 | bedingter Anteil dieser beiden Übergangskanäle |
| (γ_M−γ_T)/(γ_M+γ_T) | Differenz zweier positiver Parameterwerte | Summe derselben Parameterwerte | algebraisch normalisierter Kontrast; zunächst keine gemeinsame Zustandsanzahl |
| Ω_M(t) im benutzten kosmologischen Modell | Materiedichte zur angegebenen Epoche | kritische Dichte derselben Epoche | kosmologischer Dichteparameter, keine Ereigniszählung oder Register-Normierung |

Im flachen, auf Materie und Λ reduzierten Modell ist die kritische Dichte gleich der Summe dieser beiden Dichten. Diese Modellvoraussetzung darf nicht rückwirkend als Identität mit den Nennern der anderen drei Zeilen eingesetzt werden. Andere Komponenten, Epoche und Beobachtungsmodell müssen ausgewiesen bleiben.

## 4. Was die Registerformel wirklich umrechnet

Für V = |b| gilt λ± = (1±V)/2. Dann q = (1−V)/(1+V). Unter der gewählten Parametrisierung V = sech(2η_f) ist q = tanh²η_f. Dies wandelt Registerkontrast in ein Eigenwertverhältnis um.

Die normierten Eigenanteile sind dagegen λ₊ = 1/(1+q) und λ₋ = q/(1+q). Wer q als Anteil eines Zweikanalbudgets verwendet, hat damit ein anderes Budget definiert als die ursprünglichen Eigengewichte. Eine solche zusätzliche Abbildung kann als Modell gesetzt werden; sie folgt nicht aus der Normierung λ₊+λ₋ = 1.

Auch ein beliebiger fester Messport ist nicht automatisch ein Eigenport. Die Analysatorausrichtung bleibt Teil des Auftrags aus dem vorherigen Datenblatt.

## 5. Was die Markov-Kaskade wirklich beweist

Schon die Ausgangskette von r31 lautet S8→S4 mit q = β² und S8→S2 mit 1−q. Eine Rückweg-Regel erzeugt im beschriebenen stationären Modell Besetzungen proportional zu (1, qr, r).

Damit gilt für den direkten Ausfluss aus S8: f₄ = p₈q und f₂ = p₈(1−q). Die Division durch f₄+f₂ gibt den eingesetzten Anteil q zurück. Die Unabhängigkeit vom Rückwegparameter ist eine Aussage über dieses Modell und diese Flussnormierung; sie bestimmt q nicht.

Besetzungen liefern bereits einen anderen Vergleich: p₄/p₂ = qr. Dieser hängt an der Rückwegregel. Die stabilen Übergangsanteile sind deshalb nicht automatisch stabile Materie-/Vakuumbestände oder Energiedichten.

**Präzisierung einer früheren Zusammenfassung:** Die r05-Fundstellennotiz nennt r31 eine Stelle, an der das Verhältnis „aus einer Dynamik kommt statt gesetzt zu werden“. Eng gelesen kommt die Stationarität aus der Dynamik; die Verzweigungszahl ist bereits Eingang. Die historische Notiz bleibt unverändert. Diese spätere Klarstellung verhindert, dass eine Stabilitätsrechnung als unabhängige Zahlenvorhersage verwendet wird.

## 6. Was die Zählgleichungen wirklich liefern

r63 definiert γ als Lösung von Σ_j g(j) exp(−2πγ sqrt(j(j+1))) = 1. Die Einschränkung auf minimalen Spin und die volle Summe mit gewähltem Gewicht führen zu verschiedenen γ-Werten. γ_M und γ_T sind hier Parameterlösungen verschiedener Zählregeln, nicht die kardinalen Anzahlen N_M und N_T einer bereits gemeinsam definierten Population.

r67 verwendet γ_L = γ_M/γ_T und q = (γ_L−1)/(γ_L+1). Daraus folgt algebraisch q = (γ_M−γ_T)/(γ_M+γ_T). Die Umformung ist nachvollziehbar, erzeugt aber keine Abbildung zwischen Mikroereignissen und Materieenergie.

Selbst wenn die minimalen Zustände in einer größeren Zustandsmenge enthalten sind, darf aus dem Einschluss nicht die Identifikation „Differenz der beiden Parameterlösungen = Anzahl der zusätzlichen Zustände“ abgeleitet werden. Dafür müsste erst ein gemeinsames Zählmaß und dessen Relation zu γ angegeben sein. r67 benennt die Brücke zum Energiebudget selbst als offen.

## 7. Der verbleibende Kern der kosmologischen Behauptung

Die gemeinsame Zahl q ist in den vorhandenen Strängen unterschiedlich verwendet:

`gewählte Zählregeln → γ-Verhältnis → q; q als Kaskadeneingabe → stabiler bedingter Flussanteil; zusätzliche Identifikation → Ω_M(heute)`.

Die Markov-Rechnung ist damit kein unabhängiger zweiter Nachweis der kosmologischen Identifikation. Registeralgebra und Zählumformung liefern ebenfalls keine doppelte empirische Bestätigung. Sie können dieselbe parametrisierte Zahl beschreiben, solange ihre Abbildung als zusätzliche Annahme offengelegt wird.

Das kleinste sauber formulierte verbleibende Aussagepaket ist H96: Mit den festgelegten Zählannahmen wird der heutige kosmologische Materieanteil mit q identifiziert und an den registrierten künftigen Daten geprüft. Die Neuordnung verschärft oder lockert keines seiner Kriterien. Auch ein künftiger Zahlentreffer wäre ohne weitere Brücke noch keine Ableitung der ursprünglichen Λ-Auslöschung.

## 8. Nächste Entscheidung ohne neue Rechnung

Die Quellenprüfung der unmittelbaren Identifikationskette hat damit einen belastbaren Zwischenabschluss: Die zusätzliche Gleichsetzung q = Ω_M(heute) ist lokalisiert, aber nicht hergeleitet. Ein neuer Nenner, ein neuer Wirkungsansatz oder eine passende Zeitregel werden hier nicht ergänzt.

Als nächster eigenständiger Schritt kann ein kompaktes Gesamturteil zur neuen OP5-Arbeitsfrage erstellt werden: gesicherte algebraische Teile, explizite Modellannahmen, historische Fehlschlüsse und die eine noch fehlende physikalische Brücke. Erst eine anschließend beauftragte neue Herleitung oder ein konkreter Test würde diese Quellenrekonstruktion verlassen.

Guards unverändert; keine Änderungen an bestehenden Runden oder veröffentlichten Payloads. H96 offen, H97 widerlegt, W1/W2 eingefroren. Diese Notiz ist keine neue nummerierte Forschungsschicht.
