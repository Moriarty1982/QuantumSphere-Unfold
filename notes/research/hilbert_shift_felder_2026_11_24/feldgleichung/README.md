# Allgemeine Feldgleichung für den Hilbert-Shift-Turm, rekursiv geschrieben (Erkundung k290, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Der Ansatz lässt sich rekursiv schreiben, L_{n+1}[ψ + χℓ] = L_n[ψ] + Δ_n[ψ, χ]: Jede Stufe hängt das neue Halbfeld χ an, und zwar immer
gerade in χ, sodass die Vorstufe als Lösung χ = 0 erhalten bleibt. Dazu bringt jede Stufe genau **einen** Term neuer Art mit, der auf allen Vorstufen identisch
verschwindet (Fläche, Kommutator, Assoziator, Normdefekt). Mit diesen Termen hat die Lagrangedichte je Stufe genau die Symmetrie aus k253 (0, U(1), SU(2), G₂, G₂;
Stabilisator 0, 0, 1, 8). Die offenen Vorzeichen aus k282 sind im Ansatz **freie Parameter** und werden von der Rekursion allein nicht festgelegt. Die Rekursion sagt
aber, was sie sind: das Vorzeichen des Abstands zwischen der Masse des Anhangs und der Masse der Vorstufe.

Auftrag des Autors (25.11.2026): „erstmal wieder eine allgemeine Feldgleichung jeweils hinschreiben, die wir dann Stück für Stück rekonstruieren“, wenn möglich
rekursiv, „dass jede Stufe nur noch was anhängt“; dazu seine Vermutung, die Vorzeichen folgten erst aus der finalen Feldgleichung. **Erkundung, nicht blind:** Hier wird
ein Ansatz aufgeschrieben und auf Konsistenz geprüft. Die benutzten Identitäten (Hurwitz, Alternativität, Aut(𝕆) = G₂, Skyrme-artige Terme) sind Standard, und die
Stufenergebnisse standen aus k253 fest. Keine H-Nummer, keine Runde. Vergeben: Skripte **k290, k290b** (k283 bis k289 bleiben dem parallelen Thread zu H128).

Werkzeuge: Python mit sympy (exakte Identitäten mit symbolischen Vorzeichen g₀ … g₃) und numpy (Symmetrie-Algebren bis Dimension 16). Wolfram Language als
unabhängige zweite Implementierung für alle exakten Identitäten und für die Symmetrie-Dimensionen bis n = 3 mit exaktem Rang (k290b). Beide stimmen in allen
gemeinsamen Punkten überein. Qiskit nicht eingesetzt: Es gibt keine Schaltung und keinen Messablauf. Kein HDL/MMA-Vergleich (kein RUN_TAPE, kein endlicher Auswahlablauf).

## Vorwissen geprüft
- k253 (Regel ψ̇ = uωψ, Tabelle Der/Stabilisator je Stufe, HS(4) ohne neue Symmetrie), k270–k272 (rückwärts: g = −1 erzwungen, Amplitude, Frequenz, Phase frei),
  k274 (Duffing-Term bringt nur eine Skala), k250 (a − b wählt den Drehsinn nicht).
- k275–k282 und die Bilanz der Setzungen (Albert-Algebra, ein Element hat nur Tr W² und N(W), σ und C des Verdopplungsschritts mit freien Vorzeichen).
- H10 (Assoziator, `v4_8_0_r03_r12/llm/`), r42/r43 (Projektor ½(1 + iL_u), links/rechts), I4 und H78/H79 (das T-Bild sieht −V).
- Suche nach „Lagrangedichte“, „Skyrme“, „Assoziator“ unter `notes/research`, `wiki`, `analysis`: keine Lagrangedichte für den Turm, kein rekursiver Ansatz.

## Der Ansatz

**Feld.** ψ_n(x) ∈ A_n (Cayley–Dickson, 2ⁿ reelle Komponenten), x in der Raumzeit. Verdopplung ψ_{n+1} = ψ_n + χ_n·ℓ_n mit ψ_n, χ_n ∈ A_n und ℓ_n² = g_n.
Skalarprodukt ⟨x, y⟩ = Re(x̄y), Norm N(x) = ⟨x, x⟩. Die Vorzeichen g_n bleiben frei (k272 verlangt g_n = −1).

**Bausteine**, mit X_μ = D_μψ:

