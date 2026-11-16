# Ergebnis H110: Das Triplett-Paar {Betrachter, F} legt die Biegung nicht fest (widerlegt)

Gerechnet am 2026-11-16 nach der Vorab-Notiz `Vorab_Notiz_H110_Betrachter_HS7_Haelfte.md` (Commit 8a97d9c). Skript `k232_test_h110.py`,
Ausgabe `k232_out.txt`.

## Ergebnis
Kontrollen wie erwartet: rein $K=2/3$, $\varphi=\pi/4$; Singulett $K=1/2$, $\varphi=0$. Variante A gibt mit $T$ oder $J_B$ statt $R$ dieselben Werte.

| Variante | Betrachter | $K$ | $\varphi$ |
|---|---|---|---|
| A (nur ein Frame gepaart, 7+6+6) | $+n$ | 0,7376 | 0,4920 |
| A | $-n$ | 0,5372 | 1,4376 |
| B (alle gepaart) | $+n$ | 0,8888 | 0,1568 |
| B | $-n$ | 0,5609 | 0,5422 |
| C (Mittel über die Aufteilungen) | $+n$ | 0,7304 | 0,4772 |
| C | $-n$ | 0,5361 | 0,8972 |

**6 Versuche, kein Treffer → widerlegt.** Keiner trifft die Phase (nächster Abstand 0,124), und alle verfehlen $K=2/3$ um mindestens 0,064.

## Einordnung
- Das Triplett-Paar mischt die Auslesung nicht nur, es **zieht ihren Bloch-Vektor zum Betrachter hin** (bei $+n$) oder von ihm weg (bei $-n$). Damit
  ändert sich der Längsanteil entlang der Zyklusachse, und $K=(9+|R|^2)/18$ verlässt 2/3. Genau den Längsanteil darf ein Mechanismus nach dem
  Nachtrag der Erkundung nicht berühren: $K=2/3$ hält nur eine reine Querdephasierung um die Zyklusachse.
- Die Kopientausch-Regel (Triplett) ist damit die falsche Art der Verschränkung für diese Rolle. Gebraucht wäre eine Aufzeichnung, die nur die
  Kohärenz quer zur Zyklusachse mindert, mit dem Faktor $\kappa=0{,}938459$ ($\kappa^2=0{,}880706$). Eine native Konstruktion dafür ist im Bestand
  nicht gefunden; der naheliegende Kandidat ($o$, $Fo$) gibt $\kappa=1/\sqrt3$ (vorab gesehen, nicht gezählt).

## Status
OP3 offen. Rest 0,012376 unerklärt nach sechs Wegen (H106–H110 und Renormierung). Positiv festgehalten (aus der Erkundung, nicht aus diesem Test):
Im Bild „Algebra je Frame, Kopie 00 als Betrachter“ ist die Bedingung an einen Mechanismus jetzt scharf: Querdephasierung um die Zyklusachse mit
$\kappa^2=0{,}880706$; dann gilt $K=2/3$ exakt und $\varphi=\arctan(\kappa^2/(2-\kappa^2))$.
