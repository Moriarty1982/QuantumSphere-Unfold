# Ergebnis H187: Die Adjunkte liefert das Produkt und den dritten Eigenwert, aber nicht die Quarkmassen

**Stand:** 27.11.2026. Vorab-Notiz `Vorab_Notiz_H187_Adjunkte_und_Determinante_gegen_sechs_Quarkmassen.md` (Commit beaa6ae, vor der Rechnung). Skripte
`k390_test_h187.py` (`k390_out.txt`) und `k390b_gegenprobe.wl` (`k390b_out.txt`).

Werkzeuge: Python (numpy, scipy) wie k389: zweite Variation von zwölf Invarianten mit Adjunkter W^# und Kreuzprodukt A × B auf den 36 Farbrichtungen,
Anpassung an sieben Funktionen des Paars über vier Vakua, Fehlerfortpflanzung linear, Zufallskontrolle mit 2000 erfundenen Datensätzen. Wolfram
Language exakt im reduzierten Modell (Quaternion-Unteralgebra, Vakuum diagonal): dieselben Funktionen. Qiskit nicht eingesetzt. Warnungen in Wolfram:
nur Hinweise der Auswerteumgebung.

**Ergebnis in einem Satz:** Die Adjunkte liefert genau die zwei Funktionen, die den Spurpotenzen fehlten (das Produkt l_i l_j und den dritten
Eigenwert l_k), aber weder eine noch zwei Funktionen je Sektor geben die sechs Quarkmassen; Down wird in keiner Lesart getroffen.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H187a | reines l_i l_j aus a5, d3; reines l_k aus a1, a3, d1; reines l_k² aus a2, a4, a7, d2, d4 (Rest ≤ 7·10⁻¹³) | beides gefunden | **bestätigt** |
| H187b | eine Funktion je Sektor: bester Abstand Up 82σ, Down 69σ | beide Sektoren < 3σ | **widerlegt** |
| H187c | zwei Funktionen je Sektor: Up trifft zweimal (0,74σ; 1,05σ), Down nie (bester Abstand 11,8σ) | beide Sektoren < 3σ bei gleicher Lesart und Zuordnung | **widerlegt** |
| Kontrolle | 2000 erfundene Datensätze: Treffer mit einer Funktion 0,00 %, mit zwei Funktionen 2,45 % | Bericht | – |

Verglichen: 9 Funktionen, 36 Paare, je 3 Lesarten (X = √m, m, m²) und 2 Zuordnungen der Generationen, je Sektor.

## Schritt 1 (ohne Daten): Funktion des Paars je Kandidat
Frequenzquadrat der Farbmode zum Paar (i, j); l_k ist der dritte Eigenwert des Vakuums.

