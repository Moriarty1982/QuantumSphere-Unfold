# QAM store – erster Aufbauschritt

## Gemeinsamer Bau beider Dokumente

`python -m qam.tools.build_v5_documents --out build/v5-paired-new` erzeugt
beide englischen Entwürfe gemeinsam in einem neuen Ordner. Der Ablauf legt
einen eigenen Aussagenbestand an, friert beide Editionen ein, prüft ihre
gemeinsamen Quellhashes und setzt beide Dokumente mit pdflatex ohne
Shell-Escape. Bis zu sechs Durchläufe warten auf stabile Hilfsdateien.

Das Paket enthält beide benannten PDFs, den exportierten Langquellbaum,
die Aussagen-Datenbank, beide Zusammenstellungsmanifeste, Auditdaten,
Compilerprotokolle, die verwendeten Erzeugungsskripte und `SHA256SUMS.txt`.
`build-manifest.json` meldet `build_complete` nur, wenn beide PDFs vorhanden
sind und Quellen-/Verweisprüfungen bestehen. Auch ein gescheiterter Lauf
schreibt ein ausdrücklich fehlgeschlagenes Manifest. Offene wissenschaftliche
Reviews und Guards bleiben erhalten; `publication_ready` bleibt immer false.
Satzüberläufe werden gezählt und verlangen redaktionelle Prüfung.

Der erste erfolgreiche gemeinsame Lauf lieferte 1397 Seiten Langfassung
und 27 Seiten Physikpaper; 58 Satzüberläufe im Langtext, keine im Physikpaper.
Keine offenen Verweise, doppelten Labels oder verbleibenden Rerun-Meldungen.
Das ist keine fachliche oder vollständige visuelle Freigabe der Langfassung.
Workflow: `.github/workflows/qsc-v5-dual-documents.yml`, manuell oder nach
passenden Änderungen auf main. Er archiviert auch Fehlerdiagnosen und
reserviert weder eine DOI noch lädt er etwas auf Zenodo hoch.

Der anschließende reine Layoutnachzug beseitigt lokal alle 58 Satzüberläufe:
1402 Seiten Langfassung und unverändert 27 Seiten Physikpaper, beide ohne
Overfull-Boxen oder offene Verweise. Die historische Argumentation bleibt
erhalten; ihre Quellhashes ändern sich durch die Satzbefehle und werden
bei der Zusammenstellung neu registriert. Prüfung und Grenzen:
`notes/research/v5_layout_reflow_2026_11_11.md`.

## Zwei Dokumentzusammenstellungen (Schema v6)

`python -m qam.tools.configure_v5_editions --out build/v5-editions-new`
legt die vollständige und die Physikfassung reproduzierbar an. Der Zielordner
muss neu sein; die Datenbank bleibt standardmäßig `build/qam.sqlite3`.
Ein erneuter Lauf mit unveränderten Eingaben behält dieselben Editionshashes.
Geänderte Inhalte erzeugen eine neue Revision mit geprüftem Vorgänger.

`qstore_editions`, `qstore_edition_sections` und `qstore_edition_members`
speichern Version, Abschnittsfolge und genaue Aussagezuordnung. Die Daten
sind unveränderlich; die Abschnittszuordnung ist keine Beweisabhängigkeit.
`edition-read`, `edition-save` und `edition-export` stehen in `store_db` bereit.
Beispiel: `python -m qam.tools.store_db edition-read --hash HASH --out build/edition.json`.

- `qsc-v5-physics`: sieben Abschnitte, registrierte Einführungstexte,
  vollständiges Methodenbeispiel mit rationalen Matrixbelegen und die
  kuratierten Koide-/HC-Argumente. Fünf weitere konkrete Aussagen zu Träger,
  Teilchen/Generationen und Geometrie bleiben als Kandidaten sichtbar.
- `qsc-v5-full`: 61 Quellstationen in Eingabereihenfolge und 2468 Aussagen.
  Der Export enthält den gehashten vollständigen Quellbaum und dessen
  Einstiegspunkt. Er bewahrt auch Text ohne Satzumgebung. Dies ist noch
  kein vollständig verifizierter Datenbankersatz für den Langtext.

Die Physikfassung wird inzwischen als zusammenhängendes Paper mit Abstract,
Einleitung, wissenschaftlichem Haupttext, Literatur und Beweisanhang ausgegeben.
`presentation.style=physics-paper` und die registrierte Abstractversion sind
Teil der unveränderlichen Editionsrevision (Format v2, Schema bleibt v6).
Die Textblöcke stammen aus `qam/editions/v5_physics_article.tex`, die Literatur
aus `v5_physics_references.tex`. Sieben zusätzliche registrierte Blöcke
`v5_expanded_<Abschnitt>.tex` entwickeln die Argumente; jeder Abschnitt
enthält die Einführung und genau diesen Ausbau. Fehlende Ausbauquellen
brechen die Zusammenstellung ab. Die früheren Audit-Ausgaben bleiben abrufbar.

Der erweiterte Entwurf vom 11.11.2026 umfasst 27 Seiten: 24 Seiten
Argumentation, eine Seite Literatur und zwei Seiten Beweisanhang. Er enthält
das vollständig hergeleitete elektromagnetische Intervallbeispiel, bedingte
Teilchen-/Generationen-Konstruktionen, Gram-/Schur-Massenauslesung,
Positivitätsgrenzen, projizierte Dynamik, geometrische Kompatibilität und
den Zeta-/Unschärfevergleich. Der gespeicherte MMA-Intervallbeleg liegt in
`qam/editions/evidence/gram_interval_receipt.json`; seine bedingten Prämissen
bleiben offen. Die sieben Ausbauten sind redaktionelle Erklärungsobjekte,
keine automatisch als bewiesen registrierten neuen Aussagen.

Der Export erzeugt `paper.tex`, `assembly.json` und `audit.md`. Einzelne
Versionskennungen, noch ungeprüfte Kandidaten und Prüfstatus stehen im
Auditbericht; ihre fachlichen Grenzen bleiben im Haupttext ausdrücklich
beschrieben. Die neue Darstellung verleiht keinem importierten Satz einen
Beweisstatus. Fehlende TeX-Ressourcen blockieren die lesbare Fassung, statt
Abschnitte still wegzulassen. Quellenänderungen werden vor dem Export erkannt.

Editionsdaten sind wie benannte Paper-Metadaten außerhalb des
Inventar-Snapshotumfangs; ihre Speicherung ändert daher nicht den zugehörigen
Inventarcheckpoint. Vollständige DB-Backups enthalten sämtliche Editionstabellen.
Der Export ist ein Forschungsentwurf und keine Publikationsfreigabe. Ein
gemeinsamer automatischer PDF-/Zenodo-Releasejob bleibt ein eigener Schritt.

Dokumententwicklung seit 11.11.2026: **v5.0.0-draft**. Dies bezeichnet die
datenbankgestützte Dokumentarchitektur, nicht eine neue Schemamigration oder
eine mathematische Beweisfreigabe. Die historische Aufbauchronik unten bleibt
erhalten. Aktueller Umfang: `notes/research/v5_0_0_development.md`.

Die erste Migration ergänzt die lokale QAM-Datenbank um Tabellen mit dem Präfix qstore_. Die bestehenden Claim-, Prämissen-, Cache- und Belegtabellen sowie das Manuskriptinventar werden bei der Initialisierung erhalten.

Aufruf aus dem Repository mit `python -m qam.tools.store_db`. Für eine andere Datenbank dient `--db PFAD`. Wiederholte Initialisierung ist idempotent. Migration und Typenkatalog werden in einer gemeinsamen Schreibtransaktion angelegt. Unbekannte Schemaversionen und abweichende Typenkataloge führen zum Abbruch.

