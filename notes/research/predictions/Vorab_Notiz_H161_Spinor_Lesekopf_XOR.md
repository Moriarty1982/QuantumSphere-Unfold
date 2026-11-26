# Vorab-Notiz H161: Ist der Spinor ein zweigeteilter Lesekopf, dessen Auslesen per XOR den Datenstrom rekonstruieren (RAID5)?

**Stand:** 2026-11-26, vor der Rechnung festgelegt und vor dem ersten Skriptlauf committet. **Überwiegend nicht blind** (siehe „Vorab offengelegt“).
Anlass: Autor, 26.11.2026, 07:50 und 07:59 UTC: bei kugelförmigem Kern zeige sich der gemittelte Umlauf „als spinor auf der oberfläche“, als „zweigeteillter
lesekopf der über das selbe band fährt und dessen aulesungen (evtl. xor zueinander genommen) den ursprünglichen datenstrom rekonstruiert … das spinor wäre quasi ein
RAID5“; liegen die Punkte nicht gegenüber, sei eine Transformation zu suchen, die die Geometrie so verbiegt, dass die Bahnen wieder wie Kreise aussehen, und
die Paritätsrekonstruktion erzeuge „ein virtuelles drittes objekt“. Freigabe zum Rechnen 09:25 UTC.
Skripte **k352** (Python mit **Qiskit** für die Messabläufe und sympy/numpy für die Algebra) und **k352b** (Wolfram Language, unabhängig, exakt).
Werkzeugwahl: Qiskit, weil die Aussage ein explizit definierter Messablauf auf einem oder zwei Qubits ist; Wolfram für die exakte Algebra (Paritäten, Möbius-Abbildung).
Kein HDL/MMA-Vergleich: `RUN_TAPE` und die SystemVerilog-Steuerung werden nicht geändert, und es wird keine Aussage über deren Übergangsregeln gemacht. „Band“ ist hier
das Bild des Autors, nicht das QAM-Band. Kein Guard wird berührt.

## Vorwissen geprüft
- **H137** (k310): Die Bandschaltung wirkt auf Überlagerungen linear und phasentreu, bleibt aber klassisch (Permutation der Basis).
- **r42/r43** (Projektor ½(1 + iL_u), links/rechts), k253/k292 (Hopf-Sphäre, cos ϑ = (a² − b²)/(a² + b²)), H159 (Fixpunktmenge von J).
- Topologie-Notiz `op3_topology_core_2026_11_16`, Screening `openai_math_screening_2026_11_23` (Stichwortsuche „Peres“, „Mermin“, „Kontextualität“): keine Rechnung
  zu Paritätsprüfungen an Spinoren.
- Suche nach „RAID“, „XOR“, „Parität“ zusammen mit „Spinor“ und nach „Möbius“, „Aberration“ unter `notes/research`, `wiki` (26.11.): keine Fundstelle.

## Übersetzung (gesetzt)
- Spinor = Zustand eines Qubits; Punkt auf der Kugel = Bloch-Vektor n = ψ†σψ. Eine Auslese = Messung einer Pauli-Größe mit Ergebnis-Bit.
- RAID5 mit drei Platten: jede Platte ist das XOR der beiden anderen.
- Lesart 1 (ein Kopf, zwei Hälften): ein Spinor, gelesen in X und in Z; rekonstruiert werden soll Y.
- Lesart 2 (zwei Köpfe gegenüber): zwei Qubits in einem Bell-Zustand; die drei „Platten“ sind die gemeinsamen Auslesen XX, ZZ, YY.

## Hypothese H161
Die Auslesen eines Spinors verhalten sich wie ein RAID5: Aus zwei Auslesen folgt die dritte per XOR, es gibt einen zugrunde liegenden Datenstrom, und für nicht
gegenüberliegende Punkte stellt eine Verbiegung der Geometrie die Gegenüberlage her, wobei ein drittes Objekt entsteht.

