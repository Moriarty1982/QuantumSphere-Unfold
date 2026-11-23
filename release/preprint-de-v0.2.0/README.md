# Deutscher Preprint, Fassung 0.2.0: Release-Paket

**Status (23.11.2026):** reserviert (Workflow-Lauf 45257076362: Entwurf `deposition_id` 24481107, Version-DOI
10.5281/zenodo.24481107), PDF mit DOI auf der Titelseite gebaut; nicht hochgeladen, nicht veröffentlicht. Jeder Zenodo-Schritt nur mit
ausdrücklicher Freigabe des Autors (`AGENTS.md`).

- Quelle: `paper/preprint-de/` (Fassung 0.2.0, 55 Seiten, Build ohne Overfull und ohne undefinierte Verweise).
- Metadaten: `release/zenodo/metadata_preprint_de_0_2_0.json` (Concept-DOI 10.5281/zenodo.24405552, Vorgänger 0.1.0
  10.5281/zenodo.24405553, Bezug Companion v5.3.0 10.5281/zenodo.24434403).
- Payload: `Quantum_Sphaera_Preprint_0.2.0.pdf` in diesem Ordner, wird **nach** der Reservierung gebaut, weil die Titelseite die
  Version-DOI trägt; dazu `SHA256SUMS.txt`.
- Lokaler Trockenlauf von `tools/zenodo_publish.py` (`--new-version-of 24405553 --reserve-only --dry-run`) am 23.11.2026
  bestanden (Metadaten gültig, eine Datei, keine API-Änderung).

## Schritte

1. **Reservierung** (Freigabe nötig; legt einen unveröffentlichten, verwerfbaren Entwurf an):
   ```
   gh workflow run "Zenodo Release" --repo Moriarty1982/QuantumSphere-Unfold --ref release/preprint-de-0.2.0-prep \
     -f environment=production -f new_version_of=24405553 -f reserve_only=true -f replace_files=false \
     -f publish=false -f confirm_publish=false -f dry_run=false \
     -f metadata=release/zenodo/metadata_preprint_de_0_2_0.json -f files_glob='release/preprint-de-v0.2.0/*'
   ```
   Vorher derselbe Aufruf mit `-f dry_run=true`. Aus dem Protokoll `deposition_id` und `reserved_doi` festhalten.
2. **Titelseite und PDF:** in `paper/preprint-de/article.tex` `\newcommand{\versiondoi}{10.5281/zenodo.<id>}` setzen, die Literaturlinks
   auf den Release-Commit pinnen (erledigt: d2020d17), dreimal bauen, PDF als `Quantum_Sphaera_Preprint_0.2.0.pdf` hierher kopieren,
   `sha256sum Quantum_Sphaera_Preprint_0.2.0.pdf > SHA256SUMS.txt`, in den Metadaten die Version-DOI in `notes` eintragen.
3. **Upload** (Freigabe nötig; Entwurf erbt die Datei von 0.1.0, deshalb `replace_files=true`):
   ```
   gh workflow run "Zenodo Release" --repo Moriarty1982/QuantumSphere-Unfold --ref release/preprint-de-0.2.0-prep \
     -f environment=production -f deposition_id=<id> -f reserve_only=false -f replace_files=true \
     -f publish=false -f confirm_publish=false -f dry_run=false \
     -f metadata=release/zenodo/metadata_preprint_de_0_2_0.json -f files_glob='release/preprint-de-v0.2.0/*.pdf' \
     -f default_preview=Quantum_Sphaera_Preprint_0.2.0.pdf
   ```
   Danach den Entwurf auf Zenodo ansehen, besonders die Vorschau (Haupt-PDF).
4. **Veröffentlichung** (Freigabe nötig, endgültig): derselbe Aufruf mit `-f publish=true -f confirm_publish=true`.
5. **Danach:** Tag `preprint-de-v0.2.0` und GitHub-Release mit Version-DOI und Record-Link; README des Preprints, Wiki
   (Versionen und Quellen) und Übergabe nachziehen; Register #17 kommentieren.
