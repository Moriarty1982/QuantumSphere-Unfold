# Anleitung: Werkzeug qs.py und Abläufe am Monolithen

Werkzeugunabhängig. Projektfakten (Dateien, DOIs, Guard-Listen, Audit-Baseline) stehen in `AGENTS.md`
im Projektwurzelverzeichnis. Diese Anleitung beschreibt die Abläufe und das Werkzeug. Jedes Modell mit Shell ruft
`qs.py` direkt auf; ohne Shell nennt es den Befehl, und der Autor führt ihn aus.

## Werkzeug

`.claude/skills/quantum-sphaera/tools/qs.py` (Python 3, keine Abhängigkeiten; der Ordner heißt nur aus historischen Gründen so). Alle Kommandos lesen nur.

```bash
python .claude/skills/quantum-sphaera/tools/qs.py <kommando> [...]
```

| Kommando | Zweck |
|---|---|
| `outline <tex> [--rounds] [--depth 1] [--grep X]` | Gliederung, Rundenliste, Zeilennummern |
| `xref <tex> [--number 3.2 \| --label thm:FE \| --section 13]` | LaTeX-Nummerierung auflösen |
| `citations <tex> --source KEY=<quelle.tex>` | `\cite`-Verweise mit Nummer gegen die Quelle prüfen |
| `guards <tex> [--start N --end M]` | Kandidaten für unbewachte verbotene Claims |
| `ledger <tex>` | Guard-/Residual-Vektoren über alle Runden |
| `audit <log> [--compare REF.log]` | Compile-Log gegen Baseline oder Referenzbuild |
| `doi <pdf>` | DOI-Vorkommen und Compact-Titlepage-Regel im PDF (braucht `pypdf`) |
| `manifest <dir> [--only ...]` | SHA256-Manifest im CSV-Format der Release-Dateien |

`xref` bildet geteilte Theoremzähler nach (`\newtheorem{lemma}[theorem]{Lemma}`),
den Reset durch `[section]` und den Unterschied zwischen `\section` und `\section*`.
Genau daran scheitert Handzählen. Es meldet `\appendix`, `\numberwithin` und
`\setcounter` als Unsicherheitsstellen.

## Ablauf: Querverweis prüfen oder neu setzen

Nie eine Theoremnummer aus dem Gedächtnis oder durch Zählen im Kopf setzen.

```bash
python .claude/skills/quantum-sphaera/tools/qs.py xref "riemann_arxiv_v4__15_ (1).tex" --number 3.2
```

Für den Rundumschlag über alle Verweise des Companion:

```bash
python .claude/skills/quantum-sphaera/tools/qs.py citations Quantum_Sphaera_Companion_v4_7_0_source.tex --source "brendecke2026rh=riemann_arxiv_v4__15_ (1).tex" --source "brendecke2026main=quantum_sphaera_v3_1_4_monolith_stable_main (1).tex"
```

`citations` prüft, ob die Nummer existiert und der Typ stimmt, und stellt den
**Titel des Ziels** neben den **Zitatkontext**. Die Bewertung bleibt beim Leser:
eine existierende Nummer kann trotzdem das falsche Objekt sein. Genau so wurde
gefunden, dass zwei Stellen Stone–von Neumann auf „Theorem 3.2" stützen, während
Theorem 3.2 der RH-Arbeit die Funktionalgleichung ist.

