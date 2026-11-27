# Bauplan: ein Quanten-Coprozessor für QAM/MML/MMA

Stand 25.11.2026. Planungsdokument, keine Runde und kein Befund des Companion. Die erste Baustufe (Abschnitt 7)
ist gebaut und geprüft; alles danach ist Plan.

## 1. Kurz gesagt

- **Was wir bauen:** einen klassischen Rechenbeschleuniger, der Quantenschaltungen *exakt nachrechnet* und dabei die
  QAM-Regeln (Guards, Status `continue`/`guard`/`reject`, Belege per Hash) in der Hardware selbst durchsetzt. Ein
  echter Quantenprozessor ist das nicht; er rechnet mit gewöhnlichen Bits.
- **Wie er rechnet:** Der Prozessor bekommt ein **Band** als Eingabe (Kopf mit Größe, Budget und Prämissen-Hash, danach
  die Befehlszellen) und rechnet darauf selbstständig, bis er hält oder ein Guard greift. Der Host lädt nur und liest
  am Ende aus. Die Steuerung ist die vorhandene Bandmaschine (Abschnitt 3a).
- **Wo er läuft:** in zwei Ausführungen mit demselben Befehlssatz. Auf der **Grafikkarte** für Größe (bis etwa 30
  Qubits auf einer üblichen Karte) und in **HDL/FPGA** für einen kleinen, exakten, nachprüfbaren Kern, in dem MMA-Guards
  hart verdrahtet sind.
- **Grenze:** Ein allgemeiner Zustand aus n Qubits braucht 2ⁿ Amplituden. Daran ändert weder Grafikkarte noch FPGA
  noch Dixon-Algebra etwas. Kompression gibt es nur für Zustände mit Struktur (Abschnitt 5).
- **Erste Baustufe steht:** eine exakte Zwei-Qubit-Einheit in SystemVerilog. Sie stimmt in 2005 Fällen bitgenau mit
  einer exakten Referenz und numerisch mit Qiskit überein, in sechs Fällen auch exakt mit Wolfram
  ([`qam/examples/coprocessor/`](../../qam/examples/coprocessor/README.md)).

## 2. Was schon im Companion und im Repo steht

| Baustein | Wo | Was er festlegt |
|---|---|---|
| Rollen der Maschine (Band, Steuerung, Verzweigung, Rückkehr) | Companion 19K–19T, `sources/research/parts/v470/24_computational_specification.tex` | Zustand $(\tau, h, q, \rho, \chi)$: Band, Kopf, Steuerzustand, Auslese, Schalenzertifikat. Spinorband-Hypothese **STH** und Z3-Route sind *Voraussetzungen*, nicht bewiesen. |
| Bandmaschine in SystemVerilog | `qam/examples/zuse_machine/hdl/tape_core.sv` | Zwei Steuerungen (direkt, zyklisch), Stopgründe `halted`, `boundary`, `stuck`, `step_limit`, `cell_limit`. 209 Fälle gleich MMA. |
| Streaming-Guard | `.../hdl/guard_stream.sv` | Zwei Zulässigkeitsmasken je Kandidat, ein Kandidat pro Takt, Zähler für gewählt/blockiert/mehrdeutig. Das ist schon ein Stück „QAM in Hardware“. |
| Reversible Bandschaltung | `qam/examples/zuse_machine/machine_qiskit.py` | Ein Maschinenschritt als reversible Qiskit-Schaltung; die Schaltung und ihr Inverses stellen eine Überlagerung wieder her. Der Test auf Überlagerungen läuft in einem eigenen Thread. |
| MML/MMA | `qam/README.md`, `qam/tools/readout_db.py`, Repo `qam-framework-interface` | MML-Aufträge (`RUN_TAPE`, `READOUT`, `SEARCH_ROUTE`, `EXPORT`, `SCRUB`), MMA-Antwort `continue`/`guard`/`reject`, Belege mit SHA-512-Hash in SQLite. |

Der Coprozessor setzt hier an: Die Bandmaschine ist die *Steuerung*, der neue Teil ist ein *Zustandsrechenwerk*, das
statt eines Bits auf dem Band einen Quantenzustand trägt.

## 3. Architektur

