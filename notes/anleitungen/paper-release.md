# Anleitung: Eigenständige Papers veröffentlichen

Gilt für die beiden eigenständigen englischen Artikel, die je einen **eigenen Zenodo-Record** bekommen (Entscheidung des
Autors vom 25.11.2026), nicht für den Companion und nicht für den deutschen Preprint (dafür `zenodo-release.md`):

| Paper | Quelle | Konfiguration | Metadaten | Tag |
|---|---|---|---|---|
| QAM-Paper „What a Conclusion Rests On“ | `paper/qam-standalone/` | `release/papers/qam-standalone.json` | `release/zenodo/metadata_qam_standalone_1_0_0.json` | `qam-paper-v1.0.0` |
| Physik-Paper „One Object, Three Frames“ | `paper/physics-standalone/` | `release/papers/physics-standalone.json` | `release/zenodo/metadata_physics_standalone_1_0_0.json` | `physics-paper-v1.0.0` |

Werkzeuge: `tools/paper_release.py` (Build, Prüfung, Stempel, Zenodo-Aufrufe, Vorschau, Release-Notiz) und der Workflow
`.github/workflows/paper-release.yml` („Paper release (standalone papers)“). Für Zenodo ruft beides die bewährten Skripte
`tools/zenodo_publish.py` und `tools/zenodo_fix_preview.py` auf; alle Argumente kommen aus der Konfigurationsdatei, damit
keine veralteten Workflow-Voreinstellungen in einen Lauf geraten.

## Freigaben — nie ohne ausdrückliches Wort des Autors

| Schritt | Wirkung |
|---|---|
| `stage=build`, jeder Lauf ohne `execute` | nichts nach außen (Trockenlauf) |
| `stage=reserve`, `execute=true` | legt einen **unveröffentlichten** Entwurf an (verwerfbar), vergibt die Version-DOI |
| `stage=upload`, `execute=true` | lädt die Dateien in den Entwurf |
| `stage=publish`, `execute=true`, `confirm_publish=true` | **endgültig**, DOI wird öffentlich |
| Merge des Release-PRs, Tag, GitHub-Release | ändert das öffentliche Repository |

Vorher gilt [zenodo-datenbank-vorbereiten.md](zenodo-datenbank-vorbereiten.md) (AGENTS.md, Zenodo-Vorbereitung).

## Voraussetzung im Artikel: die Titelzeile

Die Titelseite muss Version und Version-DOI aus `release-info.tex` zeigen. Das Werkzeug schreibt die Datei beim Stempeln;
ohne sie zeigt der Artikel die Entwurfszeile. Einmal im Artikel einbauen (im PR des Papers):

- Physik-Paper, `article.tex`: vor `\begin{document}`
  `\InputIfFileExists{release-info}{}{\def\releaseline{Draft\enspace$\cdot$\enspace November 2026}}`
  und in der Autorzeile `{\small Draft \enspace$\cdot$\enspace November 2026}` durch `{\small\releaseline}` ersetzen.
- QAM-Paper, `main.tex`: `\date{Draft, \today}` ersetzen durch
  `\InputIfFileExists{release-info}{}{\def\releaseline{Draft, \today}}` und `\date{\releaseline}`.

Der Release-Build (`--final`) bricht ab, wenn die Titelseite die DOI nicht zeigt oder noch „Draft“ sagt.

## Ablauf

Alles auf einem Release-Zweig, z. B. `release/qam-paper-v1.0.0`, nachdem der Artikel-PR gemergt ist. Der Workflow liest
Konfiguration und Payload vom Zweig, auf dem er läuft.

### 1. Probe-Build und Prüfung (frei)

```bash
python tools/paper_release.py build --paper qam-standalone     # setzt in build/paper-release/<id>/tree, Repo bleibt unberührt
python tools/paper_release.py check --paper qam-standalone     # Metadaten ↔ Konfiguration, Scope-Absatz, verbotene Formulierungen
```

oder auf GitHub:

```bash
gh workflow run "Paper release (standalone papers)" --repo Moriarty1982/QuantumSphere-Unfold --ref <zweig> \
  -f paper=qam-standalone -f stage=build -f execute=false -f confirm_publish=false -f environment=production -f final=false
```

Der Build prüft: undefinierte Verweise und Zitate, doppelte Labels und Rerun-Hinweise (harte Nullwerte), zählt
Overfull/Underfull, Seitenzahl, Titel auf Seite 1. Beim QAM-Paper laufen zusätzlich `build.sh` (Hashes der eigenen Akte
mit `qamhash.py`) und im Workflow der Lean-Prüfer `qamcheck` auf `main.qam`. Die Prüfung der Metadaten verlangt einen
Absatz „Scope“, den Bezug auf die Companion-Concept-DOI und das Repository und lehnt Formulierungen ab, die ein OP
(OP1–OP5, C5, C6/T2) als gelöst oder die Riemann-Hypothese als bewiesen darstellen.

