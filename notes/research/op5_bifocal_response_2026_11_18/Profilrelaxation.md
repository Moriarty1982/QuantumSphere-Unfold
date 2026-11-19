# OP5: Relaxation des skalaren Wandprofils beim Biegen

Analytische Erkundung mit numerischer Kontrolle nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/3d291188c7a090ccbd46fdae8e66fdf68b508b19/notes/research/op5_bifocal_response_2026_11_18/Profilrelaxation_Vorab.md). Fortsetzung von [Normalmoden_Biegung.md](Normalmoden_Biegung.md) und [Fragmentationsbilanz.md](Fragmentationsbilanz.md). Verwendet werden der kanonische lösbare Tanh-Kink m=yχ mit Mℓ=1, dasselbe lokale fermionische Hauptsymbol, konstante lokale Hauptkrümmungen und die führende Gleichgewichtsdichte auf der Wand. Intrinsische Spektralantwort auf eine nichtsphärische Fläche, Krümmungsgradienten und weitere Feldterme sind außerhalb dieses Modells.

## Linearer Profildruck und Translationsnullmode

Schreibe h=2H=k₁+k₂. Die skalare Flächenenergie im Normalenschlauch hat in linearer Krümmungsordnung den Anteil h∫s[(χ′)²/2+U(χ)]ds. Die Ableitung dieses Moments nach dem Profil am ebenen Kink ist −χ₀′. In der lokalen Fermirechnung ist vᵢ=1−kᵢ⟨s⟩+O(kᵢ²). Bei fester Teilchenzahl pro Referenzfläche lautet der lineare Fermienergieterm daher −h ε_F⟨s⟩/2. Dabei wird ⟨s⟩ mit der normierten Normaldichte des jeweils variierten Profils gebildet.

Bei einer Verschiebung des Kinks und der gebundenen Dichte um a verschieben sich das erste skalare Energiemoment um aσ und der Fermionschwerpunkt um a. Die Gesamtvariation lautet h a(σ−ε_F/2). Am führenden Druckausgleich ε_F=2σ fällt sie exakt weg. Der Krümmungsantrieb ist somit orthogonal zur Translationsnullmode. Das einzelne skalare Moment allein hätte diese Bedingung nicht erfüllt.

## Inversion in der Form des lösbaren Kinks

Setze x=Ms, χ₀=v tanh x und definiere
     
    q(x)=sech²x,    I(x)=∫_|x|^∞ t sech²(t) dt/2,
    B(x)=−q(x)+(8/3) I(x).

Der dimensionale lineare Profilantrieb, nach Herausziehen von h, ist v M B(x). Zur Herleitung der Fermionquelle variiert man f(s)∝exp[−y∫₀ˢχ(t)dt]. Weil der Schwerpunkt der ungestörten geraden Dichte null ist, hat die Normierungsvariation im ersten Moment keinen Beitrag. Man erhält die funktionale Ableitung δ⟨s⟩/δχ(s)=−2y I(Ms). Mit ε_F=2σ und σ=4v²M/3 ergibt sich der angegebene B(x). Explizit bestätigen ∫q² dx=4/3 und ∫Iq dx=1/2 die Orthogonalität ∫qB dx=0.

Der dimensionslose skalare Fluktuationsoperator ist L=−∂ₓ²+4−6 sech²x=A†A mit A=∂ₓ+2 tanh x und Nullmode q. Auf dem orthogonalen Raum reduziert die Minimierung des quadratischen Energiefunktionals die Energie um

    Δε_rel = −(h²/2)(v²/M) I_rel,
    I_rel = ⟨B,L_⊥⁻¹ B⟩ = ∫u(x)² dx,
    u(x) = [∫ₓ^∞ q(t)B(t)dt]/q(x).

Die letzte Gleichung löst A†u=B. Die zu B und q gerade Normalquelle gibt eine ungerade Lösung u. Die Krümmung induziert also einen negativen Beitrag κ_rel=−(v²/M)I_rel zum Koeffizienten vor h²/2. Es gibt in dieser Ordnung keinen zusätzlichen Gaußterm aus der Relaxation.

## Numerische Kontrolle und neue Aufspaltungsbilanz

Für M=v=1 wurde auf 0≤x≤24 integriert, mit zusammengesetzter Simpson-Integration im inneren Schwanzintegral und Mittelpunktregel im äußeren Integral. Die Symmetrie ergänzt die negative Hälfte. Bei 65.536 Teilintervallen ergibt sich I_rel=0,003409821580610. Mit 32.768 Teilintervallen ändert sich der Wert um weniger als 1,2·10⁻¹⁷. Das numerische Orthogonalitätsresiduum liegt unter 8,3·10⁻¹⁷. In Einheiten σ/M² beträgt die Biegekorrektur folglich κ_rel/(σ/M²)=−3 I_rel/4≈−0,00255737.

Auf der Kugel addiert der Biegeterm 8πκ_rel zur Energie pro Komponente. In der Normierung der Fragmentationsbilanz wird aus C(r) für r=k_*/M

    C_relax(r) = r²/3 [π²/4−1/2−(3/2)I_rel−(12/5)j r²],
    j=M⁴J≈0,711747742502.

Die hinreichende Bedingung C_relax>1/6 liegt jetzt bei 0,617660<r<0,875925. Zuvor waren es 0,615294<r<0,879293. Bei r=0,70 fällt der Zuschlag von 0,184630 auf 0,183794 und bleibt oberhalb von 1/6. Im selben lokalen Modell bleibt auch der Biegekoeffizient für Formmoden im gebundenen Bereich positiv: κ_lokal/(σ/M²)=2[π²/12−(9/10)j r²]−3 I_rel/4 hat bei r→1 noch rund 0,36123. Das ist die Summe der hier gerechneten lokalen Beiträge. Das nichtkugelige intrinsische Fermionspektrum und weitere Terme können für die vollständige Stabilität relevant sein. H96 bleibt offen.
