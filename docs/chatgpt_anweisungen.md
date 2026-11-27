# Anweisungen für ChatGPT/Codex (lokal)

Codex liest `AGENTS.md` im Repo-Wurzelverzeichnis automatisch, sobald es im lokalen Klon gestartet wird
(vorher `git pull` auf `main`). Für die ChatGPT-App (Einstellungen → Personalisierung → Eigene Anweisungen)
den folgenden Text einfügen:

```
Ich arbeite an „Quantum Sphaera“ (Repo QuantumSphere-Unfold, lokaler Klon). Antworte auf Deutsch.
Verbindlich sind AGENTS.md und notes/anleitungen/ im Repo; bei Konflikt gelten sie.
Kernregeln:
- Jeder Test HNN bekommt vor der Rechnung eine Vorab-Notiz (Kriterium, Vorwissen geprüft), committet. Ohne Vorab-Notiz heißt es „Erkundung“.
- Nächste freie H-/k-Nummer vor Vergabe gegen origin/main prüfen.
- Rechnung in Python, Gegenprobe in Wolfram; Ausgaben mit ablegen.
- Hergeleitetes offen von Gesetztem/Angepasstem/Nachträglichem trennen. Offene Probleme nie als geschlossen darstellen.
- Trägt eine Vermutung nicht: Eingaben einzeln per Stichprobe prüfen, dann variieren.
- Vor „von Daten disfavorisiert“ prüfen, ob in den Materie-Frame übertragen.
- Offene Vorzeichen folgen aus der Feldgleichung, nicht setzen.
- Namen: Ruheframe R, Materie-Frame M, Dual-Frame T, Lichtpunkt P.
- Runden append-only; Inhalte über Zweig und PR, laufend pushen; bei grüner CI mergen.
- Zenodo-Schritte und neue Versionen nur mit meiner Freigabe (nur deposition_id, Vorschau prüfen).
- Schwere Herleitungen mit dem stärksten Modell, Routine mit kleinerem.
```
