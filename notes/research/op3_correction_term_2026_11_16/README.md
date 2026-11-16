# OP3: Zeitabhängiger Korrekturterm, rückwärts rekonstruiert – Ergebnis der ersten Rechnung (Erkundung, nicht blind)

16. November 2026. Idee des Autors; Methode vor der Rechnung festgelegt in `Methoden_Notiz.md` (85e975b, Nachtrag zur Benennung des Ziels
f838987). Skript `correction_term.py`, Ausgaben `run/correction_term_stdout.txt` und `run/correction_term_result.json`. Keine H-Nummer.

## Ergebnis in Zahlen (beste Lösung je Lauf, 20 Zufallsstarts)

| Start | Art | V0 Haupt (A) | V1 glatt (A) | V2 τ = π/3 (A) | V2 τ = 3π (A) |
|---|---|---|---|---|---|
| S1 Spin-1-Dreieck | unitär | 9·10⁻⁵ | 9,7·10⁻³ | 8·10⁻⁵ | 1,56 (nicht konvergiert) |
| S1 | dissipativ | 5,6·10⁻³ | 6,0·10⁻² | 5,6·10⁻³ | 2,95 (nicht konvergiert) |
| S2 flacher Oktant | unitär | 4,8·10⁻³ | 1,4·10⁻² | 1,4·10⁻² | 2,77 (nicht konvergiert) |
| S2 | dissipativ | 4,9·10⁻² | 6,6·10⁻² | 4,9·10⁻² | 2,81 (nicht konvergiert) |

Alle Läufe erreichen das Ziel im Spielraum (319 von 320 Starts). Fubini–Study-Abstand zum Ziel: S1 0,0067, S2 0,1178.

## Formmerkmale
- **M1 Richtung (unitär):** Dipolanteil 34 % / 48 % / 17 % / 51 % (S1) und 15 % / 31 % / 10 % / 53 % (S2) über die Varianten. **Nicht stabil.**
- **M2 Charakter:** Beide Arten erreichen das Ziel; Dissipation ist nicht nötig. Die Kosten sind nicht vergleichbar (verschiedene Funktionale).
  Dissipativ ist die Mischung im Hauptlauf und bei τ = π/3 für **beide** Starts gleich: 91 % J₊, 9 % J₋² (J₋² schiebt Gewicht von m = +1 direkt nach
  m = −1, zum Elektron). In der glatten Variante weicht sie ab (S1: 34 % J₊, 57 % J₊²; S2: 70 % J₊, 22 % J₊²). **Nicht stabil.** Die Gleichheit
  zwischen S1 und S2 ist geometrisch erklärt: Beide liegen auf dem Koide-Kreis nahe dem Ziel, ihre Verschiebungen zeigen fast in dieselbe Richtung
  (Δp ∝ (0,233; −1; 0,767) bzw. (0,249; −1; 0,751)), die Tangente des Kreises; die billigste nichtnegative Zerlegung in Übergänge ist dann dieselbe.
- **M3 Zeitverlauf:** Spektralspitzen bei 2 (Dipol) und 4 (Quadrupol) = Aufspaltungen von H₀; Hülle im Hauptlauf nahezu konstant, Schwerpunkt bei
  t/τ ≈ 0,5; bei τ = π/3 Spitze bei 6 = Frequenzauflösung. **Alles vorab benannte Artefakte** (Resonanz, Geodätenform).
- **M4 Integral:** Pulsfläche S1 0,0155, S2 0,123 (V0). **Kein Treffer** in der Konstantenliste (≤ 10⁻³); am nächsten S2 0,123 gegen γ_M/2 = 0,1188
  (3,8 %), Fubini–Study-Abstand S2 0,1178 gegen γ_M/2 (0,8 %); beide außerhalb des Kriteriums.

## Technisches Problem
Die Läufe mit τ = 3π sind **nicht konvergiert**: Ein längeres Fenster kann nie mehr Eingriff brauchen als ein kürzeres (man kann warten), trotzdem
liegt A dort um das Hundert- bis Zehntausendfache höher; die Spektren zeigen das stehengebliebene Zufallsrauschen des Startfelds. Auch die große
Streuung über die Starts im Hauptlauf (bis 2,4) zeigt, dass das Minimum nicht sauber getroffen wird. Die Robustheitsprüfung V2 ist damit für τ = 3π
nicht auswertbar.