```
 Host (PC)                                   Coprozessor
 ┌──────────────────────────┐   Auftrag      ┌───────────────────────────────────────────┐
 │ MML-Auftrag (JSON)       │ ─────────────▶ │ Befehlsdekoder  (Opcode, Ziel, Steuerung) │
 │ MMA: Kontext + Guards    │                │        │                                  │
 │   prüfen, Programm       │                │        ▼                                  │
 │   übersetzen             │                │ Guard-Einheit  (Wertebereich, erlaubte    │
 │ Beleg (SHA-512) in       │ ◀───────────── │   Befehle, Budget)  → continue/guard/     │
 │   SQLite                 │   Ergebnis +   │   reject als Statusregister               │
 └──────────────────────────┘   Spur         │        │                                  │
                                             │        ▼                                  │
                                             │ Zustandsrechenwerk  (Amplituden exakt,    │
                                             │   eine Gatterstufe pro Takt)              │
                                             │        │                                  │
                                             │ Auslese (Koeffizienten, Wahrscheinlich-   │
                                             │   keiten, Spur für den Beleg)             │
                                             └───────────────────────────────────────────┘
```

**Arbeitsteilung.** MMA bleibt auf dem Host: Kontext, Prämissen, Hashes und die Datenbank sind Software und sollen es
bleiben. In die Hardware kommen nur die Prüfungen, die *pro Schritt* fallen: Ist der Befehl bekannt (sonst `reject`)?
Passt das Ergebnis in die Wortbreite, ist das Budget nicht erschöpft (sonst `guard`)? Der Status ist ein Register, und
nach `guard` oder `reject` nimmt die Einheit keinen weiteren Befehl an, bis der Host neu lädt. Das entspricht der
MMA-Regel, dass ein Guard den Auftrag stoppt und den Kontext nicht verändert.

**Zahlendarstellung.** Für das Projekt ist Exaktheit wichtiger als Tempo. Deshalb rechnet der Kern nicht mit
Gleitkomma, sondern im Ring $\mathbb Z[\omega]$ mit $\omega = e^{i\pi/4}$:

$$a = \frac{c_0 + c_1\omega + c_2\omega^2 + c_3\omega^3}{\sqrt2^{\,k}}, \qquad c_j \in \mathbb Z .$$

Damit sind alle Clifford+T-Gatter ohne Rundung darstellbar. Das T-Gatter ist eine Multiplikation mit $\omega$, also ein
Oktantschritt, und kostet in Hardware nur ein Umsortieren der vier Koeffizienten mit einem Vorzeichenwechsel. H
addiert und subtrahiert Paare und erhöht $k$. Für beliebige Drehwinkel reicht das nicht; die werden entweder
durch Clifford+T angenähert (mit ausgewiesenem Fehler) oder in der GPU-Ausführung mit Gleitkomma gerechnet und dann als
*nicht exakt* markiert.

**Befehlssatz (Entwurf).** Gatter `NOP X Z S SDG T TDG H CX`, später `CCX`, `SWAP`, Messung/Projektion mit Auslese,
dazu Steuerbefehle für das Band (Abschnitt 3a).

## 3a. Das Band als Eingabe

Der Prozessor arbeitet wie die Bandmaschine aus 19K–19L: Er bekommt ein Band, setzt den Kopf auf die erste Befehlszelle
und rechnet ohne Zutun des Hosts, bis ein Stopgrund eintritt. Der Host greift nur zweimal ein, beim Laden und beim
Auslesen.

**Bandformat (Entwurf, Wörter zu 32 Bit).**

| Teil | Inhalt |
|---|---|
| Kopf | Kennung und Formatversion; Zahl der Qubits n; Zahlendarstellung (exakt $\mathbb Z[\omega]$ oder Gleitkomma); Wortbreite W; Budget `max_steps`; erlaubte Opcodes als Bitmaske; die ersten 64 Bit des SHA-512-Hashs des MMA-Kontexts (Prämissenbindung) |
| Startzustand | leer = $\lvert 0\dots0\rangle$, sonst Koeffizienten |
| Befehlszellen | je Zelle: Opcode (8 Bit), Ziel (8 Bit), Steuerqubit oder Sprungweite (16 Bit) |
| Ende | `HALT` |

