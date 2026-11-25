# Vorab-Notiz H149: Was legt θ = π/4 und δ = 2/9 fest?

**25.11.2026, vor jeder Rechnung committet.** Anlass: Autor „mergen, pushen und weiter“ nach H148; Frage aus H148 „Was offen bleibt“: warum θ = π/4
und woher δ = 2/9. Vergeben: H149, Skripte k332 (Python, sympy/numpy) und k332b (Wolfram, unabhängige Gegenprobe). Qiskit nicht vorgesehen (keine
Schaltung, kein Messablauf). Kein HDL/MMA-Vergleich (kein RUN_TAPE, kein endlicher Auswahlablauf). Vorzeichen werden **nicht** gesetzt: Wo ein
Ergebnis von einem Vorzeichen abhängt, werden beide Fälle angegeben.

## Vorwissen geprüft
- H148 (k331): K = 1/(3cos²θ) in der Amplituden-Auslesung g_k = 1/√3 + √(2/3)·w⊗f_k, Ψ = cosθ + sinθ·w⊗n(δ); θ = π/4 ⇔ K = ⅔; δ = 2/9 eingesetzt.
- H147 (k330): Mischwinkel zwischen HS(0)-Einheit e₀ und e₇ von der Symmetrie frei; e₇² = −e₀.
- r13/k255 (Koide aus exp(uπ/4)), r16/r17 (Photonpunkt, Stokes-Mitte), H123 (Oktant-Phase).
- k290 (Ansatz: ein Element hat nur die Invarianten N(ψ) und Re ψ; V = V(N, Re ψ); bei geeichter U(1) V = V(N)), k291 (μ₀ = μ₁ = 0, Marc),
  k297 (Tausch Vorstufe ↔ Anhang = Orientierungsumkehr μ → 1/μ = Materie- gegen Tachyon-Frame; invariant nur μ = 1, die lineare Polarisation;
  der HC mit μ = β_sym² bricht den Tausch), k282 (Albert-Algebra: Tr W², N(W)).
- v4.8.0-r10 (kein kanonischer Winkel für die Lepton-Phase, π/12 zweitnächster), r11/H1 (δ = K/3 = 2/9 nur für Lepton-Polmassen, für Quarks und
  laufende Massen widerlegt), r12.1 (v₀v₁v₂ = t³(1 − 3r²/2 + r³cos3δ/√2)), H11 (r16) und H16 (v4.9.0-r26): Potentiale in den Slot-Normen bis
  Grad sechs haben kein Minimum mit drei verschiedenen Normen.
- `../../op3_selection_principle_2026_11_13.md` (Oktant = Fluss π/4 mit masselosem Elektron, H101; nötiger Fluss ΔΦ = 3(π/12 − θ_e)),
  CT-002 (ΔΦ = γ_M/2, also δ = π/12 − γ_M/6, Platzhalter), `../../op3_time_cycle_2026_11_15/README.md` (Gewichte aus Koide und Phase; kein
  nativer Wert unter 24 Kandidaten), `../../op3_phase_source_search_2026_11_12.md`.
- Zurückgestellte Ideen I1–I7: kein Auslöser getroffen (I1 berührt nur über CT-002, das hier nicht neu bewertet wird).
- **Suchrichtung:** rückwärts. Ziel θ = π/4, δ = 2/9; notwendige Bedingung für eine Festlegung ohne Anpassung ist ein stationärer Punkt eines
  zulässigen Terms, der dort ohne abgestimmte Koeffizienten liegt. Daraus werden die Kandidaten erzeugt, nicht durch Simulation.

## Hypothesen und Kriterien
Bezeichnungen: Ψ = cosθ·1 + sinθ·U mit U = w⊗n(δ) reine Einheit, ReΨ² = cos 2θ, c_k = ⟨g_k, Ψ⟩.

- **H149a (nicht blind, analytisch, Kontrolle):** θ = π/4 ⇔ ReΨ² = 0 ⇔ Ψ lichtartig in der Form x₀² − |x⃗|² ⇔ Ψ fest unter dem Tausch
  J: ψ ↦ U·ψ̄ (in der Ebene {1, U}; entspricht μ = b/a = 1 aus k297) ⇔ p₊ = p₋. Gilt für jedes δ.
  *Kriterium:* exakte Identitäten in sympy und Wolfram. Bestätigt, wenn alle Äquivalenzen exakt gelten.
- **H149b (gewertet):** Jeder Term der Form V(N(Ψ), ReΨ) (k290) hängt auf dem Ansatz nicht von δ ab: ∂_δV ≡ 0. Bei geeichter U(1) (V = V(N)) hängt er
  auch nicht von θ ab; θ ist dann die Phase der U(1) und eine flache Richtung.
  *Kriterium:* symbolisch für allgemeines V bis Grad 4. Bestätigt, wenn ∂_δV = 0 identisch und bei V(N) zusätzlich ∂_θV = 0.
