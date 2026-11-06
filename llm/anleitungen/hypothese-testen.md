# Anleitung: eine Hypothese HNN testen

Werkzeugunabhängig. Gilt für jeden Test mit Entscheidungskriterium, auch außerhalb von OP5. Maßgeblich bleiben die Regeln
in `AGENTS.md`; bei OP5 zusätzlich `op5-vergleichsmodell-rechnen.md`.

## 1. Nummer und Vorwissen
1. **Freie H-Nummer:** in `llm/Uebergabe.md` steht „Zuletzt vergebene Hypothese“. Gegenprüfen:
   `ls llm notes/research/predictions 2>/dev/null | grep -oE 'H[0-9]+' | sort -V | tail -3`
   (auch Erkundungsnotizen durchsuchen). Nie eine Nummer doppelt vergeben.
2. **Vorwissen-Pflicht** – vor dem Schreiben suchen, mit Schlüsselbegriffen der Frage:
   - `grep -ril '<begriff>' llm/Ergebnis_* llm/Erkundung_* llm/Vorab_Notiz_* llm/k*.py analysis/OP5_* notes/research/predictions/`
   - bei OP5 den Abschnitt „Bereits beantwortet“ der OP5-Anleitung;
   - `wiki/Gesamtbild.md` (GitHub): welche These T1–T15 wird berührt?
   - externe Literatur nur, wenn ein Literatur-Werkzeug verbunden ist; sonst als „aus Vorwissen, ungeprüft“ kennzeichnen.
3. Ist die Frage schon beantwortet: dem Autor die Fundstelle nennen und **nicht** neu vorschlagen.
4. `llm/Zurueckgestellte_Ideen.md` (GitHub: `notes/research/v4_10_0_w1/`): trifft ein Auslöser zu, dem Autor die Idee als
   möglichen Ausweg nennen, nicht still umsetzen.

## 2. Vorab-Notiz `llm/Vorab_Notiz_HNN_<Thema>.md`
Aufbau (wie H86):
```
# Vorab-Notiz HNN: <Titel>
**Stand:** <Datum>, vor der Rechnung festgelegt. <blind | nicht blind | teilweise nicht blind | nachträglich motiviert – mit Grund>. <Autorzitat mit Uhrzeit, falls Anlass>
## Vorwissen geprüft
<Fundstellen mit Kurzbefund>
## Aufbau
<Gleichungen, Parameter, Einstellungen, Skriptname kNNN>
## Hypothesen und Kriterien
- **HNNa (...):** <messbares Kriterium mit Schranke>
- **Kontrolle:** <Kontrollgröße und Schranke>
## Folge, vorab festgelegt
<was aus Bestätigung/Widerlegung folgt und was nicht>
```
Regeln:
- Steht das Ergebnis analytisch schon fest oder stammen die Hypothesen aus bereits gesehenen Daten: **„nicht blind“**
  offen sagen und an neuen Einstellungen prüfen.
- Kontrollschranken nicht unter den numerischen Boden legen (~1e-11), nie nachträglich lockern.
- Commit **vor** der Rechnung: `git add llm/Vorab_Notiz_HNN_* && git commit -m "HNN vorab festgelegt (...)"`.
  Commit-Hash notieren. Kann das Modell nicht committen, hält der Autor den Commit vor der Rechnung fest; ohne Commit
  heißt die Rechnung „Erkundung“.

## 3. Rechnen
- Skript `llm/kNNN_<thema>.py` (nächste freie k-Nummer), Ausgabe `llm/kNNN_out.json`. Keine festen absoluten Pfade. Nur
  kurze Zusammenfassung ausgeben.
- Schwere Läufe im Hintergrund oder auf GitHub-Runnern (`rechnen/**`-Branch, `ci/…/auftrag.txt`); Details in der
  OP5-Anleitung. Rechenwerkzeuge des jeweiligen Modells (z. B. Wolfram, Code-Interpreter) sind erlaubt; Skript und
  Ausgabe kommen trotzdem als Datei ins Repo.
- Wird ein Kriterium nach einem Vorlauf geändert: datierter Nachtrag in der Vorab-Notiz **vor** dem nächsten Lauf, Lauf
  als „nicht blind“ markieren. Unbrauchbare Läufe offenlegen, nicht verschweigen.

## 4. Ergebnis-Notiz `llm/Ergebnis_HNN_<Thema>.md`
```
# Ergebnis HNN: <Ergebnis in einem Satz>
**<Datum>. Vorab-Notiz `...` (Commit <hash>). Skript `kNNN_...py`, Ausgabe `kNNN_out.json`. Status: HNNa bestätigt/widerlegt/ungültig nach Kriterium, ...**
## Kontrollen
## Ergebnis (Tabelle: Teil | Messwert | Kriterium | Entscheidung)
## Warum es scheitert / trägt
## Lesart
<nur was das Kriterium hergibt; Nachträgliches als „nachträglich“ markieren; nächste Frage nur mit neuer Vorab-Notiz>
```
Commit: `HNN bestaetigt|widerlegt: <Kurzinhalt>`.

## 5. Nachtragen
- `llm/Uebergabe.md`: HNN-Zeile (Vorab-Hash, blind/nicht blind, kNNN, Befund, „Noch nicht auf GitHub: … → Runde rNN“);
  zuletzt vergebene Nummer.
- Beim nächsten Rundeneinbau (`qsc-runde-einbauen.md`) wandern Vorab- und Ergebnis-Notiz nach
  `notes/research/predictions/`, und `notes/research/predictions/README.md` bekommt den Status; Wiki
  `Vorhersagen-und-Tests.md` (`wiki-nachziehen.md`).
- Dem Autor drei Zeilen: Befund je Teil, was offen bleibt, mögliche nächste Frage (ohne sie schon zu rechnen).
