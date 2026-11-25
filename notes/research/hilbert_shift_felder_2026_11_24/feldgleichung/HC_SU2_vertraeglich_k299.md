# Eine Fassung des HC, die mit SU(2) verträglich ist: Bedingung an den Strom statt an die Norm (Erkundung k299, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Unter SU(2) links ist der Winkel zwischen Vorstufe und Anhang keine messbare Größe, das Potential kann nur von der vollen Norm
abhängen, und deshalb musste die Fassung aus k297 scheitern (H132). Invariant ist dagegen der Strom J = ψ̄·Dψ, und auf der Lösung aus k292 ist
J_i = ω(a² − b²) und |J_⊥| = 2abω. Das Verhältnis |J_⊥|/J_i = 2μ/(1 − μ²) ist die Form der Ellipse in eichinvarianter Schreibweise. Als Bedingung an die
**Form der Bewegung** (Fassung F) verträgt sich der HC mit SU(2): Licht bleibt masselos, die Eichfeldmassen sind die von k291, die Lösung bleibt exakt.
Als **Stauchung** des Bewegungsterms (Fassung S) verträgt er sich ebenfalls mit SU(2) und masselosem Licht, verschiebt aber m_W/m_Z, und das ist für jede
naheliegende Zuordnung zu γ_L durch die Messung ausgeschlossen, falls das Feld das elektroschwache ist.

Auftrag des Autors (25.11.2026, 11:12 UTC): „weiter bitte“ auf den Vorschlag, eine SU(2)-verträgliche Fassung des HC zu rechnen. **Erkundung, nicht blind:**
Die Invarianten und die Massenformeln stehen beim Aufschreiben fest, und der Messwert von ρ war mir bekannt. H133 bleibt frei. Vergeben: Skripte **k299, k299b**.

Werkzeuge: Python mit sympy (exakt). Wolfram Language unabhängig mit Quaternionen als 2×2-Matrizen (k299b), alles stimmt überein. Qiskit nicht eingesetzt.
Kein HDL/MMA-Vergleich.

## Vorwissen geprüft
k290 (Zusatzterme aus D_μψ oder aus Strömen; die Stromvariante behält die so(4)), k291 Punkt 6 (elektroschwache Massenmatrix auf ℍ), k292 (Linksladung
ω(a² + b²), Rechtsladung ω(a² − b²)), k297 (HC als η(B − μ²A)², Setzung), H132/k298 (kein masseloses Feld mit U(1) × U(1); HC-Potential nicht SU(2)-invariant).
`thm:hc-quasiconformal` (μ = β_sym², K = γ_L). Im Repo gibt es keine Rechnung zum elektroschwachen ρ-Parameter (Suche nach „custodial“ und „ρ-Parameter“, 25.11.; die Treffer zu „rho_0“ in den
OP3- und OP5-Notizen meinen andere Größen).

## Ergebnisse
1. **Was SU(2) links übrig lässt (k299 Abschnitt 1):** N ist invariant, B − μ²A nicht. Der Strom J = ψ̄·Dψ ist unter allen Linksdrehungen invariant.
   Unter der Rechtsdrehung um i sind J_i und |J_⊥|² invariant, J_j und J_k drehen ineinander. Es gilt Re J = ½∂N und N(J) = N(ψ)·N(∂ψ).
2. **Die Ellipse im Strom (Abschnitt 2, Z1):** Auf ψ = e^{iωt}(a + b·j) ist J_t = ω(a² − b²)·i + 2abω·k. Mit b = μa: |J_⊥|/J_i = 2μ/(1 − μ²) = (K − 1/K)/2.
   Mit γ_L = 1,8644: 0,6640. Der Anteil des Stroms in der Richtung i ist cos 2θ = 0,8331.
3. **Fassung S, Stauchung (Abschnitt 3, Z2):** L = ½N(Dψ) + ξ·J_i²/(2N). Das ist die Sphäre S³, entlang der Hopf-Faser gestaucht oder gestreckt.
   - Massenquadrate g²f²/4 (zweimal), (g² + g′²)(1 + ξ)f²/4 und **0**, unabhängig vom Winkel θ. Licht bleibt masselos.
   - **ρ = m_W²/(m_Z² cos²θ_W) = 1/(1 + ξ).** In der Sprache des Standardmodells ist das der Operator, der die Custodial-Symmetrie bricht.
   - Die Stauchung legt die Form der Bahn nicht fest: Die Energie der Drehung ist ½ω²f²(1 + ξ·cos²2θ), stationär nur bei b = 0 (Kreis) und a = b (Linie).
