# AGENTS.md

Gemeinsame Arbeitsanleitung für alle KI-Assistenten in diesem Repository (Codex, Claude, ChatGPT und andere). Sie gilt
unabhängig vom Werkzeug. `CLAUDE.md` verweist nur hierauf. Regeln werden **hier** geändert.

## Was dieses Repository ist
Quellen, Notizen und Werkzeuge zum *Quantum Sphaera Companion*, dem mathematischen Unfold der Paper-Reihe „Quantum
Sphaera“. Die öffentliche Baseline ist **v5.2.0** vom 2026-11-17
(Version-DOI 10.5281/zenodo.24294648, Concept-DOI 10.5281/zenodo.19210728;
Vorgänger v5.1.0, 10.5281/zenodo.24237112; davor v5.0.0, 10.5281/zenodo.24152615).
v5.2.0 bringt die Runden v4.10.0-r15 bis r28 und im Physik-Paper den Abschnitt 5.8 zur Herkunft der fehlenden Zahl
(1457/30 Seiten); Paketquellstand 8fb6e9378f6e6789697c60d3ba8b748cc2b56de6, Tag v5.2.0.
v5.1.0 brachte die Runden v4.10.0-r12 bis r14, das Gegenterm-Register und einen Abschnitt zum gebogenen Oktanten im
Physik-Paper (1412/29 Seiten); Paketquellstand dfdb41387264e728a13a9a51a8636fd532011ff2, Tag v5.1.0.

Version 5 enthält die datenbankgestützte Dokumentarchitektur und zwei englische
Ausgaben (1402/28 Seiten). Der veröffentlichte Paketquellstand ist
539b75bfce29ce20bb9aa7e59c251727b49faa45, Tag v5.0.0. Nachfolgende Arbeit ist
Forschungsschicht, kein neues Release. Die offene Stringrelaxationsfrage bleibt
offen; Veröffentlichung und technische Paketprüfung schließen keine Guards.
Details: `release/v5.0.0/README.md`, Entwicklungsgeschichte in
`notes/research/v5_0_0_development.md`.

- `sources/research/`: der modulare Kandidat (`v480-companion.tex` mit Teilen unter `parts/`). Die Runden v4.9.0-r01–r86 stehen in
  `parts/v490-post-release-layers.tex` (so in v4.10.0 veröffentlicht); neue Runden heißen `v4.10.0-rNN` und kommen in eine neue Schichtdatei
  (z. B. `parts/v4100-post-release-layers.tex`).
- `notes/research/v4_10_0_rNN/`: Notizen, Skripte und Rundentext je Runde. Vorab-Notizen liegen in
  `notes/research/predictions/`.
- `analysis/`: Arbeitsstände, u. a. das OP5-Vergleichsmodell unter `analysis/op5-field-slices/`.
- `wiki/`: Quelle des GitHub-Wikis. Sie wird beim Push auf `main` automatisch gespiegelt.
- `notes/anleitungen/`: Schritt-für-Schritt-Abläufe.