**Steuerbefehle.** Neben den Gattern liest der Kopf Steuerzellen: `MEASURE q → Bit` (Projektion, Ergebnis in ein
klassisches Bandbit), `JUMP_IF Bit, ±d` (Verzweigung, die Rolle *Branch* aus 19P), `LOOP`/`RETURN` (die Rolle
*Loop/Return* aus 19Q) und `HALT`. Damit ist das Band ein Programm mit Verzweigung und Schleife, und die
Übergangstabelle der Bandmaschine entscheidet, was beim Lesen einer Zelle geschieht. Die Steuerung selbst bleibt klassisch; dass die
vorhandene Bandschaltung Überlagerungen nur als Orakel mit Kopie der Eingabe trägt, zeigt Test H137 (Abschnitt 9). Die Messung macht den Lauf
zufallsabhängig; der Beleg hält dann den Zufallsstartwert fest, oder MMA verlangt alle Zweige.

**Ablauf.**

1. *Laden:* Der Host schreibt das Band in den Speicher des Prozessors. Die Guard-Einheit prüft den Kopf (Format,
   n passt in den Speicher, Opcode-Maske, Budget). Fehler: `reject`, es wird nichts gerechnet.
2. *Laufen:* Pro Schritt liest der Kopf eine Zelle, das Rechenwerk führt sie aus, die Guard-Einheit prüft das
   Ergebnis, der Kopf rückt weiter oder springt.
3. *Stoppen:* `halted` (HALT gelesen), `boundary` (Sprung oder Kopf über das Bandende), `stuck` (Zelle ohne Regel),
   `step_limit` (Budget erschöpft), `guard` (Überlauf, Modus verlassen), `reject` (verbotener Opcode). Das sind die
   Stopgründe von `RUN_TAPE`, ergänzt um die zwei MMA-Status.
4. *Auslesen:* Endzustand, Stopgrund, Schrittzahl, Kopfposition und ein laufender Hash über alle ausgeführten Zellen.
   Der Host legt daraus den MMA-Beleg an.

MML bekommt dafür einen Auftrag nach dem Muster von `RUN_TAPE`, Arbeitsname `RUN_QTAPE`, dessen Argument ein
QAM-Objekt mit dem Band ist.

**Auf dem FPGA** liegt das Band im Block-RAM, der Kopf ist ein Adresszähler, und die vorhandene Steuerung aus
`tape_core.sv` (direkte Regelwahl) wählt pro Zelle die Wirkung. **Auf der Grafikkarte** liegt das Band im
Grafikspeicher neben dem Zustandsvektor. Ein kleiner Steuerkern auf der Karte liest die Zellen und startet die
Gatterkerne, sodass kein Umweg über den Host pro Gatter nötig ist; nur bei `MEASURE` mit anschließendem Sprung entsteht
eine Abhängigkeit, die die Karte selbst auflöst. Beide Varianten lesen dasselbe Bandformat und liefern dieselben
Stopgründe; das ist die Grundlage für den Kreuzvergleich.

Die Testbench der Stufe 0 liest schon eine einfache Form dieses Bandes (Zeilen `B`, `G op ziel`, `E`), nur ohne Kopf
und Steuerbefehle.

## 4. Grafikkarte oder FPGA?

Beides, in dieser Reihenfolge der Nutzung: Die Grafikkarte trägt die großen Rechnungen, der HDL-Kern trägt die exakten
und belegpflichtigen. Beide sprechen denselben Befehlssatz und dieselbe Zahlendarstellung, damit sie sich gegenseitig
prüfen.

| | Grafikkarte (GPU) | FPGA / HDL |
|---|---|---|
| Speicher | 8–24 GB auf üblichen Karten: 2³⁰ Amplituden in einfacher Genauigkeit (8 GB) gehen, also etwa 30 Qubits | Block-RAM meist wenige MB: etwa 16–20 Qubits; mit externem DDR mehr, aber langsam |
| Tempo | sehr hoch für große Zustände, da jede Gatterstufe ein paralleler Durchlauf über alle Amplituden ist | pro Takt eine Stufe, aber nur so breit, wie Logik da ist |
| Exaktheit | Gleitkomma üblich; exakte $\mathbb Z[\omega]$-Kerne mit 64-Bit-Ganzzahlen sind möglich | exakt von Haus aus, jede Bitbreite wählbar |
| Guards | in Software um den Kern herum (Prüfung vor/nach jedem Durchlauf) | als Logik im Kern, Takt für Takt |
| Einstieg | sofort: Qiskit Aer mit GPU oder NVIDIA cuQuantum (cuStateVec). Braucht eine NVIDIA-Karte, unter Windows über WSL2 | Simulation sofort am PC (Icarus Verilog), Platine später (50–300 €) |
| Nachweis für den Companion | Ergebnisse sind Software-Läufe wie heute | ein synthetisierbarer, taktgenauer Kern, dessen Verhalten gegen MMA geprüft ist, wie bei der Bandmaschine |

