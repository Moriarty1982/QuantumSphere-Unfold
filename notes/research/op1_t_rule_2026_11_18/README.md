# OP1: Die Regel des Frames T (nur j = ½) – Bestand der Gründe und eine Kreisstelle (Erkundung, nicht blind, 18.11.2026)

**Ergebnis in einem Satz:** Von fünf Gründen dafür, dass T nur j = ½ zählt, ist keiner datenfrei und tragfähig: Zwei sind im Repo schon belastet,
zwei sind ausdrückliche Annahmen, und der fünfte, die Dimensionsleiter der Moran-Lesart, setzt das T-Quant als Einheit und ist damit für T im Kreis.

Auftrag des Autors: „T-Regel angehen“ (schwächste Stelle aus `../op1_common_premise_2026_11_18/`). Erkundung, nicht blind; die eine Rechnung
(`k237_ladder_unit.py`, Ausgabe `run/k237_stdout.txt`) prüft nur, für welche Einheit die Dimensionsleiter gilt. Keine H-Nummer.

## Vorwissen geprüft
`../op1_common_premise_2026_11_18/` (fünf Gründe), `../v4_10_0_r09/Erkundung_Zaehlregel_Prinzip.md` und `../v4_10_0_r10/Erkundung_Bruecke_P2_Unruh.md` (P2),
`../op1_frame_irreducibility_2026_11_15/` und `../op1_s1_check_2026_11_16/` (Irreduzibilität, (A)), `../op1_i1_crossing_2026_11_16/` und
`../op1_flux_lines_2026_11_17/` (Querungen), `../op1_i1_string_endpoints_2026_11_15/` (I1, CT-004), `../op1_moran_geometry_2026_11_17/` (Leiter),
`../op1_two_readings_2026_11_17/` (Lesart (B)), `../v4_10_0_r09/llm/k218_out.txt` (γ-Werte der neun Regeln).

## Die fünf Gründe
| Grund | Stand |
|---|---|
| G1 Tachyon-Boden: T erreicht nur die kleinste Anregung (P2) | trägt nicht: Über erstes Gesetz und Unruh zählen M und T gleich (r10) |
| G2 Irreduzibilität: T wirkt irreduzibel, also j = ½ (r17.3) | braucht (A); (A) ist keine Gleichheit der Gruppen und fällt unter (S1′) (16.11.) |
| G3 Eine Querung = ein Strang (r24.4) | Annahme CT-002; Querungen passen nicht zum isolierten Horizont (17.11.); die Frequenzkette gilt nur unter (H), der Bestand stützt (B) |
| G4 Endpunkte offener Strings in der Fundamentaldarstellung (I1) | Annahmen Chan–Paton und „T = String-Sektor“ (CT-004) |
| G5 Dimensionsleiter: T ist die reichste Regel auf einer Linie | **im Kreis**, siehe unten |

## Neu: Die Leiter hängt an der Einheit, und die Einheit ist T
Die Moran-Lesart schreibt die Zählgleichung in Einheiten des T-Quants (2πγ_T a(½) = ln 2). Damit ist D_T = 1 und „T füllt die Strecke genau“
(2 · ½ = 1) Folge der Wahl, nicht Befund. Allgemein passt eine Regel R in ℝ^d genau dann, wenn γ_R ≤ d · γ₀ (γ₀ = Einheit). Gerechnet:

| Einheit γ₀ | d = 1 | d = 2 | d = 3 |
|---|---|---|---|
| γ_T (Moran-Notiz) | **T** | M | P |
| γ_M/2 (M füllt die Ebene) | S1, g = 2 | M | P |
| γ_P/3 (P füllt den Raum) | S1, g = 2 | I, g = 2 | P |
| 1/(2π) | I, g = 2 | P | P |

Die Leiter T, M, P gilt genau für γ₀ ∈ [1; 1,0757) · γ_T. Die **untere Grenze ist γ_T selbst**: Jede Einheit darunter verliert T auf der Linie.
Wählt man die Einheit über M (D_M = 2) oder P, steht auf der Linie eine andere Regel. Für M und P ist die Leiter also eine Aussage, für T nur dann,
wenn eine Einheit im schmalen Fenster ohne Bezug auf T begründet wird. Das ist bisher nicht geschehen.