## Definitionen und Seeds

Der versionierte Typenkatalog catalogue_v1.json enthält insbesondere definition und seed. Eine Definition beschreibt Bedeutung, Geltungsbereich und Voraussetzungen. Ein mathematischer Seed ist ein Ausgangswert oder Ausgangsobjekt mit Typ, Frame, Herkunft und Annahmen. Ein Seed soll auf die konkrete Definitionsversion seiner Interpretation verweisen. Diese Verknüpfung wird im nächsten Schritt über die Registrierungs- und LINK-Schnittstelle validiert.

Davon getrennt ist das technische Datenbank-Seeding. In diesem Schritt wird nur der Objekttypenkatalog initialisiert. Physikalische Ausgangswerte, Definitionen und Behauptungen müssen mit Quellen registriert werden. Der Datenbestand enthält dadurch noch keine neuen mathematischen Aussagen.

## Schema und nächste Schnittstelle

qstore_objects hält stabile Objektkennungen und ihren Typ. qstore_versions hält unveränderliche Inhaltsversionen mit Status und Frame. qstore_sources verknüpft Versionen mit Quellenstand, Quellhash und Fundstelle. qstore_relations nimmt typisierte Beziehungen zwischen genauen Versionen auf. qstore_guards hält offene oder geprüfte Verpflichtungen. qstore_ledger hält append-only Ereignisse.

Das ist das erste physische Schema. Die STORE/LINK-API muss als Nächstes kanonische Versionshashes, Seed-Pflichtfelder, Quellprüfung, Relationsvokabular und atomare Ledgerereignisse durchsetzen. Die Statusmarke reviewed benötigt definierte Review-Provenienz. Relation- und Guard-Revisionen, Snapshots, Branches und Exportmanifeste folgen vor dem ersten produktiven Import. Bis dahin werden neue Objekte ausschließlich mit der später geprüften Registrierungsschnittstelle angelegt.

Auf Autorentscheidung wird SQLAlchemy 2.0 als ORM über der vorhandenen SQLite-Datenbank eingesetzt. Das Schema modelliert den Store-Abschnitt aus sources/research/parts/v470/07_qam_infrastructure.tex und folgt dem Fahrplan notes/research/qam_store_latex_fahrplan_2026_11_11.md.

## SQLAlchemy-Zugriff

SQLAlchemy 2.0 ist die gewählte ORM-Schicht. Installation mit python -m pip install -r qam/store/requirements.txt. Das Modul qam/store/orm.py bildet die vorhandenen qstore_-Tabellen über Schema-Reflection auf ORM-Klassen ab. Die SQL-Migration bleibt für Constraints und Trigger maßgeblich. Beziehungen werden vorerst über ihre expliziten Endpunktspalten abgefragt; die geprüfte LINK-Schnittstelle folgt als eigener Schritt.

Mit python -m qam.tools.store_db status läuft eine erste reguläre Abfrage über SQLAlchemy. store_session liefert eine transaktionale Session und die Modellklassen. Erfolgreiche Blöcke werden committet, Fehler führen zum Rollback. Jede ORM-Verbindung aktiviert Fremdschlüssel und explizite Transaktionen.

python -m unittest qam.store.test_orm prüft Commit, Rollback, wiederholte Initialisierung, Fremdschlüssel sowie die Unveränderlichkeit von Inhaltsversionen und Ledger. Die Testwerte werden ausschließlich in einer temporären Datenbank angelegt. Die API für Hashprüfung und mathematische Registrierung folgt vor dem produktiven Inhaltsimport.

## STORE und LINK für Definitionen und Seeds

Die CLI unterstützt store --request DATEI und link --request DATEI neben initialize und status. --repo legt die Wurzel der zu prüfenden Quelldateien fest. STORE erwartet object_id, kind, frame, status, payload und source. Erlaubte erste Objekttypen sind definition und seed, mit Status imported-unreviewed, declared oder conditional.

Eine Definition benötigt title, body, scope und assumptions. Ein Seed benötigt title, value, value_type, origin, assumptions und definition_version. assumptions ist eine Liste expliziter Annahmen. Ein leerer Eintrag oder ein fehlender Seedwert führt zum Abbruch. definition_version muss auf eine registrierte Definition im gleichen deklarierten Frame zeigen. Eine semantische Typprüfung des Feldwerts ist noch offen.

source enthält den relativen Pfad path, den SHA256 der aktuellen Dateibytes, revision und locator. Der Pfad muss innerhalb der angegebenen Repositorywurzel liegen. Revision und Locator sind deklarierte Herkunftsangaben; ihre semantische Zuordnung zu Git beziehungsweise einer Aussage wird noch nicht automatisch geprüft. Eine Quellenänderung erzeugt eine neue Fundstelle und bei geändertem registriertem Inhalt eine neue Inhaltsversion.

Versionshashes verwenden einen eigenen SHA256-Vertrag qstore-version-v1 über kanonisches UTF-8-JSON mit sortierten Schlüsseln, kompakten Trennzeichen und ausgeschlossenen NaN-/Infinity-Werten. Identität, Typ, Frame, Status und Payload gehen ein. Quellfundstellen werden separat protokolliert. Dieser Vertrag ist vom bestehenden QAM-MD5-Belegformat getrennt.

Ein identischer STORE-Aufruf erzeugt keine zusätzliche Version oder Ledgerereignisse. Seedversion und interpreted-by-Verknüpfung werden atomar registriert. Fehler rollen Objekt, Version, Quelle und Ledger gemeinsam zurück. Schreibtransaktionen werden vor der Leseprüfung serialisiert.

LINK erwartet source, target als Versionshashes sowie kind, status und description. Die ersten Beziehungstypen sind interpreted-by, requires, explains, proves, contains und supersedes. proposed und declared kennzeichnen den Registrierungsstand. Auch ein declared-proves-Eintrag ist eine Autorendeklaration. Eine überprüfte Beweiskante benötigt die spätere Review-Schnittstelle. Eine interpretierende Definition muss im selben Frame liegen; allgemeine Framebrücken sind noch nicht implementiert.

Die automatisierten Tests qam.store.test_registry prüfen Wiederholbarkeit, neue Inhaltsversionen, veraltete Quellhashes, atomare Zurückweisung ungültiger Seeds und die Sperre einer ungeprüften Statuspromotion.

## Offene Brücken registrieren

guard --request DATEI registriert eine offene Nachweispflicht. Pflichtfelder sind subject als exakter Versionshash, target als Versionshash oder null, title, obligation und source mit demselben Quellformat wie STORE. Beide vorhandenen Endpunkte werden geprüft. Die Registrierung erfolgt atomar und identische Wiederholung erzeugt keinen zusätzlichen Eintrag. Der eigene qstore-guard-v1-Hash umfasst Endpunkte, offenen Status und Payload einschließlich Herkunft.

guards gibt alle offenen Verpflichtungen mit Quellen und Endpunkten in stabiler Reihenfolge als JSON aus. Eine fehlende Verbindung kann damit gespeichert werden, ohne eine logische Abhängigkeit als bewiesen zu behandeln. Diese Schnittstelle erlaubt ausschließlich das Anlegen offener Verpflichtungen. Erledigung und Revision einer Verpflichtung benötigen die folgende Review-/Revisionsschicht mit konkreter Evidenz und nachvollziehbarer Herkunft.

Die Registry-Tests prüfen zusätzlich identische Wiederholung, gespeicherten offenen Status, fehlende Endpunkte und die Zurückweisung eines mitgelieferten Erledigungsstatus. Die produktive Datenbank ist bisher ohne registrierte mathematische Inhalte; die Tests legen Beispiele in einer temporären Datenbank an.

## Revisionsspur für Brücken und Beziehungen

