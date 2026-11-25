# Wo tritt das Amplituden-Potential ein? Die erste Skala steht im Anhang von HS(2) (Erkundung k295, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Das Potential λ(N − f²)² aus k294 kann in der vollen Norm nicht erst bei HS(2) eintreten, denn auf der Vorstufe wäre es nicht null und
enthielte dort einen Massenterm. Verlangt man die Rekursion (Δ = 0 ohne Anhang) und „keine Masse auf HS(1)“ zusammen, bleiben bis zur vierten Ordnung genau drei
Terme übrig: B, A·B und B² mit A = N(ψ₁) und B = N(χ). Die einzige Größe mit Massendimension ist dann der Koeffizient μ² von B. Die Skala f tritt also zum ersten Mal
im Anhang von HS(2) auf, und ihr Vorzeichen (μ² < 0 oder > 0) entscheidet, ob der Anhang eine feste Amplitude bekommt. Dieses Vorzeichen legt die Rekursion nicht fest.

Auftrag des Autors (25.11.2026): „merge und pushen dann weiter“, in der Linie Feldgleichung und Vorzeichen, mit der Frage, ob das Amplituden-Potential erst bei HS(2)
eintritt. **Erkundung, nicht blind:** Alle Schritte sind Polynomrechnung, das Ergebnis stand beim Aufschreiben der Bedingungen fest. Keine H-Nummer (H129 bleibt frei).
Vergeben: Skripte **k295, k295b**. Nachtrag zu k290 bis k294, das dort Geschriebene bleibt stehen.

Werkzeuge: Python mit sympy (exakt). Wolfram Language unabhängig, mit anderem Weg: Zählung der zulässigen Terme über die Erzeuger der Drehungen und den Rang
der Bedingungsmatrix, Massen über die Hesse-Matrix in vier reellen Komponenten (k295b). Qiskit nicht eingesetzt (keine Schaltung). Kein HDL/MMA-Vergleich.

## Vorwissen geprüft
k290 (Rekursion L_{n+1} = L_n + Δ_n, Δ gerade in χ und null bei χ = 0), k291 (μ₀ = μ₁ = 0, Lesarten A und B), k292 (HC legt die Form fest, nicht die Amplitude),
k293 (Zusatzterme bevorzugen den Anhang nicht), k294 (Schwelle mit λ(N − f²)²), k272 (Amplituden frei), k282 und die Bilanz der Rückwärtssuche (σ-Term als
Massenunterschied zwischen Anhang und Vorstufe, Vorzeichen offen).

## Rechnung
Schreibweise: ψ = ψ₁ + χ·j mit ψ₁, χ in ℂ, A = N(ψ₁), B = N(χ), N(ψ) = A + B.

1. **Volle Norm geht nicht (k295 Abschnitt 1, k295b V1):** λ(N − f²)² wird bei χ = 0 zu λ(A − f²)². Das ist nicht null und enthält den Massenterm −2λf²·A der
   Vorstufe. Entweder steht das Potential schon in L₁ (dann hat HS(1) eine Masse, gegen die Vorgabe), oder es verletzt Δ[ψ,0] = 0.
2. **Zulässige Terme (Abschnitt 2, V2):** Unter den 17 Monomen vom Grad 2 und 4, die gerade in χ sind und bei χ = 0 verschwinden, sind genau drei invariant unter der
   Links- und der Rechtsdrehung um i: **B, A·B, B²**. Verlangt man nur die Linksdrehung (die Regel ψ̇ = ωiψ), kommen zwei weitere dazu: Real- und Imaginärteil von
   (ψ₁χ̄)². Der Term A² gehört nicht zum Anhang. Er steht in L₁, trägt keine Skala und gibt keine Masse.
3. **Potential:** V = λ_A·A² + κ·A·B + λ_B·B² + μ²·B. Einzige Größe mit Massendimension: μ².
4. **Vakuum (Abschnitt 3, V3):**
   - μ² > 0: χ = 0 ist stabil, der Anhang ist ein gewöhnliches massives Feld, es entsteht keine feste Amplitude.
   - μ² < 0, κ ≥ 0: Minimum bei A = 0, B = −μ²/(2λ_B). Die feste Norm f² = −μ²/(2λ_B) liegt ganz im Anhang.
   - μ² < 0, κ < 0, κ² < 4λ_Aλ_B: Minimum im Inneren, A = −κμ²/(κ² − 4λ_Aλ_B), B = 2λ_Aμ²/(κ² − 4λ_Aλ_B), Verhältnis A/B = −κ/(2λ_A).
     Das ist der Fall a² und b² beide ungleich null aus k292, jetzt mit festgelegten Werten.