**Empfehlung.** (1) HDL-Kern mit Band als Eingabe in der Simulation weiterbauen, weil er Bandformat und Semantik festlegt und mit Guards prüfbar ist.
(2) Danach die GPU-Ausführung für dasselbe Band über Qiskit Aer-GPU anbinden; das ist wenig Arbeit und bringt Größe.
(3) Einen eigenen GPU-Kern für die exakte $\mathbb Z[\omega]$-Darstellung erst schreiben, wenn wir exakte Ergebnisse
über ~10 Qubits brauchen. (4) FPGA-Platine erst, wenn der Kern in der Simulation stabil ist. **Offen:** Welche
Grafikkarte hast du? Für die GPU-Etappe braucht es eine NVIDIA-Karte (CUDA).

**Wie die Guards an die GPU andocken.** Der Host zerlegt das Programm in Blöcke. Vor jedem Block prüft MMA die
Prämissen und das Budget, nach jedem Block prüft eine kleine GPU-Reduktion den Zustand (Norm = 1 innerhalb der
ausgewiesenen Toleranz, bei exakter Darstellung: kein Überlauf). Fällt eine Prüfung, wird der Block verworfen und der
Status ist `guard`. Der Beleg enthält Blockgrenzen, Prüfwerte und den Hash des Zustands nach jedem Block.

## 5. Kompression über Hilbert-Shift und Dixon-Algebra

Die Frage war, ob uns der Turm HS(0)…HS(n) und die Dixon-Algebra $\mathbb C\otimes\mathbb H\otimes\mathbb O$ stark
komprimieren lassen. Die ehrliche Antwort: **für bestimmte Zustandsklassen ja, für allgemeine verschränkte Zustände
nein.**

**Warum nicht allgemein.** Die Dixon-Algebra hat 64 reelle Dimensionen, also 32 komplexe; das ist genau ein Register
aus 5 Qubits. Der Turm verdoppelt in jeder Stufe ($C_n = 2^n$, Atlas r26). Er *ist* also das exponentielle Wachstum,
in algebraischer Form, und nimmt es nicht weg. Könnte eine feste Algebra jeden n-Qubit-Zustand mit polynomial vielen
Zahlen beschreiben und Gatter darauf effizient rechnen, wären Quantenrechner klassisch effizient simulierbar. Das gilt
als ausgeschlossen (unbewiesen, aber allgemein erwartet), und wir sollten nichts bauen, was davon abhängt.

**Wo Kompression trägt.** Sie trägt, wenn der Zustand durch die *Regel* beschrieben ist, die ihn erzeugt hat, statt
durch seine Amplituden:

| Zustandsklasse | Speicher statt 2ⁿ | Bezug zum Projekt |
|---|---|---|
| Produktzustände (Kopien unabhängig) | n kleine Blöcke | HS(7), HS(8) als Kopien von HS(6), solange die Kopien nicht verschränkt sind (r25, r26) |
| Symmetrischer Unterraum (alle Kopien gleichberechtigt) | $\binom{n+d-1}{d-1}$ statt $d^n$, für $d=2$ nur $n+1$ | Generationen als vertauschbare Kopien; Triplett/Singulett aus r25 ist genau so eine Zerlegung |
| Zustände in einer Darstellung einer Symmetriegruppe | Dimension der Darstellung | z. B. $G_2$ auf $\mathbb O$ (7-dim.), $\mathfrak{g}_2\oplus\mathfrak{su}(3)$ aus H128, sofern die Rechnung die Darstellung nicht verlässt |
| Stabilisatorzustände (nur Clifford-Gatter) | etwa $2n^2$ Bits (Gottesman-Knill) | jedes Programm ohne T-Gatter; mit wenigen T-Gattern wächst der Aufwand nur mit deren Zahl |
| Wenig verschränkte Ketten | Matrixproduktzustände, $n\cdot\chi^2$ | Bandstruktur: eine 1-D-Kette mit begrenzter Verschränkung zwischen Nachbarn |