Schema v2 ergänzt unveränderliche Review-Einträge und schützt auch ursprüngliche Guards und Relationen gegen Überschreiben und Löschen. Bestehende v1-Datenbanken werden bei Initialisierung atomar erweitert.

review --request DATEI erwartet kind (guard oder relation), subject als ursprünglichen Hash, previous als aktuellen Review-Hash oder null beim ersten Review, status, reviewer, reason und evidence. evidence verwendet das geprüfte Quellenformat. Eine neue Bewertung nennt den unmittelbaren Vorgänger; konkurrierende veraltete Bewertungen werden zurückgewiesen. Identische Wiederholung bleibt idempotent. Bewertungswechsel, einschließlich Wiederöffnung, erhalten die bisherige Historie.

Das Review ist eine deklarierte Beurteilung eines benannten Menschen oder Agenten mit nachprüfbarem Dateihash. Die Schnittstelle prüft die Existenz des Nachweises und die Historie. Sie authentifiziert keine Person und führt keine automatische mathematische Beweisprüfung oder MMA-Zertifizierung aus. Der Status satisfied bedeutet deshalb eine protokollierte Beurteilung mit dieser Evidenzart.

guards berücksichtigt den letzten Review-Status. Der ursprüngliche Eintrag bleibt unverändert. Die Tests prüfen Erledigung, Wiederöffnung, identische Wiederholung und konkurrierende Vorgänger. Der produktive Manuskriptimport steht weiterhin aus.

## Automatische Prüfung
Der erste rationale Matrixprüfer und seine Belegverträge stehen in [VERIFICATION.md](VERIFICATION.md). Schema v3 speichert unveränderliche Prüfbelege samt exakten Eingabeversionen. Die CLI stellt verify und receipt bereit.

## Snapshots des Store-Bestands

Schema v4 speichert unveränderliche, inhaltsadressierte Bestands-Snapshots. snapshot --label NAME bindet sämtliche Store-Objekte, Versionen, Quellen, Beziehungen, Guards, Reviews und Prüfbelege einschließlich der Eingabeverknüpfungen. Das zugehörige Ledger wird eingebettet und zusätzlich gehasht. snapshot-read --hash HASH liest den eingebetteten Zustand nach Integritätsprüfung zurück.

Die Snapshots tragen inventory-checkpoint. Damit lassen sich auch bedingte oder ungeprüfte Bestände festhalten. Die stärkere mathematische Zulässigkeit eines guarded snapshot bleibt eine spätere SCRUB-Verpflichtung. Das ältere Claim-/MMA-Register und das Manuskriptinventar liegen außerhalb dieses ersten Snapshotumfangs; referenzierte Quelldateien werden durch Herkunftsmetadaten erfasst.

Ein identischer Bestand mit identischem Label erzeugt denselben Snapshot. Die Snapshot-Buchungsereignisse selbst sind aus dem eingebetteten Ledger ausgeschlossen, damit die Wiederholung unverändert bleibt. Alle anderen Ledgerereignisse gehen ein. Ein anderer Labeltext erzeugt einen eigenen Snapshot.

Der erste lokale Snapshot matrix-comparison-first enthält vier Inhaltsversionen, drei Definitionsverknüpfungen und zwei Matrixprüfbelege. Die vier Testsuiten einschließlich qam.store.test_snapshots prüfen Wiederholung, Unveränderlichkeit, Abfrage über CLI und den Erhalt alter Snapshots nach späterer Erweiterung des Live-Bestands. CLONE und ROLLBACK folgen als eigene Funktionen.

## Auswahl aus einem festen Snapshot

select --hash SNAPSHOT --request DATEI liest eine Anfrage mit roots als Liste genauer Versionshashes. Die Auswahl wird ausschließlich aus dem eingebetteten Snapshotzustand berechnet. interpreted-by und requires ziehen bei declared oder reviewed ihre Ziele als Voraussetzungen hinzu. proposed wird als offene Verbindung gemeldet. rejected wird nicht als Abhängigkeit verfolgt. Dokumentzugehörigkeit bestimmt keine logische Ableitung.

Die Ausgabe enthält die Voraussetzungen vor ihren Verwendungen, jede Version einmal, einen deterministischen Auswahlhash sowie Statushinweise, Annahmen, offene beziehungsweise fehlgeschlagene Guards und erforderliche Framebrücken. Ein Zyklus oder eine im Snapshot fehlende Zielversion bricht die Auswahl mit Diagnose ab.

Verwandte Prüfbelege werden mitgeführt. all_matrix_inputs_selected kennzeichnet, ob die Matrixeingaben des Belegs vollständig in der Auswahl enthalten sind. Ein nur über eine gemeinsame Definition verwandter Kontrollbeleg gilt dadurch nicht als Prüfung der gesamten Auswahl. passed hebt weder Objektstatus noch offene Voraussetzungen auf. LaTeX-Ressourcen und Veröffentlichungseignung sind noch gesondert zu prüfen.

Der erste Auswahltest am gespeicherten Vergleichs-Snapshot liefert eine Definition und zwei Seeds sowie den passenden erfolgreichen Matrixbeleg. Der Regressionstest test_selection kontrolliert die Reihenfolge, Mehrfachverwendung, offenen Voraussetzungen, fehlende Wurzeln, Zyklen und die Unabhängigkeit eines alten Snapshots von späteren Live-Verknüpfungen.

## Erster LaTeX-Export

export --hash SNAPSHOT --request DATEI --out NEUER_ORDNER verwendet dieselbe roots-Anfrage wie select. Er erzeugt paper.tex und manifest.json. Bestehende Ausgabeordner werden zurückgewiesen. Das Manifest wird zuletzt geschrieben; eine Ausgabe ohne Manifest gilt als unvollständig. Die Generierung startet keinen Compiler.

Der erste Export unterstützt Definitionen und rationale Matrix-Seeds. Registrierte Textfelder werden als Text maskiert; die Matrixformeln werden aus den bereits geprüften rationalen Eingabeformaten erzeugt. Das ist die erste begrenzte Exportroute. Originale LaTeX-Bausteine, Beweise, Übergangstexte und deren Makro-/Literaturabhängigkeiten folgen als weitere Objekttypen. Der aktuelle pdfLaTeX-Prototyp wurde mit dem englischen Vergleichsbestand geprüft; beliebige Unicode-Inhalte benötigen eine gesonderte Engine-/Fontprüfung.

Der Entwurf zeigt Status, Frames, offene Voraussetzungen und nur diejenigen Matrixbelege, deren konkrete Matrixeingaben vollständig ausgewählt sind. Das Manifest enthält die vollständige Auswahl, Snapshot- und Versionshashes sowie SHA256 des erzeugten TeX und des Generator- und Auswahlcodes. Die TeX-/Manifestausgabe ist bei gleicher Auswahl und gleichem Code reproduzierbar. Ein PDF-Build ist ein separater Schritt.

Der geprüfte lokale Beispielentwurf liegt unter build/qam-paper-comparison-v3/paper.pdf. Er wurde mit zwei pdfLaTeX-Durchläufen gebaut und als einseitiges A4-Dokument visuell kontrolliert. Das Log enthält keine undefinierten Verweise, doppelten Labels, Rerun- oder Overfull-Meldungen. Die sechs Testsuiten einschließlich test_latex_export prüfen Manifestintegrität, Reproduzierbarkeit, Textmaskierung und die Sperre gegen Überschreiben.

## Originale LaTeX-Blöcke und Übergangstexte

STORE unterstützt jetzt claim, proof, explanation und transition mit title, latex, assumptions und dependencies. dependencies nennt konkrete Versionshashes und wird atomar als deklarierte requires-Verknüpfung registriert. Alle abhängigen Versionen müssen im selben Frame liegen. Der LaTeX-Inhalt muss wörtlich in der per Hash geprüften Quelldatei vorkommen. Zeilenenden dürfen sich durch LF/CRLF-Konvertierung unterscheiden. Originaltext und Herkunft bleiben damit verbunden.