4. **Fassung F, Form der Bewegung (Abschnitt 4, Z3, Z4):** P = η₂(|J_⊥|² − τ²J_i²)²/N² mit τ = 2μ/(1 − μ²).
   - Invariant unter SU(2) links und U(1) rechts.
   - Im Vakuum ist P von vierter Ordnung in den Eichfeldern: **keine Massen, ρ = 1, Licht masselos**, Spektrum wie k291.
   - Auf der Lösung mit b = μa ist P = 0 mit doppelter Nullstelle, die Lösung bleibt exakt. Eine Abweichung b = (μ + d)a kostet 64a⁴μ²ω⁴d²/(1 − μ²)².
     Der HC wirkt also nur, wenn sich das Feld dreht, und stellt dann das Achsenverhältnis zurück.
5. **Zahlen (Abschnitt 5, Z5):**
   | Zuordnung in Fassung S | ρ |
   |---|---|
   | 1 + ξ = γ_L² | 0,288 |
   | 1 + ξ = γ_L | 0,536 |
   | 1 + ξ = 1/γ_L | 1,864 |
   | 1 + ξ = 1/γ_L² | 3,476 |
   | 1 + ξ = 1 + μ² | 0,917 |
   | 1 + ξ = 1/cos²2θ | 0,694 |

   Gemessen ist ρ₀ ≈ 1,0004 ± 0,0002 (aus dem Gedächtnis, nicht nachgeschlagen). Erlaubt wäre |ξ| unter etwa 0,001. Keine Zuordnung passt.
   In Fassung F kommt die Skala nur aus V(N) und den Schleifen der Eichfelder: m_s² = 3(2g⁴ + (g² + g′²)²)f²/(128π²), mit g = 0,652, g′ = 0,357, f = 246 GeV
   also m_s ≈ 9,8 GeV. Das ist der bekannte Coleman–Weinberg-Wert ohne Fermionen, weit unter den gemessenen 125 GeV.

## Einordnung
- **Zur Spannung aus H129 und H132:** Sie löst sich in Fassung F. Der HC ist dann keine Bedingung an das Vakuum, sondern an die Bewegung. Vorstufe und Anhang
  sind im Vakuum nicht unterscheidbar (der Winkel ist Eichung), unterscheidbar sind sie nur am drehenden Feld, über die zwei Stromanteile J_i und J_⊥.
  Das passt zu k292 („der HC legt die Form fest, nicht die Amplitude“) besser als die Fassung aus k297.
- **Was dabei verloren geht:** Das Bild aus k297, in dem der HC die flache Richtung des Potentials ist und die Schleife dort die Skala erzeugt. In Fassung F
  hat der HC mit der Skala nichts zu tun. Die Vorzeichen-Aussagen aus k297 (κ < 0) gelten nur für die Fassung dort.
- **Fassung S ist prüfbar und fällt durch,** wenn das Feld von HS(2) das elektroschwache ist und ξ von der Größenordnung γ_L. Das ist die erste Stelle in
  diesem Faden, an der eine Messung eine Fassung ausschließt. Sie schließt nicht den HC aus, sondern seine Lesart als Stauchung des Zielraums.
- **Die Zuordnung zum elektroschwachen Feld bleibt eine Lesart** (k291 Grenzen). Der Wert 9,8 GeV zeigt, dass die Skala in dieser einfachsten Form nicht
  aus den Eichfeld-Schleifen allein kommen kann, falls die Zuordnung gilt.

## Grenzen
- Zwei Fassungen, beide gesetzt. Der Bestand führt den HC als lineare Projektion; welche Feldgröße er einschränkt, ist nicht hergeleitet.
- Fassung F ist ein Term achter Ordnung in den Feldern mit vier Ableitungen und einem Koeffizienten mit Massendimension. Stabilität, Schleifen und die Wirkung
  auf ortsabhängige Lösungen sind nicht geprüft.
- Messwerte aus dem Gedächtnis. Klassische Massenmatrix, ohne Fermionen, nur ℂ → ℍ. β_sym und γ_L eingesetzt (OP1).
- OP1, OP3, OP4, OP5 bleiben offen, kein Guard ist berührt.

## Mögliche nächste Schritte
- **Fassung F am Igel aus k291:** Der ruhende Igel hat nur räumliche Ströme. Ändert P seine Energie oder seine Form, und hängt das an μ? Das Ergebnis steht nicht
  vorab fest (numerische Minimierung), wäre also ein Kandidat für H133.
- **Schritt ℍ → 𝕆:** Dort gibt es keinen assoziativen Strom mehr; was aus J wird, ist die nächste Strukturfrage.

## Dateien
`k299_hc_su2_vertraeglich.py` (`k299_out.txt`), `k299b_gegenprobe.wl` (`k299b_out.txt`).
