# Methodenprüfung: Stufenweise Elimination und Kondition des Symbols

Stand: 3. November 2026. Methodenprüfung (kein Test). Skripte `k150_stufen.py` (stufenweise Elimination des
linearisierten Fortsetzungssystems: c_N, c_{N−1}, … nacheinander über Linkskerne der Spaltenblöcke; nur Matrizen in
Symbolgröße) und `k151_kondition.py` (Kondition). Betrifft nur das OP5-Vergleichsmodell.

## Probe der Elimination gegen bekannte Werte

| fester Jet bis | Gleichungen bis Grad | Größe | erwartet | k150 | Lücke |
|---|---|---|---|---|---|
| 4 | 6 | P₅ | 371 | 371 | 3e3 (Wert 1,4e-8 zwischen echt und Rauschen) |
| 4 | 6 | P₅₆ | 852 | 852 | 2e7 |
| 5 | 6 | P₆ | 481 | 481 | 1e5 |
| 5 | 7 | P₆ | 477 | **476** | **4e2** (Werte 8,5e-9, 6,6e-9) |

Die Elimination arbeitet mit kleinen Matrizen und braucht wenig Speicher. Sie behebt das Genauigkeitsproblem aber nicht:
Wieder liegen Werte um 1e-8 zwischen echten Werten und Rauschen.

## Woher die Werte um 1e-8 kommen

- Das prolongierte Symbol aus **J allein** ist gut konditioniert: kleinster echter Wert 4e-5 (p = 4 und 6), Rauschen 1e-15,
  Lücke 3e10. Eine Equilibrierung (Ruiz) der 32 Zeilen und 24 Komponenten ändert daran nichts Wesentliches. An der
  Skalierung liegt es nicht.
- Die kleinen Werte entstehen erst mit **Ω** (Lücke dann 1,5e-8 gegen 1e-15) und den daraus folgenden Bedingungen. Das passt
  zu r71.3: Ω trägt neue Information nur auf dem Lichtkegel und auf den Ebenen Π₀, Π₁ und ist sonst eine rationale Folge
  der J-Zeilen. Als Zeile ist Ω also fast linear abhängig von J; sein unabhängiger Anteil hat das Gewicht ~1e-8. Die vier
  Bedingungen sechster Ordnung wiederholen das eine Stufe tiefer (sie wirken nur auf dem Lichtkegel).
- In double precision (Rundung 1e-16) lassen sich solche Stufen ein- bis zweimal sauber trennen, danach nicht mehr.

## Folgerung

Die Grenze liegt in der Struktur des Vergleichssystems, nicht in der Rechentechnik. Elimination und Symmetrie (die
Spiegelung z → −z würde die Matrizen halbieren) verkleinern die Rechnung, verbessern aber die Kondition nicht.
Weiterkommen lässt sich nur auf zwei Wegen:

1. **Mehrgenauigkeit der ganzen Kette:** Keim → Linearisierung → Elimination mit 30 oder mehr Stellen (z. B. python-flint
   mit arb-Kugelarithmetik). Großer Aufwand, Laufzeit unsicher.
2. **Umformulierung auf der charakteristischen Menge:** Weil Ω und die vier Bedingungen nur auf dem Lichtkegel und auf
   Π₀, Π₁ wirken, könnte man die Rechnung auf ebene Wellen dort beschränken. Dort sind diese Bedingungen kein
   kleiner Rest, sondern von der Größe 1. Das ist ein neuer Ansatz und noch nicht ausgearbeitet.
