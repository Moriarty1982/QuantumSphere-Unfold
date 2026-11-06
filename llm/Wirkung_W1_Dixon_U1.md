# Wirkung W1: Einstein–Cartan–Dirac auf der Dixon-Ablage mit dem U(1) aus L_{e₇}

**4. November 2026. Status: Aufstellung und erste Identitäten (Erkundung, ohne Kriterium).** Grundlage sind die fünf Autorentscheidungen in `Bestandsaufnahme_Wirkungsansaetze.md`.

## Felder (alle unabhängig variiert, W1)
- Koframe e^a_μ, Lorentz-Verbindung ω_μ^{ab} = −ω_μ^{ba} (Entscheidungen 1 und 3);
- U(1)-Potential A_μ, reell, Erzeuger Q_J = i·L_{e₇} auf der Dixon-Ablage (Entscheidung 4);
- Spinor Ψ ∈ C⊗ℍ⊗𝕆 ≅ ℂ³² nach Aufteilung D (r41): Lorentz durch Linksmultiplikation auf ℍ, also **ein** linkshändiger Weyl-Index, kein zusätzlicher Dirac-Faktor; das sind die 16 linkshändigen Weyl-Zustände einer Generation mit ν_R (r42.1(b)).
- P_C7 := C_ch = ½(1 + J), J = i·L_{e₇} (Entscheidung 5) wirkt **als Projektor in den Kopplungen**: Bild = Dubletts (u, d)_L, (ν, e)_L, Kern = Singuletts u^c, d^c, e^c, ν^c; die schwache SU(2)' = C_ch T_a wirkt nur auf dem Bild (r42.1(d)). Die U(1)-Ladung J ist +1 auf dem Bild, −1 auf dem Kern.
- **Korrektur (4.11., vor jeder weiteren Rechnung):** Die erste Fassung dieser Notiz beschränkte Ψ auf das Bild von C_ch und setzte einen zusätzlichen Lorentz-Spinor-Faktor an. Beides widerspricht r41/r42: Die Beschränkung hätte die Singuletts gestrichen, und auf dem Bild allein wäre B − L anomal (Tr q³ = −1,78, k171). Auf dem ganzen Raum gilt für J, iR_{e₇} und B − L jeweils Tr q = Tr q³ = 0 (k171).

## Wirkung (Frame M, Entscheidung 2)
S = ∫ e [ (1/2κ) R(e, ω) + ½(Ψ̄ iγ^μ D_μΨ − (D_μΨ)‾ iγ^μ Ψ) − ¼ F_μν F^μν ],
in Weyl-Form ½(Ψ† iσ̄^μ D_μΨ + c.c.) mit σ̄^a = (1, −σ_i), D_μ = ∂_μ + (1/8)ω_μab(σ^aσ̄^b − σ^bσ̄^a) + i q A_μ J; kein Λ-Term. Massenterme fehlen vorerst; nach r44 brauchen sie ein Higgs-artiges Feld.

## QAM-Buchführung (Eingaben, nicht hergeleitet)
- `\qaminput{Pclosure}{M}{conditional}`: P_C7 = C_ch (Wahl, r42/r43);
- `\qaminput{U1e7}{M}{conditional}`: Eichrichtung L_{e₇} (Wahl, r49/r51);
- `\qaminput{adjoint}{M}{conditional}`: Dirac-Adjungierte im Frame M;
- `\qamclaim{sectors}{*}{proved}`: Sektorzerlegung r48 (Lean `Sektoren.lean`).