### 2. Reservierung (Freigabe)

```bash
gh workflow run "Paper release (standalone papers)" --repo Moriarty1982/QuantumSphere-Unfold --ref <zweig> \
  -f paper=qam-standalone -f stage=reserve -f execute=true -f confirm_publish=false -f environment=production -f final=false
```

Erst mit `execute=false` (Trockenlauf). Erste Fassung: `new_version_of` bleibt leer, es entsteht ein neuer Record mit
eigener Concept-DOI. In der Zusammenfassung des Laufs stehen `deposition_id` und die reservierte Version-DOI.

### 3. Stempeln, Release-Build, Payload committen (frei, im Zweig)

```bash
python tools/paper_release.py stamp --paper qam-standalone --deposition-id <id>
git add release/papers/qam-standalone.json release/zenodo/metadata_qam_standalone_1_0_0.json paper/qam-standalone/release-info.tex
git commit -m "QAM-Paper 1.0.0: reservierte DOI eingetragen"
python tools/paper_release.py build --paper qam-standalone --final
git add release/qam-standalone-v1.0.0 && git commit -m "QAM-Paper 1.0.0: Payload" && git push
```

`stamp` schreibt `deposition_id`, Version-DOI und Datum in die Konfiguration, die DOI in `notes` der Metadaten und
`release-info.tex` in den Artikelordner. `build --final` verlangt saubere Quellen und legt unter `payload_dir` ab: PDF,
Quellarchiv (`git archive` des letzten Commits, der die Quellen berührt; beim QAM-Paper mit `qam.sty` und
`qam-physics.sty`), beim QAM-Paper die geprüfte Akte `.qam`, `SHA256SUMS.txt` und `BUILD_INFO.json` (Quellcommit,
Seiten, TeX-Version). PDF und Archiv sind reproduzierbar (Datum aus dem Quellcommit): ein zweiter Build mit derselben
TeX-Version ergibt dieselben Bytes. Hochgeladen wird genau, was `SHA256SUMS.txt` nennt, plus diese Datei.

Wer den Payload aus der GitHub-Toolchain will, startet den Build mit `final=true` und committet das Artefakt
`<paper>-payload/final`.

### 4. Upload (Freigabe)

Derselbe Aufruf mit `-f stage=upload -f execute=true`. Vorher prüft das Werkzeug Metadaten, SHA256 und die DOI auf der
Titelseite des Payload-PDFs und bricht vor jedem API-Aufruf ab, wenn etwas nicht stimmt. Es lädt mit `replace_files`
(der Entwurf enthält danach genau den Payload), setzt das Haupt-PDF als Vorschau und liest sie zurück; eine falsche
Vorschau lässt den Lauf scheitern. Dann den Entwurf auf Zenodo ansehen lassen.

### 5. Veröffentlichen (Freigabe, endgültig)

`-f stage=publish -f execute=true -f confirm_publish=true`. Der Lauf lädt die Dateien erneut hoch, setzt die Vorschau,
veröffentlicht und **prüft danach die Vorschau des veröffentlichten Records** mit `zenodo_fix_preview.py`; ist sie falsch,
korrigiert er sie per Metadaten-Edit (Dauerauftrag des Autors vom 24.11.2026). Das Ergebnis steht in der Zusammenfassung
des Laufs und kommt in die Release-Notiz. Getrennt prüfen oder nachkorrigieren: `-f stage=preview` (`execute=false`
meldet, `execute=true` setzt).

### 6. Danach

```bash
python tools/paper_release.py notes --paper qam-standalone   # schreibt RELEASE_NOTES.md und gibt die Tag-Befehle aus
```

Release-PR mergen (Freigabe). Tag und GitHub-Release: die Cloud-Umgebung kann keine Tags pushen. Entweder der Workflow
„GitHub Release anlegen“ (Befehl gibt `notes` aus; Ziel ist der Quellcommit aus `BUILD_INFO.json`) oder lokal beim Autor
`git tag -a … && git push origin <tag>`. Danach: Concept-DOI aus dem Record in Konfiguration (`new_version_of` für die
nächste Fassung = diese Record-ID), README des Papers, Wiki (Versionen und Quellen), `AGENTS.md` (DOI-Liste),
Übergabe und Register #17 nachziehen.

### Spätere Fassungen

Neue Version desselben Records: `version`, `pdf_name`, `source_archive`, `payload_dir`, `tag` und Metadatendatei hochzählen,
`new_version_of` auf die Record-ID der Vorfassung, `deposition_id` und `version_doi` leeren. In den Metadaten
`isVersionOf` (Concept-DOI) und `isNewVersionOf` (Vorfassung) ergänzen; `check` verlangt das.
