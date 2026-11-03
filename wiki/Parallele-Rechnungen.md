# Parallele Rechnungen auf GitHub

Große Rangrechnungen am OP5-Vergleichsmodell lassen sich auf mehrere GitHub-Runner verteilen. Der Workflow
[`op5-parallel.yml`](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/.github/workflows/op5-parallel.yml)
startet **einen Job je Ordnung p**; jeder Runner hat 4 Kerne und 16 GB, die Jobs laufen gleichzeitig. Ein letzter Job
fasst alles zu einer Tabelle zusammen (Lauf-Zusammenfassung unter *Actions*, Einzelergebnisse als Artefakt `op5-ergebnisse`).
Die Laufzeit bestimmt damit die größte Ordnung, nicht die Summe aller.

## Starten

- *Actions → OP5 parallel (Symbolränge) → Run workflow*, Feld „Ordnungen“ z. B. `2-12` oder `7,9,11`.
- Oder ein Push auf einen Branch `rechnen/<name>`, der etwas unter `ci/op5/` ändert; die Ordnungen stehen dann in
  `ci/op5/auftrag.txt`.

Wie neue Rechnungen eingehängt werden, steht in [`ci/op5/README.md`](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/ci/op5/README.md):
ein Skript, das genau einen Parameter nimmt und ein JSON schreibt; nötige Daten müssen im Repository liegen.

## Erster Lauf (3. November 2026, Erkundung)

Gerechnet wurde die Dimension der Symbolräume des eingefrorenen $\Omega$-Symbols (Datei `completion-omega-witness.npz`,
also $\Omega$ vom älteren Keim), ungeeicht ($g_p$) und mit der $\vartheta$-Eichung ($g'_p$), aufgebaut wie in r71 und k137.

| p | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $\dim g_p$ | 127 | 208 | 308 | 427 | 565 | 726 | 910 | 1118 | 1351 | **1610** | **1896** |
| $\dim g'_p$ | 117 | 188 | 273 | 371 | 481 | 606 | 745 | 898 | **1065** | **1246** | **1441** |

- Alle zuvor bekannten Werte (r71, k137, k148) wurden genau reproduziert; fett sind neue Werte.
- Für jedes p gilt $\dim g'_p = \dim g_p - \binom{p+3}{3}$: die Eichung nimmt genau eine Funktion von vier Variablen heraus.
- Beim geeichten Symbol sind die zweiten Differenzen ab $p = 7$ konstant 14. Das passt zu den 14 Funktionen von drei
  Variablen aus H51. Die neuen Werte bestätigen also das Bild bis $p = 12$.
- Alle Rangentscheidungen hatten eine Singulärwertlücke von mindestens $4\cdot 10^{7}$.
- Laufzeit des ganzen Laufs gut 9 Minuten, die größte Matrix (p = 12) hatte 12 323 × 10 920 Einträge und brauchte 3,2 GB.

Grenze: Das betrifft nur das eingefrorene Symbol des Vergleichsmodells, ohne die vier versteckten Bedingungen aus r73.
Es ist kein Test mit Vorab-Notiz. OP5 bleibt offen, die Guards sind unverändert.

## Was diese Parallelisierung nicht leistet

- Rechnen modulo Primzahlen ist nur bei exakten (rationalen) Eingaben sinnvoll. Die Keimdaten sind reelle Zahlen mit
  70–100 Stellen; gerundet hätte das Symbol den Rang an einem Nachbarpunkt, also den generischen Rang statt des Rangs am Keim.
- Die hochgenaue Kette (Ω und die vier Bedingungen mit 100 Stellen) lässt sich so verteilen, sobald ihre Eingaben im
  Repository liegen; die Genauigkeitsgrenze aus r74 löst die Parallelisierung allein nicht.
