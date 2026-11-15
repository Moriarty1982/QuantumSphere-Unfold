# OP3: Das Spin-1-Dreieck und die Suche nach seiner Bezugsrichtung

15. November 2026, Claude Opus. **Erkundung, nicht blind** (Koide 2/3, die Lepton-Phase 2/3 und das Ziel der Suche
waren bekannt). Auftrag des Autors: „ja und weiter, bin gespannt wo das jetzt hinführt“, nach dem Nebenbefund in
`../op3_horizon_shadow_2026_11_15/README.md`. Keine H-Nummer, kein CT-Eintrag, Guards unverändert. Skript
`spin1_triangle.py`, Ausgabe `run/spin1_triangle_stdout.txt`.

## Vorwissen geprüft
- Spin-½-Oktant (r12), gebogene Achsen (r14.5), das Hindernis „Spin ½ gegen Spin 1“
  (`../op3_cs_dixon_map_2026_11_15/README.md`, Lesart): Spin ½ gibt Koide, aber Rang 2; Spin 1 auf orthogonalen Achsen
  gibt Rang 3, aber K = 1/3.
- r33.1: Generationstripel Im H mit A4/2T als Symmetrie; r13.6: Weg B mit K = 1/2.
- Volltextsuche nach spin-1-kohärenten Zuständen: im Repo nicht vorhanden. Die Treffer zu √2 in der Kernkarte betreffen
  die Brannen-Formel.

## Teil A: das Spin-1-Dreieck (exakt)
Drei kohärente Spin-1-Zustände |n_k⟩, symmetrisch um eine Zyklusachse, mit paarweiser Überlappung
|⟨n_k|n_l⟩|² = cos⁴(a/2) = ½:
- Seitenwinkel a mit **cos a = √2 − 1** (65,53°);
- Winkel ψ jeder Richtung zur Zyklusachse mit **cos² ψ = (2√2 − 1)/3** (38,68°);
- Koide K = (1 + 2·½)/3 = 2/3;
- Bargmann-Phase (Ladung 1) **φ = 3·arccos(1 − 1/√2) − π = 0,679042**;
- Gram-Determinante (√2 cos φ − 1)/2 = 0,0503 > 0, also **Rang 3**: drei positive Massen, Wurzel-Verhältnisse
  1 : 16,24 : 65,93.

**Bedeutung:** Eine einzige su(2) mit Spin 1 trägt zugleich Koide 2/3, drei Generationen und einen Zyklus der Ordnung 3.
Das hebt das Hindernis „Spin ½ gegen Spin 1“ auf, sofern die drei Zustände nicht auf orthogonalen Achsen liegen
(die geben K = 1/3), sondern um die Zyklusachse gekippt. Das Dreieck ist ohne jeden Kern schon gebogen (φ < π/4); bis
zur Lepton-Phase 2/3 fehlen 0,012376.

## Teil B: Rückwärtssuche nach der Bezugsrichtung
Kandidatenliste vorab im Skript festgelegt (143 Kandidaten), Toleranz ±0,05°, Zufallserwartung 0,16:
- Gitterrichtungen mit Einträgen in {−2, …, 2}: Achsen, Kantenmitten und Diagonalen von A4/2T, Vorzeichen-Permutationen;
- Δ(96)-Spalten, Fourier ⟨e₀|F|e₀⟩, Überlappung ½, β_sym²;
- Hopf-Winkel θ_H und θ_H/2, arctan und arccos von β_sym;
- π/12, π/6, π/4, 2/3 rad, 2/9 rad, γ_M rad, der magische Winkel und der halbe Spin-1-Seitenwinkel.

**Ergebnis: kein Treffer.** Am nächsten liegen 2/3 rad (38,20°, −0,48°) und die Gitterrichtung (2, 1, 0) (39,23°,
+0,56°). Native A4-Richtungen geben K = 1/2 (Achsen) oder K ≈ 0,708 (Kantenmitten).

## Was daraus folgt
- **Die Richtung ist keine unabhängige Größe.** cos² ψ = (2√2 − 1)/3 folgt allein aus der Überlappung ½. Eine native
  Richtung bei 38,68° zu finden, wäre dasselbe wie die Koide-Überlappung ½ herzuleiten. Die Suche führt also auf die
  Kernfrage von Koide zurück, nur in Spin-1-Geometrie.
- **Gleichwertige, einheitliche Form:** Überlappung ½ heißt in jeder Darstellung Fubini–Study-Abstand π/4, also genau
  die Hälfte des größten Abstands (π/2 für orthogonale Zustände). Koide verlangt drei Zustände, die paarweise *genau auf
  halbem Weg zwischen gleich und orthogonal* liegen. Die Spin-Zahl entscheidet nur, wie diese Lage im Raum aussieht:
  Oktant bei Spin ½ (Rang 2), gekipptes Dreieck bei Spin 1 (Rang 3).
- **Der Gewinn des Spin-1-Bildes:** Es braucht für Rang 3 keinen Kern und keinen Fluss. Ein Kern wäre nur noch für den
  Rest von 0,012376 nötig (etwa 1,8 % der Phase). Dieser Rest ist nicht erklärt. Ihn mit Schatten, Strahlungskorrektur oder
  Laufen der Massen zu deuten, wäre mit bekanntem Ziel; ein Test ginge nur mit Vorab-Notiz und einem Mechanismus, der
  die Größe vor der Rechnung festlegt.
- **Offen wie zuvor:** Ladungsneutralität (das Im-H-Tripel bricht Q_em nach r33) und die Überlappung ½ selbst.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.
