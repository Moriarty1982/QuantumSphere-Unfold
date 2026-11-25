# Ergebnis H128: Der Kollaps bei HS(4) lässt G₂ × SU(3) übrig; erst die Ladungsrichtung macht daraus SO(3), mit Massenverhältnis 9/10

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H128_Kollaps_Hilbert_Shift_Familiensymmetrie.md` (Commit 2b53bbd, 09:48 UTC, vor der Rechnung; teilweise nicht blind).
Skripte `notes/research/hilbert_shift_felder_2026_11_24/kollaps_h128/k283_test_h128.py` (Ausgabe `k283_out.txt`, `k283_out_n5.txt`), `k283b_exakt.wl` (`k283b_out.txt`),
`k283c_struktur.py` (`k283c_out.txt`, nachträglich). Status: H128a widerlegt; H128b für u = e₇ bestätigt, für u = e₈ widerlegt.**

Werkzeuge: Python (numpy) für die Derivationen (Nullraum, Singulärwerte) und die Massenform; Wolfram Language exakt für die Massenform bei n = 3 und 4.
Qiskit nicht eingesetzt (keine Schaltung). Anlass: Vermutung des Autors, der Hilbert-Shift schaffe mehr Dimensionen und sei zugleich ein Kollaps der inneren Struktur,
aus dem sich die Symmetriegruppen ergeben.

## Kontrollen
| Kontrolle | Messwert | Schranke | |
|---|---|---|---|
| (i) dim Der für n = 0 … 3 | 3, 8, 21, 52 | 3, 8, 21, 52 | erfüllt |
| (ii) r₃ − 1 | −2·10⁻¹⁶; Wolfram 36/36 | < 10⁻¹¹ | erfüllt |
| (iii) Tr(L_W²), V gegen S, n = 4 | −2·10⁻¹⁶; Wolfram 10 und 10 | < 10⁻¹¹ | erfüllt |
| (iv) Mischterm, Streuung im Spin-Raum | 4·10⁻¹⁶, 2·10⁻¹⁶; Wolfram Mischterm 0 | < 10⁻¹¹ | erfüllt |
| (v) Wolfram exakt | r₃ = 1, r₄(e₇) = 108/120, r₄(e₈) = 120/120 | gleich Python | erfüllt |

Der Lauf ist gültig. Offengelegt: Der erste Lauf für n = 5 und der erste Lauf von k283c brachen wegen Speichermangels ab (volle SVD); danach rechnet `nullspace` die
schlanke SVD. Die Werte für n ≤ 4 sind vor und nach dieser Änderung gleich. Ein Wolfram-Aufruf mit Rang modulo p lief in die Zeitgrenze; die Dimension 22 ist nur
numerisch belegt (Lücke 1,5·10¹³, Probe auf allen Basispaaren 4·10⁻¹⁶).

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H128a: dim Der(H₃(𝕊)) | **22** (Lücke 1,5·10¹³); Anteil außerhalb von g₂ ⊕ so(3): 0,16 | = 17 | **widerlegt** |
| H128b, u = e₇ (Ladungsrichtung) | K(Spin 2) = 60, K(Spin 1) = 54, **r = 9/10** (Wolfram exakt) | \|r − 1\| > 10⁻⁶ | **bestätigt** |
| H128b, u = e₈ (Verdopplungseinheit) | K = 60 und 60, r = 1 (Wolfram exakt) | \|r − 1\| < 10⁻⁹ | **widerlegt** |

Dimensionen und Symmetrie im Turm (dim H₃(A_n) / dim Der): ℝ 6/3, ℂ 9/8, ℍ 15/21, 𝕆 27/52, **𝕊 51/22**, A₅ 99/22 (Erkundung).

## Warum es so ausgeht (nachträglich, k283c)
- **Was überlebt, ist g₂ ⊕ su(3).** Der Kommutant des g₂-Anteils in Der(H₃(𝕊)) ist achtdimensional, abgeschlossen, mit negativ definiter Killing-Form (alle Eigenwerte −0,300),
  also su(3). Er enthält die Familien-so(3) und wirkt auf H₃(ℂ_e₈) treu als deren volle Symmetrie (Rang 8, kein Leck). Der Grund: 𝕊 = ℂ_e₈ ⊕ ℂ_e₈ ⊗ 7 unter G₂ (k254), und die
  hermiteschen Matrizen über ℂ_e₈ sind genau der G₂-neutrale Teil von H₃(𝕊). In H₃(𝕆) war der G₂-neutrale Teil nur H₃(ℝ) mit SO(3).
- **Die Ladungsebene sieht davon nur die SO(3).** Der Stabilisator von H₃(ℂ_e₇) in Der(H₃(𝕊)) hat Dimension 11 (su(3)_c ⊕ so(3)) und wirkt auf dem Feld nur als so(3)
  (Rang 3). Dasselbe gilt für e₁₅. Für jede Einheit gilt exakt r(u) = 1 − (1 − u₈²)/10 (geprüft an u = cos t·e₇ + sin t·e₈ und sechs Zufallseinheiten, Abweichung < 10⁻⁸).
  **Die Brechung SU(3) → SO(3) ist also der Winkel zwischen der Ladungsrichtung und der Verdopplungseinheit.**
- **HS(5) wiederholt das Muster (Erkundung):** dim Der(H₃(A₅)) = 22; die SU(3) hängt jetzt an der neuen Einheit e₁₆ (r = 1), für e₇, e₈, e₃₁ ist r = 174/216 = 29/36.
  Jeder weitere Shift nimmt der bisherigen Einheit die SU(3) und gibt sie der neuen.
- **SO(3) → A₄** kommt wie vorab offengelegt nicht aus dem Turm. Mit der Ladung je Platz bleiben auch in H₃(𝕊) 12 von 24 Würfeldrehungen (A₄), für u = e₇ und u = e₈.
- K hat keinen Diagonalterm: K(diag) = K(Nebendiagonale reell). Den C-Term aus k282 erzeugt der Turm also nicht.

## Lesart
- **Die Vermutung des Autors trägt, aber anders als in H128a formuliert.** Der Schritt 𝕆 → 𝕊 verdoppelt fast die Dimension (27 → 51) und senkt die Symmetrie von F₄ (52) auf
  G₂ × SU(3) (22). Übrig bleibt genau ein Produkt aus der Symmetrie der Oktonionen und einer SU(3) auf den drei Plätzen, die mit ganz G₂ vertauscht. In H₃(𝕆) vertauschte
  die Familien-SU(3)′ nur mit der Farbe su(3)_c (k275).
- **Der Massenunterschied, den k281 verlangt und k282 von Hand setzt, entsteht für die Ladungsrichtung e₇ von selbst**, mit festem Verhältnis μ₁²/μ₂² = 9/10 in der Form K.
  In der Sprache von k282: K = 57·(|s|² + |v|²) + 3·(|s|² − |v|²), also ein σ-Term mit festem relativem Gewicht 3/57 und kein C-Term.
- **Vorzeichen (nach der Rechnung gegen die Tabelle aus k282 gelesen):** K ist eine Summe von Quadraten, in ihr ist Spin 1 der leichtere Teil. Geht K mit positivem
  Vorzeichen in das Potential ein, ist das der Fall „Spin 1 leicht“ aus k282 (Vakuum ℤ₃, keine flache Richtung). Mit negativem Vorzeichen ist es „Spin 1 schwer“
  (ℤ₂ mit flacher Richtung). **Der Turm legt das Verhältnis fest, nicht das Vorzeichen, mit dem K im Potential steht.** Das stützt die Einschätzung des Autors vom 25.11.
  (09:48 UTC), das Vorzeichen folge erst aus der Feldgleichung. Es wird hier nicht gesetzt und als offene Eingabe an die Feldgleichung übergeben.
- **Grenzen:** K ist eine gesetzte, wenn auch kanonische Form (Offenlegung in der Vorab-Notiz). Nicht gezeigt ist, dass die drei Plätze Generationen sind, dass H₃(𝕊) im
  Turm entsteht, und warum die Ladungsrichtung e₇ und nicht e₈ ist (r42 setzt e₇). H₃(𝕊) ist keine Jordan-Algebra mehr (Rest der Jordan-Identität 54). OP3 und OP4
  bleiben offen, kein Guard ist berührt.
- **Mögliche nächste Frage (nur mit neuer Vorab-Notiz):** Legt der Turm die Ladungsrichtung relativ zur Verdopplungseinheit fest (Winkel t in r = 1 − cos²t/10)?
