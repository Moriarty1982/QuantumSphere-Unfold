# Ergebnis H69: Das versetzte M–T-Paar trägt weder Nettostrom noch Nettoenergie

**5. November 2026. Vorab-Notiz `Vorab_Notiz_H69_MT_Paar_flach.md` (Commit dbcc40d). Skript `k175_test_h69.py`, Ausgabe `k175_out.json`. Status: H69a und H69b bestätigt.**

## Kontrollen (alle gültig)
- Weyl-Gleichung für ψ_M und ψ_T: Residuum 0 (analytische Ableitungen).
- Ein-Frame-Kontrolle: j⁰ ≥ 8,7 > 0 auf dem Raster, ohne T-Anteil ist K verletzt.
- T_μν symmetrisch (Abweichung 0); ∂^μT^M_μν = 0 relativ 1,6e-9 (Schwelle 1e-6).

## Ergebnis
| Teil | Δω·δ | relatives Residuum | Entscheidung |
|---|---|---|---|
| H69a Strom j_M + j_T | π | 4,5e-15 | bestätigt |
| | 3π | 9,4e-15 | (ungerades Vielfaches, wie vorhergesagt) |
| | 0 | 2,0 | wie vorhergesagt verletzt |
| | π/2 | 1,41 | wie vorhergesagt verletzt |
| H69b Energie-Impuls T^M + s_T T^T | π | 1,0e-15 | bestätigt |

Die Kreuzterme von T^M sind nicht klein (zum Beispiel T_tx = 3,3 bei T_tt = 14,7). Sie heben sich gegen den T-Anteil ebenso exakt auf wie die vorab bekannten Diagonalanteile.

## Lesart
- Ein Paar aus Materie und ihrem um δ versetzten Tachyonbild nach Konvention F, mit Frequenzabstand Δω = π/δ (ungerade Vielfache), löst W1 einschließlich der Gleichungen der komplexen Lesart im flachen Raum. Es hat **keinen Nettostrom und keinen Nettoenergie-Impuls**: G = 0, Torsion 0, A = 0 sind konsistent. Lokal fließen trotzdem Ströme, quer zur Achse mit der Schwebung Δω.
- Der Versatz legt damit eine Frequenz fest, die **Schwebung** der beiden gegenläufigen Wellen.
- Für OP5 heißt das: Ein solches Paar trägt klassisch nicht zur Vakuumenergie bei, gleich wie groß die Amplituden sind. Das ist eine klassische Kompensation, keine Aussage über die Quanten-Vakuumenergie.

## Grenzen (wie vorab)
- s_T = −1 ist eine Eingabe aus F3. Nach `OP5_Neutral_Pair_Dynamics_Result.md` folgt ein solches Vorzeichen nicht aus dem Frame-Etikett allein. Es ist ein Feldinhalt negativer Norm, dessen Zulässigkeit (Stabilität, Quantisierung) offen ist.
- Die Aufhebung ist für diese Zwei-Wellen-Familie gezeigt, nicht für beliebige Lösungen.
- Der Λ-Term bleibt nach Entscheidung 3 weggelassen; die freie Konstante C ist unberührt.
- δ(a) ist nicht getestet; das kommt als H70 auf gekrümmtem Hintergrund.
