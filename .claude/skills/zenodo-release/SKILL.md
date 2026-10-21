---
name: zenodo-release
description: Zenodo-Release einer neuen Version des Quantum Sphaera Companion über das GitHub-Repository Moriarty1982/QuantumSphere-Unfold — Version-DOI reservieren, Metadaten anlegen, Titelseite nach der Compact-Titlepage-Regel setzen, Release-Payload bauen, hochladen und veröffentlichen. Diesen Skill laden, sobald eine Version-DOI reserviert, eine neue Version (z. B. v4.9.0) auf Zenodo vorbereitet, der Workflow „Zenodo Release" oder tools/zenodo_publish.py benutzt, release/zenodo/metadata_*.json angelegt oder eine Titelseite mit neuer DOI versehen werden soll. Auch bei den Stichworten Zenodo, DOI reservieren, new version, Deposition, Release-Payload, CITATION.cff.
---

# Zenodo-Release

Projektfakten (DOIs, Guard-Listen, Verhältnis lokal ↔ GitHub) stehen in `CLAUDE.md`. Dieser Skill beschreibt den
Ablauf auf GitHub. Werkzeuge dort: Workflow `.github/workflows/zenodo_release.yml`, Hilfsskript
`tools/zenodo_publish.py`, Metadaten unter `release/zenodo/`.

## Freigaben — nie ohne ausdrückliches Wort des Nutzers

| Schritt | Wirkung nach außen |
|---|---|
| Reservierung (`dry_run=false`) | legt einen **unveröffentlichten** Entwurf im Zenodo-Konto an (verwerfbar) |
| Upload (`reserve_only=false`, `dry_run=false`) | lädt Dateien in den Entwurf |
| Veröffentlichen (`publish=true` **und** `confirm_publish=true`) | **endgültig**, DOI wird öffentlich |
| Merge eines Release-PRs, Push auf `main`, Tag | ändert das öffentliche Repository |

Trockenläufe (`dry_run=true`) und alles im lokalen Klon brauchen keine Freigabe.

## Ablauf

### 0. Klon und Ausgangslage

```bash
git clone --branch main https://github.com/Moriarty1982/QuantumSphere-Unfold.git <scratchpad>/qsu
cd <scratchpad>/qsu && git config core.autocrlf false && git checkout -- .
```

Die globale Git-Einstellung des Nutzers ist `core.autocrlf=true`; ohne die zweite Zeile erscheinen Hunderte Dateien als
geändert (CRLF im Arbeitsbaum, LF im Repository). Neue Dateien mit **LF** schreiben. Das lokale Monolith-Repository hat
keinen gemeinsamen Vorfahren mit GitHub — dort nicht arbeiten.

Vorher prüfen, dass die Vorgängerversion auf Zenodo **veröffentlicht** ist (`https://zenodo.org/records/<id>`); von einem
unveröffentlichten Entwurf lässt sich keine neue Version abzweigen.

### 1. Metadaten

`release/zenodo/metadata_vX_Y_Z.json` nach dem Muster der Vorversion anlegen:

- `version`: `"vX.Y.Z"`; `related_identifiers`: `isVersionOf` Concept-DOI `10.5281/zenodo.19210728`,
  `isNewVersionOf` die Version-DOI der Vorgängerversion, `isSupplementTo` das GitHub-Repository.
- Beschreibung nur aus dem belegten Inhalt (README des Kandidaten, Änderungsübersicht in `analysis/`), mit
  Scope-Guard-Absatz; keine verbotene Aussage (Guard-Liste in `CLAUDE.md`).
- `publication_date` vorläufig; vor dem Veröffentlichen auf das tatsächliche Datum setzen.

Prüfen:

```bash
python tools/zenodo_publish.py --metadata release/zenodo/metadata_vX_Y_Z.json --files "release/vX.Y.Z/*" \
  --environment production --new-version-of <vorgaenger-id> --reserve-only --dry-run
python <lokal>/llm/training/guard_linter.py release/zenodo/metadata_vX_Y_Z.json
```

