# Quanten-Coprozessor, Baustufe 0

Erste Baustufe des [Bauplans](../../../notes/quanten_coprozessor/Bauplan.md): eine exakte Zustandsvektor-Einheit für
zwei Qubits in SystemVerilog. Jede Amplitude ist $(c_0 + c_1\omega + c_2\omega^2 + c_3\omega^3)/\sqrt2^{\,k}$ mit
ganzzahligen $c_j$ und $\omega = e^{i\pi/4}$; $k$ gilt für den ganzen Zustand. Damit rechnet die Einheit alle
Clifford+T-Gatter ohne Rundung. Ein Gatter pro Takt; Status `continue`, `guard` (Überlauf der Wortbreite W) oder
`reject` (unbekannter Opcode) wie bei MMA.

| Datei | Inhalt |
|---|---|
| [`hdl/qstep2.sv`](hdl/qstep2.sv) | die Einheit, Opcodes `NOP X Z S SDG T TDG H CX` |
| [`hdl/qstep2_tb.sv`](hdl/qstep2_tb.sv) | Testbench, liest ein einfaches Befehlsband (`B`, `G op ziel`, `E`) |
| [`check.py`](check.py) | erzeugt Fälle, simuliert mit Icarus Verilog, vergleicht mit exakter Referenz und Qiskit |
| [`check_out.txt`](check_out.txt) | Ausgabe des Laufs mit 2000 Schaltungen, Seed 1 |
| [`wolfram/qstep2_exakt.wl`](wolfram/qstep2_exakt.wl) | exakte Gegenprobe mit Kronecker-Matrizen, [Ausgabe](wolfram/qstep2_exakt_out.txt) |

```sh
python -m qam.examples.coprocessor.check --cases 2000 --seed 1
```

Braucht `iverilog`/`vvp` im Suchpfad und Qiskit 2.x. Ergebnis vom 25.11.2026: 2005 Fälle für W = 16, 4 und 3
bitgenau gleich der Referenz, alle `continue`-Fälle gleich Qiskit (Abweichung ≤ 3·10⁻¹⁵), sechs Fälle exakt gleich
Wolfram. Die Darstellung ist noch nicht kanonisch (Kürzen nur durch 2, nicht durch √2). Keine Synthese, keine
Hardware-Messung.
