# Aussagen-Datenbank und LLM-Kontext für Zenodo vorbereiten

Diese Reihenfolge gilt für jede neue Zenodo-Veröffentlichung des Quantum Sphaera Companion.

1. Zuerst das Datenbankschema der Aussagen-Datenbank für den aktuellen Forschungsstand aktualisieren und die Migration prüfen. [QAM-Datenbank](../../qam/store/README.md)
2. Danach die Einträge im aktualisierten Schema auf den aktuellen Forschungsstand bringen. Aussagenstatus, Belege und offene Guards mit dem vorgesehenen Quellstand abgleichen.
3. Nach der Aktualisierung der Einträge die [LLM-Kontextanleitung](llm-cache-optimieren.md#abgleich-vor-dem-zenodo-release) mit demselben Quellstand abgleichen. Geänderte Einstiegspunkte, Datenbankabfragen und Belegverweise nachziehen und die Links prüfen.
4. Erst danach die Editionen für das Release zusammenstellen und den Kandidaten bauen.
