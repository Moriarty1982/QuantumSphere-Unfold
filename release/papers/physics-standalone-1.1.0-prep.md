# Physik-Artikel „One Object, Three Frames“, Fassung 1.1.0: Vorbereitung

**Status (26.11.2026): vorbereitet, nicht reserviert, nicht veröffentlicht.** Kein Zenodo-Aufruf mit Wirkung, kein Stempel, kein Tag.
Vorfassung: 1.0.0, Record 24539644, Version-DOI 10.5281/zenodo.24539644 (unverändert, `release/physics-standalone-v1.0.0/`).
Ablauf: `notes/anleitungen/paper-release.md`, Abschnitt „Spätere Fassungen“.

## Offener Punkt vor dem Upload: Concept-DOI des Records

Die Concept-DOI des Physik-Artikel-Records steht nirgends im Repository (gesucht in Konfiguration, Metadaten und Release-Ordner 1.0.0,
`wiki/Versionen-und-Quellen.md`, `AGENTS.md`). Sie wurde **nicht geraten**. In `release/zenodo/metadata_physics_standalone_1_1_0.json` fehlt
deshalb die Beziehung `isVersionOf`; `isNewVersionOf` 10.5281/zenodo.24539644 ist eingetragen. `check` meldet das Fehlen nicht (es verlangt
nur `isNewVersionOf`). Der Autor liest die Concept-DOI vom Record ab („Cite all versions“); dann `isVersionOf` in den Metadaten ergänzen und
die DOI in README, Wiki und `AGENTS.md` nachtragen.

## Was geändert wurde

- `release/papers/physics-standalone.json`: `version` 1.1.0, `pdf_name`, `source_archive`, `payload_dir` (`release/physics-standalone-v1.1.0`),
  `tag` `physics-paper-v1.1.0`, `metadata` (neue Datei), `new_version_of` = 24539644; `deposition_id`, `version_doi`, `release_date` leer
  (schreibt `stamp`).
- `release/zenodo/metadata_physics_standalone_1_1_0.json` (neu, aus 1.0.0): Version 1.1.0; Beschreibung an die jetzige Zusammenfassung des
  Artikels angeglichen, Absatz „New in 1.1.0“, Absatz „Scope“ (Runden bis v4.10.0-r67, „no number of generations“, Hinweis auf 1.0.0);
  `isNewVersionOf`. `publication_date` 2026-11-26 ist ein Platzhalter, `stamp` setzt das Datum.
- `paper/physics-standalone/release-info.tex` **entfernt**. Die Datei trug die Zeile der Fassung 1.0.0 mit deren DOI; ein Probe-Build des
  berichtigten Textes hätte damit „Version 1.0.0 · doi:…24539644“ auf der Titelseite gezeigt. Ohne die Datei setzt `article.tex` die
  Entwurfszeile („Draft · November 2026“). `stamp` schreibt die Datei nach der Reservierung neu (Version 1.1.0, neue DOI, Datum);
  `build --final` verlangt sie und bricht ab, wenn die Titelseite die neue DOI nicht zeigt oder „Draft“ sagt.
- Nicht angefasst: `paper/physics-standalone/article.pdf` (im Repo noch das PDF der 1.0.0). Nach dem Release-Build durch das neue ersetzen
  oder so lassen; Entscheidung beim Release-Commit.

## Änderungen 1.0.0 → 1.1.0

