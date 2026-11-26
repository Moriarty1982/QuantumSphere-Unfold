# Ergebnis H159: Am Photonpunkt ist Netto null und Brutto nicht null, aber γ_L⁵ kommt nicht aus der Superposition; das HC-Problem löst sich zur Hälfte

**Stand:** 2026-11-26. Test nach Vorab-Notiz `notes/research/predictions/Vorab_Notiz_H159_Lambda_Photon_Superposition.md` (Commit 45ae26a, vor dem ersten Lauf).
**Teilweise nicht blind**, wie dort offengelegt: Der Überschlag im Kopf legte alle drei Urteile weitgehend fest. Offen waren die Suche nach γ_L⁵, die Ordnung der
Kosten in Fassung F und die Frage, ob 0,694 eine Identität mit 1 − β_sym² ist.
Skripte: `k350_test_h159.py` (Python, sympy, exakt), Ausgabe `k350_out.txt`; Gegenprobe `k350b_gegenprobe.wl` (Wolfram Language, Quaternionen als 2×2-Matrizen),
Ausgabe `k350b_out.txt`. Beide stimmen in allen gemeinsamen Punkten überein. Qiskit nicht eingesetzt (keine Schaltung, kein Messablauf; die „Superposition“ ist
die Zerlegung einer klassischen Feldlösung in zwei gegenläufige Kreisanteile). Kein HDL/MMA-Vergleich. Kein Guard berührt. OP1 bis OP5 bleiben offen.

## Gesamturteil
**H159 trägt teilweise.** Das entspricht der Vorhersage.

| Kriterium | Vorhersage | Ergebnis |
|---|---|---|
| K-a (Netto null, Anteile nicht null) | trägt teilweise | **trägt teilweise**: gilt für die Ladung und für ein tauschsymmetrisches HC-Potential; die Zuordnung zur Vakuumdichte ist gesetzt |
| K-b (Verhältnis γ_L⁵) | widerlegt | **widerlegt**: keines von 50 Verhältnissen ist K⁵; der Exponent 5 kommt nur aus der Gewichtsregel |
| K-c (HC am Photon) | trägt teilweise | **trägt teilweise**: c1 trägt teilweise (regulär, SU(2)-verträglich, aber Rückstellung erst in vierter Ordnung), c2 widerlegt |

## Welches HC-Problem am Photon dokumentiert ist
Der Bestand führt kein einzelnes Problem unter diesem Namen, sondern vier Stellen:
1. **Entartung:** Der HC ist als quasikonforme Abbildung für |μ| < 1 erklärt (`thm:hc-quasiconformal`). Am Fixpunkt des Tauschs ist μ = 1, K = ∞, die
   Ellipse eine Linie und die Ladung null (k292, k297; r69.1(a): „P ist ein entarteter Grenzfall und braucht eine eigene normierte Observable“).
2. **Keine Wirkung:** Bei P stört keine unitäre HC-Dynamik a = b (k250).
3. **Licht und HC schließen sich aus:** Mit dem HC-Potential bleibt kein Eichfeld masselos, und es verträgt sich nicht mit SU(2) (H129, H132).
4. **Zwei „Photon-Frames“:** Die alten Aussagen (Λ = 0 bei β_sym = 0) gehören zu R (r69, v4.9.0-r24), der Fixpunkt des Tauschs ist P.

## Ergebnisse
Aufbau: ψ = e^{iωt}(a + b·j), Schatten z = a·e^{iφ} + b·e^{−iφ}, μ = b/a. R: μ = 0, M: μ = β_sym² = 0,30178 (eingesetzt), P: μ = 1, T: 1/μ_M.

1. **Der Tausch und der HC als Projektion (k350 Teil 1, P1, P2).** J: z ↦ i·z̄ wirkt auf die Koeffizienten als (a, b) ↦ (i·b̄, i·ā), also μ → 1/μ wie in k297.
   Die Fixpunkte haben |a| = |b| und liegen auf der 45°-Linie (θ = π/4 wie H149). C = ½(1 + J) ist eine reell-lineare Projektion vom Rang 2 von 4, und
   **ihr Bild ist genau die Fixpunktmenge**: Jeder Zustand wird auf lineare Polarisation abgebildet. In dieser Lesart ist der Photon-Zustand nicht der Ort, an dem
   der HC versagt, sondern das, was der HC herstellt. Das Verhältnis μ = β_sym² aus `thm:hc-quasiconformal` ist dann eine Eigenschaft des M-Zustands vor der
   Projektion, nicht der Projektion.
2. **Netto und Brutto (Teil 2, P3).** Unter J gerade: Norm a² + b², |J_⊥| = 2abω, Energie der Drehung ½ω²(a² + b²), K₁ = Q², beide Halbachsen.
   **Ungerade ist allein die Ladung** Q = J_i = ω(a² − b²). Sie ist bei P null, ihre Anteile +ωa² und −ωb² sind gleich groß und nicht null. Damit ist
   Netto := J-ungerader Teil und Brutto := die zwei Anteile eine saubere Definition, wie r69.3(c) sie verlangt. Sie trifft aber eine Ladung. Jede Energiegröße
   des Ansatzes ist J-gerade und bei P nicht null.
