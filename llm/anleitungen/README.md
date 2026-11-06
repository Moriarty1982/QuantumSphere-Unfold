# Anleitungen für alle Sprachmodelle

Dieser Ordner ist die **einzige Quelle** der Arbeitsabläufe im Projekt Quantum Sphaera. Er gilt für Claude, ChatGPT,
Codex und jedes andere Modell gleich. Werkzeugspezifische Hüllen (Claude-Skills unter `.claude/skills/`) verweisen nur
hierher und enthalten keine eigenen Regeln. Wer einen Ablauf ändert, ändert ihn **hier**.

Auf GitHub (`Moriarty1982/QuantumSphere-Unfold`) liegen dieselben Dateien unter `notes/anleitungen/`.

## Welche Anleitung wann

| Anlass | Anleitung |
|---|---|
| Neue Sitzung, „weitermachen“, „wo waren wir“ | `weitermachen.md` |
| Ende eines Arbeitsblocks, „übergeben“, vor einer Kontextverdichtung | `sitzung-uebergeben.md` |
| Ein Test HNN mit Entscheidungskriterium (Vorab-Notiz, Rechnung, Ergebnis) | `hypothese-testen.md` |
| Rechnung am OP5-Vergleichsmodell | `op5-vergleichsmodell-rechnen.md` (zusätzlich zu `hypothese-testen.md`) |
| Neue Runde v4.9.0-rNN schreiben und einbauen | `qsc-runde-einbauen.md` |
| Wiki im selben PR nachziehen | `wiki-nachziehen.md` |
| Querverweise, Theoremnummern, Guards, Ledger, Audit, Manifest | `qs-werkzeug.md` |
| Neue Version auf Zenodo veröffentlichen | `zenodo-release.md` |

Regeln, Rundenstand und Projektfakten stehen in `AGENTS.md`; der Stand der letzten Sitzung in `llm/Uebergabe.md`.

## Wie jedes Modell sie nutzt

- **Claude (Code, Desktop):** Die Skills `weitermachen`, `qs-sitzung-uebergeben`, `qs-hypothese-testen`,
  `qs-wiki-nachziehen`, `qsc-runde-einbauen`, `op5-vergleichsmodell-rechnen`, `quantum-sphaera` und `zenodo-release`
  laden die passende Datei aus diesem Ordner. `CLAUDE.md` verweist auf `AGENTS.md`.
- **Codex:** liest `AGENTS.md` automatisch; dort steht die Liste dieser Anleitungen.
- **ChatGPT (Projekt oder mit GitHub-Verbindung):** Zu Beginn eines Chats die Anleitung nennen oder anhängen. Bewährter
  Einstieg:

  > Lies `AGENTS.md`, `llm/Uebergabe.md` und `llm/anleitungen/weitermachen.md` und arbeite danach. Für jeden weiteren
  > Ablauf gilt die passende Datei aus `llm/anleitungen/` (Übersicht in `llm/anleitungen/README.md`).

  Ohne Dateizugriff: die genannten Dateien als Projektdateien hochladen. Ohne Shell nennt das Modell die Befehle,
  statt sie auszuführen, und der Autor führt sie aus.

## Schreibregeln für diese Anleitungen

- Keine Werkzeugnamen eines bestimmten Modells als Pflicht (z. B. „Grep-Tool“, „Unteragent“, „Write-Tool“). Stattdessen
  sagen, was zu tun ist; Modellspezifisches höchstens als Hinweis „(Claude: …)“.
- Pfade relativ zum Repo-Wurzelverzeichnis; keine festen absoluten Pfade.
- Befehle so, dass sie in einer POSIX-Shell (Git-Bash, Linux, macOS) laufen; Python als `python3` (unter Windows `python`).
- Freigaben nach außen (Merge, Zenodo, Veröffentlichen) bleiben beim Autor, gleich welches Modell arbeitet.
