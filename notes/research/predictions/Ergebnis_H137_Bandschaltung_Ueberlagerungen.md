# Ergebnis H137: Die Bandschaltung trägt Überlagerungen linear, rechnet aber klassisch

**Stand:** 2026-11-25. **Nicht blind** nach [Vorab-Notiz](Vorab_Notiz_H137_Bandschaltung_Ueberlagerungen.md), Commit b57f745 vor der Rechnung.
Skripte und Ausgaben in `notes/research/bandschaltung_ueberlagerung_2026_11_25/`: `k310_test_h137.py` mit `k310_out.txt` (Qiskit 2.x, Statevector),
`k310b_gegenprobe.wl` mit `k310b_out.txt` (Wolfram Language, exakt). Alle Ausgänge entsprechen der vorab offengelegten Erwartung.

## Ergebnis

| Teil | Frage | Ausgang | Zahlen |
|---|---|---|---|
| H137a | unitär und linear auf Überlagerungen | **bestätigt** | n = 2: ‖U†U − I‖ = 1,0·10⁻¹⁴, Permutationsmatrix; n = 3: Basisabbildung auf allen 2¹⁴ Eingängen bijektiv; kleinste Treue aus je 200 zufälligen Überlagerungen 1 − 1,1·10⁻¹⁴ (n = 2), 1 − 2,0·10⁻¹³ (n = 3) |
| H137b | Kohärenz im Folgezustand | **widerlegt** | größtes Nebendiagonalelement des Ausgaberegisters 6,1·10⁻¹⁶ (n = 2), 1,5·10⁻¹⁵ (n = 3); Reinheit zwischen 0,145 und 1, in allen 400 Fällen gleich Σ_y (Σ_{f(c)=y} \|a_c\|²)² |
| H137c | Schritt ohne Protokoll (f injektiv) | **widerlegt** | P: 16 → 12 (4 Kollisionen) und 48 → 36 (12 Kollisionen), wie n·2ⁿ⁻¹; Wolfram unabhängig gleich |
| Kontrolle zu c | umkehrbares Programm R mit Bennett-Schritt | erfüllt | f injektiv (24 und 72 Konfigurationen); Hilfsregister für alle Basiseingänge wieder \|0⟩; kleinste Treue 1 − 1,9·10⁻¹³ (n = 2), 1 − 10⁻¹⁵ (n = 3), Reinheit 1 |
| H137d1 | Verschränkung Band gegen Kopf | **bestätigt** | 1 Bit (Qiskit und Wolfram) |
| H137d2 | Verschränkung zwischen zwei Zellen | **widerlegt** | ρ(Zelle 0, Zelle 1) = diag(0, ½, ½, 0), Negativität 0 (Wolfram exakt) |

Kontrollen: (i) die Basisspuren `room` und `edge` stimmen zeichengleich mit `qam/examples/zuse_machine/verification.md` überein; (ii) Wolfram gibt
dieselben Kollisionszahlen (P) und Bijektivität (R: 24 → 24, 72 → 72) und die reduzierten Zustände zu H137d exakt; (iii) ‖UU† − I‖ = 1,0·10⁻¹⁴ (n = 2). (iv, wegen der Methodenänderung ergänzt) qiskit-aer und `quantum_info` geben auf einer 14-Qubit-Überlagerung denselben Zustand (Abweichung 5,4·10⁻¹⁴).

**Abweichung vom Vorab-Plan (Methode, nicht Kriterium):** Für n = 3 (14 Qubits) und den Bennett-Schritt (bis 16 Qubits) passt die volle Matrix nicht in
den Speicher (4 GB und mehr; der erste Lauf wurde abgebrochen). Weil die Schaltungen nur aus X-artigen Gattern (CX, MCX mit Steuerwerten, SWAP) bestehen,
ist U eine Basispermutation; Unitarität wurde dort als Bijektivität der klassischen Basisabbildung auf allen 2^nq Eingängen geprüft. Für n = 2 wurde
diese Methode gegen die `Operator`-Matrix geprüft (gleiche Permutation). Die Zustandsentwicklung mit 16 Qubits (Bennett-Schritt, n = 3) lief in `quantum_info` zu langsam (über 28 Minuten, abgebrochen) und läuft deshalb mit qiskit-aer (Statevector-Methode), geprüft durch Kontrolle (iv). Die Zufallsüberlagerungen des Endlaufs sind andere als im abgebrochenen Lauf; die Teilergebnisse dort stimmten in allen Kriterien überein. Der Wolfram-Teil zu H137d lief erst im zweiten Anlauf; der erste hatte einen
Klammerfehler (`k310b_out.txt`).

