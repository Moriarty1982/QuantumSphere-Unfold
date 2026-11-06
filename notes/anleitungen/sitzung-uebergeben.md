# Anleitung: Sitzung übergeben

Werkzeugunabhängig. Gegenstück zu `weitermachen.md`. Auslöser: „Schluss für heute“, „übergeben“, „Übergabe schreiben“,
nach einem Merge, vor einer absehbaren Kontextverdichtung oder wenn ein Arbeitsblock abgeschlossen ist.
Datei: `llm/Uebergabe.md`. Sie muss für jedes Modell lesbar sein, also keine modellspezifischen Befehle als einzigen Weg.

## 1. Fakten einsammeln, nicht erinnern
- lokal: `git log --oneline -8`, `git status --short`, letzter eingebundener Commit (= nächste Bundle-Basis);
- GitHub: `gh pr list --state all -L 3`, `gh run list -L 3`, offene Branches `rechnen/**`, `research/**`;
- zuletzt vergebene H- und k-Nummer:
  `ls llm | grep -oE '^(Vorab_Notiz|Ergebnis)_H[0-9]+' | grep -oE 'H[0-9]+' | sort -V | tail -1` und
  `ls llm | grep -oE '^k[0-9]+' | sort -V | tail -1`;
- letzter Build: Seiten, Labels, Overfull, harte Werte, Guard-Linter;
- offene Autorentscheidungen und Arbeitsannahmen (mit Uhrzeit des Autorzitats).

## 2. Datei neu schreiben (überschreiben, nicht fortschreiben)
Ziel: **unter ~60 Zeilen**, damit der Einstieg wenig Token kostet. Geschichte gehört in `AGENTS.md`, Runden und
Ergebnis-Notizen, nicht hierher.

```
# Übergabe: Stand der letzten Sitzung
**Diese Datei wird am Ende jedes Arbeitsblocks überschrieben, nicht fortgeschrieben.** …

## Stand vom <Datum>, ca. <Uhrzeit> (<Modell>)
- **GitHub:** zuletzt gemergt PR #NN als <hash> (Runde rNN, Inhalt in einer Zeile); offene PRs; laufende Actions mit Run-ID.
- **Lokal:** letzter Commit, Build-Zahlen, **nächste Bundle-Basis: <hash>**.
- **Noch nicht auf GitHub:** HNN… (je eine Zeile: Vorab-Hash, blind/nicht blind, Befund, Datei) → kommt in Runde rNN+1.
- **Zuletzt vergebene Hypothese:** HNN (nächste frei HNN+1); letztes Skript kNNN.
- **Offene Autorentscheidungen / Arbeitsannahmen:** …
- **Ausgelöste Zurückgestellte Ideen:** I… (nur wenn neu)
- **Nächster Schritt:** <einer, konkret> · zur Wahl: <höchstens 4>
- **Aufräumen:** Branches, die weg können; Sperrdateien.

## Davor (<Uhrzeit>)
<nur der unmittelbar vorige Block, auf ≤ 5 Zeilen gekürzt>

## Inhaltlicher Stand
<≤ 6 Zeilen: was das Projekt gerade trägt, was offen ist>
```

Das Modell trägt sich in der Kopfzeile ein (z. B. „Claude Opus“, „ChatGPT“), damit die nächste Sitzung weiß, wer zuletzt
gearbeitet hat. Ältere „Davor“-Blöcke löschen: ihr Inhalt steht in den Runden und in der Rundentabelle von `AGENTS.md`.
Fehlt dort etwas, zuerst dort nachtragen, dann hier kürzen.

## 3. Abschließen
- Prüfen, dass jede Angabe aus Schritt 1 stammt (Hashes, Nummern, PRs).
- Lokal committen: `git add llm/Uebergabe.md && git commit -m "Uebergabe <Datum> <Uhrzeit>"`.
  Ohne Shell: den fertigen Text ausgeben und den Autor bitten, ihn zu speichern und zu committen.
- Dem Autor zwei Zeilen: wo es steht, was der nächste Schritt ist.
