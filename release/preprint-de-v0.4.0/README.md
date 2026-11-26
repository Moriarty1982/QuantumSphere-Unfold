# Deutscher Preprint, Fassung 0.4.0: Release-Paket

**Status (26.11.2026): reserviert, nicht hochgeladen, nicht veröffentlicht.** Zenodo-Entwurf 24563916 als neue Fassung des Records
24497991, reservierte Version-DOI 10.5281/zenodo.24563916 (Trockenlauf 45842918715, Reservierung 45843670966, Workflow „Zenodo Release“;
vom Autor am 26.11.2026 freigegeben). Für Upload und Veröffentlichung weiter `deposition_id=24563916` verwenden, nicht `new_version_of`. Jeder Zenodo-Schritt (Reservierung, Upload, Veröffentlichung) braucht die ausdrückliche Freigabe des Autors (`AGENTS.md`); dasselbe
gilt für die Entscheidung, dass diese Fassung erscheint. Concept-DOI 10.5281/zenodo.24405552; Vorgänger 0.3.0 vom 24.11.2026,
[Record 24497991](https://zenodo.org/records/24497991), DOI 10.5281/zenodo.24497991.

- Quelle: `paper/preprint-de/` (Fassung 0.4.0; lokaler Build am 26.11.2026 mit leerer Version-DOI: 61 Seiten, 0 Overfull, keine
  undefinierten Verweise oder Zitate).
- Metadaten: `release/zenodo/metadata_preprint_de_0_4_0.json` (isVersionOf Concept 24405552, isNewVersionOf 0.3.0 24497991, Bezug
  Companion v5.4.0, DOI 10.5281/zenodo.24500009, und Repository). **Erscheint vorher der Companion v5.5.0, den Bezug in den
  Metadaten (`related_identifiers` und Absatz „Geltungsbereich“) auf dessen Version-DOI umstellen.** `publication_date` 2026-11-26 ist
  vorläufig und wird vor dem Veröffentlichen auf das tatsächliche Datum gesetzt, ebenso das Datum auf der Titelseite.
- Payload: `Quantum_Sphaera_Preprint_0.4.0.pdf` in diesem Ordner. Gebaut am 26.11.2026 nach der Reservierung, mit der
  Version-DOI auf der Titelseite (61 Seiten); Prüfsumme in `SHA256SUMS.txt`.
- Lokaler Trockenlauf von `tools/zenodo_publish.py` (`--new-version-of 24497991 --reserve-only --dry-run`) am 26.11.2026: bestanden
  (Meldung „Dry-run only: metadata validated; no Zenodo API mutation performed.“). Das Muster `*` erfasst zu diesem Zeitpunkt nur diese README; bei der Reservierung wird nichts hochgeladen.

## Änderungen gegenüber 0.3.0

Quelle jeder Änderung ist eine Companion-Runde (`sources/research/parts/v4100-post-release-layers.tex`); der Artikel gibt sie verkürzt
wieder. Kein offenes Problem ist geschlossen, kein Guard aufgehoben. Die Runden r60 bis r65 rechnen nichts neu; sie halten Befunde mit
dem Status der Ergebnis-Notizen fest.

### Tests mit vorab festgelegtem Kriterium

| Test | Runde | Blind? | Ergebnis |
|---|---|---|---|
| H127 (Brechung der Familien-SO(3) durch die Ladung) | r60.2 | vorab festgelegt | Stufe A bestätigt (reiner Spin-3-Tensor); Stufe B nach dem Wortlaut widerlegt, für jede zulässige Kopplung leer (r60.3) |
| H138–H147 (Oktonion-Kopien in den Sedenionen, Rest-Generation) | r62 | teils nicht blind | widerlegt: H138a, H138b, H142b, H144c, nach dem Wortlaut H139a, H145c; übrige Teile bestätigt. Drei Kopien, bedingt an die Definition; drei Lesarten einer Generation, nicht drei Generationen; keine Massen |
| H148–H156 (Koide-Punkt) | r63 | teils nicht blind | widerlegt: H150b in einem Teil, H155c, nach dem Wortlaut H150c, H155d; teilweise H151b, H156c; übrige Teile bestätigt (H153b bis auf eine Teilvorhersage). K = ⅔ folgt aus einem Postulat mit gesetzter Skala, nicht aus der Algebra |
| H128, H130 (Familiensymmetrie und Träger in den Sedenionen) | r64.1, r64.2 | teils nicht blind | H128a widerlegt (22 statt 17, numerischer Rang); H128b für e₇ bestätigt, für e₈ widerlegt; H130a, b bestätigt; CT-003 nicht gestützt, bleibt Platzhalter |
| H131, H134 (Mischung aus den Kopien) | r64.3 | teils nicht blind | H131a bestätigt, H131b widerlegt; H134a, c bestätigt, H134b widerlegt; Verträglichkeit, keine Vorhersage |
| H129, H132, H133, H135, H136 (rekursive Feldgleichung auf dem Turm) | r64.4 | teils nicht blind | H129, H133 nicht bestätigt; H132, H135, H136 widerlegt; keine Skala, kein Wert |
| H105 (Flächenschritte und Echos) | r64.5 | vorab festgelegt, gegen künftige Daten | offen, Frist 31.12.2028 |
| H162 (Ladungsachse) | r65.1–r65.3 | a, b, d nicht blind | a bis d bestätigt (c nur numerisch); Teil e ist eine Erkundung |
| H164 (β als Überlapp zweier Auslesen) | r66 | überwiegend nicht blind | trägt teilweise; gilt für jeden Wert von β und leitet keinen her |
| H165 (Schließungsbedingung der zwei Auslesen) | r67 | überwiegend nicht blind | widerlegt: erzwingt β = 1/√3, nicht den gemessenen Wert |

### Erkundungen (nicht blind, prüfen nichts)

| Thema | Runde | Kern |
|---|---|---|
| Trialität und Familien-SO(3) (k275) | r60.1 | Kommutant von G₂ in F₄; die Ladung bricht zu genau A₄ |
| No-go für die Quarks, Albert-Norm, Vakuumausrichtung (k277) | r60.3–r60.5 | bei exakter A₄ entartete Quarkmassen und keine Mischung; Ausrichtung hängt an freien Koeffizienten, kein blinder Test möglich |
| Korrekturen zu r56.4 und r07.4 (k320) | r61 | ρ_Λ = Λ/κ; Wurzel in β; keine Zahl, kein Testergebnis und kein Status ändert sich |
| Präzisierungen älterer Runden | r64.6–r64.8 | Zahlen und Geltungsbereiche, keine Statusänderung; der Tausch J ist weder z ↦ iz noch z ↦ z̄ |
| Zwei Ladungstypen (k361, nur numerisch) | r65.4 | das relative CP-Vorzeichen hängt an der Setzung „dieselbe Seite der Multiplikation in beiden Sektoren“ |
| Nachrechnung mit dem exakten β (k358) | r68 (Forschungsnotiz k358) | kein Urteil ändert sich; m_W gegen PDG 2026 von −0,44σ auf −0,13σ; m_τ (H102) bleibt bei +2,3σ |

Nicht hergeleitet und im Artikel so benannt: das Zählpostulat (r67, vom Autor am 26.11.2026 angenommen; OP1 bleibt offen) und das Postulat
der Gleichberechtigung von Materie- und Tachyon-Frame (r63, Arbeitsannahme des Autors vom 26.11.2026).

### Im Artikel

- Titelseite: „Fassung 0.4.0“, Datum 26.11.2026 (vorläufig), Version-DOI leer bis zur Reservierung (die Titelseite zeigt dann „wird bei
  der Reservierung auf Zenodo vergeben“). Zusammenfassung: Zählregel als Postulat, relatives Vorzeichen „unter einer benannten
  Setzung“, ein Satz zum Neuen, Vorgänger 0.3.0 genannt.
- Abschnitt 5.4: zwei Absätze zum Zählpostulat (r67), zur Zwei-Auslesen-Lesart (r66) und zu H165 (bereits nach 0.3.0 im Entwurf).
- Abschnitt 5.7: ein Satz mit Verweis auf die Einschränkung durch r65.
- Neuer Abschnitt 5.8 „Familiensymmetrie, Kopien und der Koide-Punkt“ (r60–r65, k358); der Abschnitt zu den offenen Punkten ist jetzt 5.9,
  seine Tabelle verweist bei OP3 und OP4 auf 5.8.
- Literatur: neue Einträge `countingpostulate` (r66, r67), `roundsr60r65` und `recalc` (k358); `layers` bis r67, mit dem Hinweis, dass die
  Runden bis r59 in v5.4.0 veröffentlicht sind.

## Schritte

0. **Quellstand auf `main`** (Merge nur mit Freigabe des Autors). Die Literaturlinks sind auf 3fc66afd (Merge von PR #337, Runden r60–r67)
   und c0657a6a (Merge von PR #338, k358) gepinnt. Vor der Reservierung die
   [Vorbereitung der Aussagen-Datenbank](../../notes/anleitungen/zenodo-datenbank-vorbereiten.md) anwenden.
1. **Reservierung** (**Freigabe des Autors nötig**; legt einen unveröffentlichten, verwerfbaren Entwurf an). Zuerst als Trockenlauf mit
   `-f dry_run=true`, dann:
   ```
   gh workflow run "Zenodo Release" --repo Moriarty1982/QuantumSphere-Unfold --ref claude/project-thread-edbdbc \
     -f environment=production -f new_version_of=24497991 -f reserve_only=true -f replace_files=false \
     -f publish=false -f confirm_publish=false -f dry_run=false \
     -f metadata=release/zenodo/metadata_preprint_de_0_4_0.json -f files_glob='release/preprint-de-v0.4.0/*'
   ```
   Aus dem Protokoll `deposition_id` und `reserved_doi` festhalten.
2. **Titelseite und PDF:** in `paper/preprint-de/article.tex` `\newcommand*{\versiondoi}{10.5281/zenodo.<id>}` setzen, Datum prüfen, dreimal
   bauen (0 Overfull, keine undefinierten Verweise), PDF als `Quantum_Sphaera_Preprint_0.4.0.pdf` hierher kopieren,
   `sha256sum Quantum_Sphaera_Preprint_0.4.0.pdf > SHA256SUMS.txt`, in den Metadaten die Version-DOI und den Quellcommit in `notes`
   eintragen, Seitenzahl hier, in `paper/preprint-de/ZENODO.md` und in der Beschreibung prüfen.
3. **Upload** (**Freigabe des Autors nötig**; der Entwurf erbt die Datei von 0.3.0, deshalb `replace_files=true`):
   ```
   gh workflow run "Zenodo Release" --repo Moriarty1982/QuantumSphere-Unfold --ref claude/project-thread-edbdbc \
     -f environment=production -f deposition_id=<id> -f reserve_only=false -f replace_files=true \
     -f publish=false -f confirm_publish=false -f dry_run=false \
     -f metadata=release/zenodo/metadata_preprint_de_0_4_0.json -f files_glob='release/preprint-de-v0.4.0/*.pdf' \
     -f default_preview=Quantum_Sphaera_Preprint_0.4.0.pdf
   ```
   **Danach die Vorschau prüfen:** den Entwurf auf Zenodo ansehen; die Vorschau muss das Haupt-PDF zeigen und die geerbte Datei von
   0.3.0 muss entfernt sein. Bei Bedarf korrigieren (`zenodo-fix-preview.yml`, siehe `notes/anleitungen/zenodo-release.md`).
4. **Veröffentlichung** (**Freigabe des Autors nötig, endgültig**): vorher `publication_date` und das Datum der Titelseite auf den
   tatsächlichen Tag setzen (bei geändertem Datum PDF neu bauen und Schritt 3 wiederholen); dann derselbe Aufruf wie in Schritt 3 mit
   `-f publish=true -f confirm_publish=true`. **Danach die Vorschau des veröffentlichten Records erneut prüfen** und bei Bedarf mit
   `zenodo-fix-preview.yml` korrigieren.
5. **Danach:** Tag `preprint-de-v0.4.0` und GitHub-Release mit Version-DOI und Record-Link; README des Preprints, `ZENODO.md`, Wiki
   (Versionen und Quellen, Forschungsstand) und Übergabe nachziehen; Register #17 kommentieren.
