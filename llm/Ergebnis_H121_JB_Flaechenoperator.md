# Ergebnis H121: J_B tauscht quer zur M–T-Achse Drehungen und Boosts und macht aus γ dort −1/γ; das trifft γ_T nicht, und Konjugation ändert kein Spektrum

**23. November 2026. Vorab-Notiz `llm/Vorab_Notiz_H121_JB_Flaechenoperator.md` (Commit c35174df). Skript `llm/k241_h121_jb_area.py`, Ausgabe
`llm/k241_out.txt`. Status: H121a bestätigt (nicht blind); H121b bestätigt (nicht blind); H121c widerlegt.**

## Kontrollen
- Die Matrizen der Vektordarstellung erfüllen [L, L] = εL, [L, K] = εK, [K, K] = −εL.
- Reeller Boost mit η_sym: Γ′ bei γ_M quer zur Achse [[0,163; −0,571], [0,571; 0,163]], längs γ_M (berichtet, nicht bewertet).

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H121a | J_B = exp(iπ/2·K_x): L_x, K_x fest; L_y ↦ iK_z, L_z ↦ −iK_y, K_y ↦ −iL_z, K_z ↦ iL_y; die Bilder erfüllen dieselben Vertauschungsrelationen | exakt | bestätigt |
| H121b | (½, 0), (½, ½), (1, 0), O = J² und J_z: größte Abweichung der Spektren 8,9·10⁻¹⁶ | ≤ 10⁻¹⁰ | bestätigt |
| H121c | aus K = γL folgt K′ = Γ′L′ mit Γ′ = diag(γ, −1/γ, −1/γ); bei γ_M: −4,2099 quer, 0,2375 längs; gegen γ_T: relative Abweichung 32,05 bzw. 0,865; γ_M/|γ′| gegen γ_L: 0,970 bzw. 0,464 | ≤ 10⁻³ | widerlegt |

## Warum es scheitert
- J_B ist ein Automorphismus der Lorentz-Algebra. Als Konjugation eines Operators lässt er dessen Eigenwerte unverändert, gleich ob unitär oder
  nicht: Aus Ov = λv folgt (UOU⁻¹)(Uv) = λ(Uv). Nicht-Unitarität allein ändert also kein Flächenspektrum. In den geprüften endlichen
  Darstellungen ist der komplexe Boost sogar unitär (entgegengesetzte Drehungen der beiden Hälften); in den unitären unendlichdimensionalen
  Darstellungen der Lorentz-Gruppe ist er es nicht, dort bleiben Fragen des Definitionsbereichs offen.
- Ändern kann sich das Flächenquant nur, wenn T die Fläche mit der transformierten Simplizitätsbedingung abliest. Dann wird quer zur Achse γ zu
  −1/γ, die bekannte Dualität γ ↔ −1/γ, und entlang der Achse bleibt γ. Keines davon ist γ_T = 0,127384 oder gibt γ_L.

## Lesart
- Der letzte im Bestand benannte strukturelle Kandidat für ein frame-abhängiges Flächenquant trägt nicht: Weder ein unitärer Boost (Rovelli–Speziale)
  noch J_B (Konjugation oder transformierte Simplizität) noch eine Holst-Dualitätsdrehung (r31.3/r31.4) bildet γ_M auf γ_T ab.
- OP1 hängt damit allein an der Zuordnung der Zählregeln selbst (U2 für M, die T-Regel j = ½), nicht an einer Frame-Abbildung des Flächenoperators.
- Nachträglich, nicht vorab festgelegt: J_B macht aus γ quer zur Achse −1/γ und lässt es entlang der Achse; ein frame-abhängiges Quant entstünde so
  nur richtungsabhängig, nicht als ein Faktor.
- OP1 bleibt offen.