## Rückwärtssuche: Was ein datenfreier Grund für T leisten müsste
Ziel: T zählt je Punktierung genau ein Dublett mit der kleinsten Fläche (j = ½, zwei Zustände). Notwendig ist eine Eigenschaft von T, die vor den
Daten feststand und M davon trennt. Im Bestand stehen dafür nur: T ist das J_B-Bild von M (Konvention F, Rapidität η + iπ/2), T kehrt Helizität
und Laufrichtung um (r16.3(b), 16.11.), und T zählt in r24.4 Querungen. Daraus Kandidaten, keiner geprüft:
1. **J_B als Auswahl:** Welche Extremdubletts |j, ±j⟩ bildet die Dualitätsdrehung um π/2 so ab, dass J_B² = −1 auf ihnen gilt wie auf χ? Falls nur
   j = ½, wäre G2 ohne (A) ersetzt. Analytisch prüfbar.
2. **Unabhängige Einheit für G5:** eine vorab festgelegte Liste natürlicher Einheiten (ohne γ_T) gegen das Fenster [1; 1,0757) · γ_T; das Fenster ist
   schmal, ein Treffer wäre selten, keiner zu erwarten.
3. **Literatur (aus Vorwissen, ungeprüft):** Der ABCK-Wert entstand aus der Annahme, dass Punktierungen mit j = ½ dominieren; DL und Meissner haben
   sie später aufgehoben. Die T-Regel ist also die frühere Näherung der Literatur. Ein Grund, warum ein Frame genau diese Näherung „sieht“, fehlt.

Die zurückgestellte Idee I1 (Auslöser 3) ist bereits G4 und gibt nur eine weitere Annahme.

## Lesart
- Die T-Regel ist im Bestand nicht begründet. Die Dimensionsleiter trägt für T nichts Eigenes, solange die Einheit an T hängt; das schwächt auch die
  Moran-Lesart als gemeinsames Prinzip für M und T (gemeinsame-Prämisse-Notiz, Befund 5).
- OP1 offen; H98, H102, H112 unverändert.

## Nachtrag (18.11.2026): Kandidat 1 geprüft – J_B² = −1 wählt nicht j = ½
Auftrag des Autors: „J_B-Kandidat prüfen“. **Erkundung, nicht blind:** Der Ausgang steht analytisch fest. Skript `k238_jb_square.py`, Ausgabe
`run/k238_stdout.txt`.

**Berichtigung zuerst:** Kandidat 1 war schon weitgehend beantwortet. Der Nachtrag vom 15.11. in `../op1_frame_irreducibility_2026_11_15/` zeigt,
dass „R² = −1“ die Kramers-Regel wählt (alle halbzahligen j, β = 0,337, ausgeschlossen). Unter (A) wirkt J_B wie R als exp(−iπJ_k); das gilt also
auch für J_B. Das hätte oben stehen müssen. Neu ist nur die Wirkung von J_B ohne (A).

| Wirkung von J_B auf einer Punktierung | J_B² = −1 für | Regel |
|---|---|---|
| (a) unter (A): exp(−iπJ_k) | alle halbzahligen j | Kramers |
| (b1) Dualitätsdrehung um π/2, Phase je Vorzeichen der Helizität (wie beim Maxwell-Feld) | jedes j | keine Auswahl |
| (b2) Dualitätsdrehung um π/2, Phase je Helizität ±j | j = 1, 3, 5, … | schließt j = ½ aus |

**Ergebnis:** Keine natürliche Wirkung von J_B wählt allein j = ½. Kandidat 1 entfällt. Von den Eigenschaften der Frame-Abbildungen geben j = ½ allein
nur die Irreduzibilität (braucht (A)) und der fermionische Austausch (S2, reine Setzung, 15.11.). Offen bleibt Kandidat 2 (eine unabhängige Einheit
für die Dimensionsleiter). OP1 offen.
