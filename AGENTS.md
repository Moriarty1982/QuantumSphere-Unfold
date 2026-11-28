# AGENTS.md

Gemeinsame Arbeitsanleitung für alle KI-Assistenten in diesem Repository (Codex, Claude, ChatGPT und andere). Sie gilt
unabhängig vom Werkzeug. `CLAUDE.md` verweist nur hierauf. Regeln werden **hier** geändert.

## Was dieses Repository ist
Quellen, Notizen und Werkzeuge zum *Quantum Sphaera Companion*, dem mathematischen Unfold der Paper-Reihe „Quantum
Sphaera“. Die öffentliche Baseline ist **v5.5.0** vom 2026-11-26
(Version-DOI 10.5281/zenodo.24563811, Concept-DOI 10.5281/zenodo.19210728;
Vorgänger v5.4.0, 10.5281/zenodo.24500009; davor v5.3.0, 10.5281/zenodo.24434403, und v5.2.0, 10.5281/zenodo.24294648).
**Reserviert, unveröffentlicht (28.11.2026):** v5.6.0 mit den Runden v4.10.0-r69 bis r75, Zenodo-Entwurf 24632437, Version-DOI
10.5281/zenodo.24632437 (löst erst nach der Veröffentlichung auf); deutscher Preprint 0.5.0, Entwurf 24632440, Version-DOI 10.5281/zenodo.24632440. Upload und
Veröffentlichung nur mit Freigabe des Autors; bis dahin bleibt v5.5.0 die öffentliche Baseline.
v5.5.0 bringt die Runden v4.10.0-r60 bis r68 (1572/38 Seiten); Paketquellstand e69452a4073426f71c4337617a5ed902347eec4b,
Tag v5.5.0 (legt der Autor an). Am selben Tag veröffentlicht: Physik-Artikel 1.1.0 (10.5281/zenodo.24563808; Concept-DOI des Records
10.5281/zenodo.24539643) und deutscher Preprint 0.4.0 (10.5281/zenodo.24563916).
v5.4.0 bringt die Runden v4.10.0-r31 bis r59 (überwiegend Erkundungen) und im Physik-Paper den durchgerechneten OP5-Fall,
Ergänzungen im Grenzen-Teil (r52–r58) und die Händigkeitsserie (r59) (1537/36 Seiten); Paketquellstand
122eb34315a7870106a3e7a8d8fcbf74c438449d, Tag v5.4.0.
v5.3.0 brachte die Runden v4.10.0-r29 und r30 und im Physik-Paper die Abschnitte 5.9 (Orientierung des Oktantschritts) und
7.7 (eine Zahl, mehrere Übersetzungen) (1465/31 Seiten); Paketquellstand 53e9393a9502a9773300d8876bada7950999f138, Tag v5.3.0.
v5.2.0 bringt die Runden v4.10.0-r15 bis r28 und im Physik-Paper den Abschnitt 5.8 zur Herkunft der fehlenden Zahl
(1457/30 Seiten); Paketquellstand 8fb6e9378f6e6789697c60d3ba8b748cc2b56de6, Tag v5.2.0.
v5.1.0 brachte die Runden v4.10.0-r12 bis r14, das Gegenterm-Register und einen Abschnitt zum gebogenen Oktanten im
Physik-Paper (1412/29 Seiten); Paketquellstand dfdb41387264e728a13a9a51a8636fd532011ff2, Tag v5.1.0.

Eigenständiger Physik-Artikel „One Object, Three Frames“ 1.1.0 vom 2026-11-26 als eigener Record: Version-DOI 10.5281/zenodo.24563808
(Vorgänger 1.0.0 vom 2026-11-25, 10.5281/zenodo.24539644)
(Quelle `paper/physics-standalone/`, Ablauf `notes/anleitungen/paper-release.md`).

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
  - `paper-release.md`: eigenständige Papers (QAM-Paper, Physik-Paper) als eigene Zenodo-Records.
- **Modellunabhängig arbeiten:** Ohne Shell oder GitHub-Zugang nennt das Modell die Befehle, und der Autor führt sie aus.
- **Vorab-Notizen:** Jeder Test mit Entscheidungskriterium wird vor der Rechnung festgeschrieben und committet.
  Erkundungen ohne Vorab-Notiz heißen „Erkundung“.
