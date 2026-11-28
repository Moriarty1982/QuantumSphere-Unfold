# Ergebnis H221 (k434): Der neutrale Sektor schließt Skala und Konjugationsterm als universelle Quelle des Versatzes aus — gleiche Versätze kommen aus einer skalenfreien Drehung

**Datum:** 2026-11-28. **Vorab:** `Vorab_H221_Skala_zwei_Sektoren.md` (Commit d8fbbb9, vor der Rechnung). **Urteil: trägt teilweise** (beide Wege in universeller
Form ausgeschlossen, sie werden nicht gegeneinander getrennt); **nach dem vorab festgelegten Gesamtkriterium: spricht für skalenfrei.**
**Werkzeuge:** Python (`k434_test_h221.py` → `k434_out.txt`), Wolfram unabhängig (`k434b_gegenprobe.wl` → `k434b_out.txt`); alle gemeinsamen Zahlen stimmen
überein, Teil d in Wolfram symbolisch. Qiskit nicht einschlägig. Teil a nicht blind (H168), b teilweise nicht blind (lineares √2 vorab gesehen), c und d blind.

## Frage
H167 fand im geladenen Sektor (Im-Sektor, geladene Leptonen, c = 1) zwei gleichwertige Wege, das Elektron aus dem Oktanten zu heben: den skalenfreien
Konjugationsterm (α/α′ = 0,0793) und einen Term sechster Ordnung, der eine Skala braucht (q/α′ = −0,0852, q = β₃v²/Λ²). Der neutrale Sektor (Re-Sektor, c = 0)
muss denselben Versatz tragen (H168; H213: x_ν = 0,04336 ± 0,00213). Trennt er die beiden Wege, wenn ihre dimensionslosen Koeffizienten in beiden Sektoren gleich sind?

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| Kontrolle | geladen, Weg S: Minimum 0,2222220 (δ* auf 2·10⁻⁹); Weg K: δ* ist eines von zwei entarteten Minima (bis Ordnung 4 wählt nichts, H167) | — | reproduziert |
| a (nicht blind) | Weg K neutral: V = (1 + α) cos 2δ, Minimum bleibt bei π/6, **x_ν,pred = 0**, R = 0,0407 (**+23σ**) | ≤ 2σ | **scheitert** |
| b (teilw. nicht blind) | Weg S neutral, \|q/α′\| = 0,0852: x_ν,pred = **+0,0630** (richtiges Vorzeichen, **+9,2σ**, R = 0,0261, −8,7σ) bzw. −0,0630 (anderes Vorzeichen, −50σ). Verhältnis zum geladenen Versatz **1,59** (linear √2) | ≤ 2σ | **scheitert** |
| c (blind, Fit) | beide Terme universell: (α/α′, q/α′) = (+0,0238, −0,0596) bzw. (+0,0266, −0,0567) treffen beide Versätze exakt, als globale Minima; weitere Lösungen nur mit \|α\| > 1 | Existenz, Größe | natürliche Lösung existiert — **zwei Parameter für zwei Zahlen, keine Vorhersage** |
| d (blind) | gemeinsame Drehung χ → χ + φ in beiden Sektoren: Minima exakt bei π/12 − φ und π/6 − φ für **jedes** φ (Wolfram: Steigung 0, Krümmung 4, symbolisch); Python 4·10⁻⁹ (Grenze der Brent-Suche ≈ 10⁻⁸) | < 10⁻⁹ | **trägt** (exakt) |

**Gesamturteil.** Nach den vorab festgelegten Regeln: a und b scheitern (> 3σ), d trägt ⇒ **spricht für skalenfrei.** Zur Hypothese „der Re-Sektor trennt K und S“:
**trägt teilweise** — er schließt beide in universeller Form aus, trennt sie aber nicht voneinander.

## Lesart
- **Eine Skala als Quelle des gemeinsamen Versatzes passt nicht.** Mit einer Sektorskala Λ_s ∝ v_s (die einzige nach H168 zulässige Form) ist q in beiden Sektoren
  dieselbe Zahl. Der Term sechster Ordnung verschiebt dann den neutralen Sektor um das 1,59-Fache des geladenen, weil cos 3δ am neutralen Zweig (δ ≈ π/2) mit voller
  Steigung, am geladenen (δ ≈ 5π/4) nur mit 1/√2 eingreift. Die Daten verlangen aber gleiche Versätze (1,78σ verträglich); der Skalenweg liegt 9σ daneben.
