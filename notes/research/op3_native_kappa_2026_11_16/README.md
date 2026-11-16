# OP3: native Kohärenz κ für die Querdephasierung um die Zyklusachse (Erkundung, nicht blind)

16. November 2026. Auftrag des Autors: „Native κ suchen“, nach H110. Ziel aus der Betrachter-Erkundung
(`../op3_frame_algebras_observer_2026_11_16/`, Nachtrag): Eine Querdephasierung um die Zyklusachse mit $\kappa^2=0{,}880706$ ($\kappa=0{,}938459$)
gibt $K=2/3$ exakt und $\varphi=0{,}666665$. Skript `native_kappa.py`, Ausgabe `run/native_kappa_stdout.txt`.

**Nicht blind, keine H-Nummer:** Der Zielwert war bekannt, und jeder Kandidat lässt sich im Kopf auswerten. Die Liste steht vor dem Lauf im Skript;
sie ist trotzdem eine nachträgliche Suche. Ein Treffer wäre kein Beleg.

## Vorwissen geprüft
- r16.9(d): Rückwärtssuche mit 24 vorab gelisteten Kernkonstanten ($\gamma_M$, $\gamma_T$, $\gamma_L$, $\beta_{\rm sym}$, $\eta_{\rm sym}$, Brüche,
  Wurzeln) gegen fünf aus der Biegung abgeleitete Größen, Toleranz 0,5 %: kein Treffer. Diese Konstanten werden hier nicht noch einmal abgesucht,
  nur die Dephasierungs-Lesarten.
- r23.4 und v4.9.0-r28.2(b): Dephasierung über viele Frequenzen ∝ $N^{-1/2}$; $P$ nur im Grenzwert.
- r16.9(b): Autokorrelation nach einem Drittel der Periode hat bei Koide den Betrag $1/\sqrt2$.
- r22 (Konvention F): Sichtbarkeit $|b|=1/\gamma$, Kompensator-Eigenwert $p_+$; r10: Kick-Lesart $\cos^2(\pi/6)=3/4$.
- H110 und Nachtrag: Aufzeichnung $o$, $Fo$ gibt $\kappa=1/\sqrt3$.

## Ergebnis

**1. Welche Kanäle passen der Form nach.**

| Kanal | Längsanteil | Queranteil | passt |
|---|---|---|---|
| Zwirbeln mit $n\cdot\sigma=(R+T+J_B)/\sqrt3$, Wahrscheinlichkeit $p$ | fest | $\times(1-2p)$ | ja |
| die drei Frame-Abbildungen gleich gewichtet beigemischt | schrumpft | schrumpft | nein ($K$ bricht) |
| Mittel über den Generationszyklus | fest | 0 | nein (vollständig dephasiert) |

Der passende Kanal ist das Zwirbeln mit der normierten **Summe** der drei Frame-Abbildungen. Gebraucht wird $p=(1-\kappa)/2=0{,}0308$, eine
schwache Störung von etwa 3 %. Gleichwertig: Die zwei Aufzeichnungszustände des Betrachters stehen im Winkel $\theta=40{,}41^\circ$ zueinander.

**2. Die nativen Kandidaten sind alle viel zu stark.**

| Kandidat | $\kappa^2$ | $\varphi$ | Abstand zum Ziel |
|---|---|---|---|
| N1 Dephasierung über $N\ge2$ Frequenzen | ≤ 0,5 | ≤ 0,322 | ≥ 0,345 |
| N2 $\kappa=|b|=1/\gamma_M$ | 0,287 | 0,166 | −0,500 |
| N3 Zeitmittel über ein Drittel der Periode, $\kappa=\operatorname{sinc}(\pi/3)$ | 0,684 | 0,479 | −0,187 |
| N4 Aufzeichnung $o$, $Fo$: $\kappa=1/\sqrt3$ | 0,333 | 0,197 | −0,469 |
| N5/N6 zwei Oktantenzustände bzw. Autokorrelation bei Koide: $1/\sqrt2$ | 0,5 | 0,322 | −0,345 |
| N7 Kick-Lesart: $\kappa^2=3/4$ bzw. $\kappa=3/4$ | 0,75 / 0,5625 | 0,540 / 0,373 | −0,126 / −0,294 |
| N8 Kompensator-Eigenwert: $\kappa^2=p_+$ bzw. $\kappa=p_+$ | 0,768 / 0,590 | 0,557 / 0,396 | −0,109 / −0,271 |
| N9 Spin-1-Aufzeichnung (Quadrat der Einzelüberlappung) | 0,111 / 0,25 | 0,059 / 0,142 | ≤ −0,525 |

Kein Kandidat kommt näher als 0,109. Alle nativen Größen sind von der Ordnung 1; gebraucht wird eine Dephasierung von nur etwa 6 % in $\kappa$.

## Einordnung
- In diesem Bild beginnt die Biegung beim Oktanten ($\pi/4$), nicht beim Spin-1-Dreieck (0,679042). Zu erklären ist hier also $\pi/4-2/3=0{,}1187$,
  nicht der Rest 0,012376.
- Gebraucht wird eine **kleine** Störung, die nur quer zur Zyklusachse wirkt. Die Kerngrößen des Bestands sind dafür zu groß. Ein kleiner Parameter
  wäre eher eine Kopplung (etwa eine Feinstruktur- oder Laufgröße) als eine geometrische Konstante. Aus der Renormierungs-Erkundung ist bekannt,
  dass die QED-Kopplung allein die Phase in die falsche Richtung schiebt; ob eine Kopplung als Zwirbel-Wahrscheinlichkeit $p=0{,}0308$ gelesen
  werden kann, ist hier nicht geprüft und wäre wieder eine Setzung.
- Ergebnis: Im Bestand ist kein natives κ gefunden. Die Bedingung ist jetzt in drei gleichwertigen Formen notiert: $\kappa^2=0{,}880706$,
  Zwirbel-Wahrscheinlichkeit $p=0{,}0308$ mit $n\cdot\sigma$, Aufzeichnungswinkel $40{,}41^\circ$. OP3 offen.
