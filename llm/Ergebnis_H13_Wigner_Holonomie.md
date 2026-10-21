# Ergebnis H13: Auslesefaktor als Wigner-Holonomie

Vorab-Notiz `llm/Vorab_Notiz_H13_Wigner_Holonomie.md` (Commit 645295f), Skript `llm/k35_test_h13.py`.
Gerechnet am 2026-10-21 nach dem Commit der Notiz, Verfahren 1–4 unverändert.

## Werte

| Größe | Wert |
|---|---|
| Rapidität je Frame η_H | 0,658479 (Geschwindigkeit 1/√3) |
| Boostanteil der Holonomie | 2,6 · 10⁻¹⁶ (reine Rotation, wie gefordert) |
| Wigner-Winkel δ | 0,49853 rad = 28,56° |
| Gegenprobe: Fläche des hyperbolischen Dreiecks | 0,49853 rad (Seitenlänge 1,1588, Innenwinkel 50,48°) |
| **f₁₃ = cos δ** | **0,8783** |
| f(+) aus K39 | 0,9436 ± 0,0083 |
| z | **−7,9** |

## Urteil

Nach dem festgelegten Kriterium (|z| ≥ 3) **widerlegt für diese Konstruktion**. Die Wigner-Holonomie der
Triolen-Schleife ist rund dreimal zu groß für den gesuchten Faktor (1 − cos δ = 0,122 gegen 1 − f(+) = 0,056).

Die Notiz legt fest: Die Holonomie-Route mit Triolen-Boosts gilt damit für f(+) als geschlossen. Andere Konstruktionen
(andere Rapidität, andere Vergleichsgröße, andere Richtungen) wurden nicht gerechnet und bräuchten eine eigene Notiz.
Weil f(+) selbst nur eine Anpassung ist (K39), schließt das Ergebnis eine Erklärung des Faktors aus, nicht den Faktor.

## Nebenbefund (M, unabhängig vom Urteil)

Die Gegenprobe bestätigt die Rechnung: Für drei Materie-Frames mit Geschwindigkeit 1/√3 in Triolen-Richtungen ist die
Holonomie eine reine Rotation um 28,56°, gleich dem Winkeldefekt des gleichseitigen hyperbolischen Dreiecks. Das ist
eine parameterfreie Größe der Hopf-Starteinstellung; eine Deutung hat sie nicht.

## Nachbefund (nicht registriert, zählt nicht)

Nach dem Ergebnis gefragt: Was liefert der halbe Winkel? Festgehalten, weil die Hälfte eine Herkunft im Text hat; als
Beleg zählt nichts davon, und H13 bleibt widerlegt.

| Kandidat (nachträglich) | f | z gegen f(+) |
|---|---:|---:|
| cos δ (registriert) | 0,878 | −7,9 |
| **cos²(δ/2) = (1 + cos δ)/2** | **0,939** | **−0,5** |
| cos(δ/2) | 0,969 | +3,1 |
| 1 − δ/2π | 0,921 | −2,8 |

Einer von vier naheliegenden Kandidaten trifft innerhalb von 1σ, etwa die Zufallsquote.

**Herkunft der Bestandteile.**
1. *Halber Winkel — aus dem Text erzwungen, wenn der Spinor ausgelesen wird.* r06.4: z(ψ) ist quadratisch in ψ ∈ ℂ²,
   SL(2,ℂ) auf ψ erzeugt SO(3,ℂ) auf z (K2.2: ψ als Qubit). Eine Drehung der Frames um δ dreht ψ um δ/2.
2. *Quadrat — Born-Regel, eine Deutung.* |⟨ψ|U(δ)ψ⟩|²; das Dokument liest Wahrscheinlichkeiten als Quadrate
   (Ω_M = tanh²η, Ω_Λ = sech²η, r18 (c)). Die Amplitude cos(δ/2) allein verfehlt mit +3,1σ.
3. *Ausrichtung — eine Wahl.* |⟨ψ|Uψ⟩|² = cos²(δ/2) + sin²(δ/2)·cos²θ, θ = Winkel zur Drehachse. Die Achse der
   Holonomie steht senkrecht auf der Triolenebene. Spinor längs der Achse: 1 (nur Phase δ/2 = 14,28°); in der Ebene:
   cos²(δ/2) = 0,939; gemittelt über alle Richtungen: 0,959.

**Strukturbefund dabei (M, nachgerechnet).** Das Triolen-Photon c(1, ω, ω²) ist ein Nullfeld (E·B = 0, |E| = |B|), und
E × B zeigt entlang (1,1,1), der Normalen der Triolenebene z₁ + z₂ + z₃ = 0. Sein Spinor liegt auf der Drehachse und
erfährt nur die Phase δ/2, keine Abschwächung. cos²(δ/2) entsteht für einen Spinor in der Ebene, etwa die Helizität eines
Materie-Frames, der sich in Triolen-Richtung bewegt.

**Lesart (V).** Materie-Lesungen werden um cos²(δ/2) abgeschwächt, das Photon erhält nur eine geometrische Phase δ/2;
das passt zu K39 (Faktor nur auf Materie-Lesungen), ist aber nachträglich zusammengesetzt. Mit f = cos²(δ/2) bildet die
Hopf-Starteinstellung auf β = 0,5500 ab (β_sym 0,5493, 0,12 %) und γ_L = 1,8675 (LQG-Verhältnis 1,8644, 0,16 %) —
Kategorie wie P3 (Koinzidenz, bis ein Test besteht). Vorhersage für sin²θ₁₂ (0,3094) von H9 (0,3086) nicht trennbar.

**Zweite Lesart derselben Formel.** (1 + cos δ)/2 ist auch das gleichgewichtete Mittel aus unverändert und
transportiert (zwei Blätter, r19.2); für 50/50 gibt es keinen Grund.

**Was vorab festzulegen wäre.** Die Lesart sagt für das Photon eine reine Phase δ/2 = 14,28° ohne Abschwächung voraus.
Ob und wo eine solche Phase im Dokument oder in Daten vorkommt, wäre vor dem Nachsehen als Notiz festzulegen.