latex-resource registriert zunächst Paketabhängigkeiten mit title, package und assumptions. Im ersten Paketumfang stehen amsthm, amssymb und array zur Verfügung. Der Export sammelt diese Ressourcen einmalig im Vorspann. Makros, Literatur, Abbildungen und Pakete außerhalb dieses Umfangs benötigen weitere geprüfte Ressourcentypen. Die deklarierte Abhängigkeitsliste wird noch nicht automatisch aus beliebigem TeX erschlossen.

Ausgewählte Textblöcke werden als Original-LaTeX ausgegeben. Der Export startet weiterhin keinen Compiler. Redaktionelle Reihenfolge folgt der Wurzelauswahl unter Wahrung der deklarierten Voraussetzungen. Ein transition-Objekt ist derzeit ein explizit ausgewählter Textbaustein mit Voraussetzungen; die automatische Platzierung zwischen bestimmten Quell- und Zielaussagen folgt später.

python -m qam.tools.store_latex_example --out NEUER_ORDNER registriert den vorhandenen Satz v480:native-penalty-identity und seinen Originalbeweis aus native-operator-link.tex. Die positiven Metrik-/Domänenannahmen werden mitgeführt. Das lokale Ergebnis build/qam-original-latex-example/paper.pdf wurde zweimal kompiliert und visuell als einseitige Ausgabe kontrolliert. Die Kompilierung prüft die Darstellung; eine neue mathematische Beweisprüfung ist damit nicht erfolgt.

Sieben Testsuiten sind erfolgreich. test_latex_blocks prüft Paketauflösung, wortgetreuen Beweisexport, Übergangstext mit offener Voraussetzung, Quellenbindung sowie atomaren Abbruch bei fehlenden Abhängigkeiten.

## Automatische Übergangsplatzierung

transition unterstützt optional placement mit after und before als genauen Versionshashes. Beide Endpunkte müssen bereits im selben Frame registriert sein. Diese Angaben steuern die redaktionelle Reihenfolge und werden getrennt von dependencies gespeichert.

Sind beide Endpunkte in einer Snapshot-Auswahl enthalten, wird der passende Übergang automatisch hinzugenommen. Wird ein Übergang selbst als Wurzel ausgewählt, werden seine beiden Endpunkte als Kontext aufgenommen. Die resultierende Reihenfolge erfüllt logische Voraussetzungen und die redaktionelle Bedingung after vor Übergang vor before. Widersprechende Bedingungen werden als Zyklus diagnostiziert.

Bei mehreren Versionen desselben passenden Übergangsobjekts ist eine explizite Versionsauswahl erforderlich. Die Auswahl verwendet alle Informationen ausschließlich aus dem gewählten Snapshot. Ein Übergangstext wird durch seine Platzierung nicht zu einem geprüften mathematischen Schluss.

Das Beispiel store_latex_example registriert jetzt einen eigenen redaktionellen Text aus penalty_transition.tex zwischen Originalsatz und Originalbeweis. Die resultierende PDF build/qam-transition-example-v2/paper.pdf wurde als eine Seite gebaut und visuell geprüft. Acht Tests prüfen unter anderem automatische Einfügung, explizite Versionswahl, alte Snapshots und Reihenfolgekonflikte.

## Makro- und Literaturressourcen

latex-resource unterstützt zusätzlich resource_type macro und bibliography. Gemeinsame Felder sind title, latex, assumptions und dependencies. Makros besitzen name ohne führenden Backslash; im ersten Umfang ist genau eine passende balancierte newcommand-Deklaration mit optionaler Argumentanzahl erlaubt. Literaturbausteine besitzen key und genau ein passendes bibitem. Beide müssen wörtlich in der angegebenen Quelldatei vorkommen.

Der Export sammelt Makros nach Voraussetzungssortierung im Vorspann und Literaturbausteine am Dokumentende. Verschiedene ausgewählte Versionen derselben Makro- oder Literaturkennung führen vor Anlegen der Ausgabe zu einem Konflikt. Benutzerdefinierte Makros werden noch nicht automatisch im freien LaTeX erkannt; die benötigten Versionen werden als dependencies deklariert. Gleiches gilt für Zitate. Allgemeine Makrorekursion, Paketoptionen, BibTeX und Biber sind weitere Ausbaustufen.

python -m qam.tools.store_resource_example --out NEUER_ORDNER übernimmt das Versionsmakro aus working-preamble.tex und den vorhandenen Edwards1974-Eintrag aus der Bibliografie. Ein expliziter Beispieltext verwendet beide. Die erzeugte einseitige PDF build/qam-resources-example/paper.pdf wurde zweimal kompiliert und visuell geprüft; das Log enthält keine undefinierten Zitate oder Verweise. Der Inhalt ist ein Montagebeispiel. Die bibliografische Quelle wird damit nicht fachlich neu verifiziert.

Neun Tests prüfen unter anderem Ressourcensammlung, Einmaligkeit, Quellenbindung und Konflikte zwischen zwei Makroversionen. Das Manifest enthält zusätzlich den Hash des Ressourcencodes.

## Technische Referenzprüfung vor dem Export

scrub --hash SNAPSHOT --request DATEI prüft dieselbe roots-Auswahl wie select. Der begrenzte statische Prüfer erfasst literale label-, ref-, eqref-, pageref-, autoref-, cref-/Cref- und cite-/citep-/citet-/nocite-Verwendungen. Er überspringt Kommentare und maskierte Kontrollzeichen. Unterstützte Optionsklammern an Zitaten werden berücksichtigt. Doppelte Labels einschließlich Kollisionen mit generierten qv-Labels, fehlende Zielkennungen und fehlende Bibliografieeinträge führen zu blocked.

Dynamisch gebildete Referenzen, externe Einbindungen und erkannte Verbatim-/Listing-Umgebungen sind außerhalb dieses ersten Prüfvertrags und blockieren die automatische Freigabe. Der Prüfer expandiert keine Makros und interpretiert keine beliebige TeX-Programmlogik. Die allgemeine Prüfung verfügbarer Makros und Paketbefehle steht noch aus. passed betrifft ausschließlich den dokumentierten statischen Umfang; der LaTeX-Build bleibt eine weitere Kontrolle.

EXPORT führt diese Prüfung vor dem Anlegen des Ausgabeordners aus und legt Bericht sowie Prüferhash im Manifest ab. Die eigenständige scrub-Abfrage gibt bei blocked Prozesscode 1 zurück. Fachliche Findings und offene Guards bleiben im Entwurf sichtbar. Der technische Prüfstatus ändert ihre Beurteilung nicht.

Elf Tests prüfen die bisherigen Pfade sowie Kommentare, dynamische Verweise, fehlende Zitate, doppelte Labels und den Abbruch vor der Dateierzeugung. Das Ressourcenbeispiel besteht die neue Prüfung. Sein erzeugter TeX-Text wurde bytegenau mit dem bereits kompilierten und visuell geprüften Beispiel verglichen.

## Begrenzter Makro- und Umgebungscheck

SCRUB prüft zusätzlich verwendete Kontrollwörter gegen einen expliziten Katalog für die feste article-/amsmath-Ausgabe, die ausgewählten Paketressourcen und die registrierten Makronamen. Erkannte unbekannte Befehle führen zu unresolved-command. Zum Beispiel benötigt mathbb die Paketressource amssymb und die proof-Umgebung amsthm. Weitere gültige TeX-Befehle außerhalb des Katalogs können deshalb zunächst blockiert werden und benötigen eine begründete Erweiterung des Vertrags.

