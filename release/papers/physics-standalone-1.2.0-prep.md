# Physik-Artikel „One Object, Three Frames“, Fassung 1.2.0: Vorbereitung

**Status (28.11.2026): Entwurf, nicht reserviert, nicht veröffentlicht.** Kein Zenodo-Schritt ist erfolgt. Vorfassung: 1.1.0, Record 24563808,
Version-DOI 10.5281/zenodo.24563808 (veröffentlicht 26.11.2026); Concept-DOI des Records 10.5281/zenodo.24539643.
Ablauf: `notes/anleitungen/paper-release.md`, Abschnitt „Spätere Fassungen“.

Grundlage: Companion v5.6.0 (reserviert, Version-DOI 10.5281/zenodo.24632437, Schichten v4.10.0-r69 bis r75); Vorgänger v5.5.0
(10.5281/zenodo.24563811). Der deutsche Preprint 0.5.0 (reserviert, 10.5281/zenodo.24632440) beruht auf derselben Companion-Version und wird
im Artikel und in den Metadaten mit DOI genannt (Dauerauftrag vom 28.11.2026, gegenseitige Verlinkung).

## Was neu ist (1.1.0 → 1.2.0)

| Datei | Änderung |
|---|---|
| `sections/00-abstract` | Leptonphase (Winkel, gesetztes Vorzeichen, gemessener Wert 0.0395773); Hinweis auf den datierten Vorhersage-Abschnitt; „dual frame“ |
| `sections/01-introduction` | Stand v5.6.0 (r69–r75), Verweise auf die neuen Abschnitte; Koide-Phase „auf einen gemessenen Drehwinkel zurückgeführt“ |
| `sections/03-frames` | Absatz „Names from r69 on“ ergänzt: Re-/Im-Sektor (nur Leptonen, Lesart unter H99); Lage der Frames auf der Halbkugel der Feldzustände (r70.1, r70.2); Korrektur r70.4 an r69.4 |
| `sections/05-koide` | neuer Unterabschnitt „The lepton phase: an angle, a branch and one measured number“ (r73, r74; H213–H236, Massenbilanz H227); zwei Zeilen in der Testtabelle; Zusammenfassung. Der Winkel heißt im Artikel `φ_ℓ`, weil `φ` dort schon der Biegewinkel des gebogenen Oktanten ist; der Text sagt, dass der Companion ihn `φ` nennt |
| `sections/09-open` | neuer Unterabschnitt „Predictions of this version (as of 28 November 2026)“ mit Tabelle (Größe / Vorhersage / Quelle / beruht auf) und Versionsregel, Verweis auf r75 als vollständiges Register; OP3 um r73/r74 ergänzt; Guards „bis r75“, Wächter W_γ nach r72 („no global photon-clock theorem“); OP2: „Riemann work“ durch „an earlier manuscript of the author“ ersetzt (war beim Kürzen in 33e035b6 übersehen) |
| `sections/10-conclusion` | Leptonphase, Vorhersagetabelle |
| `sections/A-ledger` | sechs Zeilen (r69, r70, r73, r74, r75) |
| `sections/B-reproduction` | Quellstand v5.6.0, Runden bis r75, Ordner der Tests H213–H236; Preprint 0.5.0 zitiert |
| `refs/references.tex` | QSC auf v5.6.0 (10.5281/zenodo.24632437, Vorgänger v5.5.0); neuer Eintrag `QS-preprint-de` (0.5.0, 10.5281/zenodo.24632440) |
| `release/zenodo/metadata_physics_standalone_1_2_0.json` | neu: Version 1.2.0; Absatz „New in 1.2.0“ mit Vorhersagen und Einordnung (gemessen/gesetzt/Postulat/angepasst), Versionsregel; „Scope“ (OP1–OP5, C5, C6/T2 offen); `isNewVersionOf` 24563808, `isVersionOf` 24539643, `isSupplementTo` und `references` Companion v5.6.0, `references` v5.5.0, Concept-DOI und Preprint 0.5.0; „Version DOI: to be reserved“ |