## Bewertung nach der Methoden-Notiz
- **Kein Befund.** Kein Merkmal ist über V1–V3 und beide Starts stabil und zugleich kein vorab benanntes Artefakt.
- Der minimale Eingriff sieht so aus, wie ein kürzester Weg zwischen zwei nahen Punkten auf dem Koide-Kreis aussieht: Er folgt der Tangente des
  Kreises, schwingt mit der freien Entwicklung und hat keine Größe, die einer Kernkonstante entspricht.
- Inhaltlich bestätigt die Rechnung zwei bekannte Zahlen in neuer Form: Vom Spin-1-Dreieck aus ist der nötige Eingriff winzig (Rest 0,012), vom
  Oktanten aus etwa fünfzigmal größer (Biegung 0,119).
- Offen: eine saubere Wiederholung der nicht konvergierten Varianten (Startfeld nahe null statt Zufallsrauschen), als gekennzeichneter Nachtrag zur
  Methode. Erst danach ist die Robustheitsprüfung vollständig.

OP3 offen; keine H-Nummer vergeben (H111 frei).

## Nachlauf N1 (τ = 3π, Startfeld nahe null; Nachtrag N1 in der Methoden-Notiz, 0588c5d)
Ausgaben `run/correction_term_nachlauf_stdout.txt`, `run/correction_term_nachlauf.json`; analytische Kontrolle `mix_analytic.py`,
`run/mix_analytic_stdout.txt`.

| Start | Art | A (τ = 3π, N1) | A (τ = π, V0) | Streuung über Starts | Merkmal |
|---|---|---|---|---|---|
| S1 | unitär | 4,3·10⁻⁵ | 9·10⁻⁵ | 0,03 | Dipol 41 %; Pulsfläche 0,0189 |
| S1 | dissipativ | 5,60·10⁻³ | 5,6·10⁻³ | 0,000 | 91 % J₊, 9 % J₋² |
| S2 | unitär | 1,65·10⁻³ | 4,8·10⁻³ | 0,001 | Dipol 7 %; Pulsfläche 0,1244 |
| S2 | dissipativ | 4,99·10⁻² | 4,9·10⁻² | 0,002 | 91 % J₊, 9 % J₋² |

- **Jetzt konvergiert:** Streuung über die Starts nahezu null, und das längere Fenster braucht wie erwartet höchstens so viel Eingriff wie τ = π.
  Die Robustheitsprüfung V2 ist damit vollständig.
- **M1 Richtung:** Dipolanteil über alle Varianten 7 % bis 53 %, je nach Start verschieden. Weiter **nicht stabil**.
- **M2 dissipative Mischung:** 91 % J₊ / 9 % J₋² jetzt in V0, V2 (π/3 und 3π) und für beide Starts, nur in V1 (glatt) anders. **Sie ist
  analytisch festgelegt:** Mit nur J₊ und J₋² bestimmt die Richtung der Verschiebung Δp die beiden Raten eindeutig (Restfehler 10⁻¹⁶); das ergibt
  91,2 % (S1) bzw. 90,9 % (S2). Die Richtung ist die Tangente des Koide-Kreises, die Raten hängen nur an den Populationen. Kein Befund über die
  Dynamik, sondern Geometrie (und das L1-Funktional wählt die sparsamste Zerlegung).
- **M4:** Pulsfläche S2 0,1244 gegen γ_M/2 = 0,1188 (4,7 %); kein Treffer.

## Gesamtbewertung nach Nachlauf
**Kein Befund.** Die Rechnung hat etwas anderes gezeigt, das als Ergebnis festgehalten wird: In der Darstellung auf S (r16.8/r16.9) hängen K und φ nur
an den Populationen, und kein natives Element des Bestands verschiebt Populationen (die Zeitverschiebung ist diagonal, die Frame-Abbildungen wirken
auf S skalar oder antilinear). Jeder Korrekturterm ist dort fremd, und sein minimaler Verlauf ist reine Geometrie: die Bewegung entlang der Tangente
des Koide-Kreises. **In dieser Darstellung kann die Methode grundsätzlich nichts über eine Dynamik verraten.**

Eine Darstellung, in der das anders wäre, ist die mit Verbindung statt Zustand: der bewachte Kern (H102) ändert nicht die Zustände, sondern die
Berry-Verbindung auf der Generationskugel. Ein zeitabhängiger Korrekturterm müsste dann eine zeitabhängige **Verbindung** (ein Fluss, der sich mit der
Zeit aufbaut) sein, und seine Form könnte Struktur zeigen (Verteilung, Ort, Zeitverlauf des Flusses). Das wäre eine neue Methoden-Notiz.

