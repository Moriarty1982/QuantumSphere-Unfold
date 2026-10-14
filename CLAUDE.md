# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Werkzeug zuerst

Für Querverweise, Rundenanlage, Guard-Prüfung, Ledger und Manifest gibt es den
Skill `quantum-sphaera` mit dem CLI `.claude/skills/quantum-sphaera/tools/qs.py`.
Theoremnummern **nie** von Hand zählen — `qs.py xref` bildet die LaTeX-Zähler nach.

## Was dieses Verzeichnis ist

Kein Software-Repository im üblichen Sinn, sondern ein einzelnes LaTeX-Monolith-Dokument: der *Quantum Sphaera Companion*, ein mathematisches Preprint von Marc Brendecke (über 1000 PDF-Seiten, über 64.000 Quellzeilen, 3,4 MB `.tex`). Keine Build-Skripte, keine Tests im üblichen Sinn. Die Qualitätssicherung läuft über LaTeX-Compile-Audits und Claim-Scope-Disziplin.

## Versionskontrolle

Git-Repository, Branch `main`, 74 Commits von v0.6.0 bis heute. Ein Commit pro Dokumentstand.

```
v0.6.0     1.238 Zeilen   Beginn der archivierten Historie
v1.0.0     1.378
v2.9.0     6.933
v3.0.0    20.034
v4.0.0    35.108          ab hier zweigeteilt: Kern + historischer Teil
v4.4      49.615          zu einem Monolithen zusammengeführt
v4.6.0    53.160
RC19      63.202  r84     Datei trägt ab hier ihren Release-Namen
RC20              r85     Zitatreparatur, Scope-Trennung
RC21              r86     C5-Kollar-Konsolidierung (Q5)
RC22              r88     Fensterkalibrierung (Q3), Non-Collar-Routen
                          — r87 darin fehlerhaft, siehe r89
                  r89     Korrektur von r87
RC23/RC24         r90/r91 Δ_γ-Rekonstruktion, Q4 ausgeführt
v4.8.0    65.000+ r94     + v4.8.0-r01 (Planck-Readout), r02 (Release)
```

Bis v4.6.0 heißt die Datei `companion.tex` (bei zweigeteilten Ständen zusätzlich `companion_historical.tex`), ab RC19 `Quantum_Sphaera_Companion_v4_7_0_source.tex`, ab v4.8.0 `Quantum_Sphaera_Companion_v4_8_0_source.tex`. Git erkennt die Übergänge als Rename, `git log --follow` läuft durch.

**Die Daten vor v4.0.0 sind Archivierungs-, keine Entstehungsdaten** — die Quelldateien stammen aus einem Download-Ordner, in dem ganze Versionsblöcke denselben Zeitstempel tragen. Die *Reihenfolge* stimmt (aus den Versionsnummern), die Tage nicht. Ab v4.0.0 kommen die Daten aus den Release-Archiven und sind belastbar.

Aufgenommen sind die 58 Hauptversionen `x.y.0` aus v0–v3 plus alle v4-Stände. Die Mikroversionen (etwa v2.26.1 bis v2.26.44) und die Arbeitsstände liegen weiterhin in `C:\Users\marcb\Downloads\Quantum Sphere`. Zwei Versionen (v3.17.0, v3.29.0) fehlen: dort existiert nur eine Wrapper-Datei ohne Volltext.

**`.gitattributes` mit `* -text` ist nicht verhandelbar.** Die SHA256-Werte in den Manifesten gelten für die Bytes der Dateien. Jede Zeilenenden-Konvertierung beim Checkout würde jeden dieser Hashes brechen und die Provenienzkette entwerten. Verifiziert: ein Checkout von Tag `RC19` reproduziert `019e7a35…` exakt.

**PDFs sind ignoriert** — sie sind aus dem Quelltext reproduzierbar und machen über 75 % des Ordners aus; ihre Prüfsummen stehen in den Manifesten. Einzige Ausnahme ist `Quantum_Sphaera_Companion_v4_7_0.pdf` (RC19): es stammt aus einer anderen Toolchain (45 statt 58 Overfull) und lässt sich nicht bitgenau nachbauen.

