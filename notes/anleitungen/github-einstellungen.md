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
| Umgebungen | nur `github-pages`; Zenodo-Lauf ohne Umgebung, Geheimnisse auf Repo-Ebene |
| Copilot-Einrichtung | fehlte bis zu diesem PR |

## Empfohlen, nach Nutzen geordnet

1. **Umgebung `zenodo` mit Pflichtprüfer** (Settings → Environments → New environment `zenodo`):
   - Required reviewers: der Autor; „Prevent self-review“ aus, damit der Autor selbst freigeben kann.
   - Deployment branches: „Selected branches“ mit `main` und `release/*`.
   - Die Geheimnisse `ZENODO_TOKEN` und `ZENODO_SANDBOX_TOKEN` hierher verschieben und auf Repo-Ebene löschen.
   - Wirkung: Der Workflow `zenodo_release.yml` (seit diesem PR `environment: zenodo`) wartet vor jedem Lauf auf den Klick des
     Autors. Kein Assistent kann ohne diese Freigabe reservieren, hochladen oder veröffentlichen. Auch Trockenläufe brauchen dann den
     Klick.

2. **Copilot Coding Agent für das Repo einschalten** (Settings → Copilot → Coding agent):
   - Zugang für dieses Repository erlauben.
   - Firewall: zusätzlich erlauben `zenodo.org`, `doi.org`, `ctan.org` und `mirrors.ctan.org`. PyPI und die Ubuntu-Paketquellen
     stehen in der Standardliste.
   - Optional: MCP-Server `qsc-qam` eintragen, damit Copilot QAM-Belege lesen kann (Startbefehl aus `mcp/README.md`).

3. **Ruleset für `main`** (Settings → Rules → Rulesets → New branch ruleset, Ziel `main`):
   - „Restrict deletions“ und „Block force pushes“ an.
   - „Require a pull request before merging“ an, mit **Bypass für Repository-Admins**. So bleiben die Buchführungs-Commits des
     Autors und seiner Assistenten direkt auf `main` möglich (Dauerauftrag vom 15.11.), alle anderen Änderungen gehen über PRs.
   - „Require status checks to pass“: `QAM TeX checks`, `QAM batch checks` und `paired-documents` (Dokumentbau, seit diesem PR auch
     auf PRs).

4. **Zweige nach Merge automatisch löschen** (Settings → General → Pull Requests → „Automatically delete head branches“ an). Das
   erledigt den Dauerauftrag vom 14.11. für GitHub-Zweige von selbst.

5. **Workflows auf Copilot-PRs:** GitHub verlangt für Workflows auf PRs des Coding Agents eine Freigabe („Approve and run
   workflows“). Das ist eine sinnvolle Sperre; beim Durchsehen des Draft-PRs einmal freigeben.

6. **Labels anlegen:** `release` und `copilot` (Issues → Labels). Die Issue-Vorlagen setzen sie; fehlen sie, entfallen sie still.

7. **Copilot Code Review** (optional, Settings → Rules → Ruleset → „Request pull request review from Copilot“): automatische
   Durchsicht jedes PRs. Ersetzt die fachliche Prüfung nicht.

## Nicht empfohlen

- `GITHUB_TOKEN` auf Schreiben stellen oder „Allow GitHub Actions to create and approve pull requests“ einschalten: Kein Ablauf
  braucht es, und es würde Freigaben umgehbar machen.
- Auto-Merge für Release-PRs: Merges bleiben eine Entscheidung des Autors.

## Ablauf mit Copilot (Kurzform)

1. Autor: Zielversion festlegen; Issue „Release 1: Runde schreiben“ anlegen und Copilot zuweisen.
2. Copilot: Draft-PR. Autor: Workflows freigeben, lesen, mergen.
3. Wie 1–2 mit „Release 2: Artikel nachziehen“ und „Release 3: Bau und Metadaten“.
4. Autor: Reservierung starten (Workflow `Zenodo Release`, `reserve_only=true`, `dry_run=false`) und in der Umgebung freigeben.
5. „Release 4: DOI eintragen“ an Copilot. Danach Upload, Vorschau-Prüfung und Veröffentlichung durch den Autor; Tag und
   GitHub-Release nach `zenodo-release.md`, Register #17 und OP-Issues nachziehen.
