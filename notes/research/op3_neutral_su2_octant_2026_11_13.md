# Erkundung: Oktant in einer neutralen SU(2) (Sumino) und die Rolle von Spin 1/2

13. November 2026, spät. Autorenauftrag: „aufräumen, dann weitersuchen“. Weitergesucht wurde beim offenen Hindernis
der Oktanten-Lesart: Im Isospinfaktor bricht sie die Ladung (r33), im Oktonionenfaktor die Farbe, im neutralen
Dixon-Teil verhindert die Signatur (2,1) den exakten Oktanten (`op3_hopf_octant_2026_11_13.md`). Erkundung, nicht
blind, kein Datenvergleich. Keine H-Nummer, kein MMA-Beleg, keine Änderung offener Guards. Einordnung T5/T8, OP3.
Skript `op3_neutral_su2_octant_2026_11_13.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- `op3_eta_form_search_2026_11_13.md` (Oktanten-Tripel der Qubits: ρ² = 1/2, Rang 2, π/4), `op3_hopf_octant_2026_11_13.md`
  (Orte und Hindernisse), `op3_slot_u3_gauging_2026_11_13.md` (Platzindex-U(3), Sumino-Abgleich).
- r33 (i, j, k als Labels im Isospinfaktor nicht Q_em-invariant), Gram-Notiz (Hopf-Träger K ≤ 1/2).
- Sumino, arXiv:0812.2103, Abschnitte 2 und 5 (nachgelesen): Φ transformiert unter U(3) × SU(2) als Φ → U Φ Oᵀ mit
  O ∈ SO(3). Die SU(2) wird geeicht und bei hoher Skala gebrochen; sie ist farb- und ladungsneutral. Die Massenmatrix
  ist ψ̄_L Φ Φᵀ e_R; im Vakuum ist Φ diagonal, die drei Generationen sitzen also auf drei orthogonalen Achsen des
  SO(3)-Vektorindex. Suminos „Vereinigung mit SU(2)_L“ bei 10²–10³ TeV ist eine Gleichheit der Kopplungen, kein
  gemeinsamer Gruppenschritt.

## Ergebnis

**1. Der Oktant ist in Suminos Vakuum schon angelegt.** Die drei Generationen stehen auf drei orthogonalen Achsen einer
neutralen SO(3). Ein Oktanten-Tripel in dieser Gruppe bricht weder Ladung noch Farbe; das Hindernis aus r33 entfällt,
wenn das Qubit zu dieser SU(2) gehört statt zum Isospin.

**2. Nur Spin 1/2 gibt Koide und π/4.** Für Zustände höchsten Gewichts mit Spin j entlang x, y, z (numerisch exakt):

| j | Treue = (1/2)^{2j} | ρ² | K | Bargmann-Phase j · π/2 |
|---|---|---|---|---|
| 1/2 | 0,5 | 0,5 | **2/3** | **π/4** |
| 1 | 0,25 | 0,25 | 1/2 | π/2 |
| 3/2 | 0,125 | 0,125 | 5/12 | 3π/4 |
| 2 | 0,0625 | 0,0625 | 3/8 | π |

Die reellen SO(3)-Vektoren selbst (Suminos zweiter Index) sind orthogonal: Überlappung 0, keine Phase. Koide
(ρ² = 1/2) und die Verschiebung π/4 gehören also zusammen zu Spin 1/2 an drei orthogonalen Achsen. Nebenbefund:
j = 1 gibt K = 1/2, den Wert, den die Gram-Notiz für den Hopf-Träger und das Tensorprodukt fand.

**3. Lesart.** H99 hieße dann: Die Neutrinos tragen gegenüber den geladenen Leptonen die Phase eines Spin-1/2-Objekts
der neutralen Familien-SU(2), dessen Richtung an den drei Generationen auf Suminos orthogonalen Achsen steht. Die
geladenen Leptonen koppeln über den Vektorindex (keine Phase aus dieser Gruppe), die Neutrinos über einen Spinor.

## Bewertung
- Ein farb- und ladungsneutraler Ort für das Oktanten-Tripel ist gefunden, aber nicht im Companion, sondern in Suminos
  Modell (neutrale SU(2) mit SO(3)-Vektorindex). Dort ist er durch das Vakuum vorgegeben.
- Spin 1/2 ist ausgezeichnet: Nur er verbindet Koide-Überlappung und Phase π/4.
- Nicht gezeigt: dass ein Feld des Neutrino-Sektors ein Spinor dieser SU(2) ist und die geladenen Leptonen nicht; dass
  der Companion eine solche neutrale SU(2) enthält. Gesichtete Kandidaten im Companion tragen Ladung (Isospin, r33),
  Farbe (quaternionische Unteralgebren der Oktonionen) oder brechen die Isotropie (räumliche Drehungen).
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert; H100 unberührt.

## Nächste Fragen
- Hat der Companion eine neutrale SU(2), deren Vektorindex die Generationen trägt (etwa ein zweiter Quaternionenfaktor
  oder der Platzindex selbst, als SO(3) ⊂ U(3))? Suminos SU(2)_V ⊂ U(3) × SU(2) wirkt als 3 auf (Φ_2, Φ_5, Φ_7).
- Welches Neutrino-Feld könnte deren Spinor sein (ν^c aus r44.1(d))?