**Künftige RCs brauchen keine Snapshot-Datei mehr.** Ein Tag leistet dasselbe. Die vorhandenen `..._RC19..._RC22_*_source.tex` bleiben, weil die Manifeste sie hashen — neue nicht mehr anlegen.

Das Repository liegt in einem OneDrive-Ordner. Bisher unauffällig; falls je Sync-Konflikte im `.git`-Verzeichnis auftreten, ist ein Umzug außerhalb der Cloud die Abhilfe.

## Dateien

| Datei | Rolle |
|---|---|
| `Quantum_Sphaera_Companion_v4_8_0_source.tex` | **Die Arbeitsdatei.** Hier wird editiert. |
| `Quantum_Sphaera_Companion_v4_8_0.pdf` + `V4_8_0_*` + `v4_8_0_release_summary.json` | **Release v4.8.0**, Zenodo-Entwurf 23365244 |
| `Quantum_Sphaera_Companion_v4_7_0_RC19_concept_doi_restore_source.tex` | **Eingefrorener RC19-Snapshot** — nicht editieren |
| `Quantum_Sphaera_Companion_v4_7_0.pdf` | RC19-PDF — eingefroren, nie überschreiben |
| `..._RC20_citation_repair_source.tex` + `..._r85.pdf` + `V4_7_0_RC20_*` | RC20 (Stand r85), eingefroren |
| `..._RC21_c5_collar_consolidation_source.tex` + `..._r86.pdf` + `V4_7_0_RC21_*` | RC21 (Stand r86), eingefroren |
| `..._RC22_clock_window_collar_routes_source.tex` + `..._r88.pdf` + `V4_7_0_RC22_*` | RC22 (Stand r88), eingefroren |
| `quantum_sphaera_v3_1_4_monolith_stable_main (1).tex` | Hauptpapier, Bibkey `brendecke2026main` |
| `riemann_arxiv_v4__15_ (1).tex` | Riemann-Arbeit v4.15, Bibkey `brendecke2026rh` |
| `V4_7_0_RC19_CONCEPT_DOI_RESTORE_AUDIT_REPORT.md` | Compile-Audit der letzten Runde |
| `v4_7_0_RC19_concept_doi_restore_summary.json` | Dieselben Audit-Zahlen maschinenlesbar |
| `V4_7_0_RC19_SHA256_MANIFEST.csv` | Hashes aller Release-Dateien |
| `V4_7_0_RC19_ZENODO_METADATA_DRAFT.txt` | Zenodo-Upload-Metadaten |

Die vier RC19-Begleitdateien gehören zusammen: wer den Quelltext ändert und neu kompiliert, muss alle vier aktualisieren, sonst driften Hashes und Audit-Zahlen auseinander.

Nicht in diesem Verzeichnis, aber referenziert: `RC14_uncompressed_reference_source.tex` im RC16-Quellpaket enthält den ungekürzten r55–r80-Solve-Log. Er wird gebraucht, sobald an C5 oder C4 inhaltlich gearbeitet wird.

## Dokumentaufbau

`article`-Klasse, keine `\input`/`\include` — alles in einer Datei.

| Zeilen | Inhalt |
|---|---|
| 1 – ~52.111 | Mathematischer Hauptkorpus: QAM-über-ZF, MML/MMA, Heisenberg-Compensator, Millennium Matrix, OP-Architektur |
| 52.112 – 62.648 | Solve-Log, Runden r03 – r54, je ein `\section` pro Runde |
| 62.649 – 62.705 | r55 – r80, auf ein Invariantentheoremlet komprimiert |
| 62.706 – Ende | r81 – r84: Frame-Skalen-Typisierung und Release-Scope |

## Der Runden-Workflow