## Erste Befunde (k170–k173, Erkundung)
1. **Symmetrische Kinetik ist reell.** Im L ≡ 0 punktweise (geprüft, exakt 0). Damit ist Im S = 0 und die K-Lesart fügt bei der symmetrischen Form nichts hinzu: K = R.
2. **Nicht symmetrisierte Kinetik.** Punktweise gilt Im(Ψ̄ iγ^μD_μΨ) = ½(e^μ_a ∂_μ j^a + ω_a{}^a{}_b j^b) mit j^a = Ψ̄γ^aΨ, also ½ e^μ_a D^{(ω)}_μ j^a (geprüft an 200 Zufallspunkten, Residuum ≤ 2e-14). Das U(1)-Potential fällt aus Im L heraus (≤ 1e-14).
3. **Folge für die K-Lesart mit unabhängiger Verbindung.** In Im S kommt ω nur linear über ½ e e^μ_a ω_μ{}^{a}{}_{b} j^b vor. Stationarität nach ω_μ^{ab} verlangt e^μ_{[a} j_{b]} = 0; Kontraktion mit e^c_μ gibt δ^c_a j_b − δ^c_b j_a = 0, also **j^a = 0**. Im Frame M ist j⁰ = Ψ†Ψ ≥ 0, damit **Ψ = 0**.
4. **Inneres gegen äußeres i.** Auf dem Bild von C_ch gilt L_{e₇} = −i, auf dem Kern +i. Sektorweise fällt die K-Frage für die innere Einheit mit der für die äußere zusammen (bis auf ein Vorzeichen, das an „Im S = 0“ nichts ändert).
5. **Weyl-Form (k172):** dieselbe Identität Im L = ½(div j + ω-Spur j) für linkshändige 2-Spinoren (Residuum 1e-14); j⁰ = |ψ|² ≥ 0, Befund 3 gilt unverändert.
6. **Torsion (k173):** Die Kopplung der symmetrischen Kinetik an die Verbindung ist total antisymmetrisch und proportional zu ε_abcd j^d (Abweichung 1e-16); der algebraische Krümmungsanteil ist R(K) = 6 k·k (lorentzinvariant geprüft). Nach Elimination der Torsion: L_eff = −(3/16) κ j·j. Kontrolle Dirac: −(3/16) κ (j₅)², der bekannte Hehl–Datta-Wert. Für Weyl ist j der **Gesamtstrom aller 16 Zustände** (geprüft mit N = 2, 3, 16 Feldern); ein einzelner Weyl-Strom ist lichtartig.

## Lesart
- Die K-Lesart ist in diesem Rahmen entweder leer (symmetrische Kinetik) oder tödlich (nicht symmetrisiert, unabhängige Verbindung: keine Spinoren in einem Frame). Sie liefert die Schließung hier also **nicht** dynamisch; die Chiralität bleibt eine Eingabe.
- Das ist kein Widerspruch zu `HC_Null_Axis_Dynamical_Closure.md`: Dort wirkt die komplexe Stationarität in der Kompensator-Gleichung, hier im Dirac-Teil.
- **Offene Lücke, nur als Frage:** j^a = 0 ließe sich ohne Ψ = 0 erfüllen, wenn Komponenten mit negativer Dichte beitragen, etwa ein Tachyon-Frame-Anteil mit umgekehrtem Vorzeichen (Konvention F). Das wäre eine Frame-Kopplung M–T und muss eigens nach Konvention F formuliert werden; hier nicht behauptet. Sie berührt Auslöser 1 von I1 nicht, wohl aber die Frage nach getrennten Sektoren.

## Feldgleichungen der reellen W1 (nach Elimination der Torsion)
Mit j^a = Σ_s ψ_s†σ̄^aψ_s (alle 16 Zustände) und j^a_J = Σ_s J_s ψ_s†σ̄^aψ_s:
1. Weyl je Zustand s: iσ̄^μ ∇̃_μψ_s − q J_s A_μ σ̄^μψ_s − (3κ/8) j_a σ̄^aψ_s = 0 (∇̃ Levi-Civita).
2. Maxwell: ∇̃_μF^{μν} = q j^ν_J; Ward ∇̃_ν j^ν_J = 0 folgt aus der Eichinvarianz und ist wegen Tr J = Tr J³ = 0 auch anomaliefrei.
3. Einstein: G̃_μν = κ (T^Weyl + T^Maxwell + T^(4f))_μν, ohne Λ.

## Lesart der Feldgleichungen
- Die Torsion koppelt an den **Gesamtstrom**, nicht an die U(1)-Ladung J: Die Vier-Fermionen-Kopplung ist universell und ladungsblind.
- **W7 (Vakuumterm):** W1 erzeugt keinen. Ohne Skalarpotential gibt es keinen Term ∝ g_μν mit konstantem Koeffizienten; der Vier-Fermionen-Anteil verhält sich bei homogener Dichte wie eine Materie mit p = ρ und ρ ∝ −κn² (bekanntes Einstein–Cartan-Verhalten, Vorzeichen konventionsabhängig), nicht wie Λ. Für OP5 braucht es also den Skalar- bzw. Kompensatorsektor.
- Auslöser von I1 (`Zurueckgestellte_Ideen.md`): keiner getroffen; keine Überbestimmung, ein Koframe genügt.

