# Deutscher Preprint, Fassung 0.3.0: Release-Paket

**Status (24.11.2026): vorbereitet, nicht reserviert, nicht veröffentlicht.** Jeder Zenodo-Schritt nur mit ausdrücklicher Freigabe des
Autors (`AGENTS.md`). Concept-DOI 10.5281/zenodo.24405552; Vorgänger 0.2.0, Record 24481107, DOI 10.5281/zenodo.24481107.

- Quelle: `paper/preprint-de/` (Fassung 0.3.0, 58 Seiten, lokaler Build mit TeX Live 2023: 0 Overfull, keine undefinierten Verweise).
- Metadaten: `release/zenodo/metadata_preprint_de_0_3_0.json` (isVersionOf Concept 24405552, isNewVersionOf 0.2.0 24481107, Bezug
  Companion v5.3.0 und Repository).
- Payload: `Quantum_Sphaera_Preprint_0.3.0.pdf` in diesem Ordner, wird **nach** der Reservierung gebaut, weil die Titelseite die
  Version-DOI trägt; dazu `SHA256SUMS.txt`.
- Lokaler Trockenlauf von `tools/zenodo_publish.py` (`--new-version-of 24481107 --reserve-only --dry-run`) am 24.11.2026 bestanden
  (Metadaten gültig, keine API-Änderung).

## Änderungen gegenüber 0.2.0

Quelle jeder Änderung ist eine Companion-Runde (`sources/research/parts/v4100-post-release-layers.tex`); der Artikel gibt sie verkürzt
wieder. Kein offenes Problem ist geschlossen, kein Guard aufgehoben.

### Tests mit vorab festgelegtem Kriterium

| Test | Runde | Blind? | Ergebnis |
|---|---|---|---|
| H123 (zeitlich geordnete Oktant-Auslese) | r58 | a–c nicht blind, d grob vorab geschätzt | a, c bestätigt; b widerlegt (trennt nur j ∉ 2ℕ); d trägt nicht (m_W −20σ) |
| H124 (Kaskade mit Attraktor Ω_M = β², gegen DESI DR2) | r57 | nicht blind | nicht ausgeschlossen (p = 0,072), aber Ω_M heute ≈ 0,50 und Δχ² = 7,87 gegen ΛCDM |
| H125 (relatives CP-Vorzeichen Leptonen/Quarks) | r59.6 | Stufe A nicht blind; Stufe B blind gegen künftige Daten | Stufe A bestätigt; Stufe B offen (sin δ_PMNS < 0 unter Setzung S1, Frist 2035) |
| H126 (PMNS aus zwei Oktonion-Richtungen) | r59.11 | vorab festgelegt | nicht prüfbar (Konstruktion überall entartet) |

### Erkundungen (nicht blind, prüfen nichts)

| Thema | Runde | Kern |
|---|---|---|
| Λ als Eingabe (Negativ-Schluss des OP5-Rests) | r56 | für die genannte Klasse ist der Absolutwert von Λ eine Eingabe, gleichwertig die Epoche „heute“ |
| Hopf-Lücke als Nullpunkt (k245) | r59.1 | mit j + ½ exakt β_sym = 1/√3; Daten verfehlt |
| Restdrehung als Holonomie (k246) | r59.2 | größter Formzyklus dreht um −π; γ_M bleibt eingesetzt |
| Licht als Vermittler (k247–k249) | r59.3 | τ_T = −τ_M; Drehsinn nirgends hergeleitet |
| Drehsinn aus dem Lichtgewicht (k250) | r59.4 | a − b hat die Parität von τ; absoluter Drehsinn = Wahl von i |
| Λ und Drehrate (k251) | r59.5 | nur Formvergleich, Umbenennung von Λ |
| Erzeugungsregel des HS-Turms (k253) | r59.7 | HS(0)–HS(3) mit U(1), SU(2), G₂/su(3); ab HS(4) keine stetige Symmetrie mehr |
| HS(4), S₃ und Bott (k254) | r59.8 | diskrete S₃ der Oktonionen-Kopien; Achsen nach Radon–Hurwitz, Periode 4 |
| r13 neu gelesen (k255) | r59.9 | K = ⅔ genau bei exp(uπ/4); δ frei; drei Generationen passen nicht |
| Mischung aus der Kopiengeometrie (k256) | r59.10 | nur bekannte Muster |
| Turm rückwärts (k270–k272) | r59.12 | N_c = 3 im Turm-Modell erzwungen; nur (−,−,−) kompakt |
| Drei Generationen rückwärts (k273) | r59.13 | CP-Phase erst ab N = 3; Verdopplungseinheiten wirken als Dublett |
| Nichtlineares Ursprungsfeld (k274) | r59.14 | Skala ja, Struktur unverändert |

