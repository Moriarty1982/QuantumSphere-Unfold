# Das Rechenmodell des Companion ausprobieren

Dieses Beispiel setzt die Rollen aus Abschnitt 19K–19L in einer binären Bandmaschine um. Der Zustand besteht aus Band, Kopfposition und endlicher Steuerung. Pro Schritt wählt das Paar aus Steuerzustand und gelesenem Bit einen Eintrag der Übergangstabelle. Der Eintrag legt Schreibbit, Kopfbewegung und Folgezustand fest. Als Beispiel wandelt die Maschine die erste Null hinter einer Folge von Einsen in eine Eins um und hält dann.

## Starten

Vom Stammverzeichnis des Repositorys mit Wolfram Engine beziehungsweise Python 3 und Qiskit 2.x:

```powershell
wolframscript -file qam/examples/zuse_machine/machine.wls
python qam/examples/zuse_machine/machine_qiskit.py
```

Für beide Aufrufe lässt sich der Pfad zu einer eigenen JSON-Datei anhängen. [machine.json](machine.json) zeigt das Format. Verwende ein nichtleeres Band aus Bits, eindeutige Zustandsnamen, einen Haltzustand ohne ausgehende Regeln und höchstens eine Regel je Zustand und Lesebit. Adressen beginnen bei null. `move` erlaubt −1, 0 und +1. `steps` begrenzt die ausgeführten Schritte. Die JSON-Ausgabe enthält den Startzustand und jeden ausgeführten Schritt. `stuck` bedeutet, dass eine Regel fehlt. `boundary` verwirft den ganzen Schritt, einschließlich eines vorgesehenen Schreibvorgangs.

Im Mathematica-Notebook lassen sich die Funktionen direkt laden. Die Pfade im Beispiel gehen vom Stammverzeichnis des Repositorys aus.

```wolfram
Get["qam/examples/zuse_machine/machine.wls"];
program = Import["qam/examples/zuse_machine/machine.json", "RawJSON"];
ZuseTrace[program, Last[program["examples"]], True]
```

Mit `True` hängt Wolfram bei Bedarf rechts eine Nullzelle an und arbeitet mit derselben Übergangstabelle weiter. Links bleibt die Grenze bei Adresse null. Mit `False` ist das Band fest.

Qiskit baut für jede Bandlänge eine reversible Einzelschrittschaltung. Alle Entscheidungsfälle stehen in der Schaltung, wirksam wird nur der Fall mit passendem Zustand, Kopf und Lesebit. Die Schaltung erhält die Eingabe und XOR-verknüpft das Ergebnis mit einem separaten Register. `FiniteBand(program, cells).circuit` liefert die Schaltung für eigene Experimente. Der Python-Treiber liest das Ergebnis jedes Schritts aus und verwendet es als Basiszustand für den nächsten Schritt. Der Statevector-Beispiellauf ist auf 18 Qubits begrenzt.

## Mit QAM, MML und MMA rechnen

Für den Abgleich beider Steuerungen mit MMA gibt es einen
[SystemVerilog-Testbench mit automatisch erzeugtem Laufbericht](hdl/README.md).

```powershell
python -m qam.tools.readout_db mma qam/examples/zuse_machine/mma_context.json qam/examples/zuse_machine/run_tape_mml.json --summary
```

Für eigene Rechnungen kopiere [den QAM-Kontext](mma_context.json) und [den MML-Auftrag](run_tape_mml.json). Der QAM-Operator deklariert `states`, `halt` und `rules`. Der QAM-Startzustand deklariert `tape`, `head` und `state`. `RUN_TAPE` referenziert die Namen beider Objekte und setzt Bandmodus, Schritt- und Zellgrenze sowie die optionale Ablaufspur. MMA prüft die deklarierten Guards und speichert das Ergebnis in der lokalen QAM-Datenbank.

`halted` bedeutet regulären Halt, `stuck` eine fehlende Regel und `boundary` einen versuchten Schritt über eine feste Bandgrenze. `step_limit` und `cell_limit` markieren das ausgeschöpfte Rechenbudget. Ein Lauf kann mit den Feldern `tape`, `head` und `state` als neuem QAM-Startzustand und größerem Budget fortgesetzt werden. `mma_status: continue` besagt, dass MMA den Auftrag ausführen durfte. Die Entscheidung der Bandmaschine steht unter `stop`.

```powershell
python -m qam.tools.readout_db receipt RECEIPT_HASH --replay
```

Die binäre Übergangstabelle und das Bandwachstum sind Modellentscheidungen. Die Identifikation des spinoriellen Trägers und der HC-Rückkehr aus 19K–19L bleibt eine Voraussetzung des Companion. Die Läufe prüfen die ausführbare Übergangssemantik im Beispiel. [Laufprotokoll](verification.md) · [Abschnitte 19K–19L](../../../sources/research/parts/v470/24_computational_specification.tex#L63)
