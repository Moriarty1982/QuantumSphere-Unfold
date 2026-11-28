# Ergebnis H234 (k448): Keine gemeinsame Feinstufe erkennbar; die Feinwerte sind (bei heutigen Fehlern) unabhängig

**Datum:** 2026-11-28. **Vorab:** `Vorab_H234_Gemeinsame_Feinstufe.md` (Commit 85da2af, vor der Rechnung). **Urteil: widerlegt.**
**Werkzeuge:** Python (`k448_test_h234.py` → `k448_out.txt`) mit Monte-Carlo-Zufallsabschätzung; Wolfram unabhängig mit exakten Eingaben für die Bestwerte
(`k448b_gegenprobe.wl` → `k448b_out.txt`), übereinstimmend. Qiskit nicht einschlägig.

## Frage
Marc: Sind die Eingaben Grob- und Feintuning? Die groben Werte sind diskret und hergeleitet. Spart ein Zwei-Stufen-Bild Eingaben, weil alle Feinwerte aus einer
kleinen Zahl ε folgen (F = c·ε^n, 15 einfache Faktoren c, n = 1 … 3)? Feinwerte: φ, β_sym − ½, D/B − 1, x_ν − x.

## Ergebnis
| Lesart | Befund | Zufall (Monte Carlo) | Entscheidung |
|---|---|---|---|
| A: ε = φ | β_sym − ½: bestes √2·φ, **36σ** daneben. D/B − 1 ≈ ¼·φ (1,4σ), x_ν − x ≈ 2φ² (0,3σ) | D/B − 1 und x_ν − x treffen bei ihren Fehlern **immer** (Rate 100 %); p = 1 | nein |
| B: ε frei (φ = c·ε^n) | φ = ε² mit ε = 0,1989: β − ½ ≈ ¼ε (1,8σ), D/B − 1 ≈ ε³ (0,6σ), x_ν − x ≈ ½ε³ (0,1σ); beide scharfen Werte treffen | unter 44 ε-Wahlen trifft der Zufall genauso oft: p = 0,74 | nein (Zufall) |
| nachträglich (nicht gewertet) | (β_sym − ½)/φ = 1,2483, 0,37σ_β neben 5/4 | einfache Brüche p/q (q ≤ 4) decken ~12 % ab | kein Befund |

**Gesamturteil nach Vorab: widerlegt** (kein Treffer der scharfen Werte, der über den Zufall hinausgeht).

## Lesart
- **Das Muster stimmt, die Ersparnis nicht.** Die Unterscheidung grob/fein beschreibt den Stand gut: Alles Diskrete ist hergeleitet, alles Stetige ist offen. Aber
  die Feinwerte lassen sich nicht auf eine gemeinsame kleine Zahl zurückführen. Mit 15 Faktoren und drei Potenzen ist die Grammatik so dicht, dass Werte mit
  10 % oder 50 % Fehler immer „passen“; der einzige scharfe Prüfstein neben φ, β_sym − ½, trifft mit ε = φ nicht (36σ) und mit freiem ε nur auf Zufallsniveau.
- **Was das für das Zwei-Feld-Bild heißt.** Ein äußeres Feld, das alle Feinkorrekturen aus einer Kopplung erzeugt, wird von den Daten nicht nahegelegt. Wenn es
  ein äußeres Feld gibt, braucht es mehrere unabhängige Zahlen, also keine Ersparnis gegenüber dem jetzigen Bild. Teil 2 (dynamisches Zwei-Feld-Modell) lohnt
  sich daher nur mit einer neuen physikalischen Zutat, die die Kopplungen festlegt.
- **5/4.** (β_sym − ½) ≈ (5/4)·φ fällt auf, liegt aber im Bereich dessen, was einfache Brüche zufällig abdecken (~12 %), und war nachträglich. Nicht gewertet.

## Hergeleitet, gesetzt, nachträglich
- **Gerechnet:** Bestwerte (c, n) je Feinwert (exakt in Wolfram), Zufallsraten (Python).
- **Gesetzt:** Liste der Feinwerte und ihrer groben Bezüge (½ für β_sym ist eine Lesart), Grammatik, Intervall der Zufallszahlen.
- **Nachträglich:** 5/4 (in der Vorab offengelegt), nicht gewertet.

## Grenzen
Nur vier Feinwerte, drei davon mit großen oder mittleren Fehlern; schärfere Messungen von D/B und x_ν könnten die Frage neu stellen. Kein Guard berührt; OP3/OP4 offen.

## Dateien
`Vorab_H234_Gemeinsame_Feinstufe.md`, `k448_test_h234.py`/`k448_out.txt`, `k448b_gegenprobe.wl`/`k448b_out.txt`, `README.md`.

Vergeben: H234, k448. Nächste frei: H235, k449 (vor Vergabe gegen `main` prüfen).