| Term | Formel | verschwindet auf | Lesart |
|---|---|---|---|
| kinetisch | ½⟨D_μψ, D^μψ⟩ | nie | Ausbreitung |
| Potential | V(N(ψ), Re ψ) | nie | ein Element erzeugt nur ℂ, also gibt es nur diese zwei Invarianten |
| K₁ Fläche | N(X_μ)N(X_ν) − ⟨X_μ, X_ν⟩² | ℝ (HS(0)) | Fläche und Ladung von HS(1) |
| K₂ Kommutator | N([X_μ, X_ν]) | ℂ (HS(1)) | Skyrme-artig, erste nichtabelsche Struktur |
| K₃ Assoziator | N([X_μ, X_ν, X_ρ]) | ℍ (HS(2)) | braucht drei unabhängige Richtungen |
| K₄ Normdefekt | N(X_μX_ν) − N(X_μ)N(X_ν) | 𝕆 (HS(3)) | das Leck von HS(4) |
| Eichanteil | −(1/4e²)·tr F_μνF^μν, D_μ = ∂_μ + 𝒜_μ | – | 𝒜_μ in einer Unteralgebra der Symmetrie der Stufe |
| erste Ordnung (wahlweise) | ½⟨ψ̇, uψ⟩ − (ω/2)N(ψ) | – | gibt ψ̇ = ωuψ, die Regel aus k253 |

**Je Stufe ausgeschrieben** (alle c, μ², ρ, λ, κ, e mit freiem Vorzeichen, soweit nicht anders gesagt):

- **HS(0), ψ = φ ∈ ℝ:** L₀ = ½(∂φ)² − V₀(φ), V₀ = ½μ₀²φ² + ⅓ρ₀φ³ + ¼λ₀φ⁴. Feldgleichung □φ + V₀′(φ) = 0. Kein Eichfeld, keine K-Terme.
- **HS(1), ψ = φ + χi:** L₁ = L₀[φ] − g₀·[½(∂χ)² − ½μ₁²χ²] − (Viertordnung in φ, χ) + c₁·K₁ + Eichanteil U(1).
  Es ist K₁ = −g₀(∂_μφ∂_νχ − ∂_νφ∂_μχ)², die Fläche zum Quadrat. U(1) verlangt V = V(N) allein, also ρ₀ = 0 und μ₁ = μ₀.
- **HS(2), ψ = ψ₁ + χ₁j:** L₂ = L₁[ψ₁] + Δ₁ mit dem neuen Term c₂·K₂. Ohne K₂ ist die Symmetrie so(4) = su(2) ⊕ su(2) (links und rechts getrennt), mit K₂ nur die
  diagonale su(2) = Der(ℍ). Eichgruppe: eine SU(2), welche, ist frei.
- **HS(3), ψ = ψ₂ + χ₂ℓ:** L₃ = L₂[ψ₂] + Δ₂ mit dem neuen Term c₃·K₃. Symmetrie g₂, bei ausgezeichneter Einheit u su(3). Eichgruppe: SU(3) (oder G₂).
- **HS(4):** neuer Term c₄·K₄, aber keine neue Symmetrie. Die Regel erster Ordnung gilt für allgemeines u nicht mehr.
- **Ausblick Produktstufen:** Ψ ∈ ℂ⊗ℍ⊗𝕆 mit D_μ = ∂_μ + g′B_μY + g₂W_μᵃT_a + g₃G_μᴬΛ_A, wobei jede Gruppe auf ihrem Faktor wirkt. Die Hyperladungen Y und
  die Kopplungen sind frei. Das ist nur hingeschrieben, nicht gerechnet.

**Die Rekursion.** L_{n+1}[ψ + χℓ] = L_n[ψ] + Δ_n[ψ, χ] mit

Δ_n = −g_n·[½⟨Dχ, Dχ⟩ − ½μ²_{n+1}N(χ)] − [V_{n+1}(ψ + χℓ) − V_n(ψ)] + Σ_{k≤n} c_k·[K_k(ψ + χℓ) − K_k(ψ)] + c_{n+1}·K_{n+1} − (1/4e²_{n+1})·tr F²_neu.

Vier Eigenschaften machen daraus eine echte Rekursion, und alle vier sind geprüft:
1. N_{n+1}(ψ + χℓ) = N_n(ψ) − g_n·N_n(χ). Der freie Teil des Anhangs ist also eine Kopie der Vorstufe mit dem Faktor −g_n.
2. σ_n: χ → −χ ist ein Automorphismus von A_{n+1}. Deshalb ist Δ_n gerade in χ, enthält keinen in χ linearen Term, und χ = 0 löst die Gleichungen der Stufe n + 1.
3. Δ_n[ψ, 0] = 0: Die Einschränkung auf χ = 0 gibt jeden Term der Vorstufe genau zurück.
4. K_{n+1} verschwindet identisch auf A_n. Er ist das Einzige, was auf der neuen Stufe von neuer Art ist.