## Entscheidungskriterien
- **K-a (Etiketten):** Die Pauli-Etiketten ohne Phase bilden GF(2)², und X ⊕ Z = Y, sodass je zwei das dritte geben: bestätigt, sonst widerlegt.
- **K-b (zwei Köpfe):** In Qiskit für die vier Bell-Zustände nacheinander XX, ZZ und YY als Paritäten messen (4096 Läufe je Zustand). Ist das YY-Bit in allen
  Läufen XX-Bit ⊕ ZZ-Bit ⊕ c mit festem c: bestätigt. Sonst widerlegt.
- **K-c (ein Kopf):** In Qiskit auf einem Qubit nacheinander X, Z, Y messen, für 20 Zufallszustände je 4096 Läufe. Trifft X-Bit ⊕ Z-Bit (⊕ festes c) das Y-Bit in
  mehr als 90 % der Läufe: bestätigt. Liegt die Trefferquote bei 50 % ± 5 %: widerlegt. Dazwischen: trägt teilweise.
- **K-d (Datenstrom):** Für die neun Größen des Peres–Mermin-Quadrats alle 512 Belegungen mit ±1 durchzählen. Gibt es eine Belegung, die alle sechs Paritätsprüfungen
  erfüllt: bestätigt (ein klassischer Datenstrom existiert). Höchstens fünf von sechs: widerlegt. Dazu in Qiskit die sechs Prüfungen messen.
- **K-e (Verbiegung und drittes Objekt):** Zu zwei verschiedenen Punkten der Kugel gibt es eine Möbius-Abbildung (SL(2,ℂ)), die sie auf Gegenpunkte legt und Kreise
  auf Kreise abbildet; geprüft exakt für den symmetrischen Fall und numerisch für 1000 Zufallspaare und je einen Zufallskreis. Zusätzlich wird berichtet, welche
  Invariante der zwei Punkte dabei erhalten bleibt. Existenz und Kreistreue: bestätigt, sonst widerlegt.
- **Gesamturteil:** bestätigt nur, wenn K-a bis K-e bestätigt sind. „Trägt teilweise“, wenn K-a, K-b und K-e bestätigt sind und K-c oder K-d scheitert.

## Vorab offengelegt (kein Teil der Vorhersage)
Fast alles hier ist Lehrbuchwissen, das mir beim Aufschreiben bekannt war:
- Pauli-Etiketten als Paare (x|z): X = (1,0), Z = (0,1), Y = (1,1). K-a steht fest.
- Für Bell-Zustände gilt (XX)(ZZ) = −YY. K-b steht fest, mit c abhängig von der Vorzeichenkonvention der Bits.
- X, Z, Y eines einzelnen Qubits vertauschen nicht; nach der X- und der Z-Messung ist das Y-Bit gleichverteilt. K-c steht fest.
- Das Peres–Mermin-Quadrat hat keine klassische Belegung (Produkt der sechs Bedingungen −1). K-d steht fest.
- Möbius-Abbildungen sind kreistreu und dreifach transitiv; als Lorentz-Transformation der Himmelskugel ist das die Aberration. Zwei Lichtstrahlen im Winkel θ liegen
  im Schwerpunktsystem gegenüber, mit β = cos(θ/2) bei gleicher Energie, und die erhaltene Größe ist die invariante Masse M² = 2E₁E₂(1 − cos θ). K-e steht fest.
Offen ist die Umsetzung als Schaltung, der Wert von c je Bell-Zustand und ob der Überschlag in allen Punkten stimmt.

## Vorhersage
- K-a: **bestätigt.** K-b: **bestätigt.** K-c: **widerlegt.** K-d: **widerlegt.** K-e: **bestätigt.**
- Gesamt: **trägt teilweise.** Das RAID-Bild gilt innerhalb eines Satzes vertauschender Auslesen und für die Etiketten, nicht für einen einzelnen Kopf und nicht
  für alle Auslesen zusammen.

## Grenzen (vorab)
Die Übersetzung Spinor = Qubit und Platte = Pauli-Auslese ist gesetzt. Idealer Simulator ohne Rauschen. Keine Größe des Companion geht ein; eine Zuordnung zu Kern,
Band oder Frames des Modells wird nicht behauptet. OP1 bis OP5 bleiben offen.