## Für alle Modelle verbindlich
- **Rechenwerkzeuge wählen:** Bei jeder neuen oder wiederaufgenommenen Rechen- und Beweisaufgabe vor dem Ansatz prüfen, ob Wolfram Language und/oder Qiskit für Herleitung, Rechnung oder unabhängige Kontrolle besser geeignet sind. Das jeweils besser geeignete Werkzeug tatsächlich einsetzen, bei verschiedenen geeigneten Teilaufgaben beide. Wolfram insbesondere für symbolische und exakte Rechnungen, Qiskit für explizit definierte Quantenschaltungen, Zustands- und Messsimulationen. Die Werkzeugwahl, die durchgeführten Prüfungen und die Grenzen des Ergebnisses bei relevanten Befunden festhalten. Die vorgesehenen QAM/MML/MMA-Abläufe gelten weiterhin.
- **Rechenausgaben festhalten:** Bei Skripten für Forschungsbefunde die relevanten tatsächlich erzeugten Ausgaben (insbesondere `Print[...]` in Wolfram Language) zusammen mit dem Skript oder der Ergebnisnotiz im Projekt ablegen. Symbolische Nullreste, Rückgabewerte und Warnungen unterscheiden.
- **Standardsprache für Medien:** Präsentationen, Audio und Videos für dieses Projekt standardmäßig auf Englisch erstellen. Das gilt auch für Folientexte, Sprechskripte und Untertitel. Eine andere Sprache verwenden, wenn der Autor sie für den jeweiligen Auftrag ausdrücklich vorgibt.
- **QAM-Belege abrufen:** Bei Fragen zu gespeicherten MMA-Belegen, QAM-Aussagen oder Prämissenspuren im Projekt
  zuerst den schreibgeschützten MCP-Server `qsc-qam` verwenden, falls verfügbar. Belege per Hash prüfen und
  offene Guards in der Antwort angeben. Falls MCP nicht verfügbar ist, die lokalen Lesebefehle aus
  `mcp/README.md` verwenden, soweit verfügbar. Neue MML-Rechnungen laufen über den dafür vorgesehenen MMA-Ablauf.
  Stapelberichte ohne bekannten Hash über `list_qam_batch_reports` suchen und anschließend per Hash abrufen.
- **Subagenten projektweit einsetzen:** Gibt es mehrere substanzielle unabhängige Teilaufgaben, verteilt der
  Hauptagent sie standardmäßig parallel auf Subagenten, sofern das Werkzeug sie unterstützt. Das gilt im
  gesamten Repository, etwa für getrennte Forschungsfragen, Rechnungen und unabhängige Gegenprüfungen,
  Codeänderungen, Tests und Dokumentation. Jeder Subagent erhält eine konkrete Aufgabe und bei Änderungen
  einen klar abgegrenzten Dateibereich. Der Hauptagent koordiniert gemeinsame Prämissen und Abhängigkeiten,
  prüft die Ergebnisse und führt sie zusammen. Kleine Einzelaufgaben und unmittelbar voneinander abhängige
  Schritte bearbeitet der Hauptagent direkt. Die Vorgaben zur QAM-Belegprüfung gelten zusätzlich.
- **QAM-Belegprüfung parallelisieren:** Bei einem Auftrag zur Prüfung mehrerer unabhängiger MMA-Belege oder
  Prämissenzweige in Codex je Prüfgruppe einen `qam_evidence_reviewer` parallel einsetzen. Gemeinsame
  Prämissen nur einmal prüfen, Abhängigkeiten in ihrer Reihenfolge auswerten und die Befunde nach Beleg-
  und Prämissenhash zusammenführen. Einzelne Abrufe direkt erledigen.
- **MML-Stapel ausführen:** Für ausdrücklich beauftragte gespeicherte Paarstapel in Codex `qsc-qam-batch`
  verwenden, falls verfügbar. Den Sammelbericht in Eingabereihenfolge auswerten und blockierte Anfragen mit
  ihrem Vorgänger benennen. Bei fehlendem Stapelserver den lokalen `mma-batch`-Aufruf aus `qam/README.md` nutzen.
  Für ausdrücklich beauftragte Paarstapel aus dem Chat `run_qam_pair_batch` auf demselben Server nutzen.
- **HDL-Vergleich automatisch einsetzen:** Bei Änderungen an `RUN_TAPE`, der zugehörigen SystemVerilog-Steuerung
  oder Aussagen über deren Übergangsregeln die Vergleichssuite mit MMA ausführen. In Codex
  `run_qam_hdl_check` auf `qsc-qam-batch` verwenden, wenn verfügbar. Sonst den lokalen Aufruf in
  `qam/examples/zuse_machine/hdl/README.md` nutzen. Bei offenen Problemen den Vergleich als unabhängige
  Kontrolle einsetzen, wenn die Schlussfolgerung von einem konkret definierten endlichen Such-, Auswahl-
  oder Guard-Ablauf abhängt. Ist dieser Ablauf in der festen Suite nicht abgedeckt, dafür eigene Testfälle
  formulieren und mit den MMA-Referenzspuren vergleichen. Den geprüften Bereich, gegebenenfalls die
  erste Abweichung und offene Voraussetzungen festhalten. Die Wahl der Rechenwerkzeuge für die fachliche Herleitung
  richtet sich weiterhin nach der jeweiligen Aufgabe.
