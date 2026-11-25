# Der HC bricht die Tauschsymmetrie und gibt die Form vor, die Schleife gibt die Größe (Erkundung k297, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Der Tausch Vorstufe ↔ Anhang aus H129 wirkt auf den Beltrami-Koeffizienten des HC als μ → 1/μ, also als die Orientierungsumkehr,
die r23 als Tachyon-Frame führt. Der HC mit μ = β_sym² < 1 ist darunter nicht invariant und zeichnet die Vorstufe als den größeren Teil aus. Schreibt man seine
Bedingung als Potential, V = η(B − μ²A)², dann ist das genau ein zulässiges skalenfreies Potential aus k295, es hat κ < 0 und liegt genau auf der flachen
Richtung der Klasse (iv) aus H129. Damit passt alles zusammen: Der HC legt die Form fest und lässt die Größe frei (k292), die Schleife legt die Größe fest (H129),
und zwar in der einzigen Klasse, in der immer eine Skala entsteht.

Auftrag des Autors (25.11.2026, 11:01 UTC): „ja bitte“ auf die Frage, ob der HC als Brecher der Tauschsymmetrie geprüft werden soll. **Erkundung, nicht blind:**
Dass μ → 1/μ gilt und dass η(B − μ²A)² die Form aus k295 hat, stand beim Aufschreiben fest. Ein blinder Test war nicht ehrlich formulierbar. Keine H-Nummer.
Vergeben: Skripte **k297, k297b**.

Werkzeuge: Python mit sympy (exakt). Wolfram Language unabhängig (k297b), alle Größen stimmen überein. Qiskit nicht eingesetzt (keine Schaltung).
Kein HDL/MMA-Vergleich: benutzt wird nur die quasikonforme Lesart des HC, kein RUN_TAPE-Ablauf.

## Vorwissen geprüft
`thm:hc-quasiconformal` (HC als quasikonforme Projektion, μ = β_sym² = (γ_L − 1)/(γ_L + 1), K = γ_L; Statusvermerk r23: im Tachyon-Frame |μ| > 1 und
Orientierungsumkehr), k292 (μ = b/a, K = (a + b)/(a − b); HC legt die Form fest, nicht die Amplitude; Schatten ψ₁ + χ̄), k295 (zulässige Terme B, A·B, B²; A² in L₁),
H129/k296 (β-Funktionen, Klassen (i) bis (iv), Tauschsymmetrie), k272 (Amplitude frei). β_sym und γ_L sind eingesetzt (OP1 offen).

## Ergebnisse
1. **Tausch = Orientierungsumkehr (k297 Abschnitt 1):** Für ψ = e^{iωt}(a + b·j) ist der Schatten in ℂ die Ellipse a·e^{iωt} + b·e^{−iωt} mit μ = b/a.
   Der Tausch (Rechtsmultiplikation mit j) vertauscht a und b, also μ → 1/μ und K → −K. Invariant ist nur μ = 1, die lineare Polarisation von HS(0).
   Der Fall |μ| > 1 ist der, den r23 als Tachyon-Frame mit umgekehrter Orientierung führt. Die Tauschsymmetrie von H129 ist also keine neue Symmetrie,
   sondern die bekannte Wahl zwischen Materie-Frame und Tachyon-Frame.
2. **Die HC-Bedingung als Potential (Abschnitt 2, W1, W3):** B = μ²A als Bedingung, quadratisch bestraft: V = η(B − μ²A)² = ημ⁴·A² − 2ημ²·A·B + η·B².
   Das sind genau die Terme, die k295 zulässt (A² in L₁, A·B und B² im Anhang), ohne Term in B allein, also ohne Skala und ohne Masse der Vorstufe.
   Es ist κ = −2ημ² < 0 und κ + 2√(λ_Aλ_B) = 0: genau die Stabilitätsgrenze, die flache Richtung der Klasse (iv).
3. **Form fest, Größe frei (Abschnitt 3, W2):** Auf der Richtung B = μ²A ist V = 0 und der Gradient null, für jede Größe f. Massenquadrate: dreimal 0
   (zwei Phasen, die Größenmode) und einmal m_H² = 8ημ²f² (die Formmode, die das Achsenverhältnis zurückstellt). ψ = e^{i(ωt − kx)}(a + μa·j) löst die Feldgleichung
   als masselose Welle mit freiem a. Das ist die Aussage von k292 und k272, jetzt als Eigenschaft eines Potentials.
