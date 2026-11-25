# Frame-Korrektur auf die TM1-Klasse (Test H134, k263)

Test H134, teilweise nicht blind. Vorab-Notiz `../../predictions/Vorab_Notiz_H134_Frame_Rapiditaet_TM1_JUNO.md` (Commit a0ab92e, vor der Rechnung),
Ergebnis `../../predictions/Ergebnis_H134_Frame_Rapiditaet_TM1_JUNO.md`.

| Datei | Inhalt |
|---|---|
| `k263_test_h134.py` | Test; Regel und Funktionen aus `../../v4_10_0_r56_r60/llm/k100_test_h45.py`. Aufruf `python3 k263_test_h134.py [Schritt in Grad]` |
| `k263_out.txt` | Ausgabe mit dem Raster der Vorab-Notiz (2°); maßgeblich für die Entscheidung |
| `k263_out_fein.txt` | Ausgabe mit 0,5° (nachträglich, weil Kontrolle (i) auf 2° leer ist) |
| `k263c_trefferpunkt.py`, `k263c_out.txt` | ein Trefferpunkt mit Matrizen (nachträglich, für Kontrolle (iv)) |
| `k263b_kontrolle.wl`, `k263b_out.txt` | Wolfram: Trefferpunkt und ε = 0 unabhängig nachgerechnet |

Laufzeit: 2° etwa 5 Minuten, 0,5° etwa 19 Minuten auf vier Kernen (multiprocessing).