Registrierte Makros werden auf Kollisionen mit bekannten Befehlen und auf direkt erkennbare Rekursion über andere registrierte Makros geprüft. Unterstützte Umgebungen sind ebenfalls ausdrücklich begrenzt. Allgemeine TeX-Expansion, bedingte Definitionen, dynamische Befehlsnamen und sämtliche Kontrollsymbole werden dadurch nicht vollständig analysiert. Der technische Status bleibt auf diesen statischen Umfang beschränkt.

Zwölf Tests prüfen die bisherigen Abläufe sowie fehlende Makros, fehlende Pakete, unbekannte Umgebungen, Selbstrekursion und Namenskollisionen. Die bereits gebauten Beispiele mit Originalbeweis und mit Versionsmakro/Literatur bestehen die erweiterte Prüfung auf ihren gespeicherten Auswahlen.

## Erster zusammenhängender Forschungszweig

python -m qam.tools.store_koide_branch --out NEUER_ORDNER übernimmt den begrenzten Abschnitt zur zusätzlichen Koide-Bedingung aus koide-and-kernel.tex. Enthalten sind der Ausgangsrahmen nichtnegativer Hauptwurzeln, vier Aussagen, vier Originalbeweise und vier Erläuterungen. Das umfasst Gleichnormbedingung, bedingte HC-Realisierung, Radius/Phase und die zyklische Symmetriesperre.

Die Abhängigkeiten sind für diesen begrenzten Ausschnitt ausdrücklich zugeordnet. Die ursprünglichen Labels bleiben erhalten. Die native Massenauslesung und eine unabhängig hergeleitete Gleichnorm-/HC-Bedingung stehen als zwei offene Guards im Store. Der historische Zahlenvergleich behält seine Quellenqualifikation. Sämtliche mathematischen Textobjekte sind conditional übernommen. Dieser Import führt keine neue automatische Prüfung der allgemeinen Beweise durch.

Die erzeugte PDF build/qam-koide-branch-v2/paper.pdf umfasst drei Seiten und wurde nach zwei LaTeX-Läufen visuell geprüft. Das Log enthält keine Overfull-, Referenz-, Label- oder Rerun-Meldungen. Wiederholte gleichlautende Prüfhinweise werden im sichtbaren Entwurf gezählt zusammengefasst; das Manifest behält alle einzelnen Findings. Dreizehn Tests prüfen einschließlich des echten Quellenimports die vier Aussagen, vier Beweise und zwei offenen Anschlussstellen.

## Fachliche Argumentansicht

view --hash SNAPSHOT --request DATEI verwendet die roots-Auswahl und erzeugt Markdown mit Mermaid-Graph, Bausteintabelle, genauen Versionshashes und offenen Anschlussstellen. --out DATEI schreibt die Ansicht in eine neue Datei. Die Ansicht wird vollständig aus dem Snapshot berechnet.

requires und interpreted-by werden von der Voraussetzung zur Verwendung gezeichnet. Andere Beziehungen folgen ihrer gespeicherten Richtung. Deklarierte und vorgeschlagene Kanten sind gepunktet, review-markierte Kanten durchgezogen. Ein solcher Review ist die protokollierte Beurteilung mit ihrer vorhandenen Evidenzart. Er ist keine automatische mathematische Zertifizierung.

Die Auswahl enthält nun auch die zugehörigen Relationsdatensätze mit effektivem Reviewstatus. Das ändert den Auswahlhash des erweiterten Ausgabeformats; bestehende Snapshots, Belege und alte Exportmanifeste behalten ihre ursprünglichen Inhalte. Die live erzeugte Argumentansicht kann deshalb einen anderen Auswahlhash als ein früherer PDF-Export derselben Wurzeln haben.

Die erste Ansicht build/qam-koide-branch-v2/argument.md enthält 14 Bausteine und 17 deklarierte Kanten sowie zwei offene Guards. Vierzehn Tests prüfen inzwischen die Store-Kette einschließlich dieser Graphprojektion. Die fachliche Abhängigkeitszuordnung dieses begrenzten Zweigs ist ausdrücklich deklariert und noch separat zu prüfen.

## Integrität des eingebetteten Store-Bestands

snapshot-check --hash HASH prüft die internen Versions-, Relations-, Guard-, Review- und Belegidentitäten sowie deren Verweise. Die gleiche Prüfung läuft vor dem Speichern und nach dem Lesen eines Snapshots. Ein gültiger äußerer Snapshot-Hash allein genügt damit nicht, um inkonsistente eingebettete Daten als gültigen Bestand weiterzureichen.

Geprüft werden insbesondere rekonstruierte Inhaltsversionshashes, fehlende Adressen, Review-Vorgänger und Verzweigungen, Belegheader und die Zuordnung ihrer Eingabeversionen. Die Prüfung betrifft den gespeicherten Stand. Aktuelle Dateibytes auf dem Dateisystem und mathematische Gültigkeit sind zusätzliche Prüfungen. Inhaltsadressierung ersetzt keine Authentifizierung des Urhebers.

Fünfzehn Tests sind erfolgreich. Die Integritätstests verändern Kopien eines Snapshots und prüfen die Erkennung geänderter Inhalte, fehlerhafter Relationen, widersprüchlicher Belegheader und entfernter Eingabeverknüpfungen. Der bestehende Koide-Snapshot besteht die neue Integritätsprüfung.

## Quellenstand und Auswirkungen

freshness --hash SNAPSHOT vergleicht gespeicherte Quell-SHA256 mit den aktuellen Dateien unter --repo. Beobachtungen unterscheiden matches, bytes-changed, missing, unreadable und invalid-path. Die Auswertung erfasst Quellenfundstellen sowie Guard-Quellen und Review-Nachweise. Schon eine reine Änderung der Zeilenenden kann bytes-changed ergeben. Das ist ein Anlass zur Prüfung und keine automatische Aussage über eine mathematische Änderung.

impact --hash SNAPSHOT --request DATEI verfolgt roots als genaue Versionshashes über deklarierte und review-markierte requires-/interpreted-by-Kanten zu abhängigen Versionen. Redaktionelle Übergangsendpunkte werden als eigene Kontextabhängigkeiten berücksichtigt. Die Ausgabe listet betroffene Prüfbelege, Guards und gespeicherte Snapshots, die betroffene Versionen enthalten. Vorgeschlagene oder abgelehnte Abhängigkeiten werden dabei nicht als bestätigte Voraussetzungen verfolgt.

freshness enthält getrennte Auswirkungen veränderter Inhaltsquellen und veränderter Evidenzdateien. Ein Review mit inzwischen geänderter Nachweisdatei wird zur erneuten Prüfung gemeldet. Historische Reviews und Belege bleiben in ihren gespeicherten Zuständen erhalten. containing_snapshots bezeichnet Bestände, die die genannten Versionen enthalten. Daraus folgt keine automatische Ungültigkeit jeder möglichen Auswahl aus diesen Beständen.

Beide Abfragen ändern weder Inhalt noch Ledger. Bei Quellenabweichungen liefert freshness den Status review-needed und Prozesscode 1. Der Bericht hat einen eigenen Inhalts-Hash. Die Zuordnung eines gespeicherten Textblocks zum genauen Locator ist weiterhin eine deklarierte Herkunftsangabe.

Sechzehn Tests sind erfolgreich. Der neue Test verändert Definition und Review-Nachweis, prüft transitive Abhängigkeiten, historische Ergebnisse, fehlende Dateien, CLI-Prozesscode und das unveränderte Ledger. Am vorhandenen Koide-Snapshot stimmen alle 27 erfassten Quellverknüpfungen einschließlich Guard-Quellen mit dem aktuellen Dateistand überein.

## Gespeicherte Paperfassungen

