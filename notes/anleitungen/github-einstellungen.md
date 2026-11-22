# GitHub-Einstellungen für Releases mit Copilot und anderen Assistenten

Stand 22.11.2026, geprüft über die GitHub-API. Diese Einstellungen setzt der Autor in der GitHub-Oberfläche; die Dateien im Repo
(`.github/copilot-instructions.md`, `.github/workflows/copilot-setup-steps.yml`, `.github/ISSUE_TEMPLATE/release-*.yml`) sind schon da.

## Ausgangslage

| Einstellung | Wert heute |
|---|---|
| Schutz für `main` | keiner (kein Branch-Schutz, kein Ruleset) |
| Zweige nach Merge automatisch löschen | aus |
| Auto-Merge erlaubt | an |
| `GITHUB_TOKEN` Standardrechte | nur lesen; darf keine PRs genehmigen |
| Umgebungen | nur `github-pages`; Zenodo-Lauf ohne Umgebung, Geheimnisse auf Repo-Ebene (so beabsichtigt) |
| Copilot-Einrichtung | fehlte bis zu diesem PR |

## Leitlinie: einmal einrichten, danach ohne Eingriff

Der Autor will im laufenden Betrieb nicht in GitHub klicken müssen. Freigaben gibt er im Chat („PR NN mergen“, „Reservierung
freigeben“); die Assistenten führen sie aus. Deshalb gibt es **keine** Pflichtprüfer-Umgebung für Zenodo und keine Regeln, die
für jeden PR einen Klick verlangen. Die Grenze „Zenodo nur mit Freigabe“ bleibt eine Regel in `AGENTS.md`, keine technische Sperre;
die Zenodo-Schlüssel bleiben als Repo-Geheimnisse.

## Einmalig einzurichten

1. **Copilot Coding Agent für das Repo einschalten** (Settings → Copilot → Coding agent).
   - Falls angeboten: die Freigabepflicht für Workflow-Läufe auf Copilot-PRs ausschalten. Sonst wartet jeder Copilot-PR mit
     seinen Prüfungen auf einen Klick.
   - Firewall: `zenodo.org`, `doi.org`, `ctan.org`, `mirrors.ctan.org` erlauben.
2. **„Automatically delete head branches“** einschalten (Settings → General → Pull Requests). Erledigt den Dauerauftrag vom 14.11.
   auf GitHub ohne Zutun.
3. **Labels** `release` und `copilot`: am 22.11.2026 angelegt, nichts zu tun.
4. Optional, ohne laufenden Aufwand: **Ruleset für `main`** nur mit „Restrict deletions“ und „Block force pushes“. Das verhindert
   versehentliches Löschen oder Überschreiben von `main` und verlangt nie einen Klick.

## Bewusst nicht

- Umgebung mit Pflichtprüfer für Zenodo: würde jeden Lauf, auch Trockenläufe, an einen Klick binden.
- „Require a pull request“ oder Pflicht-Statusprüfungen für `main`: würde Übergabe-Commits blockieren bzw. Merges verzögern.
- Schreibrechte für `GITHUB_TOKEN` oder Auto-Merge für Release-PRs.

## Ablauf mit Copilot (Kurzform)

Der Autor sagt im Chat nur, was er will („v5.4.0 vorbereiten“, „freigeben“). Den Rest steuert der Hauptassistent:

1. Hauptassistent: Issue „Release 1: Runde schreiben“ anlegen und Copilot zuweisen; gleichzeitig „Release 2“ vorbereiten.
2. Copilot: Draft-PR. Hauptassistent: Prüfungen und Inhalt durchsehen, Fehler zurückmelden oder selbst korrigieren, dem Autor eine
   kurze Zusammenfassung geben. Merge nach „PR NN mergen“ im Chat.
3. Wie 1–2 mit „Release 2: Artikel nachziehen“ und „Release 3: Bau und Metadaten“.
4. Nach „Reservierung freigeben“ im Chat startet der Hauptassistent den Workflow `Zenodo Release` und legt „Release 4: DOI eintragen“
   für Copilot an.
5. Upload und Veröffentlichung nach Freigabe im Chat durch den Hauptassistenten. Die Vorschau auf Zenodo prüft der Hauptassistent
   über die API und meldet sie; Tag, GitHub-Release, Register #17 und OP-Issues zieht er nach `zenodo-release.md` nach.
