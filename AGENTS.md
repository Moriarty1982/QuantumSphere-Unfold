# AGENTS.md

Gemeinsame Arbeitsanleitung für alle KI-Assistenten in diesem Repository (Codex, Claude, ChatGPT und andere). Sie gilt
unabhängig vom Werkzeug. `CLAUDE.md` verweist nur hierauf. Regeln werden **hier** geändert.

## Was dieses Repository ist
Quellen, Notizen und Werkzeuge zum *Quantum Sphaera Companion*, dem mathematischen Unfold der Paper-Reihe „Quantum
Sphaera“. Die öffentliche Baseline ist **v4.9.0** (Version-DOI 10.5281/zenodo.23534954, Concept-DOI
10.5281/zenodo.19210728). Alles danach liegt als Forschungsschicht vor und ist kein Release.

- `sources/research/`: der modulare Kandidat (`v480-companion.tex` mit Teilen unter `parts/`). Neue Runden werden an
  `parts/v490-post-release-layers.tex` angehängt.
- `notes/research/v4_10_0_rNN/`: Notizen, Skripte und Rundentext je Runde. Vorab-Notizen liegen in
  `notes/research/predictions/`.
- `analysis/`: Arbeitsstände, u. a. das OP5-Vergleichsmodell unter `analysis/op5-field-slices/`.
- `wiki/`: Quelle des GitHub-Wikis. Sie wird beim Push auf `main` automatisch gespiegelt.
- `notes/anleitungen/`: Schritt-für-Schritt-Abläufe.

## Für alle Modelle verbindlich
- **Abläufe:** `notes/anleitungen/qsc-runde-einbauen.md` (neue Runde) und
  `notes/anleitungen/op5-vergleichsmodell-rechnen.md` (OP5-Vergleichsmodell).
- **Vorab-Notizen:** Jeder Test mit Entscheidungskriterium wird vor der Rechnung festgeschrieben und committet.
  Erkundungen ohne Vorab-Notiz heißen „Erkundung“.
- **Append-only:** Bestehende Runden werden nie umgeschrieben. Korrekturen kommen in eine neue Runde.
- **Merges** auf `main` nur nach ausdrücklicher Freigabe des Autors.
- **Wiki:** Jede inhaltliche Änderung zieht `wiki/` im selben PR mit. Das Wiki gibt den Inhalt wieder, nicht nur Links.
- **Keine festen absoluten Pfade** in Skripten. Datenordner als Argument übergeben oder relativ zum Repo auflösen.
- **Sparsam arbeiten:** Skripte als Dateien ablegen und nur kurze Zusammenfassungen ausgeben.
- **Ehrlicher Status:** offene Probleme (OP1–OP5, C5, C6/T2) nicht als geschlossen darstellen. Die Guards stehen im
  jeweiligen Ledger der Runde.

## Lokale Arbeitskopie des Autors
Die Monolith-Fassung und die vollständige Rundentabelle liegen im lokalen Ordner des Autors. Dessen `AGENTS.md` ist die
ausführliche Fassung dieser Datei. Der aktuelle Forschungsstand für Leser steht im Wiki unter „Forschungsstand“ und
„Hinweise für LLMs“.