Das Dokument wächst **append-only in nummerierten Runden** (`rNN`). Eine neue Runde ist ein neuer Abschnitt unmittelbar vor `\end{document}`; bestehende Runden werden nicht umgeschrieben. Aktueller Stand: **r94** und **v4.8.0-r02**. Runden der v4.8.0-Linie heißen `v4.8.0-rNN`, Labels `sec:v480-rNN-...`; `qs.py outline` und `ledger` erkennen beide Formen.

Eine Runde folgt einem festen Muster:

1. `\section{v4.7.0-rNN <Titel>}` bzw. `\section*{...}` plus `\addcontentsline{toc}{section}{...}` — beide Varianten kommen vor; ab r82 wird durchgängig `\section*` mit `addcontentsline` verwendet
2. `\label{sec:rNN-<kebab-case-titel>}`, jede Unterüberschrift bekommt ebenfalls ein `\label{subsec:rNN-...}`
3. Source-only-Klausel: kein PDF, keine neue DOI, kein Public Release, sofern nicht ausdrücklich anders beauftragt
4. Inhalt als Theoremlet mit `\paragraph{Theoremlet rNN.}` und `\paragraph{Proof sketch.}`, abgeschlossen mit `\(\square\)`
5. Guard-Update am Ende: die Residual- und Guard-Vektoren der Runde

## Guard-Disziplin — die wichtigste Regel

Das Dokument arbeitet mit einem expliziten System erlaubter und verbotener Aussagen. **Neuer Text darf niemals eine der verbotenen Aussagen behaupten**, auch nicht implizit oder in abgeschwächter Formulierung.

Erlaubt (effektiv/lokal/frame-typisiert):

```
0_M^ε ⇒ 0_termdata                          Matter-Frame-Epsilon-Terminalität
ℓ_T² = −λ_T², λ_T > 0                       Tachyon-Frame-Vorzeichenskala
OP5_eff                                      effektive OP5-Schließung
C5_det/eff bei θ = 1/256 nach n = 20         Detektor-Schwellen-Terminalität
W_clk^loc unter Δ_γ < 1/5                    lokale Photon-Clock-Selektor-Erhaltung
C_mix^typed lokal                            typisierte Mixed-Comparison-Kontrolle
```

Verboten (exakt/global):

```
C5 = 0                    exakte endliche C5-Null-Schließung
0_termdata ⇒ 0_all        exakte All-Readout-Terminalität
C6 / T2                   T2-Schließung
W_γ^glob                  globales Photon-Clock-/RH-Theorem
W_all                     globale All-Readout-Schließung
```

Die sichere Release-Formulierung lautet: *guarded effective/local and frame-typed closures, not exact global closure.*

### Ledger-Notation

Jede Runde bilanziert am Ende:

- `Γ_guard = (1,1,1,1,1)` — alle fünf Guards stehen. Eine `1` heißt: der Guard ist **nicht ausgegeben**. Ein Guard darf nur mit ausdrücklicher Zustimmung des Nutzers fallen.
- `R_glob = (0,1,1,1,1)` — globales Residuum. Seit r60 unverändert; die erste Komponente fiel damals durch die konservative C4-Relative-Seam-Behandlung.
- `R_eff/local = (0,0,0,0,0)` gegen `R_exact/global = (1,1,1,1,1)`
- `β₄ = 1/256` ist der ungespendete C4-Guard.

Wenn eine neue Runde diese Vektoren nicht verändert, ist das der Normalfall und muss so deklariert werden. Wenn sie einen Wert verändert, ist das ein Ereignis, das explizit begründet gehört.

## DOI-Disziplin

Vier DOIs, die nie vermischt werden dürfen:

- **Version-DOI** `10.5281/zenodo.23365244` — v4.8.0, gehört als einzige sichtbare DOI-Zeile auf die Titelseite
- **Vorgänger-DOI** `10.5281/zenodo.20232911` — v4.7.0, seit v4.8.0 nur Provenienz
- **Concept-DOI** `10.5281/zenodo.19210728` — stabil über alle Versionen
- **Previous/Baseline-DOI** `10.5281/zenodo.20117361` — nur Provenienz, nie als aktuelle DOI