Zahlen der Vorhersagetabelle aus `qam/editions/v5_expanded_limits.tex` (Abschnitt „Predictions of this version“) und Schicht r75 übernommen
und gegen r73.10/r75.3 abgeglichen. Kein offenes Problem ist geschlossen; φ ist gemessene Eingabe, das Vorzeichen der Zweigwahl eine Setzung,
β_sym aus dem Zählpostulat (r67) berechnet, nicht hergeleitet.

**Nicht angefasst:** `release-info.tex` (schreibt `stamp`), `release/papers/physics-standalone.json` (stellt der Koordinator um),
`article.tex`, Abbildungen, Skripte, `article.pdf`.

**Achtung `release-info.tex`:** Die Datei trägt noch Version 1.1.0 mit DOI 10.5281/zenodo.24563808. Ein Probe-Build zeigt damit
„Version 1.1.0 · doi:…24563808“ auf der Titelseite. Wie bei 1.1.0 vor dem Probe-Build entfernen (dann Entwurfszeile) oder nach der
Reservierung mit `stamp` neu schreiben.

## Geprüft (28.11.2026, Cloud-Container, tatsächliche Ausgaben)

- Kein `pdflatex` im Container (`which pdflatex` leer): **kein Build, keine Seitenzahl gemessen.** Geschätzter Zuwachs etwa 2 bis 3 Seiten
  (Leptonphase gut 1 Seite, Vorhersageabschnitt mit Tabelle etwa 1,3 Seiten, Rest kurze Ergänzungen) gegenüber 51 Seiten der 1.1.0.
- Skriptprüfung der LaTeX-Quellen (`article.tex`, `sections/`, `figures/*.tex`, `refs/`): Klammern ausgeglichen, Umgebungen paarig, keine
  doppelten Labels, alle `\ref`/`\eqref` mit Label, alle `\cite` mit `\bibitem`, kein ungenutzter Eintrag. Benutzt nur geladene Pakete
  (`tabularx`, `booktabs`, `array`).
- Guard-Linter (`notes/research/v4_8_0_r03_r12/llm/training/guard_linter.py`) auf Metadaten und geänderte TeX-Dateien: „0 Treffer“.
- `check_metadata` aus `tools/paper_release.py` in-process mit einer auf 1.2.0 umgestellten Konfiguration (ohne Dateiänderung): keine Probleme.
- `python tools/paper_release.py check --paper physics-standalone`: „Result: ok“, prüft aber noch die Konfiguration 1.1.0.
- Kein Vorkommen von „Riemann“ in Artikel und Metadaten außer dem physikalischen Fachbegriff „Riemann–Silberstein vector“ (Abschnitt 2, Literatur).

## Nächste Schritte (jeder Zenodo-Schritt nur mit ausdrücklicher Freigabe des Autors)

1. Koordinator: `release/papers/physics-standalone.json` auf 1.2.0 umstellen (`version`, `pdf_name`, `source_archive`, `payload_dir`
   `release/physics-standalone-v1.2.0`, `tag` `physics-paper-v1.2.0`, `metadata` neue Datei, `new_version_of` 24563808; `deposition_id`,
   `version_doi`, `release_date` leeren); `release-info.tex` entfernen; `check` und Probe-`build` laufen lassen (Seitenzahl, Log).
2. **Reservieren** (`stage=reserve`, `execute=true`), dann `stamp --deposition-id <id>`; Metadaten (Notes/Beschreibung) mit der neuen DOI.
3. `build --final`, Payload committen, `check --final`.
4. **Upload**, Vorschau prüfen; **Veröffentlichen** erst nach Companion v5.6.0 oder zusammen mit ihm (Version-DOI 24632437 löst erst danach auf).
5. Release-Notiz, Tag `physics-paper-v1.2.0`, README im Payload, Wiki „Versionen und Quellen“, `AGENTS.md`, Übergabe, Register #17.
