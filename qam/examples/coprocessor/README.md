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

## Brücke zu Qiskit, Wolfram und OpenQASM (27.11.2026)

[`bridge.py`](bridge.py) verbindet den HDL-Kern mit anderen Werkzeugen, ohne den Kern zu ändern.

- **Gatterfolgen:** OpenQASM 2 oder 3 (Gatter `id x z s sdg t tdg h cx` auf zwei Qubits) ↔ Befehlsband der Testbench.
  Qiskit-Schaltungen gehen direkt (`circuit_to_gates`), jede Gatterfolge lässt sich als OpenQASM 3 ausgeben. Nicht vorhandene
  Gatter werden mit Namen abgelehnt, nicht stillschweigend übersetzt.
- **Zustände:** JSON `qcop-state-1` mit den exakten Koeffizienten in ℤ[ω], k, Status und Gleitkomma-Amplituden;
  `to_statevector` gibt einen Qiskit-`Statevector`, `to_wolfram` einen exakten Wolfram-Ausdruck.
- **Ausführen:** `run(...)` auf dem simulierten HDL-Kern (Icarus Verilog) oder mit `simulate=False` auf der exakten Referenz;
  Konfigurationsregister lassen sich je Lauf mitgeben.

```sh
python -m qam.examples.coprocessor.bridge run schaltung.qasm --json zustand.json --wolfram zustand.wl
python -m qam.examples.coprocessor.bridge band schaltung.qasm     # OpenQASM -> Band
python -m qam.examples.coprocessor.bridge qasm band.txt           # Band -> OpenQASM 3
python -m qam.examples.coprocessor.bridge_check --cases 300 --seed 7
```

[`bridge_check.py`](bridge_check.py) ([Ausgabe](bridge_check_out.txt)) prüft in drei Richtungen: 300 zufällige Qiskit-Schaltungen
laufen über OpenQASM 3 → Brücke → Band → OpenQASM 3 → Brücke verlustfrei; die HDL-Simulation gleicht dem Qiskit-Statevector
(Abstand ≤ 7·10⁻¹⁶, ohne Phasenausgleich); der JSON-Zustand ist verlustfrei. Für Wolfram schreibt `--write-wolfram` acht
feste Fälle mit den exakten HDL-Zuständen nach [`wolfram/bridge_exakt.wl`](wolfram/bridge_exakt.wl); Wolfram rechnet sie mit
Kronecker-Matrizen exakt nach (alle Differenzen 0, [Ausgabe](wolfram/bridge_exakt_out.txt), dazu eine Gegenkontrolle mit
absichtlich falschem Zustand). In der CI verlangt der Lauf, dass die aktuelle HDL-Ausgabe genau den gespeicherten Fällen
entspricht; ist `wolframscript` vorhanden, läuft das Skript zusätzlich. Grenzen: zwei Qubits, nur Clifford+T, keine
Messung (kommt mit Stufe 2).

## Boot-Monitor und portables Programmabbild (27.11.2026)

Programme lassen sich jetzt tauschen, ohne die Hardware neu zu bauen. [`hdl/qboot.sv`](hdl/qboot.sv) liest ein Programmabbild
(QIMG) aus dem Programmspeicher, prüft Kopf und Prüfsumme und führt es auf dem Kern aus; [`hdl/qcop2_sys.sv`](hdl/qcop2_sys.sv)
verbindet Programmspeicher (synchron gelesen, also Block-RAM; vom Host beschreibbar), Monitor und `qcop2_top`. Die Idee ist die
einer kleinen virtuellen Maschine mit portablem Programmformat: dasselbe Abbild läuft in der Simulation, später auf dem FPGA und
auf der Python-Referenz. Ein Soft-Core (z. B. RISC-V) kann später denselben Speicher und dieselben Register bedienen.

| Wort | Inhalt |
|---|---|
| 0 | `0x51494D47` („QIMG“) |
| 1 | Version 1 in Bit 31–16, Zahl N der Programmworte in Bit 15–0 |
| 2 | Summe der N Programmworte mod 2³² |
| 3 … | Programm: `HALT` (0), `CFG adr` (1, Wert im nächsten Wort), `LOAD` (2), `GATE op ziel` (3), `EMIT` (4) |

Der Monitor meldet `idle`, `running`, `done` oder `reject` (falsches Magic, falsche Version, zu lang für den Speicher, falsche
Prüfsumme, unbekannter Befehl, `CFG` ohne Wert). Bei `reject` führt er nichts aus. Ein Programmwort braucht zwei Takte (synchrones
Lesen mit Wartetakt).

