# Wiki-Pflege

Das Wiki erschließt Quellen und Forschungsergebnisse. Neue mathematische Behauptungen benötigen ihre Begründung in den Projektquellen; eine Wiki-Formulierung allein ändert keinen Beweisstatus.

## Aktualisierung

1. Aktuellen Remote-Stand und vorhandene Wiki-Änderungen abrufen. Lokale Arbeitskopien können hinter GitHub zurückliegen.
2. Öffentliche Baseline anhand README, CITATION, Release-Payload und Publikationsnachweis prüfen. Layer sind keine Releases.
3. Betroffene Quellen, Statusnotizen und spätere Korrekturen lesen. Voraussetzungen und offene Pflichten erhalten.
4. Startseite, Quellenkarte und Fachübersicht zusammen aktualisieren, wenn sich Version oder Aussagegrenzen ändern. Für reproduzierbare Angaben einen vollständigen Commit verlinken.
5. Dateipfade, Wiki-Navigation, DOI-Verweise und Versionen prüfen; Änderungen im Ordner `wiki/` des Hauptrepositorys per Pull Request einbringen.

## Formelsatz und gemeinsamer Leseweg

Mathematik mit GitHubs LaTeX-Darstellung setzen: kurze Ausdrücke zwischen `$…$`, eigenständige Gleichungen zwischen `$$` auf eigenen Zeilen. Dateinamen, Labels und Befehle bleiben Code. Formeln nicht als Bilder einfügen; ihr Markdown-Quelltext bleibt so auch für LLMs lesbar.

Der Fließtext erklärt die Inhalte für Menschen. Technische Extraktionshinweise und Satzlabels in eingerückten **Anmerkungen für LLMs und Quellenprüfung** sammeln. Voraussetzungen und fachliche Grenzen bleiben in der menschlichen Erklärung sichtbar. Englisch entsprechend **Note for LLMs and source checking**. Formeln nach Veröffentlichung auf GitHub visuell prüfen.

## Quellenpriorität

Deutsch ist die redaktionelle Hauptsprache. Der Dokumentführer und das Koide-Beispiel haben englische Begleitfassungen. Inhaltliche Änderungen zuerst in der deutschen Fassung klären und anschließend in der zugehörigen englischen Seite nachziehen. Fundstellen, Voraussetzungen, Statusgrenzen und Kontrollantworten müssen übereinstimmen. Die englische Einstiegsseite benennt den Übersetzungsumfang; sie darf keine vollständige Übersetzung des Manuskripts suggerieren.

Der Dokumentführer verwendet eine didaktische Reihenfolge. Beim Aktualisieren die tatsächliche Include-Reihenfolge und Abschnittstitel der Quellen prüfen; keine dauerhaften PDF-Seitenzahlen ohne Versionsbindung verwenden. Lehrbeispiele ausdrücklich von nativen Modellen und Messwerten unterscheiden.

Für eine Veröffentlichung gelten deren unveränderte Payloads und Metadaten. Für Forschung gelten die zum gewählten Commit gehörenden Quellen einschließlich Korrektur- und Statuslayern. Ältere Berichte bleiben Herkunftsnachweise; ihr damaliger Status ist nicht automatisch aktuell. Bei Widersprüchen den Konflikt offenlegen und neuere, spezifische Statusangaben mit Herkunft benennen.

Hypothesen, Fits, negative Kontrollen und offene Fragen behalten ihre Kennzeichnung. Issues verlinken, ihren fachlichen Status aber nur nach Prüfung der Belege zusammenfassen.

## Technischer Ort und Pflegeumfang

Quelle der Seiten ist der Ordner [`wiki/`](https://github.com/Moriarty1982/QuantumSphere-Unfold/tree/main/wiki) im Hauptrepository. Der Workflow `.github/workflows/wiki-sync.yml` spiegelt ihn bei jedem Push auf `main`, der `wiki/` ändert, in das Wiki-Repository `https://github.com/Moriarty1982/QuantumSphere-Unfold.wiki.git`; er lässt sich auch von Hand starten. `_Sidebar.md` und `_Footer.md` liefern Navigation und Standhinweise.

**Nicht direkt im Wiki bearbeiten.** Änderungen über die Wiki-Oberfläche oder direkt im Wiki-Repository überschreibt der nächste Abgleich. Wiki-Änderungen gehören in denselben Pull Request wie die Repository-Änderung, die sie beschreiben.

Die Pflege erfolgt im Rahmen beauftragter Projektarbeiten. Eine zeitgesteuerte Hintergrundpflege ist durch diese Erstbefüllung nicht eingerichtet.

## Änderungsnachweis

**28.10.2026, Quelle ins Hauptrepository verlegt:** Seiten liegen jetzt unter `wiki/` und werden per Workflow ins Wiki gespiegelt, damit Wiki-Änderungen mit den Repository-Änderungen über Pull Requests laufen.

**28.10.2026, Layer r69:** Patches für r66–r68 eingespielt (lagen seit dem 25.10. lokal). Forschungsstand um einen OP5-Abschnitt zur Einbindung der Arbeitsserie vom 25.–27.10. ergänzt; Stand- und Layerangaben auf Commit b12adf5 und r69 gesetzt. Im r67-Eintrag den versehentlich ersetzten Commit wieder auf c4df998 gestellt.

**25.10.2026, Layer r68:** Forschungsstand um die unabhängige Nachrechnung ergänzt (U(1)- gegen SU(2)-Zählung); Stand- und Layerangaben auf Commit f2de387 und r68 gesetzt.

**25.10.2026, Layer r66:** Forschungsstand korrigiert: Der Widerspruch `thm:k-values` gegen `thm:frame-offset` stammt aus v4.9.0-r09 und ist dort aufgelöst; r66 holt die Zitierung nach. Hinweis zum lokalen Frame-Faktor ergänzt. Quellenstand: Merge von PR #43 (ce264ba).

**25.10.2026, Layer r67:** Forschungsstand um die Prüfung von `rem:einstein-blunder` ergänzt; Stand- und Layerangaben auf Commit c4df998 und r67 gesetzt. Fundstellen geprüft; keine mathematischen Manuskriptänderungen durch das Wiki.

**25.10.2026, Formelsatz und Lesefluss:** Deutscher und englischer Dokumentführer als gemeinsamer Weg für Menschen und LLMs überarbeitet; technische Hinweise als Anmerkungen markiert. Formeln in beiden Lesewegen, beiden Koide-Beispielen und im Forschungsstand auf LaTeX-Satz umgestellt. Mathematische Aussagen und Quellenstand beibehalten.

**25.10.2026, Leseweg-Erweiterung:** Acht Lernstationen mit Zielen, Erklärungen, Abschnittslinks und Kontrollfragen; Koide-Rechenbeispiel; englische Begleitfassungen und englischer Einstieg. Deutsch bleibt Hauptfassung. Quellenstand unverändert 64973ef. Quellenpfade und interne Verweise geprüft; Lehrrechnungen separat nachgerechnet. Keine mathematischen Manuskriptänderungen.

**25.10.2026:** Erstbefüllung mit Leseweg, Versions- und Quellenkarte, Forschungsstand, Begriffen und LLM-Hinweisen. Quellenbasis: Hauptrepository-Commit `64973efe8409cfd2ae985fbbd17b4ebc95845780`. Keine Release-Payloads oder mathematischen Quellen geändert; kein neuer Beweisaudit durchgeführt.
