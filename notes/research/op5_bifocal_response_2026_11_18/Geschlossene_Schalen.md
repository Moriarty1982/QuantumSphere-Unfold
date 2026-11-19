# OP5: Zweite Formvariation bei geschlossenen Dirac-Schalen

Analytische Erkundung mit numerischer Kontrolle nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/c3465cd6700e7152b4330b16b09ed2db83d28b66/notes/research/op5_bifocal_response_2026_11_18/Geschlossene_Schalen_Vorab.md), Fortsetzung von [Schalenverformung.md](Schalenverformung.md). Alle positiven Schalen k≤L sind vollständig mit g identischen Dirac-Zweigen besetzt. Die numerischen Eigenwerte werden in Einheiten 1/R geführt. Die Rechnung betrifft die flächenerhaltende quadrupolare Richtung u=P₂(cos θ). Die Fläche bleibt bei 4πR².

## Konforme Ersatzkurve und Spurformel

Sei g₀ die runde Metrik. Nutze die exakt flächenerhaltende konforme Kurve g_δ=e^(2δu)g₀/⟨e^(2δu)⟩, wobei ⟨·⟩ das Kugelmittel bezeichnet. Die flächenerhaltende eingebettete radiale Störung hat dieselbe erste Metrikvariation. In zweiter Ordnung können sich die Metriken unterscheiden. Für eine volle Schale ist das erste Differential ihrer Eigenwertsumme an der runden Kugel rotationsinvariant und daher proportional zur Flächenvariation. Das folgt direkt durch Mittelung des metrischen Störtensors über SO(3): Sein invariantes Mittel ist ein konstantes Vielfaches von g₀ und wird durch seine integrierte Spur bestimmt. Da beide Kurven die Fläche erhalten, erzeugt ihre Differenz zweiter Ordnung in diesem Differential keinen Energiebeitrag. Die konforme Rechnung gibt deshalb denselben quadratischen Koeffizienten wie die eingebettete Störung für volle Schalen.

Im festen L²-Raum ist der dimensionslose Dirac-Operator D_δ=W D₀ W mit der [konformen Transformationsregel](https://epub.uni-regensburg.de/25547/1/MP176.pdf), W=⟨e^(2δu)⟩^(1/4) e^(−δu/2). Aus ⟨u⟩=0 und ⟨u²⟩=1/5 folgt

    W = 1−δu/2+δ²(u²/8+1/10)+O(δ³).

Der erste Operator ist −{u,D₀}/2. Bei einer vollen Schale ergibt die Spur des direkten quadratischen Operators und des virtuellen Terms zusammen

    A_k = (2k²)/5 + (k/2) T_{k,k}
              + Σ_{ν≠k} [k(k+ν)/(2(k−ν))] T_{k,ν},
    T_{k,ν}=Σ_{m,m′}|⟨ν,m′|u|k,m⟩|².

Denn der direkte Term trägt aus den u²- und uD₀u-Anteilen pro Übergang (k+ν)/4. Für ν≠k kommt der virtuelle Term (k+ν)²/[4(k−ν)] hinzu. Für ν=k bleibt nur der direkte Term k/2. Die konstante Maßnormierung liefert 2k²/5. Die Spurformel gilt trotz der linearen Aufspaltung, solange die ganze Schale besetzt bleibt und von den übrigen Schalen als Spektralgruppe getrennt ist.

## Summation der Übergangsstärken

In der Orbitschreibweise D₀=σ·L+1 hat der positive Zustand k die Bahnzahl l=k−1. Die Multiplikation mit u=P₂ koppelt l an l und l±2. Die Vorzeichen und Multiplizitäten ergeben sich aus der Spinaddition j=l±1/2. Verwende C_{l,a}=√[(l²−a²)/(4l²−1)], mit null für nicht vorhandene Zustände, in der Rekursion cos θ Y_{l,a}=C_{l+1,a}Y_{l+1,a}+C_{l,a}Y_{l−1,a}. Zweimalige Anwendung und die Clebsch-Gordan-Gewichte ergeben nach Summe über m

    a(k) = 3k(k+1)(k+2)/[5(2k+1)(2k+3)],
    b(k) = 6k(k+1)/[5(2k−1)(2k+1)(2k+3)],

    T_{k,k}       = 2k(k²−1)/[5(4k²−1)],
    T_{k,k+2}     = a(k),       T_{k,k−2}     = a(k−2),
    T_{k,−(k+1)}  = b(k),       T_{k,−(k−1)}  = b(k−1).

Bei nicht vorhandenen Schalen ist der Eintrag null. Die übrigen Übergänge verschwinden. Die Summe aller Stärken gibt 2k/5, wie direkt aus der rotationsinvarianten Schalenprojektordichte folgt. Einsetzen in die Spurformel und algebraisches Zusammenfassen liefert

    A_k = 3 k² (4k⁴−3k²+1) / [5(4k²−1)²] > 0   für k≥1.

Der Zähler hat positives Vorzeichen, da 4k⁴−3k²+1=k²(4k²−3)+1. Daher ist auch der Koeffizient der vollständig besetzten Schalen positiv:

    ΔE_intr = (g/R) δ² Σ_{k=1}^L A_k + O(δ³).

Eine direkte Auswertung der orbitalen Rekursion und Spinormatrizen ohne die vereinfachte Formel bestätigte für die geprüften k≤32 den Einzelkoeffizienten bis auf 2.84e-13. Die Summen lauten:

| L | N/g | Σ A_k |
|---:|---:|---:|
| 1 | 2 | 0.133333333 |
| 2 | 6 | 0.698666667 |
| 3 | 12 | 2.012299320 |
| 8 | 72 | 30.326408292 |
| 32 | 1056 | 1714.827225264 |

## Vergleich und Grenze

Der lokale Biegeausdruck aus Wandform.md liefert für u=P₂ und den nach Profilrelaxation verbleibenden lokalen Koeffizienten κ_lokal den Term (48π/5)κ_lokal δ². Er ist in dem dort geprüften gebundenen Bereich positiv. Auch der intrinsische Term erhöht bei voller Schale die quadrupolare Energie. Damit ist die runde Wand im additiven Modell entlang dieser Prüfrichtung stabil. Aus dem Vorzeichen folgt keine Entscheidung für höhere Formmoden, offene Schalen, dynamische Stabilität oder tatsächliche Aufspaltung. Die Entwicklung gilt bei festem endlichem L und hinreichend kleinem δ. Die Störungsgrenze ist aufgrund der wachsenden Matrixelemente im Verhältnis zum Schalenabstand nicht in L uniform. H96 bleibt offen.
