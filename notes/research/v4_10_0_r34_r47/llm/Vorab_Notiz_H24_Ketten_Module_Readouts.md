# Vorab-Notiz H24: Generationenketten verschiedener Länge unter Hilbert-Shift-Zoom und gemischten Readouts

Festgelegt am 2026-10-23, **vor** der Rechnung. Autoridee (2026-10-23): Die gemischten Readouts waren dafür gedacht, dass die
Generationen bei oft genug wiederholtem Zoom einen Kreis bilden; interessant wäre, was bei verschiedenen Moduln passiert, also bei
unterschiedlich langen Generationenketten, aus denen sich verschiedene Lesarten ergeben könnten. Bezug: H22e (S₃ × D₄, Perioden
{1, 2, 3, 4, 6, 12}), H23 (Frames und Generationen brauchen verschiedene Ebenen), `def:qam-hilbert-shift-plan`
(H_QAM: Etikett i ↦ i + 1), `def:binary-mask-registry-mixed-readouts` (Bits β_j = 2^j, Maske = ODER), HS(n) mit C_n = 2^n Kanälen.

## Rahmen (Modellwahl, offen gelegt)

- Eine **Kette** der Länge m ist die zyklische Gruppe ⟨g⟩, ord g = m; ein Schritt der Selbstdurchwanderung ist g.
- **Readout der Stufe j** (Bit β_j = 2^j) sieht die Kette in Schritten von 2^j, also ⟨g^{2^j}⟩. Sichtbare Länge ℓ_j = ord(g^{2^j}).
- **Gemischte Maske** S ⊂ {0, 1, …} mit k = Σ_{j∈S} 2^j, zwei Lesarten der Aggregation μ:
  (Σ) die Maske wirkt als ein Schritt k: ⟨g^k⟩; (∨) die Maske sieht alle Komponenten gemeinsam: ⟨g^{2^j} : j ∈ S⟩.
- Auf der Struktur aus H22e: G = ⟨τ, ρ, T, R⟩ ≅ S₃ × D₄ auf ℂ ⊗ 𝕆³.

## Hypothesen

- **H24a (ungerade Ketten überleben):** Für ungerades m ist ℓ_j = m für alle j. Für m = 3, g = τ gilt τ^{2^j} = τ für gerades j und
  τ^{2^j} = τ⁻¹ = ρτρ für ungerades j: Der Generationenkreis bleibt auf jeder Stufe vollständig, seine Orientierung wechselt mit der
  Parität von j, und die umgekehrte Orientierung ist das ρ-Spiegelbild (Frame-Spiegelung aus H23).
- **H24b (Zweierketten sterben aus):** Für m = 2^a ist ℓ_j = 2^{a−j} für j < a und 1 für j ≥ a. In G: Die Menge der Ordnungen
  {ord(g^{2^j}) : g ∈ G} ist {1, 2, 3, 4, 6, 12} für j = 0, {1, 2, 3, 6} für j = 1 und {1, 3} für alle j ≥ 2; für j ≥ 2 liegt jedes
  g^{2^j} in ⟨τ⟩ × {1}. Ab Stufe 2 bleibt von der ganzen Struktur nur der Triality-Kreis sichtbar, Frame-Wechsel und Dualitätsdrehung
  verschwinden.
- **H24c (gemischte Masken, m = 3):** In der Lesart (Σ) sieht die Maske eine Generation, wenn 3 | k (etwa S = {0, 1}, k = 3), sonst drei;
  in der Lesart (∨) sieht jede nichtleere Maske drei Generationen. Für alle 2^C − 1 nichtleeren Masken über C = 6 Bits (HS(6)-Leiter bis
  2⁵) gilt: Anzahl der Masken mit 3 | k ist 21.
- **H24d (allgemeine Länge m):** (Σ) ℓ = m / gcd(m, k); (∨) ℓ = m / gcd(m, 2^{min S}). In der Lesart (∨) ist der ungerade Anteil von m
  unter jedem Readout unverändert, nur der Zweieranteil kann durch Zoom verschwinden. Geprüft für alle m ≤ 64 und alle Masken über
  6 Bits.
- **H24e (Ebenen):** Für j = 0 sind in G Frames (Ordnung 2, 4) und Generationen (Ordnung 3) zugleich sichtbar; für j ≥ 2 nur die
  Generationen. Die in H23 offene Trennung „Frames und Generationen auf verschiedenen Ebenen“ ist damit im Modell die Trennung nach
  Zoomstufe.

## Entscheidungskriterium (verbindlich)

Jede Hypothese bestätigt oder widerlegt nach der wörtlichen Aussage (exakte Ganzzahl- bzw. Matrixrechnung, Toleranz 10⁻⁹). Einordnung
vorab: Die Aussagen sind **elementare Zahlentheorie** über zyklische Gruppen; ihr Gehalt liegt allein in der Modellwahl (Zoom = Schritt
2^j, Maske = Σ oder ∨). Sie zeigen, was verschiedene Moduln im Modell bewirken, und erklären nichts über die Natur. Insbesondere
entsteht in G keine Kette der Länge 4 oder mehr für Generationen: Die Generationenlänge ist durch die Gruppe auf 1, 2, 3 begrenzt.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
