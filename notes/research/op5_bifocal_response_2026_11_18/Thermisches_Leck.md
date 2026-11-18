# Thermische Leckage an der OP5-Zweikanalwand

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/14f8c38a72bccfa39696fe1fcd511403fa7a80ae/notes/research/op5_bifocal_response_2026_11_18/Thermisches_Leck_Vorab.md). Massensprung und Teilchennormierung wie in [Kanalleck.md](Kanalleck.md), 0<m<M. Eine einzige von links einfallende leichte Sorte, klassisch verdünnter eindimensionaler Fluss bei Temperatur τ in Energieeinheiten. Der Flussfaktor v=∂E/∂p auf p>0 hebt den Wechsel von dp zu dE auf. Für eine Boltzmann-Besetzung ist die auf den Einfallsfluss normierte Energieverteilung daher w(E)=exp[−(E−m)/τ]/τ, E≥m. Keine relativistische Vielteilchendynamik, Rückstreuung aus einem zweiten Reservoir oder thermische Wandlösung.

## Getrennte Kanäle

Für θ=0 ist T=0 zwischen m und M. Oberhalb von M wird derselbe Kanal auf der Gegenseite propagierend. Schreibe k=√(E²−m²) und q=√(E²−M²). An der Stufe sind die beiden Spinorkomponenten stetig. Mit oberen Komponenten 1,r,t und unteren Komponenten (m+ik)/E für Einfall, (m−ik)/E für Reflexion und (M+iq)/E für Ausfall erhält man t=2ik/[m−M+i(k+q)]. Das Verhältnis der Stromnormierungen ist q/k. Damit

    T₀(E) = 4kq / [(M−m)²+(k+q)²],    E>M.

Setze Δ=M−m und k₀=√(M²−m²). Für ε=E−M↓0 folgt T₀(M+ε)=C√ε+O(ε) mit C=4 k₀ √(2M)/[(M−m)²+k₀²]. Integration mit w(E) ergibt

    ⟨T₀⟩ = exp(−Δ/τ) [C (√π/2) √τ + O(τ)].

Die ideale Kanalsperre macht den thermischen Durchlass somit bei positiver Temperatur nicht exakt null. Durch kommen nur Teilchen aus dem Anteil der Verteilung oberhalb von M.

## Fester Mischwinkel

Für 0<θ<π/2 folgt bei E=m+ε aus Kanalleck.md

    Tθ(m+ε) = Bθ ε + O(ε²),
    Bθ = 8 sin²θ (M+m) / [m (M−m) cos⁴θ].

Der Beitrag des Sperrfensters beträgt Bθ τ+O(τ²). Stromerhaltung beschränkt den nicht eigens aufgelösten Beitrag für E≥M durch exp(−Δ/τ). Bei festem θ und tiefer Temperatur dominiert somit ein linearer Durchlass. Bθ ist für kleine θ proportional zu θ². Diese Asymptotik gilt bei festem Winkel abseits von π/2.

## Numerische Kontrolle

m=1, M=3, θ=0,1 Radiant. Zusammengesetzte Mittelpunktregel nach der Substitution E=E_start+τu² mit 32.768 Teilintervallen auf 0≤u≤12. E_start ist M für θ=0 und m für θ=0,1. Die ausgelassene Boltzmann-Masse nach u=12 ist höchstens exp(−144).

| τ | ⟨T₀⟩ vollständig | ⟨T₀,₁⟩ unterhalb M | Obergrenze Zusatz oberhalb M bei θ=0,1 |
|---:|---:|---:|---:|
| 0,1 | 9.16470e-10 | 0.011844012 | 2.06115e-9 |
| 0,05 | 1.47942e-18 | 0.006849994 | 4.24835e-18 |
| 0,02 | 9.01948e-45 | 0.003024870 | 3.72008e-44 |

Halbe Auflösung änderte die θ=0-Werte relativ um höchstens 2,1·10⁻¹⁴ und den Beitrag unterhalb M absolut um höchstens 3,4·10⁻¹⁷. Bei τ=0,02 ist der skalierte Koeffizient ⟨T₀⟩/[√τ exp(−Δ/τ)] etwa 1,71 (Grenzwert 2,05). Der Quotient des Mischbeitrags durch τ ist etwa 0,151 (Grenzwert 0,163). Die Abweichung der Quotienten von den Grenzwerten misst bei diesen Temperaturen die Korrekturterme, nicht den Quadraturfehler.

## Bezug zum Ausfrieren

Wenn in einem quasistatischen Modell die Restrate proportional zu diesem Mittelwert ist, die Einfallsrate zeitlich konstant bleibt und τ(t) asymptotisch wie t⁻ᵖ mit p>0 abnimmt, ist der thermische Beitrag bei θ=0 für jedes p>0 zeitlich integrierbar. Bei festem 0<θ<π/2 ist er genau dann integrierbar, wenn p>1. Das zeigt unter expliziten Annahmen, wann trotz endlichem augenblicklichem Durchlass ein Restüberschuss möglich wäre. W2/OP5 liefern hier weder Temperaturgeschichte, Fluss und Mischwinkel noch das Ausgangsprofil oder die gravitative Auslese. H96 bleibt offen. Die I3-Lesart einer späteren Λ-Auslese setzt weiterhin einen unabhängig begründeten Überschuss voraus.
