# Ergebnis H149: θ = π/4 ist der Fixpunkt des Frame-Tauschs, δ = 2/9 legt kein Term ohne Anpassung fest

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H149_Was_legt_Theta_und_Delta_fest.md` (Commit 42f0900; a nicht blind).
Skripte `k332_theta_delta.py` (`k332_out.txt`), `k332b_gegenprobe.wl` (`k332b_out.txt`, Wolfram exakt). Status: H149a–e bestätigt.**

Anlass: Autor „mergen, pushen und weiter“ nach H148, Frage: Was legt θ = π/4 und δ = 2/9 fest? Werkzeuge: Python (sympy exakt, numpy, explizite
Oktonionen), Wolfram unabhängig; alle gemeinsamen Größen stimmen überein. Qiskit nicht eingesetzt (keine Schaltung). Kein HDL/MMA-Vergleich.
Suchrichtung rückwärts: gesucht waren stationäre Punkte zulässiger Terme, die ohne abgestimmte Koeffizienten bei θ = π/4 bzw. δ = 2/9 liegen.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H149a | ReΨ² = cos 2θ = x₀² − \|x⃗\|²; Tausch J: ψ ↦ Uψ̄ bildet θ auf π/2 − θ ab, J² = 1, einziger Fixpunkt in [0, π) ist π/4; in den Oktonionen explizit (Fehler 3·10⁻¹⁶) | exakt | **bestätigt** (nicht blind) |
| H149b | N(Ψ) = 1, ReΨ = cos θ: ∂_δV ≡ 0 für jedes V(N, Re) bis Grad 4 (14 Koeffizienten); bei V(N) auch ∂_θV ≡ 0; exp(αU) verschiebt θ um α | exakt | **bestätigt** |
| H149c | ∂_θV\|π/4 = −(2a − 2c + μ₀² − μ₁²)/2: genau eine lineare Bedingung, der tauschungerade Teil; mit Tausch (μ₁ = μ₀, c = a) stets stationär, Krümmung 2(2a − b) bei π/4 und −2(2a − b) bei 0; mit k291 (μ = 0) V = konst. + (2a − b)/8·cos 4θ | eine Bedingung | **bestätigt** |
| H149d | Tr W = √3 cos θ, Tr W² = 1, N(W) = (2cos 3δ − √2)/(24√3) bei θ = π/4; 966 Minima von V = Σα_kN^k (α ∈ −3…3, Grad 2, 3), 126 mit drei verschiedenen Massen, alle bei δ = π/12; kein Treffer bei 2/9 | 0 Treffer | **bestätigt** |
| H149e | δ_fit = 0,222222; π/12 +17,8 %, artanh(β_sym)/3 −7,4 %, γ_M +6,9 %, arctan(β_sym²) +31,9 % | 0 Treffer in 1 % | **bestätigt** |

Zusatz zu c (Lesart k297, tan θ = μ): Der HC gibt im Materie-Frame K = (1 + β_sym⁴)/3 = 0,364, im Tachyon-Frame 3,99. Den Koide-Wert ⅔ gibt nur
der Tausch-Fixpunkt μ = 1.

Nicht gewertet: CT-002 (δ = π/12 − γ_M/6) liegt 5·10⁻⁵ daneben, H1 (δ = K/3) trifft per Konstruktion. Der vor der Notiz bemerkte Zahlentreffer
−4cos(2/3) = −3,1435 ≈ −π hält nicht: δ = arccos(π/4)/3 = 0,222486 liegt 42σ neben dem δ aus den drei Massen (0,222225 ± 0,000006, Tau ± 0,09 MeV).

## Lesart
- **θ = π/4 hat einen Grund, aber kein Vorzeichen.** π/4 ist der Fixpunkt des Tauschs von HS(0)-Einheit und Kopienrichtung. Das ist nach k297 der
  Tausch Materie-Frame ↔ Tachyon-Frame (μ → 1/μ), und am Fixpunkt ist Ψ lichtartig (ReΨ² = 0, Photonpunkt aus r16/r17). Ist das Potential
  tauschsymmetrisch, liegt dort immer ein stationärer Punkt. Ob Minimum oder Maximum, entscheidet allein das Vorzeichen von 2a − b; das Gegenstück
  ist θ = 0 mit K = ⅓ (drei gleiche Massen). Damit ist die Frage auf ein einziges Vorzeichen der Feldgleichung zurückgeführt. Das wird nicht gesetzt.
- **Was die Tauschsymmetrie bricht, verschiebt θ.** Der HC bricht sie (k297) und gibt K = 0,364. Koide verlangt also, dass die Leptonmassen am
  ungebrochenen Punkt ausgelesen werden. Das ist eine Lesart, keine Herleitung.
- **Bei geeichter U(1) ist θ flach.** Dann ist θ die U(1)-Phase und durch kein V(N) festgelegt. Ein Term, der π/4 auszeichnet, bricht die U(1)
  auf eine Restgruppe (cos 4θ, also Z₄).
- **δ sieht nur die kubische Norm.** Ein einzelnes Element hat nur N und Re, beide unabhängig von δ. Erst N(W) = c₀c₁c₂ kennt die drei Kopien, und
  zwar nur über cos 3δ. Ohne Anpassung gibt es drei Arten stationärer Punkte: sin 3δ = 0 (zwei gleiche Massen) und N(W) = 0, also **δ = π/12 mit
  masselosem Elektron**. Das ist der Oktant aus H101. Die Abtastung findet bei drei verschiedenen Massen nur diesen Punkt.
- **δ = 2/9 bleibt eine Anpassung.** Es braucht entweder einen abgestimmten Koeffizienten (für V = αN + βN² etwa α/β = −0,00758 in dieser
  Normierung) oder die Verschiebung vom Oktanten um γ_M/6 (CT-002, Platzhalter). Die Frage ist dieselbe wie im historischen OP3: Woher kommt der
  Fluss 2/3 rad statt π/4 durch das Platzdreieck?

## Bilanz der Setzungen (H148 → H149)
- *H148:* gesetzt waren θ, δ, die Skala und die Amplituden-Auslesung; hergeleitet war K = ⅔ ⇔ θ = π/4.
- *H149:* hergeleitet ist, dass θ = π/4 der Tausch-Fixpunkt ist und dass ein tauschsymmetrisches Potential dort stationär ist. Die offene Wahl ist
  zum **Vorzeichen von 2a − b** gewandert (und zur Frage, ob die Auslesung am tauschsymmetrischen Punkt erfolgt). Für δ ist nichts hergeleitet: Die
  Wahl liegt weiter bei einem Koeffizienten bzw. bei CT-002.
- Die Frage, ob das Ziel selbst gesetzt ist: δ = 2/9 ist aus m_μ/m_e angepasst, also eine Eingabe. θ = π/4 ist nur über Koide ausgezeichnet. Hier
  entsteht die Frage in der gewählten Zerlegung (Amplituden-Auslesung mit g_k); in der Gram-Auslesung (H148) gäbe es sie in dieser Form nicht.

## Grenzen
- Die Amplituden-Auslesung (r13/k255) bleibt gesetzt, ebenso die Skala und der Tausch als Symmetrie des Potentials.
- Nur Polynome in N(W) bis Grad drei mit kleinen ganzen Koeffizienten wurden abgetastet; mit freien reellen Koeffizienten ist jeder δ-Wert
  erreichbar (dann ist es ein Fit).
- OP3, OP4 offen; Vorzeichen offen; kein Guard berührt.
- Vergeben: H149, k332. Nächste frei: H150, k333.
