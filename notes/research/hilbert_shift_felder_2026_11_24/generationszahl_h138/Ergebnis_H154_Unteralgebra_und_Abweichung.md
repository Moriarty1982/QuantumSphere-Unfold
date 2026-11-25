# Ergebnis H154: Die Algebra erzwingt die Schleife über {1, U} nicht; die Abweichung von ⅔ ist Messrauschen (0,43σ, ganz aus m_τ)

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H154_Unteralgebra_und_Abweichung.md` (Commit 5ef018d; a, g, h nicht blind). Skripte `k337_unteralgebra_abweichung.py`
(`k337_out.txt`), `k337b_gegenprobe.wl` (`k337b_out.txt`, Wolfram). Status: H154a–h bestätigt (alle wie vorhergesagt).**

Anlass: Autor „ja und prüfe woher die abweichung kommt“ (nach H153). Werkzeuge: Python (sympy symbolisch, scipy für den Fluss), Wolfram unabhängig (β-Differenz,
invariante Unterräume, K(θ, δ), Fehlerfortpflanzung, QED-Laufen, zwei Flusspunkte mit Eichung auf acht Stellen gleich). Qiskit nicht eingesetzt (keine Schaltungsfrage).

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H154a | β(1,2) − β(1,1) = [2κ², 8κλ_B, 8λ_B²]; Schleifenbeitrag von y₂: 2(κφ² + 2λ_By₁²)² | ≠ 0 für κ, λ_B ≠ 0 | **bestätigt** (nicht blind) |
| H154b | einziger Erzeuger mit invariantem span{1, U}: die U(1) aus exp(αU); U′ dabei **neutral**; sie erhält V nur bei κ = 2λ_A = 2λ_B (volle Norm) | keine Wirkung mit {1, U} invariant und U′ geladen | **bestätigt** |
| H154c | GW-Punkt (Start 0,2; −0,2; 0,2): Massenquadrate 0, 0, 0,496; y₂ Goldstone; K = 0,671941 unverändert | K unverändert | **bestätigt** |
| H154d | Eichung der Ebenen-Drehung, 40 Starts: K 0,634 … 1,922, Std 0,23; 0 Treffer; Tausch zusätzlich gebrochen | Std < 10⁻³; Treffer | **bestätigt**: startabhängig, kein Zug auf ⅔ |
| H154e | K = 0,6666645 ± 0,0000051 (m_τ = 1776,93 ± 0,09 MeV), 0,43σ unter ⅔; Fehler zu 99,99998 % aus m_τ; ⅔ exakt bei m_τ = 1776,969 MeV | < 2σ | **bestätigt**: Messrauschen |
| H154f | QED einschleifig, gemeinsame Skala m_e … M_Z: K − K_pol = +1,13 … +1,18·10⁻³ (≈ 225σ); je eigene Skala: 2·10⁻¹⁶; bei M_Z K = 0,66784 (H1: 0,6678) | Laufen erklärt nicht | **bestätigt** |
| H154g | Form S: K(SGS⁻¹) − K(G) = 0 | symbolisch 0 | **bestätigt** (nicht blind) |
| H154h | K = 1/(3cos²θ), ∂_δK ≡ 0; nötiges Δθ = −1,65·10⁻⁶ | symbolisch 0 | **bestätigt** (nicht blind) |

## Lesart: Teil 1, die Unteralgebra
- **Keine Symmetrie nimmt ein Feld aus der Schleife.** Eine Auswahlregel oder Ladung bestimmt, welche Terme im Potential stehen dürfen. Die Schleife läuft aber über alle
  Felder, die es gibt. Die zweite Ebenenrichtung U′ trägt genau [2κ², 8κλ_B, 8λ_B²] bei. Das verschwindet im Koide-Bereich nie.
- **Die Ladung zeigt in die falsche Richtung.** Die einzige Drehung, die {1, U} als Ganzes erhält, ist exp(αU). Unter ihr ist U′ neutral und {1, U} geladen. Sie erhält das
  Potential nur bei voller Norm, und dort gibt es kein Koide-Kondensat (H150). Die Spiegelung U′ → −U′ macht U′ ungerade, aber ungerade Felder laufen paarweise mit.
- **Masselos heißt nicht abwesend.** Am GW-Punkt ist U′ ein Goldstone und trägt zum Potential längs der flachen Richtung nichts bei. Der Ort des Punkts kommt aber aus dem
  Fluss davor, und dort läuft U′ masselos mit. Entkoppeln kann im skalenfreien symmetrischen Bereich nichts, weil alle Massen null sind.
- **Eichung frisst den Goldstone, aber das Eichfeld läuft dafür mit.** Weil φ neutral ist, bricht es den Tausch zusätzlich. K bleibt startabhängig (0,634 … 1,922).
- **Ergebnis:** Die Algebra erzwingt n_B = 1 nicht. Übrig bleiben zwei Wege, beide Setzungen: (i) U′ ist gar kein Freiheitsgrad, das Feld ist Ψ selbst (eine komplexe Zahl,
  δ nicht dynamisch); (ii) U′ ist schwer und entkoppelt, was eine Skala braucht (nicht skalenfrei). Das ist die Weggabelung „skalenfrei gegen Skala als Setzung“.

## Lesart: Teil 2, die Abweichung
- **Korrektur:** Die in H152 und H153 benutzte Angabe 0,666661 ± 0,000007 beruht auf dem älteren m_τ = 1776,86 ± 0,12 MeV (damit 0,91σ; die 0,81σ in H153 kamen aus dem
  gerundeten Wert). Mit m_τ = 1776,93 ± 0,09 MeV, wie in H146, liegt K 0,43σ unter ⅔. Die Entscheidungen in H152 und H153 ändern sich dadurch nicht.
- **Es gibt nichts zu erklären.** Die Differenz ist Messrauschen und kommt praktisch ganz aus dem Fehler von m_τ. ⅔ exakt verlangt m_τ = 1776,969 MeV, 0,039 MeV über dem
  Mittelwert. Das ist eine prüfbare Vorhersage für die nächsten τ-Massenmessungen.
- **Laufen macht es schlechter, nicht besser.** An einer gemeinsamen Skala verschiebt QED K um etwa +1,2·10⁻³, also rund 225σ, fast unabhängig von der Skala: Die Massen
  laufen wie M^(1 + 3α/2π), und K ist unter solchen Potenzen nicht invariant. Das stimmt mit H1 überein (0,6678 bei M_Z). Mit jeweils eigener Skala fällt der gemeinsame
  Faktor heraus. Koide gilt also für Polmassen, nicht für laufende Massen an einer gemeinsamen Skala.
- **Frame und δ tragen nichts bei.** Form S lässt K exakt gleich (Spuren). K hängt nur an θ, nicht an δ. Eine Abweichung bräuchte Δθ ≈ −1,6·10⁻⁶ aus einem
  tauschbrechenden Term. Die eingefrorene Richtung kann K also nicht verschieben.
- Die große Abweichung aus H150 (K ≈ 0,672) ist davon getrennt. Sie kommt aus 1 gegen 2 Komponenten (H151, H153).

## Grenzen
- Eine Schleife; skalare QED in Landau-Eichung nur als Modell der Eichung; QED-Laufen einschleifig ohne Hadronen- und schwache Beiträge (H1 mit vollem SM-Laufen
  gibt dasselbe Bild).
- Polmasse m_τ = 1776,93 ± 0,09 MeV wie H146; neuere Messungen sind nicht eingearbeitet.
- OP3 offen; kein Vorzeichen gesetzt; kein Guard berührt.
- Vergeben: H154, k337. Nächste frei: H155, k338.
