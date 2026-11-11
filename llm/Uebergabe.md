# Übergabe: Stand der letzten Sitzung

11. November 2026 (Codex).

- Autorenauftrag: commit/merge/push, erledigte Branches aufräumen, 5.0-Veröffentlichung vorbereiten; künftig Langfassung und Physikpaper, möglichst gemeinsame DOI.
- PR #94 gemergt als 3a68669b0b12766c256ae6eeed1f52ae0693acc4; main lokal synchronisiert. Das ist die nächste Bundle-Basis.
- Vorbereitungsbranch: `codex/v5-release-prep`.
- Entwicklung 5.0.0-draft, öffentliche Baseline 4.11.0/10.5281/zenodo.24108818.
- **Aktuelle Steuerung:** Autor möchte den Umfang der Physikfassung erst besprechen, insbesondere QAM/MML/MMA als neue Schreibweise. KEINE Entscheidung für ein reines Koide/HC-Paper.
- Plan `notes/research/v5_0_0_dual_document_plan.md`: Langfassung plus eigenständige physikalische Argumentationslinie, notwendige Notationseinführung und vollständiges Methodenbeispiel.
- Datenbankexport vorhanden, vollständiger Argumentationsbaum nicht geprüft. Automatischer gemeinsamer Zwei-PDF-Build noch nicht implementiert; keine Physikfassung fertiggestellt.
- Zenodo offiziell geprüft: mehrere Dateien können in einem Record dieselbe Versions-DOI teilen. Neue 5.0-Version bekommt neue Versions-DOI, Concept-DOI bleibt 10.5281/zenodo.19210728.
- Kein Zenodo-Entwurf/Upload/Publish in diesem Block. Keine neue DOI.
- Branch-Aufräumen blockiert: alle 22 geprüften lokalen/Remote-Verweise sind Vorfahren von main, 0 exklusive Commits. Automatische Freigabeprüfung lehnte die breite Löschung historischer Forschungsbranches wegen unklarer Autorisierung ab. NICHT umgehen oder ohne ausdrückliche Listenfreigabe erneut versuchen.
- Exakte Liste mit Spitzen: `notes/research/v5_0_0_branch_cleanup_review.md`. Nichts gelöscht; main und Vorbereitung bleiben erhalten.
- Neue Forschung (jetzt in main): reguläres positives Zeta-Spektralpaket, HC-Balance und endliche Parameter-/Fourier-Streuungen. Native Auswahl und physikalische Massenauslesung offen.
- Bisherige Mathematiknotizen: hc_root_transfer_rotation_gate_2026_11_11.md, zeta_positive_spectral_packet_2026_11_11.md.
- Weiterhin keine OP-Schließung, keine neue H-/k-Nummer oder QAM-Beweisfreigabe.
- DB build/qam.sqlite3, Inventar 2468 Aussagen/61 Dateien; viele rohe Guards offen.
- Letzte Codevalidierung vor PR93: 26 Storetests, 18 HC-Tests, 35 Koide/Kernel. PR93 main-PDF/Wiki/Lean/TeX/Batch erfolgreich.
- Nächster Schritt: mit Autor physikalische Leitfrage/Themenumfang und Methodenanteil abstimmen, dann zwei feste Ausgabeprofile und Buildautomation implementieren. Aktuelle Pläne sind noch kein Releasepaket.
- `.codex/environments/` außerhalb der Commits belassen.