Vergleich des Quellarchivs der 1.0.0 (`Quantum_Sphaera_One_Object_Three_Frames_v1.0.0_source.tar.gz`, Quellstand 4e50bff0) mit dem
Arbeitsbaum (letzter Commit an den Quellen: c0657a6a, PR #338). Unverändert: `article.tex`, `article.pdf`, F2, F3, F5, F6, F9,
`refs/A`–`D`. Einzelnachweis der Berichtigungen: `notes/research/v4_10_0_r64_nachtrag_audit/README.md`.

| Datei | Änderung |
|---|---|
| `00-abstract` | sin δ_PMNS < 0 braucht eine weitere Setzung; Koide nur in der Gram-Lesart (mittlerer quadratischer Überlapp); Überlapp auf ein Postulat zurückgeführt, Phase bleibt Fit; β_sym folgt aus einer Zählregel, die Postulat ist und nicht hergeleitet; Generationszahl nicht hergeleitet |
| `01-introduction` | „des freien Trägers“, Hinweis auf spätere Runden, Stand der Testzählung; β_sym „eingesetzt oder auf ein benanntes Postulat gestützt“ |
| `02-carrier` | Belegstellen berichtigt; „erzeugt das Photon“ als überholt statt korrigiert; Generationszahl ist auch in der größeren Algebra Eingabe |
| `03-frames` | Ladungsgleichheit M/T „gesichert als Algebra“ unter einer Lesart; Dorau–Much als Argument (reelles Skalarfeld, führende Ordnung); Herleitung φ = sech 2η_R; Ausnahme Fixpunkt einer Tauschabbildung (J vom J_B-Typ, nicht D) |
| `04-particles` | drei Oktonion-Kopien als drei Lesarten einer Generation; H130 stützt die Achse e₈ nicht; relatives CP-Vorzeichen gilt für jede Ladungsachse und hängt an einer Setzung (dieselbe Seite der Multiplikation in beiden Sektoren, r65, H162) |
| `05-koide` | K = 0,6666645 ± 0,0000051 (0,43σ unter 2/3); Mischwinkel-Form, π/4 als Fixpunkt unter Postulat; δ Fit; H102 mit ρ² = 0,500014 |
| `06-beta` | Berichtigungen (m_W = 82,69 GeV in der SU(2)-Zählung, Formulierungen, H123b in der Widerlegt-Liste); **neuer Unterabschnitt** „The counting rule as a postulate, and the two-readout reading“: Postulat C1–C3 (r67), β_sym = 0,5494056410, γ_L = 1,8646997646 als Rechnung; Zwei-Auslesen-Lesart (r66) leitet keinen Wert her; H165 widerlegt (Schließung gibt 1/√3); OP1 offen |
| `07-action` | γ_L = 1,8647; Prüfungen der richtigen Runde zugeschrieben; H88/H90/H86 „nicht blind“; ΔN_eff-Zahlen; Schleifen-Ansatz auf dem Turm legt keine Skala fest |
| `08-lambda-op5` | Λ-Auslesung „sobald das Paar der Zählregeln gewählt ist“; Wolfram-Prüfung nur der algebraischen Schritte; Definitionen und Bedingungen der Schranken ergänzt |
| `09-open` | OP1: Zählregel als Postulat, „derive the counting postulate“ bleibt offen; OP3 wieder aufgenommen; OP4 unter der Setzung „dieselbe Seite“; Tabelle: H105, NuFIT-Hinweis bei H125 |
| `10-conclusion` | auch H100 hängt nicht an β_sym; Zahlen in OP2–OP5 statt „jede“; β_sym aus postulierter, nicht hergeleiteter Zählregel |
| `A-ledger` | Status von H98, H123d, Albert präzisiert; CP-Vorzeichen „bedingt auf eine Setzung“ (r65); zwei neue Zeilen (Zählpostulat; Zwei-Auslesen-Lesart, H165 widerlegt); Tabelle in `\footnotesize` |
| `B-reproduction` | Runden bis r67 genannt („Nothing after r67 is used“); Aussagen über Rundenenden und Ablageorte der Test-Notizen berichtigt |
| `figures/F1`, `F4`, `F8` | Kante Kern → Feldklassen; Weg A mit den drei Lesarten; Maxwell-Gleichung als vorausgesetzt |
| `refs/references.tex` | Companion-Eintrag: Forschungsschicht „up to round v4.10.0-r67“ statt r61 |
| `scripts/F7`, `F10` (+ Ausgaben, PDFs neu erzeugt) | relative statt absoluter Pfade; Zahlen laut Prüfnotiz identisch |

`refs/references.tex` nannte die Forschungsschicht noch „up to round v4.10.0-r64“; im Zuge dieser Vorbereitung auf r67 angeglichen (wie `B-reproduction.tex` und der Text).

Kein offenes Problem (OP1–OP5, C5, C6/T2) ist geschlossen; die Zählregel ist Postulat, H165 ist widerlegt.

## Geprüft (26.11.2026, Cloud-Container, tatsächliche Ausgaben)

- `python tools/paper_release.py check --paper physics-standalone`: „Result: ok“ (Payload „not built yet“, „Deposition: not reserved“).
- `python tools/paper_release.py build --paper physics-standalone --out <scratch>` (ohne `--final`): **51 Seiten**, Overfull hbox 0,
  Underfull hbox 3, „Log failures: none“ (keine undefinierten Verweise oder Zitate, keine doppelten Labels, kein Rerun-Hinweis),
  „Title page DOI: not yet (draft build)“, Titelseite zeigt „Draft · November 2026“, „Result: ok“. Paketquellstand c0657a6afe231e2877531430cc199f4c283b14d0;
  pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian). Der Probe-Payload liegt nicht im Repository.
