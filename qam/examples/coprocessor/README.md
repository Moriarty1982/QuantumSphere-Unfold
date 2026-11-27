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

## Partitionierbares Bandregister (27.11.2026)

[`hdl/qband.sv`](hdl/qband.sv) ist ein Register aus 128 Zellen (Parameter `CELLS`, Zweierpotenz), das sich in bis zu 16 Bänder
(Parameter `PARTS`) der Länge 2ⁿ teilen lässt. Es gilt die Buddy-Regel: Ein Band der Stufe n beginnt auf einem Vielfachen von
2ⁿ. Damit passen 2^(7−n) Bänder der Stufe HS(n) hinein (1 × 128, 2 × 64, …, 8 × 16, 16 × 8, …, 128 × 1), und jede Mischung
geht lückenlos auf: 27.338 Größenmischungen, mit Lage rund 4,4·10²² Belegungen. Die Hardware prüft laufend, ob die
Aufteilung gültig ist (`layout_ok`: ausgerichtet, im Register, ohne Überlappung) und ob jede Zelle belegt ist (`full`);
Zugriffe auf eine ungültige Aufteilung oder hinter das Bandende melden `guard`. Ein Bus von 128 Bit (Parameter `BUSW`) liest
und schreibt das ganze Register in einem Wort.

**Eingebrannte Eigenschaften je Stufe n** (Setzungen, keine hergeleiteten Werte), je Stufe über `SET_PROF` überschreibbar und
mit `CLR_PROF` wieder auf die Vorgabe zurückzusetzen:

| Feld | eingebrannt | überschreibbar |
|---|---|---|
| HS | n | nein |
| CLOCK (Typ-Uhr mod 8, k407) | n mod 8 | ja |
| LENGTH, REPEAT | 2ⁿ, 128/2ⁿ | nein |
| WEIGHT (Q2.30) | 2ⁿ/128, Anteil am Register | ja |
| PHASE (Drehung) | n/8, ein 45°-Schritt je Stufe (vgl. H211) | ja |

Befehle: `SET_PART`, `WR_CELL`/`RD_CELL` (Band, Zelle), `WR_WORD`/`RD_WORD` (Bus), `SET_PROF`/`CLR_PROF`/`RD_PROF`. Die
Abschnittstabelle liegt als Ausgang für spätere Rechenwerke je Band an.

[`band_check.py`](band_check.py) ([Ausgabe](band_check_out.txt)): 6000 zufällige Befehle mit gültigen, lückenhaften und
absichtlich falschen Aufteilungen (falsch ausgerichtet, überlappend, zu lang) bitgenau gleich dem Python-Modell.
Gegenkontrollen: Ohne Ausrichtungsprüfung oder ohne Speichern der überschriebenen Phase fällt der Vergleich durch.
Grenzen: Die Bänder sind noch nicht an Rechenwerke angeschlossen (kommt mit den parallelen Rechenwerken), die Zellen sind
1 Bit breit (Parameter `CW` vorbereitet, Busweg nur für 1 Bit geprüft).

## Parallele Rechenwerke je Band (27.11.2026)

[`hdl/qcop2m_top.sv`](hdl/qcop2m_top.sv) schließt das Bandregister an Rechenwerke an: `LANES` Pipelines (`qstep2p`) mit je
`CTX` Kontexten, zusammen `LANES·CTX` Läufe. Band p gehört zu Spur p/CTX, Kontext p mod CTX; jede Spur nimmt je Takt ein
Gatter an, zusammen bis zu `LANES` Gatter je Takt. Gatter für ein Band, das im Bandregister nicht gültig ist (oder solange die
Aufteilung ungültig ist), werden verworfen und gezählt (`blocked`). Die Prüfung der Aufteilung im Bandregister läuft jetzt in
zwei registrierten Stufen (Paarüberlappungen parallel, Summe der Längen als Baum); nach `SET_PART` steht `busy` zwei Takte
auf 1, danach gelten `layout_ok` und `full` für die neue Tabelle.

[`lanes_check.py`](lanes_check.py) ([Ausgabe](lanes_check_out.txt)): je 1200 Fälle für 2 Spuren × 4 Kontexte (8 Bänder zu
16 Zellen) und 4 Spuren × 4 Kontexte (16 Bänder zu 8) bitgenau gleich der Referenz, auch mit fehlenden Bändern und absichtlich
ungültigen Aufteilungen; in der Simulation 1,30 bzw. 2,27 Gatter je Takt bei voll belegten Gruppen. Gegenkontrolle: Ohne
Sperre ungültiger Bänder fällt der Vergleich durch.

