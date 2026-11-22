# Hinweise für GitHub Copilot

Verbindlich sind `AGENTS.md` und die Abläufe unter `notes/anleitungen/`. Diese Datei fasst zusammen, was für Copilot-Aufträge
in diesem Repository am häufigsten zählt.

## Grenzen
- Du lieferst einen Draft-PR. Merges, Tags, GitHub-Releases und jede neue öffentliche Version entscheidet der Autor.
- Zenodo-Schritte (Reservierung, Upload, Veröffentlichung) startest du nicht. Du darfst Metadaten vorbereiten und den lokalen
  Trockenlauf `python tools/zenodo_publish.py … --dry-run` ausführen.
- Wolfram- und MMA-Rechnungen kannst du nicht ausführen. Neue Rechnungen nur, wenn der Auftrag ein Werkzeug nennt, das hier läuft.
- Keine neue H-Nummer und kein Test ohne committete Vorab-Notiz (`notes/anleitungen/hypothese-testen.md`).

## Inhalt
- **Append-only:** bestehende Runden in `sources/research/parts/v4100-post-release-layers.tex` nie umschreiben; Korrekturen kommen in
  eine neue Runde. Format: `notes/anleitungen/qsc-runde-einbauen.md`, Vorlage ist die jeweils letzte Runde.
- **Ehrlicher Status:** OP1–OP5, C5 und C6/T2 sind offen. Kein Text darf sie als geschlossen darstellen. Steht ein Ergebnis vor der
  Rechnung analytisch fest, heißt es „nicht blind“; nachträglich Gefundenes wird als nachträglich markiert.
- **Nur belegte Aussagen:** Jede neue Aussage in Runde, Paper oder Wiki muss auf eine Notiz oder ein Ergebnis im Repo verweisen.
- **Wiki im selben PR:** `notes/anleitungen/wiki-nachziehen.md`. Vor jeder Übergabe auch Physik-Paper und deutschen Preprint
  (`paper/preprint-de/`) prüfen.

## Prüfungen vor dem PR
- Guard-Linter auf neue Rundentexte: `python tools/qs.py guards <datei> --start <zeile>` (Ziel: 0 Kandidaten).
- Editionstests: `python -m unittest qam.store.test_editions`. Der Befehlskatalog der Editionen kennt nicht jeden TeX-Befehl
  (`\cot` z. B. nicht, stattdessen `\operatorname{cot}`).
- Gemeinsamer Bau: `python -m qam.tools.build_v5_documents --out build/<neuer-ordner>`; in `build-manifest.json` müssen undefinierte
  Verweise, doppelte Labels, Rerun-Meldungen und Overfull-Boxen 0 sein.
- Deutscher Preprint: in `paper/preprint-de/` dreimal
  `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build article.tex`.

## Form
- Neue Dateien mit LF-Zeilenenden. Keine festen absoluten Pfade in Skripten.
- Englische PR-Titel; im PR-Text Inhalt, Dateien und Prüfzahlen, offene Punkte und den nächsten Freigabepunkt.
