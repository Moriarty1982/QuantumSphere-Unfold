# OP5: Formstabilität der fermionisch beladenen Wand

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/6f2ae3ccb6ba8a241a345f5719ade432d70a9eb6/notes/research/op5_bifocal_response_2026_11_18/Wandform_Vorab.md). Fortsetzung von [Wandladung.md](Wandladung.md) und [Wandkontraktion.md](Wandkontraktion.md). Feste Gesamtladung, gleich tiefe Vakua, keine Selbstgravitation. Die Fermionen verteilen sich im führenden Flächenmodell bei jeder Form homogen. Nicht betrachtet werden dynamische Relaxation und der vollständige mikroskopische Krümmungskoeffizient.

## Der radiale Druckausgleich lässt Formmoden frei

Die führende Energie ist E₀(A)=σA+C N^(3/2) A^(−1/2). Sie hängt nur von Fläche A und fester Teilchenzahl N ab. Am optimalen A_* gilt E₀′(A_*)=0. Für eine radiale Störung R(Ω)=R_*[1+εu(Ω)] ist

    A = A_* + R_*² ∫[2εu + ε²(u²+|∇u|²/2)] dΩ + O(ε³).

Für jede Kugelflächenmode mit ℓ≥2 ist der lineare Flächenanteil null. Da zudem E₀′(A_*)=0, ist die Energieänderung hier erst von Ordnung ε⁴. Eine gleichzeitige Anpassung des mittleren Radius kann die Fläche exakt auf A_* halten. Alle so erzeugten Formen haben in E₀ dieselbe Energie. Das radiale Minimum belegt damit keinen quadratischen Rückstellterm gegen Abplattung oder höhere Formstörungen.

## Was ein starr fortgesetzter Kink beiträgt

Für das skalare Kinkprofil χ₀(s) sei s der vorzeichenbehaftete Normalabstand zur gewählten Oberfläche, mit Hauptkrümmungen k₁,k₂, H=(k₁+k₂)/2 und K=k₁k₂. Bei festgehaltenem Profil entlang jeder Normale ist der Volumenfaktor der parallelen Fläche (1+s k₁)(1+s k₂). Das gilt im regulären Normalenschlauch. Für große Krümmungsradien kann das Wandprofil in der Dünnwandentwicklung wegen seiner abklingenden Energie über die ganze Normale integriert werden.

Die ebene Energiedichte e(s)=v² sech⁴(s/ℓ_W)/ℓ_W² ist gerade. Ihr erstes Moment verschwindet. Die in dieser Näherung erhaltene Krümmungskorrektur lautet daher κ_G ∫K dA mit κ_G=∫s²e(s)ds>0. Ein H²-Term entsteht aus diesem starr fortgesetzten Profil nicht. Auf einer geschlossenen Fläche mit Kugeltopologie ist ∫K dA=4π. Dieser Beitrag ist konstant bei Verformung und gibt keine Rückstellkraft. Als isolierter Beitrag erhöht er die Energie um 4πκ_G pro zusätzlicher kugeltopologischer Komponente. Das entscheidet Fragmentation nur, wenn keine anderen vergleichbaren Beiträge vorhanden sind.

## Welche Krümmung eine Kugel stabilisieren könnte

Für eine lokale, unter Umkehr der Normalen symmetrische quadratische Krümmungskorrektur schreibe

    E_curv = (κ/2) ∫(2H)² dA + κ_G ∫K dA.

Aus (2H)²=4K+(k₁−k₂)² bleibt bei fester Kugeltopologie nur der spurfreie Krümmungsanteil formabhängig. Auf der Einheitskugel ist seine lineare Variation bei R(Ω)=R_*[1+εu(Ω)] bis auf Vorzeichen und den Faktor ε/R_* die spurfreie Hessematrix von u. Die Bochner-Identität liefert für orthonormal entwickelte Kugelflächenmoden u_{ℓm}

    ΔE_curv = (κ ε²/2) Σ_{ℓ,m} (ℓ−1)ℓ(ℓ+1)(ℓ+2) |u_{ℓm}|² + O(ε³).

Denn mit −Δu=λu gilt ∫|Hess(u)^TF|² dΩ=λ(λ−2)∫|u|²dΩ/2 und λ=ℓ(ℓ+1). ℓ=0 ist die Größenskalierung und ℓ=1 die Translation in linearer Ordnung. Für ℓ≥2 entscheidet das Vorzeichen des gesamten κ. Positives κ liefert eine lokale Rückstellenergie, negatives κ eine Instabilität bereits in dieser Ordnung. Bei κ=0 braucht die Entscheidung weitere Terme. Das lokale Kriterium ersetzt weder die dynamische Prüfung noch die Fragmentationsbilanz. Für kugelförmige Fragmente wäre die quadratische Korrektur 4π(2κ+κ_G) pro Komponente, sofern dieselben Koeffizienten im jeweiligen Dünnwandregime gelten.

## Einordnung

Die Rechnung isoliert, was aus dem bisher verwendeten ebenen Profil wirklich folgt. Der starre skalare Anteil gibt einen topologischen Beitrag, aber keinen Formkoeffizienten κ. Profilrelaxation und gekrümmte Fermionzustände wurden nicht integriert. [Ogure et al.](https://arxiv.org/abs/hep-ph/0212332) zeigen für ein verwandtes neutrales Fermi-Ball-Modell, dass endliche Dicke der Fermionverteilung die Fragmentationsbilanz ändern kann und Stabilität nur in einem Teil des Parameterraums folgt. Das setzt kein Vorzeichen des gesamten κ für OP5 fest. Formstabilität, native Einbettung und H96 bleiben offen.
