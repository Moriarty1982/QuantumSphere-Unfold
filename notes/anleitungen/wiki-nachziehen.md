# Anleitung: Wiki nachziehen

Werkzeugunabhängig. Gilt für `Moriarty1982/QuantumSphere-Unfold`. Quelle des Wikis ist der Ordner `wiki/` im
GitHub-Repository; `.github/workflows/wiki-sync.yml` spiegelt ihn nach dem Merge auf `main`. **Nie direkt im
Wiki-Repository oder in der Wiki-Oberfläche ändern.** Maßgeblich ist `wiki/Wiki-Pflege.md`; diese Anleitung ist die
Arbeitsliste dazu. Der lokale Monolith-Ordner hat kein `wiki/`; gearbeitet wird im GitHub-Klon.

## 1. Welche Seiten
| Änderung | Seiten |
|---|---|
| neue Runde rNN | `Forschungsstand`, `Forschungslinie`, `Inhalt` + `Content-overview` (EN), Stand-Zeilen in `Home`, `_Footer`, `Versionen-und-Quellen` |
| neuer Test HNN | `Vorhersagen-und-Tests` (Abschnitt offen / abgeschlossen / Erkundungen), ggf. `Offene-Probleme` |
| OP1–OP5, C5, C6/T2 berührt | `Offene-Probleme` (ehrlicher Status, nichts als geschlossen darstellen) |
| These T1–T15 verschoben, Autorentscheidung | `Gesamtbild` (Thesen, Mindmap, Entwicklung), `Hinweise-fuer-LLMs` |
| neuer Begriff | `Begriffe` |
| Leseweg/Struktur | `Dokumentfuehrer` + `Document-guide` (EN), `Leseweg` |
| Arbeitsabläufe für Modelle | `Hinweise-fuer-LLMs` |
| neue Seite | `_Sidebar.md` |

Vor dem Schreiben: `git diff origin/main --stat` und die Runde/Ergebnis-Notizen lesen; was die Quelle sagt, nicht was die
Zusammenfassung sagt.

## 2. Wie schreiben
- **Inhalt wiedergeben, nicht verlinken:** was die Quelle sagt, unter welchen Voraussetzungen, wie weit es trägt, was
  offen ist; wichtigste Formeln und Zahlen. Links auf TeX/Labels stehen dahinter zum Nachprüfen.
- Widerlegte Tests, Korrekturen und zurückgezogene Aussagen ausdrücklich kennzeichnen; ältere Aussagen nicht still ändern,
  sondern als korrigiert markieren.
- Formeln: `$…$` inline, `$$` auf eigenen Zeilen. In Tabellen Ausdrücke mit `|` oder `_` als Backtick-Mathe
  (`` $`...`$ ``). Keine Formelbilder.
- Technische Hinweise in eingerückte **Anmerkungen für LLMs und Quellenprüfung** (EN: **Note for LLMs and source checking**).
- Deutsch zuerst, dann die englische Begleitseite inhaltsgleich (Fundstellen, Voraussetzungen, Status).
- Keine dauerhaften PDF-Seitenzahlen; Labels und Abschnittstitel verwenden. Für reproduzierbare Angaben vollen Commit verlinken.
- Stand-Zeilen (`**Stand: <Datum>**`, „Stand nach rNN“) auf allen berührten Seiten nachziehen.

## 3. Prüfen
- Links: `grep -oE '\]\(https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/[^)]+' wiki/*.md | sed 's/.*wiki\///' | sort -u`
  gegen `ls wiki` abgleichen.
- Version/DOI: die in `AGENTS.md` genannte aktuelle Baseline mit Version-DOI und Concept-DOI 10.5281/zenodo.19210728 –
  Forschungslayer sind keine Releases.
- Kurzer Eintrag oben im **Änderungsnachweis** von `Wiki-Pflege.md` (Datum, Layer, Seiten, was).

## 4. Abgeben
- Im selben Branch/PR wie die Repo-Änderung committen; reine Wiki-Nachzüge als eigener Branch `docs/wiki-…`.
- Merge nur nach ausdrücklicher Freigabe („PR NN mergen“). Nach dem Merge prüfen: `gh run list -w wiki-sync.yml -L 1`;
  nach Veröffentlichung Formeln auf GitHub stichprobenartig ansehen.
