# OP5: Höhere Formmoden vollständig gefüllter Dirac-Schalen

Analytische Erkundung und numerische Kontrolle nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/a62ec9cda06278246656a659ff40a98c213f119a/notes/research/op5_bifocal_response_2026_11_18/Hoehere_Formmoden_Vorab.md). Fortsetzung von [Geschlossene_Schalen.md](Geschlossene_Schalen.md). Festes R aus der erhaltenen Fläche und vollständig gefüllte positive Schalen bis einschließlich L. Die Entwicklung behandelt bei festem L den Grenzfall kleiner Verformung. Nackte Flächenenergie und lokale Biegung entsprechen den bisherigen Modellannahmen.

## Rotationssymmetrie und endliche Summen

Bei geschlossenen Schalen ist die quadratische intrinsische Energie ein unter SO(3) invariantes Funktional der linearen Metrikvariation u. Daher koppelt sie keine verschiedenen Kugelflächengrade. Innerhalb eines Grades ist sie ein Vielfaches der L²-Norm. Es genügt somit, das axiale Profil u=P_ℓ(cos θ) für jeden Grad ℓ zu rechnen. Dies erfasst auch eingebettete radiale Verformungen gleicher Fläche, da deren Abweichung vom konformen Ersatzpfad zweiter Ordnung im ersten, nur flächenabhängigen Differential der vollen Schalen verschwindet.

Die Spurformel aus Geschlossene_Schalen.md gilt mit ⟨u²⟩=1/(2ℓ+1):

    A_{k,ℓ}=2k²/(2ℓ+1)+(k/2)T_{k,k}^{(ℓ)}
            +Σ_{ν≠k} [k(k+ν)/(2(k−ν))] T_{k,ν}^{(ℓ)},
    B_{L,ℓ}=Σ_{k=1}^L A_{k,ℓ},
    ΔE_intr=(g/R) B_{L,ℓ} δ²+O(δ³).

Die Übergangsstärken sind die Summen der quadratischen Matrixelemente von P_ℓ über beide Schalen. Der Gesamtwert je Anfangsschale ist 2k/(2ℓ+1). Die Legendre-Rekursion (d+1)P_{d+1}=(2d+1)xP_d−d P_{d−1} und die beiden Schritte der cos-θ-Rekursion der Kugelflächenfunktionen liefern die orbitalen Matrixelemente. Die Spinaddition liefert die positiven und negativen Dirac-Zwischenzustände. Alle möglichen Zwischenzustände liegen im endlichen orbitalen Band |l′−l|≤ℓ. Die Auswertung nutzt daher keinen spektralen Abschneideparameter zusätzlich zu L und ℓ.

## Erster Schalenabschluss für beliebige Formgrade

Für k=1 ist l=0. Multiplikation mit P_ℓ führt nur zu orbitalem l′=ℓ. Bei ℓ≥1 verteilen sich die Stärken auf ν=ℓ+1 und ν=−ℓ. Sie lauten 2(ℓ+1)/(2ℓ+1)² bzw. 2ℓ/(2ℓ+1)². Einsetzen gibt

    B_{1,ℓ} = (ℓ−1)(ℓ+2)/[ℓ(ℓ+1)(2ℓ+1)].

Damit ist die erste voll besetzte Schale in jeder einzelnen Formrichtung ℓ≥2 intrinsisch positiv in zweiter Ordnung. Der Wert für ℓ=1 ist null. Das ist die lineare Richtung einer Translation und eine Kontrolle der Flächennormierung. Der Fall ℓ=0 wird durch die Flächenbedingung ausgeschlossen.

## Weitere Schalenabschlüsse

Das reproduzierbare Skript [hoehere_formmoden.mjs](hoehere_formmoden.mjs) wertet die endlichen Übergangssummen aus. Alle 704 Kombinationen 2≤ℓ≤12 und 1≤L≤64 ergaben B_{L,ℓ}>0. Die kleinste Zahl je Grad und der Vergleich bei L=64 sind:

| ℓ | min über L=1,…,64 | B_{64,ℓ} |
|---:|---:|---:|
| 2 | 0.133333333 | 13413.627368416 |
| 3 | 0.119047619 | 0.119047619 |
| 4 | 0.100000000 | 4190.196648538 |
| 5 | 0.084848485 | 0.339393939 |
| 6 | 0.073260073 | 2013.566260231 |
| 7 | 0.064285714 | 0.658285714 |
| 8 | 0.057189542 | 1178.402764762 |
| 9 | 0.051461988 | 1.075450531 |
| 10 | 0.046753247 | 772.570067444 |
| 11 | 0.042819499 | 1.590826932 |
| 12 | 0.039487179 | 545.500783268 |

Der maximale Fehler der Übergangsnorm war 4,3·10⁻¹⁴. Die analytische Quadrupolformel stimmt in den Einzelkoeffizienten bis auf 2,7·10⁻¹². Für ℓ=1 blieb die numerische Summe im Betrag unter 6,8·10⁻¹². Bei festem L können die unterschiedlichen Grade innerhalb des geprüften Bereichs wegen der Rotationssymmetrie linear kombiniert werden, ohne dass gemischte Terme in der quadratischen Energie entstehen.

Für u=P_ℓ addiert das lokale Modell den Biegeterm

    [2π κ_lokal/(2ℓ+1)] (ℓ−1)ℓ(ℓ+1)(ℓ+2) δ².

Er ist bei dem in Profilrelaxation.md gerechneten positiven κ_lokal ebenfalls positiv, soweit die lokale Dünnwandentwicklung bei der jeweiligen Formwellenlänge anwendbar ist. Die intrinsische Rechnung liefert einen Beweis für L=1 und eine Rasterkontrolle für weitere Schalenabschlüsse. Sie liefert keinen Satz über beliebiges L und ℓ, keine Aussage zur offenen Schale, zur zeitlichen Dynamik oder zur Fragmentationsbarriere. H96 bleibt offen.
