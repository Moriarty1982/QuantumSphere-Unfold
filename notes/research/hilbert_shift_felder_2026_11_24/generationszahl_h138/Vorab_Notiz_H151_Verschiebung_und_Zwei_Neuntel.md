# Vorab-Notiz H151: Hängt die Koide-Verschiebung aus H150 mit δ = 2/9 zusammen?

**25.11.2026, vor jeder Rechnung committet.** Anlass: Autor „schau mal, ob diese 0.06 mit den 2/9 zusammenhängen könnten“. Lesart (vom Koordinator, hier übernommen):
gemeint ist die Verschiebung des skalenfreien Flusses aus H150 (K ≈ 0,672 statt ⅔ bei 1 gegen 2 Komponenten); die Differenz ist dort ≈ 0,005, nicht 0,06. Falls eine
andere Zahl gemeint ist, wird nachgefragt. Vergeben: H151, Skripte k334 (Python) und k334b (Wolfram). Qiskit nicht vorgesehen. Kein HDL/MMA-Vergleich.

## Vorwissen geprüft
- H150 (k333): β-Funktionen (1, 2): 16π²β_A = 4(κ² + 18λ_A²), β_κ = 8κ(2κ + 3λ_A + 4λ_B), β_B = 2(κ² + 40λ_B²); am Gildener–Weinberg-Punkt tan²θ = √(λ_A/λ_B),
  K = (1 + tan²θ)/3; Start auf λ_A = λ_B, κ < 0: K von 0,6667 bis 0,6778 (Median 0,6719), also **vom Startwert abhängig**.
- H149: δ sieht nur die kubische Norm N(W) über cos 3δ; B = Norm der Kopienrichtung ist unter Drehungen in der Kopien-Ebene invariant.
- H149 Nachtrag: Zahlentreffer −4cos(2/3) ≈ −π hielt nicht (42σ); δ aus den drei Massen 0,222225 ± 0,000006.
- Brannen/Koide: δ = 2/9 ist eine Phase in der Kopien-Ebene (Azimut), θ ist der Winkel zwischen Einheit und Kopien-Ebene (Polwinkel). Das sind verschiedene Winkel.

## Hypothesen und Kriterien
- **H151a (nicht blind, analytisch):** Der Fluss aus H150 kann δ nicht erzeugen. V(A, B) und seine β-Funktionen hängen nur von B = Σy_i² ab, sind also O(n_B)-invariant in
  der Kopien-Ebene; jede Lösung lässt δ frei. Die 1:2-Asymmetrie verschiebt nur θ. *Kriterium:* Invarianz exakt (symbolisch). Bestätigt, wenn exakt.
- **H151b (gewertet):** Die Verschiebung ΔK = K − ⅔ am GW-Punkt ist keine feste Zahl, sondern hängt von den Startkopplungen ab. Eine feste Zahl gibt es nur als Grenzwert
  (Fixstrahl des Flusses, alle Kopplungen im festen Verhältnis). Vorhersage: Es gibt genau einen anziehenden Fixstrahl mit κ < 0 bzw. einen Grenzwert für κ₀ → 0⁻, und
  ΔK am Fixstrahl ist eine algebraische Zahl ohne π. *Kriterium:* Fixstrahlen exakt bestimmen (sympy, Wolfram).
- **H151c (gewertet, Zahlentreffer):** Für die festen Größen X ∈ {ΔK*, θ* − π/4, tan²θ* − 1} (am Fixstrahl bzw. Grenzwert, je n_B = 2 und n_B = 7) wird gegen die
  vorab feste Liste f(δ) mit δ = 2/9 verglichen: δ, δ², δ/3, δ/4, δ²/2, 1 − cos δ, sin²δ, 1 − cos 3δ. *Kriterium:* Treffer bei relativer Abweichung < 0,5 %.
  Look-elsewhere: Zufallserwartung = Anzahl Vergleiche × Trefferwahrscheinlichkeit für log-gleichverteilte Zahlen im Bereich der Liste; ausgewiesen. Ein Treffer zählt nur,
  wenn er gegen δ aus den Massen (0,222225 ± 0,000006) innerhalb 3σ bleibt, sofern die Größe exakt ist. Vorhersage: kein Treffer (es gibt keinen Mechanismus, s. a).
- Nicht gewertet: Median und Spannweite von ΔK auf dem Gitter (gitterabhängig) werden nur berichtet.

## Nachtrag vor der Rechnung (Autor 25.11., 20:17 UTC): alle von Hand eingesetzten Werte
„sonst prüfe nochmal einen zusammenhang zu allen werten die wir bisher von hand einsetzen müssen.“ Committet vor jeder Rechnung zu H151.

**Liste der Setzungen** (dimensionslos; Quellen: Ledger/Wiki, k297, k303, CT-002, H45, H149):
| Nr. | Setzung | Wert |
|---|---|---|
| S1 | Brannen-Phase δ | 2/9 = 0,222222 |
| S2 | Mischwinkel θ | π/4 |
| S3 | Frame-Versatz β_sym (β² = (γ_L − 1)/(γ_L + 1)) | 0,549400 |
| S4 | γ_L | 1,864700 |
| S5 | ε = artanh β_sym (Maske H45) | 0,617564 (aus S3) |
| S6 | HC-Koeffizient μ = β_sym² | 0,301837 |
| S7 | κ-Treffer (γ_L + 1/γ_L)/2 (k303) | 1,200 (aus S4) |
| S8 | Ziel κ* (k303) | 1,2039 |
| S9 | Überlappung ρ² (Koide) | ½ |
| S10 | γ_M (Immirzi, Platzhalter CT-001/002) | 0,237533 |
| S11 | CT-002-Verschiebung γ_M/6 bzw. ΔΦ = γ_M/2 | 0,039589 bzw. 0,118767 |
| S12 | γ_T | 0,127384 |
| S13 | Komponentenzahl 1 : 2 bzw. 1 : 7 | ½ bzw. 1/7 |

Nicht vergleichbar und deshalb ausgelassen: die Skala 9,8 GeV (k300, dimensionsbehaftet; ein Verhältnis zu einer anderen Skala wäre eine weitere Setzung) und der freie
Drehwinkel der Mischung (H131/H134, ohne festen Wert).

- **H151d (gewertet):** Jede feste Größe X aus H151c wird gegen jede Setzung s (S1–S13, mit S11 zweifach) in den Formen s, s², √s, 1/s, s/3, s/9 verglichen.
  *Kriterium:* relative Abweichung < 0,5 %. *Look-elsewhere:* erwartete Zahl zufälliger Treffer = Σ über alle Paare der Wahrscheinlichkeit, dass eine
  log-gleichverteilte Zahl im Intervall [10⁻³, 10] in das 1-%-Fenster fällt; zusätzlich empirisch mit 10⁴ Zufallssätzen gleicher Größe. Ein Treffer gilt nur als
  auffällig, wenn die beobachtete Trefferzahl über dem 99-%-Quantil der Zufallsverteilung liegt. Vorhersage: nicht auffällig.

## Grenzen
- Eine Schleife, ohne Eichfelder. Die Komponentenzahl der Kopienrichtung (2 oder 7) ist eine Lesart.
- OP3 offen; kein Vorzeichen gesetzt; kein Guard berührt.
