# Ergebnis H90: Die Einstein-Gleichung von W1 ist voll nichtlinear hergeleitet und verträglich, aber W1 wie notiert hat das falsche Vorzeichen der Gravitation

Vorab-Notiz `Vorab_Notiz_H90_W1_Einstein_nichtlinear.md`, Commit `e5d03d8` (nicht blind, Erwartungen analytisch vorgerechnet). Code `k205_w1_einstein_nichtlinear.py` (Python/numpy, Ausgabe `k205_out.json`, Laufzeit 7 s) und `k205b_schwachfeld.wl` (Wolfram-Connector). Ein Lauf, keine Fehlläufe.

## Methode
Alle Felder als Jets bis zur dritten Ordnung an einem allgemeinen Punkt: Vierbein als zufälliges Polynom dritten Grades (gekrümmt, nicht diagonal), drei Weyl-Felder mit J = (+1, −1, +1), reelles A, q = 0,7, κ = 1,3. Die Spinor-Jets erfüllen die Weyl-Gleichung (Eichkopplung, Vier-Fermionen-Term) am Punkt und in erster Ableitung, A die Maxwell-Gleichung am Punkt. Drei Zufallshintergründe je Vorzeichen σ_g der Gravitationswirkung S_grav = (σ_g/2κ)∫e R, dazu je ein Lauf mit Spinoren, die die Feldgleichung verletzen.

Kontrollen der Rechnung: ω̃ aus dem Tetradenpostulat ist antisymmetrisch und torsionsfrei (Rest ≤ 4·10⁻¹⁶); R(ω̃) aus der Frame-Krümmung gleich dem Ricci-Skalar aus den Christoffel-Symbolen (≤ 3·10⁻¹⁵); die analytische Ableitung nach dem inversen Vierbein stimmt mit dem Differenzenquotienten (≤ 10⁻⁹, Grenze des Quotienten); ∇̃^μ G̃_μν = 0 (≤ 7·10⁻¹⁶).

## Ergebnisse (größte Reste über die drei Hintergründe und beide Vorzeichen)
- **H90a(i) bestätigt:** ω̃ löst die Cartan-Gleichung ohne Spinoren, samt Ableitungsterm (Rest 1·10⁻¹⁵ bei Termen der Größe 0,5–1). Mit Spinoren löst ω = ω̃ + K sie (Rest 2·10⁻¹⁴), K total antisymmetrisch (2·10⁻¹⁴), **K_cab = c κ ε_cabd j^d mit c = −σ_g/4** (Anpassungsrest 7·10⁻¹⁵).
- **H90a(ii) bestätigt:** Die Einstein–Cartan-Gleichung (Variation nach dem Vierbein bei festem ω = ω̃ + K) ist auf den Feldgleichungen symmetrisch (antisymmetrischer Teil 10⁻¹⁵) und gleich einem Vielfachen von G̃_μν + σ_g κ T^eff_μν (Rest 10⁻¹⁵) mit T^eff = T^Bel − g L_W + T^Maxwell − g λ j·j. Also **G̃ = −σ_g κ T^eff**, voll nichtlinear.
- **H90a(iii) bestätigt:** Der K-Term der Einstein–Cartan-Weyl-Gleichung ist 2λ j_a σ̄^a ψ mit **λ = −σ_g·3κ/16** (Rest 4·10⁻¹⁵, Imaginärteil 3·10⁻¹⁶).
- **H90b bestätigt:** ∇̃^μ T^eff_μν = 0 auf den Feldgleichungen (relativ 4·10⁻¹⁵).
- **Negativkontrollen:** Ohne Vier-Fermionen-Term in T^eff steigt der Rest der Einstein-Gleichung auf 0,12–0,19 und die Divergenz auf 0,25–0,81; mit Spinoren außerhalb der Feldgleichung auf 0,16–0,19 bzw. 0,92–1,05, der antisymmetrische Teil auf 0,30–0,35.
- **H90c bestätigt:** Für W1 wie notiert (σ_g = +1) ist **G̃ = −κ T^eff** (Faktor −1,000000000000 auf 4·10⁻¹⁵), λ = −3κ/16. Für σ_g = −1 ist G̃ = +κ T^eff und λ = +3κ/16.
- **H90d bestätigt (Wolfram):** Im schwachen statischen Feld ist G_00 = 2∇²Φ in derselben Krümmungskonvention (symbolischer Rest 0). G = +κT gibt ∇²Φ = 4πGρ, also Anziehung; G = −κT Abstoßung.