3. **γ_L⁵ (Teil 3, P4, P5).** Zehn Größen, Zustand P oder R gegen M, bis zu drei Normierungen: 50 Verhältnisse, davon 27 endlich und positiv. Keines ist als
   Identität K⁵ oder K⁻⁵. Die Exponenten log(Verhältnis)/log γ_L liegen zwischen −1 und +1,92. Die Anteile im M-Zustand stehen im Verhältnis 1/μ² = 10,98 = γ_L^3,85
   (Ladungsanteile) und γ_L (Halbachsen). Grund: Jede Größe der Lagrangedichte hat geraden Grad in den Amplituden; (a + b)^p(a − b)^q gibt K^(p−q) mit p − q gerade.
   Der Exponent 5 = 4·(3/2) − 1 steht in der Gewichtsregel (v4.8.0-r03.1) und wird dort eingesetzt. Bei gleicher Fläche ist die Ellipse von M die um γ_L^(1/2)
   gestreckte und gestauchte Kreisbahn von R (Halbachsenquadrate γ_L^(±1)); das ist die einzige Stelle, an der der Formalismus eine Potenz von γ_L als Frame-Verhältnis liefert.
4. **Fassung F am Photonpunkt (Teil 4a, P6 bis P9).** τ = 2μ/(1 − μ²) divergiert bei μ = 1, die Bedingung selbst nicht: P/τ⁴ → η′·J_i⁴/N². Der HC am Photon
   heißt dann schlicht **J_i = 0, Netto-Ladung null**. Das ist invariant unter SU(2) links und U(1) rechts, im Vakuum von vierter Ordnung in den Eichfeldern (keine
   Massen, ρ = 1, Licht masselos), und a = b ist exakte Lösung. Die Kosten einer Abweichung b = (1 + d)a sind aber 4a⁴ω⁴·d⁴: Der Koeffizient von d² ist allgemein
   4a⁴ω⁴(1 − μ²)²/μ² und verschwindet bei μ = 1. Die Formmode ist am Photon in führender Ordnung frei. Die quadratische Variante J_i²/N (Kosten 2a²ω²·d²) ist
   Fassung S aus k299 und verschiebt ρ auf 1/(1 + ξ).
5. **Licht mit dem HC-Potential (Teil 4b, P10).** Die Determinante der Massenmatrix aus H132 ist g_L²g_R²f⁴·sin²2θ. Sie ist bei θ = 45° **am größten**, die
   Eigenwerte sind g_L²f² und g_R²f². Null ist sie bei θ = 0, also bei R. Am Photonpunkt bleibt in dieser Fassung kein Eichfeld masselos.
6. **Tauschsymmetrisches HC-Potential (Teil 4c, P11 bis P15).** V = η(B − μ₀²A)² ist unter A ↔ B nur für μ₀ = 1 symmetrisch. Gilt die Frame-Gleichberechtigung
   (Postulat des Autors, 26.11.), dann muss in dieser Fassung μ₀ = 1 stehen. Das ist zugleich der einzige feste Punkt des Flusses aus k297 Punkt 5. Dann gilt:
   - V(P) = 0, als Summe der Anteile ηA² = ηf⁴/4, ηB² = ηf⁴/4 und −2ηAB = −ηf⁴/2. **Die Summe ist null, die Anteile nicht.** Ihr Verhältnis ist 1 : 1 : −2.
   - V(M) = V(T) = ηf⁴·cos²2θ mit cos 2θ = (1 − μ²)/(1 + μ²) = 2γ_L/(γ_L² + 1), V(R) = ηf⁴. Also V(M)/V(R) = 0,69399.
   - Am Vakuum A = B eine Formmode mit 8ηf² und drei masselose Moden.
   - **Zahlennähe, keine Identität:** 0,69399 liegt 0,6 % unter 1 − β_sym² = 0,69822 (H96: Ω_M = β_sym²). Gleichheit verlangte μ = 0,29560 statt 0,30178. Keine Behauptung.
   - Mit dem Materie-Wert μ₀ = μ_M statt 1 ist V(M) = 0 und V(P)/V(R) = (1 − μ²)²/(4μ⁴) = 24,90. Das ist nicht γ_L⁵ = 22,53.

## Was das für die Folgerung „Cosmological constant revisited“ heißt
- Der Widerspruch aus r69.3(c) löst sich **nicht** dadurch, dass eine Größe im Photon-Frame Erwartungswert null und Anteile im Verhältnis γ_L⁵ hätte. Am Fixpunkt
  des Tauschs sind die Anteile gleich groß (Verhältnis 1), sonst wäre es kein Fixpunkt.
