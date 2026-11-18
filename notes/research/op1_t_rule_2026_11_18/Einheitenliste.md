# Einheitenliste für die Dimensionsleiter (vor der Auswertung festgelegt, 18.11.2026)

Auftrag des Autors: „Einheitenliste prüfen“ (Kandidat 2 der T-Regel-Notiz). Gesucht: eine Einheit γ₀, die ohne Bezug auf das T-Quant natürlich ist und im
Fenster [γ_T; γ_P/2) = [0,127384; 0,137033) liegt; dort gibt die Dimensionsleiter T, M, P auf Linie, Fläche, Raum (k237).
**Nicht blind gegenüber einzelnen Einträgen:** γ_M/2, γ_P/3, γ_P/2 und 1/(2π) sind in k237 schon ausgewertet (alle außerhalb); die Liste nimmt sie trotzdem
auf, damit sie nach einer Regel gebaut ist und nicht nach dem Ergebnis. Skript `k239_unit_list.py`, Ausgabe `run/k239_stdout.txt`.

## Liste (nach zwei Bauregeln, vollständig)
**L1 Flächenquantum-Einheiten:** γ₀ = c/(2π a) mit
- c ∈ {1, ½, ln 2, ln 3, 2 ln 2, π} (Zählkonstanten: Einheit, halbe Einheit, Bit, Trit, zwei Bits, Halbkreis),
- a ∈ {√3/2 (a(½)), √2 (a(1)), ½ (lineares j + ½ bzw. j bei ½), 1};
- **ausgenommen** c = ln 2, a = √3/2: das ist γ_T selbst. 23 Einträge.
**L2 Regel-Einheiten:** γ₀ = γ_R/d für jede Regel R des Regelraums S außer T (acht Regeln, γ aus k218) und d ∈ {1, 2, 3}
(„R füllt ℝ^d genau“). 24 Einträge.

## Auswertung, vorab festgelegt
- Treffer: γ₀ im Fenster [0,127384; 0,137033).
- Zufallserwartung: Anteil des Fensters an der logarithmischen Spannweite der 47 Einträge, mal 47.
- Lesart: Kein Treffer → Kandidat 2 entfällt; die Leiter bleibt für T im Kreis. Treffer → nur bemerkenswert, wenn die Zufallserwartung unter 0,3 liegt;
  sonst „mit Zufall verträglich“. Die Liste wird nach dem Commit nicht geändert.