- **Abläufe:** Schritt-für-Schritt-Anleitungen in `notes/anleitungen/` (Übersicht und Nutzung je Modell in
  `notes/anleitungen/README.md`). Sie sind die einzige Quelle; Claude-Skills im lokalen Ordner verweisen nur darauf.
  - `weitermachen.md`: Sitzungsstart, Stand aus Übergabe und Repo rekonstruieren.
  - `sitzung-uebergeben.md`: am Ende eines Arbeitsblocks die Übergabe neu schreiben.
  - `hypothese-testen.md`: Test HNN von der Vorab-Notiz bis zur Ergebnis-Notiz.
  - `qsc-runde-einbauen.md`: neue Runde schreiben und einbauen.
  - `op5-vergleichsmodell-rechnen.md`: Rechnungen am OP5-Vergleichsmodell.
  - `wiki-nachziehen.md`: Ordner `wiki/` im selben PR nachziehen.
  - `qs-werkzeug.md`: `tools/qs.py` (Querverweise, Guards, Ledger, Audit, Manifest).
  - `zenodo-release.md`: neue Version auf Zenodo.
- **Modellunabhängig arbeiten:** Ohne Shell oder GitHub-Zugang nennt das Modell die Befehle, und der Autor führt sie aus.
- **Vorab-Notizen:** Jeder Test mit Entscheidungskriterium wird vor der Rechnung festgeschrieben und committet.
  Erkundungen ohne Vorab-Notiz heißen „Erkundung“.
- **Append-only:** Bestehende Runden werden nie umgeschrieben. Korrekturen kommen in eine neue Runde.
- **Merges** auf `main` nur nach ausdrücklicher Freigabe des Autors.
- **Gemergte Zweige löschen:** Zweige, die vollständig in `main` enthalten sind und keinen offenen PR haben, nach
  jedem Merge ohne Rückfrage löschen, lokal und auf GitHub (Dauerauftrag des Autors vom 14.11.2026). Prüfen mit
  `git merge-base --is-ancestor <zweig> <remote>/main`. Nicht gemergte Zweige bleiben stehen, auch fremde. Den Zweig
  eines ausgecheckten Worktrees nicht löschen; ungetrackte Dateien in Worktrees vor dem Entfernen sichern.
- **Versionsverwaltung** (Dauerauftrag des Autors vom 15.11.2026):
  - **Interne Nummern ohne Rückfrage vergeben:** H-, k-, Runden- (v4.10.0-rNN) und CT-Nummern. Vorher gegen das Repo
    prüfen, damit keine Nummer doppelt vergeben wird, und die vergebene Nummer in der Übergabe nennen.
  - **Buchführungs-Commits ohne Rückfrage auf `main` pushen:** `llm/Uebergabe.md` sowie Stand-Zeilen und
    Änderungsnachweise ohne neuen Inhalt.
  - **Weiterhin nur mit Freigabe:**
    - inhaltliche Änderungen (nur über Zweig und PR) und Merges;
    - jeder Zenodo-Schritt (Reservierung, Upload, Veröffentlichung);
    - die Entscheidung, dass eine neue öffentliche Version entsteht.
- **Issues nachziehen** (Dauerauftrag des Autors vom 15.11.2026): Nach jeder inhaltlichen Änderung (Runde, Erkundung mit
  OP-Bezug, Merge, Release) das OP-Register #17 und die berührten OP-Issues ohne Rückfrage aktualisieren, im selben Schritt
  wie das Wiki. Fehlt einem offenen Problem ein Issue, eines anlegen und in #17 verlinken. Ehrlicher Status: kein OP als
  geschlossen darstellen.
