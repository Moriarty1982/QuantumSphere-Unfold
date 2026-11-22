# Wolfram-Prüfung von Abschnitt 3 · Preprint 0.1.0

**Ergebnis:** 29 von 29 exakten Einzelprüfungen bestanden. Geprüft am veröffentlichten Preprint [10.5281/zenodo.24405553](https://doi.org/10.5281/zenodo.24405553). Die Rechnung verwendet den Wolfram-Connector mit Kernel 15.0.1 für Linux x86-64.

- Publiziertes PDF, SHA-256: `99aec02ead80b924fdb93182227307eeb8e4a2f3636f16ff6604a45507dc01dc`.
- Lokale Arbeitsquelle `sections/05-mass.tex`, SHA-256: `e875ac36a81c166bdeee403ee311efd86d467eb162ce77b243d051361f3e650a`.
- Ausführung: [koide.wl](koide.wl) im Wolfram Language Evaluator, mit 60 Sekunden Laufzeitgrenze. Lokal verwendbar als `wolframscript -file koide.wl`. [Unveränderte Ausgabe](koide.txt).
- Exakte symbolische Ausdrücke, algebraische Kontrollfälle und die exakten Winkel $0,\pi/12,\pi/6,\pi/4,\pi/2$. Keine Messdaten, numerischen Toleranzen oder Zufallsstichproben.

## Welche Aussagen geprüft sind

Die Koide-Zerlegung, die Fourier-Radiusformel, das konkrete HC-Beispiel, Spur- und Spektralformeln für die Gram-Familie, Bargmann-Produkt und Umphasierung, der Oktantenrand und die beiden Mittelungsreihenfolgen stimmen mit dem Manuskript überein. Die Eigenwerte und das Gewicht der schweren Komponente im Flat-Gap-Block folgen aus der geprüften Eigenvektor- und Normierungsrechnung.

Für die Gram-Positivität liefern die drei positiven kleineren Hauptminoren zusammen mit der Determinante die Bedingung $|\varphi|\le\pi/4$ im Hauptwertintervall. Positive Definitheit gilt im offenen Intervall. Am Rand ist der Rang exakt zwei. Im Inneren liefert $\theta=\varphi/3$ für positives $\theta$ die aufsteigenden Eigenwertabstände $\sqrt6\sin\theta$ und $\sqrt6\sin(\pi/3-\theta)$. Beide sind positiv. Das negative Vorzeichen der Phase tauscht die beiden kleineren Werte aus. Damit bestimmt der Betrag der Phase das ungeordnete Spektrum in dieser Familie.

Die Coisometrie wurde in einem exakt konstruierten Test von Dimension vier zu drei kontrolliert. Allgemein gewährleistet der $J$-invariante Kern zusammen mit der Selbstadjungiertheit von $J$ auch die Invarianz von $(\ker B)^\perp$; deshalb überträgt $B$ dort die Involution. Die symbolische Flat-Gap-Rechnung setzt $\Delta>0$ und für die negative Eigenzahl $\mu\sigma_i>0$ voraus.

Die Zwischenläufe zeigten falsch-negative Testmeldungen durch die Normalisierung exakter algebraischer Zahlen, eine kombinierte trigonometrische Ungleichung und die Form einer Substitutionsregel im Prüfskript. Die Endprüfung setzt die algebraischen Zahlen in kanonische Form, prüft die trigonometrischen Differenzen symbolisch und substituiert direkt für die Kopplung. Der Endlauf meldet keine Warnung und `FAILED: {}`. Sein `Out[1]= Null` ist der Rückgabewert der letzten Print-Anweisung.

Die native Teilchenzuordnung, der physikalische Wurzeloperator und die absolute Massenskala bleiben offene Voraussetzungen. Die Prüfungen behandeln die vorgelegte Algebra.