Takt (ECP5-85k, [`timing_out.md`](timing_out.md)): Mit der ersten, einstufigen Prüfung der Aufteilung lag der kritische Pfad
im Bandregister (2 Spuren 43 MHz, 4 Spuren 23 MHz). Mit der zweistufigen Prüfung erreichen 2 Spuren × 4 Kontexte 62,0 MHz bei
14 887 LUT4, also bis zu 124 Mio. Gatter/s (eine Pipeline allein: 71 Mio.). Für 4 Spuren wurde die Platzierung mit der neuen
Prüfung nach zwei Stunden nicht fertig; dieser Wert fehlt noch.

## Kanonische √2-Form (27.11.2026)

Mit `flags` Bit 1 kürzt der Kern nach jedem Gatter durch √2 statt durch 2. Regel ([`hdl/qnorm2.sv`](hdl/qnorm2.sv)):
x = a₀ + a₁ω + a₂ω² + a₃ω³ ist genau dann durch √2 = ω − ω³ teilbar, wenn a₀ ≡ a₂ und a₁ ≡ a₃ (mod 2); dann ist
x/√2 = ((a₁−a₃) + (a₀+a₂)ω + (a₁+a₃)ω² + (a₂−a₀)ω³)/2. Der Schritt läuft zweimal hintereinander. Das genügt: Nur H ändert den
kleinsten Exponenten, und weil H sich selbst invers ist, um höchstens eins nach unten, also nach kn = k + 1 höchstens zwei
Schritte. Danach ist k der kleinste mögliche Exponent (kanonische Form, Voraussetzung für einen Hash-Speicher mit Dedup).

Prüfung in [`check.py`](check.py) (`check_canonical`): 505 Fälle bitgenau gleich der Referenz; am Ende jedes Falls ist der
Zustand nicht weiter durch √2 teilbar; die Amplituden sind gleich der Rechnung ohne Kürzen. Summe der Exponenten 721 statt
795 beim Kürzen durch 2. Gegenkontrolle: Mit nur einem √2-Schritt bleiben in 48 von 3000 Fällen Zustände kürzbar.
Wolfram-Gegenprobe der Formeln ([`wolfram/norm_wurzel.wl`](wolfram/norm_wurzel.wl), [Ausgabe](wolfram/norm_wurzel_out.txt)).
Kosten: Der längere Pfad senkt den Takt. In der Pipeline laufen die zwei √2-Schritte deshalb in S2 (`qroot2`) und der Guard
in S3 (`qguard2`, zusammen mit dem Zurückschreiben): 59,5 MHz statt 41 MHz bei allem in S2 (ohne kanonische Form 71 MHz). Im
Ein-Takt-Kern kostet sie 43 → 26 MHz. Mit dem Makro `QCOP_NO_CANON` wird die Form weggelassen.

## Selbstüberwachung: Normwächter (27.11.2026)

[`hdl/qmon.sv`](hdl/qmon.sv) prüft den exakten Zustand: |x|² = P + √2·Q mit P = Σaⱼ², Q = a₀a₁ + a₁a₂ + a₂a₃ − a₃a₀; der Zustand
ist genau dann normiert, wenn ΣP = 2ᵏ und ΣQ = 0. [`hdl/qcop2s_top.sv`](hdl/qcop2s_top.sv) schaltet den Wächter mit `flags`
Bit 2 zu: Bei einer Verletzung nimmt der Kern schon das Gatter im selben Takt nicht mehr an, `fault` bleibt bis zum nächsten
`load`, `faults` zählt. Ein einzelnes gekipptes Bit unterhalb des Vorzeichenbits ändert P immer (Begründung im Kopf von
`qmon.sv`); beim Vorzeichenbit gilt das nicht.

[`monitor_check.py`](monitor_check.py) ([Ausgabe](monitor_check_out.txt)): 800 Fälle mit zufälliger Konfiguration; ohne
Einspeisung kein Fehlalarm, mit gekipptem Bit am Eingang des Wächters sofort angehalten (Ergebnis = Referenz der Gatter
davor), bei ausgeschaltetem Wächter weitergerechnet. Gegenkontrollen: Anhalten erst einen Takt später oder ein Wächter, der
immer „ok“ meldet, fallen durch. Grenzen: Die Fehler werden am Eingang des Wächters nachgebildet, nicht im Kern; der Wächter
ist kombinatorisch und groß (32 Multiplikationen; generische Synthese 93 000 Zellen), eine sequenzielle Fassung wäre kleiner.

## Selbstjustierung: Rückkopplungswerk (27.11.2026)