## Ergebnisse der Prüfung
1. **Rekursion der Norm und Geradheit (k290 S1, S2, k290b W1, W2):** exakt null mit symbolischen g für n = 1, 2, 3; Geradheit und Einschränkung auch für n = 4 (exakt, rational).
   Die acht Einheiten von A₃ haben die Normen 1, −g₀, −g₁, g₀g₁, −g₂, g₀g₂, g₁g₂, −g₀g₁g₂.
2. **Die Regel aus k253 ist die Gleichung erster Ordnung (S3, W3, W6):** ⟨ux, y⟩ + ⟨x, uy⟩ = 0 und u(ux) = −N(u)x gelten exakt für n ≤ 3. Die Euler–Lagrange-Gleichung von
   ½⟨ψ̇, uψ⟩ − (ω/2)N(ψ) ist ψ̇ = ωuψ, also ψ̈ = u²ω²ψ = gω²ψ. Bei n = 4 ist der Rest für allgemeines u nicht null (rationales Beispiel 3595/8019, numerisch bis 0,94).
3. **Zusatzterme (S4, W4):** K₁ = 0 auf ℝ, K₂ = 0 auf ℂ, Assoziator = 0 auf ℍ, K₄ = 0 auf 𝕆, jeweils als symbolischer Nullrest. Auf der nächsten Stufe sind sie nicht null:
   K₁ = −g₀·(Fläche)², K₂(e₁, e₂) = 4g₀g₁, K₃(e₁, e₂, e₄) = −4g₀g₁g₂, K₄ = −4 am Nullteiler (e₁ + e₁₀)(e₄ − e₁₅) = 0. Die Vorzeichen der Terme tragen also Produkte der g.
4. **Symmetrie der Lagrangedichte je Stufe (k290 Teil N, k290b W5):** Dimension der Unteralgebra von so(2ⁿ), die die Terme erhält.

   | Terme | n = 0 | 1 | 2 | 3 | 4 |
   |---|---|---|---|---|---|
   | kinetisch, V(N), K₁ | 0 | 1 | 6 | 28 | 120 |
   | dazu K₂ | 0 | 1 | 3 | 21 | 15 |
   | dazu K₃ | 0 | 1 | 3 | 14 | 14 |
   | dazu K₄ | 0 | 1 | 3 | 14 | 14 |
   | dazu Abhängigkeit von Re ψ | 0 | 0 | 3 | 14 | 14 |
   | dazu feste Einheit u = ℓ | 0 | 0 | 1 | 8 | 14 |
   | dazu feste Einheit u = e₁ | – | 0 | 1 | 8 | 8 |

   Das ist die Tabelle aus k253 (Der 0, 0, 3, 14, 14; Stabilisator 0, 0, 1, 8, 8), jetzt als Symmetrie einer Lagrangedichte. Die freie Theorie sieht die Algebra nicht
   (ganz so(2ⁿ)). Erst der Term der jeweiligen Stufe senkt die Symmetrie auf die Automorphismen. Bei n = 4 sind die Einheiten nicht mehr gleichwertig (14 gegen 8). n = 4 ist nur
   numerisch gerechnet.
5. **Stromvariante (Teil N):** Baut man K₂ und K₃ aus den Strömen J_μ = ψ̄D_μψ statt aus D_μψ, bleibt bei n = 2 die volle so(4) erhalten (links und rechts getrennt) und bei
   n = 3 mit dem Assoziator g₂. Welche Variante gilt, ist eine freie Wahl des Ansatzes. Für die Chiralität (r43) ist sie wichtig.
6. **HS(0) und HS(1) (S6):** Die Ellipse a·e^{iωt} + b·e^{−iωt} löst die Gleichung zweiter Ordnung. Die Noether-Ladung ist Q = ω(a² − b²), bei a = b null, und K₁(ψ, ψ̇) = Q².
   Die Zeitumkehr vertauscht a und b. Für b = 0 ist ψ̇ψ⁻¹/ω = i. Das sind die Befunde aus k253.
7. **Vorzeichen g (Teil N, S5):** Jedes Muster mit einem g = +1 hat vier Richtungen mit negativer Norm, also einen Anhang mit negativer Bewegungsenergie. Nur g = (−1, −1, −1)
   ist positiv definit. Das ist der Befund aus k272 in der Sprache der Lagrangedichte.
8. **Familienteil (S7, W7):** H₃(A_n) hat die Dimensionen 6, 9, 15, 27. Der Anhang je Stufe sind drei Einträge b_kℓ mit 3, 6, 12 Komponenten. Für ℝ → ℂ gilt
   Tr(W∘σW) = Tr W² − 4|v|² (k282).