Auf einen Zweig `release/vX.Y.Z-prep` committen und pushen; der Workflow liest die Metadaten vom Zweig, auf dem er läuft.

### 2. Reservierung

**Die Voreinstellungen des Workflows zeigen auf eine alte Version** (`metadata_v4_8_0.json`, `release/v4.8.0/*`) und
`dry_run` steht auf `true`. Immer alle Eingaben ausdrücklich setzen. Auch `reserve_only` **schreibt die Metadaten** in den
Entwurf — mit falschen Metadaten bekäme der neue Entwurf die Beschreibung der Vorversion.

Erst Trockenlauf, dann (nach Freigabe) dasselbe mit `dry_run=false`:

```bash
gh workflow run "Zenodo Release" --repo Moriarty1982/QuantumSphere-Unfold --ref release/vX.Y.Z-prep \
  -f environment=production -f new_version_of=<vorgaenger-id> -f reserve_only=true \
  -f replace_files=false -f publish=false -f confirm_publish=false -f dry_run=true \
  -f metadata=release/zenodo/metadata_vX_Y_Z.json -f files_glob='release/vX.Y.Z/*'
```

Im Protokoll stehen `deposition_id` und `reserved_doi` (die DOI-Nummer ist die Deposition-ID). Beides sofort festhalten:
in der Beschreibung der Metadaten (`Version DOI: …`), in `CLAUDE.md` (DOI-Disziplin, als reserviert/unveröffentlicht).
Der Entwurf **erbt die Dateien der Vorversion**; beim Upload deshalb `replace_files=true`.

Ab hier nicht mehr `new_version_of` verwenden — das legte einen zweiten Entwurf an —, sondern `deposition_id=<id>`.

### 3. Titelseite

Im v4.9-Kandidaten kommt die Titelseite aus `sources/research/parts/working-preamble.tex` (`\title`, `\author`,
`\date`, `\workingversion`, `\hypersetup`), **nicht** aus dem eingefrorenen Fragment `parts/v470/01_opening.tex`, das nur
`\maketitle` aufruft. Fragmente unter `parts/v470/` nie editieren.

Compact-Titlepage-Regel: genau eine Version-DOI-Zeile, genau eine Concept-DOI-Zeile; Vorgänger-DOIs und
Provenienz in den Fließtext. `\workingversion` von `X.Y.Z-draft` auf `X.Y.Z`; PDF-Metadaten (`pdftitle`, `pdfsubject`)
anpassen.

Prüfen mit dem erweiterten DOI-Kommando (ohne Parameter gilt v4.8.0 als aktuelle Version):

```bash
python .claude/skills/quantum-sphaera/tools/qs.py doi <pdf> --version-doi 10.5281/zenodo.<id> --version-label vX.Y.Z
```

Ziel: keine Beanstandung. Werden weitere DOIs Vorgänger, `DOI_ROLES` in `qs.py` nachziehen.

### 4. Build

- GitHub: Push auf `main` baut seit PR #20 auch `sources/research/` und lässt den Lauf scheitern, wenn der Kandidat nicht
  sauber baut (`qsc_research_gate.py`). Auf einem Zweig von Hand:
  `gh workflow run "QSC LaTeX PDF Build" --repo Moriarty1982/QuantumSphere-Unfold --ref <zweig>`.
- Lokal unter MiKTeX gegen den Vorstand: `qs.py audit <neu.log> --compare <ref.log>`. Harte Nullwerte: undefinierte
  Verweise/Zitate, doppelte Labels, Rerun. Overfull ist toolchain-abhängig (TeX Live 45, MiKTeX 58).

### 5. Payload und Repository

Unter `release/vX.Y.Z/`: PDF, Quelltext, `VX_Y_Z_SHA256_MANIFEST.csv` (`qs.py manifest`). Beim modularen Kandidaten
vorher entscheiden (Nutzer), ob der Quelltext als zusammengeführte Einzeldatei oder als Archiv der Teile beiliegt.
Dazu `CITATION.cff`, `.zenodo.json` und die Beschreibung aktualisieren. Alles als PR; Merge erst auf Freigabe.

