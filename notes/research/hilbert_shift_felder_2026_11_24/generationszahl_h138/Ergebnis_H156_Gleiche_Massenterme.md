# Ergebnis H156: Die Algebra verlangt μ_A² = μ_B² nicht; gleiche Massen folgen erst, wenn der Tausch J als Symmetrie gefordert wird

**26.11.2026. Vorab-Notiz `Vorab_Notiz_H156_Gleiche_Massenterme.md` (Commit fdac350; a, d nicht blind). Skripte `k339_gleiche_massen.py` (`k339_out.txt`),
`k339b_gegenprobe.wl` (`k339b_out.txt`, Wolfram). Status: H156a, b, d bestätigt; H156c teilweise (Massenrichtung nur für κ < 0 anziehend).**

Anlass: nach H155 die Frage, ob die Algebra die verbliebene Setzung μ_A² = μ_B² verlangt. Werkzeuge: Python (sympy: Invariantentheorie, linearisierter Fluss; numpy:
explizite Oktonionen), Wolfram unabhängig (dieselben Invarianten, dieselben Matrizen, J). Alle Ausgaben stimmen überein. Qiskit nicht eingesetzt.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H156a | μ_A A + μ_B B = ½(μ_A + μ_B)N + ½(μ_A − μ_B)ReΨ²; Konjugation und ein G₂-Element (zyklischer Shift der Oktonion-Einheiten, Fehler 2·10⁻¹⁵) lassen N und ReΨ² invariant | symbolisch | **bestätigt** (nicht blind): ungleiche Massen sind erlaubt |
| H156b | Z₄ = ⟨L_U⟩: quadratisch nur N, quartisch zusätzlich φy(y² − φ²), das θ von π/4 schiebt; Z₂ = ⟨J⟩ und D₄ = ⟨L_U, Konjugation⟩: gleiche Massen, gleiche λ, κ frei, kein schiebender Term; SO(2): nur N, N² (κ = 2λ) | „geeignet“ wie vorab definiert | **bestätigt**: geeignet sind genau ⟨J⟩ und D₄ |
| H156c | n_B = 1: Tauschlinie invariant; Raten für (s, r) = (δμ²/μ², δλ/λ): 8κ und 2κ²/λ − 72λ (in 1/16π² je e-Folge); n_B = 2: Quelle (8λ − 4κ, 8λ − 2κ²/λ) ≠ 0 | anziehend? | **teilweise**: Quartikrichtung anziehend für \|κ\| < 6λ, Massenrichtung nur für κ < 0; mit n_B = 2 kein Attraktor |
| H156d | J(1)J(1) = −1 ≠ J(1) = U; \|J(z)\| = \|z\|; J(zw) = J(z)·w̄ | symbolisch | **bestätigt** (nicht blind): J ist Isometrie, kein (Anti-)Automorphismus |

## Lesart
- **Die Algebra lässt zwei Massenterme zu.** Die Norm N und die lichtartige Form ReΨ² sind beide unter allen Automorphismen invariant. Gleiche Massen heißt: kein ReΨ²-Term.
  Dafür braucht es eine Symmetrie, die ReΨ² das Vorzeichen umdreht.
- **Die passende Symmetrie ist genau der Tausch J.** Die stetige Drehung exp(αU) ist zu stark (sie erzwingt κ = 2λ, dann gibt es kein Koide-Kondensat). Linksmultiplikation
  mit U allein (Z₄) ist zu schwach: Sie erlaubt einen tauschungeraden Quartikterm, der θ von π/4 schiebt. Erst J selbst, oder D₄ = ⟨L_U, Konjugation⟩, das J enthält,
  erzwingt genau die Form aus H155: gleiche Massen, gleiche λ, κ frei.
- **J ist keine Symmetrie der Multiplikation.** J erhält die Norm, verträgt sich mit dem Produkt aber nur bis auf Konjugation (J(zw) = J(z)w̄). Die Algebra allein liefert J
  also nicht. Es muss als Symmetrie der Feldtheorie gefordert werden. Nach k297 ist J der Wechsel Materie-Frame ↔ Tachyon-Frame. Gleiche Massenterme sind damit gleichwertig
  mit dem Postulat, dass beide Frames gleichberechtigt sind.
- **Die Dynamik hilft nur schwach.** Mit einer Ebenenrichtung (n_B = 1) zieht der Fluss die Kopplungen zur Tauschlinie hin, die Massen aber nur für κ < 0. Die Raten sind
  von der Ordnung κ/16π² je e-Folge, also langsam. Mit zwei Ebenenrichtungen erzeugt der Fluss die Abweichung selbst.

## Bilanz der Setzungen (H150 bis H156)
- Skalenfrei: K hängt am Startwert; n_B = 1 nicht erzwungen (H150–H154).
- Mit Skala: K = ⅔ folgt aus der Tauschsymmetrie J des Potentials (H155). Die Algebra liefert J nicht (H156). Gesetzt sind die Skala und J, also die Gleichberechtigung
  der Frames; δ ist ein angepasster Parameter.
- Die offene Wahl ist von „Startwert“ über „Massenterme“ zu einem einzigen Postulat gewandert: Frame-Gleichberechtigung. Das ist eine Aussage über die Physik, keine
  Rechnung. Sie wird dem Autor als Weggabelung vorgelegt.

## Grenzen
- Invarianten in der Ebene {1, U}; im vollen Raum von 𝕆 bzw. 𝕊 führt L_U aus dem Drei-Felder-Raum heraus (nur benannt).
- Eine Schleife, logarithmisches Laufen.
- OP3 offen; kein Vorzeichen gesetzt; kein Guard berührt.
- Vergeben: H156, k339. Nächste frei: H157, k340.
