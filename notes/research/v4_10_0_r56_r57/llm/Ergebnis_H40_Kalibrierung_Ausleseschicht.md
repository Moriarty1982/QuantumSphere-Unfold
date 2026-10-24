# Ergebnis H40: Die kalibrierte Ausleseschicht zeigt keine Struktur über Zufall hinaus

Vorab-Notiz: `Vorab_Notiz_H40_Kalibrierung_Ausleseschicht.md`, Commit fdb27ae (2026-10-24 17:33 MESZ), vor der Rechnung. Skript `k96_test_h40.py`, Ausgabe `k96_out.txt`.

## Kalibrierte Einstellungen (Form S, ein ε je Sektor; Bereich über alle 294 Quark- und 1008 Lepton-Kombinationen aus H38)

| Größe | Bereich | Größe | Bereich |
|---|---|---|---|
| ε_u | [1.36, 1.63] | \|b\|/\|a\| u | [0.953, 1.032] |
| ε_d | [1.42, 1.47] | \|b\|/\|a\| d | [0.994, 1.076] |
| ε_e | [0.44, 0.82] | \|b\|/\|a\| e | [1.22, 6.41] |
| ε_ν | [0.27, 0.55] | \|b\|/\|a\| ν | [0.45, 1.57] |
| ε_u/ε_d | [0.951, 1.111] | θ u, d, e, ν | fast der ganze Bereich [0, π/3] |
| ε_e/ε_ν | [0.89, 2.96] | ε_d/ε_e | [1.73, 3.34] |
| ε_u/ε_ν | [2.47, 6.04] | | |

Zählung: 16 Einstellungen (+ m₁) für 17 Messgrößen; die Kompression ist gering.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H40a Struktur | **widerlegt** | 76 Treffer der 14 Kandidaten; Zufallssätze im Mittel 65.3 (95 %-Quantil 73), p = 0.019 > 0.01 |
| H40b Gleichheit | bestätigt, zählt nicht (ohne H40a) | 1 liegt in den Bereichen von ε_u/ε_d und ε_e/ε_ν |

## Einordnung

1. **Die Einstellungen, soweit die Daten sie festlegen, zeigen keine Struktur über Zufall hinaus.** Die Bereiche sind zu breit: Die Phasen θ füllen fast ihren ganzen
   Bereich, ε_e, ε_ν und die Lepton-Brannen-Größen streuen über Faktoren 2–5. Viele Kandidaten treffen deshalb, aber kaum mehr als Zufallswerte.
2. **Scheinbare Struktur, die keine ist:** |b|/|a| ≈ 1 bei u und d (schmal um 1) folgt aus der Hierarchie selbst. Für λ ≈ (0, 0, 1) ist C ≈ ⅓(1 + P + P²), also
   |b| = |a|. Das ist eine Eigenschaft hierarchischer Spektren, keine der Struktur. Ebenso enthält ε_u/ε_d zwar 1 im Bereich, aber kein zulässiger Fall liegt genau auf
   ε_u = ε_d (H36c).
3. **Lesarten nach der Rechnung (kein Kriterium):**
   - Master-Gleichung: m₀ ↔ a, β ↔ |b|, γ ↔ ε. Für die Quarks wäre β/m₀ ≈ 1 (aus der Hierarchie) und γ ≈ 1.4–1.6, für die Leptonen γ ≈ 0.3–0.8.
   - Beltrami: D = exp(εW) als Verformung mit Dilatation K = exp(ε · Spannweite W); |μ| ≈ 0.88–0.93 (u), 0.89–0.90 (d), 0.58–0.84 (e), 0.38–0.68 (ν). Quarks
     stark, Leptonen mäßig verformt; schmal ist nur d.
4. **Folge für den Weg „Filterebene einstellen“:** Mit 16 Einstellungen für 17 Größen legen die Daten die Einstellungen kaum fest; deshalb kann in ihnen keine Struktur
   sichtbar werden. Damit die Kalibrierung etwas lehrt, braucht die Filterebene weniger Einstellungen (Kompression), etwa eine Regel, die die Brannen-Größen festlegt,
   oder schärfere Daten (CP-Phasen, Massen genauer). Die Lesart aus r55 (Untergruppen statt freier ε) ist ein Schritt in diese Richtung.
