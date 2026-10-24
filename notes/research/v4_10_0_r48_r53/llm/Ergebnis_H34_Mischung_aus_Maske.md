# Ergebnis H34: Die Maske aus r47 erklärt weder die CKM- noch die PMNS-Mischung

Vorab-Notiz: `Vorab_Notiz_H34_Mischung_aus_Maske.md`, Commit 8d8b761 (2026-10-24 03:31 MESZ), vor der Rechnung. Skript `k90_test_h34.py`,
Ausgabe `k90_out.txt`. Der erste Lauf (`k90_out_erstlauf.txt`) brach nach H34a in einer Diagnose-Ausgabe ab (kein Zweigpaar bei ε = 0.1);
korrigiert wurden nur diese Ausgabe und die Behandlung von m₁ = 0 (absolute statt relative Abweichung, die relative ist bei Masse 0 nicht
definiert). Die H34a-Werte beider Läufe sind gleich. Die Nachkontrollen 1–4 sind nach der Auswertung ergänzt und kein Teil des Kriteriums.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H34a CKM | **widerlegt** | 0 von 7488 Kombinationen (ε, Zweigpaar) treffen \|V_us\|, \|V_cb\|, \|V_ub\| zugleich auf ±20 %; der nächste Fall weicht um 96 % ab (ε = 0.055: 0.438, 0.0015, 0.00048) |
| H34b gemeinsames ε | **widerlegt** | kein ε erfüllt H34a, also kein Treffer |
| H34c Richtung | zählt nicht | ohne H34a gegenstandslos |

## Nachkontrollen (nach der Auswertung)

1. **Die Hierarchie begrenzt ε.** Lösungen mit den gemessenen Massen gibt es nur bis ε ≈ 0.06 (up), 0.125 (down), 0.13 (geladene Leptonen),
   0.025–0.23 (Neutrinos, je nach m₁). Abschätzung: Für eine fast rang-1 Kopplung erzeugt der Term ε² W C W eine Masse der Größe
   ≈ (|Wv|² − (v†Wv)²) ε² m₃, also (2/3) ε² m_t für Quarks und 2 ε² m_τ für Leptonen; sie darf die zweite Masse nicht übersteigen.
2. \|V_us\| allein lässt sich treffen (312 Kombinationen), aber dann liegen \|V_cb\| und \|V_ub\| nicht gleichzeitig richtig.
3. **Auch die Leptonen allein**, mit eigenem ε, erreichen die 3σ-Bereiche in keinem Fall.
4. Der nächste Lepton-Fall (ε = 0.08, m₁ = 0.003 eV) hat sin²θ₁₂ = 0.067, sin²θ₂₃ = 0.96, sin²θ₁₃ = 0.036, liegt also bis zu 71 % neben den Bereichen.

## Einordnung

1. **Die Modellannahme von r47 ist für die Mischung widerlegt.** Die Form der Maske folgt aus der Struktur (r47, r48), aber als schwache
   Störung der Kopplungen, M ↦ M + ε(WM + MW) mit zirkulanten Kopplungen, liefert sie die gemessenen Mischungsmuster nicht, weder für
   Quarks noch für Leptonen, und erst recht nicht mit einem gemeinsamen ε.
2. **Der Grund ist strukturell:** Die Massenhierarchie erzwingt kleine ε (Nachkontrolle 1), und bei kleinem ε ist das Muster der Maske zu
   „demokratisch“, um die starke Hierarchie |V_us| ≫ |V_cb| ≫ |V_ub| und die großen PMNS-Winkel zugleich zu erzeugen.
3. **Was bleibt:** r47.1(a), (b), (d) (Form der Maske, Frame-Verhalten, Fourier-Form, √3) sind unberührt; widerlegt ist nur ihre Verwendung
   als schwache Störung zirkulanter Kopplungen. Mischung braucht in diesem Bild eine andere Kopplungsform oder eine weitere Brechung.