```sh
python -m qam.examples.coprocessor.bridge band schaltung.qasm > band.txt   # OpenQASM -> Band
python -m qam.examples.coprocessor.qimage asm band.txt > prog.hex          # Band -> Abbild
python -m qam.examples.coprocessor.qimage dis prog.hex                     # Abbild lesbar
python -m qam.examples.coprocessor.qimage --cases 600 --seed 3             # Prüfung
```

[`qimage.py`](qimage.py) ([Ausgabe](qimage_out.txt)): 600 Läufe in 20 Abbildern, davon 315 mit eigener Konfiguration, bitgenau
gleich der Referenz; sieben fehlerhafte bzw. Grenz-Abbilder richtig behandelt. Gegenkontrollen: Ein Monitor ohne
Prüfsummenvergleich und einer mit festem Zielqubit fallen beide durch. Synthese mit Programmspeicher (1024 Worte) auf iCE40:
8 Block-RAM, Zellen in [`synth_out.md`](synth_out.md). Grenzen: keine Sprünge oder Schleifen im Abbild (kommen mit Stufe 2),
keine Taktmessung auf Hardware.

## Beschleunigung: Pipeline mit Kontexten (27.11.2026)

Der Kern ist jetzt in zwei kombinatorische Bausteine zerlegt, die beide Fassungen teilen: [`hdl/qgate2.sv`](hdl/qgate2.sv)
(Gatterwerk) und [`hdl/qnorm2.sv`](hdl/qnorm2.sv) (Kürzen und Guard; beide Vergleichsfälle laufen parallel, die Grenzen der
Guard-Breite kommen aus `qguard_limits`). `qstep2` setzt sie in einen Takt wie bisher (bitgenau gleich, alle Prüfungen
unverändert). [`hdl/qstep2p.sv`](hdl/qstep2p.sv) setzt sie in eine Pipeline mit vier Stufen (Annahme, Gatter, Kürzen/Guard,
Zurückschreiben) und `CTX` Kontexten: unabhängige Läufe, die sich abwechseln. Ab vier Kontexten nimmt die Einheit bei voller
Belegung jeden Takt ein Gatter an; ein einzelner Lauf braucht vier Takte je Gatter, ist allein also langsamer. Die Pipeline
lohnt sich deshalb für viele gleichzeitige Läufe, etwa je Band des Bandregisters. Die Konfiguration ist für alle Kontexte
gemeinsam. Oberste Ebene: [`hdl/qcop2p_top.sv`](hdl/qcop2p_top.sv).

Takt und Fläche auf einem ECP5-85k ([`timing_check.py`](timing_check.py), Yosys `synth_ecp5` + nextpnr, ein Seed; Messrahmen
`qcop2_bench.sv`/`qcop2p_bench.sv` mit registrierten Pins), Ausgabe [`timing_out.md`](timing_out.md):

| Variante | LUT4 | FF | Fmax | Mio. Gatter/s bei voller Belegung |
|---|---:|---:|---:|---:|
| vorher, erste synthesefeste Fassung (#390) | 6132 | 1910 | 42,8 MHz | 42,8 |
| ein Takt je Gatter (qstep2, jetzt) | 5569 | 1910 | 41,0 MHz | 41,0 |
| Pipeline, 4 Kontexte | 6413 | 3645 | 70,5 MHz | 70,5 |
| Pipeline, 8 Kontexte | 8533 | 4782 | 64,3 MHz | 64,3 |

Die Pipeline mit vier Kontexten bringt also rund 1,65-mal so viele Gatter je Sekunde bei 5 % mehr LUTs. Mehr Kontexte kosten
Fläche und, wegen der breiteren Auswahl der Kontexte, wieder etwas Takt. Gemessen in der Simulation
([`pipe_check.py`](pipe_check.py), [Ausgabe](pipe_check_out.txt)): 1200 Fälle je Kontextzahl 1, 4, 8 bitgenau gleich der
Referenz, auch mit zufälliger Konfiguration je Gruppe; bei ungleich langen Läufen erreicht der Wechsel 0,69 (4 Kontexte)
bzw. 0,88 (8 Kontexte) Gatter je Takt, weil am Ende einer Gruppe Kontexte leer laufen. Die Werte schwanken mit dem
Platzierungs-Seed um einige Prozent; keine Messung auf echter Hardware.