## Nächster Schritt
- Feldgleichungen 1–3 symbolisch mit sympy aus der Wirkung ableiten (bisher punktweise numerisch für den Torsionsteil, Rest aus der Standardtheorie übernommen) und die Bianchi- und Ward-Identität explizit prüfen.
- Skalar- bzw. Higgs-Sektor nach r44 dazunehmen (Massenterme antilinear, H-Quantenzahlen); erst dort kann ein Vakuumterm entstehen (W7).
- Test Tr(M₁₆ P_C7) ≡ 0 mod HC: braucht zuerst eine konkrete Definition von „mod HC“; mit 𝓜 = λ₀C_ch + λ₁(1 − C_ch) (r42.1(e)) ist Tr(𝓜 C_ch) = 16λ₀. Frage an den Autor.

## Nachtrag (5.11., H88, Wolfram)
Unabhängige Herleitung mit Wolfram (`llm/k203_w1_feldgleichungen.wl`): Erzeuger kovariant (D_μ j^c = ∂_μ j^c + ω_μ{}^c{}_b j^b); Torsion aus den Definitionen mit allen 24 Kontorsionskomponenten → L_eff = −(3/16)κ j·j (Gesamtstrom), wie k173; Weyl-Gleichung 1 per Variationsableitung exakt; Ward-Identität (M hermitesch). Nicht geprüft: Einstein-Gleichung 3 und Bianchi-Identität. Siehe `llm/Ergebnis_H88_W1_Feldgleichungen_Wolfram.md`.

## Nachtrag (6.11., H89, Wolfram)
Energie-Impuls-Tensor hergeleitet (`llm/k204_w1_einstein.wl`): Vierbein-Variation erster Ordnung mit torsionsfreiem Spinzusammenhang = −Belinfante, symmetrisch. Der Vier-Fermionen-Anteil allein gibt T^(4f) = (3κ/16) j² g_μν (Λ-Form, Höhe ∝ j², nicht konstant). Für einen homogenen Zustand (zwei entgegengesetzte Spins, Moden positiver Frequenz) ist der ganze Tensor ρ = p = (3κ/16) n² > 0. **Korrektur zur Lesart oben:** „p = ρ“ stimmt für den ganzen Tensor; „ρ ∝ −κn², Vorzeichen konventionsabhängig“ trifft nicht zu, das Vorzeichen hängt am Zustand (hier positiv); „nicht wie Λ“ gilt für den ganzen Tensor, nicht für den Vier-Fermionen-Term allein. „W1 erzeugt keinen Vakuumterm“ bleibt. Siehe `llm/Ergebnis_H89_W1_Einstein_Gleichung.md`.

## Nachtrag (6.11., H90, nichtlinear)
Einstein-Gleichung voll nichtlinear hergeleitet (`llm/k205_w1_einstein_nichtlinear.py`, Jets an allgemeinen Punkten gekrümmter Hintergründe): Cartan-Gleichung gelöst durch ω = ω̃ + K, K_cab = −(σ_g/4)κ ε_cabd j^d; Einstein–Cartan-Gleichung = G̃ + σ_g κ T^eff mit T^eff = T^Bel − g L_W + T^Maxwell − g λ j·j, λ = −σ_g·3κ/16; ∇̃^μ T^eff_μν = 0 auf den Feldgleichungen. **Vorzeichen:** Mit der Wirkung wie oben (+R/2κ, σ_g = +1, Krümmung R^ab = dω^ab + ω^a_c∧ω^cb) gilt G̃ = −κT^eff, die Gravitation stößt ab. Physikalisch richtig ist −(1/2κ)R in dieser Signatur; dann L_4f = +(3/16)κ j·j, T^(4f) = −(3κ/16) j² g, homogener Zustand ρ = p = −(3κ/16)n² < 0 (die ursprüngliche Lesart „ρ ∝ −κn²“ stimmt dann). Autorentscheidung offen. Siehe `llm/Ergebnis_H90_W1_Einstein_nichtlinear.md`.

**Autorentscheidung (6.11.): korrigiert.** Ab jetzt S = ∫ e [ −(1/2κ) R(e, ω) + L_Weyl − ¼F² ] in der Signatur (+, −, −, −); Feldgleichung 3 lautet G̃ = κ(T^Weyl + T^Maxwell + T^(4f)) mit T^(4f) = −(3κ/16) j² g, und Feldgleichung 1 trägt +(3κ/8) j_a σ̄^a ψ_s statt −(3κ/8). Die Abschnitte oben bleiben als Stand vor der Korrektur stehen.
