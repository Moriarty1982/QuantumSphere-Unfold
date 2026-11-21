# Vergleich von MMA und SystemVerilog

Beide HDL-Steuerungen stimmten in allen 209 Fällen mit MMA überein.
Das umfasst 204 Startkombinationen aus allen Binärbändern der Längen 1–3, allen Kopfpositionen, drei Zuständen und zwei Bandmodi eines Verzweigungsprogramms.

Takte ab geladener Startkonfiguration bis zur Stopmeldung

| Fall | Stop | Gezählt in MMA | Direkt | Zyklisch |
|---|---|---:|---:|---:|
| 7 + 1 | `halted` | 4 | 4 | 24 |
| 7 + 1, festes Band | `boundary` | 3 | 3 | 18 |
| 7 + 1, Zelllimit | `cell_limit` | 2 | 3 | 18 |
| 7 + 1, Schrittlimit | `step_limit` | 1 | 1 | 6 |
| Schrittlimit null | `step_limit` | 0 | 0 | 0 |

Bandspur für 7 + 1 mit wachsendem Band

`[1, 1, 1]` → `[0, 1, 1]` → `[0, 0, 1]` → `[0, 0, 0, 0]` → `[0, 0, 0, 1]`

Generische Yosys-Zellen (synth -noabc, ohne FPGA-Mapping)

| Direkt | Zyklisch |
|---:|---:|
| 564 | 613 |

## Laufumgebung

Lokaler Lauf unter Ubuntu in WSL mit Icarus Verilog 10.3 und Yosys 0.9
(`1979e0b`). Die Ausführung prüfte auch, dass sich zwischen gemeldeten
Schritten kein Band-, Kopf- oder Steuerzustand ändert. Inaktive physische
Zellen wurden mit Einsen vorgeladen, damit jede freigegebene Nullzelle
tatsächlich initialisiert werden musste. Die 22 bestehenden MMA- und
Framework-Tests liefen ebenfalls erfolgreich.

In einer temporären Kopie des HDL-Kerns wurde absichtlich auch beim
Stoppsignal `boundary` geschrieben. Der Vergleich meldete die folgende
erste Abweichung.

```text
7 + 1, festes Band, Direkt, Schritt 3: MMA (3, {'tape': [0, 0, 1], 'head': 2, 'state': 'scan', 'status': 'boundary'}), HDL (3, {'tape': [0, 0, 0], 'head': 2, 'state': 'scan', 'status': 'boundary'})
```