| Kandidat | gerade (beide Ladungen gleich) | Kandidat mit D | ungerade (Up − Down)/2 |
|---|---|---|---|
| a1 Re Tr(W^# ∘ W̄) | −4 l_k (dazu ladungsmischend) | d1 Re Tr((W̄ × DW) ∘ W_U) | −⅓ l_k |
| a2 Tr(W^# ∘ W̄^#) | +4 l_k² (dazu ladungsmischend) | d2 Re Tr((W̄ × DW) ∘ (W_U ∘ W̄_U)) | −⅓ l_k² |
| a3 Tr((W × W̄) ∘ W_U) | −2 l_k | d3 Re Tr((W̄ × DW) ∘ W_U^#) | −⅓ l_i l_j |
| a4 Tr((W × W̄) ∘ (W_U ∘ W̄_U)) | −2 l_k² | d4 Re Tr((DW × W_U) ∘ (W̄ × W̄_U)) | +⅙ l_k² |
| a5 Tr((W × W̄) ∘ W_U^#) | −2 l_i l_j | | |
| a6 Tr((W × W̄)²) | −4 l_i l_j + 2 l_k² (dazu ladungsmischend) | | |
| a7 Tr((W × W_U) ∘ (W̄ × W̄_U)) | + l_k² | | |
| a8 Re Tr(W^# ∘ W̄_U^#) | 0 | | |

Funktionsmenge R für Schritt 2 (neun): l_k, l_k², l_i l_j, l_i l_j − ½ l_k², 1, l_i + l_j, l_i² + l_j², ½(l_i² + l_j²) + l_i l_j, l_k(l_i + l_j).

## Schritt 2: gegen die sechs Massen
| Lesart, Zuordnung | Up: eine Funktion | Up: zwei Funktionen | Down: eine Funktion | Down: zwei Funktionen |
|---|---|---|---|---|
| √m, A | 487σ | 8,8σ | 69σ | 11,8σ |
| √m, B | 82σ | **0,74σ** (l_k², ½(l_i² + l_j²) + l_i l_j) | 110σ | 52,6σ |
| m, A | > 10⁵σ | **1,05σ** (l_i l_j, l_i + l_j) | 1201σ | 45,4σ |
| m, B | 1774σ | 219σ | 153σ | 99σ |
| m², A und B | > 10⁸σ | 120σ | > 10⁴σ | 80σ bis 90σ |

(Zuordnung A: Paare nach l_i + l_j aufsteigend ↔ Generationen 1, 2, 3; B: umgekehrt.)

## Lesart
- **Algebraisch trägt der Hinweis aus H186.** Das Kreuzprodukt setzt an die Stelle der zwei Eigenwerte des Paars den dritten: W × W̄ gibt l_k, mit
  der Adjunkten von W_U zusammen das Produkt l_i l_j. Beide gibt es gerade und, mit D, als reinen Unterschied zwischen den Ladungen.
- **Als Erklärung der Massen trägt er nicht.** Down liegt in keiner der sechs Kombinationen näher als 11,8σ. Die zwei Treffer für Up allein sind
  kein Befund: Ein Sektor mit einer Vorhersage und 216 Vergleichen wird leicht getroffen; verlangt war beides zugleich (Zufallsquote dafür 2,45 %).
- **Stand der Lesart „ein Vakuum, Sektoren schwingen“:** Die Symmetrie gibt die richtige Zahl von Zuständen (zwei Ladungen, drei Generationen,
  Brannen-Form), aber die Massen bleiben in allen bisher geprüften Termen frei oder falsch. Die Hierarchie der Quarks ist keine einfache Funktion
  der Lepton-Eigenwerte bis zum Grad 2.

## Bilanz der Setzungen
| | gesetzt | hergeleitet | offene Wahl wandert nach |
|---|---|---|---|
| Träger, Vakuum, Symmetrie | wie H185/H186 | – | – |
| Terme | zwölf Kandidaten mit W^#, A × B, D bis Grad 4 | Funktionen l_k, l_k², l_i l_j, exakt | Koeffizienten |
| Vergleich | Lesart (3), Zuordnung (2), je Sektor eigene Koeffizienten | keine Kombination trifft beide Sektoren | – |
| Massen | Frequenzquadrat ↔ √m, m oder m² | – | welche Abbildung gilt; ob Massen überhaupt Frequenzen dieser Art sind |

Zur Regel „Bilanz der Setzungen“ (AGENTS.md): H184 bis H187 betreffen dieselbe offene Voraussetzung (was die Frequenzen der Farbschwingungen
festlegt). Was gesetzt blieb: das Vakuum (K = ⅔, δ = 2/9), die Farbphase, die Abbildung Frequenz ↔ Masse, die Zuordnung der Generationen.
Was hergeleitet ist: Zahl und Form der Zustände, die Funktionen je Term. Wohin die offene Wahl wanderte: von „welches Potential“ (H183) über
„welche Symmetrie“ (H184, H185) zu „welche Koeffizienten“ (H186, H187), ohne kleiner zu werden. Stillschweigend gewählte Weggabelung, die dem Autor
vorgelegt wird: Alle vier Tests nehmen an, dass Quarkmassen **Frequenzen um das Leptonvakuum im Potential** sind. Nicht geprüft sind
Ableitungsterme (K₁ bis K₃ der Feldgleichung), die die Normierung der Schwingungen je Generation ändern, und die Möglichkeit, dass die Quarks an
einer anderen HS-Stufe sitzen.

## Grenzen
Kandidatenliste nicht vollständig (keine Terme mit zwei D, keine vom Grad > 4, keine Ableitungsterme); Massen bei M_Z ohne Laufen; Stabilität des
Vakuums und Vorzeichen der Frequenzquadrate nicht geprüft; drei oder mehr Funktionen je Sektor geben keine Vorhersage und wurden nicht verglichen.
Kein Vorzeichen gesetzt. OP3 und OP4 bleiben offen.

## Nächster Schritt (Vorschlag, Entscheidung beim Autor)
Entweder die Ableitungsterme der Feldgleichung einbeziehen (kinetische Normierung je Generation; nächste Prüfung in derselben Lesart) oder die
Lesart wechseln (Quarks auf anderer HS-Stufe oder als getrennte Felder). Vergeben: H187, k390. Nächste frei: H188, k391.
