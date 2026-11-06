# Vorab-Notiz H90: Die volle nichtlineare Einstein-Gleichung von W1, ihre Verträglichkeit (Bianchi) und das Vorzeichen der Gravitationswirkung

**Stand:** 6. November 2026, vor der Rechnung festgelegt. **Nicht blind:** Die Erwartungen sind analytisch vorgerechnet, besonders das Vorzeichen in H90c. Autor (6.11.): „Einstein-Gleichung W1“, Option 1 der Übergabe (in H88 und H89 offen geblieben). Hauptrechnung lokal mit Python/numpy (`llm/k205_w1_einstein_nichtlinear.py`), weil die Wolfram-Cloud nach etwa 100 s abbricht. Gegenprobe des Vorzeichens im schwachen Feld mit Wolfram (`llm/k205b_schwachfeld.wl`).

## Vorwissen geprüft
- `Wirkung_W1_Dixon_U1.md`: Wirkung S = ∫ e [ (1/2κ) R(e, ω) + L_Weyl − ¼F² ], η = diag(1, −1, −1, −1), Feldgleichung 3 „G̃ = κ(T^Weyl + T^Maxwell + T^(4f)), ohne Λ“ (aus der Standardtheorie übernommen, nicht hergeleitet). Die Krümmungskonvention von R(ω) steht dort nicht.
- `k173_torsion.py` (Docstring): Die Kontrolle gegen Hehl–Datta prüft nur den Betrag |c| = 3/16, nicht das Vorzeichen. Der Krümmungsanteil ist R(K) = K_μ^a_c K_ν^cb − K_ν^a_c K_μ^cb, also die Standardkonvention R^ab = dω^ab + ω^a_c ∧ ω^cb; ebenso `rsc` in `k203_w1_feldgleichungen.wl`.
- H88 (`Ergebnis_H88_…`): L_eff = −(3/16)κ j·j, Weyl-Gleichung, Ward bestätigt, jeweils mit dem Vorzeichen +1/(2κ) der Wirkung. H89 (`Ergebnis_H89_…`): T^(4f) = (3κ/16) j² g, homogener Zustand ρ = p = +(3κ/16)n², Korrektur der W1-Notiz („ρ ∝ −κn²“ trifft nicht zu). Beides hängt am Vorzeichen der Gravitationswirkung.
- `Erkundung_Torsion_Kondensat.md` (r82.4): Paarkanal „anziehend, H_int ⊃ −(3/4)κΦ†Φ“ aus L = −(3/16)κ j·j; hängt am selben Vorzeichen.
- `Vorab_Notiz_H48_Einfrieren_beta.md`: Hehl–Datta-Vorzeichen dort aus der Literatur übernommen, nicht aus W1.
- Suche nach „Kerlick“, „abstoßend“, „Landau“, „Vorzeichen der Gravitationswirkung“ in `llm/`: kein Vorbefund zum Vorzeichen der Wirkung.

## Aufbau
An einem allgemeinen Punkt eines gekrümmten Hintergrunds (Vierbein als zufälliges Polynom zweiten Grades) werden alle Felder als Jets bis zur zweiten Ordnung geführt: drei Weyl-Felder mit U(1)-Ladungen J = (+1, −1, +1), das Potential A, der Vierbein. Die Spinor- und A-Jets werden auf die Feldgleichungen gelegt (Weyl-Gleichung mit Vier-Fermionen-Term und Eichkopplung bis zur ersten Ableitung, Maxwell am Punkt). Konventionen wie k203/k204: D_μψ = ∂_μψ + ½ω_μab Σ^{ab}ψ + iqJA_μψ, Σ^{ab} = ¼(σ^aσ̄^b − σ^bσ̄^a), Krümmung R^ab_μν = ∂_μω_ν^ab − ∂_νω_μ^ab + ω_μ^a_c ω_ν^cb − ω_ν^a_c ω_μ^cb. Die Gravitationswirkung wird mit Vorzeichen σ_g geschrieben, S_grav = (σ_g/2κ)∫e R; W1 wie notiert ist σ_g = +1. Beide Vorzeichen werden gerechnet.