## Lesart
1. **Die Einstein-Gleichung von W1 ist jetzt unabhängig hergeleitet**, nicht mehr aus der Standardtheorie übernommen: Cartan-Gleichung, Elimination der Torsion, Einstein–Cartan-Gleichung, ihre Riemann-Form mit dem Vier-Fermionen-Term und die Verträglichkeit mit der Bianchi-Identität. Die Form der Feldgleichung 3 der W1-Notiz stimmt, kein Λ.
2. **Das Vorzeichen stimmt nicht.** Mit +(1/2κ)R in der Signatur (+, −, −, −) und der Krümmungskonvention von k173/k203 stößt die Gravitation positive Energie ab. Physikalisch richtig ist S_grav = −(1/2κ)∫e R (wie bei Landau–Lifschitz in dieser Signatur), gleichwertig: W1 wie notiert mit κ < 0 lesen. Die W1-Notiz nennt ihre Krümmungskonvention nicht; die Rechnungen k173, k203 und k204 benutzen die hier geprüfte.
3. **Mit dem physikalischen Vorzeichen** (σ_g = −1) gilt:
   - L_4f = +(3/16) κ j·j statt −(3/16) κ j·j. Der Betrag 3/16 aus H88 und k173 bleibt.
   - T^(4f) = −(3κ/16) j² g. Die Λ-Form aus H89a bleibt, das Vorzeichen kehrt sich um.
   - Der homogene Zustand aus H89b hat ρ = p = −λn² = −(3κ/16) n² < 0. Das ist die negative Spin-Energiedichte, wie sie aus der Einstein–Cartan-Literatur bekannt ist (Kerlick, Hehl u. a.; Literatur hier nicht neu nachgeschlagen).
4. **Folgen für frühere Aussagen.** Sie werden nicht umgeschrieben, die Korrektur kommt in die nächste Runde:
   - H88/r81 („Torsion −(3/16)κ j²“) und H89a/b: richtig für die Wirkung wie notiert, physikalisch mit umgekehrtem Vorzeichen.
   - Die Korrektur r86.4 („ρ ∝ −κn² trifft nicht zu, ρ > 0“) gilt nur für die Wirkung wie notiert. Mit dem physikalischen Vorzeichen stimmte die ursprüngliche Lesart der W1-Notiz.
   - r82.4 (Torsions-Paarkanal „anziehend, H_int ⊃ −(3/4)κΦ†Φ“): Mit dem physikalischen Vorzeichen ist der Kanal abstoßend (H_int ⊃ +(3/4)κΦ†Φ). Ein Paarkondensat an der Planck-Skala entsteht über diesen Kanal dann nicht; die daran geknüpfte ν^c-Majorana- und See-saw-Lesart fällt.
   - Noch nicht geprüft: r82 (H74, H75), r83 (H76) und r84/r85, soweit sie das Vorzeichen von κ oder des Vier-Fermionen-Terms benutzen. H76 und H75 hängen am Graviton und damit am Vorzeichen der Gravitation. Das muss vor der Korrekturrunde durchgesehen werden.
   - „W1 erzeugt keinen Vakuumterm“ (r81) bleibt richtig.
5. **Zurückgestellte Ideen:** Der Auslöser von I3 (Λ-Rechnung) ist berührt. Der Vier-Fermionen-Anteil hat Λ-Form, mit dem physikalischen Vorzeichen als negative Vakuumenergie (T^(4f) = −(3κ/16) j² g). Das wird dem Autor genannt.

## Offen
- Die Autorentscheidung, ob W1 auf S_grav = −(1/2κ)∫e R korrigiert wird (empfohlen), oder ob eine Lesart mit κ < 0 gemeint war.
- Die Durchsicht von r82 bis r85 auf Abhängigkeit vom Vorzeichen.
- Die Korrekturrunde v4.10.0-r01 (H90 und die Korrekturen).
