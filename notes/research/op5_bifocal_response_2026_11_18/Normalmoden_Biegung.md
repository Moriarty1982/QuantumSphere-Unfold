# OP5: Virtuelle Normalmoden schwächen den positiven Biegebeitrag ab

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/b4d58e727ee638ae06c0be9bbb4c97cc0b5fafc7/notes/research/op5_bifocal_response_2026_11_18/Normalmoden_Biegung_Vorab.md). Fortsetzung von [Fermion_Biegung.md](Fermion_Biegung.md). Festgehaltener Kink, lokal konstante Hauptkrümmungen k₁,k₂, Normalmaß-Normierung wie zuvor. Behandelt wird dasselbe lokale Hauptsymbol, jetzt einschließlich der Mischung mit dem normalen Kontinuum in zweiter Krümmungsordnung.

## Störungsrechnung im Normalkanal

Schreibe D für den ebenen Normal-Diracoperator, α(p)=p₁α₁+p₂α₂ für das tangentiale Symbol und p=|p|>0 für den Betrag des Tangentialimpulses. Die αᵢ sind hermitesch, erfüllen die Clifford-Relationen und antikommutieren mit D. Der gesamte Normalnullraum hat Projektor P, Q=1−P. Auf dem Normalnullraum hat das positive Band die Energie p. Die Krümmungsstörungen aus den inversen Tangentialskalen sind

    V₁=−s α(b),  bᵢ=kᵢ pᵢ,
    V₂=s² α(c),  cᵢ=kᵢ² pᵢ.

Wegen der geraden Normaldichte verschwindet P V₁ P. Der direkte Beitrag von V₂ ist μ₂ (k₁²p₁²+k₂²p₂²)/p mit μ₂=⟨f,s²f⟩.

Auf Q ist bei E=p der Resolvent von D+α(p) gleich −[p+D+α(p)](D²|_Q)⁻¹. Der Term mit D verschwindet im Matrixelement, weil D die Normalgraduierung wechselt, während s, αᵢ und D² sie erhalten und f in einer festen Graduierung liegt. Bezeichne das gemeinsame positive Normalmoment mit J=⟨sf,(D²|_Q)⁻¹sf⟩. Die Clifford-Relationen geben im positiven Tangentialspinor ⟨α(b)[p+α(p)]α(b)⟩=2(p·b)²/p. Somit lautet der virtuelle Energieterm

    δE_mix = −2J (k₁ p₁²+k₂ p₂²)²/p.

Die negative Korrektur ist kubisch in p. Sie stammt aus dem normalen Kontinuum des gewählten Symbols. Die Rechnung schließt keine Übergänge aufgrund von Krümmungsableitungen ein.

## Biegekoeffizient des gefüllten Bandes

Bei festgehaltener lokaler Flächenbesetzung lässt sich die Energieänderung erster Ordnung in der bereits quadratischen Störung über den ungestörten Fermikreis integrieren. Die Verschiebung seiner Grenze trägt bei festem Teilcheninhalt in dieser Ordnung nichts bei. Winkelmittel sind ⟨cos⁴φ⟩=3/8 und ⟨cos²φ sin²φ⟩=1/8. Das Verhältnis der radialen Momente ∫p⁴ dp/∫p² dp ist 3k_F²/5. Mit ebener Fermienergie pro Fläche ε_F folgt

    Δε/ε_F = (μ₂/2)(k₁²+k₂²)
              − (3J k_F²/20)[3(k₁²+k₂²)+2 k₁ k₂].

In der Konvention Δε=(κ/2)(2H)²+κ_G K ergibt das

    κ/ε_F   = μ₂ − (9/10)J k_F²,
    κ_G/ε_F = −μ₂ + (3/5)J k_F².

Für den lösbaren Kink m(s)=M tanh(Ms) hat D² die Partneroperatoren A†A und AA†, mit A=∂ₛ+m(s). Der zweite Partner ist AA†=−∂ₛ²+M². Die nichtverschwindenden Spektren beider Partner stimmen über die Polarzerlegung überein. Daher ist D²≥M² auf Q. Weil sf orthogonal zu f ist, folgt J≤μ₂/M². Im gebundenen Bereich k_F<M bleibt der lokale Koeffizient strikt positiv. Sogar die grobe analytische Schranke lässt mehr als ein Zehntel seines ursprünglichen Werts übrig.

## Numerische Kontrolle des Normalmoments

Das Moment J ist die Norm zum Quadrat der Lösung u von A†u=sf. Aus f′=−mf folgt u(s)=f(s)⁻¹∫ₛ^∞ t f(t)²dt. Für M=1 und f=sech(s)/√2 wurde die gerade Norm auf |s|≤25 per Mittelpunktregel mit 65.536 Intervallen auf der positiven Hälfte integriert. Ergebnis J≈0,711747742502 und μ₂≈0,822467033424, in Übereinstimmung mit μ₂=π²/12. Halbierung der Auflösung änderte J um weniger als 2,4·10⁻¹⁴. Die diskrete Kontrolle ergibt J/μ₂≈0,865381485. Selbst am Grenzwert k_F→M bleibt in diesem Symbol dadurch rund 22,1 % des ursprünglichen Biegebeitrags bestehen. Die Positivität hängt nicht von der Quadratur ab.

## Grenze für OP5

Der positive Formterm übersteht die geprüfte virtuelle Normalmischung. Diese Rechnung hält das skalare Profil fest und behandelt die Fermionen lokal als gefülltes Band. Intrinsische Spektralkorrekturen auf einer geschlossenen Fläche und die Profilrelaxation können weiterhin zur Gesamtenergie beitragen. Die [mikroskopische Fermi-Ball-Rechnung von Ogure et al.](https://arxiv.org/abs/hep-ph/0212332) behandelt Stabilitätsfragen in einem verwandten Modell mit endlicher Fermionbreite. Die volle Form- und Fragmentationsstabilität sowie H96 bleiben hier offen.
