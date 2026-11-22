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

1. **Copilot in the cloud** (früher „Coding Agent“). Stand 22.11.2026:
   - **Lizenz fehlt:** Aufgaben an Copilot zuweisen verlangt Copilot Pro, Pro+, Business oder Enterprise. Das Konto des Autors hat
     keine dieser Lizenzen; die Zuweisung von Issue #231 scheiterte mit „Copilot agent is not enabled in this repository“. Bis eine
     Lizenz da ist, arbeiten Claude oder Codex die Release-Vorlagen ab.
   - Freischaltung (mit Lizenz): Profilbild → Copilot settings → Cloud agent → Policies → Repository access
     (https://github.com/settings/copilot/coding_agent).
   - Firewall: Repository → Settings → „Code, planning, and automation“ → Copilot → Internet access → „Custom allowlist“ mit
     `zenodo.org`, `doi.org`, `ctan.org`, `mirrors.ctan.org`. Vom Autor am 22.11.2026 eingestellt.
   - „Require approval for workflow runs“ (Copilot-Einstellungen): vom Autor am 22.11.2026 ausgeschaltet. Ausgleich: Der
     Hauptassistent weist Copilot nur selbst geschriebene Issues zu und prüft bei jedem Copilot-PR zuerst Änderungen unter
     `.github/workflows/`.
   - „Allow Copilot to approve pull requests“: aus lassen; betrifft Review-Freigaben, nicht Workflow-Läufe.
   - „Approval for running fork pull request workflows from contributors“ (Settings → Actions → General): bleibt auf
     „first-time contributors“; betrifft nur Fork-PRs Fremder.
2. **Zweige nach Merge automatisch löschen:** am 22.11.2026 per API eingeschaltet (`delete_branch_on_merge`).
3. **Labels** `release` und `copilot`: am 22.11.2026 angelegt, nichts zu tun.
4. **Ruleset für `main`** „main: no deletion, no force push“ (ID 27827305): am 22.11.2026 per API angelegt, nur Lösch- und
   Force-Push-Sperre; normale Pushes und Merges laufen wie bisher.

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
Ohne Copilot-Lizenz übernimmt der Hauptassistent (oder Codex) die Schritte 1–4 selbst, mit denselben Vorlagen als Checkliste.

5. Upload und Veröffentlichung nach Freigabe im Chat durch den Hauptassistenten. Die Vorschau auf Zenodo prüft der Hauptassistent
   über die API und meldet sie; Tag, GitHub-Release, Register #17 und OP-Issues zieht er nach `zenodo-release.md` nach.
