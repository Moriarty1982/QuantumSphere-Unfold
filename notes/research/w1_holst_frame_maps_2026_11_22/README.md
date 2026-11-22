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

## Nachtrag (22.11.2026, nachträglich, analytisch): Die Dualität erhält A² + B²; damit ist γ_L ausgeschlossen
Anlass: Fragen des Autors, ob die 0,5-%-Nähe bei π/4 an der Geometrie der Kugel, am Winkel, an einer Verzerrung der Kugel unter
gleichem Weg oder an einer zweimal ausgeführten imaginären Verzerrung liegen könnte. Keine neue Rechnung; die Aussage folgt aus
Abschnitt (3) der Ausgabe (A′ = A cos θ + B sin θ, B′ = B cos θ − A sin θ).

1. **Erhaltungsgröße.** Jede Dualitätsdrehung, auch eine komplexe und auch mehrfach hintereinander, erhält A² + B², weil
   cos²θ + sin²θ = 1 auch für komplexe θ gilt. Mit A = −1/(2κ), B = A/γ ist das (1 + 1/γ²)/(4κ²).
2. **Folge für das Flächenquant.** Soll das Ergebnis reell sein (reelles γ′, reelles κ′, reelles Flächenquant), sind A′, B′ reelle
   Vielfache derselben Form; dann gilt für das Flächenquant a ∝ κγ = −1/(2B) exakt
   a′/a = ±√((1 + γ′²)/(1 + γ²)).
   Für γ′ = γ_T und γ = γ_M ist das **±0,981** (in der Ausgabe als a′/a bei θ* bereits enthalten: 0,9807913), unabhängig vom Weg,
   von der Zahl der Schritte und von jeder Verzerrung der Kugel, die nur ändert, welcher Winkel zu welchem Wegstück gehört.
   Eine zweimal ausgeführte imaginäre Drehung kann höchstens das Vorzeichen wählen, nicht den Betrag.
3. **Widerspruch zu r10.3.** r10.3 verlangt gleiches G und ein um γ_L kleineres Flächenquant in T (Faktor 0,536). Eine
   Dualitätsdrehung ändert G und γ stets zusammen und hält A² + B² fest; ein reelles Verhältnis 0,536 ist damit für jede Folge von
   Dualitätsdrehungen ausgeschlossen, nicht nur für die vorab gelisteten Winkel.
4. **Zur Nähe bei π/4.** Dort ist γ′ = 1,62, nicht γ_T; der Faktor 1,855 gehört zu einem anderen Endpunkt und hat mit der Zuordnung
   M/T nichts zu tun. Die einzige im Bestand vorhandene Verzerrung (Registerbreite b = 1/γ_L mit Bures-Geometrie, r29.5, r17.2) staucht
   den Winkel ohnehin (Bures-Abstand senkrechter Zustände bei b ≈ 0,54 etwa 0,39 statt π/4).

**Lesart:** Innerhalb von W1 + Holst kann keine Dualitätsdrehung, reell, komplex, verzerrt oder mehrfach, ein frame-abhängiges γ bei
gleichem G liefern. Das bräuchte einen Mechanismus, der A² + B² nicht erhält, also eine Abbildung jenseits einer Dualitätsdrehung der
Krümmung. OP1 bleibt offen.
