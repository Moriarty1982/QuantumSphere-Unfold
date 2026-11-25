# Release-Konfiguration der eigenständigen Papers

Eine Datei je Paper; `tools/paper_release.py` und der Workflow `paper-release.yml` lesen nur von hier.
Ablauf: [`notes/anleitungen/paper-release.md`](../../notes/anleitungen/paper-release.md).

| Feld | Bedeutung |
|---|---|
| `title`, `version` | müssen mit den Zenodo-Metadaten übereinstimmen (`check`) |
| `source_dir`, `main`, `build` | Quelle und Build (`["sh", "build.sh"]` oder Liste von Engines) |
| `texinputs`, `build_needs` | Zusatzpfade, die beim Setzen gebraucht werden (nicht im Archiv) |
| `source_extra` | Zusatzdateien im Quellarchiv |
| `extra_files` | weitere Payload-Dateien aus dem Build-Baum |
| `lean_check` | QAM-Akte für `qamcheck` im Workflow (leer = keiner) |
| `pdf_name`, `source_archive`, `payload_dir`, `tag` | Namen der Release-Dateien |
| `new_version_of` | leer für die erste Fassung (neuer Record); sonst Record-ID der Vorfassung |
| `deposition_id`, `version_doi`, `release_date` | schreibt `stamp` nach der Reservierung |