**Wie man das in der Architektur nutzt.** Das Zustandsrechenwerk bekommt *Darstellungsmodi*, und die Guard-Einheit
wacht darüber, dass ein Modus nur so lange gilt, wie das Programm ihn nicht verlässt:

1. **Dixon-Register:** ein fester Block mit 64 reellen (exakten) Koeffizienten und der Oktonionen-Multiplikationstafel
   als feste Verdrahtung (Vorzeichen- und Indextabelle, 8×8). Das ist in HDL ideal, weil die Tafel konstant ist.
2. **Kopien-Modus:** mehrere Dixon-Register nebeneinander, solange nur Operationen *innerhalb* einer Kopie oder
   *Vertauschungen* von Kopien vorkommen. Ein verschränkendes Gatter zwischen Kopien löst einen `guard` aus, und der Host
   wechselt kontrolliert in den vollen Zustandsvektor.
3. **Symmetrie-Modus:** Zustand in der Basis eines Symmetrie-Unterraums, Gatter als vorab berechnete kleine Matrizen.
   Ein Gatter, das die Symmetrie bricht, ist ein `guard`.
4. **Voller Zustandsvektor** als Rückfallebene (GPU).

Der Moduswechsel ist damit selbst ein QAM-Vorgang: Er hat eine Prämisse („Programm bleibt in der Klasse“), MMA prüft
sie, und der Beleg hält fest, in welchem Modus gerechnet wurde. Ob die physikalisch interessanten Rechnungen des
Projekts in einer dieser Klassen bleiben, ist eine offene Frage und keine Annahme dieses Plans.

## 6. Etappen

| Stufe | Inhalt | Prüfung | Ergebnis |
|---|---|---|---|
| **0** (fertig) | exakte Zwei-Qubit-Einheit, Clifford+T, Status-Register | HDL = exakte Python-Referenz, = Qiskit, = Wolfram (Stichprobe) | `qam/examples/coprocessor/` |
| 1 | Band als Eingabe: Bandformat mit Kopf, Bandspeicher, Kopfzähler, `HALT`, Stopgründe wie `RUN_TAPE`; Rechenwerk weiter mit 2 Qubits | gleiche Bänder in HDL und Python-Referenz, Stopgründe einzeln getestet | Prozessor rechnet selbstständig auf einem Band |
| 2 | `MEASURE`, `JUMP_IF`, `LOOP`/`RETURN` über die Steuerung aus `tape_core.sv`; MML-Auftrag `RUN_QTAPE`, MMA-Beleg in `readout_db` | HDL-Vergleichssuite mit MMA, Beleg-Replay per Hash | Verbindung zu 19K–19Q, Coprozessor ist ein MMA-Werkzeug |
| **2s** (fertig, 27.11.2026) | Software-Referenz der Steuerbefehle vor dem HDL: Band mit `ROT`, `HC`, `MEASURE`, `JUMP_IF`, `LOOP`/`END`, Rückführung über Register, Bandwechsel `ADD`/`DROP` (Spin-Bänder), `NOISE`; Protokoll je Zelle mit Begründung und Hash. Gleitkomma, nicht exakt | Bausteine gegen Qiskit, Schleife L3 aus k395, Guards einzeln | `qam/examples/coprocessor/stufe2/`; ersetzt weder Stufe 1 noch Stufe 2 in HDL |
| 3 | n Qubits als Parameter, Zustand im Speicher statt in Registern, kanonische Form (minimales k), `CCX` | wie Stufe 0, plus Yosys-Zellzahlen | synthetisierbarer Kern bis ~10 Qubits |
| 4 | GPU-Ausführung: Band und Zustand im Grafikspeicher, Gatter zunächst über Qiskit Aer-GPU, derselbe Bandsatz | Kreuzvergleich GPU ↔ HDL ↔ Wolfram auf denselben Bändern | große Läufe |
| 5 | Darstellungsmodi (Dixon-Register, Kopien, Symmetrie) mit Modus-Guards | gegen vollen Zustandsvektor | Kompression, wo sie trägt |
| 6 | FPGA-Platine | gleiche Suite auf echter Hardware | messbare Takte |
| optional | eigener exakter GPU-Kern | gegen Stufe 3 | exakte Läufe > 10 Qubits |

