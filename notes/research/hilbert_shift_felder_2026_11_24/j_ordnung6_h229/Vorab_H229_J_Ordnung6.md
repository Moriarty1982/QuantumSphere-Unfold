# Vorab-Notiz H229 (k443): J bei Ordnung 6 lockern – legt das volle Quadrat N² Zweig und Winkel φ fest?

Stand 28.11.2026, vor der Rechnung festgeschrieben. Auf der Entscheidungskarte nach H228 („Wie geht es nach H228 mit dem Winkel φ weiter?“) hat der Autor
um 12:19 UTC „J bei Ordnung 6 lockern“ gewählt. Das ist eine **Postulatsänderung** auf Probe. J in der Ebenen-Lesart (H157/H158) gilt dabei weiter
bis Ordnung 4 und für die J-erlaubten Terme der Ordnung 6. Zusätzlich wird der J-verbotene Teil zugelassen, und zwar nur in der Form, die ihn natürlich
erzeugt: das volle Quadrat der kubischen Norm, λN² mit λ ≥ 0 (Beschränktheit).

## Vorwissen geprüft

- k436: N² = φ⁶ − 6φ⁴r² + 9φ²r⁴ + 2r⁶ + 4φr³(φ² − 3r²) cos 3δ + 2r⁶ cos 6δ. Die Teile φr⁵ cos 3δ und r⁶ cos 6δ haben unter J keinen Partner.
  Stabilität legt im J-erlaubten Raum das Vorzeichen nicht fest.
- H223/k437, nachträglich bemerkt: Im vollen Quadrat kommt das Vorzeichen der Daten nur aus dem J-verbotenen Teil; bei K = ⅔ überwiegt −12φr⁵ den
  J-erlaubten Teil +4φ³r³.
- H222/k435: Zweig = Vorzeichen von cos 3δ (q < 0 wählt in beiden Sektoren den Datenzweig; der verworfene Re-Zweig liegt 51σ daneben).
- H221/k434: Ordnung 6 mit Sektorskala als Quelle des Versatzes ausgeschlossen (9σ, Faktor 1,59), gemeinsame Drehung gibt gleiche Versätze exakt.
- H225/k439: E(φ) = e_Im(φ) + e_Re(φ), Sektortausch V_Re(−δ; π/4 − φ) = V_Im(δ; φ) exakt für alle q und r; Minimum π/8 bei q allein,
  0,916 bzw. π/8 bei r cos 6δ allein. H226: Tauschbruch widerlegt. H228: φ als Asymptote widerlegt.

**Vorab bekannt, also nicht blind:** Bei K = ⅔ (φ_N² = 2r²) ist der δ-Teil von N² gleich 2r⁶ g(δ) mit g(δ) = −2√2 cos 3δ + cos 6δ. Der cos 3δ-Koeffizient ist
negativ, also wählt der Term in führender Ordnung den Datenzweig (H222). Teil a ist deshalb nicht blind. Neu ist, dass cos 6δ mit **festem** Verhältnis
r/q = −1/(2√2) mitkommt; was das für Zweig und φ bedeutet, ist nicht vorab gerechnet.

## Modell (fest)

Je Sektor, wie H225: V_s(δ) = −α′_s cos 2(δ − χ_s − φ) + w·g(δ) mit (α′, χ) = (+1, π/4) im Im-Sektor und (−1, 0) im Re-Sektor; w = λ·2r⁶/|α′| ≥ 0
dimensionslos. Datenzweige: δ_Im = π/12 − φ, δ_Re = π/6 − φ (H222). Ziel x = 0,0395773407 (σ 7,8·10⁻⁷), x_ν = 0,04336 ± 0,00213.

## Teile und Kriterien

- **a (Zweig, nicht blind):** Für w ∈ {10⁻⁴, 10⁻³, 10⁻², 0,03, 0,1, 0,3, 1, 3} und φ ∈ [0,01; 0,06] liegt das globale Minimum in δ jedes Sektors auf dem
  Datenzweig? Bericht: der w-Bereich, in dem beide Sektoren richtig wählen.
- **b (Winkel als Modulus, blind):** Globale Minima von E(φ; w) über eine Periode, w wie in a und zusätzlich fein in [10⁻⁴; 10].
  - *trägt:* globales Minimum innerhalb 1 % von x im skalenfreien Grenzfall w → 0⁺ oder bei w = 1 (vorab benannt als natürliche Werte);
  - *trägt teilweise:* nur für einen angepassten Wert w* liegt das globale Minimum bei x (eine Zahl für eine Zahl, keine Vorhersage); dann wird geprüft, ob w*
    in beiden Sektoren den Datenzweig wählt;
  - *widerlegt:* kein w gibt ein globales Minimum innerhalb 1 % von x.
  Vorab erwartet wegen des exakten Sektortauschs: Minima treten paarweise bei φ* und π/4 − φ* auf (oder bei π/8); ein Paar ist zulässig.
- **c (ohne Drehung, Skalen-Lesart, blind):** φ = 0. w wird aus dem Im-Sektor so bestimmt, dass das Minimum bei δ_Im = π/12 − x liegt; damit wird der
  Re-Versatz x_ν^pred vorhergesagt. *trägt teilweise*, wenn x_ν^pred innerhalb 2σ von 0,04336 liegt (ein Parameter für zwei Zahlen), sonst *widerlegt*.
  Vergleich mit H221 (dort J-erlaubte Ordnung 6, 9σ).

**Gesamturteil:** trägt, wenn b trägt; trägt teilweise, wenn b oder c teilweise trägt; sonst widerlegt. Teil a fließt nicht ins Urteil ein, wird aber
berichtet (wählt w den falschen Zweig, entfällt das betreffende w in b und c).

## Werkzeuge

Python `k443_test_h229.py` (numpy/scipy, Ausgabe `k443_out.txt`); Wolfram `k443b_gegenprobe.wl` (Ausgabe `k443b_out.txt`): N² symbolisch (δ-Teil bei
K = ⅔), Minima in δ mit FindMinimum und Gitter (N vor Sort), E(φ) an Stichproben und Teil c unabhängig. Qiskit ist nicht geeignet.

Vergeben: H229, k443.
