# Vorab-Notiz H164: Ist β_sym im Modell der Überlapp zweier Auslesen (θ = 113,35°)?

**Stand:** 2026-11-26, vor der Rechnung festgelegt und vor dem ersten Skriptlauf committet. **Überwiegend nicht blind** (siehe „Vorwissen“ und „Vorab offengelegt“).
Anlass: H161 (k352) fand für zwei Richtungen im Winkel θ, dass ein Boost mit β = cos(θ/2) sie auf Gegenpunkte legt und dass |⟨ψ₁|ψ₂⟩| = β gilt; β = β_sym entspräche
θ = 113,35°, ohne Zuordnung. Freigabe des Autors 26.11.2026, 10:11 UTC („merge und weiter“).
Skripte **k355** (Python: sympy für die Identitäten, **Qiskit** `quantum_info` für Zustände, Überlappe und Mischungen) und **k355b** (Wolfram Language, exakt).
Werkzeugwahl: Wolfram für die symbolischen Identitäten; Qiskit, weil Zustände, Dichtematrizen und Überlappe explizit definiert sind. Kein HDL/MMA-Vergleich
(kein RUN_TAPE-Ablauf). Kein Guard wird berührt.

## Vorwissen geprüft
- **`thm:bsym-hopf`** (v470/10): β_sym = sin(θ_H/2) mit dem Hopf-Winkel θ_H ≈ 66,64° des Materie-Spinors gegen den Photonpol. Statusvermerk: Halbwinkelbeziehung eines
  reinen Zustands vom Pol aus, also im Bezugs-Frame R (r24); der Materie-Zustand der Konvention F ist bei gleichem β ein gemischter Zustand mit Bloch-Länge 1/γ_L
  (r17, r24.3: |b| = sech 2η); der Satz liest einen R-Zustand als Materie-Versatz (r61). Die Gleichsetzung „Versatz = Sinus des halben Winkels“ wird dort mit der
  „üblichen Halbwinkelbeziehung“ begründet, nicht hergeleitet.
- **`rem:bsym-hopf-gap`**: Hopf-Wert β = 1/√3, θ_H = 70,53°, γ_L = 2; γ_L = (1 + β²)/(1 − β²). k245: Hopf-Wert aus dem Nullpunkt j + ½.
- **r27**: Kickwinkel α mit cos 2α = 1/γ_L, also tan α = β: 28,78° gemessen, 30° am Hopf-Wert.
- **H45**: Maske mit ε = artanh β_sym. **k292**: Hopf-Sphäre von HS(2) mit cos ϑ = (a² − b²)/(a² + b²), Pol b = 0 (R), Äquator a = b (P); μ = b/a = β² bei M.
- **H161**: Boost β = cos(θ/2), invariante Masse M² = 2E₁E₂(1 − cos θ), Überlapp = β.
- Suche nach „Tetraeder“, „SIC“, „Aberration“ im Zusammenhang mit β_sym (26.11.): keine Fundstelle.

## Übersetzung (gesetzt)
Die Hopf-Sphäre wird als Himmelskugel von Lichtrichtungen gelesen (wie in H161); Zustände sind Spinoren (cos ϑ/2, e^{iφ}·sin ϑ/2). Benannte Zustände: N (Pol, R),
S (Gegenpol), K₁ (reiner Zustand im Winkel θ_H vom Pol), k_α (Kickzustand ∝ (1, β)), h (∝ (1, β²), HS(2) bei M), E (Äquator, ∝ (1, 1)), jeweils mit dem Tausch
(Komponenten vertauscht) und der Tachyon-Abbildung (zweite Komponente mal i).

## Hypothese H164
β_sym ist im Modell der Überlapp zweier Auslesen im Sinn von H161: Ein im Companion benanntes Zustandspaar hat den Überlapp β_sym als Identität, der zugehörige
Boost hat eine Bedeutung im Modell, und die gleichgewichtete Mischung der zwei Auslesen ist der Materie-Zustand.

