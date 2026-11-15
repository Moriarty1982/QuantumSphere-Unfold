# OP3: Die dritte Lorentz-Invariante w und die invariante Matrix S

15. November 2026, Claude Opus. **Erkundung, nicht blind** (die Aussagen (1)–(3) standen analytisch vorher fest). Auftrag
des Autors: „Erkundung, dann H105“, nach dem Befund, dass das Dublett χ = (√s₊, √s₋) aus
`../op3_helicity_axis_2026_11_15/README.md` (r16.3) nicht der vollständige invariante Inhalt eines Feldes ist. Keine
H-Nummer, kein CT-Eintrag, Guards unverändert. Skript `third_invariant.py`, Ausgabe `run/third_invariant_stdout.txt`.

## Vorwissen geprüft
- v4.8.0-r06.3: Bahnen von SO(3, ℂ) sind die Niveaumengen von s = z·z.
- v4.9.0-r05.2(b): Matrix der Zeitmittel Ĝ = F̂†F̂ (Hermitesch), σ_y-Teil = Helizität.
- r16.3, r16.4, r16.7 (Runde r16, Zweig `research/op3-cycle-search`): Dublett χ, Feldvorzeichen, Oktant aus den sechs
  Polen; Aussage r16.4(c) über lineare Feldabbildungen.
- r14.5: Die Biegung von π/4 auf φ = 2/3 verlangt, das Qubit nach ℂ³ zu verlassen.
- Volltextsuche nach Takagi und nach einer dritten bzw. zeitgemittelten Invariante: im Repo nur r05.2(b), nichts zu
  F₊·F̄₋.

## Ergebnisse
1. **Sechs reelle Invarianten.** Ein zeitharmonisches Feld mit komplexen Amplituden hat 12 reelle Freiheitsgrade; die
   generischen Lorentz-Bahnen sind 6-dimensional. Die Invarianten sind Real- und Imaginärteil von
   s₊ = F₊·F₊, s₋ = F₋·F₋ und **w = F₊·F̄₋** (unter 400 Boosts erhalten bis 10⁻¹⁴). F₊·F₋ ist nicht invariant; das war der
   Term in r16.4(c), dessen invarianter Partner w dort übersehen wurde. Die Aussage von r16.4(c) über lineare Abbildungen
   bleibt richtig.
2. **Bedeutung.** Die augenblickliche Invariante s(t) = (E(t) + iB(t))² zerfällt exakt in
   s(t) = ¼ [s₊ e^{−2iωt} + 2w + s̄₋ e^{2iωt}].
   w ist der Mittelwert von s(t) (also von E² − B² und E·B), s₊ und s̄₋ sind die bei ∓2ω schwingenden Anteile.
3. **Die invariante Matrix S.** Mit Φ = [F₊, F̄₋] (3×2) ist S = ΦᵀΦ = [[s₊, w], [w, s̄₋]] komplex symmetrisch; unter Boosts
   geht Φ in MΦ über (M ∈ SO(3, ℂ)), S bleibt erhalten. S ist ein Element von Sym²(ℂ²), also ein **Spin-1-Objekt** über dem
   Dublett (F₊, F̄₋). Es gilt:
   - die Zeitverschiebung wirkt als U S U mit U = diag(e^{−iτ}, e^{iτ}): Gewichte −1, 0, +1 auf s₊, w, s̄₋;
   - die Dualitätsdrehung ist auf S ein Skalar (e^{−2iα});
   - R wirkt als −1, T als S ↦ X S̄ X (antilinear, tauscht s₊ und s̄₋), J_B als −X S̄ X.
4. **Die sechs Pole haben Rang 1.** Materie, Tachyon und die beiden Photonseiten haben S ∝ [[1, 1], [1, 1]] und sind als
   Strahlen von S **dieselben**; das selbstduale und das antiselbstduale Feld haben S = diag(−4, 0) bzw. diag(0, −4). Die
   Unterscheidung von Materie, Tachyon und Seite steckt nur in den Wurzeln, also in χ. Allgemeine komplexe Felder haben
   Rang 2 (Takagi-Verhältnis σ₂/σ₁ im Mittel 0,31).

## Folgerungen
- **Kohärenter Sektor = χ.** Rang-1-Matrizen S = ψψᵀ entsprechen genau den Dubletts ψ; das sind die kohärenten
  Spin-1-Zustände. Das Oktant aus r16.7 liegt ganz in diesem Sektor.
- **Platz für die Biegung, aber keine Größe.** Die dritte Richtung, die die Biegung nach r14.5 braucht, hat das Feld: Sie
  ist der Rang-2-Anteil von S (σ₂ > 0), also Felder, deren Mittelwert-Invariante w nicht durch s₊ und s₋ festgelegt ist. Wie
  weit die Auslesungen den kohärenten Sektor verlassen, legt die Feldstruktur aber nicht fest: σ₂/σ₁ ist ein freier
  Parameter jedes Feldes. Die Größe der Biegung bleibt damit beim Kern (γ_M, OP1).
- **Zeitverschiebung als Spin-1-Achse.** Die Achse, um die die Zeitverschiebung dreht, hat als Pole die reinen Anteile
  F̄₋ = 0 bzw. F₊ = 0, also selbst- und antiselbstduale Felder: Sie ist die Helizitätsachse. Das Spin-1-Dreieck aus r15.3
  ließe sich um diese Achse nativ legen. Seine Überlappung ½ (Spin 1) ist aber eine andere Bedingung als die
  Spin-½-Überlappung ½ des Oktanten aus r16.7; beide zugleich gelten nicht.

## Zu H105
Eine Vorab-Notiz verlangt eine Konstruktion, die vor der Rechnung ohne freie Wahl feststeht. Die Erkundung zeigt:
- Die linearen Größen (S, auch mit dem Skalarprodukt aus Parseval oder dem Hilbert–Schmidt-Produkt auf Sym²) unterscheiden
  Materie, Tachyon und die Seiten nicht; mit ihnen ist das Oktant von r16.7 gar nicht darstellbar.
- Die Wurzelgrößen (χ) geben das Oktant, aber exakt flach (π/4).
- Die Biegung hängt an σ₂/σ₁, und dafür liefert der Bestand keinen Wert.

Jede Vorab-Notiz müsste also einen Wert oder eine Wahl für die Biegung setzen; getestet würde diese Wahl, nicht die
Struktur. Bei bekanntem Ziel 2/3 wäre das nahe am Zahlenfischen. **H105 ist deshalb nicht vergeben.** Sinnvoll wäre ein
Test erst mit einem Prinzip, das σ₂/σ₁ (oder den Kern) vor der Rechnung festlegt.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.
