# AGENTS.md

Gemeinsame Arbeitsanleitung für alle KI-Assistenten in diesem Repository (Codex, Claude, ChatGPT und andere). Sie gilt
unabhängig vom Werkzeug. `CLAUDE.md` verweist nur hierauf. Regeln werden **hier** geändert.

## Was dieses Repository ist
Quellen, Notizen und Werkzeuge zum *Quantum Sphaera Companion*, dem mathematischen Unfold der Paper-Reihe „Quantum
Sphaera“. Die öffentliche Baseline ist **v4.11.0** vom 2026-11-10 (Version-DOI 10.5281/zenodo.24108818, Concept-DOI
10.5281/zenodo.19210728; Vorgänger v4.10.0, 10.5281/zenodo.23991357). Alles danach liegt als Forschungsschicht vor und ist kein Release.

Die aktuelle Entwicklungslinie ist **v5.0.0-draft** (seit 2026-11-11):
datenbankgestütztes Aussageninventar und ausgewählte LaTeX-Exporte. Sie hat
für v5.0.0 die reservierte, unveröffentlichte Version-DOI
10.5281/zenodo.24152615 (Entwurf 24152615); öffentliche Baseline und
Zitation bleiben bis zur Veröffentlichung v4.11.0.
Details: `notes/research/v5_0_0_development.md`.

- `sources/research/`: der modulare Kandidat (`v480-companion.tex` mit Teilen unter `parts/`). Die Runden v4.9.0-r01–r86 stehen in
  `parts/v490-post-release-layers.tex` (so in v4.10.0 veröffentlicht); neue Runden heißen `v4.10.0-rNN` und kommen in eine neue Schichtdatei
  (z. B. `parts/v4100-post-release-layers.tex`).
- `notes/research/v4_10_0_rNN/`: Notizen, Skripte und Rundentext je Runde. Vorab-Notizen liegen in
  `notes/research/predictions/`.
- `analysis/`: Arbeitsstände, u. a. das OP5-Vergleichsmodell unter `analysis/op5-field-slices/`.
- `wiki/`: Quelle des GitHub-Wikis. Sie wird beim Push auf `main` automatisch gespiegelt.
- `notes/anleitungen/`: Schritt-für-Schritt-Abläufe.

## Für alle Modelle verbindlich
- **QAM-Belege abrufen:** Bei Fragen zu gespeicherten MMA-Belegen, QAM-Aussagen oder Prämissenspuren im Projekt
  zuerst den schreibgeschützten MCP-Server `qsc-qam` verwenden, falls verfügbar. Belege per Hash prüfen und
  offene Guards in der Antwort angeben. Falls MCP nicht verfügbar ist, die lokalen Lesebefehle aus
  `mcp/README.md` verwenden, soweit verfügbar. Neue MML-Rechnungen laufen über den dafür vorgesehenen MMA-Ablauf.
  Stapelberichte ohne bekannten Hash über `list_qam_batch_reports` suchen und anschließend per Hash abrufen.
- **QAM-Belegprüfung parallelisieren:** Bei einem Auftrag zur Prüfung mehrerer unabhängiger MMA-Belege oder
  Prämissenzweige in Codex je Prüfgruppe einen `qam_evidence_reviewer` parallel einsetzen. Gemeinsame
  Prämissen nur einmal prüfen, Abhängigkeiten in ihrer Reihenfolge auswerten und die Befunde nach Beleg-
  und Prämissenhash zusammenführen. Einzelne Abrufe direkt erledigen.
- **MML-Stapel ausführen:** Für ausdrücklich beauftragte gespeicherte Paarstapel in Codex `qsc-qam-batch`
  verwenden, falls verfügbar. Den Sammelbericht in Eingabereihenfolge auswerten und blockierte Anfragen mit
  ihrem Vorgänger benennen. Bei fehlendem Stapelserver den lokalen `mma-batch`-Aufruf aus `qam/README.md` nutzen.
  Für ausdrücklich beauftragte Paarstapel aus dem Chat `run_qam_pair_batch` auf demselben Server nutzen.
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