- Die zwei Aussagen lassen sich aber trennen. „Null“ ist eine Netto-Aussage am Photonpunkt P: für die Ladung immer, für die Potentialenergie, wenn das HC-Potential
  tauschsymmetrisch ist. „γ_L⁵“ ist eine Brutto-Aussage der Gewichtsregel zwischen dem Bezugsbild R und M. Es sind zwei Größen und zwei Frame-Paare. Die erste
  ist im Formalismus ausrechenbar, die zweite bleibt eine eingesetzte Regel.
- Neu gegenüber dem Bestand: Mit Postulat und Fassung k297 hat der M-Zustand eine Potentialenergie über dem Photon-Vakuum, V(M) = ηf⁴·(2γ_L/(γ_L² + 1))², und T
  hat dieselbe. Das gibt der alten Aussage „im Photon-Frame null, für den Materie-Beobachter nicht null“ eine rechenbare Form, mit dem Null bei P statt bei R.
  η und f sind frei; eine Zahl für Λ folgt daraus nicht.

## Was das für das HC-Problem heißt
- **Stelle 1 (Entartung) löst sich:** Der Photonpunkt ist das Bild von C, das Vakuum des tauschsymmetrischen Potentials und in Fassung F die reguläre Bedingung
  J_i = 0. Die Divergenz K = ∞ ist eine der Koordinate τ, nicht der Bedingung.
- **Stelle 2 (keine Wirkung) bekommt ein Gegenstück:** In Fassung F ist die Rückstellung bei P von vierter Ordnung. Das passt zu k250.
- **Stelle 3 (Licht) löst sich nicht:** Mit dem HC-Potential ist die Lage bei P am schlechtesten. Masseloses Licht gibt es nur mit SU(2) (dann ohne das Potential)
  oder in Fassung F. Beide Befunde aus H132 und k299 bleiben stehen.
- **Stelle 4:** Alles, was die alten Stellen dem „Photon-Frame“ zuschreiben (masseloses Feld, HC trivial), liegt im Formalismus bei R (θ = 0, b = 0). Was bei P
  verschwindet, sind Q, K₁, die kleine Halbachse und das symmetrische Potential.

## Gesetzt und hergeleitet
| | Stand |
|---|---|
| Photon-Frame = Fixpunkt des Tauschs J | gesetzt (Lesart des Autors für diese Hypothese; der Bestand führt die alten Stellen als R) |
| J wirkt auf den Schatten z als z ↦ i·z̄ | gesetzt (übertragen aus r63/r64; μ → 1/μ stimmt mit k297 überein) |
| Bild von C = Fixpunktmenge, Rang 2 | hergeleitet |
| Ladung J-ungerade, Energiegrößen J-gerade | hergeleitet |
| Vakuumdichte = Ladung oder = HC-Potential | gesetzt |
| Form des HC-Potentials η(B − μ₀²A)² | gesetzt (k297) |
| μ₀ = 1 | hergeleitet aus Postulat (Frame-Gleichberechtigung) und Potentialform |
| V(M)/V(R) = cos²2θ | hergeleitet, mit β_sym eingesetzt (OP1) |
| Exponent 5 | gesetzt (Gewichtsregel), im Formalismus nicht erreichbar |
| Fassung F und S | gesetzt (k299) |

## Offen
- Mit μ₀ = 1 ist der M-Zustand kein Vakuum. Was ihn bei μ = β_sym² hält, ist offen; in k297 hielt ihn das Potential selbst (μ₀ = μ_M), und das ist mit dem
  Postulat nicht verträglich. Das ist die Spannung zwischen Postulat und `thm:hc-quasiconformal`, in einer Zeile.
- Ob Λ etwas mit V(M) zu tun hat, ist nicht gezeigt. Λ bleibt Eingabe (r04, r06.3), H96 bleibt offen, OP5 bleibt offen.
- Die Zahlennähe 0,694 gegen 0,698 ist mit heutigen Daten nicht trennbar (Ω_Λ ist auf etwa 0,007 bekannt, aus dem Gedächtnis). Sie ist nachträglich
  gefunden und zählt nicht als Vorhersage.

Zurückgestellte Ideen: I4 (das T-Bild sieht −V) wäre die einzige Quelle einer J-ungeraden Energiedichte. In diesem Ansatz ist V(T) = V(M); I4 bietet hier keinen
Ausweg und bleibt unter den geltenden Lesarten gescheitert.

## Grenzen
Klassische Lösung und klassische Massenmatrix, nur ℂ → ℍ, ohne Fermionen, ohne Schleifen. Die Suche nach γ_L⁵ deckt den vorab festgelegten Suchraum ab, nicht
jede denkbare Größe. β_sym und γ_L sind eingesetzt (OP1). Messwerte aus dem Gedächtnis.

## Dateien
`k350_test_h159.py` (`k350_out.txt`), `k350b_gegenprobe.wl` (`k350b_out.txt`, Wolfram über den Cloud-Kernel, Warnungen dort festgehalten).
Aufruf: `python k350_test_h159.py > k350_out.txt`, Laufzeit etwa 15 Sekunden.
