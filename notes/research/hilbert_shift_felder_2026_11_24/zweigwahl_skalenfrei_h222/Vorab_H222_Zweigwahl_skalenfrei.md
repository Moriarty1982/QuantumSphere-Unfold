# Vorab-Notiz H222 (k435): Wählt das Vorzeichen der kubischen Spektralinvariante den Zweig in beiden Lepton-Sektoren, ohne Skala?

**Datum:** 2026-11-28, vor der Rechnung committet. **Auftrag:** Marc 28.11. („dann weiter“, „weiter“): nach H221 die skalenfreie Zweigwahl suchen.
**Werkzeuge:** Python (`k435_test_h222.py` → `k435_out.txt`), Wolfram unabhängig und symbolisch (`k435b_gegenprobe.wl` → `k435b_out.txt`). Qiskit nicht einschlägig.

## Ausgangslage
H221: Eine gemeinsame Drehung χ → χ + φ verschiebt die Minima beider Sektoren exakt um φ, ohne Skala. Es bleibt eine doppelte Entartung:
- Im-Sektor (geladene Leptonen, c = 1, α′ = +1, χ = π/4 + φ): Minima (gefaltet) bei π/12 − φ und π/4 + φ.
- Re-Sektor (neutrale Leptonen, c = 0, α′ = −1, χ = φ): Minima bei π/6 − φ und π/6 + φ.
Die zwei Zweige eines Sektors sind verschiedene Spektren (δ und δ + π/3 unterscheiden sich durch das Vorzeichen der Wurzeln). Bisher wählte nur der Term sechster
Ordnung q cos 3δ mit q = β₃v²/Λ² den Zweig (H167), also die Skala.

## Idee (Hypothese H222)
Die gefaltete Phase ist nur bis auf δ → −δ (Konjugation) und δ → δ + 2π/3 (Umbenennung) bestimmt; das Spektrum hängt nur von der Klasse ab. Die Funktionen, die unter
dieser Gruppe D₃ invariant sind, sind Funktionen von cos 3δ. Die niedrigste Spektralinvariante ist damit cos 3δ, und sie ist die Determinante der Wurzelmatrix:
det Y / μ³ = 1 − 3a²/4 + (a³/4) cos 3δ, bei a = √2: −½ + cos 3δ/√2. Ein dimensionsloser Ausdruck, keine Skala.
**H222:** Eine einzige skalenfreie Regel „unter den entarteten Minima liegt der physikalische Zweig dort, wo cos 3δ (gleichwertig det Y/μ³) größer ist“ wählt in
**beiden** Sektoren den Zweig der Daten. Das entspricht dem Grenzfall q → 0⁻ des Terms sechster Ordnung: der Betrag (die Skala) fällt weg, nur das Vorzeichen bleibt.

## Vorwissen geprüft
- H167 (`delta_h166`/`delta_h168`-Umfeld, Bilanz in H221): Weg S mit q/α′ = −0,0852 wählt im Im-Sektor δ* (= Zweig π/12 − φ); bis Ordnung 4 wählt nichts.
- H168 (`delta_h168/Ergebnis_H168_Skala_und_Sektoren.md`, Z. 36): Für c = 0 ohne Drehung sind beide Minima gleichwertig (beide bei π/6), keine Zweigwahl nötig.
  Mit der Drehung aus H221 spalten sie in π/6 ± φ auf; dann ist auch im Re-Sektor eine Wahl nötig.
- H213d (`versatz_spannung_h213/k426_out.txt`): Für normale Ordnung hat R = R_obs in [0, 2π/3) nur die Lösungen 0,48024 (= π/6 − x) und 1,61416 (dieselbe Klasse);
  bei π/6 + x liegt keine Lösung. Wie weit R dort abweicht, ist nicht gerechnet. Invertierte Ordnung: −16σ.
- H221 (`skala_zwei_sektoren_h221/`): nachträglich bemerkt, dass der Weg S im Re-Sektor q mit demselben Vorzeichen wie im Im-Sektor verlangt (q < 0 in beiden, also
  q/α′ entgegengesetzt). **Deshalb ist Teil b teilweise nicht blind.**
- predictions/: keine Vorab-Notiz zu einer skalenfreien Zweigwahl gefunden (Suche nach „Zweigwahl“, „Zweig“, „cos 3“).

## Teiltests und Kriterien (vorab festgelegt)
- **a (nicht blind):** Im-Sektor, Drehung φ = x_lepton = 0,0395773: wählt „max cos 3δ“ den Zweig π/12 − φ (δ*)? Kriterium: ja für alle φ in [0,01; 0,06].
- **b (teilweise nicht blind):** Re-Sektor, dieselbe Drehung: wählt die Regel den Zweig π/6 − φ (x_ν > 0, der Zweig der Daten aus R)? Kriterium: ja für alle φ in [0,01; 0,06].
  Wählt sie π/6 + φ, ist H222 **widerlegt** (dann bräuchten die Sektoren entgegengesetzte Vorzeichen, keine universelle Regel).
- **c (teilweise nicht blind, H213d):** Ist der verworfene Re-Zweig π/6 + x_lepton von den Daten ausgeschlossen? R_NO und R_IO dort gegen R_obs (NuFIT wie H99b/H213).
  Kriterium: ausgeschlossen, wenn > 3σ in beiden Ordnungen; dann ist die Regel durch die Daten geprüft. Sonst „von den Daten nicht geprüft“.
- **d (blind, Wolfram symbolisch):** (i) ∏(1 + a cos(δ + 2πk/3)) = 1 − 3a²/4 + (a³/4) cos 3δ exakt; (ii) cos 3δ ist invariant unter δ → −δ und δ → δ + 2π/3 und
  wechselt das Vorzeichen unter δ → δ + π/3; (iii) die niedrigste nicht konstante Fourier-Mode, die unter D₃ invariant ist, ist cos 3δ. Kriterium: alle drei exakt.
- **e (blind):** Robustheit: V = Drehung + q cos 3δ mit q = −ε, ε ∈ {10⁻², 10⁻⁴, 10⁻⁶}, φ = x_lepton, beide Sektoren. Kriterium: globales Minimum eindeutig (keine Entartung
  innerhalb 10⁻¹²) auf dem gewählten Zweig, Abstand zum Zweig π/12 − φ bzw. π/6 − φ fällt mit ε (bei 10⁻⁶ unter 10⁻⁵).

## Gesamturteil (vorab)
- **trägt:** a, b, d, e erfüllt und c schließt den verworfenen Zweig aus (> 3σ).
- **trägt teilweise:** a, b, d, e erfüllt, c schließt nicht aus; oder alle erfüllt — in jedem Fall wird offen gesagt, dass das **Vorzeichen** des kubischen Terms gesetzt
  bleibt (die Regel ersetzt eine Skala durch ein Vorzeichen, sie leitet das Vorzeichen nicht her).
- **widerlegt:** b scheitert (die Sektoren verlangen entgegengesetzte Regeln) oder a scheitert.

## Grenzen (vorab)
Zirkulantensektor, Baumniveau, K = ⅔, H99 vorausgesetzt. Ein Term ∝ det Y/μ³ ist als Potentialterm nicht polynomial; die Regel wird als Auswahlregel geprüft, nicht als
Feldgleichung. Der Drehwinkel φ selbst bleibt unhergeleitet (H221).