- **H149c (gewertet):** Für das allgemeine Potential vierter Ordnung in φ = ReΨ und χ = |ImΨ| (Koeffizienten μ₀², μ₁², a, b, c mit
  V = ½μ₀²φ² + ½μ₁²χ² + aφ⁴ + bφ²χ² + cχ⁴) auf N = 1 ist θ = π/4 genau dann stationär, wenn **eine** lineare Bedingung gilt
  (Vorhersage: der tauschungerade Anteil, also die Kombination aus μ₀² − μ₁² und a − c, muss verschwinden). Mit k291 (μ₀ = μ₁ = 0) bleibt a = c. Unter dem Tausch J
  (a = c, μ₀ = μ₁) ist π/4 immer stationär; ob Minimum oder Maximum, entscheidet das Vorzeichen eines Koeffizienten (b − 2c bzw. von Re Ψ⁴), und
  das Gegenstück ist θ = 0 (K = ⅓, drei gleiche Massen).
  *Kriterium:* Anzahl unabhängiger Bedingungen für ∂_θV|π/4 = 0. Bestätigt bei genau einer, die der tauschungerade Anteil ist.
  *Zusatz (Lesart k297):* Liest man θ als Winkel zwischen Vorstufe und Anhang (tanθ = μ), gibt der HC tanθ = β_sym² bzw. im Tachyon-Frame
  tanθ = β_sym⁻², also K = (1 + β_sym⁴)/3 bzw. (1 + β_sym⁻⁴)/3. Vorhersage: keiner davon ist ⅔; der Koide-Punkt ist der Tausch-Fixpunkt, den der
  HC gerade bricht. Wird mitgerechnet, nicht als eigener Test gewertet (analytisch klar).
- **H149d (gewertet):** δ sieht nur ein Term, der die drei Kopien kennt. Der niedrigste ist die kubische Norm N(W) = c₀c₁c₂ (W = diag(c_k), Albert,
  k282), mit cos3δ als einziger δ-Abhängigkeit bei festem θ (Tr W, Tr W² hängen nicht von δ ab). Für jedes V(Tr W, Tr W², N(W)) liegen die
  δ-stationären Punkte bei sin3δ = 0 (zwei gleiche Massen) oder dort, wo ∂V/∂N = 0, was einen abgestimmten Koeffizienten verlangt.
  *Kriterium:* (i) Tr W und Tr W² δ-unabhängig, N(W) = A + B·cos3δ exakt; (ii) für V = αN + βN² und V = αN + βN² + γN³ mit festen ganzzahligen
  Koeffizienten aus {−3,…,3} (ohne Anpassung an Daten) gibt kein Minimum in δ drei verschiedene Massen mit δ innerhalb 1 % von 2/9.
  Bestätigt, wenn (i) exakt gilt und (ii) keinen Treffer gibt. Widerlegt bei einem Treffer.
- **H149e (gewertet):** Strukturelle Kandidaten für δ, vorab fest, genau die
  vier Werte π/12 = 0,261799, artanh(β_sym)/3 (β_sym = 0,5493), γ_M = 0,237533, arctan(β_sym²). *Kriterium:* innerhalb 1 % von δ_fit
  (aus m_μ/m_e bei θ = π/4). Vorhersage: kein Treffer.

## Nicht gewertet (bekannt oder vorab gesehen)
- δ = π/12 − γ_M/6 (CT-002, Platzhalter) und δ = K/3 (H1, Koides eigene Beziehung; mit K = 1/(3cos²θ) wäre δ = 1/(9cos²θ)) treffen bekanntlich;
  sie werden nur nachgerechnet und nicht als Herleitung gezählt.
- **Vor dieser Notiz bemerkt:** Mit zwei Harmonischen V = a·cos3δ + b·cos6δ liegt das Minimum bei cos3δ = −a/(4b); δ = 2/9 verlangt
  a/b = −4cos(2/3) = −3,1435, nahe −π. Das ist ein Zahlentreffer bei einem frei gewählten Verhältnis. Es wird nachgerechnet, ob
  δ = arccos(π/4)/3 mit dem aus den Massen bestimmten δ und dessen Unsicherheit verträglich ist, aber nicht gewertet.

## Grenzen
- Die Amplituden-Auslesung (r13/k255) bleibt gesetzt; ebenso die Skala.
- Ein stationärer Punkt aus Symmetrie ist keine Herleitung des Vorzeichens; Minimum oder Maximum bleibt offen.
- OP3, OP4 offen; kein Guard wird berührt.