- **Wiki:** Jede inhaltliche Änderung zieht `wiki/` im selben PR mit. Das Wiki gibt den Inhalt wieder, nicht nur Links.
- **Keine festen absoluten Pfade** in Skripten. Datenordner als Argument übergeben oder relativ zum Repo auflösen.
- **Sparsam arbeiten:** Skripte als Dateien ablegen und nur kurze Zusammenfassungen ausgeben.
- **Ehrlicher Status:** offene Probleme (OP1–OP5, C5, C6/T2) nicht als geschlossen darstellen. Die Guards stehen im
  jeweiligen Ledger der Runde.
- **Gesamtbild zuerst:** vor inhaltlicher Arbeit `wiki/Gesamtbild.md` lesen (Mindmap, Thesen T1–T15, Dokumentkarte) und jede Einzelfrage dort einordnen.
- **Vorwissen-Pflicht:** vor jeder neuen Hypothese das Repo nach Vorbefunden durchsuchen: `notes/research/predictions/`, die Notizen und Skripte unter `notes/research/v4_10_0_*/`, `analysis/OP5_*`. Die Fundstellen kommen in einen Abschnitt „Vorwissen geprüft“ der Vorab-Notiz. Für OP5 gilt der Abschnitt „Bereits beantwortet“ in `notes/anleitungen/op5-vergleichsmodell-rechnen.md`.
- **Suchrichtung prüfen:** Bei Wiederaufnahme, vor einem größeren Rechenlauf und nach zwei Varianten mit derselben offenen Voraussetzung prüfen, ob eine Rückwärtssuche günstiger ist. Ziel und notwendige Bedingungen festhalten, daraus Kandidaten erzeugen oder ausschließen und vorhandene QAM-Regeln, Prämissen und Belege abgleichen. Erst danach weitere Kandidaten simulieren. Fehlt einer Modellroute eine native Operation, diese Lücke direkt untersuchen und Modelloptimierung nur bei einer konkreten offenen Modellfrage fortsetzen.
- **Nicht blind = offen sagen:** Steht das Ergebnis vor der Rechnung analytisch fest, wird es als Erkundung oder ausdrücklich „nicht blind“ geführt, nicht als blinder Test. Nachträglich Gefundenes wird als nachträglich markiert.
- **Zurückgestellte Ideen:** `notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md` führt Ideen des Autors mit Auslösern (I1–I4). Beim Start und immer, wenn ein Ansatz scheitert, die Auslöser prüfen; trifft einer zu, die Idee dem Autor als möglichen Ausweg vorschlagen.
- **Stand der letzten Sitzung:** Im lokalen Ordner des Autors ist `llm/Uebergabe.md` der Einstiegspunkt (Stand, offene PRs, zuletzt vergebene H-Nummer, nächster Schritt). Auf GitHub: jüngste Runde unter `notes/research/`, offene PRs, Actions-Läufe.
- **Parallel rechnen:** große Rangrechnungen über `.github/workflows/op5-parallel.yml`, ein Job je Parameter (Einzelheiten in der OP5-Anleitung).
- **Frames:** Konvention F (M, T, P) einhalten; Größen verschiedener Frames erst nach einer erklärten Abbildung vergleichen. Tachyon-Abbildung (z ↦ iz) und Zeitumkehr (z ↦ z̄) nicht verwechseln (r51, r81).

## Lokale Arbeitskopie des Autors
Die Monolith-Fassung und die vollständige Rundentabelle liegen im lokalen Ordner des Autors. Dessen `AGENTS.md` ist die
ausführliche Fassung dieser Datei. Der aktuelle Forschungsstand für Leser steht im Wiki unter „Forschungsstand“ und
„Hinweise für LLMs“.
