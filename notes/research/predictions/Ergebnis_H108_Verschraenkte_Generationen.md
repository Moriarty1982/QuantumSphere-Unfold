# Ergebnis H108: Verschränkte Generationszustände (Majorana-Paare) schließen den Rest nicht (widerlegt)

**16.11.2026.** Vorab-Notiz `Vorab_Notiz_H108_Verschraenkte_Generationen.md` und Skript `k230_test_h108.py` (Commit 01a0f86, vor der
Rechnung), Ausgabe `k230_out.txt`. Auftrag des Autors „Ja, rechnen“. Blind nur darin, dass die Familie vor der Rechnung festgelegt war; der
Zielwert 0,666665 war bekannt.

## Ergebnis: widerlegt

| Mechanismus (zweiter Majorana-Punkt) | ψ (beide Lösungen) | Phase φ | φ − 0,666665 | det G |
|---|---|---|---|---|
| E1 Nachbar n_{k+1} | 57,70° / 122,30° | 0,176250 | −0,4904 | 0,1962 |
| E2 Pol +z | 72,41° / 139,79° | 0,785398 = π/4 | +0,1187 | 0 |
| E3 Pol −z | 40,21° / 107,59° | 0,785398 = π/4 | +0,1187 | 0 |
| E4 Gegenpunkt −n_k (polar) | 26,22° / 153,78° | 0 | −0,6667 | 0,2071 |
| E5 Gegenpunkt des Nachbarn | 28,57° / 151,43° | 0 | −0,6667 | 0,2071 |
| zum Vergleich: kohärent (beide Punkte n_k) | 38,68° | 0,679042 | +0,0124 | 0,0503 |

Zehn Versuche, kein Treffer innerhalb 0,0002 rad.

## Was die Rechnung strukturell zeigt
- **Ein gemeinsamer Bezugspunkt macht das Dreieck wieder flach.** Haben alle drei Generationen einen Majorana-Punkt am Pol der Zyklusachse
  (E2, E3), ist die Phase genau π/4 und det G = 0: der flache Oktant mit einer masselosen Generation, wie bei zwei Kopien (r25.2). Der
  gemeinsame Punkt trägt nichts zur Unterscheidung bei, und es bleibt effektiv ein Qubit.
- **Gegenpunkte geben reelle Zustände.** Polare Zustände (E4) und die Gegenpunkte der Nachbarn (E5) sind reelle Vektoren; die Phase ist 0, wie
  vorab erwartet.
- **Nachbarpunkte (E1) überdrehen.** Die Phase fällt auf 0,176, weit unter den Zielwert.
- Unter allen geprüften Spin-1-Zuständen mit Überlappung ½ bleibt das **kohärente Dreieck** (unverschränkt) der Lepton-Phase am nächsten. Die
  Lepton-Phase liegt knapp jenseits davon, auf der vom flachen Oktanten abgewandten Seite. Eine stetige Familie zwischen dem kohärenten Fall
  und E1 würde 2/3 bei kleiner Aufspaltung der Punkte treffen; das hätte einen freien Parameter und wird hier nicht gerechnet.

## Einordnung
- Mit H106, H107 und H108 sind drei parameterfreie Familien widerlegt: Singulettbeimischung, verschachtelte Normierung, verschränkte
  Majorana-Paare. Der Rest 0,012376 ist mit der Kopienstruktur von HS(8) allein nicht erklärt.
- **Suchrichtung:** Nach drei Varianten mit derselben offenen Voraussetzung (der Rest kommt aus der Kopienstruktur) verlangt AGENTS, die
  Suchrichtung zu prüfen. Der vom Autor genannte zweite Weg, die **Renormierung** (Polmassen gegen laufende Massen), setzt an einer anderen
  Voraussetzung an und ist der naheliegende nächste Schritt.
- OP3 bleibt offen. H102 und H105 sind unberührt.
