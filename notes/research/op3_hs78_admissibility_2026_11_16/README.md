# Zulässigkeit von HS(7) und HS(8) nach den Atlas-Regeln

16. November 2026, Claude Opus 5.5. **Erkundung, nicht blind** (die Blockrechnung steht analytisch fest), ohne Kriterium, keine H-Nummer.
Auftrag des Autors: „prüfe die Zulässigkeit von HS(7) und HS(8)“, offener Punkt aus Runde r25. Skript `hs78_admissibility.py`, Ausgabe
`run/hs78_admissibility_stdout.txt`.

## Was der Atlas festlegt (v470/32, Schicht r58, Abschnitte „Two-clock Hilbert-shift grammar“ bis „Audit target“)
- **Allgemein:** Trägeruhr C_n = 2ⁿ und Maskenuhr |Mask_n| = 2^(2ⁿ) sind für jedes n definiert. Gedeutet sind nur HS(0) bis HS(6).
- **HS(4)-Tor:** Mit dem Meta-Septum-Projektor Q verlangt der Atlas Leak⁽⁴⁾(M) = (1 − Q)MQ + QM(1 − Q) = 0, gleichwertig [M, Q] = 0.
- **HS(5)-Verdopplung:** HS(5) = HS(4)_vorne ⊕ HS(4)_hinten mit P⁽⁵⁾ = diag(P, P). Schuldfrei heißt Debt⁽⁵⁾(T) = 0, und Vergleiche zwischen den
  Seiten laufen über erklärte Vergleichstensoren oder Selektoren.
- **HS(6):** Der Dixon-Träger mit 64 Kanälen; eine Maske ist zulässig, wenn sie Fangklasse, HS(4)-Tor und HS(5)-Schuldfreiheit achtet.
- **Zwei ausdrückliche Grenzen:**
  - „The next meaningful layer is not a new shift. It is the image audit of the coding map.“ Der Atlas empfiehlt also, nicht weiter zu
    schieben, sondern erst die Bildprüfung der Codierung zu machen. Das ist eine Empfehlung, kein Verbot.
  - „No spectrum or Standard Model overclaim“: Der Dixon-Träger dient dort als **endlicher Routen-Code für OP5**; ausdrücklich wird kein
    Teilchenspektrum hergeleitet.

**Urteil zur Lage:** HS(7) und HS(8) sind im Atlas weder definiert noch ausgeschlossen. Eine Zulässigkeit gibt es erst, wenn eine Regel für
die Stufen über HS(6) erklärt wird.

## Die naheliegende Regel und ihre Prüfung
**Gesetzte Regel (nach dem Muster von HS(5)):** HS(n + 1) = HS(n) ⊕ HS(n), P⁽ⁿ⁺¹⁾ = diag(P⁽ⁿ⁾, P⁽ⁿ⁾) = 1₂ ⊗ P⁽ⁿ⁾, Schuld wie in HS(5).
Damit ist HS(7) = 2 × HS(6) und HS(8) = 4 × HS(6), wie in r25.4.

Ergebnisse (mit einem Platzhalter-Projektor vom Rang 7 auf 16 Kanälen; die Aussagen hängen nur an der Blockgestalt):
1. **Jede Operation nur auf dem Kopienindex ist schuld- und leckfrei.** X ⊗ 1 vertauscht mit 1 ⊗ P; die Schuld verschwindet identisch
   (Rechnung: höchstens 6·10⁻¹⁵ für zwei und vier Kopien).
2. **Die Operationen aus r25 sind Kopienoperationen** und damit zulässig: Hadamard und Phase auf den Kopien-Qubits, die Projektion auf
   Triplett und Singulett (Schuld höchstens 3·10⁻¹⁵). Das Spatprodukt aus r25.3 ist keine Operation auf dem Träger, sondern eine
   Auslese aus drei Zuständen; es berührt die Register nicht.
3. **Schuld entsteht nur innerhalb einer Kopie.** Eine Bewegung A mit [A, P] ≠ 0 erzeugt Schuld, ob man sie mit einer Kopienmischung
   verbindet oder nicht (beide Male 31,00). Das Mischen von Kopien selbst erzeugt keine. Das HS(4)-Tor muss also in jeder Kopie gelten,
   genau wie in HS(5) auf jeder Seite.
4. **Die Stufen bleiben verschachtelt:** P⁽⁸⁾ auf einer Hälfte ist P⁽⁷⁾, auf einem Viertel P⁽⁶⁾. Die Halbierung aus r25.4 ist mit der Regel
   verträglich.

## Folgerung
- **Formal zulässig unter der gesetzten Regel.** Wird die Verdopplung von HS(5) als allgemeine Regel für jede Stufe erklärt, dann sind HS(7) und
  HS(8) zulässige Erweiterungen, und alle Konstruktionen aus r25 (Kopien-Qubit, Triplett und Singulett, Spatprodukt) halten Leck- und
  Schuldregister bei null. Bedingung bleibt, dass jede Dixon-Kopie für sich das HS(4)-Tor erfüllt.
- **Zwei Vorbehalte aus dem Atlas selbst:**
  1. Die Regel ist **gesetzt**: Der Atlas definiert nur HS(5) als Verdopplung und empfiehlt, vor jeder neuen Stufe die Bildprüfung von HS(6) zu
     machen. Eine Erweiterung müsste als neue Definition erklärt werden.
  2. **Bedeutungswechsel:** Im Atlas ist der HS-Turm eine Grammatik für OP5-Routen, mit ausdrücklichem Verzicht auf Teilchenaussagen. r25 liest
     die Kopien als Generationsträger. Die Zulässigkeit nach den Atlas-Regeln zeigt nur, dass sich beides nicht widerspricht; sie stützt die
     physikalische Lesart nicht. Für r25 kommt es eigentlich nur auf die Kopien von C⊗H⊗O an, nicht auf den Atlas-Turm.
- OP3 und OP5 bleiben offen; der Status der Bildprüfung von HS(6) ist unverändert.
