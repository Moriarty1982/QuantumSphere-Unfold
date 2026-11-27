# Quanten-Coprozessor, Baustufe 0

Erste Baustufe des [Bauplans](../../../notes/quanten_coprozessor/Bauplan.md): eine exakte Zustandsvektor-Einheit für
zwei Qubits in SystemVerilog. Jede Amplitude ist $(c_0 + c_1\omega + c_2\omega^2 + c_3\omega^3)/\sqrt2^{\,k}$ mit
ganzzahligen $c_j$ und $\omega = e^{i\pi/4}$; $k$ gilt für den ganzen Zustand. Damit rechnet die Einheit alle
Clifford+T-Gatter ohne Rundung. Ein Gatter pro Takt; Status `continue`, `guard` (Überlauf der Wortbreite W) oder
`reject` (unbekannter Opcode) wie bei MMA.

| Datei | Inhalt |
|---|---|
| [`hdl/qstep2.sv`](hdl/qstep2.sv) | die Einheit, Opcodes `NOP X Z S SDG T TDG H CX` |
| [`hdl/qcfg.sv`](hdl/qcfg.sv) | Konfigurationsregister: Laufzeitwerte und Bank für bisher unsichere Größen |
| [`hdl/qcop2_top.sv`](hdl/qcop2_top.sv) | oberste Ebene: `qcfg` + `qstep2` |
| [`hdl/qstep2_tb.sv`](hdl/qstep2_tb.sv) | Testbench, liest ein einfaches Befehlsband (`C adr wert`, `R adr`, `B`, `G op ziel`, `E`) |
| [`check.py`](check.py) | erzeugt Fälle, simuliert mit Icarus Verilog, vergleicht mit exakter Referenz und Qiskit, prüft die Register |
| [`check_out.txt`](check_out.txt) | Ausgabe des Laufs mit 2000 Schaltungen, Seed 1 |
| [`synth_check.py`](synth_check.py), [`synth_out.md`](synth_out.md) | Yosys-Synthese aller HDL-Bausteine (auch Bandmaschine), Zellenzahlen |
| [`wolfram/qstep2_exakt.wl`](wolfram/qstep2_exakt.wl) | exakte Gegenprobe mit Kronecker-Matrizen, [Ausgabe](wolfram/qstep2_exakt_out.txt) |

```sh
python -m qam.examples.coprocessor.check --cases 2000 --seed 1
python -m qam.examples.coprocessor.synth_check            # braucht yosys oder yowasp-yosys
```

Braucht `iverilog`/`vvp` im Suchpfad und Qiskit 2.x. Ergebnis vom 25.11.2026: 2005 Fälle für W = 16, 4 und 3
bitgenau gleich der Referenz, alle `continue`-Fälle gleich Qiskit (Abweichung ≤ 3·10⁻¹⁵), sechs Fälle exakt gleich
Wolfram. Die Darstellung ist noch nicht kanonisch (Kürzen nur durch 2, nicht durch √2). Keine Synthese, keine
Hardware-Messung.

## Synthesefest und Eingabewerte von außen (27.11.2026)

Die erste Fassung lief nur im Simulator: Yosys brach in `qstep2.sv` ab, weil die Phasenschleife eine variable Grenze hatte.
Jetzt haben alle Schleifen feste Grenzen; die Phase ω^r ist ein Umsortieren der vier Koeffizienten mit Vorzeichenwechsel.
`synth_check.py` synthetisiert alle HDL-Bausteine (Coprozessor und Bandmaschine) und läuft mit dem Vergleich in der CI
(Workflow `qam-batch.yml`, Job `coprocessor`). Mit den Vorgabewerten rechnet die Einheit bitgenau wie vorher (gleiche
2005 Fälle, gleiche Status). Zellenzahl für W = 16 mit Registern: siehe [`synth_out.md`](synth_out.md) (generisch, vor
dem Mapping auf ein FPGA; keine Taktmessung).

**Konfigurationsregister** (`qcfg.sv`, 32 × 32 Bit). Der Host schreibt jederzeit; wirksam werden die Werte mit dem nächsten
`load`, sodass ein Lauf immer einen festen Satz sieht. Lesen geht jederzeit.

| Adr. | Name | Format | Vorgabe | Wirkung |
|---|---|---|---|---|
| 0x00 | ID | – | 0x51430001 | nur lesen |
| 0x01 | ALLOW | Bitmaske | 0x1FF | Bit n erlaubt Opcode n, sonst `reject` (wie `ALLOW` in Stufe 2) |
| 0x02 | W_EFF | Bit | W | Guard-Breite, auf 2…W begrenzt |
| 0x03 | K_MAX | ganz | 255 | größtes k, darüber `guard` |
| 0x04 | BUDGET | ganz | 0 | höchstens so viele Gatter (0 = unbegrenzt), dann Status 3 `step_limit` |
| 0x05 | FLAGS | Bits | 1 | Bit 0: Kürzen durch 2 |
| 0x10 | BETA_SYM | Q2.30 | 0,5494056 | Zählpostulat |
| 0x11 | EPSILON | Q2.30 | 0,6175295 | artanh β_sym, Maske H45 |
| 0x12 | CHI | Drehung | 0 | Neigung der Bandachse (H211, frei) |
| 0x13 | DELTA_NU | Drehung | 1/12 | δ_ν = π/6 (H173) |
| 0x14 | BAND_WEIGHT | Q2.30 | 1 | Bandgewicht (H209/H210, gesetzt) |
| 0x15 | X_OFFSET | Q2.30 | 0,0396 | gemeinsamer Versatz (H168/H207) |
| 0x16 | ROT_ALPHA | Drehung | 0 | Winkel für `ROT` |
| 0x17–0x1A | SWAP_X, ADD_MU, DROP_LAMBDA, NOISE_EPS | Q2.30 | 0 | Stärken für `SWAP`, `ADD`, `DROP`, `NOISE` |
| 0x1B–0x1F | frei | – | 0 | – |

Q2.30 heißt vorzeichenbehaftet, Wert/2³⁰; „Drehung“ heißt vorzeichenlos, Bruchteil einer vollen Drehung (Wert/2³²).
Die Bank 0x10–0x1F wird in Stufe 0 **nicht gelesen**: Der exakte Clifford+T-Kern kennt keine solchen Größen. Sie liegt als
Ausgang `phys` an der obersten Ebene und ist für die Rechenwerke der Stufe 2 (Drehung, Bandwechsel, Rauschen) gedacht. Die
Vorgaben sind die derzeitigen Setzungen bzw. Postulate des Projekts, keine hergeleiteten Werte.

`check.py` prüft zusätzlich: alle 32 Register nach dem Reset (ID und Vorgaben), Schreiben und Zurücklesen, Schreibschutz der
ID, und 2005 Fälle mit zufälligen Laufzeitwerten (ALLOW, W_EFF, K_MAX, BUDGET, FLAGS) bitgenau gegen die Referenz.
