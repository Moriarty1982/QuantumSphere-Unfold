# 5.0: Zwei Dokumente aus einem gemeinsamen Bestand

11. November 2026. Veröffentlichungsvorbereitung, noch keine veröffentlichte
Version. Autorenauftrag: Langfassung und eigenständig lesbare Physikfassung
zukünftig gemeinsam erzeugen und möglichst unter einer Zenodo-DOI ablegen.
Nach der Themenbesprechung hat der Autor die Einrichtung der vorgeschlagenen
Zusammenstellungen beauftragt. Die Physikfassung umfasst die unten stehende
Argumentationslinie einschließlich QAM/MML/MMA; sie ist nicht auf Koide/HC
beschränkt. Die Zuordnung ist eingerichtet, fachliche Lücken bleiben offen.

## Zwei Fassungen, gemeinsamer Aussagenbestand

1. Langfassung: vollständiger Companion mit Begriffsarchitektur, Herleitungen,
   Themenzweigen, Methoden, Forschungsrunden und Historie.
2. Physikfassung: eine eigenständige physikalische Argumentationslinie mit
   ausgewählten Resultaten und expliziten Grenzen. Enthält einen ausreichenden
   Methodenteil zu QAM/MML/MMA und verweist für Details auf die Langfassung.

Die Physikfassung folgt der eingerichteten Leitfrage und Themenfolge unten.
Die konkreten Aussagen sind zugeordnet; noch offene fachliche Prüfung wird
nicht durch die redaktionelle Auswahl ersetzt.

## Eingerichtete Themenauswahl

Leitfrage: Welche Teilchen- und Geometrieauslesungen lassen sich aus einem
gemeinsamen graduierten Träger konsistent konstruieren, und welche zusätzlichen
physikalischen Annahmen sind dafür erforderlich?

Die Physikfassung ist als Paper über das Framework und seine geprüften
Schnittstellen angelegt. Eingerichtete Reihenfolge:

| Abschnitt | Inhalt | Grenze / Voraussetzung |
|---|---|---|
| 1. Physikalische Frage | Gemeinsamer Träger, unterschiedliche Auslesungen; Ziel und Status | Physikalische Identifikation bleibt Hypothese |
| 2. Mathematischer Kern | Biquaternion-/Dixon-Träger, HC-Zerlegung, Sektoren und erklärte Frame-Abbildungen | Algebra von physikalischer Deutung trennen |
| 3. QAM/MML/MMA als Methode | Minimale Sprache, Guards, Voraussetzungen und vollständiges HC-Beispiel | Hash und Ausführungsprotokoll ersetzen keinen Beweis |
| 4. Teilchen und Generationen | Bedingte Eichgruppen-/Generationen-Konstruktionen und benannte Wahlen | Fachliche Auswahlprüfung nötig; rohe Inventarimporte nicht als Beweise behandeln |
| 5. Massen als Schnittstellentest | HC-/Koide-Bedingung, Kopplung, Positivität, Anpassung versus Vorhersage | Native Auslesung und Skala offen |
| 6. Dynamik und Geometrie | Ausgewählte Wirkungs-, Mastergleichungs- und Geometrie-Schnittstellen | Lokale Vergleichsresultate von nativer Feldtheorie unterscheiden |
| 7. Grenzen und offene Prüfungen | Fehlende Operationen, Statuskarte, belegte Prüffragen | Keine neuen Vorhersagen aus Zusammenfassungen erfinden |

Kurzer Ausblick: Zeta/Unschärfe als neue Vergleichsroute mit offenen Auswahl-
und Massenauslesepflichten, ohne verworfene globale Zeta-Spektralbehauptung.

Nur in der Langfassung ausführlich: ZF-/Kodierungsgrundlagen, gesamte
QAM-Spracharchitektur, alle MML/MMA-Varianten, Forschungsrunden, negative
Versuchsserien, große Tabellen und alternative Modellrouten. Kosmologie,
Hawking-, String-/LQG- und Konstanten-Deutungen werden im Physikpaper nur
ausgeführt, wenn ihre geprüften Aussagen die Leitfrage tragen; sonst in
der Grenzenübersicht genannt und in der Langfassung behandelt.
Zurückgezogene Herleitungen dürfen nicht als aktuelle Begründung auftreten.

Die Ausgabeprofile sind als Forschungszusammenstellungen gespeichert.
Vor einem Veröffentlichungsbuild müssen die noch offenen Aussagen,
Voraussetzungen, Belege und Verbindungen je Abschnitt fertig geprüft werden.

## QAM/MML/MMA im Physikpaper

Die neue Schreibweise muss erklärt werden, soweit sie im Dokument verwendet wird:

- QAM: verwendete Objekt-/Aussagesprache mit Bedeutung der lokalen Notation.
- MML: die im Paper tatsächlich vorkommenden typisierten Anweisungen.
- MMA: Ausführungssemantik und überprüfbare Rechenbelege dieser Anweisungen.
- Voraussetzungen, Frames, Guards und Herkunft einer Aussage.
- Unterschied zwischen mathematischem Beweis, beschränktem Rechenbeleg
  und noch offener physikalischer Identifikation.
