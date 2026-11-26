# Ergebnis H177: Die Phasenhalbierung zwischen den Sektoren gilt bei keiner gemeinsamen Skala

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H177_Phasenhalbierung_gemeinsame_Skala.md` (Commit 0887d27, vor der Rechnung). Die Beobachtung der
Halbierung war nachträglich (k374); blind war die Frage, wie δ_d und δ_u oberhalb von M_Z laufen. Skripte k375 (Python, 10⁵ Ziehungen, Seed 20261126)
und k375b (Wolfram, Zentralwerte, NDSolve). Zentralwerte stimmen überein. Qiskit nicht eingesetzt.

**Ergebnis in einem Satz:** Das Laufen ist zu schwach und geht für die beiden Quarktypen in entgegengesetzte Richtung; weder δ_d = δ_e/2, δ_u = δ_e/4
noch δ_d = π/24, δ_u = π/48 wird zwischen M_Z und der Planck-Skala erreicht. **H177a ist in beiden Fassungen widerlegt.**

## Ergebnisse gegen die Kriterien
| Fassung | Ziel δ_d / δ_u | Befund im Bereich I ∈ [0; 0,1337] | Urteil |
|---|---|---|---|
| V1 (Verhältnis) | 0,111111 / 0,055556 | δ_d läuft von 0,1001 auf 0,1077 (z von −11,5 bis −3,3), δ_u von 0,0518 auf 0,0484 (z von −7,7 bis −15,9); bestes gemeinsames I: beide −9,6σ | **widerlegt** |
| V2 (Baumwerte) | 0,130900 / 0,065450 | z von −32,3 bis −22,6 (Down), −28,1 bis −37,8 (Up) | **widerlegt** |

Der Bereich: I(1 TeV) = 0,019, I(10¹⁰ GeV) = 0,090, I(2·10¹⁶ GeV) = 0,123, I(M_Planck) = 0,1337 (y_t fällt von 0,967 auf 0,400).

## Bericht (H177b)
- **Gegenläufig.** Mit wachsender Skala steigt δ_d und fällt δ_u. Für V1 bräuchte Down I = +0,191 (oberhalb der Planck-Skala) und Up I = −0,135
  (unterhalb von M_Z, wo das Verhältnis in dieser Näherung nicht läuft). Ein gemeinsames I gibt es deshalb grundsätzlich nicht, unabhängig vom Bereich.
- **δ_d/δ_u = 2** gilt bei I = 0,0323 (μ ≈ 8 TeV): δ_d = 0,10190, δ_u = 0,05095. Dort ist aber δ_e/δ_d = 2,18, nicht 2. Ein einzelnes Verhältnis, das
  im Bereich von 1,93 bis 2,23 läuft, trifft die 2 zwangsläufig irgendwo; das ist kein Befund.
- **K:** K_d fällt von 0,7478 auf 0,7352, K_u steigt von 0,8876 auf 0,8941. Keiner erreicht ⅔. Die Quarks entfernen sich im Up-Sektor sogar vom Leptonwert.
- **Negative leichteste Wurzel:** δ_d von 0,1522 bis 0,1632, δ_u von 0,0565 bis 0,0527.
  Nachträglich bemerkt: δ_u = 0,0565 bei M_Z liegt 1,9σ neben δ_e/4. Der Partner δ_d = 0,152 liegt aber weit neben δ_e/2. Kein Treffer.

## Lesart
- **Was widerlegt ist.** Die Reihe δ ≈ π/6, π/12, π/24, π/48 aus k374 ist keine exakte Beziehung, auch nicht bei einer anderen Skala. Die grobe Halbierung
  (Faktoren 2,16 / 2,22 / 1,93 bei M_Z) bleibt als Größenordnung stehen, mehr nicht.
- **Was das für die Konfigurationen heißt.** Die beiden Stellgrößen der Quarks (K, δ) sind unter dem Laufen fast starr: δ ändert sich über 17 Größenordnungen
  der Skala um 7 %, K um 1 bis 2 %. Die Quarkwerte bei M_Z sind also keine Zufälle der Skalenwahl; eine Erklärung muss K_d ≈ 0,74, K_u ≈ 0,89 und
  δ_d ≈ 0,10, δ_u ≈ 0,05 als solche liefern.
- **HS-Stufen.** Eine Zuordnung „je Stufe halbe Phase“ trägt in exakter Form nicht. Die Zählung aus k374 (Stellgrößen je Algebra) ist davon nicht berührt.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| k374 | Brannen-Form je Sektor, Skala M_Z | Baumwert CKM = 𝟙; Zählung je Algebra | vier Zahlen (K, δ) der Quarks, Brechung der Mischungen |
| H177 | Ein-Schleifen-Laufen, Top-Dominanz | δ und K der Quarks fast skalenunabhängig | die vier Quarkzahlen bleiben unerklärt; Halbierung keine Regel |

## Grenzen
Eine Schleife, Top-Dominanz, keine Schwellen, nur Standardmodell-Inhalt. Mit zusätzlichen Teilchen (etwa zwei Higgs-Dubletts mit großem tan β) liefe
auch der Down-Sektor stärker; das ist nicht gerechnet. Yukawa-Werte bei M_Z aus k14/k367 übernommen. Kein Vorzeichen gesetzt; kein Guard berührt;
OP3 und OP4 offen. Vergeben: H177, k375. Nächste frei: H178, k376.