Schema v5 ergänzt qstore_papers als unveränderliche Folge benannter Zusammenstellungen. paper-save --request DATEI erwartet paper_id, title, snapshot_hash, roots, profile und previous. Im ersten Umfang ist profile research-draft. previous ist null für die erste Fassung und danach der aktuelle Paperhash. Ein veralteter oder fremder Vorgänger wird zurückgewiesen.

Die Fassung speichert neben der Wurzelauswahl die vollständig aufgelöste Auswahl und den Hash des Auswahlcodes. Damit bleibt die gewählte Reihenfolge samt automatischen Voraussetzungen festgehalten. paper-read --hash HASH prüft Inhaltsidentität, gespeicherten Auswahlhash und den referenzierten Snapshot. paper-export --hash HASH --out NEUER_ORDNER verwendet die eingefrorene Auswahl und schreibt Paperidentität und Titel in das Manifest. Die aktuelle technische Exportprüfung läuft erneut. Bei geändertem Generator können sich Ausgabe und Manifest ändern; die Generatorhashes machen das sichtbar.

Die Paperfassungen sind Metadaten über einem Snapshot und liegen außerhalb dessen bisherigem mathematischen Tabellenumfang. Eine vollständige Datenbanksicherung muss deshalb auch qstore_papers enthalten. Eine veröffentlichungsfähige Statusfreigabe und ein vollständiger portabler Store-Export stehen weiter aus.

Die erste lokale Zusammenstellung koide-condition-note bindet den bisherigen Koide-Snapshot mit seinen offenen nativen Guards. Ihr Hash lautet e2ffe9581d15ebc347e60f77f3d83993fe0aeaa6b948fc7eddf057d0cb18354c. Die dreiseitige Ausgabe build/qam-koide-paper-profile/paper.pdf wurde gebaut und visuell geprüft. Sie ist ein Forschungsentwurf mit eigenem Titel.

Siebzehn Tests prüfen einschließlich Paperrevisionen die Wiederholung, unveränderte alte Fassungen, identische Wiederholungsexporte bei gleichem Code, enthaltene Paperidentität, konkurrierende Vorgänger und die Sperre gegen Überschreiben oder Löschen.

## Vollständige Datenbanksicherung und Wiederherstellung

backup --out NEUER_ORDNER erzeugt mit der SQLite-Backup-API eine konsistente Kopie der ganzen Datenbank. Dadurch sind alle Tabellen enthalten, einschließlich älterer QAM-Claims und MMA-Belege, Store-Objekte, Snapshots und Paperfassungen. Änderungen im SQLite-WAL werden berücksichtigt. Der Lauf begrenzt die Kopierzeit auf 30 Sekunden.

Die Ausgabe besteht aus qam.sqlite3 und einem zuletzt geschriebenen manifest.json mit Dateihash, Größe, SQLite-Version und Zeilenzahlen aller Tabellen. backup-check --archive ORDNER prüft Hash, Größe, SQLite-integrity_check, Fremdschlüssel und Tabelleninventar. Quellen- und PDF-Dateien außerhalb der Datenbank bleiben separate Artefakte. Die Sicherung des Quellrepositorys und der Python-Abhängigkeiten gehört für eine andere Maschine dazu.

restore --archive ORDNER --out NEUE_DATENBANK validiert zuerst die Sicherung. Eine temporäre Kopie wird erneut geprüft und danach atomar unter einem neuen Datenbankpfad bereitgestellt. Vorhandene Ziele werden zurückgewiesen. Das Archivformat enthält eine vollständige SQLite-Datenbank und ist kein SQL-Dump, der beim Import frei definierte Anweisungen ausführt.

Die lokale Sicherung build/qam-backup-2026-11-11 enthält 25 Tabellen. Die Wiederherstellung nach build/qam-restore-verification/qam.sqlite3 wurde geprüft. Aus der wiederhergestellten Datenbank erzeugte die gespeicherte Koide-Paperfassung byteidentische paper.tex- und manifest.json-Dateien. Es handelt sich um eine lokale Sicherung im Buildordner; eine unabhängige externe Kopie muss separat abgelegt werden.

Achtzehn Tests sind erfolgreich. Der Sicherungstest deckt WAL-Inhalte, zusätzliche bestehende Tabellen, gespeicherte Paperfassungen, identische Wiederexporte, vorhandene Zielpfade und ein beschädigtes Archiv ab.

## Gesamtinventar im Store

import-inventory --out NEUER_ORDNER übernimmt die unterstützten Aussageumgebungen der aktiven Einbindungskette in einer gemeinsamen Store-Transaktion. Erfasst werden definition, theorem, lemma, proposition, corollary, assumption, axiom und conjecture. Definitionen erhalten den Typ definition, Annahmen/Axiome assumption und die übrigen Aussageformen claim. Der ursprüngliche Umgebungstyp bleibt als Metadatum erhalten.

Der Import bewahrt den Originaltext einschließlich Kommentaren. Kommentare werden für die Erkennung längentreu maskiert. Geschachtelte gleichartige Umgebungen werden bis zum passenden Ende gelesen. Die Erkennung erfolgt vor TeX-Expansion; Aussagen in freiem Fließtext, bedingte TeX-Ausführung, Makrodefinitionen mit eingebettetem Umgebungstext und Verbatim-Sonderfälle benötigen weitere fachliche beziehungsweise Parserprüfung.

Jede Aussage trägt imported-unreviewed, Frame unspecified und eine offene Prüfpflicht für Status, Interpretation, tatsächliche Voraussetzungen, Beweiszuordnung und Ressourcen. Die Prüfpflicht verlangt eine native physikalische Brücke nur dort, wo sie fachlich erforderlich ist. Der Import schreibt keine bewiesenen logischen Abhängigkeiten. Insbesondere ist eine im Quelltext theorem genannte Umgebung dadurch nicht mathematisch neu bestätigt. Archiv- und historische Texte innerhalb der aktiven Einbindung sind enthalten.

Dateien und Themen sind topic-Objekte. contains-Kanten deklarieren die Dokumentstruktur, belongs-to-Kanten sind vorgeschlagene organisatorische Themenzuordnungen. Die Heuristik nutzt Dateinamen, Titel und den letzten erkannten Abschnitt. Ihre Kategorien lehnen sich an das Gesamtbild an. Mehrdeutige Fälle verbleiben im Bereich Übergreifend oder noch zuzuordnen.

Eine Importgeneration bindet die Quellhashes sowie Importer- und Collector-Codehashes. Root-, Datei- und Themencontainer werden je Generation versioniert, damit eine spätere Quelle nicht die frühere Dokumentstruktur überschreibt. Aussageidentitäten verwenden quellqualifizierte Labels, bei fehlenden Labels vorläufige positionsabhängige Kennungen. Diese Kennungen benötigen bei Umstellungen eine gesonderte Identitätsprüfung. Früher manuell kuratierte Fassungen bleiben separat; eine automatische mathematische Gleichsetzung mit Importobjekten erfolgt nicht.

Der Lauf am 11. November erfasste 2468 Aussageumgebungen aus 61 Dateien, darunter 983 Definitionen. Er legte 2468 offene Prüfpflichten an. 518 Aussagen haben kein Label. 841 Aussagen bleiben thematisch übergreifend oder unzugeordnet. Ein identischer Wiederholungslauf erzeugte keine neuen Objekte oder Ledgerereignisse.

inventory-view --hash SNAPSHOT --request DATEI mit root als Inventar-Rootversion rekonstruiert die Übersicht direkt aus den gespeicherten contains- und belongs-to-Kanten. --out DATEI schreibt sie in eine neue Datei. Die Übersicht enthält Themenzahlen und eine Quellenliste. Die technische Prüf- und Exportbereitschaft einzelner importierter Aussagen ist weiterhin separat herzustellen.

