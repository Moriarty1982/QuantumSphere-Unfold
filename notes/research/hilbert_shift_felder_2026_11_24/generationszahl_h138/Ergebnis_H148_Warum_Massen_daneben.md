# Ergebnis H148: Die Werte liegen daneben, weil die Gram-Auslesung die starre 120°-Überlappung misst; Koide braucht den Mischwinkel π/4 zwischen HS(0)-Einheit und Kopienrichtung

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H148_Warum_Massen_daneben.md` (Commit 8887b23; a und die Formel in c nicht blind, Messwerte bekannt).
Skripte `k331_massen_diagnose.py` (`k331_out.txt`), `k331b_gegenprobe.wl` (`k331b_out.txt`, Wolfram exakt). Status: H148a, b, c, d bestätigt
(c mit einer Klarstellung zur Vorzeichenkonvention, siehe unten).**

Anlass: Autor: „prüfe doch mal, wieso die Werte danebenliegen?“ Werkzeuge: Python (numpy, scipy), Wolfram exakt; Qiskit nicht eingesetzt.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H148a | Gram-Auslesung, Sedenion-Tripel: Leptonen \|a\|² = 1/16 (K = 3/8), Farbe \|a\|² = ¼ (K = ½); K = ⅔ braucht \|a\|² = ½ = cos²(π/4); Kopienwahl (H146, erschöpfend) und Frame-Maske (Form S) ändern nichts | vorab | **bestätigt** |
| H148b | mit cos θ·e₀ + sin θ·e₇: genau ein θ* = 26,2242° mit K = ⅔ (Wolfram exakt: a² = ½, Eigenwerte 1 + √2, 1 − 1/√2 zweifach); zwei Massen gleich; nächste Projektgröße halber magischer Winkel (Abstand 0,020 rad) | alle drei | **bestätigt** |
| H148c | Amplituden-Auslesung: K = 1/(3 cos²θ) (Wolfram exakt, Sec²θ/3), also K = ⅔ genau bei θ = π/4; mit δ = 2/9 (eingesetzt): m_μ/m_e = 206,770 (Messung 206,768), m_τ/m_μ = 16,8180 (16,8177), Abweichung ≤ 2·10⁻⁵ | K(π/4) = ⅔, < 1 % | **bestätigt** |
| H148d | komplexer Ladungszustand (e₀ + i e₇)/√2: K zwischen 0,343 und 0,346 für alle δ | \|K − ⅔\| > 10⁻³ | **bestätigt** |

**Klarstellung zu c:** K = 1/(3cos²θ) gilt mit vorzeichenbehafteten Amplituden (√m_k = c_k, Brannen-Konvention). Mit Beträgen gilt es nur,
solange alle drei Amplituden ≥ 0 sind; bei δ = 2/9 ist das der Fall. Der erste Lauf hatte Beträge genommen und deshalb bei θ = π/4 eine
δ-Abhängigkeit gezeigt; der Nachtrag im Skript rechnet beides.

## Lesart
- **Warum es danebenliegt:** Die Gram-Auslesung vergleicht feste Zustände der drei Kopien miteinander. Deren Überlappung ist durch die
  120°-Lage festgelegt, die Im z³ = 0 erzwingt (−½ bzw. ¼). Koide braucht dagegen „halb gleich, halb verschieden“, Überlappung² ½, also
  π/4. Mit 120° geht das nicht, egal welche Kopien und in welchem Frame.
- **Was hilft:** Ein Zustand, der die reelle Einheit (HS(0)) und die imaginäre Kopienrichtung mit dem Winkel θ mischt, genau der freie
  Mischwinkel aus H147. In der Amplituden-Auslesung von r13/k255 gibt **θ = π/4 exakt K = ⅔**, für jedes δ. π/4 ist im Projekt schon
  ausgezeichnet (exp(uπ/4), Oktant-Phase, H123). Mit δ = 2/9 kommen die Lepton-Verhältnisse auf 2·10⁻⁵ heraus.
- **Ehrlich getrennt:**
  - *Abgeleitet:* K = ⅔ ⇔ θ = π/4 (eine Gleichung, keine Anpassung); dass der Koide-Zustand reell sein muss (der komplexe Ladungszustand gibt
    K ≈ 0,34) und damit zeitumkehrfest ist (vgl. H144).
  - *Angepasst bzw. gesetzt:* θ = π/4 selbst (die Symmetrie lässt θ frei; ausgezeichnet ist π/4 nur durch die Koide-Forderung bzw. den Oktanten),
    δ = 2/9 (aus m_μ/m_e angepasst, Brannen; die Symmetrie erlaubt nur 120°-Schritte), die Skala, die Amplituden-Auslesung selbst.
  - Die Gram-Variante mit θ* = 26,2° trifft K, aber mit zwei gleichen Massen; θ* ist keine Projektgröße.
- **Was offen bleibt:** warum θ = π/4 (Potential bzw. Feldgleichung), woher δ = 2/9, die Skala, Quarks. OP3 offen; Vorzeichen offen; kein Guard
  berührt.
- Vergeben: H148, k331. Nächste frei: H149, k332.