[`hdl/qtune.sv`](hdl/qtune.sv) sucht eine von außen gesetzte Größe in Q2.30 selbst: Es wertet f(x) = c₀ + c₁x + c₂x² in
Festkomma aus (ein Schritt je Takt) und läuft entweder als Fixpunktsuche x ← f(x) (Modus FIX, bis |f(x) − x| ≤ tol oder
`max_iter`) oder als Halbierung für f(x) = target in [lo, hi] (Modus BISECT, mit Prüfung der Klammer). In FIX meldet es die
letzten zwei Schrittweiten; ihr Verhältnis schätzt |f′(x*)|, also wie stabil der Fixpunkt ist. [`hdl/qcop2t_top.sv`](hdl/qcop2t_top.sv)
hängt das Werk an den Kern: Mit Rückschreiben landet ein konvergiertes Ergebnis im live-Register 0x10 + n der Bank (wirksam ab
dem nächsten `load`) und das Bit n im Register ADJUSTED wird gesetzt. **Jedes so geschriebene Ergebnis ist als „angepasst“
markiert** (gesucht, nicht hergeleitet). Schreibt der Host das Register selbst, verschwindet die Markierung: Der Wert ist dann
gesetzt. Hostzugriffe haben Vorrang.

[`tune_check.py`](tune_check.py) ([Ausgabe](tune_check_out.txt)): 403 Läufe (zufällige Polynome, Grenzen, Toleranzen,
Schrittzahlen; konvergiert, `max_iter`, ungültige Klammer) bitgenau gleich dem Python-Modell, Rückschreiben und Markierung wie
erwartet. Beispiele: Die logistische Abbildung x′ = 1,5x(1 − x) läuft ab 0,9 in 24 Schritten auf 1/3, das Verhältnis der
letzten Schritte ist 0,502 (|f′(1/3)| = 0,5); die Halbierung für x² = ½ liefert 0,707106781 in 30 Schritten.
Gegenkontrollen: Ohne Löschen der Markierung beim Hostschreiben oder mit vertauschter Halbierungsrichtung fällt der Vergleich
durch. Grenzen: Wertebereich Q2.30 ([−2, 2)); die HC-Schleife b′ = 1 − 2b + 2b² braucht c₂ = 2 und passt so nicht hinein.
Welche Größe (β_sym, χ, Gewicht) mit welcher Zielfunktion gesucht wird, legt der Host fest; das Werk erklärt nichts, es
findet nur Werte und misst ihre Stabilität. Das ist die Grundlage für den geplanten Stabilitätstest mit Vorab-Notiz.

## Zustandsspeicher nach ZFS-Vorbild (27.11.2026)

[`hdl/qstore.sv`](hdl/qstore.sv) legt exakte Zustände (16 Koeffizienten zu 16 Bit und k, 264 Bit) inhaltsadressiert ab, wie
ZFS Blöcke: Jeder Datensatz trägt seine Prüfsumme (CRC-32 wie `zlib.crc32`). Namen zeigen auf Plätze, ein Platz zählt seine
Nutzer.

| Befehl | Wirkung |
|---|---|
| PUT a | Datensatz unter Name a ablegen; gleicher Inhalt schon vorhanden → derselbe Platz (Dedup); Copy-on-write bei geteilten Plätzen |
| GET a | lesen; stimmt ein Spiegel nicht mit der Prüfsumme, wird aus dem anderen gelesen und repariert (Selbstheilung) |
| SNAP a → b | Schnappschuss: b zeigt auf denselben Platz und ist nur lesbar |
| CLONE a → b | Klon: b zeigt auf denselben Platz und ist schreibbar; eine eigene Kopie entsteht erst beim PUT |
| DEL a | Name löschen, Platz frei, wenn niemand mehr darauf zeigt |
| FLIP | (nur für Prüfungen) ein Bit in einem Spiegel kippen |

Dazu ein laufender Prüfhash über alle PUT (`audit`), sodass zwei Läufe mit gleichem Hash dieselben Zustände in derselben
Reihenfolge abgelegt haben. [`store_check.py`](store_check.py) ([Ausgabe](store_check_out.txt)): 3000 Befehle bitgenau gleich
dem Python-Modell (407 Dedup-Treffer, 51 Reparaturen, 22 Fälle mit beiden Spiegeln falsch korrekt als Fehler gemeldet).
Gegenkontrollen: Ohne Reparatur oder ohne Freigabe des alten Platzes fällt der Vergleich durch.

Warum die kanonische √2-Form dafür nötig ist: Aus 600 Schaltungen entstehen 403 verschiedene Zustandsvektoren. Kanonisch sind
das genau 403 Datensätze, mit Kürzen durch 2 aber 407 und ohne Kürzen 453: Derselbe Zustand hätte sonst mehrere Darstellungen,
und die Dedup würde ihn nicht wiedererkennen. Die Paritätsspur aus dem Plan bleibt Erkundung und ist nicht gebaut. Grenzen:
8 Plätze und 8 Namen (Parameter), Speicher in Registern (46 000 generische Zellen), noch nicht an den Kern angeschlossen.

