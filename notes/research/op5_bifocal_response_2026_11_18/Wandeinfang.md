# OP5: Einfang in die Dirac-Wandmode durch Emission einer Wandwelle

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/a3cd99aac75dd31a47c6dd82a16821f5b47bcd65/notes/research/op5_bifocal_response_2026_11_18/Wandeinfang_Vorab.md). Fortsetzung von [Wandladung.md](Wandladung.md). Ebene statische Hintergrundwand mit kleinen dynamischen skalaren Fluktuationen, lokal flaches 3+1-dimensionales effektives Yukawa-Modell. Asymptotische Fermionmasse M>0. Es wird der erste Emissionsprozess geprüft. Rückwirkung auf den Kink und die Besetzungsdynamik werden nicht bestimmt.

## Elastischer Einfang ist ausgeschlossen

Bei fester statischer Wand sind Energie und Tangentialimpuls p_∥ erhalten. Ein einfallendes Fermion mit normalem Impuls p_x hat E_in²=M²+p_x²+|p_∥|². Die gebundene masselose Fermionmode hätte bei gleichem Tangentialimpuls E_W=|p_∥|. Da M>0, sind die beiden Energien verschieden. Der elastische Einteilchenoperator kann den Ladungsfluss daher nicht in diese Mode umleiten. Die räumliche Überlappung allein leistet keinen Einfang.

## Kinematik mit einem zusätzlichen Emissionskanal

Bei normalem Einfall setze E=√(M²+p_x²). Ein gebundenes Endfermion mit tangentialem Impulsbetrag k und ein emittiertes skalares Kontinuumsquant der Masse μ haben entgegengesetzte Tangentialimpulse. Normale Impulserhaltung gilt wegen der Wand nicht. Mit normalem Impuls q_x des Skalars verlangt die Energie

    E=k+√(k²+q_x²+μ²),   0≤k≤(E²−μ²)/(2E).

Ein offenes kinematisches Intervall setzt E>μ voraus. Ein gefüllter Fermikreis bis k_F blockiert diesen Prozess vollständig, sobald k_F mindestens so groß ist wie die rechte Grenze. Die Formel gibt noch kein Matrixelement für das Kontinuum an.

## Der Kink hat bereits eine dynamische Emissionsmode

Für den kanonischen Kink χ₀ aus Domaene.md folgt aus der abgeleiteten statischen Gleichung (−∂ₓ²+U″(χ₀))χ₀′=0. Eine kleine Translation der Wand hat damit das skalare Normalprofil χ₀′ und als Welle entlang der Wand ω=|q_∥|. Dieser Modentyp ist auch in der [Literatur zu effektiven Wandwirkungen](https://doi.org/10.1103/PhysRevD.111.056007) beschrieben. Anders als ein emittiertes freies Kontinuumsquant bleibt die Welle normal an die Wand gebunden.

Bei normalem Einfall sind der Tangentialimpuls des Endfermions und der Wandwelle entgegengesetzt und beide Energien gleich k. Energieerhaltung ergibt k=E/2. Es bleibt zu prüfen, ob das Yukawa-Vertex diese kinematische Möglichkeit überhaupt realisiert.

Wähle den expliziten Kink m(x)=gχ₀(x)=M tanh(Mx), also Mℓ=1. In der Normalbasis αₓ=σ₂⊗I, β=σ₁⊗I ist die gebundene Fermionmode proportional zu (sech(Mx),0)ᵀ ⊗ ξ. Der einfallende positive Streuzustand mit p_x=p>0 ist proportional zu exp(ipx)((m(x)−ip)/E,1)ᵀ ⊗ η. Er erfüllt die Normalgleichung, weil m²+m′=M². Die zweite Komponente bleibt eine laufende ebene Welle. Die Spinoren ξ und η wirken im zweidimensionalen Tangentialraum. Bei normalem Einfall kann η mit nichtverschwindendem Überlapp zum positiven tangentialen Endspinor ξ gewählt werden.

Das linearisierte Yukawa-Vertex g β δχ für die Translationswelle hat δχ proportional zu χ₀′∝sech²(Mx). Da β die beiden Normalkomponenten vertauscht, ist das räumliche Matrixelement bis auf nichtverschwindende Kopplungs- und Normierungsfaktoren proportional zu

    (ξ†η) ∫ sech³(Mx) exp(ipx) dx
      = (ξ†η) (2/M) |Γ((3+ip/M)/2)|².

Die Gleichheit folgt durch Einsetzen u=exp(2Mx) in das Integral und die Beta-Funktion. Es existiert somit ein Einfangsmatrixelement ungleich null. Für langsamen normalen Einfall ist k näherungsweise M/2 und liegt bei p<√3 M unter der Ruheenergie freier Fermionen. Der gezeigte Einfang ist möglich, solange der Endzustand bei k=E/2 frei ist. Bei einer Wand mit besetzten skalaren Wellen wäre auch die Umkehrreaktion zu berücksichtigen.

## Grenze für OP5

Die Wand kann im Kontrollmodell ein Fermion aufnehmen und die überschüssige Energie in eine Welle entlang der Wand abgeben. Die Welle ist dynamisch, während der Hintergrund in führender Näherung statisch bleibt. Das zeigt einen konkreten Beladungskanal und bestimmt weder die Einfangrate noch den Nettoüberschuss: Letzterer hängt von den einfallenden Ladungsträgern, Pauli-Sperre, Rückreaktion und Abtransport der Wandwellen ab. Eine statische Ladungsdifferenz allein liefert keine Ladungsproduktion. Die native W2/OP5-Kopplung, Bildung der Wand und die gravitative Zuordnung bleiben offen. H96 bleibt offen.