## 7. Die erste Baustufe

[`qam/examples/coprocessor/hdl/qstep2.sv`](../../qam/examples/coprocessor/hdl/qstep2.sv) hält zwei Qubits, also vier
Amplituden mit je vier ganzzahligen Koeffizienten und einem gemeinsamen $k$. Pro Takt führt sie ein Gatter aus.
Sind nach einem Schritt alle Koeffizienten gerade und $k\ge2$, kürzt sie durch 2. Überläuft ein Koeffizient die
Wortbreite W, stoppt sie mit `guard` und lässt den Zustand unverändert; ein unbekannter Opcode gibt `reject`.

Prüfung (`python -m qam.examples.coprocessor.check --cases 2000 --seed 1`, Ausgabe in
[`check_out.txt`](../../qam/examples/coprocessor/check_out.txt)):

- 2005 Fälle (2000 Schaltungen mit bis zu 40 Gattern, darunter lange H-T-Ketten, plus 5 mit unbekanntem Opcode):
  HDL-Ausgabe bitgenau gleich der exakten Referenz, für W = 16, 4 und 3.
- Alle `continue`-Fälle stimmen mit dem Qiskit-Statevector überein, größte Abweichung $3\cdot10^{-15}$ (Rundung von
  Qiskit, nicht der HDL).
- Guard-Fälle: 1 bei W = 16 (die Kette mit 60 H-T-Paaren), 4 bei W = 4, 5 bei W = 3; HDL und Referenz stoppen jeweils
  am selben Gatter.
- Wolfram (exakte Kronecker-Matrizen) für sechs Fälle, darunter die Kette aus 20 H-T-Paaren mit $k = 12$: exakte
  Differenz null ([Skript](../../qam/examples/coprocessor/wolfram/qstep2_exakt.wl),
  [Ausgabe](../../qam/examples/coprocessor/wolfram/qstep2_exakt_out.txt)).

**Grenzen.** Die Darstellung ist nicht kanonisch: Ein durch $\sqrt2$ (statt durch 2) teilbarer Zustand wird nicht
gekürzt, gleiche Zustände können also verschiedene Koeffizienten haben. Die Referenz in Python folgt derselben Regel
und ist deshalb keine unabhängige Prüfung der Semantik; diese Rolle haben Qiskit und Wolfram. Keine Synthese, keine
Taktmessung auf Hardware.

**Werkzeugwahl.** Qiskit für die Schaltungssemantik (Statevector), Wolfram für den exakten Vergleich, Icarus Verilog
für die Simulation. Ein MMA-Lauf entfällt in Stufe 0, weil es noch keinen MML-Auftrag für Bänder mit Quantenbefehlen gibt (`RUN_QTAPE`, Stufe 2).

## 8. Schritt für Schritt: Wie der Prozessor entsteht (ohne HDL-Vorwissen)

**Was HDL ist.** Eine Hardwarebeschreibungssprache wie SystemVerilog beschreibt keine Abfolge von Befehlen, sondern
eine *Schaltung*: Register, die bei jeder Taktflanke einen neuen Wert übernehmen, und Logik dazwischen, die aus den
alten Werten die neuen berechnet. Alles läuft gleichzeitig. In `qstep2.sv` ist `always @(posedge clk)` die Stelle,
an der bei jedem Takt der neue Zustand aus dem alten und dem Befehl entsteht.