- Ein vollständiges Beispiel von gewöhnlicher Formel über registrierte
  Voraussetzungen bis zur Interpretation des Belegs.

Ein Hash belegt Inhaltsidentität, nicht mathematische Wahrheit. Die neue
SQLAlchemy-Ablage ist die Organisation der Aussagen; sie ist nicht mit
der gesamten formalen QAM-Sprache oder einem Beweisassistenten gleichzusetzen.

Vorgeschlagene Struktur: kurze Leseanleitung vor der ersten Verwendung,
Methodenteil für das Beispiel, technische Sprachdetails in einem Anhang
der Langfassung. Umfang erst nach Wahl der benötigten Notation festlegen.

## Automatisierungsvertrag

Die vorhandene Infrastruktur bietet Snapshots, eingefrorene Auswahlen,
Abhängigkeitsabschluss, statische LaTeX-Prüfung, Export und Sicherung.
Sie kann die Redaktion der Themenwahl noch nicht automatisch ersetzen.
Der gesamte Argumentationsbaum des Manuskripts ist noch nicht geprüft.

Nach inhaltlicher Festlegung werden zwei versionierte Ausgabeprofile
eingeführt. Ein gemeinsamer Build soll beide Profile erzeugen, kompilieren,
Verweise/Quellenfrische/Guards prüfen und ein gemeinsames Manifest schreiben.
Bei fehlender Ausgabe oder fehlgeschlagener Prüfung darf kein vollständiges
Releasepaket gemeldet werden. Derselbe Quellstand und genaue Auswahlhashes
müssen im Manifest stehen; redaktionelle Überleitungen bleiben eigenständige
registrierte Textblöcke. Die Langfassung nutzt vorerst den vollständigen
Quellbaum; ein vollständig datenbankgenerierter Ersatz ist noch nicht fertig.

Geplante Dateien (noch nicht erzeugt):

- `Quantum_Sphaera_Companion_v5_0_0_full.pdf`
- `Quantum_Sphaera_Companion_v5_0_0_physics.pdf`
- zugehörige Quellen, Auswahl-/Buildnachweise, README und SHA256-Manifest.

## Zenodo: gemeinsames Paket

Beide PDFs können als Dateien eines Zenodo-Records dieselbe Versions-DOI
teilen. Die Metadaten beschreiben dann das gemeinsame Werk und die beiden
Fassungen; Zitate unterscheiden die Ausgabe zusätzlich über ihren Dateinamen.
Sie erhalten dadurch nicht jeweils eine eigenständige Artikel-DOI.

Eine neue 5.0-Version der bestehenden Record-Reihe erhält eine neue
Versions-DOI; die Concept-DOI 10.5281/zenodo.19210728 bleibt die gemeinsame
versionsübergreifende Adresse. Die Version-DOI von 4.11.0 wird nicht als
DOI der neuen Dateien verwendet. Reservierung, Upload und Veröffentlichung
sind hier noch nicht erfolgt.

Offizielle Quellen: [Dateiverwaltung](https://help.zenodo.org/docs/deposit/manage-files/),
[DOI-Versionierung](https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning).

## Noch offen vor einem konkreten Releasepaket

- Physikalische Leitfrage und aufzunehmende Themenzweige gemeinsam festlegen.
- Erforderliche QAM-Notation und deren minimale Einführung auswählen.
- Beide Ausgabeprofile und die Buildautomation implementieren und prüfen.
- Beide PDFs fachlich und visuell prüfen; erst danach Zenodo-Entwurf/DOI,
  Metadaten, Upload und endgültige Veröffentlichung getrennt freigeben.

Aktueller Status nach dem Einrichtungsauftrag: Beide Zusammenstellungen
sind mit Schema v6 in der Datenbank registriert. Die Physikfassung hat
sieben geordnete Abschnitte, Einführungstexte, das Methodenbeispiel,
kuratierte Koide-/HC-Beweise und fünf ausdrücklich offene Kandidaten.
Die Langfassung führt 61 Quellstationen und 2468 Aussagen; der Export
bewahrt den vollständigen gehashten LaTeX-Quellbaum. Es gibt einen
LaTeX-Export beider Zusammenstellungen und einen PDF-Entwurf der Physikfassung,
aber noch keine veröffentlichungsfertige Physikfassung oder einen garantierten
gemeinsamen Zwei-PDF-Releasejob. Historische Planpunkte oben beschreiben die
weiteren Schritte vor einer Veröffentlichung.

Nach Autorenkritik am protokollartigen Stil wurde die Physikfassung
redaktionell neu geschrieben. Das aktuelle Ausgabeprofil enthält einen
zusammenhängenden Haupttext mit Abstract, Motivation, Modell, Ergebnissen,
Methoden, Diskussion und Literatur. Die Originalbeweise stehen im Anhang;
technische Kennungen und Prüfstatus in `audit.md` und `assembly.json`.
Fachliche Voraussetzungen und Grenzen werden weiterhin im Paper erklärt.
Der neue Entwurf umfasst fünf Seiten Haupttext einschließlich Literatur
und zwei Seiten Beweisanhang. Dies ist eine redaktionelle Synthese,
keine zusätzliche Beweisfreigabe für die Rohimporte und noch kein Abschluss
der Veröffentlichungsvorbereitung.
