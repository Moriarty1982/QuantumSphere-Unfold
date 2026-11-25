# Vorab-Notiz H137: Arbeitet die reversible Bandschaltung auf Überlagerungen von Bandkonfigurationen quantenmechanisch?

**Stand:** 2026-11-25, vor der Rechnung festgelegt. **Nicht blind:** Die Schaltung ist aus Mehrfach-Toffoli-Gattern gebaut und damit eine
Permutationsmatrix. Die meisten Ausgänge stehen deshalb analytisch fest; sie sind unten als Erwartung offengelegt. Die Rechnung prüft, ob die
Implementierung und die Lesart tragen, und liefert die Zahlen (Kollisionen, Reinheit, Entropien). Anlass: Autor, 25.11.2026, 15:16 UTC, auf die
Frage, ob die vorhandene Schaltung auf Überlagerungen laufen soll: „mach das“. Punkt 2 der Liste „Was fehlt für einen Quantenrechner im Träger“.
Skripte ab **k310** (Block k310–k319 für diesen Faden; k306 ff. gehören dem Faden Feldgleichung, k264 ff. dem Faden Hilbert-Shift).

**Werkzeugwahl:** Qiskit (2.x, `Statevector`, `Operator`, `partial_trace`) für die Schaltung selbst, weil sie dort definiert ist
(`qam/examples/zuse_machine/machine_qiskit.py`, `FiniteBand`). Wolfram Language unabhängig und exakt für die Schrittabbildung f (eigene
Implementierung aus der Regeltabelle), die Kollisionszahl und die reduzierten Zustände des Beispiels zu H137d. MMA/HDL-Vergleich nicht nötig:
`RUN_TAPE` und die SystemVerilog-Steuerung werden nicht geändert, und die Basisspuren werden nur zur Kontrolle gegen das Laufprotokoll gelesen.

## Vorwissen geprüft
- **Companion 19K–19R** (r60-Datei ab Z. 28415; `sources/research/parts/v470/24_computational_specification.tex`): Spinorband-Hypothese STH,
  fünf offene Verpflichtungen U_T, U_Q, U_B, U_L, U_S. Nichts dort spricht von Überlagerungen von Bandzuständen; die Maschine ist klassisch gelesen.
- **`qam/examples/zuse_machine/`** (README, `verification.md`, 21.11.): `FiniteBand` baut je Bandlänge eine Einzelschrittschaltung
  |x, y⟩ ↦ |x, y ⊕ (f(x), Status)⟩. Der Treiber liest jedes Ergebnis aus (Statevector, Ergebnis muss ein Basiszustand sein) und startet den
  nächsten Schritt neu im Basiszustand. Geprüft: 24 Zweizellen-Spuren gegen Wolfram; „Schaltung und Inverse stellen eine zweikomponentige
  Eingabeüberlagerung wieder her“. Kohärenz im Ausgang, Injektivität von f, Verschränkung: nicht geprüft.
- **H116, H117** (`llm/`): Phasenauslese und Orientierung des Rückwegs am Spinorband, Wolfram exakt, ohne Schaltung und ohne Übergangsregel.
  H117 hält mehrere Orientierungen als Maske in einem Zustand (klassisch, keine Amplituden).
- **k244** (`llm/k244_h123_qiskit_cycle_test.py`): Qiskit-Schaltung zum zyklischen Registertausch (H123), unitär, keine Bandmaschine.
- **`qam/examples/*coherent*`, `rotation_filter_*`**: kohärente Qiskit-Beispiele zu Fluss und Drehfiltern, keine Bandmaschine.
- Suche nach „Bennett“, „Toffoli“, „quantum Turing“ in `notes/`, `qam/examples/`, `sources/research/parts/`: keine Fundstelle.

## Aufbau
- **Programm P (Beispiel):** `machine.json` (Zustände `scan`, `halt`). Bandlängen n = 2 und n = 3 (10 bzw. 14 Qubits).
- **Programm R (umkehrbar, nur für H137c-Kontrolle und H137d):** Zustände `a`, `b`, `halt`; Regeln `a/r → schreibe 1−r, bleibe, b`,
  `b/r → schreibe r, bleibe, a`. Die Schrittabbildung ist auf gültigen Konfigurationen eine Bijektion (Status immer „running“ außer bei `halt`).
  R ist eine Setzung für den Test, kein Programm des Companion.
- **Gültige Konfigurationen:** Band ∈ {0,1}ⁿ, Kopf 0…n−1, Zustand aus der Liste; Ausgaberegister |0⟩.
- **Kohärenter Einzelregisterschritt (Bennett):** für ein injektives f aus U_f (FiniteBand) und U_{f⁻¹} (allgemeines XOR-Orakel, eigens gebaut):
  |c, 0⟩ → |c, f(c)⟩ → Tausch → |f(c), c⟩ → U_{f⁻¹} → |f(c), 0⟩.

## Erwartung, vorab offengelegt (analytisch)
1. U ist eine Permutation der Basis, also unitär auf dem vollen Raum, und linear: Σ a_c |c, 0⟩ ↦ Σ a_c |c, f(c)⟩ mit unveränderten Amplituden und
   Phasen. Aus einem Basiszustand entsteht nie eine Überlagerung.
