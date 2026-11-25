# Bandschaltung auf Überlagerungen (H137, k310)

25.11.2026. Test H137, nicht blind. Vorab-Notiz und Ergebnis unter `notes/research/predictions/`
(`Vorab_Notiz_H137_Bandschaltung_Ueberlagerungen.md`, `Ergebnis_H137_Bandschaltung_Ueberlagerungen.md`).

- `k310_test_h137.py`: Qiskit. Lässt `FiniteBand` aus `qam/examples/zuse_machine/machine_qiskit.py` auf Überlagerungen laufen (Programm aus
  `machine.json`, n = 2, 3) und baut für ein umkehrbares Programm R den Bennett-Schritt. Aufruf vom Repo-Stamm:
  `python notes/research/bandschaltung_ueberlagerung_2026_11_25/k310_test_h137.py`. Laufzeit etwa 4 Minuten; braucht `qiskit` und für die 16-Qubit-Fälle `qiskit-aer`.
- `k310_out.txt`: tatsächliche Ausgabe (JSON-Zeilen).
- `k310b_gegenprobe.wl`, `k310b_out.txt`: Wolfram Language, exakt: Schrittabbildung aus den Regeln, Kollisionen, reduzierte Zustände zu H137d.

Nummern: Block k310–k319 für diesen Faden; vergeben k310.