Die aktuelle Übersicht liegt unter build/qam-manuscript-inventory/database-overview.md, der Importbericht unter build/qam-manuscript-inventory/import.json. Der geprüfte Snapshot ist 2a3b9f873a47cdb91eca2c4016820b492ca30c516918112fc714b65200073735. Eine lokale vollständige Sicherung liegt unter build/qam-manuscript-inventory-backup. Die Grenzen der externen Quelldateisicherung gelten weiterhin.

Zwanzig Tests sind erfolgreich. Die neuen Regressionen prüfen Kommentare, geschachtelte Umgebungen, wiederholten Import, unverändertes Ledger, neue Inhaltsversionen, erhaltene alte Snapshots und die direkt aus der Datenbank erzeugte Übersicht.

## Fachliche Selbstprüfung des ersten Koide-Zweigs

python -m qam.tools.review_koide_store --out NEUER_ORDNER gleicht die vier importierten Propositionen mit den kuratierten Aussageblöcken ab. Die Prüfung ist an den konkreten SHA256 der Originalquelle und den Bericht notes/research/koide_store_branch_review_2026_11_11.md gebunden. Eine geänderte Originalquelle verhindert die erneute Anwendung ohne Überprüfung des Berichts.

Die dokumentarische same-source-as-Beziehung wird nach exaktem Vergleich des inneren Propositionstexts registriert. Sie gleicht Herkunft ab; sie ist keine physikalische Frameabbildung. Die vier Originalbeweise und ihre mathematischen Voraussetzungen wurden als Selbstprüfung unter den genannten Hypothesen beurteilt. Die zugehörigen Beweis- und Definitionsbeziehungen tragen deklarierte Review-Provenienz. Drei explizite Definitionsbereiche präzisieren die abstrakte reelle Interpretation.

Für das zyklische lineare Lemma wurde die unnötige Abhängigkeit von Hauptwurzelpositivität zurückgewiesen. Vier alte generische Importprüfpflichten sind über die geprüfte kuratierte Interpretation bearbeitet protokolliert. Der rohe Import behält seinen ursprünglichen ungeprüften Status und den unspezifizierten Frame; sein alleiniger Export ist damit nicht freigegeben.

Vier präzise native Guards betreffen Wurzelwörterbuch, Gleichnormauswahl, Phase/Skala und Hierarchiemechanismus. Die beiden vorherigen breiten nativen Guards bleiben offen. Die sechs offenen Einträge bedeuten vier präzisierte Pflichten neben den zwei übergeordneten Pflichten. Historische Zahlenvergleiche wurden nicht als neue Messungen oder neue numerische Vorhersagen geprüft.

Der neue Snapshot ist 627534d5a7a69033cba57f9f5facb4f1a0fd4a1d9c300eb27fe46be99e7abeae. Die gespeicherte Paperrevision 6c0a3b0b995b5031648e3a0795fe84f23f456583abc1a62c3c031569648f2688 bindet die geprüften mathematischen Abhängigkeiten. Ihre Ausgabe build/qam-koide-reviewed-paper/paper.pdf wurde als vierseitiger Entwurf gebaut und visuell geprüft. Der Graph build/qam-koide-reviewed-v2/argument.md enthält zusätzlich die importierten Entsprechungen.

22 Storetests einschließlich Quellenbindung, Idempotenz und verbleibender Guards sowie die 35 vorhandenen Koide-/Kerneltests sind erfolgreich. Die mathematischen Urteile stammen aus der dokumentierten Selbstprüfung. Die Tests und Reviewmarkierungen werden nicht als unabhängiges oder formales Beweiszertifikat behandelt.


## HC-Identifikationszweig: Selbstprüfung vom 2026-11-11

Fünf Aussagen aus `hc-mass-identification.tex` sind mit Originalbeweisen,
expliziten lokalen Definitionsbereichen und geprüften Quellzuordnungen registriert.
Die Selbstprüfung bestätigt die abstrakten Aussagen unter ihren Voraussetzungen.
Sie konstruiert keine native Massenauslesung. Vier Guards bleiben offen:
HC-/Skalarinterpretation, native Mass-root-Abbildung, Generationenkopplung sowie
unabhängige Normselektion, Phase und Skala. Die generischen Guards der Rohimporte
bleiben vorsichtshalber offen; deren Metadaten werden nicht umgeschrieben.

Reproduktion: `python -m qam.tools.review_hc_store --db build/qam.sqlite3 --out build/hc-review-new`.
Der Zielordner muss neu sein. Der Lauf prüft den festgehaltenen Quellhash und
registriert wiederholt dieselben Versionen. Ausgabe: Argumentationsbaum, JSON-Bericht
und LaTeX-Entwurf. Selbstprüfung: `notes/research/hc_identification_store_review_2026_11_11.md`.
Die Übertragung zum Koide-Zweig ist noch nicht als eigene geprüfte Verbindung registriert.

### Bedingte HC–Koide-Verbindung (Folgeschritt, 2026-11-11)

Die zuvor fehlende Verbindung ist jetzt als source-pinned Erklärung mit zwei
geprüften Abhängigkeiten zu den Originalbeweisen registrierbar:
`python -m qam.tools.review_hc_koide_bridge --out build/hc-koide-new`.
Voraussetzung sind der registrierte Koide- und HC-Zweig. Der Zielordner muss neu sein.
`hc_koide_bridge.py` prüft beide Quellhashes vor der Registrierung.
Die wiederholte Anwendung fügt keine neuen Versionen oder Reviews hinzu.

Abstieg plus unabhängiger Seed und zulässiges Wurzelgesetz liefern
`K=2/[3(1+h)]`, mit `h=<B*e,JB*e>`. Erst `h=0` liefert Koide.
Drei zusätzliche Guards bleiben offen: native Realisierung, unabhängige
Orthogonalität und maschinenprüfbare Frame-Abbildung. Die Auswahl behält
`frame-bridge-required`; eine manuelle Selbstprüfung ersetzt keinen typisierten
Abbildungsnachweis. Die Originalquellen und bestehende Guards bleiben unverändert.
Bericht: `notes/research/hc_koide_bridge_review_2026_11_11.md`.

## Gegenterm-Register (Schema v7, Phase 1, 2026-11-14)

Das Register trennt einen geschützten Strukturkern von lokalen, effektiven
Kompensationstermen δ_i. Ein Gegenterm ist Buchführung, keine Herleitung:
Er schließt weder OP1–OP5 noch C5 oder C6/T2. Die Tests verwenden nur die
Fixture CT-000-TEST in einer temporären Datenbank. Seit 2026-11-14 sind
zwei physikalische Gegenterme als reproduzierbare Eintragung festgehalten:
CT-001 (Phaseneinheit des Lepton-Flusses, partially_constrained) und CT-002
(Kopplung an eine Horizont-Punktierung, placeholder), dazu H102 mit
`depends-on-counterterm`-Kanten. Skript und Bericht mit allen Hashes:
`notes/research/counterterms/register_ct001_ct002_2026_11_14.py` und
`register_2026_11_14_report.json`. Die Datenbank selbst liegt unter `build/`
und ist nicht versioniert; das Skript baut sie mit denselben Hashes neu.

Schema v7 ergänzt nur den Typenkatalog um `counterterm-scheme` und
`counterterm-transition` (`catalogue_v7.json`) und sperrt den Katalog gegen
Ändern und Löschen. Bestehende Tabellen und Trigger bleiben unverändert;
v1–v6-Datenbanken werden bei der Initialisierung erweitert. Der neue
Relationstyp `depends-on-counterterm` verlangt als Ziel eine
`counterterm-scheme`-Version im selben Frame. `impact` folgt ihm wie
`requires`.