Die `PRUEF`-Markierung ist ein Stichwortabgleich zwischen Zieltitel und Kontext.
Sie erzeugt False Positives, wenn das Stichwort im Kontext nur als Formel
vorkommt (`Adj_J(L₀)` gegen den Titel „Adjunction vanishes"). Immer nachlesen.

`T1+T3`, `T4+T5`, `T6` sind symbolische Namen, keine Nummern — nicht prüfbar,
werden nur gezählt.

## Ablauf: neue Runde anhängen

1. Letzten Stand feststellen: `outline <companion> --rounds | tail -5`
2. `.claude/skills/quantum-sphaera/assets/round_template.tex` als Gerüst nehmen, Platzhalter ersetzen
3. Unmittelbar vor `\end{document}` einfügen (append-only, nie ältere Runden umschreiben)
4. `guards` über den neuen Zeilenbereich laufen lassen
5. `ledger` prüfen: hat sich ein Vektor geändert? Wenn ja — war das beabsichtigt?

Zwingend in jeder Runde: Source-only-Klausel, `\label` auf Abschnitt und jeden
Unterabschnitt, Guard-Bilanz am Ende. Ab r82 wird durchgängig `\section*` plus
`\addcontentsline` verwendet — diese Form beibehalten.

**Ein Guard fällt nur mit ausdrücklicher Zustimmung des Autors.** `Γ_guard` steht
seit r60 auf `(1,1,1,1,1)`, `R_glob` auf `(0,1,1,1,1)`. Eine Runde, die daran
etwas ändert, ist ein Ereignis und keine Routine.

## Ablauf: Release-Kandidat

Ein RC entsteht aus r84 oder später, nie aus einem älteren Handoff.
Namensmuster nach RC19/RC20: `..._RC<N>_<zweck>_source.tex`,
`V4_7_0_RC<N>_<ZWECK>_AUDIT_REPORT.md`, `v4_7_0_RC<N>_<zweck>_summary.json`,
`V4_7_0_RC<N>_SHA256_MANIFEST.csv`, `V4_7_0_RC<N>_ZENODO_METADATA_DRAFT.txt`.

1. Neuen Snapshot der Arbeitsdatei unter RC-Namen anlegen; `doi <pdf>` prüft die
   Compact-Titlepage-Regel (genau eine Version- und eine Concept-DOI-Zeile auf Seite 1)
2. Artefakte des vorigen RC unangetastet lassen und ihre Hashes gegenprüfen
3. Drei pdfLaTeX-Durchläufe, dann `audit <build>.log` gegen die Baseline

   Außerhalb des Projektverzeichnisses bauen (einem temporären Ordner), damit `.aux`/`.log`/`.toc`
   nicht im Release-Ordner landen. Das RC19-PDF **nie überschreiben** — es ist im
   Manifest gehasht. Neues PDF unter neuem Namen ablegen.

   `pages` und `overfull` ändern sich bei jeder Textänderung; das ist normal.
   `undefined_refs`, `undefined_cites`, `duplicate_labels` und `rerun` müssen 0 bleiben.
4. `manifest .` erzeugt die CSV neu — Hashes müssen zu den ausgelieferten Dateien passen
5. Zenodo-Metadaten und Audit-Report auf die neuen Zahlen bringen

MiKTeX liegt unter `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64` und ist **nicht
im PATH** — beim Aufruf voranstellen. Näheres in `AGENTS.md`.

## Fallstricke

**Backslashes verschwinden in Bash-Argumenten.** `grep -F "\section{" datei.tex`
findet null Treffer, obwohl der String tausendfach vorkommt. Für alles mit
LaTeX-Befehlen: `qs.py`, ein Such- oder Editierwerkzeug des Modells ohne Shell-Quoting oder ein
Python-Skript als Datei verwenden — nicht Bash mit `grep`/`sed`/Heredoc. `sed -n 'A,Bp'` für reine Zeilenbereiche ist unkritisch.

**Nie die ganze Datei lesen.** Der Companion hat über 71.000 Zeilen. Über `outline`
den Bereich bestimmen, dann gezielt `sed -n`.

**Versionsnummern sind keine Mathematik.** Revisionskennungen, DOI-Fragmente und
Release-Labels dürfen nie als Objektnamen, Indizes, Exponenten oder Beweisdaten
auftreten — das ist eine ausdrückliche Regel des Dokuments.

**Historische Schichten nicht als aktuellen Stand lesen.** Der Companion enthält
Versionsstände von `legacy.15.0` bis v4.7 nebeneinander. Was gilt, sagt die
jeweils jüngste Runde, nicht der nächstgelegene Textblock.
