# OP5: Wanddurchlass in einem expandierenden Hintergrund

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/4c47fffd1c0474f73f9b4739ca9c58c107a521df/notes/research/op5_bifocal_response_2026_11_18/Expansion_Leck_Vorab.md). Fortsetzung von [Thermisches_Leck.md](Thermisches_Leck.md) und [Ausfrieren.md](Ausfrieren.md). Betrachtet werden zwei gleich große komovierende Reservoirs mit einer gemeinsamen komovierenden ebenen Wand. Der flache FRW-Hintergrund ist vorgegeben. Die Wand ist lokal quasistatisch, die Eigenmassen m<M und der kleine Mischwinkel 0<θ<π/2 sind fest. Für die Teilchen wird ein auf beiden Seiten gleiches, homogenes isotropes nichtrelativistisches Impulsprofil pro Teilchen angesetzt. Es handelt sich um einen Abschluss auf Ebene der Teilchenzahlen. Homogenität nach wiederholter Streuung folgt nicht aus der Rechnung.

## Expositionsrate statt konstanter Einfallsfluss

Die physikalische Wandfläche ist S=a² S_c und das physikalische Volumen jeder Seite V=a³ V_c. Für Teilchenzahl N auf einer Seite ist die einseitige Einfallszahl pro Zeit gleich

    S (N/V) ⟨(v_n)_+⟩,

wobei (v_n)_+=max(v_n,0) mit zur Wand gerichteter Normalgeschwindigkeit. Eine isotrope Maxwell-Verteilung ergibt ⟨(v_n)_+⟩=√[τ/(2πm)]. Frei rotverschobene physikalische Impulse skalieren als a⁻¹. In der nichtrelativistischen Näherung folgt daraus τ=τ₀(a₀/a)² und ⟨(v_n)_+⟩∝a⁻¹. Die Entkopplungsskalierung ist auch in der [Literatur zur kinetischen Entkopplung](https://arxiv.org/abs/hep-ph/0612238) beschrieben.

Der Anteil von N, der pro Zeit auf die Wand trifft, skaliert folglich als a⁻². Das ist eine Rate pro Teilchen. Die Verdünnung der Dichte wird dabei genau einmal über S/V erfasst.

Die Normierung der Transmission über den Einfallsfluss gewichtet die Normalgeschwindigkeit. Für den nichtrelativistischen Gaußfaktor der Normalimpulse ist die resultierende Verteilung der normalen kinetischen Energie ε_n=p_n²/(2m) genau exp(−ε_n/τ)/τ. In der lokalen ebenen Streurechnung kann ein Tangentialimpuls durch einen Boost längs der Wand entfernt werden, da das statische skalare Massenprofil nur von der Normalenkoordinate abhängt. Die normale Energie des Dirac-Problems ist dann √(m²+p_n²)=m+ε_n+O(ε_n²/m). Der führende Faktor des aus der vorherigen Runde bekannten Mittelwerts bleibt somit Bθ τ.

## Transportbilanz

Bei gleicher Einfallsstatistik und derselben Transmissionswahrscheinlichkeit in beiden Richtungen definiere K=(S/V)⟨(v_n)_+⟩⟨T⟩ als einseitige Übergangsrate pro Teilchen. Die komovierenden Gesamtzahlen N_L und N_R ändern sich mit dem Nettofluss F=K(N_L−N_R). Für Q=N_L−N_R gilt daher Q̇=−ΓQ mit Γ=2K. Folglich

    Γ(a) ∼ 2 (S_c/V_c) √[τ₀/(2πm)] Bθ τ₀ a₀³ a⁻⁴.

Dabei ist a dimensionslos und a₀ sein Wert am Referenzzeitpunkt. Zwei Potenzen a⁻¹ kommen aus Wandfläche pro Volumen und Normalgeschwindigkeit, zwei aus der sinkenden Transmissionswahrscheinlichkeit. Für exakt getrennte Kanäle fällt die Rate schneller. Für den rotverschobenen Gaußabschluss erfordert der obere Kanal p_n²≥M²−m², seine Flusswahrscheinlichkeit ist dadurch exponentiell klein in a². Für diesen Fall benötigt die Integrabilitätsaussage keine Extrapolation der früheren relativistischen Boltzmann-Asymptotik in den hochenergetischen Teil des rotverschobenen Verteilungsprofils.

## Wann bleibt eine Differenz erhalten?

Für a(t)∝tᵖ in der späten Phase und festen nichtverschwindenden Mischwinkel gilt Γ(t)∝t⁻⁴ᵖ. Die kumulative Restrate ist genau für p>1/4 endlich. Bei p=1/4 divergiert sie logarithmisch. Beispiele für die Fortsetzung einer reinen Potenzphase:

| Expansion | Abfall der Restrate | Integrierte Restrate der späten Phase |
|---|---|---|
| a∝t^(1/2) | t⁻² | endlich |
| a∝t^(2/3) | t⁻⁸ᐟ³ | endlich |
| a∝t^(1/4) | t⁻¹ | logarithmisch divergent |

Für Q(t₀)≠0 ist Q(∞)=Q(t₀) exp[−∫Γ dt] im konvergenten Fall von null verschieden. Der Wert hängt vom Ausgangsüberschuss, Wandfläche pro Volumen und der Ratenhistorie ab. Der Befund betrifft die komovierende Differenz. Die zugehörige physikalische Dichtedifferenz Q/V verdünnt sich weiter wie a⁻³, wenn Q gegen einen nichtverschwindenden Wert geht.

## Grenze für OP5

Gegenüber der zuvor konstant gesetzten Exposition ermöglicht schon die geometrische und kinematische Abnahme der Einfälle das Ausfrieren im angesetzten expandierenden Modell. Daraus folgen weder komovierende OP5-Wände und ihre Stabilität noch der Anfangsüberschuss oder ein gravitativer Tensor. H96 bleibt offen. Für die I3-Lesart wäre der erhaltene Überschuss erst der mögliche Eingang einer gesondert herzuleitenden Λ-Auslese.
