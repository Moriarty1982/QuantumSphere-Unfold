# Vorab-Notiz H93: Asymptotik der Urknall-Beimischung, hergeleitet: ln|C| = −πkΔ + c√(kΔ) − Re L/2 + O((kΔ)^{−1/2}), c = 2√π Γ(3/4)/Γ(1/4)·Re√L

**Stand:** 6. November 2026, vor der Rechnung festgelegt. Autor (6.11.): „H93 herleiten“. **Teilweise nicht blind:** Die Erkundung aus H92 (ln|r| bis kΔ = 200, Fit c = 1,81) und C bis kΔ = 60 sind bekannt. Die Herleitung unten nutzt diese Zahlen nicht. Die Wahl des Umkehrpunkts (siehe unten) ist aber mit Kenntnis des Vorzeichens getroffen: |r| wächst. Neu und blind sind die Werte bei kΔ = 300 und 600 (lokal) und bei kΔ = 80–120 (volles Problem).

## Vorwissen geprüft
`Ergebnis_H91_…` (k206: C bis kΔ = 60, wellige Steigung), `Ergebnis_H92_…` (k207: C ≈ r(λ)e^{−πkΔ}, λ = L kΔ/2; a verfehlt um ln R ≈ −0,62, nachträglich e^{−L/2}; Erkundung ln|r| ≈ 1,81√(kΔ); Kandidat |√L| = 1,834 nicht entschieden). Keine frühere Notiz enthält eine WKB-Herleitung oder die Konstante Γ(3/4)/Γ(1/4).

## Herleitung
1. **u-Form.** Die Gleichung y'' + p y' + k² y = 0 mit p = w'/w geht mit y = w^{−1/2}u über in u'' + Q u = 0, Q = k² − p²/4 − p'/2. Links ist w = 1, rechts w = e^L. Kommt u als e^{ikt} herein und geht als … + C_u e^{−ikt} hinaus, so ist **C = e^{−L/2} C_u**. Das ist der in H92a fehlende Faktor, jetzt hergeleitet.
2. **Lokal.** An t₀ = iπΔ/2 gilt p ≈ −β/τ², β = LΔ/2, τ = t − t₀. In σ = kτ ist das lokale Q = 1 − λ²/(4σ⁴) − λ/σ³ mit λ = βk = L kΔ/2. In u-Form ist die lokale Reflexion dieselbe wie in y-Form, weil e^{−λ/(2σ)} → 1. Also C_u ≈ r(λ)e^{−πkΔ}, wie in H92.
3. **WKB für großes λ.** Mit σ = √λ·2^{−1/2}·η gilt in führender Ordnung Q₀ = 1 − η^{−4}, mit vier Umkehrpunkten η⁴ = 1. Die Überbarriere-Reflexion (Pokrovskii–Khalatnikov) ist r ≈ −i·exp(2iF) mit F = σ_t + ∫_∞^{σ_t}(√Q − 1)dσ. Für den Umkehrpunkt η_t = −i (aus dem Vorzeichen: |r| wächst, die übrigen geben fallendes oder kleineres |r|) ist
   F₀ = √(λ/2)·(−i)·(1 + I),  1 + I = 1 + ∫₁^∞(1 − √(1 − η^{−4}))dη = 2√π Γ(3/4)/Γ(1/4) = 1,1981402.
   (Mit u = η^{−4} wird das Integral zur unvollständigen Betafunktion: B(−¼, 3/2) = −8√π Γ(3/4)/Γ(1/4).) Daraus folgt ln|r| = −2 Im F₀ = **c√(kΔ)** mit **c = 2√π Γ(3/4)/Γ(1/4)·Re√L = 1,809205** (für L und L̄ gleich; das ist die asymptotische Form von H92c).
4. **Erste Korrektur.** Der Term −λ/σ³ in Q gibt δF = −½∫_∞^{ζ_t} dζ/(ζ³√(1 − 1/(4ζ⁴))) = −½·[−arcsin(1/(2ζ²))] = −π/4 (mit ζ = σ/√λ, ζ_t² = −½). Das ist reell, also nur eine Phase. Der Vorfaktor −i hat Betrag 1. Daher **ln|r| = c√(kΔ) + 0 + O((kΔ)^{−1/2})**, ohne additive Konstante.
5. **Subdominanter Beitrag (Wellen).** Der Umkehrpunkt η = +1 gibt e^{1,24637√(kΔ)}. Er ist relativ um e^{−0,5628√(kΔ)} kleiner und schwingt mit 2Re(F_{−i} − F_{+1}) = −3,0556√(kΔ), also mit Periode ≈ 2,06 in √(kΔ). Das ist die Quelle der Wellen aus H91. Sein Verbindungskoeffizient wird nicht vorhergesagt.
6. **Volles Problem.** Die Korrekturen der lokalen Näherung (nächster Laurent-Term von sech²) gehen in der Phase mit O((kΔ)^{−1/2}). Zusammen:
   **ln|C| = −πkΔ + c√(kΔ) − Re L/2 + O((kΔ)^{−1/2}),  −Re L/2 = −½ln(a/b) = −0,599001.**

## Rechnung
`llm/k208_wkb_pruefung.py` (Python/scipy). Lokal: r(λ) wie k207 bei kΔ = 300 und 600, mit h = 1 + 0,5√|λ| (der reflektierte Anteil soll nicht unter die Rechengenauigkeit fallen), Kontrolle 0,7·h und doppeltes S. Voll: C wie k206 (Konturen 0,90 und 0,95·πΔ/2) bei kΔ = 80, 100, 120. Beide Drehsinne.

## Hypothesen und Kriterien
- **H93a (Koeffizient):** Die Steigung (ln|r(600)| − ln|r(300)|)/(√600 − √300) liegt innerhalb 0,3 % bei c = 1,809205.
- **H93b (keine Konstante):** |ln|r| − c√(kΔ)| ≤ 0,05 bei kΔ = 300 und 600, und bei 600 kleiner als bei 300.
- **H93c (volles Problem):** |ln|C| + πkΔ − c√(kΔ) + 0,599001| ≤ 0,02 bei kΔ = 100 und 120.
- **H93d (Drehsinne):** a–c gelten für beide Drehsinne mit denselben Zahlen (Unterschied ≤ 10⁻⁶ in ln).
- **Gültigkeit:** Kontrollen relativ ≤ 10⁻⁶; die beiden Konturen des vollen Problems ≤ 10⁻⁶. Sonst gelten a–d als ungültig.

## Umgang mit Abweichungen
Wenn a verfehlt wird, ist die Wahl des Umkehrpunkts oder die Konstante falsch. Dann werden die vier Umkehrpunkte einzeln geprüft und das offengelegt, ohne c anzupassen. Wenn b verfehlt wird, a aber erfüllt ist, gibt es eine Konstante, die Schritt 4 übersieht. Wenn c verfehlt wird, a und b aber erfüllt sind, liegt der Fehler in Schritt 1 oder 6.
