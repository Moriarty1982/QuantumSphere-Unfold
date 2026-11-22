# W1 mit Holst-Term: Welche Frame-Abbildung ändert den Immirzi-Parameter? (Erkundung, nicht blind, 22.11.2026)

**Ergebnis in einem Satz:** In der Wirkung W1 + Holst lassen alle Lorentz-Transformationen, auch der komplexe Boost mit Rapidität
η + iπ/2, den Barbero-Immirzi-Parameter γ fest. Nur eine Dualitätsdrehung der Krümmung ändert ihn, und zwar exakt nach
**arctan γ′ = arctan γ + θ** (nur auf R) bzw. **+ 2θ** (auf Σ und R). Keiner der vorab gelisteten Winkel bildet γ_M auf γ_T ab.

Auftrag des Autors: „Ja, Holst-Erkundung“. Damit ist die seit 6.11. eingefrorene Dynamik-Linie W1/W2 für diese Erkundung geöffnet.
Verfahren vor der Rechnung festgelegt: `Methoden_Notiz.md` (Commit 1e9a5e2a). Skript `holst_duality.wl`, Ausgabe
`run/holst_duality.txt`, Werkzeug Wolfram Language (exakt). Keine H-Nummer.

## Rechnung
L = A⟨⋆Σ, R⟩ + B⟨Σ, R⟩ mit A = −1/(2κ) (W1, Vorzeichen nach v4.10.0-r01) und B/A = 1/γ (Holst); ⟨X, Y⟩ = ½ X_ab Y^ab, Signatur (+,−,−,−).
1. ⋆² = −1, ⟨⋆Σ, ⋆R⟩ = −⟨Σ, R⟩, ⟨Σ, ⋆R⟩ = ⟨⋆Σ, R⟩: exakt.
2. Boost, Drehung und komplexer Boost (η + iπ/2) auf Σ und R zugleich: L exakt invariant. Ein komplexer Boost ändert γ also nicht.
3. Dualitätsdrehung R ↦ cos θ R + sin θ ⋆R:
   - (D1) nur auf R: A′ = A cos θ + B sin θ, B′ = B cos θ − A sin θ, also **γ′ = tan(arctan γ + θ)**;
   - (D2) auf Σ und R: dasselbe mit 2θ.
   - Flächenquant a ∝ κγ = −1/(2B): **a′/a = cos(arctan γ)/cos(arctan γ + θ)** (D1), mit 2θ (D2).
   - Die Drehung um π/2 (J_B) gibt unter D1 γ′ = −1/γ (γ_M ↦ −4,21); unter D2 bleibt γ, nur das Vorzeichen von A kehrt sich um.

## Vorab festgelegte Auswertung (Schranke 0,5 %)
| θ | γ′ (D1) | γ′ (D2) | a′/a (D1) | a′/a (D2) |
|---|---|---|---|---|
| π/4 | 1,623 | −4,210 | 1,855 | −4,210 |
| π/2 (J_B) | −4,210 | 0,2375 | −4,210 | −1 |
| iπ/2 | 0,036 + 0,925 i | 0,002 + 0,997 i | komplex | komplex |
| η | 1,140 | 9,718 | 1,475 | 9,505 |
| 2η | 9,718 | −0,469 | 9,505 | −1,074 |

Ziel γ_T = 0,1274 bzw. a′/a = 1/γ_L = 0,5363: **kein Treffer** (kleinste Abweichung 33 %, bei iπ/2 ohnehin komplex). Der Winkel, der γ_M
exakt auf γ_T bringt, ist θ* = −0,1065 (D1) bzw. −0,0533 (D2); dort ist a′/a = 0,981, nicht 1/γ_L. Mit weiteren Konstanten nicht verglichen.

**Nachträglich (nach dem Sehen der Ausgabe, zählt nicht):** a′/a(D1, π/4) = 1,8548 liegt 0,53 % neben γ_L selbst (nicht 1/γ_L, wie
vorab verglichen). Richtung und Schranke passen nicht zur vorab festgelegten Auswertung; bei 20 Vergleichen und mehreren nachträglich
denkbaren Lesarten ist das ohne Gewicht und wird nur der Vollständigkeit halber genannt.

## Lesart
- **Die einzige Stelle in W1 + Holst, an der ein frame-abhängiges γ entstehen kann, ist eine Dualitätsdrehung der Krümmung.** Das schärft
  r30.1: Nicht die imaginäre Rapidität iπ/2 (ein komplexer Boost) ändert γ, sondern nur eine Dualität auf R. Eine solche Drehung ist keine
  Symmetrie der Wirkung; sie ändert κ und γ zugleich. J_B auf die Krümmung fortzusetzen wäre eine Setzung.
- Die natürliche Fortsetzung (J_B = Drehung um π/2) gibt die bekannte Abbildung γ ↦ −1/γ (D1) oder lässt γ fest (D2), nicht γ_T.
- **Für OP1 heißt das:** Die Feldgleichung W1 + Holst erzeugt das Verhältnis γ_M/γ_T = γ_L nicht aus einer der Frame-Abbildungen. Der
  benötigte Winkel θ* = −0,1065 ist im Bestand nicht ausgezeichnet. OP1 bleibt offen; ein Test mit Kriterium bräuchte erst einen Grund
  für einen bestimmten Winkel.
- Die Dynamik-Linie W1/W2 bleibt im Übrigen, wie am 6.11. entschieden, eingefroren; diese Erkundung ändert W1 nicht.
