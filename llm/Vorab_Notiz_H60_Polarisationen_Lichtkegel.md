# Vorab-Notiz H60: Polarisationen je Nullrichtung im involutiven Symbol

**Geschrieben und committet am 3. November 2026 vor der Rechnung. Status: vorregistriert, nicht blind.** Bekannt sind die Charaktere 723, 130, 12, 0 und aus r73.2(c) ein Wert bei p = 6.

## Brücke zur Physik
Ein involutives Symbol mit dem letzten Charakter s_3 = 12 lässt eine allgemeine Lösung zu, die von 12 Funktionen dreier Variablen abhängt: Das sind die Cauchy-Daten. Der führende Koeffizient des Hilbert-Polynoms ist die Summe der Grade der dreidimensionalen Komponenten der charakteristischen Varietät, gewichtet mit ihren Multiplizitäten. Die Ebenen Π_0, Π_1 und die isolierten Richtungen tragen dazu nicht bei. Der Lichtkegel q hat Grad 2, also gilt Multiplizität × 2 = 12, und die Multiplizität ist 6. Ist der Symbolmodul auf dem Kegel reduziert, sind das 6 unabhängige ebene Wellen je Nullrichtung, also 6 reelle masselose Moden. Zum Vergleich: Eine Weyl-Spinor-Mode hat 2 reelle Polarisationen je Nullrichtung, das Photon 2, das Graviton 2.

## Hypothese H60
Für generische Nullrichtungen ξ (q(ξ) = 0) gilt dim{u : ξ^p ⊗ u ∈ g''_p} = 6 bei p = 8 und bei p = 9. Für generische Richtungen außerhalb des Kegels und der Ebenen ist der Wert 0.

## Messung (k160)
- Basis von g''_p aus dem Rechenweg von k158 (hochgenaues g''_6, Prolongation in float).
- 200 Nullrichtungen aus q = ξᵀQξ (Q am Keim, k160_qmat.npy) und 50 Richtungen außerhalb.
- Rang von (1 − P_g) W_ξ mit W_ξ = (ξ^α/√α!) ⊗ e_j über die 24 Spalten. Die Polarisationszahl ist 24 − Rang.
- Kontrolle: p = 6 muss mit r73.2(c) übereinstimmen, also 6 = 7 − 1.

## Gültigkeit
- Die Lücke am Rang ist ≥ 1e5 für ≥ 95 % der Richtungen.
- Die Kontrolle bei p = 6 stimmt.

## Entscheidung
| Ergebnis | Bedingung |
|---|---|
| bestätigt | Median = 6 bei p = 8 und p = 9, und 0 außerhalb |
| widerlegt | Median < 6. Dann ist der Modul auf dem Kegel nicht reduziert, und die 12 Daten liegen zum Teil in nilpotenter Struktur und nicht in ebenen Wellen |
| ungültig | Median > 6, oder ≠ 0 außerhalb |

## Lesart
Eine Bestätigung zeigt nur, dass das Vergleichsmodell 6 reelle masselose Moden trägt. Sie sagt nicht, um welche Felder es sich handelt. Die Zahl 3 der Blöcke von Ψ ist eingebaut und nicht hergeleitet, daher wäre eine Lesart als drei Generationen hier nicht begründet.
