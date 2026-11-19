# OP5: Biegebeitrag aus der endlichen Fermionbreite

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/c7beac553d17a71869042276bd891781a534e819/notes/research/op5_bifocal_response_2026_11_18/Fermion_Biegung_Vorab.md). Fortsetzung von [Wandform.md](Wandform.md). Lokale adiabatische Einzelbandprojektion auf die festgehaltene ebene Dirac-Nullmode. Das Modell hält auch das skalare Wandprofil fest. Langsame Krümmungsvariation, kleine Wandbreite gegenüber beiden Krümmungsradien, keine Eichfeldenergie und keine Vakuumenergie der Fermionen.

## Projektion der Tangentialkinetik

Seien k₁,k₂ die lokalen Hauptkrümmungen und s der Normalabstand. In Hauptkrümmungsrichtung i ist der Tangentialskalenfaktor der parallelen Fläche 1+s kᵢ. Man arbeitet mit dem Normalspinor in flacher Normalmaß-Normierung, d. h. mit dem durch J^(1/2) reskalierten Spinor für J=(1+s k₁)(1+s k₂). Die führenden Tangentialableitungen im lokalen Hauptsymbol tragen dann das inverse Skalenmaß (1+s kᵢ)⁻¹. Ableitungen der Krümmung und Verbindungsterme sind in dieser Projektion keine Eingabe.

Für das gerade, normierte ebene Normalprofil |f(s)|² und dessen Varianz μ₂=∫s²|f(s)|²ds ergibt der projizierte Geschwindigkeitsfaktor

    vᵢ = ⟨(1+s kᵢ)⁻¹⟩ = 1 + μ₂ kᵢ² + O(kᵢ⁴).

Die Mittelung ist als lokale Entwicklung im regulären Normalenschlauch zu verstehen. Der lineare Term verschwindet wegen der geraden Dichte. Für den exakt lösbaren Kink m(s)=M tanh(Ms) gilt |f|²=(M/2)sech²(Ms) und μ₂=π²/(12M²). Dies folgt etwa aus der zweiten Ableitung der charakteristischen Funktion [(π t)/(2M)]/sinh[(π t)/(2M)] bei t=0.

Für E(p)=√[(v₁p₁)²+(v₂p₂)²] wird die besetzte Impulsfläche durch qᵢ=vᵢpᵢ auf einen Kreis abgebildet. Bei fester Teilchenzahl pro Fläche n_s ist der neue Fermiimpuls im q-Raum gegenüber dem ebenen Wert um √(v₁v₂) erhöht. Die Energie pro Fläche ist damit ebenfalls um diesen Faktor erhöht. Schreibe ε_F für die ebene Flächenenergie bei n_s und H=(k₁+k₂)/2, K=k₁k₂. Die lokale Korrektur lautet

    Δε = (ε_F μ₂/2)(k₁²+k₂²)
        = (ε_F μ₂/2)(2H)² − ε_F μ₂ K.

In der Konvention aus Wandform.md ist dieser einzelne Beitrag κ_F=ε_F μ₂>0 und κ_G,F=−ε_F μ₂. An der führenden radialen Gleichgewichtsfläche gilt ε_F=2σ. Für die quadratische Energie einer kleinen Formstörung am flächenoptimierten Hintergrund genügt es, diese Koeffizienten bei der ungestörten Flächendichte auszuwerten. Bei festem N verschiebt die Krümmung die optimale lokale Dichte erst in der nächsten Ordnung der Entwicklung.

## Unabhängige Zylinderkontrolle der Projektion

Für M=1, k₁=1/R, k₂=0 wurde v₁ direkt auf |s|≤R/2 über die symmetrisierte Funktion 1/[1−(s/R)²] integriert, mit derselben Schlauchnormierung im Nenner. Die Mittelpunktsumme nutzte 65.536 Intervalle auf der positiven Hälfte. Die Tabelle zeigt den Faktor F=√v₁ für die Fermi-Energie und seine skalierte Abweichung.

| R | F | R²(F−1) |
|---:|---:|---:|
| 10 | 1.0042384051 | 0.423840513 |
| 20 | 1.0010366039 | 0.414641565 |
| 40 | 1.0002575454 | 0.412072666 |

Halbe Auflösung änderte F um höchstens 4,4·10⁻¹⁴. Der skalierte Faktor nähert sich π²/24≈0,411234. Die endliche Begrenzung des Normalenschlauchs ändert bei wachsendem R die asymptotischen Potenzkoeffizienten nicht.

## Einordnung

Die Breite der Normalmode liefert in der gewählten Projektion einen positiven Beitrag zur lokalen Rückstellenergie der Kugel. Die Projektion berechnet weder die Mischung mit anderen Normalmoden noch die Eigenwertkorrekturen der intrinsischen Dirac-Kinetik auf geschlossenen Flächen oder die Relaxation des skalaren Profils. Beiträge derselben Krümmungsordnung können dadurch fehlen. Das Vorzeichen des gesamten κ und die Kosten der Fragmentation sind folglich offen. [Ogure et al.](https://arxiv.org/abs/hep-ph/0212332) berücksichtigen endliche Fermionbreite in einer weitergehenden mikroskopischen Rechnung für ein verwandtes Modell. H96 bleibt offen.