**Die vier Werkzeuge** (alle kostenlos, unter Windows am einfachsten als Paket
[OSS CAD Suite](https://github.com/YosysHQ/oss-cad-suite-build)):

1. **Icarus Verilog** (`iverilog`, `vvp`): simuliert die Schaltung am PC. Das reicht für die Stufen 0 bis 5.
2. **GTKWave**: zeigt die Signale als Zeitdiagramm (Datei `.vcd`), wie ein Oszilloskop.
3. **Yosys**: übersetzt die Beschreibung in Gatter und zählt sie (wie groß würde der Chip?).
4. **nextpnr** plus Platine: erst für Stufe 6.

**Eine erste Übung (etwa 30 Minuten).**

1. OSS CAD Suite entpacken, im Ordner `start.bat` ausführen; damit stehen die Befehle im Terminal bereit.
2. Im Repo die vorhandene Bandmaschine prüfen:
   `python -m qam.examples.zuse_machine.hdl.check --report build/hdl.md --wave build/hdl.vcd`
3. `gtkwave build/hdl.vcd` öffnen, links `clk`, `state`, `head`, `tape` anklicken. Man sieht, wie sich der Kopf
   Takt für Takt bewegt.
4. Die neue Stufe prüfen (braucht zusätzlich `pip install qiskit`):
   `python -m qam.examples.coprocessor.check --cases 200`
5. In `qstep2.sv` eine Zeile ändern, etwa `rot = 1` beim T-Gatter auf `rot = 2`, und Schritt 4 wiederholen. Die
   Prüfung meldet den ersten falschen Fall. So sieht man, dass die Prüfkette Fehler findet.

**Wie eine neue Stufe entsteht.**

1. Wir schreiben vorher fest, was die Stufe können soll und woran wir das prüfen (Referenz, Qiskit, Wolfram, MMA).
2. Claude schreibt den HDL-Code, die Testbench und das Prüfskript und lässt alles in der Cloud laufen.
3. Du lässt die Prüfung bei dir laufen (ein Befehl) und schaust dir bei Interesse die Signale in GTKWave an.
4. Die Ergebnisse und Ausgaben kommen ins Repo, Änderungen über einen PR, gemergt mit deinem Okay.
5. Wenn eine Stufe stabil ist, zählt Yosys die Gatter; ab Stufe 6 kommt die Platine.

**Was du entscheidest und was Claude macht.**

| Du | Claude |
|---|---|
| welche Rechnungen der Prozessor können soll (Gattersatz, Größe, exakt oder schnell) | HDL-Code, Testbenches, Prüfskripte, Berichte |
| welche Grafikkarte/Platine (falls gekauft wird) | Vergleich mit Qiskit, Wolfram, MMA |
| ob ein Darstellungsmodus (Abschnitt 5) physikalisch gerechtfertigt ist | Umsetzung des Modus und seines Guards |
| Merges | PRs und Laufprotokolle |

**Platine für später.** Für den Einstieg eignet sich eine Platine mit Lattice ECP5 oder iCE40 (offene Werkzeuge,
50–150 €) oder Xilinx Artix-7 (z. B. Arty A7, mit der kostenlosen Vivado-Version). Kaufen erst ab Stufe 6.

## 9. Offene Punkte

- Grafikkarte vorhanden, und ist es eine NVIDIA-Karte?
- Soll Stufe 3 beliebige Drehwinkel enthalten (dann nicht mehr exakt) oder bei Clifford+T bleiben?
- Erledigt durch Test H137 (Bandschaltung auf Überlagerungen, PR #317): Die Qiskit-Bandschaltung ist ein
  klassisch-reversibles Orakel $\lvert x,0\rangle \mapsto \lvert x,f(x)\rangle$. Sie ist auf Überlagerungen linear
  und phasentreu, aber der Folgezustand allein ist nicht kohärent, weil die Eingabe als Kopie stehen bleibt, und das
  Beispielprogramm ist nicht injektiv. Mit umkehrbarer Regeltabelle und Bennett-Schritt entsteht ein sauberer unitärer
  Schritt. Es fehlen ein Amplituden mischender Schritt (Hadamard-artig) und eine Kopplung zwischen Zellen ohne Kopf.
  **Folge für den Plan:** Die Bandmaschine bleibt in Stufe 2 die *klassische* Steuerung, die das Band liest; die
  Überlagerungen trägt das Rechenwerk. Genau die beiden fehlenden Bausteine liefert es schon: `H` mischt Amplituden,
  `CX` koppelt Qubits ohne Kopf. Eine reversible Steuerung (Bennett) bleibt eine spätere Option.
- Die Spinorband-Hypothese STH und die HC-Rückkehr bleiben Voraussetzungen des Companion. Der Coprozessor ist ein
  Werkzeug und kein Beleg für sie.