- `python tools/paper_release.py zenodo --paper physics-standalone --stage reserve` (Trockenlauf, ohne `--execute`): Exit 0,
  „Dry-run only: metadata validated; no Zenodo API mutation performed.“; der Aufruf enthält `--new-version-of 24539644`.
- Nicht gelaufen: `stamp`, `build --final`, `check --final`, Upload, Veröffentlichung, `notes`, Lauf im GitHub-Workflow.

## Nächste Schritte (jeder nur mit ausdrücklicher Freigabe des Autors)

Auf einem Release-Zweig (z. B. `release/physics-paper-v1.1.0`), Workflow „Paper release (standalone papers)“ mit `paper=physics-standalone`.
Vorher `notes/anleitungen/zenodo-datenbank-vorbereiten.md` anwenden.

1. **Reservieren:** `stage=reserve`, `execute=true`. Legt einen unveröffentlichten Entwurf als neue Version von 24539644 an, vergibt die Version-DOI.
2. **Stempeln:** `python tools/paper_release.py stamp --paper physics-standalone --deposition-id <id>`; Konfiguration, Metadaten und
   `release-info.tex` committen. Dabei `isVersionOf` mit der Concept-DOI ergänzen (siehe oben).
3. **Release-Build und Payload:** `build --final`, dann `release/physics-standalone-v1.1.0/` committen und pushen; `check --final`.
4. **Upload:** `stage=upload`, `execute=true`; Entwurf und Vorschau auf Zenodo ansehen.
5. **Veröffentlichen (endgültig):** `stage=publish`, `execute=true`, `confirm_publish=true`.
6. **Vorschau prüfen:** nach Upload und nach Veröffentlichung (`stage=preview`; Dauerauftrag vom 24.11.2026).
7. **Release-Notiz, Merge, Tag:** `python tools/paper_release.py notes --paper physics-standalone`; Release-PR mergen; Tag
   `physics-paper-v1.1.0` und GitHub-Release. Die Cloud-Umgebung kann keine Tags pushen: der Autor setzt den Tag lokal oder über den
   Workflow „GitHub Release anlegen“, dessen Aufruf `notes` ausgibt.
8. **Nachziehen:** `release/physics-standalone-v1.1.0/README.md`, Wiki (Versionen und Quellen), `AGENTS.md` (DOI-Liste), `CITATION.cff` falls
   betroffen, Übergabe, Register #17; Tabelle in `notes/anleitungen/paper-release.md` (nennt noch Metadatendatei und Tag der 1.0.0).
