# Fahrplan zum QAM-Aussagenspeicher und LaTeX-Export

11. November 2026. Planungsstand auf Autorauftrag. Die folgenden Phasen sind geplante Arbeit. Die Auswahl einer Zugriffsbibliothek ist offen.

## Ziel und Quellen

Ein registrierter Aussagenbestand soll fachliche Baumansichten und reproduzierbare Paperfassungen ermöglichen. Aussagen, Beweise, Erläuterungen, Übergangstexte und technische LaTeX-Bausteine werden versioniert referenziert. Fehlende mathematische Verbindungen erhalten eigene offene Verpflichtungen.

Grundlage ist der vorhandene [QAM-Store-Abschnitt](../../sources/research/parts/v470/07_qam_infrastructure.tex#L222), insbesondere die Definitionen des Store-Zustands, der Instruktionen, der Ausführungssemantik und der Snapshots. Die Register A, O, R, G und L entsprechen Adressen, Objekten, Relationen, Guards und Herkunftsledger. STORE, LINK, SNAPSHOT, CLONE, ROLLBACK, SCRUB, MERGE_CAND und EXPORT geben die Schnittstelle vor.

Das [Manuskriptinventar](../../qam/tools/manuscript_inventory.py) ist ein vorhandener Importprototyp. Sein gemeldeter Bestand umfasst 61 Dateien und 2468 Aussageumgebungen. Die Einträge sind ungeprüft und besitzen Dokument-Elternkanten. Fachliche Abhängigkeiten und die Erfassung von Fließtext sind noch aufzubauen. Das bestehende SQLite-Register für QAM-Claims, Hashes, Prämissen und MMA-Belege ist bei der Planung zu berücksichtigen.

## Phase 1 – Bestand und Verträge prüfen

- Vorhandene Store-, MML-, MMA-, Datenbank- und Exportimplementierungen inventarisieren. Für jeden Store-Befehl Quelle, Implementierung, Prüfungen und offene Teile zuordnen.
- Hashformate, Normalisierung, Transaktionsgrenzen und bisherige Datenbankmigrationen ermitteln. Einen Quellhash, einen Inhaltsversionshash und eine mathematische Äquivalenz getrennt behandeln.
- Klären, welche Daten dauerhaft versioniert werden und wie sich die lokale Datenbank daraus wiederherstellen lässt. Importwiederholung, Parallelzugriffe und abgebrochene Importe müssen konsistente Zustände liefern.
- SQLAlchemy als mögliche Zugriffsschicht gegen die vorhandenen SQLite-Werkzeuge prüfen. Entscheidung anhand der tatsächlichen Migrations- und Abfrageanforderungen dokumentieren.

Abnahme erfolgt durch eine Bestandskarte und einen konkreten Schemaentwurf mit Migrations- und Wiederherstellungsweg.

## Phase 2 – Objektmodell und Registrierung

Geplante Entitäten sind Objektidentität, unveränderliche Objektversion, Quellenfundstelle, Relation, offene Verpflichtung beziehungsweise Guard, Belegreferenz und Ledgerereignis. Ein Objekt kann mehrere Quellenfundstellen und mehrere Verwendungen in Argumentzweigen haben.

Objekttypen umfassen Aussage, Definition, Annahme, Beweis, Erläuterung, Übergangstext, Literaturquelle und LaTeX-Hilfsmittel. Formeln und Texte behalten Frame, Sprache beziehungsweise Profil, Autorenstatus und Prüfstatus. Historische Rücknahmen und Ersatzversionen werden explizit verknüpft.

Ein Übergangstext erhält eine eigene Version mit LaTeX-Inhalt und Verwendungsbedingungen. Die Zuordnung zu Ausgangs- und Zielobjekten erfolgt über Relationen. Derselbe Text kann in mehreren Zusammenstellungen verwendet werden, sofern sein Kontext passt.

STORE registriert Version und Herkunft. LINK registriert typisierte Beziehungen wie Dokumentzugehörigkeit, benötigt, beweist, erläutert, ersetzt, widerspricht und verwendet Übergang. Eine vermutete Verbindung trägt eine offene Verpflichtung mit benannten Endpunkten, fehlender Operation oder Begründung und Quellenhinweis. Der Status der Beziehung ist unabhängig vom Status ihrer Endpunkte.

Abnahme erfolgt an einem kleinen Ausschnitt mit Definition, bedingter Aussage, Beweis und fehlender Brücke. Ein erneuter identischer Import darf keine neuen Inhaltsversionen erzeugen. Ein geänderter Inhalt muss als neue Version erkennbar sein. Vorhandene Belege müssen weiterhin auf ihre ursprünglichen Prämissen zeigen.

## Phase 3 – Inventar in fachliche Ansichten überführen

- Aktive Einbindungskette mit Quellenrevision und Importlauf erfassen. Originaltext, Beweise und Umfeld zuordnen. Grenzen des automatischen LaTeX-Parsers ausdrücklich erfassen.
- Aussagen in Fließtext und mehrteiligen Umgebungen ergänzen. Historische Überschriften mit späteren Statuskorrekturen abgleichen.
- Dokumentreihenfolge, Themenzugehörigkeit und logische Abhängigkeit als eigene Relationstypen verwalten.
- Zunächst einen begrenzten Argumentzweig fachlich zuordnen und offene Brücken konkret benennen. Anschließend den übrigen Bestand schrittweise bearbeiten.

Abnahme erfolgt durch eine lesbare Baumansicht mit Mehrfachverwendungen, prüfbaren Quellenstellen und sichtbaren offenen Verpflichtungen. Jeder Knoten muss auf seine genaue registrierte Version zurückführen.

## Phase 4 – Snapshots und Paperzusammenstellungen

Ein Snapshot bindet Objektversionen, Relationsversionen, Guards und Ledgeranker. Eine Paperzusammenstellung speichert Auswahl, fachliche Reihenfolge, erlaubte Statusgruppen, Framekontext, Übergangstexte und Exportprofil auf diesem Snapshot. CLONE öffnet eine bearbeitbare Variante. ROLLBACK stellt eine protokollierte Auswahl wieder her. MERGE_CAND legt eine prüfbare Zusammenführung mit Konflikten vor.

Abnahme erfolgt durch zwei Fassungen mit gemeinsam genutzter Aussage, aber unterschiedlicher Gliederung. Eine spätere Quellenänderung darf den früheren Snapshot nicht verändern. Konflikte dürfen die gewählte Inhaltsversion nicht still überschreiben.

## Phase 5 – Abfrage und LaTeX-Export

Die Abfrage wählt Thema oder Zielaussagen und ermittelt die erforderlichen Bausteine. Nur als solche deklarierte logische Abhängigkeiten bestimmen die topologische Reihenfolge. Zyklen führen zu einer Diagnose oder einem ausdrücklich gruppierten wechselseitigen Block. Redaktionelle Reihenfolge wird separat berücksichtigt.

EXPORT löst Beweise, Definitionen, Makros, Pakete, Labels, Querverweise, Literatur, Abbildungen und Übergänge auf. Nummernverweise müssen mit der erzeugten Fassung übereinstimmen. Es bleibt zu entscheiden, ob ein erster Prototyp ganze bestehende Dateien einbindet oder bereits registrierte Einzelbausteine ausgibt. Einzelbausteine benötigen eine verifizierte technische Abhängigkeitsliste.

Für einen Forschungsentwurf dürfen offene Brücken als sichtbare Platzhalter mit Verpflichtungskennung ausgegeben werden. Ein als geschlossen angeforderter Argumentexport meldet solche Lücken als blockierend. Die Veröffentlichungseignung verlangt eine zusätzliche fachliche Prüfung der ausgewählten Aussagen und ihrer Status.

Jeder Export erhält ein Manifest mit Snapshot, Auswahl, Inhaltsversionen, Quellenständen und Generatorversion. Abnahme erfolgt durch einen reproduzierbaren kleinen PDF-Build ohne undefinierte Verweise oder doppelte Labels sowie einen gezielten Test, der eine fehlende Brücke sichtbar macht.

## Phase 6 – SCRUB und Anschluss an die bestehenden Werkzeuge

SCRUB prüft Adressen, Quellen- und Inhaltsintegrität, gültige Referenzen, Lineage, fehlende Bausteine, Statuskonflikte und offene Guards. Prüfungsergebnisse werden als eigene Ledgerereignisse gespeichert. Änderungen an Aussagen sollen betroffene Belege, Verpflichtungen und Zusammenstellungen auffindbar machen.

Danach CLI und gegebenenfalls MCP-Abfragen für Registrierung, Baumansicht, offene Brücken und Export bereitstellen. Vorhandene QAM-Prämissenspuren und MMA-Belege über ihre bestehenden Hashes anbinden. Die neu registrierte Manuskriptbehauptung und ein erfolgreich geprüfter MMA-Beleg behalten getrennte Evidenzstatus.

Abnahme erfolgt durch gezielte Fehlerfälle für veraltete Quelle, gebrochene Referenz, unpassenden Frame und abgebrochenen Schreibvorgang sowie durch den Wiederaufbau aus dem versionierten Bestand.

## Erster begrenzter Durchstich

Nach Phase 1 einen kleinen vorhandenen Koide-Argumentzweig auswählen. Seine Definitionen, eine bedingte Aussage, ihren Beweis und eine ausdrücklich offene native Brücke registrieren. Daraus eine kurze LaTeX-Fassung mit Quellenmanifest und sichtbarer Lücke erzeugen. Dieses Beispiel prüft die gesamte Kette von STORE und LINK über SNAPSHOT bis SCRUB und EXPORT, bevor der Gesamtbestand fachlich umgebaut wird.

## Noch zu entscheidende Punkte

- Dauerhafte Quelle des registrierten Bestands und Synchronisation mit den TeX-Dateien.
- Identitäts- und Hashregeln sowie Umgang mit alten Quellenständen.
- Zugriffsschicht und Migrationsstrategie.
- Granularität der Einzelbausteine und Behandlung des umgebenden Fließtexts.
- Gewichtung redaktioneller Reihenfolge gegenüber logischer Abhängigkeit.
- Regeln für exportierbare historische, bedingte und ungeprüfte Aussagen.

Nächster Arbeitsschritt ist Phase 1. Der Fahrplan selbst enthält keine Entscheidung über die mathematische Gültigkeit oder Aktivierung offener Modellbrücken.
