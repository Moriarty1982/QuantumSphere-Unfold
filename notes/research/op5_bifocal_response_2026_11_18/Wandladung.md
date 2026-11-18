# OP5: Energie einer besetzten Dirac-Wandmode

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/9d1e2b0ca2b4d8da137fda53ae2e526c7ecffa8b/notes/research/op5_bifocal_response_2026_11_18/Wandladung_Vorab.md). Ergänzung zu [Domaene.md](Domaene.md) und [Wand_Stress.md](Wand_Stress.md). Ein effektives Dirac-Feld mit erhaltener globaler Teilchenladung und vorzeichenwechselnder Masse wird angenommen. Die Prüfung betrachtet den Besetzungsbeitrag relativ zur unbesetzten Wand, ohne Eichfeldenergie, mit festem Wandprofil und bei Temperatur null. Die bisherige Reservoir­differenz Q wird nicht mit der Wandladung gleichgesetzt.

## Die Normalnullmode propagiert entlang der Wand

Mit x als Wandnormale sei H_⊥=−iα_x∂ₓ+βm(x) mit m(x)→±m_∞, m_∞>0. Die Standard-Dirac-Matrizen sind hermitesch und antikommutieren paarweise. Die Nullmode erfüllt ∂ₓψ=−(iα_xβ)mψ. Der Projektor auf den Eigenwert +1 von iα_xβ liefert das beidseitig abklingende Profil exp[−∫₀ˣm(u)du]. Beide Tangentialmatrizen α_y,α_z kommutieren mit iα_xβ. Auf dem normalen Nullraum bleiben sie antikommutierende involutorische Matrizen. Folglich hat die darauf eingeschränkte Wirkung von H_∥=α_y k_y+α_z k_z die Zweige E=±|k_∥|. Die Mode ist normal gebunden und tangential masselos.

## Ladung trägt eine positive Flächenenergie

Für g gleichartige positive Zweige und Dichte n_s=|Q_W|/A in Einheiten einer Einzelladung sei der passende Teilchen- oder Antiteilchenzweig bis k_F gefüllt. In zwei Tangentialdimensionen liefert Zustandszählung in Einheiten ħ=c=1

    n_s = g k_F²/(4π),
    ε_F = g k_F³/(6π) = [4√π/(3√g)] n_s^(3/2).

Dabei ist ε_F Energie pro Fläche. Die Teilchenkomponente hat bei fester Ladung den isotropen Tangentialdruck −∂(A ε_F)/∂A=ε_F/2. Die normale Auflagerung des Gases wird in dieser führenden Dünnwandbeschreibung nicht als eigener Normaldruck behandelt.

Für ein isotrop orientiertes Ensemble komovierender Wände mit erhaltener Ladung je komovierender Wandfläche folgt n_s∝a⁻². Die zusätzliche volumenbezogene Energiedichte ist ε_F S/V∝a⁻⁴. Aus der Mittelung der zwei Tangentialdrücke folgt p_F=ρ_F/3. Die Ladung kann in dieser Belegung somit zur mittleren Energie beitragen. Der Beitrag ist gerade im Ladungsvorzeichen und verhält sich bei komovierender Fläche wie Strahlung. Die nackte Wandspannung trägt weiterhin ihren Beitrag ∝a⁻¹. Wenn die Wandladung aus den Reservoirs stammt, muss der dort entfallende Energiebeitrag für die Gesamtbilanz mitgerechnet werden.

## Geschlossene Wand bei festem Ladungsinhalt

In der führenden Dünnwandnäherung einer großen kugelförmigen Wand mit gleichen inneren und äußeren Vakuumenergien ist A=4πR². Setze C=4√π/(3√g) und nackte positive Flächenspannung σ. Die Energie bei fester Wandladung ist

    E(R)=4πσR² + C|Q_W|^(3/2)/(√(4π) R).

Für Q_W≠0 hat E(R) ein radiales Minimum. Dort gilt ε_F=2σ, die Nettotangentialspannung verschwindet in führender Ordnung, und E″(R)=24πσ>0. Der Fermiimpuls am Minimum ist k_F=(12πσ/g)^(1/3) und unabhängig von Q_W. In dieser Einzweigrechnung ist k_F<m_∞ das führende energetische Kriterium gegen Emission eines Teilchens in das äußere freie Kontinuum. Sind weitere gebundene Zweige unterhalb k_F zugänglich, muss die Besetzung aller dieser Zweige neu bestimmt werden. Für die Anwendung gelten außerdem R viel größer als Wanddicke und k_F R viel größer als eins.

Der optimale Radius wächst wie √|Q_W| und die führende minimale Energie ist E_min=k_F |Q_W|. Damit ist Fragmentation in dieser Ordnung energetisch unentschieden. Ein radiales Minimum beweist weder Formstabilität noch Bildung; die [Fermi-Ball-Literatur](https://arxiv.org/abs/hep-ph/0212332) behandelt dafür Krümmungskorrekturen. Eine Population tatsächlich stabiler kompakter Objekte mit erhaltener komovierender Anzahl, fester Masse und kleinen Schwerpunktsgeschwindigkeiten würde sich im Mittel wie Staub verdünnen. Das ist eine andere Geometrie als die komovierenden ausgedehnten Wandflächen.

## Grenze für OP5

Die Variante liefert eine ausdrücklich ladungsabhängige Energie im Kontrollmodell. Ob und wie der in OP5 betrachtete Überschuss die Dirac-Wandmode besetzt, ob die erforderliche Bindung existiert und ob sich stabile geschlossene Wände bilden, bleibt offen. Eine Λ-Auslese folgt aus keiner der beiden Skalierungen. H96 bleibt offen. Die I3-Lesart lässt sich hier als Trennung zwischen einer möglichen Materiekomponente und der weiterhin offenen Λ-Auslese anwenden.
