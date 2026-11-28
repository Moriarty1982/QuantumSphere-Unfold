# Vorab-Notiz H219 (k432): Rückwärtssuche nur mit Endzahlen als Ziel (symbolische Regression)

Stand 28.11.2026, vor der Rechnung festgeschrieben. Frage des Autors vom 28.11.2026, 00:17: „was passiert wenn man weniger vorgibt sondern
nur sagt welche endzahlen man haben will?“ Auf den Vorschlag des Koordinators hat er um 00:18 mit „ja bitte“ geantwortet.

## Frage

Statt einer Schleife oder Formel wird nur die Zielzahl vorgegeben. Gesucht werden alle Ausdrücke aus Bausteinen des Rahmens bis zu einer
festen Größe. Getestet wird, ob die Ziele mit kürzeren Ausdrücken getroffen werden als gleich genaue Zufallszahlen, einzeln oder als
Familie mit einer gemeinsamen Formel f(n).

**Alle Treffer sind „angepasst“** (gesucht, nicht hergeleitet). Das Urteil betrifft nur die Frage, ob die Trefferlage den Zufall übersteigt.

## Bausteine (fest)

- **Blätter:** 1, 2 (Gewicht je Spin), 3 (Generationen bzw. Farben), π, ln 2 (ein Bit).
- **Einstellige Operationen:** √x, x², 1/x, 2^(−x) (1-Bit-Gewicht).
- **Zweistellige Operationen:** +, −, ×, ÷.
- **Größe** = Zahl der Knoten, also Blätter plus Operationen. Zahlenausdrücke bis Größe **9**. Vorlagen mit Blatt n, ausgewertet für
  n = 1, 2, 3, bis Größe **8**.
- Ausdrücke mit gleichem Wert (relativ 10⁻¹¹; bei Vorlagen ist es der Wertvektor) werden zusammengefasst, die kleinste Größe zählt.
  Dadurch fallen Abwandlungen desselben Treffers zusammen, etwa x·1, √(x²) oder die vielen Fassungen eines Werts wie in H216.
- γ_L, β_sym, γ_M und andere abgeleitete Konstanten sind **keine** Blätter. γ_T = ln 2/(π√3) ist mit Größe 6 erreichbar.
- Die Mengen wurden vor dem Blick auf Ziele gemessen (Skript `enum_h219.py`, ohne Ziele): Bis Größe 9 gibt es 5 778 991 verschiedene
  Werte (Größe 8: 724 138, Größe 9: 4 926 181), bis Größe 7 bei den Vorlagen 243 533 Wertvektoren.

## Ziele (fest)

Übernommen wird der feste Zielkatalog aus k235 (`notes/research/chance_estimate_2026_11_18/k235_chance_estimate.py`, 16 Größen mit
Werten und σ wie dort). Hinzu kommen β_sym mit dem k358-Fenster [0,54907; 0,54978] und m_e/m_μ aus den Polmassen in k427
(0,51099895/105,6583755 mit fortgepflanztem σ). Zusammen sind das 18 Ziele. Trefferfenster: Zentralwert −2σ_unten bis +2σ_oben.

## Messgrößen und Kontrollen

- **s_min(Ziel):** kleinste Größe eines Ausdrucks im Fenster, ∞ falls keiner bis Größe 9.
- **N(Ziel):** Zahl der verschiedenen Werte im Fenster, nur berichtet.
- **Kontrollen:** Je Ziel 1000 Zufallswerte, log-gleichverteilt in [x/3, 3x] (Startwert 219), jeweils mit derselben relativen Fensterbreite.
  p = Anteil der Kontrollen mit s_min ≤ s_min(Ziel); Gleichstände zählen gegen das Ziel.
- **Familien** (Zuordnung n ↔ Ziel fest, Reihenfolge nach Generationsindex):
  - Leptonen: n = 1 m_e/m_μ, n = 2 m_μ/m_τ;
  - CKM: n = 1 |V_us|, n = 2 |V_cb|, n = 3 |V_ub|;
  - PMNS: n = 1 sin²θ₁₂, n = 2 sin²θ₂₃, n = 3 sin²θ₁₃.

  Eine Familie gilt als getroffen, wenn eine Vorlage f(n) **alle** Glieder in ihren Fenstern trifft. Statistik und Kontrollen wie oben,
  mit 1000 Zufallsfamilien, deren Glieder unabhängig gezogen werden.

## Kriterium

- **trägt:** mindestens ein Ziel mit p < 0,05/18 (Bonferroni über die Ziele) oder mindestens eine Familie mit p < 0,05/3;
- **trägt teilweise:** kein Einzelbefund übersteht die Korrektur, aber mindestens 4 der 18 Ziele haben p < 0,05. Das ist die Schwelle über
  dem 95-%-Quantil von Bin(18; 0,05), das bei 3 liegt;
- **widerlegt:** sonst. Die Endzahlen-Suche findet dann mit den Bausteinen des Rahmens nicht mehr als der Zufall.

## Vorwissen geprüft

- k235 (Zufallsabschätzung der γ_L-Treffer): Der Dreifachtreffer ist mit Zufall verträglich, sobald man die Auswahl mitzählt. Die
  Zählweise mit Kontrollen wird hier übernommen.
- H215 bis H217: Die Schleifensuche bevorzugt geschlossene Formen, und Abwandlungen blähen Wortzählungen auf. Deshalb wird hier nach Werten
  dedupliziert.
- **Bekannte Nähen:** 2^(1−γ_L) ≈ β_sym (k396) ist mit diesen Blättern nicht darstellbar, weil γ_L kein Blatt ist. Bekannt sind außerdem
  sin²θ₁₂ ≈ ⅓ (TM1/TBM), das bei 2σ außerhalb des Fensters liegt (0,3088 + 0,0134 < ⅓), und sin²θ_W ≈ 3/13, das ebenfalls außerhalb
  liegt (Fenster ±8·10⁻⁵). Weitere geschlossene Formen für die Ziele sind im Bestand nicht festgeschrieben.

**Erwartung (keine Rechnung):** Ziele mit breitem Fenster werden früh getroffen, aber genauso früh wie ihre Kontrollen. Erwartet wird
„widerlegt“.

## Prüfwege

1. Hauptrechnung in Python: `k432_test_h219.py`, Ausgabe `k432_out.txt`.
2. Gegenprobe in Wolfram: `k432b_gegenprobe.wl`, Ausgabe `k432b_out.txt`. Sie zählt die Aufzählung bis Größe 5 unabhängig und rechnet die
   kürzesten Treffer je Ziel neu aus.

Ordner: `notes/research/hilbert_shift_felder_2026_11_24/endzahlen_suche_h219/`.
