# Übergabe: Stand der letzten Sitzung

11. November 2026 (Codex). Einstieg, keine vollständige Forschungsgeschichte.

- Branch: `codex/qam-statement-store`; letzter Commit vor diesem Block `31c11e6`.
- Öffentliche Baseline laut Repo: v4.11.0; kein Release in diesem Block.
- Änderungen dieses Blocks: HC-Zweig (5 Aussagen/Originalbeweise) und bedingter HC–Koide-Anschluss mit quellengebundener Selbstprüfung.
- Koide/HC-Quellen unverändert. Abstrakte Aussagen gelten unter den expliziten Hypothesen; native Realisierung bleibt offen.
- Koide-Anschluss: K=2/[3(1+h)], h=<B*e,JB*e>; Koide genau bei h=0.
- Drei neue Guards: native Abbildung/Seed/Wurzelgesetz; unabhängige Orthogonalität; maschinenprüfbare Frame-Abbildung.
- Frame-Warnung bleibt bewusst bestehen; kein impliziter M/T/P-Wechsel.
- Aktuelle DB: `build/qam.sqlite3`. Generierte Dateien sind lokale Buildartefakte.
- Bridge-Snapshot: `14a0793aec6832a8471ac18bf2c3305be1f47de08ab8970fa44780a74252e6dc`.
- Baum/LaTeX: `build/qam-hc-koide-bridge/argument.md` und `paper/paper.tex`.
- Reproduktion: `python -m qam.tools.review_hc_koide_bridge --out build/hc-koide-new` (neuer Zielordner).
- Berichte: `notes/research/hc_identification_store_review_2026_11_11.md`, `hc_koide_bridge_review_2026_11_11.md`.
- Neue Regressionstests prüfen Originalzuordnung, transitive Auswahl, offene Guards, Quellenänderungen und Idempotenz.
- Validierung: 26 Storetests und 18 HC-Tests erfolgreich; statischer LaTeX-Export bestanden, kein PDF-Build dieses Blocks.
- Keine neue H-/k-Nummer. Bisherige Übergabe nannte H98/k219; nicht neu vergeben.
- `.codex/environments/` bleibt außerhalb des Commits.
- Kein Push/Merge in diesem Block; GitHub-PRs/Actions hier nicht neu abgefragt.
- Nächster Schritt: eigenen typisierten Abbildungsdatensatz mit expliziter Quell-/Zieldomäne und Prüfpflichten entwerfen, bevor Frame-Warnungen aufgehoben werden.

## Voriger Stand

Gesamtinventar: 2468 Aussagen aus 61 Dateien, Rohimporte mit offenen Prüfpflichten.
Koide-Zweig: vier Selbstprüfungen, originale Beweise, sechs offene native Guards.
Die frühere lange Übergabe ist unter
`notes/research/qam_store_handoff_history_2026_11_11.md` erhalten.
OP1–OP5 und sonstige offene physikalische Identifikationen bleiben unverändert offen.
