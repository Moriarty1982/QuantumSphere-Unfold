# Ergebnis H184: Farbschwingungen um ein zirkulantes Leptonvakuum bilden eine hermitesche Zirkulante

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H184_Quarks_als_Schwingungen_um_das_Leptonvakuum.md` (Commit 3048625, vor der Rechnung). Skripte
`k387_test_h184.py` (`k387_out.txt`) und `k387b_gegenprobe.wl` (`k387b_out.txt`). Anlass: Entscheidung des Autors nach H183, „Ein Vakuum, Sektoren
schwingen“.

Werkzeuge: Python (numpy) mit expliziten Oktonionen und Jordan-Produkt auf H₃(𝕆), invariante quadratische Formen aus dem Stabilisator (Mittelung über
die Gruppe, Nullraum), zweite Variation aus den Polynomen. Wolfram Language exakt für die Regel der Spurpotentiale und für Eigenwerte und
Eigenvektoren der Zirkulante. Qiskit nicht eingesetzt (keine Schaltung). Grenze der Gegenprobe: Der symbolische Vergleich der charakteristischen
Polynome wurde von Simplify nicht auf null gebracht; die Brannen-Form der Eigenwerte ist in Wolfram nur numerisch gezeigt (1,1·10⁻¹⁶), exakt gezeigt
sind die Eigenwerte auf den Fourier-Vektoren (α + 2β_r, α − β_r ∓ √3β_i), was dieselbe Aussage ist.

**Ergebnis in einem Satz:** Um das Leptonvakuum W₀ (Zirkulante in H₃(𝕆), K = ⅔, δ = 2/9 als Eingabe) haben die 18 Farbrichtungen genau drei
Frequenzquadrate mit Vielfachheit je sechs (drei Generationen eines Farbtripletts), gegeben durch eine hermitesche Zirkulante mit drei freien Größen
und festen Fourier-Eigenrichtungen; Zahlen für die Quarkmassen folgen daraus nicht.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H184a (nicht blind) | Vielfachheiten (6, 6, 6) in 25 von 25 Proben; Form α + βS + β̄S² mit Rest 1,3·10⁻¹⁵; Spektrum α + 2\|β\|cos(arg β + 2πk/3) | ≥ 20 Proben, (6, 6, 6), Fourier-Eigenräume | **bestätigt** |
| H184b | mit τ: Vielfachheiten (6, 12) in 25 von 25 Proben; Im β ≤ 2,3·10⁻¹⁷ | in allen Proben entartet | **bestätigt** |
| H184c | farblose 9 Richtungen: 0 Nullrichtungen in 8 von 8 Proben (mit P und mit P und τ); erwartet 0 | Zahl = Bahndimension | **bestätigt** |
| Bericht | freie Größen der Farb-Zirkulante: 3 (α, Re β, Im β) für drei Massen; mit τ: 2. Stabile Proben (alle Frequenzquadrate > 0): 0 von 8 | Bericht | keine Aussage zur Stabilität |

Zahl der invarianten quadratischen Formen auf den Farbrichtungen: nur Farbe 9 (hermitesche 3×3-Matrizen im Platzindex), mit P 3, mit P und τ 2.

Kontrollen: P und T (Platztausch zweier Plätze) sind Automorphismen des Jordan-Produkts (Defekt 1,3·10⁻¹⁵ und 1,8·10⁻¹⁵). Die Konjugation K der
Einträge und τ = K∘T sind es **nicht** (Defekt 6,86). W₀ ist fest unter P und τ, nicht unter T (T bildet δ auf −δ ab). Eigenwerte von W₀:
0,04035; 0,580212; 2,379438 (Brannen-Form, K = 0,666667). Farbe lässt W₀ fest (1,2·10⁻¹⁶).

## Lesart
- **Drei Generationen.** Die drei Frequenzen je Farbtriplett kommen allein aus der Symmetrie des Vakuums (SU(3)_c × ℤ₃). Die Form ist dieselbe wie
  bei den Leptonen (Brannen-Form), mit eigenem α, |β| und eigener Phase. Das stützt die Lesart „ein Vakuum, Sektoren schwingen“ strukturell: Ein
  Quarktyp bekommt K und δ als freie Größen der Schwingungen, nicht als zweites Vakuum.
- **Keine Vorhersage.** Drei freie Größen für drei Massen. K und δ der Quarks sind damit angepasst, nicht hergeleitet.
- **τ muss gebrochen sein.** Mit τ sind zwei Frequenzen gleich. Drei verschiedene Quarkmassen verlangen Im β ≠ 0. τ ist kein Automorphismus der
  Albert-Algebra; seine Brechung ist also keine zusätzliche Annahme gegenüber einem Potential aus Jordan-Invarianten, aber ihre Größe ist frei.
- **Mischung.** Alle Zirkulanten haben dieselben Eigenrichtungen (Fourier-Vektoren). Haben zwei Quarktypen diese Form, ist der Baumwert der
  CKM-Matrix die Einheit (wie k374). Die ganze CKM-Matrix braucht weiter eine Brechung des Platztauschs P.

## Zusatz (nachträglich, Erkundung): Potentiale aus Spuren der Albert-Algebra
Jede Farbmode gehört zu einem Paar (i, j) von Eigenrichtungen von W₀ (Eigenwerte l_i, l_j, dritter l_k). Zweite Variation je Invariante
(Python über vier Vakua angepasst; für Tr Wⁿ in Wolfram exakt):

| Invariante | Frequenzquadrat der Mode (i, j) |
|---|---|
| Tr W² | 4 |
| Tr W³ | 6(l_i + l_j) |
| Tr W⁴ | 8(l_i² + l_i l_j + l_j²) |
| (Tr W²)² | 8(l_i² + l_j²) + 8l_k² |
| Tr W · Tr W³ | 6(l_i² + l_j²) + 12 l_i l_j + 6 l_k(l_i + l_j) |
| (Tr W)² Tr W² | 4(l_i² + l_j²) + 8 l_i l_j + 8 l_k(l_i + l_j) + 4 l_k² |
| Tr W² · Tr W_U² | 4(l_i² + l_j²) + 4 l_k² |
| Tr W² ∘ W_U² | keine Funktion des Paars allein (Rest 0,34) |
| Tr W_U², Tr W_U³, Tr W_U⁴, (Tr W_U²)², (Tr W)² Tr W_U² | 0 |

(W_U: Anteil von W in H₃(ℂ_U), also ohne Farbe.)

- **Regel (Wolfram exakt):** Für ein F₄-invariantes Potential Σ v(l_k) ist das Frequenzquadrat der Mode (i, j) gleich
  2(v′(l_i) − v′(l_j))/(l_i − l_j). Ist W₀ stationär (v′(l_k) = 0 für alle k), sind **alle Farbschwingungen masselos**: Sie liegen in der Bahn von
  W₀ unter F₄ (Python: höchstens 1,6·10⁻¹²).
- **Folge:** Frequenzen der Farbschwingungen kommen allein aus Termen, die U auszeichnen (hier Tr W² ∘ W_U² und Tr W² · Tr W_U²). Die Quarkmassen
  messen in dieser Lesart die Brechung F₄ → SU(3)_c × SU(3) durch die Wahl von U, nicht das Leptonvakuum selbst.
- Im F₄-invarianten Beispiel hat der farblose Block die Eigenwerte −1,514; sechsmal 0; 1,924; 7,089. Sechs Nullrichtungen aus der
  Familien-SU(3), drei massive, davon eine negativ: W₀ ist dort ein Sattel (bei kubischem v′ liegt der mittlere Eigenwert auf einem Maximum von v).
  Ein Minimum braucht ebenfalls die U-abhängigen Terme oder höheren Grad. Nicht weiter verfolgt.

## Bilanz der Setzungen
| | gesetzt | hergeleitet | offene Wahl wandert nach |
|---|---|---|---|
| Träger | W ∈ H₃(𝕆), reell (ein Quarktyp) | – | Up/Down im komplexen Feld (H182) |
| Vakuum | Zirkulante, K = ⅔, δ = 2/9 (Messwerte) | – | Herkunft von δ (H166) |
| Symmetrie | SU(3)_c, P; τ wahlweise | Zirkulante, (6, 6, 6), Fourier-Richtungen; mit τ (6, 12) | Größe der τ-Brechung (Im β) |
| Potential | Grad ≤ 4, Koeffizienten zufällig | F₄-Teil trägt nichts zu den Farbfrequenzen bei | Koeffizienten der U-abhängigen Terme |
| Massen | keine Zuordnung Frequenz ↔ Masse | – | α, β je Quarktyp (angepasst) |

## Grenzen
Reelles Feld, daher ein Quarktyp; die Trennung von Up und Down (H182) verlangt das komplexe H₃(ℂ ⊗ 𝕆) und ist nicht gerechnet. J ist auf H₃(𝕆)
nicht gefordert. Grad ≤ 4, statisch und homogen, ohne Ableitungsterme und ohne rotierende Lösungen. Stabilität von W₀ ist nicht gezeigt (0 von 8
Zufallsproben stabil, ohne Aussage). Die Invariantenfamilie des Zusatzes ist nicht vollständig; H184a und H184b stützen sich auf die vollständige
Zählung der invarianten quadratischen Formen. Kein Vorzeichen gesetzt. OP3 und OP4 bleiben offen.

## Nächster Schritt (Vorschlag)
Komplexes Feld in H₃(ℂ ⊗ 𝕆): ob der eine ladungsungerade Term aus H182 die Zirkulanten für Up und Down trennt, und welche U-abhängigen Terme α und β
festlegen. Vergeben: H184, k387. Nächste frei: H185, k388.
