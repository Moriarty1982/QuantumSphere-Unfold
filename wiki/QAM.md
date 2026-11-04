# QAM – Buchführungsprüfung für Forschungstexte

Die QAM ist eine kleine typisierte Buchführungssprache für lange Forschungstexte, mit oder ohne Sprachmodelle. Sie hängt **nicht** am Projekt Quantum Sphaera; das Projekt ist nur ihre erste Fallstudie. Ausführlich: Methodenpapier `paper/qam/` (Entwurf, 12 Seiten, nur Zenodo).

## Drei Fehler, drei Regeln

| Fehler | Regel | TeX (`qam.sty`) | Lean (`QSFormal.Provenance`) |
|---|---|---|---|
| **Beförderung**: eine bedingte oder gerechnete Aussage wird als bewiesen behandelt | eine Folgerung hat höchstens den Status ihrer schwächsten Prämisse | Fehler bei `\qamderive`, `\qamconvert` | `no_promotion`, `proved_only_from_proved` |
| **Eingabe als Ergebnis**: ein von Hand eingesetzter Wert wird später als hergeleitet zitiert | jede Aussage trägt die Eingaben mit, auf denen sie beruht; keine geht verloren, keine wird erfunden | Fehler bei `\qamindependent` | `inputs_tracked`, `inputs_sourced`, `independent_iff` |
| **Frame-Vermischung**: Größen verschiedener Frames werden verglichen oder verknüpft | nur innerhalb eines Frames verknüpfen und vergleichen; Frame-Wechsel nur über eine erklärte Abbildung | Fehler bei `\qamderive`, `\qamcompare`, `\qamconvert` | `frames_declared`, `no_maps_same_frame` |

Statusordnung: `open < reading < conditional < computed < proved`. Zusätzlich lehnt das TeX-Paket Schlüssel ab, die vor ihrer Erklärung benutzt oder doppelt erklärt werden (der Text ist append-only).

## Prüfung beim Kompilieren

Das LaTeX-Paket `qam/tex/qam.sty` lässt den TeX-Compiler beim ersten Regelverstoß mit einer Fehlermeldung anhalten (Option `mode=warning` nur Warnungen). Beispiel aus der Fallstudie, die Frame-Verschiebung β aus zwei Literaturwerten:

```latex
\qamframe{M} \qamframe{T} \qammap{G}{M}{T}
\qaminput{gamma}{M}{computed}               % zwei Literaturwerte, eingesetzt
\qamclaim{counting}{M}{proved}              % die Zählformel
\qamderive{beta}{computed}{gamma,counting}  % geht durch
\qamderive{beta2}{proved}{gamma,counting}   % hält an:
% ! Package qam Error: Promotion: `beta2' is declared `proved', but its weakest
% (qam)                premise `gamma' is only `computed'.
\qamindependent{beta}                       % hält an: beta beruht auf gamma
```

`\qamshow{beta}` setzt `[computed | frame M | inputs: gamma]`. Das Methodenpapier benutzt das Paket selbst. Tests (Dokumente, die durchlaufen müssen, und solche, die mit einem bestimmten Fehler anhalten müssen): `sh qam/tex/tests/run_tests.sh`, Workflow `qam-tex.yml`.

## Automatisch erzeugte QAM-Schreibweise

Die Erklärungen enthalten alles, was die QAM-Schreibweise braucht; das Paket setzt sie selbst. Das optionale erste Argument ist das Symbol (`\qaminput[\gamma]{gamma}{M}{computed}` usw.). Dann liefert

- `\qam{gamma}` → `^M γ := R(w_γ), w_γ = ⟨6, γ⟩ [computed]` (Eingabe als Auslese eines Witness),
- `\qam{beta}` → `^M β ⇐ ^M γ, ^M κ, W = {w_γ} [computed]` (Prämissen und Witness-Menge),
- `\qam{betaT}` → `^T β' = ^T_M G ^M β, W = {w_γ} [conditional]` (Frame-Wechsel mit Quelle und Ziel),
- `\qam*{…}` ohne Status, `\qamledger` eine Tabelle aller Aussagen in Erklärungsreihenfolge.