OP3 offen; H111 frei.

## Methoden-Notiz 2: zeitabhängige Verbindung – Ergebnis
Methode `Methoden_Notiz_Verbindung.md` (e8370d7) mit Nachtrag N2 (e4f7b30), Skript `connection_flow.py`, Ausgaben `run/connection_flow_stdout.txt`,
`run/connection_flow.json`. Ziel: ΔΦ = 0,118724 Berry-Fluss aus dem Oktantendreieck T bringen; K = 2/3 bleibt dabei exakt.

| Gitter (Knoten) | V0 Randlösung: Breite des geleerten Saums | Kosten W2 | Lage der geleerten Knoten (Winkel zur Zyklusachse) | V1 Kosten (Kantenlänge²) |
|---|---|---|---|---|
| 3 (642) | 0,081 rad | 7,6·10⁻⁵ | 31,3° bis 54,7° | 4,4·10⁻⁶ |
| 4 (2562) | 0,066 rad | 1,08·10⁻⁴ | 33,1° bis 54,7° | 5,7·10⁻⁷ |
| 5 (10 242) | 0,060 rad | 1,03·10⁻⁴ | 33,0° bis 54,7° | 7,3·10⁻⁸ |

| Kern-Konfiguration (exakter W2, LP) | Gitter 3 dicht | Gitter 3, Schranke 0,6 | Gitter 4, Schranke 0,6 |
|---|---|---|---|
| K-A: flussfreie Kappe, Fluss am Gegenpol (H102) | 0,0533 | 0,0533 | 0,0295 |
| K-B: flussfreie Kappe, Fluss gleichmäßig verteilt | 0,0275 | 0,0275 | 0,0154 |
| Verhältnis K-A / Rand | 702 | 702 | 273 |
| Verhältnis K-B / Rand | 363 | 363 | 143 |

- **N1 (wo verlässt der Fluss T?):** über die Ränder. Es bildet sich ein **flussfreier Saum** entlang der drei Kanten des Dreiecks (Breite gegen 0,05 bis
  0,06 rad, gut 3°; Mittelpunkt-zu-Kante 35,3°, Ecken 54,7°), **kein Kern in der Mitte**. Das ist die vorab genannte Erwartung.
- **N2 (wohin?):** direkt jenseits des Randes, im Abstand gleich dem Randabstand.
- **N3 (Zeitverlauf):** analytisch gleichförmig (Verschiebungsinterpolation).
- **N4 (Kosten):** Die Kern-Konfiguration von H102 kostet mindestens das 270-fache der Randlösung (Gitter 4; die Kern-Kosten sinken mit der
  Verfeinerung noch, das Verhältnis bleibt über 100). Gegenpol (K-A) kostet etwa doppelt so viel wie gleichmäßige Verteilung (K-B), passend zu
  „B ist das Energieminimum“ in der Kern-Notiz. V1 (Stromnorm ohne Gewichtung) ist entartet: Die Kosten gehen mit der Verfeinerung gegen null, der
  Strom sitzt nur auf den Randkanten.
- Die Schranke 0,6 rad ändert auf Gitter 3 nichts (Kaskaden aus kurzen Schritten reichen); die Kern-Werte sind also nicht durch die Schranke
  verfälscht.

**Bewertung nach Abschnitt 6:** Kein Befund im Sinne einer unerwarteten Struktur; die Randlösung bestätigt sich über V0, V1 und drei Gitter. Das ist
ein **Ausschluss:** Ein lokaler, sparsamer Fluss erzeugt den Kern von H102 nicht; er leert einen Saum an den Kanten. Der Kern braucht einen nicht
lokalen Grund (Umkehrwalze als feste Regel) oder eine zusätzliche Bedingung.

**Eine Bedingung, die den Kern erzwingen würde (Lesart, nicht gerechnet):** Sind die Kanten von T **undurchlässig** (etwa weil sie Geodäten zwischen
festen Auslesezuständen sind), kann der Fluss T nicht über den Rand verlassen. Dann bleibt nur ein Abfluss durch eine **Punktierung** im Inneren, also
genau die Lesart „removed“ aus Faden 1 der Kern-Notiz (S³ ∖ B_ε(K)). Ob ein undurchlässiger Rand im Bestand begründet ist, wäre die nächste Frage;
das wäre eine eigene Methoden-Notiz.

OP3 offen; H111 frei.