Abgelaufen und nicht mehr zu verwenden: `10.5281/zenodo.20181842`.

Die **Compact-Titlepage-Regel**: auf der Titelseite steht genau eine Version-DOI-Zeile und eine Concept-DOI-Zeile. Release-Hinweise, Provenienz der Vorgänger-DOI und Claim-Scope-Erklärungen gehören in den Fließtext, nicht auf die Titelseite.

## Kompilieren

**MiKTeX 25.12** ist als User-Installation eingerichtet:

```
%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64
```

Es liegt **nicht im PATH** — den Pfad im Aufruf voranstellen oder für die Sitzung setzen. Automatisches Paketnachladen ist aktiviert (`[MPM]AutoInstall=1`), fehlende Pakete werden also ohne Dialog geholt. Alle Pakete der Präambel sind verfügbar, einschließlich `slashed`, `centernot` und `datetime2`.

Gebaut wird mit **drei pdfLaTeX-Durchläufen**, außerhalb des Projektverzeichnisses:

```bash
pdflatex -interaction=nonstopmode Quantum_Sphaera_Companion_v4_8_0_source.tex
```

Danach `qs.py audit <log>` gegen die Baseline. Das RC19-PDF im Projektordner nie überschreiben — es ist im Manifest gehasht.

Die Präambel setzt `\pdfcompresslevel=0` und `\pdfobjcompresslevel=0` — daher die 14 MB PDF-Größe. Das ist Absicht (Diffbarkeit), nicht zu „optimieren".

PDF-Lesezeichen sind seit dem Stand nach v4.8.0 wieder an (`bookmarks=true,bookmarksnumbered=true`); der r25/r27-Notbehelf `bookmarks=false` ist entfernt. Getestet mit drei pdfLaTeX-Läufen unter TeX Live 2022: 968 Lesezeichen, Seiten, Labels und harte Audit-Werte unverändert. `\pdfstringdefDisableCommands` in der Präambel hält Symbole wie `\to` und `\Lambda` im Lesezeichentext lesbar; die übrigen „Token not allowed in PDF string“-Warnungen (37) sind harmlos. Das veröffentlichte v4.8.0-PDF ist noch ohne Lesezeichen gebaut. Unter MiKTeX ist der Test noch nicht gelaufen.

### Audit-Baseline (RC19)

Nach jedem Rebuild gegen diese Werte prüfen:

| Prüfung | Sollwert |
|---|---:|
| PDF-Seiten | 1014 |
| Undefinierte Referenzen / Zitate | 0 / 0 |
| Duplikat-Label-Warnungen | 0 |
| Rerun-Warnungen | 0 |
| Rohe `??`-Marker in Quelle / PDF | 0 / 0 |
| Labels gesamt | 3290 |
| Overfull-hbox-Warnungen | 45 (siehe unten) |
| Sichtbare Version-DOI-Zeilen auf Titelseite | 1 |
| Sichtbare Concept-DOI-Zeilen auf Titelseite | 1 |
| Treffer der abgelaufenen DOI im PDF | 0 |

**Die Overfull-Zahl ist toolchain-abhängig und taugt nicht als fester Sollwert.** Der ursprüngliche RC19-Build meldete 45; derselbe Quelltext liefert unter MiKTeX 25.12 reproduzierbar **58** — bei identischer Seitenzahl (1014) und Labelzahl (3290). Für eine belastbare Aussage den Vergleichsstand mitbauen und `qs.py audit <neu.log> --compare <ref.log>` verwenden. Nur `undefined_refs`, `undefined_cites`, `duplicate_labels` und `rerun` sind harte Nullwerte.

Unter derselben Toolchain: RC19 1014 Seiten / 3290 Labels, RC20 1016 / 3296, RC21 1019 / 3305, RC22 1025 / 3322. Overfull durchgehend 58, alle harten Werte 0.

## Fallstricke

