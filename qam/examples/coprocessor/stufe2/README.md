# Quanten-Coprozessor, Baustufe 2 als Software-Referenz (Band mit Drehung, Messung im Lauf, Schleife)

Stand 27.11.2026. Diese Stufe ist **Software** (Python, Dichtematrix in Gleitkomma), kein HDL und nicht exakt im Sinn der Stufe 0.
Sie legt Bandformat und Semantik für die Steuerbefehle des [Bauplans](../../../../notes/quanten_coprozessor/Bauplan.md) fest (Abschnitt 3a:
`MEASURE`, `JUMP_IF`, `LOOP`/`RETURN`, `HALT`) und ergänzt, was die Schleifenrechnungen brauchen: einen Drehbefehl, die Rückführung über
Register, den Wechsel des Trägerbands und einen Rauschbefehl. Die Stufe 1 (Band als Eingabe in HDL) ist damit nicht ersetzt.

| Datei | Inhalt |
|---|---|
| [`qtape.py`](qtape.py) | die Maschine (`QTape`), Befehlssatz im Kopfkommentar, Primzahl-Rauschgenerator (`PrimeNoise`) |
| [`baender/`](baender) | Bänder (Programme) als Textdateien |
| [`check.py`](check.py), [`check_out.txt`](check_out.txt) | Abnahme: Bausteine gegen Qiskit, Schleife L3 aus k395, Guards, Messung, Rauschgenerator |
| `l3_schleife_protokoll.jsonl` | vollständiges Protokoll eines Laufs (eine Zeile je ausgeführter Zelle) |

```sh
python -m qam.examples.coprocessor.stufe2.check > qam/examples/coprocessor/stufe2/check_out.txt
```

**Zustand.** Eine Menge von Bändern k = 0, 1, 2, …; Band k trägt einen Spin j = k/2 (symmetrischer Zustand aus k Qubits). Band 1 ist das
Dublett der Feldzustände. Ein Wechsel des Trägerbands ist `ADD` (ein Qubit ankoppeln, Gesamtspin messen: k → k ± 1 nach Clebsch-Gordan)
oder `DROP` (ein Qubit abgeben: k → k − 1).

**Protokoll.** Je ausgeführter Zelle eine Zeile: Schritt, Kopfposition, Zelle, was getan wurde, **warum** (welche Regel griff), Polarisation b,
Gewichte der Bänder, fortlaufender SHA-512-Hash über die ausgeführten Zellen. Gleiches Band und gleicher Startwert geben denselben Hash.

**Status und Stopgründe** wie bei MMA und `RUN_TAPE`: `continue`, `guard`, `reject`; `halted`, `boundary`, `step_limit`, `guard`, `reject`.

**Rauschen.** `NOISE reg modus eps` ändert ein Register um eps mal einen Rauschwert. Modi: `prime_gap` (die Primzahlen der Reihe nach;
Wert = normierte Lücke (p′ − p)/ln p′ − 1), `prime_mod<m>` (p mod m, auf ±½ gebracht), `random` (Zufallszahl mit festem Startwert, als
Vergleich). Die Primzahlfolge ist deterministisch (Sieb); der Wert an jeder Stelle ist exakt berechenbar, mit oder ohne Riemann-Vermutung.

**Abnahme (27.11.2026):** alle Prüfungen bestanden. `DROP`, `ADD`, `ROT` stimmen für k = 1 bis 4 mit expliziten Qubit-Rechnungen in Qiskit
überein (Abweichung ≤ 5·10⁻¹⁶); die Schleife L3 läuft auf dem Band und landet bei b = ½ mit dem Verlauf der geschlossenen Form; sechs
Guard-Fälle; Messung mit Zufall (Stichprobe aus 4000 Läufen).

**Grenzen.** Kein HDL, keine Synthese, kein MML-Auftrag `RUN_QTAPE`, kein MMA-Beleg. Gleitkomma. Die Maschine rechnet, was auf dem Band
steht; welche Regeln auf dem Band stehen, ist Sache der jeweiligen Notiz.