Mit `\usepackage[export]{qam}` wird jede Aussage zusätzlich als Zeile in `\jobname.qam` geschrieben, z. B. `beta := derive(gamma,counting); frame M; status computed; inputs {gamma}`, lesbar für andere Werkzeuge. Weil nichts von Hand getippt wird, kann die Schreibweise nicht von den Erklärungen abweichen.

## Prüfung der exportierten Datei in Lean

`formal/QSFormal/QamFile.lean` liest eine `.qam`-Datei und prüft jede Zeile gegen den Stand davor; aufgerufen mit `cd formal && lake exe qamcheck ../qam/examples/example.qam`. Der Prüfer ist eine Lean-Funktion, und Lean beweist, was sein Erfolg bedeutet: jede hergeleitete Aussage ist neu, hat Prämissen, höchstens deren Status und deren Frame (`derive_sound`, `checked_no_promotion`), ihre Eingaben sind genau die der Prämissen; ein Frame-Wechsel nutzt eine erklärte Abbildung mit passender Quelle (`convert_sound`); Unabhängigkeit und Vergleiche stimmen (`indep_sound`, `compare_sound`). Die Prüfung ist unabhängig vom TeX-Paket: eine von Hand geänderte Datei (Beispiel `bad_inputs.qam`, eine Eingabe gelöscht) wird trotzdem abgelehnt. Nicht verifiziert ist nur das Einlesen der Textzeilen.

## Hash-Kette ab der Ausgangsthese

Ein Papier startet meist mit einer Ausgangsthese; jede weitere Aussage entsteht daraus durch weitere Schritte. `\qamthesis[\tau]{thesis}{M}{conditional}{Wortlaut}` erklärt die These, ihr Wortlaut geht in den Hash ein. Jede Aussage bekommt einen Hash: MD5 von `Art;Name;Frame;Status;Eingaben;Quellen;Wortlaut`, wobei *Quellen* die Hashes ihrer Prämissen sind. Eine hergeleitete Aussage nennt damit genau die Fassungen, aus denen sie stammt. Ändert sich ein Wort der These, ändern sich alle Hashes darunter; was nicht davon abhängt, behält seinen Hash (Beispiel `qam/examples/thesis.tex`: Eingabe und Zählung bleiben gleich, x und z ändern sich).

Geprüft wird unabhängig von TeX zweifach: `qam/tools/qamhash.py verify` rechnet jeden Hash nach, Lean (`qamcheck`) prüft die Verkettung (`link_derive_sound` u. a.). Für eine Veröffentlichung schreibt `qamhash.py manifest` die SHA-256-Summen von Quelle, PDF und `.qam` samt Record-Hash. Gleiche Hashes heißen gleicher Stand, nicht richtiger Inhalt.

**Grenze:** Geprüft wird nur, was erklärt ist, und eine Erklärung kann falsch sein. Ob `gamma` wirklich eine Eingabe ist, sagt der Autor, nicht das Paket. Die QAM sichert die Form, nicht den Inhalt.

## Was sonst in Lean bewiesen ist

- `QSFormal.QAM`: acht Objektarten (Zustand, Schicht, Operator, Auslese, Zweig, Schale, Witness, Tensor) sind disjunkt; Hilbert-Verschiebung exakt umkehrbar; zulässige Transportketten erhalten Abschlussklassen und verträgliche Auslesen.
- `QSFormal.Models`: die Axiome haben triviale Modelle – sie legen nicht fest, was zulässig ist.
- `QSFormal.Route`: Pfade über Frames bleiben zulässig; Schleifen ändern die Klasse nicht.
- `QSFormal.Store`, `StoreProgress`: die Speicher-Maschine verlässt nie einen zulässigen Zustand, bleibt nie hängen, weist ungültige Schritte ohne Nebenwirkung ab, protokolliert jeden Schritt und kann keine falsche Aussage zertifizieren.

Alles ohne `sorry`, in CI gebaut (`lean-build.yml`).