### Im Artikel

- Titelseite: „Fassung 0.3.0“, Datum 24.11.2026, Version-DOI leer bis zur Reservierung; Zusammenfassung um einen Satz zum Drehsinn ergänzt,
  Vorgänger 0.2.0 genannt.
- Neuer Abschnitt 5.7 „Drehsinn und Turm der Hilbert-Shifts“ (r59); Tabelle der offenen Probleme verweist bei OP3 und OP4 darauf.
- Abschnitt 5.8 (bis 0.2.0 Nummer 5.7): r56, r57, r58 (bereits nach 0.2.0 im Entwurf).
- Anhang C: Originalausgaben zu r58 (Wolfram und Qiskit).
- Literatur: neuer Eintrag `towerlayer` (r59), `layers` bis r59.

## Schritte

0. **PR mergen** (Freigabe nötig), danach die Literaturlinks `towerlayer`, `lambdainput` und SOURCES.md auf den Merge-Commit pinnen.
1. **Reservierung** (Freigabe nötig; legt einen unveröffentlichten, verwerfbaren Entwurf an):
   ```
   gh workflow run "Zenodo Release" --repo Moriarty1982/QuantumSphere-Unfold --ref <Zweig> \
     -f environment=production -f new_version_of=24481107 -f reserve_only=true -f replace_files=false \
     -f publish=false -f confirm_publish=false -f dry_run=false \
     -f metadata=release/zenodo/metadata_preprint_de_0_3_0.json -f files_glob='release/preprint-de-v0.3.0/*'
   ```
   Vorher derselbe Aufruf mit `-f dry_run=true`. Aus dem Protokoll `deposition_id` und `reserved_doi` festhalten.
2. **Titelseite und PDF:** in `paper/preprint-de/article.tex` `\newcommand*{\versiondoi}{10.5281/zenodo.<id>}` setzen, dreimal bauen, PDF als
   `Quantum_Sphaera_Preprint_0.3.0.pdf` hierher kopieren, `sha256sum Quantum_Sphaera_Preprint_0.3.0.pdf > SHA256SUMS.txt`, in den Metadaten
   die Version-DOI und den Quellcommit in `notes` eintragen.
3. **Upload** (Freigabe nötig; der Entwurf erbt die Datei von 0.2.0, deshalb `replace_files=true`):
   ```
   gh workflow run "Zenodo Release" --repo Moriarty1982/QuantumSphere-Unfold --ref <Zweig> \
     -f environment=production -f deposition_id=<id> -f reserve_only=false -f replace_files=true \
     -f publish=false -f confirm_publish=false -f dry_run=false \
     -f metadata=release/zenodo/metadata_preprint_de_0_3_0.json -f files_glob='release/preprint-de-v0.3.0/*.pdf' \
     -f default_preview=Quantum_Sphaera_Preprint_0.3.0.pdf
   ```
   Danach den Entwurf auf Zenodo ansehen, besonders die Vorschau (Haupt-PDF).
4. **Veröffentlichung** (Freigabe nötig, endgültig): derselbe Aufruf mit `-f publish=true -f confirm_publish=true`.
5. **Danach:** Tag `preprint-de-v0.3.0` und GitHub-Release mit Version-DOI und Record-Link; README des Preprints, ZENODO.md, Wiki
   (Versionen und Quellen, Forschungsstand) und Übergabe nachziehen; Register #17 kommentieren.
