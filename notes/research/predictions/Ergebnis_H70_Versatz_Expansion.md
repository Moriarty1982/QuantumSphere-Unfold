# Ergebnis H70: Nur ein mitbewegt fester Versatz erhält das M–T-Paar; ein falsch gekoppelter Versatz erzeugt einen homogenen, aber nicht Λ-artigen Rest

**5. November 2026. Vorab-Notiz `Vorab_Notiz_H70_Versatz_Expansion.md` (Commit 54c354a, nicht blind). Skript `k176_test_h70.py`, Ausgabe `k176_out.json`. Status: H70a bestätigt (C3 im Strahlungshintergrund nicht anwendbar), H70b widerlegt; die vorab offen gelegte analytische Erwartung zum räumlichen Mittel war falsch.**

## Kontrollen (gültig)
- Konforme Invarianz mit der Spin-Verbindung des FRW-Koframes (ω_{j0j} = +ℋ): Residuum 2e-16.
- Flacher Fall (a ≡ 1) reproduziert H69: Strom 2,7e-14, Energie 1,3e-14.

## Ergebnis (Maxima über das Fenster a ∈ [0,5; 2])
| Hintergrund | Kandidat | Weyl-Rest von χ_T | Strombilanz | Energiebilanz | räumliches Mittel / Rest |
|---|---|---|---|---|---|
| Materie | C1 (δ = c/H) | 4,6e-2 | 1,7 | 0,62 | 1,0 (ganz homogen) |
| Materie | **C2 (mitbewegt fest)** | **0** | **2,7e-14** | **1,3e-14** | (Rauschen) |
| Materie | C3 (`thm:expansion`) | 1,8 | 2,4 | 3,3 | 1,0; undefiniert für t ≤ β (40 von 121 Zeitpunkten) |
| Strahlung | C1 | 8,7e-2 | 2,4 | 1,0 | 1,0 |
| Strahlung | **C2** | **0** | **1,9e-14** | **9,2e-15** | 0 |
| Strahlung | C3 | – | – | – | nicht anwendbar: bei a = 1 ist t₀ = ½ < β, Δω nicht festlegbar |

- **H70a bestätigt:** Nur C2 erhält das Paar über das ganze Fenster, in beiden Hintergründen. C1 verletzt alles. C3 verletzt alles, wo es definiert ist; im Strahlungshintergrund ist es schon heute undefiniert.
- **H70b widerlegt:** Bei C1 und C3 ist der Energierest räumlich konstant (Mittel = Amplitude), nicht null.

## Struktur des homogenen Rests (Nachuntersuchung, Erkundung)
Materie, C1, Δτ′ = 0,0477 (konstant): Mittelwert R_ττ = −1,72, R_τz = 0,81, alle Raumkomponenten 0, Spur η^{μν}R_μν = −1,72.
- **Nicht Λ-artig:** Ein Vakuumterm wäre ∝ g_μν mit gleichen Raumkomponenten.
- **Ursache:** Mit zeitabhängigem Versatz ist χ_T keine Weyl-Lösung mehr. Seine Frequenz ist um (1 + Δτ′) gestaucht, und die Diagonalanteile heben sich deshalb nicht mehr auf. Die vorab offen gelegte Annahme „Diagonalanteile heben sich unabhängig vom Versatz auf“ übersah diese Kettenregel. Der Rest ist ein Artefakt einer Konfiguration, die die Feldgleichung verletzt, und keine physikalische Quelle.

## Lesart
- **Der Versatz zwischen den Frames muss in konformer Zeit fest sein.** In kosmischer Zeit wächst er dann mit dem Skalenfaktor, δ ∝ a. Die Frames laufen also genau mit der Expansion auseinander. Die Schwebungsfrequenz ist in konformer Zeit konstant und wird physikalisch wie Licht rotverschoben, ∝ 1/a.
- **Die Form aus `thm:expansion` (C3) trägt nicht.** Sie verletzt die Weyl-Gleichung des T-Bildes und ist für t ≤ β gar nicht definiert. Mit der Hubble-Zeit (C1) geht es ebenfalls nicht.
- **OP5:** Im einzig konsistenten Fall C2 ist der Energie-Impuls des Paares exakt null. Das Paar erzeugt keinen Vakuumterm, es ist klassisch exakt neutral. Ein Λ-artiger Term entsteht in keinem Fall; die falschen Kopplungen erzeugen nur einen nicht-Λ-artigen Rest aus verletzten Feldgleichungen.
- **Grenzen:** wie vorab. Klassisch, s_T = −1 als Eingabe, Testfelder auf vorgegebenem FRW. Die Konstante C bleibt unberührt.
