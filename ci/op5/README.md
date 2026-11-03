# Parallele OP5-Rechnungen auf GitHub Actions

Der Workflow `.github/workflows/op5-parallel.yml` verteilt eine Rangrechnung auf mehrere Runner, **ein Job je Ordnung p**.
Jeder Runner hat 4 Kerne und 16 GB; die Jobs laufen gleichzeitig. Am Ende fasst ein Job alle Ergebnisse zu einer Tabelle
zusammen (Lauf-Zusammenfassung und Artefakt `op5-ergebnisse`).

## Starten
- **Push auf einen Branch `rechnen/<name>`**, der etwas unter `ci/op5/` ändert. Die Ordnungen stehen in `auftrag.txt`
  (z. B. `2-12` oder `7,9,11`).
- Sobald der Workflow auf `main` liegt, zusätzlich über *Actions → OP5 parallel → Run workflow* mit eigener Liste.

## Erste Nutzlast: `symbol_rang.py`
dim g_p (ungeeicht) und dim g'_p (ϑ-geeicht) des eingefrorenen Ω-Symbols aus `completion-omega-witness.npz`, aufgebaut
wie `balanced_spencer_check.py` und k137. Bekannt sind g_p für p = 2…10 (r71) und g'_p für p = 2…9 (k137, k148);
p = 11 und 12 sind neu. Das ist eine **Erkundung** auf dem älteren Keim (θ vom alten Keim), kein Test mit Vorab-Notiz.
Lokal: `python ci/op5/symbol_rang.py --p 7`.

## Neue Nutzlasten
Ein Skript, das genau einen Parameter nimmt (`--p`, später auch Primzahl, Punkt, Saat …) und ein JSON schreibt, lässt sich
in denselben Workflow hängen. Schwere Daten (z. B. hochgenaue Keime) gehören ins Repo oder als Release-Asset, damit
jeder Runner sie ohne Zugriff auf lokale Ordner bekommt.

## Grenzen
- Rechnen modulo Primzahlen ist nur bei exakten (rationalen) Eingaben sinnvoll. Die Keimdaten sind reelle Zahlen mit
  70–100 Stellen; gerundet hätte das Symbol den Rang am Nachbarpunkt, also den generischen Rang statt des Rangs am Keim.
- Ein Job darf höchstens 6 Stunden laufen.