**Backslashes in Bash-Argumenten werden verschluckt.** `grep -F "\section{" datei.tex` liefert hier 0 Treffer, obwohl der String tausendfach vorkommt — und `grep -oE '\\(a|b)'` matcht die literale Klammer statt der Gruppe. Für alles, was LaTeX-Befehle sucht oder schreibt, das **Grep-Tool** und **Write/Edit** verwenden, nicht Bash mit `grep`/`sed`/Heredoc. `sed -n 'A,Bp'` für Zeilenbereiche ist unproblematisch, weil dort keine Backslashes im Muster stehen.

**Nie die ganze Datei lesen.** Über 64.000 Zeilen. Mit `sed -n` gezielt Bereiche holen oder das Grep-Tool mit `-C` verwenden.

**Nie behaupten, ein Datum fehle, ohne die Nachbarrunden zu prüfen.** Die Solve-Kette tabelliert in einer Runde und verbraucht in einer anderen. r87 behauptete, die V9-Chart-Parameter seien nicht dokumentiert — sie stehen in r14, eine Runde vor der gelesenen, und der zugehörige Lift in r17, zwei Runden danach. Die Korrektur ist als r89 protokolliert. Eine Aussage über Fehlen betrifft den ganzen Monolithen und braucht einen Grep über die gesamte Datei plus die angrenzenden Runden.

**Keine externen Grafiken.** `\safegraphic` ist in der Präambel definiert, wird aber nirgends aufgerufen — es fehlen keine Asset-Dateien, und ein Platzhalterrahmen im PDF wäre ein Fehler, kein Normalzustand.

**Der RC19-Snapshot ist eingefroren.** `_RC19_concept_doi_restore_source.tex` dokumentiert den Zustand, der als RC19 kompiliert und im Manifest gehasht wurde. Er wird nicht nachträglich verändert — sonst geht die Provenienz verloren. Alle Änderungen laufen in `_source.tex` und gehören zum nächsten RC. Seit der ersten Post-RC19-Änderung sind die beiden Dateien deshalb **nicht mehr byte-identisch**, und der Manifest-Eintrag für `_source.tex` ist überholt; beides ist gewollt. Ein neuer RC bekommt einen neuen Snapshot unter neuem Namen und ein neu erzeugtes Manifest.

## Offene Zweige

Aus der r48-Branch-Queue: Q₁ (r49–r54), Q₂ (r55–r80), Q₅ (r86) abgearbeitet, Q₃ in r87 kalibriert. Offen:

- **Q₄** C4-Mixed-Kernel-Lokalisierung — gesperrt, würde `β₄ = 1/256` ausgeben
- **Q₃ Restteil**: Die Schranke `Δ_γ < 1/5` hat im vorliegenden Quelltext **keine Herleitung**. Sie stammt aus r65, das im komprimierten r55–r80-Block steckt; der Volltext liegt in `RC14_uncompressed_reference_source.tex` (nicht hier). r87 zeigt, dass sie aus der r15/r16-Fensterschicht nicht rekonstruierbar ist.

Eine konkrete, guard-neutrale Datenlücke: **der unkomprimierte r65-Text** für `Δ_γ < 1/5`. Er liegt nicht im Projektordner und auch nicht in `C:\Users\marcb\Downloads\Quantum Sphere` — jener Ordner enthält 841 `.tex` der Versionen v0.1 bis v3.35, aber kein v4-Material und keinen einzigen Treffer für `Delta_\gamma`.

Zum C5-Stand nach r86/r88: Die Frage „gibt es einen endlichen Abschluss?" zerfällt in (a) *innerhalb* der multiplikativen Kollar-Rekursion — beweisbar nein, allein wegen `q > 0` — und (b) *außerhalb* davon. r88 schließt von den drei Kandidatenformen für (b) zwei: der subtraktive Kanal trifft die Null nur bei maßnull-abgestimmtem `c` und verlässt danach den zulässigen Bereich, braucht also eine Stoppregel — und die ist die von `LG₅^bd` verbotene Abschneidung. Offen bleibt nur Form (iii): ein Zeuge außerhalb der Kollar-Iteration, der die Obstruktion selbst erreicht statt den Score.