## Was das für die offenen Vorzeichen heißt
- **Zwei Vorzeichen stecken in dem einen g des Bestands.** In der Gleichung erster Ordnung ist ψ̈ = u²ω²ψ, das Vorzeichen der Algebra (ℓ² = g) und das der Bewegung sind
  dasselbe. In der Gleichung zweiter Ordnung trennen sie sich: g_n bestimmt die Signatur der Norm und damit das Vorzeichen der Energie des Anhangs, das Vorzeichen von μ²
  bestimmt, ob ψ = 0 schwingt oder wächst. Wachstum bei kleiner Amplitude mit g = −1 ist dann möglich (μ² < 0 mit λ > 0, ein Potential mit Mulde), ohne Nullteiler. k272
  schließt g_n = +1 aus, über das Vorzeichen von μ² sagt es in dieser Form nichts. An dieser Stelle tritt auch die Frame-Frage ein (das T-Bild sieht −V, H78/H79, I4). Das ist
  hier nicht ausgewertet.
- **Die Wahl von u.** Mit dem Term erster Ordnung ist u ein fester äußerer Parameter, und die Symmetrie ist von Hand gebrochen. Ohne ihn ist u = ψ̇ψ⁻¹/ω eine Eigenschaft
  der Lösung und die Ladung Q eine Erhaltungsgröße. Der Drehsinn ist dann ein Anfangswert und kein Parameter der Gleichung. Das passt zu k250 und k253: Die Gleichung sagt,
  welche Wahl ansteht, und nicht, wie sie fällt.
- **Die Vorzeichen aus k282.** Der σ-Term ist in der Rekursion der Unterschied zwischen μ² der Vorstufe und μ² des Anhangs: Tr(W∘σW) zählt den Anhang v mit umgekehrtem
  Vorzeichen. Das freie Vorzeichen d_v aus k282 sagt also, ob der Anhang schwerer oder leichter ist als die Vorstufe. Die Rekursion lässt beides zu. Der C-Term (Diagonale
  gegen Nebendiagonale) ist nicht von dieser Form, er gehört zur Matrixstruktur von H₃.
- **Was die Vorzeichen festlegen könnte**, ohne dass es hier gerechnet ist: (a) Eichinvarianz. Wird eine Gruppe geeicht, die Vorstufe und Anhang mischt, dann müssen die
  Massen gleich sein, und der σ-Term verschwindet. Bei HS(1) ist das U(1) mit μ₁ = μ₀. (b) Die Forderung, dass die Lagrangedichte nur die Algebra der höchsten Stufe kennt.
  Auch dann verschwindet er (k281). (c) Schleifenkorrekturen aus den Eichfeldern. Ein von null verschiedenes Vorzeichen kann also nur aus einem Term kommen, der sich an den
  Verdopplungsschritt erinnert. Die Vermutung des Autors ist damit weder bestätigt noch widerlegt, aber genauer gefasst.

## Freie Parameter des Ansatzes (nicht gesetzt)
| Parameter | Bedeutung | Stand |
|---|---|---|
| g_n ∈ {−1, 0, +1} | Vorzeichen der Verdopplung | k272: −1 |
| Vorzeichen und Größe von μ²_n | Schwingung oder Wachstum bei ψ = 0; μ²_{n+1} − μ²_n ist der σ-Term | frei |
| ρ_n (Abhängigkeit von Re ψ) | bricht U(1) bei HS(1) | frei, null bei geeichter U(1) |
| λ_n, κ_n | Viertordnung, Kopplung von Vorstufe und Anhang | frei |
| c₁ … c₄ | Gewicht und Vorzeichen der vier Zusatzterme | frei |
| Bauart der Zusatzterme | aus D_μψ oder aus den Strömen ψ̄D_μψ | frei |
| Eichgruppe je Stufe und e_n | welche Unteralgebra geeicht wird | frei |
| Term erster Ordnung, u, ω | fester Drehsinn oder Anfangswert | frei |
| d_d, c (Familienteil) | C-Term und Ladungsmischung aus k282 | frei |

## Grenzen
- Ein Ansatz ist keine Herleitung. Geprüft ist nur, dass die rekursive Form in sich stimmt und die Stufenergebnisse aus k253, k272 und k282 wiedergibt.
- Für eine rein zeitabhängige Lösung verschwinden K₁ bis K₃ (sie brauchen zwei oder drei unabhängige Ableitungsrichtungen). Die Oszillator-Regel des Bestands sieht die Stufen
  deshalb gleich, und die Unterschiede erscheinen erst mit Ortsabhängigkeit. Lösungen mit Ortsabhängigkeit sind nicht gerechnet.
