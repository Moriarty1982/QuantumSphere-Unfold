# Übergabe: Stand der letzten Sitzung

## Stand vom 19.11.2026 (Codex)

- **Abbildungen in PR #196:** Vier Julia-Panels und Vergleichsseite als PDF/PNG rekonstruiert. Neue OP5-Modellgrafik für Langfassung und Physik-Paper. Sechs historische Julia-Dateiverweise gelöst. Sechs historische OP5-Fitdateien bleiben ohne Original-Benchmarkdaten offen.

- **Dokumentindex:** PR #196 um den Historical Witness und die abfragbaren TeX-Verweise erweitert. Lokal in `build/qam.sqlite3` aktiv. Langfassung 62, Historical Witness 10 und Physik-Paper 1 indexierte LaTeX-Quellen. Zwölf historische Grafikziele fehlen am geprüften Quellstand. QAM-Guardregister und Forschung bleiben unverändert.

- **GitHub:** `main` bei `f85f29b8c094307c724369143c07e3ca0cce9a21`. PR #194 (ungerade Plateaus), #195 (bifokale Sondenform) und #187 (Vermittlerprofil) gemergt. Wiki Sync 44442247354 und Dokumententwurf 44442247290 erfolgreich.
- **Offen:** Entwurfs-PR #196, Dokument-Store und Buildmanifest. Die drei Notizen sind quellgebunden importiert; die drei Prüfpflichten stehen einzeln offen. 17 lokale Tests bestanden, frischer und migrierter Store erzeugten beide LaTeX-Exporte. GitHub-Build auf dem Toolchain-Commit `3ec7fb5687ddb41634478eb49820f088d4a517dd` erfolgreich: [Lauf 44444680332](https://github.com/Moriarty1982/QuantumSphere-Unfold/actions/runs/44444680332).
- **Lokal:** `build/qam.sqlite3` auf Schema 7 migriert. Integrität, Fremdschlüssel und Erhalt von alten Quellen, Versionen, Guards, Reviews, Checks, Ledger, Editionen und Snapshots geprüft. Snapshot `dd8f3d3b2a08a14061c85c8a87017c3fee5f04cd0dafad2f7a8dede1b2302a77`. Abgeleiteter Manuskriptindex: 62 Dateien und 2.856 Aussagen. Sicherung: `build/qam-before-refresh-f85f29b.sqlite3`.
- **Arbeitskopie:** Getrackter lokaler Checkout steht bei `0f8fda0`. Aktuelle Verifikation in isoliertem Arbeitsordner `build/qsc-db-refresh-f85f29b`. Lokaler MiKTeX-Lauf am Verzeichniszugriff gescheitert. Maßgeblich für PDF-Checks ist der Container-Build.
- **Forschung:** OP5 braucht eine hergeleitete native Randkopplung und physikalische Auslese. Nichtlineare und dynamische Stabilität sowie H96 bleiben offen. Keine neue Hypothese oder Veröffentlichung. Öffentliche Basis v5.2.0; H112 und die übrigen Spuren stehen in der [vorigen Übergabe](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/f85f29b8c094307c724369143c07e3ca0cce9a21/llm/Uebergabe.md).
