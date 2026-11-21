# Laufprotokoll vom 21. November 2026

Wolfram Language Kernel über den Evaluator. Die Definitionen aus `machine.wls` wurden mit dem Inhalt aus `machine.json` ausgeführt. Der lokale `wolframscript`-Starter war in der Testumgebung nicht verfügbar. Der Evaluator meldete beim Einlesen `Symbol::undefined2` für die im selben Lauf definierten Symbole. Die vier `Print`-Ausgaben waren vollständig.

```jsonl
{"example":"room","mode":"fixed","trace":[{"tape":[1,1,0],"head":0,"state":"scan","status":"running"},{"tape":[1,1,0],"head":1,"state":"scan","status":"running"},{"tape":[1,1,0],"head":2,"state":"scan","status":"running"},{"tape":[1,1,1],"head":2,"state":"halt","status":"halted"}]}
{"example":"edge","mode":"fixed","trace":[{"tape":[1,1],"head":0,"state":"scan","status":"running"},{"tape":[1,1],"head":1,"state":"scan","status":"running"},{"tape":[1,1],"head":1,"state":"scan","status":"boundary"}]}
{"example":"room","mode":"grow","trace":[{"tape":[1,1,0],"head":0,"state":"scan","status":"running"},{"tape":[1,1,0],"head":1,"state":"scan","status":"running"},{"tape":[1,1,0],"head":2,"state":"scan","status":"running"},{"tape":[1,1,1],"head":2,"state":"halt","status":"halted"}]}
{"example":"edge","mode":"grow","trace":[{"tape":[1,1],"head":0,"state":"scan","status":"running"},{"tape":[1,1],"head":1,"state":"scan","status":"running"},{"tape":[1,1,0],"head":2,"state":"scan","status":"running"},{"tape":[1,1,1],"head":2,"state":"halt","status":"halted"}]}
```

Qiskit 2.6.2 gab für die beiden Fälle mit `"mode":"fixed"` dieselben JSON-Zeilen aus. Ein zusätzlicher Abgleich verwendete alle 24 Startkombinationen aus vier Zweibitbändern, zwei Kopfpositionen und den Zuständen `a`, `b` und `halt`. Die Tabelle überschrieb bei `a/0` die Null und bewegte den Kopf nach links zu `b`, bei `a/1` die Eins und bewegte ihn nach rechts zu `b`, und schrieb bei `b/0` eine Eins mit Übergang zu `halt`. Für `b/1` fehlte die Regel. Der Lauf war pro Kombination auf drei Schritte begrenzt.

```text
24 two-cell traces match Wolfram Language.
Statuses: ['boundary', 'halted', 'running', 'stuck']
The circuit and its inverse recover the two-component input superposition.
```

## MML und MMA

Beide Modi liefen über `python -m qam.tools.readout_db mma` mit dem QAM-Beispielkontext und wurden in `build/qam.sqlite3` abgelegt. Die vollständigen MMA-Spuren stimmten mit der Ausgabe des Wolfram-Kernels überein. Der feste Lauf stimmte zusätzlich mit dem Qiskit-Statevector-Lauf überein. Der CLI-Replay verglich Ergebnis und Beleg einschließlich Hash.

```jsonl
{"receipt_hash":"346ca46bd934c6f920c3a2ba766367431ee521bbe5a6eb376ef9736d58d88f13a679b9d15b36f1c696cf30e21990e19e88dd867e181ca2740be0d489d20f5d8b","instruction":"RUN_TAPE","mma_status":"continue","errors":[],"obligations":[],"declared_guards":{},"mode":"fixed","steps":2,"stop":"boundary","final":{"tape":[1,1],"head":1,"state":"scan","status":"boundary"},"replay":{"receipt_matches":true,"result_matches":true,"current_receipt_hash":"346ca46bd934c6f920c3a2ba766367431ee521bbe5a6eb376ef9736d58d88f13a679b9d15b36f1c696cf30e21990e19e88dd867e181ca2740be0d489d20f5d8b","changed_fields":[]}}
{"receipt_hash":"f57db2d03c09e889f9bc02cda1bb632ed07860492e3a3f4e71690acb8266aa0517fcd26d9c09733b7c165cf6a6abe9083d2ea2e99b2063a5bcb7a3e07f9b2e08","instruction":"RUN_TAPE","mma_status":"continue","errors":[],"obligations":[],"declared_guards":{},"mode":"grow","steps":3,"stop":"halted","final":{"tape":[1,1,1],"head":2,"state":"halt","status":"halted"},"replay":{"receipt_matches":true,"result_matches":true,"current_receipt_hash":"f57db2d03c09e889f9bc02cda1bb632ed07860492e3a3f4e71690acb8266aa0517fcd26d9c09733b7c165cf6a6abe9083d2ea2e99b2063a5bcb7a3e07f9b2e08","changed_fields":[]}}
```

Die fünf neuen Integrationstests und die 17 bestehenden Tests der Framework-Schnittstelle liefen erfolgreich.