- **Append-only:** Bestehende Runden werden nie umgeschrieben. Korrekturen kommen in eine neue Runde.
- **Merges** auf `main`: PRs ohne Rückfrage mergen, sobald die CI grün ist, und danach kurz melden (Dauerauftrag des Autors vom
  26./27.11.2026). Ist keine CI gelaufen oder ist sie rot, nur mit ausdrücklicher Freigabe.
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
- **Zenodo-Vorschau prüfen** (Auftrag des Autors vom 24.11.2026): Nach jedem Hochladen auf Zenodo, auch nach dem Veröffentlichen,
  die Vorschau kontrollieren und bei Bedarf korrigieren (`zenodo-fix-preview.yml`; Einzelheiten in `notes/anleitungen/zenodo-release.md`).
- **Zenodo-Vorbereitung:** Vor jeder neuen Veröffentlichung die
  [Anleitung zur Vorbereitung der Aussagen-Datenbank und des LLM-Kontexts](notes/anleitungen/zenodo-datenbank-vorbereiten.md) anwenden.
- **Issues nachziehen** (Dauerauftrag des Autors vom 15.11.2026): Nach jeder inhaltlichen Änderung (Runde, Erkundung mit
  OP-Bezug, Merge, Release) das OP-Register #17 und die berührten OP-Issues ohne Rückfrage aktualisieren, im selben Schritt
  wie das Wiki. Fehlt einem offenen Problem ein Issue, eines anlegen und in #17 verlinken. Ehrlicher Status: kein OP als
  geschlossen darstellen.
- **Artikel vor jeder Übergabe nachziehen** (Dauerauftrag des Autors vom 22.11.2026): Vor jeder Übergabe alle Artikel auf den
  Forschungsstand bringen, soweit seit dem letzten Abgleich neue Befunde dazugekommen sind: das Physik-Paper
  (`qam/editions/v5_physics_article.tex` mit `v5_expanded_*.tex`), die Wiki-Seiten Gesamtbild und Forschungsstand sowie den deutschen
  Preprint (`paper/preprint-de/`, Zenodo-Concept-DOI 10.5281/zenodo.24405552). Inhaltliche Änderungen über Zweig und PR; eine neue
  Zenodo-Version des Preprints nur mit Freigabe. In der Übergabe vermerken, welcher Artikel auf welchem Stand ist.
- **Hauptpaper bleibt Quelle** (Dauerauftrag des Autors vom 22.11.2026): Wird in einem Artikel (Physik-Paper, deutscher Preprint)
  ein Nachweis, eine Herleitung oder ein neuer Befund ergänzt, kommt er im selben Arbeitsgang als Runde in den Companion
  (`sources/research/parts/v4100-post-release-layers.tex`), mit Beweis und Prüfung. Die Artikel verweisen auf diese Runde und geben
  sie verkürzt wieder; der Companion ist die maßgebliche Fassung.
- **Wiki:** Jede inhaltliche Änderung zieht `wiki/` im selben PR mit. Das Wiki gibt den Inhalt wieder, nicht nur Links.
- **Keine festen absoluten Pfade** in Skripten. Datenordner als Argument übergeben oder relativ zum Repo auflösen.
- **Sparsam arbeiten:** [Anleitung für LLM-Kontext und Cache](notes/anleitungen/llm-cache-optimieren.md) anwenden.
- **Artikel mitziehen und DOIs verlinken** (Dauerauftrag des Autors vom 28.11.2026): Bei jeder neuen Companion-Version den deutschen Preprint
  (`paper/preprint-de/`) und das englische Physik-Paper „One Object, Three Frames“ (`paper/physics-standalone/`) mit einer neuen Fassung nachziehen.
  Die DOIs verlinken sich gegenseitig: in den Zenodo-Metadaten Companion `isSupplementedBy` Preprint und Paper, Preprint und Paper je `isSupplementTo`
  Companion und `references` das jeweils andere; im Text nennt jeder Artikel den Companion und den anderen Artikel mit DOI.
- **Physik-Ausgabe im Companion-Paket** (Entscheidung des Autors vom 28.11.2026): v5.6.0 erscheint noch mit beiden Ausgaben (Companion und
  Physik-Ausgabe „Graded carriers and physical readouts“). Ab v5.7.0 wird die Physik-Ausgabe nicht mehr mitgebaut; das englische Physik-Paper ist dann
  allein „One Object, Three Frames“ (`paper/physics-standalone/`, eigener Record). Build, Tests und Anleitungen dafür vor v5.7.0 umstellen.