## Was das heißt

1. **Die Schaltung ist ein klassisch-reversibles Orakel** |x, 0⟩ ↦ |x, f(x)⟩. Sie bildet Überlagerungen linear und phasentreu ab: Eine Eingabe
   Σ a_c |c⟩ wird zu Σ a_c |c, f(c)⟩. Aus einem Basiszustand entsteht aber nie eine Überlagerung; jede Amplitude wird nur verschoben.
2. **Das Band allein bleibt nicht kohärent.** Die Eingabe bleibt als Kopie stehen und wirkt wie eine Wegmarke. Im Folgezustand allein ist jede
   Überlagerung zu einem Gemisch zerfallen. Bei zwei Eingaben mit demselben Folgezustand (Kollision) wandert die relative Phase ganz ins
   Eingaberegister (Betrag ½, Phase 0,7 wiedergefunden), der Folgezustand ist rein und trägt sie nicht.
3. **Ein unitärer Schritt auf dem Band allein existiert für das Beispielprogramm nicht**, weil `scan` beim Lesen der Null mit einer schon haltenden
   Konfiguration zusammenfällt. Für ein umkehrbares Programm (R) geht es: Der Bennett-Schritt (Orakel, Tausch, inverses Orakel) gibt das Hilfsregister
   für alle Basiseingänge auf |0⟩ zurück und bildet Überlagerungen mit Reinheit 1 auf Σ a_c |f(c)⟩ ab. Das ist die Form, in der Punkt 2 („unitäre
   Schritte“) erfüllbar ist: umkehrbare Regeltabelle oder ein Protokollband, das je Schritt wächst.
4. **Verschränkung entsteht nur über den Kopf.** Mit dem Kopf in Überlagerung verschränkt ein R-Schritt Band und Kopf (1 Bit, GHZ-artig). Zwischen zwei
   Zellen bleibt nach Spur über den Kopf ein klassisches Gemisch ohne Verschränkung. Das liegt an der Gattermenge: Permutationen verschieben Amplituden,
   sie mischen sie nicht.
5. **Was für einen Quantenrechner im Träger fehlt**, wird dadurch schärfer: (a) eine umkehrbare Regeltabelle oder Protokollband mit Rückrechnung,
   (b) mindestens ein Schritt außerhalb der Permutationen, der Amplituden mischt (Hadamard-artig oder eine Phase, die nicht diagonal in der
   Bandbasis wirkt), (c) eine Kopplung zwischen Zellen, die nicht über den Kopf läuft. Toffoli-Gatter zusammen mit einem Hadamard-artigen Gatter sind
   bekanntlich universell; (b) ist also der eigentlich fehlende Baustein. Welcher Teil des Turms ihn liefern könnte (etwa die Holonomie ab HS(2)
   oder die Oktantphasen aus H116/H118), ist nicht geprüft und eine offene Frage.

## Grenzen
- Geprüft ist die Implementierung `FiniteBand` für das Beispielprogramm und für ein eigens gesetztes Programm R, Bandlängen 2 und 3. Die Aussagen 1, 2
  und 4 folgen allgemein aus der Gattermenge; 3 hängt am Programm.
- Der Python-Treiber `FiniteBand.step` misst nach jedem Schritt und verwirft dabei Überlagerungen; das ist Absicht des Beispiels, nicht Fehler.
- Kein OP und keine Verpflichtung U_Q, U_B, U_L, U_T, U_S ist berührt; Q1a (Kollaps, Auslese) bleibt offen. Paper und Preprint sind nicht geändert.