### 6. Upload und Veröffentlichung

Erst `dry_run=true`, dann nach Freigabe:

```bash
-f deposition_id=<id> -f reserve_only=false -f replace_files=true -f publish=false -f confirm_publish=false \
-f dry_run=false -f metadata=release/zenodo/metadata_vX_Y_Z.json -f files_glob='release/vX.Y.Z/*'
```

Den Entwurf auf Zenodo vom Nutzer prüfen lassen. Veröffentlichen nur auf ausdrückliches Wort, mit `publish=true` und
`confirm_publish=true`.

### 7. Danach

Tag `vX.Y.Z` auf GitHub, in `CLAUDE.md` die DOI-Disziplin umstellen (neue Version-DOI aktuell, bisherige als
Vorgänger, nur Provenienz), `DOI_ROLES` in `qs.py` aktualisieren.

## Fallstricke

- `git show "github/main:.github/…"` unter Git-Bash mit `MSYS_NO_PATHCONV=1`, sonst wird der Pfad umgeschrieben.
- Backslashes in Heredocs der Bash werden verschluckt: LaTeX und Regex-Skripte mit dem Write-Tool als Datei anlegen.
- Artefaktnamen dürfen kein `/` enthalten; der LaTeX-Workflow ersetzt es seit PR #20 selbst.
- `build-summary` des LaTeX-Workflows kann Overfull dreifach zählen: `qsc_latex_build.py` nimmt die erste `*.log` im
  Ausgabeordner, manchmal das latexmk-Konsolenprotokoll aller Läufe. Maßgeblich ist `<name>.log`
  (`qs.py audit`). Bei v4.9.0: 135 gemeldet, tatsächlich 45.
- Manifest nie in den Ordner schreiben, den es beschreibt, ohne `--only`: sonst zählt es sich selbst leer mit.
- Die Präambel des v4.9-Kandidaten ist ein eingefrorenes v4.7-Fragment mit `bookmarks=false`; das Release-PDF hat
  deshalb keine Lesezeichen (wie das veröffentlichte v4.8.0-PDF).
- Shell-Prüfungen auf CR mit `$'\r'` sind hier unzuverlässig (das Muster wird leer und passt auf jede Zeile); Bytes mit
  Python prüfen.

## Stand v4.9.0

| Feld | Wert |
|---|---|
| Vorgänger | v4.8.0, veröffentlicht 2026-10-14, Record `23365244` |
| Reservierte Version-DOI | `10.5281/zenodo.23534954`, Entwurf `23534954`, unveröffentlicht, keine Dateien hochgeladen (erbt die v4.8.0-Dateien) |
| Metadaten | `release/zenodo/metadata_v4_9_0.json` auf Zweig `release/v4.9.0-prep` |
| Reservierungslauf | GitHub Actions `39605210856` (Trockenlauf `39605097888`) |
| Titelseite | erledigt auf `release/v4.9.0-prep` (`c8f5d91`): Version-DOI und Concept-DOI je einmal, Vorgänger-DOIs in `working-orientation.tex`; MiKTeX 1124 Seiten / 3590 Labels, GitHub-Build `39607324287` grün; `qs.py doi --version-doi` ohne Beanstandung |
| Payload | erledigt (`36e1c9b`): Einzeldatei aus 54 `\input` zusammengeführt (Skript im Scratchpad: Zeilen, die nur `\input{…}` enthalten, bytegenau ersetzen), SHA256 `787226d2…`; PDF aus dem TeX-Live-Container (Lauf `39608246966`), 1123 Seiten, SHA256 `57d20e0b…`; Text auf allen Seiten identisch mit dem modularen Build; `CITATION.cff` mit vorläufigem `date-released` |
| PR | #21 (Entwurf), erst zum Release mergen |
| Offen | Upload in Entwurf 23534954 (6), Prüfung auf Zenodo, Veröffentlichung, Datum setzen, Merge, Tag |