- Die Zusatzterme sind die einfachsten ihrer Art, nicht die einzigen. Stabilität, Energiepositivität und Renormierbarkeit sind nicht geprüft.
- Der Eichanteil ist nur als Form angegeben. Eichkovarianz folgt für Automorphismen aus der Symmetrie der Terme. Hyperladung, Kopplungen und die Produktstufen sind nicht hergeleitet.
- Der Familienteil ist nur für den quadratischen Term angeschlossen. Die kubische Norm N(W) auf höheren Stufen ist nicht rekursiv ausgeschrieben.
- OP1, OP3, OP4, OP5 bleiben offen, kein Guard ist berührt.

## Mögliche nächste Schritte (Rekonstruktion Stück für Stück)
- **HS(1) zuerst:** L₁ mit c₁ und geeichter U(1) ausschreiben und prüfen, ob μ₁ = μ₀ und ρ₀ = 0 mit dem Übergang HS(0) → HS(1) verträglich sind (ungerader Stoß, k253 Punkt 2).
- **Vorzeichen als Test:** Legt eine der drei Bedingungen (a) bis (c) d_v fest? Für (c) wäre die Einschleifenkorrektur aus dem Eichfeld auszurechnen. Hier könnte ein blinder Test
  liegen, weil die Tabelle aus k282 vorab feststeht.
- **Bauart entscheiden:** D_μψ oder Ströme. Die Stromvariante hält bei HS(2) links und rechts getrennt und ist damit die, die zu r43 passt.

## Nachtrag (25.11.2026, k291)
Auf Hinweis des Autors, dass es auf HS(0) und HS(1) keine Masse im strengeren Sinn gibt: `Masse_zuerst_k291.md`. Dort werden μ₀ = μ₁ = 0 gesetzt, ω als
Wellenfrequenz gelesen und zwei Lesarten (Urknall bei HS(2) oder Protomasse bei HS(1)) geführt.

Zur Frage, welche der beiden Lesarten gilt: `HC_feste_Norm_k292.md` (k292, eher A; die Skala wird von HS(1) geerbt).

Ob der gegenläufige Anteil bei HS(2) in den Anhang wandern muss: `Anhang_Energie_k293.md` (k293, die Zusatzterme sprechen dagegen).

Wettbewerb mit einem Amplituden-Potential: `Schwelle_feste_Norm_k294.md` (k294, scharfe Schwelle in der Wellenzahl).

Wo das Amplituden-Potential eintritt: `Potential_im_Anhang_k295.md` (k295, die erste Skala μ² steht im Anhang von HS(2), ihr Vorzeichen bleibt frei).

Ob Schleifen die Skala selbst erzeugen (Test H129): `Ergebnis_H129_Schleifen_Skala.md` (k296, Skala teilweise, Richtung nicht festgelegt).

Ob der HC die Tauschsymmetrie bricht: `HC_Tauschsymmetrie_k297.md` (k297, ja: Tausch = Orientierungsumkehr μ → 1/μ; HC-Bedingung als Potential ist die flache Richtung).

Eichfelder auf der HC-Richtung (Test H132): `Ergebnis_H132_Eichfelder_HC.md` (k298, widerlegt: kein masseloses Eichfeld; für g_L = g_R ist m₋/m₊ = β_sym²).

Eine SU(2)-verträgliche Fassung des HC: `HC_SU2_vertraeglich_k299.md` (k299, Bedingung an den Strom J = ψ̄Dψ; Fassung F hält Licht masselos und ρ = 1, Fassung S verschiebt ρ und fällt gegen die Messung durch).

Die Schleifen-Skala von 9,8 GeV, die Ähnlichkeit mit g und Fassung F am Knoten: `Skala_9_8_GeV_und_Igel_k300.md` (k300, k301).
Die Kopplung des HS(3)-Anhangs (Test H133): `Ergebnis_H133_Anhang_HS3_Kopplung.md` (k302).
Die Rückwärtssuche nach einer Regel für κ ≈ 1,2: `Rueckwaertssuche_kappa_k303.md` (k303).

## Dateien
`k290_rekursive_feldgleichung.py` (`k290_out.txt`), `k290b_gegenprobe.wl` (`k290b_out.txt`, Wolfram über den Cloud-Kernel, Ausgaben und Warnungen dort festgehalten).
Aufruf: `python k290_rekursive_feldgleichung.py > k290_out.txt`, Laufzeit etwa 20 Sekunden.