- **Vorhersagen je Version** (Dauerauftrag des Autors vom 28.11.2026): Jede öffentliche Version (Companion, Physik-Paper, deutscher Preprint)
  enthält einen datierten Abschnitt mit dem Modellstand und seinen Vorhersagen (Datum, DOI; ältere Versionen bleiben sichtbar). Für jede Vorhersage
  offen kennzeichnen, was hergeleitet, was gesetzt (Postulat, Setzung), was gemessene Eingabe und was nachträglich gefunden ist. Korrekturen nur in
  einer neuen Version mit Begründung (Modellfortschritt oder Fehler), nie Nachjustieren nach einer neuen Messung. Als Test zählt die Version, die vor
  der Messung festgeschrieben war. Maßgeblich ist das Register im Companion (zuerst Runde v4.10.0-r75 für v5.6.0).
- **Bilanz der Setzungen:** Nach zwei Runden in Folge mit „trägt teilweise“ zur selben offenen Voraussetzung vor der nächsten Runde
  eine Bilanz ziehen: je Runde, was gesetzt, was hergeleitet und wohin die offene Wahl gewandert ist. Dabei prüfen, ob das Ziel selbst eine
  gesetzte Eingabe ist und ob die Frage nur in einer gewählten Zerlegung entsteht; eine stillschweigend gewählte Weggabelung dem Autor vorlegen
  (Anlass: r45).
- **Ehrlicher Status:** offene Probleme (OP1–OP5, C5, C6/T2) nicht als geschlossen darstellen. Die Guards stehen im
  jeweiligen Ledger der Runde.
- **Gesamtbild zuerst:** vor inhaltlicher Arbeit `wiki/Gesamtbild.md` lesen (Mindmap, Thesen T1–T15, Dokumentkarte) und jede Einzelfrage dort einordnen.
- **Vorwissen-Pflicht:** vor jeder neuen Hypothese das Repo nach Vorbefunden durchsuchen: `notes/research/predictions/`, die Notizen und Skripte unter `notes/research/v4_10_0_*/`, `analysis/OP5_*`. Die Fundstellen kommen in einen Abschnitt „Vorwissen geprüft“ der Vorab-Notiz. Für OP5 gilt der Abschnitt „Bereits beantwortet“ in `notes/anleitungen/op5-vergleichsmodell-rechnen.md`.
- **Suchrichtung prüfen:** Bei Wiederaufnahme, vor einem größeren Rechenlauf und nach zwei Varianten mit derselben offenen Voraussetzung prüfen, ob eine Rückwärtssuche günstiger ist. Ziel und notwendige Bedingungen festhalten, daraus Kandidaten erzeugen oder ausschließen und vorhandene QAM-Regeln, Prämissen und Belege abgleichen. Erst danach weitere Kandidaten simulieren. Fehlt einer Modellroute eine native Operation, diese Lücke direkt untersuchen und Modelloptimierung nur bei einer konkreten offenen Modellfrage fortsetzen.
- **Nicht blind = offen sagen:** Steht das Ergebnis vor der Rechnung analytisch fest, wird es als Erkundung oder ausdrücklich „nicht blind“ geführt, nicht als blinder Test. Nachträglich Gefundenes wird als nachträglich markiert.
- **Zurückgestellte Ideen:** `notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md` führt Ideen des Autors mit Auslösern (I1–I6). Beim Start und immer, wenn ein Ansatz scheitert, die Auslöser prüfen; trifft einer zu, die Idee dem Autor als möglichen Ausweg vorschlagen.
- **Stand der letzten Sitzung:** Im lokalen Ordner des Autors ist `llm/Uebergabe.md` der Einstiegspunkt (Stand, offene PRs, zuletzt vergebene H-Nummer, nächster Schritt). Auf GitHub: jüngste Runde unter `notes/research/`, offene PRs, Actions-Läufe.
- **Parallel rechnen:** große Rangrechnungen über `.github/workflows/op5-parallel.yml`, ein Job je Parameter (Einzelheiten in der OP5-Anleitung).
- **Frames:** Konvention F (M, T, P) einhalten; Größen verschiedener Frames erst nach einer erklärten Abbildung vergleichen. Tachyon-Abbildung (z ↦ iz) und Zeitumkehr (z ↦ z̄) nicht verwechseln (r51, r81).
- **Namen der Frames und Sektoren** (Entscheidung des Autors vom 26.11.2026, Runde v4.10.0-r69): In neuen Texten heißen die Frames
  R **Ruheframe** (rest frame; bisher Referenz-/Bezugsframe), M **Materie-Frame**, T **Dual-Frame** (dual frame; bisher Tachyon-Frame) und
  P **Lichtpunkt** (light point; bisher Photon-Eigenframe). Die zwei Lepton-Sektoren heißen **Re-Sektor** (neutrale Leptonen, c = 0) und
  **Im-Sektor** (geladene Leptonen, c = 1), nur für Leptonen und als Lesart unter H99; Quarks behalten Up- und Down-Sektor. Beim ersten
  Auftreten den alten Namen in Klammern dazuschreiben. Bestehende Runden und veröffentlichte Fassungen nicht umbenennen. „Bosonisch/fermionisch“
  und „Licht-Frame“ nicht als Namen für Frames oder Sektoren verwenden.

