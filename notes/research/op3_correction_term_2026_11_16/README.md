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
