# 5.0: Zwei Dokumente aus einem gemeinsamen Bestand

11. November 2026. Veröffentlichungsvorbereitung, noch keine veröffentlichte
Version. Autorenauftrag: Langfassung und eigenständig lesbare Physikfassung
zukünftig gemeinsam erzeugen und möglichst unter einer Zenodo-DOI ablegen.
Der Autor möchte die inhaltliche Aufteilung einschließlich QAM/MML/MMA
vor der Wahl einer kurzen Physikfassung besprechen. Eine Beschränkung auf
Koide/HC ist deshalb NICHT beschlossen.

## Zwei Fassungen, gemeinsamer Aussagenbestand

1. Langfassung: vollständiger Companion mit Begriffsarchitektur, Herleitungen,
   Themenzweigen, Methoden, Forschungsrunden und Historie.
2. Physikfassung: eine eigenständige physikalische Argumentationslinie mit
   ausgewählten Resultaten und expliziten Grenzen. Enthält einen ausreichenden
   Methodenteil zu QAM/MML/MMA und verweist für Details auf die Langfassung.

Die Physikfassung soll nicht bloß alle Themen verkürzt aufzählen. Zuerst
müssen Leitfrage, Hauptaussagen und erforderliche Argumentationszweige
redaktionell festgelegt werden. Diese Auswahl ist derzeit offen.

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

Aktueller Status: Scope zur Diskussion, keine veröffentlichungsfertige
Physikfassung und noch kein garantierter gemeinsamer Zwei-PDF-Build.