## Entscheidungskriterien
- **K-a (Paar):** Unter allen Paaren der benannten Zustände gibt es eines mit |⟨ψ₁|ψ₂⟩| = β als Identität in β (symbolisch, nicht nur beim Zahlenwert):
  bestätigt. Nur Zahlentreffer innerhalb 1 % ohne Identität: widerlegt.
- **K-b (Boost):** Für dieses Paar gilt exakt: (i) Geschwindigkeit des Boosts auf Gegenpunkte = β_sym, Rapidität = ε der Maske (artanh β); (ii) zwei Frames mit ±β
  gegen das System der Gegenpunkte haben den relativen Lorentz-Faktor γ_L = (1 + β²)/(1 − β²); (iii) sech 2ε = 1/γ_L (r24.3). Alle drei: bestätigt.
- **K-c (Mischung):** Die gleichgewichtete Mischung der zwei Auslesen hat Bloch-Länge 1/γ_L und die Besetzungen des Materie-Zustands (1, β²)/(1 + β²): bestätigt.
  Andere Länge: widerlegt.
- **K-d (Bilder unter dem Boost):** Die Bilder von N, S, K₁, E unter dem Boost liegen (außer dem Gegenpunktpaar selbst) auf benannten Punkten oder im Winkel
  θ_H, 2α oder 4α zueinander (Identität in β): bestätigt. Sonst widerlegt.
- **Gesamturteil:** bestätigt, wenn K-a bis K-d bestätigt sind. „Trägt teilweise“, wenn K-a und K-b bestätigt sind und K-c oder K-d scheitert.

## Ohne Kriterium (Erkundung)
- Hopf-Wert β = 1/√3 in dieser Lesart: Winkel θ, Zahl der gleichwinkligen Zustände auf der Kugel mit diesem Überlapp.
- Für welches β fielen Mischung der zwei Auslesen und Materie-Zustand zusammen?
- Zahlentreffer innerhalb 1 % unter allen Paaren, als Liste ohne Wertung.

## Vorab offengelegt (kein Teil der Vorhersage)
Beim Lesen des Bestands und im Überschlag gesehen:
- θ = 113,35° ist das Supplement des Hopf-Winkels: θ = π − θ_H, denn cos((π − θ_H)/2) = sin(θ_H/2) = β. Das Paar ist (K₁, S). K-a steht damit fest.
- K-b (i) bis (iii) sind Identitäten in β (Additionstheorem der Geschwindigkeiten). K-b steht fest.
- Die gleichgewichtete Mischung zweier reiner Zustände im Bloch-Winkel θ hat die Länge cos(θ/2) = β, nicht 1/γ_L. Gleich wären sie für β³ + β² + β − 1 = 0,
  β = 0,5437. K-c steht als widerlegt fest. Der Materie-Zustand ist der dephasierte Kickzustand (1, β), das ist r27.
- Am Hopf-Wert ist θ = arccos(−1/3) = 109,47°, der Tetraederwinkel; vier Zustände mit paarweisem Überlapp 1/√3 bilden ein Tetraeder (SIC-Messung eines Qubits).
- Zahlentreffer (M, T) in HS(2): 2β²/(1 + β⁴) = 0,5533 gegen 0,5493 (0,7 %), keine Identität.
Offen vor der Rechnung: K-d (Lage der Bilder) und die vollständige Liste der Paare.

## Vorhersage
- K-a: **bestätigt.** K-b: **bestätigt.** K-c: **widerlegt.** K-d: **offen** (Vermutung: widerlegt).
- Gesamt: **trägt teilweise.**

## Grenzen (vorab)
Die Lesart „Hopf-Sphäre = Himmelskugel von Lichtrichtungen“ ist gesetzt. β_sym bleibt Eingabe (OP1); ein bestätigtes Ergebnis leitet seinen Wert nicht her, es
verbindet nur zwei vorhandene Lesarten (Winkel und Geschwindigkeit). Frames: Das Paar (K₁, S) ist nach r24/r61 ein Paar von R-Zuständen. OP1 bis OP5 bleiben offen.