2. Weil die Eingabe stehen bleibt, ist das Ausgaberegister mit ihr verschränkt. Der reduzierte Zustand des Ausgaberegisters hat zwischen
   verschiedenen Folgekonfigurationen keine Nebendiagonale; seine Reinheit ist Σ_y (Σ_{f(c)=y} |a_c|²)².
3. f von P ist nicht injektiv: `scan` liest 0, schreibt 1 und hält; das Ergebnis fällt mit der schon haltenden Konfiguration zusammen. Erwartet
   n·2^{n−1} Kollisionen, also |Bild| = 2n·2ⁿ − n·2^{n−1} (n = 2: 16 → 12; n = 3: 48 → 36). Dann gibt es keinen unitären Schritt auf dem
   Konfigurationsregister allein; ein kohärenter Lauf braucht ein Protokollregister, das je Schritt wächst.
4. Für R ist der Bennett-Schritt unitär auf dem Konfigurationsregister und erhält Reinheit und Phasen.
5. Mit dem Kopf in Überlagerung erzeugt ein R-Schritt Verschränkung zwischen Band und Kopf (GHZ-artig, Kopf als Wegmarke). Nach Spur über Kopf und
   Zustand bleibt zwischen zwei Zellen ein klassisch korrelierter, separabler Zustand.

## Hypothesen und Kriterien
- **H137a (unitär auf Überlagerungen):** Für P mit n = 2 und n = 3 gilt ‖U†U − I‖_max < 10⁻¹⁰, und für 200 zufällige komplexe Überlagerungen
  gültiger Konfigurationen (je n) ist die Treue mit Σ a_c |c, f(c), Status⟩ ≥ 1 − 10⁻¹⁰.
  - **Bestätigt:** beides erfüllt. **Widerlegt:** sonst. Erwartung: bestätigt.
- **H137b (Kohärenz im Folgezustand):** Für P erhält der Schritt Kohärenz im Ausgaberegister: Es gibt unter den 200 Überlagerungen je n
  mindestens eine, bei der der reduzierte Zustand des Ausgaberegisters ein Nebendiagonalelement |ρ_{yy'}| > 10⁻⁶ zwischen verschiedenen
  Folgekonfigurationen y ≠ y' hat.
  - **Bestätigt:** ja. **Widerlegt:** max |ρ_{yy'}| ≤ 10⁻⁶ für alle. Erwartung: widerlegt.
- **H137c (Schritt ohne Protokoll):** Die Schrittabbildung f von P (Konfiguration ↦ Konfiguration und Status) ist auf den gültigen
  Konfigurationen injektiv.
  - **Bestätigt:** injektiv. **Widerlegt:** mindestens eine Kollision. Erwartung: widerlegt mit n·2^{n−1} Kollisionen.
  - **Kontrolle zu c:** Für R ist f injektiv, und der Bennett-Schritt bringt das Hilfsregister für alle gültigen Basiszustände auf |0⟩ zurück und gibt
    für 200 zufällige Überlagerungen Treue ≥ 1 − 10⁻¹⁰ mit Σ a_c |f(c)⟩ (Reinheit 1).
- **H137d (Verschränkung zwischen Zellen):** R, n = 2 und n = 3, Start Band 0…0, Zustand `a`, Kopf (|0⟩ + |1⟩)/√2, ein kohärenter Bennett-Schritt.
  - **H137d1:** Von-Neumann-Entropie der Bandzellen gegen Kopf und Zustand > 0,01 Bit. Erwartung: bestätigt (1 Bit).
  - **H137d2:** Negativität zwischen Zelle 0 und Zelle 1 nach Spur über alles andere > 10⁻⁶. Erwartung: widerlegt (0).
- **Kontrollen:** (i) Die Basisspuren der Beispiele `room` und `edge` (fester Modus) stimmen mit `verification.md` überein. (ii) Wolfram rechnet f für P
  (n = 2, 3) und R unabhängig aus den Regeln und gibt dieselbe Kollisionszahl; die reduzierten Zustände zu H137d exakt. (iii) ‖U U† − I‖ < 10⁻¹⁰.
  Schlägt eine Kontrolle fehl, ist der Lauf ungültig.

## Folge, vorab festgelegt
- Fallen a bestätigt, b und c widerlegt aus, heißt das: Die Schaltung ist ein klassisch-reversibles Orakel. Sie trägt Überlagerungen linear, aber das
  Band als Einzelregister nicht kohärent: Jeder Schritt hinterlässt eine Kopie, und der Treiber misst. Für Punkt 2 („unitäre Schritte“) fehlen dann
  (1) ein umkehrbares Programm oder ein Protokollband, (2) eine Uncompute-Stufe, (3) ein nicht-permutatives Gatter (Amplituden, Hadamard-artig),
  das der Turm liefern müsste. Ohne (3) bleibt die Maschine klassisch, auch auf Überlagerungen.
- Fällt d1 bestätigt und d2 widerlegt aus, entsteht Verschränkung nur über den Kopf als Wegmarke, nicht zwischen Zellen selbst; echte Zell-Zell-
  Verschränkung braucht eine Kopplung außerhalb der Permutationsgruppe (Punkt 3 der Liste).
- Weicht ein Ausgang von der Erwartung ab, wird er als Befund gemeldet und nicht nachträglich umgedeutet.
- **Status:** kein OP berührt; die Verpflichtungen U_Q, U_B, U_L, U_T, U_S und Q1a bleiben offen. Paper und Preprint werden nicht angefasst.
