# k398: Primzahl-Rauschen auf der Schleife, und was unter der Riemann-Vermutung folgt (Erkundung, 27.11.2026)

**Status:** Erkundung ohne Vorab-Notiz, kein Test. **Anlass:** Auftrag des Autors vom 27.11.2026: einen Rauschgenerator einbauen, der zuerst die
Primzahlen der Reihe nach ausgibt und das Signal leicht verrauscht; „Anthropics Arbeiten zur Riemann-Vermutung“ als Grundlage; Muster und Wert an
Position X berechnen und das Problem wie einen Angriff auf ElGamal oder RSA angehen. **Werkzeuge:** Python (Maschine, Sieb), mpmath für li(x).

## 1 Primzahl-Rauschen gegen Zufallsrauschen
Der Befehl `NOISE reg prime_gap eps` addiert zu einem Register eps mal die normierte Primzahllücke (p′ − p)/ln p′ − 1 (Mittel nahe 0, Streuung
0,72). Auf der Schleife L3 (Fixpunkt b = ½), eps auf dem Drehwinkel, 3000 Runden:

| eps | Primzahl: Mittel b | Zufall gleicher Streuung: Mittel b |
|---|---|---|
| 0,01 | 0,499980 | 0,500024 |
| 0,05 | 0,500269 | 0,500480 (Spanne der Startwerte 0,50017 bis 0,50089) |
| 0,10 | 0,501989 | 0,501862 |

Die Verschiebung des Mittels folgt aus der Krümmung der Schleife (+2·Var(b)) plus dem kleinen Mittel der Lücken; beide Rauschquellen gleicher
Streuung sind innerhalb der Spanne der Startwerte nicht zu unterscheiden. **Die Reihenfolge der Werte (das Muster der Primzahlen) geht nicht ein,**
weil die Schleife am Fixpunkt gedächtnislos ist (Steigung 0). Ein strukturiertes Rauschen wirkt hier wie weißes Rauschen.

## 2 Was ist an Position X exakt berechenbar, mit und ohne Riemann-Vermutung
Die n-te Primzahl ist durch ein Sieb exakt und schnell (Nr. 10⁶ = 15485863 in 0,17 s), ganz **ohne** die Vermutung. Die Riemann-Vermutung gibt
keine Formel für die n-te Primzahl, sondern eine **Fehlerschranke** für die Zählfunktion (Schoenfeld 1976: |π(x) − li(x)| < √x ln x /(8π) für
x ≥ 2657):

| x | π(x) | li(x) | Abweichung | Schranke |
|---|---|---|---|---|
| 10⁴ | 1229 | 1246,1 | −17,1 | 36,6 |
| 10⁶ | 78498 | 78627,5 | −129,5 | 549,7 |
| 10⁷ | 664579 | 664918,4 | −339,4 | 2028,0 |

Die Schranke sagt, wie weit π(x) höchstens von li(x) abweicht. Sie liefert weder die n-te Primzahl noch die Teiler einer Zahl.

## 3 Warum das kein Angriff auf RSA oder ElGamal ist
Zu dem Gedanken, das Problem wie einen Angriff auf RSA oder ElGamal anzugehen: Die Sicherheit beider beruht nicht auf der Verteilung der
Primzahlen, sondern auf dem Faktorisieren großer Zahlen (RSA) bzw. dem diskreten Logarithmus (ElGamal). Die Riemann-Vermutung und ihre
Verschärfungen verbessern nur die Fehlerterme im Primzahlsatz und einige Laufzeiten (z. B. machen sie den Miller-Rabin-Test unter GRH
deterministisch). **Kein Ergebnis der hier geprüften Arbeiten (siehe Einordnung) gibt eine berechenbare Formel für die Primzahl an Position X,
die ein Faktorisieren oder einen diskreten Logarithmus beschleunigt.** Die eigene Schleife ist zudem das Gegenteil einer Chiffre: Mit bekanntem
Bauprinzip und bekannter Folge ist jede Runde exakt vorhersagbar (Abweichung Maschine gegen Nachrechnung 5·10⁻¹³; gleicher Lauf, gleicher Hash),
und sie löscht Unterschiede im Startwert, statt sie zu verbreiten. Es gibt hier kein Geheimnis zu brechen.

## Einordnung der Riemann-Arbeiten (Stand 27.11.2026, aus öffentlichen Berichten)
- **Anthropic (Claude), August 2026:** Eine untere Schranke für den Anteil der Nullstellen der Zeta-Funktion auf der kritischen Geraden wurde von
  41,6 % auf 67,2 % angehoben (Alpöge, Furman, arXiv 2608.13637, „More than two thirds of the zeros … are simple and on the critical line“, in
  Lean formalisiert). Das ist **kein** Beweis der Vermutung; Fachleute (Maynard) nannten es einen interessanten Beitrag ohne Weg zur vollen
  Vermutung.
- **Anthropic (Claude), 20.–25. November 2026:** L. Alpöge kündigte, mit Claude, einen Beweis der Riemann- und der verallgemeinerten
  Riemann-Vermutung an, als großer Lean-Beweis (rund 17 Mio. Zeilen, später auf rund 76000 kompakt verkürzt). Die Lean-Entwicklung kompiliert
  und besteht Kernel-Prüfungen (Rubinstein, Sutherland); die lesbare Fassung (265 Seiten) ist ein Arbeitsstand und führt die Kernungleichung auf
  dreizehn ungbewiesene Hilfsaussagen zurück. Der Status „akzeptierter Satz“ ist noch offen.
- **OpenAI, Oktober 2026:** eine „Quasi-Riemann-Vermutung“ (Nullstellen in einem schmalen Streifen, nicht auf der Geraden); schwächer als die volle
  Vermutung, teils Lean-geprüft, teils nicht.
- **Für Primzahlen folgt aus der (verallgemeinerten) Riemann-Vermutung:** kleine, kontrollierte Fehler im Primzahlsatz und schnellere/deterministische
  Primzahltests. **Nicht** eine geschlossene Formel für die n-te Primzahl und **keine** Folge für RSA oder ElGamal. Genau das bestätigt die
  Einordnung in Abschnitt 3.

Die Primzahlfolge taugt hier also als deterministische, reproduzierbare Rauschquelle (nützlich als Werkzeug), nicht als Hebel, der aus einer
Vermutung einen berechenbaren Wert oder einen kryptographischen Vorteil zieht.

## Quellen
- [arXiv 2608.13637 (Alpöge, Furman)](https://arxiv.org/abs/2608.13637)
- [Scientific American: „No, AI didn’t just solve the thorniest problem in math“](https://www.scientificamerican.com/article/no-ai-didnt-just-solve-the-thorniest-problem-in-math/)
- [Quanta Magazine: „AI Proved the Quasi-Riemann Hypothesis“](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/)
- [M. Rubinstein (Waterloo): Alpöge/Claude GRH, Prüfstand](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)
- [The AI Insider: Anthropic bound 41,6 % → 67,2 %](https://theaiinsider.tech/2026/08/11/anthropic-says-claude-improved-a-longstanding-bound-tied-to-the-riemann-hypothesis/)