## Teile und Erwartungen
- **H90a (Einstein–Cartan-Gleichungen, nichtlinear):**
  (i) Der Spinzusammenhang ω̃ aus dem Tetradenpostulat löst die Cartan-Gleichung (Variation nach ω samt Ableitungsterm) ohne Spinoren; mit Spinoren löst ω = ω̃ + K sie, K_cab = c·κ·ε_cabd j^d total antisymmetrisch.
  (ii) Die Einstein–Cartan-Gleichung (Variation nach dem Vierbein bei festem ω = ω̃ + K, algebraisch) ist auf den Feldgleichungen bis auf einen Faktor gleich G̃_μν + σ_g κ T^eff_μν mit
  T^eff = T^Bel − g L_W + T^Maxwell − g λ j·j, λ = −σ_g·(3κ/16),
  und ihr antisymmetrischer Teil verschwindet. Also G̃ = −σ_g κ T^eff, voll nichtlinear.
  (iii) Der K-Term der Einstein–Cartan-Weyl-Gleichung ist gleich 2λ j_a σ̄^a ψ (der Vier-Fermionen-Term in der Riemann-Form).
- **H90b (Verträglichkeit, Bianchi):** ∇̃^μ T^eff_μν = 0 auf den Feldgleichungen, an einem allgemeinen Punkt des gekrümmten Hintergrunds; ∇̃^μ G̃_μν = 0 als Kontrolle der Rechnung.
- **H90c (Vorzeichen):** Mit W1 wie notiert (σ_g = +1, η = +−−−, Krümmung wie oben) gilt **G̃ = −κ T^eff**: Gravitation stößt positive Energie ab. Physikalisch richtig ist σ_g = −1, also S_grav = −(1/2κ)∫e R in dieser Signatur (wie bei Landau–Lifschitz). Dann gilt λ = +3κ/16, also L_4f = +(3/16)κ j·j, T^(4f) = −(3κ/16) j² g, und der homogene Zustand aus H89b hat ρ = p = −(3κ/16)n² < 0 (das bekannte Einstein–Cartan-Verhalten mit negativer Spin-Energiedichte, Kerlick, Hehl u. a.).
- **H90d (Gegenprobe Wolfram):** Für g = diag(1 + 2Φ, −(1 − 2Φ), −(1 − 2Φ), −(1 − 2Φ)), linear in Φ(x, y, z), ist G_00 = 2∇²Φ in der Konvention oben; G = +κT gibt ∇²Φ = 4πGρ (anziehend).

## Kriterien
- H90a, b: relative Reste < 10⁻⁹ an drei unabhängigen Zufallspunkten (verschiedene Hintergründe und Felder), für σ_g = +1 und −1. Der Faktor in H90a(ii) wird angepasst; das Verhältnis zwischen G̃- und T-Anteil ist das geprüfte Ergebnis. Negativkontrollen: ohne Vier-Fermionen-Term in T^eff und mit Spinor-Jets, die die Feldgleichung verletzen, muss der Rest von der Größe 1 sein.
- H90c bestätigt, wenn das Verhältnis in H90a(ii) für σ_g = +1 auf 10⁻⁹ den Wert G̃ = −κT^eff ergibt und λ auf 10⁻⁹ den Wert −σ_g·3κ/16 hat. H90d bestätigt, wenn der symbolische Rest 0 ist.

## Umgang mit Abweichungen und Folgen
Abweichungen werden wie in H88 und H89 erst auf Konventionen im Prüfcode, dann auf Rechenfehler, dann auf die W1-Notiz zurückgeführt; jeder Fehllauf wird offengelegt. **Wenn H90c bestätigt wird:** Die W1-Wirkung wie notiert hat das falsche Vorzeichen der Gravitation (oder ist mit κ < 0 zu lesen). Dann sind neu zu bewerten, ohne sie umzuschreiben (Korrektur in der nächsten Runde): das Vorzeichen von L_eff in H88/r81 (Betrag bleibt), H89a/b und die Korrektur r86.4 (dann stimmte die ursprüngliche Lesart „ρ ∝ −κn²“ der W1-Notiz), der Paarkanal in r82.4 (dann abstoßend, kein Kondensat), r83/r84, soweit sie das Vorzeichen benutzen. Die Beträge und Formen (Λ-Form des Vier-Fermionen-Terms, p = ρ) bleiben. Wenn H90c nicht bestätigt wird, wird die Ursache bestimmt, bevor etwas an der W1-Notiz geändert wird.
