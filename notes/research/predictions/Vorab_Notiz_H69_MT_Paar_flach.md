# Vorab-Notiz H69: Ein versetztes M–T-Paar in W1 im flachen Raum (Strom und Energie-Impuls)

**Geschrieben und committet am 5. November 2026 vor der Rechnung. Status: vorregistriert.**

## Vorwissen geprüft
Suchbegriffe in `llm/Ergebnis_*`, `Erkundung_*`, `Vorab_Notiz_*`, `analysis/OP5_*`, `analysis/HC_*`, `notes/research/predictions/`: „negative norm / ghost / Schwebung / beat / gegenläufig / frame offset / Frame-Versatz / time offset / Zeitversatz / desynchron“.
- `Erkundung_MT_Luecke.md` (k174 und die Nachträge 1–2): T-Strom = Λ(iπ) j_M; die K-Bedingung lautet j_M + j_T = 0; bei Versatz δ ist der Querstrom antiperiodisch. Der Vorschlag für H69 stammt von dort.
- `analysis/OP5_Neutral_Pair_Dynamics_Result.md` §3–4:
  - Neutralität und Shift-Symmetrie legen die absolute Vakuumhöhe nicht fest, eine Konstante C bleibt frei.
  - „Der bilineare Vorzeichenwechsel z → iz ist keine negative statistische Gewichtung“: Entgegengesetzte Determinantengewichte brauchen begründeten Feldinhalt und ein Maß. Daraus folgen die Grenzen unten.
- `Ergebnis_H48_Einfrieren_beta.md`: eingefrorene Länge hängt an der Expansionsgeschichte; anderer Mechanismus.
- Keine frühere Prüfung eines M–T-Paares mit Versatz in einer Weyl-Wirkung gefunden.

## Aufbau (k175)
- Flacher Raum, A = 0 (U(1) abgeschaltet), keine Torsion (konsistent, falls j_gesamt = 0, k173). Linkshändige Weyl-Gleichung σ̄^μ∂_μψ = 0 mit σ̄ = (1, −σ_i).
- Materie: ψ_M = a·e^{−iω₁(t − z)} u₁ + b·e^{−iω₂(t + z)} u₂. Die Spinoren u₁, u₂ sind so gewählt, dass jede Welle die Weyl-Gleichung löst (gegenläufige Wellen entlang n = z).
- Tachyon-Anteil nach Konvention F: ψ_T(x) = −iσ_z ψ_M(x + δ·e_t), mit Kinetikvorzeichen s_T = −1 (F3, Gewicht 1). **Das ist eine Eingabe**, siehe Grenzen.
- Ströme j = ψ†σ̄ψ; Bedingung K: j(ψ_M) + s_T·j(ψ_T) = 0.
- Energie-Impuls (symmetrisch): T_μν = (i/4)[ψ†σ̄_μ∂_νψ + ψ†σ̄_ν∂_μψ − c.c.]; gesamt T^M + s_T·T^T.
- Prüfung auf einem Raster von 400 Punkten (t, x, y, z), Parameter a, b, ω₁, ω₂ zufällig.

## Was vorab analytisch bekannt ist (offen gelegt)
- Querstrom: Der Kreuzterm der beiden Wellen oszilliert mit e^{−i(ω₁ − ω₂)t}. Die Bedingung K verlangt (ω₁ − ω₂)δ ≡ π (mod 2π); die Längsanteile sind konstant und heben sich ab.
- Energie-Impuls: Die Diagonalanteile jeder Welle heben sich gegen den T-Anteil ab (T^T = −T^M für Nullvektoren k_μk_ν unter Λ(iπ)⊗Λ(iπ) mit s_T = −1). Die Kreuzterme sind **nicht** vorab berechnet.

## Hypothese H69
- **H69a (Strom):** Mit a, b ≠ 0 gilt j_M + j_T = 0 auf dem ganzen Raster genau dann, wenn (ω₁ − ω₂)δ ≡ π (mod 2π). Geprüft bei Δωδ = π (Erwartung ≤ 1e-12 relativ) sowie Δωδ = 0 und π/2 (Erwartung ≥ 0,1 relativ zur Querstrom-Amplitude).
- **H69b (Energie-Impuls):** Bei Δωδ = π verschwindet T^M + s_T T^T auf dem ganzen Raster, relativ zu |T^M|.
- **Folge, falls a und b gelten:** Das Paar löst W1 mit Re- und Im-Gleichungen im flachen Raum mit G = 0, Torsion 0 und A = 0. Es wäre ein M–T-Paar ohne Nettostrom und ohne Nettoenergie. Scheitert b, wird der Rest T^M + s_T T^T berichtet; er wäre eine Quelle von Krümmung.

## Kontrollen (Gültigkeit)
- ψ_M und ψ_T lösen die Weyl-Gleichung, Residuum ≤ 1e-12 (analytische Ableitung).
- Ein-Frame-Kontrolle: Ohne T-Anteil ist j ≠ 0 (j⁰ = |ψ|² > 0).
- Symmetrie: T_μν = T_νμ, und ∂^μT^M_μν = 0 auf der Lösung (Differenzen mit Schritt 1e-4, relativ ≤ 1e-6).

## Entscheidung (je Teil)
| Ergebnis | Bedingung |
|---|---|
| bestätigt | relatives Residuum ≤ 1e-12 (a: bei Δωδ = π; zusätzlich ≥ 0,1 bei 0 und π/2) |
| widerlegt | relatives Residuum ≥ 1e-3 bei Δωδ = π (a bzw. b), oder bei a ein Verschwinden auch für Δωδ = 0 oder π/2 |
| unentschieden | dazwischen |
| ungültig | eine Kontrolle verfehlt |

## Grenzen (vorab)
- Rein klassisch. Über die Quanten-Vakuumenergie wird nichts gesagt; ein Λ-Term bleibt nach Entscheidung 3 von Hand weggelassen, also bleibt die freie Konstante C aus `OP5_Neutral_Pair_Dynamics_Result` unberührt.
- s_T = −1 ist eine Eingabe aus F3, keine Herleitung. Nach dem Vorbefund folgt ein solches Vorzeichen nicht aus dem Frame-Etikett allein; es bedeutet einen Feldinhalt negativer Norm, dessen Zulässigkeit offen ist.
- Die Kopplung des Versatzes an die Expansion, δ(a), ist hier **nicht** getestet. Sie braucht einen gekrümmten Hintergrund und kommt als eigene Vorab-Notiz (H70).
