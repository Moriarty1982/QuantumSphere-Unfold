# OP5: Leckage bei schwacher Mischung der Wandkanäle

Analytische Erkundung gemäß [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/611edac208ef5cca3363fc3f644b98341809a596/notes/research/op5_bifocal_response_2026_11_18/Kanalleck_Vorab.md). Fortsetzung von [Kanalauswahl.md](Kanalauswahl.md), [Higgs_Spektren.md](Higgs_Spektren.md) und [Generationensperre.md](Generationensperre.md). Abrupte stationäre Grenzfläche, keine Dynamik der Entstehung des Hintergrunds. Gleiche Energie- und Stromnormierung auf beiden Seiten.

## Stetige Spinoren am Massensprung

Setze ħ=c=1 und H=−iσ₂⊗I ∂ₓ+σ₁⊗𝓜(x). Links hat die reellsymmetrische Kanalmatrix 𝓜 die Eigenrichtungen A (Masse m) und B (Masse M), mit 0<m<M. Rechts sind die Eigenrichtungen sA+cB (Masse m) und cA−sB (Masse M), mit s=sin θ, c=cos θ und 0≤θ≤π/2. Bei θ=0 sind die offenen Richtungen orthogonal. Bei θ=π/2 stimmen sie überein. Da nur ein beschränkter Massensprung ohne Delta-Term vorliegt, sind alle Spinorkomponenten an x=0 stetig.

Für m<E<M setze k=√(E²−m²), κ=√(M²−E²), p=(m+ik)/E, ℓ=(M+κ)/E und d=(M−κ)/E. Bei auf eins normierten oberen Spinorkomponenten hat der leichte rechtseinlaufende Modus untere Komponente p, der reflektierte p*. Der schwere links nach außen abklingende Modus hat untere Komponente ℓ, der rechts abklingende d. Mit Reflexion r, Transmission t und den beiden abklingenden Amplituden a,b lautet die Stetigkeit

    1+r = s t+c b,      p+p* r = s p t+c d b,
      a = c t−s b,          ℓ a = c p t−s d b.

Die beiden propagierenden Ströme haben dieselbe Betragsnormierung, 2k/E, daher ist T=|t|². Eliminieren von r,a,b und die Identität (E²−Mm)²+κ²k²=E²(M−m)² ergeben

    T(E,θ) = 4 sin²θ κ² k² / [cos⁴θ E²(M−m)² + 4 sin²θ κ² k²].

Damit ist T=0 bei θ=0. Für jeden 0<θ≤π/2 ist T>0 im gesamten offenen Band. Bei θ=π/2 ergibt sich T=1.

## Stärke der Leckage

Setze F(E)=(M²−E²)(E²−m²)/[E²(M−m)²]. Auf dem Band liegt F zwischen null und eins. Aus E²+(Mm)²/E²≥2Mm folgt F=1 genau bei E²=Mm. Da T mit F wächst (bei θ=π/2 ist T konstant), gilt

    max T = 4 sin²θ/(1+sin²θ)²  bei E=√(mM),
    T(E,θ) = 4θ² F(E)+O(θ⁴)  für kleine θ.

Die direkte komplexe lineare Lösung der vier Stetigkeitsgleichungen mit Pivotisierung ergab für m=1 und M=3:

| θ (Radiant) | T(1,2) | T(√3) | T(2,8) |
|---:|---:|---:|---:|
| 0 | 0,00000000 | 0,00000000 | 0,00000000 |
| 0,05 | 0,00576569 | 0,00994194 | 0,00253423 |
| 0,10 | 0,02294991 | 0,03908389 | 0,01018601 |
| π/2 | 1,00000000 | 1,00000000 | 1,00000000 |

Formel und direkte Lösung unterschieden sich um höchstens 2,3·10⁻¹⁶. Die Summe T+|r|² wich um höchstens 5,6·10⁻¹⁶ von eins ab.

## OP5

Der Winkel ist die lokale Ausrichtung der Masseneigenräume im gewählten Wandmodell. Er ist weder ein beobachteter CKM-Winkel noch ein aus W2 abgeleiteter Parameter. Die Rechnung bestimmt eine Durchlasswahrscheinlichkeit pro Einfall, ohne einfallenden Fluss, Energiebesetzung, Übergangsoperator oder Wandgeschichte und damit ohne physikalische Leckrate. Als Verbindung zum [Ausfriermodell](Ausfrieren.md) ergibt sich eine bedingte Schranke: Falls die Restrate im betrachteten Band höchstens eine konstante Einfallsrate mal max T beträgt, reicht ein zeitlich quadratintegrierbarer kleiner Mischwinkel für endliche integrierte Restrate. Diese Voraussetzungen sind im Companion nicht hergeleitet. H96 bleibt offen.
