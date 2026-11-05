# Ergebnis H60: 6 Polarisationen je Nullrichtung, bestätigt

Grundlage ist die Vorab-Notiz H60 (Commit 1e1f17c, vor der Rechnung). Die Rechnung macht `k160_polarisationen.py`; die Basis kommt aus dem Rechenweg von k158, Q aus `k160_qmat.npy`.

## Werte
Für jede Ordnung p wurden 200 Nullrichtungen geprüft, außerdem 50 Richtungen außerhalb des Kegels.

| p | Polarisationen auf dem Kegel | kleinste Lücke | außerhalb: kleinster Singulärwert |
|---|---|---|---|
| 6 | 6 (alle 200) | 5e10 | 1.1e-2 → 0 Polarisationen |
| 7 | 6 (alle 200) | 4e10 | 1.4e-2 |
| 8 | 6 (alle 200) | 3e7 | 2.0e-2 |
| 9 | 6 (alle 200) | 5e7 | 2.4e-2 |

## Prüfung der Kriterien
- Die Kontrolle bei p = 6 stimmt: 6 = 7 − 1 wie in r73.2(c).
- Die Lücke liegt bei 100 % der Richtungen über 1e5.
- Der Median ist bei p = 8 und bei p = 9 gleich 6, außerhalb des Kegels ist der Wert 0.

**H60 ist bestätigt.**

## Lesart
Der Symbolmodul ist an generischen Punkten des Lichtkegels reduziert. Die 12 Cauchy-Daten (s_3 = 12) sind genau die 6 reellen masselosen Moden, also 6 ebene Wellen je Nullrichtung. Der Fehlbetrag der ebenen Wellen in r74.4 kommt deshalb nicht vom generischen Kegel, sondern von niedrigerdimensionalen Teilen der charakteristischen Varietät: den Ebenen Π_0 und Π_1 und den isolierten Richtungen.

Das Ergebnis bestimmt nicht, welche Felder das sind. Mögliche Zählungen sind zum Beispiel drei Weyl-Moden zu je 2 Polarisationen oder Photon, Graviton und eine Weyl-Mode zu je 2. Eine Lesart als drei Generationen ist nicht begründet, weil die drei Blöcke von Ψ eingebaut sind.