`python -m qam.store.counterterms store --request DATEI` registriert eine
Version. Die Payload verlangt genau title, target_sector, operator_basis,
compensation_function (symbolic, parameters, form), reference_scale,
matching_condition, rg_flow (Text oder null), validity_domain (variable,
interval, samples, description), magnitude_convention (signed oder
magnitude), replacement_tolerance, open_guards, assumptions und scope.
Parameter tragen value (exakt rational oder null), bounds und role
(fit_parameter, regulator_cutoff, fixed_input). Werte außerhalb der Grenzen,
leere Intervalle, Stützstellen außerhalb des Gültigkeitsbereichs und eine
leere Guard-Liste werden abgelehnt. Die Rolle orientation_sign ist verboten:
Das Orientierungsvorzeichen o_R bleibt ein eigener Faktor außerhalb von
|δ_i|. Jeder Eintrag in open_guards wird als offener Guard der Version
gespeichert. `form` ist optional ein exaktes Polynom (`qam-polynomial-v1`,
Koeffizienten als Rationalzahlen oder Parameternamen).

Der Lebenslauf jeder Gegenterm-Version ist eine append-only Kette von
`counterterm-transition`-Versionen (`transition`). Ohne Übergang gilt
placeholder. Erlaubt sind placeholder → partially_constrained | deprecated,
partially_constrained → structurally_matched | deprecated und
structurally_matched → deprecated; deprecated ist endgültig. Jeder Übergang
nennt den aktuellen Vorgänger, Prüfer, Grund und eine gehashte Evidenzdatei.
Eine veraltete Vorgängerangabe wird abgelehnt. Jeder Statuswechsel schreibt
das Ledgerereignis `COUNTERTERM-REAUDIT` mit allen abhängigen Versionen.
Das markiert Kandidaten für eine Neuprüfung und widerruft nichts.

`residual --request DATEI` mit scheme und replacement wertet
Δ = F − δ exakt an den deklarierten Stützstellen aus. Die Ersatzstruktur ist
ein Seed mit value_type `qam-polynomial-v1` im selben Frame. Fehlende
Parameterwerte ergeben `blocked`. Liegt |Δ| an einer Stelle über
replacement_tolerance, ergibt sich `failed`, und der Beleg enthält die
Verschiebung Δ je Stützstelle. Bei magnitude_convention = magnitude gilt ein
negativer δ-Wert als `failed`, weil dann ein Vorzeichen absorbiert sein kann.
Der Beleg prüft nur endlich viele Punkte und ist keine Schranke auf dem ganzen
Bereich. structurally_matched verlangt einen bestandenen Beleg für genau
dieses Paar.

`resolve --hash VERSION` folgt deklarierten oder geprüften `requires`-,
`interpreted-by`- und `depends-on-counterterm`-Kanten. Jeder erreichte
Gegenterm mit Status ≠ structurally_matched vererbt seine offenen Guards;
deprecated wird zusätzlich gesondert ausgewiesen. Nach einem Strukturabgleich
folgt die Auflösung der Ersatzstruktur, deren eigene Guards unter
replacement_guards erscheinen.

`roles --request DATEI` prüft Termmarkierungen einer Aussage und speichert
einen Beleg `qam-term-role-v1`. Die Rollen structural_core und
counterterm_compensation sind Termrollen. Sie sind von den Front/Back-
Indexrollen von `qam-role-audit/2` getrennt. Regeln: T1 unbekannte Rolle oder
eingemischte Indexrolle; T2 Kompensationsterm ohne registrierten Gegenterm
oder ohne deklarierte Abhängigkeitskante; T3 Absorption in den Kern ohne
protokollierten Strukturabgleich; T4 absorbiertes oder fehlendes
Orientierungsvorzeichen; T5 eine reine Kernaussage, die still von einem nicht
abgeglichenen Gegenterm abhängt. Tests: `python -m unittest
qam.store.test_counterterms`. Der LaTeX-Export der Registertabelle folgt
unten (Phase 2).

### Rapid Prototyping: Fit-Herkunft, Blindheit und Δ als Vorhersage

Das Register soll schnelle Prototypen tragen, deren Gegenterme später durch
Herleitungen ersetzt werden. Dafür gilt zusätzlich:

- `operator_basis` ist ein Objekt aus kind (lagrangian_operator oder
  readout), expression und frame. Eine benannte Auslesegröße ist zulässig.
  Ihr Frame muss dem deklarierten Frame entsprechen.
- Ein Parameter mit der Rolle discrete_choice trägt options als endliche
  Liste und value als gewählte Option oder null. Er hat keine Grenzen.
- `fitted_on` ist null, wenn alle θ gesetzt sind. Andernfalls enthält es
  method, die angepassten parameters, data mit label, source, version und
  value, uncertainty als rationales σ je stetigem Fitparameter und scan.
  scan ist null oder eine Auswahl aus trials, hits und chance_expectation.
- `known_tensions` hält bekannte Spannungen vor jeder Ersetzung fest. Jeder
  Eintrag enthält description, convention, delta und source.
- `blindness --request DATEI` mit statement und tested_against (label,
  source, version) meldet `not_blind`, sobald ein Vergleichsdatum über
  (source, label) im fitted_on eines Gegenterms der Abhängigkeitshülle
  vorkommt. Abweichende Datenversionen werden ausgewiesen. Der Beleg gilt nur
  für registrierte Fits; nicht registriertes Tuning bleibt unerkannt.
- Der Residuenbeleg weist Δ je Stützstelle gegen die Toleranz und gegen das
  Fitband aus. Das Fitband ist die lineare Fehlerfortpflanzung
  Σ_k |∂δ/∂θ_k| σ_k. Das Urteil lautet compatible-within-tolerance,
  exceeds-tolerance-within-fit-uncertainty oder deviates-from-fit. Nur das
  erste Urteil erlaubt structurally_matched. Andernfalls bleibt δ_i stehen,
  und Δ_i wird als Abweichung der Herleitung vom Fit berichtet.

### Phase 2: Registertabelle im LaTeX-Export (2026-11-14)

- `select_versions` folgt jetzt auch `depends-on-counterterm`-Kanten. Erreicht
  eine Auswahl einen Gegenterm, trägt sie den Schlüssel `counterterms` mit
  Lebenslaufstatus, Übergängen, Ersatzstruktur und offenen Guards jedes
  Eintrags, gelesen nur aus dem Snapshot. Auswahlen ohne Gegenterm bleiben
  bitgleich, ihre Hashes ändern sich nicht.
- `render` setzt Gegenterm-Einträge nie als Kerntext. Jede Aussage, die über
  `requires`, `interpreted-by` oder `depends-on-counterterm` einen Gegenterm
  erreicht, bekommt einen Vermerk „Effective scope“ mit Status und geerbten
  Guards; nach einem Strukturabgleich verweist er auf den Anhang.
- Der Anhang „Counterterm and compensation registry“ listet jeden Eintrag mit
  Status, Basis, Funktionsform, Parametern (Grenzen oder diskrete Optionen),
  Gültigkeitsbereich, Fit-Herkunft samt Hinweis „nicht blind“, bekannten
  Spannungen und offenen Guards. Bei structurally_matched nennt er die
  Abgleichsidentität F = δ + Δ mit Ersatzstruktur und Residuenbeleg; die
  phänomenologische Form bleibt in der Versionsgeschichte.
- Harte Prüfung in `export_selection`: Fehlt einer abhängigen Aussage ihr
  Vermerk oder einem Eintrag sein Anhangsabschnitt, bricht der Export ab
  (`counterterm_export_issues`).
- Tests: `python -m unittest qam.store.test_counterterm_export`, einschließlich
  einer pdflatex-Übersetzung des Entwurfs, wenn pdflatex vorhanden ist.