- **Der skalenfreie Konjugationsterm passt auch nicht.** Für c = 0 ist er dieselbe Funktion wie der Spin-1-Term und verschiebt nichts (H168); 23σ daneben.
- **Was gleiche Versätze von selbst liefert, ist eine Drehung.** Wird der Mischungswinkel χ in beiden Sektoren um denselben Winkel φ gedreht, rücken beide Minima
  exakt um φ — für jedes φ, ohne weiteren Term. Eine Drehung ist dimensionslos, sie braucht keine Skala. Das ist die Antwort, die diese Rechnung auf die Frage des
  Autors gibt („einen Grund, warum es skalenfrei sein muss“): **Der gemeinsame Versatz beider Sektoren ist ein Winkel, keine Skala.** Die Skala erklärt ihn nicht.
- **Was offen bleibt.** (i) Der Drehwinkel φ = x selbst ist nicht hergeleitet (eine dimensionslose Zahl, gemessen über m_μ/m_e). (ii) Ohne Ordnung 6 ist jedes Minimum
  zweifach entartet (π/12 ± φ bzw. π/6 ± φ); bisher wählte nur der Term sechster Ordnung den Zweig (H167). Eine skalenfreie Zweigwahl ist nicht gefunden.
  (iii) Eine Mischung beider Terme mit kleinen Werten passt (c), braucht aber wieder eine Skala (q ≠ 0) und ist ein Fit.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet/gerechnet:** Versatz im neutralen Sektor für beide Wege (exakt), Verhältnis 1,59 (linear √2), Exaktheit der Drehung (symbolisch), Fit-Lösungen in c.
- **Gesetzt:** Universalität der dimensionslosen Koeffizienten zwischen den Sektoren (|α′| gleich, Λ_s ∝ v_s); Vorzeichen von α′_ν so, dass c = 0 bei π/6 liegt;
  Zirkulantensektor, Baumniveau, K = ⅔; bei Ordnung 6 nur cos 3δ; H99.
- **Nachträglich bemerkt:** Das passende Vorzeichen im Weg S verlangt q_ν = −|q| bei α′_ν = −1, also q/α′ in beiden Sektoren mit **entgegengesetztem** Vorzeichen
  (geladen −0,085, neutral +0,085). Das ändert das Urteil nicht (Betrag 9σ daneben).

## Bilanz der Setzungen (Skala-Strang)
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H155 | Skala, Tauschsymmetrie | K = ⅔ stabil bis 2. Ordnung | δ als Fit (R*) |
| H167 | Skala, J, c = 1 | Oktant aus Spin-1-Term; Phase dimensionslos; Skala wählt Zweig | ein kleines Verhältnis (α/α′ oder q/α′) |
| H168 | Brannen für ν, c = 0 | gleicher Versatz beider Sektoren; feste gemeinsame Skala ausgeschlossen | ein dimensionsloses x |
| H221 | Universalität der Koeffizienten | Skala (Ordnung 6) und Konjugationsterm geben ungleiche Versätze; Drehung gibt gleiche exakt | x als Drehwinkel (dimensionslos); Zweigwahl ohne Skala offen |

## Grenzen
Nur Zirkulantensektor, Baumniveau; Stabilität gegen nicht zirkulante Richtungen nicht gerechnet. Ordnung 6 nur cos 3δ. Universalität der Koeffizienten ist eine
Setzung; mit sektorabhängigen Koeffizienten kann jeder Weg jeden Versatz treffen (dann ohne Vorhersage). H99 vorausgesetzt. Kein Guard berührt; OP3/OP4/OP5 offen.

## Dateien
- `Vorab_H221_Skala_zwei_Sektoren.md` — Vorab-Notiz (vor der Rechnung committet).
- `k434_test_h221.py`, `k434_out.txt` — Python-Rechnung und Ausgabe (zweiter Lauf; der erste Lauf mit grober Gitter-Entartungsliste ist ersetzt, siehe unten).
- `k434b_gegenprobe.wl`, `k434b_out.txt` — Wolfram-Gegenprobe und Ausgabe.

Hinweis zur Rechnung: Ein erster Python-Lauf bestimmte entartete Minima nur auf dem Gitter (Auflösung 1,6·10⁻⁵); das gab scheinbare Abweichungen von 10⁻⁵ in d und
verhinderte die Fit-Konvergenz in c. Behoben durch Nachschärfen jedes lokalen Minimums (Brent); Ergebnisse a und b unverändert.

Vergeben: H221, k434. Nächste frei: H222, k435 (vor Vergabe gegen `main` prüfen).
