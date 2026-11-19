# OP5: Welche Energie trägt der erhaltene Ladungsrest?

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/e5e28942502f5862acdfb18c76a861e0a8344ffb/notes/research/op5_bifocal_response_2026_11_18/Wand_Stress_Vorab.md). Fortsetzung der [Expansionsrechnung](Expansion_Leck.md). Untersucht wird der späte nichtrelativistische Wand- und Teilchenbeitrag im bisherigen Kontrollmodell. Gemeinsamer lokaler Ruheschnitt, zwei gleich große Reservoirs, gleiche leichte Ruhemasse auf beiden Seiten, gleiche kinetische Verteilung pro Teilchen. Wandspannung und Teilchenmasse werden unabhängig bewertet. Ein zusätzlicher aus Q gespeister Feld- oder Bindungsbeitrag ist keine Eingabe.

## Eingefrorene Differenz und mittlere Teilchenenergie

V ist das physikalische Volumen jeder Seite, N=N_L+N_R die Gesamtzahl der betrachteten Teilchen, Q=N_L−N_R die komovierende Zahlendifferenz aus der Leckrechnung. Mit Ruhemasse m und gleicher mittlerer kinetischer Energie e_kin je Teilchen gilt

    ρ_part = (m+e_kin) N/(2V),
    ρ_L−ρ_R = (m+e_kin) Q/V.

Im homogen gemittelten Teilchenanteil verschwindet somit jede Abhängigkeit von Q bei festem N und festem kinetischem Profil. Ein eingefrorener Q kann einen lokalen Dichtekontrast tragen, während das Gesamtgewicht durch N bestimmt wird. Diese Aussage setzt gleiche Massen der besetzten leichten Moden und gleiche Energieverteilung pro Teilchen voraus. Energieänderungen durch zusätzliche massive Zustände, durch erneute Thermalisierung, Feld- oder Bindungsenergie sind darin nicht enthalten. Bei kinetischer Entkopplung und V∝a³ trägt die Ruhemasse ρ_m∝a⁻³. Weil die nichtrelativistische kinetische Energie pro Teilchen wie a⁻² abnimmt, skalieren der kinetische Dichtebeitrag und sein Druck wie a⁻⁵. Der asymptotische führende Teil verhält sich wie Staub.

## Lokaler Spannungstensor des Kinks

Für den kanonisch normierten Skalar aus [Domaene.md](Domaene.md), mit Potentialenergie relativ zum gemeinsamen Vakuum, schreibe für eine ebene statische Wand mit Normale n im lokalen orthonormalen Ruhesystem

    ρ_χ = (χ′)²/2 + U(χ),
    p_n = (χ′)²/2 − U(χ),
    p_t = −(χ′)²/2 − U(χ).

Das statische erste Integral und U(±v)=0 liefern (χ′)²/2=U. Somit ist p_n=0 und jeder der beiden Tangentialdrücke ist −ρ_χ. Die Oberfläche trägt nach Integration σ=∫ρ_χ dx=2√(2λ)v³/3, und der räumliche integrierte Tensor ist −σ(δ_ij−n_i n_j). Eine einzelne Wand ist anisotrop. Erst bei einer isotropen flächengewichteten Orientierungsverteilung gilt ⟨n_i n_j⟩=δ_ij/3, also p_W=−2ρ_W/3. Für konstante Eigenwandspannung, vernachlässigbare Wandgeschwindigkeit und komovierende Gesamtfläche folgt ρ_W=σ S_phys/V_phys∝a⁻¹. Dieses Ergebnis entspricht dem [bekannten statischen Wandfluid](https://arxiv.org/abs/gr-qc/0010046). Es setzt keinen dynamisch stabilen Zustand eines realen Wandnetzes voraus.

## Gemeinsame homogene Wirkung

Weil der Druck der Teilchen nichtnegativ und ρ_W positiv ist, liegt w_eff=(p_part−2ρ_W/3)/(ρ_part+ρ_W) stets oberhalb oder auf −2/3. Keine positive Mischung dieser beiden Komponenten hat den Vakuum-Zustandssatz p=−ρ. Im späten nichtrelativistischen Grenzfall, in dem der kinetische Druck vernachlässigt wird, gilt bei Referenzskalenfaktor a₀

    ρ_W/ρ_m = (ρ_W,0/ρ_m,0)(a/a₀)²,
    w_eff = −(2/3) [ρ_W/(ρ_m+ρ_W)].

In einem hypothetisch nur aus diesen zwei Komponenten aufgebauten Hintergrund könnte Wanddominanz die Expansion beschleunigen, denn ρ+3p≈ρ_m−ρ_W. Die Anteilsrelation hängt von der Wanddichte und der Gesamtteilchenzahl am Referenzzeitpunkt ab. Kein festgelegter Materieanteil folgt aus dem eingefrorenen Q. Es ist außerdem keine Ableitung des reinen Casimir-Beitrags, der im separat betrachteten idealen Dilatationsmodell anders skaliert.

## Konsequenz für OP5

Der erhaltene Dipol bzw. die Ladungsdifferenz kann Information über die Verteilung speichern. Im geprüften Tensor trägt diese Differenz bei festem N keinen eigenen homogenen Massenterm. Die Wand liefert negativen Druck, doch ihre Energie verdünnt sich. Für die I3-Lesart müsste eine echte Kopplung vom Überschuss an eine zusätzliche homogene Energie noch hergeleitet werden. H96 bleibt offen.
