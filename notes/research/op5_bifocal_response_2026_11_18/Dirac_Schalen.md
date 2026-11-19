# OP5: Diskrete Dirac-Schalen und Aufspaltung der Kugel

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/f65b593bd8456164bd998cf9772771cff8ac78e6/notes/research/op5_bifocal_response_2026_11_18/Dirac_Schalen_Vorab.md). Fortsetzung von [Wandladung.md](Wandladung.md) und [Normalmoden_Biegung.md](Normalmoden_Biegung.md). Hier wird nur die intrinsische masselose Dirac-Kinetik der runden Kugel plus konstante nackte Flächenspannung σ betrachtet. Die Kugel ist eine vorgeschriebene Form. Bei offener Schale wird nur die Gesamtenergie der besetzten Zustände verwendet. Extrinsische Korrekturen, Selbstgravitation und Profilrelaxation sind ausgelassen.

## Exakte Besetzungsenergie

Das positive intrinsische Dirac-Spektrum auf der runden S² hat Energien j/R und Multiplizität 2j für j=1,2,…. Es folgt z. B. aus der Darstellung des Einheitskugeloperators als σ·L+1: Addition von Bahndrehimpuls und Spin 1/2 liefert die Zweige ±j mit Multiplizität 2j. Siehe auch [Camporesi und Higuchi](https://arxiv.org/abs/gr-qc/9505009). Für g identische unabhängige Zweige sei S(N)=R E_F(N,R). Sind die ersten L Schalen voll, gilt

    N_L=g L(L+1),
    S(N_L)=g L(L+1)(2L+1)/3.

Für N=N_L+n, 0≤n<2g(L+1), ist S(N)=S(N_L)+(L+1)n. Das Kontinuumsmodell liefert S₀(N)=2N^(3/2)/(3√g). An geschlossenen Schalen gilt S/S₀=√[1+g/(4N)]>1. Auch dazwischen liegt die Energie über dem Kontinuumswert: S interpoliert linear zwischen den geschlossenen Werten, und S₀ ist konvex.

Setze h=L+1, η=n/(2gh) und b=2η−1. Dann ist N/g=h²+bh und S/g=2h³/3+bh²+h/3. Bei großem h lautet die Differenz

    S−S₀ = gh[1/3−b²/4] + O(g).

Der Koeffizient läuft von 1/12 bei geschlossenen Schalen bis 1/3 bei halber Füllung. Bei festem Radius entspricht dies einem Energiezuschlag (S−S₀)/R. Im Dünnwandgleichgewicht, wo R wie √N wächst, bleibt der Zuschlag von Ordnung N⁰ und hängt weiterhin von der Schalenfüllung ab.

## Energiebilanz zweier Kugeln

Minimieren von U(R)=4πσR²+S/R ergibt R_*³=S/(8πσ) und

    U_*(N)=3(4πσ)^(1/3)[S(N)/2]^(2/3).

Sei μ₀ der konstante Energie-pro-Teilchen-Wert des Kontinuumsmodells am radialen Minimum. Dann gilt U_*/μ₀=N(S/S₀)^(2/3). Die führende Schalenkorrektur zu U_*/μ₀ ist g[1/3−b²/4], mit Fehler O(g/h). Die lineare Kontinuumsenergie hebt sich zwischen Mutter und Töchtern exakt weg.

Für g=1 und zwei gleich große Töchter mit geschlossener Schale L habe die Mutter N=2L(L+1). Getestet wurde das Vorzeichen von S(N)²−8S(N/2)² mit Ganzzahlarithmetik. Es ist dasselbe wie das Vorzeichen der beim Zerfall verfügbaren Energie Δ=U_*(N)−2U_*(N/2). Positives Δ bedeutet energetisch günstigere getrennte Kugeln im geprüften Modell.

| L der Tochter | N der Mutter | Füllung η der letzten Mutterschale | Δ/μ₀ |
|---:|---:|---:|---:|
| 298 | 178204 | 0.642180 | 0.146348 |
| 299 | 179400 | 0.056604 | -0.029859 |
| 300 | 180600 | 0.470588 | 0.165825 |

Für 1≤L≤300 sind 244 Fälle energetisch günstig und 56 ungünstig, ohne Gleichstand. Das sind Konfigurationen einer gewählten Folge, keine physikalischen Wahrscheinlichkeiten. Die Zahlen prüfen, ob beide Vorzeichen tatsächlich auftreten. Asymptotisch kostet jede geschlossene Tochterschale g/12 in Einheiten μ₀. Die Mutter kann weniger oder mehr als ihre Summe g/6 kosten, je nach Füllung.

## Einordnung

Die intrinsische Schalenkorrektur ist bei fester Teilchenzahl positiv, doch ihre Differenz zwischen einer und zwei Kugeln hat kein festes Vorzeichen. Die Rechnung bestimmt weder einen Formkoeffizienten für nichtsphärische Störungen noch eine Zerfallsbarriere. Extrinsische Biegung, andere mikroskopische Beiträge derselben Größenordnung und die energetische Bindung gegenüber freien Fermionen bleiben für eine Gesamtentscheidung zu berücksichtigen. OP5/H96 bleiben offen.