## Arbeitsweise des Autors (gilt für jedes Modell, auch lokal mit ChatGPT/Codex)
- **Sprache:** Mit dem Autor auf Deutsch kommunizieren.
- **Nummern:** Nächste freie H- und k-Nummer vor der Vergabe gegen `origin/main` prüfen (`git grep -n "H2[0-9][0-9]"`, Ordnernamen unter
  `notes/research/`); parallele Sitzungen vergeben ebenfalls Nummern. Stand 27.11.2026: nächste freie H212, k425.
- **Rechnung und Gegenprobe:** Hauptrechnung in Python (Skript `kNNN_*.py`, Ausgabe `kNNN_out.txt`), unabhängige Gegenprobe in
  Wolfram Language (`kNNNb_gegenprobe.wl`, Ausgabe `kNNNb_out.txt`); Nachträge als `kNNNc_*`. Wolfram-Fallstrick: `N` vor `Sort`.
- **Hergeleitet vs. angepasst:** In jeder Ergebnis-Notiz offen trennen, was hergeleitet, was gesetzt/angepasst und was nachträglich
  gefunden ist. Urteile: trägt / trägt teilweise / widerlegt.
- **Wenn eine Vermutung nicht trägt:** zuerst die Eingaben einzeln mit Stichproben durchgehen, dann variieren (stochastische Suche);
  für jeden Sektor einzeln die nötige Konfiguration suchen und vergleichen, was gesetzt sein muss (HS-Stufe beachten).
- **Vor „von Daten disfavorisiert“:** prüfen, ob die Vorhersage in den Materie-Frame übertragen ist (für Mischung Maske mit
  ε = artanh β_sym, H45).
- **Offene Vorzeichen** sollen aus der finalen Feldgleichung folgen, nicht gesetzt werden.
- **Laufend pushen:** Änderungen während der Arbeit regelmäßig committen und pushen, nicht erst am Ende; Zwischenergebnisse laufender
  Rechnungen sofort melden.
- **Zenodo:** Nur `deposition_id` verwenden, nie `new_version_of`; jeder Zenodo-Schritt und jede neue öffentliche Version nur mit
  Freigabe des Autors; nach jedem Upload/Publish die Vorschau prüfen.
- **Wiki:** Absätze in `wiki/Offene-Probleme.md` sind mehrzeilig; nie „nach der ersten Zeile“ einfügen, sondern nach dem ganzen Absatz.
- **Ordner für neue Runden:** `notes/research/v4_10_0_rNN/` gehört zur alten v4.9.0-Serie. Neue v4.10.0-Runden bekommen einen eigenen
  Ordner `notes/research/v4_10_0_rNN_<thema>/`; der Text kommt nach `sources/research/parts/v4100-post-release-layers.tex`.
- **Modellwahl:** Offene, schwere Herleitungen und lange Argumentketten mit dem stärksten verfügbaren Modell; klar umrissene Tests,
  Rechnungen und PRs mit einem starken Standardmodell; Routine (Branches, Wiki, Formatierung) mit einem kleineren Modell. Bei einer
  neuen Aufgabe von sich aus ein passendes Modell vorschlagen.
- **Keine privaten Daten** (E-Mail-Adressen, Zugangsdaten) in Dateien, Commits oder Anfragen an externe Dienste.

## Lokale Arbeitskopie des Autors
Die Monolith-Fassung und die vollständige Rundentabelle liegen im lokalen Ordner des Autors. Dessen `AGENTS.md` ist die
ausführliche Fassung dieser Datei. Der aktuelle Forschungsstand für Leser steht im Wiki unter „Forschungsstand“ und
„Hinweise für LLMs“.