4. **Die Schleife legt die Größe fest (Abschnitt 4, W4):** Mit V₁ = m_H⁴/(64π²)·(ln(m_H²/M²) − 3/2) liegt das Minimum bei f² = e·M²/(8ημ²), mit V₁ < 0.
   Die Größenmode bekommt die Masse m_s² = (ημ²/π²)·m_H². Mit μ = β_sym²: m_s²/m_H² = 0,00923·η. Die Größenmode ist also viel leichter als die Formmode.
5. **Das Verhältnis ist nicht fest unter dem Fluss (Abschnitt 5, W5):** Auf der flachen Fläche gilt für ρ = λ_B/λ_A = μ⁻⁴: 16π²·dρ/dt = 64λ_A·ρ(ρ − 1).
   Fest ist nur ρ = 1, also μ = 1. Für μ < 1 läuft μ ins Infrarote langsam auf 1 zu und ins Ultraviolette auf 0. Die Schleifen erzeugen den Wert β_sym² nicht.
   Er gilt an der Skala, an der die flache Richtung erreicht wird, und bleibt Eingabe.
6. **Zahlen (Abschnitt 6, W6; β_sym eingesetzt):** μ = 0,3018, B/A = 0,0911, der Anhang trägt 8,35 % der Norm, λ_B/λ_A = 120,6, m_H² = 0,7285·η·f²,
   Winkel auf der Hopf-Sphäre 33,58° vom Pol (wie k292).

## Einordnung
- **Zur Frage aus H129:** Ja, der HC bricht die Tauschsymmetrie, und er wählt eine Richtung: Die Vorstufe ist der größere Teil (91,65 % der Norm),
  der Anhang der kleinere. Das ist aber die Wahl μ < 1 statt μ > 1, also Materie-Frame statt Tachyon-Frame. Hergeleitet wird diese Wahl hier nicht, sie wird
  aus dem Bestand übernommen.
- **Zur Vermutung des Autors (Vorzeichen aus der Feldgleichung):** Mit dem HC als Bedingung sind zwei Vorzeichen keine freien Parameter mehr:
  κ < 0 (beide Anteile ungleich null) und, über H129, das Vorzeichen der erzeugten Skala (feste Amplitude). Frei bleiben η, die Zahl β_sym (OP1) und die
  Wahl des Frames.
- **Zu „HC kommt ab HS(1), wirkt aber erst nach dem nächsten Schritt“ (Autor, 25.11.):** In dieser Lesart genau so. Bei HS(1) ist μ nur die Form der Ellipse,
  ohne Energie. Erst mit dem Anhang gibt es die Größe B, und die Bedingung B = μ²A wird zu einem Potential, dessen Schleife die Skala erzeugt.
- **Preis:** Die Vorstufe bleibt nicht unberührt. Der gemeinsame Phasenanteil ist masselos, aber Vorstufe und Anhang sind über κ gekoppelt. Was davon „Licht“ ist,
  entscheidet erst die Eichung (k291 Punkt 6), die hier fehlt.

## Grenzen
- **Die quadratische Strafe ist eine Setzung.** Der Bestand führt den HC als lineare Projektion; dass seine Bedingung im Feld als η(B − μ²A)² steht, ist die
  einfachste Übersetzung, nicht die einzige. Jede Funktion mit derselben Nullstelle gäbe dieselbe flache Richtung, aber andere Massen.
- Die Zuordnung Schatten = ψ₁ + χ̄ stammt aus k292 und ist eine Lesart. Dass der gegenläufige Anteil im Anhang sitzt, ist nicht erzwungen (k293).
- Eine Schleife, ohne Eichfelder, nur ℂ → ℍ. Die Formel für V₁ setzt voraus, dass nur die Formmode beiträgt (die anderen drei sind auf der flachen Richtung masselos).
- β_sym und γ_L sind eingesetzt. OP1, OP3, OP4, OP5 bleiben offen, kein Guard ist berührt.

## Mögliche nächste Schritte
- **Eichung dazunehmen:** Links-U(1) oder SU(2) links und U(1) rechts wie in k291 Punkt 6, auf der HC-Richtung. Welche Eichfelder werden massiv, und bleibt eines
  masselos? Die Massenverhältnisse hingen dann an μ = β_sym², das wäre eine Zahl, die vor der Rechnung nicht feststeht.
- **Schritt ℍ → 𝕆:** dieselbe Konstruktion mit dem nächsten Anhang.

## Dateien
`k297_hc_tauschsymmetrie.py` (`k297_out.txt`), `k297b_gegenprobe.wl` (`k297b_out.txt`).
