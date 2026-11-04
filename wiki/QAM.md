# QAM – Buchführungsprüfung für Forschungstexte

Die QAM ist eine kleine typisierte Buchführungssprache für lange Forschungstexte, mit oder ohne Sprachmodelle. Sie hängt **nicht** am Projekt Quantum Sphaera; das Projekt ist nur ihre erste Fallstudie. Ausführlich: Methodenpapier `paper/qam/` (Entwurf, 11 Seiten, nur Zenodo).

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

**Grenze:** Geprüft wird nur, was erklärt ist, und eine Erklärung kann falsch sein. Ob `gamma` wirklich eine Eingabe ist, sagt der Autor, nicht das Paket. Die QAM sichert die Form, nicht den Inhalt.

## Was sonst in Lean bewiesen ist

- `QSFormal.QAM`: acht Objektarten (Zustand, Schicht, Operator, Auslese, Zweig, Schale, Witness, Tensor) sind disjunkt; Hilbert-Verschiebung exakt umkehrbar; zulässige Transportketten erhalten Abschlussklassen und verträgliche Auslesen.
- `QSFormal.Models`: die Axiome haben triviale Modelle – sie legen nicht fest, was zulässig ist.
- `QSFormal.Route`: Pfade über Frames bleiben zulässig; Schleifen ändern die Klasse nicht.
- `QSFormal.Store`, `StoreProgress`: die Speicher-Maschine verlässt nie einen zulässigen Zustand, bleibt nie hängen, weist ungültige Schritte ohne Nebenwirkung ab, protokolliert jeden Schritt und kann keine falsche Aussage zertifizieren.

Alles ohne `sorry`, in CI gebaut (`lean-build.yml`).
