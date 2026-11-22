# Arbeitsauftrag für ein LLM – Zenodo-Release vorbereiten

**Repository:** `Moriarty1982/QuantumSphere-Unfold`

Bereite für den Quantum Sphaera Companion einen technisch geprüften Release-Kandidaten vor. Dieser Arbeitsauftrag eignet sich für GitHub Copilot oder ein anderes LLM mit Repository-Zugriff. Liefere die Änderung in einem Draft-PR mit Prüfbericht ab, sobald der Autor eine konkrete Release-Vorbereitung beauftragt hat.

## Mit GitHub Copilot

Die Arbeit ist in vier Issue-Vorlagen geteilt („Release 1“ bis „Release 4“ unter `.github/ISSUE_TEMPLATE/`), je eine pro Draft-PR.
Copilots Umgebung (TeX Live, Python) richtet `.github/workflows/copilot-setup-steps.yml` ein; Regeln in `.github/copilot-instructions.md`.
Einstellungen, die der Autor auf GitHub setzt (Umgebung `zenodo` mit Pflichtprüfer, Ruleset für `main`, Firewall): [github-einstellungen.md](github-einstellungen.md).

## Eingaben und Quellen

- Übernimm Zielversion und freigegebenen Quellstand vom Autor. Ermittle Tag und Version-DOI der veröffentlichten Vorgängerversion aus dem Repository. Fehlen Zielversion oder Quellstand, prüfe die Ausgangslage und melde die offenen Angaben. [Projektregeln](../../AGENTS.md)
- Lies die verbindliche Release-Anleitung und den Ablauf für Aussagen-Datenbank und LLM-Kontext. Verwende für Prüfungen denselben Quellstand wie für das Paket. [Zenodo-Ablauf](zenodo-release.md) · [Datenbank und LLM-Kontext](zenodo-datenbank-vorbereiten.md)

## Arbeitsreihenfolge

1. **Schema.** Bringe das Schema der Aussagen-Datenbank auf den für den vereinbarten Forschungsstand benötigten Stand. Prüfe die Migration mit einem vorhandenen Bestand und die Neuinitialisierung. Halte Ausgangs- und Zielstand sowie Testergebnisse fest.
2. **Einträge.** Aktualisiere anschließend die Einträge aus dem freigegebenen Quellstand. Gleiche Quellverweise, Aussage- und Prüfstatus, Belege und offene Guards ab. Protokolliere den Snapshot oder die nachgewiesene Auswahl und ihren Hash.
3. **LLM-Kontext.** Prüfe danach die Kontextanleitung mit demselben Quellstand. Ziehe geänderte Einstiegspunkte, Datenbankabfragen und Belegverweise nach und teste die Links. [Abgleich vor dem Release](llm-cache-optimieren.md#abgleich-vor-dem-zenodo-release)
4. **Dokumente und Paket.** Baue beide englischen Ausgaben aus demselben Quellsnapshot. Stelle PDFs, Quellen, Aussagen-Datenbank, Zusammenstellungsmanifeste, Buildprotokolle und SHA‑256-Prüfsummen bereit. Prüfe Referenzen, Zitate, doppelte Labels und verbleibende Wiederholungsanforderungen des TeX-Builds. Führe Satzüberläufe zur Sichtprüfung auf. [Dokument-Build](../../qam/store/README.md)
5. **Metadaten und Trockenlauf.** Bereite Release-Notizen, `CITATION.cff`, Zenodo-Metadaten und die Dateiübersicht vor. Prüfe den Bezug zur Concept-DOI und zur Vorgängerversion. Markiere eine noch ausstehende Version-DOI im Bericht als offen. Verwende für den Reservierungs-Trockenlauf ausdrücklich `dry_run=true`. Nach der separat genehmigten Reservierung kannst du die zugewiesene DOI in Titel, Metadaten und Paket abgleichen und den Paket-Trockenlauf ausführen. [Metadaten und DOI-Prüfung](zenodo-release.md#1-metadaten)

## Abgabe im Draft-PR

Gib Zielversion, Quellcommit, Schemaversion und Snapshothash, Build- bzw. Actions-Links, Dateiliste und die Prüfsummenprüfung an. Nenne die tatsächlich ausgeführten Tests, verbleibende offene Guards, ausstehende Sichtprüfungen und den nächsten Freigabepunkt. Verwende den technischen Buildstatus als Nachweis für den Paketbau. Die fachliche und redaktionelle Freigabe dokumentiert der Autor separat.

## Freigaben des Autors

Die Entscheidung über eine neue öffentliche Version sowie ihre Zielversion und ihr Quellstand liegen beim Autor. Merge und Push auf `main`, Tag und GitHub-Release sowie **Zenodo-Reservierung, Upload und Veröffentlichung** brauchen je die entsprechende ausdrückliche Freigabe. Vor der Veröffentlichung prüft der Autor den Entwurf einschließlich Haupt-PDF als Vorschau. Bei einem Copilot-Draft-PR kann zusätzlich die Freigabe der GitHub-Actions-Läufe nötig sein. [Projektfreigaben](zenodo-release.md#freigaben--nie-ohne-ausdrückliches-wort-des-nutzers) · [Copilot-Prüfungen](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations)
