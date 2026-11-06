# Anleitung: weitermachen, wo die letzte Sitzung aufgehört hat

Werkzeugunabhängig. Auslöser: „weitermachen“, „mach weiter“, „wo waren wir“ oder der Start eines neuen Chats im Projekt.
Ziel: in wenigen Schritten den Stand rekonstruieren und mit dem nächsten Schritt beginnen, ohne aus Erinnerung oder
Zusammenfassungen zu raten. Gegenstück: `sitzung-uebergeben.md`.

## 1. Stand lesen, in dieser Reihenfolge
1. **`llm/Uebergabe.md`**: Stand der letzten Sitzung, offene Branches und PRs, zuletzt vergebene H-Nummer, nächster Schritt.
2. **`AGENTS.md`**: Regeln (Vorab-Notizen, Vorwissen-Pflicht, Merges nur nach „PR NN mergen“, Wiki im selben PR) und die
   letzte Zeile der Rundentabelle.
3. **Die einschlägige Anleitung** in diesem Ordner (Übersicht `README.md`), bei OP5 `op5-vergleichsmodell-rechnen.md` mit
   dem Abschnitt „Bereits beantwortet“.
4. **`llm/Zurueckgestellte_Ideen.md`**: Auslöser prüfen; trifft einer zu, die Idee dem Autor nennen.

## 2. Gegen die Wirklichkeit prüfen
Die Übergabe kann veraltet sein, etwa wenn ein anderes Modell weitergearbeitet hat. Deshalb kurz nachsehen:
- lokal `git log --oneline -5` und `git status --short`; Bundles `r*.bundle` sind erwartet;
- auf GitHub (`Moriarty1982/QuantumSphere-Unfold`), soweit erreichbar:
  - die letzten Commits auf `main`;
  - offene PRs (`gh pr list` oder `gh api repos/Moriarty1982/QuantumSphere-Unfold/pulls`);
  - Branches `rechnen/**` und `research/**` mit neueren Commits;
  - laufende oder fertige Actions-Läufe (`gh run list -L 5`).

Hat das Modell keine Shell oder keinen GitHub-Zugang: den Autor bitten, diese Befehle auszuführen und die Ausgabe
einzufügen. Frühere Chats nur bei Lücken heranziehen, wenn das Werkzeug dafür vorhanden ist. Repo und Übergabe gehen vor.

Wenn sich etwas widerspricht, gilt das Repo vor der Übergabe. Den Widerspruch nennen und nicht still übergehen.

## 3. Dem Autor kurz melden
Drei bis fünf Zeilen:
- der letzte Stand, mit gemergten Runden, offenen PRs und laufenden Rechnungen;
- der nächste Schritt laut Übergabe;
- was davon abweicht, falls etwas abweicht.

Dann mit dem nächsten Schritt beginnen. Nur fragen, wenn er eine Entscheidung des Autors braucht, etwa einen Merge oder
die Wahl eines Ansatzes.

## 4. Am Ende jedes Arbeitsblocks
`llm/Uebergabe.md` nach `sitzung-uebergeben.md` überschreiben und lokal committen.

## Fallstricke
- Nicht aus einer Kontextzusammenfassung weiterarbeiten, ohne die Übergabe und die Anleitung neu zu lesen.
- Schon beantwortete Fragen nicht erneut vorschlagen; dafür gibt es „Bereits beantwortet“ und die Vorwissen-Pflicht.
- Git-Lock-Dateien im synchronisierten Ordner (OneDrive): nur eigene `.lock`-Dateien entfernen.