5. **Massen (Abschnitt 4, V4):** Im Fall A = 0 hat die Radialmode des Anhangs m² = −4μ² und die Vorstufe ψ₁ m² = −κμ²/λ_B. **Für κ = 0 bleibt ψ₁ masselos**,
   obwohl der Anhang eine feste Amplitude hat. Im inneren Minimum sind beide Phasen masselos, die zwei Radialmoden haben Determinante 32κλ_Aμ⁴/(κ² − 4λ_Aλ_B)
   (positiv unter den Bedingungen aus Punkt 4; Beispiel λ_A = λ_B = 1, κ = μ² = −1: A = 1/3, B = 2/3, Eigenwerte 4(3 ± √3)/3).
6. **Die Lösung im Anhang ist exakt (Abschnitt 5, V5):** ψ₁ = a·e^{ip₁}, χ = b·e^{−ip₂} mit lichtartigen Phasen löst die volle Gleichung genau dann, wenn
   dV/dA = dV/dB = 0. Die Amplituden a und b, die in k272 frei waren, sind dann durch das Potential bestimmt.
7. **Wann der Anhang wächst (Abschnitt 6, V6):** Kleines χ auf einem Hintergrund A hat ω² = q² + 2(μ² + κA). Für μ² + κA < 0 wachsen die langen Wellen mit
   q² < −2(μ² + κA). Das passt zur Schwelle aus k294 (lange Wellen feste Norm). Das Potential aus k294 ist der Sonderfall λ_A = λ_B = λ, κ = 2λ, μ² = −2λf²
   zusammen mit dem hier ausgeschlossenen Massenterm der Vorstufe.

## Einordnung
- **Zu A oder B (k291, k292):** Mit der Vorgabe des Autors (keine Masse auf HS(0) und HS(1)) und der Rekursion ist die Skala f eine Größe des Anhangs von HS(2).
  Das ist Lesart A, jetzt nicht mehr nur über den HC begründet, sondern über die Bauart des Ansatzes. Die „Protomasse“ von HS(1) bleibt die skalenfreie
  aus k291 (E² − P² gekreuzter Wellen) und die Form der Ellipse.
- **Licht bleibt masselos:** Für κ = 0 koppelt die Vorstufe nicht an die feste Amplitude des Anhangs und bleibt masselos. Das ist der einfachste Weg, auf dem
  im Ansatz Masse entsteht und das Feld von HS(1) trotzdem lichtartig bleibt. κ = 0 ist eine Wahl, keine Folge.
- **Zum Vorzeichen (Vermutung des Autors):** Das Vorzeichen, das k282 als σ-Term offen ließ (Anhang leichter oder schwerer als die Vorstufe), ist in dieser
  Schreibweise das Vorzeichen von μ². μ² < 0 heißt: der Anhang ist ohne Kondensat instabil und bekommt die feste Amplitude. Die Rekursion lässt beide Vorzeichen
  zu. Festlegen müsste es etwas, das μ² erzeugt statt setzt, etwa eine Schleifenkorrektur aus den Zusatztermen. Das ist nicht gerechnet. Die Zuordnung zu k282 ist
  eine Lesart.

## Grenzen
- Nur das Potential bis zur vierten Ordnung, ohne Eichfelder und ohne die Zusatzterme K₁, K₂ im Vakuum. Mit geeichter U(1) wird eine der masselosen Phasen gegessen
  (k291 Punkt 5 und 6), das ist hier nicht wiederholt.
- λ_A, λ_B, κ und μ² sind freie Parameter. „Keine Masse auf HS(1)“ ist die Vorgabe, nicht hergeleitet. Klassisch gerechnet: Schleifen können einen Massenterm
  der Vorstufe erzeugen, wenn keine Symmetrie ihn verbietet.
- Nur der Schritt ℂ → ℍ. Für ℍ → 𝕆 ist die Zählung der zulässigen Terme nicht gemacht.
- OP1, OP3, OP4, OP5 bleiben offen, kein Guard ist berührt.

## Mögliche nächste Schritte
- **Erzeugt der Ansatz μ² selbst?** Einschleifenbeitrag der Zusatzterme und der Kopplung κ zum Koeffizienten von B, mit der Frage nach dem Vorzeichen. Das wäre
  die erste Rechnung, bei der das Ergebnis nicht vorab feststeht (Kandidat für H129).
- **Schritt ℍ → 𝕆:** dieselbe Zählung mit der Stabilisatorgruppe aus k253.

## Dateien
`k295_potential_im_anhang.py` (`k295_out.txt`), `k295b_gegenprobe.wl` (`k295b_out.txt`).
